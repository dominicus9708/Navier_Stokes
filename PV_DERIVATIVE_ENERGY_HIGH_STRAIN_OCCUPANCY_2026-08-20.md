# Derivative-Energy Occupancy Forced by H1 Production — 2026-08-20

Overall status: **GLOBAL-TO-HIGH-STRAIN OCCUPANCY LEMMA — GLOBAL REGULARITY NOT PROVED.**

The compatibility tax derived on a high-strain core becomes useful globally only if that core carries a definite fraction of the total strain-gradient energy. This note extracts such an occupancy directly from the H1 production rate.

---

## 1. Sharp static production bound

Let

\[
P=\|\nabla S\|_2^2,
\qquad
N=-\langle\mathcal R_{VI},-\Delta S\rangle.
\]

The sharp trace-free estimate gives

\[
\boxed{
N
\le
C_H\int|S||\nabla S|^2dx,
\qquad
C_H=\frac4{\sqrt6}.
}
\]

Define the instantaneous production per strain-gradient energy

\[
\boxed{q=N/P.}
\]

Then every positive-production time satisfies

\[
\boxed{
\frac1P\int|S||\nabla S|^2dx
\ge
\frac q{C_H}
=
\frac{\sqrt6}{4}q.
}
\]

---

## 2. Derivative-energy probability measure

Define

\[
d\mu_P
=\frac{|\nabla S|^2}{P}dx.
\]

This is a probability measure. Let

\[
B=\|S\|_\infty.
\]

Then

\[
\mathbb E_{\mu_P}|S|
\ge
\frac q{C_H}.
\]

Define the dimensionless production-amplitude ratio

\[
\boxed{
\beta
=\frac{q}{C_HB}
=\frac{\sqrt6}{4}\frac qB.
}
\]

The static bound implies `0 <= beta <= 1`.

---

## 3. High-strain occupancy

For `0 < theta < 1`, define

\[
E_\theta
=\{x:|S(x)|\ge\theta B\}
\]

and its derivative-energy occupancy

\[
\alpha_\theta
=\mu_P(E_\theta)
=
\frac{\int_{E_\theta}|\nabla S|^2dx}{P}.
\]

Since `|S| <= theta B` outside `E_theta` and `|S| <= B` everywhere,

\[
\mathbb E_{\mu_P}|S|
\le
\theta B(1-\alpha_\theta)+B\alpha_\theta.
\]

Combining with the production lower bound gives

\[
\beta
\le
\theta+(1-\theta)\alpha_\theta.
\]

Therefore, whenever `theta < beta`,

\[
\boxed{
\alpha_\theta
\ge
\frac{\beta-\theta}{1-\theta}.
}
\]

This is an exact distributional consequence of the H1 production requirement.

---

## 4. Canonical half-beta threshold

Choose

\[
\theta=\frac\beta2.
\]

Then

\[
\boxed{
\alpha_{\beta/2}
\ge
\frac{\beta}{2-\beta}.
}
\]

The corresponding absolute strain threshold is

\[
\theta B
=
\frac{q}{2C_H}
=
\boxed{
\frac{\sqrt6}{8}q.
}
\]

An important feature is that this threshold is independent of `B`.

Thus at any time with production ratio `q`, a definite fraction of derivative energy must lie where

\[
\boxed{|S|\ge\frac{\sqrt6}{8}q,}
\]

provided `beta` is bounded below.

---

## 5. Insert the Leray recurrence requirement

At a recurrent Leray time,

\[
\frac12P_s+rac34P+\nu H=N.
\]

At a nondecreasing/recovery checkpoint with `P_s >= 0`, one has

\[
q=\frac NP
\ge
\frac34+
u\frac HP.
\]

If

\[
\kappa=P/H,
\]

then

\[
\boxed{
q\ge\frac34+\frac\nu\kappa.
}
\]

Hence the high-strain derivative-energy set contains the absolute threshold

\[
\boxed{
|S|
\ge
\frac{\sqrt6}{8}
\left(
\frac34+\frac\nu\kappa
\right).
}
\]

This is stronger than merely requiring a nonzero strain somewhere.

---

## 6. Uniform compact-class occupancy

Suppose on a recurrent compact class `K`,

\[
B\le B_K<\infty
\]

and

\[
\kappa\le\kappa_K^+<\infty.
\]

Then

\[
q\ge q_-:=\frac34+\frac\nu{\kappa_K^+}.
\]

Therefore

\[
\beta
\ge
\boxed{
\beta_K
:=
\frac{q_-}{C_HB_K}
}
\]

and the derivative-energy occupancy of

\[
|S|
\ge
\frac{q_-}{2C_H}
\]

is at least

\[
\boxed{
\alpha_{high,K}
\ge
\frac{\beta_K}{2-\beta_K}
>0.
}
\]

Thus a finite class-level strain-amplitude ceiling immediately converts recurrence into a uniform high-strain derivative-energy occupancy.

---

## 7. Branch if the class amplitude ceiling fails

The remaining issue is to quantify `B_K`.

On the non-H/T first-hitting class, precompactness and local analyticity imply `B_K < infinity` abstractly. To make the occupancy numerical one needs an explicit upper estimate for `B_K`, for example from:

- the first-hitting vorticity cap plus Calderon--Zygmund/Hölder control;
- the existing BMO + finite-energy/Hermite logarithmic route;
- local Biot--Savart splitting into analytic near field and passive halo.

If no uniform `B_K` exists, then strain amplitude itself escapes while vorticity remains first-hitting bounded, creating a separate singular-integral/halo branch rather than a compact recurrent `P_V` profile.

---

## 8. Relation to the half-amplitude compatibility ball

The present occupancy lemma and `PV_HALF_AMPLITUDE_BALL_SHAPE_BOUND_2026-08-20.md` serve complementary roles.

- The half-amplitude ball gives a universal local coherence shape bound `chi <= 2` when the positive-middle spectrum persists.
- The present lemma gives a global lower bound on how much derivative energy must occupy high-strain regions when recurrence demands large H1 production.

The next step is a covering/selection lemma: select one or finitely many high-strain components carrying the occupancy `alpha_high,K`, then apply the localized compatibility tax to those components. If the occupancy fragments into many components, the multicore branch is activated.

Status: **RECURRENT H1 PRODUCTION FORCES A DEFINITE FRACTION OF STRAIN-GRADIENT ENERGY INTO A HIGH-STRAIN SET. ON A PRECOMPACT CLASS WITH FINITE STRAIN-AMPLITUDE CEILING, THIS OCCUPANCY IS UNIFORM AND CAN BE FED INTO THE LOCAL COMPATIBILITY TAX.**