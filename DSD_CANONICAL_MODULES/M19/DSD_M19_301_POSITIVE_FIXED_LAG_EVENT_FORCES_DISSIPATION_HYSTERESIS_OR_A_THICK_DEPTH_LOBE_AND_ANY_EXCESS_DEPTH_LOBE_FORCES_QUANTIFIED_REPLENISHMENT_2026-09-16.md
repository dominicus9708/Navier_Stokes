# M19-301 — A positive fixed-lag event forces dissipation, hysteresis, or a thick depth lobe; any excess depth lobe forces quantified replenishment

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE REDUCTION / QUANTITATIVE THREE-WAY DICHOTOMY / DEPTH-REPLENISHMENT GATE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Positive conditioned event

On the fixed-lag overlap block choose the smooth production marker `m_h` so that the M19-269 positive signed-energy event contributes a strictly positive conditioned mean.

Define

\[
\boxed{
\Lambda_E
:=
2\sqrt{z_E}\,\langle m_h\Gamma_E\rangle
>0.
}
\]

M19-297/300 give

\[
\boxed{
\Lambda_E
=
D_m(z_E)+Z_m(z_E)+B_m(z_E),
}
\]

where

\[
D_m=\mathscr D_m\ge0,
\qquad
Z_m=-\mathscr E_m',
\qquad
B_m=\mathscr B_m.
\]

## 2. Quantitative three-way payer split

If all three terms were strictly less than `Lambda_E/3`, their sum would be strictly less than `Lambda_E`.

Hence

\[
\boxed{
D_m(z_E)\ge\frac{\Lambda_E}{3}
\quad\lor\quad
B_m(z_E)\ge\frac{\Lambda_E}{3}
\quad\lor\quad
Z_m(z_E)\ge\frac{\Lambda_E}{3}.
}
\]

This split is purely algebraic and remains valid even when one of the other signed channels is negative.

The first branch is ordinary conditioned dissipation and remains subject to the M5-598 physical-accumulation firewall.

The second branch is the production--energy hysteresis/factor route of M19-289.

The third branch is analyzed below.

## 3. A positive depth payer thickens in z

Suppose

\[
Z_m(z_E)\ge\zeta,
\qquad
\zeta:=\frac{\Lambda_E}{3}>0.
\]

The retained wedge is smooth on every finite depth interval and the marked hull is compact. Therefore on a fixed neighborhood of `z_E` there is a finite constant

\[
L_Z<\infty
\]

such that

\[
|Z_m'(z)|\le L_Z.
\]

If `L_Z=0`, the positive lower bound persists throughout that connected neighborhood. Otherwise, on at least one interval adjacent to `z_E` of length

\[
\delta_z
:=
\min\left\{\delta_*,\frac{\zeta}{2L_Z}\right\},
\]

where `delta_*` is a fixed available wedge-depth margin,

\[
\boxed{
Z_m(z)\ge\frac\zeta2.
}
\]

Thus the positive-depth contribution has area at least

\[
\boxed{
A_Z
:=
\int (Z_m)_+dz
\ge
\frac\zeta2\,\delta_z.
}
\]

In the non-boundary-limited case this gives the explicit scale

\[
\boxed{
A_Z\ge\frac{\zeta^2}{4L_Z}.
}
\]

## 4. Exact terminal-budget versus replenishment dichotomy

M19-298 gives

\[
\int_0^\infty Z_m(z)dz
=
\mathscr E_m(0).
\]

Write

\[
Z_m=Z_m^+-Z_m^-,
\qquad
Z_m^\pm\ge0.
\]

Whenever these positive/negative variations are finite on the interval under consideration,

\[
\int Z_m^+-\int Z_m^-
=
\mathscr E_m(0).
\]

Since the local positive lobe gives

\[
\int Z_m^+\ge A_Z,
\]

we obtain the exact alternative

\[
\boxed{
\mathscr E_m(0)\ge A_Z
\quad\lor\quad
\int_0^\infty Z_m^-(z)dz
\ge
A_Z-\mathscr E_m(0)>0.
}
\]

Thus a depth lobe larger than the terminal conditioned energy cannot disappear. It forces a quantitatively nonzero opposite-sign replenishment elsewhere in depth.

For the weaker signed-integral interpretation, the same conclusion holds on a finite interval containing the positive lobe and any compensating return needed to match the endpoint difference.

## 5. Terminal scattering cap

Because

\[
\mathscr E_m(0)
=
\frac12\left\langle
m_h\int_{S^2}|A|^2d\omega
\right\rangle
\]

and `0<=m_h<=1`, a uniform terminal amplitude bound `|A|<=M_A` gives

\[
\boxed{
\mathscr E_m(0)
\le
2\pi M_A^2.
}
\]

Therefore an eventual quantitative estimate satisfying

\[
A_Z>2\pi M_A^2
\]

would force the replenishment branch independently of the detailed production/scattering correlation.

No such numerical dominance is currently certified.

## 6. Interpretation of the replenishment branch

If

\[
Z_m(z)<0
\]

on a set of nonzero depth measure, then

\[
\mathscr E_m'(z)>0.
\]

The production-conditioned spherical energy increases with depth there.

By M19-300 this increase is not an undefined source. It must satisfy

\[
Z_m
=
D_m+B_m-(2zJ_m'+J_m).
\]

Therefore quantified replenishment returns directly to explicit event-boundary hysteresis and radial-current redistribution.

## 7. Updated dynamic-core tree

The positive fixed-lag event now yields

\[
\boxed{
\mathcal E_{fixed\ lag}^{+}
\Longrightarrow
\mathcal D_{cond}^{large}
\lor
\mathcal B_{hyst}^{large}
\lor
\mathcal Z_{terminal\ budget}
\lor
\mathcal Z_{replenishment}.
}
\]

The first is an unsigned physical-scaling problem.
The second and fourth are recurrent circulation/redistribution problems.
The third is a finite terminal scattering budget.

Thus no new untyped signed payer remains in the depth channel.

## 8. Next target

The most informative next step is to combine `B_hyst` and `Z_replenishment` geometrically. Both describe circulation rather than exhaustion:

- `B_hyst` is circulation in recurrent q/event phase;
- `Z_replenishment` is return flow in wedge depth.

The next audit should determine whether together they form a source-free two-dimensional cycle or whether the exact wedge PDE forces a nonzero source term that returns to dissipation/current export.

---

\[
\boxed{\text{M19-301 COMPLETE; THE DEPTH BRANCH IS REDUCED TO A FINITE TERMINAL BUDGET OR EXPLICIT QUANTIFIED REPLENISHMENT.}}
\]