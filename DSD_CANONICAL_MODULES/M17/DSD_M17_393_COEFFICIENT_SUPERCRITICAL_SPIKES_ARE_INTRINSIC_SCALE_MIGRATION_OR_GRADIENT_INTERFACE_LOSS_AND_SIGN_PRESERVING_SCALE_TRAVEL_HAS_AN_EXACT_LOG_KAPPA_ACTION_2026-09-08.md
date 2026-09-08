# DSD M17-393 — Coefficient-supercritical spikes are intrinsic-scale migration or gradient/interface loss, and sign-preserving scale travel has an exact log-`kappa` action

Date: 2026-09-08  
Canonical ID: **M17-393**

Status: **ACTIVE SCALE-IDENTITY CORRECTION / COEFFICIENT-MIGRATION ACTION / SUPERCRITICAL-SPIKE RECLASSIFICATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-392 closes ordinary bounded-coefficient flux turnover by the standard-energy variation ledger

\[
\sum_jR_j\operatorname{Var}(\Phi_j^2)<\infty.
\]

One remaining exit is

\[
|\kappa|R^2\to\infty.
\]

The present module audits the meaning of that exit.

On exact CE-H, `kappa` already defines its own intrinsic spatial scale.

Therefore a coefficient that is supercritical relative to an externally chosen scale `R` must first be reclassified by its own coefficient scale before being treated as an independent blow-up mechanism.

## 2. Exact intrinsic coefficient scale

On the active set

\[
\kappa\ne0,
\]

define

\[
\boxed{
r_\kappa:=|\kappa|^{-1/2}.}
\]

This is exactly the scale used by M17-381.

If on a nominal scale-`R` region

\[
|\kappa|R^2=A,
\]

then

\[
\boxed{
r_\kappa=R A^{-1/2}.}
\]

Hence

\[
|\kappa|R^2\gg1
\]

is equivalent to

\[
\boxed{r_\kappa\ll R.}
\]

Thus the coefficient has not created an untyped scalar infinity; it has selected a smaller intrinsic coefficient scale.

## 3. M17-381 ownership reclassification

M17-381 gives the exact CE-H identity

\[
|\Delta W|^2=\kappa^2|W|^2
\]

and assigns every nonzero raw-`H2` density point to the unique dyadic coefficient bin corresponding to

\[
r_\kappa\sim|\kappa|^{-1/2}.
\]

Therefore a point with

\[
|\kappa|R^2\gg1
\]

must be counted in the smaller `r_kappa` coefficient-scale class, not repeatedly in the larger scale-`R` class.

This preserves the M17-381 no-double-counting rule.

The correct audit statement is

\[
\boxed{
G_{|\kappa|R^2\gg1}
\Longrightarrow
H_{smaller\ intrinsic\ coefficient\ scale}
\lor
G_{coefficient\ localization/interface}.
}
\]

## 4. Spatial realization at the smaller scale

M17-382 applies at the actual intrinsic scale `r_kappa`.

If

\[
\boxed{
r_\kappa^3|\nabla\kappa|\le G_*}
\]

then a coefficient-core point has a genuine spatial neighborhood of radius comparable to `r_kappa` on which

\[
|\kappa|\asymp r_\kappa^{-2}.
\]

Thus a nominal supercritical spike becomes an actual smaller own-scale cell.

If instead

\[
r_\kappa^3|\nabla\kappa|\to\infty,
\]

retain the already typed transverse coefficient-gradient decompactification branch.

If the spatial realization fails through cutoff, rank, interface, or domain loss, retain that branch explicitly.

Therefore

\[
\boxed{
\begin{aligned}
G_{coefficient\ supercritical\ relative\ to\ R}
\Longrightarrow{}&
H_{true\ smaller\ own\text{-}scale\ cell}\\
&\lor G_{normalized\ coefficient\ gradient}\\
&\lor G_{interface/rank/domain}.
\end{aligned}
}
\]

## 5. Time-dependent intrinsic scale

Now work in physical variables on a same-material sign-preserving interval on which

\[
\kappa(t)\ne0.
\]

Define

\[
r_\kappa(t):=|\kappa(t)|^{-1/2}.
\]

Then

\[
\log r_\kappa
=-\frac12\log|\kappa|.
\]

Taking the material derivative,

\[
\boxed{
D_t\log r_\kappa
=-\frac12\frac{D_t\kappa}{\kappa}.
}
\]

Therefore the total log-scale travel obeys

\[
\boxed{
\operatorname{Var}_I(\log r_\kappa)
\le
\frac12
\int_I
\frac{|D_t\kappa|}{|\kappa|}dt.
}
\]

For a monotone sign-preserving scale change from `r_0` to `r_1`, equality holds at the endpoint level:

\[
\boxed{
\left|
\log\frac{r_1}{r_0}
\right|
=
\frac12
\left|
\log\frac{|\kappa_0|}{|\kappa_1|}
\right|
\le
\frac12
\int_I
\frac{|D_t\kappa|}{|\kappa|}dt.
}
\]

Thus crossing many intrinsic coefficient scales requires a definite log-`kappa` material action.

## 6. Dyadic scale-crossing count

Suppose one material label moves through `N` dyadic intrinsic scales while preserving the sign of `kappa`.

