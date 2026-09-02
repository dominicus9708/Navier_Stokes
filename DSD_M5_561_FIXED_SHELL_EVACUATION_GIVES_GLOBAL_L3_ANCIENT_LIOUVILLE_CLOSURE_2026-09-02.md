# DSD M5-561 — Fixed-shell evacuation gives global-L3 ancient Liouville closure

Date: 2026-09-02

Status: **CONDITIONAL TAIL CLOSURE / FINITE ENSTROPHY ALREADY GIVES A UNIFORM PARABOLIC-SCALE LOCAL `L3` BOUND, SO THE ONLY GAP TO THE ALBRITTON--BARKER GLOBAL-`L3` LIOUVILLE THEOREM IS LARGE-SCALE TAIL SUMMABILITY / IF A RECURRENT TIME-SHIFT SEQUENCE HAS FIXED-SHELL EVACUATION OUTSIDE ONE FINITE CORE, LOCAL STRONG COMPACTNESS FORCES THE LIMIT VELOCITY GRADIENT TO VANISH ON THE ENTIRE EXTERIOR / GLOBAL `L6` THEN FORCES THE EXTERIOR CONSTANT TO BE ZERO, HENCE THE NONTRIVIAL LIMIT IS GLOBALLY `L3` AND IS RULED OUT BY THE KNOWN ANCIENT LIOUVILLE THEOREM / THEREFORE ANY SURVIVING LOCALLY RECURRENT CORE MUST PREVENT FIXED-SHELL EVACUATION BY REPLENISHING CRITICAL TAIL ACTIVITY AT FINITE SIMILARITY RADII / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Ancient package used here

Let `u(x,s)` be the physical ancient velocity and `omega=curl u` its vorticity, with `s<0`.

The retained Type-I finite-enstrophy package contains

\[
\boxed{
\|\omega(s)\|_2^2
\le C|s|^{-1/2}.
}
\]

In the Biot--Savart/homogeneous Sobolev gauge,

\[
\|\nabla u(s)\|_2
=\|\omega(s)\|_2.
\]

Hence Sobolev gives

\[
\boxed{
\|u(s)\|_6
\le C\|\omega(s)\|_2
\le C|s|^{-1/4}.
}
\]

This estimate is global.

---

## 2. Uniform parabolic-scale local `L3` bound

Fix `L>=1` and consider

\[
B_{L\sqrt{|s|}}.
\]

By Holder,

\[
\|u(s)\|_{L^3(B_{L\sqrt{|s|}})}
\le
|B_{L\sqrt{|s|}}|^{1/6}\|u(s)\|_6.
\]

Since

\[
|B_{L\sqrt{|s|}}|^{1/6}
\asymp
L^{1/2}|s|^{1/4},
\]

we obtain

\[
\boxed{
\|u(s)\|_{L^3(B_{L\sqrt{|s|}})}
\le C L^{1/2}.
}
\]

Thus the survivor already has a scale-critical local `L3` bound on every fixed multiple of the parabolic radius.

The problem is only the limit `L->infinity`.

---

## 3. Similarity form of the same estimate

Let

\[
a=-s=e^{-\theta},
\qquad
y=x/\sqrt a,
\]

and

\[
U(y,\theta)=\sqrt a\,u(\sqrt a\,y,-a).
\]

The `L3` norm is scale invariant, so

\[
\boxed{
\|U(\theta)\|_{L^3(B_L)}
\le C L^{1/2}
}
\]

uniformly in `theta`.

Also

\[
\boxed{
\|U(\theta)\|_6
\le C
}
\]

uniformly on the complete similarity hull.

Therefore every finite ball is harmless; only the infinite shell sum can violate global `L3`.

---

## 4. Connection with the previously quantified critical tail

The repository's dyadic shell audit showed that global `L3` failure requires a critical large-scale stack.

For dyadic annuli

\[
A_R=\{R<|y|<2R\},
\]

