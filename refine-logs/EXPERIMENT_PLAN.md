# Experiment Plan

**Problem**: 构造一个非 toy 的单层三区域低空交通流量规划与控制实验。三区域两两互联，每个区域在稳态时必须有几十架飞行器，并用完整参数检验手稿中的静态规划到动态闭环控制理论。

**Method Thesis**: 在三区域完全互联、六个有向 OD 需求均为正的低空单层网络中，若静态聚合满足守恒，目标累积位于 MFD 自由流分支，执行容量有余量，且内部转移矩阵 `B` 满足 `rho(B)<1`，则手稿提出的起飞准入与边界放行闭环应在目标附近表现为局部指数稳定。无出口循环、超 MFD 容量和远初值饱和应被检查器明确拒绝，不能被误报为理论支持。

**Date**: 2026-05-30

**Manuscript Source**: `drafts/LAATDraft_v1.3.tex`

**Scale Reference**: `markdown_docs/LAAT/Urban low-altitude air transport management Bridging dynamic.md`

## Scale Guard

这版实验不再是“每区几架”的 toy model。基准目标累积为：

```text
bar n = (60.1491, 63.1814, 63.1814) aircraft
```

因此每个区域稳态均为几十架飞行器。尺度向 Weng et al. 的 LAAT 案例靠齐：

| Reference Item | Value Used in Reference | Value Used Here |
|---|---:|---:|
| airspace region size | `2 km x 2 km x 1 km` | same reference scale |
| critical accumulation | `n_cr=110.4` aircraft | `n_cr=110.4` |
| jam accumulation | `n_jam=800` aircraft | `n_jam=800` |
| workday equilibrium | `(43.6, 36.3)` aircraft | lower than our non-toy target |
| holiday equilibrium | `(82.8, 69.0)` aircraft | same order as our target |
| time-varying demand example | `120 min`, 20% peak excess, 0.5% Gaussian noise | optional robustness only |

The main theorem-support experiment is deterministic because the theorem is about a fixed feasible equilibrium. The optional robustness profile is separated so noise is not confused with proof evidence.

## Claim Map

| Claim | Why It Matters | Minimum Convincing Evidence | Linked Blocks |
|---|---|---|---|
| C1: Fully connected OD demand can be aggregated into the manuscript's regional MFD variables | The theorem must work beyond a chain or triangular toy network | all six OD flows positive; conservation residual `<=1e-10`; beta rows sum to one; target residual `<=1e-8` | B1 |
| C2: Local closed-loop stability holds at non-toy accumulation scale | The user-facing claim is meaningful only when each region carries tens of aircraft | `rho(B)=0.4977163954<1`; max real eigenvalue of `A` is negative; local trajectories decay without saturation | B2 |
| C3: The result checker prevents overclaiming | Stress cases should fail for the right reason | no-exit circulation gives spectral assumption failure; demand stress gives MFD capacity failure; far initial condition gives outside-local label | B3 |

## Fully Connected Three-Zone Scenario

### Region and Network Parameters

| Parameter | Value | Meaning |
|---|---:|---|
| `R` | `3` | number of airspace regions |
| region set | `{1,2,3}` | single-layer low-altitude regions |
| virtual exit node | `0` | completed trips leave the dynamic system |
| adjacency | `N_1={2,3}`, `N_2={1,3}`, `N_3={1,2}` | each region connects to the other two |
| directed transfer links | `1->2,1->3,2->1,2->3,3->1,3->2` | all six directed inter-region flows are allowed |
| altitude layers | `1` | no multi-layer airspace |
| explicit flight delay | `0` | no delay state in this minimal theorem experiment |
| vertiport queue | outside dynamic state | unaccepted demand is not counted in regional aircraft accumulation |
| routing mode | fixed direct regional path | each OD uses one direct regional link |

### Demand Parameters

Units are aircraft per simulation minute. The base OD pattern is the previous fully connected table multiplied by `20`, so it keeps the same routing proportions but moves the aircraft accumulation to realistic tens.

| OD | Path | Served Demand `q_m` | Potential Demand `bar q_m` | Path Share |
|---|---|---:|---:|---:|
| `M12` | `(1,2)` | `2.40` | `3.00` | `1.0` |
| `M13` | `(1,3)` | `2.00` | `2.60` | `1.0` |
| `M21` | `(2,1)` | `1.80` | `2.40` | `1.0` |
| `M23` | `(2,3)` | `2.80` | `3.40` | `1.0` |
| `M31` | `(3,1)` | `2.20` | `2.80` | `1.0` |
| `M32` | `(3,2)` | `1.60` | `2.00` | `1.0` |

Demand matrix:

```text
q =
[[0.00, 2.40, 2.00],
 [1.80, 0.00, 2.80],
 [2.20, 1.60, 0.00]]
```

Potential demand matrix:

