# Residual singularity growth certificate

Date: 2026-08-12

Status: **CONDITIONAL NECESSARY CERTIFICATE + NO CONTRADICTION YET**.

This note records what the Grujic vorticity analyticity/sparseness theorem forces on any hypothetical finite singular time after combining it with the repository's vorticity-window dissipation channel.

## 1. Pointwise lower growth of the vorticity maximum

Let `T*` be a hypothetical singular time and

\[
W(t)=\|\omega(t)\|_\infty.
\]

The vorticity theorem states that if there exists a time `t<T*` with

\[
t+\frac{1}{d_0^2W(t)}\ge T^*,
\]

then `T*` is not singular, because the local analyticity interval already reaches beyond the putative singular time.

Therefore any actual singular time must satisfy, for every sufficiently late `t<T*`,

\[
t+\frac{1}{d_0^2W(t)}<T^*.
\]

Equivalently,

\[
\boxed{
W(t)>
\frac{1}{d_0^2(T^*-t)}.
}
\]

This is a conditional necessary lower growth rate inside the same external theorem framework.

## 2. Combine with the vorticity-window certificate

The repository's geometric packing bridge gave the scale-invariant window channel

\[
\mathcal Z_\omega(t)
=
W(t)^{1/2}
\int_{I_t}\|\omega(s)\|_2^2ds,
\]

where

\[
I_t=
\left[
 t+\frac{1}{4d_0^2W(t)},
 t+\frac{1}{d_0^2W(t)}
\right].
\]

To evade the sufficient sparseness gate, a hypothetical singular cascade must have arbitrarily late times for which

\[
\mathcal Z_\omega(t)
\ge c_{\delta,d_0}>0.
\]

Thus

\[
\boxed{
\int_{I_t}\|\omega(s)\|_2^2ds
\ge
c_{\delta,d_0}W(t)^{-1/2}.
}
\]

The pointwise growth condition implies only

\[
W(t)^{-1/2}
<d_0(T^*-t)^{1/2}.
\]

This is an **upper**, not a lower, estimate on the required window cost.  Hence the pointwise Leray/analyticity-scale growth does not make the cumulative enstrophy cost diverge.

## 3. Why the tempting summation route fails

Suppose one selects a sequence of disjoint natural windows with starting times `t_n` and writes

\[
\Delta t_n\asymp W(t_n)^{-1}.
\]

The non-sparseness cost is then of order

\[
W(t_n)^{-1/2}
\asymp
(\Delta t_n)^{1/2}.
\]

Even though

\[
\sum_n\Delta t_n<\infty
\]

when `t_n->T*`, it is possible that

\[
\sum_n(\Delta t_n)^{1/2}<\infty;
\]

for example geometrically shrinking time steps have this property.

Therefore the route

\[
\text{non-sparseness on every natural window}
+\text{finite total dissipation}
\Longrightarrow\text{contradiction}
\]

is **not valid without an additional restriction on the rate at which the natural windows can shrink**.

## 4. Residual growth requirement

If infinitely many disjoint dangerous windows survive while total enstrophy dissipation remains finite, then necessarily

\[
\sum_n W(t_n)^{-1/2}<\infty.
\]

Thus the vorticity maxima along such a dangerous sequence must grow fast enough for the reciprocal square roots to be summable.

This is a structural restriction, not a contradiction.

For instance, polynomial growth

\[
W(t_n)\sim n^q
\]

would require

\[
q>2
\]

for this particular series to converge.  This statement concerns the sequence index `n`, not a universal time-domain blow-up exponent.

## 5. DSD residual-class interpretation

The complement-elimination program now leaves a hypothetical singular cascade that must satisfy simultaneously:

1. the weighted mean-flow velocity oscillation fails the pressure-free epsilon gate at arbitrarily small scales;
2. pressure transfer is locally sustained in scale, since macroscopically remote affine-free pressure is suppressed;
3. intense vorticity does not become sufficiently line-sparse on the natural `W^{-1/2}` scale;
4. the critical local enstrophy/occupancy channel remains non-small at the required comparison times;
5. the natural-window channel `Z_omega` remains non-small on arbitrarily late windows;
6. `W(t)` grows at least at the analyticity lower rate `1/[d0^2(T*-t)]`;
7. if there are infinitely many disjoint dangerous windows with finite total dissipation, their `W(t_n)^{-1/2}` costs must form a summable sequence;
8. vorticity-direction and strain-eigenvalue regularity gates must also be evaded.

The remaining task is to show that this residual class is empty, or to identify a further independent gate that removes it.

## 6. Claim boundary

The theorem-level vorticity analyticity/sparseness alternatives are external.  The algebraic consequences and summability observation above are derived here.

No global-regularity contradiction is claimed.
