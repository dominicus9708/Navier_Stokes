# Localized Betchov-shape compatibility gate

Date: 2026-08-13

Status: **DERIVED LOCALIZATION SCHEME USING THE EXISTING GLOBAL FOURIER ANGLE GAP + STANDARD DIVERGENCE CORRECTION; QUANTITATIVE CONSTANTS NOT YET OPTIMIZED**.

This note localizes the repository's global fact that the formal Betchov determinant-optimal strain shape cannot lie in the incompressible strain Fourier subspace.

## 1. Formal source-optimal shape

Normalize the trace-free symmetric matrix

\[
A_*
=\frac1{\sqrt6}\operatorname{diag}(-2,1,1),
\qquad |A_*|_F=1.
\]

For each nonzero Fourier frequency, an incompressible strain mode has the form

\[
M(\xi,v)
=\frac12(\xi\otimes v+v\otimes\xi),
\qquad \xi\cdot v=0,
\]

and the repository derived the uniform spectral-angle gap

\[
\boxed{
\operatorname{dist}(A_*,\mathcal R_\xi)\ge\frac12.
}
\]

Consequently for every scalar field `a` and every whole-space divergence-free strain `S_v=sym nabla v`,

\[
\boxed{
\|S_v-aA_*\|_2
\ge\frac12\|a\|_2.
}
\]

The same statement holds after a fixed orthogonal rotation of `A_*`.

## 2. Localize an actual Navier--Stokes strain

Let `u` be divergence free and

\[
S=\operatorname{sym}\nabla u.
\]

Choose a cutoff `chi` with

- `chi=1` on `B_R`,
- `supp chi subset B_{2R}`,
- `|nabla chi| <= C/R`.

The raw localized field `chi u` is not divergence free:

\[
\nabla\cdot(\chi u)=u\cdot\nabla\chi.
\]

Use a standard Bogovskii/divergence-correction field `w`, supported in the buffer annulus, satisfying

\[
\nabla\cdot w=u\cdot\nabla\chi,
\qquad
\|\nabla w\|_2
\lesssim
R^{-1}\|u\|_{L^2(B_{2R}\setminus B_R)}.
\]

Then

\[
v=\chi u-w
\]

is whole-space divergence free and compactly supported in the buffer.

Its strain obeys

\[
S_v
=
\chi S
+\operatorname{sym}(u\otimes\nabla\chi)
-\operatorname{sym}\nabla w.
\]

Hence

\[
\boxed{
\|S_v-\chi aA_*\|_2
\le
\|\chi(S-aA_*)\|_2
+C R^{-1}\|u\|_{L^2(B_{2R}\setminus B_R)}.
}
\]

## 3. Local compatibility inequality

Apply the global `1/2` Fourier gap to `S_v` and scalar `chi a`:

\[
\frac12\|\chi a\|_2
\le
\|S_v-\chi aA_*\|_2.
\]

Therefore

\[
\boxed{
\frac12\|\chi a\|_2
\lesssim
\|\chi(S-aA_*)\|_2
+
R^{-1}\|u\|_{L^2(B_{2R}\setminus B_R)}.
}
\]

Interpretation: a determinant-efficient, nearly fixed-eigenframe strain core cannot be localized cheaply.  At least one of the following must occur:

1. **shape/eigenframe defect** inside the core;
2. **kinetic-energy reservoir** in the annular buffer.

A variable eigenframe is not included for free: its variation is a separate orientation/curvature residual channel.

## 4. Scale consequence

Suppose on a substantial fraction of `B_R`

\[
|a|\gtrsim A
\]

and the shape defect is a sufficiently small fraction of `A R^{3/2}`.  Then

\[
\boxed{
\int_{B_{2R}\setminus B_R}|u|^2dx
\gtrsim
A^2 R^5.
}
\]

At an instantaneous vorticity level `W`, write a mesoscopic physical scale as

\[
R_{\rm phys}=W^{-1/2+\theta}.
\]

If the coherent strain magnitude is of order `A~W`, then the annular kinetic-energy cost scales like

\[
\boxed{
A^2R_{\rm phys}^5
\sim
W^{-1/2+5\theta}.
}
\]

Thus a source-optimal coherent strain of order `W` cannot persist on scales with

\[
\boxed{\theta>1/10}
\]

under a fixed finite kinetic-energy budget as `W->infinity`.

This reproduces the `1/10` mesoscopic exponent by a compatibility mechanism rather than by Gaussian affine-mean decay.

## 5. Why this strengthens the affine-mean cutoff

The previous estimate

\[
|L_R|\lesssim \|u_0\|_2 R^{-5/2}
\]

only says the *mean affine strain* dies at large mesoscopic scales.

The present gate says more: even if the mean cancels, a strain field that remains locally close to one fixed Betchov-optimal eigenframe shape must pay annular kinetic energy.  To evade that cost it must develop

- eigenframe rotation,
- shape variation,
- sign/phase cancellation,
- or other non-affinity.

Those are precisely residual/curvature channels already typed elsewhere in the repository.

## 6. Claim boundary

The local inequality uses a standard divergence-correction construction.  A referee-grade version should specify the annular Bogovskii domain and constants and should treat slowly varying eigenframes by an additional commutator/orientation term.

It does **not** by itself exclude finite-time blowup.  It is a routing lemma:

\[
\boxed{
\text{coherent source-optimal mesoscopic strain}
\Rightarrow
\text{shape defect or shell kinetic energy}.
}
\]
