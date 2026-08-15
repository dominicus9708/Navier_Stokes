# Flux-retaining precursor persistence obstruction

Date: 2026-08-15

Status: **DERIVED FROM DIVERGENCE-FREE VORTICITY + THE PREVIOUS FIRST-HITTING `L^infinity` CAP. A MATERIAL-FLUX-RETAINING PRECURSOR FOR AN `O(R^2)` COHERENT TERMINAL/CROSSING FLUX CANNOT BE A SHORT `q`-COMPRESSED PANCAKE. UNLESS IT DEVELOPS OPPOSITE POLARITY OR OFF-AXIS SIDE LEAKAGE, ITS ORIENTED FLUX MUST PERSIST FOR AXIAL LENGTH AT LEAST `R sqrt(q)` AT THE PREVIOUS CHECKPOINT. GLOBAL REGULARITY NOT PROVED.**

## 1. Current coherent flux and previous cap

At the coherent crossing, take a robust cross-section with

\[
\boxed{\Phi_c\ge\kappa R^2}
\]

and current cross-sectional area

\[
A_c\asymp R^2.
\]

Trace the material flux backward to the previous first-hitting checkpoint, and work on the flux-retention lane:

\[
\boxed{\Phi_-\ge c\Phi_c\ge c\kappa R^2.}
\]

The previous normalized vorticity cap is

\[
\boxed{\|\Omega_-\|_\infty\le q^{-1}.}
\]

Therefore every previous cross-section carrying this signed flux must have area

\[
\boxed{
A_-\ge q\Phi_-\gtrsim qR^2.
}
\]

A comparable disk radius is thus

\[
\boxed{
\rho_-\gtrsim \sqrt q\,R.
}
\]

## 2. Pointwise side-flux ceiling

Fix the coherent previous axis `e` on a straight cylindrical comparison region of radius `rho_-`. Let

\[
\Phi(s)
=\int_{D_{\rho_-}(s)}\Omega_-\cdot e\,dA.
\]

Because

\[
\nabla\cdot\Omega_-=0,
\]

the change in axial flux between two cross-sections separated by length `L` equals minus the lateral side flux:

\[
\Phi(s+L)-\Phi(s)
=-\int_{\Sigma_{\rho_-}}\Omega_{-,\perp}\cdot\nu_\perp dS.
\]

The pointwise first-hitting cap gives

\[
|\Omega_{-,\perp}|\le q^{-1}.
\]

The lateral area is

\[
|\Sigma_{\rho_-}|=2\pi\rho_-L.
\]

Hence

\[
\boxed{
|\Phi(s+L)-\Phi(s)|
\le
\frac{2\pi\rho_-L}{q}.
}
\]

This is stronger than an `L2` side-leakage estimate because it uses the previous checkpoint maximum-vorticity cap directly.

## 3. Minimum axial termination length

Suppose a fixed fraction of the retained flux is lost over length `L`, say

\[
|\Phi(s+L)-\Phi(s)|
\ge\eta\Phi_-
\gtrsim R^2.
\]

Then

\[
R^2
\lesssim
\frac{\rho_-L}{q}.
\]

Using

\[
\rho_-\asymp\sqrt q\,R
\]

at the minimal-area scale gives

\[
\boxed{
L
\gtrsim
R\sqrt q.
}
\]

If the actual previous cross-section is even larger, this estimate changes in the obvious radius-dependent form

\[
L\gtrsim qR^2/\rho_-,
\]

while the enlarged transverse support is itself stronger spatial non-tightness.

Thus a minimally sized flux-retaining precursor cannot terminate in an axial distance comparable to `R`, much less in the naive volume-preserving pancake thickness `R/q`.

## 4. Why the naive compact pancake is impossible

A heuristic homogeneous axial stretch by factor `q` would map a current `R x R x R` core backward to transverse dimensions `sqrt(q)R` and axial thickness `R/q`.

But at the previous vorticity cap `1/q`, a flux `~R^2` through that transverse area cannot turn out through the lateral boundary of a cylinder of length `R/q`:

\[
\text{maximum side flux}
\lesssim
\frac1q
(\sqrt q R)(R/q)
=
R^2q^{-3/2}
\ll R^2.
\]

Hence the vorticity lines cannot simply end inside the volume-preserving precursor slab.

They must instead

1. continue axially far beyond that material slab;
2. bend/leave the selected constant axis through substantial off-axis geometry;
3. undergo radial opposite-polarity cancellation;
4. or rely on viscous material-flux change, which is already the derivative/palinstrophy lane.

## 5. Long-persistence alternative

If the signed flux remains `~R^2` for axial length

\[
L\gtrsim R\sqrt q,
\]

then the previous precursor is spatially non-tight relative to both

- the current coherent radius `R`;
- the previous natural first-hitting scale `sqrt(q)`.

Indeed its transverse radius is `~sqrt(q)R` and its required axial persistence length is also `~sqrt(q)R`.

Thus its coherent flux support occupies a characteristic linear scale

\[
\boxed{
R\sqrt q,
}
\]

which is a factor `R->infinity` larger than the ordinary previous natural scale `sqrt(q)`.

This is a genuine scale-space precursor-reservoir branch, not a local adjacent-scale inheritance.

## 6. Minimal enstrophy occupancy of the long precursor

On each previous cross-section,

\[
\int_{D_{\rho_-}}|\Omega_-|^2dA
\ge
\frac{\Phi_-^2}{A_-}.
\]

At the minimal area `A_-~qR^2`,

\[
\int_{D_{\rho_-}}|\Omega_-|^2dA
\gtrsim
\frac{R^2}{q}.
\]

Persistence over

\[
L\gtrsim R\sqrt q
\]

therefore gives

\[
\boxed{
E_{\rm tube,-}
\gtrsim
\frac{R^3}{\sqrt q}.
}
\]

This occupancy bound is not by itself contradictory with the previous-checkpoint logistic enstrophy ceiling, but it quantifies the reservoir that the local contraction mechanism requires.

## 7. Radial-polarity and off-axis alternatives

If robust same-sign flux does not persist across the required transverse radial band, cancellation of the inner flux requires an opposite-polarity axial population.

If axial flux terminates by bending rather than polarity cancellation, the divergence-free cylinder identity forces off-axis side leakage.

These are exactly the existing

\[
\boxed{
\text{polarity/projective defect}
\quad\text{or}\quad
\text{off-axis/derivative geometry}
}
\]

channels.

At the critical crossing, repeated projective/high-Hermite regeneration has already been reduced to derivative-radius collapse or material deformation.

## 8. Consequence for Branch 3

The flux-retaining `q`-area-contraction mechanism cannot be a purely local compact deformation from one natural first-hitting scale to the next.

It requires

\[
\boxed{
\text{a precursor flux reservoir at scale }R\sqrt q
}
\]

or one of the already charged off-axis/polarity/viscous derivative alternatives.

Since `R->infinity`, the required reservoir lies increasingly far beyond the previous natural scale.

The remaining task is to show that repeated import from this super-natural precursor scale either violates the fixed-time/multiscale packing ledgers or requires the same critical strain/transport action already identified in Branch 3.

Status: **COMPACT PANCAKE PRECURSOR EXCLUDED / FLUX-RETENTION REQUIRES SUPERNATURAL `R sqrt(q)` RESERVOIR OR PROJECTIVE/POLARITY/DERIVATIVE ESCAPE / GLOBAL REGULARITY NOT PROVED.**
