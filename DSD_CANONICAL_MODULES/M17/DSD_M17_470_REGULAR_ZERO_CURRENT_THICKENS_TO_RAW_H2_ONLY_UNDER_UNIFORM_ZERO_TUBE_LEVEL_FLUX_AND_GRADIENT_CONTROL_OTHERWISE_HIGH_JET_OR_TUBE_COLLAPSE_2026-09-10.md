# M17-470 — Regular zero current thickens to raw-H2 only under uniform zero-tube level-flux and gradient control; otherwise high-jet or tube collapse remains

**Date:** 2026-09-10  
**Status:** ACTIVE ZERO-CURRENT THICKENING / RAW-H2 OR HIGH-JET-TUBE DICHOTOMY

## 1. Scope and provenance firewall

This module starts only from the currently certified regular zero-current quantity
\[
J_0
:=
\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|\,dS
=
\int \rho^2\delta(\kappa)|\nabla\kappa|^2\,dx.
\]

A historical M17-409 module appears to have used a related zero-level/coarea corridor quantity, but its exact symbol-level formula was not reliably recovered during this audit. Therefore **no identity with M17-409 is assumed here**. If that source is later recovered, equivalence or overlap must be checked explicitly rather than inferred from naming.

The purpose of M17-470 is to state the exact assumptions needed to convert \(J_0\), a codimension-one current, into a bulk near-zero coefficient cost.

## 2. Level-current function

For regular levels \(s\) in a zero tube, define
\[
F(s)
:=
\int_{\{\kappa=s\}}\rho^2|\nabla\kappa|\,dS.
\]
Then
\[
\boxed{F(0)=J_0.}
\]

The coarea formula gives, for \(\delta>0\),
\[
\boxed{
\int_{\{|\kappa|<\delta\}}
\rho^2|\nabla\kappa|^2\,dx
=
\int_{-\delta}^{\delta}F(s)\,ds.
}
\]

This identity is exact whenever the coarea integrals are well-defined.

## 3. Why regularity at one level is insufficient

For each fixed smooth record, regularity of the zero level can yield a small local tube in which nearby levels remain regular. However the width of that tube can shrink from record to record.

Therefore the implication
\[
J_0\gtrsim1
\quad\Longrightarrow\quad
\int_{|\kappa|<\delta_*}\rho^2|\nabla\kappa|^2dx\gtrsim1
\]
with a **record-uniform** \(\delta_*>0\) is not certified by zero-level regularity alone.

A uniform lower bound requires a quantitative zero-tube hypothesis.

## 4. Uniform level-current stability hypothesis

Assume that on the retained normalized record family there exist constants
\[
\delta_0>0,
\qquad
c_0\in(0,1],
\]
independent of the record, such that
\[
\boxed{
F(s)\ge c_0F(0)=c_0J_0
\qquad
\text{for all }|s|\le\delta_0.
}
\]

A sufficient geometric route would be a record-uniform regular zero tube with controlled level-set Jacobians and controlled variation of \(\rho^2|\nabla\kappa|\), but this module uses only the displayed level-current stability as the certified hypothesis.

Then coarea immediately gives
\[
\boxed{
\int_{\{|\kappa|<\delta_0\}}
\rho^2|\nabla\kappa|^2dx
\ge
2c_0\delta_0J_0.
}
\]

Thus a nontrivial zero current forces a bulk coefficient-gradient charge unless the uniform level-current tube collapses.

## 5. Raw-H2 thickening needs an additional gradient ceiling

Define the raw-H2 content of the near-zero slab,
\[
H_{0,\delta}
:=
\int_{\{|\kappa|<\delta\}}
\kappa^2\rho^2dx.
\]

Coarea gives
\[
\boxed{
H_{0,\delta}
=
\int_{-\delta}^{\delta}
s^2
\left(
\int_{\{\kappa=s\}}
\frac{\rho^2}{|\nabla\kappa|}\,dS
\right)ds.
}
\]

Assume in addition a record-uniform upper gradient bound throughout the zero tube,
\[
\boxed{|\nabla\kappa|\le G_*<\infty.}
\]
At regular points,
\[
\frac1{|\nabla\kappa|}
\ge
\frac{|\nabla\kappa|}{G_*^2}.
\]
Therefore
\[
\int_{\{\kappa=s\}}
\frac{\rho^2}{|\nabla\kappa|}dS
\ge
G_*^{-2}F(s).
\]
Using the uniform level-current stability,
\[
\begin{aligned}
H_{0,\delta_0}
&\ge
G_*^{-2}
\int_{-\delta_0}^{\delta_0}s^2F(s)ds\\
&\ge
c_0G_*^{-2}J_0
\int_{-\delta_0}^{\delta_0}s^2ds.
\end{aligned}
\]
Hence
\[
\boxed{
H_{0,\delta_0}
\ge
\frac{2c_0}{3}
\frac{\delta_0^3}{G_*^2}
J_0.
}
\]
Equivalently,
\[
\boxed{
J_0
\le
\frac{3G_*^2}{2c_0\delta_0^3}
H_{0,\delta_0}
\le
\frac{3G_*^2}{2c_0\delta_0^3}
H_{\rm raw}.
}
\]

