# DSD M5-196 — Enstrophy Quantile-Radius Envelope and Minimum-Tail-Fraction Audit

Date: 2026-08-29

Parent: `DSD_M5_195_RADIUS_NORMALIZATION_PROJECTIVE_VS_TRACEFREE_DOMINANCE_AUDIT_2026-08-29.md`

Status: **POSITIVE DISTRIBUTION-PROFILE REDUCTION / THE TRACE-FREE + DIRICHLET + VARIANCE-TIMING CERTIFICATE EXTENDS FROM ONE FIXED QUARTER-TAIL RADIUS TO EVERY ENSTROPHY QUANTILE RADIUS FOR WHICH THE SAME PURE VARIANCE CORRIDOR HOLDS / A SURVIVING PURE BRANCH MUST LIE ABOVE AN EXPLICIT MONOTONE RADIUS ENVELOPE `R_epsilon >= T(epsilon) sqrt(nu)` / EQUIVALENTLY, AT EACH NORMALIZED RADIUS IT MUST LEAVE A MINIMUM FRACTION OF ENSTROPHY OUTSIDE THE BALL / FOR `q=2`, A BALL OF RADIUS `sqrt(nu)` MUST LEAVE ABOUT `32.16%` OF ENSTROPHY OUTSIDE, WHILE A BALL OF RADIUS `1.2 sqrt(nu)` MUST LEAVE ABOUT `24.98%` OUTSIDE / THIS CONVERTS THE LARGE-RADIUS SURVIVOR INTO A QUANTITATIVE NON-TIGHTNESS PROFILE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Quantile radius

For `0<epsilon<1`, define the centered enstrophy quantile radius

\[
\boxed{
R_\varepsilon(s)
:=
\inf\left\{
R>0:
\int_{B_R(X(s))}|\Omega|^2dY
\ge
(1-\varepsilon)Z(s)
\right\},
}
\]

where

\[
Z(s)=\|\Omega(s)\|_2^2.
\]

Thus `epsilon` is the allowed enstrophy tail fraction outside the selected ball.

The quarter-tail radius used previously is

\[
R_{1/4}.
\]

Monotonicity is immediate:

\[
\varepsilon_1<\varepsilon_2
\quad\Longrightarrow\quad
R_{\varepsilon_1}\ge R_{\varepsilon_2}.
\]

---

## 2. Tightness frequency coefficient for an arbitrary tail fraction

The optimized Dirichlet cutoff calculation gives

\[
\boxed{
\frac QZ
\ge
\frac{\Lambda_{tight}(\varepsilon)}{R_\varepsilon^2},
}
\]

where

\[
\boxed{
\Lambda_{tight}(\varepsilon)
=
\left[
\sqrt\pi(1-\varepsilon)^{1/4}
-\varepsilon^{1/4}
\right]^4
}
\]

whenever the bracket is positive.

The bracket is positive for

\[
\boxed{
\varepsilon
<
\frac{\pi^2}{1+\pi^2}
\approx0.90800033.
}
\]

Thus the optimized tightness floor covers essentially every useful quantile short of an extremely weak `~9%` retained mass requirement.

---

## 3. Apply the variance timing ceiling at the same quantile radius

Assume that at the chosen `R_epsilon` the same pure low-turnover variance thresholds used in M5-194Z hold.

Then

\[
L_j
\le
\Pi_{pure}(q)
\frac{R_\varepsilon^2}{\nu},
\]

and therefore

\[
K_I
\le
C_q
\frac{R_\varepsilon^2}{\nu},
\]

where

\[
C_q
=
\frac{q^2}{q-1}\Pi_{pure}(q).
\]

Substitution into the trace-free master gate is identical to M5-194Z, now with `epsilon` arbitrary.

---

## 4. Quantile closure envelope

Define

\[
\boxed{
T_q(\varepsilon)
:=
\left\{
\sqrt3
\left[
\Lambda_{tight}(\varepsilon)
+\frac1{4C_q}
\right]
\right\}^{1/2}.
}
\]

Then the pure branch is closed whenever

\[
\boxed{
R_\varepsilon
<
T_q(\varepsilon)\sqrt\nu.
}
\]

Consequently, a survivor which remains pure at that quantile radius must obey the necessary condition

\[
\boxed{
R_\varepsilon
\ge
T_q(\varepsilon)\sqrt\nu.
}
\]

This is the enstrophy quantile-radius envelope.

---

## 5. `q=2` explicit envelope

For `q=2`,

\[
C_2
\approx5.9871046992.
\]

Representative values are:

