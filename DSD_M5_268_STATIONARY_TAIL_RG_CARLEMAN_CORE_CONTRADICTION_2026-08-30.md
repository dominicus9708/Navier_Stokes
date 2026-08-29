# DSD M5-268 — Stationary-Tail RG Carleman / Smooth-Core Contradiction

Date: 2026-08-30

Parent: `DSD_M5_267_DESCENDANT_RADIUS_SCALING_CORRECTION_AND_SMALL_BALL_GATE_SCOPE_2026-08-30.md`

Status: **MAJOR STATIONARY-BRANCH CLOSURE ON THE AUDITED REALIZED-W1 CORRIDOR / M5-145 CANNOT BE APPLIED DIRECTLY BETWEEN A W1 STATE AND AN ARBITRARY STATIONARY REFERENCE, BUT M5-240 GIVES A DIFFERENT ROUTE: IF THE REALIZED CANONICAL TAIL IS STATIONARY, THE EXACT RG RECURSION FORCES EVERY POSITIVE RG JET OF THE REALIZED RECONSTRUCTION TO VANISH / AFTER REVERSING `rho` TO A FORWARD NAVIER--STOKES TIME, THE REALIZED RG PATH AND THE CONSTANT STATIONARY TAIL FORM EXACTLY THE LOCAL OSEEN DIFFERENCE SYSTEM USED IN M5-217 / ALL-ORDER RG FLATNESS ALLOWS ZERO EXTENSION AND THE SAME CARLEMAN WEIGHT-GAP ARGUMENT, FORCING EQUALITY ON A PRETERMINAL OPEN SET / SPATIAL ANALYTIC CONTINUATION AT AN INTERIOR RG TIME THEN IDENTIFIES THE REALIZED DESCENDANT WITH THE STATIONARY TAIL ON THE ENTIRE PUNCTURED SPACE / THE DESCENDANT IS SMOOTH AT THE SCALING CENTER, SO THE TAIL SINGULARITY IS REMOVABLE; THE RESULTING ENTIRE STATIONARY FIELD WITH `O(1/r)` VELOCITY, `O(1/r^2)` GRADIENT/PRESSURE DECAY HAS ZERO DIRICHLET ENERGY BY A CUTOFF ENERGY IDENTITY AND IS ZERO / THIS CONTRADICTS THE NONZERO HOMOGENEITY-DEFECT / CHECKPOINT TAIL WITNESS / THEREFORE THE NONZERO STATIONARY CRITICAL TAIL BRANCH IS EMPTY UNDER THE ESTABLISHED REALIZED-RG/FUCHSIAN/CARLEMAN PACKAGE / GLOBAL REGULARITY STILL UNPROVED BECAUSE THE RESIDUAL-ACTIVE APERIODIC BRANCH REMAINS.**

---

## 1. Scope correction from M5-145

M5-145 proves all-order terminal/Fuchsian equality for **two realized W1 states in the same minimal set with the same canonical tail**.

It does not permit the shortcut

\[
\text{W1 state }V
\quad\text{vs}\quad
\text{arbitrary stationary punctured reference }T
\]

unless that reference has separately been shown to be a realized W1 state.

Therefore the proposed direct physical-time comparison

\[
u_V-u_T=O((T^*-t)^N)\quad\forall N
\]

is not imported from M5-145.

The stationary branch is closed below by the exact RG equation instead.

---

## 2. Exact realized RG path

For a realized canonical tail `T=T_V`, M5-237 defines

\[
\mathscr R_\rho(T),\qquad 0<\rho\le1,
\]

with

\[
\mathscr R_0(T)=T
\]

in the punctured local topology and

\[
\boxed{
\partial_\rho\mathscr R_\rho
=-\nu\Delta\mathscr R_\rho
+\mathbb P\nabla\cdot
(\mathscr R_\rho\otimes\mathscr R_\rho).
}
\]

At `rho=1`,