let

\[
e_R(\theta)
:=
\int_{A_R}|\nabla U(y,\theta)|^2dy.
\]

The mean-free shell cubic mass obeys

\[
\|U-(U)_{A_R}\|_{L^3(A_R)}^3
\lesssim
(R e_R)^{3/2}.
\]

A non-`L3` survivor may therefore carry the sharp critical stack

\[
e_R\sim R^{-1},
\]

for which ordinary enstrophy is summable but the weighted shell sequence is not `ell^{3/2}`.

This is the exact low-frequency gap left by the local estimate above.

---

## 5. Recurrent time-shift compactness

Let

\[
\theta_j\to+\infty
\]

be a recurrence sequence for the nontrivial active core.

Use the compact analytic hull to extract

\[
U_j(y,s)
:=
U(y,\theta_j+s)
\to
U_\infty(y,s)
\]

in `C^1_loc` on

\[
\mathbb R^3\times\mathbb R
\]

along a subsequence.

The limit is a complete smooth similarity solution and corresponds, under the inverse similarity transform, to a mild bounded ancient Navier--Stokes solution.

The recurrent carrier ensures a nontriviality mark such as

\[
\boxed{
\int_{B_{R_c}}|W_\infty(y,0)|^2dy
\ge e_c>0
}
\]

for some fixed `R_c`.

---

## 6. Fixed-shell evacuation hypothesis

Assume that outside the recurrent active core every fixed annulus evacuates along this same recurrence sequence.

Precisely, for every fixed

\[
R>R_c
\]

and every finite `T>0`, assume

\[
\boxed{
\sup_{|s|\le T}
\int_{A_R}
|\nabla U(\theta_j+s)|^2dy
\longrightarrow0.
}
\]

This is stronger than merely saying that the remote tail has negligible influence on the core.

It says that the tail itself leaves every fixed similarity shell.

This is the quantitative meaning of complete no-replenishment for the escaping conveyor branch.

---

## 7. The limit has zero exterior gradient

Fix one annulus `A_R` with `R>R_c`.

By local `C1` convergence,

\[
\nabla U_j\to\nabla U_\infty
\]

strongly on compact subsets of `A_R x [-T,T]`.

The fixed-shell evacuation assumption therefore implies

\[
\boxed{
\nabla U_\infty(y,s)=0
}
\]

for all

\[
y\in A_R,
\qquad
|s|\le T.
\]

Since `R>R_c` and `T` were arbitrary,

\[
\boxed{
\nabla U_\infty=0
\quad\text{on}\quad
\{|y|>R_c\}\times\mathbb R.
}
\]

---

## 8. Global `L6` kills the exterior constant

For each `s`, the connected exterior region

\[
\{|y|>R_c\}
\]

has zero velocity gradient.

Hence

\[
U_\infty(y,s)=c(s)
\]

there.

But the inherited global bound gives

\[
U_\infty(\cdot,s)\in L^6(\mathbb R^3).
\]

A nonzero spatial constant is not in `L6` on an infinite-volume exterior domain.

Therefore

\[
\boxed{
c(s)=0.}
\]

Thus

\[
\boxed{
U_\infty(y,s)=0
\quad\text{for }|y|>R_c,
\quad\forall s\in\mathbb R.
}
\]

---

## 9. The limit is globally `L3`

Since the velocity is supported in the fixed ball `B_Rc`, Holder and the global `L6` bound give

\[
\|U_\infty(s)\|_3
\le
|B_{R_c}|^{1/6}\|U_\infty(s)\|_6.
\]

Hence

\[
\boxed{
\sup_{s\in\mathbb R}
\|U_\infty(s)\|_3
<\infty.
}
\]

Because `L3` is invariant under the inverse similarity scaling, the corresponding physical ancient solution is bounded in global `L3` at every backward time, in particular along a sequence tending to `-infinity`.

---

