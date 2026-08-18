# Signed-tube termination versus projective charge and L3 extension

Date: 2026-08-19

Status: **DIVERGENCE-FREE SPATIAL UNCERTAINTY LEMMA FOR A SIGNED COHERENT TUBE. SHORT AXIAL TERMINATION FORCES TRANSVERSE/PROJECTIVE VORTICITY ENERGY; LONG SIGNED CIRCULATION EXTENSION FORCES ENDPOINT-CRITICAL L3 OCCUPANCY. GLOBAL REGULARITY NOT PROVED.**

## 1. Geometry

Fix a unit axis `e` and decompose

\[
\omega=a e+b,
\qquad b\perp e.
\]

Let the physical tube radius be `r`. Choose a smooth cross-sectional cutoff `phi_r(x_perp)` satisfying

- `phi_r=1` on the inner core;
- support in a fixed-ratio `O(r)` disk;
- `|grad_perp phi_r| <= C/r`.

Define the signed axial flux observable

\[
F(z)=\int_{\mathbb R^2}\phi_r(x_\perp)a(x_\perp,z)dx_\perp.
\]

Assume `F` changes by a fixed fraction of a flux amplitude `Gamma>0` over an axial distance at most `L`.

## 2. Divergence-free converts axial termination into transverse vorticity

Because

\[
\nabla\cdot\omega=0,
\]

we have

\[
\partial_e a=-\nabla_\perp\cdot b.
\]

Hence

\[
F'(z)
=\int \phi_r\partial_e a\,dx_\perp
=\int \nabla_\perp\phi_r\cdot b\,dx_\perp.
\]

Since

\[
\|\nabla_\perp\phi_r\|_{L^2(\mathbb R^2)}\lesssim1,
\]

Cauchy-Schwarz yields

\[
|F'(z)|^2
\lesssim
\int_{\operatorname{supp}\nabla\phi_r}|b(x_\perp,z)|^2dx_\perp.
\]

The one-dimensional variation bound gives

\[
\int |F'(z)|^2dz
\ge
\frac{|\Delta F|^2}{L}
\gtrsim
\frac{\Gamma^2}{L}.
\]

Therefore

\[
\boxed{
\int_{\rm tube}|P_{e^\perp}\omega|^2dx
\gtrsim
\frac{\Gamma^2}{L}.
}
\]

Thus a signed coherent tube cannot terminate rapidly in the axial direction while remaining projectively one-axis.

## 3. Long circulation extension forces L3

Suppose the signed circulation remains comparable to `Gamma` along an axial segment of length `L` and through a fixed-ratio transverse annulus `r <= rho <= 2r`.

On each transverse loop `C_rho`,

\[
\left|\oint_{C_\rho}u\cdot d\ell\right|\gtrsim\Gamma.
\]

Hölder on the loop gives

\[
\int_{C_\rho}|u|^3d\ell
\gtrsim
\frac{\Gamma^3}{\rho^2}.
\]

Integrating over `rho in [r,2r]` and along the tube length gives

\[
\boxed{
\int_{\rm annular\ tube}|u|^3dx
\gtrsim
\Gamma^3\frac{L}{r}.
}
\]

This is scale invariant.

## 4. Critical uncertainty product

Multiply the two lower bounds. The natural projective critical charge of the terminating tube is

\[
\mathfrak p_{\rm tube}
:=
r\int_{\rm tube}|P_{e^\perp}\omega|^2dx.
\]

Then

\[
\boxed{
\mathfrak p_{\rm tube}
\left(
\int_{\rm annular\ tube}|u|^3dx
\right)
\gtrsim
\Gamma^5.
}
\]

For the natural compact packet normalization `Gamma~1`,

\[
\boxed{
\mathfrak p_{\rm tube}\,\|u\|_{L^3(\rm annulus)}^3\gtrsim c.
}
\]

Hence

\[
\boxed{
\text{short signed termination}
\Rightarrow
\text{projective critical charge},
}
\]

whereas

\[
\boxed{
\text{small projective charge}
\Rightarrow
\text{long signed extension / L3 cost}.
}
\]

## 5. Relation to the compact genealogy

This lemma replaces part of the previous cutoff-localization discussion by a direct divergence-free geometry statement.

A projectively coherent compact child cannot simply disappear at the edge of its observation cell:

- if its signed flux terminates there, transverse vorticity is generated;
- if it does not terminate, the circulation extends and pays endpoint-critical `L3` occupancy;
- if the axis bends instead of the signed amplitude terminating, the angular/projective channel is activated.

Thus the localization complement of the coherence/Sobolev-gap branch is already contained in the projective/L3 genealogy ledgers.

## 6. Limitation

Both factors are scale-critical and may diverge in a hypothetical singularity. The product lower bound is therefore a structural routing theorem, not a contradiction.

Status: **SIGNED COHERENT TERMINATION PRICED BY PROJECTIVE CHARGE OR L3 EXTENSION / NO FREE LOCAL CUTOFF ESCAPE.**