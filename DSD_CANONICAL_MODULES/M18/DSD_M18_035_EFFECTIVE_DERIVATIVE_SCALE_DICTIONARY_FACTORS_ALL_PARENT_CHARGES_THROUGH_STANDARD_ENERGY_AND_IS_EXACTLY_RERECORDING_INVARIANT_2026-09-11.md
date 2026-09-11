# M18-035 — Effective derivative-scale dictionary factors all parent charges through standard energy and is exactly rerecording invariant

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE SCALE-DICTIONARY AUDIT / PARENT-CHARGE FACTORIZATION / RERECORDING FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-032--034 introduced three spacetime effective coefficient/frequency scales on one exact-CE-H record:

\[
K_P^{\rm eff}
=\frac{q_P}{q_E},
\]

\[
K_H^{\rm eff}
=\left(\frac{q_H}{q_E}\right)^{1/2},
\]

and

\[
K_3^{\rm eff}
=\left(\frac{q_{J_3}}{q_E}\right)^{1/3}.
\]

All three scale like a coefficient, i.e. like inverse length squared.

This module compares them with the record factor \(R\) and rewrites every generic derivative parent charge as the standard-energy parent charge times a dimensionless internal-scale ratio.

## 2. Parent charges

Define

\[
C_E:=Rq_E,
\]

\[
C_P:=R^{-1}q_P,
\]

\[
C_H:=R^{-3}q_H,
\]

and

\[
C_3:=R^{-5}q_{J_3}.
\]

These are the parent-accounted standard-energy, palinstrophy, raw-H2, and D3 charges respectively.

## 3. Dimensionless effective scale ratios

Since the natural coefficient scale associated with record factor \(R\) is \(R^2\), define

\[
\boxed{
\zeta_P
:=
\frac{K_P^{\rm eff}}{R^2},
}
\]

\[
\boxed{
\zeta_H
:=
\frac{K_H^{\rm eff}}{R^2},
}
\]

and

\[
\boxed{
\zeta_3
:=
\frac{K_3^{\rm eff}}{R^2}.
}
\]

These are dimensionless.

## 4. Exact parent-charge factorization

From

\[
q_P=K_P^{\rm eff}q_E,
\]

we obtain

\[
C_P
=R^{-1}K_P^{\rm eff}q_E
=
\frac{K_P^{\rm eff}}{R^2}
(Rq_E).
\]

Hence

\[
\boxed{
C_P=\zeta_PC_E.
}
\]

Similarly,

\[
q_H=(K_H^{\rm eff})^2q_E
\]

gives

\[
\boxed{
C_H=\zeta_H^2C_E.
}
\]

Finally,

\[
q_{J_3}=(K_3^{\rm eff})^3q_E
\]

gives

\[
\boxed{
C_3=\zeta_3^3C_E.
}
\]

Thus

\[
\boxed{
(C_P,C_H,C_3)
=
(\zeta_P,\zeta_H^2,\zeta_3^3)
C_E.
}
\]

The generic derivative ledgers are therefore not unrelated currencies: on exact CE-H they are the standard-energy parent charge multiplied by invariant internal-scale ratios.

## 5. Spacetime log-convexity in scale-ratio form

M18-034 proved

\[
q_H^2\le q_Pq_{J_3}.
\]

Substituting the effective scales gives

\[
(K_H^{\rm eff})^4
\le
K_P^{\rm eff}(K_3^{\rm eff})^3.
\]

After division by \(R^8\),

\[
\boxed{
\zeta_H^4
\le
\zeta_P\zeta_3^3.
}
\]

This is a completely dimensionless record-level interpolation constraint.

Equivalently,

\[
\boxed{
\zeta_3
\ge
\zeta_H
\left(
\frac{\zeta_H}{\zeta_P}
\right)^{1/3}
}
\]

when \(\zeta_P>0\).

Thus RMS coefficient intermittency, \(\zeta_H/\zeta_P\gg1\), forces derivative-scale separation between D3 and the raw-H2 scale.

## 6. Exact rerecording invariance

Suppose one intrinsically rerecords the same event by factor \(r\).

The composed record factor is

\[
\widehat R=Rr.
\]

All coefficient-like effective scales transform as

\[
\widehat K^{\rm eff}=r^2K^{\rm eff}.
\]

Therefore

\[
\boxed{
\frac{\widehat K^{\rm eff}}{\widehat R^2}
=
\frac{r^2K^{\rm eff}}{R^2r^2}
=
\frac{K^{\rm eff}}{R^2}.
}
\]

Hence

\[
\boxed{
\widehat\zeta_P=\zeta_P,
\qquad
\widehat\zeta_H=\zeta_H,
\qquad
\widehat\zeta_3=\zeta_3.
}
\]

