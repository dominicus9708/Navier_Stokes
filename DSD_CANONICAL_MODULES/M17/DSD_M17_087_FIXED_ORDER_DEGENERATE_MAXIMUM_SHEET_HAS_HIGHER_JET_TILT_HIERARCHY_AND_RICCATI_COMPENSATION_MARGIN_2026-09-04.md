# DSD M17-087 — A fixed-order degenerate maximum sheet has a higher-jet tilt hierarchy and Riccati compensation margin

Date: 2026-09-04
Canonical ID: **M17-087**

Status: **INTERNAL DEGENERATE MAXIMUM FINITE-JET GATE / LET A PURE-KERNEL LINE MAXIMUM HAVE FIRST NEGATIVE AMPLITUDE DERIVATIVE ORDER `2r>=4`, SO `g=D_xi log rho` SATISFIES `G_j=D_xi^j g=0` FOR `0<=j<=nu-1`, `nu=2r-1`, AND `H_nu=D_xi^nu g<0`. TO PERSIST AS A FIXED-DEGENERACY MAXIMUM SHEET WITH TANGENT `T=n+Theta_nu xi`, EVERY LOWER VANISHING JET MUST REMAIN ZERO. FOR `j<=nu-2`, `D_TG_j=D_nG_j` BECAUSE `G_{j+1}=0`, SO PERSISTENCE FORCES THE HIERARCHY `D_nD_xi^j g=0`. AT THE TOP VANISHING JET, `D_TG_{nu-1}=D_nG_{nu-1}+Theta_nu H_nu=0`, GIVING THE HIGHER-JET TILT `Theta_nu=-(D_nD_xi^(nu-1)g)/(D_xi^nu g)`. THE ANGLE-UNIFORM FLATNESS LAW OF M17-079 IS VALID AT `g=0` WITHOUT DIVIDING BY `C`; WITH `C=D_xi g=0` IT BECOMES `D_nq=2q^2-rD_ks`. ALONG THE FIXED-DEGENERACY TANGENT, `D_Tq=2q^2-M_deg^(nu)` WITH `M_deg^(nu)=rD_ks-Theta_nu D_xi q`. THUS A COMPLETE PERSISTENT DEGENERATE MAXIMUM SHEET MUST SERVICE `M_deg^(nu)>0` TO AVOID THE SAME RICCATI FOCUSING OBSTRUCTION. IF ANY LOWER-JET TRANSVERSE CONDITION FAILS, THE BRANCH EXITS TO A LOWER-ORDER/REGULAR MAXIMUM OR A CRITICAL TOPOLOGY EVENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed finite degeneracy order

Let `s` be vortex-line arclength and suppose a positive amplitude maximum has first nonzero line derivative of `rho` at even order

\[
2r\ge4.
\]

Set

\[
\boxed{
\nu:=2r-1\ge3,
\qquad
g:=D_\xi\log\rho.
}
\]

At the maximum,

\[
\boxed{
G_j:=D_\xi^jg=0
\qquad(0\le j\le\nu-1),
}
\]

while

\[
\boxed{
H_\nu:=D_\xi^\nu g<0.
}
\]

The sign follows from the negative first nonzero even derivative of `rho` as in M17-086.

---

## 2. A persistent fixed-order sheet must preserve every vanishing jet

Suppose this degeneracy order persists on a local critical sheet and choose a candidate tangent in the `xi-n` plane:

\[
\boxed{
T=n+\Theta_\nu\xi.
}
\]

For every scalar `G_j`,

\[
D_TG_j
=D_nG_j+\Theta_\nu D_\xi G_j
=D_nG_j+\Theta_\nu G_{j+1}.
\]

Persistence of the fixed degeneracy requires

\[
D_TG_j=0
\]

for every

\[
0\le j\le\nu-1.
\]

---

## 3. Lower-jet transverse compatibility hierarchy

For

\[
0\le j\le\nu-2,
\]

we have

\[
G_{j+1}=0.
\]

Therefore the tangent parameter cannot repair a transverse failure:

