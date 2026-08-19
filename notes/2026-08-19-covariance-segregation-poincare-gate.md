# Strain-gradient covariance segregation and the weighted Poincare gate

Date: 2026-08-19

Status: **DERIVED POINTWISE COVARIANCE-DERIVATIVE BOUND + CONDITIONAL H/T DICHOTOMY / GLOBAL REGULARITY NOT PROVED**.

This note treats the spatial covariance-segregation branch left by the projective angular analysis.

---

## 1. Local covariance field

Write the six strain-component gradient vectors schematically as

\[
g_\alpha=\nabla S_\alpha,
\]

and set

\[
p=\sum_\alpha|g_\alpha|^2=|\nabla S|^2,
\]

\[
G=\sum_\alpha g_\alpha\otimes g_\alpha,
\qquad
C=G/p
\]

where `p>0`.

Then `C` is positive semidefinite with trace one.

---

## 2. Pointwise derivative bound for the covariance

For each spatial derivative `partial_l`, let

\[
h_{\alpha,l}=\partial_l g_\alpha,
\qquad
H_l=\sum_\alpha|h_{\alpha,l}|^2.
\]

Then

\[
|\partial_lG|_F
\le
2\sqrt{pH_l},
\]

and

\[
|\partial_lp|
\le
2\sqrt{pH_l}.
\]

Since `G` is positive semidefinite with `tr G=p`,

\[
|G|_F\le p.
\]

Differentiating `C=G/p` therefore yields

\[
|\partial_lC|_F
\le
4\sqrt{H_l/p}.
\]

Consequently

\[
\boxed{
p|\nabla C|_F^2
\le
16|\nabla^2S|^2.
}
\]

After integration over `R3`, Fourier equivalence gives

\[
\boxed{
\int p|\nabla C|_F^2dx
\le
16\|\Delta S\|_2^2.
}
\]

Thus rapid spatial rotation/segregation of the strain-gradient covariance cannot occur for free; it is paid directly by second derivatives of strain.

---

## 3. Gradient-energy probability measure

Let

\[
P_S=\int p\,dx
\]

and define

\[
\boxed{
d\mu_C(x)=\frac{p(x)}{P_S}dx.}
\]

The global covariance is

\[
\bar C=\int C\,d\mu_C,
\]

and the spatial covariance variance is

\[
\boxed{
\mathcal V_C
=\int|C-\bar C|_F^2d\mu_C.
}
\]

Moreover

\[
\boxed{
\int|\nabla C|_F^2d\mu_C
\le
16\frac{\|\Delta S\|_2^2}{P_S}.
}
\]

---

## 4. Weighted Poincare length

Let `L_C^2` denote the optimal weighted Poincare constant of `mu_C` for matrix-valued test functions, i.e. the least number such that

\[
\operatorname{Var}_{\mu_C}(F)
\le
L_C^2\int|\nabla F|^2d\mu_C
\]

for the relevant class of `F`.

Applying this to `F=C` gives

\[
\boxed{
\mathcal V_C
\le
16L_C^2
\frac{\|\Delta S\|_2^2}{P_S}.
}
\]

Equivalently, if

\[
\mathcal V_C\ge v_0>0,
\]

then

\[
\boxed{
\frac{\|\Delta S\|_2^2}{P_S}
\ge
\frac{v_0}{16L_C^2}.
}
\]

Thus non-small covariance segregation has only two realizations:

1. `||Delta S||_2^2/P_S` is large: a higher-derivative `H` cost;
2. `L_C` is large: the gradient-energy measure has a large Poincare length, indicating weak connectivity, separated cores, bottlenecks, or large spatial extent, i.e. a typed multicore/material-turnover `T` geometry.

---

## 5. Near-isotropic global Fourier state

Recall the exact anisotropy decomposition

\[
\mathfrak A_{\nabla S}
=
\mathcal V_C
+\frac23-\mathcal J_{\nabla S}.
\]

If

\[
\mathcal J_{\nabla S}\to\frac23
\]

while advection saturation requires

\[
\mathfrak A_{\nabla S}\ge a_0>0,
\]

then necessarily

\[
\mathcal V_C\ge a_0/2
\]

for all sufficiently late states.

The weighted Poincare gate therefore implies

\[
\boxed{
\mathcal J_{\nabla S}\to\frac23
+\text{ advection saturation}
\Longrightarrow
H\ \text{or}\ T,
}
\]

where failure of a controlled weighted Poincare length is itself classified as the multicore/weak-connectivity `T` branch.

---

## 6. Endpoint reduction for the projective dispersion

Together with the transverse angular uncertainty lemma,

\[
\mathcal J_{\nabla S}\to0
\Longrightarrow H\text{ or }T,
\]

and the present covariance-segregation gate,

\[
\mathcal J_{\nabla S}\to\frac23
\Longrightarrow H\text{ or }T
\]

for an advection-saturated sequence, subject in the second implication to the weighted Poincare classification above.

Therefore a genuinely new tight/nonconcentrating survivor must keep

\[
\boxed{
\mathcal J_{\nabla S}
\in[j_-,j_+]
\Subset(0,2/3)
}
\]

along the dangerous subsequence.

The final unresolved angular branch is consequently an **interior projective-dispersion saturation** rather than either endpoint geometry.

Status: **COVARIANCE SEGREGATION TYPED AS H OR WEAK-CONNECTIVITY T; BOTH ANGULAR ENDPOINTS REDUCED; INTERIOR DISPERSION PACKING REMAINS OPEN**.
