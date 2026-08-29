# DSD M5-194Z — `K_I` Elimination and Trace-Free Tightness-Radius Closure

Date: 2026-08-29

Parent chain: `M5-194S` -- `M5-194Y`

Status: **POSITIVE CONSTANT CLOSURE ON THE PURE STRONG-TIGHTNESS/LOW-TURNOVER CORRIDOR / THE ABSTRACT CONTINUOUS TYPE-I CONSTANT `K_I` CAN BE ELIMINATED USING THE EXISTING VARIANCE STAGE CEILING AT THE SAME VORTICITY-TIGHTNESS RADIUS / THE TRACE-FREE + OPTIMIZED DIRICHLET FREQUENCY CERTIFICATE THEN BECOMES A SINGLE DIMENSIONLESS RADIUS INEQUALITY / FOR `q=2`, `epsilon_Z=1/4`, THE SUFFICIENT CLOSED RADIUS IMPROVES FROM `R_Z <= 1.16869819 sqrt(nu)` TO `R_Z < 1.19924130 sqrt(nu)` ON THE PURE VARIANCE CORRIDOR / FAILURE OF THE PURE VARIANCE HYPOTHESES IS ROUTED TO `T_var/bdry(R_Z)` / GLOBAL REGULARITY UNPROVED.**

---

## 1. Existing strong-tightness master certificate

On the stage-wide vorticity-tight corridor the optimized Dirichlet argument gives

\[
\boxed{
\frac{Q}{Z}
\ge
\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2},
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
\right]^4.
}
\]

Combined with the universal trace-free stretching coefficient, the existing master sufficient condition is

\[
\boxed{
2K_I
\left(
\frac1{\sqrt3}
-\nu\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}
\right)_+
<\frac12.
}
\]

Previously `K_I` was retained as a separate Type-I timing constant.

---

## 2. Continuous backward Type-I constant from a stage ceiling

For first-hitting levels

\[
W_{j+1}=qW_j,
\]

the continuous backward vorticity estimate derived earlier has constant

\[
\boxed{
K_I
=\frac{q^2}{q-1}L_+
}
\]

when every late dynamic stage obeys

\[
L_j\le L_+.
\]

This follows from the geometric sum of the backward stage durations and is the same constant used in the ancient continuous Type-I note.

---

## 3. Eliminate `L_+` on the pure variance corridor

The tightness-radius variance stage-ceiling theorem gives, on the explicitly defined low-turnover pure corridor at the same radius `R_Z`,

\[
\boxed{
L_j
\le
L_{var,+}
=
\Pi_{pure}(q)\frac{R_Z^2}{\nu},
}
\]

where

\[
\boxed{
\Pi_{pure}(q)
=
\frac8{\pi^2}
\left(
\frac12\log q+\frac32
\right).
}
\]

Therefore

\[
\boxed{
K_I
\le
C_q\frac{R_Z^2}{\nu},
}
\]

with

\[
\boxed{
C_q
:=
\frac{q^2}{q-1}\Pi_{pure}(q).
}
\]

This removes the solution-dependent timing constant on the pure branch.

If the variance/boundary assumptions needed for this ceiling fail, the solution has already exited to

\[
T_{var/bdry}(R_Z),
\]

so this estimate is not used there.

---

## 4. Substitute into the trace-free master certificate

Because the coefficient in parentheses is nonnegative after taking the positive part, replacing `K_I` by its upper bound gives the sufficient condition

\[
2C_q\frac{R_Z^2}{\nu}
\left(
\frac1{\sqrt3}
-\nu\frac{\Lambda_{tight}}{R_Z^2}
\right)_+
<\frac12.
\]

Introduce the dimensionless radius squared

\[
\boxed{
\rho_Z:=\frac{R_Z^2}{\nu}.
}
\]

Then

\[
\boxed{
2C_q
\left(
\frac{\rho_Z}{\sqrt3}
-\Lambda_{tight}(\varepsilon_Z)
\right)_+
<\frac12.
}
\]

Thus the entire timing+tightness certificate depends only on

\[
q,
\qquad
\varepsilon_Z,
\qquad
\rho_Z.
\]

---

## 5. Closed radius formula

If

\[
\rho_Z
\le
\sqrt3\,\Lambda_{tight},
\]

the positive part vanishes and the branch is already closed by the timing-independent viscosity gate.

Above that value, the inequality is

