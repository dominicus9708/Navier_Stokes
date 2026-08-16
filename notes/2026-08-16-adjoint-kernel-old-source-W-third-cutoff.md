# Finite kinetic-energy dissipation removes stretching sources older than a `W^(1/3+)` normalized horizon

Date: 2026-08-16

Status: **EXACT ADJOINT-KERNEL TAIL ESTIMATE USING THE DRIFT-INDEPENDENT HEAT-KERNEL CEILING AND THE GLOBAL ENERGY-DISSIPATION BUDGET. THE `W^(1/3)` TEMPORAL SCALE REAPPEARS INDEPENDENTLY OF THE EARLIER ADAPTIVE CHECKPOINT DESIGN. GLOBAL REGULARITY NOT PROVED.**

## 1. Exact vorticity Duhamel representation

Fix a terminal normalized spacetime point and write backward age as `tau`. The scalar adjoint advection--diffusion kernel `K_tau` gives the exact vector representation

\[
\Omega_T(x_*)
=P_{0,T}\Omega(s_0)(x_*)
+
\int_0^{T-s_0}
P_{T-\tau,T}(S\Omega)(x_*)d\tau.
\]

For the source term we use only the scalar kernel ceiling, valid for divergence-free advection,

\[
\boxed{
\|K_\tau\|_\infty
\lesssim
(\nu\tau)^{-3/2}.
}
\]

---

## 2. L1 size of the stretching source

By Cauchy--Schwarz and the exact `L2` strain/vorticity equivalence,

\[
\|S\Omega\|_1
\le
\|S\|_2\|\Omega\|_2
\lesssim
E,
\]

where

\[
E=\|\Omega\|_2^2.
\]

Hence a source slice of age `tau` contributes at most

\[
C(\nu\tau)^{-3/2}E(T-\tau).
\]

---

## 3. Old-source tail

For a cutoff age `L>0`, define

\[
I_{\rm old}(L)
=\int_L^{T-s_0}
P_{T-\tau,T}(S\Omega)(x_*)d\tau.
\]

Then

\[
\begin{aligned}
|I_{\rm old}(L)|
&\lesssim
\nu^{-3/2}
\int_L^{T-s_0}
\tau^{-3/2}E(T-\tau)d\tau\\
&\le
C\nu^{-3/2}L^{-3/2}
\int E(s)ds.
\end{aligned}
\]

The terminal normalization satisfies

\[
E_{\rm norm}(s)=W^{-1/2}E_{\rm phys}(t),
\qquad ds=Wdt.
\]

The physical kinetic-energy identity gives

\[
\nu\int E_{\rm phys}(t)dt
\le
\frac12\|u_0\|_2^2.
\]

Therefore

\[
\boxed{
\int E_{\rm norm}(s)ds
\lesssim_\nu
W^{1/2}\|u_0\|_2^2.
}
\]

Consequently

\[
\boxed{
|I_{\rm old}(L)|
\lesssim
C_{\nu,u_0}
W^{1/2}L^{-3/2}.
}
\]

---

## 4. The one-third temporal cutoff

Choose

\[
\boxed{
L=W^{1/3+\delta},
\qquad \delta>0.
}
\]

Then

\[
W^{1/2}L^{-3/2}
=
W^{-3\delta/2}.
\]

Hence

\[
\boxed{
I_{\rm old}(W^{1/3+\delta})
=o(1).
}
\]

Thus order-one terminal vorticity cannot be generated directly by stretching source older than `W^(1/3+delta)` normalized time.

This conclusion does not assume Gaussianity, affine structure, coherent geometry, or bounded kernel deformation.

---

## 5. Relation to the clean precursor lifespan

The clean minimum-enstrophy checkpoint satisfies, for fixed `0<beta<4`,

\[
s_c-s_m
\gtrsim
\nu^3\frac{W}{R^{2\beta}}.
\]

Using the crossing energy bound `R <= C W^(1/10)` gives

\[
s_c-s_m
\gtrsim
W^{1-\beta/5}
\]

up to fixed constants/logarithms in the worst power-law case.

For example, with `beta=2`,

\[
s_c-s_m
\gtrsim W^{3/5},
\]

which is much larger than

\[
W^{1/3+\delta}
\]

for every fixed sufficiently small `delta<4/15`.

Therefore the clean precursor can lie far outside the actual terminal source-active horizon. The stochastic Cauchy inheritance from that precursor is then realized through long deformation/history, while the *fresh stretching production* of the terminal value is concentrated much later.

---

## 6. Independent reappearance of the W^(1/3) scale

Earlier the adaptive checkpoint ratio slightly above `W^(1/3)` arose from residual-memory and shell-density balances.

The present derivation reaches the same exponent from a different calculation:

\[
\boxed{
\text{kernel ceiling }\tau^{-3/2}
\times
\text{normalized total enstrophy budget }W^{1/2}.
}
\]

The threshold for the product to vanish is exactly

\[
L\gg W^{1/3}.
\]

Thus the one-third exponent is not only a bookkeeping choice; it is also the natural old-source cutoff for pointwise vorticity generation under the global energy budget.

---

## 7. What remains inside the recent layer

The exact adjoint identity now has the form

\[
\Omega_T(x_*)
=
\text{transported precursor term}
+
\int_0^{W^{1/3+\delta}}
P(S\Omega)d\tau
+o(1).
\]

If the precursor term is small at the terminal point, an order-one source must therefore occur inside the recent layer.

The existing kernel weighted-enstrophy routing then gives the alternatives

\[
\boxed{
\text{mesoscopic enstrophy-time occupancy}
\quad\lor\quad
\text{terminal enstrophy concentration / positive-middle-strain escalation}.
}
\]

The present note does not show that the recent-layer cost is non-summable across an infinite first-hitting cascade.

Overall status: **STRETCHING SOURCE OLDER THAN `W^(1/3+)` IS POINTWISE NEGLIGIBLE / SOURCE-ACTIVE ENDGAME TEMPORALLY LOCALIZED TO THE RECENT ONE-THIRD HORIZON.**
