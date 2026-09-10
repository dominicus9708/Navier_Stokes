# M17-476 — Compact common-mode source return collapses to raw-H2 or palinstrophy and has no independent terminal payer

**Date:** 2026-09-10  
**Status:** ACTIVE COMPACT-BRANCH COLLAPSE THEOREM / COMMON-MODE TERMINAL-PAYER ELIMINATION

## 1. Purpose

M17-466 reconstructed the sign-even geometry source exactly at interval level,
\[
2G_{\rm cm}
=\dot A+2J_0+2C_{0\sigma}-2S_A-2\Delta Q.
\]
M17-468--475 then classified every term on the right except for explicit compactness exits.

This module combines those results into one quantitative dichotomy. The objective is not to prove a contradiction, but to decide whether a fixed normalized common-mode event can survive as a new terminal payer.

The answer is no on the compact branch: it must pay either normalized raw-\(H^2\) or normalized palinstrophy, unless one of the stated compactness/genealogy hypotheses fails.

## 2. Certified interval identity

Let
\[
I=[t_0,t_1],
\qquad
\Gamma_I:=\left|\int_I G_{\rm cm}(t)\,dt\right|.
\]
Then M17-466 gives
\[
2\Gamma_I
\le
|\Delta A|
+2\int_IJ_0dt
+2\int_I|C_{0\sigma}|dt
+2\int_I|S_A|dt
+2\int_I|\Delta Q|dt.
\]

Write
\[
X_I:=\int_IH_{\rm raw}(t)dt,
\qquad
Y_I:=\int_IP(t)dt.
\]

## 3. Compact-branch hypotheses

Assume on a normalized record family:

1. **enstrophy compactness**
\[
E(t)=\|\Omega(t)\|_2^2\le E_*;
\]

2. **vorticity-amplitude compactness**
\[
\|\Omega(t)\|_\infty\le M_*;
\]

3. **regular zero-tube compactness**, sufficient for M17-470, so that
\[
\int_IJ_0dt\le C_JX_I;
\]

4. **zero-level trace compactness**, sufficient for M17-471, so that
\[
\int_I|C_{0\sigma}|dt
\le C_{CH}X_I+C_{CP}Y_I;
\]

5. the normalized interval length satisfies
\[
|I|\le T_*;
\]

6. any endpoint used by the endpoint branch possesses a backward same-generation smooth exact-CE-H window of normalized length at least \(\tau_*>0\), and those enlarged endpoint windows retain bounded overlap under ancestry mapping.

Failure of any item is kept as an explicit exit and is not silently absorbed into the theorem.

## 4. Bulk terms

M17-468 gives
\[
\int_I|\Delta Q|dt\le X_I.
\]

M17-462 gives
\[
|S_A|
\lesssim
M_*E_*^{1/2}H_{\rm raw}^{1/2}.
\]
Therefore Cauchy--Schwarz in time yields
\[
\int_I|S_A|dt
\le
C_SM_*E_*^{1/2}T_*^{1/2}X_I^{1/2}.
\]

Hence for constants depending only on the retained compact family,
\[
\boxed{
2\Gamma_I
\le
|\Delta A|
+C_HX_I
+C_PY_I
+C_{1/2}X_I^{1/2}.
}
\]

This already shows that the only non-bulk term left is the endpoint increment \(\Delta A\).

## 5. Endpoint branch

Assume
\[
\Gamma_I\ge g_*>0.
\]
Split into two cases.

### Case A: small endpoint increment

If
\[
|\Delta A|<g_*,
\]
then
\[
g_*
\le
C_HX_I+C_PY_I+C_{1/2}X_I^{1/2}.
\]
Therefore there exist explicit constants \(x_*(g_*)>0\), \(y_*(g_*)>0\) such that
\[
\boxed{
X_I\ge x_*
\quad\lor\quad
Y_I\ge y_*.
}
\]
For example one may take
\[
x_*
=
\min\left\{
\frac{g_*}{3C_H},
\left(\frac{g_*}{3C_{1/2}}\right)^2
\right\},
\qquad
 y_*=\frac{g_*}{3C_P},
\]
with the obvious convention if one coefficient vanishes.

### Case B: large endpoint increment

If
\[
|\Delta A|\ge g_*,
\]
then because \(A\ge0\), at least one endpoint satisfies
\[
A(t_i)\ge g_*.
\]
M17-469 gives
\[
H_{\rm raw}(t_i)
\ge
\frac{g_*^2}{E_*}
=:h_*.
\]

