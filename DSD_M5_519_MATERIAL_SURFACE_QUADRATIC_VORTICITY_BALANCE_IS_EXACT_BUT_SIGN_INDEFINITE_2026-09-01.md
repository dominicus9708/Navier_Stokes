# DSD M5-519 — Material-surface quadratic vorticity balance is exact but sign-indefinite

Date: 2026-09-01

Status: **PACKET-LEVEL AMPLITUDE AUDIT / TO HANDLE THE M5-518 MARKER-MIGRATION BRANCH, TRACK THE QUADRATIC VORTICITY CONTENT `A2 = int_Sigma |W|^2 dA` OF A PERSISTENT MATERIAL SURFACE / THE SIMILARITY MATERIAL VELOCITY `B=U+y/2` GIVES THE EXACT AREA LAW `D_B dA = (1-n·Sigma n)dA`, AND COMBINING THIS WITH THE MAGNITUDE EQUATION YIELDS `A2' = int_Sigma [(2 sigma -1-sigma_n)rho^2 +2rho Delta rho -2rho^2|grad xi|^2]dA` / THIS IS A GENUINE SURFACE/PACKET EVOLUTION LAW, BUT THE FULL THREE-DIMENSIONAL LAPLACIAN CANNOT BE TURNED INTO A PURELY NEGATIVE SURFACE DIRICHLET TERM WITHOUT NORMAL-DERIVATIVE, CURVATURE, AND BOUNDARY TERMS; ALSO A MATERIAL-SURFACE NORMAL NEED NOT ALIGN WITH THE ANCHORED VORTICITY AXIS / THEREFORE `A2` IS NOT THE MISSING STRICT COCYCLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Target from M5-518

M5-518 separated a persistent material-flux lineage from any one point representative.

If the active marker migrates on the same material surface, the pointwise exact law

\[
D_B\log\rho=\lambda_{eff}-1
\]

need not give a bounded coboundary.

A natural lineage-level replacement is the quadratic material-surface vorticity content

\[
\boxed{
A_2(\theta)
:=
\int_{\Sigma(\theta)}|W(y,\theta)|^2dA.
}
\]

Here `Sigma(theta)` is transported by the similarity material velocity

\[
B=U+\frac12y.
\]

---

## 2. Evolution of a material area vector

Let

\[
N
=
\partial_\alpha X\times\partial_\beta X
\]

be the oriented area vector of a material parametrization `X(alpha,beta,theta)` satisfying

\[
\partial_\theta X=B(X,\theta).
\]

The standard area-vector transport identity is

\[
\boxed{
D_BN
=
\bigl[(\nabla\cdot B)I-(\nabla B)^T\bigr]N.
}
\]

Write

\[
N=n\,dA,
\qquad |n|=1.
\]

Taking the scalar area rate gives

\[
\boxed{
D_B(dA)
=
\bigl(\nabla\cdot B-n\cdot\nabla B\,n\bigr)dA.
}
\]

Only the symmetric part contributes to the quadratic normal contraction.

---

## 3. Similarity area law

Since

\[
B=U+\frac12y,
\qquad
\nabla\cdot U=0,
\]

we have

\[
\nabla\cdot B=\frac32.
\]

Also

\[
\nabla B
=\nabla U+\frac12I.
\]

Let

\[
\Sigma
=\frac12(\nabla U+\nabla U^T)
\]

and define the normal strain

\[
\boxed{
\sigma_n
:=
n\cdot\Sigma n.
}
\]

The antisymmetric part of `grad U` has zero quadratic contraction with `n`, so

\[
n\cdot\nabla B\,n
=\sigma_n+\frac12.
\]

Therefore

\[
\boxed{
D_B(dA)
=(1-\sigma_n)dA.
}
\]

The explicit `+1` is the surface-area counterpart of backward similarity dilation.

---

## 4. Magnitude-squared equation

From M5-486/M5-517,

\[
D_B\rho
=(\sigma-1)\rho
+\Delta\rho
-\rho|\nabla\xi|^2,
\]

where

\[
\sigma=\xi\cdot\Sigma\xi.
\]

Multiply by `2rho`:

\[
\boxed{
D_B(\rho^2)
=2(\sigma-1)\rho^2
+2\rho\Delta\rho
-2\rho^2|\nabla\xi|^2.
}
\]

This identity is exact wherever `rho>0`; the squared equation extends continuously through zeros.

---

## 5. Exact material-surface quadratic balance

Differentiate

\[
A_2(\theta)
=
\int_{\Sigma(\theta)}\rho^2dA.
\]

Using the material scalar derivative and the area law,

\[
\frac{dA_2}{d\theta}
=
\int_{\Sigma(\theta)}
\left[
D_B(\rho^2)
+(1-\sigma_n)\rho^2
\right]dA.
\]

Substitute Section 4:

\[
\boxed{
\frac{dA_2}{d\theta}
=
\int_{\Sigma(\theta)}
\Bigl[
(2\sigma-1-\sigma_n)\rho^2
+2\rho\Delta\rho
-2\rho^2|\nabla\xi|^2
\Bigr]dA.
}
\]

This is the exact packet-level quadratic vorticity law.

---

## 6. Comparison with the whole-space enstrophy identity

The global similarity enstrophy law is

\[
\frac12E'
+\frac14E
+P
=Q.
\]

There the full-space diffusion term can be integrated by parts without boundary:

\[
\int_{\mathbb R^3}W\cdot\Delta W
=-\int_{\mathbb R^3}|\nabla W|^2.
\]

For a two-dimensional material surface,

\[
\int_{\Sigma}\rho\Delta\rho\,dA
\]

contains the **ambient three-dimensional Laplacian**.

It is not equal to

\[
-\int_{\Sigma}|\nabla_\Sigma\rho|^2dA
\]

