# M17-476 — Compact common-mode source return collapses to existing raw-H2 and palinstrophy ledgers with endpoint temporal thickening

**Date:** 2026-09-10  
**Status:** ACTIVE COMPACT COMMON-MODE COLLAPSE THEOREM / SOURCE-RETURN BRANCH COMPRESSION

## 1. Purpose

M17-466 reconstructed the sign-even geometric common mode from the certified Kato balance, M17-470--471 absorbed the regular zero-current and zero-level strain trace into bulk ledgers under compact finite-jet/tube hypotheses, and M17-475 supplied quantitative temporal thickening for endpoint raw-H2 spikes.

This module combines those results and removes the retained **compact common-mode source-return** scenario as an independent late-CE-H payer.

It does **not** prove a contradiction across generations. The resulting fixed normalized payments return to the already certified ancestry weights \(R^{-3}\) for raw-H2 and \(R^{-1}\) for palinstrophy.

## 2. Exact common-mode interval identity

The certified sign-moment balance is
\[
\dot A+2J_0
=-2C_{0\sigma}+2G_{\rm cm}+2S_A+2\Delta Q.
\]
Hence
\[
\boxed{
2G_{\rm cm}
=\dot A+2J_0+2C_{0\sigma}-2S_A-2\Delta Q.
}
\]
For \(I=[t_0,t_1]\),
\[
\boxed{
2\int_I G_{\rm cm}dt
=\Delta A
+2\int_IJ_0dt
+2\int_IC_{0\sigma}dt
-2\int_IS_Adt
-2\int_I\Delta Qdt.
}
\]

## 3. Compact record hypotheses

Assume on a normalized record interval \(I\):

1. exact whole-space smooth CE-H persists;
2. enstrophy and vorticity amplitude satisfy
\[
E(t)=\|\Omega(t)\|_2^2\le E_*,
\qquad
\|\Omega(t)\|_\infty\le M_*;
\]
3. the M17-470 regular zero-tube/level-flux compactness hypotheses hold, so
\[
\boxed{J_0\le C_JH_{\rm raw}};
\]
4. the M17-460/471 finite-jet trace hypotheses hold, so
\[
\boxed{|C_{0\sigma}|\le C_TH_{\rm raw}+C_PP};
\]
5. a backward CE-H/genealogy window of normalized length at least \(T_*>0\) is available ending at either endpoint whenever that endpoint is selected by the endpoint branch.

The constants \(E_*,M_*,C_J,C_T,C_P,T_*\) are record-uniform within the compact family.

## 4. Bulk absorption of all non-endpoint terms

