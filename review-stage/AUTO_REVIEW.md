# Auto Review Log

Target manuscript: `drafts/NewDraft_v1.0_20260525.tex`

Date: 2026-05-30

## Round 1

### Assessment Summary

- Score: 7/10
- Verdict: almost
- Key criticisms:
  - MFD had been generalized, but the calibrated objects were stated too narrowly.
  - The free-flow uniqueness claim needed an explicit boundary: fixed throughput, fixed control, fixed routing, free-flow branch only.
  - Multi-region stability conditions needed one consolidated local smoothness and support-invariance statement.
  - The total-outflow identity needed a support-consistency qualifier.

### Reviewer Raw Response

<details>
<summary>Click to expand full reviewer response</summary>

Score: 7/10

Verdict: almost

Critical weaknesses:

1. MFD is basically in general single-peaked form, but calibrated-object wording is inconsistent. The MFD section says only `n_I^{cr,*}` and `G_I^{max}` are needed, while later target construction, algorithms, and control require `G_{I,s}^{-1}` and evaluable `G_I(n_I)`.
2. The general single-peaked MFD supports capacity checking, free-flow target construction, and uniqueness only under fixed `\Lambda_I`, fixed `\bar u_I`, and fixed routing. The manuscript needed to avoid reading this as global equilibrium uniqueness.
3. Multi-region stability under general MFD is valid because the unsaturated law cancels `G_I(n_I)u_I` into `\Lambda_I+\kappa_Ie_I`, but the local theorem needed explicit smoothness, positivity, inactive max branch, unsaturation, and support invariance.
4. The total-outflow identity depends on support consistency and beta normalization for positive-mass components.
5. No old explicit generalized exponential MFD residue was found.

Minimum fixes:

1. State that calibrated MFD objects include `n_I^{cr,*}`, `G_I^{max}`, `G_{I,s}^{-1}`, and evaluable `G_I(n_I)`.
2. Extend algorithm input to include a queryable calibrated MFD curve/table.
3. Add a uniqueness-boundary remark.
4. Centralize local smoothness and support-invariance conditions in the multi-region stability theorem.
5. Qualify the total-outflow identity by support consistency and beta normalization.

Overall judgment: the MFD main line has moved from the old explicit form to a general single-peaked framework; after fixing the calibrated-object and local-condition interfaces it can be ready.

</details>

### Actions Taken

- Rewrote the MFD calibration remark to list all required objects: `n_I^{cr,*}`, `G_I^{max}`, `G_{I,s}^{-1}`, and evaluable `G_I(n_I)`.
- Updated the network verification algorithm input to use a queryable calibrated MFD object.
- Added a remark bounding the uniqueness theorem to the free-flow branch under fixed throughput, control, and routing.
- Tightened the local stability theorem assumptions with `C^1` local MFD, positive free-flow neighborhood, inactive max branch, unsaturation, and support-set invariance.
- Qualified the total-outflow identity by support consistency and positive-mass beta normalization.

### Result

The manuscript compiled successfully with `latexmk -xelatex`, and grep checks found no old explicit MFD residues such as `A_I`, `n_{I,cr}`, `xi_I`, `mfd_from_speed`, or `representative_length`.

## Round 2

### Assessment Summary

- Score: 8.5/10
- Verdict: ready
- Key criticisms:
  - The MFD abstraction and downstream logic were structurally sound.
  - Two polishing-level consistency fixes remained: qualify the scalar-control motivation bullet and include evaluable `G_I(\cdot)` in the simulation calibration sentence.

### Reviewer Raw Response

<details>
<summary>Click to expand full reviewer response</summary>

Score: 8.5/10

Verdict: ready

Remaining weaknesses:

1. MFD general-form logic is now acceptable. The paper no longer relies on a closed-form generalized exponential MFD; it consistently uses a calibrated single-peaked `G_I`, free-flow inverse `G_{I,s}^{-1}`, and evaluable `G_I(n_I)`.
2. Capacity check, target construction, uniqueness, control law, and local stability now close under the general MFD assumptions. The uniqueness remark correctly limits the claim to fixed `\Lambda_I`, fixed `\bar u_I`, fixed routing, and the free-flow branch.
3. No old explicit MFD residues found for `A_I`, `n_{I,cr}`, `xi_I`, `\xi_I`, `mfd_from_speed`, `representative_length`, or generalized exponential MFD references.
4. Two minor wording leftovers remain: the scalar-control motivation bullet still states the total outflow identity without repeating the support-consistency qualifier; the simulation calibration sentence says simulations only use `n_I^{cr,*}`, `G_I^{max}`, and `G_{I,s}^{-1}`, but should also include evaluable `G_I(\cdot)`.

Minimum fixes:

