# DSD M5-368 — Compact `q`-Poincaré Defect: Exact Periodic Alpha-Limit or Persistent Reformation

Date: 2026-08-31

Status: **ON A PRECOMPACT `alpha=3/2` EULER SIMILARITY ORBIT, ARBITRARILY SMALL ONE-`q`-STEP SHAPE DEFECT PRODUCES AN EXACT `log q`-PERIODIC ALPHA-LIMIT BY CONTINUITY OF THE EULER FLOW / THAT PERIODIC LIMIT IS REMOVED BY THE DSS RIGIDITY LEDGER ON NO-H / THEREFORE ANY NONTRIVIAL COMPACT SURVIVOR MUST PAY A FIXED POSITIVE SHAPE-REFORMATION DISTANCE EVERY LATE `log q` INTERVAL / ENERGY IS EXACTLY NEUTRAL, SO THIS IS NOT YET A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-365 identified the natural similarity-time DSS period

\[
 T_q=\log q.
\]

The checkpoint clock may approach this spacing without the full profile becoming periodic.

The right question is therefore whether the actual similarity shape nearly returns after time `T_q`.

## 2. Similarity flow

At the energy-conserving Euler exponent

\[
 \alpha=\frac32,
\]

the profile solves

\[
 V_s+\frac35V+\frac25(y\cdot\nabla)V+(V\cdot\nabla)V+\nabla P=0,
 \qquad
 \nabla\cdot V=0.
\]

Let

\[
 \Phi_\sigma:V(s)\mapsto V(s+\sigma)
\]

denote the similarity-time Euler flow in a strong topology `X` in which the extracted orbit is defined and the solution map is continuous.

## 3. One-`q`-step shape defect

Define

\[
 \boxed{
 \Delta_q(s)
 :=
 \|\Phi_{T_q}V(s)-V(s)\|_X,
 \qquad
 T_q=\log q.
 }
\]

This quantity measures actual shape locking, not merely checkpoint-time spacing.

Exact DSS is

\[
 \Delta_q(s)\equiv0.
\]

## 4. Compactness hypothesis

Assume the late similarity orbit

\[
 \mathcal O_+=\{V(s):s\ge s_0\}
\]

is precompact in `X`.

This is the natural quiet complement of derivative/spatial-tail/turnover failure. If precompactness fails, that failure is already an H/T-type escape and this audit is not needed.

## 5. Small defect subsequence produces an exact periodic limit

Suppose

\[
 \liminf_{s\to\infty}\Delta_q(s)=0.
\]

Choose \(s_n\to\infty\) with

\[
 \Delta_q(s_n)\to0.
\]

By precompactness, after a subsequence

\[
 V(s_n)\to V_*
\]

strongly in `X`.

Continuity of the time-`T_q` flow gives

\[
 \Phi_{T_q}V(s_n)	o\Phi_{T_q}V_*.
\]

But

\[
 \|\Phi_{T_q}V(s_n)-V(s_n)\|_X\to0.
\]

Hence

\[
 \boxed{
 \Phi_{T_q}V_*=V_*.
 }
\]

Thus the alpha-limit orbit through \(V_*\) is exactly periodic with period dividing `T_q`.

In physical Euler variables this is an exact `alpha=3/2` DSS solution with scaling factor

\[
 \lambda=q^{2/5}
\]

(or a divisor-period scale).

## 6. Periodic limit is excluded on the no-H branch

M5-366 shows that an exact nontrivial `alpha=3/2` DSS profile cannot survive if the profile gradient remains globally controlled: finite `L2` plus the no-H gradient bound gives sublinear growth, and Chae--Wolf 2023 forces the DSS profile to be spatially constant, hence zero by finite energy.

Alternatively, the Chae--Wolf 2017 energy-conserving DSS theorem applies under the corresponding Euler Type-I gradient bound.

Therefore on the compact no-H derivative lane,

\[
 \boxed{
 \liminf_{s\to\infty}\Delta_q(s)=0
 \Longrightarrow
 \text{contradiction with nontriviality}.
 }
\]

## 7. Persistent-reformation conclusion

Consequently every nontrivial compact no-H survivor must satisfy

\[
 \boxed{
 \liminf_{s\to\infty}\Delta_q(s)>0.
 }
\]

Equivalently, there exist \(s_1\) and \(\delta_q>0\) such that

