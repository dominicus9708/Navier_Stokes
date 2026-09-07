# DSD M17-348 — Scale-consistent interpolation audit shows finite palinstrophy plus Type-I enstrophy can pay fixed critical `Q_0` on geometric record windows

Date: 2026-09-08  
Canonical ID: **M17-348**

Status: **ACTIVE ANTI-SHORTCUT / CRITICAL-RESOURCE SCALING AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M17-346 gives on the compact fixed-segment branch a positive-density scale-critical spatial crossing currency

\[
\mathcal Q_0.
\]

M5-477 gives for the first marked ancient element

\[
\boxed{
\mathscr P_{anc}
:=
\int_{-\infty}^{0}\|\nabla\Omega\|_2^2dt
<\infty.
}
\]

At backward record times/windows with scale `R_m`, M5-477 also gives the Type-I enstrophy order

\[
\|\Omega(t)\|_2^2\sim R_m^{-1}
\]

when `|t|~R_m^2`.

The tempting shortcut is to combine finite palinstrophy with the critical `Q_0` and declare a contradiction.  This module audits that step.

## 2. Scaling of the two standard spacetime resources

On a record window `I_m^{anc}` define

\[
P_m
:=
\int_{I_m^{anc}}\|\nabla\Omega\|_2^2dt,
\]

and

\[
E_m
:=
\int_{I_m^{anc}}\|\Omega\|_2^2dt.
\]

Under parabolic blow-down to a unit window,

\[
P'_m=R_mP_m,
\]

whereas

\[
E'_m=R_m^{-1}E_m.
\]

Thus `P` has scale exponent `+1` and spacetime enstrophy `E` has exponent `-1`.

The product

\[
\boxed{(P_mE_m)^{1/2}}
\]

is scale critical.

## 3. Type-I size of spacetime enstrophy on a record window

A geometric record window has duration

\[
|I_m^{anc}|\asymp R_m^2.
\]

M5-477's Type-I enstrophy rate gives

\[
\|\Omega(t)\|_2^2\lesssim R_m^{-1}
\]

through the corresponding fixed-ratio time annulus.

Therefore

\[
\boxed{
E_m\lesssim R_m.
}
\]

This is large, not summable.

## 4. What a hypothetical critical interpolation would actually imply

Suppose optimistically that one could prove on each record window

\[
\boxed{
\mathcal Q_0(I_m^{anc})
\le C(P_mE_m)^{1/2}.
}
\]

This inequality is dimensionally compatible with the critical scaling.

If the recurrent descendant branch gives

\[
\mathcal Q_0(I_m^{anc})\ge q_*>0,
\]

then

\[
P_mE_m\ge c q_*^2.
\]

Using `E_m<=C R_m`,

\[
\boxed{
P_m\gtrsim\frac{q_*^2}{R_m}.
}
\]

But the record scales grow geometrically:

\[
R_m\asymp q^{m/2}.
\]

Hence

\[
\boxed{
\sum_m\frac1{R_m}<\infty.
}
\]

Therefore the forced palinstrophy lower costs are entirely compatible with

\[
\sum_mP_m<\infty.
\]

## 5. This is exactly the M17-307 scaling phenomenon again

The conclusion is not an accident.

A fixed critical descendant event can cost only order

\[
R_m^{-1}
\]

in the supercritical ancestral palinstrophy ledger.

Thus even a perfect critical interpolation of the schematic form

\[
Q_0\lesssim(P E)^{1/2}
\]

would **not** close the record genealogy.

It would recover the same geometrically summable inverse-record-scale price already isolated in M17-307.

## 6. Other obvious standard resources do not repair the problem

At one time,

\[
\|\Omega\|_2^2
\]

has scale exponent `+1`, just like palinstrophy spacetime cost, so positive powers of the two cannot by themselves make a critical quantity.

The time integral

\[
\int\|\Omega\|_\infty dt
\]

is scale critical, but the Type-I bound

\[
\|\Omega(t)\|_\infty\lesssim(-t)^{-1}
\]

allows an order-one contribution on every logarithmic record annulus.  Its total backward integral can therefore diverge logarithmically and is not a certified finite resource.

Similarly, M5-477 gives

\[
\int_{I_m}\|S\|_3^2dt=O(1)
\]

on geometric annuli, not a summable global critical budget.

## 7. Consequence

The route

\[
\boxed{
\text{positive critical }Q_0
+
\text{finite total palinstrophy}
\Longrightarrow
\text{contradiction}
}
\]

is rejected.

A genuine closure now requires one of:

1. a **finite scale-critical ancestral resource**, not presently known;
2. a rigidity theorem directly excluding positive recurrent `Q_0` on the dilation hull;
3. a tail-improvement theorem upgrading the hull into a known Liouville class such as strong global `L3`;
4. a genealogy theorem forcing more than the geometrically summable `R_m^{-1}` palinstrophy cost.

## 8. DSD-theory role

The useful heuristic is the separation of currencies by scaling dimension before attempting accumulation.

The mathematical audit is pure Navier--Stokes scaling plus the M5-477 Type-I estimates.

No DSD axiom is used as a proof premise.

## 9. Updated target

The highest-value live target is therefore

\[
\boxed{
\text{critical }Q_0
+\text{CE-H/dilation structure}
\Longrightarrow
\text{tail improvement or rigidity},
}
\]

not another conversion into palinstrophy.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
