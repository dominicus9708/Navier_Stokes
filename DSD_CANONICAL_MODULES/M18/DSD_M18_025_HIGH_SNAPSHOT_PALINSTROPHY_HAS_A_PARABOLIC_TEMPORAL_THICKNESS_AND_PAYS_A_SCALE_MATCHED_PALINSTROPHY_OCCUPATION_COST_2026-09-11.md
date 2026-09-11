# M18-025 — High snapshot palinstrophy has a parabolic temporal thickness and pays a scale-matched palinstrophy occupation cost

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / PALINSTROPHY SPIKE THICKENING / ANCESTRY THRESHOLD

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-024 reduced the full combined strain/geometry source square to

\[
R_\phi
\lesssim
P^{5/4}J_3^{3/4},
\]

where

\[
P(t):=\|\nabla\Omega(t)\|_2^2,
\qquad
J_3(t):=\|D^3\Omega(t)\|_2^2.
\]

Since the D3 spacetime resource is already finite, the newly exposed standard exit is

\[
\sup_I P(t)\to\infty.
\]

This module asks whether a large palinstrophy snapshot can be arbitrarily thin in time.

The answer is no on a same-branch smooth window: the Navier--Stokes equation gives a scale-matched one-sided growth inequality

\[
P'\lesssim \nu^{-1/3}P^{5/3},
\]

so a doubling to height \(p\) requires time \(\gtrsim\nu^{1/3}p^{-2/3}\) and therefore pays spacetime palinstrophy \(\gtrsim\nu^{1/3}p^{1/3}\).

## 2. Vorticity equation

For incompressible Navier--Stokes on \(\mathbb R^3\),

\[
\partial_t\Omega+(u\cdot\nabla)\Omega
=(\Omega\cdot\nabla)u+
u\Delta\Omega.
\]

Set

\[
P(t):=\int|\nabla\Omega|^2dx,
\qquad
H(t):=\int|D^2\Omega|^2dx.
\]

Differentiate \(P\) in time. After integrating the transport derivative by parts and using \(\nabla\cdot u=0\), one obtains

\[
\frac12P'(t)+\nu H(t)
=I_1+I_2+I_3,
\]

where the three nonlinear terms have the schematic forms

\[
I_1\sim\int \nabla u\,\nabla\Omega\,\nabla\Omega,
\]

\[
I_2\sim\int \nabla u\,\nabla\Omega\,\nabla\Omega,
\]

and

\[
I_3\sim\int \Omega\,D^2u\,\nabla\Omega.
\]

No CE-H assumption is needed for this standard whole-space estimate.

## 3. Scale-correct nonlinear bound

Calderon--Zygmund and Sobolev estimates give

\[
\|\nabla u\|_6
\lesssim
\|\Omega\|_6
\lesssim
\|\nabla\Omega\|_2
=P^{1/2},
\]

and

\[
\|D^2u\|_{12/5}
\lesssim
\|\nabla\Omega\|_{12/5}.
\]

Interpolation between \(L^2\) and \(L^6\) gives

\[
\|\nabla\Omega\|_{12/5}
\lesssim
\|\nabla\Omega\|_2^{3/4}
\|D^2\Omega\|_2^{1/4}
=
P^{3/8}H^{1/8}.
\]

Therefore every nonlinear term obeys

\[
|I_j|
\lesssim
P^{1/2}
\left(P^{3/8}H^{1/8}\right)^2
=
P^{5/4}H^{1/4}.
\]

Hence

\[
\boxed{
P'+2\nu H
\le
C P^{5/4}H^{1/4}.
}
\]

The scaling is exact: both sides scale as \(R^5\) instantaneously.

## 4. Absorb the second-derivative term

Young's inequality with exponents \(4\) and \(4/3\) gives

\[
C P^{5/4}H^{1/4}
\le
\nu H
+C_\nu P^{5/3},
\]

with

\[
C_\nu\asymp \nu^{-1/3}
\]

up to a universal constant.

Thus

\[
\boxed{
P'(t)
\le
C\nu^{-1/3}P(t)^{5/3}.
}
\]

This is a one-sided upward-growth bound. It does not say that palinstrophy must grow; it says only that upward growth cannot be faster than the displayed parabolic rate.

## 5. Doubling-time theorem

Suppose on a smooth same-branch interval \([t_1,t_2]\),

\[
P(t_1)=\frac p2,
\qquad
P(t_2)=p,
\]

and

\[
\frac p2\le P(t)\le p
\qquad(t_1\le t\le t_2).
\]

From Section 4,

\[
\frac{dP}{dt}
\le
K_\nu P^{5/3},
\qquad
K_\nu=C\nu^{-1/3}.
\]

Therefore

\[
t_2-t_1
\ge
\int_{p/2}^{p}
\frac{dP}{K_\nu P^{5/3}}.
\]

The integral is explicit:

\[
\boxed{
 t_2-t_1
\ge
c\nu^{1/3}p^{-2/3},
}
\]

for a universal \(c>0\).

The dimensionless combination

\[
\boxed{
p^{2/3}(t_2-t_1)}
\]

is invariant under the Navier--Stokes scaling; \(\nu\) is itself scaling invariant.

Thus the temporal thickness is exactly parabolic-scale matched.

## 6. Spacetime palinstrophy payment

Throughout the crossing interval,

\[
P(t)\ge\frac p2.
\]

Hence

\[
\int_{t_1}^{t_2}P(t)dt
\ge
\frac p2(t_2-t_1).
\]

Using Section 5,

