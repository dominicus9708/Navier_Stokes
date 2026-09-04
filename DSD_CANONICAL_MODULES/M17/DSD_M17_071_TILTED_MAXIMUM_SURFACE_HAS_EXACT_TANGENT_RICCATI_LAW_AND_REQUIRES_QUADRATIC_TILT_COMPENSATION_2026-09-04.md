# DSD M17-071 — A tilted maximum surface has an exact tangent Riccati law and requires a quadratic tilt-compensation payment

Date: 2026-09-04
Canonical ID: **M17-071**

Status: **INTERNAL RANK-TWO TILTED-MAXIMUM REDUCTION / ON THE ORTHOGONAL PURE-KERNEL BRANCH, LET `g=D_xi log rho` AND CONSIDER A REGULAR LINEWISE MAXIMUM SHEET `C={g=0}` WITH `C_xi:=D_xi g<0` AND TILT NUMERATOR `A_n:=D_n g`. THE M17-049 TILT `Theta=A_n/(-C_xi)` DEFINES THE ACTUAL IN-SURFACE DIRECTION `T=n+Theta xi`, SINCE `D_T g=0`. M17-047 GIVES `D_n q=2q^2-C_xi` AT EVERY CROSS-ALIGNED CRITICAL POINT. THEREFORE THE TANGENT DERIVATIVE IS EXACTLY `D_T q=2q^2-C_xi+Theta D_xi q`. BECAUSE `C_xi<0`, THE EXCESS OVER THE RICCATI RATE HAS THE SIGN OF `C_xi^2+A_n D_xi q`. THUS TILT DOES NOT AUTOMATICALLY ESCAPE THE M17-048 FOCUSING MECHANISM: TO BECOME SUB-RICCATI ALONG THE MAXIMUM SURFACE IT MUST PAY THE SHARP SIGNED COST `A_n D_xi q < -C_xi^2`. IF `C_xi^2+A_n D_xi q >=0` PERSISTS ALONG A COMPLETE T-INTEGRAL CURVE WITH BOUNDED TILT, THE RECIPROCAL COMPARISON AGAIN GIVES A FINITE-DISTANCE OBSTRUCTION. THE SURVIVING TILTED MAXIMUM NETWORK IS THEREFORE REDUCED TO A STRONGLY COMPENSATED CROSS-GRADIENT CLASS OR TO FINITE INTERFACE/DEGENERATION EXITS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular maximum critical surface

On the orthogonal-stretch pure-kernel Rank-2 branch define

\[
\boxed{g:=D_\xi\log\rho.}
\]

A nondegenerate linewise maximum satisfies

\[
\boxed{
g=0,
\qquad
C:=D_\xi g<0.}
\]

Since `C != 0`, the implicit-function theorem gives a regular local surface

\[
\boxed{\mathcal C_{max}:=\{g=0,\ D_\xi g<0\}.}
\]

Define the transverse derivative

\[
\boxed{A:=D_ng.}
\]

M17-049 uses the signed tilt ratio

\[
\boxed{
\Theta:=\frac{A}{-C}.
}
\]

The previously closed M17-048 class is `A=0`; the current survivor has `A != 0` on at least part of the maximum sheet.

---

## 2. The actual in-surface tilted direction

Define the nonunit vector

\[
\boxed{T:=n+\Theta\xi.}
\]

Then

\[
D_Tg
=D_ng+\Theta D_\xi g
=A+\frac{A}{-C}C
=0.
\]

Therefore

\[
\boxed{T\in T\mathcal C_{max}.}
\]

Thus the M17-049 tilt ratio has a direct geometric meaning: it is exactly the amount of vortex-direction motion that must be added to `n` in order to remain on the critical surface.

The unit tangent is

\[
\widehat T
=\frac{T}{\sqrt{1+\Theta^2}},
\]

but the unnormalized `T` is algebraically cleaner for the Riccati comparison.

---

## 3. Cross-aligned critical flatness input

M17-040 shows that every orthogonal-stretch line critical point is cross aligned:

\[
D_\xi\xi=q\,n,
\qquad
D_n\xi=r\,k,
\]

with

\[
q\neq0,
\qquad
r\neq0
\]

on the full-rank branch.

M17-047 gives the exact Euclidean-flatness identity

