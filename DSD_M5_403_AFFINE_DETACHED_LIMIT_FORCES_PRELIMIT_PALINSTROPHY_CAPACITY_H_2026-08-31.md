# DSD M5-403 — An affine detached limit forces prelimit palinstrophy-capacity H

Date: 2026-08-31

Status: **THE AFFINE/SOLID-ROTATION FIXED-POINT ANTI-MODEL OF M5-285 REMAINS A VALID LOCAL ANCIENT SOLUTION, BUT IT CANNOT APPEAR ON ARBITRARILY LARGE FIXED SATELLITE WINDOWS FROM SMOOTH FINITE-ENSTROPHY PRELIMITS WITHOUT AN EXPLICIT CAPACITY COST / IF THE DETACHED LIMIT HAS NONZERO CONSTANT VORTICITY, LOCAL CONVERGENCE ON `B_R` MAKES ONE FIXED VORTICITY COMPONENT ORDER ONE THROUGHOUT `B_R`; THE GLOBAL `dot H1 -> L6` SOBOLEV INEQUALITY THEN FORCES PRELIMIT PALINSTROPHY `int |grad omega|^2 >= c R` / DIAGONALIZING `R -> infinity` GIVES DIVERGENT NORMALIZED PALINSTROPHY / THUS THE EXACT AFFINE FIXED-POINT ESCAPE ROUTES TO `H_cap/pal` EVEN THOUGH THE LIMIT ITSELF HAS ZERO VORTICITY GRADIENT / THIS DOES NOT EXCLUDE GENERAL DETACHED ANCIENT PROFILES OR CLOSE H / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-285 records the exact stationary affine anti-model

\[
u_\infty(x)=Ax,
\qquad A^T=-A,
\qquad A\ne0,
\]

with constant nonzero vorticity.

Satellite recentering reproduces this profile modulo a Galilean constant, so repeated satellite extraction is not an infinite-descent contradiction.

M5-283 correctly warns that finite physical energy need not pass to the detached local limit on expanding windows.

However the prelimit fields are not arbitrary local solutions. At every smooth preterminal snapshot their vorticity lies in the finite Sobolev class required for the ordinary global Sobolev inequality.

This supplies a simpler ancestry test for the specific constant-vorticity affine fixed point.

---

## 2. Detached affine convergence

Let

\[
\widetilde u_n
\to
u_\infty
\]

smoothly on every fixed compact spatial set at one retained satellite time, after the usual Galilean normalization.

Assume the limiting profile is the nonzero solid-rotation affine solution

\[
u_\infty(x)=Ax
\]

with constant vorticity

\[
\omega_\infty
:=
\nabla\times u_\infty
\ne0.
\]

Normalize the satellite mark so that

\[
|\omega_\infty|=1.
\]

Let

\[
e:=\omega_\infty.
\]

Then

\[
\boxed{
e\cdot\omega_\infty\equiv1.}
\]

---

## 3. Fixed-window convergence produces a large constant-sign vorticity ball

Fix any finite radius

\[
R>1.
\]

Smooth local convergence implies that for all sufficiently large `n=n(R)`,

\[
\sup_{B_R}
|\widetilde\omega_n-\omega_\infty|
\le\frac12.
\]

Therefore the scalar component

\[
f_n:=e\cdot\widetilde\omega_n
\]

satisfies

\[
\boxed{
f_n\ge\frac12
\quad\text{on }B_R.}
\]

No expanding-window convergence theorem is used here: `R` is fixed first, and only then is the prelimit index taken sufficiently large.

---

## 4. Global Sobolev capacity estimate

At every finite smooth preterminal stage, the scaled vorticity is a smooth finite-energy/enstrophy field and the retained snapshot has finite palinstrophy. Hence

\[
f_n\in\dot H^1(\mathbb R^3)
\]

for each fixed `n`.

The standard homogeneous Sobolev inequality gives

\[
\|f_n\|_{L^6}^2
\le
C_S\|\nabla f_n\|_{L^2}^2.
\]

But since `f_n>=1/2` on `B_R`,

\[
\begin{aligned}
\|f_n\|_6^2
&=
\left(\int|f_n|^6dx\right)^{1/3}\\
&\ge
\left(
2^{-6}|B_R|
\right)^{1/3}\\
&\ge
cR.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_{\mathbb R^3}|\nabla f_n|^2dx
\ge cR.
}
\]

Since

\[
|\nabla f_n|
\le
|\nabla\widetilde\omega_n|,
\]

we obtain

\[
\boxed{
\int_{\mathbb R^3}
|\nabla\widetilde\omega_n|^2dx
\ge cR.
}
\]

