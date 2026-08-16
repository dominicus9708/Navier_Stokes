# Parabolic-saturation adversarial family

Date: 2026-08-16

Status: **SHARPNESS AUDIT. THE NEW PARABOLIC-HORIZON AND SEED/STRAIN BARRIERS ARE STILL COMPATIBLE WITH A SUPER-SEPARATED HYPOTHETICAL CASCADE. THIS IDENTIFIES THE REMAINING CRITICAL WALL.**

## 1. Test family

Use the previously surviving power family

\[
R=W^{\delta/4},
\qquad
0<\delta<1/5.
\]

This lies safely inside the finite-energy Gaussian-tail constraint and the earlier scalar occupancy barriers.

Take a geometric first-hitting sequence

\[
W_j=2^j.
\]

Then

\[
R_j=2^{\delta j/4}\to\infty.
\]

## 2. Terminal coherent occupancy remains summable

The physical enstrophy-time cost of the fixed normalized terminal block is

\[
c_j^{(E)}
\asymp
\frac{R_j^3}{\sqrt{W_j}}
=W_j^{3\delta/4-1/2}.
\]

Since `delta<1/5`,

\[
3\delta/4-1/2<0.
\]

Therefore

\[
\boxed{
\sum_j c_j^{(E)}<\infty.
}
\]

Finite physical kinetic-energy dissipation does not exclude the sequence.

## 3. Core-parabolic times remain summable

The physical coherent-core radius is

\[
\ell_j=R_jW_j^{-1/2}.
\]

Its parabolic time is

\[
\ell_j^2
=\frac{R_j^2}{W_j}
=W_j^{\delta/2-1}.
\]

Thus

\[
\boxed{
\sum_j\ell_j^2<\infty.
}
\]

Hence infinitely many parabolic-critical source episodes can still fit into finite physical time at the scalar level.

## 4. Productive residual/strain costs can also shrink

The seed-amplification dichotomy gives, for example,

\[
\mathcal B_R\ge R^{-1}
\quad\text{or}\quad
A_R\gtrsim\log R.
\]

A residual-seed action converted only through local volume/enstrophy bounds has physical cost no larger in exponent than powers such as

\[
\frac{R}{\sqrt W}\,\operatorname{polylog}R
=W^{\delta/4-1/2}\operatorname{polylog}W,
\]

which is also summable along the geometric sequence.

On the strain branch,

\[
A_{R_j}\gtrsim\log R_j
\asymp j.
\]

Thus

\[
\sum_j A_{R_j}=\infty,
\]

but such divergence is not a contradiction: a hypothetical singular solution is expected to have divergent BKM/critical strain action.

## 5. Meaning of the stress test

The new estimates remove arbitrary Zeno timing and arbitrary late-source creation. They force the minimal survivor into a very specific pattern:

\[
\boxed{
\text{one core-parabolic source episode per late crossing}
}
\]

with either residual covariance seeding or logarithmic symmetric-strain amplification.

However, the physical scalar costs still shrink rapidly enough to be summable.

Therefore any final contradiction must improve one of the following qualitatively:

1. prove a cross-scale packing theorem for the productive residual/strain channels;
2. show that the `log R` strain episodes cannot be supported by distinct shrinking spatial regions without a non-summable derivative or pressure cost;
3. show that near-resonant/near-slow fast-rotation concentration is incompatible with the coherent crossing geometry;
4. obtain a scale-critical rigidity theorem for the crossing-scale residual equation with the affine/Coriolis background.

## 6. Claim boundary

This construction is not a Navier--Stokes solution and is not evidence that blow-up exists. It is an exponent-level adversarial ledger showing that the presently proved inequalities do not yet contradict one another.

Status: **CURRENT BOUNDS ARE SHARP ENOUGH TO FORCE PARABOLIC CRITICAL SATURATION BUT NOT STRONG ENOUGH TO EXCLUDE A SUPER-SEPARATED CASCADE / GLOBAL REGULARITY NOT PROVED.**