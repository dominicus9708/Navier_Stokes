# DSD W1 Periodic Divergence-Free Finite-Energy Quotient

Date: 2026-08-26

Status: **NAIVE CUTOFF-DIVERGENCE DEFECT IDENTIFIED / ZERO FLUX OF THE CANONICAL DSS TAIL PROVED / COMPACT BOGOVSKII CUTOFF CORRECTION AVAILABLE / PERIODIC W1 DECOMPOSED INTO A DIVERGENCE-FREE CRITICAL TAIL EXTENSION PLUS A GLOBAL DIVERGENCE-FREE L2 INTERSECTION L3 QUOTIENT / PHYSICAL QUOTIENT VANISHES IN L2 AT THE CANDIDATE SINGULAR TIME / FORCED-PERTURBATION RIGIDITY STILL OPEN / GLOBAL REGULARITY UNPROVED.**

## 1. Input

From the preceding canonical-tail note, the periodic W1 branch has

\[
U(Y,s)=T(Y,s)+R(Y,s)
\]

for sufficiently large `|Y|`, where

\[
T(Y,s)
=
|Y|^{-1}
\Phi\!\left(
\widehat Y,
\log|Y|-\frac{s}{2}
\right),
\]

`Phi` is periodic in its log-radius argument with period

\[
L=S/2,
\]

and

\[
U-T\in L^3(|Y|>R_0).
\]

The same interpolation argument also contains stronger `L2` information, which will be used below.

The naive cutoff

\[
Q=U-\chi T
\]

is not necessarily divergence free because

\[
\nabla\cdot(\chi T)=\nabla\chi\cdot T.
\]

This file repairs that point.

---

## 2. The canonical tail is divergence free

Each far blow-down limit inherits

\[
\nabla\cdot T=0
\]

away from the origin.

The canonical tail is also discretely homogeneous:

\[
\boxed{
T(\lambda Y,s)=\lambda^{-1}T(Y,s),
\qquad
\lambda=e^{S/2}>1,
}
\]

at a fixed periodic phase, with the equivalent spacetime/log-phase formulation already established in the preceding notes.

---

## 3. Spherical flux of a `-1` DSS divergence-free tail is zero

Define

\[
\mathcal F(r,s)
:=
\int_{|Y|=r}T(Y,s)\cdot n\,dS.
\]

Since `div T=0` on every annulus excluding the origin, the divergence theorem gives

\[
\boxed{
\mathcal F(r_2,s)=\mathcal F(r_1,s)
}
\]

for every `0<r1<r2` on the tail domain.

On the other hand, discrete homogeneity gives

\[
\begin{aligned}
\mathcal F(\lambda r,s)
&=
\int_{|Y|=\lambda r}T(Y,s)\cdot n\,dS\\
&=
\lambda
\mathcal F(r,s).
\end{aligned}
\]

Because the flux is also radius-independent,

\[
\mathcal F(\lambda r,s)=\mathcal F(r,s).
\]

Thus

\[
(\lambda-1)\mathcal F(r,s)=0.
\]

Since `lambda>1`,

\[
\boxed{
\mathcal F(r,s)=0.
}
\]

Therefore the periodic critical tail carries no net source/sink flux through a sphere.

This zero-flux fact is exactly what is needed for a compact divergence correction of a radial cutoff.

---

## 4. Radial cutoff and compatibility condition

Choose a smooth radial cutoff `chi_R` satisfying

\[
\chi_R=0\quad(|Y|\le R),
\]

\[
\chi_R=1\quad(|Y|\ge2R),
\]

with

\[
|\nabla\chi_R|\lesssim R^{-1}.
\]

Set

\[
g_R:=\nabla\chi_R\cdot T.
\]

Then `g_R` is supported in the bounded annulus

\[
A_R^*:=\{R<|Y|<2R\}.
\]

Its integral is

\[
\begin{aligned}
\int_{A_R^*}g_RdY
&=
\int_{\mathbb R^3}\nabla\cdot(\chi_RT)dY\\
&=
\lim_{r\to\infty}
\int_{|Y|=r}T\cdot n\,dS\\
&=0.
\end{aligned}
\]

Thus the standard Bogovskii compatibility condition holds:

\[
\boxed{
\int g_R=0.
}
\]

---

## 5. Compact Bogovskii divergence correction

On the fixed-shape annulus `A_R^*`, let

\[
b_R:=\mathcal B_{A_R^*}(g_R)
\]

be a Bogovskii solution of

\[
\nabla\cdot b_R=g_R,
\]

