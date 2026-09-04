# DSD M17-094 — Normalized Rank-2 critical type has a conditional peak-track continuity ledger with explicit birth/death source

Date: 2026-09-05
Canonical ID: **M17-094**

Status: **INTERNAL CONDITIONAL CRITICAL-TYPE TRACK LEDGER / M17-093 GIVES THE STRAIN-FREE TYPE VARIABLE `Z_nu=H_nu/|b|^(nu+1)` WITH MOVING-PEAK LAW `D_* Z_nu=S_nu^crit+V_rel^max·grad Z_nu`. ON ANY TIME INTERVAL WHERE A FINITE OR FINITELY WEIGHTED FAMILY OF SMOOTH TYPE-NU PEAK TRACKS CAN BE FOLLOWED WITHOUT BIRTH, DEATH, TYPE SWITCH, RANK LOSS, OR CHART EXIT, FIXED BOOKKEEPING WEIGHTS DEFINE AN EMPIRICAL DISTRIBUTION `F_nu` AND CURRENT `G_nu` SATISFYING `partial_theta F_nu+partial_z G_nu=0` DISTRIBUTIONALLY. WHEN TRACK EVENTS OCCUR AN EXPLICIT SOURCE/SINK DISTRIBUTION `B_nu` MUST BE RETAINED. THERE IS NO CANONICAL COUNTING MEASURE OR NEW CONSERVED PHYSICAL CHARGE HERE; THE LEDGER IS CONDITIONAL ON THE CHOSEN TRACK POPULATION. THE ONE-SIDED CURRENT AT `Z_nu=0` RECORDS TYPE-NU LOSS/ENTRY, WHILE CROSS-NU CANCELLATION CANNOT BE CLAIMED WITHOUT A MATCHING CONVENTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-093

On the full-rank pure-kernel branch, let

\[
Z_\nu:=\frac{H_\nu}{|b|^{\nu+1}},
\qquad
H_\nu=D_\xi^\nu g<0,
\qquad
g=D_\xi\log\rho.
\]

M17-093 gives

\[
\boxed{
D_*Z_\nu
=S_\nu^{crit}
+V_{rel}^{max}\cdot\nabla Z_\nu,
}
\]

where

\[
\boxed{
S_\nu^{crit}
=\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{|b|^{\nu+1}}.
}
\]

The operator `D_*` follows the moving peak, not a fixed material marker.

---

## 2. Track-preserving interval

Assume that on a time interval `I` there is a finite or finitely weighted family of smooth type-`nu` peak tracks

\[
X_i(\theta),\qquad i\in\mathcal I_\nu,
\]

such that throughout `I`:

1. the same tracks remain identifiable;
2. their critical order remains `nu`;
3. `b!=0` and the pure-kernel chart remains valid;
4. there are no births, deaths, mergers, splits, rank losses, or type switches.

Choose fixed positive bookkeeping weights

\[
w_i>0.
\]

These weights are **not** asserted to be a new invariant density.

Define

\[
Z_i(\theta):=Z_\nu(X_i(\theta),\theta).
\]

Then

\[
\boxed{
\dot Z_i
=S_\nu^{crit}(X_i,\theta)
+V_{rel,i}^{max}\cdot\nabla Z_\nu(X_i,\theta).
}
\]

---

## 3. Empirical type distribution and current

Define the distribution on the scalar `z` axis

\[
\boxed{
F_\nu(z,\theta)
:=\sum_{i\in\mathcal I_\nu}
w_i\,\delta(z-Z_i(\theta)).
}
\]

Define the associated current

\[
\boxed{
G_\nu(z,\theta)
:=\sum_{i\in\mathcal I_\nu}
w_i\,\dot Z_i(\theta)\,\delta(z-Z_i(\theta)).
}
\]

For any compactly supported test function `varphi(z)`,

\[
\frac d{d\theta}\int\varphi F_\nu\,dz
=\sum_iw_i\varphi'(Z_i)\dot Z_i
=\int\varphi'G_\nu\,dz.
\]

Therefore, distributionally,

\[
\boxed{
\partial_\theta F_\nu
+\partial_zG_\nu
=0
}
\]

on every track-preserving interval.

---

## 4. The current contains only the exact peak dynamics

Substituting the moving law,

\[
\boxed{
G_\nu(z,\theta)
=\sum_iw_i
\left[
S_\nu^{crit}
+V_{rel,i}^{max}\cdot\nabla Z_\nu
\right]_{X_i}
\delta(z-Z_i).
}
\]

