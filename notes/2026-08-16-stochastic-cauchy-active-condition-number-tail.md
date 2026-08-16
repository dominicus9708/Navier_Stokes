# Stochastic Cauchy activity forces a quantitative large-condition-number tail

Date: 2026-08-16

Status: **EXACT CONSEQUENCE OF THE STOCHASTIC CAUCHY MARTINGALE, THE DEEP FIRST-HITTING CAP, AND VOLUME-PRESERVING MATRIX ALGEBRA. IT REEXPRESSES THE RARE-HISTORY BRANCH AS A MATERIAL CONDITION-NUMBER TAIL. GLOBAL REGULARITY NOT PROVED.**

## 1. Good coherent terminal set

At the coherent Reynolds-one crossing choose a good set

\[
G_R\subset B_{cR}
\]

with

\[
|G_R|\gtrsim R^3
\]

and one fixed unit axis `e` such that

\[
\boxed{\Omega_T(x)\cdot e\ge c_0>0}
\]

for every `x in G_R` after discarding a negligible bad subset.

Choose the deep checkpoint

\[
q=q_\beta=W/R^\beta,
\qquad
\|\Omega_-\|_\infty\le q^{-1}.
\]

---

## 2. Stochastic Cauchy scalar

For a fixed terminal point `x`, let

\[
Z_x^\varpi
=D_T^{- ,\varpi}(x)
\Omega_-(A_T^{- ,\varpi}(x))
\]

be the deep-checkpoint stochastic Cauchy invariant transported to the terminal tangent space.

The exact stochastic Cauchy representation gives

\[
\boxed{E_\varpi Z_x^\varpi=\Omega_T(x).}
\]

Define the scalar

\[
Y_x^\varpi=e\cdot Z_x^\varpi
\]

and second moment

\[
m_2(x)=E_\varpi|Z_x^\varpi|^2.
\]

Then

\[
E Y_x\ge c_0.
\]

---

## 3. Positive-probability active histories

Let

\[
A_x=\{Y_x\ge c_0/2\}.
\]

On the complement, `Y_x<c0/2`. Therefore

\[
\begin{aligned}
c_0
&\le E Y_x\\
&\le c_0/2
+E[|Y_x|1_{A_x}]\\
&\le c_0/2
+m_2(x)^{1/2}P(A_x)^{1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
P(A_x)
\ge
\frac{c_0^2}{4m_2(x)}.
}
\]

Thus bounded stochastic Cauchy second moment forces a nonvanishing fraction of genuinely active histories; rare histories can dominate only by making `m2` large.

---

## 4. Active history implies a q-size deformation

On `A_x`,

\[
|Z_x|\ge c_0/2.
\]

Since the deep precursor obeys

\[
|\Omega_-|\le q^{-1},
\]

we obtain

\[
\boxed{
\|D_T^{- ,\varpi}(x)\|_{op}
\ge c_1 q
}
\]

on every active history.

For the stochastic flow derivative the determinant is one pathwise because the drift is incompressible and the Brownian noise is additive:

\[
\det D_T^{- ,\varpi}=1.
\]

Let the singular values be

\[
\sigma_1\ge\sigma_2\ge\sigma_3>0,
\qquad
\sigma_1\sigma_2\sigma_3=1.
\]

If

\[
\sigma_1\ge c_1q,
\]

then

\[
\sigma_2\sigma_3=\sigma_1^{-1}
\le(c_1q)^{-1}.
\]

Since `sigma3<=sqrt(sigma2 sigma3)`,

\[
\sigma_3\le(c_1q)^{-1/2}.
\]

Therefore the condition number satisfies

\[
\boxed{
\kappa(D_T^{- ,\varpi})
=\sigma_1/\sigma_3
\ge c_2 q^{3/2}.
}
\]

So every stochastic history that actually carries an order-one terminal Cauchy contribution is a very strongly distorted history.

---

## 5. Integrate over the whole coherent core

Define the core-averaged second moment

\[
\boxed{
\bar m_2
=\frac1{|G_R|}
\int_{G_R}m_2(x)dx.
}
\]

Integrating the pointwise probability lower bound and using Cauchy--Schwarz / harmonic-arithmetic mean,

