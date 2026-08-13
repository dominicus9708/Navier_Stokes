# Material vorticity flux: transport cancellation and viscous erosion

Date: 2026-08-13

Status: **EXACT MATERIAL-FLUX IDENTITY + BOUNDARY DERIVATIVE COST / OPEN BULK PALINSTROPHY GLUING**.

This note continues the oriented-flux persistence branch in time rather than along the axial coordinate.

The point is to distinguish material transport from genuine destruction of signed vorticity flux.

---

## 1. Vorticity equation

For smooth incompressible Navier--Stokes flow,

\[
\partial_t\omega+(u\cdot\nabla)\omega
=(\omega\cdot\nabla)u+\nu\Delta\omega,
\qquad
\nabla\cdot u=0,
\qquad
\nabla\cdot\omega=0.
\]

Equivalently,

\[
\partial_t\omega
=\nabla\times(u\times\omega)+\nu\Delta\omega.
\]

---

## 2. Material-surface flux identity

Let `S(t)` be a smooth orientable material surface transported by the flow map of `u`.

Define

\[
\boxed{
\Phi_S(t)
=\int_{S(t)}\omega\cdot n\,dA.
}
\]

The transport formula for a vector flux through a material surface is

\[
\frac d{dt}
\int_{S(t)}b\cdot n\,dA
=
\int_{S(t)}
\left[
\partial_tb+(u\cdot\nabla)b-(b\cdot\nabla)u
+b\,\nabla\cdot u
\right]\cdot n\,dA.
\]

For `b=omega` and incompressible flow, the transport and stretching terms cancel with the vorticity equation, leaving

\[
\boxed{
\frac{d\Phi_S}{dt}
=
\nu\int_{S(t)}\Delta\omega\cdot n\,dA.
}
\]

Since `div omega=0`,

\[
\Delta\omega
=-\nabla\times(\nabla\times\omega).
\]

Stokes' theorem then gives the boundary form

\[
\boxed{
\frac{d\Phi_S}{dt}
=-\nu
\oint_{\partial S(t)}
(\nabla\times\omega)\cdot d\ell.
}
\]

Thus material advection and vortex stretching do not directly destroy vorticity flux through a material surface.  Flux erosion is a viscous boundary-derivative effect.

---

## 3. Boundary derivative cost

Let

\[
\Gamma(t)=\partial S(t)
\]

and denote its length by

\[
\ell_\Gamma(t).
\]

Cauchy--Schwarz gives

\[
\left|\frac{d\Phi_S}{dt}\right|^2
\le
\nu^2\ell_\Gamma(t)
\oint_{\Gamma(t)}
|\nabla\times\omega|^2d\ell.
\]

Integrating from `t_1` to `t_2`,

\[
\boxed{
|\Phi_S(t_2)-\Phi_S(t_1)|^2
\le
\nu^2
\left(
\int_{t_1}^{t_2}\ell_\Gamma(t)dt
\right)
\left(
\int_{t_1}^{t_2}
\oint_{\Gamma(t)}
|\nabla\times\omega|^2d\ell dt
\right).
}
\]

Therefore order-one material flux loss forces a boundary `curl omega` cost unless the material loop becomes very long.

The loop-length growth is a separate geometry/deformation channel already compatible with the Lagrangian metric track.

---

## 4. Natural-time scaling

Suppose at a dangerous scale

\[
r=aW^{-1/2}
\]

that a material cross-section carries flux

\[
\Phi_0\asymp\kappa W r^2
\]

and loses a fixed fraction `eta` over a natural time

\[
\tau=\lambda W^{-1}.
\]

Assume the material boundary remains of controlled natural length,

\[
\ell_\Gamma(t)
\le
K_\Gamma r
\]

through the interval.

Then

\[
\int_{t_1}^{t_2}\ell_\Gamma(t)dt
\le
K_\Gamma r\tau.
\]

If

