# Compact packet: critical angular roughness versus mesoscopic external-strain cluster

Date: 2026-08-18

Status: **DERIVED AS A GEOMETRIC DECOMPOSITION OF THE COMPACT NATURAL-PACKET LANE. A NATURAL PACKET CANNOT BOTH HAVE SUBCRITICAL VORTICITY-DIRECTION ROUGHNESS AND SELF-SUPPLY ORDER-W STRETCHING. IF SELF-STRETCH IS DEPLETED, ORDER-W EXTERNAL STRAIN MUST COME FROM A MESOSCOPIC CLUSTER, UNLESS AN EXTRA GLOBAL ENSTROPHY RESERVOIR IS PRESENT. GLOBAL REGULARITY NOT PROVED.**

## 1. Natural scale

Write

\[
W=K^2,
\qquad
\ell=K^{-1}.
\]

At a high-vorticity point let

\[
\xi=\omega/|\omega|.
\]

Assume on the natural high-vorticity neighborhood that

\[
|\sin\angle(\xi(x),\xi(y))|
\le
G|x-y|^{1/2}.
\]

The exponent `1/2` is the critical vorticity-direction coherence exponent in the classical geometric-depletion theory.

## 2. Local self-stretch bound

The Biot--Savart representation of vortex stretching contains the vorticity-direction angle factor. Restricting to the natural ball and using `|omega|<=W`,

\[
|\xi(x)^TS_{self}(x)\xi(x)|
\lesssim
W\int_0^\ell G\rho^{1/2}\frac{d\rho}{\rho}
\lesssim
WG\ell^{1/2}.
\]

Therefore

\[
\boxed{
|\xi^TS_{self}\xi|
\lesssim
K^{3/2}G.
}
\]

For self-stretch to have the natural first-hitting size `~W=K^2`, it is necessary that

\[
\boxed{G\gtrsim K^{1/2}.}
\]

Thus

\[
G=o(K^{1/2})
\]

forces the order-`W` extensional strain to come predominantly from outside the natural packet.

This does not invoke the vorticity-direction regularity theorem as a proof of regularity; it uses only the same Biot--Savart angle depletion mechanism and identifies the critical scaling.

## 3. Far-strain localization under packet-dominant enstrophy

Assume the `N` natural packets carry the relevant terminal enstrophy up to a fixed factor,

\[
E_{phys}\lesssim C NK.
\]

For `r=R/K`, the absolutely convergent far part of the strain satisfies

\[
|S_{>r}(x)|
\lesssim
\int_{|x-y|>r}\frac{|\omega(y)|}{|x-y|^3}dy.
\]

Cauchy--Schwarz gives

\[
|S_{>r}(x)|
\lesssim
E_{phys}^{1/2}r^{-3/2}.
\]

Hence

\[
\boxed{
|S_{>R/K}(x)|
\lesssim
N^{1/2}K^2R^{-3/2}.
}
\]

If the external field is to contribute a fixed fraction of `K^2`, one must have

\[
\boxed{R\lesssim C N^{1/3}.}
\]

Equivalently the responsible external strain lies within physical radius

\[
\boxed{
r_{cluster}\lesssim C\frac{N^{1/3}}{K}.
}
\]

## 4. Resulting compact-lane trichotomy

A packet-dominant compact multiplicity realization therefore satisfies at least one of

\[
\boxed{G\gtrsim K^{1/2}}
\]

(critical vorticity-direction roughness),

\[
\boxed{r_{cluster}\lesssim N^{1/3}/K}
\]

(mesoscopic interacting packet cluster), or

\[
\boxed{E_{phys}\gg NK}
\]

(an additional global enstrophy reservoir beyond the counted packet sector).

When `N->infinity`, the mesoscopic cluster has terminal-normalized radius

\[
R_{cluster}\sim N^{1/3}\to\infty.
\]

Thus even the compact packet lane regenerates a large-radius geometric scale unless it pays critical angular roughness or a separate enstrophy reservoir.

## 5. Limitation

A large mesoscopic cluster need not be coherent. Different packet orientations may keep the parent Gaussian residual variance order one. Hence this lemma does not by itself place the cluster into the previously derived low-variance coherent affine fixed point. The next question is whether a large noncoherent cluster must pay projective/angular scale increments strongly enough to prevent repeated regeneration.

Status: **COMPACT PACKET SELF-STRETCH TYPED / SUBCRITICAL ANGULAR ROUGHNESS -> MESOSCOPIC EXTERNAL-STRAIN CLUSTER OR ENSTROPHY RESERVOIR / GLOBAL REGULARITY NOT PROVED.**