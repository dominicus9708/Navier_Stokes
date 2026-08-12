# Reproducibility protocol

## Scope

The current executable is a **first-pass DSD-to-Navier–Stokes bridge audit**. It checks one analytic Schwartz initial field on `R^3`, shell diagnostics, typed undefined/zero behavior, a whole-space pressure-fluctuation harmonic, and Navier–Stokes scaling identities.

It does not prove global existence, smoothness, coercivity, or a global a-priori estimate.

## Environment

Recommended:

- Python 3.11+
- SymPy 1.12+

Install:

```powershell
python -m pip install -r requirements.txt
```

## Main run

```powershell
python src\dsd_bridge_baseline.py --output-dir results
```

Expected headline:

```text
DSD/Navier-Stokes first-pass bridge: 12/12 checks passed
```

Generated outputs:

```text
results\dsd_bridge_first_pass.json
results\dsd_bridge_first_pass.md
```

## Regression tests

```powershell
python -m unittest discover -s tests -v
```

The current baseline contains six regression tests.

## Analytic seed

For

\[
\psi(x)=e^{-|x|^2},
\]

the `z`-axis benchmark is

\[
u_0=\nabla\times\nabla\times(\psi e_z).
\]

This seed is smooth, divergence-free, and rapidly decaying. It is used because it permits exact symbolic checks and closed-form shell reductions. It is a benchmark family, not a restriction on the eventual proof class.

## Claim boundary

Passing checks mean only that the displayed finite/symbolic bridge construction is reproduced. The centered benchmark must later be generalized to arbitrary admissible smooth divergence-free data, and any candidate DSD descriptor must still be connected to a mathematically sufficient regularity norm and a global a-priori estimate.
