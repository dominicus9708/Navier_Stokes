# Branch 2 — spatial non-tightness / shell transport reduced by material-flux closure

Date: 2026-08-15

Status: **SPATIAL NON-TIGHTNESS IS CLOSED AS AN INDEPENDENT CAUSAL BRANCH ON THE COHERENT CRITICAL-CROSSING TRACK. AFTER PASSING TO MATERIAL SURFACES, TRANSLATION/ADVECTION IS NOT A VORTICITY-FLUX SOURCE. PERSISTENCE OR LOSS OF THE COHERENT CORE ROUTES TO DERIVATIVE/PALINSTROPHY CONCENTRATION OR STRAIN-DRIVEN LAGRANGIAN DEFORMATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Critical crossing supplies a macroscopic coherent vorticity core

At the first Gaussian Reynolds-one crossing,

\[
\boxed{
B_cR_c^4=1,
}
\]

and the terminal low-Reynolds action estimate forces

\[
\boxed{
|\bar\Omega_c|\ge c_K>0.
}
\]

Moreover

\[
V_{\omega,c}\le2B_c=2R_c^{-4}.
\]

Let

\[
e=\bar\Omega_c/|\bar\Omega_c|.
\]

For a fixed small `a>0`, the Gaussian density on `B_{aR_c}` is comparable below to `R_c^{-3}`. Therefore

\[
\int_{B_{aR_c}}
|\Omega-\bar\Omega_c|^2dx
\lesssim_K
R_c^3V_{\omega,c}
\lesssim_K R_c^{-1}.
\]

Thus the coherent crossing is much stronger than a pointwise peak: on a region of volume `~R_c^3`, the vorticity is `L2`-close to one constant nonzero vector.

By Chebyshev, for every fixed `eta>0`, the bad set

\[
\{x\in B_{aR_c}:|\Omega-\bar\Omega_c|>\eta\}
\]

has Euclidean volume `O(R_c^-1)`. Hence almost all of the macroscopic crossing core has the same orientation and order-one magnitude.

## 2. Cross-sectional signed flux is macroscopically large

Use coordinates

\[
x=se+y,
\qquad y\in e^\perp.
\]

Inside a fixed inner cylinder of radius `aR_c` and axial length `aR_c`, define

\[
\Phi(s)=
\int_{|y|<aR_c}\Omega(se+y)\cdot e\,dy.
\]

The constant mean contribution is

\[
\Phi_{\rm mean}
=\pi a^2R_c^2|\bar\Omega_c|.
\]

Let

\[
f=(\Omega-\bar\Omega_c)\cdot e.
\]

Then

\[
\int|f|^2dx\lesssim R_c^{-1}.
\]

Cauchy--Schwarz on each cross-section gives

\[
|\Phi(s)-\Phi_{\rm mean}|^2
\lesssim
R_c^2
\int_{|y|<aR_c}|f(se+y)|^2dy.
\]

Integrating in `s` over an interval of length `~R_c`,

\[
\int|\Phi(s)-\Phi_{\rm mean}|^2ds
\lesssim R_c.
\]

Hence for all but a vanishing relative subset of axial labels,

\[
\boxed{
\Phi(s)\ge c_KR_c^2.
}
\]

The critical crossing therefore contains a robust family of material cross-sections carrying signed vorticity flux of order `R_c^2`.

## 3. Eulerian displacement is not a source

Let `S(t)` be any one of these cross-sections transported by the material flow.

For incompressible Navier--Stokes,

\[
\boxed{
\frac d{dt}
\int_{S(t)}\omega\cdot n\,dA
=-\nu
\oint_{\partial S(t)}
(\nabla\times\omega)\cdot d\ell.
}
\]

Thus

- translation of the whole core;
- advection of the material tube;
- inviscid vortex stretching inside the tube

are not independent sources or sinks of the **material vorticity flux**.

Inviscid stretching can increase vorticity magnitude only by deforming the material cross-sectional geometry while preserving the flux.

Therefore the Eulerian statement

\[
\text{dangerous vorticity came from spatial infinity / another shell}
\]

is not an independent causal mechanism once the terminal material labels are followed backward.

It becomes a statement about either

1. material deformation;
2. viscous flux change;
3. pure translation, which is removable by the moving frame.

## 4. Robust flux change forces bulk palinstrophy or large deformation

For a nested radial/axial family of material cross-sections, the established material-tube coarea identity gives

\[
\boxed{
\int_I\int_{A(t)}|\nabla\omega|^2dxdt
\gtrsim
\frac{H(\Delta\Phi)^2}
{\nu^2M_F^2\tau},
}
\]

where

- `H` is the axial label thickness;
- `tau` is the time interval;
- `M_F` is the maximal material deformation factor.

Thus a fixed fractional erosion of the coherent crossing flux has only two possibilities.

### B2-P — geometry controlled

If

\[
M_F\le K,
\]

then the flux change forces a quantitative bulk palinstrophy cost.

This is exactly the derivative-concentration remainder carried from Branch 1.

### B2-S — large material deformation

If

\[
M_F>K,
\]

then

\[
\boxed{
\int_I\|S(t)\|_\infty dt
\ge\log K.
}
\]

This is the symmetric-strain/Lagrangian-deformation branch, i.e. Branch 3.

## 5. If material flux does not change

Suppose instead the material flux remains essentially constant.

Then there is no vorticity-flux creation to explain spatially. The terminal coherent core is simply the deformed image of a precursor material tube carrying the same flux.

There are again only two possibilities:

1. the precursor tube remains quantitatively comparable in geometry — then the coherent vorticity structure persists backward and spatial translation is removed by the moving frame;
2. the precursor tube differs greatly in cross-sectional area, aspect ratio, or length — then its creation of the terminal intense core requires large Lagrangian deformation, hence accumulated symmetric strain.

Thus persistent flux also routes to Branch 3 unless it remains a compact material precursor, in which case it is not a spatial non-tightness escape at all.

## 6. Relation to shell and critical-L3 formulations

The Eulerian shell identities remain useful diagnostics:

- side leakage routes signed axial flux loss into off-axis vorticity;
- critical `L3` mass influx routes non-tight velocity mass into shell flux or pressure work;
- finite-shell selectors suppress artificial cutoff leakage on bounded-energy blocks.

But at the coherent vorticity crossing the material-flux formulation gives the causal reduction more directly:

\[
\boxed{
\text{Eulerian shell transport}
\longrightarrow
\text{material translation}
\lor
\text{viscous derivative erosion}
\lor
\text{strain deformation}.
}
\]

The first is coordinate bookkeeping; the latter two are already Branch 1 and Branch 3.

## 7. Revised status of Branch 2

Branch 2 began as

\[
\text{spatial non-tightness / shell transport}.
\]

At the coherent Reynolds-one crossing it no longer remains an independent endpoint branch.

It is reduced to

\[
\boxed{
\text{Branch 1 remainder: palinstrophy / derivative concentration}
}
\]

or

\[
\boxed{
\text{Branch 3: large symmetric-strain / material deformation}.
}
\]

Pure spatial translation is removable by the accelerating/moving frame and carries no internal regularity difficulty.

Status: **BRANCH 2 CLOSED AS AN INDEPENDENT CAUSAL ESCAPE ON THE COHERENT CROSSING TRACK / ALL NONTRIVIAL SPATIAL ESCAPE ROUTES MERGE INTO DERIVATIVE CONCENTRATION OR SYMMETRIC-STRAIN DEFORMATION / GLOBAL REGULARITY NOT PROVED.**
