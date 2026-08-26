# DSD M5-30 — Smooth Threshold Collar Degeneracy

Date: 2026-08-27

Status: **DERIVED STRUCTURAL BARRIER / DIRECT COMMUTATOR ABSORPTION BY A SMOOTH HARD THRESHOLD ENTROPY LOSES DIRECTION COERCIVITY AT THE THRESHOLD / GLOBAL REGULARITY UNPROVED.**

## 1. Formation core recalled

On the normalized threshold-one cell let

\[
a=|V|,\qquad n=V/a,
\]

and for the quadratic excess

\[
\Phi_2(a)=\frac12(a-1)_+^2
\]

let

\[
W_2=\nabla_V\Phi_2(V)=(a-1)_+n.
\]

The exact formation work is

\[
T_{form}
=-\langle \Omega\times V,[\mathbb P,f_2]V\rangle
=\mathcal G'+\nu\mathcal D_{exc},
\]

where

\[
f_2(a)=(1-a^{-1})_+.
\]

At a fixed positive first hit,

\[
T_{form}\ge c_{form}>0.
\]

## 2. Lamb field in amplitude-direction variables

Using

\[
\Omega=\nabla a\times n+a\,\nabla\times n
\]

and `|n|=1`,

\[
\boxed{
\Omega\times V
=-a\nabla_\perp a+a^2(n\cdot\nabla)n.
}
\]

The first term is amplitude deformation. The second is streamline/direction curvature.

For the quadratic excess entropy,

\[
\mathcal D_{exc}
=
\int_{a>1}
\left[
|\nabla a|^2+a(a-1)|\nabla n|^2
\right]dz.
\]

Thus the amplitude part is directly controlled, while the direction weight loses the factor needed to control `a^2(n·grad)n` uniformly as `a downarrow 1`.

## 3. General smooth radial truncation

Let

\[
\mathcal E_\Phi(V)=\int \Phi(|V|)\,dz
\]

with

\[
\Phi(a)=0\qquad (a\le1),
\]

and assume `Phi` is convex and `C^1` across `a=1`.

Because `Phi` is constant on the inactive side,

\[
\boxed{\Phi'(1)=0.}
\]

For smooth positive `a`, the Hessian of the radial function gives the viscous form

\[
\boxed{
\mathcal D_\Phi
=
\int
\left[
\Phi''(a)|\nabla a|^2
+a\Phi'(a)|\nabla n|^2
\right]dz.
}
\]

The direction coefficient is therefore

\[
a\Phi'(a),
\]

and necessarily

\[
\boxed{
a\Phi'(a)\to0\qquad(a\downarrow1).}
\]

Hence every smooth hard-threshold amplitude entropy has a direction-coercivity collar degeneracy.

## 4. DSD interpretation

This is not a defect of the particular quadratic choice. It is forced by the typed requirements

1. exact inactive region `a<=1`;
2. smooth `C^1` matching across the state boundary;
3. radial amplitude entropy.

The state-boundary condition forces the first derivative to vanish, and the first derivative is exactly the coefficient multiplying angular/direction diffusion.

Thus

\[
\boxed{
\text{smooth hard threshold}
\Longrightarrow
\text{direction dissipation degenerates at the threshold}.
}
\]

## 5. Consequence for direct commutator absorption

A direct universal estimate of the form

\[
|T_{form}|
\le\theta\nu\mathcal D_\Phi,
\qquad\theta<1,
\]

cannot be obtained merely by pointwise comparison of the Lamb curvature term with the smooth-threshold Hessian, because the curvature carries an `a^2` weight while the entropy direction dissipation carries `a Phi'(a)` and the latter vanishes at `a=1`.

This does not prove that every more sophisticated commutator estimate fails. It proves that **the naive same-entropy coercive absorption route has an intrinsic threshold collar gap**.

## 6. Next admissible route

To remove this particular degeneracy one must relax at least one of the preceding typed requirements. The most conservative option is to retain the exact hard threshold but allow a nonsmooth convex entropy with a positive right derivative at `a=1`.

The canonical candidate is

\[
\Phi_1(a)=(a-1)_+,
\]

or the combined entropy

\[
\Phi_\beta(a)
=
\frac12(a-1)_+^2+\beta(a-1)_+,
\qquad\beta>0.
\]

Its direction coefficient is nondegenerate on the active side, at the cost of a positive level-set measure in the amplitude Hessian.

That tradeoff is the target of M5-31.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
