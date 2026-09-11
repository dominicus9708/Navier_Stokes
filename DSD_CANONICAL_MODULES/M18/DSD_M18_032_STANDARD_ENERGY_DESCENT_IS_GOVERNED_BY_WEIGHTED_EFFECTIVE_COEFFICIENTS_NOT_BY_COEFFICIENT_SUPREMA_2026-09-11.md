# M18-032 — Standard-energy descent is governed by weighted effective coefficients, not by coefficient suprema

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE EFFECTIVE-COEFFICIENT AUDIT / SPECTATOR-SUPREMUM REMOVAL / EXACT ENERGY ACCOUNTING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-031 used

\[
K_m=\|\kappa_m\|_\infty
\]

to write the standard-energy lower bounds

\[
q_E\ge q_P/K_m,
\qquad
q_E\ge q_H/K_m^2.
\]

These inequalities are correct but can be very non-sharp. A coefficient supremum may decompactify on a set carrying negligible \(\rho^2\) weight and therefore may not actually weaken the energy descent.

This module replaces the supremum by exact spacetime weighted effective coefficients.

## 2. Record-window charges

On one exact-CE-H record window \(I\), define

\[
q_E
:=
\int_I\int_{\mathbb R^3}\rho^2dxdt,
\]

\[
q_P
:=
\int_I\|\nabla\Omega\|_2^2dt
=
-\int_I\int\kappa\rho^2dxdt,
\]

and

\[
q_H
:=
\int_I\|\Delta\Omega\|_2^2dt
=
\int_I\int\kappa^2\rho^2dxdt.
\]

Assume \(q_E>0\).

## 3. Effective palinstrophy coefficient

Define

\[
\boxed{
K_P^{\rm eff}
:=
\frac{q_P}{q_E}.
}
\]

Then exactly

\[
\boxed{
q_P=K_P^{\rm eff}q_E,
\qquad
q_E=\frac{q_P}{K_P^{\rm eff}}
}
\]

when \(q_P>0\).

Equivalently,

\[
K_P^{\rm eff}
=
-
\frac{
\iint_{I\times\mathbb R^3}
\kappa\rho^2dxdt
}{
\iint_{I\times\mathbb R^3}
\rho^2dxdt
}.
\]

Thus \(K_P^{\rm eff}\) is the negative signed coefficient mean seen by the spacetime vorticity-energy measure.

## 4. Effective raw-H2 coefficient

Define

\[
\boxed{
K_H^{\rm eff}
:=
\left(
\frac{q_H}{q_E}
\right)^{1/2}.
}
\]

Then exactly

\[
\boxed{
q_H=(K_H^{\rm eff})^2q_E,
\qquad
q_E=rac{q_H}{(K_H^{\rm eff})^2}.
}
\]

Equivalently,

\[
K_H^{\rm eff}
=
\left(
\frac{
\iint\kappa^2\rho^2dxdt
}{
\iint\rho^2dxdt
}
\right)^{1/2}.
\]

Thus \(K_H^{\rm eff}\) is the RMS coefficient seen by the same spacetime vorticity-energy measure.

## 5. Exact relation between the two effective coefficients

Spacetime Cauchy--Schwarz gives

\[
\left|\iint\kappa\rho^2\right|^2
\le
\left(\iint\rho^2\right)
\left(\iint\kappa^2\rho^2\right).
\]

Hence

\[
\boxed{
K_P^{\rm eff}
\le
K_H^{\rm eff}.
}
\]

The raw-H2 effective coefficient is therefore the stronger magnitude measure; the palinstrophy effective coefficient additionally records the signed imbalance required by

\[
P=-\int\kappa\rho^2\ge0.
\]

## 6. Relation to the supremum ceiling

If

\[
K_\infty
:=
\operatorname*{ess\,sup}_{I\times\mathbb R^3}|\kappa|,
\]

then

\[
\boxed{
K_P^{\rm eff}
\le
K_H^{\rm eff}
\le
K_\infty.
}
\]

Therefore

\[
K_\infty\to\infty
\]

does not imply either effective coefficient diverges.

A high coefficient value living on vanishing \(\rho^2\)-weighted spacetime mass is a **spectator coefficient spike** for the standard-energy descent.

## 7. Exact parent energy accounting

The standard kinetic-energy dissipation ledger is

\[
\sum_mR_mq_{E,m}<\infty.
\]

Using the effective coefficients gives the exact identities

\[
\boxed{
R_mq_{E,m}
=
R_m\frac{q_{P,m}}{K_{P,m}^{\rm eff}}
}
\]

and

\[
\boxed{
R_mq_{E,m}
=
R_m\frac{q_{H,m}}{(K_{H,m}^{\rm eff})^2}.
}
\]

Thus the canonical standard-energy ancestry tests are

\[
\boxed{
\sum_m
R_m\frac{q_{P,m}}{K_{P,m}^{\rm eff}}
<\infty
}
\]

and

\[
\boxed{
\sum_m
R_m\frac{q_{H,m}}{(K_{H,m}^{\rm eff})^2}
<\infty.
}
\]

These are not estimates. They are two representations of the same parent energy charge on exact CE-H.

## 8. Correct survival thresholds

Suppose on a geometric record sequence

\[
q_{P,m}\gtrsim R_m^\alpha,
\qquad
K_{P,m}^{\rm eff}\asymp R_m^\kappa.
\]

