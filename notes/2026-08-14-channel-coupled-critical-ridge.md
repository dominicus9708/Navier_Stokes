# Channel-coupled critical ridge: peak height, vorticity share, scale, and pulse duration

Date: 2026-08-14

Status: **DERIVED NECESSARY COUPLED CONDITIONS FOR A SURVIVING BOUNDED-AFFINE RESIDUAL CASCADE / GLOBAL REGULARITY NOT PROVED**.

The previous calculations produced two independent constraints on a residual-dominant first-hitting step:

1. finite physical dissipation excludes a repeatedly very-low residual plateau;
2. finite kinetic energy plus Hermite interpolation forces a low-curvature residual to obey `B R^5 <= C W^(1/2)`.

This note adds the exact vorticity-share dependence of the residual Duhamel source.  The result collapses the surviving low-curvature branch to a coupled amplitude/scale/channel/duration corridor.

---

## 1. Sharpen the mean-vorticity cancellation bound

Let

\[
B=\mathcal B_\gamma
=V_S+\frac12V_\omega,
\]

where

\[
V_\omega
=\int\gamma|\Omega-\bar\Omega|^2.
\]

For the residual velocity `r`,

\[
\int\gamma r=0,
\qquad
\int\gamma\nabla r=0,
\qquad
\nabla\cdot r=0,
\]

and

\[
\int\gamma|\nabla r|^2=B.
\]

The nonlinear residual vorticity source is

\[
f_r
=(\Omega\cdot\nabla)r-(r\cdot\nabla)\Omega.
\]

Write

\[
\delta\Omega=\Omega-\bar\Omega.
\]

The mean-vorticity terms cancel exactly:

\[
\boxed{
\int\gamma f_r
=
\int\gamma(\delta\Omega\cdot\nabla)r
+
\int\gamma\delta\Omega\,
(r\cdot\nabla\log\gamma).
}
\]

The first term obeys

\[
\left|
\int\gamma(\delta\Omega\cdot\nabla)r
\right|
\le
\sqrt{V_\omega B}.
\]

On a bounded-condition Gaussian, the creation/annihilation estimate gives

\[
\|r\cdot\nabla\log\gamma\|_{L^2(\gamma)}
\le C_K\sqrt B.
\]

Therefore

\[
\boxed{
\left|
\int\gamma f_r
\right|
\le
C_K\sqrt{V_\omega B}.
}
\]

This is sharper than the previously retained bound `<= C_K B`.

---

## 2. Vorticity-share variable

Whenever `B>0`, define

\[
\boxed{
\theta
:=\frac{V_\omega}{B}.
}
\]

Because

\[
B=V_S+\frac12V_\omega,
\]

one has

\[
0\le\theta\le2.
\]

The source bound becomes

\[
\boxed{
\left|
\int\gamma f_r
\right|
\le
C_K\sqrt\theta\,B.
}
\]

Thus a strain-dominated residual with `theta << 1` is inefficient at producing endpoint vorticity.

---

## 3. Source requirement forces more residual mass when the vorticity share is small

Suppose a residual-dominant endpoint contribution has fixed size

\[
\mathfrak R_\gamma\ge\rho>0.
\]

On the responsible interval `I`, assume

\[
\theta(s)\le\Theta.
\]

The bounded-affine Duhamel factors are uniformly controlled, so

\[
\rho
\le
C_K\int_I\sqrt{\theta(s)}B(s)ds
\le
C_K\sqrt\Theta\int_I B(s)ds.
\]

Hence

\[
\boxed{
\int_I B(s)ds
\ge
c_{K,\rho}\Theta^{-1/2}.
}
\]

---

## 4. Insert into the residual-peak dissipation rearrangement

Let

\[
m=\sup_I B.
\]

The Gaussian-volume rearrangement lemma gives, for residual mass `M_B=int_I B ds`,

\[
\int_I\|\nabla U\|_2^2ds
\ge
c_K M_B^{5/2}m^{-3/2}.
\]

Using the source requirement,

\[
\boxed{
\int_I\|\nabla U\|_2^2ds
\ge
c_{K,\rho}
\Theta^{-5/4}m^{-3/2}.
}
\]

Returning to physical variables at terminal level `W`,

\[
\boxed{
D_{\rm phys}(I)
\ge
c_{K,\rho}
W^{-1/2}
\Theta^{-5/4}
m^{-3/2}.
}
\]

---

## 5. Necessary condition for an infinite disjoint cascade

Consecutive first-hitting intervals can be chosen disjoint in physical time.  Since total physical kinetic-energy dissipation is finite, the per-step lower bound must tend to zero along any surviving infinite cascade.

Therefore necessarily

\[
W^{-1/2}
\Theta^{-5/4}
m^{-3/2}
\to0.
\]

Equivalently,

\[
\boxed{
W^{1/3}m\,\Theta^{5/6}
\to\infty.
}
\]

Define the dimensionless peak surplus above the previously found critical height

\[
\boxed{
\Lambda
:=W^{1/3}m.
}
\]

