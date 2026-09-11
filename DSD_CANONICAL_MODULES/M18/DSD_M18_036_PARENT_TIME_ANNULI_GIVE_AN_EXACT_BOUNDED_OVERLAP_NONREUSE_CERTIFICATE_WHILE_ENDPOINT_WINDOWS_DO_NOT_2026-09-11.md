# M18-036 — Parent-time annuli give an exact bounded-overlap nonreuse certificate, while endpoint windows do not

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE GENEALOGY AUDIT / TIME-SUPPORT NONREUSE / ENDPOINT-NESTING FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-035 reduced the next global question to event counting:

> when do two high-scale records represent genuinely distinct parent events rather than overlapping or rerecorded views of the same event?

This module gives an exact time-support criterion.

The result is sharp at the organizational level:

- normalized time windows bounded away from the distinguished endpoint generate parent-time annuli with uniformly bounded overlap on geometric record scales;
- normalized windows touching the endpoint generate nested parent windows, so scale separation alone gives no nonreuse certificate.

## 2. Record time map

Under

\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]

a normalized descendant time interval

\[
I\subset(-\infty,0]
\]

maps to parent time support

\[
\boxed{T_R:=R^2I.}
\]

A representation-safe ancestry sum may count charges from many records only if these parent supports are disjoint or have uniformly bounded overlap, unless an independent material/spatial nonreuse label is available.

## 3. Annular normalized windows

Let

\[
I=[-b,-a],
\qquad
0<a<b<\infty.
\]

Then

\[
T_m
=[-bR_m^2,-aR_m^2].
\]

In absolute parent time \(\tau=-t>0\), this is the annulus

\[
\boxed{
A_m=[aR_m^2,bR_m^2].
}
\]

Assume geometric scale separation

\[
\boxed{
R_{m+1}\ge\lambda R_m,
\qquad
\lambda>1.
}
\]

## 4. Exact overlap-count bound

Fix one parent absolute time \(\tau>0\).

If

\[
\tau\in A_m,
\]

then

\[
aR_m^2\le\tau\le bR_m^2,
\]

so

\[
\frac{\tau}{b}
\le
R_m^2
\le
\frac{\tau}{a}.
\]

For two admissible record indices \(m<n\), geometric separation gives

\[
R_n^2
\ge
\lambda^{2(n-m)}R_m^2.
\]

But all admissible scales lie in a multiplicative interval of width

\[
\frac{\tau/a}{\tau/b}
=
\frac ba.
\]

Therefore the number of indices whose parent annulus can contain the same \(\tau\) is bounded by

\[
\boxed{
N_{time}
\le
1+\left\lceil
\frac{\log(b/a)}{2\log\lambda}
\right\rceil.
}
\]

This constant is independent of the number of records and of \(\tau\).

Hence

\[
\boxed{
\sum_m\mathbf 1_{T_m}(t)
\le
N_{time}
}
\]

for every parent time.

## 5. Automatic ancestry additivity on annular windows

Let \(r(t)\ge0\) be any parent resource density integrated only in time after the relevant spatial norm has already been taken.

Then

\[
\sum_m\int_{T_m}r(t)dt
\le
N_{time}
\int_{\cup_mT_m}r(t)dt.
\]

Thus a geometric sequence of annular record windows is automatically safe against unbounded temporal double counting.

This applies to the established parent-time ledgers whenever the record charge pulls back to such a nonnegative parent density.

## 6. Disjointness as a stronger special case

If

\[
\lambda^2a>b,
\]

then

\[
aR_{m+1}^2
> bR_m^2.
\]

Hence adjacent annuli are disjoint:

\[
oxed{A_m\cap A_{m+1}=\varnothing.}
\]

Therefore sufficiently separated geometric scales give exact temporal nonreuse without any additional labeling.

## 7. Endpoint windows

Now let

\[
I=[-b,0].
\]

Then

\[
T_m=[-bR_m^2,0].
\]

For increasing \(R_m\),

\[
T_1\subset T_2\subset T_3\subset\cdots.
\]

