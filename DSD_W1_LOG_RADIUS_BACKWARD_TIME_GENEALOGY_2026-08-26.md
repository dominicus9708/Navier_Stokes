# DSD W1 Log-Radius / Backward-Time Genealogy

Date: 2026-08-26

Status: **ALL-AGE CO-MOVING TRANSPORT CONVERTED INTO A UNIFORM RADIAL-GENEALOGY LAW / PERIODIC LOG-PERIODIC TAIL AND APERIODIC RECURRENT TAIL UNIFIED AS TWO DYNAMICAL TYPES OF THE SAME BACKWARD-ORBIT ENCODING / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The W1 endpoint was previously split dynamically into

\[
P_{DSS}^{long}
\lor
A_{min}^{aper}.
\]

The periodic branch produced a canonical log-periodic critical tail, while the aperiodic branch appeared to require a different tail construction.

The all-age co-moving estimate shows that this separation is unnecessary at the level of far-tail kinematics.

The far logarithmic radius is an asymptotic record of backward Leray time on the compact minimal set.

---

## 2. Complete trajectories on the minimal set

Let `M` be the compact minimal invariant W1 set and `S(h)` the Leray semiflow.

We already have

\[
S(h)M=M
\qquad(h\ge0).
\]

Hence every point `V_0 in M` possesses at least one complete backward trajectory inside `M`.

Indeed, for each integer `n` choose compatible preimages under `S(1)`; compactness and the finite-intersection/inverse-limit argument produce a sequence

\[
\ldots,V_{-2},V_{-1},V_0
\]

with

\[
S(1)V_{-j}=V_{-j+1}.
\]

Using the continuous flow segments between these points gives a complete trajectory

\[
V(\tau)\in M,
\qquad \tau\in\mathbb R,
\qquad V(0)=V_0,
\]

satisfying

\[
S(h)V(\tau)=V(\tau+h)
\qquad(h\ge0).
\]

Uniqueness of the backward extension is not required below.

---

## 3. Fixed-cell shell map

For a state `V` and radius `R`, define

\[
\boxed{
\mathcal F_R[V](z)
:=
R V(Rz),
\qquad 1<|z|<2.
}
\]

The all-age W1 transport theorem gives, for every W1 state `W`, every sufficiently large `R`, and every `h>=0`,

\[
\boxed{
\left\|
\mathcal F_{e^{h/2}R}[S(h)W]
-
\mathcal F_R[W]
\right\|_{L^3(A)}
\le
CR^{-1/2},
}
\]

with a constant independent of `h`.

The corresponding stronger weak estimates are

\[
\|\cdot\|_{H^{-1}}
\le CR^{-2},
\qquad
\|\cdot\|_2
\le CR^{-1}.
\]

---

## 4. Radial genealogy law

Take the complete trajectory `V(tau)` through `V_0` and set

\[
W=V(-h).
\]

Then

\[
S(h)W=V_0.
\]

Therefore

\[
\boxed{
\left\|
\mathcal F_{e^{h/2}R}[V_0]
-
\mathcal F_R[V(-h)]
\right\|_{L^3(A)}
\le
CR^{-1/2}
\qquad\forall h\ge0.
}
\]

Set

\[
\rho:=\frac h2.
\]

Then

\[
\boxed{
\left\|
\mathcal F_{Re^\rho}[V_0]
-
\mathcal F_R[V(-2\rho)]
\right\|_{L^3(A)}
\le
CR^{-1/2}
\qquad\forall\rho\ge0.
}
\]

This is the **log-radius / backward-time genealogy law**.

The error depends on the base radius `R` but is uniform over the entire outward half-line `rho>=0`.

Hence, after taking `R->infinity`, one unit of logarithmic radius corresponds asymptotically to two units of backward Leray time.

---

## 5. DSD interpretation

The current far shell at radius

\[
Re^\rho
\]

is not an independent old shell.

It is, to vanishing critical error, the scale-normalized shell state of an ancestor

\[
V(-2\rho)
\]

on the same minimal dynamical set.

Thus

\[
\boxed{
\text{outward log-radius}
\quad\leftrightarrow\quad
\text{backward structural age}.
}
\]

In DSD language the W1 critical tail is a **spatialized genealogy of the recurrent dynamics**.

This is stronger than merely saying that mass is transported by similarity dilation.

---

## 6. Periodic branch is recovered automatically

Suppose `V` is periodic with period `S`:

\[
V(\tau-S)=V(\tau).
\]

Increase `rho` by `S/2`.  Then

\[
V[-2(\rho+S/2)]
=
V(-2\rho-S)
=
V(-2\rho).
\]

Therefore

