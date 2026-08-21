# Smooth L2 Determinant / Projective-Tax Closure — 2026-08-21

Status: **SMOOTH MULTISTAGE S-CLOSURE OF A LARGER PURE POSITIVE-MIDDLE CORRIDOR / GLOBAL REGULARITY NOT PROVED.**

This note combines the projective-action frequency tax with the lower-order strain `L2` ledger. The resulting estimate is stronger than the analogous H1 ledger because the determinant production ceiling is small while the viscous frequency tax enters with coefficient two.

## 1. Exact normalized strain L2 ledger

For smooth incompressible Navier-Stokes,

\[
\frac d{dt}\|S\|_2^2
+2\nu\|\nabla S\|_2^2
=
-4\int_{\mathbb R^3}\det S\,dx.
\]

Under the running first-hitting normalization,

\[
E=\|\Sigma\|_2^2,
\qquad
P=\|\nabla\Sigma\|_2^2,
\qquad
b=(\log M)_s,
\]

this becomes

\[
\boxed{
E_s+\frac b2E+2\nu P
=-4\int\det\Sigma\,dy.
}
\]

Divide by `E` and write

\[
\lambda=P/E.
\]

Then

\[
\boxed{
(\log E)_s
+\frac b2
+2\nu\lambda
=
\frac{-4\int\det\Sigma}{E}.
}
\]

On a geometric first-hitting stage,

\[
\int b\,ds=\log q,
\]

so

\[
\boxed{
\log\frac{E(s_1)}{E(s_0)}
+\frac12\log q
+2\nu\int_{I_j}\lambda ds
=
\int_{I_j}\frac{-4\int\det\Sigma}{E}ds.
}
\]

## 2. Sharp trace-free determinant ceiling

For a trace-free symmetric `3x3` matrix,

\[
|\det\Sigma|
\le
\frac1{3\sqrt6}|\Sigma|^3.
\]

Equality occurs at the axisymmetric spectrum proportional to `(-2,1,1)` up to sign/permutation.

Therefore

\[
-4\det\Sigma
\le
\frac4{3\sqrt6}|\Sigma|^3.
\]

If

\[
B_S=\|\Sigma\|_\infty,
\]

then

\[
\frac{-4\int\det\Sigma}{E}
\le
\boxed{
C_{det}B_S,
\qquad
C_{det}=\frac4{3\sqrt6}\approx0.54433105395.
}
\]

Hence

\[
\int_{I_j}\frac{-4\int\det\Sigma}{E}ds
\le
C_{det}B_+L_j.
\]

## 3. Reuse the projective-action frequency tax

From `SMOOTH_PROJECTIVE_ACTION_VISCOUS_TAX_CLOSURE_2026-08-21.md`, the pure positive-middle anti-ribbon stage satisfies

\[
\nu\int_{I_j}\lambda ds
\ge
2K_P^{-4/3}
\bar Z_+^{-2/3}
L_j^{-1/3}A(L_j)^{4/3},
\]

where

\[
K_P=\frac1{3\sqrt2}S_3^{-3/4},
\qquad
S_3=3\left(\frac\pi2\right)^{4/3},
\]

\[
A(L)
=
\left[
\frac\pi2-
\left(\frac12+\frac{\sqrt2}{4}\right)L
\right]_+.
\]

The factor `2` on the right is the conservative bound `nu/rho0^2 >= 2` after using `c_*(2)>=1` and `sigma=1/2`.

## 4. Pure moving-ball stage ceiling

The audited broad pure corridor gives

\[
\boxed{
L_j\le L_{\max}(r)=0.7483880874\,r^2,
}
\]

where

\[
r=R_C/\rho_0.
\]

For fixed `r` in the range where `A(L_max)>0`, the determinant production upper bound increases with `L`, while the projective-frequency lower bound decreases with `L`. Hence the worst case is `L=L_max(r)`.

## 5. Enstrophy-tight strain ceiling

The explicit second-Taylor Biot-Savart estimate gives

\[
B_+(r)
\le
A_B(\varepsilon_Z)r^{6/7},
\]

where

