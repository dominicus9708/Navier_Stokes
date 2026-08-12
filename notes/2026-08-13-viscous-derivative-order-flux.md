# Viscous derivative-order flux identity and finite geometric budget

Date: 2026-08-13

Status: **DERIVED NEIGHBOR-COVARIANCE IDENTITY + FINITE GEOMETRIC V-BUDGET / OPEN WEIGHTED-r_k CLOSURE**.

This note sharpens the viscous branch of the derivative projective covariance chain.

The key point is that the neighboring-covariance factor

\[
\mathcal A_k
=
\operatorname{tr}(C_kC_{k+1})
-\operatorname{tr}(C_k^2)
\]

is not an arbitrary mismatch scalar. It has an exact decomposition into a derivative-order dispersion drop and a coercive covariance-distance penalty.

No novelty claim is made without a separate literature audit.

## 1. Exact neighbor identity

Recall

\[
J_k=1-\operatorname{tr}(C_k^2)
\]

and define

\[
\boxed{
\Delta_k
=\|C_{k+1}-C_k\|_F.
}
\]

The Frobenius identity gives

\[
\Delta_k^2
=
\operatorname{tr}(C_{k+1}^2)
+\operatorname{tr}(C_k^2)
-2\operatorname{tr}(C_kC_{k+1}).
\]

Therefore

\[
\begin{aligned}
2\mathcal A_k
&=
2\operatorname{tr}(C_kC_{k+1})
-2\operatorname{tr}(C_k^2)\\
&=
\operatorname{tr}(C_{k+1}^2)
-\operatorname{tr}(C_k^2)
-\Delta_k^2\\
&=
J_k-J_{k+1}-\Delta_k^2.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal A_k
=
\frac12
\left[
J_k-J_{k+1}-\Delta_k^2
\right].
}
\]

## 2. Sign of viscous directional mixing

The derivative covariance-chain budget is

\[
\frac14\dot J_k
=
\mathcal M_{N,k}
+\nu r_k\mathcal A_k,
\qquad
r_k=E_{k+1}/E_k.
\]

Since `nu r_k>0`, positive viscous directional mixing at order `k` requires

\[
\mathcal A_k>0.
\]

The exact identity implies

\[
\boxed{
\mathcal A_k>0
\Longrightarrow
J_k-J_{k+1}>\Delta_k^2>0.
}
\]

Thus viscosity can increase the normalized projective dispersion `J_k` only when the next derivative level is **less projectively dispersed** than the current one by more than the covariance mismatch penalty.

In particular,

\[
J_{k+1}\ge J_k
\Longrightarrow
\mathcal A_k\le-\frac12\Delta_k^2\le0.
\]

If directional dispersion is nondecreasing with derivative order, viscosity can only demix the current derivative level.

## 3. Flux form of the projective chain

Substituting the identity gives

\[
\boxed{
\dot J_k
+2\nu r_k\Delta_k^2
=
4\mathcal M_{N,k}
-2\nu r_k(J_{k+1}-J_k).
}
\]

This has a useful interpretation:

- `4 M_N,k`: nonlinear directional source;
- `-2 nu r_k (J_{k+1}-J_k)`: directional flux across derivative order;
- `2 nu r_k Delta_k^2`: coercive covariance-mismatch loss.

Thus derivative order behaves as an additional discrete channel index, not as a new spatial dimension.

## 4. Finite geometric budget on a consecutive positive-V block

Suppose

\[
\mathcal A_k>0
\]

for every

\[
k=m,m+1,\ldots,n.
\]

Then `J_k` is strictly decreasing on this block. Summing the exact identity yields

\[
\boxed{
\sum_{k=m}^{n}\mathcal A_k
=
\frac12
\left[
J_m-J_{n+1}
-\sum_{k=m}^{n}\Delta_k^2
\right].
}
\]

Since

\[
0\le J_k\le\frac23,
\]

we obtain

\[
\boxed{
0<
\sum_{k=m}^{n}\mathcal A_k
\le
\frac12J_m
\le
\frac13.
}
\]

Therefore a consecutive run in which viscosity is directionally mixing at every derivative level has a finite **unweighted geometric budget**.

## 5. Quantitative length bound when derivative ratios are moderate

The actual positive viscous mixing rate is

\[
V_k
=\nu r_k\mathcal A_k.
\]

Assume on a consecutive block

\[
0<V_k\quad\text{and}\quad r_k\le R.
\]

If in addition

\[
V_k\ge\eta>0
\]

for every `k=m,...,n`, then

\[
\mathcal A_k
\ge
\frac{\eta}{\nu R}.
\]

Using the finite geometric budget,

\[
(n-m+1)\frac{\eta}{\nu R}
\le\frac13.
\]

Hence

\[
\boxed{
 n-m+1
\le
\frac{\nu R}{3\eta}.
}
\]

Interpretation: an order-one positive V-branch cannot persist through arbitrarily many consecutive derivative orders while the derivative-energy ratios remain uniformly moderate.

## 6. Consequence for a long V-dominant cascade

If the actual V-branch

\[
\nu r_k\mathcal A_k
\]

remains large over a long derivative-order block, then one of two events must occur:

1. the geometric factors `A_k` consume the finite projective-dispersion drop budget and the positive-V block ends;
2. some derivative ratios

\[
\boxed{
r_k=E_{k+1}/E_k}
\]

become large enough to compensate for shrinking `A_k`.

The second event is precisely high-derivative activation: the characteristic derivative scale

\[
\ell_k\sim r_k^{-1/2}
\]

shrinks rapidly.

This is the point at which the higher-derivative analyticity / sparseness / generating-function track becomes the natural external/internal continuation.

## 7. S/V interaction

The finite geometric V-budget does **not** by itself prove regularity because nonlinear mixing can increase `J_{k+1}` again at higher derivative levels.

Therefore an indefinitely alternating derivative-order pattern would have to look schematically like

\[
\boxed{
\text{S-chain regenerates }J_k
\quad\longrightarrow\quad
\text{V-chain spends the regenerated dispersion drop}
\quad\longrightarrow\quad
\text{S-chain regenerates again}.
}
\]

This converts the former parallel S/V branches into an interacting cycle.

To sustain the cycle indefinitely, a hypothetical singular cascade must repeatedly pay either

- nonlinear derivative forcing `L_k`, or
- rapidly increasing derivative ratios `r_k`,

while also respecting the covariance mismatch penalty `Delta_k^2`.

## 8. Stronger residual-class statement

The V-branch can no longer be treated as an independent escape route.

A residual singularity using positive viscous directional mixing across many derivative levels must satisfy

\[
\boxed{
\text{repeated S-regeneration of }J_k
\quad\text{or}\quad
\sup_k r_k\to\infty
\text{ along the active chain}.
}
\]

The first alternative feeds the nonlinear derivative convolution / strain-alignment route.

The second feeds the high-derivative scale / sparseness / analyticity route.

The next target is to put a common scale-critical weight on the S-regeneration cost and the derivative-ratio escalation so that an infinite S--V cycle would force a contradiction with an existing finite spacetime budget.

Status: **OPEN WEIGHTED S--V CYCLE CLOSURE**.
