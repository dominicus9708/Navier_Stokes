# DSD M5-192 — Abstract Backward-Uniqueness Critical-Time-Singularity Firewall — CORRECTED

Date: 2026-08-28

Status: **P1_B ABSTRACT-THEOREM AUDIT / CLASSICAL BACKWARD-UNIQUENESS THEORY DOES NOT AUTOMATICALLY COVER THE W1 TERMINAL-CRITICAL `1/tau` SYMMETRIC CHANNEL / A SCALAR MODEL SUPPORTS NONZERO TERMINAL-ZERO SOLUTIONS AT THAT ORDER / HOWEVER PHYSICAL TERMINAL L2 COLLAPSE MUST NOT BE IDENTIFIED WITH DECAY OF THE NORMALIZED W1 DIFFERENCE, BECAUSE LERAY SCALING ALONE PRODUCES THE COLLAPSE / GENERIC ABSTRACT PARABOLIC THEORY THEREFORE CANNOT CLOSE THE GATE, AND MINIMAL RECURRENCE CANNOT BE INVOKED FROM PHYSICAL TERMINAL ZERO WITHOUT AN ADDITIONAL NORMALIZED BRIDGE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Classical backward-uniqueness framework

Classical Lions--Malgrange / Agmon--Nirenberg theory proves backward uniqueness for broad uniformly parabolic evolutions with a controlled principal form, sufficient coefficient regularity, and an admissible finite-energy solution class.

It does not imply injectivity for every signed time-singular critical lower-order form.

---

## 2. W1 terminal-critical scale

Set

\[
\tau:=T_*-t.
\]

The common-tail strain satisfies

\[
|S_{B_T}(x,\tau)|\lesssim(|x-x_*|^2+\tau)^{-1},
\]

so at the center

\[
\boxed{|S_{B_T}(x_*,\tau)|\sim\tau^{-1}.}
\]

This is the nonintegrable terminal-critical temporal scale.

---

## 3. Scalar terminal-critical countermodel

The ODE

\[
\partial_\tau f-\frac c\tau f=0,
\qquad c>0,
\]

has

\[
\boxed{f(\tau)=C\tau^c},
\]

with

\[
f(0)=0,
\qquad
f\not\equiv0.
\]

Thus a generic signed `1/tau` potential can support a nontrivial terminal-zero branch.

---

## 4. Finite energy does not repair the generic model

For `w_0 in L2`,

\[
W(\tau)=\tau^cw_0
\]

is a finite-energy nonzero terminal-zero solution of

\[
\partial_\tau W-\frac c\tau W=0.
\]

Therefore

\[
\boxed{
L^2+\text{terminal zero}+\text{generic critical }1/\tau\text{ coefficient}
\not\Rightarrow
\text{backward uniqueness}.
}
\]

---

## 5. Why a classical theorem cannot simply be inserted

For each fixed `tau>0` the physical W1 coefficients are smooth and bounded, but

\[
\|U(\tau)\|_\infty\sim\tau^{-1/2},
\qquad
\|\nabla U(\tau)\|_\infty\sim\tau^{-1}
\]

as `tau downarrow0`.

The common-tail strain has no geometry-only sign by M5-191.

Hence a standard uniformly controlled parabolic backward-uniqueness theorem does not automatically cover the terminal endpoint.

---

## 6. Critical correction: physical collapse is not normalized decay

The scalar ODE intuition must **not** be transferred directly to the normalized W1 pair.

For the physical same-tail difference `w` and normalized Leray difference `Z`, scaling gives

\[
\boxed{
\|w(t)\|_2^2
=
\tau^{1/2}\|Z(s)\|_2^2,
\qquad s=-\log\tau.
}
\]

Therefore even if

\[
\|Z(s)\|_2\sim1
\]

along a compact recurrent normalized orbit, one still has

\[
\|w(t)\|_2\to0
\]

as `t up T_*`.

This is exactly the M5-117/M5-128 firewall:

\[
\boxed{
\text{physical terminal }L^2\text{ collapse}
\not\Rightarrow
\text{normalized terminal equality or decay}.
}
\]

Consequently a physical terminal-critical mode cannot be labeled a normalized exponentially decaying direction without removing the similarity prefactor and spatial dilation explicitly.

The former Section-6 statement asserting such a direct correspondence is withdrawn.

---

## 7. Consequence for minimal recurrence

Minimal recurrence cannot be invoked merely from

\[
w(T_*)=0
\]

in physical `L2`.

A legitimate recurrence contradiction would require a new normalized observable `J[Z]` such that:

1. `J` removes the universal similarity collapse;
2. `J` is continuous on the compact W1 pair system;
3. the critical physical dynamics forces `J(S_sV,S_sW) -> 0` for a nontrivial same-tail pair.

No such observable has yet been proved.

Thus

\[
\boxed{
\text{physical backward criticality}
\not\Rightarrow
\text{minimal-pair contraction}
}
\]

is now a permanent RED arrow.

---

## 8. What remains valid

The scalar countermodel still proves the intended negative result:

- finite energy alone is insufficient;
- Hardy boundedness alone is insufficient;
- critical differential order alone is insufficient;
- generic abstract backward uniqueness cannot be inserted without verifying endpoint assumptions.

The actual W1 problem still may possess additional structure, but it must be demonstrated explicitly.

---

## 9. Legitimate next routes

After M5-190/M5-191 and the present correction, the noncircular routes are:

1. an adapted symmetrizer or log-convexity observable for the **full common canonical-tail operator**;
2. a critical Oseen--Stokes Carleman theorem using genuine divergence-free/pressure structure;
3. a normalized pair observable removing the similarity prefactor and proving actual contraction, not physical `L2` collapse;
4. an external theorem whose hypotheses explicitly allow the terminal Type-I critical coefficient class.

---

## 10. DSD audit

### Formation — GREEN

The abstract countermodel is used only as a theorem-generality test.

### Axis — CORRECTED

Physical terminal time and normalized Leray dynamics are no longer conflated.

### Static aggregation — GREEN

Finite energy is not mistaken for temporal coercivity.

### Dynamics — GREEN FIREWALL / W1 INJECTIVITY OPEN

Generic critical backward uniqueness is excluded; actual W1 backward injectivity remains open.

### Cross-audit — GREEN

The correction restores consistency with M5-117/M5-128.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