\[
D_TG_j=D_nG_j.
\]

Hence fixed-order persistence forces

\[
\boxed{
D_nD_\xi^jg=0
\qquad(0\le j\le\nu-2).
}
\]

This is the degenerate-maximum analogue of the lower alignment hierarchy in Rank 1.

If any one of these conditions fails, the retained fixed-order degenerate sheet cannot continue in the `n` direction. The event must be reclassified as

\[
\boxed{
\text{lower-order/regular maximum transition}
\ \lor\
\text{critical-sheet topology change}
\ \lor\
\text{chart/interface exit}.
}
\]

---

## 4. The top vanishing jet determines the higher-order tilt

For

\[
j=\nu-1,
\]

we have

\[
D_\xi G_{\nu-1}=G_\nu=H_\nu\neq0.
\]

Therefore

\[
0=D_TG_{\nu-1}
=D_nG_{\nu-1}+\Theta_\nu H_\nu.
\]

Thus

\[
\boxed{
\Theta_\nu
=-\frac{D_nD_\xi^{\nu-1}g}{D_\xi^\nu g}.
}
\]

This is well defined because

\[
D_\xi^\nu g<0.
\]

It is the finite-jet replacement for the regular maximum tilt

\[
\Theta=\frac{D_ng}{-D_\xi g}.
\]

Indeed, in the nondegenerate case `nu=1`, the same pattern formally reduces to the ordinary regular-sheet construction.

---

## 5. Angle-uniform flatness remains valid at C=0

M17-079 derives, after differentiating the full normalized shear field before restriction to the critical set,

\[
\boxed{
D_nq
=2q^2-C-rD_ks,
}
\]

where

\[
C:=D_\xi g.
\]

This identity requires

\[
g=0
\]

but does not require division by `C`.

At a degenerate maximum,

\[
C=0,
\]

so

\[
\boxed{
D_nq
=2q^2-rD_ks.
}
\]

Thus the local flatness mechanism does not disappear when the ordinary maximum curvature vanishes.

---

## 6. Higher-jet tangent Riccati law

Along

\[
T=n+\Theta_\nu\xi,
\]

we have

\[
D_Tq
=D_nq+\Theta_\nu D_\xi q.
\]

Use Section 5:

\[
D_Tq
=2q^2-rD_ks+\Theta_\nu D_\xi q.
\]

Define the degenerate compensation margin

\[
\boxed{
\mathcal M_{deg}^{(\nu)}
:=rD_ks-\Theta_\nu D_\xi q.
}
\]

Then

\[
\boxed{
D_Tq
=2q^2-\mathcal M_{deg}^{(\nu)}.
}
\]

The three regimes are exactly analogous to M17-079:

\[
\mathcal M_{deg}^{(\nu)}<0
\Longrightarrow
D_Tq>2q^2,
\]

\[
\mathcal M_{deg}^{(\nu)}=0
\Longrightarrow
D_Tq=2q^2,
\]

\[
\mathcal M_{deg}^{(\nu)}>0
\Longrightarrow
D_Tq<2q^2.
\]

---

## 7. Persistent complete-sheet survival requires positive compensation

The reciprocal Riccati comparison used in M17-048 applies whenever the retained critical-sheet tangent is complete enough for the inequality to be integrated and no branch/interface exit intervenes.

Therefore a persistent complete fixed-order degenerate maximum sheet cannot remain in the super/exact Riccati regime.
It must satisfy

\[
\boxed{
\mathcal M_{deg}^{(\nu)}>0
}
\]

or leave the sheet before the Riccati obstruction becomes applicable.

Thus finite-order degeneracy removes the direct curvature payment `C<0`, but it does not create a free escape. The payment must come from

\[
\boxed{
rD_ks
\quad\text{and/or}\quad
-\Theta_\nu D_\xi q.
}
\]

---

## 8. Orthogonal and frozen-angle limits remain unified

The normalized shear

\[
s=\frac{a\cdot b}{|a|^2}
\]

is division-free across the orthogonal limit.
Therefore the degenerate margin

