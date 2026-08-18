# Compact multiplicity deep checkpoint and logarithmic middle-strain cost

Date: 2026-08-18

Status: **DERIVED ON THE COMPACT/NATURAL-SCALE PACKET LANE. PACKET MULTIPLICITY CANNOT GROW FROM A DEEP FIRST-HITTING PRECURSOR WITHOUT LOGARITHMIC SCALE-CRITICAL POSITIVE-MIDDLE-STRAIN ACTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Terminal packet scale

Let the physical first-hitting vorticity level be

\[
W=K^2,\qquad K\to\infty,
\]

so the natural physical length is

\[
\ell=K^{-1}.
\]

Normalize at the terminal level. A natural packet has normalized radius `O(1)` and, by the packet occupancy assumption used in the compact lane, normalized enstrophy bounded below by a fixed constant.

If there are `N` bounded-overlap dangerous packets, then

\[
\boxed{E_c\gtrsim N.}
\]

## 2. Deep compact checkpoint

Choose the earlier first-hitting level

\[
W_-=K,
\]

so the amplitude ratio is

\[
\boxed{q=\frac{W}{W_-}=K.}
\]

Since `K->infinity`, this is still a late checkpoint. In terminal normalization the previous pointwise vorticity cap is

\[
\|\Omega_-\|_\infty\le K^{-1}.
\]

The first-hitting logistic enstrophy ceiling gives

\[
E_-\lesssim \frac{K}{q}=O(1)
\]

(up to the fixed viscosity/initial-energy constants in the established ceiling).

Hence

\[
\boxed{\frac{E_c}{E_-}\gtrsim N.}
\]

## 3. Productive middle-strain action

Use

\[
\frac12E'+\nu P=Q,
\qquad
Q\le2M,
\]

where

\[
M=\int\lambda_2^+|S|^2dx.
\]

As in the established positive-middle-strain lemma,

\[
M\lesssim
\|\lambda_2^+\|_3 E^{1/2}P^{1/2}.
\]

Dividing by `E`, integrating from a minimum-enstrophy time after the deep checkpoint to the terminal packet time, and optimizing over `int P/E`, yields

\[
\boxed{
\int\|\lambda_2^+(s)\|_3^2ds
\gtrsim
\nu\log\frac{E_c}{E_-}.
}
\]

Therefore

\[
\boxed{
\int\|\lambda_2^+\|_3^2ds
\gtrsim c_\nu\log N.
}
\]

This is scale invariant.

## 4. Interpretation

The compact lane cannot increase packet multiplicity merely by spatial replication while keeping the productive strain ledger bounded. If `N->infinity`, the positive-middle-strain critical action must diverge at least logarithmically along the corresponding clean/deep-to-terminal episode.

This does not contradict a hypothetical singularity because the critical middle-strain norm is allowed to diverge. It does, however, remove `slow packet multiplication with bounded productive strain` as an independent escape.

Status: **COMPACT MULTIPLICITY -> LOGARITHMIC CRITICAL MIDDLE-STRAIN ACTION / GLOBAL REGULARITY NOT PROVED.**