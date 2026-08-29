# DSD M5-274 — Global-`rho` RG Extension and Nonlinear Stretching Necessity

Date: 2026-08-30

Parent: `DSD_M5_273_PINEAU_VICOL_WEIGHTED_ENSTROPHY_INVARIANT_MEAN_GENERALIZATION_AUDIT_2026-08-30.md`

Status: **GLOBAL-RG RANGE UPGRADE / ON THE RETAINED COMPLETE RECURRENT W1 ORBIT, THE DESCENDANT/RG RECONSTRUCTION IS NOT MERELY A FINITE BACKWARD-PARABOLIC SEGMENT `0<rho<=1`: THE SAME EXACT DEFINITION EXTENDS TO EVERY `rho>0` USING NEGATIVE LERAY TIMES / AFTER `tau=-rho`, THIS IS AN ANCIENT SMOOTH NAVIER--STOKES EVOLUTION ON `(-infinity,0)` WITH TYPE-I BOUND `|U(x,tau)|<=C/(sqrt(-tau)+|x|)` AND LOCAL DECAY TO ZERO AS `tau->-infinity` / ITS GLOBAL VORTICITY IS L2 FOR EVERY `rho>0` AND OBEYS A BACKWARD-RG ENSTROPHY IDENTITY / THE LINEAR BACKWARD-HEAT ANTI-MODEL OF M5-241 IS THEREFORE ELIMINATED AS A MODEL OF THE FULL REALIZED RANGE: A NONZERO GLOBAL-RG SURVIVOR MUST HAVE STRICT NET VORTEX-STRETCHING PAYMENT THAT OVERCOMES BACKWARD VISCOSITY / THIS PAYMENT IS EXACTLY THE EXPONENTIALLY WEIGHTED PAST FORM OF THE LERAY H0 RECURRENCE TAX, SO IT IS A STRUCTURAL NARROWING RATHER THAN A NEW CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Complete W1 orbit

The W1 recurrent/minimal state is obtained from an eternal time-translate limit of the autonomous Leray flow. On the retained recurrent corridor one has a complete smooth trajectory

\[
S(h)V,
\qquad
h\in\mathbb R,
\]

remaining in the compact W1 class.

M5-237 defined the descendant for `h>=0` by

\[
\mathcal D_h[V](Y)
=e^{h/2}(S(h)V)(e^{h/2}Y)
\]

and set

\[
\rho=e^{-h}.
\]

Nothing in the algebraic definition fails for finite negative `h` as long as the complete W1 orbit exists.

Therefore define for **all** `rho>0`

\[
\boxed{
\mathscr R_\rho(T_V)(Y)
:=
\rho^{-1/2}
\bigl(S(-\log\rho)V\bigr)
\left(\rho^{-1/2}Y\right).
}
\]

For `0<rho<=1` this agrees with M5-237/M5-239.

At `rho=1`,

\[
\mathscr R_1(T_V)=V.
\]

---

## 2. Exact RG equation remains valid globally

The differentiation in M5-237 is local in `h` and uses only the Leray equation and scaling.

Hence for every `rho>0`,

\[
\boxed{
\partial_\rho\mathscr R_\rho
=-\nu\Delta\mathscr R_\rho
+\mathbb P\nabla\cdot
(\mathscr R_\rho\otimes\mathscr R_\rho).
}
\]

Thus the realized tail belongs not merely to a finite-time backward-RG range, but to the **global positive-`rho` range** of this anti-parabolic evolution.

This statement uses the complete recurrent W1 orbit; it is not asserted for arbitrary tails outside the realized class.

---

## 3. Standard Navier--Stokes time `tau=-rho`

Set

\[
\tau=-\rho<0,
\qquad
U(Y,\tau):=\mathscr R_{-\tau}(T)(Y).
\]

Then

\[
\boxed{
U_\tau-\nu\Delta U
+(U\cdot\nabla)U
+\nabla P=0,
\qquad
\nabla\cdot U=0,
}
\]

for every

\[
\tau\in(-\infty,0).
\]

Thus every realized canonical tail determines an **ancient smooth Navier--Stokes solution** in the RG/physical variable `tau`.

The terminal trace at `tau=0` is the critical tail `T` on the punctured space.

---

## 4. Global Type-I bound along the RG ancient solution

On the compact W1 corridor assume the retained spatial Type-I bound

\[
|S(h)V(X)|
\le
\frac{C_*}{1+|X|}
\]

uniformly in `h`.

Using the global descendant formula,

\[
\begin{aligned}
|\mathscr R_\rho(T)(Y)|
&\le
\rho^{-1/2}
\frac{C_*}{1+|Y|/\sqrt\rho}\\
&=
\boxed{
\frac{C_*}{\sqrt\rho+|Y|}.
}
\end{aligned}
\]

Equivalently,

\[
\boxed{
|U(Y,\tau)|
\le
\frac{C_*}{\sqrt{-\tau}+|Y|},
\qquad \tau<0.
}
\]

The derivative Type-I hierarchy similarly gives

\[
|\nabla^kU(Y,\tau)|
\lesssim
(\sqrt{-\tau}+|Y|)^{-k-1}
\]

on the audited smooth corridor.

---

## 5. Local decay as `tau -> -infinity`

For every fixed compact `K`,

\[
\sup_{Y\in K}|U(Y,\tau)|
\le
C_K(-\tau)^{-1/2}
\to0
\]

as

\[
\tau\to-\infty.
\]

Thus

\[
\boxed{
U(\cdot,\tau)\to0
\quad\text{locally uniformly as }\tau\to-\infty.
}
\]

This does not imply global finite-energy decay because every RG state retains a critical `1/r` far tail.

---

## 6. Vorticity scaling and global enstrophy

