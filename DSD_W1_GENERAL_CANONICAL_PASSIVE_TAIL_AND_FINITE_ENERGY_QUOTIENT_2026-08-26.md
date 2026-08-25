# DSD W1 General Canonical Passive Tail and Finite-Energy Quotient

Date: 2026-08-26

Status: **CANONICAL PASSIVE CRITICAL TAIL CONSTRUCTED FOR EVERY W1 STATE, NOT ONLY PERIODIC STATES / TAIL COVARIANCE PROVED / EXTERIOR DIFFERENCE SHOWN L2 INTERSECTION L3 / DIVERGENCE-FREE GLOBAL CUTOFF QUOTIENT REDUCES PERIODIC AND APERIODIC W1 TO ONE FORCED FINITE-ENERGY PROBLEM / GLOBAL REGULARITY UNPROVED.**

## 1. Global descendant field

For a W1 state `V` define, for `Y neq 0`,

\[
D_h[V](Y)
:=
 e^{h/2}(S(h)V)(e^{h/2}Y).
\]

On an annulus `A_R={R<|Y|<2R}` this is exactly the co-moving blow-down divided by the fixed scale normalization:

\[
R D_h[V](Rz)
=
W_R(z,h).
\]

The descendant-limit theorem therefore gives convergence on every sufficiently remote annulus.
Compatibility on overlapping annuli is automatic because all local limits arise from the same globally defined fields `D_h[V]`.

Define the canonical passive tail

\[
\boxed{
T_V(Y)
:=
\lim_{h\to\infty}D_h[V](Y)
}
\]

in local H^-1, L2, and L3 on the punctured exterior.

By starting the argument after a finite age at which a fixed compact annulus has moved into the uniform W1 far region, the same limit can be defined on every compact subset of `R3\{0}`.  Only the quantitative small-error estimates below require large initial radius.

---

## 2. Quantitative tail approximation

On a large fixed annulus `A_R`, the descendant estimates give

\[
\left\|
R[V(R\cdot)-T_V(R\cdot)]
\right\|_{H^{-1}(A)}
\le CR^{-2},
\]

\[
\left\|
R[V(R\cdot)-T_V(R\cdot)]
\right\|_2
\le CR^{-1},
\]

and

\[
\boxed{
\left\|
R[V(R\cdot)-T_V(R\cdot)]
\right\|_3
\le CR^{-1/2}.
}
\]

Because L3 is scale invariant,

\[
\boxed{
\|V-T_V\|_{L^3(A_R)}
\le CR^{-1/2}.
}
\]

For L2,

\[
\int_{A_R}|V-T_V|^2dY
=
R
\left\|
R[V(R\cdot)-T_V(R\cdot)]
\right\|_2^2,
\]

so

\[
\boxed{
\|V-T_V\|_{L^2(A_R)}^2
\le CR^{-1}.
}
\]

Along dyadic shells these bounds are summable:

\[
\sum_k
\|V-T_V\|_{L^3(A_{2^kR_0})}^3
\lesssim
\sum_k(2^kR_0)^{-3/2}<\infty,
\]

and

\[
\sum_k
\|V-T_V\|_{L^2(A_{2^kR_0})}^2
\lesssim
\sum_k(2^kR_0)^{-1}<\infty.
\]

Hence

\[
\boxed{
V-T_V
\in
L^2(\{|Y|>R_0\})
\cap
L^3(\{|Y|>R_0\}).
}
\]

The constants are uniform on the compact W1 class.

---

## 3. Divergence-free and Type-I character

Every field `D_h[V]` is divergence-free.  The local limit therefore satisfies

\[
\boxed{\nabla\cdot T_V=0}
\]

distributionally on `R3\{0}`.

The remote Type-I bound passes to the limit:

\[
\boxed{|T_V(Y)|\le A_0|Y|^{-1}}
\]

in the corresponding essential/shell sense.

Consequently the tail is critical weak-L3 at infinity:

