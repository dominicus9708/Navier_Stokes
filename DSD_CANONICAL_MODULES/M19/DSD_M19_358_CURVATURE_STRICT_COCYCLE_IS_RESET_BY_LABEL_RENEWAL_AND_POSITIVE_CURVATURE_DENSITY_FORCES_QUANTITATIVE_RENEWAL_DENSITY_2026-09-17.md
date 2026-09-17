# DSD M19-358 — The curvature strict cocycle is reset by material-label renewal, and positive curvature density forces quantitative renewal density

Date: 2026-09-17  
Canonical ID: **M19-358**

Status: **ACTIVE STRICT-COCYCLE AUDIT / RESET-CORRECTED COCYCLE / QUANTITATIVE LABEL-RENEWAL THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M5-485 and M5-621

M5-485 constructs a compact marked dilation hull \((\mathfrak H,\sigma,\mu,a)\) with

\[
\sigma_*\mu=\mu,
\qquad
\int a\,d\mu>0.
\]

It identifies the ideal closure mechanism

\[
\Phi\circ\sigma-\Phi\ge c a
\]

for a bounded continuous state observable \(\Phi\).

M5-621 later finds an exact strict material-label cocycle on the CE-H curvature channel. For a fixed nondegenerate material vortex-tube label,

\[
X
:=
\log\frac{\rho|\mathcal K|}{|\phi|},
\qquad
\mathcal K=(\xi\cdot\nabla)\xi,
\]

satisfies

\[
\boxed{D_BX=-\frac32.}
\]

This has no \(\sigma\)- or \(\kappa\)-remainder.

## 2. The strict cocycle is label-local, not a global hull potential

The M5-621 law applies while one follows the **same material-flux label** with

\[
0<\phi_-\le|\phi|\le\phi_+<\infty.
\]

On the compact CE-H hull,

\[
\rho|\mathcal K|\le M_1.
\]

If curvature activity is recorded only when

\[
\rho|\mathcal K|\ge z_*>0,
\]

then during a curvature-active episode

\[
\boxed{
X_-\le X\le X_+,
}
\]

where

\[
X_-:=\log\frac{z_*}{\phi_+},
\qquad
X_+:=\log\frac{M_1}{\phi_-}.
\]

Thus the active-state range is finite:

\[
\boxed{
\Delta X_*:=X_+-X_-
=
\log\frac{M_1\phi_+}{z_*\phi_-}.
}
\]

M5-621's curvature-active lifetime is exactly

\[
\boxed{
T_{curv}=\frac23\Delta X_*.
}
\]

However, when curvature activity transfers to a **new material label**, the new label may enter with a fresh value of \(X\) near \(X_+\). Therefore the full recurrent system does not possess one globally decreasing bounded state variable obtained by simply concatenating the label-local \(X\)'s.

This is the reset firewall.

## 3. Reset-corrected cocycle

Let \(r_1<r_2<\cdots\) be renewal times at which the curvature carrier changes to a newly admitted fixed-flux material label. Between renewals,

\[
\frac{dX}{d\theta}=-\frac32.
\]

At a renewal \(r_k\), define the upward reset jump

\[
J_k
:=
\bigl[X(r_k^+)-X(r_k^-)\bigr]_+.
\]

Because active labels lie in \([X_-,X_+]\),

\[
\boxed{0\le J_k\le\Delta X_*.}
\]

For any interval \([\theta_0,\theta_1]\) during which the selected curvature carrier is defined piecewise through such renewals,

\[
\boxed{
X(\theta_1)-X(\theta_0)
=
-\frac32\,T_{act}
+
\sum_{r_k\in(\theta_0,\theta_1]}\Delta X_k,
}
\]

where \(T_{act}\) is the total similarity-time spent on the curvature-active tracked pieces, and signed reset jumps \(\Delta X_k\) have positive parts bounded by \(\Delta X_*\).

Consequently

\[
\boxed{
\frac32T_{act}
\le
2\Delta X_*
+
\Delta X_*N_{ren}(\theta_0,\theta_1),
}
\]

