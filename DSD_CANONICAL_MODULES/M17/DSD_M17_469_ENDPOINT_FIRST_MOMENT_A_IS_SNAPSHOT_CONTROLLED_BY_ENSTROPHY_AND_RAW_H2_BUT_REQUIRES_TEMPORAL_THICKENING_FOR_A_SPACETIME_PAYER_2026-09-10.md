# M17-469 — Endpoint first moment A is snapshot-controlled by enstrophy and raw-H2 but requires temporal thickening for a spacetime payer

**Date:** 2026-09-10  
**Status:** ACTIVE ENDPOINT REDUCTION / SNAPSHOT-TO-SPACETIME FIREWALL

## 1. Scope

M17-466 reduced persistent interval common-mode geometry to endpoint \(\Delta A\), zero-current \(J_0\), trace/high-jet, raw-\(H^2\), and the second-moment asymmetry. M17-468 absorbed the second-moment asymmetry into raw-\(H^2\).

This module tests whether the remaining endpoint \(A\)-channel is independent.

## 2. Exact interpolation inequality

Recall
\[
A(t)=\int |\kappa|\rho^2\,dx,
\qquad
E(t)=\int\rho^2\,dx,
\qquad
H_{\rm raw}(t)=\int\kappa^2\rho^2\,dx.
\]
By Cauchy–Schwarz,
\[
\begin{aligned}
A
&=\int (|\kappa|\rho)\rho\,dx\\
&\le
\left(\int\kappa^2\rho^2dx\right)^{1/2}
\left(\int\rho^2dx\right)^{1/2}.
\end{aligned}
\]
Therefore
\[
\boxed{A^2\le E\,H_{\rm raw}.}
\]
This is exact on exact CE-H and uses no compactness or coefficient-gradient hypothesis.

## 3. Endpoint consequence

Let \(I=[t_0,t_1]\), and suppose
\[
E(t_i)\le E_*,\qquad i=0,1.
\]
Because \(A\ge0\),
\[
|A(t_1)-A(t_0)|
\le
\max\{A(t_0),A(t_1)\}.
\]
Hence if
\[
|\Delta A|:=|A(t_1)-A(t_0)|\ge a_*>0,
\]
then at at least one endpoint \(t_i\),
\[
A(t_i)\ge a_*.
\]
The interpolation inequality gives
\[
\boxed{
H_{\rm raw}(t_i)
\ge
\frac{a_*^2}{E_*}.
}
\]
Thus endpoint first-moment growth is not an independent **snapshot** resource under bounded enstrophy.

The branch reduces to
\[
\boxed{
G_{\Delta A}
\Longrightarrow
G_{E\text{-decompactification}}
\ \lor\ 
G_{\rm instantaneous\ raw\text{-}H^2\ spike}.
}
\]

## 4. Why this does not yet give a spacetime raw-H2 payer

A lower bound at one endpoint does not by itself imply
\[
\int_IH_{\rm raw}(t)dt\gtrsim1.
\]
A continuous function can have a narrow spike with arbitrarily small time integral unless one has a quantitative modulus of continuity or derivative bound.

Accordingly, the inference
\[
H_{\rm raw}(t_i)\gtrsim1
\quad\Longrightarrow\quad
\int_IH_{\rm raw}dt\gtrsim1
\]
is forbidden without an additional temporal-thickening theorem.

Possible sufficient inputs would include a certified bound on a time derivative/high jet strong enough to control the width of the spike, but no such bound is assumed here.

## 5. Integrated first-moment variant

There is, however, a direct spacetime inequality for an **integrated** first moment.

If
\[
E(t)\le E_*
\quad\text{on }I,
\]
then pointwise
\[
A(t)\le E_*^{1/2}H_{\rm raw}(t)^{1/2}.
\]
Therefore
\[
\int_IA(t)dt
\le
E_*^{1/2}|I|^{1/2}
\left(\int_IH_{\rm raw}dt\right)^{1/2}.
\]
Equivalently,
\[
\boxed{
\int_IH_{\rm raw}dt
\ge
\frac{\left(\int_IA(t)dt\right)^2}{E_*|I|}.
}
\]
Thus a sustained first-moment amplitude does pay spacetime raw-\(H^2\). The unresolved issue is specifically the conversion of an **endpoint jump** into sustained amplitude.

## 6. Scaling consistency

M17-467 gives
\[
A_R=R^3A,
\qquad
H_{{\rm raw},R}=R^5H_{\rm raw},
\qquad
E_R=R E.
\]
Indeed
\[
A_R^2=R^6A^2,
\qquad
E_RH_{{\rm raw},R}=R^6EH_{\rm raw},
\]
so
\[
A^2\le EH_{\rm raw}
\]
is exactly scale-covariant.

## 7. Updated common-mode source tree

Combining M17-466–469,
\[
\boxed{
\begin{aligned}
G_{\rm cm}^{\rm interval}
\Longrightarrow{}&
G_{J_0}\\
&\lor G_{\rm palinstrophy/trace\text{-}high\text{-}jet}\\
&\lor G_{\rm raw\text{-}H^2}\\
&\lor G_{E\text{-decompactification}}\\
&\lor G_{\rm endpoint\ raw\text{-}H^2\ spike\ without\ temporal\ thickening}.
\end{aligned}
}
\]

The standalone \(\Delta A\) branch is removed as a snapshot resource. What remains is the snapshot-to-spacetime conversion debt.

## 8. Audit status

Closed/reduced here:

- endpoint \(A\) as an independent snapshot payer under bounded enstrophy;
- sustained integrated \(A\) as an independent spacetime payer.

Still OPEN:

- temporal thickening of endpoint raw-\(H^2\) spikes;
- zero-current \(J_0\);
- trace/high-jet decompactification;
- non-summable allocation of raw-\(H^2\);
- enstrophy decompactification;
- verified termwise provenance of \(\mathcal R_{\rm geom}\);
- genealogy/interface/domain persistence;
- inherited ROOT-CERT and non-CE-H roots.

## 9. Next target

The narrowest algebraically independent common-mode balance term is now \(J_0\). The next audit should determine whether the regular zero-level current can be thickened into a near-zero coefficient slab under an explicit finite-jet hypothesis, and whether the resulting bulk cost lands in palinstrophy/raw-\(H^2\) or merely creates another high-jet escape.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