## 10. Apply the known ancient Liouville theorem

Albritton--Barker prove that a mild ancient Navier--Stokes solution satisfying

\[
\sup_k\|u(\cdot,t_k)\|_3<\infty
\]

for a sequence

\[
t_k\downarrow-\infty
\]

must be identically zero.

Therefore the physical ancient solution associated with `U_infty` must satisfy

\[
\boxed{u_\infty\equiv0.}
\]

Equivalently,

\[
U_\infty\equiv0.
\]

But the recurrent core nontriviality mark gives

\[
\int_{B_{R_c}}|W_\infty(y,0)|^2dy
\ge e_c>0,
\]

a contradiction.

Hence the fixed-shell evacuation hypothesis is incompatible with a nontrivial recurrent core.

---

## 11. Conditional closure theorem

We have proved the following conditional statement inside the audited compact class:

\[
\boxed{
\begin{aligned}
&\text{nontrivial recurrent Type-I finite-enstrophy core}\\
&+\text{fixed-shell evacuation outside a finite core}\\
&\Longrightarrow\text{global-}L3\text{ ancient limit}\\
&\Longrightarrow U_\infty=0,
\end{aligned}
}
\]

which contradicts core nontriviality.

Therefore

\[
\boxed{
\text{nontrivial recurrent survivor}
\Longrightarrow
\text{failure of fixed-shell evacuation}.
}
\]

---

## 12. Meaning of failure of evacuation

The critical tail cannot merely drift outward forever while leaving every finite exterior shell empty on the core recurrence sequence.

At least one finite similarity scale beyond the active core must be repopulated recurrently.

Schematically,

\[
\boxed{
\exists R>R_c,
\ \epsilon_R>0:
\quad
\limsup_{j\to\infty}
\int_{A_R}|\nabla U(\theta_j)|^2dy
\ge\epsilon_R.
}
\]

More generally, if the shell activity migrates among finite radii, a diagonal replenishment statement is required.

Thus the escaping-tail endpoint is converted into a **finite-radius replenishment problem**.

---

## 13. Relation to the dilation conveyor

The previous `ANCIENT_CRITICAL_TAIL_DILATION_CONVEYOR` note showed that the passive critical tail obeys, to leading order,

\[
\partial_\theta V
+\frac12V
+\frac12y\cdot\nabla V
=0,
\]

so a critical shell moves outward by

\[
R\mapsto e^{\Delta\theta/2}R.
\]

Therefore recurrent activity at a fixed finite shell cannot be supplied forever by the same passive shell.

It requires one of:

1. inward-to-outward replenishment from smaller similarity radii;
2. non-passive remote dynamics;
3. nonlinear/diffusive shell regeneration.

These are precisely the mechanisms that must now be tied to the existing historical-recycling / remote / turnover ledgers.

---

## 14. What remains unproved

M5-561 does **not** yet prove that the passive-tail no-replenishment branch automatically satisfies fixed-shell evacuation.

The leading conveyor suggests it, but the exact Navier--Stokes tail equation contains nonlinear, pressure, and viscous remainders.

The next theorem-level task is therefore:

> Prove that, on the spectator-tail branch with no historical replenishment and no active remote coupling, the exact far-field remainder is integrable along the outward log-radius characteristics strongly enough to imply fixed-shell evacuation.

If this is achieved, the escaping-tail branch closes by the argument above.

---

## 15. Revised tail frontier

The global `L3` issue is now reduced to one precise implication:

\[
\boxed{
\text{passive critical conveyor}
+\text{no replenishment}
\stackrel{?}{\Longrightarrow}
\text{fixed-shell evacuation}.
}
\]

Combined with M5-561,

\[
\boxed{
\text{fixed-shell evacuation}
\Longrightarrow
\text{Liouville contradiction}.
}
\]

Thus the only surviving tail mechanism is recurrent finite-radius replenishment strong enough to defeat the outward conveyor.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
