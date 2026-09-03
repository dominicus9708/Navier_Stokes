# DSD M5-662 — A boundary-attached silent fold forces amplitude-threshold material turnover

Date: 2026-09-03

Status: **INTERNAL TURNOVER REDUCTION / AFTER M5-661, A SMOOTH RANK-ONE SILENT FOLD CAN SURVIVE ONLY BY REACHING THE BOUNDARY OF THE FIXED HIGH-AMPLITUDE COMPONENT OR BY DEVELOPING HIGHER CRITICAL DEGENERACY / IF A BOUNDARY-ATTACHED SILENT FOLD SEPARATES THE PERSISTENT CARRIER FROM ITS SAME-COMPONENT PAYER, THE FOLD TOGETHER WITH A PIECE OF THE AMPLITUDE LEVEL `rho=a0` BOUNDS A SHEET-DOMAIN CONTAINING A FIXED POSITIVE-VOLUME CARRIER/PAYER BALL / THE FOLD PART HAS MATERIAL NORMAL VELOCITY, SO THE ONLY WAY TO OFFSET THE EXACT `+3V/2` MATERIAL-VOLUME EXPANSION IN A BOUNDED RECURRENT DOMAIN IS A NONZERO MATERIAL FLUX THROUGH THE AMPLITUDE-THRESHOLD PART / USING THE LEVEL-SET VELOCITY, THIS CROSSING RATE IS EXACTLY `-(D_B rho)/|grad rho| = -a0(sigma+kappa-1)/|grad rho|` WITH THE APPROPRIATE ORIENTATION / THUS THE BOUNDARY-ATTACHED SILENT FOLD REDUCES TO POSITIVE-RATE MATERIAL SHEATH TURNOVER ACROSS A FIXED AMPLITUDE LEVEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Boundary-attached sheet domain

Let

\[
C_L\subset\{\rho>a_0\}
\]

be the M5-657 connected amplitude component.

Assume a smooth rank-one differential-silent fold `Sigma` is properly embedded in `C_L` and reaches

\[
\partial C_L\subset\{\rho=a_0\}.
\]

Suppose the fold separates the persistent carrier and the strongly-negative payer into distinct sheet regions.

Choose one side `Omega(theta)` whose boundary consists of

\[
\partial\Omega
=
\Sigma
\cup
A_{a_0},
\]

where

\[
A_{a_0}\subset\{\rho=a_0\}
\]

is the corresponding amplitude-boundary patch, up to lower-dimensional edge sets.

---

## 2. Fixed positive volume on one side

M5-657 gives fixed-radius coherent balls for both the persistent carrier and the strongly-negative payer.

At least one chosen side of the separating fold contains one such ball.

Therefore there is a uniform constant

\[
\boxed{v_0>0}
\]

such that on every retained event

\[
\boxed{|\Omega(\theta)|\ge v_0.}
\]

The domain also remains inside the fixed normalized core and hence has a uniform upper volume bound.

---

## 3. Fold part of the boundary is material-normal

By M5-660,

\[
\boxed{V_\Sigma\cdot n=B\cdot n}
\]

on the differential-silent rank-one fold.

Hence the relative normal material velocity vanishes there:

\[
\boxed{(B-V_\Sigma)\cdot n=0.}
\]

So the fold contributes no material volume exchange between the two sheet domains.

---

## 4. Moving amplitude-level velocity

Let `V_a` denote the normal velocity of the regular amplitude level surface

\[
\rho=a_0.
\]

Along the moving level,

\[
\partial_\theta\rho+V_a\cdot\nabla\rho=0.
\]

Therefore

\[
D_B\rho
=
\partial_\theta\rho+B\cdot\nabla\rho
=
(B-V_a)\cdot\nabla\rho.
\]

For the outward normal of the superlevel side,

\[
n_a=-\frac{\nabla\rho}{|\nabla\rho|},
\]

we obtain

\[
\boxed{
(B-V_a)\cdot n_a
=
-\frac{D_B\rho}{|\nabla\rho|}.
}
\]

On CE-H,

\[
D_B\rho
=(\sigma+\kappa-1)\rho.
\]

Hence on `rho=a0`,

