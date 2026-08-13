# Compressive eigenaxis rotation source: pressure Hessian, viscous curvature, or normal-vorticity leakage

Date: 2026-08-13

Status: **EXACT POINTWISE EIGENFRAME IDENTITY / CONNECTS BIAXIAL AXIS ROTATION TO EXISTING PRESSURE, HIGH-DERIVATIVE, AND COVARIANCE CHANNELS**.

The rotation-independent affine diffusion lemma already shows that rapid rotation of the compressive axis cannot erase the transverse precursor requirement in the linear affine model.

For the full nonlinear Navier--Stokes dynamics one can go further: the material rotation of a **simple compressive strain eigendirection** has an exact source decomposition.  In the hard extensional-plane geometry, the local vorticity term that could rotate the strain eigenframe is itself depleted.  Fast rotation must therefore be supplied mainly by an off-diagonal pressure Hessian, viscous strain curvature, or loss of the extensional-plane covariance condition.

---

## 1. Velocity-gradient and strain equations

Let

\[
G=\nabla u,
\qquad
S=\frac12(G+G^T),
\qquad
A=\frac12(G-G^T).
\]

The gradient equation for smooth incompressible Navier--Stokes is

\[
\boxed{
D_tG+G^2
=-\nabla^2p+\nu\Delta G,
}
\]

where

\[
D_t=\partial_t+u\cdot\nabla.
\]

Taking the symmetric part and using that `SA+AS` is skew gives

\[
\boxed{
D_tS+S^2+A^2
=-\nabla^2p+\nu\Delta S.
}
\]

---

## 2. Antisymmetric square in terms of vorticity

The antisymmetric velocity gradient acts as

\[
Ax=\frac12\omega\times x.
\]

Hence

\[
\boxed{
A^2
=\frac14
(\omega\otimes\omega-|\omega|^2I).
}
\]

This gives an explicit vorticity contribution to strain-eigenframe rotation.

---

## 3. Material derivative of a simple compressive eigenvector

Let

\[
Sn=\lambda_1n,
\qquad |n|=1,
\]

where `lambda1` is simple and

\[
\lambda_1<\lambda_2\le\lambda_3.
\]

Differentiate the eigenvalue equation materially:

\[
(D_tS)n+S(D_tn)
=(D_t\lambda_1)n+\lambda_1D_tn.
\]

Because

\[
n\cdot D_tn=0,
\]

projection to an orthogonal eigenvector `e_j`, `j=2,3`, gives

\[
\boxed{
e_j\cdot D_tn
=\frac{e_j\cdot(D_tS)n}
{\lambda_1-\lambda_j}.}
\]

Therefore, with eigengap

\[
\boxed{g=\lambda_2-\lambda_1>0,}
\]

we have

\[
\boxed{
|D_tn|
\le
\frac1g
|P_{n^\perp}(D_tS)n|.
}
\]

For the rank-one projector

\[
P_-=n\otimes n,
\]

\[
\boxed{
|D_tP_-|_F
=\sqrt2|D_tn|.
}
\]

---

## 4. `S^2` cannot rotate the strain eigenframe

Since `n` is an eigenvector of `S`,

\[
S^2n=\lambda_1^2n.
\]

Thus

\[
\boxed{
P_{n^\perp}S^2n=0.
}
\]

Self-interaction of the strain eigenvalues changes their magnitudes but does not directly rotate a simple eigenvector.

This removes one apparently nonlinear term completely from the rotation ledger.

---

## 5. Exact vorticity contribution to eigenaxis rotation

Using

\[
A^2n
=\frac14
[(\omega\cdot n)\omega-|\omega|^2n],
\]

we get

\[
\boxed{
P_{n^\perp}A^2n
=\frac14
(\omega\cdot n)\omega_\perp,
}
\]

where

\[
\omega_\perp
=P_{n^\perp}\omega.
\]

Therefore

\[
\boxed{
|P_{n^\perp}A^2n|
=\frac14
|\omega\cdot n|\,|\omega_\perp|.
}
\]

---

## 6. Full compressive-axis rotation inequality

Project the strain equation onto `n^perp`.  Since the `S^2` term vanishes there,

\[
P_{n^\perp}(D_tS)n
=-P_{n^\perp}(\nabla^2p)n
-P_{n^\perp}A^2n
+\nu P_{n^\perp}(\Delta S)n.
\]

Hence

