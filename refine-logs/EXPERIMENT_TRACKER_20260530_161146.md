# Experiment Tracker

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|--------|-----------|---------|------------------|-------|---------|----------|--------|-------|
| R001 | M0 | Encode explicit Weng-scale scenario | 20x OD table with six positive directed demands | deterministic | parameter equality checks | MUST | DONE | SUPPORTS_THEOREM; Scenario matches the non-toy Weng-scale deterministic plan table |
| R002 | M1 | Static aggregation and feasibility | Non-toy fully connected base scenario | deterministic | conservation/beta/target/capacity margins | MUST | DONE | SUPPORTS_THEOREM; Static bridge and target feasibility passed |
| R003 | M2 | Coupled matrix stability check | Non-toy fully connected base scenario | deterministic | rho(B), eig(A), A mismatch | MUST | DONE | SUPPORTS_THEOREM; Spectral and hand-computed matrix checks passed |
| R004 | M3 | Local trajectory 1 | Perturbation 0.10*bar n*(+,+,+) | local | final ratio, slope, saturation, oracle mismatch | MUST | DONE | SUPPORTS_THEOREM; Local theorem-support trajectory |
| R005 | M3 | Local trajectory 2 | Perturbation 0.10*bar n*(+,-,+) | local | final ratio, slope, saturation, oracle mismatch | MUST | DONE | SUPPORTS_THEOREM; Local theorem-support trajectory |
| R006 | M3 | Local trajectory 3 | Perturbation 0.10*bar n*(-,+,-) | local | final ratio, slope, saturation, oracle mismatch | MUST | DONE | SUPPORTS_THEOREM; Local theorem-support trajectory |
| R007 | M4 | Spectral falsification | Fully connected no-exit circulation | stress | rho(B), classification | MUST | DONE | ASSUMPTION_FAILURE; Correctly rejected stress case: rho(B)=1; failures=['L3_stability_assumptions'] |
| R008 | M4 | Capacity falsification | Base OD demand scaled by s=1.20 | stress | capacity residual, classification | MUST | DONE | ASSUMPTION_FAILURE; Correctly rejected stress case: Lambda_i >= ubar_i Gmax; failures=['L2_target_feasibility', 'region 1: Lambda=10.08 is not below ubar*Gmax=9.936', 'region 2: Lambda=10.32 is not below ubar*Gmax=9.936', 'region 3: Lambda=10.32 is not below ubar*Gmax=9.936'] |
| R009 | M4 | Local-region falsification | Base plan with far initial error (+80,-20,+80) | stress | saturation, classification | MUST | DONE | OUTSIDE_LOCAL_REGION; Correctly flagged as outside the local unsaturated region |
| R010 | M5 | Sampled-hold check | Euler sampled update | engineering | rho(I+A dt), step sensitivity | NICE | DONE | SUPPORTS_THEOREM; Sampled Euler stability and step-sensitivity check passed |
| R011 | M6 | Final result audit | All completed runs | report | L0-L6 pass matrix and labels | MUST | DONE | SUPPORTS_THEOREM; Final audit passed |
