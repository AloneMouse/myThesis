# Experiment Tracker

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|--------|-----------|---------|------------------|-------|---------|----------|--------|-------|
| R001 | M0 | Encode scenario | Valid 3-zone single-layer instance | deterministic | parameter equality checks | MUST | DONE | SUPPORTS_THEOREM; Scenario matches the deterministic plan table |
| R002 | M1 | Static feasibility and target construction | Valid instance | deterministic | conservation/beta/target/capacity margins | MUST | DONE | SUPPORTS_THEOREM; Static bridge and target feasibility passed |
| R003 | M2 | Spectral and closed-loop matrix check | Valid instance | deterministic | rho(B), eig(A), A mismatch | MUST | DONE | SUPPORTS_THEOREM; Spectral and hand-computed matrix checks passed |
| R004 | M3 | Local trajectory 1 | Valid instance, perturbation (+,+,+) | local | final ratio, slope, saturation, oracle mismatch | MUST | DONE | SUPPORTS_THEOREM; Local theorem-support trajectory |
| R005 | M3 | Local trajectory 2 | Valid instance, perturbation (+,-,+) | local | final ratio, slope, saturation, oracle mismatch | MUST | DONE | SUPPORTS_THEOREM; Local theorem-support trajectory |
| R006 | M3 | Local trajectory 3 | Valid instance, perturbation (-,+,-) | local | final ratio, slope, saturation, oracle mismatch | MUST | DONE | SUPPORTS_THEOREM; Local theorem-support trajectory |
| R007 | M4 | Spectral falsification | Closed cycle, no exit flow | stress | rho(B), classification | MUST | DONE | ASSUMPTION_FAILURE; Correctly rejected stress case: rho(B)=1; failures=['L3_stability_assumptions'] |
| R008 | M4 | Capacity falsification | Valid flows multiplied by 1.6 | stress | capacity residual, classification | MUST | DONE | ASSUMPTION_FAILURE; Correctly rejected stress case: Lambda_i >= ubar_i Gmax; failures=['L2_target_feasibility', 'region 1: Lambda=0.96 is not below ubar*Gmax=0.9', 'region 2: Lambda=0.96 is not below ubar*Gmax=0.9', 'region 3: Lambda=0.96 is not below ubar*Gmax=0.9'] |
| R009 | M4 | Local-region falsification | Valid plan with far initial state | stress | saturation, classification | MUST | DONE | OUTSIDE_LOCAL_REGION; Correctly flagged as outside the local unsaturated region |
| R010 | M5 | Sampled implementation check | Valid instance, Euler sampled hold | engineering | rho(I+A dt), step sensitivity | NICE | DONE | SUPPORTS_THEOREM; Sampled Euler stability and step-sensitivity check passed |
| R011 | M6 | Final result audit | All completed runs | report | L0-L6 pass matrix and labels | MUST | DONE | SUPPORTS_THEOREM; Final audit passed |
