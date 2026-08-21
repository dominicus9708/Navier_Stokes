# Smooth Projective-Action / Viscous-Tax Closure — 2026-08-21

Status: **SMOOTH MULTISTAGE S-CLOSURE CERTIFICATE FOR A BOUNDED PURE P_V CORRIDOR / GLOBAL REGULARITY NOT PROVED.**

This note converts the transverse anti-ribbon projective action itself into a lower bound on the frequency integral `int lambda ds`, and hence into a viscous H1 tax. It remains entirely on finite smooth first-hitting stages; only the final contradiction sums many such stages.

## 1. Stage data

Work on a geometric first-hitting stage `I_j` with normalized length

\[
L_j=|I_j|.
\]

Let

\[
E=\|\Sigma\|_2^2,
\qquad
P=\|\nabla\Sigma\|_2^2,
\qquad
H=\|\Delta\Sigma\|_2^2,
\qquad
\lambda=P/E.
\]

Let

\[
Z=\|\Omega\|_2^2=2E.
\]

Assume the broad pure moving-ball corridor, so for `q=2`, `M0=2`, `sigma=1/2`,

\[
\boxed{
L_j
\le
L_{\max}(r)
:=
\frac12\,1.4967761748\,r^2
}
\]

where

\[
r=R_C/\rho_0
\]

and the conservative replacement `c_*(2)>=1` has already been made.

Numerically,

\[
L_{\max}(r)=0.7483880874\,r^2.
\]

## 2. Exact projective-speed/frequency relation

The algebraic projective residual satisfies

\[
\frac{\|\mathcal V\|_2}{\|\Sigma\|_2}
\le
\frac13S_3^{-3/4}\lambda^{3/4}E^{1/2}
+\frac{\sqrt2}{4},
\]

where

\[
S_3=3\left(\frac\pi2\right)^{4/3}.
\]

Define the instantaneous projective speed

\[
c_V(s)=\frac{\|\mathcal V(s)\|_2}{\|\Sigma(s)\|_2}
\]

and

\[
c_0=\frac{\sqrt2}{4},
\qquad
K_P=\frac1{3\sqrt2}S_3^{-3/4}.
\]

Since `E=Z/2`,

\[
\boxed{
c_V-c_0
\le
K_P\lambda^{3/4}Z^{1/2}.
}
\]

Hence, if `Z(s)<=Z_+` throughout the stage,

\[
\boxed{
\lambda(s)
\ge
K_P^{-4/3}Z_+^{-2/3}
(c_V(s)-c_0)_+^{4/3}.
}
\]

Numerically,

\[
K_P\approx0.06582682817.
\]

## 3. Anti-ribbon action lower bound

The transverse material-line/eigenframe angle gate gives

\[
\frac{L_j}{2}+\operatorname{TV}(\theta_e)
\ge
\frac\pi2.
\]

On the pure projective lane, the eigenframe total variation is controlled by the projective action,

\[
\operatorname{TV}(\theta_e)
\le
\int_{I_j}c_V(s)ds.
\]

Therefore

\[
\boxed{
\int_{I_j}c_V(s)ds
\ge
\frac{\pi-L_j}{2}.
}
\]

It follows that

\[
\int_{I_j}(c_V-c_0)_+ds
\ge
\left[
\frac\pi2-\left(\frac12+c_0\right)L_j
\right]_+.
\]

Set

\[
A(L)
=
\left[
\frac\pi2-\left(\frac12+\frac{\sqrt2}{4}\right)L
\right]_+.
\]

## 4. Projective action forces a frequency integral

Holder/Jensen gives

\[
\int_{I_j}(c_V-c_0)_+^{4/3}ds
\ge
L_j^{-1/3}
\left(
\int_{I_j}(c_V-c_0)_+ds
\right)^{4/3}.
\]

Therefore

\[
\boxed{
\int_{I_j}\lambda ds
\ge
K_P^{-4/3}Z_+^{-2/3}
L_j^{-1/3}A(L_j)^{4/3}.
}
\]

This is the central new bridge: projective anti-ribbon action necessarily creates a positive viscous-frequency budget.

## 5. Insert enstrophy tightness

Assume enstrophy is `epsilon_Z`-tight in the common normalized radius `R_C=r rho0` throughout the pure stage. Since `|Omega|<=1`,

\[
Z_+
\le
\frac{4\pi}{3}
\frac{R_C^3}{1-\varepsilon_Z}.
\]

Define dimensionless

\[
\bar Z_+=Z_+/\rho_0^3.
\]

Then

\[
\boxed{
\bar Z_+
\le
\frac{4\pi}{3}
\frac{r^3}{1-\varepsilon_Z}.
}
\]

Also

