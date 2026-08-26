# DSD W1 Complete Critical Formation-Cycle Block

Date: 2026-08-26

Status: **PRESSURE/AMPLITUDE AND VORTICITY/STRETCHING CERTIFICATES ASSEMBLED INTO UNIFORMLY BOUNDED LERAY-TIME CYCLE BLOCKS / SCALE-INVARIANT GLOBAL RATIO SHOWS NET AMPLITUDE AND VORTICITY FORMATION MUST BALANCE OVER LONG CYCLE TRAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Two recurrent event classes

The current W1 minimal class contains two already-established open recurrent event types.

### Amplitude/pressure formation event `A`

On a fixed finite parent region one has a quantitatively nontrivial pressure-amplitude/Hodge-work event, together with an intermediate-scale amplitude oscillation and

\[
D_{3,amp}\ge d_*>0.
\]

By the amplitude--vorticity--direction co-localization lemma, the same intermediate-scale witness also carries at least one fixed direction/vorticity cost.

### Vorticity/stretching event `V`

The invariant enstrophy and maximum-vorticity ledgers force recurrent positive vorticity stretching, including finite-core supercritical strain events.

Both event classes are open in the local smooth topology on the compact minimal set `M` after slightly lowering their thresholds.

---

## 2. Minimality gives bounded return gaps

For every nonempty open set in a compact minimal flow, return times are syndetic.

Hence there exist finite constants

\[
H_A<\infty,
\qquad
H_V<\infty
\]

such that every orbit segment of length `H_A` meets an amplitude event and every orbit segment of length `H_V` meets a vorticity event.

Set

\[
\boxed{
H_{cyc}:=H_A+H_V.
}
\]

Starting from any amplitude event, a vorticity event occurs within the next `H_V`; starting from any vorticity event, an amplitude event occurs within the next `H_A`.

Therefore the orbit can be partitioned, up to uniformly bounded overlap/end effects, into recurrent **complete formation-cycle blocks** of Leray length at most `H_cyc` containing both mechanisms.

---

## 3. Fixed action inside each complete block

Local smooth compactness allows the threshold events to be thickened in time. Therefore there are fixed positive durations and action floors such that every complete cycle block `J_k` satisfies

\[
\boxed{
\int_{J_k}\mathcal A_{amp}(s)ds\ge a_{amp}>0,
}
\]

and

\[
\boxed{
\int_{J_k}\mathcal A_{vor}(s)ds\ge a_{vor}>0,
}
\]

for suitable nonnegative normalized critical observables. Examples include the already established amplitude-flow/BMO/D3 certificate and the positive stretching/middle-strain certificate.

Thus

\[
\boxed{
\int_{J_k}
\bigl(\mathcal A_{amp}+\mathcal A_{vor}\bigr)ds
\ge a_{cyc}>0.
}
\]

This is a `beta=0` normalized action statement: it is measured in Leray time, not in the subcritical physical-energy clock.

---

## 4. Scale-invariant global formation ratio

Define

\[
X_4(s):=\|U(s)\|_4^4,
\qquad
Z(s):=\|\Omega(s)\|_2^2,
\]

and

\[
\boxed{
\Theta_4(s)
:=
\log\frac{Z(s)}{X_4(s)}.
}
\]

Both `Z` and `X4` carry the same Navier--Stokes scaling weight, so `Theta4` is scale invariant.

The exact `p=4` and enstrophy balances give

\[
\boxed{
\Theta_4'(s)
=\mathfrak g_\Omega(s)-\mathfrak g_4(s),
}
\]

where

\[
\mathfrak g_\Omega
:=
\frac{2\mathcal S}{Z}
-
\frac{2\nu P_\Omega}{Z},
\]

and

\[
\mathfrak g_4
:=
\frac{4\Pi_4}{X_4}
-
\frac{4\nu D_4}{X_4}.
\]

The Leray linear damping cancels identically.

Since `M` is compact and nontrivial, `Theta4` is bounded on `M`.

---

## 5. Long cycle trains must have balanced net formation

For any orbit and any `S>0`,

\[
\int_0^S
(\mathfrak g_\Omega-\mathfrak g_4)ds
=
\Theta_4(S)-\Theta_4(0).
\]

Thus

\[
\boxed{
\left|
\int_0^S
(\mathfrak g_\Omega-\mathfrak g_4)ds
\right|
\le 2\|\Theta_4\|_{L^\infty(M)}.
}
\]

Dividing by `S` gives

\[
\boxed{
\frac1S\int_0^S
(\mathfrak g_\Omega-\mathfrak g_4)ds
\to0.
}
\]

Therefore a long train of complete formation cycles cannot have a persistent net bias toward vorticity formation or velocity-amplitude formation.

The two channels must compensate in the scale-invariant clock.

---

## 6. Existence of nearly balanced cycle blocks

Partition a long orbit segment into complete blocks `J_k` of uniformly bounded length. Define the block imbalance

\[
\Delta_k
:=
\int_{J_k}
(\mathfrak g_\Omega-\mathfrak g_4)ds.
\]

The cumulative sum over the first `N` blocks remains bounded up to uniformly bounded partition errors because it telescopes through `Theta4`.

Hence a scenario in which all sufficiently late blocks obey either

\[
\Delta_k\ge\delta>0
\]

or

\[
\Delta_k\le-\delta<0
\]

is impossible.

Consequently there are infinitely many late complete cycle blocks with arbitrarily small net imbalance after passing to suitable cycle groupings/subsequences:

\[
\boxed{
|\Delta_k|\to0
\quad\text{along a recurrent cycle subsequence.}
}
\]

This is a block-level version of pressure--stretch locking. It does not require the two active regions to coincide pointwise or instantaneously.

---

## 7. DSD interpretation

The old logical split

\[
\text{pressure core overlaps vorticity core}
\quad\lor\quad
\text{they remain separated}
\]

is no longer terminal.

If they overlap, the local relative-vorticity ratio supplies the locking condition.

If they do not overlap, minimal recurrence packs them into one uniformly bounded complete cycle block, and the global scale-invariant ratio forces their **net formation gains to balance** over recurrent cycle trains.

Thus both cases are represented by one object:

\[
\boxed{
\text{complete critical formation cycle}
+
\text{asymptotically zero scale-invariant imbalance}.
}
\]

---

## 8. Remaining theorem

This note does not yet prove that a balanced cycle cannot repeat.

The final endpoint target can now be sharpened to:

\[
\boxed{
\text{prove that a complete formation cycle with fixed critical action cannot recur at positive Leray-time density while its scale-invariant imbalance remains bounded/telescoping.}
}
\]

A successful theorem must exploit more than ordinary kinetic energy, because every such subcritical physical event cost remains summable.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
