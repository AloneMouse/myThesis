# Experiment Tracker

| Run ID | Milestone | Purpose | System / Variant | Split | Metrics | Priority | Status | Notes |
|--------|-----------|---------|------------------|-------|---------|----------|--------|-------|
| R001 | M0 | Encode explicit fully connected scenario | Base OD table with six positive directed demands | deterministic | parameter equality checks | MUST | TODO | Verify OD, path, MFD, capacity, controller, and solver parameters |
| R002 | M1 | Static aggregation and feasibility | Fully connected base scenario | deterministic | conservation, beta, target, capacity margins | MUST | TODO | Must match `q^g,T,T_0,Lambda,beta` from the plan |
| R003 | M2 | Coupled matrix stability check | Fully connected base scenario | deterministic | `rho(B)`, eigenvalues of `A`, expected matrix mismatch | MUST | TODO | Expected `rho(B)=0.4977163954`, max real eigenvalue `-0.2809134418` |
| R004 | M3 | Local trajectory 1 | Perturbation `0.10*bar n*(+,+,+)` | local | final ratio, log slope, saturation, oracle mismatch | MUST | TODO | Theorem-support run only if saturation fraction is zero |
| R005 | M3 | Local trajectory 2 | Perturbation `0.10*bar n*(+,-,+)` | local | final ratio, log slope, saturation, oracle mismatch | MUST | TODO | Tests mixed-sign coupling under fully connected `B` |
| R006 | M3 | Local trajectory 3 | Perturbation `0.10*bar n*(-,+,-)` | local | final ratio, log slope, saturation, oracle mismatch | MUST | TODO | Tests lower-state perturbations without leaving nonnegative domain |
| R007 | M4 | Spectral falsification | Fully connected no-exit circulation `T_ij=0.10` for all `i!=j` | stress | `rho(B)`, checker classification | MUST | TODO | Expected label `ASSUMPTION_FAILURE` with `rho(B)=1` |
| R008 | M4 | Capacity falsification | Base OD demand scaled by `s=2.10` | stress | MFD capacity margin, checker classification | MUST | TODO | Expected label `ASSUMPTION_FAILURE`; `Lambda_2=Lambda_3=0.903>0.90` |
| R009 | M4 | Local-region falsification | Base plan with far initial error `(+8,-2,+8)` | stress | saturation fraction, checker classification | MUST | TODO | Expected label `OUTSIDE_LOCAL_REGION` |
| R010 | M5 | Sampled-hold check | Euler sampled update with `Delta t={0.05,0.10,0.25,0.50}` | engineering | `rho(I+A Delta t)`, step sensitivity | NICE | TODO | Mandatory only if final implementation uses sampled control |
| R011 | M6 | Final audit | All completed runs | report | L0-L6 pass matrix, labels, artifact paths | MUST | TODO | Should not count stress runs as theorem support |
