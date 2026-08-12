# Residual singularity class after complement elimination

Date: 2026-08-12

Status: **LOGICAL PROOF MAP / OPEN EMPTINESS OBLIGATION**.

This note uses the Formation-Axiom-style complement-elimination idea conservatively: each established regularity gate removes a class of candidate singular configurations.  It does not claim that the remaining intersection is empty.

## 1. Universe of candidate endpoint configurations

Let `S` denote the class of hypothetical finite-time singular configurations compatible with the baseline 3D incompressible Navier--Stokes equations on `R^3` and arising as limits of smooth evolution before a maximal time `T*`.

The current project does not construct `S`; it reasons conditionally:

\[
T^*\text{ singular}
\Longrightarrow
\text{the solution must avoid every sufficient regularity gate below.}
\]

## 2. Gate G_osc: moving mean-flow oscillation

The weighted moving-center lemma and the generalized translation lemma allow the internal velocity

\[
v=u-\bar U_\ell
\]

to be tested in an ordinary suitable cylinder.

A published pressure-free one-scale epsilon criterion then removes configurations for which a critical spacetime velocity norm is sufficiently small.

The repository interpolation bridge expresses one convenient sufficient route through

\[
(\sup C_\phi)^{\alpha(p)}
(\mathfrak E_\phi)^{\beta(p)}
<\varepsilon_p/C.
\]

Define the safe class `G_osc` by this implication.

A residual singularity must lie in

\[
G_{\rm osc}^{c}.
\]

Interpretation: coherent translation has been removed; the **internal velocity difference** must remain critically non-small along arbitrarily fine endpoint scales.

## 3. Gate G_sparse: intense-vorticity sparseness

Grujic's geometric theorem removes configurations in which the intense-vorticity super-level set becomes linearly sparse at the vorticity analyticity scale.

The repository supplies the sufficient occupancy bridge

\[
\mathcal W_r
=r\int_{B_r}|\omega|^2dx
\quad\text{small enough}
\Longrightarrow
\rho_{\rm vol}\text{ small}
\Longrightarrow
\rho_{\rm line,min}\text{ small}.
\]

Define this regularity class as `G_sparse`.

A residual singularity must lie in

\[
G_{\rm sparse}^{c}.
\]

Interpretation: the intense-vorticity region must remain **geometrically dense enough** at the natural scale to avoid every guaranteed sparse direction.

## 4. Gate G_dir: vorticity-direction coherence

Published vorticity-direction criteria remove classes of configurations in which the direction

\[
\xi=\frac{\omega}{|\omega|}
\]

is sufficiently coherent in the high-vorticity region.

Define the union of the direction-coherence regularity classes being used as external anchors by `G_dir`.

A residual singularity must lie in

\[
G_{\rm dir}^{c}.
\]

Interpretation: high vorticity cannot merely be dense; its direction geometry must also be irregular enough to evade the known depletion of vortex stretching.

## 5. Gate G_strain: middle strain eigenvalue

For ordered strain eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\operatorname{tr}S=0,
\]

published scale-critical regularity criteria involving the positive part

\[
\lambda_2^+
\]

remove another class of flows.

Call their safe union `G_strain`.

A residual singularity must lie in

\[
G_{\rm strain}^{c}.
\]

This channel is not identified with the vorticity-direction channel: the repository's exact examples show that strain geometry and vorticity alignment carry different information.

## 6. Gate G_high: higher-derivative sparseness chains

Grujic--Xu's higher-derivative `Z_alpha^(k)` framework gives additional sparseness/analyticity restrictions and asymptotically reduces the scaling gap as derivative order grows.

Call configurations already excluded by that established derivative-chain framework `G_high`.

A residual singularity must lie in

\[
G_{\rm high}^{c}.
\]

The present DSD project treats this as an external anchor, not a novel DSD theorem.

## 7. Pressure locality is a transfer constraint, not a separate gate