\[
\boxed{
\begin{aligned}
g|D_tn|
\le{}&
|P_{n^\perp}(\nabla^2p)n|\\
&+\frac14
|\omega\cdot n|\,|\omega_\perp|\\
&+\nu
|P_{n^\perp}(\Delta S)n|.
\end{aligned}
}
\]

Equivalently for the projector,

\[
\boxed{
\begin{aligned}
\frac g{\sqrt2}|D_tP_-|_F
\le{}&
|P_{n^\perp}(\nabla^2p)n|\\
&+\frac14|\omega\cdot n||\omega_\perp|\\
&+\nu|P_{n^\perp}(\Delta S)n|.
\end{aligned}
}
\]

This is the exact pointwise rotation-source inequality.

---

## 7. Specialize to the Betchov hard branch

For the determinant/source-optimal strain shape

\[
(\lambda_1,\lambda_2,\lambda_3)
\approx(-2a,a,a),
\]

the compressive eigengap is

\[
\boxed{g\approx3a.}
\]

The exact affine-covariance envelope showed that maximal affine source requires depletion of vorticity covariance along the compressive normal:

\[
\boxed{e_1^TCe_1\ll1.}
\]

Pointwise, the corresponding ideal condition is

\[
|\omega\cdot n|\ll|\omega|.
\]

But the vorticity-driven eigenframe-rotation term is precisely proportional to

\[
|\omega\cdot n|\,|\omega_\perp|.
\]

Thus the same geometry that maximizes extensional-plane stretching **depletes the direct vorticity source of compressive-axis rotation**.

---

## 8. Local covariance estimate for the vorticity rotation source

On a region `B` with approximately constant compressive axis `n`, define

\[
E_B=\int_B|\omega|^2,
\]

and the covariance normal fraction

\[
\boxed{
c_-=n^TC_Bn
=\frac1{E_B}\int_B|\omega\cdot n|^2.}
\]

Then

\[
\int_B|\omega_\perp|^2
=E_B(1-c_-).
\]

Cauchy--Schwarz gives

\[
\boxed{
\int_B
|\omega\cdot n|\,|\omega_\perp|
\le
E_B\sqrt{c_-(1-c_-)}.
}
\]

Hence the aggregate `A^2` rotation source vanishes as

\[
\boxed{c_-\to0.}
\]

This is the quantitative covariance-to-eigenframe bridge.

---

## 9. Updated axis-rotation channels

Fast material rotation of the compressive axis with a robust eigengap requires at least one of:

### P — pressure-Hessian rotation

\[
\boxed{
|P_{n^\perp}(\nabla^2p)n|
\text{ is large}.}
\]

This is a nonlocal pressure-coupling channel.

### V2S — viscous strain-curvature rotation

\[
\boxed{
\nu|P_{n^\perp}(\Delta S)n|
\text{ is large}.}
\]

Since `S` is a zero-order transform of vorticity, this is a high-derivative/viscous channel related to second vorticity derivatives.

### N — normal-vorticity leakage

\[
\boxed{
|\omega\cdot n||\omega_\perp|
\text{ is not depleted}.}
\]

This means the vorticity covariance leaves the source-optimal extensional plane and pays an affine-coupling deficit.

Thus the rotating-axis escape is not free; it returns to already recognizable pressure, high-derivative, or covariance-leakage channels.

---

## 10. Relation to the rotation-independent affine diffusion bound

The linear affine heat-covariance theorem already eliminates axis rotation as an independent mechanism for erasing all compression-enhanced diffusion: at least a transverse precursor reservoir remains regardless of rotation.

The present pointwise identity adds a nonlinear source ledger:

\[
\boxed{
\text{fast axis rotation}
\Longrightarrow
P\text{ or }V2S\text{ or }N.
}
\]

Therefore future perturbative analysis does not need to treat the entire eigenvector path as an unexplained fourth escape channel.

---

## 11. Claim boundary

The pressure-Hessian term is not yet controlled by the existing pressure-difference estimates, which mostly operate at lower derivative level.

Likewise, the local covariance estimate assumes a sufficiently coherent choice of compressive axis across the observation region.

The note does not prove that any of `P`, `V2S`, or `N` is impossible.  It only identifies the exact sources required to rotate the compressive eigenframe.

Status: **AXIS-ROTATION SOURCE DECOMPOSITION CLOSED / PRESSURE-HESSIAN AND HIGH-DERIVATIVE ROTATION COSTS REMAIN TO BE CLOSED**.
