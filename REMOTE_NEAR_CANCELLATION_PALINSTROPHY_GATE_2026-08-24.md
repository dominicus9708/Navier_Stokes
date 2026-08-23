# Remote/Near Cancellation -> Palinstrophy Gate — 2026-08-24

Status: **EXPLICIT NONUNIFORM-CANCELLATION PALINSTROPHY TAX / FINITE-STAGE CLOSURE TEST / GLOBAL REGULARITY NOT PROVED.**

This note follows `CANONICAL_WEIGHTED_AFFINE_COVARIANCE_OPERATOR_2026-08-24.md`.

A large remote affine strain that is uniformly canceled by the local field is not, by itself, an obstruction: the total local dynamics only sees the sum.  A derivative tax is required only when the cancellation succeeds at the affine/mean level but fails spatially across a substantial part of the thick core.

---

## 1. Fixed-axis transverse strain on a thick core

Fix a reference unit core axis `xi_*` during an interval on which axis tilt is below the already typed projective threshold.  Set

\[
P_*=I-\xi_*\otimes\xi_*.
\]

For the full normalized strain `Sigma`, define the fixed-axis transverse trace-free tensor

\[
\boxed{
\mathcal D(y,s)
=\operatorname{dev}_{\xi_*^\perp}
\big(P_*\Sigma(y,s)P_*\big).
}
\]

Because the projection is a constant orthogonal linear map,

\[
|\nabla\mathcal D|
\le |\nabla\Sigma|.
\]

Let `B_r` be a normalized thick-core ball and let

\[
\bar{\mathcal D}_r(s)
=|B_r|^{-1}\int_{B_r}\mathcal D(y,s)dy.
\]

Let `D_rem(s)` denote the leading remote affine transverse trace-free strain on the same core, and set

\[
d(s)=|D_{rem}(s)|_F.
\]

The non-affine variation of the remote harmonic field across `B_r` is excluded from `D_rem` and belongs to the already typed remote non-affine/residual lane.

---

## 2. Three-way cancellation split

Fix constants

\[
0<\eta<\beta<1,
\qquad
0<\theta\le1.
\]

At a time with `d(s)>0`, there are three relevant cases.

### A. transmitted mean strain

\[
\boxed{
|\bar{\mathcal D}_r(s)|_F\ge\eta d(s).
}
\]

Then a fixed fraction of the remote affine magnitude survives in the actual total transverse strain at core-average level.  This belongs to the transmitted affine/covariance/projective lane.

### B. uniform neutralization

Suppose

\[
|\bar{\mathcal D}_r(s)|_F<\eta d(s)
\]

and the set on which the total transverse strain remains at least `beta d(s)` has volume fraction less than `theta`.

Then the large remote affine component has been canceled on most of the thick core.  It is **neutralized/passive** at this leading transverse order.  No derivative tax is claimed or needed merely from the existence of two large opposite scale-decomposed pieces.

### C. nonuniform cancellation

Suppose

\[
\boxed{
|\bar{\mathcal D}_r(s)|_F<\eta d(s)
}
\]

but there is a measurable set

\[
E_s\subset B_r,
\qquad
|E_s|\ge\theta|B_r|
\]

such that

\[
\boxed{
|\mathcal D(y,s)|_F\ge\beta d(s)
\quad(y\in E_s).
}
\]

Then the cancellation is necessarily spatially nonuniform.

---

## 3. Ball Poincare forces strain-gradient energy

On `E_s`,

\[
|\mathcal D-\bar{\mathcal D}_r|_F
\ge
(\beta-\eta)d(s).
\]

Therefore

\[
\boxed{
\int_{B_r}
|\mathcal D-\bar{\mathcal D}_r|_F^2dy
\ge
\theta|B_r|(\beta-\eta)^2d(s)^2.
}
\]

For the Euclidean ball, Payne-Weinberger gives

\[
\int_{B_r}|F-F_{B_r}|^2
\le
\frac{4r^2}{\pi^2}
\int_{B_r}|\nabla F|^2.
\]

Hence

\[
\theta|B_r|(\beta-\eta)^2d(s)^2
\le
\frac{4r^2}{\pi^2}
\int_{B_r}|\nabla\mathcal D|^2.
\]

Since

\[
|\nabla\mathcal D|\le|\nabla\Sigma|,
\]

and for a smooth rapidly decaying divergence-free field

\[
\boxed{
\|\nabla\Sigma\|_2^2
=\frac12\|\nabla\Omega\|_2^2
=\frac12Q,
}
\]

we obtain

\[
\boxed{
Q(s)
\ge
C_{can}\,r\,d(s)^2,
}
\]

where

\[
\boxed{
C_{can}
=
\frac{2\pi^3}{3}
\theta(\beta-\eta)^2.
}
\]

This is the pointwise-in-normalized-time palinstrophy tax for nonuniform cancellation.

---

## 4. Remote action form

Let `J` be a subinterval on which the nonuniform-cancellation conditions hold and define the remote transverse action

\[
A_{rem}(J)
=\int_J d(s)ds.
\]

Integrating the preceding estimate and using Cauchy-Schwarz,