Then

\[
\left|
\log\frac{r_{final}}{r_{initial}}
\right|
\ge
N\log2-O(1).
\]

Hence

\[
\boxed{
\int_I
\frac{|D_t\kappa|}{|\kappa|}dt
\gtrsim
2N\log2-O(1).
}
\]

So unbounded coefficient-scale migration is not free.

Its exact canonical payer is the normalized coefficient-velocity action

\[
\boxed{
\mathcal A_{mig}(I)
:=
\int_I
\frac{|D_t\kappa|}{|\kappa|}dt.
}
\]

This action is dimensionless and counts logarithmic scale travel.

## 7. Physical CE-H constitutive decomposition

M17-339 gives

\[
\boxed{
D_t\kappa
=
L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{geom}.
}
\]

Therefore on a sign-preserving active interval,

\[
\mathcal A_{mig}(I)
\le
\int_I
\frac{|L_\rho\kappa|}{|\kappa|}dt
+
\int_I
\frac{|L_\rho\sigma|}{|\kappa|}dt
+
\int_I
\frac{|\mathcal R_{geom}|}{|\kappa|}dt.
\]

Consequently a long scale journey must be serviced by at least one of

1. coefficient weighted diffusion;
2. strain weighted diffusion;
3. geometric remainder;
4. loss of the sign-preserving active interval through `kappa=0`;
5. interface/domain/genealogy loss.

This is a constitutive payer split, not a global budget closure.

## 8. Zero crossing is a separate branch

The quantity

\[
\frac{|D_t\kappa|}{|\kappa|}
\]

is singular at

\[
\kappa=0.
\]

Therefore M17-393 must not be used across a zero crossing.

If a scale-migration history reaches or crosses `kappa=0`, route it to the existing zero-level current/crossing machinery M17-323/326/338--346.

Thus

\[
\boxed{
\text{sign-preserving scale migration}
\quad\text{and}\quad
\text{zero-level turnover}
}
\]

remain distinct canonical channels.

## 9. Relation to M17-379

M17-379 gives the cross-scale exposure ledger

\[
\sum_m\tau_m^{own}
\gtrsim
\log\frac1r.
\]

That theorem does not require one material coefficient value to move monotonically through all scales; the exposure can be distributed across labels and times.

Therefore one may not silently replace it by

\[
\mathcal A_{mig}\gtrsim\log(1/r).
\]

However, on the subbranch where the **same material label or same controlled family** is shown to traverse those scales in sign-preserving order, M17-393 gives precisely such a log-scale migration action.

If no such genealogy exists, retain the multi-label/cross-scale allocation branch instead.

## 10. Why M17-393 does not yet close the branch

No globally finite first-generation ledger has yet been certified for

\[
\boxed{
\int
\frac{|D_t\kappa|}{|\kappa|}dt.
}
\]

The physical constitutive law contains second-order weighted coefficient/strain diffusion and geometric terms.

These sit above the ordinary kinetic-energy level and may also become singular near coefficient interfaces or zeros.

Therefore

\[
\boxed{
\text{large coefficient scale migration}
\not\Rightarrow
\text{standard-energy contradiction}
}
\]

at the present stage.

What has been achieved is a precise reclassification of the old `coefficient-supercritical spike` escape.

## 11. Revised late-CE-H migration branch

The old terminal-looking branch

\[
G_{coefficient\ supercritical\ spike}
\]

is replaced by

\[
\boxed{
\begin{aligned}
G_{coefficient\ supercritical\ relative\ to\ current\ scale}
\Longrightarrow{}&
H_{smaller\ intrinsic\ own\text{-}scale\ cell}\\
&\lor G_{normalized\ coefficient\ gradient}\\
&\lor H_{sign\text{-}preserving\ log\text{-}scale\ migration\ action}\\
&\lor H_{zero\text{-}level\ crossing}\\
&\lor G_{interface/rank/domain/genealogy}.
\end{aligned}
}
\]

Thus a large coefficient is no longer an untyped endpoint.

It either creates a smaller scale, pays normalized spatial gradient, travels through coefficient scale, crosses zero, or loses the canonical domain.

## 12. DSD audit role

The DSD role is a scale-identity audit.

A coefficient may appear `supercritical` only because it is being compared with the wrong spatial clock.

The intrinsic quantity

\[
r_\kappa=|\kappa|^{-1/2}
\]

removes that ambiguity.

The time-dependent audit then uses the exact logarithmic derivative of this intrinsic scale.

All canonical mathematics is elementary differentiation plus the already established physical CE-H constitutive law and M17-381/382 coefficient-scale allocation.

## 13. Audit verdict

**PASS — coefficient-supercritical spike removed as an untyped terminal escape.**

The next unresolved payer is now sharper:

\[
\boxed{
\mathcal A_{mig}
=
\int
\frac{|D_t\kappa|}{|\kappa|}dt
}
\]

on sign-preserving scale-migration branches, together with the already separated zero-level current and normalized coefficient-gradient/interface exits.

The next highest-value calculation is to determine whether `A_mig` can be bounded or spatialized by an already certified critical coefficient-diffusion/zero-current ledger without reintroducing the M17-338 representation errors.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
