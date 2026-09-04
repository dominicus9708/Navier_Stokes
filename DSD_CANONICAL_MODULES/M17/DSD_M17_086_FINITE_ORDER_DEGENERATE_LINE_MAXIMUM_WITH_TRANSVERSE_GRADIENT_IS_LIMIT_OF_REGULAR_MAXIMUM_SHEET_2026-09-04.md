# DSD M17-086 — A finite-order degenerate line maximum with transverse gradient is a limit point of a regular maximum sheet

Date: 2026-09-04
Canonical ID: **M17-086**

Status: **INTERNAL DEGENERATE-MAXIMUM GEOMETRY REDUCTION / M17-085 REDUCED TWO-ENDED DECAYING PURE-KERNEL LINES TO FINITE REGULAR OR FINITE-ORDER DEGENERATE LINE MAXIMA. LET A DEGENERATE MAXIMUM HAVE FIRST NEGATIVE EVEN AMPLITUDE DERIVATIVE `D_xi^(2r) rho<0`, `r>=2`. THEN `g=D_xi log rho` HAS FIRST NONZERO LINE JET `H=D_xi^(2r-1)g<0`. IF ANY TRANSVERSE FIRST DERIVATIVE `D_eta g` IS NONZERO (`eta` IN `span{k,n}`), THE IMPLICIT FUNCTION THEOREM WRITES THE CRITICAL SET `g=0` LOCALLY AS A SMOOTH GRAPH THROUGH THE DEGENERATE POINT. ITS NEARBY NONCENTRAL POINTS HAVE `D_xi g<0` BECAUSE THE LEADING POWER `2r-2` IS EVEN. THEY ARE ORDINARY REGULAR LINE MAXIMA AND THEREFORE OBEY M17-079--080. SO SUCH A DEGENERATE MAXIMUM IS A TRANSITION/LIMIT POINT OF THE REGULAR MAXIMUM NETWORK, NOT AN INDEPENDENT NONCRITICAL SURVIVOR. A GENUINELY NEW PERSISTENT DEGENERATE BRANCH MUST AT LEAST SATISFY THE FULL FIRST-GRADIENT CRITICALITY `g=D_xi g=D_k g=D_n g=0` AND IS THEREFORE A HIGHER-JET CRITICAL/TOPOLOGY EVENT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Finite-order degenerate amplitude maximum

Let `s` be arclength along the vortex direction `xi` and let `s=0` be a positive linewise amplitude maximum.
Assume it is degenerate of finite order:

\[
\boxed{
D_\xi^j\rho(0)=0
\quad(1\le j<2r),
\qquad
D_\xi^{2r}\rho(0)<0,
\qquad
r\ge2.
}
\]

Set

\[
\boxed{g:=D_\xi\log\rho.}
\]

Because every lower amplitude derivative vanishes at the peak, the first nonzero line derivative of `g` is order

\[
2r-1.
\]

More precisely,

\[
\boxed{
H:=D_\xi^{2r-1}g(0)
=\frac{D_\xi^{2r}\rho(0)}{\rho(0)}<0.
}
\]

Thus locally along the central vortex line,

\[
\boxed{
g(x,0)
=\frac{H}{(2r-1)!}x^{2r-1}
+O(x^{2r}).}
\]

---

## 2. Add one transverse direction

Let

\[
\eta\in\operatorname{span}\{k,n\}
\]

be a transverse direction and use local coordinates `(x,y)` with `x` along `xi` and `y` along `eta`.
Define

\[
\boxed{A:=D_\eta g(0).}
\]

Suppose

\[
\boxed{A\neq0.}
\]

Then the local Taylor form is

\[
\boxed{
g(x,y)
=\frac{H}{(2r-1)!}x^{2r-1}
+A y
+\text{higher terms}.}
\]

Because the derivative with respect to `y` is nonzero at the origin, the implicit function theorem applies to the critical set

\[
g=0.
\]

---

## 3. The critical set is a smooth cusp-flat graph

There exists a smooth local function

\[
y=f(x)
\]

with

\[
f(0)=0
\]

such that

\[
\boxed{g(x,f(x))=0.}
\]

Its leading behavior is

\[
\boxed{
f(x)
=-\frac{H}{A(2r-1)!}x^{2r-1}
+o(x^{2r-1}).}
\]

Since `2r-1>=3`,

\[
f'(0)=0.
\]

Thus the degenerate point is a high-contact point of a smooth critical sheet whose tangent there is the vortex-line direction.

This explains why the regular tilt formula `Theta=D_n g/(-C)` blows up as the degenerate point is approached: the regular-sheet tangent rotates toward `xi`.

---

## 4. Nearby critical points are regular maxima

Differentiate the leading Taylor form in the line direction:

\[
D_\xi g(x,f(x))
=\frac{H}{(2r-2)!}x^{2r-2}
+o(x^{2r-2}).
\]

The exponent

\[
2r-2
\]

is even.
Since

\[
H<0,
\]

for every sufficiently small nonzero `x`,

\[
\boxed{
D_\xi g(x,f(x))<0.
}
\]

Therefore the neighboring points of the same critical sheet are ordinary nondegenerate line maxima:

\[
\boxed{
g=0,
\qquad
C=D_\xi g<0.}
\]

They fall directly under M17-079--080.

---

## 5. Degenerate point is a boundary point of the unified margin regime