```text
bar q =
[[0.00, 3.00, 2.60],
 [2.40, 0.00, 3.40],
 [2.80, 2.00, 0.00]]
```

Demand totals:

| Quantity | Region 1 | Region 2 | Region 3 | Total |
|---|---:|---:|---:|---:|
| takeoff inflow `q_i^g` | `4.40` | `4.60` | `3.80` | `12.80` |
| completion flow `T_i0` | `4.00` | `4.00` | `4.80` | `12.80` |
| aggregate dynamic load `Lambda_i=q_i^g+sum_j T_ji` | `8.40` | `8.60` | `8.60` | `25.60` |
| outgoing potential demand | `5.60` | `5.80` | `4.80` | `16.20` |

Main simulation demand rules:

| Demand Requirement | Value |
|---|---|
| demand mode | deterministic constant demand |
| time interval | `t in [0,60]` minutes |
| served OD demand | exactly the `q` matrix above |
| potential OD demand | exactly the `bar q` matrix above |
| stochastic noise | none in theorem-support runs |
| demand scale | `20.0` from previous toy table |
| capacity-stress demand scale | additional `s=1.20`, so `Lambda=(10.08,10.32,10.32)` |
| optional robustness profile | Weng-style trapezoid over `120 min`, 20% peak excess, 0.5% Gaussian noise; not must-run |

### Static Aggregation

Internal transfer matrix equals the demand matrix. Completion vector:

```text
T_0 = (4.00, 4.00, 4.80)
Lambda = (8.40, 8.60, 8.60)
```

Routing ratios:

| Ratio | Value |
|---|---:|
| `beta_12` | `0.2857142857` |
| `beta_13` | `0.2380952381` |
| `beta_10` | `0.4761904762` |
| `beta_21` | `0.2093023256` |
| `beta_23` | `0.3255813953` |
| `beta_20` | `0.4651162791` |
| `beta_31` | `0.2558139535` |
| `beta_32` | `0.1860465116` |
| `beta_30` | `0.5581395349` |

Internal matrix:

```text
B =
[[0.0000000000, 0.2857142857, 0.2380952381],
 [0.2093023256, 0.0000000000, 0.3255813953],
 [0.2558139535, 0.1860465116, 0.0000000000]]

rho(B) = 0.4977163954
```

### MFD Parameters

Use a Weng-scale single-peaked accumulation MFD:

```text
G_i(n) = Gmax * n(1 - n/n_jam)^p / [n_cr(1 - n_cr/n_jam)^p]
p = n_jam/n_cr - 1
```

| Parameter | Value |
|---|---:|
| `Gmax` | `16.56` aircraft/min |
| `n_cr` | `110.4` aircraft |
| `n_jam` | `800.0` aircraft |
| `p` | `6.2463768116` |
| boundary release margin `bar u_i` | `0.60` for all regions |
| effective MFD capacity `bar u_i Gmax` | `9.936` aircraft/min |

Target construction:

| Region | `Lambda_i` | `Lambda_i/bar u_i` | `bar n_i` | Capacity Margin `bar u_i Gmax-Lambda_i` |
|---|---:|---:|---:|---:|
| 1 | `8.40` | `14.0000` | `60.1491` | `1.5360` |
| 2 | `8.60` | `14.3333` | `63.1814` | `1.3360` |
| 3 | `8.60` | `14.3333` | `63.1814` | `1.3360` |

All targets are below `n_cr=110.4`, so they lie on the free-flow branch.

### Capacity Parameters

Takeoff capacities:

| Region | `q_i^g` | `bar q_i^a` | Margin |
|---|---:|---:|---:|
| 1 | `4.40` | `11.00` | `6.60` |
| 2 | `4.60` | `11.00` | `6.40` |
| 3 | `3.80` | `10.00` | `6.20` |

Interface capacities:

| Interface Type | Capacity | Planned Max Flow | Minimum Margin |
|---|---:|---:|---:|
| each internal directed link | `7.00` | `2.80` | `4.20` |
| each exit link `i->0` | `14.00` | `4.80` | `9.20` |

### Controller Parameters

| Parameter | Region 1 | Region 2 | Region 3 |
|---|---:|---:|---:|
| `bar u_i` | `0.60` | `0.60` | `0.60` |
| `kappa_i` | `0.40` | `0.40` | `0.40` |
| `eta_i` | `0.08` | `0.08` | `0.08` |
| denominator guard `epsilon_i` | `0.05` | `0.05` | `0.05` |

Expected local unsaturated matrix:

```text
A = (B^T - I)K - H
  =
[[-0.4800000000,  0.0837209302,  0.1023255814],
 [ 0.1142857143, -0.4800000000,  0.0744186047],
 [ 0.0952380952,  0.1302325581, -0.4800000000]]

eig(A) =
-0.2809134418
-0.5795432791 +/- 0.0268601600 i
```

