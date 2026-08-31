# DSD M5-404 — A nonzero affine-gradient detached limit forces enstrophy escalation and the remote route

Date: 2026-08-31

Status: **THE AFFINE FIREWALL CAN BE SHARPENED BEYOND CONSTANT-VORTICITY SOLID ROTATION / IF A DETACHED LOCAL LIMIT HAS A NONZERO CONSTANT VELOCITY GRADIENT `A`, THEN LOCAL `C1` CONVERGENCE ON `B_R` FORCES PRELIMIT GRADIENT ENERGY `int_{B_R}|grad u_n|^2 >= c|A|^2 R^3` / FOR WHOLE-SPACE DIVERGENCE-FREE FINITE-ENERGY PRELIMITS, `||grad u_n||_2^2 = ||omega_n||_2^2`, SO THE SATELLITE-FRAME NORMALIZED ENSTROPHY ESCALATES ALONG A DIAGONAL `R -> infinity` / M5-401 THEN FORCES ANOTHER REMOTE ACTIVE SATELLITE / THUS A NONZERO AFFINE HARMONIC STRAIN OR ROTATION CANNOT BE A QUIET DETACHED TERMINAL OF THE FINITE-ENERGY PRELIMIT SEQUENCE, EVEN THOUGH THE AFFINE LIMIT ITSELF IS AN EXACT LOCAL/ANCIENT ANTI-MODEL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-403 treats the nonzero constant-vorticity affine fixed point by a vorticity-capacity argument and obtains divergent prelimit palinstrophy.

A more general detached affine profile may contain a symmetric trace-free harmonic strain as well as rotation:

\[
u_\infty(x)=Ax+b,
\qquad
\operatorname{tr}A=0,
\qquad
A\ne0.
\]

The symmetric part may have zero vorticity, so the constant-vorticity capacity argument alone does not detect it.

The finite-energy prelimit sequence does detect a nonzero constant gradient through global gradient/enstrophy energy.

---

## 2. Detached affine-gradient hypothesis

After Galilean normalization assume

\[
\widetilde u_n
\to
u_\infty(x)=Ax
\]

in `C1` on every fixed compact set at one satellite time, with

\[
A\ne0,
\qquad
\operatorname{tr}A=0.
\]

The matrix `A` may contain

- an antisymmetric solid-rotation part;
- a symmetric trace-free harmonic strain part;
- or both.

No decay or finite energy is assumed for the limit itself.

---

## 3. Fixed-window gradient lower bound

Fix any finite radius

\[
R>1.
\]

By local `C1` convergence, for all sufficiently large `n=n(R)`,

\[
\sup_{B_R}
|\nabla\widetilde u_n-A|
\le
\frac14|A|.
\]

Hence throughout `B_R`,

\[
|\nabla\widetilde u_n|
\ge
\frac34|A|.
\]

Therefore

\[
\boxed{
\int_{B_R}
|\nabla\widetilde u_n|^2dx
\ge
c|A|^2R^3.
}
\]

This uses only fixed-window convergence.

---

## 4. Whole-space gradient-vorticity identity

For every smooth divergence-free whole-space prelimit with sufficient decay/finite energy,

\[
\int_{\mathbb R^3}|\nabla v|^2dx
=
\int_{\mathbb R^3}|\nabla\times v|^2dx
+
\int_{\mathbb R^3}|\nabla\cdot v|^2dx.
\]

Since

\[
\nabla\cdot\widetilde u_n=0,
\]

we have

\[
\boxed{
\|\nabla\widetilde u_n\|_2^2
=
\|\widetilde\omega_n\|_2^2.
}
\]

Thus Section 3 implies

\[
\boxed{
Z_n^{sat}
:=
\|\widetilde\omega_n\|_2^2
\ge
c|A|^2R^3.
}
\]

A locally curl-free affine strain therefore still requires global rotational/enstrophy content somewhere in the finite-energy prelimit. The harmonic strain cannot be realized as a free whole-space `H1` mode.

---

## 5. Diagonalize `R -> infinity`

Choose

\[
R_m\to\infty.
\]

For each `R_m`, choose `n_m` sufficiently large that the affine-gradient approximation holds on `B_{R_m}`.

Then

\[
\boxed{
Z_{n_m}^{sat}
\ge
c|A|^2R_m^3
\to\infty.
}
\]

Thus

\[
\boxed{
A_{detached}^{affine,\,grad\ne0}
\Longrightarrow
H_{enstrophy\,mass}^{sat}.
}
\]

