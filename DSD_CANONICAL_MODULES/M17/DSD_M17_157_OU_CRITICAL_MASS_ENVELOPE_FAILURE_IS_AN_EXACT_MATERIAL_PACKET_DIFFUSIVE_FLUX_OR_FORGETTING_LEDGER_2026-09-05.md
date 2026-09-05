# DSD M17-157 — OU critical-mass-envelope failure is an exact material-packet diffusive-flux / forgetting ledger

Date: 2026-09-05  
Canonical ID: **M17-157**

Status: **MASS-GENEALOGY REDUCTION / M17-156 CLOSES THE RELATIVE-THICK QUIET BOUNDED-POTENTIAL RIBBON BRANCH WHEN THE AMPLITUDE-NORMALIZED PACKET OBEYS A TWO-SIDED CRITICAL OU MASS ENVELOPE. THE PRESENT MODULE DERIVES THE EXACT MATERIAL-PACKET ENSTROPHY IDENTITY. AFTER MULTIPLYING BY THE OU CRITICAL FACTOR `exp(theta/2)`, THE ONLY TERMS ARE STRAIN PRODUCTION, NEGATIVE DIFFUSION, AND THE DIFFUSIVE BOUNDARY FLUX. ON THE RELATIVE-THICK QUIET REMOTE BRANCH THE STRAIN-PRODUCTION RATE IS `o(1)` RELATIVE TO PACKET MASS. THEREFORE A LARGE FORWARD VIOLATION OF THE OU ENVELOPE REQUIRES POSITIVE DIFFUSIVE IMPORT THROUGH THE PACKET BOUNDARY (OR FAILURE OF THE QUIET/THICK HYPOTHESES), WHILE A LARGE BACKWARD-ANCESTOR/PRESENT MASS MISMATCH IS A STRONG DISSIPATIVE EXPORT/FORGETTING EVENT. THUS `G_mass` IS NOT A FREE NEW SURVIVOR: IT IS ROUTED TO THE EXISTING TURNOVER/BOUNDARY-FLUX LEDGER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity vorticity equation

On the CE-H branch, and in fact before using `Delta W=kappa W`, the similarity vorticity equation is

\[
\boxed{
D_BW
=
\Delta W+\Sigma W-W,
}
\]

where

\[
B=U+\frac12y,
\qquad
\nabla\cdot B=\frac32.
\]

The antisymmetric part of `grad U` annihilates `W`, so the stretching term is `Sigma W`.

---

## 2. Material packet

Let `D(theta)` be a smooth material packet transported by `B`:

\[
\frac{d}{d\theta}X(\theta)=B(X(\theta),\theta),
\qquad
D(\theta)=\Phi_{\theta,\theta_0}D(\theta_0).
\]

Define

\[
E_D(\theta):=\int_{D(\theta)}|W|^2dy,
\]

\[
\mathcal D_D(\theta):=\int_{D(\theta)}|\nabla W|^2dy,
\]

\[
\mathcal P_D(\theta):=\int_{D(\theta)}W\cdot\Sigma W\,dy,
\]

and the diffusive boundary flux

\[
\boxed{
\mathcal F_D(\theta)
:=
\int_{\partial D(\theta)}W\cdot\partial_nW\,dA.
}
\]

---

## 3. Exact material enstrophy identity

Reynolds transport gives

\[
\frac12\frac d{d\theta}E_D
=
\int_D
\left[
W\cdot D_BW
+\frac12(\nabla\cdot B)|W|^2
\right]dy.
\]

Insert the vorticity equation and `div B=3/2`:

\[
\frac12E_D'
=
\int_DW\cdot\Delta W\,dy
+\mathcal P_D
-\frac14E_D.
\]

Integrating the Laplacian by parts,

\[
\int_DW\cdot\Delta W
=-\mathcal D_D+\mathcal F_D.
\]

Therefore

\[
\boxed{
E_D'
=
-2\mathcal D_D
+2\mathcal P_D
-\frac12E_D
+2\mathcal F_D.
}
\]

This identity is exact.

---

## 4. Critical OU-weighted packet mass

Define

\[
\boxed{
Q_D(\theta):=e^{\theta/2}E_D(\theta).
}
\]

Then the linear similarity damping cancels:

\[
\boxed{
Q_D'
=
2e^{\theta/2}
\left(
\mathcal P_D
-\mathcal D_D
+\mathcal F_D
\right).
}
\]

