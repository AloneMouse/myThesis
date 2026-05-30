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

