# Weighted mean-flow sphere and localized energy bridge

Date: 2026-08-12

Status: **DERIVED SMOOTH LOCAL-ENERGY BRIDGE + OPEN SUITABLE-WEAK PASSAGE**.

## 1. Smooth radial observation window

Choose a fixed nonnegative radial cutoff

\[
\phi\in C_c^\infty(B_2(0)),
\]

and scale it by

\[
\phi_\ell(y)=\phi(y/\ell).
\]

Define the moving center by the weighted local mean

\[
\boxed{
\dot X_\ell(t)
=
\frac{
\int \phi_\ell(y)u(X_\ell(t)+y,t)dy
}{
\int\phi_\ell(y)dy
}.
}
\]

Set

\[
v(y,t)=u(X_\ell(t)+y,t)-\dot X_\ell(t).
\]

Then

\[
\boxed{
\int\phi_\ell(y)v(y,t)dy=0.
}
\]

The weighted sphere therefore removes coherent local translation without introducing a hard spatial boundary.

## 2. Accelerating-frame pressure correction cancels in the weighted energy budget

For smooth solutions define

\[
q(y,t)=p(X_\ell(t)+y,t)+\ddot X_\ell(t)\cdot y.
\]

The translated pair satisfies the standard incompressible Navier--Stokes form.

The only place the linear pressure correction enters the localized kinetic-energy balance is

\[
\int
(\ddot X_\ell\cdot y)
\,v\cdot\nabla\phi_\ell\,dy.
\]

Using `div v=0` and integration by parts,

\[
\begin{aligned}
\int
(\ddot X_\ell\cdot y)
\,v\cdot\nabla\phi_\ell\,dy
&=-\int\phi_\ell
\nabla\cdot[(\ddot X_\ell\cdot y)v]dy\\
&=-\ddot X_\ell\cdot\int\phi_\ell vdy\\
&=0.
\end{aligned}
\]

Thus the moving-frame acceleration contributes **no extra localized energy channel** when the frame velocity is chosen by the same weighted mean.

## 3. Dimensionless localized channels

Define

\[
C_\phi
=
\ell^{-1}\int\phi_\ell|v|^2dy,
\]

\[
D_\phi
=
\nu\ell\int\phi_\ell|\nabla v|^2dy,
\]

\[
A_\phi
=
\ell\int\frac{|v|^2}{2}
\,v\cdot\nabla\phi_\ell\,dy,
\]

\[
P_\phi
=
\ell\int p(X_\ell+y,t)
\,v\cdot\nabla\phi_\ell\,dy,
\]

and

\[
B_\phi
=
\frac{\nu\ell}{2}
\int|v|^2\Delta\phi_\ell\,dy.
\]

For a smooth solution the exact weighted energy identity is

\[
\boxed{
\frac{\ell^2}{2}\frac{d}{dt}C_\phi
+D_\phi
=A_\phi+P_\phi+B_\phi.
}
\]

Every displayed channel is invariant under the Navier--Stokes parabolic scaling when the spatial scale is transformed with `ell`.

## 4. Why this replaces the hard-sphere budget in the rigorous bridge

The hard mean-flow sphere remains useful for intuitive shell accounting and deterministic numerical diagnostics.

The weighted sphere is preferable for a theorem-level local-energy bridge because the suitable weak formulation is defined using smooth compactly supported nonnegative test functions.  The radial cutoff already has exactly that structure.

Accordingly the roles are now:

- **hard mean-flow sphere:** geometric/diagnostic visualization and numerical shell budget;
- **weighted mean-flow sphere:** preferred local-energy proof bridge;
- **deforming material cell:** structural lineage, strain, and material-axis diagnostics.

## 5. What is still not automatic

The calculation above is exact for smooth solutions.  A proof of global regularity by contradiction would ultimately need to use suitable weak/local-energy information at a candidate singular time.

The remaining bridge lemma must justify the moving weighted coordinates at that level.  In particular one must control the regularity of the center path and interpret the linear pressure correction distributionally, or formulate the same weighted moving-window inequality directly in the original Eulerian variables without requiring a second time derivative of `X_ell`.

The literature search performed for this project did not identify a ready-made theorem asserting precisely this time-dependent weighted-mean translation invariance for suitable weak solutions.  Therefore it remains an explicit **OPEN BRIDGE LEMMA**, rather than being assumed.

## 6. Preferred next formulation

To avoid unnecessary dependence on `X_ell''`, the next derivation should work directly with a time-dependent test function

\[
\varphi(x,t)
=
\phi\left(\frac{x-X_\ell(t)}{\ell}\right)
\]

inside the original local energy inequality.

Then

\[
\partial_t\varphi
=-\dot X_\ell\cdot\nabla\varphi,
\]

which requires only the first derivative of the path.  Combining this term with the advective flux should reproduce the relative-velocity channel `u-Xdot` directly in Eulerian variables.

If successful, this gives a suitable-weak-compatible moving-window inequality without invoking accelerating coordinates at all.

Status: **NEXT DERIVATION TARGET**.