\[
\mathscr R_1(T)=V
\]

up to the fixed normalization convention of M5-239.

The path is known to exist because `T` is a **realized** tail. No claim is made that arbitrary critical data admit such a backward-RG trajectory.

---

## 3. Stationarity kills every positive RG jet

Assume the stationary branch

\[
\boxed{\mathcal F(T)=0}
\]

where

\[
\mathcal F(U)
=\nu\Delta U
-\mathbb P\nabla\cdot(U\otimes U).
\]

M5-240 gives the triangular realized RG recursion

\[
\boxed{
(n+1)A_{n+1}
=-\nu\Delta A_n
+\sum_{i+j=n}\mathcal B(A_i,A_j),
\qquad A_0=T.
}
\]

The first coefficient is

\[
A_1=-\mathcal F(T)=0.
\]

If

\[
A_1=\cdots=A_n=0,
\]

then at order `n` every term on the right contains either `A_n` in the viscous term or at least one positive-order coefficient in the bilinear sum, except the `n=0` stationary combination already canceled by `F(T)=0`.

Hence

\[
A_{n+1}=0.
\]

By induction,

\[
\boxed{A_n=0\qquad\forall n\ge1.}
\]

Because M5-240 identifies these coefficients with the actual realized integer Fuchsian/RG jets, for every fixed punctured compact

\[
K\Subset\mathbb R^3\setminus\{0\},
\]

every finite spatial derivative order `k`, and every integer `N`,

\[
\boxed{
\|\mathscr R_\rho(T)-T\|_{C^k(K)}
=O_{K,k,N}(\rho^N)
\qquad(\rho\downarrow0).
}
\]

The corresponding pressure difference has the same all-order punctured flatness after fixing the canonical pressure gauge, by the same elliptic pressure/Fuchsian hierarchy already used in M5-145/M5-240.

This is a realized finite-jet statement. No convergence of a formal Taylor series is assumed.

---

## 4. Reverse the RG variable to ordinary Navier--Stokes time

Set

\[
\tau=-\rho\in[-1,0),
\qquad
U(\tau,x):=\mathscr R_{-\tau}(T)(x).
\]

Then

\[
\partial_\tau U
=\nu\Delta U
-\mathbb P\nabla\cdot(U\otimes U).
\]

Equivalently, for a pressure `P_U`,

\[
\boxed{
U_\tau-\nu\Delta U
+(U\cdot\nabla)U
+\nabla P_U=0,
\qquad \nabla\cdot U=0.
}
\]

The stationary tail `T` satisfies

\[
\boxed{
-\nu\Delta T
+(T\cdot\nabla)T
+\nabla P_T=0
}
\]

on the punctured space.

Thus `T` is a time-independent solution of the same standard Navier--Stokes evolution in `tau` away from the puncture.

---

## 5. Exact Oseen difference equation

Let

\[
W(\tau,x):=U(\tau,x)-T(x),
\qquad
q:=P_U-P_T.
\]

Then on every fixed bounded smooth

\[
\Omega\Subset\mathbb R^3\setminus\{0\}
\]

one has

\[
\boxed{
W_\tau-\nu\Delta W
+(U\cdot\nabla)W
+(W\cdot\nabla)T
+\nabla q=0,
\qquad
\nabla\cdot W=0.
}
\]

This is exactly the Bellassoued--Imanuvilov--Yamamoto / M5-217 linearized Navier--Stokes form with

\[
A=U,
\qquad
B=T.
\]

Although `T` may be singular at the origin, on fixed `Omega` both `U` and `T` and all coefficient derivatives required by the local Carleman theorem are smooth and bounded up to `tau=0`.

Therefore the origin singularity is irrelevant to the **local punctured Carleman step**.

---

## 6. All-order flatness permits zero extension through `tau=0`

Section 3 gives

\[
\boxed{
\|W(\tau)\|_{C^k(K)}
=O_{K,k,N}(|\tau|^N)
\quad\forall N.
}
\]

