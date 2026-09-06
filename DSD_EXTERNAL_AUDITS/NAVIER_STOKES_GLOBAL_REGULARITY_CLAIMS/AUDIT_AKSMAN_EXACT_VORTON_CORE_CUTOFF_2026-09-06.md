# DSD Audit — Aksman Exact Vorton Decomposition / Uniform Core Exclusion

Date: 2026-09-06
Source family: *Global Regularity of the 3D Incompressible Navier–Stokes Equations — A Rigorous Proof via Exact Vorton Decomposition, Uniform Core Exclusion, and the Fredholm Boundary Anchor*, June–July 2026, Zenodo family including 21169188.
Audit status: **SCALE-LIMIT / UNIVERSAL-UV-CUTOFF HINGE FAIL**

## 1. Claimed mechanism

The manuscript represents vorticity using vorton dipoles/chains and identifies a finite vortex-core radius with inter-vorton spacing. It claims a strict physical UV cutoff at the Kolmogorov microscale `δ_K`, then uses core exclusion/no-collision to obtain a uniform H1 bound on a punctured domain and passes to a regular continuum solution.

## 2. DSD object separation

Three distinct assertions must not be conflated:

1. a discrete/vorton representation has a finite spacing at a fixed discretization;
2. turbulence phenomenology defines a dissipation scale for a given flow/regime;
3. every arbitrary smooth solution of the exact classical NSE possesses a universal strictly positive lower geometric scale for all finite times.

Only (3) would close the Clay regularity problem through a UV cutoff. It is not a consequence of (1) or (2).

## 3. Fixed-cutoff dilemma

Assume the representation retains

\[
\delta_K\ge\delta_*>0
\]

uniformly through refinement.

Then the representation cannot resolve continuum variations on scales below `δ_*`. To prove density/equivalence with arbitrary classical NSE data, one must show that such sub-`δ_*` structures are never required. That statement is itself a regularity/spectral-tail theorem.

Alternatively, allow

\[
\delta_K\to0
\]

so refinement can recover arbitrary small scales. Then estimates on a punctured/core-excluded domain generally contain constants depending on the core radius, and those constants may diverge as `δ_K→0`.

Thus:

\[
\boxed{
\text{fixed cutoff}\Rightarrow\text{continuum-density problem},
\qquad
\text{vanishing cutoff}\Rightarrow\text{uniform-bound problem}.
}
\]

## 4. Punctured-domain audit

A uniform bound on

\[
\Omega_{\delta_K}=\Omega\setminus\bigcup \text{cores}
\]

is not automatically a bound on the entire domain. One must control:

- the measure/capacity of excluded cores;
- traces near core boundaries;
- concentration as cores shrink or move;
- convergence of nonlinear terms across the excluded regions.

Without those estimates, smoothness on the punctured domain does not imply global smoothness of the original continuum field.

## 5. Phenomenology audit

A Kolmogorov microscale is a physically meaningful dissipation scale in turbulence theory, but its usual formula depends on dissipation/viscosity and describes statistical/phenomenological cascades. Treating it as a theorem that forbids arbitrary exact NSE concentration below a positive scale would already solve a major part of the regularity problem and therefore requires a PDE proof independent of the regularity conclusion.

## 6. Surviving value

Potentially useful components include:

- discrete filament/vorton representations as numerical or structural models;
- geometric no-collision estimates within a fixed model;
- boundary reconstruction mechanisms;
- compactness lemmas once truly uniform estimates are available.

These remain distinct from an unconditional continuum proof.

## 7. DSD verdict

\[
\boxed{
\text{The universal positive UV cutoff is the unproved bridge.}
}
\]

The core-exclusion argument cannot simultaneously use a fixed positive cutoff to obtain uniform bounds and claim unrestricted continuum density without a theorem reconciling the two limits.

Global regularity remains unproved.