\[
\mathcal M_{deg}^{(\nu)}
=rD_ks-\Theta_\nu D_\xi q
\]

has the same branch unification as M17-079:

- on an exact orthogonal component, `s=0` and the payment is entirely higher-jet tilt/mixed geometry;
- on a nonzero-angle component, `rD_ks` is the normalized-shear-gradient payment;
- at spatial angle interfaces, the interface remains a separate turnover class.

No logarithm of `s` is required.

---

## 9. Why the lower hierarchy matters

It is not enough to define `Theta_nu` from the top vanishing jet.
For `j<=nu-2`, the line derivative `G_{j+1}` vanishes, so no choice of `Theta_nu` can cancel a nonzero

\[
D_nG_j.
\]

Hence the true fixed-order branch carries the full set

\[
\boxed{
D_nD_\xi^jg=0
\qquad(0\le j\le\nu-2),
}
\]

plus the top tilt equation.

This is a finite codimension jet-locking hierarchy, not merely a single higher-order tilt formula.

---

## 10. k-direction companion hierarchy

A two-dimensional fixed-degeneracy critical sheet also requires compatibility in the independent transverse `k` direction.
Exactly the same argument gives

\[
\boxed{
D_kD_\xi^jg=0
\qquad(0\le j\le\nu-2),
}
\]

with its top-order sheet tilt determined by

\[
\boxed{
\Theta_{\nu,k}
=-\frac{D_kD_\xi^{\nu-1}g}{D_\xi^\nu g}.
}
\]

Thus a genuinely persistent fixed-order degenerate maximum surface is locked by two transverse finite-jet hierarchies.

---

## 11. DSD analysis

The degenerate maximum branch is now described by

\[
\boxed{
\text{critical order }\nu
+
\text{lower transverse jet locks}
+
\text{top higher-jet tilt}
+
\text{Riccati compensation margin}.
}
\]

This replaces the vague descriptor "degenerate maximum" by a finite list of explicit conditions once `nu` is fixed.

---

## 12. DSD audit

### Audit A — using the regular tilt at C=0
Rejected. The correct denominator is the first nonzero line jet `D_xi^nu g`, not `C`.

### Audit B — preserving only the top critical jet
Rejected. Every lower vanishing line jet must remain zero; these produce independent transverse compatibility equations.

### Audit C — claiming the flatness law vanishes with C
Rejected. The `rD_k s` compensation remains in `D_nq=2q^2-rD_ks`.

### Audit D — applying Riccati comparison without a persistent tangent sheet
Restricted correctly. If the fixed-order sheet terminates, changes order, or hits an interface before the comparison applies, that is a turnover exit rather than a contradiction.

### Audit E — claiming finite order is uniformly bounded across the whole hull
Not yet proved here. M17-085--086 provide pointwise finite order under analyticity; a compact-hull uniform-order result remains a separate audit.

### Audit F — proof status
The degenerate branch has an explicit finite-jet gate but is not closed.

---

## 13. Corrected Rank-2 maximum frontier

The peak geometry is now

\[
\boxed{
R_{2,max}
\Longrightarrow
R_{2,max}^{regular,\mathcal M_{R2}>0}
\ \lor\
R_{2,max}^{deg,\nu,\mathcal M_{deg}^{(\nu)}>0}
\ \lor\
T_{max/order/interface}.
}
\]

For the degenerate class, survival additionally requires the lower transverse jet-lock hierarchy in Sections 3 and 10.

Thus the former tail gap has been converted into a regular-or-finite-jet maximum compensation problem on the two-ended decaying subclass.

---

## 14. Next target — uniform critical-order compactness gate

The next high-value question is whether the compact analytic hard hull supplies a uniform upper bound

\[
\nu\le\nu_*<\infty
\]

for persistent Rank-2 line maxima, analogous to M17-009's finite nodal-event jet order.

If yes, the entire decaying/oscillatory Rank-2 peak problem reduces to a finite collection of explicit compensation hierarchies rather than an unbounded tower of critical orders.

This is the **Uniform Rank-2 Critical-Order Gate (URCOG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
