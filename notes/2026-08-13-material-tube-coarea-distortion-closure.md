# Material-tube coarea closure up to Lagrangian distortion

Date: 2026-08-13

Status: **DERIVED DISTORTION-AWARE BULK PALINSTROPHY LEMMA / OPEN STRAIN-PALINSTROPHY UNIFORM CLOSURE**.

This note closes the codimension gap left by the material vorticity-flux erosion identity, under a robust nested-family hypothesis.

The remaining price is an explicit Lagrangian deformation factor.

---

## 1. Restarted material coordinates

Restart the flow map at time `t_1`:

\[
X(a,t_1)=a,
\qquad
\partial_tX(a,t)=u(X(a,t),t).
\]

Let

\[
F(a,t)=D_aX(a,t).
\]

For incompressible flow,

\[
\boxed{
\det F(a,t)=1.
}
\]

Take an initial straight cylindrical coordinate system

\[
a=s n+\rho e_\rho(\theta),
\]

with

\[
0<s<H,
\qquad
r<\rho<2r.
\]

For each pair `(rho,s)`, let

\[
S_{\rho,s}(t)
\]

be the material image of the initial disk of radius `rho` at axial label `s`, and let

\[
\Gamma_{\rho,s}(t)=\partial S_{\rho,s}(t).
\]

---

## 2. Robust material-flux erosion hypothesis

Let

\[
\Phi_{\rho,s}(t)
=\int_{S_{\rho,s}(t)}\omega\cdot n_{\rho,s}(t)dA.
\]

Assume that every member of the nested radial/axial family loses at least

\[
\Delta\Phi_0>0
\]

over the time interval

\[
I=[t_1,t_2],
\qquad
\tau=t_2-t_1:
\]

\[
\boxed{
|\Phi_{\rho,s}(t_2)-\Phi_{\rho,s}(t_1)|
\ge\Delta\Phi_0
}
\]

for all

\[
r\le\rho\le2r,
\qquad
0\le s\le H.
\]

The material-flux identity gives

\[
\Delta\Phi_{\rho,s}
=-\nu
\int_I
\oint_{\Gamma_{\rho,s}(t)}
(\nabla\times\omega)\cdot d\ell\,dt.
\]

---

## 3. Loop-length distortion

Define

\[
\boxed{
M_F
=\sup_{a\in A_0,\ t\in I}
\|F(a,t)\|_{\rm op},
}
\]

where `A_0` is the initial annular tube.

The initial azimuthal tangent has physical length element

\[
d\ell
=
\rho|F e_\theta|d\theta.
\]

Therefore

\[
\ell_{\rho,s}(t)
\le
2\pi\rho M_F
\le
4\pi rM_F.
\]

The time-integrated boundary estimate from the previous note yields

\[
\begin{aligned}
\Delta\Phi_0^2
&\le
\nu^2
\left(
\int_I\ell_{\rho,s}(t)dt
\right)
\left(
\int_I
\oint_{\Gamma_{\rho,s}(t)}
|\nabla\times\omega|^2d\ell dt
\right)\\
&\le
4\pi\nu^2rM_F\tau
\left(
\int_I
\oint_{\Gamma_{\rho,s}(t)}
|\nabla\times\omega|^2d\ell dt
\right).
\end{aligned}
\]

Hence every nested loop satisfies

\[
\boxed{
\int_I
\oint_{\Gamma_{\rho,s}(t)}
|\nabla\times\omega|^2d\ell dt
\ge
\frac{\Delta\Phi_0^2}
{4\pi\nu^2rM_F\tau}.
}
\]

---

## 4. Lagrangian coarea identity

Integrate the boundary quantity over the initial labels `rho` and `s`.

Because

\[
da=\rho\,d\theta d\rho ds
\]

and `det F=1`,

\[
\begin{aligned}
&\int_0^Hds
\int_r^{2r}d\rho
\oint_{\Gamma_{\rho,s}(t)}
|\nabla\times\omega|^2d\ell\\
&=
\int_{A_0}
|\nabla\times\omega(X(a,t),t)|^2
|F(a,t)e_\theta|da\\
&\le
M_F
\int_{A(t)}
|\nabla\times\omega(x,t)|^2dx,
\end{aligned}
\]

where

\[
A(t)=X(A_0,t).
\]

Integrating in time and combining with the lower bound for every loop gives

\[
M_F
\int_I\int_{A(t)}
|\nabla\times\omega|^2dxdt
\ge
Hr
\frac{\Delta\Phi_0^2}
{4\pi\nu^2rM_F\tau}.
\]

