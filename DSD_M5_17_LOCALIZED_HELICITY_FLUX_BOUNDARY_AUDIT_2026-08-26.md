# DSD M5-17 — Localized Helicity Flux Boundary Audit

Date: 2026-08-26

Status: **DERIVED LOW-FREQUENCY HELICITY-FLUX BOUND / SPECTRAL LOCALIZATION BREAKS EXACT T_+=T_- BY A BOUNDARY FLUX / VERY LOW FREQUENCIES CANNOT CREATE ORDER-ONE HELICAL MIXING FROM FINITE ENERGY / NO GLOBAL REGULARITY CLAIM.**

## 1. Why localization is necessary

M5-16 is exact on finite prelimit states, but a W1 `1/r` corridor may have logarithmically divergent global `dot H^{1/2}` size. Therefore any transfer of the helical argument to the W1 endpoint must be localized in frequency or physical scale.

Localization destroys the exact global equality `T_+=T_-`: the missing term is a helicity flux through the localization boundary.

## 2. Low-frequency helicity flux

Let `P_{<K}` be a smooth Fourier cutoff to `|k|\lesssim K`, commuting with curl and the helical projectors.

Write

\[
N:=\mathbb P(u\cdot\nabla u).
\]

The nonlinear contribution to low-frequency helicity is, up to the cutoff convention,

\[
\Pi_H^{<K}
:=-2\langle N,\nabla\times P_{<K}^2u\rangle.
\]

Global helicity conservation says the corresponding full-space nonlinear pairing is zero, so this term is exactly a spectral boundary-transfer object.

## 3. Fourier bound from finite energy

The convection term is a divergence:

\[
(u\cdot\nabla)u=\nabla\cdot(u\otimes u).
\]

Hence its Fourier transform satisfies

\[
|\widehat N(k)|
\le
C|k|\,(|\widehat u|*|\widehat u|)(k).
\]

By Cauchy--Schwarz convolution,

\[
(|\widehat u|*|\widehat u|)(k)
\le
\|\widehat u\|_2^2
=\|u\|_2^2.
\]

Therefore

\[
\boxed{
|\widehat N(k)|
\le
C|k|\,\|u\|_2^2.
}
\]

Now

\[
|\Pi_H^{<K}|
\lesssim
\|u\|_2^2
\int_{|k|\lesssim K}|k|^2|\widehat u(k)|\,dk.
\]

Cauchy--Schwarz gives

\[
\int_{|k|\lesssim K}|k|^2|\widehat u(k)|dk
\le
\left(\int_{|k|\lesssim K}|k|^4dk\right)^{1/2}
\|u\|_2
\lesssim
K^{7/2}\|u\|_2.
\]

Thus

\[
\boxed{
|\Pi_H^{<K}(t)|
\le
C K^{7/2}\|u(t)\|_2^3.
}
\]

For an unforced finite-energy solution, the energy inequality bounds `||u(t)||_2` uniformly, hence

\[
\boxed{
\sup_t|\Pi_H^{<K}(t)|\to0
\qquad(K\downarrow0).
}
\]

## 4. DSD interpretation

This distinguishes **boundary storage/transport** from **interior formation**.

Very low physical frequencies cannot create order-one helical mixing through the Euler nonlinearity when the total kinetic energy is finite. Therefore any persistent two-helicity mixture observed in an infrared-normalized W1 boundary sector must be inherited from, or transported out of, a more interior scale range.

This is analogous to earlier pressure/amplitude audits where the far boundary stores/transports a critical defect but is not an independent finite-core source.

## 5. Important scaling audit

The estimate is a physical-frequency statement. Under Leray rescaling, a fixed normalized frequency corresponds to a physical frequency growing like `(T_*-t)^{-1/2}`.

Therefore the limit `K->0` at fixed physical coordinates must not be confused with a fixed Leray-frequency statement near blow-up.

The bound does **not** by itself control the high physical frequencies relevant to singularity formation.

## 6. Consequence for localized helical floors

A localized version of M5-16 has the schematic form

\[
T_+^{window}-T_-^{window}
=\Pi_H^{boundary}.
\]

M5-17 shows that the infrared boundary contribution can be made small at sufficiently low physical frequency from finite energy alone.

What remains uncontrolled is the transfer through critical/high-frequency moving boundaries. That flux is the actual spectral analogue of the M5 cross-scale cascade.

## 7. Updated target

The next useful question is:

> Can the critical/high-frequency helicity boundary flux be controlled by the same `K`-tail or by the cross-radius coherence constraints, without assuming the desired tail smallness?

If yes, M5-16 could be upgraded to a scale-local two-helicity floor.
If not, the high-frequency helicity flux is another equivalent representation of the unresolved M5 bridge.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