\[
\boxed{
(B-V_a)\cdot n_a
=
-\frac{a_0(\sigma+\kappa-1)}{|\nabla\rho|}.
}
\]

This is the exact material crossing speed through the amplitude threshold.

---

## 5. Volume balance for the sheet domain

For a moving domain with boundary velocity `V_boundary`,

\[
\frac d{d\theta}|\Omega|
=
\int_\Omega\nabla\cdot B\,dy
-
\int_{\partial\Omega}(B-V_{boundary})\cdot n\,dS.
\]

Using

\[
\nabla\cdot B=\frac32,
\]

and the zero relative flux on `Sigma`,

\[
\boxed{
\frac d{d\theta}|\Omega|
=
\frac32|\Omega|
-
\int_{A_{a_0}}(B-V_a)\cdot n\,dS.
}
\]

Equivalently, with the orientation chosen consistently,

\[
\boxed{
\mathcal T_{a_0}(\theta)
:=
\int_{A_{a_0}}(B-V_a)\cdot n\,dS
=
\frac32|\Omega|-|\Omega|'.
}
\]

---

## 6. Recurrent average forces positive threshold turnover

The sheet-domain volume is bounded above and below on the recurrent retained branch.

Therefore its invariant/recurrent mean derivative is zero:

\[
\langle |\Omega|'\rangle=0.
\]

Thus

\[
\boxed{
\langle\mathcal T_{a_0}\rangle
=
\frac32\langle|\Omega|\rangle
\ge
\frac32v_0>0.
}
\]

Hence a boundary-attached silent fold cannot be maintained without a **positive mean material turnover across the fixed amplitude threshold**.

---

## 7. Exact amplitude form of the turnover tax

Insert the level-crossing formula:

\[
\boxed{
\left\langle
-\int_{A_{a_0}}
\frac{a_0(\sigma+\kappa-1)}{|\nabla\rho|}
\,dS
\right\rangle
\ge
\frac32v_0
}
\]

with the orientation convention of the chosen sheet domain.

Thus the turnover is not an abstract topological event; it is directly encoded in the CE-H amplitude transport coefficient.

---

## 8. Relation to M5-560 and M5-633

M5-560 showed that a positive-volume material packet cannot remain in a bounded similarity core because of exact `3/2` volume expansion.

M5-633 therefore retained

\[
\text{lower-dimensional persistent spine}
+
\text{renewing material sheath}.
\]

The present result shows that a boundary-attached silent fold realizes **exactly that same sheath-turnover branch**.

Hence

\[
\boxed{
K_{fold}^{boundary-attached}
\Longrightarrow
T_{sheath}^{rho=a_0}.
}
\]

It is not an independent silent-sheet loophole.

---

## 9. What this does and does not close

The positive turnover rate does not by itself contradict Leray energy or finite material volume; earlier audits showed that material-volume pullbacks can form a summable geometric series.

Therefore this is a branch reduction, not a final contradiction.

However it removes the possibility of a **turnover-free** boundary-attached silent fold.

The only genuinely silent/no-turnover geometry left is now higher-order kappa-critical degeneracy.

---

## 10. Updated cross-sheet frontier

Combining M5-658--662,

\[
\boxed{
T_{high-amplitude\ cross-sheet}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{force}
\lor
T_{sheath}^{rho=a_0}
\lor
K_{higher}^{degenerate}.
}
\]

The smooth closed and boundary-attached rank-one silent-fold branches have both been reduced.

---

## 11. Next target

The remaining differential-silent/no-turnover branch is concentrated on higher-order critical strata

\[
\nabla\kappa=0,
\qquad
\nabla h=0,
\qquad
\operatorname{rank}\nabla^2\kappa=0
\]

or on singular transitions between rank-one strata.

The next calculation should use the uniform analytic regularity of the compact ancient hull to bound the possible vanishing order of `kappa-kappa_0` at such high-amplitude critical points and extract a finite-order jet charge whenever topology changes.

---

## 12. Firewall

The argument assumes a separating boundary-attached fold and a regular amplitude boundary patch for the chosen threshold. Singular threshold times can be handled by nearby regular levels or retained as an additional amplitude-critical event; they are not silently ignored.

No claim is made that positive sheath turnover is itself impossible.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]