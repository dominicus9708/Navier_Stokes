# Smooth Record-Component Sparseness/Thickness Gate — 2026-08-20

Status: **EXTERNAL REGULARITY GATE + SMOOTH RECORD-POINT CONTRAPOSITIVE / THICK SIGNED CORE QUANTIFIED / GLOBAL REGULARITY NOT PROVED.**

This note uses the componentwise geometric regularity framework of Bradshaw--Farhat--Grujic, *An algebraic reduction of the scaling gap in the Navier--Stokes regularity problem*, Arch. Rational Mech. Anal. (2019), arXiv:1704.05546.

The main proof remains on actual smooth first-hitting solutions. The external theorem is used only as a gate: a record point that satisfies the required component sparseness cannot support further blow-up growth.

## 1. Fixed constants from the component criterion

The paper fixes

\[
h_*
=\frac2\pi
\arcsin
\frac{1-(3/4)^{2/3}}
{1+(3/4)^{2/3}},
\]

and chooses `M_*` by

\[
\frac12h_*+(1-h_*)M_*=1.
\]

Numerically,

\[
\boxed{
h_*\approx0.06095468348,
\qquad
M_*\approx1.0324556666.
}
\]

The signed-component superlevel threshold is

\[
\boxed{
\lambda_*=\frac1{2M_*}
\approx0.4842822953.
}
\]

The relevant one-dimensional sparsity ratio is

\[
\boxed{
\delta_1=(3/4)^{1/3}
\approx0.9085602964.
}
\]

The theorem's admissible scale is comparable to the vorticity analyticity scale. For viscosity one it may be taken no larger than

\[
\rho\le
\frac1{2c(M_*)\|\omega\|_\infty^{1/2}}.
\]

After restoring viscosity and first-hitting normalization, this is a fixed normalized scale of order `sqrt(nu)/c(M_*)`.

## 2. Record-point local use of the harmonic-measure proof

The published theorem imposes the sparseness property around every spatial point in order to control the full `L-infinity` norm.

For the present first-hitting route we use only the local step of its proof at an actual component-record maximum.

Use the component norm

\[
W_\square(t)
=\max_j\|\omega_j(t)\|_\infty.
\]

Divergence of the Euclidean vorticity maximum implies divergence of `W_square`, so an infinite component first-hitting subsequence exists.

At a record point `x_*`, select the signed component `omega_j^+` or `omega_j^-` that realizes `W_square`. If the corresponding superlevel set

\[
\boxed{
V^{j,\pm}
=\{x:\omega_j^\pm(x)>\lambda_*W_\square\}
}
\]

is linearly `delta_1`-sparse along one admissible line through `x_*`, the harmonic-measure maximum-principle step gives the same local maximum suppression used in the published theorem. Such a point cannot realize the required new record growth.

Therefore a surviving component-record point must fail this local sparseness gate.

## 3. Failure of all line-sparseness forces 3D thickness

Fix an admissible radius `r` at the record point. Suppose no direction through the record point is linearly `delta_1`-sparse.

Choose one representative direction from each unoriented line, i.e. a hemisphere `H` of area `2pi`. For every `d in H`, let

\[
A_d
=\{s\in[-r,r]:x_*+sd\in V^{j,\pm}\}.
\]

Failure of linear sparsity means

\[
|A_d|>2\delta_1r.
\]

For a subset of `[-r,r]` of fixed length `2 delta_1 r`, the weighted integral of `s^2` is minimized by the centered interval. Hence

\[
\int_{A_d}s^2ds
\ge
\frac{2}{3}\delta_1^3r^3.
\]

Integrating over the hemisphere gives

\[
|V^{j,\pm}\cap B_r(x_*)|
\ge
\frac{4\pi}{3}\delta_1^3r^3.
\]

Since

\[
\delta_1^3=\frac34,
\]

we obtain the explicit thick-core alternative

\[
\boxed{
|V^{j,\pm}\cap B_r(x_*)|
\ge
\frac34|B_r|.
}
\]

Thus the survivor is not merely non-sparse in an abstract sense: at the analytic scale, at least 75 percent of the ball is occupied by one fixed signed vorticity component above level `lambda_* W_square`.

## 4. Fixed normalized enstrophy occupancy

Normalize the selected component record so that

\[
W_\square=1.
\]

On the thick superlevel set,

\[
|\Omega|^2
\ge
(\Omega_j^\pm)^2
>\lambda_*^2.
\]

Hence

\[
\boxed{
\int_{B_r}|\Omega|^2
\ge
\frac34\lambda_*^2|B_r|
=
\pi\lambda_*^2r^3.
}
\]

Numerically,

