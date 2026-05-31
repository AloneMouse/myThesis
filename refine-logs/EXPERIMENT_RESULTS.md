# Initial Experiment Results

**Date**: 2026-05-30 16:11
**Plan**: `refine-logs/EXPERIMENT_PLAN.md`
**Implementation**: `tools/laat_three_zone_experiment.py`
**Command**: `python.exe tools\laat_three_zone_experiment.py`
**Scale Note**: non-toy Weng-scale three-zone case; each steady-state region has tens of aircraft.

## Scenario Settings

| Quantity | Value |
|----------|-------|
| region geometry reference | `2 km x 2 km x 1 km` per region |
| demand matrix | `[(0, 2.4, 2); (1.8, 0, 2.8); (2.2, 1.6, 0)]` |
| takeoff inflow `q_g` | `(4.4, 4.6, 3.8)` |
| completion flow `T_i0` | `(4, 4, 4.8)` |
| aggregate load `Lambda` | `(8.4, 8.6, 8.6)` |
| target accumulation `bar n` | `(60.1491, 63.1814, 63.1814)` aircraft |
| MFD | `Gmax=16.56, n_cr=110.4, n_jam=800, p=6.24638` |
| takeoff caps | `(11, 11, 10)` |
| internal / exit interface caps | `7 / 14` |
| controller gains | `ubar=(0.6, 0.6, 0.6), kappa=(0.4, 0.4, 0.4), eta=(0.08, 0.08, 0.08)` |
| simulation | `T_final=60, samples=1201, rtol=1e-10, atol=1e-12` |

## Summary

- MUST-RUN completed: `10/10`.
- MUST-RUN expected criteria passed: `10/10`.
- Nice-to-have completed: `1/1`.
- Main result: `positive`.
- Ready for `/auto-review-loop`: `YES`.

## Results by Milestone

### M0-M2: Preflight and Stability Matrix

| Run | Classification | Key Metrics | Status |
|-----|----------------|-------------|--------|
| R001 | `SUPPORTS_THEOREM` | `parameter_max_abs_mismatch=1.776e-15` | `DONE` |
| R002 | `SUPPORTS_THEOREM` | `conservation_residual=0`; `beta_residual=1.11e-16`; `target_residual=0` | `DONE` |
| R003 | `SUPPORTS_THEOREM` | `rho_b=0.4977`; `max_real_eig_a=-0.2809`; `a_matrix_max_abs_mismatch=5.551e-17` | `DONE` |

### M3: Local Closed-Loop Trajectories

| Run | Classification | Final Error Ratio | Log Slope | Saturation Fraction | Oracle Mismatch | Status |
|-----|----------------|-------------------|-----------|---------------------|-----------------|--------|
| R004 | `SUPPORTS_THEOREM` | `4.80707e-08` | `-0.280896` | `0` | `1.04698e-09` | `DONE` |
| R005 | `SUPPORTS_THEOREM` | `1.41871e-08` | `-0.285072` | `0` | `7.51542e-10` | `DONE` |
| R006 | `SUPPORTS_THEOREM` | `1.41871e-08` | `-0.285072` | `0` | `7.61867e-10` | `DONE` |

### M4: Falsification Checks

| Run | Expected Failure Type | Classification | Key Diagnostic | Status |
|-----|-----------------------|----------------|----------------|--------|
| R007 | spectral radius violation | `ASSUMPTION_FAILURE` | `rho_b=1` | `DONE` |
| R008 | MFD capacity violation | `ASSUMPTION_FAILURE` | `capacity_margin=-0.384` | `DONE` |
| R009 | outside local unsaturated region | `OUTSIDE_LOCAL_REGION` | `saturation_fraction=0.05273` | `DONE` |

### M5-M6: Numerical and Final Audit

| Run | Classification | Key Metric | Status |
|-----|----------------|------------|--------|
| R010 | `SUPPORTS_THEOREM` | `dt=0.05`, `step_sensitivity=7.78757e-10` | `DONE` |
| R011 | `SUPPORTS_THEOREM` | `failed_expectations=[]` | `DONE` |

## Output Artifacts

- JSON summary: `refine-logs/results/three_zone_laat_results.json`
- Run metrics CSV: `refine-logs/results/three_zone_laat_run_metrics.csv`
- Trajectory CSV directory: `refine-logs/results/trajectories_20260530_161146`
- Figures directory: `refine-logs/figures`
- Updated tracker: `refine-logs/EXPERIMENT_TRACKER.md`

## Interpretation

- R004-R006 show local exponential decay with zero saturation and tiny nonlinear-vs-linear oracle mismatch, so they support the manuscript's local theorem on the non-toy fully connected three-zone instance.
- R007 and R008 are correctly rejected before being treated as theorem evidence, which checks the spectral-radius and MFD-capacity assumptions.
- R009 is correctly labeled as outside the local unsaturated region, so saturation is not overclaimed as a theorem failure or theorem support.