\[
\mathcal F_{Re^{\rho+S/2}}[V_0]
-
\mathcal F_{Re^\rho}[V_0]
\to0
\]

in the critical shell topology as the base radius tends to infinity.

Thus the previously derived logarithmic period

\[
\boxed{L=S/2}
\]

and DSS factor

\[
\boxed{\lambda=e^{S/2}}
\]

follow directly from the genealogy law.

The periodic canonical tail is therefore the periodic special case of one more general construction.

---

## 7. Aperiodic branch

If the complete W1 trajectory is minimal and aperiodic, then the map

\[
\rho\mapsto V(-2\rho)
\]

is a recurrent aperiodic orbit in the compact set `M`.

The genealogy law therefore implies that the current far tail is asymptotically aperiodic and recurrent in logarithmic radius:

\[
\boxed{
\rho\mapsto
\mathcal F_{Re^\rho}[V_0]
\quad\text{shadows}\quad
\rho\mapsto V(-2\rho)
}
\]

with an error `O(R^-1/2)` uniform for all `rho>=0`.

Thus the aperiodic branch does not require a separate passive-tail evolution law.

Its tail is the radial image of the aperiodic minimal core dynamics.

This does **not** make the aperiodic branch contradictory.

---

## 8. Observable correspondence

Let `G` be a Lipschitz functional on the fixed-annulus L3 shell state.

Then

\[
\left|
G(\mathcal F_{Re^\rho}[V_0])
-
G(\mathcal F_R[V(-2\rho)])
\right|
\le
C_G R^{-1/2}
\]

uniformly in `rho>=0`.

Averaging over `0<=rho<=L` gives

\[
\boxed{
\frac1L\int_0^L
G(\mathcal F_{Re^\rho}[V_0])d\rho
=
\frac1{2L}\int_0^{2L}
G(\mathcal F_R[V(-t)])dt
+O(R^{-1/2}).
}
\]

Thus log-radial statistics of the tail equal backward-time statistics of the minimal orbit in the large-base-radius limit.

This is an asymptotic radial/time ergodic correspondence.

---

## 9. Critical cubic mass

For

\[
G(F)=\int_A|F|^3dz,
\]

uniform fixed-annulus H1 bounds make `G` locally Lipschitz on the bounded shell class. Hence

\[
\boxed{
\frac1L\int_0^L
\Psi_{Re^\rho}(V_0)d\rho
=
\frac1{2L}\int_0^{2L}
\Psi_R(V(-t))dt
+O(R^{-1/2}).
}
\]

Positive critical radial density is therefore exactly a positive backward-time mean shell charge on the complete W1 orbit.

The center-mode memory can be read either as a scale current or as a time-history density.

---

## 10. Physical memory horizon

At an actual prelimit time `s_n`, normalized radius `R` corresponds to physical radius

\[
r=e^{-s_n/2}R.
\]

A genealogical age `h` appears at normalized radius

\[
Re^{h/2}
\]

and hence at physical radius

\[
r(h)=e^{-s_n/2}Re^{h/2}.
\]

The finite-energy scale-infinity capacity allows the W1-like tail, at the level of scaling, out to

\[
R_{max}\asymp e^{s_n/2}.
\]

Starting from fixed large base `R`, the corresponding maximal encoded age is

\[
\boxed{
h_{max}
\sim
2\log\frac{R_{max}}R
=
s_n-O(1).
}
\]

Thus the expanding normalized tail has exactly enough radial extent to encode an amount of backward Leray history proportional to the elapsed Leray time.

This is another exact scaling match rather than a contradiction.

---

## 11. Unified W1 tail picture

At the level of far-tail kinematics,

\[
\boxed{
W1
\Longrightarrow
\text{one radial-history tail cocycle over the minimal set }M.
}
\]

Then

\[
\boxed{
P_{DSS}^{long}
=
\text{periodic radial genealogy},
}
\]

while

\[
\boxed{
A_{min}^{aper}
=
\text{aperiodic recurrent radial genealogy}.
}
\]

The periodic/aperiodic split remains relevant to dynamical rigidity, but it is no longer a split into two unrelated tail mechanisms.

---

## 12. New common frontier

Both dynamical types now face the same realization question:

\[
\boxed{
\text{Can a finite-energy unforced Navier--Stokes prelimit realize, on expanding similarity windows,}
\newline
\text{a radial genealogy that asymptotically encodes an entire nontrivial compact minimal Leray orbit?}
}
\]

This is more precise than a generic DSS/non-DSS Liouville problem.

It combines:

- recurrent core dynamics;
- critical `1/R` tail memory;
- scale-infinity energy capacity;
- and the expanding-window/prelimit interface.

No theorem excluding such a realization is yet proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
