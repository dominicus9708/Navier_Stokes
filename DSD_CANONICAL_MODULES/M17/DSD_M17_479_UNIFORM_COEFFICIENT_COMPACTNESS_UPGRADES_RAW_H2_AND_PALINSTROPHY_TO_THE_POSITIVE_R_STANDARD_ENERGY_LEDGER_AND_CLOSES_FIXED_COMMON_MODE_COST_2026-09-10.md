# M17-479 — Uniform coefficient compactness upgrades raw-H2 and palinstrophy to the positive-R standard-energy ledger and closes fixed common-mode cost

**Date:** 2026-09-10  
**Status:** ACTIVE STANDARD-ENERGY UPGRADE / COMPACT-COEFFICIENT COMMON-MODE CLOSURE

## 1. Purpose

M17-476 showed that on the compact common-mode branch a fixed normalized source-return event must pay either normalized spacetime raw-\(H^2\) or normalized spacetime palinstrophy. M17-472/473 audited those payments only against their derivative ledgers, with ancestry weights \(R^{-3}\) and \(R^{-1}\), which are summable on geometric records.

This module observes that when the normalized CE-H coefficient itself is uniformly bounded, both derivative resources are dominated by the vorticity enstrophy
\[
E=\|\Omega\|_2^2,
\]
whose spacetime integral is the standard kinetic-energy dissipation resource.

That changes the ancestry weight from a decaying derivative weight to a **positive record weight \(R\)**. Consequently a fixed normalized common-mode payment cannot persist through infinitely many large records on the compact-coefficient branch.

## 2. Standard kinetic-energy dissipation resource

For smooth divergence-free velocity in \(\mathbb R^3\) with the usual finite-energy decay,
\[
\frac12\|u(t_b)\|_2^2
+\nu\int_{t_a}^{t_b}\|\nabla u(t)\|_2^2dt
=
\frac12\|u(t_a)\|_2^2.
\]

In the whole-space divergence-free setting,
\[
\|\nabla u\|_2^2=\|\Omega\|_2^2=E.
\]
Thus the same standard-energy finite-dissipation hypothesis already used in the late-M17 standard-energy ledger supplies
\[
\boxed{
\int_{\mathcal T}E(t)dt<\infty
}
\]
on the certified parent time region \(\mathcal T\).

For a family of parent record windows with overlap bounded by \(B\),
\[
\sum_m\int_{R_m^2I_m}E(t)dt
\le
B\int_{\mathcal T}E(t)dt<\infty.
\]

## 3. Exact scaling of spacetime enstrophy

Under
\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s),
\]
we have
\[
E_R(s)
=\|\Omega_R(s)\|_2^2
=R\,E(R^2s).
\]
Hence
\[
\boxed{
\int_{I}E_R(s)ds
=R^{-1}
\int_{R^2I}E(t)dt.
}
\]

Equivalently, the parent-accounted cost of normalized spacetime enstrophy is
\[
\boxed{
R\int_I E_R(s)ds.
}
\]

Therefore bounded overlap yields the standard-energy ancestry ledger
\[
\boxed{
\sum_mR_m\int_{I_m}E_m(s)ds<\infty.
}
\]

This is the relevant positive-\(R\) ledger.

## 4. Raw-H2 domination by enstrophy under coefficient compactness

On exact CE-H,
\[
\Delta\Omega=\kappa\Omega.
\]
Thus
\[
H_{\rm raw}
=\|\Delta\Omega\|_2^2
=\int\kappa^2|\Omega|^2dx.
\]
If
\[
\|\kappa\|_\infty\le K_*,
\]
then pointwise in time
\[
\boxed{
H_{\rm raw}\le K_*^2E.
}
\]
Consequently
\[
\boxed{
\int_IH_{\rm raw}ds
\le K_*^2\int_IEds.
}
\]

For an ancestry family,
\[
\boxed{
\sum_mR_m
\int_{I_m}H_{{\rm raw},m}ds
\le
K_*^2
\sum_mR_m\int_{I_m}E_mds
<\infty.
}
\]

Thus on a uniformly coefficient-compact exact-CE-H branch, raw-\(H^2\) possesses a much stronger conditional ledger than the generic cubic \(R_m^{-3}\) ledger.

## 5. Palinstrophy domination by enstrophy under coefficient compactness

The whole-space exact CE-H identity from M17-455 gives
\[
P
=\|\nabla\Omega\|_2^2
=-\int\kappa|\Omega|^2dx.
\]
Therefore
\[
0\le P
\le
\|\kappa\|_\infty E.
\]
Under \(\|\kappa\|_\infty\le K_*\),
\[
\boxed{P\le K_*E.}
\]
Hence
\[
\boxed{
\sum_mR_m
\int_{I_m}P_mds
\le
K_*
\sum_mR_m\int_{I_m}E_mds
<\infty.
}
\]

Again this is much stronger than the generic M17-307 \(R_m^{-1}\) palinstrophy ancestry ledger, but only on the coefficient-compact exact-CE-H subbranch.

## 6. Fixed normalized derivative payment is impossible on infinitely many large records

Suppose \(R_m\to\infty\) and there is a fixed \(q_*>0\) such that on infinitely many bounded-overlap records either
\[
\int_{I_m}H_{{\rm raw},m}ds\ge q_*
\]
or
\[
\int_{I_m}P_mds\ge q_*.
\]