\[
\boxed{
D_nq
=2q^2-D_\xi g.
}
\]

On the maximum sheet this is

\[
\boxed{
D_nq
=2q^2-C
=2q^2+|C|.
}
\]

---

## 4. Exact tangent derivative of q

Because

\[
T=n+\Theta\xi,
\]

we have

\[
D_Tq
=D_nq+\Theta D_\xi q.
\]

Insert Section 3:

\[
\boxed{
D_Tq
=2q^2-C+\Theta D_\xi q.
}
\]

This is the exact **tilted maximum-surface tangent Riccati law**.

The extra term

\[
\Theta D_\xi q
\]

is the sole local escape from the M17-048 `n`-tangent super-Riccati rate.

---

## 5. Rewrite the excess in a sharp quadratic form

Use

\[
\Theta=-\frac AC.
\]

Then

\[
-C+\Theta D_\xi q
=-C-\frac{A}{C}D_\xi q.
\]

Since `C<0`,

\[
\boxed{
-C+\Theta D_\xi q
=
-\frac1C
\left(
C^2+A D_\xi q
\right).
}
\]

The prefactor

\[
-\frac1C>0.
\]

Therefore the sign of the excess over `2q^2` is exactly the sign of

\[
\boxed{
\mathcal K_{tilt}
:=C^2+A D_\xi q.
}
\]

This is the new canonical tilted-maximum compensation descriptor.

---

## 6. Three tangent regimes

The maximum sheet therefore splits pointwise into three exact classes.

### Super-Riccati tangent class

If

\[
\boxed{
\mathcal K_{tilt}>0,
}
\]

then

\[
\boxed{D_Tq>2q^2.}
\]

### Exact-Riccati tangent class

If

\[
\boxed{
\mathcal K_{tilt}=0,
}
\]

then

\[
\boxed{D_Tq=2q^2.}
\]

### Sub-Riccati compensated class

If

\[
\boxed{
\mathcal K_{tilt}<0,
}
\]

then

\[
\boxed{D_Tq<2q^2.}
\]

Hence **tilt alone is not the escape**.
The escape is the stronger signed cross-gradient condition

\[
\boxed{
A D_\xi q<-C^2.
}
\]

---

## 7. Sharp compensation cost

Since

\[
C^2>0,
\]

the sub-Riccati condition implies

\[
\boxed{A D_\xi q<0.}
\]

Thus the transverse critical-surface slope and the vortex-direction gradient of the curvature coefficient `q` must have opposite signs.

Moreover their product must satisfy the quantitative lower bound

\[
\boxed{
|A D_\xi q|>C^2.
}
\]

So a tilted maximum can avoid the Riccati rate only by paying at least the square of the linewise amplitude curvature.

This is substantially stronger than the previous condition

\[
A\neq0.
\]

---

## 8. Persistent nonnegative K_tilt gives a Riccati obstruction along the maximum surface

Let `gamma(s)` be an integral curve of `T` contained in a regular maximum component:

\[
\frac{d\gamma}{ds}=T(\gamma(s)).
\]

Assume on an interval that

\[
\boxed{\mathcal K_{tilt}\ge0.}
\]

Then

\[
\boxed{
\frac{dq}{ds}
=D_Tq
\ge2q^2.
}
\]

For

\[
q\neq0,
\]

define

\[
u:=1/q.
\]

Then

