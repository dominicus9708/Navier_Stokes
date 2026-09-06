# DSD Certificate — Pavesi explicit spectral-flux counterexample and implementation mismatch

Date: 2026-09-06  
Repository: `dominicus9708/Navier_Stokes`  
Paper: Luca Eliseo Pavesi, *Global Regularity for the Three-Dimensional Incompressible Navier–Stokes Equations via Geometric Frustration and Helical Quasi-Trapping* (2026).  
Status: **SAFE CORE-HINGE COUNTEREXAMPLE / NUMERICAL-IMPLEMENTATION SCOPE MISMATCH**

## 1. Target statement

Theorem 6.1 claims an absolute constant `C_*`, independent of the initial data and viscosity, such that for every smooth solution and every `K>=1`,

\[
|\Pi(K,t)|\le C_*\frac{E_{>K}(t)^{1/2}E(t)^{1/2}}{K}.
\]

The spectral flux is the standard Hermitian energy pairing of the high-frequency velocity with the nonlinear Fourier term.

Because the theorem is stated for every smooth initial datum, it must in particular hold at `t=0` for every smooth divergence-free trigonometric polynomial initial datum.

## 2. Explicit real divergence-free six-mode datum

On `T^3`, let

\[
p=(1,0,0),\qquad q=(0,1,0),\qquad r=p+q=(1,1,0).
\]

Take the only nonzero Fourier coefficients to be

\[
\hat u(p)=\hat u(-p)=e_3,
\]

\[
\hat u(q)=\hat u(-q)=e_1,
\]

\[
\hat u(r)=i e_3,\qquad \hat u(-r)=-i e_3.
\]

Conjugate symmetry gives a real field, and

\[
k\cdot\hat u(k)=0
\]

for every active mode, so the datum is divergence-free and smooth.

Equivalently, in physical variables one may write

\[
u(x,y,z)=
\bigl(2\cos y,\ 0,\ 2\cos x-2\sin(x+y)\bigr).
\]

## 3. Exact nonlinear flux at `K=1`

Use

\[
F(k)=-iP_k\sum_{a+b=k}(\hat u(a)\cdot b)\hat u(b).
\]

At `k=r`, only the ordered pairs `(p,q)` and `(q,p)` from the active support contribute to the `r` coefficient relevant to the pairing.  They give

\[
(\hat u(p)\cdot q)\hat u(q)=0,
\]

and

\[
(\hat u(q)\cdot p)\hat u(p)=e_3.
\]

Because `e_3\perp r`, the Leray projector leaves this vector unchanged, hence

\[
F(r)=-i e_3.
\]

By conjugate symmetry,

\[
F(-r)=i e_3.
\]

For cutoff `K=1`, the only presently occupied modes above the cutoff are `±r`. Therefore

\[
\Pi(1)
=\Re\left(
\overline{\hat u(r)}\cdot F(r)
+\overline{\hat u(-r)}\cdot F(-r)
\right)
=-2.
\]

The energies are exactly

\[
E=\frac12\sum_k|\hat u(k)|^2=3,
\qquad
E_{>1}=1.
\]

The accompanying executable certificate is

`certificates/pavesi_explicit_flux_scaling_counterexample.py`.

## 4. Amplitude contradiction

For any finite `A>0`, `A u` is again a smooth divergence-free admissible initial datum. At the initial instant,

\[
\Pi(1;Au)=A^3\Pi(1;u)=-2A^3,
\]

while

\[
E(Au)=3A^2,
\qquad
E_{>1}(Au)=A^2.
\]

The claimed theorem would therefore require

\[
2A^3\le \sqrt3\,C_*A^2,
\]

or

\[
A\le\frac{\sqrt3}{2}C_*.
\]

Choosing any larger finite `A` contradicts Theorem 6.1.

Thus

\[
\boxed{
\text{Theorem 6.1 is false in its stated data-independent form.}
}
\]

This conclusion does not depend on statistical turbulence assumptions, asymptotics, or numerical discretization.

## 5. Appendix B does not establish the missing deterministic estimate

The manuscript's Appendix B argues that if `|p|,|q|>K` but `|p+q|<=K`, then `p,q` are nearly opposite and nearly equal in magnitude, and then states that the volume of such configurations scales as `1/K`.

That observation does not by itself imply a deterministic bilinear operator-norm estimate for arbitrary Fourier coefficients and phases.  A solution can concentrate its Fourier mass on precisely the near-cancelling configurations.  To obtain the claimed estimate one would need an explicit weighted convolution/operator estimate controlling that concentration.  Such a derivation is not supplied in Appendix B.

DSD classification:

\[
\text{geometric rarity / phase-space volume}
\not\Rightarrow
\text{uniform deterministic norm suppression}.
\]

## 6. Numerical implementation tests the opposite spectral subspace

Section 6 defines

\[
V_K=\{u:\hat u(k)=0\text{ for }|k|\le K\},
\]

namely the **high-frequency** subspace supported strictly above `K`.

However, Appendix D.1 constructs

```python
mask_subspace = (np.sqrt(k2) <= K) & mask_dealias & (k2 > 0)
...
u_hat[d][~mask_subspace] = 0.0
```

so the numerical quasi-trapping test initializes a field in the **low-frequency** ball `|k|<=K`.

Therefore Figure 2 is not a numerical test of the `V_K` used in Lemma 6.2.

Moreover the code defines

```python
ratio = norm_outside / norm_inside
```

and the manuscript reports that this ratio is approximately `2.5`.  A ratio greater than one means the reported outside norm exceeds the inside norm, so it cannot by itself be read as evidence that only a small amount is generated outside the tested subspace.

DSD classification: **IMPLEMENTATION / CLAIM-DOMAIN MISMATCH**.

## 7. What survives

This certificate does not invalidate every helical identity or the conditional implication in Theorem 5.1.  Potentially useful survivors are:

- helical Fourier decomposition;
- conditional regularity consequences of a correctly proved flux-decay estimate;
- symbol-level cancellations that can be independently established;
- numerical experiments as diagnostics for specified ensembles.

What fails is the unconditional bridge asserting the universal flux estimate for arbitrary smooth data.

## 8. Regression rule for the internal M17 chain

The internal DSD route must not replace spectral leakage/recharge by a phase-space-rarity argument. M17-300 correctly retains the localized forcing

\[
F_j=\chi\mathcal N_j-2\nabla\chi\cdot\nabla V_j-(\Delta\chi)V_j
\]

and its band projection as an explicit payment branch.

The Pavesi counterexample therefore supplies a useful regression test:

\[
\boxed{
\text{No deterministic }1/K\text{ gain from angular/configuration rarity without an operator estimate.}
}
\]

Global 3D Navier–Stokes regularity remains unproved.