Under uniform coefficient compactness,
\[
\int_{I_m}E_mds
\ge
\min\left\{
\frac{q_*}{K_*^2},
\frac{q_*}{K_*}
\right\}
=:e_*>0.
\]
Therefore
\[
\sum_mR_m\int_{I_m}E_mds
\ge
e_*\sum_mR_m.
\]
Because \(R_m\to\infty\), the right-hand side diverges for any infinite record subsequence, contradicting the standard-energy ledger.

Thus
\[
\boxed{
\text{fixed normalized raw-H2 or palinstrophy payment cannot persist through infinitely many large coefficient-compact records.}
}
\]

## 7. Combination with M17-476

M17-476 gives, under the zero-tube/trace/time-window compactness assumptions, for fixed normalized common-mode cost
\[
\Gamma_m
:=
\left|\int_{I_m}G_{{\rm cm},m}ds\right|
\ge g_*>0,
\]
the dichotomy
\[
\int H_{{\rm raw},m}ds\ge c_H(g_*)
\quad\lor\quad
\int P_mds\ge c_P(g_*),
\]
unless one of its explicit compactness/genealogy exits occurs.

If in addition
\[
\|\kappa_m\|_\infty\le K_*
\]
uniformly and the standard-energy parent mapping has bounded overlap, Section 6 yields a contradiction for an infinite large-record family.

Therefore
\[
\boxed{
\begin{aligned}
G_{\rm persistent\ fixed\ common\text{-}mode\ cost}
\Longrightarrow{}&
G_{\kappa_\infty\text{-}decompactification}\\
&\lor G_{E/\rho_\infty\text{-}decompactification}\\
&\lor G_{\rm zero\text{-}tube/trace/high\text{-}jet\ loss}\\
&\lor G_{\rm endpoint\ time\text{-}window\ thinning}\\
&\lor G_{\rm ancestry\ overlap/genealogy\ loss}\\
&\lor G_{\rm interface/rank/domain\ loss}.
\end{aligned}
}
\]

The fully coefficient-compact common-mode subbranch is closed.

## 8. Why this does not contradict the cubic/inverse-record firewalls

The generic derivative ledgers remain correct:
\[
\sum_mR_m^{-3}\int H_m<\infty,
\qquad
\sum_mR_m^{-1}\int P_m<\infty.
\]

M17-479 adds extra structure:
\[
H_m\le K_*^2E_m,
\qquad
P_m\le K_*E_m.
\]
This lets the derivative cost be charged to a lower-order standard-energy resource whose scaling is different.

If \(K_*\) is not uniform, this upgrade fails and the generic derivative firewalls remain the correct fallback.

Thus there is no inconsistency:
\[
\boxed{
\text{positive-}R\text{ standard-energy closure is conditional on uniform normalized coefficient compactness.}
}
\]

## 9. Relation to M17-477 and M17-478

M17-477 already showed that endpoint-spike growth sufficient to challenge cubic ancestry forces \(\|\kappa\|_\infty\) to grow when enstrophy is bounded.

M17-479 explains why that coefficient decompactification is not optional: if \(\kappa\) stayed compact, standard energy would close the branch much earlier.

M17-478 further prevents pure intrinsic-scale re-recording from being counted as new ancestry charge. Therefore the surviving large-coefficient route must involve genuine scale-map change, non-reused multiplicity/residence, high-jet/interface structure, or genealogy loss.

## 10. Re-recording invariance of the standard-energy charge

Spacetime enstrophy scales as
\[
q_E[S_r\Omega]=r^{-1}q_E[\Omega].
\]
Its parent accounting uses the positive factor \(R\). Thus under scale composition,
\[
\boxed{
(Rr)\,q_E[S_r\Omega]
=(Rr)(r^{-1}q_E)
=Rq_E.
}
\]

Therefore the standard-energy parent charge is itself exactly invariant under one-to-one intrinsic-scale re-recording, consistent with the general M17-478 homogeneous-ledger principle.

## 11. Audit cautions

- The standard-energy upgrade requires the whole-space finite-energy/dissipation setting and the same representation-safe bounded-overlap parent mapping used by the existing late-M17 standard-energy arguments.
- The coefficient ceiling must hold on the support/time window to which the raw-\(H^2\) or palinstrophy payment is charged.
- If the coefficient bound grows with \(m\), no fixed positive-\(R\) lower bound follows without tracking that growth explicitly.
- Local cutoffs may create boundary terms; the theorem is stated for the certified bulk resources on mapped record windows.
- This does not close ROOT-CERT, non-CE-H roots, or genealogy/interface exits.

## 12. Audit status

Closed here:

- persistent fixed normalized common-mode cost on an infinite large-record exact-CE-H family with uniform coefficient, enstrophy/amplitude, zero-tube/trace/time-window compactness and bounded-overlap standard-energy ancestry;
- fixed normalized raw-\(H^2\) or palinstrophy payments as merely ancestry-summable on that coefficient-compact subbranch.

The correct stronger statement there is standard-energy contradiction.

Still OPEN:

- coefficient-amplitude decompactification and intrinsic-scale migration;
- non-reused multiplicity/residence after genuine scale refinement;
- coefficient-gradient/high-jet/interface exits;
- parent-to-record genealogy/scale-map persistence;
- ROOT-CERT and non-CE-H roots.

## 13. Next target

Track a decompactifying coefficient \(K_m=\|\kappa_m\|_\infty\) through the intrinsic rescaling
\[
r_m=K_m^{-1/2},
\qquad
\widehat R_m=R_mr_m.
\]
If \(\widehat R_m\to\infty\), the re-recorded coefficient-compact branch should again face the positive-\(\widehat R_m\) standard-energy closure. If \(\widehat R_m\) fails to diverge, that is a precise record-scale/genealogy mismatch rather than a hidden payer.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
