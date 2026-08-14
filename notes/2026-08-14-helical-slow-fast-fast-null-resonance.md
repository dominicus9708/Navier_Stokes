# Helical slow-fast-fast null resonance

Date: 2026-08-14

Status: **EXACT ALGEBRAIC CANCELLATION FOR FROZEN RAPID ROTATION. A STRICTLY SLOW OUTPUT MODE CANNOT RECEIVE LEADING-ORDER RESONANT FORCING FROM TWO FAST MODES. NEAR-RESONANCE AND GAUSSIAN LOCALIZATION REMAIN. GLOBAL REGULARITY NOT PROVED.**

## 1. Helical basis

Fix the coherent mean-vorticity axis `e`. For each nonzero Fourier wave vector `k`, use helical eigenvectors

\[
h_s(k),\qquad s\in\{+1,-1\},
\]

satisfying

\[
 i k\times h_s(k)=s|k|h_s(k),
\qquad
k\cdot h_s(k)=0.
\]

For rigid rotation about `e`, the projected Coriolis operator is diagonal in this basis, with inertial-wave frequency, up to the fixed background angular-frequency constant,

\[
\boxed{
\omega_s(k)=s\frac{k_\parallel}{|k|},
\qquad
k_\parallel=k\cdot e.
}
\]

A mode is `slow` when `k_parallel=0` and `fast` when `k_parallel != 0`.

## 2. Helical quadratic coefficient

For a triad

\[
k+p+q=0,
\]

the incompressible Euler/Navier--Stokes quadratic coefficient for the output helical amplitude contains the factor

\[
\boxed{
s_p|p|-s_q|q|}
\]

multiplying a bounded geometric triple product of the three helical polarization vectors.

Only this factor is needed for the cancellation below.

## 3. Exact fast-fast resonance into a slow output

Assume the output `k` is slow:

\[
k_\parallel=0.
\]

Triad closure gives

\[
p_\parallel+q_\parallel=0.
\]

Suppose both inputs are fast, so

\[
p_\parallel\neq0,
\qquad
q_\parallel\neq0.
\]

The exact temporal resonance condition is

\[
\omega_{s_p}(p)+\omega_{s_q}(q)-\omega_{s_k}(k)=0.
\]

Since the output frequency vanishes,

\[
s_p\frac{p_\parallel}{|p|}
+s_q\frac{q_\parallel}{|q|}=0.
\]

Using `q_parallel=-p_parallel`,

\[
p_\parallel
\left(
\frac{s_p}{|p|}-\frac{s_q}{|q|}
\right)=0.
\]

Because `p_parallel != 0`,

\[
\frac{s_p}{|p|}
=
\frac{s_q}{|q|}.
\]

As `|p|,|q|>0` and `s_p,s_q` are signs, this forces

\[
\boxed{
s_p=s_q,\qquad |p|=|q|.}
\]

Therefore the helical coupling factor vanishes:

\[
\boxed{
s_p|p|-s_q|q|=0.}
\]

Hence

\[
\boxed{
\text{strictly slow output}
\leftarrow
\text{fast} + \text{fast exact resonance}
=0.
}
\]

This is an algebraic null form, not merely a time-averaging estimate.

## 4. Slow-slow-slow branch

If `p_parallel=0`, then triad closure with `k_parallel=0` gives

\[
q_\parallel=0.
\]

Thus the remaining exact resonances feeding a strictly slow output are slow-slow-slow interactions.

The strictly slow velocity field depends only on the two coordinates perpendicular to `e`. Its horizontal part obeys two-dimensional incompressible dynamics and its component parallel to `e` is transported by that two-dimensional flow. In particular the slow vertical/axial vorticity has no three-dimensional vortex-stretching source capable of generating the terminal first-hitting amplification by itself.

Thus the two exact-resonance possibilities for a slow output are:

1. fast-fast input: coupling coefficient vanishes;
2. slow-slow input: reduced two-dimensional/2D3C dynamics, with no axial 3D stretching mechanism.

