# DSD M19-075 — Exact similarity symmetry audit shows rotations add genuine zero-center directions while translations and Galilean modes have ±1/2 exponents

**Date:** 2026-09-12  
**Status:** CENTER-SPECTRUM SYMMETRY CORRECTION / THE PREVIOUS SIMPLE-CENTER TARGET MUST FIRST BE QUOTIENTED BY COMPACT ROTATION SYMMETRY / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-067 identified

\[
Z_t=\partial_\theta U
\]

as an exact linearized center direction and proposed a simple-center-plus-transverse-contraction target.

Before attempting that theorem one must audit every exact symmetry of the similarity equation. Otherwise a symmetry-generated neutral direction can be misclassified as an analytic failure of contraction.

We work with

\[
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
=-\nabla\Pi+\nu\Delta U,
\qquad
\nabla\cdot U=0.
\]

The linearized equation about a complete trajectory \(U(\theta)\) is

\[
\boxed{
\partial_\theta W
+\frac12W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
+(W\cdot\nabla)U
=-\nabla Q+\nu\Delta W,
\qquad
\nabla\cdot W=0.
}
\]

## 2. Similarity-time translation

The similarity equation is autonomous in \(\theta\). Therefore

\[
U_s(y,\theta)=U(y,\theta+s)
\]

is again a solution.

Differentiating at \(s=0\) gives

\[
\boxed{
Z_t:=\partial_\theta U.
}
\]

It solves the exact linearized equation.

For a nonstationary recurrent orbit this is the familiar orbit-tangent neutral mode.

## 3. Physical scaling is not a second center direction

For the physical Navier--Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

write

\[
t=-e^{-\theta},
\qquad
x=e^{-\theta/2}y,
\qquad
u(x,t)=e^{\theta/2}U(y,\theta).
\]

Then

\[
\lambda^2t=-e^{-(\theta-2\log\lambda)},
\]

and the similarity coordinate \(y\) is unchanged. Consequently

\[
\boxed{
U_\lambda(y,\theta)
=U(y,\theta-2\log\lambda).
}
\]

Thus infinitesimal physical scaling produces

\[
\left.\partial_{\log\lambda}U_\lambda\right|_{\lambda=1}
=-2\partial_\theta U.
\]

Therefore

\[
\boxed{
\text{physical scaling tangent}
\equiv
\text{similarity-time tangent}.
}
\]

It is not an independent center dimension.

## 4. Rotations give genuine additional zero modes

For \(R\in SO(3)\), define

\[
U^R(y,\theta)
:=R\,U(R^{-1}y,\theta).
\]

The similarity equation is rotationally equivariant, so \(U^R\) is again a solution.

Let \(A\in\mathfrak{so}(3)\) be skew-symmetric and set

\[
R_\varepsilon=e^{\varepsilon A}.
\]

Differentiation at \(\varepsilon=0\) yields

\[
\boxed{
Z_A
=A\,U-(Ay)\cdot\nabla U.
}
\]

There is no factor \(e^{\gamma\theta}\). Hence \(Z_A\) solves the linearized equation as an exact symmetry tangent with formal exponent zero.

On a compact recurrent corridor whose topology controls the required first derivative, if \(Z_A\not\equiv0\) at one recurrent state then recurrence gives a sequence \(\theta_n\to\infty\) for which

\[
Z_A(\theta_n)\to Z_A(0).
\]

Uniform compact bounds prevent exponential growth, while the recurrent return prevents exponential decay to zero. Thus the corresponding Lyapunov exponent is exactly zero.

Let

\[
G_U
:=
\{R\in SO(3):R\cdot U=U\}
\]

be the rotational stabilizer. The dimension of the rotation-generated neutral orbit is

\[
\boxed{
d_{rot}=3-\dim G_U.
}
\]

For a generic trajectory with trivial continuous rotational stabilizer,

\[
\boxed{d_{rot}=3.}
\]

Therefore a nonstationary generic recurrent trajectory has at least

\[
\boxed{1+d_{rot}=4}
\]

symmetry-generated center directions before any genuinely dynamical center is counted.

## 5. Fixed-center physical translations are unstable, not center