Then the standard-energy term behaves like

\[
R_m^{1+\alpha-\kappa}.
\]

For a one-record-per-geometric-scale sequence, survival requires

\[
\boxed{
\kappa>1+\alpha.
}
\]

For a fixed palinstrophy spacetime payment \(\alpha=0\), this reduces to

\[
\boxed{
K_{P,m}^{\rm eff}\text{ must grow faster than }R_m.
}
\]

Similarly, if

\[
q_{H,m}\gtrsim R_m^\beta,
\qquad
K_{H,m}^{\rm eff}\asymp R_m^\lambda,
\]

then survival requires

\[
\boxed{
\lambda>\frac{1+\beta}{2}.
}
\]

For fixed raw-H2 payment, the effective RMS coefficient must grow faster than \(R_m^{1/2}\).

## 9. Insert M18-025 palinstrophy thickening

If endpoint palinstrophy heights satisfy

\[
p_m\asymp R_m^\eta
\]

and the crossing branch of M18-025 dominates, then

\[
q_{P,m}\gtrsim p_m^{1/3}\asymp R_m^{\eta/3}.
\]

The exact standard-energy survival condition becomes

\[
\boxed{
K_{P,m}^{\rm eff}
\text{ must grow faster than }
R_m^{1+\eta/3}.
}
\]

This is stronger than a condition on \(\|\kappa\|_\infty\): the coefficient growth must be visible to the same spacetime \(\rho^2\) measure that carries the palinstrophy payment.

## 10. Insert raw-H2 temporal thickening

In the large-height regime where M18-006 gives

\[
q_{H,m}\gtrsim h_m^{5/8}
\]

and

\[
h_m\asymp R_m^\eta,
\]

one has

\[
q_{H,m}\gtrsim R_m^{5\eta/8}.
\]

Thus survival requires

\[
\boxed{
K_{H,m}^{\rm eff}
\text{ to grow faster than }
R_m^{1/2+5\eta/16}.
}
\]

Again only weighted effective coefficient growth matters.

## 11. Effective coefficient decompactification is a real branch

M18-031 listed coefficient-amplitude decompactification as a primary CE-H escape. M18-032 sharpens this to

\[
\boxed{
G_{\rm coefficient\ decompactification}^{\rm relevant}
=
G_{K_P^{\rm eff}\to\infty}
\lor
G_{K_H^{\rm eff}\to\infty},
}
\]

with the required rates determined by the exact parent energy charge.

Pure supremum growth with bounded effective coefficients does not neutralize the standard-energy contradiction and is therefore not a canonical genealogy escape.

## 12. Representation safety

Under record scaling,

\[
K_{P,R}^{\rm eff}=R^2K_P^{\rm eff},
\qquad
K_{H,R}^{\rm eff}=R^2K_H^{\rm eff}.
\]

This is exactly the coefficient scaling.

The parent standard-energy charges

\[
R\frac{q_P}{K_P^{\rm eff}},
\qquad
R\frac{q_H}{(K_H^{\rm eff})^2}
\]

are invariant under one-to-one intrinsic rerecording once all scaling factors are transformed together. Therefore mere normalization cannot manufacture the required effective-coefficient growth.

## 13. New canonical ancestry split

For palinstrophy/raw-H2-producing CE-H records,

\[
\boxed{
\begin{aligned}
G_{\rm repeated\ derivative\ payment}
\Longrightarrow{}&
G_{\rm standard\ energy\ contradiction}\\
&\lor G_{\rm weighted\ effective\ coefficient\ growth}\\
&\lor G_{\rm ancestry\ overlap/nonreuse\ failure}\\
&\lor G_{\rm record\ window/domain/genealogy\ loss}.
\end{aligned}
}
\]

The supremum coefficient is no longer a canonical branch unless its growth is accompanied by effective weighted growth.

## 14. Audit verdict

### Certified

1. The exact energy descent is governed by \(K_P^{\rm eff}\) and \(K_H^{\rm eff}\).
2. Coefficient supremum decompactification can be a spectator phenomenon.
3. The standard-energy ancestry cost can be written exactly using effective coefficients.
4. The effective RMS coefficient dominates the effective signed palinstrophy coefficient.
5. The power-law survival thresholds in M18-031 sharpen by replacing \(K_\infty\) with the corresponding weighted effective coefficient.

### Not certified

1. An upper bound on either effective coefficient along the retained genealogy.
2. A positive weighted mass fraction at coefficient magnitude comparable to \(K_H^{\rm eff}\).
3. Divergence of the standard-energy series for the actual record sequence.
4. Non-reuse/bounded-overlap genealogy for every selected local event.
5. Global 3D Navier--Stokes regularity.

## 15. Next target

M18-033 should audit what large effective coefficient actually means as a coefficient-distribution statement under the normalized spacetime measure

\[
d\mu
=
\frac{\rho^2dxdt}{q_E}.
\]

The natural split is between:

- coherent signed coefficient drift, where \(K_P^{\rm eff}\) is comparable to \(K_H^{\rm eff}\);
- variance/tail decompactification, where \(K_H^{\rm eff}\gg K_P^{\rm eff}\).

This should determine whether effective coefficient growth can be tied to sign-separated raw-H2/palinstrophy payments or remains a genuine heavy-tail distribution endpoint.