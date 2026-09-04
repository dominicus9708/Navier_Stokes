# DSD M17-093 — The curvature-normalized Rank-2 critical jet is strain free; type turnover is its zero crossing

Date: 2026-09-04
Canonical ID: **M17-093**

Status: **INTERNAL RANK-2 CRITICAL-TYPE NORMALIZATION / M17-092 GIVES `D_B H_nu=D_xi^(nu+1)(sigma+kappa)-(nu+1)(sigma+1/2)H_nu` AT A FIXED TYPE-`nu` LINE MAXIMUM. ON THE FULL-RANK PURE-TRANSVERSE-KERNEL BRANCH M17-033 GIVES THE NONZERO VORTEX-DIRECTION CURVATURE `b=(xi·grad)xi` WITH `D_B|b|=-(sigma+1/2)|b|`. THEREFORE THE NORMALIZED TOP CRITICAL JET `Z_nu:=H_nu/|b|^(nu+1)` HAS EXACTLY CANCELLED STRAIN MULTIPLIER: `D_B Z_nu=|b|^-(nu+1) D_xi^(nu+1)(sigma+kappa)`. ALONG A MOVING MAXIMUM THE ONLY EXTRA TERM IS RELATIVE TRANSPORT `V_rel^max·grad Z_nu`. TYPE INCREASE TO HIGHER DEGENERACY IS EXACTLY `Z_nu->0` WHILE `b` REMAINS NONZERO; LOSS OF `b` IS A SEPARATE DIRECTOR-GEOMETRY DEGENERATION. THUS THE FINITE CRITICAL-TYPE TURNOVER PROBLEM OF M17-088 CAN BE REPRESENTED BY STRAIN-FREE ZERO-CROSSING CURRENTS OF `Z_nu` RATHER THAN BY RAW HIGHER JETS WITH CHANGING STRAIN EXPONENTS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Raw top critical-jet law

At a type-`nu` Rank-2 line maximum, M17-092 defines

\[
H_\nu:=D_\xi^\nu g<0,
\qquad
 g=D_\xi\log\rho,
\]

with every lower line jet zero.
Its exact material law is

\[
\boxed{
D_BH_\nu
=D_\xi^{\nu+1}(\sigma+\kappa)
-(\nu+1)(\sigma+\frac12)H_\nu.
}
\]

The raw critical amplitude therefore carries a strain-dependent homogeneous multiplier.

---

## 2. Nonzero vortex-direction curvature on the pure-kernel full-rank branch

M17-033 defines

\[
\boxed{
b:=(\xi\cdot\nabla)\xi.}
\]

On the full-rank pure-transverse-kernel branch,

\[
\boxed{b\neq0.}
\]

Its material law is

\[
\boxed{
D_Bb
=-(\sigma+\frac12)b.
}
\]

Therefore

\[
\boxed{
D_B|b|
=-(\sigma+\frac12)|b|.
}
\]

The scalar `|b|` carries precisely the same strain multiplier as one line derivative of the critical geometry.

---

## 3. Curvature-normalized top critical jet

Define

\[
\boxed{
Z_\nu
:=\frac{H_\nu}{|b|^{\nu+1}}.
}
\]

This is regular on the retained full-rank pure-kernel class because `|b|>0`.

Differentiate:

\[
\begin{aligned}
D_BZ_\nu
={}&|b|^{-(\nu+1)}D_BH_\nu\\
&-(\nu+1)H_\nu|b|^{-(\nu+2)}D_B|b|.
\end{aligned}
\]

Use Sections 1--2.
The two homogeneous strain terms cancel exactly:

\[
\boxed{
D_BZ_\nu
=\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{|b|^{\nu+1}}.
}
\]

Define the normalized recharge source

\[
\boxed{
S_\nu^{crit}
:=\frac{D_\xi^{\nu+1}(\sigma+\kappa)}{|b|^{\nu+1}}.
}
\]

Then simply

\[
\boxed{D_BZ_\nu=S_\nu^{crit}.}
\]

---

## 4. No homogeneous damping remains

Unlike the raw `H_nu` equation, the normalized variable has no term proportional to

\[
\sigma Z_\nu,
\qquad
Z_\nu,
\qquad
\kappa Z_\nu.
\]

Thus the critical-type amplitude is separated into

1. a purely geometric scale `|b|^(nu+1)`;
2. a strain-free normalized critical shape `Z_nu`;
3. an explicit higher-line-jet source `S_nu^crit`.

This is stronger than a mean-exponent cancellation: it is pointwise and exact.

---

## 5. Moving maximum law

Let a type-`nu` critical point move with

\[
\dot X_*=B+V_{rel}^{max}.
\]

Define

\[
D_*:=D_B+V_{rel}^{max}\cdot\nabla.
\]

Then

\[
\boxed{
D_*Z_\nu
=S_\nu^{crit}
+V_{rel}^{max}\cdot\nabla Z_\nu.
}
\]

There is still no strain multiplier.
The only mechanisms changing the normalized critical amplitude are

\[
\boxed{
\text{higher-line-jet recharge}
\quad+
\text{relative transport}.
}
\]

---

