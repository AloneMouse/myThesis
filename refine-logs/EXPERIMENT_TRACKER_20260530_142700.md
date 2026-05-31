# Experiment Tracker

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|--------|-----------|---------|------------------|-------|---------|----------|--------|-------|
| R001 | M0 | Encode scenario | Valid 3-zone single-layer instance | deterministic | parameter equality checks | MUST | TODO | Should reproduce `q^g,T,Lambda,beta,B` from the plan |
| R002 | M1 | Static feasibility and target construction | Valid instance | deterministic | conservation residual, beta residual, target residual, capacity margins | MUST | TODO | Blocks theorem interpretation if any precheck fails |
| R003 | M2 | Spectral and closed-loop matrix check | Valid instance | deterministic | `rho(B)`, eigenvalues of `A`, hand-computed `A` mismatch | MUST | TODO | Expected eigenvalues `(-0.5,-0.5,-0.4)` |
| R004 | M3 | Local trajectory 1 | Valid instance, perturbation `(+,+,+)` | local | final error ratio, log decay slope, saturation fraction, oracle mismatch | MUST | TODO | Perturbation scale `<=10%` of `bar n` |
| R005 | M3 | Local trajectory 2 | Valid instance, perturbation `(+,-,+)` | local | final error ratio, log decay slope, saturation fraction, oracle mismatch | MUST | TODO | Tests cross-region coupling signs |
| R006 | M3 | Local trajectory 3 | Valid instance, perturbation `(-,+,-)` | local | final error ratio, log decay slope, saturation fraction, oracle mismatch | MUST | TODO | Checks nonnegativity margin near lower side |
| R007 | M4 | Spectral falsification | Closed cycle `1->2->3->1`, no exit flow | stress | `rho(B)`, checker classification | MUST | TODO | Expected label `ASSUMPTION_FAILURE` |
| R008 | M4 | Capacity falsification | Valid flows multiplied by `1.6` | stress | capacity residual, target feasibility, checker classification | MUST | TODO | Expected label `ASSUMPTION_FAILURE` |
| R009 | M4 | Local-region falsification | Valid plan with far initial state | stress | saturation fraction, capacity violations, checker classification | MUST | TODO | Expected label `OUTSIDE_LOCAL_REGION` |
| R010 | M5 | Sampled implementation check | Valid instance, Euler or sampled hold | engineering | `rho(I+A Delta t)`, step-size sensitivity | NICE | TODO | Mandatory only if final simulator is discrete-time |
| R011 | M6 | Final result audit | All completed runs | report | L0-L6 pass matrix, support labels, assumption-failure table | MUST | TODO | Should produce the table used in paper or appendix |
