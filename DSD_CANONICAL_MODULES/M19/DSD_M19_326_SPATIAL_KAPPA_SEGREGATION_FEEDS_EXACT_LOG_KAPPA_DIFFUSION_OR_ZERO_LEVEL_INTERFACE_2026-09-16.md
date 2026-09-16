# M19-326 — Spatial kappa segregation feeds exact log-kappa diffusion or the zero-level interface branch

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / M19-324 TO M17-394 BRIDGE / SIGN-PRESERVING COEFFICIENT CURRENT / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

M19-324 gives, on the spatial CE-H variance branch, two vortex-line coefficient populations of fixed positive line measure separated by a fixed coefficient gap. On a uniformly connected own-scale weighted-Poincare component,

\[
\boxed{
\int \rho^2|\nabla_\perp\kappa|^2dx
\ge c_{\nabla\kappa}>0.
}
\]

Exact CE-H gives

\[
D_\xi\kappa=0,
\]

so all coefficient transition is transverse.

M17-394 gives on every connected sign-preserving CE-H spacetime region

\[
\boxed{
D_t\log|\kappa|
=
L_\rho\log|\kappa|
+|\nabla\log|\kappa||^2
+\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa},
}
\]

with

\[
L_\rho f=\rho^{-2}\nabla\cdot(\rho^2\nabla f).
\]

## 2. Sign-changing versus sign-preserving segregation

There are two possibilities for the two coefficient-separated line populations from M19-324.

### A. Zero-level separation

If any connected transition from one population to the other crosses

\[
\kappa=0,
\]

then the logarithmic coordinate is not admissible through the transition. This is not a failure of the method: it is exactly the zero-level branch already typed by M17-323/326/338--346.

Thus

\[
\boxed{
\mathcal G_{zero/level/interface}
}
\]

is an explicit canonical exit.

### B. Sign-preserving separation

Otherwise the relevant connected transition lies inside one region of fixed sign of \(\kappa\). Then M17-394 applies.

## 3. Fixed transverse kappa-gradient implies fixed log-kappa diffusion

Compactness gives a uniform coefficient ceiling

\[
|\kappa|\le M_\kappa.
\]

On the sign-preserving set,

\[
|\nabla\log|\kappa||^2
=
\frac{|\nabla\kappa|^2}{|\kappa|^2}
\ge
\frac1{M_\kappa^2}|\nabla\kappa|^2.
\]

Since \(D_\xi\kappa=0\),

\[
|\nabla\kappa|=|\nabla_\perp\kappa|.
\]

Therefore M19-324 yields

\[
\boxed{
D_{\log\kappa}
:=
\int \rho^2|\nabla\log|\kappa||^2dx
\ge
\frac{c_{\nabla\kappa}}{M_\kappa^2}
=:c_{\log\kappa}>0.
}
\]

Thus the spatial coefficient-variance branch is not merely a geometric gradient statement. On a sign-preserving connected component it feeds directly into the positive diffusion density of the exact M17-394 coefficient evolution law.

## 4. The exact coefficient-current interpretation

Write

\[
z_\kappa:=\log|\kappa|.
\]

Then

\[
D_t z_\kappa
-
L_\rho z_\kappa
=
|\nabla z_\kappa|^2
+
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
\]

The M19-324 line segregation therefore requires a fixed positive spatial diffusion density

\[
\rho^2|\nabla z_\kappa|^2
\]

unless it exits through zero/interface or geometric decompactification.

There is no independent longitudinal coefficient current because

\[
D_\xi\kappa=0.
\]

The coefficient current is a transverse weighted-diffusion/source balance.

## 5. Materially integrated balance

For a smooth material cutoff \(\chi\), M17-394 gives

\[
\begin{aligned}
\frac d{dt}
\int\chi\rho^2z_\kappa dx
={}&
\int\chi\rho^2|\nabla z_\kappa|^2dx\\
&-
\int\rho^2\nabla\chi\cdot\nabla z_\kappa dx\\
&+
\int\chi\rho^2
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}dx\\
&+
2\int\chi\rho^2(\sigma+\kappa)z_\kappa dx.
\end{aligned}
\]

Hence a persistent positive log-diffusion payment can be recycled by

1. cutoff/interface flux;
2. normalized strain/geometric source;
3. amplitude-growth weighting;
4. state-observable change.

Therefore the positive diffusion term is not by itself monotone.

## 6. New canonical split

Combining M19-324 with M17-394 gives

\[
\boxed{
\mathcal T_{\kappa}^{spatial}
\Longrightarrow
\mathcal G_{zero/level/interface}
\lor
\mathcal G_{transverse-size/neck}
\lor
\mathcal D_{\log\kappa}^{+},
}
\]

where

\[
\mathcal D_{\log\kappa}^{+}:
\quad
\int\rho^2|\nabla\log|\kappa||^2dx
\ge c_{\log\kappa}>0
\]

on a sign-preserving uniformly connected own-scale component.

M17-394 then refines the last branch to

\[
\boxed{
\mathcal D_{\log\kappa}^{+}
\leadsto
\text{coefficient diffusion/source/cutoff/amplitude balance}.
}
\]

## 7. Accumulation firewall

The new log-diffusion lower bound remains a fixed normalized unsigned payment. M19-317 and M18-058--059 show that ordinary recurrence gives only order-one multiplicity in a fixed normalized record cell, whereas an ancestral contradiction needs essentially record-linear multiplicity.

Thus

\[
\boxed{
\mathcal D_{\log\kappa}^{+}
\not\Rightarrow
\text{global contradiction}.
}
\]

The value of M19-326 is structural: the spatial coefficient-variance branch has now been connected to an exact PDE current. The remaining issue is whether the source/cutoff/amplitude compensation can persist recurrently without producing a signed non-coboundary current, a record-linear multiplicity, or an already typed exit.

## 8. Conclusion

The M19-322 spatial variance is no longer an isolated spectral statistic. Exact CE-H line constancy and M17-394 give the chain

\[
\boxed{
\text{spectral width}
\to
\text{kappa variance}
\to
\text{two transverse line populations}
\to
\text{log-kappa diffusion or zero/interface/geometry exit}.
}
\]

\[
\boxed{
\text{M19-326 COMPLETE; NEXT TARGET: AUDIT THE COMPENSATING SOURCE TERMS IN THE LOG-KAPPA MATERIAL BALANCE.}
}
\]
