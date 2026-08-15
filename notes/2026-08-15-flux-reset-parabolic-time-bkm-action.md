# Flux reset requires parabolic time and large BKM-scale vorticity action

Date: 2026-08-15

Status: **DERIVED L-INFINITY RATE BARRIER FOR BOUNDED-SHAPE MATERIAL PROBES / FINAL ZENO NORMAL FORM SHARPENED.**

This note gives a time-scale lower bound for the smooth material-flux reset.

Unlike the previous `L2` reset-cost estimate, the argument uses the first-hitting pointwise vorticity cap directly.

---

## 1. Physical smooth flux probe

At physical scale `ell`, use a smooth material flux probe of the form

\[
\psi_\ell(x)
=\ell^{-1}\Psi((x-a)/\ell),
\]

transported by the inviscid adjoint equation.

Under bounded shape distortion,

\[
\boxed{
\|\Delta\psi_\ell(t)\|_1
\le C_1
}
\]

uniformly on the reset interval.

The scaling is critical:

- probe amplitude: `ell^-1`;
- two derivatives: `ell^-2`;
- volume: `ell^3`;

so the `L1` norm of the Laplacian is scale independent.

---

## 2. Exact viscous rate identity

For

\[
F(t)=\langle\omega(t),\psi_\ell(t)\rangle,
\]

the material adjoint cancellation gives

\[
F'(t)
=\nu\langle\omega,\Delta\psi_\ell\rangle.
\]

Therefore

\[
\boxed{
|F'(t)|
\le
C_1\nu\|\omega(t)\|_\infty.
}
\]

This estimate is independent of the physical probe scale.

---

## 3. Reset circulation scale

At a coherent Reynolds-one crossing with physical vorticity level `W` and normalized radius `R`,

\[
\ell=R/\sqrt W.
\]

The signed vorticity flux is scale invariant and satisfies

\[
\boxed{
\Phi\asymp R^2.
}
\]

Equivalently in physical variables,

\[
\boxed{
\Phi\asymp W\ell^2.
}
\]

A fixed-fraction reset therefore changes `F` by

\[
|\Delta F|\ge c\Phi.
\]

---

## 4. BKM-action lower bound per reset

Integrating the rate estimate over a reset interval `I`,

\[
 c\Phi
\le
C_1\nu\int_I\|\omega(t)\|_\infty dt.
\]

Hence

\[
\boxed{
\int_I\|\omega(t)\|_\infty dt
\gtrsim
\frac{\Phi}{\nu}.
}
\]

At the coherent crossing,

\[
\boxed{
\int_I\|\omega(t)\|_\infty dt
\gtrsim
\frac{R^2}{\nu}.
}
\]

Thus a late reset with `R->infinity` requires a diverging amount of scale-invariant vorticity action.

This is compatible with the Beale--Kato--Majda necessity of divergent vorticity action at a hypothetical singularity; it is not by itself a contradiction.

---

## 5. Parabolic-time lower bound

On a terminal first-hitting interval ending at level `W`,

\[
\|\omega(t)\|_\infty\le W.
\]

Therefore

\[
 cW\ell^2
\lesssim
\nu W|I|,
\]

which gives

\[
\boxed{
|I|
\gtrsim
\frac{\ell^2}{\nu}.
}
\]

So a bounded-shape quantitative flux reset cannot occur faster than its viscous parabolic scale.

In terminal normalized variables the same statement is

\[
\boxed{
|I|_{\rm norm}
\gtrsim
\frac{R^2}{\nu}.
}
\]

This explains why smooth vortex reconnection may occur in arbitrarily short **physical** times at high frequency while still respecting a scale-local parabolic time.

---

## 6. Combine with the energy reset price

The previous smooth reset lemma gives

\[
\boxed{
\nu\int_I\|\omega\|_2^2dt
\gtrsim
\frac{R^5}{\sqrt W}
=q^{-1/2},
\qquad q=W/R^{10}.
}
\]

The present lemma adds

\[
\boxed{
|I|
\gtrsim
\frac{R^2}{\nu W}
=
\frac{\ell^2}{\nu},
}
\]

and

\[
\boxed{
\int_I\|\omega\|_\infty dt
\gtrsim
R^2/\nu.
}
\]

Thus every bounded-distortion reset pays simultaneously in three ledgers:

1. physical energy dissipation: `q^-1/2`;
2. physical time: `ell^2/nu`;
3. critical vorticity/BKM action: `R^2/nu`.

---

## 7. Parabolic Zeno normal form

An infinite reset cascade compatible with finite physical time and finite kinetic-energy dissipation must therefore satisfy, on any disjoint reset-selected subsequence,

\[
\boxed{
\sum_j\ell_j^2<\infty,
\qquad
\sum_jq_j^{-1/2}<\infty,
}
\]

while necessarily

\[
\boxed{
\sum_jR_j^2=\infty
}
\]

because `R_j->infinity` and each reset carries `R_j^2` of vorticity action.

This is the precise Zeno geometry:

- physical scales collapse fast enough that parabolic times are summable;
- physical energy costs collapse fast enough to be summable;
- the scale-invariant vorticity action diverges.

That is exactly the qualitative signature expected of a finite-time singular route rather than a contradiction to one.

---

## 8. Claim boundary

The `L1` Laplacian bound is a bounded material-shape hypothesis. Its failure again routes to probe derivative/deformation collapse.

The BKM-action lower bound does not prove regularity because a finite-time singularity is allowed, and indeed required, to have divergent critical vorticity action.

The important output is a much sharper final normal form, not a proof of nonexistence.

Status: **BOUNDED-DISTORTION RESET MUST OCCUPY PARABOLIC TIME AND DIVERGENT BKM ACTION / SURVIVING ENDGAME = PARABOLIC SUPER-ZENO OR PROBE-DERIVATIVE COLLAPSE.**