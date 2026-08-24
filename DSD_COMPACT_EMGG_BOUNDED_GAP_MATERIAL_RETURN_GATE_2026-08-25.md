# DSD Compact EMGG Bounded-Gap Material Return Gate

Date: 2026-08-25

Status: **POSITIVE-MEASURE HIGH STATES PRODUCE FIXED BOUNDED-LERAY-GAP HIGH-HIGH RETURNS / OCCUPIED PACKETS CAN BE TRACKED MATERIALLY ACROSS THOSE GAPS / COMPACT-CORE EMGG REDUCED TO MATERIAL RETURN OR LOCAL EXPOSURE / AGE-k WEIGHTED RETURN DENSITY STILL NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The compact RWLG and occupied-packet extraction notes prove that, on the genuinely precompact fixed-center recurrent class `K`, the Betchov high-enstrophy set

\[
A_\theta
\]

has positive invariant measure

\[
\mu(A_\theta)=d_K>0
\]

and every state in `A_theta` contains a current-scale occupied vorticity packet inside a fixed bounded Leray ball.

The remaining compact-class EMGG question is whether those repeated Eulerian packets can be compared through the actual material flow.

This note proves a bounded-gap material-return/exposure gate.

---

## 2. Discrete sampling of the invariant Leray flow

Let

\[
\Phi_s:K\to K
\]

denote the Leray-time evolution on the complete recurrent trajectory/class under consideration, and let `mu` be the invariant probability measure already used in the Betchov time-average argument.

Fix any sampling time

\[
h>0.
\]

Then the map

\[
T:=\Phi_h
\]

preserves `mu`.

Apply Poincare recurrence/Kac's return-time lemma to the measurable set `A_theta`.

Let `tau_A(x)` be the first positive integer `n` such that

\[
T^nx\in A_\theta.
\]

On the recurrent part of `A_theta`, Kac's estimate gives the conditional mean bound

\[
\mathbb E_{A_\theta}[\tau_A]
\le
\frac1{d_K}.
\]

Hence by Markov's inequality,

\[
\mu_{A_\theta}
\left(
\tau_A\le\frac{2}{d_K}
\right)
\ge\frac12.
\]

Define

\[
N_K
:=
\left\lceil\frac{2}{d_K}\right\rceil.
\]

Then a positive-measure subset of `A_theta` returns to `A_theta` in at most `N_K` discrete steps.

Because only finitely many return integers `1,...,N_K` are available, there exists at least one

\[
1\le n_*\le N_K
\]

such that

\[
\boxed{
\mu\left(
A_\theta\cap T^{-n_*}A_\theta
\right)>0.
}
\]

Set the fixed Leray return gap

\[
\boxed{
\Delta s_*:=n_*h,
\qquad
h\le\Delta s_*\le N_Kh<\infty.
}
\]

Thus the recurrent orbit contains a positive-measure family of high-high pairs separated by one fixed finite Leray-time gap.

**Status: PROVED from the invariant-measure recurrence framework.**

---

## 3. Scale comparability across the fixed Leray gap

Let the paired physical times be

\[
t_a<t_b<T^*,
\]

with

\[
s_b-s_a=\Delta s_*.
\]

Since

\[
s=-\log(T^*-t),
\]

we have exactly

\[
\boxed{
\frac{T^*-t_b}{T^*-t_a}
=e^{-\Delta s_*}.
}
\]

Hence the standard similarity length satisfies

\[
\boxed{
\frac{\sqrt{T^*-t_b}}
{\sqrt{T^*-t_a}}
=e^{-\Delta s_*/2}.
}
\]

On the first-hitting recurrent clock corridor, the first-hitting radius is two-sided comparable to the similarity radius. Therefore the natural first-hitting scales at the two paired times differ by only a fixed factor depending on `Delta s_*` and the clock constants.

Likewise the natural vorticity amplitudes differ by only a fixed multiplicative factor.

Thus a packet that remains comparable to its initial current scale at `t_a` remains a fixed-multiple current-scale packet at `t_b`.

---

## 4. Initialize the material packet at the first high state

By the compact occupied-packet extraction theorem, at `t_a` there is a physical ball

\[
B_{\ell_a}(x_a)
\]

with

\[
\boxed{
 c_r r_a
\le
\ell_a
\le
C_r r_a
}
\]

and

\[
\boxed{
|\omega(x,t_a)|
\ge
b_KW_a
\qquad
(x\in B_{\ell_a}(x_a)),
}
\]

where `r_a,W_a` denote the contemporaneous first-hitting scale/amplitude and all constants are fixed on `K`.

Let

\[
A_a(t)
\]

be the material image of this ball under the smooth pre-singular Lagrangian flow.

---

## 5. Local packet exposures across the bounded-gap interval

On

\[
I=[t_a,t_b],
\]

define the packet strain exposure

\[
\Sigma_a(I)
:=
\int_I
\sup_{x\in A_a(t)}|S(x,t)|dt,
\]

the packet diffusion exposure

\[
\mathcal D_a(I)
:=
\frac\nu{W_a}
\int_I
\sup_{x\in A_a(t)}|\Delta\omega(x,t)|dt,
\]

and a tube-deformation exposure

\[
\Lambda_a(I)
:=
\int_I
\sup_{x\in H_a(t)}|\nabla u(x,t)|dt,
\]

where `H_a(t)` contains the material packet and the connecting line segments needed for the bi-Lipschitz estimate.

Fix a finite deformation threshold `L>0` and the corresponding diffusion threshold

\[
D_*:=\frac{b_K}{2}e^{-L}.
\]

Then the packet-generic material transport theorem gives the exact finite alternative:

### Exposure branch