This is precisely the nonlinear packet counterpart of the OU critical envelope used in M17-156.

---

## 5. Relative-thick packet makes strain production small

On the M17-155 relative-thick branch, assume on the material packet over a fixed remote corridor

\[
\|W\|_{L^\infty(D)}^2
\le C_E E_D.
\]

Then

\[
\left(\int_D|W|^4dy\right)^{1/2}
\le
\|W\|_\infty E_D^{1/2}
\le
C_E^{1/2}E_D.
\]

Hence

\[
|\mathcal P_D|
\le
\|\Sigma\|_{L^2(D)}
\left(\int_D|W|^4\right)^{1/2}
\le
C E_D\|\Sigma\|_{L^2(D)}.
\]

On a quiet critical remote shell,

\[
\|\Sigma\|_{L^2(D)}
\le
\|\Sigma\|_{L^2(C_R)}
\lesssim R^{-1/2}.
\]

Therefore

\[
\boxed{
\frac{|\mathcal P_D|}{E_D}
\lesssim R^{-1/2}
\to0.
}
\]

Thus order-one packet-mass change cannot be supplied by ordinary strain production on this branch.

---

## 6. Forward supercritical mass growth requires diffusive import

Since

\[
\mathcal D_D\ge0,
\]

we have

\[
Q_D'
\le
2e^{\theta/2}
\left(
|\mathcal P_D|+\mathcal F_D^+
\right),
\]

where

\[
\mathcal F_D^+:=\max(\mathcal F_D,0).
\]

On a fixed remote quiet corridor, the strain contribution is `o(1)` relative to `Q_D`.

Therefore any fixed-factor **forward increase** of the critical mass `Q_D` requires

\[
\boxed{
\int e^{\theta/2}\mathcal F_D^+d\theta
\gtrsim
Q_D
}
\]

up to vanishing strain errors.

So forward failure of the M17-156 envelope is a genuine **diffusive packet-import / boundary-turnover event**.

---

## 7. Backward ancestor excess is a forgetting/export ledger

Suppose instead that, on tracing the packet backward, the critical mass becomes much larger than the M17-156 envelope allows.
Equivalently the present packet is much smaller than its material ancestor after removal of the universal `e^{-theta/2}` scaling.

From the integrated identity,

\[
Q_D(\theta_2)-Q_D(\theta_1)
=
2\int_{\theta_1}^{\theta_2}
 e^{\theta/2}
(\mathcal P_D-\mathcal D_D+\mathcal F_D)d\theta.
\]

A large decrease from ancestor to present requires a large contribution from

\[
\boxed{
\mathcal D_D
\quad\text{and/or}\quad
\mathcal F_D^-:=\max(-\mathcal F_D,0),
}
\]

unless the quiet strain hypothesis fails.

Thus the other direction of critical-envelope failure is exactly a **dissipative forgetting / diffusive export** event.

---

## 8. Updated branch split

The M17-156 mass exit is therefore refined to

\[
\boxed{
G_{mass}
\Longrightarrow
G_{diffusive\ import}
\ \lor\ 
G_{forget/export}
\ \lor\ 
H_{1,crit}^{spacetime}
\ \lor\ 
G_{relative-thin/boundary}.
}
\]

No independent free `mass-comparability failure` branch remains.

---

## 9. Relation to earlier M5 turnover ledgers

This is exactly the kind of quantity that the earlier amplitude-sensitive remaining-time / forgetting analysis was designed to detect.

The present module does **not** claim that the diffusive boundary flux is already globally bounded strongly enough to contradict recurrence.
It identifies the precise local quantity that must now be charged to the M5 turnover ledger:

\[
\boxed{
\int e^{\theta/2}|\mathcal F_D|d\theta.
}
\]

This is higher value than continuing the M17-154 jet differentiation ladder.

---

## 10. DSD audit

1. A material packet removes advective boundary flux but not diffusion across the boundary.
2. The diffusive boundary term is signed; positive import and negative export are kept separate.
3. Small shell `L2` strain controls strain production only because relative thickness converts `rho^2` into a packet-mass-scale density.
4. No claim is made that packet boundaries can be chosen with zero diffusive flux.
5. The next gate is a turnover/localization estimate for `F_D`, not another pointwise derivative identity.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
