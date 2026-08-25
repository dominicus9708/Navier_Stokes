# DSD Bounded-Z Type-I Excludes Relative-Campanato Escalation

Date: 2026-08-25

Status: **CAMPANATO ESCALATION EXCLUDED ON THE BOUNDED-Z TYPE-I CENTER-NESTED CORRIDOR / USES STANDARD INTERIOR TYPE-I LOCAL-ENERGY THEORY / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The preceding weak-L3 endpoint reduction gives

\[
L^{3,\infty}\text{ residual escalation}
\Longrightarrow
\text{relative-Campanato escalation}
\lor
H_{2,crit}^{tail}.
\]

This note removes the Campanato alternative on the current bounded-Z Type-I corridor.

## 2. Dynamic normalization and physical scale

Let

\[
M(t)=\|\omega(t)\|_\infty,
\qquad
r(t)=\sqrt{\nu/M(t)}.
\]

At a first-hitting state centered at `X(t)`, define

\[
U(Y,t)=\frac{u(X(t)+r(t)Y,t)}{\sqrt{\nu M(t)}}.
\]

Equivalently, if

\[
v=u/\nu,
\]

then

\[
U(Y,t)=r(t)v(X(t)+r(t)Y,t).
\]

For normalized radius `R`, set the physical radius

\[
\ell=rR.
\]

The relative Campanato quantity is exactly scale invariant:

\[
\boxed{
\mathcal C_R[U]
=
R^{-1}\int_{B_R}|U-(U)_{B_R}|^2dY
=
\ell^{-1}\int_{B_\ell(X)}|v-(v)_{B_\ell(X)}|^2dx.
}
\]

In the original velocity variable,

\[
\boxed{
\mathcal C_R[U]
=
\frac1{\nu^2\ell}
\int_{B_\ell(X)}|u-(u)_{B_\ell(X)}|^2dx.
}
\]

## 3. Bounded normalized enstrophy gives pointwise velocity Type I

Assume the recurrent corridor has

\[
Z_D(t):=\int |\Omega_D|^2dY\le Z_+,
\]

where

\[
\Omega_D=\omega/M.
\]

Scaling gives

\[
\|\omega(t)\|_2^2
=\nu^{3/2}M(t)^{1/2}Z_D(t).
\]

Hence

\[
\|\omega(t)\|_2
\le \nu^{3/4}M(t)^{1/4}Z_+^{1/2}.
\]

The whole-space Biot-Savart interpolation estimate

\[
\|u\|_\infty
\le C_{BS}\|\omega\|_\infty^{1/3}\|\omega\|_2^{2/3}
\]

therefore yields

\[
\boxed{
\|u(t)\|_\infty
\le C_{BS}\nu^{1/2}M(t)^{1/2}Z_+^{1/3}.
}
\]

On the current Type-I first-hitting corridor,

\[
(T^*-t)M(t)\le K_I.
\]

Thus

\[
\boxed{
\|u(t)\|_\infty
\le
C_{BS}\nu^{1/2}K_I^{1/2}Z_+^{1/3}(T^*-t)^{-1/2}.
}
\]

Set the unit-viscosity time

\[
\tau=\nu t,
\qquad
\tau^*=\nu T^*.
\]

Then `v=u/nu` solves unit-viscosity Navier-Stokes and

\[
\boxed{
|v(x,\tau)|
\le
M_{vel}(\tau^*-\tau)^{-1/2},
\qquad
M_{vel}=C_{BS}K_I^{1/2}Z_+^{1/3}.
}
\]

This is the standard pointwise Type-I velocity condition.

## 4. Standard interior Type-I local-energy bound

For suitable weak solutions, the standard interior Type-I theory implies that a pointwise Type-I velocity bound in a neighborhood of a singular point yields a uniform scale-invariant local-energy bound

\[
\boxed{
A_*:=
\sup_{0<\ell<\ell_0}
\sup_{\tau^*-\ell^2<\tau<\tau^*}
\ell^{-1}
\int_{B_\ell(x^*)}|v(x,\tau)|^2dx
<\infty.
}
\]

This implication is the classical Seregin-Zajaczkowski / Seregin-Sverak interior Type-I energy estimate, also recalled in later Barker-Prange Type-I work.

No new theorem is claimed in this step; the project imports the standard interior estimate.

## 5. A Campanato-escalating sequence must go to large normalized radius

Suppose for contradiction that recurrent first-hitting states contain radii `R_j` with

\[
\mathcal C_{R_j}[U_j]\to\infty.
\]

