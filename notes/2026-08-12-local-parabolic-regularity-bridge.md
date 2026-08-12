# Local parabolic regularity bridge from the all-center shell family

Date: 2026-08-12

Status: **BRIDGE DESIGN + DERIVED COAREA/SCALING IDENTITIES + OPEN PROOF OBLIGATION**.

## 1. Motivation

The global critical `L^3` route leaves a difficult pressure-correlation term. The all-center celestial-sphere representation offers a second, more local route that is geometrically compatible with established partial-regularity theory for suitable weak solutions.

The purpose here is not to restate or replace Caffarelli–Kohn–Nirenberg (CKN). It is to show that the DSD shell representation can reconstruct the local ball and parabolic-cylinder data used by standard Navier–Stokes regularity analysis without introducing a physical container.

## 2. Shells are level sets, not walls

For every analysis center `x_0` and radius `s>0`, define

\[
S_s(x_0)=\{x:|x-x_0|=s\}.
\]

For an integrable scalar channel `f`, coarea in Euclidean space gives

\[
\int_{B_r(x_0)}f(x)\,dx
=
\int_0^r\left(\int_{S_s(x_0)}f\,dS\right)ds.
\]

Thus a sufficiently resolved all-center shell family can be radially accumulated into ordinary ball integrals. The observation spheres remain mathematical sampling surfaces; no boundary condition is imposed on them.

## 3. Exact benchmark recovery

For the Gaussian double-curl seed, the committed shell formulas recover exactly

\[
\int_{\mathbb R^3}\frac12|u|^2dx
=
\frac{5\sqrt2\,\pi^{3/2}}{4},
\]

and

\[
\int_{\mathbb R^3}|\omega|^2dx
=
\frac{35\sqrt2\,\pi^{3/2}}{2}.
\]

This verifies that the shell representation does not lose these volume aggregates when the radial coordinate is retained.

## 4. Parabolic DSD channels

For a space-time center

\[
z_0=(x_0,t_0)
\]

and radius `r`, define the backward parabolic cylinder

\[
Q_r(z_0)=B_r(x_0)\times(t_0-r^2,t_0).
\]

The first local scale-aware DSD channels are

\[
C_u(z_0,r)
=
\frac1{r^2}
\int_{Q_r(z_0)}|u|^3\,dxdt,
\]

\[
C_p(z_0,r)
=
\frac1{r^2}
\int_{Q_r(z_0)}|p-\langle p\rangle_{B_r}|^{3/2}\,dxdt,
\]

and

\[
E_\nabla(z_0,r)
=
\frac1r
\int_{Q_r(z_0)}|\nabla u|^2\,dxdt.
\]

These are bridge definitions chosen because their dimensions match the natural Navier–Stokes parabolic scaling.

## 5. Exact scaling check

Under

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t),
\]

the transformed volume element contributes `lambda^-5` over space-time. Therefore each of

\[
C_u,
\qquad
C_p,
\qquad
E_\nabla
\]

is dimensionless when the center and radius are transformed together.

This scaling is verified symbolically in `src/coarea_local_bridge.py`.

## 6. DSD layer assignment

### Formation layer

Keep velocity, pressure, gradient, vorticity, center, radius, and applicability status typed separately. Missing angular or pressure information must not be zero-padded.

### Axis-property layer

The Cartesian spatial rank remains three. The radius and angular directions are local directions/coordinates inside `R^3`, not extra realized spatial axes.

### Static Aggregation layer

At each fixed time, shell component terms are radially accumulated into `B_r(x_0)` channels. Angular information may be retained as subchannels before integration to prevent premature collisions.

### Structural Reorganization Dynamics layer

The fixed-time local channels are accumulated over the natural time window of length `r^2`. This produces a space-time lineage indexed by `(x_0,t_0,r)`.

## 7. Relation to external regularity theory

The classical Caffarelli–Kohn–Nirenberg work establishes partial regularity for suitable weak solutions of the three-dimensional Navier–Stokes equations. Later interior criteria likewise use sufficiently small scaled local space-time norms to infer regularity near a point.

The DSD program will therefore treat established local regularity theorems as **external implication gates**. It will not claim that the definitions above prove regularity by themselves.

## 8. What remains genuinely hard

The unresolved task is not to write down a dimensionless local quantity. It is to prove that, for every possible candidate blow-up point, the DSD channel evolution forces some established regularity gate to activate.

In schematic form, one would need a theorem of the type

\[
\forall z_0\quad
\exists r>0:
\quad
\mathcal R_{\rm local}(z_0,r)<\varepsilon_*,
\]

where `R_local` is rigorously connected to a published epsilon-regularity criterion.

That statement is **OPEN PROOF OBLIGATION** and is essentially where the global difficulty reappears.

## 9. Immediate next search target

Rather than using only a signed shell average, track across each `(x_0,r)`:

1. local `|u|^3` concentration;
2. pressure fluctuation concentration;
3. local dissipation `|grad u|^2`;
4. positive/negative vortex-stretching separation;
5. angular concentration/entropy;
6. cross-coupling contributions between component structures.

The next question is whether these channels yield an inequality that forces concentration to disperse, transfer to a smaller scale with controlled loss, or remain below a known regularity threshold.

## References

- L. Caffarelli, R. Kohn, L. Nirenberg, *Partial regularity of suitable weak solutions of the Navier-Stokes equations*, Communications on Pure and Applied Mathematics 35 (1982), 771–831, DOI `10.1002/cpa.3160350604`.
- S. Gustafson, K. Kang, T.-P. Tsai, *Interior regularity criteria for suitable weak solutions of the Navier-Stokes equations*, Communications in Mathematical Physics 273 (2007), 161–176, arXiv `math/0607114`.
