# DSD M5-144 — Odd Multipole Coefficients Are Minimal-Set Invariants

Date: 2026-08-27

Status: **P1_A RIGIDITY / EACH REALIZED INTEGER-SECTOR ODD PRESSURE RESONANCE IS ETA-INDEPENDENT AND THEREFORE INVARIANT UNDER THE W1/Tail TRANSLATION FLOW / FINITE-ORDER TERMINAL JET CONTINUITY THEN MAKES EVERY SUCH COEFFICIENT CONSTANT ON THE COMPACT MINIMAL W1 SET / ODD MULTIPOLES MAY BE NONZERO BUT CANNOT DISTINGUISH STATES OR SAME-TAIL FIBERS INSIDE ONE MINIMAL SURVIVOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Resonant coefficient

At integer Fuchsian/Taylor order `n`, the surviving pressure resonance is

\[
p_n^{res}(x)
=
\sum_m a_{n,m}
|x-x_*|^{-(2n+2)}
Y_{2n+1,m}(\theta).
\]

Equivalently in Fuchsian variables,

\[
\Pi_n^{res}(z,\eta,\theta)
=
z^n
\sum_m a_{n,m}Y_{2n+1,m}(\theta).
\]

The bounded-kernel calculation in M5-137 shows

\[
\boxed{\partial_\eta a_{n,m}=0.}
\]

Thus the resonant coefficient is independent of genealogical coordinate.

---

## 2. W1 time translation is eta translation

M5-136 identifies W1 time translation on a fixed Fuchsian slice with translation of `eta`.

Therefore

\[
\boxed{
a_{n,m}(S_hV)=a_{n,m}(V)
\qquad\forall h\in\mathbb R
}
\]

whenever the coefficient is defined from the realized finite-order terminal/Fuchsian jet.

Hence `a_{n,m}` is a flow invariant.

---

## 3. Continuity of a finite-order coefficient

The coefficient is part of a finite terminal Taylor/elliptic decomposition on any fixed punctured annulus.

The W1 compactness topology carries local smooth convergence of the solution and pressure on such fixed compact annuli, and hence convergence of any fixed finite terminal jet after the already audited terminal extension.

Projection onto the finite-dimensional spherical harmonic space

\[
\mathcal H_{2n+1}(S^2)
\]

is continuous.

Therefore the realized coefficient functional

\[
V\mapsto a_{n,m}(V)
\]

is continuous on the W1 compact class for each fixed finite order `n`.

---

## 4. Minimality forces constancy

Let `M` be the compact minimal W1 set.

A continuous flow-invariant function on a minimal set is constant.

Indeed, for any `V,W in M`, choose a sequence

\[
S_{h_j}V\to W.
\]

Then invariance and continuity give

\[
a_{n,m}(W)
=
\lim_j a_{n,m}(S_{h_j}V)
=
a_{n,m}(V).
\]

Hence

\[
\boxed{
a_{n,m}\equiv A_{n,m}
\quad\text{on }M.
}
\]

---

## 5. Consequence for same-tail fibers

If

\[
T_V=T_W
\]

for two states in the same minimal W1 set, then automatically

\[
\boxed{
a_{n,m}(V)=a_{n,m}(W)
\qquad\forall n,m.
}
\]

Thus the entire odd resonant pressure-multipole sequence is shared by every state of `M`, not merely by each individual tail fiber.

The coefficients may still be nonzero; M5-143 showed ordinary force-free finite energy does not force them to vanish.

But they cannot be variables responsible for noninjectivity inside the minimal survivor.

---

## 6. DSD four-chain audit

### Formation — GREEN

Only realized finite-order coefficients are used, not formal arbitrary harmonic additions.

### Axis — GREEN

Genealogical translation, spherical rank, and Taylor order remain distinct.

### Static aggregation — GREEN

A nonzero global multipole constant is not treated as a state-dependent fiber resource.

### Dynamics — GREEN

Minimality is applied only to an already continuous flow invariant.

### Cross-audit — GREEN

M5-143 remains valid: the constants need not vanish. M5-144 only removes them as state/fiber distinctions.

---

## 7. P1_A reduction

The candidate algebraic same-tail freedom is now much smaller.

A same-tail fiber cannot differ by choosing different coefficients in the odd harmonic pressure resonance tower.

Any remaining algebraic difference would have to arise in a nonresonant coefficient despite identical lower data, which the next recursion audit tests.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]