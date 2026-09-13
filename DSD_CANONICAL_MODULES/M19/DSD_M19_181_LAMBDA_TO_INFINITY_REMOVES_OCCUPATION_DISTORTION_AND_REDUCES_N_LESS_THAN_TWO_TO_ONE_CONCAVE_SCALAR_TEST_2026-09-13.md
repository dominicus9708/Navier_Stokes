# M19-181 — Lambda to infinity removes occupation distortion and reduces N<2 to one concave scalar test

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / SHARPENED SUFFICIENT CRITERION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-180 gives, for the exponential-memory metric,

\[
\boxed{
\nu\langle P_\lambda\rangle+\frac14N
\le\langle T_\lambda\rangle,
}
\]

with no positive averaged connection loss.

The instantaneous vorticity Gram operator satisfies

\[
X_\lambda\le\kappa_\lambda I,
\qquad
\kappa_\lambda=1+\frac{L_+}{\lambda}.
\]

## 2. Generalized Lieb--Thirring estimate with Bessel bound

Choose a `G_lambda`-orthonormal hard frame and let

\[
\rho_\lambda(y,s)=\sum_{j=1}^N|\eta_j(y,s)|^2,
\qquad
P_\lambda(s)=\sum_{j=1}^N\|\nabla\eta_j(s)\|_2^2.
\]

The synthesis operator of the family has `L2` Bessel norm at most `kappa_lambda`. Hence the standard density estimate scales as

\[
\boxed{
\int\rho_\lambda^{5/3}
\le
C_{LT}\kappa_\lambda^{2/3}P_\lambda.
}
\]

Therefore the collective local-strain trace satisfies

\[
\boxed{
|T_{str,\lambda}|
\le
A\,\kappa_\lambda^{2/5}P_\lambda^{3/5},
}
\]

where

\[
A:=C_{LT}^{3/5}M_{5/2},
\qquad
M_{5/2}:=\sup_s\|S_U(s)\|_{5/2}.
\]

## 3. Generalized nonlocal trace

For `3/2<a<3`, retain the M19-172 exponents

\[
q(a):=\frac{3-a}{2a},
\qquad
p(a):=\frac{11}{6}-\frac{5}{2a},
\]

and

\[
d(a):=p(a)+q(a)=\frac43-\frac1a<1.
\]

The orthonormal-family estimate has collective homogeneity `d(a)`. Replacing orthonormality by a Bessel bound `kappa_lambda` therefore contributes the exact scaling factor `kappa_lambda^{1-d(a)}`. Thus

\[
|T_{nl,\lambda}|
\le
B_a\,
\kappa_\lambda^{1-d(a)}
Z_\lambda^{p(a)}P_\lambda^{q(a)},
\]

where

\[
B_a:=C_aM_a,
\qquad
M_a:=\sup_s\|\nabla\Omega(s)\|_a.
\]

Since

\[
Z_\lambda=\operatorname{tr}X_\lambda\le\kappa_\lambda N,
\]

we obtain

\[
\boxed{
|T_{nl,\lambda}|
\le
B_a\,
\kappa_\lambda^{1-q(a)}
N^{p(a)}P_\lambda^{q(a)}.
}
\]

## 4. Long-time averaging

Because `3/5<1` and `0<q(a)<1`, concavity gives

\[
\langle P_\lambda^{3/5}\rangle
\le\bar P_\lambda^{3/5},
\qquad
\langle P_\lambda^{q(a)}\rangle
\le\bar P_\lambda^{q(a)},
\]

where

\[
\bar P_\lambda:=\langle P_\lambda\rangle.
\]

Hence

\[
\frac14N+\nu\bar P_\lambda
\le
A\kappa_\lambda^{2/5}\bar P_\lambda^{3/5}
+
B_a\kappa_\lambda^{1-q(a)}N^{p(a)}\bar P_\lambda^{q(a)}.
\]

Set

\[
x:=\frac{\bar P_\lambda}{N}.
\]

After division by `N`,

\[
\boxed{
\frac14+\nu x
\le
A\kappa_\lambda^{2/5}N^{-2/5}x^{3/5}
+
B_a\kappa_\lambda^{1-q(a)}N^{d(a)-1}x^{q(a)}.
}
\]

## 5. Worst dimension is N=2

Both exponents of `N` on the right are strictly negative:

\[
-\frac25<0,
\qquad
d(a)-1<0.
\]

Therefore among all `N>=2`, the largest right-hand side occurs at `N=2`.

Thus it suffices to exclude the two-dimensional hard bundle.

## 6. Lambda can be removed

M19-180 permits `lambda` to become arbitrarily large without losing the quarter-gap. Hence

\[
\kappa_\lambda\downarrow1.
\]

A strict dimension-one criterion is therefore

\[
\boxed{
\sup_{x\ge0}\Psi_a(x)<\frac14
}
\]

for at least one `a in (3/2,3)`, where

\[
\boxed{
\Psi_a(x)
:=
A\,2^{-2/5}x^{3/5}
+
B_a\,2^{d(a)-1}x^{q(a)}
-\nu x.
}
\]

If this strict inequality holds, then

\[
\boxed{N\le1.}
\]

## 7. The maximizer is unique

For `x>0`, both powers `3/5` and `q(a)` lie strictly between zero and one. Therefore `Psi_a` is strictly concave.

Its unique maximizer `x_a^*>0` is characterized by

\[
\boxed{
\nu
=
\frac35A\,2^{-2/5}(x_a^*)^{-2/5}
+
q(a)B_a\,2^{d(a)-1}(x_a^*)^{q(a)-1}.
}
\]

Hence the original memory/occupation problem has been reduced to a one-dimensional scalar root for each `a`, followed by a one-dimensional search in `a`.

## 8. What has actually closed

The following obstruction is removed:

\[
\boxed{\kappa_{occ}\text{ is no longer an independent unknown constant}.}
\]

The only coefficients in the sharp current test are now the actual PDE background quantities contained in `A` and `B_a`, together with `nu` and the known functional-inequality constants.

## 9. What has not closed

Finiteness of `A` and `B_a` does not imply

\[
\sup_x\Psi_a(x)<1/4.
\]

A quantitative amplitude relation is still required. Therefore M19-181 is a sharp reduction, not a proof of `N<=1`.

---

\[
\boxed{\text{M19-181: N>=2 IS REDUCED TO A SHARP CONCAVE SCALAR COMPENSATION TEST.}}
\]
