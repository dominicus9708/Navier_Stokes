# M17-467 — The entire A-balance has cubic spacetime ancestry scaling and fixed normalized common-mode payments are record-scale summable

**Date:** 2026-09-10  
**Status:** ACTIVE ANCESTRY-SCALING FIREWALL / COMMON-MODE PAYER AUDIT

## 1. Scope

M17-466 reduced the interval-integrated common-mode geometry source to the exact \(A\)-balance. This module audits the Navier–Stokes scaling of every term in that balance.

No termwise formula for \(\mathcal R_{\rm geom}\) is assumed.

We use the certified rescaling convention already fixed in M17-306–307:
\[
\Omega_R(y,s)=R^2\Omega(Ry,R^2s).
\]
For velocity,
\[
u_R(y,s)=R\,u(Ry,R^2s),
\]
so the strain scales as
\[
\Sigma_R(y,s)=R^2\Sigma(Ry,R^2s).
\]
On exact CE-H,
\[
\Delta\Omega=\kappa\Omega,
\]
which implies
\[
\boxed{
\kappa_R(y,s)=R^2\kappa(Ry,R^2s).
}
\]
Also
\[
\rho_R=|\Omega_R|=R^2\rho,
\qquad
dy=R^{-3}dx,
\qquad
ds=R^{-2}dt.
\]

## 2. Endpoint first moment A

Recall
\[
A(t)=\int |\kappa|\rho^2\,dx.
\]
Then
\[
A_R(s)
=
\int |\kappa_R|\rho_R^2\,dy
=
R^{2+4-3}A(t),
\]
so
\[
\boxed{A_R=R^3A.}
\]
Therefore a fixed normalized endpoint value \(A_R\sim1\) corresponds to parent value
\[
\boxed{A\sim R^{-3}.}
\]

The same scaling holds for \(K_\pm\) and \(P=K_--K_+\).

## 3. Zero-current J0

Recall
\[
J_0
=
\int\rho^2\delta(\kappa)|\nabla\kappa|^2\,dx.
\]
The factors scale as
\[
\rho_R^2=R^4\rho^2,
\qquad
\delta(\kappa_R)=R^{-2}\delta(\kappa),
\qquad
|\nabla_y\kappa_R|^2=R^6|\nabla_x\kappa|^2.
\]
Hence
\[
\boxed{J_{0,R}=R^5J_0.}
\]
After time integration,
\[
\boxed{
\int J_{0,R}\,ds
=
R^3\int J_0\,dt.
}
\]
Thus a fixed normalized zero-current charge corresponds to a parent charge of order \(R^{-3}\).

## 4. Zero-level strain trace C_{0sigma}

For an exact CE-H strain eigenvalue \(\sigma\),
\[
\sigma_R=R^2\sigma,
\qquad
\nabla_y\sigma_R=R^3\nabla_x\sigma.
\]
Using the regular-level surface form
\[
C_{0\sigma}
=
\int_{\{\kappa=0\}}\rho^2\partial_n\sigma\,dS,
\]
and
\[
dS_y=R^{-2}dS_x,
\]
we obtain
\[
\boxed{C_{0\sigma,R}=R^5C_{0\sigma}.}
\]
Therefore
\[
\boxed{
\int C_{0\sigma,R}\,ds
=
R^3\int C_{0\sigma}\,dt.
}
\]
This scaling statement does not remove the M17-460 trace/high-jet firewall.

## 5. Strain-weighted first-moment source S_A

With
\[
S_A=\int |\kappa|\sigma\rho^2\,dx,
\]
we have
\[
\boxed{S_{A,R}=R^5S_A,}
\]
and hence
\[
\boxed{
\int S_{A,R}\,ds
=
R^3\int S_A\,dt.
}
\]

## 6. Second-moment sign asymmetry Delta Q

For
\[
Q_\pm=\int\kappa_\pm^2\rho^2\,dx,
\qquad
\Delta Q=Q_+-Q_-,
\]
we obtain
\[
\boxed{Q_{\pm,R}=R^5Q_\pm,}
\qquad
\boxed{\Delta Q_R=R^5\Delta Q.}
\]
Therefore
\[
\boxed{
\int\Delta Q_R\,ds
=
R^3\int\Delta Q\,dt.
}
\]

## 7. Common-mode geometry source