M17-468 gives
\[
\boxed{|\Delta Q|\le H_{\rm raw}}.
\]
M17-462 gives
\[
|S_A|
\le C_SM_*E_*^{1/2}H_{\rm raw}^{1/2}.
\]
Therefore, writing
\[
X_I:=\int_IH_{\rm raw}dt,
\qquad
Y_I:=\int_IPdt,
\qquad
T_I:=|I|,
\]
we have
\[
\int_I|S_A|dt
\le
C_SM_*E_*^{1/2}T_I^{1/2}X_I^{1/2}.
\]
Consequently the exact interval identity implies
\[
\boxed{
2\left|\int_IG_{\rm cm}dt\right|
\le
|\Delta A|
+C_HX_I
+C_P'Y_I
+C_S M_*E_*^{1/2}T_I^{1/2}X_I^{1/2},
}
\]
where \(C_H,C_P',C_S\) depend only on the compact trace/tube constants.

Thus the regular zero current, zero-level trace, strain-weighted first moment, and sign-scale dispersion are no longer independent common-mode payers.

## 5. Quantitative compact dichotomy

Assume the normalized source-return cost satisfies
\[
\boxed{
\left|\int_IG_{\rm cm}dt\right|\ge g_*>0
}
\]
with \(T_I\le T^*\) uniformly on the retained record family.

Set
\[
B_*:=C_SM_*E_*^{1/2}(T^*)^{1/2}.
\]
Then
\[
2g_*
\le
|\Delta A|+C_HX_I+C_P'Y_I+B_*X_I^{1/2}.
\]
Hence there exists a constant
\[
c_*=c(g_*,E_*,M_*,T^*,C_H,C_P',C_S)>0
\]
such that at least one of the following holds:
\[
\boxed{|ΔA|\ge c_*},
\qquad
\boxed{X_I\ge c_*},
\qquad
\boxed{Y_I\ge c_*}.
\]

One explicit admissible choice is obtained by requiring each of the four right-hand contributions to be \(<g_*/2\):
\[
c_*
\le
\min\left\{
\frac{g_*}{2},
\frac{g_*}{2C_H},
\frac{g_*}{2C_P'},
\left(\frac{g_*}{2B_*}\right)^2
\right\},
\]
with the obvious convention if one coefficient vanishes.

Therefore a compact persistent common-mode source-return event must already pay a fixed normalized amount of endpoint first moment, raw-H2 spacetime mass, or palinstrophy.

## 6. Endpoint first moment becomes spacetime raw-H2

Assume the endpoint alternative
\[
|\Delta A|\ge c_*
\]
holds.
Since \(A(t)\ge0\), at least one endpoint \(t_e\in\{t_0,t_1\}\) satisfies
\[
A(t_e)\ge c_*.
\]
M17-469 gives
\[
A(t_e)^2\le E(t_e)H_{\rm raw}(t_e),
\]
so under \(E(t_e)\le E_*\),
\[
\boxed{
H_{\rm raw}(t_e)\ge h_*:=\frac{c_*^2}{E_*}.
}
\]

M17-475 applies on the backward CE-H window of length at least \(T_*\) ending at \(t_e\). Therefore
\[
\boxed{
\int_{t_e-T_*}^{t_e}H_{\rm raw}(t)dt
\ge
\frac{h_*}{2}
\min\left\{
T_*,
\frac{\log2}{C\left(M_*+E_*^{1/8}h_*^{3/8}\right)}
\right\}
=:q_*>0.
}
\]

Thus the endpoint branch is no longer a snapshot-only debt inside the compact family.

## 7. Compact common-mode collapse theorem

Combining Sections 5--6 gives the normalized theorem
\[
\boxed{
\begin{aligned}
G_{\rm cm}^{\rm compact,\ persistent}
\Longrightarrow{}&
G_{\rm raw\text{-}H^2}^{\rm fixed\ spacetime\ charge}\\
&\lor
G_{\rm palinstrophy}^{\rm fixed\ spacetime\ charge}.
\end{aligned}
}
\]

Equivalently, if neither bulk ledger pays a fixed normalized charge, then at least one compactness/persistence assumption must fail:
\[
\boxed{
\begin{aligned}
G_{\rm cm}
\Longrightarrow{}&
G_{\rm raw\text{-}H^2}
\lor G_P\\
&\lor G_{E\text{-decompactification}}
\lor G_{\rho_\infty\text{-decompactification}}\\
&\lor G_{\nabla\kappa/finite\text{-}jet\text{-}decompactification}\\
&\lor G_{\rm zero\text{-}tube/trace\ geometry\ loss}\\
&\lor G_{\rm CE\text{-}H/time\text{-}window/domain/genealogy\ loss}.
\end{aligned}
}
\]

No additional codimension-one or sign-dispersion common-mode payer remains inside the compact branch.

## 8. Ancestry audit: why this is not yet a contradiction

M17-467 and M17-404--405 give the raw-H2 ancestry law
\[
\boxed{
\sum_mR_m^{-3}
\int_IH_{{\rm raw},m}(s)ds<\infty.
}
\]
M17-307 gives the palinstrophy ancestry law
\[
\boxed{
\sum_mR_m^{-1}
\int_IP_m(s)ds<\infty.
}
\]

A fixed normalized payment \(q_*>0\) at every geometric record contributes only
\[
q_*\sum_mR_m^{-3}<\infty
\]
in raw-H2, or
\[
q_*\sum_mR_m^{-1}<\infty
\]
in palinstrophy.

Therefore
\[
\boxed{
\text{M17-476 closes the compact common-mode classification, not the global ancestry contradiction.}
}
\]

M17-473 remains the exact threshold firewall: a non-reusable normalized charge must grow roughly like \(R_m^3\) in the raw-H2 channel or \(R_m\) in the palinstrophy channel, or an equivalent non-summable allocation theorem must be proved.

## 9. Relation to prior late-M17 branches

M17-476 removes the following as independent compact common-mode mysteries:

- regular zero current \(J_0\);
- zero-level strain trace \(C_{0\sigma}\);
- sign-scale dispersion \(\Delta Q\);
- strain-weighted first moment \(S_A\);
- endpoint \(A\) as a snapshot-only payer;
- interval-integrated \(G_{\rm cm}\) as an independent terminal source.

The surviving common-mode exits are therefore decompactification, persistence loss, or the already-known finite ancestral ledgers.

## 10. Audit firewalls

- The theorem is conditional on a record-uniform compact family. Failure of any compactness constant is an explicit exit, not a hidden contradiction.
- The endpoint thickening is one-sided in time. A backward same-branch window is required at the selected endpoint.
- The result uses the whole-space velocity-vorticity structure inherited by M17-475.
- Fixed normalized raw-H2 or palinstrophy cost is ancestry-summable on geometric records.
- No termwise formula for \(\mathcal R_{\rm geom}\) is reconstructed here; M17-463 remains in force.

## 11. Next target

The common-mode compact interior is exhausted. The next useful audit is therefore not another decomposition of \(G_{\rm cm}\), but a threshold audit of its **exit branches** against M17-473:

1. normalized enstrophy decompactification;
2. vorticity-amplitude decompactification;
3. finite-jet/zero-tube/trace decompactification;
4. loss of backward CE-H/genealogy time window.

The question is which of these exits, if any, automatically carries record growth strong enough to defeat the \(R^{-3}\) or \(R^{-1}\) ancestry firewall, and which merely remain genuine OPEN noncompact branches.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