### Simulation Parameters

| Parameter | Value |
|---|---:|
| script | `tools/laat_three_zone_experiment.py` |
| simulation horizon | `T_final=60.0` min |
| output samples | `1201` |
| saved sample interval | `0.05` min |
| continuous solver | `scipy.integrate.solve_ivp(method="DOP853")` |
| relative tolerance | `rtol=1e-10` |
| absolute tolerance | `atol=1e-12` |
| local perturbation scale | `10%` of `bar n_i`, about `6` aircraft per region |
| final error ratio threshold | `<=0.05` |
| nonlinear-vs-linear oracle mismatch threshold | `<=1e-3` |
| allowed saturation in theorem-support runs | `0` |
| sampled-hold Euler steps | `Delta t in {0.05,0.10,0.25,0.50}` |
| far stress initial error | `(+80,-20,+80)` aircraft |

Local theorem-support initial states:

| Run | Initial Error `e(0)` | Meaning |
|---|---|---|
| `R004` | `0.10 * bar n * (+1,+1,+1)` | all regions start high by about 6 aircraft |
| `R005` | `0.10 * bar n * (+1,-1,+1)` | mixed-sign coupling check |
| `R006` | `0.10 * bar n * (-1,+1,-1)` | opposite mixed-sign coupling check |

Stress checks:

| Run | Stress | Expected Label |
|---|---|---|
| `R007` | fully connected no-exit circulation, `rho(B)=1` | `ASSUMPTION_FAILURE` |
| `R008` | base demand scaled by `1.20`, MFD capacity exceeded | `ASSUMPTION_FAILURE` |
| `R009` | far initial error `(+80,-20,+80)` triggers saturation | `OUTSIDE_LOCAL_REGION` |

## Experiment Blocks

### B1: Static Aggregation and Feasibility

- Claim tested: C1.
- Why this block exists: verify that the fully connected non-toy OD table enters the manuscript's aggregate model without ambiguity.
- Compared systems: proposed static aggregation only.
- Metrics: conservation residual, beta residual, target residual, takeoff margin, interface margin, MFD capacity margin.
- Success criterion: residuals below tolerance and all margins positive.
- Priority: MUST-RUN.

### B2: Local Closed-Loop Stability

- Claim tested: C2.
- Why this block exists: validate the theorem near a Weng-scale target with tens of aircraft per region.
- Compared systems: nonlinear saturated ODE vs exact local linear oracle.
- Metrics: final error ratio, fitted log-error slope, saturation fraction, oracle mismatch, strict-tolerance final difference.
- Success criterion: R004-R006 all decay, have zero saturation, and match the oracle.
- Priority: MUST-RUN.

### B3: Falsification and Audit

- Claim tested: C3.
- Why this block exists: ensure invalid settings are not counted as theorem evidence.
- Compared systems: no-exit circulation, capacity-stress case, far-initial-condition case, sampled-hold implementation.
- Metrics: stress classification, `rho(B)`, capacity residual, saturation fraction, Euler step spectral radius.
- Success criterion: stress cases fail for the expected reason and final audit reports no failed expectations.
- Priority: MUST-RUN, with sampled-hold check NICE-TO-HAVE.

## Run Order and Milestones

| Run | Milestone | Purpose | Priority |
|---|---|---|---|
| R001 | M0 | exact parameter equality check against this plan | MUST |
| R002 | M1 | static aggregation and feasibility | MUST |
| R003 | M2 | spectral stability check | MUST |
| R004 | M3 | local trajectory all-high perturbation | MUST |
| R005 | M3 | local trajectory mixed perturbation | MUST |
| R006 | M3 | local trajectory opposite mixed perturbation | MUST |
| R007 | M4 | spectral falsification | MUST |
| R008 | M4 | capacity falsification | MUST |
| R009 | M4 | far initial saturation falsification | MUST |
| R010 | M5 | sampled-hold engineering check | NICE |
| R011 | M6 | final result audit | MUST |

## Compute and Data Budget

- Total estimated GPU-hours: `0`; CPU-only ODE simulation.
- Expected runtime: seconds to a few minutes on local CPU.
- Data preparation: none; all OD, MFD, capacity, controller and simulation parameters are explicit above.
- Biggest bottleneck: not compute, but ensuring stress cases are labeled as invalid assumptions rather than negative theorem evidence.

## Final Checklist

- [x] Non-toy target accumulation is in the tens of aircraft for every region.
- [x] Three regions are mutually connected with six positive directed OD flows.
- [x] Demand settings are explicit, including served demand, potential demand, and stress scale.
- [x] MFD scale is aligned with the referenced LAAT paper's `n_cr` and `n_jam`.
- [x] Simulation settings are explicit.
- [x] Stress cases are separated from theorem-support runs.
