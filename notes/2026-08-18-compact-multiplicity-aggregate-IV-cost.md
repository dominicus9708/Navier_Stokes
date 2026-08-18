# Compact packet multiplicity: duration-free aggregate I/V costs

Date: 2026-08-18

Status: **DERIVED FROM THE EXACT FIRST-HITTING CAUCHY I/V SPLIT, VOLUME PRESERVATION, AND SPATIAL HOLDER. A COMPACT TERMINAL MULTIPLICITY `N` CANNOT BE REALIZED WITH BOTH SMALL MATERIAL STRAIN-PATH COST AND SMALL VISCOUS `V2`-ROOT COST. GLOBAL REGULARITY NOT PROVED.**

## 1. Deep checkpoint and terminal dangerous volume

Use terminal normalization at

\[
W=K^2,
\qquad q=K,
\]

so the earlier first-hitting vorticity cap is

\[
\|\Omega_-\|_\infty\le K^{-1}.
\]

Assume `N` bounded-overlap natural terminal packets and choose thick dangerous subsets of fixed normalized volume inside them. Their total terminal volume satisfies

\[
|C|\gtrsim N.
\]

Pull `C` back to the earlier checkpoint. The flow is volume preserving.

The exact Cauchy-defect formula is

\[
\Omega_T=I+V.
\]

Hence at least one of the two lane sets has measure `>=cN`.

## 2. I-lane aggregate cost

On the I-lane,

\[
|F_T\Omega_-|\gtrsim1.
\]

Since `|Omega_-|<=K^-1`, the material vorticity vector is amplified by at least `cK`. For

\[
z(s)=F(s)\Omega_-,
\qquad e_z=z/|z|,
\]

the exact identity gives

\[
\frac d{ds}\log|z|=e_z^TSe_z.
\]

Thus every I-lane label satisfies

\[
\int|S(X(a,s),s)|ds
\ge
\log(cK).
\]

Integrating over labels,

\[
\int ds\int_{X(A_I,s)}|S(x,s)|dx
\gtrsim
N\log K.
\]

Because

\[
|X(A_I,s)|=|A_I|\asymp N,
\]

Holder gives

\[
\int_{X(A_I,s)}|S|dx
\le
C N^{2/3}\|S(s)\|_3.
\]

Therefore

\[
\boxed{
\int_{s_-}^{s_c}\|S(s)\|_3ds
\gtrsim
N^{1/3}\log K.
}
\]

This lower bound is independent of the duration of the amplification interval.

## 3. V-lane aggregate cost

Suppose the relevant deformation factors satisfy

\[
K_+K_-\le M.
\]

For a V-lane label,

\[
|V(a)|
\le
\nu M\int|\Delta\Omega(X(a,s),s)|ds.
\]

Since `|V(a)|>=c`, integrate over the V-lane labels:

\[
\int ds\int_{X(A_V,s)}|\Delta\Omega|dx
\gtrsim
c_{\nu,M}N.
\]

Spatial Cauchy--Schwarz on a set of volume `~N` gives

\[
\int_{X(A_V,s)}|\Delta\Omega|dx
\le
C N^{1/2}\|\Delta\Omega(s)\|_2.
\]

Hence

\[
\boxed{
\int_{s_-}^{s_c}\|\Delta\Omega(s)\|_2ds
\gtrsim
c_{\nu,M}N^{1/2}.
}
\]

If `K_+K_-` is unbounded, the episode is already in the material condition-number/deformation branch.

## 4. Compact multiplicity trichotomy

Every thick compact packet multiplicity episode therefore satisfies

\[
\boxed{
\int\|S\|_3ds
\gtrsim N^{1/3}\log K
}
\]

or

\[
\boxed{
\int\|\Delta\Omega\|_2ds
\gtrsim c_{\nu,M}N^{1/2}
}
\]

or

\[
\boxed{K_+K_-\to\infty.}
\]

This is stronger than the earlier duration-dependent `L2` lane estimates when the checkpoint interval becomes very long.

## 5. Limitation

Neither `L_t^1L_x^3` strain nor `L_t^1L_x^2` second-vorticity-derivative is known to have a finite global budget up to a hypothetical singular time. Thus the trichotomy narrows the compact lane but does not close it.

Status: **COMPACT MULTIPLICITY PAYS DURATION-FREE I/V GROWTH COST / GLOBAL REGULARITY NOT PROVED.**