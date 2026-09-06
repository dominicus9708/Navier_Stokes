# DSD Deep Audit — SAPZ v6 Route-T: Gate-A Quantifier-Order Audit

Date: 2026-09-06
Target: Lee Byoungwoo, SAPZ v6.0 and preceding v5.3r2A / v4.3r1 records.
Status: **LATEST V6 OPEN_DEEP; EARLIER COMPLETE CLAIMS SUPERSEDED BY VERSION HISTORY**

## 1. Version-aware evidence

The public v4.3r1 record explicitly stated that criterion-level closure was available but retained one Clay-level PDE target, CT3-(A3). Later v5.3r2A and v6.0 claim a Route-T discharge and a global theorem.

This is useful audit evidence:

\[
\boxed{
\text{v4.3r1 is a self-declared conditional stage; later Route-T must be checked as the new hinge.}
}
\]

The present note does not re-litigate already superseded claims. It targets the latest advertised theorem chain.

## 2. Public v6 chain

The v6 description gives the following sequence:

1. convolution-first SAPZ envelope;
2. epsilon-independent finite-window Riccati normal form;
3. CT2/CT3 residual budget;
4. CT3 persistence with scale-last selection;
5. Route-T positive transport residual on the same short window;
6. Gate A approximate-identity time-slice identification;
7. CKN concentration exclusion and continuation.

The most delicate logical interface is the quantifier order between steps 4-6.

## 3. Exact approximate-identity fact

Let

\[
f=|u(\cdot,t)|^2\ge0,
\qquad
\Psi_\varepsilon(t)=\|f*\varphi_\varepsilon\|_{L^\infty}.
\]

If one proves a genuinely uniform small-scale bound

\[
\boxed{
\sup_{0<\varepsilon<\varepsilon_0}
\Psi_\varepsilon(t)\le C,
}
\]

then the approximate-identity theorem gives

\[
f(x)\le C
\]

for almost every Lebesgue point, hence

\[
\|u(t)\|_\infty^2\le C.
\]

This Gate-A implication is legitimate.

## 4. The weaker selected-scale statement is not enough

By contrast, a statement of the form

\[
\forall t\ \exists\varepsilon(t)>0:
\Psi_{\varepsilon(t)}(t)\le C
\]

or a scale-last contradiction argument that controls only one selected mollifier scale does **not** imply `f in L^infinity`.

A function may be arbitrarily large on very small sets while a sufficiently coarse convolution remains bounded.

Thus the two quantifier patterns

\[
\sup_{\varepsilon\downarrow0}\Psi_\varepsilon<C
\]

and

\[
\exists\varepsilon:\Psi_\varepsilon<C
\]

are not interchangeable.

## 5. Route-T / Gate-A inheritance obligation

The latest proof must therefore demonstrate that the Route-T discharge exports one of the following:

- a uniform bound for **all sufficiently small** `epsilon` on the target time slice;
- a monotonic/comparison principle that converts the selected contradiction scale into all-smaller-scale control;
- another independent theorem that rules out finer concentration after the selected scale is controlled.

If CT3 uses a scale-last choice `epsilon_*` only to produce a contradiction at that scale, it cannot silently inherit the stronger Gate-A hypothesis.

## 6. Same-window quantifier firewall

The v6 description emphasizes a short backward parabolic window and persistence at a selected scale. The positive transport residual must be accumulated on that same physical window with constants independent of the selected scale.

The following invalid pattern must be excluded:

\[
\forall\varepsilon\ \exists I_\varepsilon\text{ with persistence},
\qquad
\text{then treating }I_\varepsilon\text{ as one common interval.}
\]

Similarly, epsilon-independent RNF coefficients do not automatically imply epsilon-uniform persistence times or residual lower bounds.

## 7. Current verdict

No direct contradiction with the v6 public description has been proved here. The public text explicitly advertises “uniform-scale subcriticality” and a Gate-A theorem, so the full manuscript may contain the correct quantifiers.

The decisive audit target is now exact and narrow:

\[
\boxed{
\text{Does Route-T prove all-small-scale SAPZ control needed by Gate A, or only selected-scale control?}
}
\]

Therefore:

\[
\boxed{
\text{v6 OPEN_DEEP — QUANTIFIER ORDER / ALL-SMALL-SCALES GATE.}
}
\]

If the universal small-scale bound is explicitly proved, Gate A survives this audit. If only a selected-scale bound is available, the global `L^infinity` upgrade does not follow.

New regression test for M17:

\[
\boxed{
R25:\ \text{selected-scale success cannot be exported as all-finer-scale compactness without a proved monotonicity/coverage bridge.}
}
\]

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
