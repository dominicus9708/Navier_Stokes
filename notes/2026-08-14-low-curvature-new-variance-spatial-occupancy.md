# Spatial occupancy of the low-curvature new Gaussian between-scale variance

Date: 2026-08-14

Status: **DERIVED FIXED GAUSSIAN/LEBESGUE OCCUPANCY OF CHILD AFFINE-MEAN VARIATION ON THE LOW-CURVATURE BRANCH**.

The previous note proved that for a proportional Gaussian split

\[
\Sigma=c\Sigma+(1-c)\Sigma,
\qquad 0<c<1,
\]

a parent residual with bounded mean Hermite degree creates a fixed fraction of genuinely new between-scale variance.

This note shows that the new variance cannot be concentrated on a vanishing set inside the parent Gaussian.  Ornstein--Uhlenbeck hypercontractivity and Paley--Zygmund give a fixed-probability set of child centers on which the child affine mean differs from the parent affine mean by order `sqrt(B)`.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Parent residual and OU representation

Let

\[
G(z)=g(a+\Sigma^{1/2}z),
\qquad z\sim\gamma=N(0,I),
\]

and subtract the parent Gaussian mean

\[
F=G-G_0,
\qquad
G_0=P_\Sigma g(a).
\]

Then

\[
\|F\|_{L^2(\gamma)}^2
=B_\Sigma[g](a)=:B.
\]

Choose the proportional split and set

\[
\rho=\sqrt{1-c}.
\]

The outer-position field of child affine means satisfies

\[
\boxed{
P_{c\Sigma}g\!\left(a+\sqrt{1-c}\,\Sigma^{1/2}z\right)
-P_\Sigma g(a)
=T_\rho F(z),
}
\]

where `T_rho` is the Ornstein--Uhlenbeck semigroup.

The genuinely new between-scale variance is exactly

\[
\boxed{
\Delta_cB
=\|T_\rho F\|_2^2.
}
\]

If the parent mean Hermite degree obeys

\[
\mu_\Sigma\le K,
\]

the previous Jensen bound gives

\[
\boxed{
\Delta_cB
\ge\rho^{2K}B.
}
\]

---

## 2. Choose a hypercontractive fixed scale ratio

For the standard OU semigroup, the scalar Gaussian hypercontractive estimate

\[
\|T_\rho f\|_{L^4(\gamma)}
\le
\|f\|_{L^2(\gamma)}
\]

holds whenever

\[
\rho\le\frac1{\sqrt3}.
\]

Equivalently it is enough to choose

\[
\boxed{c\ge\frac23.}
\]

Fix such a proportional split once and for all.

Let `d_g` be the finite number of scalar components of `g`.  For `g=grad U` in three dimensions,

\[
d_g=9.
\]

Since

\[
\sum_{j=1}^{d_g}
\|T_\rho F_j\|_2^2
=\Delta_cB,
\]

there exists a scalar component `j_*` such that

\[
\boxed{
\|T_\rho F_{j_*}\|_2^2
\ge
\frac{\Delta_cB}{d_g}
\ge
\frac{\rho^{2K}}{d_g}B.
}
\]

---

## 3. Paley--Zygmund occupancy

Let

\[
Y=|T_\rho F_{j_*}|^2.
\]

Then

\[
\mathbb EY
\ge
\frac{\rho^{2K}}{d_g}B.
\]

By hypercontractivity,

\[
\mathbb EY^2
=\|T_\rho F_{j_*}\|_4^4
\le
\|F_{j_*}\|_2^4
\le
B^2.
\]

Paley--Zygmund with threshold `1/2` gives

\[
\gamma\left(
Y\ge\frac12\mathbb EY
\right)
\ge
\frac14
\frac{(\mathbb EY)^2}{\mathbb EY^2}.
\]

Therefore

\[
\boxed{
\gamma(E_z)
\ge
\delta_{K,c}
:=
\frac{1}{4d_g^2}\rho^{4K}
>0,
}
\]

where on `E_z`

\[
\boxed{
|T_\rho F(z)|^2
\ge
\frac{\rho^{2K}}{2d_g}B.
}
\]

Thus the new between-scale variation occupies a fixed Gaussian probability, depending only on the curvature ratio bound and the fixed scale ratio.

---

## 4. Return to physical child centers

Set

\[
y=\sqrt{1-c}\,\Sigma^{1/2}z.
\]

The corresponding outer Gaussian has covariance