\[
\begin{aligned}
\int_{G_R}P(A_x)dx
&\ge
c\int_{G_R}\frac{dx}{m_2(x)}\\
&\ge
c\frac{|G_R|^2}{\int_{G_R}m_2(x)dx}.
\end{aligned}
\]

Hence

\[
\boxed{
\int_{G_R}P(A_x)dx
\gtrsim
\frac{R^3}{\bar m_2}.
}
\]

On this product probability--space set,

\[
\boxed{
\kappa(D_T^-)
\gtrsim q^{3/2}.
}
\]

---

## 6. Express m2 through deformation-weighted palinstrophy

The stochastic Cauchy martingale quadratic-variation identity gives

\[
E|Z_x^-|^2
-|\Omega_T(x)|^2
=
2\nu E\int_{s_-}^{T}
|D_T^s\nabla\Omega(A_T^s,s)|_F^2ds.
\]

Integrating over `G_R`, define

\[
\mathcal Q_D
=\int_{G_R}E\int_{s_-}^{T}
|D_T^s\nabla\Omega(A_T^s,s)|_F^2dsdx.
\]

Because `|Omega_T|~1` on `G_R`,

\[
\boxed{
\bar m_2
\asymp
1+
\frac{2\nu}{R^3}\mathcal Q_D
}
\]

up to fixed coherent-core constants.

Consequently the product measure of histories carrying `q^(3/2)` condition number obeys

\[
\boxed{
\mu_{\rm active}
\gtrsim
\frac{R^3}
{1+2\nu\mathcal Q_D/R^3}.
}
\]

This is the exact probability--derivative tradeoff behind the earlier strain/weighted-palinstrophy inequality.

---

## 7. Strain consequence

For a volume-preserving deformation path `F`, singular-value evolution gives

\[
\log\kappa(F)
\le
2\int\|S(X_s,s)\|_{op}ds.
\]

Therefore on the active set

\[
\boxed{
\int_{s_-}^{T}|S(X_s,s)|ds
\gtrsim
\log q.
}
\]

Thus the alternatives are now explicit:

1. `Q_D/R^3` remains bounded: then a positive fraction of the whole `R^3` coherent core must follow stochastic histories with condition number at least `q^(3/2)` and strain action at least `c log q`;
2. that active fraction collapses: then `Q_D/R^3` must diverge and the deformation-weighted derivative branch is active.

---

## 8. Relation to affine/residual factorization

For any common affine representative `F_aff` and full stochastic deformation `H`, write exactly

\[
H=F_{\rm aff}G.
\]

On every active history,

\[
\|H\|\gtrsim q.
\]

Hence for any `0<theta<1`, either

\[
\boxed{
\|F_{\rm aff}\|\gtrsim q^{1-\theta}
}
\]

or

\[
\boxed{
\|G\|\gtrsim q^\theta.
}
\]

The first is the coherent affine channel; when the stochastic tube is affine-Gaussian enough, the deep-checkpoint affine heat theorem converts it to the ordinary strain--palinstrophy product barrier.

The second is the residual counter-deformation channel and is generated by

\[
G'
=F_{\rm aff}^{-1}
(\nabla U-L)
F_{\rm aff}G.
\]

Thus it is an explicitly typed residual-gradient / non-affine deformation event rather than a new stochastic escape.

---

## 9. Claim boundary

The condition-number tail is exact. The final conversion of a large residual factor `G` into an unweighted ordinary derivative budget remains critical when `F_aff` is itself strongly anisotropic, because conjugation can amplify residual matrices.

Likewise the affine heat product barrier transfers to the nonlinear flow only on an affine-dominant stochastic tube; the Girsanov/kernel-residual ledgers measure failure of that approximation.

Overall status: **RARE STOCHASTIC CAUCHY HISTORIES CONVERTED TO A QUANTITATIVE MATERIAL CONDITION-NUMBER TAIL / BOUNDED Q_D FORCES A POSITIVE-VOLUME LARGE-DEFORMATION ENSEMBLE / THE ONLY REMAINDER IS AFFINE-VERSUS-RESIDUAL DEFORMATION TRANSFER.**