1. In the scalar-control motivation bullet, change the unconditional total-flow sentence to reference the qualified identity in Eq. `\ref{eq:total_outflow_identity}`.
2. In the simulation MFD calibration sentence, list `G_I(\cdot)` together with `n_I^{cr,*}`, `G_I^{max}`, and `G_{I,s}^{-1}`.

Overall judgment: the MFD abstraction and downstream logic are now structurally sound; remaining issues are polishing-level consistency, not theory blockers.

</details>

### Actions Taken

- Updated the scalar-control motivation bullet to refer to the qualified total-outflow identity.
- Added evaluable `G_I(\cdot)` to the simulation MFD calibration objects.

### Final Verification

- `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error NewDraft_v1.0_20260525.tex` completed successfully.
- Final log scan found no actual LaTeX warnings, undefined references, overfull boxes, or errors.
- Final residual scan found no old explicit MFD formula terms: `A_I`, `n_{I,cr}`, `xi_I`, `v_{f,I}`, `mfd_from_speed`, `representative_length`, `广义指数`, `显式表达`, `指数型`, or `thm:mfd_unimodal`.

## Method Description

The final manuscript uses a calibrated general single-peaked regional MFD `G_I(n_I)` rather than a displayed closed-form production function. Each region has a free-flow increasing branch and a congested decreasing branch; target equilibrium accumulations are constructed only on the free-flow branch through `\bar n_I=G_{I,s}^{-1}(\Lambda_I/\bar u_I)`.

The static SO and path-planning layers generate service flows, route proportions, macro boundary flows, and regional throughput demands `\Lambda_I`. The dynamic layer uses destination-labeled conservation equations and scalar perimeter controls `u_I` to match the static throughput target under fixed routing. Feasibility is checked by MFD capacity, free-flow target location, network conservation, transient cross-region transfer, and a local Hurwitz test for the component linearization.

## LAATDraft_v1.1 Logic Closure Review (2026-05-30)

Target manuscript: `LAATDraft_v1.1.tex` generated from `drafts/NewDraft_v1.0_20260525.tex`.

### Assessment Summary

- Score: 7/10 before fixes.
- Verdict: almost before fixes; fixed by minimal logic-closure edits.
- Key criticisms:
  - Static--dynamic bridge needed to be explicitly limited to flow-level closure, not strict equality between path-layer Little-law density and dynamic MFD target density.
  - Network feasibility algorithm returned before the Hurwitz stability check and did not take `\kappa_I` / `\epsilon_I` as inputs.
  - Bridge proof needed to avoid division by zero for zero-throughput neighbor regions.
  - Multi-region stability conclusion needed to be scoped to the static reachable support set `\mathcal S`.
  - Algorithm 1 needed executable inputs, inner-loop stopping rules, and a nonconvergence status flag.

### Actions Taken

- Wrote the revised manuscript to `LAATDraft_v1.1.tex`.
- Renamed and reframed Theorem `\ref{thm:steady_state_bridge}` as a flow-level bridge and added a density-closure residual remark.
- Added a remark clarifying that the candidate target construction is not an extra steady-state assumption.
- Restricted bridge-proof divisions by `\Lambda_H` to positive-throughput regions and introduced `\mathcal D_H^+` for zero destination-flow cases.
- Strengthened the equilibrium-existence proof for zero-throughput regions.
- Added the missing bridge-balance premise to the single-region Lyapunov lemma.
- Scoped the multi-region Hurwitz theorem conclusion to support-set errors and stated that support-set-external perturbations require fallback routing and a new `A`.
- Completed Algorithm 1 inputs/inner stopping/nonconvergence output and Algorithm 2 inputs/label/failure returns/stability output.
- Moved the external departure definition before the conservation lemma.
- Strengthened the SO convexity proposition by requiring nonnegative waiting-time functions.

### Verification

- `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error LAATDraft_v1.1.tex` completed successfully.
- Final log scan found no LaTeX warnings, undefined references, overfull boxes, or errors.

## LAATDraft_v1.2 Simplification Review (2026-05-30)

Target manuscript: `drafts/LAATDraft_v1.2_simplified.tex`.

### Assessment Summary

- Initial simplification review score: 5/10, verdict: not ready.
- Final review score after fixes: 9/10, verdict: ready.
- Main criticism before simplification: `LAATDraft_v1.1.tex` was mathematically patched but structurally over-complex, with static SO, path fixed point, destination-component dynamics, support-set logic, bridge proofs, existence/uniqueness, stability and feasibility all competing as the main model.
- Final accepted model: a minimal regional MFD closed loop using total regional accumulations `n_i(t)`, aggregate routing proportions `\beta_{ij}`, a calibrated single-peaked `G_i(n_i)`, free-flow target construction, and a scalar release controller.