The pressure analysis gives

\[
A_\phi,\ P_{\rm near}
\lesssim
(C_RE_R)^{3/4}
\]

and, after affine subtraction, genuinely remote pressure scales are suppressed by a dyadic kernel of the form

\[
2^{-4j}.
\]

This does not itself prove regularity.  Instead it restricts how a residual singular configuration can move through scales:

\[
\boxed{
\text{critical concentration must be sustained mainly by nearby physical scales.}
}
\]

Denote this transfer constraint by `L_pressure`.

## 8. Time-window vorticity cost

The vorticity occupancy gate gives the dimensionless natural-window channel

\[
\mathcal Z_\omega(t)
=
\|\omega(t)\|_\infty^{1/2}
\int_{I_t}\|\omega(s)\|_2^2ds.
\]

A residual singularity must have arbitrarily late dangerous times at which

\[
\mathcal Z_\omega(t)
\ge c_{\delta,d_0}>0.
\]

It must also obey the analyticity alternative's necessary growth

\[
\|\omega(t)\|_\infty
>
\frac{1}{d_0^2(T^*-t)}
\]

at sufficiently late times.

Again these are residual-class restrictions, not a contradiction.

## 9. The current residual set

The surviving class is therefore schematically

\[
\boxed{
\mathfrak R
=
S
\cap G_{\rm osc}^{c}
\cap G_{\rm sparse}^{c}
\cap G_{\rm dir}^{c}
\cap G_{\rm strain}^{c}
\cap G_{\rm high}^{c}
\cap L_{\rm pressure}.
}
\]

Any global-regularity proof along the present route must establish

\[
\boxed{
\mathfrak R=\varnothing.
}
\]

Nothing in the current repository establishes this emptiness.

## 10. Typed residual certificate

A member of `R` must simultaneously exhibit:

1. **critical internal velocity oscillation** after coherent local translation is removed;
2. **critical local dissipation** on arbitrarily small parabolic scales;
3. **near-scale nonlinear feeding**, since direct macroscopically remote pressure injection is suppressed;
4. **non-sparse intense-vorticity occupancy** at the natural `||omega||_infty^{-1/2}` scale;
5. **directional incoherence or other failure of known vorticity-direction gates**;
6. **dangerous strain history** sufficient to evade `lambda_2^+` regularity criteria;
7. **survival of higher-derivative sparseness-chain restrictions**;
8. **non-small vorticity-window dissipation cost** on arbitrarily late natural windows;
9. **at least analyticity-scale vorticity growth** near the endpoint;
10. all necessary off-diagonal nonlinear cross-couplings.

This is a much smaller target than the original set of all smooth initial flows, but it is still nonempty as far as current mathematics is known.

## 11. Independence / non-redundancy audit

The gates should not be collapsed prematurely.

- `G_osc` concerns velocity magnitude differences and local dissipation.
- `G_sparse` concerns spatial occupancy of intense vorticity magnitude.
- `G_dir` concerns the direction field where vorticity is nonzero.
- `G_strain` concerns eigenvalue geometry/history of the symmetric velocity gradient.
- `G_high` concerns higher spatial derivative super-level geometry.
- `L_pressure` concerns transfer locality across physical scales.

Known identities couple these channels, but no implication among them strong enough to delete one of the gates has been proved here.

## 12. Next proof target

The next step should seek a theorem of the form

\[
G_{\rm osc}^{c}
\cap G_{\rm sparse}^{c}
\cap L_{\rm pressure}
\Longrightarrow
G_{\rm dir}\cup G_{\rm strain}\cup G_{\rm high},
\]

or another implication that makes the intersection strictly smaller.

In words:

> if critical velocity oscillation keeps cascading locally and the intense vorticity remains geometrically dense, must the resulting strain/direction/higher-derivative geometry enter a known regularity class?

This implication is currently **OPEN** and is the principal structural target after the present complement elimination.
