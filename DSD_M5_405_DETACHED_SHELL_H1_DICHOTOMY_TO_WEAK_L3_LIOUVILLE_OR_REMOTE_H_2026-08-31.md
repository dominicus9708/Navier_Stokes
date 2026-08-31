# DSD M5-405 — Detached shell-H1 dichotomy: weak-L3 Liouville corridor or remote H

Date: 2026-08-31

Status: **A DETACHED ANCIENT SATELLITE DOES NOT REQUIRE AN INDEPENDENT RESTART ASSUMPTION ON THE CORRIDOR WHERE ITS OWN SCALE-CRITICAL GRADIENT SHELL ENERGY IS UNIFORMLY BOUNDED / THE DYADIC BOUND `sup_R R int_{A_R}|grad u|^2 <= M` IMPLIES `grad u in L^{3/2,infinity}` BY A DIRECT DISTRIBUTION-FUNCTION ESTIMATE, AND LORENTZ--SOBOLEV THEN GIVES `u-c in L^{3,infinity}` AFTER A GALILEAN CONSTANT / IF THE SHELL BOUND FAILS, FIXED-WINDOW CONVERGENCE TRANSFERS AN ARBITRARILY LARGE SHELL-H1 EVENT BACK TO THE PRELIMIT AND M5-280 ROUTES IT TO REMOTE SATELLITE/BOUNDARY ACTIVITY / ON THE UNIFORMLY BOUNDED-SHELL COMPLETE ANCIENT CORRIDOR, THE FIRST-HITTING VORTICITY CAP GIVES MILDNESS AND THE TERMINAL WEAK-L3 TRACE LIES IN THE ALBRITTON--BARKER SUBSPACE, SO THE NONTRIVIAL DETACHED PROFILE IS EXCLUDED / GLOBAL REGULARITY UNPROVED BECAUSE UNBOUNDED SHELL-H1 CAN RECURSE THROUGH REMOTE SCALES.**

---

## 1. Purpose

M5-284 identified a real firewall: local solenoidal truncation of a detached satellite does not by itself prove a coherent global weak-`L3` restart.

That firewall remains correct for a completely arbitrary detached local-energy profile.

However M5-280 already identifies the critical gradient-shell quantity whose escalation defines the static H/remote frontier.

This suggests an intrinsic dichotomy on the detached ancient profile itself:

1. its critical shell gradient energy is uniformly bounded;
2. or it is not.

On branch 1 a global weak-critical velocity bound can be derived directly, without replacing the actual detached evolution by a truncated comparison solution.

---

## 2. Detached ancient profile and shell quantity

Let

\[
u=u(x,t)
\]

be a smooth detached ancient satellite on

\[
\mathbb R^3\times(-\infty,0]
\]

with the point-picked nontrivial mark

\[
|\omega(0,0)|=1.
\]

For dyadic radii

\[
R_k=2^k,
\qquad k\ge0,
\]

let

\[
A_k=\{R_k\le|x|<2R_k\}.
\]

Define

\[
\boxed{
E_{1,k}(t)
:=
R_k\int_{A_k}|\nabla u(x,t)|^2dx.
}
\]

The quiet shell corridor is

\[
\boxed{
\sup_{t<0}\sup_{k\ge0}E_{1,k}(t)
\le M<\infty.
}
\]

The inner unit ball is controlled separately by the point-picked vorticity/ambient-strain compactness package; denote

\[
\sup_{t<0}
\|\nabla u(t)\|_{L^2(B_2)}
\le M_0
\]

on the retained no-local-H branch.

If this local bound itself fails, that is already a local derivative/ambient H route rather than the quiet detached corridor considered below.

---

## 3. Shell H1 bound implies weak `L^{3/2}` control of the gradient

Fix one time and write

\[
g=|\nabla u|.
\]

The shell bound gives

\[
\boxed{
\int_{A_k}g^2dx
\le
\frac{M}{R_k}.
}
\]

For any `lambda>0`, Chebyshev gives on each shell

\[
|\{x\in A_k:g(x)>\lambda\}|
\le
\min\left\{
C R_k^3,
\frac{M}{R_k\lambda^2}
\right\}.
\]

