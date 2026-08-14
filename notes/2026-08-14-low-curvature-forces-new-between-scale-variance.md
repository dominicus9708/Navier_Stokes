# Low curvature forces a fixed fraction of genuinely new Gaussian between-scale variance

Date: 2026-08-14

Status: **EXACT PROPORTIONAL-COVARIANCE OU/HERMITE FORMULA + STRICT INHERITED-RESIDUAL CONTRACTION ON THE LOW-CURVATURE BRANCH**.

The current frontier asks for a contraction/packing theorem inside the non-affine mesoscopic window.  The Gaussian law of total variance already separates inherited residual from genuinely new between-scale residual, but previously no pointwise lower bound on the new fraction was available.

For proportional parent/child Gaussian covariances there is an exact Ornstein--Uhlenbeck/Hermite representation.  It shows that low Gaussian curvature forces a fixed fraction of the parent residual to be genuinely new between scales.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Parent Gaussian and Hermite expansion

Let `Sigma>0` and define

\[
B_\Sigma[g](a)
=P_\Sigma|g|^2(a)-|P_\Sigma g(a)|^2.
\]

Whiten the parent Gaussian:

\[
G(z)=g(a+\Sigma^{1/2}z),
\qquad
z\sim\gamma=N(0,I).
\]

Write the standard Gaussian Hermite expansion

\[
G=G_0+\sum_{n\ge1}G_n,
\]

and set

\[
e_n=\|G_n\|_{L^2(\gamma)}^2.
\]

Then exactly

\[
\boxed{
B_\Sigma[g](a)
=\sum_{n\ge1}e_n.
}
\]

The whitened derivative energy is

\[
K_\Sigma[g](a)
:=
\int\gamma_\Sigma
\left|
(\nabla g)\Sigma^{1/2}
\right|_F^2.
\]

The Ornstein--Uhlenbeck spectral identity gives

\[
\boxed{
K_\Sigma[g](a)
=\sum_{n\ge1}n e_n.
}
\]

Define the residual-weighted mean Hermite degree

\[
\boxed{
\mu_\Sigma
:=\frac{K_\Sigma}{B_\Sigma}
=
\frac{\sum n e_n}{\sum e_n}
}
\]

when `B_Sigma>0`.

Ordinary Gaussian Poincare is simply

\[
\mu_\Sigma\ge1.
\]

---

## 2. Proportional parent/child split

Fix

\[
0<c<1.
\]

Split the parent covariance as

\[
\boxed{
\Sigma
=c\Sigma+(1-c)\Sigma.
}
\]

The Gaussian law of total variance gives

\[
\boxed{
B_\Sigma[g]
=P_{(1-c)\Sigma}B_{c\Sigma}[g]
+B_{(1-c)\Sigma}[P_{c\Sigma}g].
}
\]

The first term is inherited child residual.  Define the genuinely new between-scale increment

\[
\boxed{
\Delta_cB_\Sigma[g]
:=B_{(1-c)\Sigma}[P_{c\Sigma}g].
}
\]

---

## 3. Exact OU formula for the new increment

Let

\[
\rho=\sqrt{1-c}.
\]

For `y=Sigma^(1/2) sqrt(1-c) z`,

\[
P_{c\Sigma}g(a+y)
\]

is exactly the Ornstein--Uhlenbeck conditional expectation of the parent field `G` with correlation `rho`:

\[
P_{c\Sigma}g
\quad\leftrightarrow\quad
T_\rho G.
\]

The OU semigroup acts diagonally on Hermite chaoses:

\[
T_\rho G_n=\rho^nG_n.
\]

Therefore

\[
\boxed{
\Delta_cB_\Sigma[g](a)
=
\sum_{n\ge1}(1-c)^n e_n.
}
\]

Correspondingly,

\[
\boxed{
P_{(1-c)\Sigma}B_{c\Sigma}[g](a)
=
\sum_{n\ge1}
\left[1-(1-c)^n\right]e_n.
}
\]

These two expressions add exactly to the parent variance.

---

## 4. Low curvature gives a fixed new-variance fraction

Normalize

\[
p_n=\frac{e_n}{B_\Sigma},
\qquad
\sum p_n=1.
\]

Then

\[
\frac{\Delta_cB_\Sigma}{B_\Sigma}
=
\sum_{n\ge1}p_n(1-c)^n.
\]

Because

\[
x\mapsto(1-c)^x
\]

is convex on the real line, Jensen gives

\[
\sum p_n(1-c)^n
\ge
(1-c)^{\sum n p_n}
=(1-c)^{\mu_\Sigma}.
\]

Hence the exact lower bound

\[
\boxed{
\Delta_cB_\Sigma[g](a)
\ge
(1-c)^{\mu_\Sigma}
B_\Sigma[g](a).
}
\]