\[
\boxed{
\frac{du}{ds}
=-\frac{q'}{q^2}
\le-2.
}
\]

The same reciprocal comparison as M17-048 follows.
Thus a two-sided complete `T`-parameter curve cannot remain forever in a smooth full-rank maximum component with `K_tilt >= 0` and finite nonzero `q`.

At least one branch assumption must fail at finite `T`-parameter distance.

---

## 9. Euclidean-distance version requires bounded tilt

The parameter of `T` is not arc length because

\[
|T|=\sqrt{1+\Theta^2}.
\]

If the retained recurrent compact branch has a uniform tilt bound

\[
\boxed{|\Theta|\le\Theta_*<\infty,}
\]

then

\[
1\le|T|\le\sqrt{1+\Theta_*^2}.
\]

Finite `T`-parameter distance is then equivalent, up to fixed constants, to finite Euclidean arc length.

Therefore under uniform nondegeneracy/bounded tilt,

\[
\boxed{
\mathcal K_{tilt}\ge0
\text{ on a complete maximum tangent curve}
\Longrightarrow\bot.
}
\]

Without a tilt bound, only the finite `T`-parameter obstruction is claimed.

---

## 10. Relation to the n-tangent class

If

\[
A=0,
\]

then

\[
\Theta=0,
\qquad
T=n.
\]

Also

\[
\mathcal K_{tilt}=C^2>0.
\]

Hence M17-071 reduces exactly to the M17-048 super-Riccati maximum obstruction.

Thus the old n-tangent closure is the zero-tilt endpoint of the new tangent-surface law.

---

## 11. What a complete tilted maximum survivor must do

A complete regular maximum-surface tangent curve that avoids the Riccati obstruction must enter the strictly compensated region

\[
\boxed{
\mathcal K_{tilt}<0
}
\]

before the reciprocal focal distance is reached.

Equivalently it must realize

\[
\boxed{
A D_\xi q<-C^2.
}
\]

Thus the surviving tilted network is not arbitrary.
It requires repeated strong cross-gradient compensation.

Allowed alternatives remain

\[
\boxed{
\text{finite patch termination}
\ \lor\
\text{critical degeneration}
\ \lor\
\text{rank loss}
\ \lor\
\text{orthogonal-branch exit}.
}
\]

---

## 12. Relation to M17-049 material tilt dynamics

M17-049 derives

\[
D_B\log|\Theta|
=(\sigma-\sigma_n)+\mathcal F_{crit}^{(2)}.
\]

M17-071 shows that the dynamically maintained nonzero tilt is useful only if it simultaneously creates the spatial compensation

\[
\boxed{
C^2+A D_\xi q<0.
}
\]

Therefore the remaining maximum survivor must satisfy **both**

1. a material tilt-maintenance law;
2. a spatial tangent-Riccati compensation law.

These are independent derivative directions and cannot be merged by a simple mean-exponent argument.

---

## 13. DSD analysis

The descriptor `tilt` has now split into

\[
\boxed{
\text{geometric tilt amplitude }\Theta
}
\]

and

\[
\boxed{
\text{effective Riccati compensation }\mathcal K_{tilt}.
}
\]

A nonzero first descriptor does not guarantee the desired behavior of the second.
Only

\[
\mathcal K_{tilt}<0
\]

actually turns the in-surface `q` evolution sub-Riccati.

This removes a major false escape in the Rank-2 branch tree.

---

## 14. DSD audit

### Audit A — assuming n itself remains tangent on a tilted sheet
Rejected. The exact tangent is `T=n+Theta xi`.

### Audit B — claiming any nonzero tilt avoids M17-048
Rejected. Tilt must satisfy the stronger cross-gradient payment.

### Audit C — using T-parameter finite distance as Euclidean distance without control
Rejected. A uniform tilt bound is stated explicitly when Euclidean completeness is invoked.

### Audit D — differentiating the critical cross-aligned pattern off the surface
Avoided. Only M17-047's already audited pointwise flatness identity is used, followed by differentiation of the scalar `q` along a vector tangent to the critical surface.

### Audit E — claiming K_tilt<0 is contradictory
Rejected. It is the surviving compensation class.

### Audit F — proof status
The tilted maximum escape is substantially narrowed but remains open through strong cross-gradient compensation and interface/degeneration exits.

---

## 15. Updated Rank-2 maximum frontier

\[
\boxed{
R_{max}^{tilted}
\Longrightarrow
R_{max}^{compensated:\,A D_\xi q<-C^2}
\ \lor\
T_{crit/rank/interface}
}
\]

for a complete recurrent maximum network after excluding persistent `K_tilt >= 0` tangent curves under the stated bounded-tilt hypothesis.

---

## 16. Next target — compensation persistence gate

The remaining nondegenerate maximum class requires

\[
\boxed{
\mathcal K_{tilt}
=C^2+A D_\xi q<0.
}
\]

The next high-value calculation is to derive the material/moving-critical evolution of `K_tilt` and determine whether its strict negativity can recur while `Theta`, `q`, and the stretch ratio remain bounded away from degeneracy.

This is the **Tilt Compensation Persistence Gate (TCPG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
