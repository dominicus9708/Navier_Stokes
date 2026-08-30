# DSD M5-346 — Endpoint Atom Excludes the Velocity-Type-I-in-Time Corridor

Date: 2026-08-30

Status: **PUBLISHED ENERGY-MEASURE INPUT + INTERNAL ATOM EXTRACTION / ENERGY-BEARING AFFINE-SHIELD BRANCH FORCED INTO GENUINE VELOCITY TYPE-II TIME / GLOBAL REGULARITY UNPROVED.**

## 1. Published input

Leslie--Shvydkoy, *The Energy Measure for the Euler and Navier--Stokes Equations* (Arch. Ration. Mech. Anal. 230 (2018), 459--492), prove local-dimension bounds for the endpoint energy measure and, in particular, treat the 3D Navier--Stokes velocity-Type-I-in-time condition

\[
\boxed{
\|u(t)\|_{L^\infty(\mathbb R^3)}
\le C(T_*-t)^{-1/2}.
}
\]

Their Type-I argument yields a positive-power local kinetic-energy bound (in the endpoint `q=2` case the standard form is an `O(r)` local-energy bound on the corresponding parabolic window), and consequently the terminal energy measure has no point atoms. Their main Navier--Stokes application also gives energy equality at the first Type-I blow-up time.

The only implication used in this audit is

\[
\boxed{
\text{velocity Type-I in time}
\Longrightarrow
\mu_*(\{a\})=0
\quad\forall a.
}
\]

## 2. Internal input

M5-321 proved for the present whole-space smooth preterminal branch that the full-time endpoint energy measure exists:

\[
|u(t)|^2dx\stackrel{*}{\rightharpoonup}\mu_*
\qquad(t\uparrow T_*).
\]

It also proved that if a nested shrinking core satisfies

\[
X_j\to a,
\qquad d_j\to0,
\qquad
\int_{B_{d_j}(X_j)}|u(t_j)|^2dx\ge c_0>0,
\]

then

\[
\boxed{
\mu_*(\{a\})\ge c_0>0.
}
\]

The saturated affine-shield benchmark from M5-317/M5-320 has exactly this form.

## 3. Immediate contradiction with velocity Type-I

Assume the affine/energy-bearing branch produces an atom:

\[
\mu_*(\{a\})>0.
\]

If

\[
\limsup_{t\uparrow T_*}
\sqrt{T_*-t}\,\|u(t)\|_\infty<\infty,
\]

then an eventual velocity-Type-I bound holds, so the Leslie--Shvydkoy result gives

\[
\mu_*(\{a\})=0,
\]

contradiction.

Therefore

\[
\boxed{
\mu_*(\{a\})>0
\Longrightarrow
\limsup_{t\uparrow T_*}
\sqrt{T_*-t}\,\|u(t)\|_\infty
=\infty.
}
\]

## 4. Structural consequence

The energy-bearing affine/atom branch is not a generic terminal branch anymore. It lies entirely inside a genuine velocity-Type-II-in-time corridor.

Thus the earlier frontier

\[
\text{energy-bearing dual-hyperbolic atom}
\lor
\text{microstructure H}
\lor
T_{dyn}
\]

can be refined to

\[
\boxed{
\text{velocity-Type-II energy-bearing dual-hyperbolic atom}
\lor
H_{micro}
\lor
T_{dyn}.
}
\]

## 5. Relation to previous Type-I/W1 closure

This result is complementary to M5-275/M5-276.

- The complete realized quiet Type-I/W1 branch was already eliminated through weak-`L^3` ancient Liouville rigidity.
- M5-346 says that even before using that tail machinery, any branch which concentrates an order-one kinetic-energy atom is incompatible with the classical velocity-Type-I-in-time energy-measure bound.

Hence an energy atom is a genuinely Type-II object in the present proof tree.

## 6. What this does not prove

This does **not** exclude Type-II atoms.

It also does not follow merely from global energy equality that atoms are impossible; the local energy-measure dimension estimate is the relevant input.

No claim is made here that a BMO-controlled Type-II scenario is excluded. That requires a separate endpoint energy-measure/regularity theorem and is not imported into this branch without a full hypothesis match.

## 7. Next target

The atom branch must now pay both

\[
\boxed{
\sqrt{T_*-t}\,\|u(t)\|_\infty\to\infty
\text{ along a sequence}
}
\]

and, from M5-333/M5-345,

\[
\boxed{
\int^{T_*}\|S_-(t)\|_3^2dt=\infty,
\qquad
\int\!\int S_-:C_H\,dxdt=\infty.
}
\]

The next useful question is therefore whether the velocity-Type-II clock and the compressive Oseen-alignment clock can be separated. If not, the atom forces a quantitative Type-II concentration rate; if yes, the separation itself is a turnover/reformation channel.

## 8. Audit verdict

### PROVED/IMPORTED WITH HYPOTHESIS MATCH

- saturated affine shield gives a terminal point-energy atom (internal M5-321);
- velocity Type-I-in-time excludes terminal point-energy atoms (Leslie--Shvydkoy energy-measure theory);
- therefore any energy-bearing atom branch is necessarily velocity Type-II in time.

### OPEN

- exclusion of Type-II atoms;
- a quantitative relation between Type-II velocity growth and compressive Oseen alignment;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]