---

## 6. Invoke M5-401

M5-401 proves that normalized enstrophy escalation in any centered frame with a fixed bounded inner vorticity mark forces the dyadic remote-active parameter

\[
\Lambda_R=R^2\sup_{A_R}|\omega|
\]

to become unbounded.

Therefore

\[
\boxed{
A_{detached}^{affine,\,grad\ne0}
\Longrightarrow
S_{remote}^{next}.
}
\]

The nonzero affine-gradient fixed point is thus not a quiet terminal of the finite-energy prelimit problem. Its finite-energy approximation necessarily creates another remote active scale.

---

## 7. Comparison with M5-403

For a pure solid rotation,

\[
A^T=-A,
\qquad
\omega_\infty\ne0,
\]

M5-403 gives the stronger statement

\[
\int|\nabla\widetilde\omega_n|^2
\gtrsim R,
\]

so the prelimit pays palinstrophy-capacity H.

M5-404 gives in addition

\[
\|\widetilde\omega_n\|_2^2
\gtrsim R^3.
\]

For a pure symmetric trace-free affine strain, the M5-403 vorticity-component hypothesis may fail, but M5-404 still applies because `A != 0`.

Thus together the two notes cover the full nonzero affine velocity-gradient class.

---

## 8. Why the affine limit itself remains an exact anti-model

An affine field

\[
u_\infty=Ax
\]

can solve the local/ancient Navier--Stokes equations with the appropriate quadratic pressure for suitable constant matrices `A` considered in the earlier anti-model audits.

Its own global energy may be infinite.

M5-404 does not deny its existence.

The conclusion concerns the **finite-energy whole-space approximating sequence**: approximating a nonzero constant gradient on larger and larger balls requires increasing global `H1`/vorticity mass.

This is precisely the ancestry information absent from the bare local limit.

---

## 9. Scope beyond exactly affine limits

The same calculation applies whenever a detached profile has a gradient bounded away from zero on arbitrarily large balls:

\[
\inf_{B_{R_m}}|\nabla u_\infty|
\ge c_0>0,
\qquad
R_m\to\infty.
\]

Then local `C1` convergence yields

\[
\boxed{
Z_{n_m}^{sat}
\gtrsim
c_0^2R_m^3.
}
\]

Thus any genuinely nondecaying velocity-gradient detached profile routes to the same remote/enstrophy mechanism.

---

## 10. What remains outside this lemma

A detached ancient profile may still have

- `grad u -> 0` at infinity but fail weak-`L3` for subtler reasons;
- localized vorticity plus slowly decaying velocity tails;
- oscillatory/cancelling large-scale structure;
- critical `1/r` velocity behavior;
- no uniform lower bound for `|grad u|` on large balls.

These are not excluded by M5-404.

They remain the genuine critical-restart/expanding-window inheritance problem.

---

## 11. DSD audit

### Standard inputs

- fixed-window `C1` convergence;
- whole-space divergence-free identity `||grad u||_2=||omega||_2`;
- M5-401 dyadic enstrophy-to-satellite theorem.

### Derived

\[
\boxed{
\nabla u_n\approx A\ne0
\text{ on }B_R
\Longrightarrow
\|\omega_n\|_2^2
\gtrsim
|A|^2R^3.
}
\]

### Firewall

- the affine limit need not have finite energy;
- enstrophy escalation is not itself a contradiction;
- the result routes the finite-energy prelimit to another remote satellite;
- profiles with decaying gradient remain open.

---

## 12. Updated detached frontier

The simplest noncritical affine anti-models are no longer quiet detached endpoints:

\[
\boxed{
A_{detached}^{nonzero\ affine\ gradient}
\Longrightarrow
H_{enstrophy}^{sat}
\Longrightarrow
S_{remote}^{next}.
}
\]

Together with M5-403, the remaining detached class must have genuinely decaying/cancelling large-scale derivative structure rather than a persistent affine gradient.

---

## 13. Audit verdict

### REMOVED AS QUIET DETACHED TERMINAL

\[
\boxed{\text{nonzero affine velocity-gradient fixed point}.}
\]

### ROUTING

\[
\boxed{
A_{detached}^{affine}
\Longrightarrow
S_{remote}^{next}
\quad
(\text{and in the rotational case }H_{pal/cap}).
}
\]

### STILL OPEN

- detached profiles with decaying/cancelling gradient;
- critical weak-`L3` restart inheritance;
- iterated remote chains;
- closure of local frequency/direction H;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