with zero trace on the annular boundary.

Extend `b_R` by zero outside the annulus.

Define

\[
\boxed{
B_R:=\chi_RT-b_R.
}
\]

Then

\[
\boxed{
\nabla\cdot B_R=0
}
\]

globally in distributions.

Moreover,

\[
B_R=0
\qquad(|Y|<R),
\]

and

\[
B_R=T
\qquad(|Y|>2R).
\]

Thus `B_R` is a divergence-free extension of the canonical critical tail that modifies it only on one finite transition annulus.

Because the annulus has fixed shape after scaling and `T~R^-1` there, standard Bogovskii estimates give the natural critical-scale bounds

\[
\|b_R\|_{L^p(A_R^*)}
\lesssim
\|T\|_{L^p(A_R^*)}
\]

for finite `p` in the admissible range, with analogous first-derivative estimates.

No remote tail is altered.

---

## 6. Define the true divergence-free quotient

Set

\[
\boxed{
Q_R:=U-B_R.
}
\]

Then

\[
\boxed{
\nabla\cdot Q_R=0.
}
\]

Inside `B_R`,

\[
Q_R=U,
\]

which is smooth and locally integrable to every finite power.

Outside `B_{2R}`,

\[
Q_R=U-T.
\]

The transition annulus is bounded.

Thus the preceding canonical-tail result immediately gives

\[
\boxed{
Q_R(s)\in L^3(\mathbb R^3)
}
\]

for every periodic time `s`.

---

## 7. The same construction actually gives global `L2`

The previous scale-defect interpolation gave, on the `k`th same-phase critical cell with radius `R_k`,

\[
\|w-F_\infty\|_{L^2(cell)}
\le
CR_k^{-1}.
\]

Under critical spatial rescaling,

\[
U-T
=
R_k^{-1}(w-F_\infty)
\]

on a cell of volume scale `R_k^3`. Therefore

\[
\begin{aligned}
\|U-T\|_{L^2(C_k)}^2
&=
R_k
\|w-F_\infty\|_{L^2(cell)}^2\\
&\le
R_k\,C^2R_k^{-2}\\
&=
\boxed{C^2R_k^{-1}}.
\end{aligned}
\]

The cells are geometrically separated:

\[
R_k=R_0\lambda^k.
\]

Hence

\[
\sum_{k\ge0}R_k^{-1}<\infty.
\]

Therefore

\[
\boxed{
U-T\in L^2(|Y|>R_0).
}
\]

The interior and transition regions are bounded, so

\[
\boxed{
Q_R(s)\in L^2(\mathbb R^3)\cap L^3(\mathbb R^3).
}
\]

This is stronger than the previous quotient statement.

---

## 8. Uniform periodic quotient bounds

All constants in the periodic one-period defect estimate and W1 shell `H1` ceiling were uniform in periodic time.

Consequently, for every fixed sufficiently large cutoff radius `R`,

\[
\boxed{
\sup_{s\in[0,S]}
\left(
\|Q_R(s)\|_2
+
\|Q_R(s)\|_3
\right)
<\infty.
}
\]

The bound is not claimed uniform as `R->infinity`; indeed retaining more critical tail inside the cutoff can grow the quotient norm.

---

## 9. Physical-variable interpretation

Let the periodic Leray orbit correspond to a backward DSS physical field with candidate singular time `T*`:

\[
u(x,t)
=(T^*-t)^{-1/2}U(Y,s),
\]

\[
Y=\frac{x-X_*}{\sqrt{T^*-t}},
\qquad
s=-\log(T^*-t).
\]

The canonical tail becomes a time-independent physical critical trace

\[
t_*(x)
=
\frac1{|x-X_*|}
\Phi\!\left(
\widehat{x-X_*},
\log|x-X_*|
\right).
\]

The divergence-free cutoff extension `B_R` corresponds to a critical trace outside a core whose physical radius is

\[
R\sqrt{T^*-t}.
\]

Define the physical quotient

\[
q_R(x,t)
:=(T^*-t)^{-1/2}Q_R(Y,s).
\]

Its `L2` norm scales as

\[
\|q_R(t)\|_2^2
=
(T^*-t)^{1/2}
\|Q_R(s)\|_2^2.
\]

Therefore periodic boundedness of `Q_R` gives

\[
\boxed{
\|q_R(t)\|_2
\lesssim
(T^*-t)^{1/4}
\to0
\qquad(t\uparrow T^*).
}
\]

