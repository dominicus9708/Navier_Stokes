# Analyticity-to-Local-Mass and Leakage Gate — 2026-08-20

Status: **LOCAL NON-H/T EXCLUSION SCALE — GLOBAL REGULARITY NOT PROVED.**

This note combines the first-hitting analytic strip from `FIRST_HITTING_ANALYTIC_CONTACT_ELIMINATION_2026-08-20.md` with `LOCAL_SECOND_ORDER_SOLENOIDAL_GATE_2026-08-20.md`.

At a normalized first-hitting snapshot assume

\[
|\Omega(y_*)|=1
\]

and the analytic continuation satisfies

\[
\sup_{|\operatorname{Im}y|<\rho_0}|\Omega(y)|\le M_0,
\qquad M_0\ge1.
\]

The constants `rho_0,M_0` are uniform along the late non-H/T first-hitting sequence, although their numerical values have not yet been extracted from a specific analyticity theorem.

## 1. Cauchy derivative bounds

Apply one-variable Cauchy estimates in each coordinate using complex radius `rho_0/2`.
For every component,

\[
|\partial_j\Omega_i|
\le\frac{2M_0}{\rho_0},
\]

so

\[
\boxed{
\|\nabla\Omega\|_{op}
\le\frac{6M_0}{\rho_0}.
}
\]

Likewise

\[
|\partial_{jj}\Omega_i|
\le\frac{8M_0}{\rho_0^2},
\]

hence

\[
\boxed{
|\Delta\Omega|
\le\frac{24\sqrt3\,M_0}{\rho_0^2}.
}
\]

## 2. First-hitting maximum forces local enstrophy mass

Set

\[
r_a=\frac{\rho_0}{12M_0}.
\]

For `|y-y_*|<=r_a`, the Lipschitz bound gives

\[
|\Omega(y)-\Omega(y_*)|\le\frac12.
\]

Therefore

\[
\boxed{|
\Omega(y)|\ge\frac12
\quad\text{on }B_{r_a}(y_*).
}
\]

In particular, for every `R<=r_a`,

\[
\boxed{
\|\Omega\|_{L^2(B_R(y_*))}
\ge
\sqrt{\frac\pi3}\,R^{3/2}.
}
\]

This gives a local enstrophy mass floor directly from the first-hitting maximum and analyticity, without any global second moment.

## 3. Analytic upper bound for the local second derivative

For the doubled ball,

\[
\|\Delta\Omega\|_{L^2(B_{2R})}
\le
\frac{24\sqrt3M_0}{\rho_0^2}
\left(\frac{32\pi}{3}\right)^{1/2}R^{3/2}.
\]

Dividing by the preceding mass floor gives

\[
\boxed{
R^2
\frac{\|\Delta\Omega\|_{L^2(B_{2R})}}
{\|\Omega\|_{L^2(B_R)}}
\le
96\sqrt6\,M_0\frac{R^2}{\rho_0^2}.
}
\]

## 4. Combine with the localized second-order solenoidal gate

From `LOCAL_SECOND_ORDER_SOLENOIDAL_GATE_2026-08-20.md`, define the normalized annular leakage

\[
\mathcal L_R
:=
C_{loc}^{(2)}
\frac{
R\|\nabla\Omega\|_{L^2(A_R)}
+\|\Omega\|_{L^2(A_R)}
}{
\|\Omega\|_{L^2(B_R)}
},
\]

where

\[
A_R=B_{2R}\setminus B_R.
\]

The local gate is

\[
R^2
\frac{\|\Delta\Omega\|_{L^2(B_{2R})}}
{\|\Omega\|_{L^2(B_R)}}
+\mathcal L_R
\ge1.6799968568.
\]

Hence for every `R<=r_a`,

\[
\boxed{
\mathcal L_R
\ge
1.6799968568
-96\sqrt6\,M_0\frac{R^2}{\rho_0^2}.
}
\]

This is an explicit small-core leakage law.

## 5. Order-one leakage below an analytic exclusion scale

If

\[
R
\le
\rho_0
\sqrt{\frac{1.6799968568}{192\sqrt6\,M_0}},
\]

then the analytic second-derivative term contributes at most half the solenoidal lower bound, so

\[
\boxed{
\mathcal L_R\ge0.8399984284.
}
\]

Numerically,

\[
\sqrt{\frac{1.6799968568}{192\sqrt6}}
\approx0.05976760.
\]

Therefore define

\[
\boxed{
R_{ex}
=
\min\left\{
\frac{\rho_0}{12M_0},
\frac{0.05976760\,\rho_0}{\sqrt{M_0}}
\right\}.
}
\]

Every first-hitting core radius `R<=R_ex` must have order-one normalized annular leakage.

## 6. H/T interpretation

The leakage consists of

\[
R\|\nabla\Omega\|_{L^2(A_R)}
\quad\text{and}\quad
\|\Omega\|_{L^2(A_R)}.
\]

Thus an order-one `mathcal L_R` forces at least one of:

1. an annular derivative packet, naturally routed to `H`;
2. an annular vorticity-mass packet comparable with the tracked core, naturally routed to bounded-radius turnover/multicore `T`.

Consequently, on a quantitative non-H/T branch for which

\[
\mathcal L_R<0.8399984284,
\]

the active first-hitting radius must satisfy

\[
\boxed{R>R_{ex}.}
\]

This is a genuine active-core lower-radius statement. It does not use the global vorticity second moment and therefore avoids the scope problem identified in `RADIUS_BARRIER_SCOPE_CORRECTION_2026-08-20.md`.

## 7. Current unresolved constant

The result is explicit in `rho_0` and `M_0`, but those two constants remain inherited from the short-time vorticity analyticity theorem. The next quantitative task is to select a theorem with explicit constants, or reconstruct the mild-solution analyticity estimate with tracked constants, so that `R_ex` becomes a numerical universal multiple of `sqrt(nu)` in the normalized variables.

Status: **FIRST-HITTING ANALYTICITY PLUS THE LOCAL SECOND-ORDER SOLENOIDAL GATE PRODUCES AN EXPLICIT ACTIVE-CORE EXCLUSION SCALE. BELOW `R_ex`, ORDER-ONE ANNULAR LEAKAGE IS FORCED AND THE BRANCH RETURNS TO `H/T`. THIS IS THE FIRST LOCAL RADIUS LOWER BOUND IN THE NEW SOLENOIDAL ROUTE THAT DOES NOT DEPEND ON A GLOBAL SECOND MOMENT.**