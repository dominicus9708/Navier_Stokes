# DSD M5-217 — Linearized Navier–Stokes Carleman Match and Flat-Fiber Closure

Date: 2026-08-29

Parent: `DSD_M5_216_ZERO_EXTENSION_CENTERED_CARLEMAN_GEOMETRY_2026-08-29.md`

Status: **MAJOR POSITIVE CLOSURE INSIDE THE AUDITED W1 SAME-TAIL CORRIDOR / THE EXISTING REGULAR-WEIGHT CARLEMAN ESTIMATE OF BELLASSOUED–IMANUVILOV–YAMAMOTO APPLIES TO THE EXACT LOCAL LINEARIZED NAVIER–STOKES FORM OF THE ZERO-EXTENDED SAME-TAIL DIFFERENCE AND ALLOWS BOTH AN INHOMOGENEOUS SOURCE `F` AND NONZERO DIVERGENCE `h` / CHOOSING THE CUTOFF AS A FUNCTION OF THE CARLEMAN WEIGHT PLACES EVERY CUTOFF SOURCE STRICTLY BELOW THE TARGET WEIGHT LEVEL / THE RESULTING EXPONENTIAL GAP FORCES THE DIFFERENCE TO VANISH ON A NONEMPTY PRETERMINAL SPACETIME OPEN SET / THE PREVIOUS M5-183 ANALYTIC-CONNECTIVITY BRIDGE THEN IDENTIFIES THE TWO SAME-TAIL REALIZATIONS / THUS THE FUCHSIAN-FLAT SAME-TAIL FIBER `P1_B` IS CLOSED UNDER THE ESTABLISHED W1 LOCAL SMOOTHNESS AND ALL-ORDER TERMINAL-FLATNESS PACKAGE / THIS DOES NOT BY ITSELF PROVE GLOBAL REGULARITY.**

---

## 1. External Carleman theorem matched here

Bellassoued–Imanuvilov–Yamamoto consider the nonstationary linearized Navier–Stokes system

\[
\boxed{
\partial_t v
-\kappa\Delta v
+(A\cdot\nabla)v
+(v\cdot\nabla)B
+\nabla p
=F,
}
\]

with

\[
\boxed{\nabla\cdot v=h.}
\]

For a regular weight

\[
\varphi=e^{\lambda(d(x)-\beta(t-t_0)^2)},
\]

they prove a Carleman estimate for `(v,p)` on a bounded spacetime domain `D`.

The estimate controls, schematically,

\[
\boxed{
\begin{aligned}
\|(v,p)\|_{X_s(D)}^2
\le C&\int_D |F|^2e^{2s\varphi}
+C\int_D\bigl(|h|^2+|\nabla_{x,t}h|^2\bigr)e^{2s\varphi}\\
&+\text{boundary/Cauchy terms},
\end{aligned}
}
\]

where the positive norm `X_s` contains in particular coercive terms of the form

\[
s^2|v|^2,
\quad
|\nabla v|^2,
\quad
s^{-2}|\partial_tv|^2,
\quad
|\nabla^2v|^2,
\quad
s|p|^2,
\quad
s^{-1}|\nabla p|^2
\]

