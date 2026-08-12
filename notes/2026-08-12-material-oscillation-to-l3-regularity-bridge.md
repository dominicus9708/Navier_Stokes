# Material oscillation to critical `L^3` regularity bridge

Date: 2026-08-12

Status: **DERIVED INTERPOLATION BRIDGE + EXTERNAL EPSILON-REGULARITY ANCHOR + OPEN SMALLNESS OBLIGATION**.

## 1. Setup on a restartable material tube

Fix a restart time `t0`, material reference ball `B_ell(a)`, and a parabolic window

\[
s\in[t_0,t_0+\ell^2].
\]

Let

\[
\Omega_s=\Phi_{s;t_0}(B_\ell(a)),
\]

and use the material-cell mean velocity

\[
\bar U(s)=\frac1{|B_\ell|}
\int_{B_\ell(a)}u(\Phi_{s;t_0}(b),s)db.
\]

Define

\[
W(b,s)=u(\Phi_{s;t_0}(b),s)-\bar U(s),
\]

so that

\[
\int_{B_\ell(a)}W(b,s)db=0.
\]

The instantaneous oscillation and local gradient-energy channels are

\[
C_{\rm osc}(s)
=\ell^{-1}\int_{B_\ell(a)}|W|^2db,
\]

\[
E_\nabla(s)
=\ell\int_{\Omega_s}|\nabla u|^2dx.
\]

Both are Navier--Stokes scale invariant.

## 2. Pullback Sobolev estimate

On the fixed reference ball, Poincare--Sobolev gives

\[
\|W\|_{L^6(B_\ell)}
\le C\|\nabla_bW\|_{L^2(B_\ell)}.
\]

Since

\[
\nabla_bW=(\nabla_xu)(\Phi_{s;t_0}(b),s)F(b,s),
\]

where

\[
F=D_b\Phi_{s;t_0},
\]

we obtain

\[
\|W\|_6
\le
C\|F\|_{L^\infty(B_\ell)}
\left(\frac{E_\nabla(s)}{\ell}\right)^{1/2}.
\]

If recent extension is controlled by

\[
K_+^*
=
\sup_{s\in[t_0,t_0+\ell^2]}
\log\|F(s)\|_{L^\infty},
\]

then

\[
\|W\|_6
\le
Ce^{K_+^*}
\left(\frac{E_\nabla}{\ell}\right)^{1/2}.
\]

## 3. Critical cubic bound

Interpolation gives

\[
\|W\|_3
\le
\|W\|_2^{1/2}\|W\|_6^{1/2}.
\]

Because

\[
\|W\|_2^2=\ell C_{\rm osc},
\]

we obtain the fixed-time scale-invariant estimate

\[
\boxed{
\int_{\Omega_s}|u-\bar U|^3dx
\le
C e^{3K_+^*/2}
\left(C_{\rm osc}(s)E_\nabla(s)\right)^{3/4}.
}
\]

Define the parabolic cubic channel

\[
A_{3,{\rm osc}}
=
\ell^{-2}
\int_{t_0}^{t_0+\ell^2}
\int_{\Omega_s}|u-\bar U|^3dxds,
\]

and

\[
\mathfrak E_\nabla
=
\ell^{-2}
\int_{t_0}^{t_0+\ell^2}E_\nabla(s)ds.
\]

Using concavity/Hölder on the normalized time interval gives

\[
\boxed{
A_{3,{\rm osc}}
\le
C e^{3K_+^*/2}
\left[
\left(\sup_sC_{\rm osc}(s)\right)
\mathfrak E_\nabla
\right]^{3/4}.
}
\]

Thus a small product of internal oscillation and local dissipation, together with bounded recent deformation, forces small critical spacetime `L^3` oscillation.

## 4. This does not yet close regularity

The inequality above is a sufficient bridge to the velocity portion of classical one-scale epsilon-regularity criteria.  It does **not** show that

\[
\left(\sup C_{\rm osc}\right)\mathfrak E_\nabla
\]

is small for arbitrary smooth initial data at every candidate singular point/scale.

Indeed, Poincare only gives the one-way estimate

\[
C_{\rm osc}
\le
C e^{2K_+^*}E_\nabla.
\]

So the new channel does not automatically improve on a small local-dissipation criterion.  A genuine DSD gain must come from the coupled evolution of oscillation, pressure difference, and geometry rather than from interpolation alone.

## 5. Near-pressure bridge after mean subtraction

At each fixed time, subtracting a spatially constant vector `c` from the velocity leaves the pressure Poisson source unchanged:

\[
\partial_i\partial_j[(u_i-c_i)(u_j-c_j)]
=
\partial_i\partial_j(u_i u_j),
\]

because `div u=0` and `c` has no spatial derivatives.

Therefore the mean-centered velocity can be used in a localized pressure decomposition.
For a near-field Calderon--Zygmund solve, schematically,

\[
\|p_{\rm near}\|_{L^{3/2}}
\le C\|W\otimes W\|_{L^{3/2}}
=C\|W\|_{L^3}^2,
\]

up to the cutoff/harmonic terms required by localization.

Consequently the same small oscillatory `L^3` channel also controls the locally generated near-pressure component at the correct exponent.

The far pressure is treated separately by the differential kernel-cancellation bridge already recorded in `2026-08-12-pressure-difference-localization.md`.

## 6. External regularity target

Classical one-scale epsilon-regularity theory for suitable weak solutions contains criteria in which sufficiently small scale-normalized spacetime `L^3` velocity together with `L^{3/2}` pressure implies boundedness in a smaller parabolic cylinder.

A 2017 one-scale epsilon-regularity paper by He, Wang, and Zhou records this classical `L^3`/`L^{3/2}` criterion and proves broader one-scale criteria with weaker pressure integrability.

The present DSD route therefore has a concrete target rather than a new regularity definition:

1. make the material oscillatory `L^3` channel small;
2. control near and far pressure at the corresponding scale;
3. control recent deformation sufficiently to transfer the material tube to an Eulerian/Galilean parabolic cylinder;
4. invoke an established epsilon-regularity criterion.

## 7. Remaining proof obligation

The missing statement is now sharply localized:

\[
\boxed{
\text{Prove, for arbitrary admissible smooth data, that every candidate singular material tube reaches an epsilon-regularity smallness gate.}
}
\]

Equivalently, one must derive a non-circular mechanism forcing at least one of the dangerous channels to lose the critical concentration needed for singularity formation.

Status: **OPEN PROOF OBLIGATION**.