The pressure difference is flat to the corresponding finite orders as well.

Define

\[
\widetilde W(\tau,x)
=
\begin{cases}
W(\tau,x),&\tau<0,\\
0,&\tau\ge0,
\end{cases}
\]

and choose the pressure gauge so that

\[
\widetilde q=0\qquad(\tau\ge0).
\]

All-order punctured flatness removes every distributional jump term at `tau=0`.

The coefficient `U` can be extended through `tau=0` on `Omega` by setting

\[
U(0,\cdot)=T
\]

and continuing smoothly for positive `tau` locally if needed only for the Carleman coefficient field.

Hence the zero-extended pair is a smooth local Oseen pair through the interior time slice `tau=0` in precisely the sense used in M5-217.

---

## 7. Reuse the M5-217 Carleman level-gap construction

Use the regular weight

\[
\varphi(\tau,x)
=
\exp\{\lambda[d(x)-\beta\tau^2]\}
\]

with interior time center `tau=0`, and choose the same nested levels

\[
\mu_3<\mu_4<\mu_5.
\]

Set the cutoff as a function of the Carleman weight,

\[
\chi
=\bar\chi\!\left(
\frac{\varphi-\mu_3}{\mu_4-\mu_3}
\right).
\]

Exactly as in M5-217:

- every cutoff source lies where `phi<=mu4`;
- the target lies where `phi>=mu5`;
- artificial spatial and temporal boundaries can be placed where the localized pair vanishes;
- the external linearized-Navier--Stokes Carleman estimate allows the cutoff forcing and nonzero cutoff divergence.

Therefore

\[
c(s)e^{2s\mu_5}
\|W\|_{L^2(D_5)}^2
\le
CM_\chi^2e^{2s\mu_4}.
\]

Letting `s->infinity`,

\[
\boxed{W=0\quad\text{on a nonempty open set }D_5\cap\{\tau<0\}.}
\]

No smallness of `T` is used; only bounded coefficient control on the fixed punctured Carleman domain is needed.

---

## 8. Spatial continuation at one interior RG time

Choose an interior time

\[
\tau_1<0
\]

for which the open Carleman target has a nonempty spatial slice.

Then

\[
U(\tau_1,x)=T(x)
\]

on a nonempty spatial open set away from the origin.

At finite positive RG depth `rho_1=-tau_1>0`, the realized descendant `U(tau1)` is a smooth Navier--Stokes/Leray descendant on the whole normalized space.

Both `U(tau1)` and the stationary solution `T` are spatially real analytic on the connected punctured domain

\[
\mathbb R^3\setminus\{0\}
\]

under the retained smooth parabolic/elliptic regularity.

Therefore ordinary analytic continuation gives

\[
\boxed{
U(\tau_1,x)=T(x)
\qquad\forall x\ne0.
}
\]

Equivalently, one may propagate the local equality through overlapping regular punctured domains by the same local unique-continuation architecture; no statement across the singular point is used in this step.

---

## 9. The stationary puncture is removable because the realized descendant is smooth there

The finite-depth descendant `U(tau1)` is smooth at the scaling center `x=0`.

Since

\[
T(x)=U(\tau_1,x)
\quad(x\ne0),
\]

`T` has a smooth extension through the origin:

\[
\boxed{T_{ext}(0):=U(\tau_1,0).}
\]

All derivatives extend as well because the two fields agree on the punctured neighborhood.

Thus the point-force defect from the previous stationary-tail analysis vanishes for this realized stationary tail:

\[
\boxed{b=0.}
\]

The pressure gradient is likewise smooth through the origin after fixing its additive constant, because the stationary velocity equation determines `grad P` from smooth velocity data.

Hence `T_ext` is an entire smooth stationary Navier--Stokes field.

---

## 10. Entire smooth `O(1/r)` stationary field is zero by the cutoff energy identity

The canonical critical-tail regularity gives at infinity