\[
|\Delta\Phi_S|
\ge
\eta\kappa W r^2,
\]

the boundary derivative estimate implies

\[
\boxed{
\int_{t_1}^{t_2}
\oint_{\Gamma(t)}
|\nabla\times\omega|^2d\ell dt
\ge
\frac{\eta^2\kappa^2W^2r^4}
{\nu^2K_\Gamma r\tau}.
}
\]

Substituting the natural radius and natural time gives

\[
\boxed{
\int_{t_1}^{t_2}
\oint_{\Gamma(t)}
|\nabla\times\omega|^2d\ell dt
\gtrsim
\frac{\eta^2\kappa^2a^3}
{\nu^2K_\Gamma\lambda}
W^{3/2}.
}
\]

This is the correct scaling for a one-dimensional boundary trace of the vorticity-gradient channel over a natural time.

---

## 5. From boundary trace to bulk palinstrophy

Because

\[
|\nabla\times\omega|^2
\le
2|\nabla\omega|^2
\]

(up to the chosen matrix norm convention), the boundary quantity is a trace of the palinstrophy density.

However a single material loop is codimension two in spacetime and cannot be bounded below by the bulk palinstrophy without an additional geometric/coarea step.

The clean next construction is a nested family of material cross-sections indexed by initial radius and axial position.  If that family remains quantitatively nondegenerate under the flow map, integration over the family should convert the boundary cost into

\[
\int_I\int_{\text{material tube}}|\nabla\omega|^2dxdt
\]

up to a Lagrangian distortion factor.

This conversion is **not** assumed here.

---

## 6. Exact shear-flow benchmark

There is a simple exact Navier--Stokes class that verifies the material-flux formula.

Take

\[
u(x,y,z,t)
=
\bigl(U(y,t),0,0\bigr),
\]

with

\[
U_t=\nu U_{yy}.
\]

For example

\[
U(y,t)=e^{-\nu k^2t}\sin(ky).
\]

Then

\[
\omega
=
\bigl(0,0,-U_y\bigr)
=
\bigl(0,0,-k e^{-\nu k^2t}\cos(ky)\bigr).
\]

A rectangular material patch in the `xy` plane is sheared by the flow but preserves area.  Its vorticity flux changes exactly according to the boundary line integral of `curl omega`; the contributions on the two sheared side curves cancel, while the horizontal edges reproduce `d Phi/dt`.

This benchmark is implemented in the reproducibility audit.

---

## 7. DSD channel interpretation

Temporal oriented-flux change is now typed as

\[
\boxed{
\mathsf T_{\Phi}
=
(
\Phi_S,
\ell_\Gamma/r,
\mathcal B_{\nabla\omega}
),
}
\]

where

- `Phi_S`: material signed vorticity flux;
- `ell_Gamma/r`: boundary deformation/stretch factor;
- `B_gradomega`: boundary vorticity-gradient erosion channel.

Thus the residual branch becomes

\[
\boxed{
\text{flux survives}
\quad\text{or}\quad
\text{boundary stretches strongly}
\quad\text{or}\quad
\text{vorticity-gradient erosion is large}.
}
\]

The first branch returns to the persistence-time budget; the second to the Lagrangian deformation track; the third to the derivative/palinstrophy hierarchy.

---

## 8. Principal open target

Close the codimension gap by constructing a nested material-tube family and proving a distortion-aware coarea estimate of the schematic form

\[
\boxed{
\text{robust material-flux erosion}
\Longrightarrow
\int_I\int_{\rm tube}|\nabla\omega|^2
\gtrsim
\text{critical natural-scale cost}/\mathcal K_{\rm geom}.
}
\]

If the geometry factor `K_geom` becomes large instead, that growth itself must be charged to the already active strain/Lagrangian metric channel.

Status: **OPEN MATERIAL-TUBE COAREA / GEOMETRIC-DISTORTION CLOSURE**.
