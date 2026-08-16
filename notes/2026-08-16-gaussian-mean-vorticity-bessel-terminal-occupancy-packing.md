# Gaussian mean-vorticity Bessel packing for terminal coherent occupancy

Date: 2026-08-16

Status: **DERIVED OVERLAP-FREE PACKING OF COHERENT TERMINAL MEAN-VORTICITY EPISODES ACROSS GEOMETRICALLY SEPARATED PHYSICAL SCALES. THE RESULT MAKES THE `R^3/sqrt(W)` COST RIGOROUS UNDER ARBITRARY TEMPORAL OVERLAP, BUT THAT SERIES CAN STILL CONVERGE. GLOBAL REGULARITY NOT PROVED.**

## 1. Same Gaussian Bessel family

For physical scale `ell_j` and moving center `x_j(t)`, define the normalized Gaussian probe

\[
p_j(t,y)
=c_g^{-1}\ell_j^{3/2}g_{\ell_j,x_j(t)}(y).
\]

For geometrically separated scales

\[
\ell_{j+1}\le\rho\ell_j,
\qquad0<\rho<1,
\]

the exact Gaussian overlap estimate gives a uniform Bessel family independent of the centers:

\[
\sum_j|\langle F,p_j(t)\rangle|^2
\le C_\rho\|F\|_2^2.
\]

Apply this componentwise to physical vorticity `omega(t)`.

Because

\[
\bar\omega_j(t)
=\int g_{\ell_j,x_j(t)}(y)\omega(y,t)dy,
\]

we obtain

\[
\boxed{
\sum_j
\ell_j^3
|\bar\omega_j(t)|^2
\le
C_\rho\|\omega(t)\|_2^2.
}
\]

## 2. Activate only the terminal coherent blocks

Let `J_j` denote the physical terminal block associated with crossing `j`, corresponding to a fixed normalized time width before the crossing.

At each physical time, restrict the Bessel family to indices with `t in J_j`. Then

\[
\boxed{
\sum_j
\mathbf1_{J_j}(t)
\ell_j^3
|\bar\omega_j(t)|^2
\le
C_\rho\|\omega(t)\|_2^2.
}
\]

Integrating gives

\[
\boxed{
\sum_j
\ell_j^3
\int_{J_j}|\bar\omega_j(t)|^2dt
\le
C_\rho
\int_0^{T^*}\|\omega(t)\|_2^2dt.
}
\]

No disjointness or bounded temporal overlap of the `J_j` is needed.

## 3. Evaluate one coherent crossing

At terminal first-hitting level `W_j`, the normalized coherent crossing has

\[
|\bar\Omega_j|\ge c>0.
\]

In physical variables,

\[
|\bar\omega_j|\gtrsim W_j.
\]

The first-hitting differential bound used in the terminal occupancy argument gives a fixed normalized backward block on which the mean remains a fixed fraction of this value. Its physical duration is

\[
|J_j|\asymp W_j^{-1}.
\]

Therefore

\[
\int_{J_j}|\bar\omega_j|^2dt
\gtrsim W_j.
\]

The physical coherent-core scale is

\[
\ell_j=\frac{R_j}{\sqrt{W_j}}.
\]

Hence the Bessel contribution of episode `j` is

\[
\boxed{
\ell_j^3
\int_{J_j}|\bar\omega_j|^2dt
\gtrsim
\ell_j^3W_j
=
\frac{R_j^3}{\sqrt{W_j}}
=
\ell_jR_j^2.
}
\]

## 4. Overlap-free terminal occupancy packing

Combining Sections 2 and 3 yields, for every geometrically scale-separated coherent subsequence,

\[
\boxed{
\sum_j
\frac{R_j^3}{\sqrt{W_j}}
\lesssim
\int_0^{T^*}\|\omega(t)\|_2^2dt
<\infty.
}
\]

Equivalently,

\[
\boxed{
\sum_j\ell_jR_j^2<\infty.
}
\]

This is the terminal coherent-occupancy ledger with both temporal-overlap and center-motion double counting removed.

## 5. Relation to the affine-strain Bessel packing

The corresponding mean-strain result gives

\[
\sum_j
\ell_j^3
\int_{I_j}|\bar S_j|^2dt
<\infty.
\]

If `|I_j|~ell_j^2` and the affine branch needs `A_j>=c log R_j`, then

\[
\sum_j\ell_j(\log R_j)^2<\infty.
\]

Since

\[
R_j^2\gg(\log R_j)^2,
\]

the coherent mean-vorticity occupancy is asymptotically the stronger of these two scalar Bessel costs.

Thus scale-overlap is no longer the missing issue for either mean vorticity or mean strain.

## 6. Sharpness boundary

The adversarial power-law/super-separated Zeno families remain compatible with

\[
\sum_j\ell_jR_j^2<\infty.
\]

Hence this exact packing does not prove regularity.

What it does prove is that a survivor cannot obtain apparent summability merely by reusing the same spacetime enstrophy through overlapping observation windows. The actual physical scale weights must themselves be summable.

Status: **TERMINAL COHERENT OCCUPANCY IS EXACTLY BESSEL-PACKED ACROSS SCALE / TEMPORAL OVERLAP REMOVED / REMAINING WALL IS GENUINE SUMMABILITY OF SHRINKING PHYSICAL SCALE WEIGHTS.**