Thus every parent time near the endpoint belongs to arbitrarily many record windows.

Hence

\[
\boxed{
\text{geometric scale separation alone does not certify nonreuse for endpoint-touching windows.}
}
\]

This is the endpoint-nesting firewall.

## 8. Annular increments of endpoint windows

For nested endpoint windows, one may define the new parent-time increment

\[
D_m
:=
T_m\setminus T_{m-1}.
\]

These increments are disjoint by construction.

However, a descendant normalized charge \(q_m\) may be concentrated entirely in the old nested part

\[
T_{m-1}
\]

rather than in \(D_m\).

Therefore one must not replace the full record charge by an annular increment charge without proving an **increment-localization statement**.

Thus

\[
\boxed{
\text{nested windows} + \text{formal set difference}
\neq
\text{new ancestry payment}.
}
\]

## 9. Other valid nonreuse certificates

If time supports overlap strongly, independent nonreuse can still be certified by additional structure such as:

1. disjoint or bounded-overlap parent spacetime cells;
2. disjoint material-label sets transported by the flow;
3. disjoint spatial support at the same parent time, with a genuinely additive nonnegative resource;
4. separate interface/domain components with certified no-double-counting maps.

The essential requirement is always the same:

\[
\boxed{
\text{distinct record label}
\not\Rightarrow
\text{distinct physical event}.
}
\]

Distinctness must be proved in parent variables.

## 10. Relation to rerecording invariance

M18-009 and M18-035 show that one-to-one intrinsic rerecording preserves parent ancestry charge exactly.

M18-036 adds a support-level criterion:

- if two records map to the same or nested endpoint support and no independent nonreuse label exists, they cannot be counted as independent merely because their scales differ;
- if they map to bounded-overlap annular supports, temporal counting is legitimate up to the explicit constant \(N_{time}\).

This separates **charge invariance** from **event multiplicity**.

## 11. Consequence for ancestry thresholds

Suppose a normalized charge \(q_m\) has parent weight \(w(R_m)\).

For annular windows with bounded overlap, a divergence test of the form

\[
\sum_mw(R_m)q_m=\infty
\]

is a legitimate contradiction candidate against a finite parent ledger.

For nested endpoint windows, the same formal divergence is not meaningful until nonreuse or increment localization is separately established.

Thus the exact ancestry threshold and the nonreuse certificate are logically independent requirements.

## 12. Current genealogy split

The ancestry branch is refined to

\[
\boxed{
\begin{aligned}
G_{\rm repeated\ high\text{-}scale\ records}
\Longrightarrow{}&
G_{\rm annular\ bounded\ overlap}\\
&\lor G_{\rm independent\ material/spatial\ labels}\\
&\lor G_{\rm endpoint\ nesting/reuse}\\
&\lor G_{\rm parent\ map/domain\ loss}.
\end{aligned}
}
\]

Only the first two branches directly support multiplicity in an ancestry contradiction.

## 13. Audit verdict

### Certified

1. Geometric annular time windows have an explicit uniform overlap bound.
2. Sufficient scale separation makes them disjoint.
3. Endpoint-touching parent windows are nested and cannot be independently counted from scale separation alone.
4. Annular increments of nested windows require a separate localization theorem before they inherit record charge.
5. Event counting must be certified in parent variables.

### Not certified

1. That the current selected CE-H records use annular rather than endpoint windows in every ancestry argument.
2. Increment localization for nested endpoint records.
3. Material-label nonreuse for all surviving concentration events.
4. ROOT-CERT or non-CE-H branch completeness.
5. Global 3D Navier--Stokes regularity.

## 14. Next target

M18-037 should audit the actual genealogy architecture used by the surviving M17/M18 record arguments and classify each payment as one of:

\[
\text{annular-time safe},
\quad
\text{material/spatial-label safe},
\quad
\text{nested/reuse-unsafe},
\quad
\text{unknown map}.
\]

This is necessary before any accumulated ancestry divergence can be promoted from a formal series to a genuine contradiction.