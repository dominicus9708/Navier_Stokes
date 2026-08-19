# Remote strain H^{-1} gate and the W^{1/10} radius barrier

Date: 2026-08-19

Status: **DERIVED DUALITY BOUND / UNCONDITIONAL ACTIVE-HALO ENERGY RADIUS BARRIER / GLOBAL REGULARITY NOT PROVED**.

This note strengthens the active-halo radius packing estimate without assuming bounded normalized palinstrophy.

---

## 1. Strain as a homogeneous order-zero vorticity operator

For whole-space incompressible flow,

\[
S=\nabla_{\rm sym}U
\]

is a Calderon--Zygmund transform of vorticity `Omega`. At a core point, write schematically

\[
S_{ij}(x)
=\operatorname{p.v.}\int
K_{ij\ell}(x-y)\Omega_\ell(y)dy,
\]

where

\[
K(z)=|z|^{-3}\mathcal K(z/|z|)
\]

is homogeneous of degree `-3`.

Fix a smooth annular cutoff `chi_R` supported on

\[
R\le |y|\le 2R
\]

with the usual derivative scaling. For `x` in a fixed core `B_R0` with `R >> R0`, define the shell kernel

\[
K_{R,x}(y)=\chi_R(y)K(x-y).
\]

---

## 2. Shell kernel H1 scaling

On the remote shell,

\[
|K_{R,x}|\lesssim R^{-3},
\qquad
|\nabla_yK_{R,x}|\lesssim R^{-4}.
\]

The shell volume is `O(R^3)`, hence

\[
\boxed{
\|K_{R,x}\|_{\dot H^1_y}
\lesssim
R^{-5/2}.
}
\]

The estimate is uniform for `x` in a fixed bounded core.

---

## 3. Divergence-free H^{-1} identity

Since

\[
\Omega=\nabla\times U,
\qquad
\nabla\cdot U=0,
\]

Fourier space gives

\[
|\widehat\Omega(k)|=|k|\,|\widehat U(k)|.
\]

Therefore

\[
\boxed{
\|\Omega\|_{\dot H^{-1}}
=\|U\|_2
=K_U^{1/2}.
}
\]

By `H^{-1}`--`H^1` duality,

\[
\begin{aligned}
|S_R(x)|
&=|\langle\Omega,K_{R,x}\rangle|\\
&\le
\|\Omega\|_{\dot H^{-1}}
\|K_{R,x}\|_{\dot H^1}.
\end{aligned}
\]

Hence

\[
\boxed{
\|S_R\|_{L^\infty(B_{R_0})}
\lesssim
R^{-5/2}K_U^{1/2}.
}
\]

This is stronger for coherent remote influence than the earlier `L2`-enstrophy estimate because it measures precisely the low angular/frequency content capable of producing strain at the core.

---

## 4. Active shell requires R^5 normalized kinetic energy

If the shell is active in the sense

\[
\|S_R\|_{L^\infty(B_{R_0})}
\ge\sigma_0>0,
\]

then

\[
\boxed{
K_U
\gtrsim
\sigma_0^2R^5.
}
\]

Thus large remote vorticity occupancy is not enough: the shell must also carry a coherent `H^{-1}` component large enough to survive the cancellations of the strain kernel.

---

## 5. Physical kinetic-energy bound gives W^{1/10}

Dynamic normalization gives

\[
K_U
=W^{1/2}\|u(t)\|_2^2.
\]

The physical kinetic energy is nonincreasing, so

\[
K_U\le K_0W^{1/2}.
\]

Combining with the active-shell lower bound,

\[
\sigma_0^2R^5
\lesssim
K_0W^{1/2}.
\]

Therefore every order-one active remote shell satisfies

\[
\boxed{
R
\lesssim
K_0^{1/5}\sigma_0^{-2/5}W^{1/10}.
}
\]

This is an unconditional instantaneous radius barrier for remote strain coupling.

It improves the `W^(1/6)` radius obtained from time-integrated energy dissipation. It does not require a persistence-time assumption.

---

## 6. Combined hierarchy of active-halo radius bounds

The present route now has three nested bounds.

### Time-integrated activity

For order-one duration active coupling,

\[
R=o(W^{1/6})
\]

along an infinitely repeated finite-energy subsequence.

### Instantaneous kinetic-energy duality

For any order-one active shell,

\[
\boxed{R\lesssim W^{1/10}.}
\]

### Derivative-controlled active shell

If normalized palinstrophy is also uniformly bounded, the interpolation gate gives

\[
\boxed{R\lesssim W^{1/12}.}
\]

Thus the genuinely difficult active-halo sector is no longer arbitrary non-tightness but an intermediate shell constrained to

\[
\boxed{
1\ll R\lesssim W^{1/10}
}
\]

unconditionally, and to `R <= O(W^(1/12))` on the bounded-palinstrophy branch.

---

## 7. Interpretation boundary

The endpoint critical `L^3` theorem still forces some global non-tightness along a singular sequence. The present result does not forbid a very distant **passive** critical halo. It says that such a halo cannot produce order-one strain in the tracked core unless it lies inside the `W^(1/10)` active radius or violates the physical kinetic-energy bound.

Hence global critical non-tightness and active local production are increasingly separated into distinct sectors.

Status: **ORDER-ONE REMOTE STRAIN COUPLING CONFINED TO R <= O(W^(1/10)) BY H^{-1} DUALITY; PASSIVE FAR CRITICAL HALO REMAINS POSSIBLE.**