On every fixed normalized ball, the recurrent analytic corridor has uniform smooth bounds. Therefore `R_j` cannot remain bounded.

Hence

\[
\boxed{R_j\to\infty.}
\]

## 6. But the corresponding physical radii shrink to zero

Let

\[
\ell_j=r_jR_j.
\]

Finite physical kinetic energy gives

\[
\mathcal C_{R_j}[U_j]
\le
\ell_j^{-1}\|v(t_j)\|_2^2
\le
E_v\ell_j^{-1},
\]

where

\[
E_v=\sup_{t<T^*}\|v(t)\|_2^2<\infty.
\]

Therefore

\[
\mathcal C_{R_j}\to\infty
\Longrightarrow
\boxed{\ell_j\to0.}
\]

Thus normalized remote Campanato escalation corresponds to physical concentration onto the singular point, not to a fixed macroscopic reservoir.

## 7. Center nesting places the escalating ball at the singular point

On the no-center-turnover recurrent corridor, the tracked centers satisfy

\[
|X_j-x^*|\le C_Xr_j.
\]

Since `R_j->infinity`,

\[
\frac{|X_j-x^*|}{\ell_j}
\le
\frac{C_X}{R_j}\to0.
\]

Hence for all large `j`,

\[
B_{\ell_j}(X_j)
\subset
B_{2\ell_j}(x^*).
\]

Also

\[
\tau^*-\tau_j
=\nu(T^*-t_j)
=\Theta_jr_j^2,
\]

with `Theta_j` uniformly bounded on the Type-I corridor. Since `R_j->infinity`,

\[
\tau^*-\tau_j
\ll
\ell_j^2=R_j^2r_j^2.
\]

Thus `tau_j` lies in the parabolic time window used by the local-energy quantity at radius `2 ell_j`.

## 8. Contradiction with the Type-I local-energy bound

The relative mean minimizes squared deviation, so

\[
\begin{aligned}
\mathcal C_{R_j}[U_j]
&=
\ell_j^{-1}
\int_{B_{\ell_j}(X_j)}
|v-(v)_{B_{\ell_j}(X_j)}|^2dx\\
&\le
\ell_j^{-1}
\int_{B_{\ell_j}(X_j)}|v|^2dx\\
&\le
\ell_j^{-1}
\int_{B_{2\ell_j}(x^*)}|v|^2dx\\
&\le 2A_*.
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_j\mathcal C_{R_j}[U_j]\le2A_*<\infty,
}
\]

contradicting Campanato escalation.

Hence

\[
\boxed{
\text{bounded-Z Type-I + center nesting}
\Longrightarrow
\text{no relative-Campanato escalation}.
}
\]

## 9. Consequence for the residual weak-L3 frontier

Combining with `DSD_WEAK_L3_FROM_UNIFORM_ANNULAR_CRITICAL_H1_2026-08-25.md` and `CRITICAL_H1_TAIL_TO_CAMPANATO_OR_H2_2026-08-24.md`,

\[
\boxed{
L^{3,\infty}\text{ residual escalation}
\Longrightarrow
H_{2,crit}^{tail}
}
\]

on the bounded-Z Type-I center-nested corridor.

Thus the last residual weak-critical escape is forced into a derivative-tail `H` branch rather than a new low-frequency/turnover branch.

## 10. Scope audit

This argument depends on:

1. uniform bounded normalized enstrophy `Z_D<=Z_+` through the relevant late corridor;
2. the Type-I amplitude bound `(T^*-t)M(t)<=K_I`;
3. center nesting/no-center-turnover;
4. finite physical kinetic energy;
5. the standard interior pointwise-Type-I -> scale-invariant local-energy theorem.

If center nesting fails, that failure is already a `T`/center-turnover branch.

If bounded-Z or Type-I fails, the trajectory has already left the current survivor corridor.

## 11. Audit verdict

### PROVED, conditional on the standard imported Type-I local-energy theorem

- bounded normalized enstrophy implies pointwise velocity Type I;
- any Campanato-escalating normalized radius must satisfy `R_j->infinity` and physical radius `ell_j->0`;
- center nesting places those balls inside the singular-point local-energy cylinder;
- the standard Type-I local-energy bound forbids the escalation.

### UPDATED FRONTIER

\[
\boxed{
L^{3,\infty}\text{ residual escalation}
\Longrightarrow
H_{2,crit}^{tail}
\quad\text{or an already typed corridor failure.}
}
\]

### STILL NOT PROVED HERE

- that every `H2crit_tail` sequence produces a globally contradictory H charge;
- the final master branch audit;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