Choose the crossover radius

\[
R_*(\lambda)
:=
M^{1/4}\lambda^{-1/2}.
\]

For shells with `R_k <= R_*`, sum the volume bounds:

\[
\sum_{R_k\le R_*}
CR_k^3
\lesssim
R_*^3
=
M^{3/4}\lambda^{-3/2}.
\]

For shells with `R_k > R_*`, sum the Chebyshev bounds:

\[
\sum_{R_k>R_*}
\frac{M}{R_k\lambda^2}
\lesssim
\frac{M}{\lambda^2R_*}
=
M^{3/4}\lambda^{-3/2}.
\]

The inner ball contributes a standard finite local term controlled by `M0` and is absorbed into the same weak estimate after enlarging the constant.

Therefore

\[
\boxed{
|\{x:|\nabla u(x,t)|>\lambda\}|
\le
C(M,M_0)\lambda^{-3/2}.
}
\]

Equivalently,

\[
\boxed{
\nabla u(t)
\in
L^{3/2,\infty}(\mathbb R^3)
}
\]

with a bound uniform in `t<0` on the quiet shell corridor.

---

## 4. Lorentz--Sobolev gives weak `L3` velocity modulo a constant

The homogeneous Sobolev--Lorentz embedding in three dimensions gives, modulo spatial constants,

\[
\boxed{
\dot W^{1,(3/2,\infty)}
\hookrightarrow
L^{3,\infty}.
}
\]

Thus for every time there is a spatial constant vector `c(t)` such that

\[
\boxed{
\|u(t)-c(t)\|_{L^{3,\infty}}
\le
C\|\nabla u(t)\|_{L^{3/2,\infty}}
\le M_*.
}
\]

The constant is a Galilean gauge. Fix the detached frame by the same normalization used in the satellite compactness construction, or perform the time-dependent Galilean normalization on the retained ancient trajectory when compatible with the pressure gauge.

On the fixed normalized detached frame the conclusion is the required critical spatial bound

\[
\boxed{
\sup_{t<0}
\|u(t)\|_{L^{3,\infty}}
\le M_*.
}
\]

up to the chosen Galilean representative.

---

## 5. Scope firewall for the velocity gauge

The Lorentz--Sobolev theorem determines the velocity modulo constants, not modulo affine functions.

This is exactly appropriate:

- constant velocities are Galilean gauge;
- nonzero affine gradients are **not** gauge and are already routed by M5-403--404 to palinstrophy/enstrophy/remote H.

Thus no affine anti-model is silently removed by choosing `c(t)`.

If the constants needed at different ancient times cannot be chosen coherently with one Navier--Stokes Galilean frame, that failure is a drift/realization turnover defect and remains typed as T rather than being hidden in the weak-`L3` estimate.

---

## 6. If shell H1 is unbounded, it returns to the remote frontier

Suppose instead the detached limit satisfies

\[
\sup_{t<0,k}E_{1,k}(t)=\infty.
\]

Choose times and finite radii

\[
(t_m,R_m)
\]

such that

\[
E_1^{\infty}(R_m,t_m)\ge m.
\]

For each fixed pair `(R_m,t_m)`, smooth local convergence of the prelimit satellite sequence transfers the shell-gradient lower bound to a sufficiently late prelimit:

\[
E_{1,n_m}(R_m,t_m)\ge m/2.
\]

Therefore the original finite-energy sequence exhibits arbitrarily large critical shell-H1 events.

By M5-279--280 these route to

\[
\boxed{
T_{boundary/dynamic}
\lor
S_{remote}.
}
\]

Hence an unbounded-shell detached profile is not an independent ancient terminal.

---

## 7. Mildness on the bounded-shell branch

The point-picked detached profile has a global bounded-vorticity mark inherited on every fixed compact cylinder.

Together with the uniform weak-`L3` bound, the same local div--curl bootstrap used in M5-276 gives, on every compact negative-time slab

\[
[-B,-A]\Subset(-\infty,0),
\]

a global velocity bound

\[
\boxed{
\sup_{-B\le t\le-A}
\|u(t)\|_\infty
<\infty.
}
\]