M17-475 then thickens this endpoint spike backward in time. On the certified endpoint window \(J_i\),
\[
\boxed{
\int_{J_i}H_{\rm raw}dt
\ge
\frac{h_*}{2}
\min\left\{
\tau_*,
\frac{\log2}{C(M_*+E_*^{1/8}h_*^{3/8})}
\right\}
=:q_*(g_*,E_*,M_*,\tau_*)>0.
}
\]

Thus the endpoint term also becomes a positive spacetime raw-\(H^2\) payment on the compact branch.

## 6. Compact common-mode collapse theorem

Let \(I^\sharp\) denote \(I\) enlarged only by the bounded endpoint windows required in Case B. Under the hypotheses of Section 3,
\[
\boxed{
\Gamma_I\ge g_*
\Longrightarrow
\int_{I^\sharp}H_{\rm raw}dt\ge c_H(g_*)
\quad\lor\quad
\int_IPdt\ge c_P(g_*),
}
\]
for positive constants depending only on the normalized compact family and \(g_*\).

Equivalently,
\[
\boxed{
G_{\rm cm}^{\rm fixed\ normalized\ interval\ cost}
\Rightarrow
G_{\rm raw\text{-}H^2}^{\rm fixed\ normalized\ cost}
\lor
G_{\rm palinstrophy}^{\rm fixed\ normalized\ cost}
\lor
G_{\rm compactness/genealogy\ exit}.
}
\]

There is no remaining independent common-mode terminal payer inside the retained compact branch.

## 7. Exact list of compactness exits

The theorem does not close the following failures:

- enstrophy decompactification;
- vorticity-amplitude decompactification;
- coefficient-gradient/high-jet loss in the zero-current thickening;
- zero-tube/level-flux collapse;
- zero-level trace/high-jet collapse;
- loss of the required backward CE-H endpoint window;
- bounded-overlap failure for the enlarged windows;
- parent-to-record scale-map/genealogy failure;
- interface/rank/domain loss.

These remain typed branches rather than hidden assumptions.

## 8. Ancestry audit

M17-467 and M17-404--405 give the raw-\(H^2\) ancestry ledger
\[
\boxed{
\sum_mR_m^{-3}
\int H_{{\rm raw},m}ds<\infty.
}
\]
M17-307 gives the palinstrophy ancestry ledger
\[
\boxed{
\sum_mR_m^{-1}
\int P_mds<\infty.
}
\]

Therefore a fixed normalized payment supplied by Section 6 is still compatible with geometric record scales:
\[
\sum_mR_m^{-3}<\infty,
\qquad
\sum_mR_m^{-1}<\infty.
\]

Hence
\[
\boxed{
\text{M17-476 closes the internal common-mode classification debt, not the ancestry summability firewall.}
}
\]

## 9. Consequence for the proof search

Continuing to decompose \(G_{\rm cm}\) term-by-term cannot by itself produce a contradiction on the compact branch. A successful next step must instead do at least one of the following:

- force non-reusable multiplicity/residence above the M17-473 weighted thresholds;
- force growth of the normalized raw-\(H^2\) or palinstrophy charge with record scale;
- convert one of the compactness exits into an already certified nonsummable resource;
- establish a stronger parent-to-record allocation theorem.

The M17-463 provenance firewall on the unverified termwise formula of \(\mathcal R_{\rm geom}\) remains in force; M17-476 does not need that formula.

## 10. Audit status

Closed/reduced here:

- common-mode geometry source as an independent interval terminal payer on the compact exact-CE-H branch;
- endpoint \(A\)-increment as an unthickened snapshot debt, provided the M17-475 endpoint window is available.

Still OPEN:

- M17-473 ancestry-threshold multiplicity/residence;
- decompactification exits in Section 7;
- coefficient-scale migration/high-jet branches;
- parent-to-M17 genealogy persistence;
- ROOT-CERT and the four non-CE-H roots.

## 11. Next target

The most direct remaining question is quantitative: can the endpoint-spike thickening from M17-475 grow rapidly enough with record scale to defeat the cubic \(R_m^{-3}\) ancestry weight? If not under compact coefficients, the endpoint route itself collapses into coefficient-scale decompactification/migration.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
