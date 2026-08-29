# DSD M5-224 — Positive Log-Radial Homogeneity-Defect Mean and Abel Residue

Date: 2026-08-30

Parent: `DSD_M5_219_TAIL_CONJUGACY_NO_SHORT_RETURN_TO_LOG_RADIAL_PHASE_ACTION_2026-08-30.md`

Status: **POSITIVE CRITICAL RESIDUE / THE FINITE-ANNULUS HOMOGENEITY-DEFECT WITNESS FROM TAIL CONJUGACY OCCURS AT EVERY TAIL-TRANSLATION TIME IN ONE OF FINITELY MANY CELLS / FUBINI CONVERTS THIS TO A STRICTLY POSITIVE LOWER CESARO DENSITY OF `|partial_y Phi|^3` ALONG LOG RADIUS / THE CORRESPONDING ABEL-MELLIN CRITICAL RESIDUE OF `H_T=T+Y dot grad T` IS STRICTLY POSITIVE AND DILATION-INVARIANT / NO FINITE PHYSICAL BUDGET FOR THIS RESIDUE IS CLAIMED / GLOBAL REGULARITY UNPROVED.**

---

## 1. M5-219 finite-cell input

Write the canonical tail as

\[
T(r\theta)=r^{-1}\Phi(y,\theta),
\qquad y=\log r.
\]

M5-219 gives fixed constants

\[
h_*>0,
\qquad
N_*<\infty,
\]

and finitely many fixed enlarged log intervals

\[
J_1,\ldots,J_{N_*}
\]

such that for every tail-translation time `s` there is at least one `m=m(s)` with

\[
\boxed{
\int_{J_m\times S^2}
|\partial_y\Phi_s(y,\theta)|^3
\,dy\,d\theta
\ge h_*,
}
\]

where the exact tail flow is

\[
\boxed{
\Phi_s(y,\theta)
=
\Phi_0(y-s/2,\theta).
}
\]

By summing over all finite cells, one obtains the pointwise-in-time inequality

\[
\boxed{
\sum_{m=1}^{N_*}
\int_{J_m\times S^2}
|\partial_y\Phi_0(y-s/2,\theta)|^3
\,dy\,d\theta
\ge h_*
}
\]

for every `s` on the complete minimal orbit.

---

## 2. Define the log-radial defect density

Set

\[
\boxed{
g(y)
:=
\int_{S^2}
|\partial_y\Phi_0(y,\theta)|^3d\theta
\ge0.
}
\]

The W1 local derivative bounds imply that `g` is locally bounded and, on the compact tail hull, uniformly bounded on translated unit cells.

The finite-cell inequality is

\[
\boxed{
\sum_{m=1}^{N_*}
\int_{J_m}g(y-s/2)dy
\ge h_*.
}
\]

Let

\[
L_J
:=
\sum_{m=1}^{N_*}|J_m|<\infty,
\]

and choose finite numbers `a<b` containing every `J_m`.

---

## 3. Integrate over translation time

Integrate the finite-cell inequality over

\[
0\le s\le S.
\]

Then

\[
h_*S
\le
\sum_m
\int_{J_m}
\int_0^Sg(y-s/2)ds\,dy.
\]

For fixed `y`,

\[
\int_0^Sg(y-s/2)ds
=
2\int_{y-S/2}^{y}g(z)dz.
\]

Hence

\[
\begin{aligned}
h_*S
&\le
2\sum_m
\int_{J_m}
\int_{y-S/2}^{y}g(z)dz\,dy\\
&\le
2L_J
\int_{a-S/2}^{b}g(z)dz.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_{a-S/2}^{b}g(z)dz
\ge
\frac{h_*}{2L_J}S.
}
\]

---

## 4. Strictly positive lower Cesaro mean

The interval length is

\[
(b-a)+S/2.
\]

Dividing by it and sending `S->infinity` gives

\[
\boxed{
\liminf_{S\to\infty}
\frac{1}{S/2+(b-a)}
\int_{a-S/2}^{b}g(z)dz
\ge
\frac{h_*}{L_J}>0.
}
\]

After translating the origin in `y`, this may be stated as a backward log-radius mean:

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int_{-L}^{0}g(y)dy
\ge c_H>0.
}
\]

Because the minimal tail flow is complete and the same argument may be applied to reversed orbit segments, an analogous positive lower mean is available in the opposite log-radius direction as well:

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int_{0}^{L}g(y)dy
\ge c_H'>0
}
\]

with fixed positive constants after harmless changes of cell endpoints.

Thus the homogeneity defect is not a sparse collection of exceptional scales.

It occupies a positive fraction of logarithmic scale.

---

## 5. Physical critical homogeneity-defect density

Recall

