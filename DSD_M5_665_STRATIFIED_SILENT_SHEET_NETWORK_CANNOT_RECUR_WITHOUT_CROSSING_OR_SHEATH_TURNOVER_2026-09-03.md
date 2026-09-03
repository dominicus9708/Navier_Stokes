# DSD M5-665 — A stratified silent sheet network cannot recur in a bounded core without crossing or sheath turnover

Date: 2026-09-03

Status: **INTERNAL STRATIFIED-NETWORK CLOSURE / M5-663 GIVES FINITE ANALYTIC VANISHING ORDER, AND M5-664 SHOWS THAT EVERY REGULAR CODIMENSION-ONE CRITICAL FACE WITH NO HIGHER-JET CROSSING IS A MATERIAL NORMAL BARRIER / LOWER-DIMENSIONAL ANALYTIC JUNCTION STRATA CANNOT BY THEMSELVES SEPARATE THREE-DIMENSIONAL SHEET CELLS; IF ALL REGULAR FACES REMAIN MATERIAL, THE SMOOTH MATERIAL FLOW MAP PRESERVES THEIR INCIDENCE/TOPOLOGY AND EACH CELL BOUNDED ONLY BY SUCH FACES IS A MATERIAL REGION / ANY CELL CONTAINING A FIXED COHERENT CARRIER BALL THEN HAS POSITIVE VOLUME AND GROWS EXACTLY AS `exp(3 theta/2)`, CONTRADICTING BOUNDED RECURRENT CORE STORAGE / IF A CELL ALSO MEETS THE AMPLITUDE BOUNDARY, M5-662 FORCES POSITIVE AMPLITUDE-THRESHOLD MATERIAL TURNOVER / THEREFORE A RECURRENT HIGH-AMPLITUDE MULTI-SHEET NETWORK MUST PAY EITHER FORCE/HIGHER-JET CROSSING OR SHEATH TURNOVER; THERE IS NO SEPARATE TURNOVER-FREE SILENT NETWORK BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Analytic stratified critical network

Inside the retained high-amplitude region

\[
\rho>a_0,
\]

`kappa` is analytic.

Its critical set

\[
\mathcal K:=\{\nabla\kappa=0\}
\]

admits the standard local analytic stratification into smooth strata.

The strata relevant to separating open three-dimensional relabeling regions are codimension-one faces.

Lower-dimensional curves/points can be junctions, endpoints in a restricted region, or topology-change loci, but they do not by themselves separate a three-dimensional neighborhood without incident codimension-one faces.

---

## 2. Every finite-order silent regular face is material-normal

M5-663 excludes infinite-order active flatness and gives a finite first normal order on every regular face after stratification.

M5-664 then gives the exact alternative

\[
\boxed{
\text{regular critical face}
\Longrightarrow
C_{crit}^{higher-jet}
\lor
K_{material\ barrier}.
}
\]

On the silent branch,

\[
\boxed{(B-V_\Sigma)\cdot n=0.}
\]

Thus every regular silent face is transported with material normal velocity.

---

## 3. Material flow preserves a barrier network unless a face ceases to be material

For smooth `B`, the Lagrangian flow map is a local diffeomorphism at every finite similarity-time interval.

If a barrier face is transported with material normal velocity, tangential changes are only reparametrizations of the same set.

Hence a collection of embedded material faces cannot spontaneously cross, reconnect, merge, split, or change incidence under the diffeomorphic material map.

Therefore any actual topology change in the sheet network requires at least one face to cease satisfying the material-barrier condition.

By M5-664 this means a higher-jet crossing event, and in the first-order case it is the M5-654 critical-force creation/rotation mechanism.

Thus lower-dimensional junction strata do not create a new silent topology-change loophole.

---

## 4. Sheet cells

Remove the codimension-one silent barrier faces from one connected high-amplitude component `C_L`.

The remaining open regions are sheet cells.

Choose the cell `Omega_L` containing the fixed coherent carrier ball of a persistent lineage.

M5-657 gives a fixed ball radius and amplitude floor, so

