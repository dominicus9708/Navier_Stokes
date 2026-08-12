# Mean-flow moving sphere as the primary proof observation track

Date: 2026-08-12

Status: **ROUTE SIMPLIFICATION / DERIVED FRAME BRIDGE + EXTERNAL PRESSURE-FREE EPSILON-REGULARITY ANCHOR**.

## 1. Separate the two moving objects

Two different moving local objects are now retained for different jobs.

### A. Deforming material cell

\[
\Omega_\ell^{\rm mat}(t)=\Phi_t(B_\ell(a)).
\]

Purpose:

- follow the same fluid particles;
- record strain, axis deformation, compression/extension, vorticity alignment;
- study DSD structural lineage.

It is physically/materially natural but geometrically inconvenient for direct application of fixed-cylinder epsilon-regularity theorems.

### B. Rigid mean-flow observation sphere

Choose the sphere center by

\[
\boxed{
\dot X_\ell(t)
=
\fint_{B_\ell(X_\ell(t))}u(x,t)dx.
}
\]

The sphere

\[
B_\ell(X_\ell(t))
\]

keeps exactly the same radius and spherical shape.

Purpose:

- remove coherent local translation;
- retain a fixed ball after changing coordinates;
- connect directly to local parabolic regularity scales.

This becomes the preferred **proof observation track**.

## 2. Mean-flow frame

Set

\[
y=x-X_\ell(t),
\]

and

\[
v(y,t)=u(y+X_\ell(t),t)-\dot X_\ell(t).
\]

By the center ODE,

\[
\boxed{
\fint_{B_\ell(0)}v(y,t)dy=0
}
\]

at every time.

With the pressure correction

\[
q(y,t)=p(y+X_\ell(t),t)+\ddot X_\ell(t)\cdot y,
\]

the smooth Navier--Stokes equation preserves its usual form in the moving coordinates.

Thus the local mean motion is a frame variable rather than an internal deformation channel.

## 3. Sphere oscillation channels

Define

\[
C_{\rm sph}(\ell,t)
=
\ell^{-1}
\int_{B_\ell(X_\ell(t))}
|u-\bar u_{B_\ell}|^2dx,
\]

\[
E_{\rm sph}(\ell,t)
=
\ell
\int_{B_\ell(X_\ell(t))}
|\nabla u|^2dx.
\]

In the moving frame these are simply the mean-zero `L^2` oscillation and local gradient-energy channels on the fixed ball `B_ell(0)`.

Poincare--Sobolev and interpolation give

\[
\boxed{
\int_{B_\ell(X_\ell(t))}
|u-\bar u_{B_\ell}|^3dx
\le
C
\left(C_{\rm sph}E_{\rm sph}\right)^{3/4}.
}
\]

No deformation gradient `F` appears.

## 4. Parabolic channel

For a time window of length `ell^2`, define

\[
A_{3,{\rm sph}}
=
\ell^{-2}
\int_{t_0}^{t_0+\ell^2}
\int_{B_\ell(X_\ell(t))}
|u-\bar u_{B_\ell}|^3dxdt.
\]

and

\[
\mathfrak E_{\rm sph}
=
\ell^{-2}
\int_{t_0}^{t_0+\ell^2}
E_{\rm sph}(t)dt.
\]

Then

\[
\boxed{
A_{3,{\rm sph}}
\le
C
\left[
\left(\sup_t C_{\rm sph}(t)\right)
\mathfrak E_{\rm sph}
\right]^{3/4}.
}
\]

All displayed quantities are compatible with the Navier--Stokes critical parabolic scaling.

## 5. Pressure-free epsilon-regularity target

A one-scale epsilon-regularity theorem of Wang, Wu, and Zhou proves that for every `delta>0`, sufficiently small

\[
\iint_{Q(1)}|u|^{5/2+\delta}dxdt
\]

alone implies boundedness in a smaller cylinder for suitable weak solutions.

Taking

\[
\delta=\frac12
\]

gives a pressure-free `L^3` one-scale target.

This is especially useful here because an accelerating translation changes pressure by a linear spatial term.  A pressure-free smallness criterion avoids having to include that frame-induced pressure term in the smallness condition.

Therefore the preferred proof target becomes:

\[
\boxed{
A_{3,{\rm sph}}<\varepsilon_*
}
\]

at every candidate singular location/scale, after the appropriate moving-frame/suitable-solution bridge is justified.

## 6. What this eliminates

The direct regularity route no longer requires all of the following as primary proof variables:

- the material deformation gradient `F`;
- `F^{-T}` boundary amplification;
- a near/far pressure estimate as part of the epsilon smallness gate;
- a moving-path coverage correction.

These remain valuable diagnostics for understanding **why** oscillation might grow, but they are not necessary in the final regularity gate if the pressure-free `L^3` theorem can be invoked in the moving frame.

## 7. Remaining hard step

The unresolved problem is now sharper:

\[
\boxed{
\text{Can one prove }
\left(\sup_t C_{\rm sph}\right)
\mathfrak E_{\rm sph}
\text{ becomes uniformly small on a sufficiently small moving sphere around every candidate singular point?}
}
\]

Poincare alone only gives

\[
C_{\rm sph}\le C E_{\rm sph},
\]

so no new global-regularity result follows yet.

A genuine proof must use the DSD-resolved dynamics--pressure redistribution, strain/alignment, channel cross-coupling, and/or multiscale transport--to force the product below the epsilon threshold without assuming regularity.

## 8. Weak/suitable formulation bridge

For smooth solutions, the accelerating-frame covariance is exact.  The pressure-free theorem, however, is stated for suitable weak solutions on fixed parabolic cylinders.

Before the route can be called rigorous, one must prove that the time-dependent translational change of variables, with its linear pressure correction, preserves the required suitable/local-energy formulation on the window under consideration, or replace it with an equivalent argument that remains inside the published theorem's hypotheses.

Status: **OPEN BRIDGE LEMMA**.