\[
\int_Jd(s)^2ds
\ge
\frac{A_{rem}(J)^2}{|J|},
\]

so

\[
\boxed{
\int_JQ(s)ds
\ge
C_{can}\,r\,
\frac{A_{rem}(J)^2}{|J|}.
}
\]

If `J subset I_j`, then `|J|<=L_j`, hence any fixed action

\[
A_{rem}(J)\ge a_0>0
\]

forces

\[
\boxed{
\int_{I_j}Q\,ds
\ge
C_{can}\,r\,\frac{a_0^2}{L_j}.
}
\]

Thus hiding a fixed remote action through spatially nonuniform local cancellation becomes increasingly expensive on a short first-hitting stage.

---

## 5. Combine with the exact normalized enstrophy budget

On the existing vorticity-tight first-hitting stage,

\[
Z=\|\Omega\|_2^2,
\qquad
Q=\|\nabla\Omega\|_2^2,
\]

and the smooth enstrophy gate gives

\[
\boxed{
\nu\int_{I_j}Qds
\le
A_ZL_j+B_Z,
}
\]

with

\[
\boxed{
A_Z=\frac{Z_+}{\sqrt2},
}
\]

and

\[
\boxed{
B_Z
=\frac12(Z_+-Z_-)
-\frac{Z_-}{4}\log q.
}
\]

The lower and upper palinstrophy bounds can coexist only if

\[
\boxed{
\nu C_{can}r\frac{a_0^2}{L_j}
\le
A_ZL_j+B_Z.
}
\]

Equivalently,

\[
\boxed{
A_ZL_j^2+B_ZL_j
-\nu C_{can}ra_0^2
\ge0.
}
\]

Since `A_Z>0`, a fixed nonuniform-cancellation action requires

\[
\boxed{
L_j\ge L_{can,min}
:=
\frac{-B_Z+
\sqrt{B_Z^2+4A_Z\nu C_{can}ra_0^2}}
{2A_Z}.
}
\]

This is directly analogous to the existing thick-core material-flux minimum-time gate.

---

## 6. Direct finite-stage S-closure certificate

If the pure moving-ball variance corridor supplies

\[
L_j\le L_{var}
\]

and

\[
\boxed{
L_{var}<L_{can,min},
}
\]

then a stage carrying remote transverse action `a0` cannot hide that action through nonuniform near-field cancellation while remaining on the vorticity-tight smooth corridor.

It must leave through one of the other typed cases:

\[
\boxed{
\text{transmitted effective strain}
\lor
\text{uniform neutralization/passivity}
\lor
T/H/\text{tail/axis residual}.
}
\]

---

## 7. Why uniform neutralization is not an unresolved obstruction

Suppose the remote component is order one, but the full transverse strain is small throughout almost all of the thick core because the local field cancels it coherently.

Then the local vorticity and covariance dynamics do **not** receive an order-one transverse forcing from that remote component.  The remote field may still exist as a scale-decomposition component, but it is no longer an active core obstruction.

Therefore the correct logical route is

\[
\boxed{
H_{remote}^{large\ component}
\not\Rightarrow
H_{remote}^{active\ obstruction}.
}
\]

Only the uncanceled/transmitted part matters to the projective/covariance dynamics.  A perfectly canceled leading affine field belongs with the previously identified passive remote-H lane.

---

## 8. Updated local-compensation tree

For a large leading remote transverse affine strain,

\[
\boxed{
D_{rem}\text{ large}
\Longrightarrow
\begin{cases}
\text{mean/effective transmission},
&\to P_V/\text{covariance lane},\\
\text{uniform cancellation},
&\to H_{remote}^{passive/neutralized},\\
\text{nonuniform cancellation},
&\to Q\text{-tax and }L_{can,min},\\
\text{axis/tail/non-affine failure},
&\to T/H/\text{residual}.
\end{cases}
}
\]

Thus `local compensation` is no longer a free-standing unquantified branch.

---

## 9. Scope

The fixed-axis hypothesis is only used to avoid differentiating a rapidly moving projector.  If the vorticity axis rotates by order one over the interval, that is already the projective/tilt branch.  On a low-tilt block, choosing `xi_*` at the block entrance gives the stated fixed linear projection, with the small axis mismatch absorbed into the existing residual thresholds.

The remote affine field is assumed approximately constant across `B_r`.  Failure of this harmonic-affine approximation means the remote field itself has order-one spatial variation across the core and belongs to the non-affine remote derivative/residual lane.

Status: **NONUNIFORM REMOTE/NEAR CANCELLATION NOW HAS AN EXPLICIT PALINSTROPHY COST `Q >= C_can r |D_rem|^2` AND A FINITE-STAGE MINIMUM TIME `L_can,min`. UNIFORM CANCELLATION IS CORRECTLY RECLASSIFIED AS NEUTRALIZATION RATHER THAN FALSELY CHARGED AS A DERIVATIVE EVENT. THE OLD `LOCAL COMPENSATION` LABEL IS THEREFORE NO LONGER AN INDEPENDENT UNTYPED OBSTRUCTION. GLOBAL REGULARITY REMAINS UNPROVED.**