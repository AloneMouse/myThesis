# Initial Experiment Results

**Date**: 2026-05-30 15:14
**Plan**: `refine-logs/EXPERIMENT_PLAN.md`
**Implementation**: `tools/laat_three_zone_experiment.py`
**Command**: `python.exe tools\laat_three_zone_experiment.py`

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
| R001 | `SUPPORTS_THEOREM` | `parameter_max_abs_mismatch=5.551e-17` | `DONE` |
| R002 | `SUPPORTS_THEOREM` | `conservation_residual=0`; `beta_residual=1.11e-16`; `target_residual=1.11e-16` | `DONE` |
| R003 | `SUPPORTS_THEOREM` | `rho_b=0.4977`; `max_real_eig_a=-0.2809`; `a_matrix_max_abs_mismatch=5.551e-17` | `DONE` |

### M3: Local Closed-Loop Trajectories

| Run | Classification | Final Error Ratio | Log Slope | Saturation Fraction | Oracle Mismatch | Status |
|-----|----------------|-------------------|-----------|---------------------|-----------------|--------|
| R004 | `SUPPORTS_THEOREM` | `0.00364774` | `-0.280771` | `0` | `1.02153e-09` | `DONE` |
| R005 | `SUPPORTS_THEOREM` | `0.00109484` | `-0.312987` | `0` | `7.48595e-10` | `DONE` |
| R006 | `SUPPORTS_THEOREM` | `0.00109484` | `-0.312987` | `0` | `7.59992e-10` | `DONE` |

### M4: Falsification Checks

| Run | Expected Failure Type | Classification | Key Diagnostic | Status |
|-----|-----------------------|----------------|----------------|--------|
| R007 | spectral radius violation | `ASSUMPTION_FAILURE` | `rho_b=1` | `DONE` |
| R008 | MFD capacity violation | `ASSUMPTION_FAILURE` | `capacity_margin=-0.003` | `DONE` |
| R009 | outside local unsaturated region | `OUTSIDE_LOCAL_REGION` | `saturation_fraction=0.2366` | `DONE` |

### M5-M6: Numerical and Final Audit

| Run | Classification | Key Metric | Status |
|-----|----------------|------------|--------|
| R010 | `SUPPORTS_THEOREM` | `dt=0.05`, `step_sensitivity=2.12707e-05` | `DONE` |
| R011 | `SUPPORTS_THEOREM` | `failed_expectations=[]` | `DONE` |

## Output Artifacts

- JSON summary: `refine-logs/results/three_zone_laat_results.json`
- Run metrics CSV: `refine-logs/results/three_zone_laat_run_metrics.csv`
- Trajectory CSV directory: `refine-logs/results/trajectories_20260530_151448`
- Figures directory: `refine-logs/figures`
- Updated tracker: `refine-logs/EXPERIMENT_TRACKER.md`

## Interpretation

- R004-R006 show local exponential decay with zero saturation and tiny nonlinear-vs-linear oracle mismatch, so they support the manuscript's local theorem on the fully connected three-zone instance.
- R007 and R008 are correctly rejected before being treated as theorem evidence, which checks the spectral-radius and MFD-capacity assumptions.
- R009 is correctly labeled as outside the local unsaturated region, so saturation is not overclaimed as a theorem failure or theorem support.