Thus

\[
\boxed{
\int_I\int_{A(t)}
|\nabla\times\omega|^2dxdt
\ge
\frac{H\Delta\Phi_0^2}
{4\pi\nu^2M_F^2\tau}.
}
\]

Since

\[
|\nabla\times\omega|^2
\le2|\nabla\omega|^2,
\]

we obtain the bulk palinstrophy estimate

\[
\boxed{
\int_I\int_{A(t)}
|\nabla\omega|^2dxdt
\ge
\frac{H\Delta\Phi_0^2}
{8\pi\nu^2M_F^2\tau}.
}
\]

This is the desired codimension-lifting estimate.

---

## 5. Natural-scale form

Set

\[
r=aW^{-1/2},
\qquad
H=\beta r,
\qquad
\tau=\lambda W^{-1},
\]

and suppose every nested material disk loses a fixed fraction of a natural-scale flux,

\[
\Delta\Phi_0
\ge
\eta\kappa Wr^2.
\]

Then

\[
\boxed{
\int_I\int_{A(t)}
|\nabla\omega|^2dxdt
\ge
\frac{
\beta\eta^2\kappa^2a^5
}{
8\pi\nu^2\lambda M_F^2
}
W^{1/2}.
}
\]

Thus order-one material flux erosion over one natural time and one natural tube costs the critical integrated-palinstrophy scale `W^(1/2)`, modulo the square of the Lagrangian stretch factor.

---

## 6. Deformation is itself a strain channel

The flow gradient satisfies

\[
\dot F=(\nabla u)(X,t)F.
\]

For any material vector `v`,

\[
\frac d{dt}|Fv|^2
=2(Fv)^TS(Fv).
\]

Therefore

\[
\frac d{dt}\log|Fv|
\le
\|S(t)\|_{L^\infty},
\]

and, because the restarted map has `F(t_1)=I`,

\[
\boxed{
M_F
\le
\exp\left(
\int_I\|S(t)\|_\infty dt
\right).
}
\]

Consequently, for any chosen threshold `K>1`, one has the exact branch:

### Geometry-controlled branch

If

\[
M_F\le K,
\]

then robust natural-time material-flux erosion forces

\[
\boxed{
\int_I\int_{A(t)}|\nabla\omega|^2
\gtrsim
K^{-2}W^{1/2}.
}
\]

### Large-deformation branch

If

\[
M_F>K,
\]

then necessarily

\[
\boxed{
\int_I\|S(t)\|_\infty dt
>\log K.
}
\]

Thus geometric distortion cannot remove the cost; it only moves the burden from palinstrophy into the strain/deformation channel.

---

## 7. Relation to the Lagrangian diffusion metric

The existing material-coordinate metric is

\[
A=F^{-1}F^{-T}.
\]

Its smallest eigenvalue is

\[
\lambda_{\min}(A)
=\|F\|_{\rm op}^{-2}
\]

pointwise.

Hence the factor `M_F^{-2}` is exactly the worst material diffusion-metric eigenvalue over the tube/time window.

The same deformation that weakens the bulk palinstrophy lower bound is therefore the deformation that creates a weak material-coordinate diffusion direction.

This matches the existing Lagrangian diffusion-metric gate rather than introducing a new independent variable.

---

## 8. Residual-class update

The temporal oriented-flux erosion branch has now been reduced to

\[
\boxed{
\text{critical bulk palinstrophy}
\quad\text{or}\quad
\text{large strain-driven material deformation}.
}
\]

Together with the spatial oriented-flux trichotomy, the sign-resolved projective branch no longer has a free leakage/erosion mechanism.

The unresolved issue is uniform closure across repeated natural windows: a hypothetical singular cascade could in principle alternate between

- palinstrophy-heavy erosion windows;
- deformation-heavy windows;
- shrinking but persistent oriented tubes;
- and the previously active projective/strain derivative branches.

---

## 9. Principal next target

Construct a single cumulative functional that charges both sides of the dichotomy, for example a window cost built from

\[
\boxed{
\nu^2\int_I\int|\nabla\omega|^2
\quad\text{and}\quad
\int_I\|S\|_\infty dt,
}
\]

and determine whether repeated order-one material-flux loss on arbitrarily late natural windows has a finite global budget.

No such global cumulative bound is established here.

Status: **OPEN REPEATED-WINDOW STRAIN/PALINSTROPHY BUDGET**.