\[
\boxed{|\Omega_L|\ge v_0>0}
\]

whenever the cell is retained.

There are two geometric possibilities for its boundary.

---

## 5. Internal material cell

Suppose every two-dimensional boundary face of `Omega_L` is a silent material barrier and the cell does not meet the outer amplitude boundary `rho=a0`.

Lower-dimensional junction sets have zero surface measure and do not contribute to the normal volume flux.

Therefore `Omega_L` is a material region.

Since

\[
\nabla\cdot B=\frac32,
\]

its volume obeys

\[
\boxed{
|\Omega_L(\theta)|
=
|\Omega_L(\theta_0)|
\exp\left[\frac32(\theta-\theta_0)\right].
}
\]

But the full sheet network is retained inside the fixed bounded similarity core.

Hence such an internal material cell cannot persist recurrently for arbitrarily large forward similarity time.

---

## 6. Cell meeting the amplitude boundary

If instead the cell boundary includes a portion

\[
A_{a_0}\subset\{\rho=a_0\},
\]

then M5-662 applies.

The material barrier faces contribute no relative normal flux, while the exact `+3/2` volume expansion must be offset through `A_{a0}`.

Thus

\[
\boxed{
\langle\mathcal T_{a_0}\rangle
\ge\frac32v_0>0.
}
\]

This is the fixed-amplitude material sheath-turnover branch.

---

## 7. Uniform lifetime of a turnover-free internal cell

Let `V_core` be the volume of the fixed normalized storage ball containing the recurrent active core.

An internal material cell starts with

\[
|\Omega_L|\ge v_0
\]

and cannot exceed `V_core`.

Therefore its maximum turnover-free lifetime is

\[
\boxed{
T_{cell}^{max}
\le
\frac23\log\frac{V_{core}}{v_0}.
}
\]

Thus a persistent sheet architecture cannot postpone crossing/turnover events to arbitrarily sparse future times.

If it remains recurrent, an event must occur with a uniformly bounded gap.

---

## 8. Resulting positive-rate event alternative

For every persistent high-amplitude relabeling lineage, M5-657 provides a same-component negative payer.

The present cell argument gives

\[
\boxed{
R_{multi-sheet}^{persistent}
\Longrightarrow
C_{cross}^{force/higher-jet}
\lor
T_{sheath}^{rho=a_0},
}
\]

with a uniformly bounded event-free interval on the retained branch.

There is no additional `silent static sheet network` survivor.

---

## 9. Relation to M5-653 toy oscillator

The M5-653 oscillator contains no three-dimensional material-sheet cell with the exact similarity divergence

\[
\nabla\cdot B=\frac32.
\]

It therefore does not test the material-volume obstruction derived here.

However the oscillator still warns that repeated crossing/turnover events can in principle recycle bounded flux resources unless the PDE-specific cost of those events is controlled.

Thus M5-665 removes static silent patching but does **not** yet eliminate the dynamic event branch.

---

## 10. Updated CE-H relabeling frontier

The relabeling side is now compressed to

\[
\boxed{
R_{persistent\ relabeling}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{higher-jet}
\lor
T_{sheath}^{rho=a_0}.
}
\]

All three are positive-rate dynamic mechanisms on a recurrent survivor.

---

## 11. Next target

The next calculation should stop searching for additional static geometry and instead ask whether the three dynamic mechanisms admit a **single signed or finite-resource ledger**.

A natural candidate is the fixed-threshold quadratic truncated-amplitude functional

\[
N_a=\frac12\int(\rho-a)_+^2dy,
\]

because multiplication of the CE-H scalar elliptic equation by `(rho-a)_+` removes the amplitude-boundary term and produces the exact component deficit already used in M5-656--657.

This may couple directly to the positive-rate sheath/crossing activity at the same fixed threshold.

---

## 12. Firewall

The stratified argument assumes standard local analytic stratification in the high-amplitude region and smooth material flow over finite intervals.

It does not claim that the remaining dynamic event activity is impossible.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]