Thus the periodic W1 candidate approaches its static critical trace modulo a finite-energy divergence-free correction that vanishes in physical `L2` at the candidate singular time.

This is a genuine strengthening of the core/trace description.

---

## 10. Exact quotient equation is forced

Write the projected Leray equation as

\[
\mathcal L U
+\mathbb P\nabla\cdot(U\otimes U)=0,
\]

where

\[
\mathcal L
:=
\partial_s
+\frac12
+\frac12Y\cdot\nabla
-\nu\Delta.
\]

Since

\[
U=Q_R+B_R,
\]

we obtain

\[
\boxed{
\mathcal LQ_R
+\mathbb P\nabla\cdot(Q_R\otimes Q_R)
=
-\mathcal F_R
-\mathbb P\nabla\cdot
(Q_R\otimes B_R+B_R\otimes Q_R),
}
\]

where

\[
\boxed{
\mathcal F_R
:=
\mathcal LB_R
+\mathbb P\nabla\cdot(B_R\otimes B_R).
}
\]

Thus the quotient is a finite-energy/strong-`L3` **forced periodic Leray system** around the canonical weak-`L3` critical tail.

---

## 11. Structure of the tail forcing

Outside the transition annulus,

\[
B_R=T.
\]

The canonical tail solves only the linear dilation equation

\[
T_s+\frac12T+\frac12Y\cdot\nabla T=0.
\]

Hence its full Navier-Stokes residual is

\[
\mathcal F_{tail}
=
-\nu\Delta T
+\mathbb P\nabla\cdot(T\otimes T).
\]

Since

\[
T=O(r^{-1}),
\qquad
\nabla T=O(r^{-2})
\]

at the critical scale,

\[
\boxed{
\mathcal F_{tail}=O(r^{-3}).
}
\]

Therefore

\[
\boxed{
\mathcal F_{tail}
\in L^q(|Y|>2R)
\quad\text{for every }q>1.
}
\]

In particular,

\[
\|\mathcal F_{tail}\|_{L^{3/2}(|Y|>2R)}
\lesssim R^{-1}.
\]

The cutoff/Bogovskii part of `F_R` is supported on one finite annulus.

The cross coefficient satisfies

\[
B_R\sim r^{-1}
\]

and therefore belongs to the critical weak space

\[
B_R\in L^{3,\infty}.
\]

This is the exact endpoint nature of the remaining quotient problem.

---

## 12. Why backward uniqueness is not yet immediate

The physical quotient satisfies

\[
q_R(t)\to0
\quad\text{in }L^2
\]

as `t->T*`, but its equation contains a nonzero forcing generated by the static critical trace and the shrinking cutoff/interface.

A function can vanish at the terminal time while having a nonzero terminal time derivative because of such forcing. Schematically,

\[
q(t)=(T^*-t)f
\]

has

\[
q(T^*)=0
\]

but

\[
q_t=-f.
\]

Therefore terminal `L2` vanishing alone does not permit direct backward-uniqueness closure.

This prevents another false proof.

---

## 13. New periodic rigidity target

The periodic W1 branch has now been reduced to

\[
\boxed{
U
=
B_R
+
Q_R,
}
\]

where

\[
\boxed{
\begin{aligned}
&\nabla\cdot B_R=0,
\qquad
B_R=T\text{ outside one finite annulus},\\
&B_R\in L^{3,\infty},\\
&Q_R\in L^2\cap L^3,
\qquad
\nabla\cdot Q_R=0,\\
&Q_R\text{ is periodic},\\
&q_R(t)\to0\text{ in physical }L^2,\\
&\mathcal F_{tail}=O(r^{-3})\in L^{3/2}\text{ at infinity}.
\end{aligned}
}
\]

Thus a successful periodic closure can now target a much narrower theorem:

\[
\boxed{
\text{No nonzero periodic finite-energy/}L^3
\text{ quotient can be supported by a DSS }1/r
\text{ background with the exact W1 }r^{-3}
\text{ residual.}
}
\]

Equivalently, one needs a forced-Liouville or backward-uniqueness theorem at a weak-`L3` critical background.

This is strictly narrower than the previous generic long-period DSS problem.

---

## 14. Status of the aperiodic branch

None of the exact-period telescoping used here applies directly to the aperiodic minimal W1 branch.

Therefore the current W1 frontier is now asymmetric:

### Periodic branch

Reduced to a divergence-free

\[
L^2\cap L^3
\]

forced quotient around one canonical critical DSS trace.

### Aperiodic branch

Still requires construction of a canonical co-moving tail or an independent recurrent rigidity theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
