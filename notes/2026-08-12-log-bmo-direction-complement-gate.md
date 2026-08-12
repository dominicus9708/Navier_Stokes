# Log-BMO vorticity-direction complement gate

Date: 2026-08-12

Status: **EXTERNAL 2026 PREPRINT GATE (RESTRICTED SCOPE) + DERIVED POINCARE COMPLEMENT**.

This note integrates a recent arXiv preprint by Zoran Grujic into the residual-class map.  Because the work is recent and the present repository has not independently reproduced its full proof, it is recorded as an **external preprint gate**, not as an established theorem of this project.

## 1. Scope of the external preprint

Grujic's 2026 preprint studies a restricted potential singularity class: critical point singularities whose vorticity magnitude has the critical spatial concentration

\[
|\omega(x)|\sim |x|^{-2},
\]

corresponding naturally to the Lorentz endpoint

\[
L^{3/2,\infty}(\mathbb R^3).
\]

Within that critical-point setting, the preprint assumes a local logarithmically weighted BMO condition on the vorticity direction

\[
\xi=\frac{\omega}{|\omega|},
\]

with weight

\[
\phi(r)=\frac1{|\log r|},
\]

and derives logarithmic depletion of vortex stretching and singularity evasion.

This gate is **not** applied to arbitrary hypothetical singularity geometries without the critical-point / Lorentz hypotheses.

External source:

- Z. Grujic, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866v2 (July 2026).

## 2. DSD local direction-difference channel

For a ball `B_r(x)`, define

\[
\operatorname{MO}_\xi(x,r)
=
\fint_{B_r(x)}
|\xi(y)-\xi_{B_r(x)}|dy,
\]

where

\[
\xi_{B_r(x)}
=
\fint_{B_r(x)}\xi(y)dy.
\]

Define the logarithmic direction-difference channel

\[
\boxed{
\mathcal B_\xi(x,r)
=|\log r|\,
\operatorname{MO}_\xi(x,r).
}
\]

Uniform boundedness of the corresponding supremum over the relevant critical core/scales is the DSD readout of the preprint's `bmo_{1/|log r|}` geometric assumption (with the usual bounded base norm; `|xi|=1` where defined).

Formation typing remains mandatory: `xi` and its oscillation channel are inapplicable where `omega=0` unless an explicit restricted-domain convention is stated.

## 3. Elementary Poincare complement

Whenever `xi` belongs locally to `H^1`, the ball Poincare inequality gives

\[
\operatorname{MO}_\xi(x,r)
\lesssim
r
\left(
\fint_{B_r(x)}|\nabla\xi|^2dy
\right)^{1/2}.
\]

Therefore

\[
\boxed{
r^2
\fint_{B_r(x)}|\nabla\xi|^2dy
\gtrsim
\operatorname{MO}_\xi(x,r)^2.
}
\]

Multiplying by `|log r|^2`, define

\[
\boxed{
\mathcal Q_\xi(x,r)
=|\log r|^2r^2
\fint_{B_r(x)}|\nabla\xi|^2dy.
}
\]

Then

\[
\boxed{
\mathcal Q_\xi(x,r)
\gtrsim
\mathcal B_\xi(x,r)^2.
}
\]

Thus a quantitative failure of the log-BMO envelope forces a quantitative growth of the log-weighted direction-gradient channel.

## 4. Complement structure in the restricted critical-point class

For a critical point singularity within the scope of the preprint, the direction branch is now split as follows.

### Branch L: logarithmic mean oscillation stays controlled

\[
\sup_{x,r\downarrow0}
\mathcal B_\xi(x,r)<\infty.
\]

This is the external-preprint regularity/singularity-evasion branch.

### Branch R: logarithmic mean oscillation escapes

To evade Branch L, there must exist a shrinking sequence `(x_n,r_n)` in the relevant core with

\[
\mathcal B_\xi(x_n,r_n)\to\infty
\]

(or at least failure of the required uniform bound).

The Poincare bridge then gives

\[
\boxed{
\mathcal Q_\xi(x_n,r_n)	o\infty
}
\]

along any sequence for which `mathcal B_xi` diverges.

Hence the residual direction geometry is not simply `incoherent`; it must carry increasingly large scale-normalized direction gradients.

## 5. Connection to the exact vorticity-magnitude equation

The repository has already derived

\[
(\partial_t+u\cdot\nabla-\nu\Delta)|\omega|
=
|\omega|
\left(
\gamma-
u|\nabla\xi|^2
\right)
\]

where `omega != 0`.

Thus large direction gradients are dynamically penalized.

The complement structure becomes

\[
\boxed{
\text{log-BMO controlled}
\Rightarrow
\text{external preprint depletion gate},
}
\]

while

\[
\boxed{
\text{log-BMO strongly violated}
\Rightarrow
\text{large direction-gradient diffusion channel}.
}
\]

This is exactly the kind of two-sided complement elimination sought in the DSD proof strategy.

## 6. Important missing bridge

The Poincare estimate is an average over a ball, whereas maximum-vorticity growth uses

\[
\gamma-
u|\nabla\xi|^2
\]

at maximum-vorticity points.

Therefore the present argument does **not** prove that a large `Q_xi` average forces the negative direction-gradient term to dominate at the vorticity maximum.

The missing statement is a **co-location/occupancy bridge** connecting

- strong-vorticity occupancy;
- ball-averaged direction-gradient cost;
- and the maximum-vorticity growth set.

This is now a principal cross-gate target.

## 7. DSD typed direction block

Within the critical-point branch retain

\[
\boxed{
\mathcal D_\xi
=
\left(
\operatorname{MO}_\xi,
\mathcal B_\xi,
\mathcal Q_\xi,
\rho_{\rm occ},
\rho_{\rm line,min},
\gamma,
\nu|\nabla\xi|^2,
\mathcal G
\right).
}
\]

Do not replace mean oscillation by pointwise gradient, or vice versa; the Poincare inequality is one-way for the purpose used here.

## 8. Revised residual critical-point condition

A hypothetical critical-point singularity in the preprint's Lorentz class must either fall outside the external preprint's hypotheses or, within the direction sector, develop a failure of the logarithmic BMO envelope.

If that failure is realized by unbounded `mathcal B_xi` on shrinking core balls, the scale-normalized direction-gradient channel `mathcal Q_xi` must become unbounded along the same sequence.

The next question is whether non-sparse vorticity occupancy can force enough of this gradient penalty to overlap the intense-vorticity core to prevent the required nonintegrable positive excess `mathcal G`.

Status: **OPEN OCCUPANCY–DIRECTION-GRADIENT CO-LOCATION ESTIMATE**.
