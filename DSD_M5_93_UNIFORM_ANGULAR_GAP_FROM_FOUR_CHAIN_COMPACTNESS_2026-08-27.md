# DSD M5-93 — Uniform Angular Gap from Four-Chain Compactness

Date: 2026-08-27

Status: **COMPACTNESS PROMOTION OF M5-92 / ON THE ROBUST RETURNED UPSTROKE CLASS, THE ANGULAR RECONNECTION CHANNEL CANNOT COLLAPSE TO ZERO / UNDER THE FIXED-BAND LOCAL SMOOTH COMPACTNESS AND POSITIVE-CROSSING INPUTS THERE EXISTS A UNIFORM `G_* > 0` / THIS DOES NOT YET EXCLUDE THE GENERAL POSITIVE-G MINIMAL-PAYER ENDPOINT / GLOBAL REGULARITY UNPROVED.**

## 1. Returned pump class

Use the M5-57 robust returned upstroke neighborhood in the W1 minimal recurrent set.

On this class there are fixed normalized constants

\[
X_w\ge c_1>0
\]

on intervals of fixed positive Leray-time width.

The active amplitude weight `w` is fixed and supported in a positive band whose spatial support lies in one fixed normalized core cell.

Local analytic W1 compactness and the M5-51 far-pressure control make the corresponding localized velocity, pressure, and finite-band functionals precompact/bounded on this returned class.

---

## 2. Positive crossing cannot disappear

The exact averaged ledger is

\[
J_w=\nu D_w+X_w.
\]

Hence

\[
J_w\ge c_1.
\]

The componentwise pressure Cauchy inequality gives

\[
J_w^2
\le
S_{comp,w}T_w.
\]

On the compact returned pump class,

\[
S_{comp,w}\le S_*<\infty.
\]

Therefore

\[
\boxed{
T_w
\ge
T_*:=\frac{c_1^2}{S_*}>0.
}
\]

Thus any limiting returned upstroke retains genuine normal crossing.

---

## 3. Contradiction sequence for G

Assume no uniform angular gap exists.

Then there is a sequence of returned upstroke states `U_n` with

\[
G_w[U_n]\to0.
\]

By W1 local smooth compactness on the fixed active core, after taking a subsequence,

\[
U_n\to U_*
\]

strongly in sufficiently high local `C^m` topology.

The finite-band volume functional

\[
G_w
=
\int
\frac{w(a)}a
|U\times\nabla a|^2dy
\]

is continuous under this convergence.

Hence

\[
\boxed{G_w[U_*]=0.}
\]

At the same time the crossing floor passes to the limit:

\[
\boxed{T_w[U_*]\ge T_*>0.}
\]

The positive amplitude band remains spatially bounded in the normalized cell.

Therefore the limiting state is exactly the nontrivial bounded smooth zero-angular-gap crossing state excluded by M5-92.

Contradiction.

---

## 4. Uniform gap

Consequently there exists

\[
\boxed{G_*>0}
\]

such that every state in a sufficiently small compact returned upstroke neighborhood satisfies

\[
\boxed{G_w\ge G_*.}
\]

This is a state-space compactness result, not a time-integrated numerical budget.

---

# 5. DSD four-chain interpretation

## Formation chain

The positive amplitude pump remains a bounded formed object under the W1 return topology.

The forbidden zero-gap limit cannot escape by forming a puncture or external source.

## Axial chain

`G_w` is the tangential/oblique axial channel needed to avoid the exact-normal curvature obstruction.

M5-92 proves that this channel cannot be identically absent in a nontrivial returned pump.

## Static aggregation chain

`T_w` retains a uniform positive floor because positive pressure work and bounded pressure variance prevent the crossing square from disappearing.

Thus the limiting state cannot become the trivial no-crossing state while `G` tends to zero.

## Dynamical chain

Minimal/syndetic recurrence repeatedly returns to the same compact upstroke neighborhood.

Therefore the statewise angular gap is reproduced on every sufficiently accurate return.

The audit is algorithmic:

\[
\boxed{
\text{formed compact return class}
+\text{positive crossing}
+\text{zero-gap state rejection}
\Rightarrow
\text{uniform angular channel}.}
\]

---

## 6. Consequence for the pressure payer

M5-69 gives

\[
S_{comp,w}
\ge
4\nu^2(A_w+G_w)+4\nu X_w+H_w.
\]

Hence on the returned upstroke class,

\[
\boxed{
S_{comp,w}
\ge
4\nu^2A_w
+4\nu^2G_*
+4\nu c_1.
}
\]

This is a stronger **statewise pressure requirement** on every return.

It is not yet an accumulating finite-budget contradiction, because M5-60/M5-61 already audited that repeated critical costs need an independent finite budget or a direct statewise incompatibility.

---

## 7. What remains

The general exact M5-70 endpoint may have

\[
G_w\ge G_*>0
\]

and still satisfy

\[
X_w=\nu(T_w-A_w-G_w)>0.
\]

Therefore the next DSD parallel audit must stop treating `G` merely as a defect and instead treat it as an **active reconnection channel**.

The target becomes:

\[
\boxed{
\text{Can a bounded smooth zero-net-flux component maintain }
T>A+G
\text{ when }G\text{ is the very channel that reconnects opposite crossing signs?}
}
\]

This is the next structural problem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]