\[
\boxed{
\begin{array}{c|c|c}
\varepsilon
&\Lambda_{tight}(\varepsilon)
&T_2(\varepsilon)\\
\hline
0.10&1.83596628&1.80341651\\
0.25&0.78857702&1.19924130\\
0.50&0.17801647&0.61697471\\
0.75&0.01084541&0.30184270\\
0.85&0.00041667&0.27027007
\end{array}
}
\]

Thus, on the pure corridor at each chosen quantile,

- containing `90%` of enstrophy requires radius at least `1.80342 sqrt(nu)`;
- containing `75%` requires at least `1.19924 sqrt(nu)`;
- containing `50%` requires at least `0.61697 sqrt(nu)`.

A survivor cannot consist of a very tiny active core carrying nearly all enstrophy plus a negligible remote tail.

---

## 6. Invert the envelope: minimum tail fraction at fixed radius

Because `T_2(epsilon)` decreases monotonically over the useful range, one can invert it.

For a dimensionless radius

\[
r:=R/\sqrt\nu,
\]

define `epsilon_min(r)` by

\[
\boxed{
T_2(\varepsilon_{min}(r))=r.
}
\]

Then a pure survivor must have at least that fraction of enstrophy outside `B_R`:

\[
\boxed{
\frac{\int_{|Y-X|>R}|\Omega|^2}
{Z}
\ge
\varepsilon_{min}(R/\sqrt\nu).
}
\]

Otherwise the corresponding quantile radius would fall below the closure envelope.

---

## 7. Numerical minimum-tail benchmarks

Solving the envelope equation for `q=2` gives approximately

\[
\boxed{
\begin{array}{c|c}
R/\sqrt\nu
&\varepsilon_{min}\\
\hline
0.50&0.57038\\
0.75&0.43081\\
1.00&0.32165\\
1.20&0.24975\\
1.50&0.16370\\
1.80&0.10060\\
2.00&0.06960\\
3.00&0.00482
\end{array}
}
\]

In particular,

\[
\boxed{
R=\sqrt\nu
\quad\Longrightarrow\quad
\text{at least }32.16\%\text{ of enstrophy must lie outside}
}
\]

on a surviving pure corridor.

Likewise,

\[
\boxed{
R=1.2\sqrt\nu
\quad\Longrightarrow\quad
\text{at least }24.98\%\text{ remains outside}.
}
\]

---

## 8. DSD interpretation

The previous branch statement was only

\[
R_{1/4}\ge1.19924\sqrt\nu.
\]

The quantile envelope is substantially stronger structurally.

It says a survivor must have an entire **enstrophy distribution profile** extending across normalized radii.

Therefore the residual strong-tightness branch is not merely a `large core` in one arbitrary sense. It must maintain a prescribed amount of vorticity content outside every sufficiently small normalized ball.

This is precisely the kind of finite distribution witness that can be compared with

- multicore occupancy;
- moving-ball variance;
- remote strain;
- material replacement;
- canonical critical tails.

---

## 9. Scope firewall

The envelope at a particular `epsilon` uses the pure variance/boundary stage ceiling **at that same radius**.

It is not legitimate to assume purity simultaneously at every quantile radius without proof.

Therefore the exhaustive statement is

\[
\boxed{
\text{for each }\varepsilon:
\quad
R_\varepsilon\ge T_q(\varepsilon)\sqrt\nu
\quad\lor\quad
T_{var/bdry}(R_\varepsilon).
}
\]

If purity fails at some quantile radius, that failure is already a formed turnover/boundary/variance witness rather than a gap in the radius argument.

---

## 10. New large-radius frontier

A branch that avoids all quantile-level `T_var/bdry` exits must satisfy the entire envelope

\[
\boxed{
R_\varepsilon
\ge
T_q(\varepsilon)\sqrt\nu
}
\]

for every audited tail fraction.

This forces a broad normalized enstrophy distribution.

The remaining question is whether this broad distribution can still be **one coherent core**, or whether geometric packing/finite-memory arguments force multiple dynamically distinguishable packets.

---

## 11. Next audit target

Use the quantile envelope to estimate how many disjoint or weakly overlapping normalized subregions are required to carry the mandated outside-enstrophy fractions while preserving the pointwise first-hitting cap

\[
|\Omega|\le1.
\]

A pure volume lower bound gives only spatial occupancy and does not yet imply multiple coherent packets.

Therefore the next audit must separate:

1. one broad connected low-amplitude vorticity body;
2. several separated active packets;
3. a diffuse critical halo.

Cases 2 and 3 interface with the existing finite-memory/turnover and critical-tail ledgers; case 1 becomes the precise broad-core geometry that remains to be tested.
