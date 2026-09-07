# DSD M17-332 — Same-genealogy resonant mean splits into L1 phase locking or two-sided three-halves excursion mass

Date: 2026-09-08  
Canonical ID: **M17-332**

Status: **ACTIVE SAME-LABEL TEMPORAL REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope firewall

M17-331 concerns the stationary **ensemble pure-flux distribution** in one fixed similarity hull.

M17-134 instead tracks one material genealogy over long inter-stage intervals and, under its endpoint compactness hypotheses, gives

\[
\left\langle\kappa\right\rangle_T
=
\frac32+\varepsilon_T,
\qquad
\varepsilon_T\to0.
\]

These are different averaging objects and are not identified here.

Define on that same material label

\[
\boxed{
q(\theta):=\kappa(\theta)-\frac32.
}
\]

Then

\[
\boxed{
\left|\frac1T\int_{I_T}q(\theta)d\theta\right|
\le\epsilon_T,
\qquad
\epsilon_T\to0.
}
\]

Assume the same-label trajectory stays in a compact `kappa` corridor so that

\[
|q|\le Q<\infty.
\]

## 2. Positive and negative resonant deviations

Set

\[
q_+:=\max(q,0),
\qquad
q_-:=\max(-q,0).
\]

Define the normalized positive/negative deviation masses

\[
P_T:=\frac1T\int_{I_T}q_+d\theta,
\qquad
N_T:=\frac1T\int_{I_T}q_-d\theta.
\]

Also define total resonant variation

\[
\boxed{
V_T:=\frac1T\int_{I_T}|q|d\theta=P_T+N_T.
}
\]

Since

\[
\frac1T\int q=P_T-N_T,
\]

we have exactly

\[
P_T=rac12\left(V_T+\frac1T\int q\right),
\]

\[
N_T=rac12\left(V_T-\frac1T\int q\right).
\]

Therefore

\[
\boxed{
P_T,N_T\ge\frac12(V_T-\epsilon_T).
}
\]

## 3. Exact dichotomy

There are two possibilities.

### Branch A — L1 resonant phase locking

If

\[
V_T\to0,
\]

then

\[
\boxed{
\frac1T\int_{I_T}
\left|\kappa-\frac32\right|d\theta
\to0.
}
\]

Thus the same material genealogy is asymptotically locked to the resonant coefficient level in time-averaged `L1`.

This is stronger than merely saying the signed mean tends to `3/2`.

### Branch B — nontrivial resonant variation

Otherwise there exists a subsequence and `v_*>0` such that

\[
V_T\ge v_*.
\]

For large members of the subsequence with `epsilon_T<=v_*/2`, we obtain

\[
\boxed{
P_T,N_T\ge\frac{v_*}{4}.
}
\]

Hence the same label accumulates order-`T` positive and negative deviation from `3/2`:

\[
\boxed{
\int q_+d\theta\ge\frac{v_*}{4}T,
\qquad
\int q_-d\theta\ge\frac{v_*}{4}T.
}
\]

## 4. Quantitative two-sided excursion occupancy

Choose any

\[
0<\delta<\frac{v_*}{4}.
\]

Because `q_+<=delta` on `{0<q<delta}` and `q_+<=Q` everywhere,

\[
P_T
\le
\delta
+
Q\frac{|\{q\ge\delta\}\cap I_T|}{T}.
\]

Thus

\[
\boxed{
\frac{|\{\kappa\ge3/2+\delta\}\cap I_T|}{T}
\ge
\frac{v_*/4-\delta}{Q}.
}
\]

Likewise

\[
\boxed{
\frac{|\{\kappa\le3/2-\delta\}\cap I_T|}{T}
\ge
\frac{v_*/4-\delta}{Q}.
}
\]

So failure of `L1` phase locking forces positive-density time occupancy on both sides of the resonant level along the **same material genealogy**.

## 5. Crossing-count firewall

Two-sided positive-density occupancy does not by itself imply a positive asymptotic crossing frequency.

A continuous scalar path can spend one very long block below the threshold and another very long block above it, producing only a small number of actual crossings.

Therefore the implication

\[
\boxed{
\text{two-sided occupation}
\Rightarrow
\text{linear crossing count}
}
\]

is rejected without an additional recurrence/mixing/refresh theorem on the same label.

## 6. Relation to M17-326

M17-326's scale-critical currency counts directed crossings of the homogeneous level `kappa=0`.

The current module concerns deviations around the representation-dependent level `kappa=3/2` in one fixed similarity generation.

M17-330 forbids identifying their cross-generation currencies.

## 7. DSD-theory role

The useful DSD heuristic is to separate:

- a state mean;
- magnitude of deviation from that state;
- actual transitions between the two sides.

The standard calculation shows these are genuinely different quantities.

No DSD axiom is used as a PDE assumption.

## 8. Updated same-genealogy frontier

M17-134 now sharpens to

\[
\boxed{
H_{resonant\ mean}
\Longrightarrow
H_{L^1\ phase\ locking\ at\ 3/2}
\lor
H_{two\text{-}sided\ resonant\ excursion\ mass}.
}
\]

The excursion branch still requires a same-label refresh/crossing-frequency theorem before it can produce a repetitive payment ledger.

The phase-locking branch must instead be tested against the exact CE-H constitutive equation and the global negative-`kappa` compensator architecture.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
