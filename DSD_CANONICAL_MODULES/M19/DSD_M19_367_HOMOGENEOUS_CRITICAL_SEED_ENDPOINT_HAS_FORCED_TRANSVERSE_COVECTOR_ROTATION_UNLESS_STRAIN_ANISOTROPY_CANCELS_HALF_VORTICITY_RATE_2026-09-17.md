# DSD M19-367 — Homogeneous critical seed endpoint has forced transverse covector rotation unless strain anisotropy cancels the half-vorticity rate

Date: 2026-09-17  
Canonical ID: **M19-367**

Status: **ACTIVE TRANSVERSE ANGULAR TRANSPORT / HOMOGENEOUS-ENDPOINT REFINEMENT / NOT A CONTRADICTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M5-622 and M19-365

M5-622 gives, for

\[
G=P_\perp\nabla\log\rho,
\]

the exact equation

\[
D_BG=P_\perp\nabla(\sigma+\kappa)-L_\perp^TG,
\]

where

\[
L_\perp=P_\perp(\nabla B)P_\perp.
\]

On the homogeneous branch,

\[
P_\perp\nabla(\sigma+\kappa)=0,
\]

so

\[
\boxed{D_BG=-L_\perp^TG.}
\]

M19-365 identifies the scalar critical seed lock

\[
(\bar\kappa,\bar\sigma)\to\left(\frac32,-\frac12\right).
\]

## 2. Transverse block decomposition

Write

\[
\nabla U=\Sigma+\mathcal R,
\qquad
\mathcal Rv=\frac12W\times v.
\]

Since

\[
B=U+\frac12y,
\]

we have on the transverse plane

\[
\boxed{
L_\perp
=\Sigma_\perp+\mathcal R_\perp+\frac12I_\perp.
}
\]

Because \(W=\rho\xi\), define the positively oriented transverse quarter-turn \(J\) by

\[
Jv=\xi\times v.
\]

Then

\[
\boxed{\mathcal R_\perp=\frac\rho2J,\qquad J^T=-J.}
\]

Therefore

\[
-L_\perp^T
=-\Sigma_\perp+\frac\rho2J-\frac12I_\perp.
\]

Hence the homogeneous equation is

\[
\boxed{
D_BG
=-\Sigma_\perp G
+\frac\rho2JG
-\frac12G.
}
\]

## 3. Magnitude and direction equations

Write

\[
G=g\,n,
\qquad g=|G|>0,
\qquad |n|=1,\quad n\perp\xi.
\]

Taking the inner product with \(n\), the skew term vanishes and

\[
\boxed{
D_B\log g
=-n\cdot\Sigma n-\frac12.
}
\]

Subtracting the magnitude component yields

\[
\boxed{
D_Bn
=\frac\rho2Jn
-\Sigma_\perp n
+(n\cdot\Sigma n)n.
}
\]

This is the exact material direction equation for the transverse magnitude-gradient covector on the homogeneous branch.

## 4. Angular speed

Since the transverse plane is two-dimensional, \(D_Bn\perp n\) is proportional to \(Jn\). Define

\[
\omega_G:=Jn\cdot D_Bn.
\]

Then

\[
\boxed{
\omega_G
=\frac\rho2-Jn\cdot\Sigma n.
}
\]

Thus there is an intrinsic positive rotational contribution \(\rho/2\) from the local vorticity.

A static or slowly rotating transverse covector requires a compensating anisotropic-strain projection of the same size.

## 5. Principal-strain frame form

Let

\[
\lambda_2=-\frac\sigma2+\delta,
\qquad
\lambda_3=-\frac\sigma2-\delta
\]

be the two transverse strain eigenvalues, and write

\[
n=\cos\alpha\,e_2+\sin\alpha\,e_3.
\]

With the orientation \(Je_2=e_3\), one obtains

\[
Jn\cdot\Sigma n
=(\lambda_3-\lambda_2)\sin\alpha\cos\alpha
=-\delta\sin2\alpha.
\]

Hence

\[
\boxed{
\omega_G
=\frac\rho2+\delta\sin2\alpha.
}
\]

## 6. Quantitative dichotomy

If

\[
|\delta|\le\frac\rho2-\varepsilon
\]

on a retained event, then for every direction \(n\),

\[
\boxed{|\omega_G|\ge\varepsilon.}
\]

Thus weak transverse anisotropy cannot freeze the homogeneous covector: it forces material angular turnover at a definite rate.

Conversely, if \(|\omega_G|\) is small, then necessarily

\[
\boxed{|\delta|\ge\frac\rho2-O(|\omega_G|).}
\]

Therefore the homogeneous endpoint splits into

\[
\boxed{
H_{hom}
\Longrightarrow
G_{angular\ turnover}
\lor
G_{strong\ transverse\ strain\ anisotropy}.
}
\]

## 7. Relation to the critical scalar lock

At the M19-365 lock,

\[
\sigma\to-\frac12,
\]

so

\[
\lambda_2+\lambda_3\to\frac12.
\]

M19-367 shows that this trace condition is not enough to classify the transverse endpoint. The difference variable \(2\delta=\lambda_2-\lambda_3\) is dynamically essential because it competes directly with the half-vorticity rotation \(\rho/2\).

Hence the true critical endpoint is at least two-dimensional in its transverse state variables:

\[
\boxed{(\rho,\delta,\alpha)}
\]

in addition to the scalar lock \((\kappa,\sigma)=(3/2,-1/2)\).

## 8. Recurrent nonzero G

If \(g\) is bounded above and below recurrently, then

\[
\left\langle n\cdot\Sigma n\right\rangle=-\frac12.
\]

This constrains the strain sampled by the rotating covector but does not imply that one fixed transverse principal eigenvalue equals \(-1/2\). Rotation of \(n\) can realize the average.

Therefore the stronger claim

\[
\text{homogeneous recurrence}\Rightarrow\text{persistent repeated strain eigenvalue}
\]

is not certified and is explicitly rejected.

## 9. Connection to M5-623--624

If the strong-anisotropy branch drives one transverse eigenvalue toward the axial value \(\sigma\), M5-623--624 apply:

- crossing returns to the simple-gap strain-derivative branch;
- persistent multiplicity requires pressure-viscous anisotropy of size \(\rho^2/4\).

But M19-367 does not claim that every strong-anisotropy state reaches collision. The angular-turnover and noncollision anisotropy corridors remain live.

## 10. New target

The next gate is

\[
\boxed{
\mathcal T_{ang}^{crit}:
\text{price positive-density angular turnover of }G
\text{ or classify the strong-anisotropy locked conveyor.}
}
\]

A promising route is to compare the angular turnover with the full-rank derivative Gram tensor from M5-625--626 and with the strain-evolution/collision compensation law from M5-624.

## 11. Audit verdict

**PASS — the homogeneous Burgers-like endpoint is not static.**

Unless transverse strain anisotropy cancels the intrinsic half-vorticity rotation, the transverse magnitude-gradient covector turns at a definite material angular rate. This sharpens the critical endpoint but does not yet produce a finite cumulative contradiction.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