## 6. Recurrent type balance

Suppose a moving type-`nu` peak is recurrent with

\[
-c^*\le Z_\nu\le-c_*<0
\]

on recurrence intervals.
Then the long-time mean drift of `Z_nu` vanishes, giving

\[
\boxed{
\left\langle
S_\nu^{crit}
+V_{rel}^{max}\cdot\nabla Z_\nu
\right\rangle=0.
}
\]

No mean strain hypothesis is required.

This is the cleanest type-maintenance ledger obtained so far.

---

## 7. Type turnover is a zero crossing of Z_nu

While

\[
|b|>0,
\]

we have

\[
H_\nu=|b|^{\nu+1}Z_\nu.
\]

Therefore

\[
\boxed{
H_\nu=0
\iff
Z_\nu=0.
}
\]

A transition from type `nu` to a higher degeneracy order therefore requires

\[
\boxed{Z_\nu\to0.}
\]

This is an ordinary scalar zero-crossing event in the normalized critical descriptor.

If instead

\[
|b|\to0,
\]

the normalization itself loses validity and the branch exits to the distinct director-curvature degeneration class.

---

## 8. Downward versus upward type crossings

Because a maximum type has

\[
Z_\nu<0,
\]

approach to a higher degeneracy order means the negative quantity rises toward zero.
The sign of

\[
D_*Z_\nu
\]

at the crossing therefore distinguishes whether the current type is disappearing or re-entering.

Using Section 5, this sign is controlled by

\[
\boxed{
S_\nu^{crit}
+V_{rel}^{max}\cdot\nabla Z_\nu.
}
\]

Thus type turnover admits the same general current language as the M5 kappa-zero crossing problem, but its source variable is a higher normalized line jet rather than `h=D_B kappa`.

No covariance relation between those two currents is assumed.

---

## 9. Finite-state turnover on the compact decaying hull

M17-088 gives a finite critical-order set

\[
\nu\in\{1,3,5,\ldots,\nu_*\}
\]

on the retained compact stable two-end decaying hull.

For every state `nu`, M17-093 supplies a strain-free scalar `Z_nu` whose zero set carries transitions out of that type.

Therefore a type-resolved turnover current can be built from the crossing fluxes of finitely many scalar fields

\[
\boxed{
Z_1,Z_3,\ldots,Z_{\nu_*}.
}
\]

This is substantially more concrete than counting critical points or assigning discrete transition rates by hand.

---

## 10. Relation to the Riccati compensation margin

Type persistence and Riccati survival remain distinct obligations:

\[
\boxed{
Z_\nu\neq0
}
\]

maintains the critical order, while

\[
\boxed{
\mathcal M^{(\nu)}>0
}

prevents the corresponding critical sheet from entering the super/exact Riccati obstruction.

A recurrent survivor must therefore maintain both a nonzero normalized type amplitude and a positive compensation margin.

The next useful step is to search for a common weight/current coupling these two scalar ledgers.

---

## 11. DSD analysis

The raw hierarchy

\[
H_\nu
\]

mixed critical shape with local vortex-line curvature scale.
The normalized hierarchy

\[
Z_\nu=H_\nu/|b|^{\nu+1}
\]

separates them.

This is a DSD descriptor improvement:

\[
\boxed{
\text{raw critical jet}
\to
\text{curvature scale}
\times
\text{strain-free normalized type descriptor}.
}
\]

---

## 12. DSD audit

### Audit A — dividing by b at curvature degeneration
Rejected. `Z_nu` is used only on the full-rank pure-kernel class where `b!=0`; `b->0` is an explicit exit.

### Audit B — claiming the normalized source is sign definite
Rejected. `D_xi^(nu+1)(sigma+kappa)` is signed.

### Audit C — confusing a Z_nu zero with rank loss
Rejected. `Z_nu=0` with `b!=0` is a critical-order turnover; `b=0` is a separate director-curvature degeneration.

### Audit D — applying material recurrence to moving maxima
Avoided. The relative-transport term remains explicit.

### Audit E — identifying critical-type current with M5 kappa current
Rejected. They are distinct scalar crossing ledgers unless a new covariance theorem connects them.

### Audit F — proof status
The critical-type ledger is normalized but not closed.

---

## 13. Updated RCTTG state variables

On the compact decaying Rank-2 hard hull the natural state is now

\[
\boxed{
(\nu,
Z_\nu,
\mathcal M^{(\nu)},
V_{rel}^{max}).
}
\]

with

\[
\boxed{
D_*Z_\nu
=S_\nu^{crit}+V_{rel}^{max}\cdot\nabla Z_\nu
}
\]

and

\[
\boxed{
\mathcal M^{(\nu)}>0.
}
\]

Type turnover occurs at `Z_nu=0` or at a lower-jet/rank/interface exit.

---

## 14. Next target

Derive a flux-weighted crossing identity for the finite family of normalized type fields `Z_nu`, analogous in form to M5-685 but using the critical-peak population and a geometrically justified peak weight.

The key audit problem is to choose that weight from an existing invariant/current rather than inventing a counting measure over maxima.

Until such a measure is identified, a type-transition covariance claim would be premature.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
