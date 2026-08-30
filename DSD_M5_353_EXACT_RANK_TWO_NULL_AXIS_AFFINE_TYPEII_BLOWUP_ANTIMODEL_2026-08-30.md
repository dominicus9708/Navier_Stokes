# DSD M5-353 — Exact Rank-Two Null-Axis Affine Type-II Blow-Up Anti-Model

Date: 2026-08-30

Status: **EXACT RANK-DEFICIENT AFFINE NSE ANTI-MODEL / `det grad u = 0` CAN PERSIST THROUGH FINITE-TIME DUAL-HYPERBOLIC GROWTH / LOCAL CLOCK `Theta~1` AND FINITE-ENERGY SHIELD VELOCITY TYPE-II EXPONENT `3/5` MATCH THE PREVIOUS CRITICAL BARRIERS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-352 proved that a full-rank affine material core obeys

\[
E_{aff}\ge cV^{5/3}|\det M|^{2/3}.
\]

Thus anisotropic shape deformation cannot rescue a persistent full-rank affine core under finite energy.

The only affine shape escape is

\[
\det M\approx0.
\]

This note shows that this escape is a genuine exact PDE branch, not merely a codimension-one instantaneous crossing.

## 2. Explicit ansatz

Let

\[
D:=\operatorname{diag}(2,1,-3),
\]

and let

\[
J:=
\begin{pmatrix}
0&0&1\\
0&0&0\\
-1&0&0
\end{pmatrix}.
\]

Take

\[
\boxed{
S(t)=a(t)D,
\qquad
W(t)=\sqrt6\,a(t)J.
}
\]

Set

\[
M(t)=S(t)+W(t).
\]

The affine velocity is

\[
u(x,t)=M(t)x.
\]

## 3. Exact rank deficiency

The middle axis `e_2` contributes the scalar factor `a`. In the `e_1-e_3` plane,

\[
M_{13}
=a
\begin{pmatrix}
2&\sqrt6\\
-\sqrt6&-3
\end{pmatrix}.
\]

Its determinant is

\[
-6+6=0.
\]

Hence

\[
\boxed{
\det M(t)=0
\qquad\forall t.
}
\]

The matrix has rank two whenever `a(t) != 0`.

A null vector is

\[
\boxed{
n_0=\left(-\frac{\sqrt6}{2},0,1\right).
}
\]

Thus the affine field has one exact zero-gradient direction.

## 4. Affine Navier--Stokes compatibility

M5-350 proved that the affine ansatz solves unforced NSE if

\[
W'+SW+WS=0.
\]

Because `J` acts in the `e_1-e_3` plane,

\[
DJ+JD=(2-3)J=-J.
\]

Therefore

\[
SW+WS
=
-\sqrt6\,a^2J.
\]

Also

\[
W'=\sqrt6\,a'J.
\]

Thus the skew compatibility condition is exactly

\[
\boxed{a'=a^2.}
\]

Choose

\[
\boxed{
a(t)=\frac1{T-t}.}
\]

Then `M'+M^2` is symmetric and a quadratic pressure makes `u=Mx` an exact affine Navier--Stokes solution on `t<T`.

Viscosity again vanishes because `Delta u=0`.

## 5. Dual-hyperbolic structure

The strain eigenvalues are

\[
\boxed{
\lambda_1=\frac2{T-t},
\qquad
\lambda_2=\frac1{T-t},
\qquad
\lambda_3=-\frac3{T-t}.
}
\]

The vorticity axis is `e_2`, and its amplitude is proportional to `a(t)`:

\[
\boxed{|\omega(t)|\asymp(T-t)^{-1}.}
\]

Hence

\[
(T-t)|\omega(t)|\asymp1.
\]

The local vorticity clock is therefore

\[
\boxed{\Theta\asymp1.}
\]

At the same time, covectors/gradients along `e_3` are amplified at rate `3/(T-t)`.

Thus the exact rank-two model lies precisely in the dual-hyperbolic critical-clock branch.

## 6. Natural length and finite-energy shield

Since

\[
|\omega|\asymp(T-t)^{-1},
\]

the natural vorticity length is

\[
\boxed{r(t)\asymp\sqrt{T-t}.}
\]

The saturated finite-energy affine shield radius would be

\[
\boxed{
d_{scr}(t)\asymp r^{4/5}\asymp(T-t)^{2/5}.}
\]

At this radius,

\[
|u|\asymp |M|d_{scr}
\asymp
(T-t)^{-1}(T-t)^{2/5}.
\]

Therefore

\[
\boxed{
|u|\asymp(T-t)^{-3/5}.
}
\]

Since

\[
\frac35>\frac12,
\]

this is velocity Type-II in time, exactly as required by M5-346 for an atom-bearing finite-energy shield.

## 7. Seregin boundary

For `Theta~1`, M5-348 gives

\[
f(d)\asymp d^{1/2},
\]

corresponding to

\[
\boxed{\alpha=3/2}
\]

in Seregin's power notation.

Thus the exact rank-two affine model sits simultaneously at

- the affine energy `1/5` barrier;
- the velocity Type-II `3/5` rate;
- the local vorticity critical clock `Theta~1`;
- Seregin's `alpha=3/2` Euler-scaling boundary.

These independently derived exponents are mutually consistent.

## 8. Formation/axis meaning

The null direction `n_0` is a genuine zero-gradient channel:

\[
Mn_0=0.
\]

Therefore a material region can in principle elongate strongly along `n_0` while shrinking in the two active transverse directions, preserving volume while reducing affine kinetic energy relative to a full-rank core.

This identifies the exact hard shape geometry:

\[
\boxed{
\text{rank-two active cross-section}
+\text{long null-axis filament}.
}
\]

It is no longer useful to describe the surviving shape escape generically as arbitrary anisotropy.

## 9. Firewall

Do not claim `det M=0` is only a transient crossing. The explicit solution keeps it zero for the entire affine evolution.

Do not claim positive middle strain excludes affine dynamics. Here `lambda_2>0` throughout.

The anti-model is infinite-energy and nondecaying. The remaining proof target is therefore its finite-energy truncation/ancestry, especially the length required along the null direction.

## 10. Next target

For a fixed-volume material population in a rank-two affine field, minimizing the energy requires elongation along the null axis.

The next audit should quantify the required filament length as the active singular values grow. If that length diverges beyond the parent region, the branch exits to spatial non-tightness; if it does not, finite energy forces material turnover.

## 11. Audit verdict

### PROVED

- exact rank-two affine NSE solution;
- exact persistent `det grad u=0`;
- finite-time growth `a(t)=1/(T-t)`;
- `Theta~1`, velocity Type-II exponent `3/5`, and Seregin `alpha=3/2` consistency.

### OPEN

- finite-energy null-axis filament ancestry;
- turnover versus spatial escape of the rank-two material population;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]