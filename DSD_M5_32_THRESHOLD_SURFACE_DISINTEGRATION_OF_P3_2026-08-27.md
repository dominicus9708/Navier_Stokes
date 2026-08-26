# DSD M5-32 — Threshold-Surface Disintegration of the Critical p=3 Ledger

Date: 2026-08-27

Status: **DERIVED EXACT COAREA DISINTEGRATION / THE NONSMOOTH THRESHOLD FAMILY RECONSTRUCTS THE ENTIRE p=3 PRESSURE-DISSIPATION BALANCE / THRESHOLD LEVELS ARE NOT INDEPENDENT PAYERS / GLOBAL REGULARITY UNPROVED.**

## 1. Threshold family

For every amplitude level `lambda>0`, define

\[
E_\lambda(V)
:=
\frac12\int (a^2-\lambda^2)_+\,dz,
\qquad a=|V|.
\]

The entropy multiplier is

\[
W_\lambda
=V\,\mathbf1_{a>\lambda}.
\]

By the M5-31 nonsmooth convex-entropy calculation,

\[
\boxed{
\frac{d}{d\sigma}E_\lambda
+\nu D_\lambda^{surf}
=J_P(\lambda),
}
\]

where, for regular levels,

\[
\boxed{
D_\lambda^{surf}
=
\int_{a>\lambda}|\nabla V|^2\,dz
+\lambda\int_{a=\lambda}|\nabla a|\,dS,
}
\]

and

\[
\boxed{
J_P(\lambda)
=
\int_{a=\lambda}\Pi\,V\cdot n_\lambda\,dS,
\qquad
n_\lambda=\frac{\nabla a}{|\nabla a|}.
}
\]

The pressure term is gauge independent because

\[
\int_{a=\lambda}V\cdot n_\lambda\,dS=0.
\]

## 2. Integrating the threshold energy

For each point with amplitude `a`,

\[
\int_0^\infty
\frac12(a^2-\lambda^2)_+\,d\lambda
=
\frac12\int_0^a(a^2-\lambda^2)d\lambda
=
\frac13a^3.
\]

Therefore

\[
\boxed{
\int_0^\infty E_\lambda\,d\lambda
=
\frac13\int |V|^3\,dz.
}
\]

## 3. Integrating the volume viscous term

By Fubini,

\[
\int_0^\infty
\left(
\int_{a>\lambda}|\nabla V|^2dz
\right)d\lambda
=
\int a|\nabla V|^2dz.
\]

Since

\[
|\nabla V|^2
=|\nabla a|^2+a^2|\nabla n|^2,
\]

this equals

\[
\int
\left(
a|\nabla a|^2+a^3|\nabla n|^2
\right)dz.
\]

## 4. Integrating the level-set viscous measure

Using coarea/distributional calculus,

\[
\int_0^\infty
\lambda
\left(
\int_{a=\lambda}|\nabla a|dS
\right)d\lambda
=
\int a|\nabla a|^2dz.
\]

Hence

\[
\boxed{
\int_0^\infty D_\lambda^{surf}\,d\lambda
=
\int
\left(
2a|\nabla a|^2+a^3|\nabla n|^2
\right)dz
=D_3.
}
\]

This is exactly the critical `p=3` viscous dissipation used throughout the W1 audit.

## 5. Integrating the pressure boundary flux

Again by coarea,

\[
\begin{aligned}
\int_0^\infty J_P(\lambda)d\lambda
&=
\int_0^\infty
\int_{a=\lambda}
\Pi\,V\cdot\frac{\nabla a}{|\nabla a|}
\,dS\,d\lambda\\
&=
\int \Pi\,V\cdot\nabla a\,dz.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_0^\infty J_P(\lambda)d\lambda
=F_P.
}
\]

## 6. Exact reconstruction of the p=3 ledger

Integrating the full threshold family gives

\[
\boxed{
\frac13\frac{d}{d\sigma}\int|V|^3dz
+\nu D_3
=F_P.
}
\]

Thus the nonsmooth threshold-surface ledger is an exact amplitude-level disintegration of the global critical `p=3` balance.

## 7. DSD audit consequence

The following objects must not be counted as independent additive payers:

- the pressure work on many amplitude levels;
- the level-set viscous measures on many thresholds;
- the global `p=3` pressure work/dissipation.

They are the same critical ledger viewed at different state resolutions.

In particular, summing fixed lower bounds over many nested thresholds without tracking overlap would double count the same `p=3` action.

## 8. Updated endpoint target

M5-31 removed the smooth threshold-collar degeneracy but M5-32 shows that the resulting surface family does not create a new global budget. It resolves the existing critical budget by amplitude level.

The next useful theorem must exploit **level-to-level structure** rather than add level costs. Examples include:

1. monotonicity or one-sided variation of the pressure-gap profile `J_P(lambda)` relative to `D_lambda^{surf}`;
2. a restriction on how positive pump levels can be nested in amplitude;
3. a cross-level cancellation forced by incompressibility/pressure-Poisson geometry;
4. a Tauberian/compactness statement linking the level family to the `K` boundary coordinate without assuming the conclusion.

No such closing cross-level theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