This extends the M18-009 / legacy M17-478 rerecording firewall to the effective derivative-scale dictionary.

## 7. Parent charges are likewise invariant

Under the same one-to-one rerecording, the homogeneous ancestry rule gives

\[
\widehat C_E=C_E,
\qquad
\widehat C_P=C_P,
\qquad
\widehat C_H=C_H,
\qquad
\widehat C_3=C_3.
\]

The factorization

\[
C_j=(\text{invariant scale ratio})\times C_E
\]

is therefore representation safe term by term.

No choice of intrinsic normalization can manufacture a new ancestry cost from the same event.

## 8. Compact internal-scale regime

If

\[
\zeta_P,
\zeta_H,
\zeta_3
\le C_*
\]

uniformly on a non-reused record family, then

\[
C_P+C_H+C_3
\lesssim
C_E.
\]

Therefore all three derivative parent charges are automatically controlled by the standard-energy parent ledger on that family.

In this regime, searching for a contradiction by repeatedly recounting derivative resources cannot outperform the standard-energy audit.

## 9. Genuine scale-separation regime

A derivative branch can become stronger than standard energy only through growth of its invariant scale ratio.

Specifically,

\[
C_P/C_E=\zeta_P,
\]

\[
C_H/C_E=\zeta_H^2,
\]

\[
C_3/C_E=\zeta_3^3.
\]

Thus surviving high-order concentration is canonically typed as

\[
\boxed{
G_{\rm derivative\ concentration}
\Longrightarrow
G_{\rm internal\ scale\ separation}
\lor
G_{\rm standard\ energy\ occupation}.
}
\]

This is sharper than tracking the raw normalized derivative norms alone.

## 10. D3-dominated intermittency

The M18-034 D3-dominated branch occurs when

\[
\frac{K_H^{\rm eff}}{K_P^{\rm eff}}
=
\frac{\zeta_H}{\zeta_P}
\gg1.
\]

Then Section 5 gives

\[
\frac{\zeta_3}{\zeta_H}
\ge
\left(
\frac{\zeta_H}{\zeta_P}
\right)^{1/3}
\gg1.
\]

Hence the branch necessarily has a hierarchy

\[
\boxed{
\zeta_3
\gg
\zeta_H
\gg
\zeta_P
}
\]

in the strongly intermittent limit, modulo the precise rates.

Thus the D3 branch is not merely 'large D3'; it is a genuine separation of internal derivative scales.

## 11. Genealogy implication

Because every \(\zeta\) is rerecording invariant, an infinite ancestry sequence with increasing

\[
\zeta_3,
\quad
\zeta_H/\zeta_P,
\quad\text{or}\quad
\zeta_H
\]

cannot be explained by repeated normalization of one fixed event.

It must represent at least one of:

- genuine change of the physical/parent scale distribution;
- distinct non-reused concentration events;
- failure of the assumed parent-to-record genealogy map;
- domain/interface/rank change.

This gives a clean criterion for distinguishing real scale separation from coordinate scale selection.

## 12. Economic priority after factorization

The preferred ancestry audit order is now:

1. test \(C_E\), the standard-energy parent occupation;
2. if energy occupation is small, inspect invariant scale ratios \(\zeta_P,\zeta_H,\zeta_3\);
3. only pursue a derivative branch when its \(\zeta\) genuinely grows;
4. never treat a rescaling-induced increase of a normalized derivative norm as new multiplicity.

This is the DSD ancestry analogue of separating amplitude from resolution.

## 13. Audit verdict

### Certified

1. All exact-CE-H derivative parent charges factor through the standard-energy parent charge and invariant effective scale ratios.
2. The scale ratios obey the dimensionless interpolation law \(\zeta_H^4\le\zeta_P\zeta_3^3\).
3. The ratios are exactly invariant under one-to-one intrinsic rerecording.
4. D3-dominated coefficient intermittency is a genuine internal scale-separation phenomenon, not a normalization artifact.

### Not certified

1. Divergence of any ancestry sum from scale-ratio growth alone.
2. Non-reused multiplicity of high-\(\zeta\) events.
3. Persistence of the parent-to-record map through all selected events.
4. Closure of the local distributed-gradient, second-jet geometry, or strain-weighted endpoints.
5. Global 3D Navier--Stokes regularity.

## 14. Next target

M18-036 should shift from currency size to **event counting**.

The central genealogy question is now:

> Given a sequence of high-\(\zeta\) records, when are two records genuinely distinct physical concentration events rather than different rerecordings, overlapping windows, or nested views of the same event?

The next audit should define a representation-safe non-reuse certificate using parent time support, material/spatial labels where available, and bounded overlap.