Therefore the smooth detached solution belongs to the mild/Duhamel ancient class required by the imported Albritton--Barker theorem.

---

## 8. Terminal trace belongs to the Albritton--Barker subspace

The detached ancient solution is smooth up to the selected terminal satellite time `t=0`, so its actual terminal field

\[
T:=u(0)
\]

belongs to

\[
L^{3,\infty}.
\]

The standard embedding gives

\[
T\in\dot B^{-1}_{\infty,\infty}.
\]

Moreover for every compactly supported test function `phi`, Lorentz Holder gives

\[
|\langle T(\lambda\cdot),\phi\rangle|
\lesssim
\lambda^{-1}
\|T\|_{L^{3,\infty}}
\|\phi\|_{L^{3/2,1}}
\to0.
\]

Thus

\[
\boxed{T\in\mathbb B}
\]

in the notation of Albritton--Barker, and the required Besov distance is zero.

---

## 9. Liouville contradiction on the uniformly bounded-shell corridor

The detached ancient solution now has:

1. mild ancient Navier--Stokes structure;
2. a uniform weak-`L3` bound for all negative times, hence along every backward sequence;
3. terminal trace in `mathbb B`;
4. nonzero vorticity mark `|omega(0,0)|=1`.

The imported Albritton--Barker Liouville theorem therefore gives

\[
\boxed{u\equiv0,}
\]

contradicting the nonzero satellite mark.

Hence

\[
\boxed{
A_{detached}
+
\text{uniform shell-H1 bound}
+
\text{coherent Galilean frame}
\Longrightarrow
\bot.
}
\]

---

## 10. Reinterpret the old restart-coherence gap

M5-284 correctly shows that **local truncation alone** cannot put an arbitrary detached profile in the weak-`L3` solution class.

M5-405 does not use local truncation.

Instead it uses a stronger intrinsic no-H hypothesis on the actual detached solution:

\[
\sup_{t,R}R\int_{A_R}|\nabla u|^2<\infty.
\]

This global shell condition directly yields the weak-critical norm of the actual solution.

Thus the restart-coherence gap remains relevant only when the shell-critical control itself fails or when the Galilean constants cannot be coherently fixed.

---

## 11. DSD audit

### Derived

\[
\boxed{
\sup_R R\int_{A_R}|\nabla u|^2<\infty
\Longrightarrow
\nabla u\in L^{3/2,\infty}
\Longrightarrow
u-c\in L^{3,\infty}.
}
\]

### External/imported endpoint

- Albritton--Barker ancient Liouville theorem as already audited in M5-276/388.

### Firewall

- shell-H1 control must be uniform on the complete ancient corridor used for the common weak-`L3` bound;
- a time-incoherent velocity constant is a realization/drift T defect, not silently removed;
- if shell-H1 escalates, the result is H/remote routing, not a contradiction;
- no claim is made that every detached satellite automatically satisfies the bounded-shell hypothesis.

---

## 12. Updated detached frontier

The detached branch now has the sharper dichotomy

\[
\boxed{
A_{detached}
\Longrightarrow
H_{shell/remote}
\lor
T_{drift/realization}
\lor
\bot.
}
\]

where the contradiction is the uniform-shell weak-`L3` Liouville corridor.

Therefore a nontrivial detached survivor must continuously evade uniform critical shell control or coherent realization; it cannot remain a globally shell-critical quiet ancient profile.

---

## 13. Audit verdict

### CLOSED CONDITIONAL QUIET DETACHED CORRIDOR

\[
\boxed{
\sup_{t,R}R\int_{A_R}|\nabla u|^2<\infty
\Longrightarrow
\text{weak-}L3
\Longrightarrow
\text{Liouville contradiction}.
}
\]

### ROUTED IF THE CONDITION FAILS

\[
\boxed{
\text{shell-H1 escalation}
\Longrightarrow
S_{remote}\lor T_{dynamic}.
}
\]

### STILL OPEN

- an iterated remote/shell-H cascade;
- coherent treatment of time-dependent drift/realization defects;
- local critical frequency/direction action;
- projective/export exits;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
