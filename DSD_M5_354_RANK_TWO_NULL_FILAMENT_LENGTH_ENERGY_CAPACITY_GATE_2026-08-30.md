# DSD M5-354 — Rank-Two Null-Filament Length / Finite-Energy Capacity Gate

Date: 2026-08-30

Status: **RANK-DEFICIENT SHAPE ESCAPE QUANTIFIED / FIXED-VOLUME MATERIAL POPULATION REQUIRES NULL-AXIS LENGTH `L >= c sigma1 sigma2 V^2/E0` / EXACT CRITICAL AFFINE MODEL FORCES `L(t)~(T-t)^(-2)` OR TURNOVER / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

Let `M` be rank two with singular values

\[
\sigma_1\ge\sigma_2>0,
\qquad
\sigma_3=0.
\]

Choose singular coordinates so the third axis is the null direction.

Consider a coherent material ellipsoid with semiaxes

\[
a_1,a_2,L
\]

along the three singular directions.

Its volume satisfies

\[
\boxed{V\asymp a_1a_2L.}
\]

The affine velocity after subtracting translation is `u=Mx`.

## 2. Affine energy

By the same ellipsoid calculation as M5-352,

\[
E_{aff}
\asymp
V(\sigma_1^2a_1^2+\sigma_2^2a_2^2),
\]

because the null-axis contribution vanishes.

For fixed `V` and `L`,

\[
a_1a_2\asymp\frac{V}{L}.
\]

Minimize

\[
\sigma_1^2a_1^2+\sigma_2^2a_2^2
\]

under this product constraint.

The minimum occurs when

\[
\sigma_1a_1=\sigma_2a_2.
\]

Then

\[
\boxed{
\sigma_1^2a_1^2+\sigma_2^2a_2^2
\gtrsim
\sigma_1\sigma_2\frac{V}{L}.
}
\]

Therefore

\[
\boxed{
E_{aff}
\gtrsim
\frac{\sigma_1\sigma_2V^2}{L}.
}
\]

This is the rank-two analogue of the full-rank determinant bound.

## 3. Finite-energy length requirement

If the entire flow has kinetic energy at most `E0`, then any such affine material population must obey

\[
E_0
\ge
E_{aff}
\gtrsim
\frac{\sigma_1\sigma_2V^2}{L}.
\]

Hence

\[
\boxed{
L
\gtrsim
\frac{\sigma_1\sigma_2V^2}{E_0}.
}
\]

Thus rank deficiency does not remove the energy cost. It converts it into a required growth of the null-axis extent.

## 4. Apply to the exact M5-353 model

In M5-353,

\[
M(t)=a(t)M_0,
\]

where `M0` is a fixed rank-two matrix and

\[
a(t)=\frac1{T-t}.
\]

Therefore the two nonzero singular values satisfy

\[
\sigma_i(t)=a(t)\sigma_i(M_0),
\]

so

\[
\boxed{
\sigma_1(t)\sigma_2(t)
\asymp
(T-t)^{-2}.
}
\]

For one fixed coherent material population of volume `V_mat>0`,

\[
\boxed{
L(t)
\gtrsim
\frac{V_{mat}^2}{E_0}(T-t)^{-2}.
}
\]

Thus the null-axis length must diverge as the singular time is approached.

## 5. Natural-scale form

For the critical-clock affine model,

\[
r(t)\asymp\sqrt{T-t}.
\]

Hence

\[
\boxed{
L(t)\gtrsim c(V_{mat},E_0)r(t)^{-4}.
}
\]

The active transverse natural scale shrinks like `r`, while the null-axis extent required to preserve the same material volume and finite energy grows like `r^{-4}`.

This is an extreme aspect-ratio divergence.

## 6. Formation consequence

A persistent rank-two affine material lineage has only three possibilities:

### A. Spatial filament escape

The same material population remains coherent and stretches to the required null-axis length.

Then

\[
\boxed{L(t)\to\infty,}
\]

which is a direct spatial non-tightness / remote-filament `T` branch.

### B. Fragmentation

The material population breaks into disconnected pieces so no single coherent filament carries the full volume.

This is structural/material reformation and belongs to `T_dynamic`.

### C. Occupancy loss/replacement

The old population ceases to occupy the affine state and new material takes its place.

Again this is fixed-fraction turnover.

Thus

\[
\boxed{
\text{rank-two affine persistence}
\Longrightarrow
T_{spatial}
\lor
T_{fragment/replacement}.
}
\]

provided a fixed positive material population is tracked.

## 7. Axis-property meaning

The null axis is the only direction along which affine kinetic energy does not grow quadratically with distance.

Finite energy therefore tries to store material by sending it farther along that axis.

This converts an algebraic rank deficiency into a geometric requirement:

\[
\boxed{
\text{zero-gradient axis}
\Longrightarrow
\text{diverging support length}.
}
\]

The axis-property framework is useful here because the relevant escape is not a generic large radius; it is specifically aligned with the null singular direction of `grad u`.

## 8. Firewall

The length estimate is for a coherent material population of fixed volume. If the population itself is continually replaced, the volume need not be preserved lineage-by-lineage; that is precisely the turnover alternative.

The calculation does not by itself contradict spatial non-tightness. It routes the rank-two shape branch into an already identified `T` mechanism.

## 9. Updated affine frontier

Combining M5-351, M5-352, M5-353 and M5-354:

\[
\boxed{
\text{energy-bearing affine dual-hyperbolic branch}
\Longrightarrow
T_{dynamic}
\lor
T_{spatial}
\lor
H_{micro/occupancy}.
}
\]

Full-rank anisotropy and rank-two null-axis anisotropy are no longer independent terminal leaves.

## 10. Audit verdict

### PROVED

- optimal rank-two affine energy lower bound;
- required null-axis filament length;
- exact critical affine model requires `L~(T-t)^(-2)` for fixed material volume;
- rank-two persistence routes to spatial escape or turnover.

### OPEN

- massless/vanishing-occupancy microstructure;
- global contradiction for repeated turnover/spatial escape;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]