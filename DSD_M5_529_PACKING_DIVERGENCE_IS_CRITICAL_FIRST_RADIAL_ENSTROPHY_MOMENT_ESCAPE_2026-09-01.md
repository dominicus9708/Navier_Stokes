# DSD M5-529 — Nonsummable Dirichlet packing is a critical first-radial enstrophy-moment escape

Date: 2026-09-01

Status: **WEIGHTED-MOMENT REFORMULATION / THE M5-527 DIVERGENCE OF THE `ell^(3/2)` SCALE-CRITICAL DIRICHLET PACKING FORCES DIVERGENCE OF THE FIRST RADIAL DIRICHLET MOMENT `int |y||grad U|^2` / THE WEIGHT `|y|` IS AN `A2` MUCKENHOUPT WEIGHT IN R3, SO WEIGHTED CALDERON--ZYGMUND THEORY TRANSFERS THIS MOMENT TO THE VORTICITY AS `int |y||W|^2` / THE LOCAL SIMILARITY ENSTROPHY EQUATION THEN GIVES AN EXACT CRITICAL FIRST-MOMENT LEDGER IN WHICH ALL LINEAR SIMILARITY SCALING TERMS CANCEL / THE SURVIVING NONTRIVIAL ANCIENT CELL MUST THEREFORE CARRY AN UNBOUNDED FIRST RADIAL ENSTROPHY MOMENT TOWARD BACKWARD INFINITY / THE LEDGER IS NOT MONOTONE BECAUSE WEIGHTED STRETCHING, WEIGHTED PALINSTROPHY, RADIAL VELOCITY TRANSPORT, AND DIFFUSIVE MOMENT SPREAD ALL REMAIN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. From `ell^(3/2)` packing to the first Dirichlet moment

Use the M5-526 dyadic shells

\[
R_k=2^kR_0,
\qquad
b_k=R_kE_k,
\]

with

\[
E_k
=\int_{A_k^*}|\nabla U|^2dy.
\]

For every nonnegative sequence,

\[
\boxed{
\sum_kb_k^{3/2}
\le
\left(\sum_kb_k\right)^{3/2}.
}
\]

Indeed the right side contains all positive mixed terms in addition to the pure powers.

Therefore M5-527's conclusion

\[
\sum_kb_k(\theta)^{3/2}
\to\infty
\quad(\theta\to-\infty)
\]

implies

\[
\boxed{
\sum_kb_k(\theta)
\to\infty.
}
\]

Because `|y|~R_k` on each dyadic shell and the enlarged shells have bounded overlap,

\[
\boxed{
\sum_kb_k
\asymp
\int_{|y|>R_0}
|y|\,|\nabla U(y)|^2dy
}
\]

up to fixed geometric constants and an irrelevant bounded interior contribution.

Hence

\[
\boxed{
\int_{\mathbb R^3}|y|\,|\nabla U(y,\theta)|^2dy
\to\infty
\quad(\theta\to-\infty).
}
\]

---

## 2. Weighted Calderon--Zygmund transfer to vorticity

For a divergence-free whole-space velocity with fixed Galilean mode,

\[
\nabla U
=\mathcal R W
\]

through a finite family of Riesz transforms.

The power weight

\[
\boxed{w(y)=|y|}
\]

belongs to the Muckenhoupt class `A2(R3)` because a power weight `|y|^alpha` lies in `A2(R3)` for

\[
-3<\alpha<3.
\]

Weighted Calderon--Zygmund theory therefore gives

\[
\boxed{
\int|y|\,|\nabla U|^2dy
\le
C_{A2}
\int|y|\,|W|^2dy.
}
\]

The reverse elementary bound

\[
|W|=|\nabla\times U|
\le C|\nabla U|
\]

gives

\[
\boxed{
\int|y|\,|W|^2dy
\le
C
\int|y|\,|\nabla U|^2dy.
}
\]

Thus the two critical first radial moments are equivalent whenever finite, and by truncation the divergence implication remains valid:

\[
\boxed{
\mathcal M_1(\theta)
:=
\int_{\mathbb R^3}|y|\,|W(y,\theta)|^2dy
\to\infty
\quad(\theta\to-\infty).
}
\]

This is a standard harmonic-analysis input, not a new Navier--Stokes theorem.

---

## 3. Local similarity enstrophy conservation law

Let

\[
h:=|W|^2,
\qquad
p:=|\nabla W|^2,
\qquad
q:=W\cdot\Sigma W,
\]

and

\[
B:=U+\frac12y.
\]

From the similarity vorticity equation,

\[
\partial_\theta W
+W
+\frac12y\cdot\nabla W
+U\cdot\nabla W
=(W\cdot\nabla)U+\Delta W,
\]

one obtains

\[
\boxed{
\partial_\theta h
+\frac12h
+\nabla\cdot(Bh-\nabla h)
=2q-2p.
}
\]

Integrating over all space recovers M5-486:

\[
\frac12E'
+\frac14E
+P
=Q.
\]

---

## 4. Multiply by the critical radial weight

Formally assume first that

\[
\mathcal M_1(\theta)
=\int r hdy<\infty,
\qquad r=|y|,
\]

with sufficient decay to integrate by parts.

Multiply the local balance by `r` and integrate:

\[
\mathcal M_1'
+\frac12\mathcal M_1
-\int(Bh-\nabla h)\cdot e_r\,dy
=2\int r(q-p)dy.
\]

Since

\[
B\cdot e_r
=U_r+\frac r2,
\]

the explicit radial dilation contributes

\[
\frac12\mathcal M_1,
\]

which cancels the explicit similarity damping term exactly.

Also

\[
\int_{\mathbb R^3}\partial_rh\,dy
=-2\int_{\mathbb R^3}\frac{h}{r}dy.
\]

