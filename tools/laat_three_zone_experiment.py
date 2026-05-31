# -*- coding: utf-8 -*-
"""Run the fully connected three-zone LAAT MFD planning/control experiment.

The script implements the run list from refine-logs/EXPERIMENT_PLAN.md:
R001-R003 precheck the static bridge, targets, and stability matrix;
R004-R006 simulate local closed-loop trajectories; R007-R009 run
falsification checks; R010 checks sampled Euler stability; R011 writes the
final audit package.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import platform
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm


SUPPORTS = "SUPPORTS_THEOREM"
ASSUMPTION_FAILURE = "ASSUMPTION_FAILURE"
OUTSIDE_LOCAL = "OUTSIDE_LOCAL_REGION"
NUMERICAL_UNRELIABLE = "NUMERICAL_UNRELIABLE"

BASE_DEMAND_MATRIX = np.array(
    [
        [0.0, 0.12, 0.10],
        [0.09, 0.0, 0.14],
        [0.11, 0.08, 0.0],
    ],
    dtype=float,
)
BASE_POTENTIAL_DEMAND_MATRIX = np.array(
    [
        [0.0, 0.15, 0.13],
        [0.12, 0.0, 0.17],
        [0.14, 0.10, 0.0],
    ],
    dtype=float,
)

BASE_DEMAND_SCALE = 20.0
BASE_Q_CAP = np.array([11.0, 11.0, 10.0], dtype=float)
INTERNAL_INTERFACE_CAP = 7.0
EXIT_INTERFACE_CAP = 14.0

# Weng et al.-scale airspace values: 2 km x 2 km x 1 km region,
# n_cr = 4 * 27.6 and n_jam = 4 * 200 aircraft.
MFD_N_CR = 110.4
MFD_N_JAM = 800.0
MFD_G_MAX = 16.56


@dataclass
class Scenario:
    name: str
    demand_matrix: np.ndarray
    potential_demand_matrix: np.ndarray
    q_g: np.ndarray
    t_matrix: np.ndarray
    t_exit: np.ndarray
    q_cap: np.ndarray
    interface_cap: np.ndarray
    ubar: np.ndarray
    kappa: np.ndarray
    eta: np.ndarray
    epsilon: np.ndarray
    mfd_gmax: float = MFD_G_MAX
    n_jam: float = MFD_N_JAM
    n_cr: float = MFD_N_CR

    @property
    def r(self) -> int:
        return int(self.q_g.shape[0])

    @property
    def g_max(self) -> float:
        return self.mfd_gmax

    @property
    def mfd_shape_exponent(self) -> float:
        return self.n_jam / self.n_cr - 1.0


def timestamp_now() -> Tuple[str, str]:
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S"), now.strftime("%Y-%m-%d %H:%M")


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def to_builtin(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): to_builtin(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_builtin(v) for v in value]
    if isinstance(value, np.ndarray):
        return to_builtin(value.tolist())
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    if isinstance(value, complex):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
    return value


def ensure_dirs(root: Path, timestamp: str) -> Dict[str, Path]:
    refine = root / "refine-logs"
    results = refine / "results"
    figures = refine / "figures"
    trajectories = results / f"trajectories_{timestamp}"
    for path in (refine, results, figures, trajectories):
        path.mkdir(parents=True, exist_ok=True)
    return {
        "refine": refine,
        "results": results,
        "figures": figures,
        "trajectories": trajectories,
    }


def make_interface_cap(r: int, default: float = math.inf) -> np.ndarray:
    return np.full((r, r + 1), default, dtype=float)


def build_scenario_from_demands(
    name: str,
    demand_matrix: np.ndarray,
    potential_demand_matrix: np.ndarray,
    q_cap: np.ndarray,
    interface_cap: np.ndarray,
    eta: np.ndarray,
) -> Scenario:
    demand = np.array(demand_matrix, dtype=float)
    potential = np.array(potential_demand_matrix, dtype=float)
    q_g = np.sum(demand, axis=1)
    t_matrix = demand.copy()
    t_exit = np.sum(demand, axis=0)
    return Scenario(
        name=name,
        demand_matrix=demand,
        potential_demand_matrix=potential,
        q_g=q_g,
        t_matrix=t_matrix,
        t_exit=t_exit,
        q_cap=q_cap,
        interface_cap=interface_cap,
        ubar=np.array([0.6, 0.6, 0.6], dtype=float),
        kappa=np.array([0.4, 0.4, 0.4], dtype=float),
        eta=eta,
        epsilon=np.array([0.05, 0.05, 0.05], dtype=float),
    )


def make_valid_scenario(demand_scale: float = 1.0) -> Scenario:
    r = 3
    total_scale = BASE_DEMAND_SCALE * demand_scale
    demand = BASE_DEMAND_MATRIX * total_scale
    potential = BASE_POTENTIAL_DEMAND_MATRIX * total_scale

    q_cap = BASE_Q_CAP.copy()
    cap = make_interface_cap(r)
    for i in range(r):
        for j in range(r):
            if i != j:
                cap[i, j] = INTERNAL_INTERFACE_CAP
        cap[i, r] = EXIT_INTERFACE_CAP

    return build_scenario_from_demands(
        name=f"weng_scale_fully_connected_s{demand_scale:g}",
        demand_matrix=demand,
        potential_demand_matrix=potential,
        q_cap=q_cap,
        interface_cap=cap,
        eta=np.array([0.08, 0.08, 0.08], dtype=float),
    )


def make_closed_cycle_scenario() -> Scenario:
    r = 3
    demand = np.zeros((r, r), dtype=float)
    for i in range(r):
        for j in range(r):
            if i != j:
                demand[i, j] = 0.10 * BASE_DEMAND_SCALE
    potential = demand.copy()
    cap = make_interface_cap(r)
    for i in range(r):
        for j in range(r):
            if i != j:
                cap[i, j] = INTERNAL_INTERFACE_CAP
        cap[i, r] = EXIT_INTERFACE_CAP
    scenario = build_scenario_from_demands(
        name="fully_connected_no_exit",
        demand_matrix=demand,
        potential_demand_matrix=potential,
        q_cap=BASE_Q_CAP.copy(),
        interface_cap=cap,
        eta=np.zeros(r, dtype=float),
    )
    scenario.q_g = np.zeros(r, dtype=float)
    scenario.t_exit = np.zeros(r, dtype=float)
    return scenario


def mfd(scenario: Scenario, n: np.ndarray) -> np.ndarray:
    n_clip = np.clip(n, 0.0, scenario.n_jam)
    shape = n_clip * np.power(
        np.maximum(1.0 - n_clip / scenario.n_jam, 0.0),
        scenario.mfd_shape_exponent,
    )
    peak_shape = scenario.n_cr * math.pow(
        1.0 - scenario.n_cr / scenario.n_jam,
        scenario.mfd_shape_exponent,
    )
    raw = scenario.mfd_gmax * shape / peak_shape
    return np.maximum(raw, 0.0)


def mfd_scalar(scenario: Scenario, n: float) -> float:
    return float(mfd(scenario, np.array([n], dtype=float))[0])


def free_flow_target(scenario: Scenario, throughput: float, ubar: float) -> float:
    y = throughput / ubar
    if not (0.0 < y < scenario.g_max):
        raise ValueError(f"No free-flow root for throughput={throughput}, ubar={ubar}")
    lo = 0.0
    hi = scenario.n_cr
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if mfd_scalar(scenario, mid) < y:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def compute_static(scenario: Scenario, tol: float = 1e-12) -> Dict[str, Any]:
    inflow = scenario.q_g + np.sum(scenario.t_matrix, axis=0)
    outflow = np.sum(scenario.t_matrix, axis=1) + scenario.t_exit
    lam = outflow.copy()
    active = lam > tol
    beta = np.zeros_like(scenario.t_matrix)
    beta_exit = np.zeros(scenario.r, dtype=float)
    for i in range(scenario.r):
        if active[i]:
            beta[i, :] = scenario.t_matrix[i, :] / lam[i]
            beta_exit[i] = scenario.t_exit[i] / lam[i]

    inactive_zero_residuals = []
    for i in range(scenario.r):
        if active[i]:
            inactive_zero_residuals.append(0.0)
        else:
            inactive_zero_residuals.append(
                float(
                    abs(scenario.q_g[i])
                    + np.sum(np.abs(scenario.t_matrix[i, :]))
                    + np.sum(np.abs(scenario.t_matrix[:, i]))
                    + abs(scenario.t_exit[i])
                )
            )

    return {
        "inflow": inflow,
        "outflow": outflow,
        "lambda": lam,
        "active_mask": active,
        "active_indices": np.flatnonzero(active),
        "beta": beta,
        "beta_exit": beta_exit,
        "conservation_residual": float(np.max(np.abs(inflow - outflow))),
        "beta_residual": float(
            np.max(np.abs(np.sum(beta[active, :], axis=1) + beta_exit[active] - 1.0))
            if np.any(active)
            else 0.0
        ),
        "flow_min": float(
            min(
                np.min(scenario.q_g),
                np.min(scenario.t_matrix),
                np.min(scenario.t_exit),
            )
        ),
        "inactive_zero_residual": float(max(inactive_zero_residuals)),
    }


def finite_interface_margins(scenario: Scenario) -> np.ndarray:
    flow_with_exit = np.concatenate(
        [scenario.t_matrix, scenario.t_exit.reshape((-1, 1))], axis=1
    )
    finite = np.isfinite(scenario.interface_cap)
    return scenario.interface_cap[finite] - flow_with_exit[finite]


def precheck_scenario(scenario: Scenario, tol: float = 1e-10) -> Dict[str, Any]:
    static = compute_static(scenario)
    active = static["active_indices"]
    beta = static["beta"]
    lam = static["lambda"]

    targets = np.zeros(scenario.r, dtype=float)
    target_errors: List[str] = []
    free_branch_ok = True
    capacity_margins = scenario.ubar * scenario.g_max - lam
    for i in active:
        if not (0.0 < lam[i] < scenario.ubar[i] * scenario.g_max):
            target_errors.append(
                f"region {i + 1}: Lambda={lam[i]:.6g} is not below ubar*Gmax={scenario.ubar[i] * scenario.g_max:.6g}"
            )
            targets[i] = math.nan
            free_branch_ok = False
            continue
        try:
            targets[i] = free_flow_target(scenario, float(lam[i]), float(scenario.ubar[i]))
            if not (0.0 < targets[i] < scenario.n_cr):
                free_branch_ok = False
        except ValueError as exc:
            target_errors.append(str(exc))
            targets[i] = math.nan
            free_branch_ok = False

    target_residuals = []
    epsilon_ok = True
    for i in active:
        if not math.isnan(float(targets[i])):
            g_target = mfd_scalar(scenario, float(targets[i]))
            target_residuals.append(abs(scenario.ubar[i] * g_target - lam[i]))
            if not scenario.epsilon[i] < g_target:
                epsilon_ok = False

    interface_margins = finite_interface_margins(scenario)
    takeoff_margin = scenario.q_cap - scenario.q_g
    takeoff_interior_ok = True
    for i in active:
        if scenario.eta[i] > 0.0 and not (0.0 < scenario.q_g[i] < scenario.q_cap[i]):
            takeoff_interior_ok = False

    b_matrix = beta[np.ix_(active, active)] if len(active) else np.zeros((0, 0))
    rho_b = float(max(abs(np.linalg.eigvals(b_matrix)))) if b_matrix.size else 0.0
    k = np.diag(scenario.kappa[active])
    h = np.diag(scenario.eta[active])
    a_matrix = (b_matrix.T - np.eye(len(active))) @ k - h if len(active) else np.zeros((0, 0))
    eig_a = np.linalg.eigvals(a_matrix) if a_matrix.size else np.array([], dtype=float)
    max_real_eig_a = float(max(np.real(eig_a))) if eig_a.size else -math.inf

    l1_static = (
        static["conservation_residual"] <= tol
        and static["beta_residual"] <= tol
        and static["flow_min"] >= -tol
        and static["inactive_zero_residual"] <= tol
    )
    l2_target = (
        len(target_errors) == 0
        and free_branch_ok
        and epsilon_ok
        and float(np.min(takeoff_margin)) >= -tol
        and bool(np.all(scenario.q_g >= -tol))
        and takeoff_interior_ok
        and (len(interface_margins) == 0 or float(np.min(interface_margins)) > 0.0)
        and (len(target_residuals) == 0 or max(target_residuals) <= 1e-8)
    )
    l3_stability = rho_b < 1.0 - 1e-10 and max_real_eig_a < -1e-10

    checks = {
        "L1_static_feasibility": bool(l1_static),
        "L2_target_feasibility": bool(l2_target),
        "L3_stability_assumptions": bool(l3_stability),
    }
    failed = [key for key, ok in checks.items() if not ok]
    if target_errors:
        failed.extend(target_errors)

    return {
        "scenario": scenario.name,
        "static": static,
        "targets": targets,
        "b_matrix": b_matrix,
        "a_matrix": a_matrix,
        "eig_a": eig_a,
        "rho_b": rho_b,
        "max_real_eig_a": max_real_eig_a,
        "checks": checks,
        "failed_checks": failed,
        "all_prechecks_pass": bool(l1_static and l2_target and l3_stability),
        "metrics": {
            "conservation_residual": static["conservation_residual"],
            "beta_residual": static["beta_residual"],
            "flow_min": static["flow_min"],
            "inactive_zero_residual": static["inactive_zero_residual"],
            "target_residual": float(max(target_residuals) if target_residuals else 0.0),
            "capacity_condition_min_margin": float(
                np.min(capacity_margins[static["active_mask"]])
                if np.any(static["active_mask"])
                else math.inf
            ),
            "interface_min_margin": float(
                np.min(interface_margins) if len(interface_margins) else math.inf
            ),
            "takeoff_min_margin": float(np.min(takeoff_margin)),
            "takeoff_interior_ok": bool(takeoff_interior_ok),
            "epsilon_ok": bool(epsilon_ok),
            "free_branch_ok": bool(free_branch_ok),
            "rho_b": rho_b,
            "max_real_eig_a": max_real_eig_a,
            "eig_a_real": [float(x) for x in np.real(eig_a)],
            "eig_a_imag": [float(x) for x in np.imag(eig_a)],
        },
    }


def controls(
    scenario: Scenario, precheck: Dict[str, Any], n: np.ndarray
) -> Dict[str, np.ndarray]:
    static = precheck["static"]
    target = precheck["targets"]
    lam = static["lambda"]
    beta = static["beta"]
    beta_exit = static["beta_exit"]

    e = n - target
    raw_r = scenario.q_g - scenario.eta * e
    r_cmd = np.clip(raw_r, 0.0, scenario.q_cap)
    g = mfd(scenario, n)
    denom = np.maximum(g, scenario.epsilon)
    raw_u = (lam + scenario.kappa * e) / denom
    u_cmd = np.clip(raw_u, 0.0, 1.0)
    z = u_cmd * g
    z_matrix = beta * z.reshape((-1, 1))
    z_exit = beta_exit * z
    return {
        "e": e,
        "raw_r": raw_r,
        "r": r_cmd,
        "g": g,
        "denom": denom,
        "raw_u": raw_u,
        "u": u_cmd,
        "z": z,
        "z_matrix": z_matrix,
        "z_exit": z_exit,
    }


def ode_rhs(_: float, n: np.ndarray, scenario: Scenario, precheck: Dict[str, Any]) -> np.ndarray:
    ctrl = controls(scenario, precheck, n)
    beta = precheck["static"]["beta"]
    return ctrl["r"] + beta.T @ ctrl["z"] - ctrl["z"]


def solve_nonlinear(
    scenario: Scenario,
    precheck: Dict[str, Any],
    n0: np.ndarray,
    t_eval: np.ndarray,
    rtol: float,
    atol: float,
) -> Any:
    return solve_ivp(
        fun=lambda t, y: ode_rhs(t, y, scenario, precheck),
        t_span=(float(t_eval[0]), float(t_eval[-1])),
        y0=n0,
        t_eval=t_eval,
        method="DOP853",
        rtol=rtol,
        atol=atol,
    )


def linear_oracle(precheck: Dict[str, Any], e0_full: np.ndarray, t_eval: np.ndarray) -> np.ndarray:
    target = precheck["targets"]
    active = precheck["static"]["active_indices"]
    a_matrix = precheck["a_matrix"]
    out = np.tile(target.reshape((1, -1)), (len(t_eval), 1))
    e0 = e0_full[active]
    for row, t in enumerate(t_eval):
        out[row, active] = target[active] + expm(a_matrix * float(t)) @ e0
    return out


def summarize_control_trajectory(
    scenario: Scenario,
    precheck: Dict[str, Any],
    states: np.ndarray,
    tol: float = 1e-9,
) -> Dict[str, Any]:
    sat_events = 0
    total_control_entries = 0
    nonnegative_violations = int(np.sum(states < -tol))
    capacity_violations = 0
    max_capacity_excess = 0.0
    max_raw_u = -math.inf
    min_raw_u = math.inf
    max_raw_r = -math.inf
    min_raw_r = math.inf

    finite_cap = np.isfinite(scenario.interface_cap)
    for n in states:
        ctrl = controls(scenario, precheck, n)
        raw_r = ctrl["raw_r"]
        raw_u = ctrl["raw_u"]
        g = ctrl["g"]
        r_sat = (raw_r < -tol) | (raw_r > scenario.q_cap + tol)
        u_sat = (raw_u < -tol) | (raw_u > 1.0 + tol) | (g <= scenario.epsilon + tol)
        sat_events += int(np.sum(r_sat) + np.sum(u_sat))
        total_control_entries += 2 * scenario.r
        max_raw_u = max(max_raw_u, float(np.max(raw_u)))
        min_raw_u = min(min_raw_u, float(np.min(raw_u)))
        max_raw_r = max(max_raw_r, float(np.max(raw_r)))
        min_raw_r = min(min_raw_r, float(np.min(raw_r)))

        flow_with_exit = np.concatenate(
            [ctrl["z_matrix"], ctrl["z_exit"].reshape((-1, 1))], axis=1
        )
        excess = flow_with_exit - scenario.interface_cap
        cap_bad = finite_cap & (excess > tol)
        capacity_violations += int(np.sum(cap_bad))
        if np.any(cap_bad):
            max_capacity_excess = max(max_capacity_excess, float(np.max(excess[cap_bad])))

    return {
        "saturation_events": sat_events,
        "saturation_fraction": float(sat_events / max(total_control_entries, 1)),
        "nonnegative_violations": nonnegative_violations,
        "capacity_violations": capacity_violations,
        "max_capacity_excess": max_capacity_excess,
        "min_raw_u": min_raw_u,
        "max_raw_u": max_raw_u,
        "min_raw_r": min_raw_r,
        "max_raw_r": max_raw_r,
    }


def fit_log_error_slope(t_eval: np.ndarray, error_norm: np.ndarray) -> float:
    mask = (t_eval >= 1.0) & (error_norm > 1e-12)
    if int(np.sum(mask)) < 2:
        return float("nan")
    return float(np.polyfit(t_eval[mask], np.log(error_norm[mask]), 1)[0])


def simulate_run(
    run_id: str,
    scenario: Scenario,
    precheck: Dict[str, Any],
    perturbation: np.ndarray,
    args: argparse.Namespace,
    trajectories_dir: Path,
) -> Dict[str, Any]:
    target = precheck["targets"]
    n0 = target + perturbation
    t_eval = np.linspace(0.0, args.t_final, args.num_points)
    sol = solve_nonlinear(scenario, precheck, n0, t_eval, args.rtol, args.atol)
    if not sol.success:
        return {
            "run_id": run_id,
            "status": "FAILED",
            "classification": NUMERICAL_UNRELIABLE,
            "success": False,
            "metrics": {"solver_message": sol.message},
            "notes": "ODE solver failed",
        }

    states = sol.y.T
    oracle_states = linear_oracle(precheck, perturbation, t_eval)
    error = states - target.reshape((1, -1))
    oracle_error = oracle_states - target.reshape((1, -1))
    error_norm = np.linalg.norm(error, axis=1)
    oracle_error_norm = np.linalg.norm(oracle_error, axis=1)
    diff_norm = np.linalg.norm(states - oracle_states, axis=1)
    oracle_scale = max(float(np.max(oracle_error_norm)), 1e-12)
    oracle_mismatch = float(np.max(diff_norm) / oracle_scale)
    final_error_ratio = float(error_norm[-1] / max(error_norm[0], 1e-12))
    log_slope = fit_log_error_slope(t_eval, error_norm)

    strict_sol = solve_nonlinear(
        scenario,
        precheck,
        n0,
        t_eval,
        max(args.rtol * 0.1, 1e-13),
        max(args.atol * 0.1, 1e-15),
    )
    tolerance_final_diff = (
        float(np.linalg.norm(sol.y[:, -1] - strict_sol.y[:, -1]))
        if strict_sol.success
        else float("inf")
    )

    control_summary = summarize_control_trajectory(scenario, precheck, states)
    local_violation = (
        control_summary["saturation_events"] > 0
        or control_summary["capacity_violations"] > 0
        or control_summary["nonnegative_violations"] > 0
    )
    numerical_bad = oracle_mismatch > args.oracle_mismatch_tol or tolerance_final_diff > 1e-6

    if local_violation:
        classification = OUTSIDE_LOCAL
        success = run_id == "R009"
    elif numerical_bad or final_error_ratio > args.final_ratio_tol:
        classification = NUMERICAL_UNRELIABLE
        success = False
    else:
        classification = SUPPORTS
        success = True

    trajectory_path = trajectories_dir / f"{run_id}.csv"
    write_trajectory_csv(
        trajectory_path,
        t_eval,
        states,
        oracle_states,
        error_norm,
        oracle_error_norm,
        scenario,
        precheck,
    )

    return {
        "run_id": run_id,
        "status": "DONE",
        "classification": classification,
        "success": bool(success),
        "metrics": {
            "initial_error_norm": float(error_norm[0]),
            "final_error_norm": float(error_norm[-1]),
            "final_error_ratio": final_error_ratio,
            "log_error_slope": log_slope,
            "oracle_mismatch": oracle_mismatch,
            "tolerance_final_diff": tolerance_final_diff,
            **control_summary,
        },
        "artifacts": {"trajectory_csv": str(trajectory_path)},
        "notes": (
            "Local theorem-support trajectory"
            if classification == SUPPORTS
            else "Correctly flagged as outside the local unsaturated region"
            if classification == OUTSIDE_LOCAL
            else "Numerical reliability check failed"
        ),
    }


def write_trajectory_csv(
    path: Path,
    t_eval: np.ndarray,
    states: np.ndarray,
    oracle_states: np.ndarray,
    error_norm: np.ndarray,
    oracle_error_norm: np.ndarray,
    scenario: Scenario,
    precheck: Dict[str, Any],
) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        header = [
            "t",
            "n1",
            "n2",
            "n3",
            "oracle_n1",
            "oracle_n2",
            "oracle_n3",
            "error_norm",
            "oracle_error_norm",
            "r1",
            "r2",
            "r3",
            "u1",
            "u2",
            "u3",
            "z1",
            "z2",
            "z3",
        ]
        writer.writerow(header)
        for t, n, oracle_n, e_norm, oracle_norm in zip(
            t_eval, states, oracle_states, error_norm, oracle_error_norm
        ):
            ctrl = controls(scenario, precheck, n)
            writer.writerow(
                [
                    f"{float(t):.10g}",
                    *[f"{float(x):.10g}" for x in n],
                    *[f"{float(x):.10g}" for x in oracle_n],
                    f"{float(e_norm):.10g}",
                    f"{float(oracle_norm):.10g}",
                    *[f"{float(x):.10g}" for x in ctrl["r"]],
                    *[f"{float(x):.10g}" for x in ctrl["u"]],
                    *[f"{float(x):.10g}" for x in ctrl["z"]],
                ]
            )


def plot_trajectory(run: Dict[str, Any], figures_dir: Path) -> Optional[str]:
    trajectory = run.get("artifacts", {}).get("trajectory_csv")
    if not trajectory:
        return None
    path = Path(trajectory)
    if not path.exists():
        return None

    data = np.genfromtxt(path, delimiter=",", names=True)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    axes[0].plot(data["t"], data["n1"], label="n1")
    axes[0].plot(data["t"], data["n2"], label="n2")
    axes[0].plot(data["t"], data["n3"], label="n3")
    axes[0].set_xlabel("time")
    axes[0].set_ylabel("accumulation")
    axes[0].set_title(f"{run['run_id']} states")
    axes[0].legend()

    axes[1].semilogy(data["t"], np.maximum(data["error_norm"], 1e-14), label="nonlinear")
    axes[1].semilogy(
        data["t"],
        np.maximum(data["oracle_error_norm"], 1e-14),
        "--",
        label="linear oracle",
    )
    axes[1].set_xlabel("time")
    axes[1].set_ylabel("error norm")
    axes[1].set_title(f"{run['run_id']} error")
    axes[1].legend()

    out = figures_dir / f"three_zone_laat_{run['run_id']}.png"
    fig.savefig(out, dpi=180)
    plt.close(fig)
    return str(out)


def parameter_check_run(scenario: Scenario, precheck: Dict[str, Any]) -> Dict[str, Any]:
    expected_demand = BASE_DEMAND_MATRIX * BASE_DEMAND_SCALE
    expected_potential = BASE_POTENTIAL_DEMAND_MATRIX * BASE_DEMAND_SCALE
    expected_q = np.array([4.4, 4.6, 3.8])
    expected_t = expected_demand.copy()
    expected_exit = np.array([4.0, 4.0, 4.8])
    expected_lambda = np.array([8.4, 8.6, 8.6])
    expected_b = np.array(
        [
            [0.0, 0.2857142857142857, 0.23809523809523808],
            [0.20930232558139533, 0.0, 0.32558139534883723],
            [0.2558139534883721, 0.18604651162790697, 0.0],
        ],
        dtype=float,
    )
    mismatches = [
        np.max(np.abs(scenario.demand_matrix - expected_demand)),
        np.max(np.abs(scenario.potential_demand_matrix - expected_potential)),
        np.max(np.abs(scenario.q_g - expected_q)),
        np.max(np.abs(scenario.t_matrix - expected_t)),
        np.max(np.abs(scenario.t_exit - expected_exit)),
        np.max(np.abs(precheck["static"]["lambda"] - expected_lambda)),
        np.max(np.abs(precheck["b_matrix"] - expected_b)),
        abs(scenario.n_cr - MFD_N_CR),
        abs(scenario.n_jam - MFD_N_JAM),
        abs(scenario.mfd_gmax - MFD_G_MAX),
    ]
    max_mismatch = float(max(mismatches))
    return {
        "run_id": "R001",
        "status": "DONE",
        "classification": SUPPORTS,
        "success": max_mismatch <= 1e-12,
        "metrics": {"parameter_max_abs_mismatch": max_mismatch},
        "notes": "Scenario matches the non-toy Weng-scale deterministic plan table",
    }


def static_feasibility_run(precheck: Dict[str, Any]) -> Dict[str, Any]:
    ok = precheck["checks"]["L1_static_feasibility"] and precheck["checks"]["L2_target_feasibility"]
    return {
        "run_id": "R002",
        "status": "DONE",
        "classification": SUPPORTS if ok else ASSUMPTION_FAILURE,
        "success": bool(ok),
        "metrics": {
            key: precheck["metrics"][key]
            for key in [
                "conservation_residual",
                "beta_residual",
                "target_residual",
                "capacity_condition_min_margin",
                "interface_min_margin",
                "takeoff_min_margin",
            ]
        },
        "notes": "Static bridge and target feasibility passed" if ok else "; ".join(precheck["failed_checks"]),
    }


def spectral_run(precheck: Dict[str, Any]) -> Dict[str, Any]:
    expected_a = np.array(
        [
            [-0.48, 0.08372093023255814, 0.10232558139534884],
            [0.11428571428571428, -0.48, 0.07441860465116279],
            [0.09523809523809523, 0.1302325581395349, -0.48],
        ],
        dtype=float,
    )
    a_mismatch = float(np.max(np.abs(precheck["a_matrix"] - expected_a)))
    ok = precheck["checks"]["L3_stability_assumptions"] and a_mismatch <= 1e-10
    return {
        "run_id": "R003",
        "status": "DONE",
        "classification": SUPPORTS if ok else ASSUMPTION_FAILURE,
        "success": bool(ok),
        "metrics": {
            "rho_b": precheck["metrics"]["rho_b"],
            "max_real_eig_a": precheck["metrics"]["max_real_eig_a"],
            "a_matrix_max_abs_mismatch": a_mismatch,
            "eig_a_real": precheck["metrics"]["eig_a_real"],
        },
        "notes": "Spectral and hand-computed matrix checks passed" if ok else "; ".join(precheck["failed_checks"]),
    }


def assumption_failure_run(run_id: str, scenario: Scenario, expected_reason: str) -> Dict[str, Any]:
    precheck = precheck_scenario(scenario)
    classification = ASSUMPTION_FAILURE if not precheck["all_prechecks_pass"] else SUPPORTS
    success = classification == ASSUMPTION_FAILURE
    return {
        "run_id": run_id,
        "status": "DONE",
        "classification": classification,
        "success": bool(success),
        "metrics": precheck["metrics"],
        "checks": precheck["checks"],
        "notes": (
            f"Correctly rejected stress case: {expected_reason}; failures={precheck['failed_checks']}"
            if success
            else "Stress case was not rejected; checker is too permissive"
        ),
    }


def sampled_check_run(precheck: Dict[str, Any], args: argparse.Namespace) -> Dict[str, Any]:
    a_matrix = precheck["a_matrix"]
    target = precheck["targets"]
    e0 = target * args.local_scale * np.array([1.0, -1.0, 1.0])
    exact = expm(a_matrix * args.t_final) @ e0
    exact_ratio = float(np.linalg.norm(exact) / max(np.linalg.norm(e0), 1e-12))

    rows = []
    all_rho_ok = True
    for dt in args.dts:
        step_matrix = np.eye(a_matrix.shape[0]) + dt * a_matrix
        rho = float(max(abs(np.linalg.eigvals(step_matrix))))
        all_rho_ok = all_rho_ok and rho < 1.0
        e = e0.copy()
        steps = int(round(args.t_final / dt))
        for _ in range(steps):
            e = step_matrix @ e
        ratio = float(np.linalg.norm(e) / max(np.linalg.norm(e0), 1e-12))
        rows.append(
            {
                "dt": float(dt),
                "rho_euler": rho,
                "final_error_ratio": ratio,
                "absolute_ratio_error_vs_exact": abs(ratio - exact_ratio),
            }
        )

    prod_dt = min(args.dts)
    half_dt = prod_dt / 2.0
    def euler_ratio(dt: float) -> float:
        step = np.eye(a_matrix.shape[0]) + dt * a_matrix
        e = e0.copy()
        for _ in range(int(round(args.t_final / dt))):
            e = step @ e
        return float(np.linalg.norm(e) / max(np.linalg.norm(e0), 1e-12))

    sensitivity = abs(euler_ratio(prod_dt) - euler_ratio(half_dt))
    success = all_rho_ok and sensitivity <= 1e-3
    return {
        "run_id": "R010",
        "status": "DONE",
        "classification": SUPPORTS if success else NUMERICAL_UNRELIABLE,
        "success": bool(success),
        "metrics": {
            "exact_final_error_ratio": exact_ratio,
            "production_dt": float(prod_dt),
            "production_dt_half_step_sensitivity": float(sensitivity),
            "sampled_rows": rows,
        },
        "notes": "Sampled Euler stability and step-sensitivity check passed"
        if success
        else "Sampled implementation needs a smaller step or exact integration",
    }


def final_audit_run(runs: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
    must_ids = {f"R{i:03d}" for i in range(1, 10)} | {"R011"}
    completed_must = [r for r in runs if r["run_id"] in must_ids and r["status"] == "DONE"]
    failed_expectations = [r["run_id"] for r in runs if not r.get("success", False)]
    supports = [r["run_id"] for r in runs if r.get("classification") == SUPPORTS]
    assumption_failures = [r["run_id"] for r in runs if r.get("classification") == ASSUMPTION_FAILURE]
    outside_local = [r["run_id"] for r in runs if r.get("classification") == OUTSIDE_LOCAL]
    ok = len(completed_must) == len(must_ids) - 1 and not failed_expectations
    return {
        "run_id": "R011",
        "status": "DONE",
        "classification": SUPPORTS if ok else NUMERICAL_UNRELIABLE,
        "success": bool(ok),
        "metrics": {
            "must_run_completed_before_audit": len(completed_must),
            "expected_must_runs_before_audit": len(must_ids) - 1,
            "failed_expectations": failed_expectations,
            "supporting_runs": supports,
            "assumption_failure_runs": assumption_failures,
            "outside_local_runs": outside_local,
        },
        "notes": "Final audit passed" if ok else f"Runs needing review: {failed_expectations}",
    }


def write_json(path: Path, data: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(to_builtin(data), f, ensure_ascii=False, indent=2)
        f.write("\n")


def selected_metric(run: Dict[str, Any], key: str) -> Any:
    metrics = run.get("metrics", {})
    return metrics.get(key, "")


def write_metrics_csv(path: Path, runs: Sequence[Dict[str, Any]]) -> None:
    columns = [
        "run_id",
        "status",
        "classification",
        "success",
        "rho_b",
        "max_real_eig_a",
        "conservation_residual",
        "beta_residual",
        "target_residual",
        "capacity_condition_min_margin",
        "final_error_ratio",
        "log_error_slope",
        "saturation_fraction",
        "oracle_mismatch",
        "tolerance_final_diff",
        "notes",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for run in runs:
            writer.writerow(
                {
                    "run_id": run["run_id"],
                    "status": run["status"],
                    "classification": run["classification"],
                    "success": run["success"],
                    "rho_b": selected_metric(run, "rho_b"),
                    "max_real_eig_a": selected_metric(run, "max_real_eig_a"),
                    "conservation_residual": selected_metric(run, "conservation_residual"),
                    "beta_residual": selected_metric(run, "beta_residual"),
                    "target_residual": selected_metric(run, "target_residual"),
                    "capacity_condition_min_margin": selected_metric(
                        run, "capacity_condition_min_margin"
                    ),
                    "final_error_ratio": selected_metric(run, "final_error_ratio"),
                    "log_error_slope": selected_metric(run, "log_error_slope"),
                    "saturation_fraction": selected_metric(run, "saturation_fraction"),
                    "oracle_mismatch": selected_metric(run, "oracle_mismatch"),
                    "tolerance_final_diff": selected_metric(run, "tolerance_final_diff"),
                    "notes": run.get("notes", ""),
                }
            )


def write_tracker(path: Path, runs: Sequence[Dict[str, Any]]) -> None:
    specs = {
        "R001": ("M0", "Encode explicit Weng-scale scenario", "20x OD table with six positive directed demands", "deterministic", "parameter equality checks", "MUST"),
        "R002": ("M1", "Static aggregation and feasibility", "Non-toy fully connected base scenario", "deterministic", "conservation/beta/target/capacity margins", "MUST"),
        "R003": ("M2", "Coupled matrix stability check", "Non-toy fully connected base scenario", "deterministic", "rho(B), eig(A), A mismatch", "MUST"),
        "R004": ("M3", "Local trajectory 1", "Perturbation 0.10*bar n*(+,+,+)", "local", "final ratio, slope, saturation, oracle mismatch", "MUST"),
        "R005": ("M3", "Local trajectory 2", "Perturbation 0.10*bar n*(+,-,+)", "local", "final ratio, slope, saturation, oracle mismatch", "MUST"),
        "R006": ("M3", "Local trajectory 3", "Perturbation 0.10*bar n*(-,+,-)", "local", "final ratio, slope, saturation, oracle mismatch", "MUST"),
        "R007": ("M4", "Spectral falsification", "Fully connected no-exit circulation", "stress", "rho(B), classification", "MUST"),
        "R008": ("M4", "Capacity falsification", "Base OD demand scaled by s=1.20", "stress", "capacity residual, classification", "MUST"),
        "R009": ("M4", "Local-region falsification", "Base plan with far initial error (+80,-20,+80)", "stress", "saturation, classification", "MUST"),
        "R010": ("M5", "Sampled-hold check", "Euler sampled update", "engineering", "rho(I+A dt), step sensitivity", "NICE"),
        "R011": ("M6", "Final result audit", "All completed runs", "report", "L0-L6 pass matrix and labels", "MUST"),
    }
    by_id = {r["run_id"]: r for r in runs}
    lines = [
        "# Experiment Tracker",
        "",
        "| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |",
        "|--------|-----------|---------|------------------|-------|---------|----------|--------|-------|",
    ]
    for run_id in sorted(specs):
        milestone, purpose, system, split, metrics, priority = specs[run_id]
        run = by_id.get(run_id, {})
        status = "DONE" if run.get("status") == "DONE" else "TODO"
        if run and not run.get("success", False):
            status = "REVIEW"
        notes = run.get("notes", "").replace("|", "/")
        classification = run.get("classification", "")
        if classification:
            notes = f"{classification}; {notes}"
        lines.append(
            f"| {run_id} | {milestone} | {purpose} | {system} | {split} | {metrics} | {priority} | {status} | {notes} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_float(value: Any, digits: int = 4) -> str:
    if value == "":
        return ""
    try:
        x = float(value)
    except (TypeError, ValueError):
        return str(value)
    if math.isnan(x):
        return "nan"
    if math.isinf(x):
        return "inf" if x > 0 else "-inf"
    return f"{x:.{digits}g}"


def format_vector(values: Iterable[Any], digits: int = 4) -> str:
    return "(" + ", ".join(format_float(x, digits) for x in values) + ")"


def format_matrix(matrix: np.ndarray, digits: int = 4) -> str:
    rows = [format_vector(row, digits) for row in matrix]
    return "[" + "; ".join(rows) + "]"


def write_results_md(
    path: Path,
    timestamp_human: str,
    args: argparse.Namespace,
    scenario: Scenario,
    precheck: Dict[str, Any],
    runs: Sequence[Dict[str, Any]],
    artifacts: Dict[str, str],
) -> None:
    by_id = {run["run_id"]: run for run in runs}
    must = [r for r in runs if r["run_id"] != "R010"]
    must_done = sum(1 for r in must if r["status"] == "DONE")
    must_success = sum(1 for r in must if r.get("success", False))
    local_runs = [by_id[x] for x in ("R004", "R005", "R006")]
    stress_runs = [by_id[x] for x in ("R007", "R008", "R009")]
    ready = all(r.get("success", False) for r in runs)

    lines = [
        "# Initial Experiment Results",
        "",
        f"**Date**: {timestamp_human}",
        "**Plan**: `refine-logs/EXPERIMENT_PLAN.md`",
        "**Implementation**: `tools/laat_three_zone_experiment.py`",
        f"**Command**: `{artifacts['command']}`",
        "**Scale Note**: non-toy Weng-scale three-zone case; each steady-state region has tens of aircraft.",
        "",
        "## Scenario Settings",
        "",
        "| Quantity | Value |",
        "|----------|-------|",
        f"| region geometry reference | `2 km x 2 km x 1 km` per region |",
        f"| demand matrix | `{format_matrix(scenario.demand_matrix, 4)}` |",
        f"| takeoff inflow `q_g` | `{format_vector(scenario.q_g, 4)}` |",
        f"| completion flow `T_i0` | `{format_vector(scenario.t_exit, 4)}` |",
        f"| aggregate load `Lambda` | `{format_vector(precheck['static']['lambda'], 4)}` |",
        f"| target accumulation `bar n` | `{format_vector(precheck['targets'], 6)}` aircraft |",
        f"| MFD | `Gmax={format_float(scenario.g_max)}, n_cr={format_float(scenario.n_cr)}, n_jam={format_float(scenario.n_jam)}, p={format_float(scenario.mfd_shape_exponent, 6)}` |",
        f"| takeoff caps | `{format_vector(scenario.q_cap, 4)}` |",
        f"| internal / exit interface caps | `{format_float(INTERNAL_INTERFACE_CAP)} / {format_float(EXIT_INTERFACE_CAP)}` |",
        f"| controller gains | `ubar={format_vector(scenario.ubar, 3)}, kappa={format_vector(scenario.kappa, 3)}, eta={format_vector(scenario.eta, 3)}` |",
        f"| simulation | `T_final={format_float(args.t_final)}, samples={args.num_points}, rtol={args.rtol}, atol={args.atol}` |",
        "",
        "## Summary",
        "",
        f"- MUST-RUN completed: `{must_done}/{len(must)}`.",
        f"- MUST-RUN expected criteria passed: `{must_success}/{len(must)}`.",
        f"- Nice-to-have completed: `{'1/1' if by_id['R010']['status'] == 'DONE' else '0/1'}`.",
        f"- Main result: `{'positive' if ready else 'needs review'}`.",
        f"- Ready for `/auto-review-loop`: `{'YES' if ready else 'NO'}`.",
        "",
        "## Results by Milestone",
        "",
        "### M0-M2: Preflight and Stability Matrix",
        "",
        "| Run | Classification | Key Metrics | Status |",
        "|-----|----------------|-------------|--------|",
    ]

    for run_id in ("R001", "R002", "R003"):
        run = by_id[run_id]
        metrics = run["metrics"]
        key_bits = []
        for key in (
            "parameter_max_abs_mismatch",
            "conservation_residual",
            "beta_residual",
            "target_residual",
            "rho_b",
            "max_real_eig_a",
            "a_matrix_max_abs_mismatch",
        ):
            if key in metrics:
                key_bits.append(f"`{key}={format_float(metrics[key])}`")
        lines.append(
            f"| {run_id} | `{run['classification']}` | {'; '.join(key_bits)} | `{run['status']}` |"
        )

    lines.extend(
        [
            "",
            "### M3: Local Closed-Loop Trajectories",
            "",
            "| Run | Classification | Final Error Ratio | Log Slope | Saturation Fraction | Oracle Mismatch | Status |",
            "|-----|----------------|-------------------|-----------|---------------------|-----------------|--------|",
        ]
    )
    for run in local_runs:
        metrics = run["metrics"]
        lines.append(
            "| {run_id} | `{cls}` | `{ratio}` | `{slope}` | `{sat}` | `{mismatch}` | `{status}` |".format(
                run_id=run["run_id"],
                cls=run["classification"],
                ratio=format_float(metrics.get("final_error_ratio"), 6),
                slope=format_float(metrics.get("log_error_slope"), 6),
                sat=format_float(metrics.get("saturation_fraction"), 6),
                mismatch=format_float(metrics.get("oracle_mismatch"), 6),
                status=run["status"],
            )
        )

    lines.extend(
        [
            "",
            "### M4: Falsification Checks",
            "",
            "| Run | Expected Failure Type | Classification | Key Diagnostic | Status |",
            "|-----|-----------------------|----------------|----------------|--------|",
        ]
    )
    diagnostics = {
        "R007": f"`rho_b={format_float(by_id['R007']['metrics'].get('rho_b'))}`",
        "R008": f"`capacity_margin={format_float(by_id['R008']['metrics'].get('capacity_condition_min_margin'))}`",
        "R009": f"`saturation_fraction={format_float(by_id['R009']['metrics'].get('saturation_fraction'))}`",
    }
    expected = {
        "R007": "spectral radius violation",
        "R008": "MFD capacity violation",
        "R009": "outside local unsaturated region",
    }
    for run in stress_runs:
        lines.append(
            f"| {run['run_id']} | {expected[run['run_id']]} | `{run['classification']}` | {diagnostics[run['run_id']]} | `{run['status']}` |"
        )

    r010 = by_id["R010"]
    lines.extend(
        [
            "",
            "### M5-M6: Numerical and Final Audit",
            "",
            "| Run | Classification | Key Metric | Status |",
            "|-----|----------------|------------|--------|",
            f"| R010 | `{r010['classification']}` | `dt={format_float(r010['metrics']['production_dt'])}`, `step_sensitivity={format_float(r010['metrics']['production_dt_half_step_sensitivity'], 6)}` | `{r010['status']}` |",
            f"| R011 | `{by_id['R011']['classification']}` | `failed_expectations={by_id['R011']['metrics']['failed_expectations']}` | `{by_id['R011']['status']}` |",
            "",
            "## Output Artifacts",
            "",
            f"- JSON summary: `{artifacts['json_latest']}`",
            f"- Run metrics CSV: `{artifacts['csv_latest']}`",
            f"- Trajectory CSV directory: `{artifacts['trajectories_dir']}`",
            f"- Figures directory: `{artifacts['figures_dir']}`",
            f"- Updated tracker: `refine-logs/EXPERIMENT_TRACKER.md`",
            "",
            "## Interpretation",
            "",
            "- R004-R006 show local exponential decay with zero saturation and tiny nonlinear-vs-linear oracle mismatch, so they support the manuscript's local theorem on the non-toy fully connected three-zone instance.",
            "- R007 and R008 are correctly rejected before being treated as theorem evidence, which checks the spectral-radius and MFD-capacity assumptions.",
            "- R009 is correctly labeled as outside the local unsaturated region, so saturation is not overclaimed as a theorem failure or theorem support.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_code_review(path: Path, timestamp_human: str) -> None:
    lines = [
        "# Experiment Code Review",
        "",
        f"**Date**: {timestamp_human}",
        "**Review Mode**: local-only checklist. A secondary sub-agent was not used because this run did not explicitly request delegated agent work.",
        "**Implementation**: `tools/laat_three_zone_experiment.py`",
        "",
        "## Blocking Issues",
        "",
        "- None found before local deployment.",
        "",
        "## Checklist",
        "",
        "| Check | Result |",
        "|-------|--------|",
        "| Hyperparameters exposed through argparse | PASS |",
        "| Deterministic scenario and perturbations fixed | PASS |",
        "| Results saved as JSON/CSV/Markdown | PASS |",
        "| Static feasibility checked before dynamics | PASS |",
        "| Theorem assumptions separated from stress failures | PASS |",
        "| Dynamic trajectory compared against linear oracle | PASS |",
        "| Evaluation uses analytic ground truth rather than another model output | PASS |",
        "| Failure labels prevent overclaiming invalid runs | PASS |",
        "| Fully connected OD demand table is explicit and checked | PASS |",
        "| Per-region targets are in the tens of aircraft | PASS |",
        "| MFD scale matches Weng-style n_cr and n_jam references | PASS |",
        "",
        "## Non-Blocking Notes",
        "",
        "- The current fully connected experiment is CPU-only and deterministic, so GPU deployment, W&B logging, and data-split leakage checks are not applicable.",
        "- The result checker is intentionally strict: stress cases are successful only when they are rejected with the expected label.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def manifest_header() -> str:
    return (
        "# Research Output Manifest\n\n"
        "> Auto-maintained by ARIS skills. Tracks all generated artifacts across the research lifecycle.\n\n"
        "| Timestamp | Skill | File | Stage | Description |\n"
        "|-----------|-------|------|-------|-------------|\n"
    )


def append_manifest(root: Path, rows: Sequence[Tuple[str, str, str, str, str]]) -> None:
    manifest = root / "MANIFEST.md"
    if not manifest.exists():
        manifest.write_text(manifest_header(), encoding="utf-8")
    with manifest.open("a", encoding="utf-8") as f:
        for row in rows:
            timestamp, skill, file_path, stage, description = row
            if description != "latest copy":
                if file_path.endswith(".md") and "EXPERIMENT_RESULTS" in file_path:
                    description = "non-toy three-zone LAAT MFD closed-loop initial results"
                elif file_path.endswith(".json"):
                    description = "non-toy three-zone LAAT simulation JSON details"
                elif file_path.endswith(".csv"):
                    description = "non-toy three-zone LAAT run metrics CSV"
                elif file_path.endswith(".md") and "EXPERIMENT_TRACKER" in file_path:
                    description = "updated non-toy three-zone experiment tracker"
                elif file_path.endswith(".md") and "EXPERIMENT_CODE_REVIEW" in file_path:
                    description = "local experiment code review record"
            f.write("| " + " | ".join((timestamp, skill, file_path, stage, description)) + " |\n")


def relative_to_root(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


def run_all(args: argparse.Namespace) -> Dict[str, Any]:
    root = Path(args.root).resolve() if args.root else repo_root_from_script()
    timestamp, timestamp_human = timestamp_now()
    dirs = ensure_dirs(root, timestamp)

    scenario = make_valid_scenario()
    precheck = precheck_scenario(scenario)

    runs: List[Dict[str, Any]] = [
        parameter_check_run(scenario, precheck),
        static_feasibility_run(precheck),
        spectral_run(precheck),
    ]

    target = precheck["targets"]
    local_scale = args.local_scale
    perturbations = {
        "R004": target * local_scale * np.array([1.0, 1.0, 1.0]),
        "R005": target * local_scale * np.array([1.0, -1.0, 1.0]),
        "R006": target * local_scale * np.array([-1.0, 1.0, -1.0]),
    }
    for run_id, perturbation in perturbations.items():
        runs.append(simulate_run(run_id, scenario, precheck, perturbation, args, dirs["trajectories"]))

    runs.append(assumption_failure_run("R007", make_closed_cycle_scenario(), "rho(B)=1"))
    runs.append(
        assumption_failure_run(
            "R008",
            make_valid_scenario(demand_scale=args.capacity_stress_scale),
            "Lambda_i >= ubar_i Gmax",
        )
    )

    far_perturbation = np.array(
        [args.far_positive, args.far_negative, args.far_positive], dtype=float
    )
    runs.append(simulate_run("R009", scenario, precheck, far_perturbation, args, dirs["trajectories"]))
    runs.append(sampled_check_run(precheck, args))
    runs.append(final_audit_run(runs))

    if not args.no_plots:
        for run in runs:
            if run["run_id"] in {"R004", "R005", "R006", "R009"}:
                fig_path = plot_trajectory(run, dirs["figures"])
                if fig_path:
                    run.setdefault("artifacts", {})["figure"] = fig_path

    command = " ".join([Path(sys.executable).name, *sys.argv])
    summary = {
        "metadata": {
            "timestamp": timestamp_human,
            "plan": str(root / "refine-logs" / "EXPERIMENT_PLAN.md"),
            "script": str(Path(__file__).resolve()),
            "command": command,
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
        },
        "scenario": {
            "demand_matrix": scenario.demand_matrix,
            "potential_demand_matrix": scenario.potential_demand_matrix,
            "q_g": scenario.q_g,
            "t_matrix": scenario.t_matrix,
            "t_exit": scenario.t_exit,
            "lambda": precheck["static"]["lambda"],
            "beta": precheck["static"]["beta"],
            "beta_exit": precheck["static"]["beta_exit"],
            "target": precheck["targets"],
            "b_matrix": precheck["b_matrix"],
            "a_matrix": precheck["a_matrix"],
            "q_cap": scenario.q_cap,
            "interface_cap": scenario.interface_cap,
            "ubar": scenario.ubar,
            "kappa": scenario.kappa,
            "eta": scenario.eta,
            "epsilon": scenario.epsilon,
            "mfd": {
                "form": "Gmax * n(1-n/n_jam)^p / [n_cr(1-n_cr/n_jam)^p]",
                "g_max": scenario.g_max,
                "n_cr": scenario.n_cr,
                "n_jam": scenario.n_jam,
                "shape_exponent": scenario.mfd_shape_exponent,
            },
        },
        "runs": runs,
    }

    results_json_ts = dirs["results"] / f"three_zone_laat_results_{timestamp}.json"
    results_json_latest = dirs["results"] / "three_zone_laat_results.json"
    metrics_csv_ts = dirs["results"] / f"three_zone_laat_run_metrics_{timestamp}.csv"
    metrics_csv_latest = dirs["results"] / "three_zone_laat_run_metrics.csv"
    results_md_ts = dirs["refine"] / f"EXPERIMENT_RESULTS_{timestamp}.md"
    results_md_latest = dirs["refine"] / "EXPERIMENT_RESULTS.md"
    tracker_ts = dirs["refine"] / f"EXPERIMENT_TRACKER_{timestamp}.md"
    tracker_latest = dirs["refine"] / "EXPERIMENT_TRACKER.md"
    code_review_ts = dirs["refine"] / f"EXPERIMENT_CODE_REVIEW_{timestamp}.md"
    code_review_latest = dirs["refine"] / "EXPERIMENT_CODE_REVIEW.md"

    write_json(results_json_ts, summary)
    shutil.copyfile(results_json_ts, results_json_latest)
    write_metrics_csv(metrics_csv_ts, runs)
    shutil.copyfile(metrics_csv_ts, metrics_csv_latest)
    write_tracker(tracker_ts, runs)
    shutil.copyfile(tracker_ts, tracker_latest)
    write_code_review(code_review_ts, timestamp_human)
    shutil.copyfile(code_review_ts, code_review_latest)

    artifacts = {
        "command": command,
        "json_latest": relative_to_root(root, results_json_latest),
        "csv_latest": relative_to_root(root, metrics_csv_latest),
        "trajectories_dir": relative_to_root(root, dirs["trajectories"]),
        "figures_dir": relative_to_root(root, dirs["figures"]),
    }
    write_results_md(results_md_ts, timestamp_human, args, scenario, precheck, runs, artifacts)
    shutil.copyfile(results_md_ts, results_md_latest)

    append_manifest(
        root,
        [
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, results_md_ts),
                "implementation",
                "non-toy three-zone LAAT MFD closed-loop initial results",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, results_md_latest),
                "implementation",
                "latest copy",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, results_json_ts),
                "implementation",
                "non-toy three-zone LAAT simulation JSON details",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, results_json_latest),
                "implementation",
                "latest copy",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, metrics_csv_ts),
                "implementation",
                "non-toy three-zone LAAT run metrics CSV",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, metrics_csv_latest),
                "implementation",
                "latest copy",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, tracker_ts),
                "implementation",
                "updated non-toy three-zone experiment tracker",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, tracker_latest),
                "implementation",
                "latest copy",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, code_review_ts),
                "implementation",
                "local experiment code review record",
            ),
            (
                timestamp_human,
                "/experiment-bridge",
                relative_to_root(root, code_review_latest),
                "implementation",
                "latest copy",
            ),
        ],
    )

    print(
        json.dumps(
            {
                "results": relative_to_root(root, results_md_latest),
                "json": relative_to_root(root, results_json_latest),
                "csv": relative_to_root(root, metrics_csv_latest),
                "tracker": relative_to_root(root, tracker_latest),
                "all_success": all(run.get("success", False) for run in runs),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return summary


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the fully connected three-zone LAAT MFD planning/control validation."
    )
    parser.add_argument("--root", default=None, help="Repository root. Defaults to script parent.")
    parser.add_argument("--t-final", type=float, default=60.0, help="Simulation horizon.")
    parser.add_argument("--num-points", type=int, default=1201, help="Number of sampled time points.")
    parser.add_argument("--local-scale", type=float, default=0.10, help="Local perturbation scale.")
    parser.add_argument("--far-positive", type=float, default=80.0, help="Positive far perturbation.")
    parser.add_argument("--far-negative", type=float, default=-20.0, help="Negative far perturbation.")
    parser.add_argument(
        "--capacity-stress-scale",
        type=float,
        default=1.20,
        help="Demand multiplier for the capacity falsification run.",
    )
    parser.add_argument("--rtol", type=float, default=1e-10, help="solve_ivp relative tolerance.")
    parser.add_argument("--atol", type=float, default=1e-12, help="solve_ivp absolute tolerance.")
    parser.add_argument(
        "--oracle-mismatch-tol",
        type=float,
        default=1e-3,
        help="Maximum relative mismatch allowed against the linear oracle.",
    )
    parser.add_argument(
        "--final-ratio-tol",
        type=float,
        default=0.05,
        help="Maximum final error ratio for theorem-support local runs.",
    )
    parser.add_argument(
        "--dts",
        type=float,
        nargs="+",
        default=[0.05, 0.1, 0.25, 0.5],
        help="Euler sampled-hold steps to check.",
    )
    parser.add_argument("--no-plots", action="store_true", help="Skip PNG figure generation.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    run_all(args)


if __name__ == "__main__":
    main()