This is the desired zero-current-to-raw-H2 corridor, but only under explicit record-uniform tube and gradient control.

## 6. Spacetime consequence

If the constants \((\delta_0,c_0,G_*)\) are uniform over a time interval \(I\), then
\[
\boxed{
\int_IJ_0(t)dt
\le
C(\delta_0,c_0,G_*)
\int_IH_{\rm raw}(t)dt.
}
\]

Thus the zero-current branch is absorbed into the already-certified raw-H2 spacetime ledger on compact zero-tube/high-jet families.

## 7. Exact failure dichotomy

If a persistent \(J_0\) cannot be paid by the raw-H2 corridor above, at least one of the quantitative assumptions must fail. Therefore
\[
\boxed{
G_{J_0}
\Longrightarrow
G_{\rm raw\text{-}H^2}
\ \lor\ 
G_{\nabla\kappa\text{-}high\text{-}jet}
\ \lor\ 
G_{\rm zero\text{-}tube/level\text{-}flux\ collapse}.
}
\]

More explicitly:

- \(G_*\to\infty\): coefficient-gradient/high-jet decompactification;
- \(\delta_0\to0\): zero-tube thickness collapse;
- \(c_0\to0\): nearby level-current collapse/level-set degeneration;
- otherwise \(J_0\lesssim H_{\rm raw}\).

If one wants a literal smooth tubular foliation for every \(|s|\le\delta_0\), a record-uniform lower gradient bound \(|\nabla\kappa|\ge g_*>0\) may be imposed as part of the zero-tube regularity package. Failure of such a lower bound is included in the zero-tube/critical-level degeneration exit.

## 8. Local model proving the thickness firewall is necessary

Take a smooth local model
\[
\kappa(x)=x_1,
\qquad
\rho\approx\rho_0>0
\]
on a fixed transverse cross-section of area \(A_\perp\).

Then
\[
J_0
\asymp
\rho_0^2A_\perp.
\]
But
\[
H_{0,\delta}
\asymp
\rho_0^2A_\perp
\int_{-\delta}^{\delta}s^2ds
=
\frac23\delta^3J_0.
\]
Hence
\[
H_{0,\delta}\to0
\qquad\text{as }\delta\to0
\]
while \(J_0\) stays fixed.

Therefore a codimension-one zero current by itself cannot force a record-uniform raw-H2 payment. A uniform coefficient-thickness/tube hypothesis is genuinely necessary.

## 9. Scaling audit

Under the certified scaling
\[
\kappa_R=R^2\kappa,
\qquad
\nabla\kappa_R=R^3\nabla\kappa,
\]
we have
\[
J_{0,R}=R^5J_0,
\qquad
H_{{\rm raw},R}=R^5H_{\rm raw}.
\]
Moreover
\[
\delta_{0,R}=R^2\delta_0,
\qquad
G_{*,R}=R^3G_*.
\]
Thus
\[
\frac{\delta_{0,R}^3}{G_{*,R}^2}
=
\frac{\delta_0^3}{G_*^2},
\]
so the M17-470 thickening inequality is exactly scale-covariant.

After time integration both sides carry the cubic ancestry factor \(R^3\), consistent with M17-467.

## 10. Consequence for the current frontier

On a record family with compact normalized zero-tube and coefficient-gradient geometry,
\[
\boxed{G_{J_0}\subseteq G_{\rm raw\text{-}H^2}.}
\]

The independent residue is therefore not the zero current itself but the failure of the uniform thickening package:
\[
\boxed{
G_{J_0}^{\rm residual}
\subseteq
G_{\nabla\kappa\text{-}high\text{-}jet}
\lor
G_{\rm zero\text{-}tube/level\text{-}flux\ collapse}.
}
\]

## 11. Audit status

Closed/reduced here:

- regular zero-current as an independent bulk payer under uniform tube/gradient control;
- any unconditional claim that zero-level regularity alone implies a record-uniform raw-H2 charge.

Still OPEN:

- whether the retained CE-H record family possesses a uniform zero tube;
- whether normalized \(|\nabla\kappa|\) is uniformly bounded there;
- whether zero-level strain trace can be absorbed simultaneously with the same tube assumptions;
- non-summable use of the raw-H2 ledger despite cubic ancestry;
- temporal thickening of endpoint raw-H2 spikes;
- verified termwise provenance of \(\mathcal R_{\rm geom}\);
- inherited genealogy/interface/domain and root-level dependencies.

## 12. Next target

Combine M17-460 and M17-470. Under simultaneous zero-tube and trace-thickening compactness, test whether
\[
C_{0\sigma}
\]
reduces completely to raw-H2 plus palinstrophy, leaving only high-jet/tube collapse as the trace escape.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
