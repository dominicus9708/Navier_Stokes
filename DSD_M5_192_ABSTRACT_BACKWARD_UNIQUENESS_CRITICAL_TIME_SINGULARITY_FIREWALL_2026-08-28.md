# DSD M5-192 — Abstract Backward-Uniqueness Critical-Time-Singularity Firewall

Date: 2026-08-28

Status: **P1_B ABSTRACT-THEOREM AUDIT / CLASSICAL LIONS--MALGRANGE / AGMON--NIRENBERG BACKWARD UNIQUENESS COVERS UNIFORMLY PARABOLIC EVOLUTIONS WITH SUFFICIENT COEFFICIENT REGULARITY AND A CONTROLLED PRINCIPAL FORM, BUT THE W1 COMMON-TAIL LINEARIZATION HAS AN EXACT TERMINAL-CRITICAL `1/tau` SYMMETRIC CHANNEL / A SCALAR MODEL ALREADY SUPPORTS NONZERO TERMINAL-ZERO SOLUTIONS AT THAT ORDER / THEREFORE NO GENERIC ABSTRACT PARABOLIC THEOREM CAN CLOSE THE LARGE-AMPLITUDE W1 GATE WITHOUT USING EXTRA NAVIER--STOKES STRUCTURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Classical backward-uniqueness framework

Classical Lions--Malgrange / Agmon--Nirenberg theory proves backward uniqueness for broad uniformly parabolic evolution equations under hypotheses such as:

- a well-controlled elliptic principal part;
- sufficient time regularity of the principal coefficients;
- a solution class with finite Hilbert-space energy/regularity;
- lower-order terms that remain controlled relative to the principal evolution.

This framework explains why many bounded-coefficient heat/Oseen problems enjoy backward uniqueness.

It does **not** say that every time-singular scale-critical lower-order form is backward injective.

---

## 2. W1 terminal-critical scale

For the same-tail physical realization set

\[
\tau:=T_*-t.
\]

The common-tail strain has the scale

\[
|S_{B_T}(x,\tau)|\lesssim (|x-x_*|^2+\tau)^{-1}.
\]

At the terminal center,

\[
\boxed{|S_{B_T}(x_*,\tau)|\sim \tau^{-1}.}
\]

Hence the symmetric part of the relative generator is exactly at the nonintegrable temporal critical scale.

---

## 3. Scalar terminal-critical countermodel

The ODE

\[
\partial_\tau f-\frac c\tau f=0,
\qquad c>0,
\]

has

\[
\boxed{f(\tau)=C\tau^c}.
\]

Thus

\[
f(0)=0
\]

but

\[
f\not\equiv0.
\]

The coefficient has precisely the critical time scale `tau^-1`.

Therefore the terminal condition alone cannot distinguish the zero branch from a nonzero algebraically vanishing branch for a generic signed critical potential.

---

## 4. Why finite energy does not repair the generic countermodel

Finite `L2` energy controls the spatial size of the solution but does not remove a purely temporal critical factor.

A separable Hilbert-space model

\[
W(\tau)=\tau^c w_0,
\qquad w_0\in L^2,
\]

satisfies

\[
\partial_\tau W-\frac c\tau W=0
\]

and still has

\[
W(0)=0
\]

in `L2`.

Thus

\[
\boxed{
W\in L^2
+\text{terminal zero}
+\text{critical }1/\tau\text{ coefficient}
\not\Rightarrow
W\equiv0
}
\]

without further operator structure.

---

## 5. Why the classical theorem cannot simply be inserted

For each fixed `tau>0` the W1 physical coefficients are smooth and bounded.

However their bounds deteriorate at the terminal endpoint as

\[
\|U(\tau)\|_\infty\sim\tau^{-1/2},
\qquad
\|\nabla U(\tau)\|_\infty\sim\tau^{-1}.
\]

The symmetric form therefore has no uniform integrable bound up to `tau=0`.

Moreover M5-191 shows that the pointwise common-tail strain has no geometry-only sign.

Hence the standard chain

\[
\text{finite-energy parabolic evolution}
\to
\text{Lions--Malgrange}
\to
\text{terminal injectivity}
\]

is not justified for the present endpoint.

---

## 6. Connection to the normalized W1 dynamics

The critical temporal singularity is not accidental.

Under Leray similarity time

\[
s=-\log\tau,
\]

a factor `tau^c` becomes

\[
e^{-cs}.
\]

Thus a terminal-zero critical mode is exactly a normalized exponentially decaying direction.

The W1 minimal recurrent structure severely constrains such directions, but **that recurrence information must be used explicitly**; it cannot be replaced by a generic parabolic theorem.

This observation reconnects the physical backward problem to the normalized dynamical system without identifying the two proofs.

---

## 7. Consequence for the first large gate

The first large gate cannot be closed by one of the following alone:

- finite energy;
- Hardy boundedness;
- coefficient smoothness for every `tau>0`;
- a generic Hilbert-space backward-uniqueness theorem.

A successful proof must use at least one genuinely NSE/W1-specific input such as:

1. compact minimal recurrence in normalized time;
2. the common canonical-tail factor structure;
3. an adapted operator symmetrizer that excludes the dangerous critical mode;
4. a critical Stokes Carleman inequality whose positivity relies on divergence-free/pressure structure rather than order alone.

---

## 8. DSD four-chain audit

### Formation — GREEN

The countermodel is a legitimate abstract terminal-critical evolution and is used only to test theorem generality.

### Axis — GREEN

Physical terminal time and normalized Leray time are related but not identified.

### Static aggregation — GREEN

Finite energy is not mistaken for temporal coercivity.

### Dynamics — GREEN FIREWALL

Generic critical backward uniqueness is excluded; actual W1 backward injectivity remains OPEN.

### Cross-audit — GREEN

This corrects the overstrong wording in the original M5-185 and is consistent with M5-190/M5-191.

---

## 9. Next route

The next calculation should exploit the last line of Section 6:

\[
\boxed{
\text{a nonzero terminal-critical mode corresponds to a decaying normalized direction.}
}
\]

On a compact **minimal recurrent** W1 pair system, determine whether a same-tail flat difference can possess such a one-sided exponentially decaying direction without forcing the entire invariant pair measure onto the diagonal.

This uses actual W1 dynamics and avoids a false generic backward-uniqueness theorem.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