If the parent lies in a low-curvature regime

\[
\boxed{
K_\Sigma[g]
\le K B_\Sigma[g],
}
\]

then

\[
\mu_\Sigma\le K
\]

and therefore

\[
\boxed{
\Delta_cB_\Sigma[g](a)
\ge
(1-c)^K B_\Sigma[g](a).
}
\]

This is a **fixed positive new-residual fraction** depending only on the fixed scale ratio and the curvature ratio bound.

---

## 5. Strict contraction of the inherited residual

Using total variance,

\[
P_{(1-c)\Sigma}B_{c\Sigma}[g]
=B_\Sigma[g]-\Delta_cB_\Sigma[g].
\]

Thus on the low-curvature branch

\[
\boxed{
P_{(1-c)\Sigma}B_{c\Sigma}[g](a)
\le
\left[1-(1-c)^K\right]
B_\Sigma[g](a).
}
\]

Define

\[
\eta_{c,K}:=(1-c)^K>0.
\]

Then

\[
\boxed{
\text{inherited child residual}
\le(1-\eta_{c,K})
\times
\text{parent residual}.
}
\]

This is the pointwise contraction statement that was missing from the earlier total-variance audit.

---

## 6. Apply to the Navier--Stokes affine residual

Take

\[
g=\nabla U.
\]

Then

\[
B_\Sigma[g]
=\mathcal B_\Sigma
\]

is the four-channel Gaussian residual variance.

Moreover

\[
K_\Sigma[g]
=
\int\gamma_\Sigma
\left|
\nabla^2U\,\Sigma^{1/2}
\right|_F^2.
\]

For an isotropic covariance `Sigma=R^2I`,

\[
K_\Sigma=R^2D_g.
\]

Thus the low-curvature condition is precisely

\[
\boxed{
R^2D_g\le K\mathcal B_R.
}
\]

On that branch, every fixed-ratio descent creates at least

\[
\boxed{
\eta_{c,K}\mathcal B_R
}
\]

of genuinely new between-scale residual.

If this fails because `R^2 D_g/B` is large, the event is already typed as the complementary high-curvature branch.

Therefore one obtains a clean local dichotomy:

\[
\boxed{
\text{high curvature}
\quad\text{or}\quad
\text{fixed-fraction new scale variance}.
}
\]

---

## 7. Relation to the earlier fixed-ratio curvature descent

The earlier residual square-function argument gave

\[
\text{fixed-ratio child curvature witness}
\quad\text{or endpoint concentration}.
\]

The present result is complementary.  It acts directly on the parent residual state:

- if curvature relative to residual is high, keep the derivative witness;
- if curvature relative to residual is bounded, the law of total variance forces a strict new-information fraction at the next proportional scale split.

Thus low curvature is no longer a scale-neutral escape.

---

## 8. Why this does not yet finish global packing

The exact global identity still gives

\[
\sum_k\int_{R^3}\Delta B_k(x)dx
\le
\|g\|_2^2
\]

for a nested covariance ladder at a fixed time.

The new result supplies a pointwise lower bound

\[
\Delta B_k(a_k)
\ge
\eta B_k(a_k)
\]

at an active center on the low-curvature branch.

To convert this into a global contradiction one still needs one of:

1. a lower bound on the spatial occupancy/volume of active centers;
2. a moving-center Carleson/precursor-capacity estimate;
3. a spacetime packing lemma compatible with successive first-hitting windows.

If the active set is thick, integrating the pointwise new-increment bound immediately charges the globally telescoping scale ledger.  If it is sparse, the route should enter the pre-existing geometric sparseness/regularity gate.

Thus the remaining issue is now **spatial/spacetime occupancy of the new-increment witnesses**, not lack of a scale contraction mechanism.

---

## 9. Important audit: high Hermite degree behaves oppositely

The exact formula also explains why an unrestricted degree-spread-to-new-variance theorem would be false.

For fixed `c`, a pure high Hermite degree `n` has

\[
\frac{\Delta_cB}{B}=(1-c)^n\to0.
\]

Thus high-degree residual can be almost entirely inherited into the finer scale.  But precisely in that regime

\[
\mu_\Sigma\gg1,
\]

so the curvature ratio is high and the event belongs to the derivative branch.

This closes the logical dichotomy cleanly:

\[
\boxed{
\text{low Hermite degree}
\Rightarrow
\text{new scale variance},
\qquad
\text{high Hermite degree}
\Rightarrow
\text{high curvature}.
}
\]

Status: **LOCAL SCALE-CONTRACTION DICHOTOMY CLOSED / REMAINING FRONTIER = OCCUPANCY OR SPACETIME PACKING OF ACTIVE NEW-INCREMENT WITNESSES**.
