# Scale-time heat contraction identity

Date: 2026-08-14

Status: exact isotropic identity; nonlinear commutator packing remains open.

Let `Sigma_p=R^2 I`, `Sigma_c=c Sigma_p`, `0<c<1`, and choose `t_c-t_p` so that `2 nu (t_c-t_p)=(1-c)R^2`.

For a fixed center and parent field `g_p`, write its parent-Gaussian Hermite energies as `e_n`, `n>=1`. Pure heat evolution over this matched interval gives

\[
B_{Sigma_c}[P_{(1-c)Sigma_p}g_p]
=\sum_{n\ge1}c^n e_n
\le c\sum_{n\ge1}e_n
=c B_{Sigma_p}[g_p].
\]

For Navier--Stokes `g=grad u`, the mild equation is

\[
g(t_c)=P_{(1-c)Sigma_p}g(t_p)+Q_{p\to c},
\]

where `Q` is the nonlinear Duhamel term. Since the square root of Gaussian variance is an L2 seminorm,

\[
\boxed{
\sqrt{B_c(x)}
\le\sqrt{cB_p(x)}+\sqrt{B_Q(x)}.
}
\]

Therefore

\[
\boxed{
B_Q(x)\ge
(\sqrt{B_c(x)}-\sqrt{cB_p(x)})_+^2.
}
\]

If `B_Q<=epsilon B_c`, then

\[
\boxed{
B_p(x)\ge
\frac{(1-\sqrt\epsilon)^2}{c}B_c(x).
}
\]

When `epsilon<(1-sqrt(c))^2`, the backward precursor is strictly larger than the child residual.

With zero nonlinear commutator, backward propagation gives `B proportional to R^2`. Across `R=1` to `R=W^(1/6)` the factor is exactly `W^(1/3)`, so the amplitude `B=W^(-1/3)` is again the critical wall.

Thus a moving first-hitting cascade must use either a backward precursor chain at the future dangerous center or nonlinear Duhamel creation. The remaining task is precursor capacity versus nonlinear-commutator packing.
