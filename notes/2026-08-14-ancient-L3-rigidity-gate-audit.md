# Ancient L3 rigidity gate audit

Date: 2026-08-14

Status: exact local Gaussian H1-to-L3 estimate + identification of the missing critical gain.

Albritton--Barker, 'On local Type I singularities of the Navier--Stokes equations and Liouville theorems' (JMFM 2019, arXiv:1811.00502), Theorem 1.2 states that a mild ancient solution with uniformly bounded global L3 norm along a sequence of times tending to minus infinity is identically zero.

For the self-consistent Gaussian residual velocity `r`, Gaussian Poincare gives at radius `R`

\[
\int\gamma_R|r|^2\lesssim R^2B,
\qquad
\int\gamma_R|\nabla r|^2=B.
\]

On a fixed multiple of the Gaussian ball, the density is comparable to `R^{-3}`, so

\[
\|r\|_{L^2(B_{CR})}^2\lesssim R^5B,
\qquad
\|\nabla r\|_{L^2(B_{CR})}^2\lesssim R^3B.
\]

The local Sobolev inequality gives

\[
\|r\|_{L^6(B_{CR})}\lesssim R^{3/2}\sqrt B.
\]

Interpolating L2 and L6,

\[
\boxed{
\|r\|_{L^3(B_{CR})}
\lesssim R^2\sqrt B.
}
\]

Therefore a uniform scale-critical L3 bound would follow from

\[
\boxed{BR^4\lesssim1.}
\]

The current finite-energy Hermite barrier only gives the low-curvature ridge

\[
BR^5\lesssim W^{1/2}.
\]

Thus the present estimates fall short of the ancient-L3 Liouville gate by one spatial power.

On the surviving parameterization

\[
m=W^{-1/3}\Lambda,
\qquad
R\lesssim W^{1/6}\Lambda^{-1/5},
\]

the available local-L3 estimate at the maximal radius is

\[
R^2\sqrt m
\lesssim
W^{1/6}\Lambda^{1/10},
\]

which is not uniformly bounded by the current argument.

Hence the Albritton--Barker theorem cannot yet be invoked directly. A proof-producing compactness route needs one of:

1. an additional `1/R` gain converting `BR^5` to the critical `BR^4` scale;
2. a spatial tightness mechanism yielding global L3 control by another route;
3. a different rigidity theorem adapted to the Gaussian/Hermite residual state.

This audit prevents overclaiming the ancient-limit route and identifies the exact missing critical-velocity gain.