## 5. Quantitative near-slow identity

Let the output be nearly slow rather than exactly slow. Write

\[
k_\parallel+p_\parallel+q_\parallel=0
\]

and define the phase mismatch

\[
\Phi
=
 s_p\frac{p_\parallel}{|p|}
+s_q\frac{q_\parallel}{|q|}
-s_k\frac{k_\parallel}{|k|}.
\]

Consider the only helical sign branch that can approach the slow fast-fast resonance, namely

\[
s_p=s_q=s.
\]

Set

\[
d=s|p|-s|q|=s(|p|-|q|).
\]

Using

\[
q_\parallel=-p_\parallel-k_\parallel,
\]

we obtain

\[
\Phi
=
 s p_\parallel
\left(\frac1{|p|}-\frac1{|q|}\right)
-k_\parallel
\left(\frac{s}{|q|}+\frac{s_k}{|k|}\right).
\]

Since

\[
\frac1{|p|}-\frac1{|q|}
=
-\frac{|p|-|q|}{|p||q|}
=-\frac{s d}{|p||q|},
\]

we get the exact identity

\[
\boxed{
 d
=
-\frac{|p||q|}{p_\parallel}
\left[
\Phi
+k_\parallel
\left(
\frac{s}{|q|}+\frac{s_k}{|k|}
\right)
\right].
}
\]

Therefore, on a turnover-scale spectral block where

\[
|p|+|q|+|k|\asymp1,
\qquad
|p_\parallel|\ge\delta_f>0,
\]

we have

\[
\boxed{
|s_p|p|-s_q|q||
\lesssim_{\delta_f}
|\Phi|+\frac{|k_\parallel|}{|k|}.
}
\]

Thus the same factor that vanishes at exact slow resonance is quantitatively small for simultaneously near-resonant and near-slow output, provided the two inputs remain uniformly fast.

## 6. Opposite-helicity branch

If

\[
s_p=-s_q,
\]

then for a strictly slow output the fast-fast resonance equation would require

\[
p_\parallel
\left(
\frac{s_p}{|p|}+rac{s_p}{|q|}
\right)=0,
\]

which is impossible for `p_parallel != 0`.

Hence the opposite-helicity fast-fast branch is uniformly nonresonant away from the slow-input cone. Its long-time contribution is handled by oscillatory integration rather than the null coupling factor.

## 7. Endgame trichotomy

For a candidate secular forcing of the coherent slow/near-slow mean-vorticity core, every quadratic interaction is now routed into one of three classes:

### A. Nonresonant

\[
|\Phi|\not\ll1.
\]

Fast rotation gives an oscillatory time-integration gain.

### B. Near-resonant with uniformly fast inputs

\[
|\Phi|\ll1,
\qquad
|p_\parallel|/|p|\ge\delta_f.
\]

The helical coupling itself has the null-form gain

\[
|C_{kpq}|
\lesssim
|\Phi|+|k_\parallel|/|k|.
\]

### C. Near-slow input concentration

At least one input has

\[
|p_\parallel|/|p|\ll1.
\]

Then triad closure and near resonance push the interaction toward the slow 2D3C sector. This is the only part not controlled merely by the exact fast-fast null form.

## 8. Remaining analytic target

The generic exact-resonant escape is closed algebraically. The remaining bounded-affine low-Hermite problem is reduced to a quantitative localization statement:

\[
\boxed{
\text{near-resonant width}
+\text{near-slow spectral concentration}
+\text{Gaussian localization commutator}.
}
\]

A complete closure would follow from any estimate showing that these three remainders contribute `o(R_m^-2)` to the signed mean-vorticity source over the `R_m^2` mean-creation interval, or incur a non-summable projective/high-Hermite/palinstrophy cost.

Status: **EXACT SLOW-FAST-FAST RESONANCE REMOVED BY HELICAL NULL COUPLING / REMAINING RESONANT ESCAPE = NEAR-SLOW OR NEAR-RESONANT LOCALIZATION / GLOBAL REGULARITY NOT PROVED.**