\[
 \boxed{
 \Delta_q(s)\ge\delta_q
 \qquad\forall s\ge s_1.
 }
\]

This is a much stronger statement than simply saying the orbit is not periodic.

The full shape must move a fixed positive distance during every late `log q` interval.

## 8. Shape-speed lower bound

If the trajectory is absolutely continuous in `X`, then

\[
 \Delta_q(s)
 \le
 \int_s^{s+T_q}\|V_\sigma(\sigma)\|_X\,d\sigma.
\]

Hence

\[
 \boxed{
 \int_s^{s+\log q}\|V_\sigma\|_X\,d\sigma
 \ge\delta_q
 }
\]

for every sufficiently late `s`.

Summing disjoint periods gives

\[
 \boxed{
 \int_{s_1}^{\infty}\|V_s\|_Xds=\infty.
 }
\]

Thus the remaining endpoint is a genuine perpetual-reformation orbit.

## 9. Exact `L2` energy neutrality

Multiply the similarity Euler equation by `V` and integrate over space.

The nonlinear and pressure terms vanish by incompressibility, while

\[
 \int V\cdot(y\cdot\nabla V)
 =-\frac32\|V\|_2^2.
\]

Therefore

\[
 \frac12\frac d{ds}\|V\|_2^2
 +\frac35\|V\|_2^2
 -\frac35\|V\|_2^2
 =0.
\]

Hence

\[
 \boxed{
 \frac d{ds}\|V(s)\|_2^2=0.
 }
\]

The endpoint moves on a fixed kinetic-energy level set.

## 10. Firewall: no energy Lyapunov

Persistent shape speed does **not** contradict finite energy.

The `alpha=3/2` similarity equation is exactly energy neutral. A compact nonperiodic Euler orbit can in principle move forever on the fixed `L2` energy sphere.

Therefore

\[
 \int\|V_s\|_Xds=\infty
\]

is a dynamic necessary condition, not a regularity proof.

## 11. Rotational quotient version

For the RDSS/modulated branch define

\[
 \boxed{
 \Delta_q^{SO(3)}(s)
 :=
 \inf_{R\in SO(3)}
 \|V(s+T_q)-R_*V(s)\|_X,
 }
\]

where

\[
 (R_*V)(y)=R^{-1}V(Ry).
\]

If the rotation-minimized defect has a zero subsequential limit and the orbit is precompact, compactness of `SO(3)` gives an exact RDSS alpha-limit.

That branch is subject to the separate M5-367 RDSS theorem/hypothesis audit.

If instead

\[
 \liminf\Delta_q^{SO(3)}>0,
\]

then even after removing every rigid rotational degree of freedom, the profile has genuine internal shape reformation.

## 12. Formation-axiom endpoint

After quotienting exact periodicity, the quiet Euler endpoint has the form

\[
 \boxed{
 E_{\rm reform}:
 \quad
 \text{precompact finite-energy similarity orbit}
 +
 \Delta_q^{SO(3)}\ge\delta>0
 \text{ every late period}.
 }
\]

This is now the precise dynamic object that remains instead of the vague phrase `aperiodic Type II`.

## 13. Next target

The next audit should express `V_s` using the similarity Euler PDE and separate its finite positive action into standard channels:

\[
 V_s
 =
 -\frac35V
 -\frac25(y\cdot\nabla)V
 -(V\cdot\nabla)V
 -\nabla P.
\]

The aim is to determine whether persistent shape reformation requires

- frequency/derivative H;
- projective/angular-source action;
- pressure-Hessian/transport turnover;
- spatial-tail motion.

A finite list of such channels would reconnect the Euler borderline endpoint to the original Navier--Stokes H/T master tree.

## 14. Audit verdict

### DERIVED

- on a precompact similarity orbit, `liminf Delta_q=0` gives an exact `log q`-periodic alpha-limit;
- the no-H DSS rigidity then eliminates that alpha-limit;
- every surviving compact no-H orbit must have a fixed positive one-period shape defect;
- this implies infinite total shape variation in similarity time;
- `L2` energy is exactly neutral at `alpha=3/2`.

### FIREWALL

- infinite shape variation does not contradict energy conservation;
- recurrence in checkpoint times is not enough without strong state compactness/flow continuity.

### OPEN

- channel decomposition and pricing of persistent shape reformation;
- RDSS alpha-limits without the required far-vorticity decay;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
