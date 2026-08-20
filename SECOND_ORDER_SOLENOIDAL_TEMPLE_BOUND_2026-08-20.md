# Second-Order Solenoidal Temple Bound — 2026-08-20

Status: **FINITE-MOMENT BRANCH ONLY — GLOBAL REGULARITY NOT PROVED.**

This note strengthens the whole-space finite-second-moment radius estimate after `RADIUS_BARRIER_SCOPE_CORRECTION_2026-08-20.md`.

Let

\[
Z=\|\omega\|_2^2,
\qquad
M=\int |x|^2|\omega|^2dx,
\qquad
D=\|\Delta\omega\|_2^2,
\]

with `div omega = 0` and all three finite.

Define the direct second-order solenoidal constant

\[
\mathcal C_{2,sol}
=
\inf
\frac{M\sqrt D}{Z^{3/2}}.
\]

The previous Hamamoto-plus-Cauchy estimate gives only

\[
\mathcal C_{2,sol}\ge25/4=6.25.
\]

## 1. Fourier/tangential reduction

In Fourier space, `k dot omega_hat = 0`, so the field is tangential on every frequency sphere. The lowest tangential vector-spherical-harmonic sector is `ell=1`. Its radial quotient reduces, after `g(r)=r f(r)`, to

\[
Z=\int_0^\infty |g|^2dr,
\]

\[
M=\int_0^\infty\left(|g'|^2+2r^{-2}|g|^2\right)dr,
\]

\[
D=\int_0^\infty r^4|g|^2dr.
\]

Let

\[
\mathcal H=-d^2/dr^2+2/r^2+r^4
\]

and let `lambda_0` be its ground-state eigenvalue. Scaling of the radial problem gives

\[
\boxed{
\mathcal C_{2,sol}
=\frac{2}{3\sqrt3}\lambda_0^{3/2}.
}
\]

## 2. Explicit Temple lower bound

Set

\[
q=5^{1/3},
\qquad a=q^2.
\]

Using

\[
r^4=a r^2-a^2/4+(r^2-a/2)^2,
\]

write

\[
\mathcal H=\mathcal H_0+V,
\]

with

\[
\mathcal H_0=-d^2/dr^2+2/r^2+a r^2-a^2/4,
\]

\[
V=(r^2-a/2)^2\ge0.
\]

The first two `ell=1` oscillator eigenvalues are

\[
E_0=15q/4,
\qquad
E_1=31q/4.
\]

For the normalized ground state

\[
g_0(r)\propto r^2e^{-q r^2/2},
\]

direct Gamma moments give

\[
\langle V\rangle=q/2,
\qquad
\operatorname{Var}(V)=11/(2q).
\]

Thus the trial energy is

\[
\mu=17q/4<E_1.
\]

Temple's inequality yields

\[
\lambda_0
\ge
\mu-
\frac{\operatorname{Var}(V)}{E_1-\mu}
=
\frac{551}{140}5^{1/3}
\approx6.7299767616.
\]

Therefore

\[
\boxed{
\mathcal C_{2,sol}
\ge6.7199874273.
}
\]

This is a strict explicit improvement over `6.25`.

## 3. Consequence for the P_V H1 quotient

The vorticity-Hessian estimate is

\[
\eta_{VI}
\le
\sqrt{3/2}\,\|\omega\|_\infty\sqrt{Z/D}.
\]

The direct second-order inequality gives

\[
\sqrt{Z/D}
\le
R_\omega^2/\mathcal C_{2,sol},
\qquad
R_\omega^2=M/Z.
\]

Hence

\[
\boxed{
\eta_{VI}
\le
0.1822540421\,
\|\omega\|_\infty R_\omega^2.
}
\]

At first hitting, `||omega||_infinity = 1`, so

\[
\eta_{VI}\ge\nu
\]

implies

\[
\boxed{
R_{\omega,global}
\ge2.3424019207\sqrt\nu.
}
\]

This is a whole-field finite-second-moment statement. It is **not** yet an active-core radius bound. A core-tail comparison or Bogovskii-localized second-order estimate is still required before comparing this number to the non-`T` active-core upper radius.

A numerical finite-difference solve of the radial operator gives `lambda_0 ~ 7.10844`, suggesting a possible sharp radius near `2.4405*sqrt(nu)`, but the rigorous result recorded here is only `2.3424019207*sqrt(nu)`.