Let

\[
\Xi_\rho:=\nabla\times\mathscr R_\rho(T).
\]

From the scaling formula,

\[
\boxed{
\Xi_\rho(Y)
=\rho^{-1}
\Omega_V\left(\rho^{-1/2}Y,-\log\rho\right).
}
\]

Since the W1 vorticity decays as `|X|^-2` at infinity and is smooth at the core, it belongs to `L2(R3)`.

Therefore

\[
\boxed{
Z_R(\rho)
:=\|\Xi_\rho\|_2^2
=\rho^{-1/2}
Z_V(-\log\rho),
}
\]

where

\[
Z_V(s)=\|\Omega_V(s)\|_2^2.
\]

Compact recurrent boundedness of `Z_V` implies

\[
\boxed{
Z_R(\rho)\to0
\qquad(\rho\to\infty).
}
\]

---

## 7. Backward-RG vorticity equation

Taking curl of

\[
\partial_\rho R
=-\nu\Delta R+(R\cdot\nabla)R+\nabla q
\]

gives

\[
\boxed{
\partial_\rho\Xi
=-\nu\Delta\Xi
+(R\cdot\nabla)\Xi
-(\Xi\cdot\nabla)R.
}
\]

Pair with `Xi` in `L2`. The transport term cancels by incompressibility. Hence

\[
\boxed{
\frac12 Z_R'(\rho)
=\nu Q_R(\rho)-\mathcal P_R(\rho),
}
\]

where

\[
Q_R:=\|\nabla\Xi\|_2^2,
\]

and

\[
\mathcal P_R
:=\int\Xi^TS_R\Xi\,dY,
\qquad
S_R=\operatorname{sym}\nabla R.
\]

The sign is the reverse of ordinary forward-time enstrophy: in the backward-RG direction viscosity is destabilizing.

---

## 8. Integrate to global `rho=infinity`

Since

\[
Z_R(\infty)=0,
\]

integrating Section 7 from `rho0` to infinity gives

\[
-\frac12Z_R(\rho_0)
=
\int_{\rho_0}^{\infty}
\left(
\nu Q_R-\mathcal P_R
\right)d\rho.
\]

Therefore

\[
\boxed{
\int_{\rho_0}^{\infty}
\left(
\mathcal P_R-\nu Q_R
\right)d\rho
=
\frac12 Z_R(\rho_0)>0
}
\]

for every nonzero realized state.

Thus a nontrivial global-RG path requires strict integrated vortex stretching in excess of the backward-viscous growth term.

---

## 9. Linear backward heat anti-model is eliminated globally

If the nonlinear stretching term were absent, then

\[
\mathcal P_R\equiv0
\]

and

\[
Z_R'(\rho)=2\nu Q_R\ge0.
\]

A nonnegative nondecreasing function of `rho` cannot tend to zero as `rho->infinity` unless it is identically zero.

Therefore

\[
\boxed{
\text{global backward-heat realization}
+Z_R(\infty)=0
\Longrightarrow
Z_R\equiv0.
}
\]

The finite-interval quasiperiodic backward-heat construction of M5-241 remains a valid **finite-range** anti-model, but it cannot model the full realized recurrent W1 range after the global-`rho` extension.

Thus any surviving residual-active tail is essentially nonlinear.

---

## 10. Relation to the ordinary Leray H0 recurrence tax

Use

\[
\rho=e^{-s}.
\]

The scalings are

\[
Z_R(\rho)=\rho^{-1/2}Z_V(s),
\]

\[
Q_R(\rho)=\rho^{-3/2}Q_V(s),
\]

and

\[
\mathcal P_R(\rho)=\rho^{-3/2}\mathcal P_V(s).
\]

Since

\[
d\rho=-\rho ds,
\]

Section 8 is equivalent to

\[
\boxed{
\frac12 Z_V(s_0)
=
\int_{-\infty}^{s_0}
 e^{-(s_0-s)/2}
\left(
\mathcal P_V(s)-\nu Q_V(s)
\right)ds.
}
\]

Differentiating this Volterra identity recovers

\[
\boxed{
\frac12Z_V'
+\frac14Z_V
+\nu Q_V
=\mathcal P_V,
}
\]

which is exactly the known Leray H0 enstrophy balance.

Thus the global-RG argument does not create a new independent budget; it gives a new **range interpretation** of the same tax.

---

## 11. Consequence for the residual-active endpoint

After M5-268 closes stationary tails and M5-270 closes the naive critical-budget contradiction, the survivor now has the stronger range certificate:

\[
\boxed{
\begin{array}{c}
\text{nonstationary critical terminal trace }T,\\
\mathbf F(T)\ge\varepsilon_{glob},\\
\text{global backward-RG reconstruction for every }\rho>0,\\
\mathscr R_\rho(T)\to0\text{ locally as }\rho\to\infty,\\
\int_{\rho_0}^{\infty}(\mathcal P_R-\nu Q_R)d\rho
=\frac12Z_R(\rho_0)>0.
\end{array}
}
\]

The branch cannot be supported by a linear or passive mechanism. Persistent three-dimensional vortex stretching is mandatory.

---

## 12. DSD verdict

### NEW GREEN STRUCTURE

The realized backward-RG path is global in positive `rho` on the complete W1 recurrent corridor.

### CLOSED AS A FULL-RANGE MODEL

The linear backward-heat/quasiperiodic anti-model from M5-241.

### NOT CLOSED

The nonlinear global-RG ancient Type-I solution itself. Its stretching surplus is critically scaled and is exactly the previously known H0 recurrent production tax.

The next target should exploit a **second level** of the global-RG hierarchy or a nonlinear spectral/non-normality inequality; another H0 lower bound would be redundant.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
