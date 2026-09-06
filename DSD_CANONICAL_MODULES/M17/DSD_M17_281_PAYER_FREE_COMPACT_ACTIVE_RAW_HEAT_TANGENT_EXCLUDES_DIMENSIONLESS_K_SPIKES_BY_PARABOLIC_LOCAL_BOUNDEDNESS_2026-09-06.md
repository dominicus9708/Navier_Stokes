# DSD M17-281 — A payer-free compact active raw heat tangent excludes dimensionless K spikes by parabolic local boundedness

Date: 2026-09-06  
Canonical ID: **M17-281**

Status: **K-SPIKE CLOSURE ON THE COMPACT ACTIVE HEAT LANE / THE BOUNDED-SPIKE VERSUS K-SPIKE SPLIT OF M17-233 REMAINED EXPLICIT THROUGH M17-280. ON THE FINAL PAYER-FREE COMPACT RAW HEAT TANGENT, M17-272 GIVES UNIFORM LOCAL `W^{2,1}_p` CONTROL OF `V` FOR EVERY FINITE `p`, WHILE AN ACTIVE AMPLITUDE FLOOR GIVES `K=(V·Delta V)/|V|^2` UNIFORM LOCAL `L^p` CONTROL. THE SAME POLAR FLOOR AND `C1,alpha` CONTROL BOUND `grad log a`. M17-263 GIVES THE EXACT SCALAR EQUATION `K_tau=Delta K+2 grad log a·grad K`. STANDARD LOCAL BOUNDEDNESS FOR A LINEAR UNIFORMLY PARABOLIC EQUATION WITH BOUNDED DRIFT THEN UPGRADES THE `L^p` CONTROL TO A UNIFORM INTERIOR `L-infinity` BOUND. THEREFORE A DIMENSIONLESS `K` SPIKE CANNOT OCCUR INSIDE THE PAYER-FREE COMPACT ACTIVE CORRIDOR. ITS OCCURRENCE FORCES AMPLITUDE/NODAL FAILURE, NORMALIZED MASS/PALINSTROPHY FAILURE, OR SCALED AMBIENT/COEFFICIENT FAILURE BEFORE THE TANGENT LIMIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compact active cylinder

Work on nested cylinders

\[
Q_{1/2}\Subset Q_1\Subset Q_2.
\]

On the payer-free compact lane assume, as in M17-272,

\[
\|V_j\|_{L^2(Q_2)}\le M_0,
\]

\[
\|A_j\|_{L^\infty(Q_2)}
+\|C_j\|_{L^\infty(Q_2)}
\le M_1,
\]

and an active amplitude floor

\[
\boxed{|V_j|\ge a_*>0}
\]

on `Q_1`.

Failure of these assumptions is already typed as normalized-palinstrophy/mass escape, ambient/coefficient activity, or nodal/amplitude degeneration.

---

## 2. Parabolic Lp control of V

M17-272 gives, for every finite `p`,

\[
\boxed{
\|V_j\|_{W^{2,1}_p(Q_1)}\le C_p.
}
\]

In particular,

\[
\boxed{
\|\Delta V_j\|_{L^p(Q_1)}\le C_p.
}
\]

---

## 3. Convert to Lp control of K

The raw CE-H relation is

\[
\Delta V_j=K_jV_j.
\]

Therefore, where `|V_j|>=a_*`,

\[
K_j
=\frac{V_j\cdot\Delta V_j}{|V_j|^2}.
\]

Hence

\[
|K_j|
\le a_*^{-1}|\Delta V_j|.
\]

Thus for every finite `p`,

\[
\boxed{
\|K_j\|_{L^p(Q_1)}\le C_{p,a_*}.
}
\]

---

## 4. Drift bound in the K equation

Let

\[
a_j:=|V_j|.
\]

Then

\[
|\nabla a_j|
\le|\nabla V_j|.
\]

M17-272 with `p>5` gives a uniform interior bound on `grad V_j`, so

\[
\boxed{
\|\nabla\log a_j\|_{L^\infty(Q_{3/4})}
\le a_*^{-1}\|\nabla V_j\|_\infty
\le B_*.
}
\]

M17-263 gives

\[
\boxed{
\partial_\tau K_j
=\Delta K_j
+2\nabla\log a_j\cdot\nabla K_j.
}
\]

Thus `K_j` solves a scalar linear parabolic equation with identity diffusion and uniformly bounded drift.

---

## 5. Interior local boundedness

For a scalar solution of

\[
u_\tau=\Delta u+b\cdot\nabla u,
\qquad
\|b\|_\infty\le B_*,
\]

standard parabolic local boundedness/Moser estimates give, for any fixed `p>0`,

\[
\|u\|_{L^\infty(Q_{1/2})}
\le
C_{p,B_*}\|u\|_{L^p(Q_{3/4})}.
\]

Apply this to `K_j` and use Section 3:

\[
\boxed{
\|K_j\|_{L^\infty(Q_{1/2})}
\le C<\infty.
}
\]

The constant is independent of `j`.

---

## 6. K-spike exclusion

Therefore

\[
\boxed{
\|K_j\|_{L^\infty(Q_{1/2})}\to\infty
}
\]

is impossible while the payer-free compact active corridor remains valid.

The correct implication is

\[
\boxed{
G_{dimensionless\ K\text{-}spike}
\Longrightarrow
G_{nodal/amplitude\ degeneration}
\lor
H_{normalized\ palinstrophy/mass\ escape}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{interface/domain}.
}
\]

Thus the explicit `K`-spike branch of M17-233 is removed from the final compact active raw-heat frontier.

---

## 7. Relation to coefficient spikes before tangent compactness

This result does not say that the original pre-limit multiplier can never spike.

It says that if such spikes survive on the selected intrinsic normalization, then one of the compactness/amplitude/coefficient assumptions needed to reach the payer-free raw heat tangent must fail.

The event is therefore exported to an already explicit pre-limit payer branch rather than retained inside the tangent classification.

---

## 8. DSD audit

- `K` is controlled through the exact relation `Delta V=K V` only where the amplitude floor holds.
- No division across a node is used.
- The parabolic `K` equation is exact on the raw tangent.
- `L-infinity` boundedness is derived from `L^p` plus bounded drift, not assumed.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
