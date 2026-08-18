# Packet multiplicity versus scale-separated external strain: a sampling/Bessel energy bound

Date: 2026-08-18

Status: **DERIVED FOR BOUNDED-OVERLAP NATURAL PACKETS AND A LOWER-FREQUENCY RESPONSIBLE STRAIN FIELD. FINITE KINETIC ENERGY FORCES THE RESPONSIBLE STRAIN FREQUENCY TOWARD THE PACKET FREQUENCY AS MULTIPLICITY GROWS. THE `3/5-1/5-4/5` RIDGE REAPPEARS AS THE UNIQUE ONE-CLUSTER BALANCE. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let terminal packet frequency and vorticity scale be

\[
K=\sqrt W,
\qquad
\ell=K^{-1}.
\]

Assume `N` bounded-overlap natural packet cores.

Suppose a lower-frequency velocity field

\[
v=u_{\le L}
\]

supplies a fixed fraction of the order-`K^2` extensional strain needed by the source-active packet population.

Write

\[
\boxed{L=K/R},
\qquad R\ge1.
\]

Thus one responsible strain cell has physical radius `~R/K` and can geometrically cover at most `O(R^3)` bounded-overlap natural packet cells.

## 2. Bandlimited gradient sampling

For an `L`-bandlimited vector field, evaluation of `grad v` at points separated by `c/L` is a Bessel sampling functional. Equivalently, using the translated derivative reproducing kernels and Plancherel,

\[
\boxed{
\sum_{i=1}^M|\nabla v(x_i)|^2
\lesssim
L^5\|v\|_2^2
}
\]

for an `L^-1`-separated family `{x_i}`.

If each selected strain cell supplies

\[
|\nabla v(x_i)|\gtrsim cK^2,
\]

then

\[
M K^4
\lesssim
L^5\|u\|_2^2.
\]

Hence

\[
\boxed{
\|u\|_2^2
\gtrsim
M\frac{K^4}{L^5}
=
M\frac{R^5}{K}.
}
\]

## 3. Count the number of required strain cells

One physical strain cell of radius `R/K` contains at most `C R^3` bounded-overlap natural packet cores. Therefore to serve `N` packet cores one needs at least

\[
\boxed{M\gtrsim N/R^3}
\]

spatially separated responsible strain cells, unless a non-negligible fraction of packets obtains its stretching from higher frequencies rather than `u_{<=L}`.

Substitution gives

\[
\boxed{
\|u\|_2^2
\gtrsim
\frac{N R^2}{K}.
}
\]

Since physical kinetic energy is globally bounded,

\[
\boxed{
R\lesssim C_E\sqrt{\frac K N}.
}
\]

Equivalently the responsible external-strain frequency must satisfy

\[
\boxed{
L\gtrsim c_E\sqrt{NK}.
}
\]

## 4. Recovery of the `3/5-1/5-4/5` ridge

If all `N` packets are to lie in one mesoscopic strain cluster, its normalized radius is

\[
R_{cl}\sim N^{1/3}.
\]

The finite-energy sampling bound requires

\[
N^{1/3}
\lesssim
(K/N)^{1/2}.
\]

Hence

\[
\boxed{N\lesssim K^{3/5}.}
\]

At equality,

\[
\boxed{
N_*\sim K^{3/5},
\qquad
R_*\sim K^{1/5},
\qquad
L_*\sim K^{4/5}.
}
\]

Thus the previously found ridge is not an artifact of choosing one coherent affine cluster. It is also the balance obtained from finite-energy spatial sampling of a scale-separated external strain field.

## 5. Large multiplicity forces scale locality

As `N/K` increases, the maximum allowed scale separation satisfies

\[
R_{max}\sim(K/N)^{1/2}.
\]

Therefore

- for `N~K^(3/5)`, mesoscopic `K^(4/5)` strain is barely energetically possible;
- for `N>>K^(3/5)`, a single mesoscopic cluster is impossible and any external strain must be supplied by more numerous, smaller strain cells;
- as `N` approaches the maximal energy-compatible scale `N~K`, one has `R_max=O(1)`, so the responsible strain must be essentially same-scale.

Hence a high-multiplicity compact cascade is forced toward local high--high interactions rather than a cheap common low-frequency amplifier.

## 6. Complementary branches

The bound applies to the portion of packet stretching supplied by `u_{<=K/R}`. If it fails to account for a fixed fraction of the required stretching, that fraction is supplied by frequencies `>K/R`, which is precisely the increasingly scale-local interaction branch retained in the moving-band analysis.

Critical vorticity-direction roughness may also permit local self-stretch; that branch is retained separately.

Status: **LOW-FREQUENCY SHARED AMPLIFIER QUANTITATIVELY LIMITED / HIGH MULTIPLICITY -> SAME-SCALE INTERACTION / CRITICAL RIDGE RECONFIRMED.**