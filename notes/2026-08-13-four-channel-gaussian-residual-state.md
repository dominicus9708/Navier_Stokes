# Four-channel exact Gaussian residual state: strain shape/amplitude + vorticity projective/signed-line defects

Date: 2026-08-13

Status: **EXACT HILBERT-SPACE VARIANCE DECOMPOSITION / DSD RESIDUAL STATE REFINED**.

The self-consistent Gaussian affine closure gives

\[
\mathcal B_\gamma
=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega).
\]

The vorticity variance already splits exactly into projective and signed-line defects.  The same construction applies to the five-dimensional Hilbert space of trace-free symmetric strain matrices.

The result is a canonical four-channel residual state.

---

## 1. Strain as a vector in a five-dimensional Hilbert space

Let

\[
\mathcal H
=\{A\in\mathbb R^{3\times3}:A^T=A,\ \operatorname{tr}A=0\}
\]

with Frobenius inner product

\[
\langle A,B\rangle_F=\operatorname{tr}(AB).
\]

Then

\[
\dim\mathcal H=5.
\]

For a probability weight `gamma`, define

\[
E_{S,\gamma}
=\int\gamma|S|_F^2,
\qquad
\bar S_\gamma
=\int\gamma S.
\]

For `E_{S,gamma}>0`, define the covariance operator on `H`

\[
\mathcal C_{S,\gamma}
=\frac1{E_{S,\gamma}}
\int\gamma\,S\otimes_{\mathcal H}S.
\]

It is positive semidefinite and has trace one.

Let

\[
\mu_1
=\lambda_{\max}(\mathcal C_{S,\gamma}).
\]

---

## 2. Strain-shape defect

Define

\[
\boxed{
D_{S,\rm shape}
=E_{S,\gamma}(1-\mu_1).
}
\]

Equivalently,

\[
\boxed{
D_{S,\rm shape}
=\min_{\substack{A\in\mathcal H\\ |A|_F=1}}
\int\gamma
\left|S-\langle S,A\rangle_FA\right|_F^2.
}
\]

Thus this is the least residual strain energy outside one fixed matrix shape.

`D_S,shape=0` means that, throughout the weighted window,

\[
S(y)=a(y)A_*
\]

for one fixed trace-free symmetric matrix `A_*`, up to a null set.

Consequently the eigenframe and eigenvalue ratios are fixed; only the scalar amplitude may vary.

---

## 3. Same-shape amplitude defect

Define

\[
\boxed{
D_{S,\rm amp}
=E_{S,\gamma}\mu_1-|\bar S_\gamma|_F^2.
}
\]

Exactly as in the vector case,

\[
D_{S,\rm amp}\ge0.
\]

It measures failure of the first strain moment to saturate the largest second-moment strain-shape channel.

When `D_S,shape` is already small, this is the remaining amplitude/sign variation along the selected strain shape.

---

## 4. Exact strain variance split

The weighted strain variance is

\[
\operatorname{Var}_\gamma(S)
=E_{S,\gamma}-|\bar S_\gamma|_F^2.
\]

Insert and subtract `E_S,gamma mu_1`:

\[
\boxed{
\operatorname{Var}_\gamma(S)
=D_{S,\rm shape}+D_{S,\rm amp}.
}
\]

Both terms are nonnegative.

If both vanish, then

\[
\boxed{S(y)=\bar S_\gamma}
\]

for `gamma`-almost every `y`: the strain is genuinely affine-constant across the observation window.

---

## 5. Combine with the vorticity split

For vorticity, write

\[
D_{\omega,\rm proj}
=E_{\omega,\gamma}
[1-\lambda_{\max}(C_{\omega,\gamma})],
\]

and

\[
D_{\omega,\rm line}
=E_{\omega,\gamma}
\lambda_{\max}(C_{\omega,\gamma})
-|\bar\Omega_\gamma|^2.
\]

Then

\[
\operatorname{Var}_\gamma(\Omega)
=D_{\omega,\rm proj}+D_{\omega,\rm line}.
\]

Therefore the Gaussian affine residual-gradient variance is exactly

\[
\boxed{
\mathcal B_\gamma
=
D_{S,\rm shape}
+D_{S,\rm amp}
+\frac12D_{\omega,\rm proj}
+\frac12D_{\omega,\rm line}.
}
\]

This is the canonical four-channel residual state.

---

## 6. Meaning of the four branches

### S1 — strain-shape variation

\[
D_{S,\rm shape}>0.
\]

The local strain cannot be represented by one eigenframe/eigenvalue-ratio shape.  This intersects

- compressive-axis rotation;
- eigenvalue-gap variation;
- pressure-Hessian forcing;
- strain curvature / high derivatives.

### S2 — strain-amplitude variation

\[
D_{S,\rm shape}\approx0,
\qquad
D_{S,\rm amp}>0.
\]

The strain has nearly one fixed matrix shape but its signed scalar amplitude varies across the heat window.  Spatial variation then returns to strain-gradient / curvature channels.

### W1 — vorticity projective variation

\[
D_{\omega,\rm proj}>0.
\]

The local vorticity is genuinely multi-axis and returns to projective covariance, angular palinstrophy, pairwise cross-axis, and coherence/depletion channels.

### W2 — signed-line variation

\[
D_{\omega,\rm proj}\approx0,
\qquad
D_{\omega,\rm line}>0.
\]

The vorticity is nearly one unoriented line but still varies through sign, magnitude, or first/second-moment mismatch.  This returns to polarity, oriented-flux, magnitude-gradient, and mixed-sign channels.

---

## 7. Relation to the Betchov hard affine geometry

The affine source-optimal strain shape is

\[
A_{\rm Bet}
\propto
\operatorname{diag}(-2,1,1)
\]

up to rotation and sign.

If `D_S,shape` is small, the Gaussian window has a well-defined dominant strain shape `A_*`.

Then the affine hard branch splits again:

1. `A_*` is close to the Betchov orbit — compression-diffusion and extensional-plane covariance constraints apply;
2. `A_*` stays away from the Betchov orbit — determinant/source efficiency has a strict finite-dimensional deficit.

Thus strain-shape coherence does not create a free residual escape; it makes the remaining affine geometry more rigid.

---

## 8. Residual Duhamel form

The endpoint residual estimate becomes

\[
\boxed{
\begin{aligned}
\mathfrak R_\gamma
\lesssim
\int &\|F\|\,\|\Omega\|_\infty
(1+\sqrt{\kappa(\Sigma)})\\
&\times
\left[
D_{S,\rm shape}
+D_{S,\rm amp}
+\frac12D_{\omega,\rm proj}
+\frac12D_{\omega,\rm line}
\right]^{1/2}ds.
\end{aligned}
}
\]

A large residual therefore has a finite, explicitly typed structural cause at every affine heat scale.

---

## 9. DSD interpretation

The Gaussian affine representative is the resolved state.  Its unresolved sector has four and only four orthogonal second-moment causes at this level:

\[
\boxed{
\text{strain shape}
\oplus
\text{strain amplitude}
\oplus
\text{vorticity axis}
\oplus
\text{vorticity signed-line}.
}
\]

This is a direct static-aggregation decomposition embedded inside the dynamic Duhamel channel.

Status: **RESIDUAL GEOMETRY REDUCED TO FOUR EXACT NONNEGATIVE CHANNELS / REPEATED CRITICAL SATURATION AMONG THEM REMAINS OPEN**.