\[
(1-c)\Sigma.
\]

Let `E_y` be the image of `E_z`.  Then

\[
\boxed{
\gamma_{(1-c)\Sigma}(E_y)
\ge
\delta_{K,c}.
}
\]

For every `y in E_y`,

\[
\boxed{
\left|
P_{c\Sigma}g(a+y)-P_\Sigma g(a)
\right|^2
\ge
\frac{\rho^{2K}}{2d_g}B.
}
\]

The maximum density of the outer Gaussian is

\[
\|\gamma_{(1-c)\Sigma}\|_\infty
=(2\pi)^{-3/2}
(1-c)^{-3/2}
(\det\Sigma)^{-1/2}.
\]

Writing

\[
R=(\det\Sigma)^{1/6},
\]

we therefore obtain a Euclidean volume lower bound

\[
\boxed{
|E_y|
\ge
c_{K,c}R^3.
}
\]

Hence the low-curvature new increment has genuine three-dimensional occupancy at the parent scale.

---

## 5. Interpretation for the Navier--Stokes affine state

Take

\[
g=\nabla U.
\]

Then

\[
L_\Sigma(a)=P_\Sigma(\nabla U)(a)
\]

is the parent Gaussian affine mean gradient, while

\[
L_{c\Sigma}(a+y)=P_{c\Sigma}(\nabla U)(a+y)
\]

is the child affine mean gradient at the child center.

On the occupied set,

\[
\boxed{
|L_{c\Sigma}(a+y)-L_\Sigma(a)|
\gtrsim_{K,c}
\sqrt{\mathcal B_\Sigma(a)}.
}
\]

Thus low-curvature residual cannot descend to the child scale merely as hidden inherited noise.  A fixed fraction of a parent-scale volume must contain child affine states that are macroscopically distinguishable at the natural residual amplitude.

This is precisely the spatial realization of the new-information term in the Gaussian total-variance law.

---

## 6. Thick/sparse interpretation

For a parent active center there are now two possibilities.

### Occupied child-state branch

The set of distinguishable child affine means has

\[
|E_y|\gtrsim R^3.
\]

If many parent active centers occur with bounded overlap, a Vitali/disjoint-subfamily selection allows their occupied child volumes to be charged to an ordinary spatial or spacetime ledger.

### Geometrically sparse parent branch

If a large family of active parents cannot be selected with bounded overlap, then their centers cluster into a smaller precursor region.  The appropriate next descriptor is not another scale residual but precursor capacity / geometric sparseness of the parent family.

Thus the occupancy issue is reduced to a standard covering alternative rather than an arbitrary pointwise concentration problem.

---

## 7. Relation to global Gaussian scale packing

At fixed time the exact global increment identity is

\[
\boxed{
\int_{\mathbb R^3}\Delta_cB_\Sigma(a)\,da
=
\|P_{c\Sigma}g\|_2^2
-
\|P_\Sigma g\|_2^2.
}
\]

For the geometric ladder

\[
\Sigma_{k+1}=c\Sigma_k,
\]

these global increments telescope:

\[
\boxed{
\sum_k
\int\Delta_cB_{\Sigma_k}(a)da
\le
\|g\|_2^2.
}
\]

The present occupancy lemma explains the local geometry behind this global packing: every low-curvature active parent carries a fixed-volume family of distinguishable child affine states.

The remaining cross-checkpoint task is to select these parent/child cells with controlled overlap in spacetime.

---

## 8. Current frontier

The old non-affine low-curvature escape route required three unresolved ingredients:

1. a fixed-ratio scale transition;
2. genuinely new residual rather than inherited residual;
3. nonvanishing spatial support of the new state.

These are now supplied by:

\[
\boxed{
\text{fixed-ratio Gaussian split}
}
\]

\[
\boxed{
\Delta_cB\ge\rho^{2K}B
}
\]

and

\[
\boxed{
|E_y|\ge c_{K,c}R^3.
}
\]

Therefore the low-curvature mesoscopic branch has been reduced to a **covering/overlap problem across moving first-hitting windows**.

A successful bounded-overlap selection would turn the exact scale telescoping identity into a direct packing contradiction; failure of bounded overlap would itself define a concentrated precursor-capacity branch.

Status: **LOCAL SPATIAL OCCUPANCY OF NEW SCALE INFORMATION CLOSED / REMAINING FRONTIER = SPACETIME COVERING OR PRECURSOR CAPACITY**.