without extra terms.

This is the central sign obstruction.

---

## 7. Tangential/normal Laplacian decomposition

Locally near a smooth surface one may write schematically

\[
\Delta\rho
=
\Delta_\Sigma\rho
+\partial_{nn}\rho
+H_\Sigma\partial_n\rho,
\]

up to the chosen mean-curvature sign convention.

Thus

\[
\int_\Sigma\rho\Delta\rho\,dA
\]

splits into

1. a tangential surface-Laplacian contribution;
2. a normal second-derivative contribution;
3. a curvature-normal-gradient contribution.

If the material surface has boundary, tangential integration by parts also generates a boundary flux term.

Only the pure tangential interior piece has the favorable sign

\[
-\int_\Sigma|\nabla_\Sigma\rho|^2dA.
\]

The normal, curvature, and boundary pieces are sign-indefinite.

Therefore the ambient diffusion term cannot be treated as a surface dissipation without an additional geometric boundary/normal-control theorem.

---

## 8. Surface normal is not automatically the vorticity direction

The material flux is

\[
\Phi
=
\int_\Sigma W\cdot n\,dA.
\]

A coherent vorticity packet may be chosen initially with a cross-section whose normal is close to the packet direction.

However viscosity breaks exact vortex-line freezing.

A material surface normal is transported by the deformation gradient, while the vorticity direction obeys an additional projected diffusion term.

Hence even on the anchored branch

\[
D_B\xi=0,
\]

one does not automatically have

\[
\boxed{
n(\theta)=\xi
\quad\text{for all }\theta.
}
\]

Therefore

\[
\sigma_n
\]

and

\[
\sigma
\]

must remain distinct.

---

## 9. What would happen under the stronger aligned-surface hypothesis

For audit purposes only, suppose one had an additional theorem guaranteeing

\[
n=\xi
\]

throughout the relevant material surface.

Then

\[
\sigma_n=\sigma,
\]

and the balance simplifies to

\[
\boxed{
A_2'
=
\int_\Sigma
\left[
(\sigma-1)\rho^2
+2\rho\Delta\rho
-2\rho^2|\nabla\xi|^2
\right]dA.
}
\]

Even this stronger identity retains the sign-indefinite ambient normal-diffusion terms from `Delta rho`.

Thus normal alignment alone would not produce a monotone surface energy.

---

## 10. Anchored transverse cancellation does not remove the scalar obstruction

On the M5-516 anchored branch,

\[
\tau=-\mathcal D_\xi.
\]

This exactly cancels the **orthogonal vector** component of `Sigma W + Delta W`.

The surface quadratic law depends instead on

\[
\sigma,
\qquad
\sigma_n,
\qquad
\rho\Delta\rho,
\qquad
|\nabla\xi|^2.
\]

The orthogonal cancellation does not fix the signs of these scalar terms.

Therefore

\[
\boxed{
\tau=-\mathcal D_\xi
\not\Longrightarrow
A_2'\text{ has one sign}.
}
\]

---

## 11. Relation to material flux

The same surface has the exact scale-critical flux law

\[
\boxed{
\Phi'
=
\int_\Sigma\Delta W\cdot n\,dA.
}
\]

Thus the pair

\[
(\Phi,A_2)
\]

contains more information than either observable alone:

- `Phi` is signed and exactly scale critical, but its derivative is sign-indefinite;
- `A2` is positive and tracks packet strength, but its derivative has strain, normal-diffusion, curvature, and boundary ambiguities.

No linear combination with fixed universal coefficients has yet been shown to cancel all indefinite terms.

---

## 12. Packet-level verdict

The migrating-marker problem can be lifted to a genuine material-surface observable, but the result is

\[
\boxed{
\text{exact balance}
\ne
\text{one-sided balance}.
}
\]

Therefore `A2` is not the missing M5-485 strict cocycle.

The obstruction is now geometrically explicit:

\[
\boxed{
\text{ambient normal diffusion}
+
\text{surface-normal strain}
+
\text{boundary/curvature transport}.
}
\]

---

## 13. New typed branches

To convert the material-surface balance into a coercive law, one would need to control at least one of the following:

### S-normal

Uniform control/sign of

\[
\partial_{nn}\rho
+H_\Sigma\partial_n\rho.
\]

### S-boundary

Uniform control of the tangential boundary flux on the finite material patch.

### S-alignment

A persistent relation between material normal `n` and anchored vorticity direction `xi`.

### S-combination

A coupled observable using both `Phi` and `A2` whose indefinite normal terms cancel by an exact geometric identity.

None is presently proved.

---

## 14. Updated anchored frontier

The anchored hard core now has two exact but nonclosing scalar descriptions:

\[
\boxed{
D_B\log\rho
=\lambda_{eff}-1
}
\]

on a nondegenerate fixed material marker, and

\[
\boxed{
A_2'
=
\int_\Sigma
[(2\sigma-1-\sigma_n)\rho^2
+2\rho\Delta\rho
-2\rho^2|\nabla\xi|^2]dA
}
\]

on the persistent material surface.

The first is exact but may lose boundedness through marker migration.

The second survives marker migration but loses sign through ambient surface geometry.

This precisely identifies the remaining packet-level obstruction.

---

## 15. Highest-value next target

The next useful calculation is to track the **flux density per material area**

\[
f:=W\cdot n
\]

rather than `|W|^2`.

Because the integrated flux law is unusually simple, its pointwise material density equation may reveal which part of the ambient Laplacian is responsible for flux redistribution and whether the anchored condition `D_B xi=0` constrains the sign-changing normal/boundary terms.

If the density law is again an exact sign-indefinite transport equation, the remaining compact branch will be isolated as a genuinely viscous surface-redistribution cycle.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