Thus the current contains only

\[
\boxed{
\text{higher-line-jet recharge}
+\text{moving-peak relative transport}.
}
\]

No strain multiplier remains because of the M17-093 normalization.

---

## 5. Birth/death/type-switch source

If a peak track is created, destroyed, merged, split, changes critical order, loses `b`, or leaves the retained chart, the fixed-index derivation of Section 3 no longer applies without a source term.

The correct distributional ledger is then

\[
\boxed{
\partial_\theta F_\nu
+\partial_zG_\nu
=\mathcal B_\nu,
}
\]

where `B_nu` is the signed source/sink distribution induced by those track events.

Examples include

- creation of a type-`nu` track: positive source;
- loss of a type-`nu` track: negative source;
- transition `nu -> nu'`: sink in the `nu` ledger and, if a matched outgoing track is defined, a source in the `nu'` ledger.

No equality between these cross-type source strengths is claimed without an explicit track-matching rule.

---

## 6. Zero boundary as critical-type turnover

For a genuine type-`nu` maximum,

\[
Z_\nu<0.
\]

Higher degeneracy requires

\[
Z_\nu\to0
\]

while `b!=0`.

It is therefore natural to view the physical type-`nu` state domain as the half-line

\[
z<0.
\]

The one-sided current

\[
\boxed{G_\nu(0^-,\theta)}
\]

records the signed flux of tracked type-`nu` peaks into the turnover boundary, subject to the bookkeeping assumptions above.

A track need not continue to `z>0`; at `z=0` it may simply leave the type-`nu` class and enter the event source `B_nu`.

---

## 7. Recurrent single-track law

Suppose one moving type-`nu` peak is recurrent and remains uniformly separated from turnover:

\[
-c^*\le Z_\nu\le-c_*<0.
\]

Then

\[
D_*\log(-Z_\nu)
=\frac{D_*Z_\nu}{Z_\nu}.
\]

Since

\[
Z_\nu=\frac{H_\nu}{|b|^{\nu+1}},
\]

we obtain

\[
\boxed{
D_*\log(-Z_\nu)
=
\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{H_\nu}
+V_{rel}^{max}\cdot\nabla\log(-Z_\nu).
}
\]

A recurrent bounded track therefore satisfies

\[
\boxed{
\left\langle
\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{H_\nu}
+V_{rel}^{max}\cdot\nabla\log(-Z_\nu)
\right\rangle
=0.
}
\]

No sign follows from this equality.

---

## 8. DSD analysis

M17-093 supplied a scalar descriptor whose zero set represents type turnover.
M17-094 adds only the weakest justified population structure:

\[
\boxed{
\text{smooth tracked peaks}
\to
\text{empirical scalar distribution}
\to
\text{conditional continuity ledger}.
}
\]

The bookkeeping measure is deliberately kept separate from director area, material volume, vorticity flux, and M5 label measure.

---

## 9. DSD audit

### Audit A — inventing a canonical counting measure over maxima
Rejected. The weights `w_i` are fixed bookkeeping weights on an explicitly chosen track family.

### Audit B — claiming conservation through births/deaths/type switches
Rejected. All such events enter `B_nu`.

### Audit C — identifying `G_nu` with M5 kappa current
Rejected. They live on different descriptor spaces and use different populations/measures.

### Audit D — summing over critical orders as if type-switch sources cancel automatically
Rejected. Cross-`nu` matching must be constructed before such cancellation can be asserted.

### Audit E — proof status
The finite critical-type family now has a valid conditional crossing ledger, but no sign/cost theorem closes turnover.

---

## 10. Updated Rank-2 critical-type frontier

On the compact analytic two-ended decaying hull,

\[
\nu\in\{1,3,5,\ldots,\nu_*\}.
\]

Each retained type has

\[
\boxed{
Z_\nu<0,
\qquad
D_*Z_\nu
=S_\nu^{crit}+V_{rel}^{max}\cdot\nabla Z_\nu,
}
\]

plus the Riccati-survival margin

\[
\boxed{\mathcal M^{(\nu)}>0.}
\]

Type turnover is represented by

\[
\boxed{Z_\nu\to0}
\]

or by an explicit event in `B_nu` such as curvature/rank/chart degeneration.

---

## 11. Next target

A stronger Rank-2 closure would require a **geometrically inherited weight** — for example one derived from an already established flux/current — whose turnover across `Z_nu=0` has a sign or nonrecyclable cost.

M17-094 does not assume such a weight exists.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
