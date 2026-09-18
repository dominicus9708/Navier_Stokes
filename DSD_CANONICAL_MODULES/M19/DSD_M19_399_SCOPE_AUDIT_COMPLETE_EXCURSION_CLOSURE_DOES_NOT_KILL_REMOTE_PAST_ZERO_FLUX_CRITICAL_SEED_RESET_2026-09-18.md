# M19-399 — Scope audit: complete-excursion closure does not kill the remote-past zero-flux critical seed reset

Date: 2026-09-18

Status: **AUDIT CORRECTION / M19-397--398 CLOSE THE SAME-PACKET LONG COMPLETE POSITIVE-EXCURSION CURRENT-REVERSAL BRANCH, BUT THEY MUST NOT BE READ AS A CLOSURE OF THE M19-364 AGE-STRUCTURED CRITICAL SEED WITNESS. THE CRITICAL WITNESS MAY HAVE `kappa≈3/2` THROUGH AN ARBITRARILY LONG PREACTIVATION HISTORY WITH MATERIAL FLUX TENDING TO ZERO TOWARD THE REMOTE PAST, SO A FINITE RETAINED BASE SLICE NEED NOT CONTAIN THE PRECEDING UPWARD ZERO CROSSING OF THAT LABEL. SUCH A HISTORY ENTERS THE CURRENT PROOF AS A RESET/GENEALOGY/ASYMPTOTIC-ZERO-FLUX BOUNDARY, NOT AS A COMPLETE ZERO-TO-ZERO EXCURSION. THE NEW CLOSURE IS THEREFORE REAL BUT CONDITIONAL; THE HARD SURVIVOR IS SHARPENED TO CRITICAL SEED INJECTION FROM AN ASYMPTOTICALLY VANISHING FLUX HISTORY OR EXPLICIT MATERIAL REPLACEMENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. What M19-397--398 actually close

M19-397 proves that on the same certified material tube,

\[
\text{critical enstrophy amplification}
\]

and

\[
\text{residence-current reversal}
\]

cannot both hold over the same long complete positive-kappa excursion.

M19-398 sharpens this: for

\[
I_+
=
\left(\frac32+o(1)\right)T,
\]

current reversal would require

\[
L_d/L_u
\le
e^{-3T/2+o(T)}.
\]

A coherent critical line instead has

\[
L_d/L_u=e^{o(T)}.
\]

Thus the **same-packet / complete-excursion / short-transition** branch is closed.

---

## 2. M19-364 is not a complete-excursion model

The M19-364 stationary witness uses a remaining-time coordinate \(s\ge0\) and

\[
q(s)=\phi_*e^{-3s/2}.
\]

As one follows a future seed backward away from activation,

\[
s\to\infty
\]

and

\[
q(s)\to0.
\]

Equivalently, on the forward material history the seed may satisfy

\[
\kappa\approx\frac32
\]

for an arbitrarily long preactivation interval while its material flux starts arbitrarily small on earlier and earlier base slices.

Nothing in this scaling witness requires a finite-time preceding crossing

\[
\kappa: ; - \to + 
\quad\text{through }0.
\]

Thus the history need not be representable as one complete positive zero-to-zero excursion inside a fixed retained observation window.

---

## 3. Why M19-389 cannot be silently applied backward to infinity

M19-389 compares an upward zero crossing \(\theta_u\) and the subsequent downward zero crossing \(\theta_d\).

Its exact pair weight is based on two finite crossing events of the same retained material label.

If a critical seed has no preceding upward zero crossing in the retained genealogy, one may not invent

\[
\theta_u=-\infty
\]

and treat the asymptotic zero-flux state as an ordinary crossing.

The limiting condition

\[
\Phi(\theta)\to0
\qquad
(\theta\to-\infty)
\]

is a different boundary type.

It must be treated as

\[
\boxed{
G_{remote-past/zero-flux}^{reset}.
}
\]

---

## 4. Relation to M19-384 critical discount

M19-384 already shows that fixed material log flux is an exact potential,

\[
\int\kappa d\theta
=
\Delta\log|d\Phi|.
\]

It also records the critical reset mechanism: a future order-one carrier may begin on a fixed base slice with

\[
|d\Phi_0|
\lesssim
e^{-3T/2}
\]

and amplify to order one.

Therefore a base-transversal finite-flux argument cannot simply charge each future activation an order-one initial flux.

M19-399 preserves that firewall.

The new result does not defeat the exponential seed discount by itself.

---

## 5. Corrected critical-current survivor

After M19-397--399, the current critical branch is

\[
\boxed{
G_{seed}^{3/2}
\Longrightarrow
G_{spatial\ current}^{negative}
\lor
G_{remote-past/zero-flux}^{reset}
\lor
G_{packet/current\ segregation}
\lor
G_{genealogy/representation\ loss}.
}
\]

The first branch retains a signed spatial PDE current and can be attacked through M5-683.

The second is the genuine critical age-structured reset survivor.

The third allows a separate recurrent hysteretic population to cancel the seed current.

---

## 6. New precise theorem target

The strongest remaining critical-reset theorem is now

\[
\boxed{
\mathcal T_{zero-flux}^{ancient}:
\text{classify or exclude a positive-rate family of retained CE-H material seed histories with }
\Phi(\theta)\to0
\text{ as }\theta\to-\infty
\text{ while later reaching order-one carrier status.}
}
\]

A successful theorem could come from one of:

1. a backward-uniqueness / ancient-lineage rigidity statement;
2. a minimum coherent material-seed size theorem not defeated by arbitrary subpartition of a smooth field;
3. a representation theorem showing that vanishing-flux material labels cannot remain the certified ancestors of order-one recurrent carriers without a reset event;
4. a non-discounted physical cost for the reset/activation edge.

---

## 7. DSD audit verdict

M19-397 is a genuine branch closure.

M19-399 narrows its scope so it is not overcounted as a global critical-seed contradiction.

The progress is the replacement of a vague current-reversal escape by the much sharper survivor

\[
\boxed{
\text{asymptotically zero-flux ancient seed injection / reset}.
}
\]

This is the correct next target.

---

\[
\boxed{\text{M19-399 COMPLETE; THE REMAINING CRITICAL SEED ESCAPE IS A REMOTE-PAST ZERO-FLUX RESET/GENEALOGY PROBLEM.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