\[
\boxed{
\int_{t_1}^{t_2}P(t)dt
\ge
c\nu^{1/3}p^{1/3}.
}
\]

Therefore a large palinstrophy spike cannot be created for free: reaching height \(p\) from below \(p/2\) forces a scale-matched palinstrophy spacetime cost.

## 7. Endpoint version with a finite backward window

Let \(t_*\) be a selected endpoint with

\[
P(t_*)=p.
\]

Assume a backward same-branch window of length \(\tau>0\).

There are two cases.

### A. Persistent-high case

If

\[
P(t)>\frac p2
\]

throughout the full backward window, then

\[
\boxed{
q^P
:=
\int_{t_* -\tau}^{t_*}P(t)dt
\ge
\frac p2\tau.
}
\]

### B. Crossing case

Otherwise there is a last time \(t_1\) in the window with

\[
P(t_1)=\frac p2.
\]

The subsequent rise to \(p\) obeys Section 6, so

\[
\boxed{
q^P
\ge
c\nu^{1/3}p^{1/3}.
}
\]

Combining the two cases,

\[
\boxed{
q^P
\gtrsim
\min\left\{
p\tau,
\nu^{1/3}p^{1/3}
\right\}.
}
\]

This is the recordwise endpoint palinstrophy-payment theorem.

## 8. Ancestry test

Palinstrophy spacetime charges carry the established ancestry weight

\[
R_m^{-1}.
\]

Therefore selected record endpoints with heights \(p_m\), backward windows \(\tau_m\), and non-reusable genealogy would contradict the finite palinstrophy ledger if

\[
\boxed{
\sum_m
R_m^{-1}
\min\left\{
p_m\tau_m,
\nu^{1/3}p_m^{1/3}
\right\}
=\infty.
}
\]

This is the exact closure test supplied by the present module.

A large snapshot by itself is still insufficient. It must be combined with the ancestry weight and non-reuse conditions.

## 9. Pointwise growth threshold

If the crossing alternative dominates and one asks for a single-record charge comparable to the inverse ancestry weight, then

\[
R_m^{-1}p_m^{1/3}\gtrsim1
\]

requires roughly

\[
\boxed{
p_m\gtrsim R_m^3.}
\]

This cubic threshold is exactly the snapshot scaling of palinstrophy,

\[
P_R=R^3P.
\]

Thus the ancestry threshold and the PDE temporal-thickness law are scale consistent.

Sub-cubic growth of normalized endpoint palinstrophy can remain ancestry summable even if \(p_m\to\infty\).

## 10. Optional raw-H2 concentration inequality

Before Young absorption, Section 3 also gives information on the raw second-derivative resource during a crossing.

Let

\[
\Delta t:=t_2-t_1.
\]

Since

\[
\frac p2
\le
C p^{5/4}
\int_{t_1}^{t_2}H(t)^{1/4}dt,
\]

Holder gives

\[
\int_{t_1}^{t_2}H^{1/4}dt
\le
(\Delta t)^{3/4}
\left(\int_{t_1}^{t_2}Hdt\right)^{1/4}.
\]

Hence

\[
\boxed{
\int_{t_1}^{t_2}H(t)dt
\gtrsim
p^{-1}(\Delta t)^{-3}.
}
\]

Thus an attempted crossing much faster than the natural parabolic time must pay a rapidly growing raw-H2 cost.

This is a concentration alternative, not an independent contradiction by itself.

## 11. Updated interpretation of M18-024 source exit

M18-024 left

\[
P_I^*=\sup_IP
\to\infty
\]

as the source-square escape.

M18-025 refines it:

\[
\boxed{
\begin{aligned}
G_{\rm high\ snapshot\ palinstrophy}
\Longrightarrow{}&
G_{\rm palinstrophy\ time\ occupation}\\
&\lor G_{\rm raw-H2\ fast\ crossing\ concentration}\\
&\lor G_{\rm backward\ same\text{-}branch/genealogy\ window\ loss}.
\end{aligned}
}
\]

The first branch has the direct \(R^{-1}\) ancestry test in Section 8.

## 12. DSD audit verdict

### Certified

1. High palinstrophy cannot rise arbitrarily fast on a smooth whole-space Navier--Stokes branch.
2. The scale-correct differential inequality is
   \[
   P'\lesssim\nu^{-1/3}P^{5/3}.
   \]
3. A \(p/2\to p\) crossing requires
   \[
   \Delta t\gtrsim\nu^{1/3}p^{-2/3}.
   \]
4. The crossing pays
   \[
   \int Pdt\gtrsim\nu^{1/3}p^{1/3}.
   \]
5. The recordwise ancestry closure test is
   \[
   \sum_mR_m^{-1}
   \min\{p_m\tau_m,\nu^{1/3}p_m^{1/3}\}=\infty.
   \]

### Not certified

1. That the above series diverges on the retained genealogy.
2. A record-uniform backward window.
3. A non-reuse/bounded-multiplicity certificate for all selected spikes.
4. Elimination of normalized collar-gradient concentration.
5. Global 3D Navier--Stokes regularity.

## 13. Next target

The two most useful remaining local exits are now:

\[
\Gamma_{\mathcal K}
=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}
\to\infty
\]

and ancestry-subthreshold high-palinstrophy spikes.

M18-026 should first test whether large \(\Gamma_{\mathcal K}\) can be thickened spatially by an adapted normalized-gradient profile, or whether its only escape is a new second-coefficient-jet/critical-level concentration already covered by M18-018--019.