\[
|T(x)|\le \frac{C}{|x|},
\qquad
|\nabla T(x)|\le\frac{C}{|x|^2},
\qquad
|P_T(x)|\le\frac{C}{|x|^2}
\]

for sufficiently large `|x|` on the retained smooth tail class.

Let `chi_R` be a standard radial cutoff equal to one on `B_R`, zero outside `B_{2R}`, with

\[
|\nabla\chi_R|\lesssim R^{-1},
\qquad
|\Delta\chi_R|\lesssim R^{-2}.
\]

Multiply

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P_T=0
\]

by `chi_R T` and integrate over `R3`.

After the standard integrations by parts,

\[
\nu\int\chi_R|\nabla T|^2
\]

is bounded by cutoff-annulus terms of the forms

\[
\nu\int_{A_R}|\nabla T|\,|T|\,|\nabla\chi_R|,
\]

\[
\int_{A_R}|T|^3|\nabla\chi_R|,
\]

and

\[
\int_{A_R}|P_T|\,|T|\,|\nabla\chi_R|.
\]

Using the critical decay and `|A_R|~R^3`, each is `O(R^-1)`:

\[
R^3(R^{-2})(R^{-1})(R^{-1})=O(R^{-1}),
\]

\[
R^3(R^{-3})(R^{-1})=O(R^{-1}),
\]

\[
R^3(R^{-2})(R^{-1})(R^{-1})=O(R^{-1}).
\]

Let `R->infinity`. Then

\[
\boxed{
\nu\int_{\mathbb R^3}|\nabla T|^2dx=0.
}
\]

Thus `T` is constant, and the `O(1/r)` decay forces

\[
\boxed{T\equiv0.}
\]

This argument needs no large-amplitude stationary classification theorem.

---

## 11. Contradiction with the nontrivial stationary-tail branch

The stationary endpoint was formed from the surviving aperiodic/minimal tail branch carrying a nonzero scale-phase/homogeneity witness, e.g.

\[
\underline{\mathscr R}_H(T)>0
\]

or, on the earlier checkpoint route, a nonzero inherited vorticity witness.

But Section 10 gives

\[
T\equiv0.
\]

Therefore

\[
\boxed{
S_{crit}^{nonhom}=\varnothing
}
\]

on the audited realized W1 corridor.

More generally, any **nonzero realized stationary canonical tail** is excluded by the same RG-flatness + local Carleman + smooth-core argument.

---

## 12. Why this does not prove global regularity

M5-220 split the aperiodic minimal tail problem into

\[
R_{tail}\lor S_{crit}^{nonhom}.
\]

M5-268 closes the stationary side

\[
\boxed{S_{crit}^{nonhom}=\varnothing.}
\]

The surviving endpoint is therefore the genuinely residual-active realized tail hull:

\[
\boxed{
\mathbf F(T)\ge\varepsilon_{glob}>0
\quad\text{on the compact minimal tail hull}.
}
\]

M5-237/M5-240 show that such a tail has a unique formal all-order descendant hierarchy and at least one realized backward-RG completion, but no theorem yet excludes the aperiodic residual-active range.

Thus global regularity remains unproved.

---

## 13. DSD verdict

### GREEN

- M5-145 scope correction: it is not misapplied to an arbitrary stationary reference.
- exact RG equation and `tau=-rho` conversion to standard Navier--Stokes evolution.
- stationarity forces every positive realized RG jet to vanish.
- fixed-punctured-domain Oseen coefficient regularity.
- M5-217 Carleman weight-gap reuse.
- smooth-core removability after equality with a finite-depth realized descendant.
- cutoff-energy Liouville argument for the resulting entire `O(1/r)` stationary field.

### CLOSED

\[
\boxed{\text{nonzero realized stationary critical-tail branch}.}
\]

### OPEN

\[
\boxed{\text{residual-active aperiodic minimal realized tail hull}.}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