Therefore the exact first-moment identity is

\[
\boxed{
\frac d{d\theta}\mathcal M_1
=
2\int r(q-p)dy
+
\int U_rh\,dy
+
2\int\frac{h}{r}dy.
}
\]

Equivalently,

\[
\boxed{
\mathcal M_1'
+2\int r|\nabla W|^2dy
=
2\int r\,W\cdot\Sigma W\,dy
+
\int U_r|W|^2dy
+
2\int\frac{|W|^2}{r}dy.
}
\]

---

## 5. Why the weight `r` is exactly critical

Under the pure linear similarity dilation

\[
\partial_\theta W+W+\frac12y\cdot\nabla W=0,
\]

a packet moves to radius

\[
r(\theta)\sim e^{\theta/2}
\]

while its enstrophy decays like

\[
e^{-\theta/2}.
\]

Their product is invariant.

This is exactly why the terms

\[
\frac12\mathcal M_1
\]

cancel in Section 4.

Thus `M1` is the natural first log-scale/critical spatial moment for this similarity problem.

---

## 6. Truncated rigorous version

Because M5-529 eventually studies the branch where `M1` may be infinite, use smooth truncated radial weights

\[
w_L(r)
\]

such that

\[
w_L(r)=r
\quad(r\le L),
\]

\[
w_L(r)=\text{const.}
\quad(r\ge2L),
\]

and

\[
|w_L'|\le1,
\qquad
|w_L''|\le C/L.
\]

Testing the local enstrophy equation against `w_L` yields an exact finite identity with

\[
\nabla w_L
\]

and

\[
\Delta w_L
\]

terms.

On intervals where `M1` is finite, monotone/dominated convergence recovers the formal formula above as `L->infinity`.

When `M1` is infinite, the truncated quantities

\[
\mathcal M_{1,L}
:=
\int w_L|W|^2
\]

provide the correct audit family.

No integration by parts at an uncontrolled infinity is assumed.

---

## 7. Uniformly bounded lower-order terms

On the globally smooth compact branch,

\[
\|U\|_\infty
\le U_*<\infty,
\qquad
\|\Sigma\|_\infty
\le S_*<\infty,
\]

\[
E\le Z_*,
\qquad
P\le P_*.
\]

The radial transport term obeys

\[
\left|
\int U_r|W|^2dy
\right|
\le
U_*Z_*.
\]

Hardy's inequality gives

\[
\int\frac{|W|^2}{r^2}dy
\le
4P,
\]

and hence Cauchy--Schwarz yields

\[
\boxed{
\int\frac{|W|^2}{r}dy
\le
2E^{1/2}P^{1/2}
\le
2Z_*^{1/2}P_*^{1/2}.
}
\]

The weighted production satisfies

\[
\left|
\int r\,W\cdot\Sigma Wdy
\right|
\le
S_*\mathcal M_1.
\]

Thus, after dropping the favorable weighted-palinstrophy term,

\[
\boxed{
\mathcal M_1'
\le
2S_*\mathcal M_1+C_*.
}
\]

This guarantees that finite first moment cannot become infinite in finite forward similarity time.

It does not prevent unbounded growth toward backward infinity.

---

## 8. Why the weighted ledger does not yet close

The exact identity contains

\[
-2\int r|\nabla W|^2dy
\]

but also sign-indefinite weighted stretching

\[
2\int r\,W\cdot\Sigma Wdy.
\]

There is no current estimate showing that the weighted palinstrophy dominates the weighted production on the recurrent hard core.

Moreover the first moment is an extended, noncompact tail observable; it is not bounded on the M5-485 invariant hull.

Therefore invariant averaging cannot be applied to `M1` as though it were the missing bounded cocycle.

The correct conclusion is

\[
\boxed{
\text{critical packing escape}
\to
\text{critical radial enstrophy-moment escape},
}
\]

not a contradiction.

---

## 9. New spatial interpretation of the M5-527 branch

The unweighted enstrophy remains uniformly tight:

\[
\sup_\theta
\int_{|y|>R}|W|^2dy
\to0.
\]

Yet

\[
\mathcal M_1(\theta)
\to\infty
\quad(\theta\to-\infty).
\]

Therefore less and less unweighted vorticity mass is allowed to sit farther and farther out while its radius-weighted first moment grows without bound.

This is analogous to a probability family that is tight but whose first moment is not uniformly integrable.

Thus the precise concentration-compactness defect is

\[
\boxed{
\text{tightness without uniform first-moment integrability}.
}
\]

---

## 10. Relation to terminal Dirichlet tail

M5-481--483 isolated a critical terminal tail measured at log scales by

\[
R\int_{A_R}|\nabla V(0)|^2.
\]

M5-529 shows that the interior nonsummable packing can equivalently be regarded as failure of the first radial critical moment.

This is a useful common language, but M5-528 remains in force: the interior backward-time first-moment escape is not automatically the same object as the terminal forward-time dilation tail.

A genuine space-time transport bridge is still required.

---

## 11. Highest-value next target

The local conservation law in Section 3 suggests the correct bridge.

Let the observation radius follow the similarity dilation characteristic

\[
\boxed{
R'(\theta)=\frac12R(\theta).
}
\]

For the exterior enstrophy

\[
I_R(\theta)
=
\int_{|y|>R(\theta)}|W|^2dy,
\]

the moving-boundary term should cancel the explicit `y/2` flux.

Multiplying by `R(theta)` should also cancel the remaining linear `1/2` damping.

This should give an exact scale-critical moving-tail balance containing only

1. weighted/local vortex stretching;
2. palinstrophy;
3. physical-velocity transport across the moving sphere;
4. diffusive radial flux.

That identity can track how the first-moment defect crosses log radius in time without the invalid shell/time identification excluded in M5-528.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