Then every surviving residual cascade must satisfy

\[
\boxed{
\Lambda\to\infty
}
\]

and, more sharply,

\[
\boxed{
\Lambda\Theta^{5/6}\to\infty.
}
\]

Thus the earlier `m >= c W^(-1/3)` statement improves to a necessary asymptotic separation:

\[
\boxed{
m\gg W^{-1/3}}
\]

up to the vorticity-share factor.

If the source is strongly strain dominated, then

\[
\boxed{
\Theta
\gg
\Lambda^{-6/5}
}
\]

is necessary.

---

## 6. Combine with the finite-energy Hermite ridge

On the low-curvature branch, the Hermite barrier requires

\[
mR^5
\lesssim
W^{1/2}.
\]

Insert

\[
m=W^{-1/3}\Lambda.
\]

Then

\[
R^5
\lesssim
W^{5/6}\Lambda^{-1},
\]

so

\[
\boxed{
R
\lesssim
W^{1/6}\Lambda^{-1/5}.
}
\]

Because `Lambda -> infinity`, a surviving low-curvature residual peak cannot sit asymptotically at the old `W^(1/6)` ceiling.  Its active scale must separate downward from that ceiling:

\[
\boxed{
\frac{R}{W^{1/6}}
\to0
}
\]

along the low-curvature branch.

At the same time the non-affine regime still requires

\[
R\gg W^{1/10}.
\]

Thus the surviving corridor is

\[
\boxed{
W^{1/10}
\ll R
\lesssim
W^{1/6}\Lambda^{-1/5},
\qquad
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty.
}
\]

---

## 7. Pulse-duration lower bound

The source requirement and `B<=m`, `theta<=Theta` give

\[
\rho
\le
C_K\sqrt\Theta\,m\,|I|.
\]

Therefore the normalized pulse duration satisfies

\[
\boxed{
|I|
\ge
c_{K,\rho}
\frac{1}{m\sqrt\Theta}
}
\]

or

\[
\boxed{
|I|
\gtrsim
W^{1/3}
\Lambda^{-1}
\Theta^{-1/2}.
}
\]

The Gaussian covariance age corresponding to scale `R` is

\[
\tau_R\asymp R^2.
\]

Using the maximal low-curvature scale above,

\[
\tau_R
\lesssim
W^{1/3}\Lambda^{-2/5}.
\]

Hence

\[
\boxed{
\frac{|I|}{\tau_R}
\gtrsim
\Lambda^{-3/5}
\Theta^{-1/2}.
}
\]

This produces a new duration/channel dichotomy.

### Small-vorticity-share edge

If

\[
\Theta
\sim
\Lambda^{-6/5},
\]

then

\[
\frac{|I|}{\tau_R}
\gtrsim O(1).
\]

A strongly strain-dominated residual must therefore persist for a time comparable to the Gaussian covariance/diffusive scale.

### Larger vorticity share

If

\[
\Theta\Lambda^{6/5}\to\infty,
\]

the pulse may be shorter than the covariance age, but it necessarily carries a stronger vorticity-fluctuation channel.

Thus the surviving route is forced toward either

\[
\boxed{
\text{long scale-comparable strain-dominated pulse}
}
\]

or

\[
\boxed{
\text{shorter but vorticity-active pulse}.
}
\]

---

## 8. Relation to the old critical endpoint

The previous two independent estimates met at

\[
R\sim W^{1/6},
\qquad
m\sim W^{-1/3}.
\]

The present finite-dissipation argument shows that an infinite cascade cannot remain at that exact endpoint with fixed constants: it would pay an order-one physical dissipation cost at every disjoint first-hitting step.

Therefore a surviving cascade must move away from the endpoint in the coupled direction

\[
\boxed{
\Lambda=W^{1/3}m\to\infty,
\qquad
R/W^{1/6}\lesssim\Lambda^{-1/5}\to0.
}
\]

This is a genuine narrowing of the critical wall rather than merely a reparameterization.

---

## 9. Current frontier

The bounded-affine low-curvature residual branch is now constrained by all of

\[
\boxed{
\begin{aligned}
&m=W^{-1/3}\Lambda,
\qquad \Lambda\to\infty,\\
&W^{1/10}\ll R
\lesssim W^{1/6}\Lambda^{-1/5},\\
&\Lambda\Theta^{5/6}\to\infty,\\
&|I|\gtrsim
W^{1/3}\Lambda^{-1}\Theta^{-1/2}.
\end{aligned}
}
\]

The next useful target is to close one of the two duration/channel branches:

1. use Gaussian coercivity and scale evolution against a pulse with `|I| comparable to R^2`;
2. use vorticity projective/axis geometry against a pulse with non-negligible `theta`.

Status: **STRAIN-ONLY ENDPOINT RESIDUAL ROUTE TYPED AS INEFFICIENT / SURVIVING LOW-CURVATURE CASCADE COLLAPSED TO A COUPLED `Lambda-Theta-R-duration` CORRIDOR**.