\[
\boxed{
\mathcal H_T
:=T+Y\cdot\nabla T
=
\frac1r\partial_y\Phi.
}
\]

On a spherical shell,

\[
|\mathcal H_T|^3dx
=
\frac1{r^3}|\partial_y\Phi|^3
r^2dr\,d\theta
=
|\partial_y\Phi|^3\frac{dr}{r}d\theta.
\]

Therefore for

\[
1<r<e^L,
\]

one has exactly

\[
\boxed{
\int_{1<|Y|<e^L}
|\mathcal H_T(Y)|^3dY
=
\int_0^Lg(y)dy.
}
\]

Consequently

\[
\boxed{
\liminf_{L\to\infty}
\frac1L
\int_{1<|Y|<e^L}
|\mathcal H_T|^3dY
\ge c_H'>0.
}
\]

The aperiodic/minimal tail therefore carries a strictly positive **critical cubic homogeneity-defect density per logarithmic scale**.

---

## 6. Abel/Mellin form

Define for `epsilon>0`

\[
\boxed{
\mathscr A_H(\varepsilon;T)
:=
\varepsilon
\int_{|Y|>1}
|\mathcal H_T(Y)|^3
|Y|^{-\varepsilon}dY.
}
\]

In log radius,

\[
\boxed{
\mathscr A_H(\varepsilon;T)
=
\varepsilon
\int_0^\infty
 e^{-\varepsilon y}g(y)dy.
}
\]

The positive lower Cesaro mean and the standard Abel--Cesaro implication for nonnegative locally bounded functions give

\[
\boxed{
\liminf_{\varepsilon\downarrow0}
\mathscr A_H(\varepsilon;T)
\ge c_H'>0.
}
\]

Define the lower homogeneity-defect Abel residue

\[
\boxed{
\underline{\mathscr R}_H(T)
:=
\liminf_{\varepsilon\downarrow0}
\varepsilon
\int_{|Y|>1}
|T+Y\cdot\nabla T|^3
|Y|^{-\varepsilon}dY.
}
\]

Then every surviving aperiodic minimal tail satisfies

\[
\boxed{
\underline{\mathscr R}_H(T)>0.
}
\]

---

## 7. Dilation invariance of the residue

Let

\[
T_h=D_hT.
\]

Then in log variables

\[
g_h(y)=g(y-h/2).
\]

A finite shift changes the Abel integral only by

- a multiplicative factor `e^{-epsilon h/2}->1`, and
- a finite endpoint interval whose contribution is killed by the leading factor `epsilon`.

Therefore

\[
\boxed{
\underline{\mathscr R}_H(D_hT)
=
\underline{\mathscr R}_H(T)
\qquad(h\in\mathbb R).
}
\]

Thus the lower Abel residue is a genuine invariant of the compact tail flow.

By M5-218 conjugacy, it is also a W1 invariant on the corresponding minimal set.

---

## 8. Relation to exact homogeneity and DSS

If the tail is exactly degree `-1` homogeneous,

\[
\partial_y\Phi=0,
\]

so

\[
\underline{\mathscr R}_H=0.
\]

A nonconstant log-periodic tail instead has

\[
\underline{\mathscr R}_H>0
\]

unless it is constant almost everywhere in phase.

Likewise the aperiodic minimal branch derived above has strictly positive residue.

Hence the residue detects **nontrivial scale-phase motion**, not aperiodicity by itself.

It separates exact self-similarity from both DSS and genuinely aperiodic scale dynamics.

---

## 9. No finite-budget conclusion

The physical integrand is critical:

\[
|\mathcal H_T|^3dx
\sim
\frac{dr}{r}.
\]

Therefore a positive residue represents one fixed dimensionless payment per logarithmic generation.

It is not presently controlled by finite physical kinetic energy or ordinary viscous dissipation.

Thus

\[
\boxed{
\underline{\mathscr R}_H>0
\not\Rightarrow
\text{contradiction}.
}
\]

Its value is as a sharp classification/invariant for the final branch.

---

## 10. Updated final endpoints

The current nonstationary W1 scale dynamics can now be labeled by an actual critical invariant:

\[
\boxed{
\underline{\mathscr R}_H>0.
}
\]

Combining M5-220--M5-223, the remaining endpoints are

\[
\boxed{
R_{tail}^{align/open}
\quad\lor\quad
S_{crit,large}^{nonhom},
}
\]

and the second endpoint necessarily also has

\[
\boxed{
\underline{\mathscr R}_H>0
}
\]

if it belongs to the same nontrivial minimal scale hull.

The next audit should test whether any known scale-Mellin/Pohozaev identity for stationary Navier--Stokes controls this positive residue, or whether it remains a genuinely new large-data stationary invariant.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]