# Reproducibility protocol

## Scope

This repository is a DSD-assisted proof-audit and computational bridge for the 3D incompressible Navier–Stokes problem on `R^3`.

The executable layers currently check:

1. analytic Gaussian benchmark formation and shell diagnostics;
2. typed undefined versus defined-zero radial states;
3. pressure, vorticity, and scale-aware channel identities;
4. vortex-stretching sign separation and pressure closure;
5. translation completeness and nonlinear cross coupling;
6. critical `L3` pressure-rate behavior;
7. shell-to-ball coarea reconstruction and parabolic scaling.

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
python src\critical_channel_baseline.py --output-dir results
python src\translation_coupling_baseline.py --output-dir results
python src\critical_l3_rate_baseline.py --output-dir results
python src\coarea_local_bridge.py --output-dir results
python -m unittest discover -s tests -v
```

The first, critical-channel, translation/coupling, and coarea layers combine exact symbolic identities with deterministic finite/numerical checks. The `critical_l3_rate_baseline.py` pressure sign audit uses FFT-based Poisson inversion on a large rapidly decaying numerical window; those sign results are therefore explicitly labeled **COMPUTATIONAL CHECK**.

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
results/critical_channel_baseline.*
results/translation_coupling_baseline.*
results/critical_l3_rate_baseline.*
results/coarea_local_bridge.*
```

## Interpretation levels

- **DERIVED IDENTITY** — exact algebra/calculus from stated smooth hypotheses.
- **COMPUTATIONAL CHECK** — deterministic symbolic/numerical reproduction of a displayed benchmark.
- **BRIDGE DEFINITION** — application-specific DSD/NS dictionary.
- **CONJECTURE / TARGET** — proposed quantity or inequality not yet proved.
- **OPEN PROOF OBLIGATION** — a step required before any global-regularity claim.
- **FAILED-ROUTE CANDIDATE** — a route contradicted computationally but not yet certified as a theorem-level negative result.
- **FAILED ROUTE** — analytically or rigorously excluded.

## Claim boundary

The centered benchmark must ultimately be replaced by arbitrary admissible smooth divergence-free data. Any candidate DSD descriptor must either control a known regularity-sufficient quantity or come with a new proved regularity implication. Numerical persistence, finite-time stability, or equality of a scalar aggregate is never promoted to a global theorem.