where the endpoint term has been bounded by \(2\Delta X_*\).

Hence

\[
\boxed{
N_{ren}(\theta_0,\theta_1)
\ge
\frac{3}{2\Delta X_*}T_{act}-2.
}
\]

Equivalently,

\[
\boxed{
N_{ren}
\gtrsim
\frac{T_{act}}{T_{curv}}-O(1).
}
\]

## 4. Positive curvature-time density forces positive renewal density

Suppose along an invariant/ergodic marked component the curvature-active channel occupies similarity-time density

\[
\alpha_{curv}
:=
\liminf_{T\to\infty}
\frac{T_{act}([0,T])}{T}
>0.
\]

Then Section 3 gives

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_{ren}(0,T)}{T}
\ge
\frac{3\alpha_{curv}}{2\Delta X_*}
=
\frac{\alpha_{curv}}{T_{curv}}
>0.
}
\]

Thus a positive-density curvature channel cannot be maintained by rare renewal events. It requires a quantitatively positive material-label renewal rate.

## 5. Generation-density version

The M5-482/M5-485 first-hitting generations have normalized stage durations bounded above and below on the retained corridor:

\[
0<\ell_-\le \Delta\theta_j\le\ell_+<\infty.
\]

One material label can therefore account for at most

\[
\boxed{
N_{curv}^{max}
:=
1+\left\lceil\frac{T_{curv}}{\ell_-}\right\rceil
}
\]

curvature-active generation marks before renewal is mandatory.

If \(a_j^{curv}\in\{0,1\}\) is the curvature-channel mark, then asymptotically

\[
\boxed{
\overline d(R_{ren})
\ge
\frac{\overline d(a^{curv})}{N_{curv}^{max}}.
}
\]

Thus positive generation density of curvature activity implies positive generation density of renewal.

## 6. Relation to the full M5-619 non-Beltrami split

M5-618--619 give a uniform non-Beltrami defect and the statewise dichotomy

\[
\|\rho P_\xi^\perp\nabla\rho\|_2\ge b_*/2
\quad\lor\quad
\|\rho^2\mathcal K\|_2\ge b_*/2.
\]

Therefore on any marked invariant component one has two possibilities:

1. the curvature channel carries positive invariant frequency; then M19-358 forces positive renewal density;
2. the transverse-magnitude channel carries the missing invariant frequency; then one enters the M5-622 forced/Burgers-like branch where no universal strict scalar cocycle is available.

This is the correct curvature-versus-magnitude interpretation of the M5-485 strict-cocycle program.

## 7. Why this is not yet the desired M5-485 contradiction

The reset jumps are not a mathematical defect; they encode genuine material-label turnover.

The M5-485 contradiction would require one bounded state function whose shift drift stays positive on every marked event. M19-358 instead gives

\[
\boxed{
\text{strict negative drift on each fixed label}
+
\text{positive reset jumps at renewal}.
}
\]

Invariant recurrence can therefore survive if positive reset jumps replenish the label-local potential.

Thus the strict curvature cocycle closes **same-label recurrence**, not the entire marked hull.

## 8. New exact resource obligation

To turn M19-358 into a global contradiction, one needs a finite/nonrecyclable budget for the resets. Equivalent targets include:

\[
\boxed{
\mathcal T_{ren}^{abs-flux}:
\text{positive-density renewal forces nonsummable absolute vorticity-flux variation.}
}
\]

or

\[
\boxed{
\mathcal T_{ren}^{irr-genealogy}:
\text{each reset pays an irreversible material-lineage/topology cost with finite total budget.}
}
\]

M5-643 identifies the first as the missing global absolute-flux transversal/additivity lemma.

## 9. Audit verdict

**PASS — the M5-621 strict curvature cocycle has been upgraded to a reset-corrected theorem with a quantitative renewal-rate lower bound.**

The result does not close the compact marked dilation hull. It proves that recurrent curvature activity is possible only through quantitatively recurrent label renewal. The hard question therefore moves from construction of another local strict cocycle to control of the reset/renewal resource.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