\[
A_B(\varepsilon_Z)
=C_{BS}4^{3/7}
\left(\frac{4\pi}{3(1-\varepsilon_Z)}\right)^{2/7},
\]

\[
C_{BS}\approx0.821832758154486.
\]

Also

\[
\bar Z_+(r)
\le
\frac{4\pi}{3}
\frac{r^3}{1-\varepsilon_Z}.
\]

For the robust quarter enstrophy tail,

\[
\varepsilon_Z\le\frac14,
\]

\[
\boxed{
B_+(r)
\le
2.4335795280140466\,r^{6/7},
}
\]

and

\[
\boxed{
\bar Z_+(r)
\le
\frac{16\pi}{9}r^3.
}
\]

## 6. Multistage telescoping

At first-hitting endpoints, the record-point Taylor mass floor gives a positive lower bound on `E`, while the bounded enstrophy-tight common core gives a finite upper bound. Therefore on an eventual bounded pure corridor,

\[
\frac1N\log\frac{E_N}{E_0}\to0
\]

after summing `N` consecutive stages.

Thus an infinite pure lane requires asymptotically, per stage,

\[
C_{det}B_+(r)L_j
\ge
\frac12\log2
+2\nu\int_{I_j}\lambda ds.
\]

Using the worst-case stage length `L_max(r)`, a sufficient smooth S-closure test is

\[
\boxed{
C_{det}B_+(r)L_{\max}(r)
<
\frac12\log2
+4K_P^{-4/3}
\bar Z_+(r)^{-2/3}
L_{\max}(r)^{-1/3}
A(L_{\max}(r))^{4/3}.
}
\]

## 7. Robust quarter-tail radius

For

\[
\varepsilon_Z\le\frac14,
\]

insert

\[
L_{\max}(r)=0.7483880874r^2,
\]

\[
B_+(r)=2.4335795280140466r^{6/7},
\]

\[
\bar Z_+(r)=\frac{16\pi}{9}r^3.
\]

The equality in the closure test occurs at

\[
\boxed{
r_{L2}^{(1/4)}
\approx1.4550244347.
}
\]

Therefore the eventual bounded pure positive-middle anti-ribbon corridor is S-closed for

\[
\boxed{
r<1.4550244347
}
\]

under the quarter enstrophy-tail condition.

This strictly improves the H1 projective-tax radius `1.3030842670`.

## 8. Zero-tail benchmark

For

\[
\varepsilon_Z=0,
\]

the same calculation yields

\[
\boxed{
r_{L2}^{(0)}
\approx1.4724232909.
}
\]

## 9. Why the L2 ledger is stronger

The H1 ledger used the production ceiling

\[
N/P\le\sqrt2B_S,
\]

while the L2 ledger uses only

\[
\frac{-4\int\det\Sigma}{E}
\le
\frac4{3\sqrt6}B_S.
\]

Numerically,

\[
\frac4{3\sqrt6}\approx0.54433
\ll
\sqrt2\approx1.41421.
\]

At the same time, the viscous frequency tax enters the L2 ledger with coefficient `2` instead of `1`. Thus the lower-order ledger is substantially more restrictive once projective anti-ribbon action has forced a positive frequency integral.

## 10. Scope

This is an eventual-infinite-corridor closure obtained by summing actual finite smooth stages. It does not assert that every isolated stage below the radius is individually impossible.

If the corridor loses bounded enstrophy tightness, low moving-ball turnover, positive-middle coherence, or anti-ribbon projective control, the solution leaves this branch and enters the already typed complement.

No ancient limit or compact profile is used.

Status: **PROJECTIVE FRAME ROTATION NOW HAS TO PAY A LOWER-ORDER PRICE AS WELL: THE SAME FORCED FREQUENCY INTEGRAL ENTERS THE STRAIN L2 LEDGER WITH DOUBLE VISCOUS WEIGHT, WHILE THE AVAILABLE DETERMINANT PRODUCTION IS CAPPED BY `4/(3 sqrt(6))`. THE ROBUST QUARTER-TAIL PURE-CORRIDOR S-CLOSURE RADIUS IS THEREFORE EXTENDED TO ABOUT `1.45502 rho0`.**