\[
T_V\in L^{3,\infty}_{loc,crit}
\]

and is generally not in global L2 or strong L3.

---

## 4. Exact covariance under the W1 flow

For `tau>=0`,

\[
\begin{aligned}
T_{S(\tau)V}(Y)
&=
\lim_{h\to\infty}
 e^{h/2}(S(h+\tau)V)(e^{h/2}Y)\\
&=
 e^{-\tau/2}
\lim_{k\to\infty}
 e^{k/2}(S(k)V)(e^{k/2}e^{-\tau/2}Y).
\end{aligned}
\]

Therefore

\[
\boxed{
T_{S(\tau)V}(Y)
=
 e^{-\tau/2}
T_V(e^{-\tau/2}Y).
}
\]

Along a W1 trajectory `V(s)=S(s)V_0`, write `T(Y,s)=T_{V(s)}(Y)`.  Then the finite-difference covariance is exactly the solution law for

\[
\boxed{
T_s
+\frac12T
+\frac12Y\cdot\nabla T
=0.
}
\]

Thus the canonical W1 tail is an exact passive linear-dilation background.

No periodicity has been used.

---

## 5. Relation to radial genealogy

For a complete orbit `V(s)`, covariance gives

\[
T_{V(0)}(e^{h/2}Y)
=
 e^{-h/2}T_{V(-h)}(Y).
\]

Hence the log-radius/backward-time genealogy is built directly into the passive tail.

Periodic core dynamics makes this field log-periodic.
Aperiodic minimal dynamics makes its logarithmic radial structure recurrent and aperiodic.

They are two dynamical realizations of the same canonical field construction.

---

## 6. Zero spherical flux

For every finite `h`, `D_h[V]` is smooth and divergence-free across the origin, so

\[
\int_{|Y|=r}D_h[V]\cdot n\,dS=0
\]

for every `r>0`.

Using the local H1 control and trace convergence along a subsequence, the descendant limit inherits

\[
\boxed{
\int_{|Y|=r}T_V\cdot n\,dS=0
}
\]

for almost every `r`, hence in the distributional flux sense for all regular radii.

This is stronger than the periodic DSS argument, where zero flux was obtained from discrete homogeneity.

---

## 7. Divergence-free tail cutoff

Choose a fixed large `R_0` and a smooth radial cutoff `chi` with

\[
chi=0\quad(|Y|\le R_0),
\qquad
chi=1\quad(|Y|\ge2R_0).
\]

Then

\[
g:=\nabla chi\cdot T_V
\]

is supported in the transition annulus.  Its mean vanishes because the tail has zero spherical flux.

A Bogovskii correction `b_V` exists on the transition annulus with

\[
\nabla\cdot b_V=g.
\]

Define

\[
\boxed{
B_V:=chi T_V-b_V.
}
\]

Then

\[
\boxed{
\nabla\cdot B_V=0,
}
\]

and

\[
B_V=0\quad(|Y|\le R_0),
\qquad
B_V=T_V\quad(|Y|\ge2R_0).
\]

---

## 8. General finite-energy/L3 quotient

Define

\[
\boxed{
Q_V:=V-B_V.
}
\]

Inside `B_{2R_0}`, both terms are locally regular/integrable.
Outside `2R_0`,

\[
Q_V=V-T_V.
\]

The summable shell estimates therefore give

\[
\boxed{
Q_V\in
L^2(\mathbb R^3)
\cap
L^3(\mathbb R^3),
\qquad
\nabla\cdot Q_V=0.
}
\]

For fixed cutoff radius the norms are uniformly bounded over the compact W1 class.

This construction requires no periodicity.

---

## 9. Quotient equation

Let

\[
\mathcal L
:=
\partial_s
-\nu\Delta
+\frac12
+\frac12Y\cdot\nabla.
\]

The W1 field satisfies

\[
\mathcal LV
+\mathbb P\nabla\cdot(V\otimes V)=0.
\]

