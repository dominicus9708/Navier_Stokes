# M17-468 — Second-moment sign-scale dispersion is pointwise dominated by raw-H2 and is not an independent payer or dynamic migration theorem

**Date:** 2026-09-10  
**Status:** ACTIVE SCALE-DISPERSION COLLAPSE / RAW-H2 DOMINATION FIREWALL

## 1. Scope

M17-461 identified the second-moment sign asymmetry
\[
\Delta Q=Q_+-Q_-
\]
as a diagnostic of positive/negative coefficient-magnitude separation when the first-moment imbalance \(P\) is small.

This module asks a narrower question: does \(\Delta Q\) form an independent resource/payer branch in the M17-466 common-mode balance?

The answer is no.

## 2. Exact raw-H2 identity

On exact CE-H,
\[
\Delta\Omega=\kappa\Omega,
\qquad
\rho=|\Omega|.
\]
Define
\[
Q_+
:=
\int \kappa_+^2\rho^2\,dx,
\qquad
Q_-
:=
\int \kappa_-^2\rho^2\,dx.
\]
Because
\[
\kappa^2=\kappa_+^2+\kappa_-^2
\]
pointwise,
\[
\boxed{
H_{\rm raw}
:=
\int|\Delta\Omega|^2dx
=
\int\kappa^2\rho^2dx
=
Q_++Q_-.
}
\]
Meanwhile
\[
\boxed{\Delta Q=Q_+-Q_-.}
\]
Since \(Q_\pm\ge0\),
\[
\boxed{
|\Delta Q|
\le
Q_++Q_-
=
H_{\rm raw}.
}
\]
This is exact and requires no compactness, no local doubling estimate, and no coefficient-gradient hypothesis.

## 3. Spacetime consequence

For every time interval \(I\),
\[
\boxed{
\left|\int_I\Delta Q\,dt\right|
\le
\int_I|\Delta Q|\,dt
\le
\int_IH_{\rm raw}\,dt.
}
\]
Therefore a persistent interval second-moment asymmetry immediately pays the raw-\(H^2\) spacetime ledger.

In particular, if
\[
\left|\int_I\Delta Q\,dt\right|\ge d_*>0,
\]
then
\[
\boxed{
\int_IH_{\rm raw}\,dt\ge d_*.
}
\]

## 4. Normalized sign-asymmetry fraction

Where \(H_{\rm raw}>0\), define
\[
\eta_Q
:=
\frac{\Delta Q}{H_{\rm raw}}.
\]
Then
\[
\boxed{-1\le\eta_Q\le1.}
\]
Thus a nonzero or even order-one **relative** sign asymmetry does not by itself force an absolute resource cost if \(H_{\rm raw}\to0\). Only the absolute source \(\Delta Q\) entering the \(A\)-balance matters for replenishment.

This separates structural asymmetry from resource amplitude.

## 5. Relation to M17-461

M17-461 remains valid as a structural interpretation.

Let
\[
K_\pm=\int\kappa_\pm\rho^2dx,
\qquad
\bar\kappa_\pm=Q_\pm/K_\pm
\]
when \(K_\pm>0\). Then
\[
\Delta Q
=
\frac A2(\bar\kappa_+-\bar\kappa_-)
-
\frac P2(\bar\kappa_++\bar\kappa_-).
\]
Hence \(P\approx0\) with significant \(\Delta Q\) still indicates that the two signs occupy different coefficient magnitudes/intrinsic scales.

However the new domination identity shows that this scale separation does not create a new analytic payer:
\[
\boxed{
G_{\rm sign\text{-}scale\ dispersion}
\subseteq
G_{\rm raw\text{-}H^2}
}
\]
for purposes of absolute source accounting.

## 6. Snapshot distribution firewall: dispersion is not dynamic migration

It is useful to express the diagnostic as a signed measure on coefficient magnitude.

Let \(q=|\kappa|\) and define the first-moment measures
\[
d\nu_+=q\,\mathbf1_{\{\kappa>0\}}\rho^2dx,
\qquad
 d\nu_-=q\,\mathbf1_{\{\kappa<0\}}\rho^2dx.
\]
Then
\[
\nu_+(\mathbb R_+)=K_+,
\qquad
\nu_-(\mathbb R_+)=K_-,
\]
and
\[
Q_+=\int q\,d\nu_+,
\qquad
Q_-=\int q\,d\nu_-.
\]
Thus \(\Delta Q\) measures a **snapshot difference of coefficient-magnitude first moments** between the two signs.

This does **not** by itself prove temporal transport of a packet from one coefficient bin to another. A dynamic migration theorem would require material/genealogical identification of the same mass across times.

Therefore the term “scale dispersion” is retained for the snapshot structure, while “migration” is forbidden unless a separate time-connected transport statement is proved.

## 7. Interaction with M17-467 ancestry scaling

M17-467 gives
\[
\int H_{{\rm raw},R}\,ds
=
R^3\int H_{\rm raw}\,dt.
\]
Hence a fixed normalized \(\Delta Q\) spacetime payment is inherited by the parent with the same cubic weight
\[
R^{-3}.
\]
For geometric records,
\[
\sum_mR_m^{-3}<\infty.
\]
Thus reducing \(\Delta Q\) to raw-\(H^2\) is a genuine branch simplification, but it does not produce a contradiction.

## 8. Updated common-mode source tree

Combining M17-466–468,
\[
\boxed{
\begin{aligned}
G_{\rm cm}^{\rm interval}
\Longrightarrow{}&
G_{\Delta A}
\lor
G_{J_0}\\
&\lor
G_{\rm palinstrophy/trace\text{-}high\text{-}jet}\\
&\lor
G_{\rm raw\text{-}H^2}.
\end{aligned}
}
\]

The separate sign-dependent coefficient-scale-dispersion payer branch is removed. Its structural content remains available inside the raw-\(H^2\) branch.

## 9. Audit status

Closed/reduced here:

- \(\Delta Q\) as an independent absolute payer;
- any inference that snapshot sign-scale dispersion alone proves dynamic migration.

Still OPEN:

- endpoint \(\Delta A\) classification;
- zero-current \(J_0\) classification beyond its cubic ancestry scaling;
- trace/high-jet decompactification;
- raw-\(H^2\) non-summable allocation;
- verified termwise provenance of \(\mathcal R_{\rm geom}\);
- genealogy/interface/domain persistence;
- inherited ROOT-CERT and non-CE-H roots.

## 10. Next target

The endpoint first moment has the immediate interpolation bound
\[
A^2
\le
E\,H_{\rm raw},
\qquad
E=\int\rho^2dx.
\]
The next module should audit whether this removes \(\Delta A\) as another independent branch, while preserving the distinction between an instantaneous raw-\(H^2\) spike and a certified spacetime raw-\(H^2\) payment.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
