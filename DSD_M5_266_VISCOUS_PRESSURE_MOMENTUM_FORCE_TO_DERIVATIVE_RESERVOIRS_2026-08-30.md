# DSD M5-266 — Viscous / Pressure Momentum Force to Derivative Reservoirs

Date: 2026-08-30

Parent: `DSD_M5_265_CONVECTIVE_MOMENTUM_FORCE_MEAN_CANCELLATION_2026-08-30.md`

Status: **DIRECT VOLUME REDUCTION / THE VISCOUS MOMENTUM-FORCE COMPONENT IS THE BALL AVERAGE OF `nu Delta V` AND THEREFORE FORCES A FIXED-BALL H2 FLOOR; THE PRESSURE-FORCE COMPONENT IS THE BALL AVERAGE OF `grad P` AND, USING THE WHOLE-SPACE PRESSURE REPRESENTATION TOGETHER WITH THE W1 `L-infinity` VELOCITY CAP, IS CONTROLLED BY THE GLOBAL H1/STRAIN RESERVOIR / COMBINED WITH M5-265, ALL THREE MOMENTUM-FORCE SUBBRANCHES REDUCE TO DERIVATIVE/RELATIVE-STRUCTURE PAYERS / THRESHOLD CROSSING REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Momentum-force components

From M5-264,

\[
 b_{vis}
=\frac\nu{M_R}
\int_{\partial B_R}\partial_nV\,dS,
\]

and

\[
 b_{pres}
=-\frac1{M_R}
\int_{\partial B_R}Pn\,dS.
\]

Here

\[
M_R=|B_R|=\frac{4\pi}{3}R^3.
\]

---

## 2. Viscous force as a volume H2 quantity

By divergence theorem componentwise,

\[
\boxed{
\int_{\partial B_R}\partial_nV\,dS
=\int_{B_R}\Delta V\,dY.
}
\]

Hence

\[
\boxed{
 b_{vis}
=\frac\nu{M_R}
\int_{B_R}\Delta V\,dY.
}
\]

Cauchy--Schwarz gives

\[
\boxed{
|b_{vis}|
\le
\frac\nu{\sqrt{M_R}}
\|\Delta V\|_{L^2(B_R)}.
}
\]

---

## 3. Quantitative H2 floor

If the viscous component carries the M5-264 action floor,

\[
\langle|b_{vis}|\rangle\ge b_*/3,
\]

then

\[
\left\langle\|\Delta V\|_{L^2(B_R)}\right\rangle
\ge
\frac{b_*\sqrt{M_R}}{3\nu}.
\]

By Jensen/Cauchy,

\[
\boxed{
\left\langle
\|\Delta V\|_{L^2(B_R)}^2
\right\rangle
\ge
\frac{M_Rb_*^2}{9\nu^2}.
}
\]

Thus

\[
\boxed{
T_{vis-force}
\Longrightarrow
\text{fixed-ball H2 derivative floor}.
}
\]

This is a literal second-derivative payer.

---

## 4. Pressure force as a volume pressure-gradient quantity

Again by divergence theorem,

\[
\boxed{
\int_{\partial B_R}Pn\,dS
=\int_{B_R}\nabla P\,dY.
}
\]

Therefore

\[
\boxed{
 b_{pres}
=-\frac1{M_R}
\int_{B_R}\nabla P\,dY.
}
\]

and

\[
\boxed{
|b_{pres}|
\le
M_R^{-1/2}
\|\nabla P\|_{L^2(B_R)}.
}
\]

If

\[
\langle|b_{pres}|\rangle\ge b_*/3,
\]

then

\[
\boxed{
\left\langle
\|\nabla P\|_{L^2(B_R)}^2
\right\rangle
\ge
\frac{M_Rb_*^2}{9}.
}
\]

---

## 5. Whole-space pressure-gradient estimate

For divergence-free `V`, after fixing the usual time-dependent scalar gauge,

\[
P
=\mathcal R_i\mathcal R_j(V_iV_j).
\]

Differentiate:

\[
\nabla P
=\mathcal R_i\mathcal R_j\nabla(V_iV_j).
\]

By `L2` boundedness of Riesz transforms,

\[
\|\nabla P\|_2
\le
C_R\|\nabla(V\otimes V)\|_2.
\]

Hence

\[
\boxed{
\|\nabla P\|_2
\le
C_P\|V\|_\infty\|\nabla V\|_2.
}
\]

The W1 first-hitting/Type-I corridor has a finite global normalized velocity cap

\[
\|V\|_\infty\le M_V.
\]

Therefore

\[
\boxed{
\|\nabla P\|_2
\le
C_PM_V\|\nabla V\|_2.
}
\]

---

## 6. Pressure-force branch to global H1 floor

Combining the local pressure-force lower bound with the global upper estimate yields

\[
\frac{M_Rb_*^2}{9}
\le
\left\langle\|\nabla P\|_{L^2(B_R)}^2\right\rangle
\le
C_P^2M_V^2
\left\langle\|\nabla V\|_2^2\right\rangle.
\]

Thus

\[
\boxed{
\left\langle\|\nabla V\|_2^2\right\rangle
\ge
\frac{M_Rb_*^2}
{9C_P^2M_V^2}.
}
\]

Hence

\[
\boxed{
T_{pres-force}
\Longrightarrow
\text{global normalized H1/strain reservoir}.
}
\]

---

## 7. Combine with convective reduction

M5-265 gives

\[
T_{conv-force}
\Longrightarrow
\text{local relative-gradient/trace reservoir}.
\]

The present note gives

\[
T_{vis-force}
\Longrightarrow
H2_{local},
\]

and

\[
T_{pres-force}
\Longrightarrow
H1_{global}.
\]

Therefore the complete momentum-action branch satisfies

\[
\boxed{
T_{mom}
\Longrightarrow
D_{rel/local}
\lor
H2_{local}
\lor
H1_{global}.
}

There is no remaining untyped vector-force branch.

---

## 8. Important threshold boundary

All three conclusions are **positive lower bounds**.

The critical pure W1 corridor already carries order-one H1/H2 structure. Therefore one must compare

\[
D_{forced},\quad H2_{forced},\quad H1_{forced}
\]

with the explicit pure-corridor ceilings before reclassifying them as H escapes.

Thus

\[
\boxed{
T_{mom}
\to
\text{formed derivative payer}
}

is proved, while

\[
\boxed{
T_{mom}\to H\text{ contradiction}
}

is not yet proved.

---

## 9. Updated stationary endpoint

The stationary endpoint from M5-260 now routes entirely to finite-scale scalar/derivative structure:

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
T_{var/bdry}
\lor
D_{rel/local}
\lor
H2_{local}
\lor
H1_{global}.
}

The former mean-momentum vector branch has been eliminated as an independent category.

---

## 10. Next target

The high-leverage step is now a **threshold table** in common first-hitting units:

- inherited stationary current floor `j_R`;
- induced mean floor `m_*`;
- momentum action floor `b_*`;
- forced `D_rel`, `H2_local`, and `H1_global` floors;
- existing pure-corridor upper ceilings for those exact quantities.

If any forced floor exceeds its pure ceiling, the stationary tail branch closes. If all fit below the ceilings, the exact surviving numerical window should be recorded rather than generating another qualitative branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
