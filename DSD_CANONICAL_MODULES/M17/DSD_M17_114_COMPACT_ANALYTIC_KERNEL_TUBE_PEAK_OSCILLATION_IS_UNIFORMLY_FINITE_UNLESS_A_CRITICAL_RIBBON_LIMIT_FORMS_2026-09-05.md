# DSD M17-114 — Compact analytic kernel-tube peak oscillation is uniformly finite unless a critical-ribbon limit forms

Date: 2026-09-05
Canonical ID: **M17-114**

Status: **INTERNAL DIRECTOR-AREA PEAK OSCILLATION GATE / M17-113 IDENTIFIES THE POSITIVE PEAK MEASURE AS THE TOTAL VARIATION OF THE SIGNED DIVERGENCE MEASURE `div(H(g)J_xi)`. ON A COMPACT PURE-KERNEL FLOW BOX, ASSUME THE RESTRICTIONS OF `g=D_xi log rho` TO KERNEL-TUBE SEGMENTS FORM A COMPACT FAMILY IN THE SAME UNIFORM ANALYTIC TOPOLOGY USED IN THE HARD-HULL FINITE-JET AUDITS. THEN EITHER THE CLOSURE CONTAINS A FUNCTION IDENTICALLY ZERO ON A KERNEL SEGMENT, OR THE NUMBER OF `k`-DIRECTION ZEROS OF `g` (COUNTED WITH MULTIPLICITY) IS UNIFORMLY BOUNDED. CONSEQUENTLY THE DIRECTOR-AREA-WEIGHTED POSITIVE PEAK MEASURE IN SUCH A FLOW BOX IS BOUNDED BY A FINITE MULTIPLE OF THE TOTAL TUBE FLUX. THE EXCEPTION `g identically 0` IS NOT AN ARBITRARY OSCILLATORY LIMIT: FLATNESS FORCES `gamma_k=q` AND `D_k q=0`, WHILE `D_k xi=0`, SO THE KERNEL INTEGRAL CURVE HAS CONSTANT NONZERO CURVATURE IN A FIXED PLANE AND IS LOCALLY A CIRCULAR ARC. THUS UNBOUNDED PEAK TOTAL VARIATION CAN ONLY ACCUMULATE TOWARD A CRITICAL-RIBBON / CIRCULAR-KERNEL-FIBER BRANCH OR AN ANALYTIC-COMPACTNESS / RANK / FLOW-BOX EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Kernel-tube restriction of the peak function

On the pure-kernel Rank-2 branch,

\[
J_\xi=|J_\xi|k\neq0,
\qquad
D_k\xi=0.
\]

Let

\[
\boxed{g:=D_\xi\log\rho.}
\]

Choose a compact spatial flow box `U` in which

\[
|J_\xi|\ge c_J>0
\]

and the oriented kernel tubes admit regular coordinates

\[
(\lambda_1,\lambda_2,s),
\]

with `s` an oriented `k`-arclength coordinate on a bounded interval.

For each retained state/tube label, define the real-analytic one-variable restriction

\[
\boxed{
f_{\lambda,\theta}(s):=g(x(\lambda,s,\theta),\theta).}
\]

---

## 2. Analytic compactness hypothesis

Use the same kind of compact analytic hard-hull assumption employed in the finite-jet audits: the family of restrictions to a slightly larger common tube interval is precompact in a topology strong enough to preserve real analyticity and all derivatives on the compact subinterval.

Equivalently for the present gate, it is sufficient to assume a common analytic neighborhood with uniform analytic bounds and compact closure.

This hypothesis is stronger than a finite Sobolev derivative bound and is stated explicitly because zero-count compactness is an analytic statement.

---

## 3. Uniform zero-count dichotomy

Suppose no limit function in the compact closure is identically zero on a connected kernel segment.

If the number of zeros of `f_{lambda,theta}` on the compact segment, counted with multiplicity, were unbounded, choose a sequence with zero count tending to infinity.

Compactness gives a convergent analytic subsequence

\[
f_n\to f_\infty.
\]

Because the interval is compact, the growing zero sets have an accumulation point after passing to a further subsequence.
Analytic convergence transfers the corresponding finite-order zero constraints to the limit.
The limit therefore has a nonisolated zero set, so by analytic unique continuation in one variable,

\[
\boxed{f_\infty\equiv0}
\]

on the connected segment.

This contradicts the retained alternative.

Hence there exists

\[
\boxed{N_k<\infty}
\]

such that every retained kernel segment has at most `N_k` zeros of `g`, counted with multiplicity.

Thus

\[
\boxed{
\text{uniform finite zero count}
\quad\lor\quad
\text{critical-ribbon analytic limit}.
}
\]

---

## 4. Bound on the positive director-area peak measure

M17-113 gives in a transverse state

\[
d\mu_{peak}^J
=\delta(g)|J_\xi\cdot\nabla g|\,dV.
\]

In tube coordinates this is simply `dPhi_J` counted once per transverse zero.

Therefore, away from the finite degenerate event times and with multiplicity understood by the limiting analytic chart,