### Reviewer Raw Response

<details>
<summary>Initial simplification review</summary>

Score: 5/10

Verdict: not ready

The current manuscript has many correct mathematical patches, but the main line is overloaded. It tries to simultaneously prove elastic SO, congestion-aware path fixed point, destination-component dynamics, static-dynamic bridge, existence/uniqueness, local stability, and feasibility diagnosis. Compared with Aboudolas and Geroliminis 2013, Geroliminis et al. 2013, Yildirimoglu et al. 2015, Boufous et al. 2020, and Ma and Liu 2024, mature multi-region MFD papers usually keep one narrow model as the theoretical core and move route/signal/implementation modules into algorithmic or numerical layers.

Minimum model recommendation:
- Keep regional total accumulation `n_i(t)` as the main state.
- Let static routing output aggregate boundary flows and fixed route proportions `\beta_{ij}`.
- Keep a general single-peaked MFD `G_i`.
- Use dynamics `\dot n_i=q_i^g+\sum_{j\ne i}\beta_{ji}u_jG_j(n_j)-u_iG_i(n_i)`.
- Construct targets by `\bar n_i=G_{i,s}^{-1}(\Lambda_i/\bar u_i)`.
- Use scalar release control `u_i(t)=sat((\Lambda_i+\kappa_i(n_i-\bar n_i))/max\{G_i(n_i),\epsilon_i\})`.
- Use `\rho(B)<1` to obtain the simple closed-loop error system `\dot e=(B^T-I)Ke`.

Recommended deletions or downgrades: elastic demand inverse functions, vertiport BPR waiting costs, path-density fixed point convergence proof, destination-labeled component dynamics, support consistency, fallback routing, component Jacobian main theorem, integral Lyapunov proof, congested-branch saturation recovery, and the six-experiment simulation matrix.

</details>

<details>
<summary>Final reviewer confirmation</summary>

Score: 9/10

Verdict: ready

The final reviewer confirmed that `drafts/LAATDraft_v1.2_simplified.tex` has been reduced to the desired minimal regional accumulation loop. The nonnegative-flow and non-neighbor `T_{ij}=0` conditions are explicit; `\mathcal R_+`, `B`, `K`, and the error-vector dimensions are consistent; the projection/correction note for externally provided flows is included; the local unsaturated neighborhood is closed; and the error system is correctly stated as an exact equality in that neighborhood.

The stability proof is acceptable: `\rho(B)<1` implies `I-B^T` is a nonsingular M-matrix; right multiplication by positive diagonal `K` preserves that property via the positive-vector argument; therefore `(B^T-I)K` is Hurwitz. No blockers remain. Only minor prose polishing is left.

</details>

### Actions Taken

- Created `drafts/LAATDraft_v1.2_simplified.tex` as a new minimal-model manuscript rather than overwriting `LAATDraft_v1.1.tex`.
- Reduced the main model to regional total accumulations `n_i(t)` only.
- Moved congestion-aware path search, Logit splitting, and SO/path iteration into the static aggregation layer rather than the core stability theorem.
- Defined static conservation, `\Lambda_i`, route proportions `\beta_{ij}`, completion/leaving proportions `\beta_{i0}`, and active set `\mathcal R_+`.
- Replaced the destination-component Hurwitz test with the simpler regional error system `\dot{\bm e}=(B^T-I)K\bm e`.
- Added the M-matrix proof detail showing that `(I-B^T)K` remains a nonsingular M-matrix.
- Added a minimal validation algorithm and reduced the recommended numerical study to three experiments: closed-loop stability, routing-strategy comparison, and robustness/saturation sensitivity.

### Verification

- `latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error LAATDraft_v1.2_simplified.tex` completed successfully.
- Final log scan found no LaTeX warnings, undefined references, overfull boxes, underfull boxes, or errors.

## Method Description

The simplified method uses a regional MFD network with one state per region: `n_i(t)`. Static routing aggregates OD/path decisions into nonnegative conserved flows `T_{ij}` and completion flows `T_{i0}`, producing route proportions `\beta_{ij}` and regional throughput demands `\Lambda_i`. For each active region, a control margin `\bar u_i\in(0,1)` places the target on the MFD free-flow branch via `\bar n_i=G_{i,s}^{-1}(\Lambda_i/\bar u_i)`.

The closed-loop controller is a scalar regional release law that forces the unsaturated outflow to `\Lambda_i+\kappa_i(n_i-\bar n_i)`. In the local free-flow unsaturated neighborhood, the exact error dynamics reduce to `\dot{\bm e}=(B^T-I)K\bm e`. If the inter-region route matrix `B` is substochastic and `\rho(B)<1`, then `(B^T-I)K` is Hurwitz and the target regional accumulations are locally exponentially stable.