Translate the physical solution by a constant vector \(a\):

\[
u_a(x,t)=u(x-a,t).
\]

Relative to the same fixed similarity center,

\[
U_a(y,\theta)
=U(y-ae^{\theta/2},\theta).
\]

Differentiating at \(a=0\),

\[
\boxed{
Z_a(\theta)
=-e^{\theta/2}(a\cdot\nabla)U(\theta).
}
\]

Thus the symmetry carries the explicit factor

\[
\boxed{e^{+\theta/2}.}
\]

In the fixed-center similarity gauge its characteristic exponent is

\[
\boxed{+\frac12.}
\]

This is the familiar center-location instability and is not a zero-center direction.

It also clarifies why center-fixing in the singularity selection is a genuine gauge condition rather than a neutral quotient.

## 6. Galilean boosts are stable with exponent -1/2

The Galilean transform is

\[
u_c(x,t)=u(x-ct,t)+c.
\]

Since \(t=-e^{-\theta}\),

\[
\frac{x-ct}{\sqrt{-t}}
=y+ce^{-\theta/2}.
\]

Therefore

\[
U_c(y,\theta)
=U(y+ce^{-\theta/2},\theta)
+ce^{-\theta/2}.
\]

Differentiating at \(c=0\) gives

\[
\boxed{
Z_c(\theta)
=e^{-\theta/2}
\left[(c\cdot\nabla)U+c\right].
}
\]

Hence the Galilean symmetry has exponent

\[
\boxed{-\frac12.}
\]

and belongs to the stable, not center, spectrum.

## 7. Symmetry exponent dictionary

For the fixed singular-time/fixed-center similarity gauge:

\[
\boxed{
\begin{array}{c|c}
\text{symmetry direction} & \text{similarity exponent}\\
\hline
\text{time shift / physical scaling} & 0\\
\text{spatial rotation} & 0\\
\text{physical translation of center} & +1/2\\
\text{Galilean boost} & -1/2
\end{array}
}
\]

The time/scaling row is one direction, not two independent ones.

Discrete reflections create no infinitesimal center dimension.

A physical time translation changes the chosen terminal singular time and is outside the fixed-terminal-time gauge; it must not be silently counted as an internal center mode.

## 8. Correction to the M19-067 target

The statement

\[
\text{``the zero center is only }\partial_\theta U\text{''}
\]

is false before rotational symmetry is removed.

The correct target is

\[
\boxed{
E^c_{sym}(Y)
=
\operatorname{span}
\left\{
\partial_\theta U,
\;Z_A:A\in\mathfrak{so}(3)
\right\}
}
\]

modulo linear dependence from the stabilizer, followed by

\[
\boxed{
E^c(Y)=E^c_{sym}(Y)
\quad ?
}
\]

That is, every zero exponent should be symmetry-generated and no additional dynamically generated center should remain.

This is strictly weaker and more accurate than a one-dimensional center theorem.

## 9. What is certified

M19-075 certifies:

1. physical scaling and similarity-time translation give the same tangent direction;
2. rotations generate exact zero linearized modes;
3. center translations of the physical singularity carry exponent \(+1/2\) in fixed-center similarity variables;
4. Galilean boosts carry exponent \(-1/2\);
5. the active center-rigidity theorem must be formulated modulo the compact rotation group.

## 10. What is not certified

M19-075 does not prove:

1. that symmetry-generated center directions exhaust the full cocycle center;
2. transverse contraction after quotienting rotations;
3. absence of relative periodic/rotating recurrent solutions;
4. absence of aperiodic weak-critical scattering;
5. global regularity.

## 11. Next target

Because time quotienting destroys the q-translation information but rotational quotienting acts only on angular variables, the next calculation should ask whether

\[
\boxed{
\mathcal H/SO(3)
}

is a safe quotient for the scattering factor.

The necessary covariance is expected to be

\[
\mathscr S(R\cdot Y)(q,\omega)
=
R\,A_Y(q,R^{-1}\omega),
\]

and this action should commute with q-translation.

If so, rotational neutral modes can be removed without erasing the analytic obstruction that M19 is trying to close.

---

\[
\boxed{\text{M19-075 COMPLETE.}}
\]
