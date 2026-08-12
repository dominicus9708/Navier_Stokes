# Reproducibility protocol

## Scope

This repository is a DSD-assisted proof-audit and computational bridge for the 3D incompressible Navier–Stokes problem on `R^3`.

The executable layers currently check:

1. analytic Gaussian benchmark formation and shell diagnostics;
2. typed undefined versus defined-zero radial states;
3. pressure, vorticity, and scale-aware channel identities;
4. moving observer spheres versus deforming material cells;
5. exact material-volume preservation and local deformation-gradient channels;
6. moving-control-volume kinetic-energy transport;
7. material pullback and boundary-geometry coupling through `F^{-T}`;
8. vortex-stretching sign separation and pressure closure;
9. translation completeness and nonlinear cross coupling;
10. critical `L3` pressure-rate behavior;
11. shell-to-ball coarea reconstruction and parabolic scaling.

Passing these checks does **not** prove global existence, smoothness, coercivity, or a global a-priori estimate.

## Environment

Recommended:

- Python 3.11+
- SymPy 1.12+
- NumPy 1.26+

Install:

```powershell
python -m pip install -r requirements.txt
```

## Deterministic runs

From the repository root on Windows:

```powershell
python src\dsd_bridge_baseline.py --output-dir results
python src\moving_material_region_baseline.py --output-dir results
python src\moving_control_energy_budget.py --output-dir results
python src\material_pullback_bridge.py --output-dir results
python src\critical_channel_baseline.py --output-dir results
python src\translation_coupling_baseline.py --output-dir results
python src\critical_l3_rate_baseline.py --output-dir results
python src\coarea_local_bridge.py --output-dir results
python src\vorticity_alignment_baseline.py --output-dir results
python src\stretching_coupling_baseline.py --output-dir results
python src\vorticity_direction_gradient_baseline.py --output-dir results
python src\middle_eigenvalue_alignment_baseline.py --output-dir results
python src\strain_alignment_gate_baseline.py --output-dir results
python src\middle_eigenvalue_growth_bound.py --output-dir results
python src\spherical_energy_budget.py --output-dir results
python src\asymmetric_spherical_budget.py --output-dir results
python -m unittest discover -s tests -v
```

The symbolic layers use exact SymPy algebra where possible. The asymmetric pressure/flux audits use FFT-based differentiation and Poisson inversion on a large rapidly decaying numerical window; those sign results are explicitly labeled **COMPUTATIONAL CHECK**.

## Moving material-region interpretation

For a smooth flow map

\[
\dot\Phi_t(a)=u(\Phi_t(a),t),
\qquad
F=D_a\Phi_t,
\]

incompressibility gives

\[
\det F=1.
\]

The repository distinguishes:

- a rigid spherical observation window whose center follows `Phi_t(a)`;
- a true material cell `Phi_t(B_ell(a))` whose shape is allowed to deform.

The latter has zero relative advective mass/kinetic-energy crossing by construction, but pressure work and viscous transport remain. Bulk integrals pull back with unit Jacobian, while boundary oriented area transforms through `F^{-T}`.

The Gaussian frozen-gradient ellipsoid is only a local initial deformation witness. It is not a numerical Navier–Stokes time integration.

## Analytic benchmark

For

\[
\psi(x)=e^{-|x|^2},
\]

the axis benchmarks are

\[
u_0^{(a)}=\nabla\times\nabla\times(\psi e_a),
\qquad a\in\{x,y,z\}.
\]

They are smooth, divergence-free, and rapidly decaying. They are diagnostic families, not restrictions on the eventual proof class.

## Output families

Committed or generated outputs include:

```text
results/dsd_bridge_first_pass.*
results/moving_material_region_baseline.*
results/moving_control_energy_budget.*
results/material_pullback_bridge.*
results/critical_channel_baseline.*
results/translation_coupling_baseline.*
results/critical_l3_rate_baseline.*
results/coarea_local_bridge.*
```

## Interpretation levels

- **DERIVED IDENTITY** — exact algebra/calculus from stated smooth hypotheses.
- **DERIVED KINEMATIC BRIDGE** — exact flow-map/control-volume reformulation while a smooth flow map exists.
- **COMPUTATIONAL CHECK** — deterministic symbolic/numerical reproduction of a displayed benchmark.
- **BRIDGE DEFINITION** — application-specific DSD/NS dictionary.
- **LOCAL MODEL** — frozen-gradient or finite witness used for structural visualization, not a solved PDE trajectory.
- **CONJECTURE / TARGET** — proposed quantity or inequality not yet proved.
- **OPEN PROOF OBLIGATION** — a step required before any global-regularity claim.
- **FAILED-ROUTE CANDIDATE** — a route contradicted computationally but not yet certified as a theorem-level negative result.
- **FAILED ROUTE** — analytically or rigorously excluded.

## Claim boundary

The centered benchmark must ultimately be replaced by arbitrary admissible smooth divergence-free data. The moving-material representation removes fixed-origin bias but does not itself reduce the quantifier over all positions/scales or provide an a-priori bound. Any candidate DSD descriptor must either control a known regularity-sufficient quantity or come with a new proved regularity implication. Numerical persistence, finite-time stability, or equality of a scalar aggregate is never promoted to a global theorem.