\[
\boxed{
\Sigma_a(I)>L
\quad\lor\quad
\Lambda_a(I)>L
\quad\lor\quad
\mathcal D_a(I)>D_*.
}
\]

### Quiet material-descendant branch

Otherwise `A_a(t_b)` contains a ball of radius

\[
\boxed{
\ell_b^{desc}
\ge
c_{desc}r_a
}
\]

on which

\[
\boxed{
|\omega(x,t_b)|
\ge
b_{desc}W_a.
}
\]

Because the two natural scales/amplitudes are comparable across the fixed `Delta s_*`, this descendant ball obeys

\[
\boxed{
\ell_b^{desc}
\ge
c_{ret}r_b,
\qquad
|\omega(x,t_b)|
\ge
b_{ret}W_b
}
\]

with fixed positive constants depending only on the compact-class and return-gap data.

Thus quiet evolution creates a genuine material current-scale descendant at the second high state.

**Status: PROVED.**

---

## 6. The material descendant remains in a bounded Leray region on compact K

Let `Y(s)` be the standard Leray coordinate of the transported packet center relative to the fixed compact-class gauge/center.

A material trajectory obeys

\[
\boxed{
\frac{dY}{ds}
=V(Y,s)+\frac12Y.
}
\]

The compact `H2` strain/vorticity class and fixed gauge give a uniform velocity-gradient bound

\[
\|\nabla V(s)\|_\infty\le G_K
\]

and a fixed-gauge local velocity bound at one reference point

\[
|V(0,s)|\le V_{0,K}.
\]

Hence

\[
|V(Y,s)|
\le
V_{0,K}+G_K|Y|.
\]

Therefore

\[
\frac{d}{ds}|Y|
\le
V_{0,K}
+\left(G_K+\frac12\right)|Y|.
\]

The initial occupied packet lies in a fixed ball `B_{R_{occ,K}}`. Gronwall over the fixed interval `Delta s_*` gives

\[
\boxed{
|Y(s_b)|
\le
R_{ret,K}<\infty,
}
\]

where `R_ret,K` depends only on the compact-class bounds and the fixed return gap.

Thus on the quiet branch the material descendant cannot escape to infinite normalized radius between the paired high states.

This is a fixed-gauge compact-class statement and does not use a bare Galilean-noninvariant difference of first-hitting centers.

**Status: PROVED under the existing fixed-gauge compact-class definition.**

---

## 7. Compact-core EMGG alternative

For every start state in the positive-measure high-high pair set

\[
B_*:=A_\theta\cap\Phi_{-\Delta s_*}A_\theta,
\]

one obtains the finite material alternative

\[
\boxed{
\text{large local strain/tube-deformation exposure}
\lor
\text{large local diffusion/fixed-derivative exposure}
\lor
\text{bounded-core material return packet}.
}
\]

The last branch is a genuine material statement: the packet at the second high time contains descendants of fluid particles that occupied the first high-time packet.

No identification with the independently extracted second-time Eulerian packet is required.

Therefore the broad compact-core Eulerian-to-Material Genealogy Gate is closed:

\[
\boxed{
\text{positive-measure recurrent occupied packets on compact }K
\Longrightarrow
\text{material return}
\lor
\text{local deformation/diffusion action}.
}
\]

---

## 8. Positive-frequency version along a generic recurrent orbit

Because `mu(B_*)>0`, a recurrent orbit generic for the selected time-average measure visits `B_*` with positive asymptotic frequency, modulo the usual boundary-null approximation of the indicator by continuous observables.

The corresponding fixed-length Leray intervals have uniformly bounded overlap. By selecting one residue class / greedy disjoint subfamily, one may retain infinitely many pair intervals with positive lower occurrence frequency and disjoint interiors up to a fixed multiplicity constant.

Hence along the recurrent orbit either

1. local exposure events occur on infinitely many bounded-gap high-high intervals; or
2. bounded-core material returns occur on infinitely many such intervals; or
3. both occur.

This is stronger than an exceptional-sequence material statement.

---

## 9. What this does not close

The material return proved here is a **bounded-core recurrent return between two high states separated by a fixed Leray gap**.

It is not yet the age-`k` weighted shell return density

\[
\mathfrak R_k
\]

needed for the cubic-tail physical-dissipation contradiction.

In particular, it does not prove

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

for arbitrarily old remote labels.

The quiet-ancestor scaling audit shows why: a passive one-ancestor-per-generation critical tail has enough compact-core/material coherence to recur while still carrying only a vanishing amount of physical weighted return time at each late historical scale.

Thus compact-core EMGG and cubic-tail weighted genealogy are distinct levels and must not be conflated.

---

## 10. DSD audit

The finite formed channels are

- invariant compact class `K`;
- measurable high-state set `A_theta`;
- one fixed discrete return number `n_*`;
- one fixed Leray gap `Delta s_*`;
- one finite occupied packet at the first high state;
- one material image over a finite interval;
- local packet/tube exposure integrals;
- one bounded-core descendant packet.

No infinite material history is treated as one primitive formed object.

No equality is assumed between the material descendant and an independently selected Eulerian packet at the second time.

---

## 11. Updated frontier

On the compact recurrent branch, the chain is now

\[
\boxed{
\text{positive-density Betchov high states}
\to
\text{bounded critical shell}
\to
\text{occupied packet}
\to
\text{bounded-gap material return or local exposure}.
}
\]

Therefore the unresolved compact branch is no longer an Eulerian-to-material identification problem at finite radius.

What remains is the genuinely critical long-age question:

\[
\boxed{
\text{Can the recurrent core coexist indefinitely with the passive }1/R
\text{ genealogy tail whose physical return weight is summable?}
}
\]

This is the Leray Recurrent Motion / passive-critical-tail rigidity frontier, not an ordinary local transport gap.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
