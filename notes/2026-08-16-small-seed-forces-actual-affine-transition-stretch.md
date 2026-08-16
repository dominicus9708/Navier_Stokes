# Small residual seed forces actual affine transition stretch

Date: 2026-08-16

Status: **DERIVED EXACT VARIATION-OF-CONSTANTS DEFORMATION BARRIER. ON THE SMALL-RESIDUAL-SEED BRANCH, LARGE MEAN-VORTICITY CREATION REQUIRES A GENUINELY LARGE AFFINE TRANSITION SINGULAR VALUE; A LARGE INTEGRATED STRAIN NORM WITH STRONG DIRECTIONAL CANCELLATION CANNOT BY ITSELF EXPLAIN THE ENDPOINT. GLOBAL REGULARITY NOT PROVED.**

## 1. Exact mean equation

Along the terminal-conditioned Gaussian/kernel state, write

\[
\bar\Omega'(t)=L(t)\bar\Omega(t)+J(t),
\]

where `L` is the coherent affine velocity-gradient representative and `J` is the residual mean source.

Let the transition matrix solve

\[
\partial_tF(t,s)=L(t)F(t,s),
\qquad F(s,s)=I.
\]

Then the exact variation-of-constants formula is

\[
\boxed{
\bar\Omega(T)
=F(T,t_0)\bar\Omega(t_0)
+\int_{t_0}^{T}F(T,s)J(s)ds.
}
\]

No Gronwall overestimate is used here.

## 2. Recent-source normalization

The current recent-source frontier supplies a starting time `t0` for which the old/homogeneous contribution is negligible:

\[
\boxed{
|F(T,t_0)\bar\Omega(t_0)|=o(1).
}
\]

At the coherent crossing,

\[
\boxed{|ar\Omega(T)|\ge c_0>0.}
\]

Hence for all sufficiently late episodes,

\[
\left|
\int_{t_0}^{T}F(T,s)J(s)ds
\right|
\ge c_0/2.
\]

## 3. Residual source mass versus actual transition stretch

Define

\[
\mathcal J
:=\int_{t_0}^{T}|J(s)|ds
\]

and

\[
q_*:=\sup_{s\in[t_0,T]}\|F(T,s)\|_{op}.
\]

Then directly

\[
\frac{c_0}{2}
\le
q_*\mathcal J.
\]

Therefore

\[
\boxed{
q_*\ge\frac{c_0}{2\mathcal J}.
}
\]

If the DSD residual covariance estimate gives

\[
|J(s)|\le C B(s),
\]

and

\[
\mathcal B:=\int_{t_0}^{T}B(s)ds,
\]

then

\[
\mathcal J\le C\mathcal B
\]

and hence

\[
\boxed{
q_*\gtrsim\mathcal B^{-1}.
}
\]

In particular, on the small-seed branch

\[
\boxed{
\mathcal B\le R^{-\gamma}
}
\]

for a fixed `gamma>0`, one has

\[
\boxed{
q_*\gtrsim R^\gamma.
}
\]

There exists at least one injection time `s_*` such that

\[
\boxed{
\|F(T,s_*)\|_{op}\gtrsim R^\gamma.
}
\]

## 4. Stronger than the norm-Gronwall statement

The previous seed--amplification estimate gave only

\[
\mathcal B\le R^{-\gamma}
\Longrightarrow
\int\|\operatorname{sym}L\|dt
\gtrsim\gamma\log R.
\]

That conclusion used

\[
\|F(T,s)\|
\le
\exp\left(
\int_s^T\|\operatorname{sym}L\|dt
\right).
\]

It allowed a possible logical loophole: the strain norm could be large while changing directions so strongly that the actual net deformation remained modest.

The exact variation-of-constants argument removes that loophole on the small-seed branch. The endpoint needs the actual matrix factor itself:

\[
\boxed{
\text{small residual seed}
\Longrightarrow
\text{polynomially large actual affine transition stretch}.
}
\]

The logarithmic strain-action bound follows as a corollary, not as the primary statement:

\[
\boxed{
\int_{s_*}^{T}\|\operatorname{sym}L(t)\|dt
\ge
\log q_*
\gtrsim
\gamma\log R.
}
\]

## 5. Incompressible singular-value geometry

Because `tr L=0`,

\[
\det F(T,s_*)=1.
\]

Let its singular values be

\[
\sigma_1=q_*\ge\sigma_2\ge\sigma_3>0.
\]

Then

\[
\sigma_2\sigma_3=q_*^{-1}.
\]

Thus large endpoint stretch necessarily comes with two-dimensional transverse compression in aggregate. This is exactly the geometry seen by the accumulated affine heat matrix

\[
C(T,s_*)
=\int_{s_*}^{T}
F(\tau,s_*)^{-1}F(\tau,s_*)^{-T}d\tau.
\]

The existing rotation-independent affine diffusion theorem therefore becomes relevant to the remaining branch, provided the residual source can be inserted into the corresponding Duhamel smoothing estimate without losing the transverse heat gain.

## 6. What is and is not proved

This lemma is exact for the mean variation-of-constants equation and does not assume the full velocity is globally affine.

It does **not** yet prove that the large `q_*` forces a nonsummable cost. A residual source inserted late in the affine evolution may avoid using the full deformation history, and the residual source is not the same object as the initial vorticity in the older affine-capacity theorem.

Therefore the next target is a source-sensitive affine Duhamel estimate:

\[
\boxed{
\|F(T,s)e^{\nu C(T,s):D^2}f_{\rm res}(s)\|_\infty
}
\]

or its Gaussian mean analogue, with a quantitative two-axis diffusion penalty tied to the actual transition stretch `q(T,s)`.

Status: **SMALL SEED -> ACTUAL POLYNOMIAL AFFINE STRETCH CLOSED / DIRECTIONAL-CANCELLATION LOOPHOLE REMOVED / SOURCE-SENSITIVE AFFINE DIFFUSION BRIDGE IS THE NEXT TARGET.**
