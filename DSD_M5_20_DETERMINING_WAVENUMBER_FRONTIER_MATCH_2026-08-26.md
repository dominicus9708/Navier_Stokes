# DSD M5-20 — Determining-Wavenumber Frontier Match

Date: 2026-08-26

Status: **EXTERNAL-FRONTIER MATCH / M5-19 SPECTRAL FLUX FLOOR IS CONSISTENT WITH THE KNOWN DISSIPATION-WAVENUMBER BLOW-UP PICTURE / GENERAL SPECTRAL ESTIMATES ALONE DO NOT ADVANCE BEYOND THE KNOWN ENDPOINT / FUTURE WORK MUST USE W1-SPECIFIC STRUCTURE / GLOBAL REGULARITY UNPROVED.**

## 1. M5-19 recap

M5-19 showed that failure of the spectral M5 tightness forces arbitrarily high first-hitting events satisfying

\[
\boxed{
E_0^{1/2}\kappa^{-1/2}\Pi_E(\kappa,t_\kappa)
\ge c_*>0.
}
\]

Thus a singular survivor needs order-one scale-invariant energy flux at arbitrarily high wavenumbers.

## 2. Known dissipation-wavenumber picture

Determining/dissipation-wavenumber approaches to 3D Navier--Stokes define a threshold above which local high-frequency Reynolds numbers are sufficiently small for viscosity to dominate nonlinear transfer.

A representative condition has the form

\[
\lambda_p^{-1}\|u_p\|_\infty<c_0\nu
\]

for all dyadic modes above the dissipation wavenumber.

The established theory shows that loss of regularity is tied to the failure of such a finite dissipation range; the determining/dissipation wavenumber must become unbounded in a blow-up scenario.

The 2026 work of Cheskidov--Peng further refines time-average bounds for determining wavenumbers in the weak-solution/turbulence setting.

## 3. Interpretation of the M5-19 gate

At a first-hitting critical-tail event, the high-frequency flux must be at least as large as viscous removal:

\[
\Pi_E(\kappa,t_\kappa)
\ge
\nu\kappa^2E_{>\kappa}(t_\kappa).
\]

Therefore the frequency `kappa` cannot already lie safely inside a viscosity-dominated dissipation range.

Schematically,

\[
\boxed{
\text{M5 first-hitting tail event at }\kappa
\Longrightarrow
\Lambda_{diss}(t_\kappa)\gtrsim\kappa.
}
\]

This is not claimed as a new sharp theorem with a specific determining-wavenumber definition; it records the structural match between the project-specific flux gate and the established spectral regularity framework.

## 4. DSD audit consequence

This comparison prevents a false claim of novelty.

The chain

\[
\text{high spectral tail}
\Rightarrow
\text{large high-frequency flux}
\Rightarrow
\text{dissipation wavenumber moves upward}
\]

is part of the known regularity frontier.

Therefore continuing to sharpen only generic Fourier-energy estimates is unlikely to close M5 without reproducing an already-open determining-wavenumber problem.

## 5. What W1 adds beyond the generic frontier

The project-specific survivor is not an arbitrary large high-frequency state. It also carries, under the retained W1 route,

- recurrent critical `K` boundary defect;
- cross-radius/cross-characteristic coherence;
- finite-core pressure/amplitude processing;
- intermediate-scale amplitude oscillation and `D3` cost;
- quantitative two-helicity participation when critical cascade is active;
- negligible genuinely far/infrared creation of helicity mixing.

Any future spectral step should use at least one of these additional structures.

## 6. Updated target

The next live question is no longer

> can one prove a general upper bound for the determining wavenumber?

That is essentially the original regularity problem in spectral language.

Instead ask

\[
\boxed{
\text{Can the W1 recurrent/helical/cross-radius structure force the dissipation wavenumber to fail to track the required }\kappa_j\to\infty?
}
\]

Equivalently, can one show that the special W1 cascade cannot repeatedly realize the generic high-frequency first-hitting mechanism?

No such theorem is yet proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