The uncut tail satisfies only the passive part

\[
T_s+\frac12T+\frac12Y\cdot\nabla T=0,
\]

so its Navier--Stokes residual is

\[
\boxed{
F_T
:=
\nu\Delta T
-
\mathbb P\nabla\cdot(T\otimes T).
}
\]

On a shell of radius `R`, if

\[
F_R^T(z)=R T(Rz),
\]

then the fixed-cell H1 bound gives the critical distributional estimate

\[
\boxed{
\left\|
R^3F_T(R\cdot)
\right\|_{H^{-1}(A)}
\le C.
}
\]

Thus the tail residual has the natural `R^-3` critical size in H^-1.

After the cutoff/Bogovskii modification, `Q_V` satisfies a forced Leray equation of the form

\[
\boxed{
\mathcal LQ
+
\mathbb P\nabla\cdot
(Q\otimes Q+Q\otimes B+B\otimes Q)
=
\mathcal F_B,
}
\]

where `mathcal F_B` consists of

- the critical tail residual outside `2R_0`;
- finite transition-annulus cutoff/Bogovskii terms.

The forcing is not zero and therefore ordinary unforced Liouville/backward-uniqueness theorems cannot be applied directly.

---

## 10. Physical static-trace interpretation

Along a complete W1 orbit, let

\[
\lambda=e^{-s/2}.
\]

The passive covariance gives

\[
T(Y,s)
=
 e^{-s/2}T(e^{-s/2}Y,0).
\]

Therefore its inverse similarity transform is time-independent:

\[
\boxed{
\lambda^{-1}T(x/\lambda,s)
=T(x,0).
}
\]

Thus the canonical passive W1 tail is a **static physical critical trace field**.

The aperiodic dynamics is encoded in the log-radial spatial structure of that static trace rather than in time evolution of the trace itself.

This generalizes the physical-trace interpretation previously obtained only on the periodic branch.

---

## 11. Local convergence to the static trace

For any fixed physical annulus away from the center, its normalized radius is

\[
R=r/\lambda\to\infty.
\]

The exterior tail estimates therefore imply, for the formal physical solution associated with the W1 orbit,

\[
\|u(\cdot,t)-T_{phys}\|_{L^3(A_r)}
\lesssim
R^{-1/2}
\lesssim
\lambda^{1/2}r^{-1/2},
\]

and

\[
\|u(\cdot,t)-T_{phys}\|_{L^2(A_r)}^2
\lesssim
\lambda R^{-1}
=
\frac{\lambda^2}{r}.
\]

Hence

\[
\boxed{
u(\cdot,t)\to T_{phys}
\quad\text{strongly in local L2 and L3 away from the center.}}
\]

This is a theorem about the W1 complete-orbit model.  Passing it to the original finite-energy prelimit on an `n`-dependent expanding window remains the separate scale-infinity interface problem.

---

## 12. Major branch reduction

The earlier endpoint had two tail constructions:

\[
P_{DSS}^{long}
\quad\text{versus}\quad
A_{min}^{aper}.
\]

The present construction replaces them by

\[
\boxed{
W1
\Longrightarrow
\text{canonical passive critical background }T
+
\text{divergence-free }Q\in L^2\cap L^3.
}
\]

The periodic/aperiodic distinction survives only in the internal log-radial structure of `T` and in the dynamics of `Q`; it is no longer a split in whether a finite-energy quotient exists.

---

## 13. New common frontier

The entire W1 endpoint is now reduced to one forced quotient problem:

\[
\boxed{
\text{critical passive }T\sim1/R
\ +\
Q\in L^2\cap L^3
\ +\
\text{critical }R^{-3}\text{ residual/interface forcing}.
}
\]

A complete proof would need a rigidity theorem showing that no nonzero compact recurrent Leray solution can have this decomposition while arising as the limit of a finite-energy unforced prelimit.

No such forced-Liouville/interface theorem is presently proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