(up to the theorem's normalization).

The theorem is specifically for the Oseen/linearized-Navier–Stokes structure already present here, not merely for the heat equation.

Boulakia's nonstationary-Stokes paper independently uses the same regular weight architecture and explicitly constructs nested weight levels for local propagation.

---

## 2. Current same-tail local equation is exactly of this form

Let `V,W` be two states in the same audited W1 canonical-tail fiber and let

\[
Z=u^V-u^W,
\qquad
q=p^V-p^W
\]

be their aligned physical realizations near the common terminal event `(x_*,T_*)`.

Fix any regular point

\[
x_0\ne x_*
\]

and a bounded smooth domain

\[
\Omega\Subset\mathbb R^3\setminus\{x_*\}
\]

containing `x0`.

For `t<T_*`,

\[
\boxed{
Z_t-\nu\Delta Z
+(u^V\cdot\nabla)Z
+(Z\cdot\nabla)u^W
+\nabla q=0,
\qquad
\nabla\cdot Z=0.
}
\]

Thus in the external theorem notation,

\[
\boxed{
A=u^V,
\qquad
B=u^W,
\qquad
\kappa=\nu.
}
\]

On the fixed punctured domain `Omega`, both coefficient fields extend smoothly and boundedly to `T_*`.

Hence all local coefficient regularity assumptions of the Carleman theorem are satisfied after shrinking the time interval if necessary.

---

## 3. Zero extension gives an interior-time homogeneous Oseen pair

M5-145 proves all-order terminal flatness on every fixed punctured compact set.

M5-215 therefore allows the smooth zero extension

\[
\widetilde Z(t,x)
=
\begin{cases}
Z(t,x),&t<T_*,\\
0,&t\ge T_*,
\end{cases}
\]

with the relative pressure gauge chosen as

\[
\widetilde q=0
\quad(t\ge T_*).
\]

Extend `A=u^V` and `B=u^W` smoothly and arbitrarily for `t>T_*`.

Because

\[
\widetilde Z=0,
\qquad
\widetilde q=0
\]

there, the extended pair still satisfies

\[
\boxed{
\widetilde Z_t-\nu\Delta\widetilde Z
+(A\cdot\nabla)\widetilde Z
+(\widetilde Z\cdot\nabla)B
+\nabla\widetilde q=0
}
\]

through the terminal slice in the weak sense, and in fact smoothly under the all-order flatness package.

Thus `T_*` may be used as the interior Carleman time center

\[
\boxed{t_0=T_*.}
\]

---

## 4. Use a Carleman-level cutoff, not an independent radial cutoff

Take

\[
\varphi(t,x)
=
\exp\{\lambda[d(x)-\beta(t-T_*)^2]\}.
\]

Use the standard nested levels

\[
\mu_3<\mu_4<\mu_5
\]

from the local propagation construction, with a target cylinder contained in

\[
\boxed{D_5:=\{\varphi>\mu_5\}.}
\]

Choose

\[
\chi(t,x)
=
\bar\chi\!\left(
\frac{\varphi(t,x)-\mu_3}{\mu_4-\mu_3}
\right),
\]

where

\[
\bar\chi=0\quad\text{below }0,
\qquad
\bar\chi=1\quad\text{above }1.
\]

Then

\[
\boxed{
\chi=1\quad\text{on }\{\varphi\ge\mu_4\}
}
\]

and every derivative of `chi` is supported in

\[
\boxed{
S_\chi:=\{\mu_3\le\varphi\le\mu_4\}.
}
\]

This automatically combines the temporal and spatial source-gap construction of M5-216.

---

## 5. Localized pair and its exact source

Define

\[
v:=\chi\widetilde Z,
\qquad
p:=\chi\widetilde q.
\]

A direct calculation gives

\[
\boxed{
\begin{aligned}
F_\chi
={}&
(\partial_t\chi-\nu\Delta\chi+A\cdot\nabla\chi)\widetilde Z\\
&-2\nu(\nabla\chi\cdot\nabla)\widetilde Z
+\widetilde q\,\nabla\chi,
\end{aligned}
}
\]

and

\[
\boxed{
h_\chi:=\nabla\cdot v=\nabla\chi\cdot\widetilde Z.}
\]

The localized fields satisfy exactly

\[
\boxed{
\partial_tv-\nu\Delta v
+(A\cdot\nabla)v
+(v\cdot\nabla)B
+\nabla p
=F_\chi,
\qquad
\nabla\cdot v=h_\chi.
}
\]

Crucially,

\[
\boxed{
\operatorname{supp}F_\chi
\cup
\operatorname{supp}h_\chi
\cup
\operatorname{supp}\nabla_{x,t}h_\chi
\subset S_\chi.
}
\]

Thus every source permitted by the external theorem lies at Carleman level at most `mu4`.

---

## 6. Boundary and endpoint hypotheses

Choose the bounded local spacetime domain used in the Carleman estimate so that all artificial boundary components lie in the region where

\[
\varphi\le\mu_3.
\]

Then `chi` is identically zero in a neighborhood of those components.

Hence

\[
\boxed{
v=0,
\quad
\nabla v=0,
\quad
p=0
}
\]

on every artificial boundary where the theorem requires homogeneous data.

Likewise choose the local time interval symmetrically around `T_*` and sufficiently long compared with the selected superlevel component so that `chi=0` at both temporal endpoints.

Therefore

\[
\boxed{v(\cdot,t_-)=v(\cdot,t_+)=0.}
\]

All boundary/Cauchy terms in the external Carleman estimate vanish.

The future part `t>T_*` is even simpler because the underlying field itself is identically zero there.

---

## 7. Source side has the lower exponential weight

Since all source terms are supported in `S_chi`,

\[
\varphi\le\mu_4.
\]

Smooth punctured regularity gives a finite source norm

\[
M_\chi<\infty
\]

independent of the Carleman parameter `s`.

Therefore

\[
\boxed{
\int
\left(
|F_\chi|^2
+|h_\chi|^2
+|\nabla_{x,t}h_\chi|^2
\right)
e^{2s\varphi}
\le
M_\chi^2e^{2s\mu_4}.
}
\]

Applying the Bellassoued–Imanuvilov–Yamamoto estimate gives

\[
\boxed{
\|(v,p)\|_{X_s(D)}^2
\le
C M_\chi^2e^{2s\mu_4}.
}
\]

---

## 8. Target side has the higher exponential weight

On the nonempty target component `D5`,

\[
\chi=1
\]

and

\[
\varphi\ge\mu_5.
\]

Consequently the positive velocity term in the Carleman norm gives, for some positive polynomial factor `c(s)`,

\[
\boxed{
 c(s)e^{2s\mu_5}
\|\widetilde Z\|_{L^2(D_5)}^2
\le
C M_\chi^2e^{2s\mu_4}.
}
\]

Hence

\[
\boxed{
\|\widetilde Z\|_{L^2(D_5)}^2
\le
\frac{CM_\chi^2}{c(s)}
 e^{-2s(\mu_5-\mu_4)}.
}
\]

Since

\[
\boxed{\mu_5-\mu_4>0,}
\]

letting

\[
s\to\infty
\]

gives

\[
\boxed{
\widetilde Z=0
\quad\text{on }D_5.
}
\]

Because the target is chosen symmetrically about `T_*`, it contains a nonempty **preterminal** spacetime open subset.

Status: **PROVED by hypothesis match to the existing linearized-Navier–Stokes Carleman estimate.**

---

## 9. From local preterminal equality to same-tail injectivity

Choose any regular time

\[
t_1<T_*
\]

for which

\[
D_5\cap\{t=t_1\}
\]

contains a nonempty spatial open set.

Then

\[
Z(t_1,x)=0
\]

on that open set.

The repository's M5-183 closure bridge uses ordinary spatial analyticity/unique continuation at the smooth preterminal time to extend equality through the connected whole space:

\[
\boxed{Z(t_1,\cdot)=0\quad\text{on }\mathbb R^3.}
\]

Classical forward uniqueness for the smooth Navier–Stokes solution then gives equality of the two aligned physical realizations on the remaining interval to `T_*`.

Therefore their corresponding W1 states coincide.

Thus

\[
\boxed{
T_V=T_W
\quad\Longrightarrow\quad
V=W
}
\]

inside the audited compact W1 same-tail class.

Equivalently,

\[
\boxed{P1_B=\varnothing.}
\]

---

## 10. Relation to previous negative audits

This closure does **not** contradict M5-194/M5-210.

Those notes studied whole-space or singular-center Carleman estimates in which the common canonical tail has arbitrary Hardy-critical amplitude.

The present proof first moves to a fixed punctured local region, where

\[
A=u^V,
\quad
\nabla B=\nabla u^W
\]

are ordinary bounded smooth coefficients.

It then uses all-order same-tail terminal flatness to make `T_*` an interior time by zero extension.

Hence the critical center is **bypassed**, not perturbatively absorbed.

---

## 11. Audit of possible hidden assumptions

### A. Global boundedness of the original Type-I fields

Not used.

Only boundedness on a fixed compact set away from `x_*` is required.

### B. Terminal time analyticity

Not used.

All-order `C^∞` terminal flatness from M5-145 is enough for smooth zero extension.

### C. Artificial-boundary equality of the original pair

Not used.

The localized fields vanish near the artificial Carleman boundary because `chi=0` there.

### D. Divergence-free localization

Not required.

The external theorem explicitly permits

\[
\nabla\cdot v=h,
\]

and controls `h` and its first spacetime derivatives.

### E. Pressure-free reduction

Not required.

The external estimate is already a velocity-pressure Carleman estimate for linearized Navier–Stokes.

### F. Critical-tail smallness

Not used.

The singular core/tail amplitude never enters the fixed punctured coefficient bound.

---

## 12. DSD verdict

### Formation — GREEN

All fields, coefficients, cutoffs, source terms, and theorem hypotheses are explicit.

### Axis — GREEN

Singular-center global dynamics and fixed-punctured local continuation are not mixed.

### Static aggregation — GREEN

The literature theorem is applied only after matching the actual equation, divergence source, endpoint data, and boundary support.

### Dynamics — GREEN FOR `P1_B`

The exponential Carleman gap gives exact local preterminal equality.

### Cross-audit — GREEN

Previous RED shortcuts—terminal analyticity, exterior pointwise Biot–Savart, generic scalar BU, polynomial-weight arbitrary-critical absorption—are not used.

---

## 13. Updated frontier

The same-tail noninjectivity frontier is reduced from

\[
P1_A\lor P1_B
\]

to the already audited algebraic/minimal-set part, with the flat branch removed:

\[
\boxed{
P1_B=\varnothing.
}
\]

This is a substantial endgame closure, but it is **not yet a proof of global regularity**.

The next master audit must revisit the remaining non-same-tail / tail-selection alternatives and determine whether tail-factor injectivity plus the already closed stationary/DSS/turnover branches exhausts the full ancient survivor tree.

---

References used for theorem matching:

- M. Bellassoued, O. Yu. Imanuvilov, M. Yamamoto, *Carleman estimate for the Navier–Stokes equations and an application to a lateral Cauchy problem*, Inverse Problems 32 (2016), 025001, arXiv:1506.02534.
- M. Boulakia, *Quantification of the unique continuation property for the nonstationary Stokes problem*, Mathematical Control and Related Fields 6 (2016), 27–52.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]