\[
\nu\lambda
=
\frac\nu{\rho_0^2}(\lambda\rho_0^2)
\ge
2(\lambda\rho_0^2)
\]

because `rho0^2=(nu/2)/c_*(2)^2` and `c_*(2)>=1`.

Consequently

\[
\boxed{
\nu\int_{I_j}\lambda ds
\ge
2K_P^{-4/3}
\bar Z_+^{-2/3}
L_j^{-1/3}A(L_j)^{4/3}.
}
\]

## 6. H1 finite-stage ledger

The running first-hitting H1 ledger is

\[
\boxed{
\frac12\log\frac{P(s_1)}{P(s_0)}
+\frac34\log q
+\nu\int_{I_j}\frac HPds
=
\int_{I_j}\frac NPds.
}
\]

Interpolation gives

\[
\frac HP\ge\frac PE=\lambda.
\]

The nonnormality bound gives

\[
\frac NP\le\sqrt2\|\Sigma\|_\infty.
\]

If

\[
\|\Sigma\|_\infty\le B_+(r),
\]

then

\[
\int_{I_j}\frac NPds
\le
\sqrt2B_+(r)L_j.
\]

## 7. Explicit strain ceiling

The second-Taylor Biot-Savart bound gives, for `M0=2`,

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

For the robust quarter enstrophy tail,

\[
\varepsilon_Z\le\frac14,
\]

\[
\boxed{
B_+(r)
\le
2.4335795280140466\,r^{6/7}.
}
\]

## 8. Multistage telescoping

On a bounded pure corridor with fixed positive lower and upper bounds on endpoint `P`, summing the H1 ledger over `N` consecutive first-hitting stages makes

\[
\frac1N\log\frac{P_N}{P_0}\to0.
\]

Such endpoint bounds follow from the already-derived smooth frequency corridor together with bounded enstrophy/derivative tightness. Therefore an infinite pure lane requires asymptotically, per stage,

\[
\sqrt2B_+(r)L_j
\ge
\frac34\log q
+
u\int_{I_j}\lambda ds.
\]

For the relevant range `A(L)>0`, the production upper bound increases with `L`, while the frequency-tax lower bound decreases with `L`. Hence the worst case is `L=L_max(r)`.

Thus an infinite pure lane is S-closed whenever

\[
\boxed{
\sqrt2B_+(r)L_{\max}(r)
<
\frac34\log2
+2K_P^{-4/3}
\bar Z_+(r)^{-2/3}
L_{\max}(r)^{-1/3}
A(L_{\max}(r))^{4/3}.
}
\]

## 9. Explicit quarter-tail closure radius

Use

\[
\varepsilon_Z\le\frac14,
\qquad
\varepsilon_Q\le\frac14
\]

throughout the bounded pure corridor. The derivative-tail condition is used to keep endpoint `P` uniformly bounded for the telescoping step.

With

\[
L_{\max}(r)=0.7483880874r^2,
\]

\[
B_+(r)=2.4335795280140466r^{6/7},
\]

\[
\bar Z_+(r)=\frac{16\pi}{9}r^3,
\]

the equality in the preceding closure test occurs at

\[
\boxed{
r_{PA}^{(1/4)}
\approx1.3030842670.
}
\]

Therefore the entire eventual bounded pure positive-middle anti-ribbon corridor is S-closed for

\[
\boxed{
r<1.3030842670
}
\]

under quarter enstrophy and derivative tails.

This is stronger than the earlier direct swap threshold `1.06060560` and the double-saturation threshold `1.09820167`.

## 10. Zero-tail benchmark

For `epsilon_Z=epsilon_Q=0`, the same calculation gives

\[
\boxed{
r_{PA}^{(0)}
\approx1.3334764784.
}
\]

This is a benchmark, not a replacement for the robust quarter-tail statement.

## 11. Scope

This result closes an **eventual infinite smooth pure corridor**, not every isolated stage. The telescoping `log P` boundary term is essential.

If any of the required bounded/tight conditions fail, the stage exits to an already typed complement:

- derivative or enstrophy spatial tail;
- moving-ball boundary/material turnover;
- endpoint frequency/shape escape;
- loss of positive-middle coherent anti-ribbon geometry.

No ancient solution, compact limit or stationary-profile argument is used.

Status: **ANTI-RIBBON PROJECTIVE ACTION NOW PAYS TWICE: IT MUST ROTATE THE TRANSVERSE STRAIN FRAME AND, THROUGH THE SOBOLEV PROJECTIVE-SPEED BOUND, IT FORCES A POSITIVE FREQUENCY INTEGRAL THAT APPEARS DIRECTLY IN THE VISCOUS H1 LEDGER. THIS EXTENDS THE ROBUST QUARTER-TAIL SMOOTH PURE-CORRIDOR S-CLOSURE TO ABOUT `1.30308 rho0`.**