At the neighboring regular maxima the exact law is

\[
D_Tq
=2q^2-\mathcal M_{R2},
\]

with

\[
\mathcal M_{R2}
=C+rD_ks-\Theta D_\xi q.
\]

As the critical sheet approaches the degenerate point,

\[
C\to0^-.
\]

The coordinate `Theta` may diverge because the tangent representation `n+Theta xi` is no longer well conditioned; the geometric tangent itself remains finite after normalization and approaches the `xi` direction.

Hence the degenerate point should be treated as a **chart boundary of the regular maximum ledger**, not by substituting `C=0` into formulas containing `1/C`.

---

## 6. General transverse gradient

The argument does not depend on choosing `n` specifically.
If either

\[
D_ng\neq0
\]

or

\[
D_kg\neq0,
\]

choose a transverse direction `eta` with

\[
D_\eta g\neq0.
\]

Then the same implicit-function reduction applies.
Therefore

\[
\boxed{
C=0
\quad+\quad
|\nabla_\perp g|>0
\Longrightarrow
\text{degenerate point is a limit of regular M17-079 maxima}.}
\]

---

## 7. The genuinely new degenerate class

For a finite-order degenerate maximum to avoid the reduction above, it must satisfy

\[
D_ng=0,
\qquad
D_kg=0.
\]

Together with the defining conditions

\[
g=0,
\qquad
D_\xi g=0,
\]

we get the full first-gradient criticality

\[
\boxed{
 g=0,
\qquad
\nabla g=0.
}
\]

Equivalently in the intrinsic frame,

\[
\boxed{
 g=0,
\quad
D_\xi g=0,
\quad
D_k g=0,
\quad
D_n g=0.
}
\]

This is no longer merely a flat line maximum.
It is a higher-jet critical event of the full three-dimensional amplitude-gradient field.

---

## 8. Relation to oscillatory tails

If an oscillatory tail produces infinitely many line maxima and infinitely many of them have nonzero transverse gradient of `g`, those maxima are connected locally to regular maximum sheets and therefore repeatedly enter the M17-079--080 recharge ledger.

To avoid that ledger at every critical event, an oscillatory survivor would have to concentrate its extrema in the much narrower class

\[
\boxed{g=0,\qquad\nabla g=0}
\]

with finite higher-order jets.

Thus oscillatory-tail escape becomes a repeated higher-jet degeneration requirement rather than an absence of critical points.

---

## 9. DSD analysis

M17-085 produced the split

\[
\text{regular maximum}
\ \lor\
\text{finite-order degenerate maximum}.
\]

M17-086 now refines the second term:

\[
\boxed{
R_{max}^{deg}
\Longrightarrow
\overline{R_{max}^{regular}}
\ \lor\
R_{\nabla g=0}^{higher\ jet}.
}
\]

The bar indicates closure/limit of the regular maximum set, not an additional independent branch.

Thus the genuinely new descriptor is not `C=0` alone but the full criticality of the amplitude-gradient field.

---

## 10. DSD audit

### Audit A — dividing by C at the degenerate point
Rejected. The regular tilt coordinate becomes singular and is replaced by the implicit critical-sheet geometry.

### Audit B — assuming the zero set of g is singular whenever C=0
Rejected. If a transverse derivative is nonzero, `g=0` is a smooth sheet by the implicit function theorem.

### Audit C — assuming nearby roots might be minima
The sign is fixed by the even power `x^(2r-2)` and `H<0`; sufficiently nearby noncentral critical points have `D_xi g<0` and are maxima.

### Audit D — turning limit of regular maxima into a pointwise M17-079 equation at C=0
Rejected. M17-079 applies on neighboring regular points; the degenerate point is a chart/transition limit and requires a separate limiting audit.

### Audit E — claiming g=grad g=0 is impossible
Not claimed. It is retained as the genuine higher-jet critical survivor.

### Audit F — proof status
The degenerate maximum branch is narrowed but not closed.

---

## 11. Corrected Rank-2 peak frontier

On the two-ended decaying pure-kernel subclass,

\[
\boxed{
R_{2,pk}^{two-end\ decay}
\Longrightarrow
R_{2,max}^{regular}
\ \lor\
R_{2,crit}^{g=0,\nabla g=0,higher\ jet}.
}
\]

The first branch is governed by M17-079--080.
The second is a finite-jet critical event.

More generally,

\[
\boxed{
R_{2,pk}
\Longrightarrow
R_{2,max}^{regular}
\ \lor\
R_{2,crit}^{g=0,\nabla g=0}
\ \lor\
R_{2,end}^{nondecay/recurrence}
\ \lor\
T_{2,pk}.
}
\]

---

## 12. Next target — full critical amplitude-jet audit

The next Rank-2 target is now sharply defined:

\[
\boxed{
g=0,
\qquad
\nabla g=0.}
\]

At such a point, use the weighted-harmonic amplitude equation

\[
\Delta\rho=(\kappa+|\nabla\xi|^2)\rho
\]

and the first nonzero even line jet to classify the Hessian/higher-jet signatures of the full amplitude critical point.

The aim is to determine whether compact recurrence forces

1. nearby regular maximum sheets;
2. rank/director degeneration;
3. a finite list of analytic catastrophe types;
4. or a genuinely persistent high-order critical branch.

This is the **Full Critical Amplitude-Jet Audit (FCAJA)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
