# Stochastic Cauchy strain-Kato amplification barrier

Date: 2026-08-16

Status: **DERIVED NECESSARY STOCHASTIC STRAIN-EXPONENTIAL / ENSTROPHY-ACTION BARRIER UNDER FIRST-HITTING VORTICITY CAP / DOES NOT PROVE GLOBAL REGULARITY.**

## 1. Setup

Work in terminal first-hitting normalized variables on an interval `I=[s_-,0]` with

\[
\|\Omega(s)\|_{L^\infty}\le 1
\]

for every `s in I`. Suppose the earlier checkpoint has

\[
\|\Omega(s_-)\|_\infty\le q^{-1}
\]

while at the terminal point

\[
|\Omega(0,0)|=1.
\]

Let `X` denote the backward stochastic Lagrangian trajectory associated with viscosity `nu`, and let `D` be the stochastic deformation matrix in the Constantin--Iyer stochastic Cauchy representation.

The exact stochastic Cauchy formula has the schematic form

\[
\Omega(0,0)
=
\mathbb E\left[D(0,s_-)\,\Omega(X_{s_-},s_-)\right].
\]

The operator norm of `D` obeys pathwise

\[
\|D(0,s_-)\|_{op}
\le
\exp\left(\int_{s_-}^{0}\|S(X_s,s)\|_{op}\,ds\right),
\]

because the skew part of the velocity gradient does not increase Euclidean vector length.

Therefore the endpoint amplification forces

\[
\boxed{
\mathbb E\exp(A_{\rm str})\ge q,
}
\]

where

\[
A_{\rm str}
:=
\int_{s_-}^{0}\|S(X_s,s)\|_{op}\,ds.
\]

This includes rare stochastic histories automatically; no positive-probability near-mean ancestor hypothesis is required.

---

## 2. Scalar Feynman--Kac envelope

Let

\[
V(x,s)=\|S(x,s)\|_{op}
\]

and let `M` be the scalar Feynman--Kac exponential moment

\[
M(t,x)
=
\mathbb E_{x,t}
\exp\left(\int_0^t V(X_\tau,\tau)\,d\tau\right).
\]

For the divergence-free advection--diffusion semigroup `P_{s,t}`, Duhamel gives

\[
\|M(t)\|_\infty
\le
1
+
C\int_0^t
[\nu(t-s)]^{-3/8}
\|V(s)\|_4
\|M(s)\|_\infty\,ds.
\]

The exponent `3/8` is the `L^4 -> L^infinity` smoothing exponent in three dimensions.

A standard fractional Gronwall / Volterra iteration yields

\[
\boxed{
\log\|M(t)\|_\infty
\lesssim
\nu^{-3/5}
\int_0^t\|V(s)\|_4^{8/5}\,ds.
}
\]

Thus stochastic deformation growth is controlled by the parabolic potential norm

\[
L_t^{8/5}L_x^4.
\]

---

## 3. First-hitting cap converts the potential norm to enstrophy

Calderon--Zygmund for incompressible strain gives

\[
\|S\|_4
\lesssim
\|\Omega\|_4.
\]

Under

\[
\|\Omega\|_\infty\le1,
\]

interpolation gives

\[
\|\Omega\|_4
\le
\|\Omega\|_\infty^{1/2}
\|\Omega\|_2^{1/2}
\le
E_\omega^{1/4},
\]

where

\[
E_\omega(s)=\|\Omega(s)\|_2^2.
\]

Hence

\[
\boxed{
\|S(s)\|_4^{8/5}
\lesssim
E_\omega(s)^{2/5}.
}
\]

For an interval of normalized length

\[
T_I=|I|
\]

and enstrophy action

\[
D_I=\int_I E_\omega(s)\,ds,
\]

Holder in time gives

\[
\int_I E_\omega^{2/5}ds
\le
T_I^{3/5}D_I^{2/5}.
\]

Therefore

\[
\boxed{
\log\mathbb E e^{A_{\rm str}}
\lesssim
\nu^{-3/5}
T_I^{3/5}D_I^{2/5}.
}
\]

Combining with the necessary amplification `E exp(A_str) >= q`, we obtain

\[
\boxed{
\log q
\lesssim
\nu^{-3/5}
T_I^{3/5}D_I^{2/5}.
}
\]

Equivalently,

\[
\boxed{
D_I
\gtrsim
\nu^{3/2}
T_I^{-3/2}
(\log q)^{5/2}.
}
\]

---

## 4. Meaning

The stochastic Cauchy formula removes the deterministic late-injection loophole, but a singular route can still try to place the required deformation on rare stochastic histories.

The present estimate shows that rare histories are not free. They force a scale-critical stochastic strain potential:

\[
\boxed{
\mathcal K_{\rm str}(I)
:=
\nu^{-3/5}
\int_I\|S\|_4^{8/5}ds
\gtrsim
\log q.
}
\]

Under the first-hitting cap this implies the enstrophy-action lower bound above.

Thus stochastic ancestry has only two ways to support a large amplification ratio:

1. a long interval `T_I` over which a moderate strain-Kato potential accumulates; or
2. a shorter interval with correspondingly larger enstrophy / strain concentration.

The second route is the already typed derivative / middle-strain concentration branch.

---

## 5. Criticality audit

This bound does not yet close the problem.

On a parabolic block whose normalized duration is `T_I ~ R^2`, the lower bound is

\[
D_I
\gtrsim
\nu^{3/2}R^{-3}(\log q)^{5/2}.
\]

The existing coherent-flux reset budget can be as large as `D_I ~ R^5`, so the new logarithmic stochastic-Cauchy requirement is compatible with the existing polynomial critical budget.

Therefore the result is a routing theorem, not a contradiction.

What it does close is the untyped "rare stochastic ancestor" loophole:

\[
\boxed{
\text{rare stochastic amplification}
\Longrightarrow
\text{large }L_t^{8/5}L_x^4\text{ strain-Kato action}.
}
\]

---

## 6. Next target

The remaining task is to intersect the stochastic strain-Kato action with the coherent-crossing geometry:

- projective one-axis depletion of local self-stretching;
- finite-energy remote-strain tail;
- local Betchov divergence / shell compensation;
- positive-middle-strain and Hessian channels;
- stochastic ancestor diameter / total-curvature barrier.

A proof-producing improvement would need a strict geometric depletion of the Feynman--Kac potential on coherent stochastic ancestors, not merely a constant-factor sharpening.

Overall status: **RARE STOCHASTIC-HISTORY ESCAPE TYPED INTO A CRITICAL STRAIN-KATO / ENSTROPHY-ACTION BUDGET; CRITICAL SATURATION REMAINS OPEN.**