\[
\boxed{
\pi\lambda_*^2
\approx0.7368589.
}
\]

So the non-sparse record branch carries an order-one normalized enstrophy packet at the analytic scale.

## 5. Same-sign thickness forces a compensating signed tail

On the smooth rapidly-decaying whole-space track,

\[
\int_{\mathbb R^3}\omega_j(x,t)dx=0
\]

for each component, because `omega=curl u` and the boundary term at infinity vanishes.

Assume for concreteness that the selected sign is positive. Inside `B_r`, on at least three quarters of the volume,

\[
\Omega_j>\lambda_*,
\]

while everywhere

\[
\Omega_j\ge-1
\]

under the component normalization. Therefore

\[
\begin{aligned}
\int_{B_r}\Omega_jdx
&\ge
\lambda_*\frac34|B_r|
-1\cdot\frac14|B_r|\\
&=
\frac{3\lambda_*-1}{4}|B_r|.
\end{aligned}
\]

Since `lambda_*>1/3`, this is strictly positive. Define

\[
\boxed{
c_F=\frac{3\lambda_*-1}{4}
\approx0.1132117215.
}
\]

Then

\[
\boxed{
\left|\int_{B_r}\Omega_jdx\right|
\ge
c_F|B_r|
\approx0.4742201499\,r^3.
}
\]

The whole-space zero-mean identity forces an opposite-signed compensator outside the ball:

\[
\boxed{
\int_{B_r^c}\Omega_j^-dx
\ge
c_F|B_r|
}
\]

for the positive-core case, with the analogous statement after reversing signs.

## 6. Annulus-or-remote compensator dichotomy

Take the annulus

\[
A_r=B_{2r}\setminus B_r.
\]

Either at least one half of the compensating signed `L1` mass lies in `A_r`, or at least one half lies outside `B_{2r}`.

### Local compensator

If

\[
\int_{A_r}\Omega_j^-dx
\ge
\frac12c_F|B_r|,
\]

Cauchy--Schwarz gives

\[
\int_{A_r}|\Omega|^2dx
\ge
\frac{(c_F|B_r|/2)^2}{|A_r|}.
\]

Since

\[
|A_r|=7|B_r|,
\]

we get

\[
\boxed{
\int_{A_r}|\Omega|^2dx
\ge
\frac{c_F^2}{28}|B_r|
\approx0.00191740284\,r^3.
}
\]

This is a fixed annular opposite-sign occupancy and feeds the bounded-radius turnover/polarity branch.

### Remote compensator

Otherwise

\[
\boxed{
\int_{|x-x_*|>2r}\Omega_j^-dx
\ge
\frac12c_F|B_r|
\approx0.2371100749\,r^3.
}
\]

The record core then necessarily carries a fixed opposite-signed remote tail. This may be dynamically passive, but it cannot be removed from the smooth whole-space bookkeeping.

## 7. Cross-sectional flux consequence

The positive total component integral inside `B_r` also implies, by Fubini, that there exists a cross-section perpendicular to `e_j` for which the normalized signed component flux through the disk is at least

\[
\boxed{
\Phi_{disk}
\ge
\frac{c_F|B_r|}{2r}
=
\frac{2\pi c_F}{3}r^2
\approx0.2371100749\,r^2.
}
\]

Under first-hitting parabolic scaling, vorticity flux through a two-dimensional section is scale invariant. Thus the thick branch supplies a genuine material-flux object to the previously derived oriented-flux/material-tube ledger.

## 8. Current proof role

The large analytic-scale core is now split without leaving the smooth class:

\[
\boxed{
\text{record component sparse at analytic scale}
\Longrightarrow
\text{harmonic-measure regularity gate},
}

or

\[
\boxed{
\text{not sparse}
\Longrightarrow
\text{75 percent thick signed core}
+\text{fixed compensating signed tail}.
}
\]

The thick branch further splits into a nearby opposite-sign annular packet (turnover/polarity) or a remote compensating tail. The next direct task is to combine the scale-invariant cross-sectional flux with the smooth finite-stage deformation/diffusion ledger.

Status: **A SURVIVING RECORD CORE THAT EVADES THE KNOWN COMPONENT-SPARSENESS REGULARITY MECHANISM MUST BE QUANTITATIVELY THICK: ONE SIGNED COMPONENT OCCUPIES AT LEAST THREE QUARTERS OF AN ANALYTIC-SCALE BALL ABOVE LEVEL `lambda_* ~= 0.4843`. WHOLE-SPACE VORTICITY CANCELLATION THEN FORCES A FIXED OPPOSITE-SIGNED ANNULAR OR REMOTE COMPENSATOR.**