This is exactly the `H1` capacity of maintaining an order-one scalar state on a ball of radius `R` while remaining in the global finite Sobolev class.

---

## 5. Diagonalize the radius

Choose any sequence

\[
R_m\to\infty.
\]

For each `R_m`, local convergence provides an index `n_m` large enough that the Section 3 lower bound holds on `B_{R_m}`.

Then

\[
\boxed{
\int
|\nabla\widetilde\omega_{n_m}|^2dx
\ge
cR_m
\to\infty.
}
\]

Thus

\[
\boxed{
\text{nonzero constant-vorticity affine detached limit}
\Longrightarrow
H_{pal/cap}^{prelimit}.
}
\]

The affine limit itself has `grad omega_infinity=0`; the divergent cost lives in the transition to the finite-Sobolev exterior of the approximating fields.

---

## 6. Why M5-283's expanding-window firewall is not violated

M5-283 shows that fixed-window convergence does not transfer a global finite-energy or critical Morrey bound to the detached limit, because the radius at which physical ancestry becomes visible may diverge arbitrarily fast.

M5-403 does not attempt such a transfer.

For every fixed `R`, it uses only:

1. local convergence on `B_R`;
2. the global Sobolev inequality for the **prelimit** field.

Then it chooses a new prelimit index after increasing `R`.

No claim is made that one fixed sequence converges uniformly on a prescribed ancestry radius such as `R~L_n`.

Thus the earlier firewall remains intact.

---

## 7. Relation to transition-layer intuition

The Sobolev estimate is the coordinate-free version of the following transition fact.

A prelimit field that looks like constant nonzero vorticity throughout a larger and larger ball but belongs globally to the finite `H1` class must eventually connect that state to a decaying/finite-Sobolev exterior.

The three-dimensional capacity of the ball is proportional to its radius.

Therefore broadening the transition layer does not make the `dot H1` price vanish.

The global Sobolev inequality proves this without assuming radial symmetry, a regular transition shell, or one tubular normal foliation.

---

## 8. Extension to any persistent nondecaying scalar vorticity component

The argument does not require an exactly affine velocity.

Suppose a detached limit has a unit vector `e`, a constant `c0>0`, and radii `R_m->infinity` such that

\[
e\cdot\omega_\infty
\ge c_0
\quad\text{on }B_{R_m}.
\]

Then the same local-convergence/Sobolev argument gives

\[
\boxed{
\int|\nabla\widetilde\omega_{n_m}|^2
\gtrsim
c_0^2R_m.
}
\]

Thus any detached profile with a nondecaying constant-sign vorticity component on arbitrarily large balls routes to the same capacity H.

---

## 9. What remains outside this lemma

A detached ancient profile may have

- nonzero vorticity near the origin but vorticity decaying at infinity;
- oscillating/cancelling vorticity with no constant-sign component on large balls;
- finite critical weak-`L3` behavior;
- an affine harmonic **strain** component combined with localized vorticity;
- non-affine growth that evades the constant-component hypothesis.

M5-403 does not classify those profiles.

They remain in the detached restart/expanding-window/critical-inheritance frontier.

---

## 10. DSD audit

### Standard input

\[
\dot H^1(\mathbb R^3)
\hookrightarrow
L^6(\mathbb R^3).
\]

### Derived

\[
\boxed{
\omega_n\approx\omega_0\ne0
\text{ on }B_R
\Longrightarrow
\int|\nabla\omega_n|^2\gtrsim R.
}
\]

### Firewall

- the affine limit itself does not pay this gradient cost;
- the cost is borne by finite-Sobolev prelimit transition structure;
- divergent palinstrophy is an H event, not yet a contradiction;
- no global critical norm is claimed for the detached limit.

---

## 11. Updated satellite frontier

M5-402 leaves

\[
S_{remote}
\Longrightarrow
T_{dynamic}
\lor
A_{detached}
\lor
S_{remote}^{next}.
\]

M5-403 now removes the exact constant-vorticity affine fixed point from the **quiet detached** category:

\[
\boxed{
A_{detached}^{affine,const\ vortex}
\Longrightarrow
H_{pal/cap}.
}
\]

Therefore a genuinely quiet detached survivor must have nontrivial far-field cancellation/decay structure rather than simply being the solid-rotation affine anti-model.

---

## 12. Audit verdict

### ROUTED TO H

\[
\boxed{
\text{nonzero constant-vorticity affine detached profile}
\Longrightarrow
H_{pal/cap}^{prelimit}.
}
\]

### STILL OPEN

- detached profiles with localized/decaying/cancelling vorticity;
- affine harmonic strain plus localized vorticity;
- critical weak-`L3` restart inheritance;
- iterated satellite chains;
- global closure of palinstrophy/frequency H;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