The exact balance from M17-465 is
\[
\dot A+2J_0
=
-2C_{0\sigma}
+2G_{\rm cm}
+2S_A
+2\Delta Q.
\]
Since
\[
A_R=R^3A
\]
and \(t=R^2s\),
\[
\partial_sA_R=R^5\partial_tA.
\]
All other certified terms in the balance scale as \(R^5\). Therefore balance covariance itself forces
\[
\boxed{G_{{\rm cm},R}=R^5G_{\rm cm}}
\]
without requiring a termwise formula for \(\mathcal R_{\rm geom}\).

Hence
\[
\boxed{
\int G_{{\rm cm},R}\,ds
=
R^3\int G_{\rm cm}\,dt.
}
\]

## 8. Cubic ancestry firewall

For every spacetime term in the \(A\)-balance,
\[
\boxed{
\mathcal L_R^{\rm normalized}
=
R^3\mathcal L^{\rm parent}.
}
\]
Equivalently,
\[
\boxed{
\mathcal L^{\rm parent}
=
R^{-3}\mathcal L_R^{\rm normalized}.
}
\]

Thus if a descendant/normalized record pays a fixed order-one amount at each record scale \(R_m\), the corresponding parent ledger is bounded by
\[
\sum_m CR_m^{-3}.
\]
For geometric record scales,
\[
\boxed{
\sum_mR_m^{-3}<\infty.
}
\]

Therefore a fixed normalized payment in the M17-466 common-mode source-return balance is **ancestry-summable** and by itself cannot contradict the parent solution.

This is a stronger summability firewall than the M17-307 palinstrophy weight \(R^{-1}\).

## 9. Relation to raw-H2

The exact CE-H raw second-derivative ledger is
\[
H_{\rm raw}=\int|\Delta\Omega|^2dx
=\int\kappa^2\rho^2dx.
\]
It has instantaneous scaling
\[
H_{{\rm raw},R}=R^5H_{\rm raw}
\]
and spacetime scaling
\[
\boxed{
\int H_{{\rm raw},R}ds
=
R^3\int H_{\rm raw}dt.
}
\]
Thus the cubic scaling found above is consistent with the already-known raw-\(H^2\) ancestry firewall.

This module concerns exact rescaling of a ledger. It does not assert that every lower bound produced in a different time parametrization has the same numerical dependence on \(R\); such lower bounds must first be expressed in the certified normalized coordinates before ancestry conversion.

## 10. Consequence for the current frontier

Combining M17-466 and M17-467,
\[
\boxed{
\begin{aligned}
G_{\rm cm}^{\rm persistent}
\Longrightarrow{}&
G_{\Delta A/J_0}^{\rm cubic\ ancestry\ summable}\\
&\lor G_{\rm trace/high\text{-}jet}\\
&\lor G_{\rm raw\text{-}H^2}^{\rm cubic\ ancestry\ summable}\\
&\lor G_{\rm sign\text{-}dependent\ coefficient\text{-}scale\ dispersion}\\
&\lor G_{\rm interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

Accordingly the common-mode geometry source does not furnish a non-summable contradiction route unless an additional theorem upgrades one of the surviving branches to a stronger scale cost or prevents repeated record-scale summability.

## 11. Audit status

Closed/reduced here:

- exact scaling of \(A\);
- exact scaling of \(J_0\);
- exact scaling of \(C_{0\sigma}\) on regular zero levels;
- exact scaling of \(S_A\) and \(\Delta Q\);
- balance-implied scaling of \(G_{\rm cm}\);
- fixed-normalized-payment ancestry audit.

Still OPEN:

- termwise provenance of \(\mathcal R_{\rm geom}\);
- trace/high-jet decompactification;
- sign-dependent coefficient-scale dispersion;
- any theorem producing a non-summable scale lower bound;
- genealogy/interface/domain persistence;
- inherited ROOT-CERT and non-CE-H root branches.

## 12. Next target

The narrowest new algebraic branch is the M17-461 coefficient-scale dispersion channel. The next module should test whether \(\Delta Q\neq0\) under \(P\approx0\) can be represented as a signed transport/migration of first-moment mass between the disjoint coefficient bins of M17-381, and whether this yields any non-reusable scale ledger rather than another ancestry-summable rearrangement.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
