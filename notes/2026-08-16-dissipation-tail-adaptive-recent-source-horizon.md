# Dissipation-tail adaptive recent-source horizon and parabolic saturation

Date: 2026-08-16

Status: **DERIVED ADAPTIVE OLD-SOURCE CUTOFF. THE MINIMAL RECENT SOURCE HORIZON IS FORCED DOWN TO, BUT NOT BELOW, THE COHERENT-CORE PARABOLIC SCALE ON THE MINIMAL-DISSIPATION BRANCH. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let `t_j -> T*` be coherent first-hitting crossing times with terminal amplitude scale `W_j -> infinity` and coherent normalized radius `R_j -> infinity`.

The physical coherent-core radius is

\[
\ell_j=\frac{R_j}{\sqrt{W_j}}.
\]

Hence its physical parabolic time is

\[
\boxed{\ell_j^2=R_j^2/W_j.}
\]

The terminal-normalized enstrophy is

\[
E_j(s)=\|\Omega_j(s)\|_2^2,
\]

and physical and normalized enstrophy-time are related by

\[
\int E_j(s)\,ds
=\sqrt{W_j}\int\|\omega(t)\|_2^2dt.
\]

## 2. Split old history using the finite dissipation tail

Choose

\[
H_j=W_j^{-1/2},
\qquad
a_j=t_j-H_j.
\]

Then `H_j -> 0`, so `a_j -> T*`, while the normalized backward age of `a_j` is

\[
A_j=W_jH_j=W_j^{1/2}\to\infty.
\]

Let

\[
d_j:=\int_{a_j}^{T^*}\|\omega(t)\|_2^2dt.
\]

Finite kinetic-energy dissipation gives

\[
\boxed{d_j\to0.}
\]

For a pointwise adjoint kernel ending at the crossing point, the old source is split into:

1. `t <= a_j`, whose normalized age is at least `A_j`;
2. `a_j < t <= t_j-h`, whose total physical enstrophy-time is at most `d_j`.

The scalar adjoint-kernel ceiling is

\[
\|K(\tau)\|_\infty\lesssim_\nu \tau^{-3/2},
\]

and

\[
\|S\Omega\|_1\lesssim E.
\]

Therefore the first part is bounded by

\[
C\sqrt{W_j}A_j^{-3/2}
=CW_j^{-1/4}=o(1).
\]

If

\[
L_j=W_jh_j
\]

is the normalized recent horizon, the middle part is bounded by

\[
\boxed{C\sqrt{W_j}\,d_j\,L_j^{-3/2}.}
\]

Thus, for any arbitrarily slowly diverging `g_j -> infinity`, the choice

\[
\boxed{
L_j
=g_j\big(\sqrt{W_j}d_j\big)^{2/3}
}
\]

makes all source older than `L_j` negligible.

Equivalently,

\[
\boxed{
h_j
=g_j\,d_j^{2/3}W_j^{-2/3}.}
\]

This improves the crude universal `W^(1/3+)` normalized cutoff by using the vanishing physical dissipation tail.

## 3. Terminal coherent occupancy supplies the opposite inequality

At the coherent crossing,

\[
E_j(t_j)\gtrsim R_j^3.
\]

The first-hitting cap gives

\[
E_j'\le CE_j,
\]

so on a fixed terminal normalized block of width `tau_0>0`,

\[
E_j\gtrsim R_j^3.
\]

Therefore the physical enstrophy-time contained in that block satisfies

\[
\boxed{
d_j\gtrsim R_j^3/\sqrt{W_j}.}
\]

Define the excess-dissipation parameter

\[
\boxed{
\Xi_j
:=\frac{d_j\sqrt{W_j}}{R_j^3}.
}
\]

Then

\[
\boxed{\Xi_j\gtrsim1.}
\]

Substituting into the adaptive horizon gives

\[
\boxed{
L_j
=g_j\Xi_j^{2/3}R_j^2,
}
\]

and in physical variables

\[
\boxed{
h_j
=g_j\Xi_j^{2/3}\ell_j^2.}
\]

Thus old-source localization cannot force the fresh-generation horizon below the coherent-core parabolic scale. The terminal occupancy exactly blocks such an improvement.

## 4. Critical saturation dichotomy

The surviving branch splits into:

### D1. Excess dissipation

\[
\Xi_j\to\infty.
\]

Then the near-terminal physical dissipation is parametrically larger than the irreducible coherent-core occupancy cost.

### D2. Parabolic critical saturation

After a subsequence,

\[
\boxed{\Xi_j=O(1).}
\]

Then, up to the arbitrarily slow cutoff factor `g_j`, all source needed to create the crossing vorticity may be localized to

\[
\boxed{L_j\asymp R_j^2}
\]

normalized time, i.e. one coherent-core parabolic time.

This is the sharp scalar saturation: the finite-dissipation tail and terminal coherent occupancy meet at exactly the parabolic exponent.

## 5. Interpretation

The endgame is not an arbitrary Zeno cascade. On the minimal-dissipation branch it must operate at the scale-invariant pattern

\[
\boxed{
\text{fresh generation over one core parabolic time}
+\text{minimal terminal enstrophy occupancy}.
}
\]

Any contradiction must therefore use geometry, projective structure, resonant cancellation, pressure/Hessian structure, or a genuinely stronger packing theorem. Scalar time and energy exponents alone are saturated.

Status: **ADAPTIVE SOURCE HORIZON DERIVED / MINIMAL BRANCH IS PARABOLIC-CRITICAL / SCALAR DISSIPATION ALONE CANNOT SHORTEN THE SOURCE WINDOW FURTHER.**