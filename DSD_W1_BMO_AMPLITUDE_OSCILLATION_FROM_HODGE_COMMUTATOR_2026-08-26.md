# DSD W1 BMO Amplitude Oscillation from the Hodge Commutator

Date: 2026-08-26

Status: **CRITICAL `p=3` HODGE-COMMUTATOR WORK FORCES A POSITIVE BMO SEMINORM OF `|U|` / COMPACT CORE REGULARITY AND FAR-TAIL DECAY LOCALIZE THAT OSCILLATION TO A FIXED INTERMEDIATE LERAY SCALE / GLOBAL REGULARITY UNPROVED.**

## 1. Input: the exact commutator form of the critical work

Let

\[
m:=|U|,
\qquad
L:=\Omega\times U,
\qquad
L_s:=\mathbb P L,
\]

where `mathbb P` is the Leray projection.

The global `p=3` nonlinear/pressure work can be written as

\[
F_3
=-\langle mU,L_s\rangle.
\]

Since `mathbb P U=U`, `mathbb P` is self-adjoint, and

\[
U\cdot L=U\cdot(\Omega\times U)=0,
\]

we have

\[
\boxed{
F_3
=-\left\langle [\mathbb P,m]U,L\right\rangle.
}
\]

Thus the positive W1 endpoint work is exactly a Hodge/amplitude commutator effect.

---

## 2. Coifman--Rochberg--Weiss estimate

The Leray projection is a finite matrix of the identity and double Riesz transforms. The classical Coifman--Rochberg--Weiss theorem gives, for `1<p<infinity`,

\[
\|[\mathbb P,m]f\|_{L^p}
\le C_p\|m\|_{BMO}\|f\|_{L^p}.
\]

Choose `p=4`.

Since W1 supplies

\[
U\in L^4,
\qquad
\Omega\in L^2,
\]

we have

\[
L=\Omega\times U\in L^{4/3}
\]

and therefore

\[
\begin{aligned}
|F_3|
&\le
\|[\mathbb P,m]U\|_4\|L\|_{4/3}
\\
&\le
C\|m\|_{BMO}\|U\|_4^2\|\Omega\|_2.
\end{aligned}
\]

Hence

\[
\boxed{
|F_3|
\le
C_{BMO}
\||U|\|_{BMO}
\|U\|_4^2
\|\Omega\|_2.
}
\]

---

## 3. Positive BMO certificate on recurrent critical-work events

On the compact W1 class there are uniform ceilings

\[
\|U\|_4\le M_4,
\qquad
\|\Omega\|_2\le Z_2.
\]

The invariant endpoint has

\[
\langle F_3\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6}
=:f_*>0.
\]

Therefore the open event set

\[
\mathcal O_F
:=
\{U:F_3(U)>f_*/2\}
\]

is nonempty. By minimal recurrence it is visited with bounded Leray-time gaps.

On every such event,

\[
\boxed{
\||U|\|_{BMO}
\ge
b_*
:=
\frac{f_*}{2C_{BMO}M_4^2Z_2}
>0.
}
\]

Thus a nontrivial W1 survivor must recurrently maintain a fixed amount of scale-invariant velocity-amplitude oscillation.

---

## 4. Small spatial scales cannot realize the BMO floor

Compact smoothness of the finite W1 core supplies a uniform local Lipschitz ceiling

\[
\|\nabla U\|_{L^\infty(B_{R_c})}
\le K_c
\]

for a sufficiently large fixed core radius `R_c`.

Therefore for any ball `B_r(x)` contained in the controlled core,

\[
\fint_{B_r(x)}
\left||U|-(|U|)_{B_r(x)}\right|
\le C K_c r.
\]

Choose

\[
\boxed{
r_-:=\frac{b_*}{4CK_c}>0.}
\]

Then every core ball with `r<r_-` has mean oscillation strictly below `b_*/2`.

Outside the core, the W1 Type-I shell derivative bounds make the same conclusion stronger at sufficiently remote small relative scales.

Hence the BMO floor cannot be produced by arbitrarily small normalized structures.

---

## 5. Very large spatial scales cannot realize the BMO floor either

The W1 tail satisfies schematically

\[
|U(Y)|\lesssim |Y|^{-1},
\qquad
|\nabla U(Y)|\lesssim |Y|^{-2}
\]

on remote shells.

Consequently

\[
\int_{B_R}|U|\,dY
\lesssim R^2
\]

and therefore

\[
\fint_{B_R}|U|\,dY
\lesssim R^{-1}.
\]

For balls centered far from the core and not reaching it, the pointwise tail ceiling and derivative estimate give an analogous or stronger decay of mean oscillation.

Thus there exists a finite radius

\[
\boxed{r_+<\infty}
\]

such that every ball with radius `r>r_+` has amplitude mean oscillation below `b_*/2`.

---

## 6. Intermediate-scale amplitude-contrast witness

Since on every critical-work event

\[
\||U|\|_{BMO}\ge b_*,
\]

but neither `r<r_-` nor `r>r_+` can realize that seminorm, there must exist a ball

\[
B_{r_{osc}}(Y_{osc})
\]

with

\[
\boxed{
r_-\le r_{osc}\le r_+}
\]

such that

\[
\boxed{
\fint_{B_{r_{osc}}(Y_{osc})}
\left||U|-(|U|)_{B_{r_{osc}}}\right|dY
\ge c_{osc}>0.
}
\]

Thus the critical commutator work forces a **fixed intermediate-scale amplitude-contrast structure**, recurrently in Leray time.

This is stronger than a mere high-amplitude point or blob: it certifies nontrivial amplitude variation across a scale bounded away from both zero and infinity.

---

## 7. DSD interpretation

The Hodge projection is not an independent physical source. It converts the scalar streamline-amplitude input

\[
e=U\cdot\nabla|U|
\]

into the nonlocal pressure/Bernoulli component.

The CRW estimate shows that this conversion cannot carry fixed critical work unless the amplitude field has fixed BMO oscillation.

Hence the current DSD chain can be sharpened to

\[
\boxed{
\mathscr R_3>0
\Longrightarrow
F_3>0\text{ recurrently}
\Longrightarrow
\||U|\|_{BMO}\ge b_*
\Longrightarrow
\text{fixed intermediate-scale amplitude contrast}.
}
\]

This is a genuinely scale-critical (`beta=0`) structural witness.

---

## 8. What this does not yet prove

A positive BMO floor is not by itself contradictory. Large BMO data are not excluded by standard Navier--Stokes theory, and the physical cost of reproducing one normalized oscillation may still be subcritical when measured by kinetic energy.

The value of the result is that the remaining W1 survivor must now simultaneously maintain:

1. finite-parent pressure-downhill work;
2. recurrent vorticity stretching;
3. a fixed intermediate-scale BMO amplitude contrast;
4. large weak-`L3` criticality.

The next useful step is to combine the BMO amplitude witness with the scale-invariant ratio

\[
|\Omega|/|U|^2
\]

and determine whether pressure--stretch locking can occur without paying a fixed critical direction/gradient action on the same intermediate scale.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