\[
\boxed{
\mu_{peak}^J(U)
\le
N_k\,\Phi_J(\Lambda_U),
}
\]

where

\[
\Phi_J(\Lambda_U)
:=\int_{\Lambda_U}d\Phi_J
\]

is the total director-area flux of the tube bundle crossing the flow box.

If the compact hard hull also gives

\[
0<N_{R2}\le N_{max}
\]

on the retained positive-margin population, then

\[
\boxed{
\mathscr N_U
\le
N_{max}N_k\Phi_J(\Lambda_U).
}
\]

This is a genuine total-variation upper bound on a compact flow box, conditional on avoiding the critical-ribbon limit.

---

## 5. The exceptional analytic limit

The excluded alternative is

\[
\boxed{g\equiv0}
\]

on a connected kernel segment.

Then every point of that kernel segment is a line-critical point in the vortex direction.
In particular,

\[
D_kg=0
\]

throughout the segment.

M17-099/M17-110 flatness gives

\[
\boxed{\gamma_k=q}
\]

and

\[
\boxed{D_kq=0.}
\]

Thus the vortex-curvature coefficient `q` is constant along the kernel segment.

---

## 6. Geometry of the critical ribbon

Because

\[
D_k\xi=0,
\]

the director `xi` is constant along the kernel integral curve.
Hence the curve lies in a fixed affine plane orthogonal to that constant director.

The frame equations are

\[
\boxed{
D_kk=q\,n,
\qquad
D_kn=-q\,k,
}
\]

with

\[
D_kq=0.
\]

Full Rank 2 at a peak requires

\[
q\neq0,
\]

because `a=rk` and `q=0` would make `a` and `b=pk` linearly dependent.

Therefore the kernel curve has constant nonzero curvature and zero torsion in its fixed plane.

Hence

\[
\boxed{
\text{a critical-ribbon kernel segment is locally a circular arc of radius }|q|^{-1}.
}
\]

If the ribbon condition extends around a complete connected kernel fiber without an exit, the fiber is a closed circle up to its natural periodic parametrization.

---

## 7. Meaning for peak oscillation

The positive total variation of the peak measure cannot grow without bound inside a compact analytic flow box while staying uniformly separated from the ribbon class.

Thus any attempted infinite-fold/oscillation mechanism must enter one of

\[
\boxed{
\begin{aligned}
&\text{critical-ribbon / circular-kernel accumulation},\\
&\text{loss of analytic compactness},\\
&J_\xi\to0\text{ / flow-box exit},\\
&\text{spatial endpoint/domain exit}.
\end{aligned}
}
\]

The first is a new explicit exceptional geometry rather than an unstructured infinite-zero limit.

---

## 8. What the finite zero-count bound does not prove

Even if

\[
\mu_{peak}^J(U)
\le N_k\Phi_J,
\]

folds may repeatedly create and destroy peaks while keeping the instantaneous number below `N_k`.

Therefore this bound does not by itself control the **temporal event frequency** or sign the margin-weighted fold hysteresis of M17-109.

Likewise it does not bound the higher-jet recharge `R_R2` by less than the required `3/2` damping.

It is a spatial total-variation bound, not yet a spacetime coercive estimate.

---

## 9. DSD analysis

M17-113 exposed total variation as the missing positive quantity.
The present gate shows that analytic compactness controls that total variation unless the descriptor collapses onto a higher-symmetry ribbon state.

The new hierarchy is

\[
\boxed{
\text{finite signed degree}
\to
\text{finite positive zero count}
\lor
\text{critical ribbon}.
}
\]

Thus the oscillation firewall is reduced to one explicit geometry.

---

## 10. DSD audit

### Audit A — deriving a zero-count bound from finitely many derivative bounds
Rejected. The gate explicitly requires analytic compactness/common analytic control.

### Audit B — excluding the zero-function limit without analysis
Rejected. It is retained as the critical-ribbon branch.

### Audit C — identifying finite zero count with finite event count in time
Rejected.

### Audit D — treating local circularity as a global closed-loop theorem without persistence
Rejected. A local ribbon gives a circular arc; a full circle requires extension of the ribbon condition along the whole connected kernel fiber.

### Audit E — proof status
Peak total variation is spatially controlled away from a sharply classified critical-ribbon branch, but recurrent temporal recharge remains open.

---

## 11. Updated DAPOG frontier

On a compact analytic pure-kernel flow box,

\[
\boxed{
R_{2,peak}
\Longrightarrow
R_{finite-k-zero}^{N_k}
\ \lor\
R_{ribbon}^{g\equiv0,\ circular\ k-fiber}
\ \lor\
T_{compact/rank/spatial}.
}
\]

The next high-value calculation is the material persistence law of the critical ribbon. Since every point on the ribbon satisfies `g=0`, persistence requires `D_Bg=D_xi(sigma+kappa)=0` along the entire kernel arc. Combining this with `q=gamma_k=const along k` may reduce the ribbon to a finite connection/strain subsystem.

This is the **Critical Ribbon Persistence Gate (CRPG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