\[
2C_q
\left(
\frac{\rho_Z}{\sqrt3}
-\Lambda_{tight}
\right)
<\frac12.
\]

Therefore a sufficient closure condition on the full pure branch is

\[
\boxed{
\rho_Z
<
\rho_{TF,var}(q,\varepsilon_Z)
:=
\sqrt3
\left[
\Lambda_{tight}(\varepsilon_Z)
+
\frac1{4C_q}
\right].
}
\]

Equivalently,

\[
\boxed{
R_Z
<
R_{TF,var}(q,\varepsilon_Z)
:=
\sqrt{\nu}
\left\{
\sqrt3
\left[
\Lambda_{tight}(\varepsilon_Z)
+
\frac1{4C_q}
\right]
\right\}^{1/2}.
}
\]

This is the new combined radius certificate.

---

## 6. `q=2`, quarter-tail benchmark

For

\[
q=2,
\qquad
\varepsilon_Z=\frac14,
\]

the established constants are

\[
\Pi_{pure}(2)
\approx1.4967761748,
\]

so

\[
\boxed{
C_2
=4\Pi_{pure}(2)
\approx5.9871046992.
}
\]

Also

\[
\boxed{
\Lambda_{tight}(1/4)
\approx0.7885770233.
}
\]

Hence

\[
\rho_{TF,var}
=
\sqrt3
\left(
0.7885770233
+
\frac1{4(5.9871046992)}
\right)
\approx
\boxed{1.4381796941}.
\]

Taking the square root,

\[
\boxed{
R_Z
<
1.1992412994\,\sqrt\nu
}
\]

is sufficient to close the pure quarter-tail corridor.

Rounded conservatively,

\[
\boxed{
R_Z
<1.19924\sqrt\nu.
}
\]

---

## 7. Improvement over the timing-independent radius

The timing-independent tightness certificate gave

\[
R_Z
\le
1.16869819\sqrt\nu
\]

for `epsilon_Z=1/4`.

The new pure-variance timing insertion extends this to

\[
R_Z<1.19924130\sqrt\nu.
\]

The absolute normalized-radius gain is approximately

\[
\boxed{0.03054310\sqrt\nu,}
\]

about a `2.61%` increase in radius.

The gain is modest because the trace-free viscosity gate was already strong, but it is genuine and removes `K_I` as an independent parameter on this branch.

---

## 8. Necessary radius for any surviving pure quarter-tail branch

Consequently, a nonzero singular survivor remaining on all hypotheses of this pure lane must satisfy

\[
\boxed{
R_Z
\ge
1.19924130\sqrt\nu.
}
\]

Otherwise the trace-free/tightness/timing inequality contradicts the inherited backward enstrophy behavior.

Thus the pure survivor is forced into a **large normalized vorticity-support radius**.

This is exactly the regime in which multicore, remote-tail, variance, and boundary-flux alternatives become more plausible and should be audited next.

---

## 9. DSD branch statement

The strong-tightness branch now has the finite split

\[
\boxed{
\begin{cases}
R_Z< R_{TF,var}
&\Longrightarrow \text{pure branch closed},\\[1mm]
R_Z\ge R_{TF,var}
&\Longrightarrow \text{large-radius pure survivor},\\[1mm]
\text{variance/boundary purity fails}
&\Longrightarrow T_{var/bdry}(R_Z).
\end{cases}
}
\]

No Betchov residual parameter is required for this split on the quarter-tail strong-tightness corridor.

---

## 10. Scope firewall

This calculation does not prove that every singular branch is quarter-tail tight.

It does not prove that `R_Z>=1.19924 sqrt(nu)` is impossible.

It does not close `T_var/bdry` or the escaping critical-tail topology.

It proves only that on the explicit pure low-turnover quarter-tail corridor, the abstract Type-I timing constant can be eliminated and a larger finite radius range can be rigorously excluded by the already established scalar ledgers.

---

## 11. Next audit target

The remaining pure quarter-tail survivor now satisfies a definite large-radius condition

\[
R_Z\ge1.19924\sqrt\nu.
\]

The next calculation should compare this lower bound with the finite-core projective/anti-ribbon closure radius and the coherent-multiflux capacity radius.

If the projective closure covers the same or a larger radius range under compatible hypotheses, the overlap can eliminate another interval.

If there is a gap, its exact endpoints become the next finite parameter window rather than an unbounded qualitative branch.
