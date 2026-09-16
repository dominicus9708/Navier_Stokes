# M19-329 — Negative-kappa self-covariance is a quantitative intrinsic recycling channel for log diffusion

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / SIGN-RESOLVED COVARIANCE / INTRINSIC RECYCLING FIREWALL / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-328

On a sign-preserving CE-H material carrier, define

\[
z=\log|\kappa|,
\qquad
g=\sigma+\kappa.
\]

The normalized coefficient entropy obeys

\[
\boxed{
h'
=D_z+S_{interface}+S_{force}+2C_{gz},
}
\]

where

\[
D_z=\langle|\nabla z|^2\rangle_\pi\ge0,
\]

and

\[
C_{gz}
=
\operatorname{Cov}_\pi(\sigma,z)
+
\operatorname{Cov}_\pi(\kappa,z).
\]

M19-324 gives a fixed coefficient variance on the spatial branch.

## 2. Pair formula for covariance

For a probability law \(\pi\) and an independent copy \(K'\) of \(K\),

\[
\operatorname{Cov}(K,f(K))
=
\frac12
\mathbb E\big[(K-K')(f(K)-f(K'))\big].
\]

Take

\[
f(k)=\log|k|.
\]

## 3. Negative coefficient branch

Assume the connected sign-preserving component satisfies

\[
-M_\kappa\le\kappa<0.
\]

For \(x,y<0\), the mean-value theorem gives

\[
\log|x|-\log|y|
=\frac{x-y}{\theta}
\]

for some \(\theta\) between \(x\) and \(y\). Since \(\theta<0\) and \(|\theta|\le M_\kappa\),

\[
\frac1\theta\le -\frac1{M_\kappa}.
\]

Therefore

\[
\boxed{
(x-y)(\log|x|-\log|y|)
\le
-\frac1{M_\kappa}(x-y)^2.
}
\]

Using the pair formula,

\[
\boxed{
\operatorname{Cov}_\pi(\kappa,\log|\kappa|)
\le
-\frac1{M_\kappa}
\operatorname{Var}_\pi(\kappa).
}
\]

## 4. Quantitative consequence of M19-324

If

\[
\operatorname{Var}_\pi(\kappa)
\ge c_\kappa>0,
\]

then

\[
\boxed{
\operatorname{Cov}_\pi(\kappa,\log|\kappa|)
\le
-\frac{c_\kappa}{M_\kappa}
<0.
}
\]

Thus spatial coefficient variance on a negative-kappa sign-preserving component automatically creates a fixed negative signed covariance.

No additional strain or interface mechanism is required merely to produce a negative signed payer.

## 5. Interpretation

The sign is physically natural. More negative \(\kappa\) means stronger Laplacian eigenvalue magnitude, while \(\log|\kappa|\) is larger there. Hence

\[
\kappa\ \text{decreases}
\quad\Longleftrightarrow\quad
\log|\kappa|\ \text{increases},
\]

which generates negative covariance.

This is an intrinsic coefficient-reaction mechanism inside CE-H itself.

## 6. Recurrent entropy balance

Ignoring interface/forcing for illustration,

\[
0=\langle h'\rangle
=\langle D_z\rangle
+2\langle\operatorname{Cov}(\sigma,z)\rangle
+2\langle\operatorname{Cov}(\kappa,z)\rangle.
\]

The last term is already negative and quantitatively nonzero when coefficient variance persists.

Therefore

\[
\boxed{
\text{positive log-kappa diffusion}
\text{ can be recycled by negative-kappa self-covariance.}
}
\]

A nonzero signed covariance is therefore not automatically a forbidden defect.

## 7. Positive coefficient branch

If instead \(0<\kappa\le M_\kappa\), then \(\log\kappa\) is increasing and

\[
\boxed{
\operatorname{Cov}_\pi(\kappa,\log\kappa)\ge0.
}
\]

Hence the coefficient self-covariance cannot pay positive log diffusion on a positive-kappa component. Such a component requires negative contribution from

- strain-phase covariance;
- normalized forcing;
- interface/cutoff transport;
- or an exit through zero/sign change.

For a whole-space snapshot the global enstrophy-weighted mean satisfies

\[
\bar\kappa=-P/E\le0,
\]

so an everywhere-positive global coefficient state is impossible for nonzero vorticity. Positive-kappa regions can only occur as subcomponents balanced by negative coefficient mass elsewhere.

## 8. Stronger two-sided estimate away from zero

If the negative component is also bounded away from zero,

\[
0<\kappa_*\le|\kappa|\le M_\kappa,
\]

then

\[
-\frac1{\kappa_*}
\le f'(\kappa)
\le
-\frac1{M_\kappa},
\]

which yields

\[
\boxed{
-\frac1{\kappa_*}\operatorname{Var}(\kappa)
\le
\operatorname{Cov}(\kappa,\log|\kappa|)
\le
-\frac1{M_\kappa}\operatorname{Var}(\kappa).
}
\]

Thus on a fixed intrinsic coefficient collar the self-covariance is quantitatively equivalent to coefficient variance.

## 9. Canonical firewall

M19-328 raised the possibility that a negative coefficient-growth covariance might be the missing non-coboundary signed defect.

M19-329 shows that on the negative-kappa branch a substantial part of that signed covariance is automatic and recyclable:

\[
\boxed{
\operatorname{Var}(\kappa)>0
\Longrightarrow
\operatorname{Cov}(\kappa,\log|\kappa|)<0.
}
\]

Therefore the existence of the signed covariance alone cannot close the branch.

The genuinely informative residual is now

\[
\boxed{
\operatorname{Cov}_\pi(\sigma,\log|\kappa|)
}
\]

plus forcing/interface terms, after subtracting the intrinsic coefficient self-covariance.

## 10. Conclusion

The spatial CE-H variance branch contains its own intrinsic signed recycling mechanism on negative-kappa components. This explains how fixed positive log diffusion can coexist with compact recurrence without requiring a one-way scalar defect.

\[
\boxed{
\text{M19-329 COMPLETE; NEXT TARGET: THE RESIDUAL STRAIN--COEFFICIENT COVARIANCE AFTER REMOVING THE AUTOMATIC NEGATIVE-KAPPA SELF-RECYCLING TERM.}
}
\]
