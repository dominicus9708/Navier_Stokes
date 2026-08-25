# DSD W1 Hardy--Leray Prelimit Weighted-Enstrophy Lower Bound

Date: 2026-08-26

Status: **SHARP SOLENOIDAL HARDY--LERAY INPUT + WEIGHTED CURL CONVERSION / W1 POSITIVE CUBIC SHELL DENSITY FORCES LOGARITHMIC FIRST-WEIGHTED-ENSTROPHY GROWTH ON THE ACTUAL PRELIMIT ORBIT / DOUBLE-LOG STRAIN-ACTION NECESSITY DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The W1 endpoint has already been compressed to a positive critical cubic mass per logarithmic radius,

\[
M_{crit}>0,
\]

or equivalently a positive Bernoulli scale surplus.

A DSD audit asks for an independent representation of the same memory that does not use pressure.

The natural candidate is the first weighted enstrophy

\[
\mathcal M_1^\Omega(s)
:=
\int_{\mathbb R^3}|Y|\,|\Omega(Y,s)|^2\,dY.
\]

An earlier note derived its evolution and showed that a uniform upper bound does not follow from the standard energy/enstrophy data.  The missing direction was a rigorous **lower bound** forced by the critical shell population.

This note supplies that lower bound on the actual smooth prelimit Leray orbit.

---

## 2. External Hardy--Leray input

For smooth divergence-free vector fields on `R^3`, the sharp three-dimensional Hardy--Leray inequality at weight exponent `gamma=1/2` gives

\[
\boxed{
\frac53
\int_{\mathbb R^3}\frac{|U|^2}{|Y|}\,dY
\le
\int_{\mathbb R^3}|Y|\,|\nabla U|^2\,dY.
}
\]

This is a solenoidal inequality; no axisymmetry assumption is used.

Reference background:

- Cazacu et al., *Three-dimensional sharp Hardy--Leray inequality for solenoidal fields*, Nonlinear Analysis (2020).
- subsequent sharp Hardy--Leray work for solenoidal fields, Journal of Functional Analysis (2024).

Only the displayed inequality is imported here.

Set

\[
J(U):=
\int\frac{|U|^2}{|Y|},
\qquad
I(U):=
\int |Y||\nabla U|^2.
\]

Then

\[
I\ge\frac53J.
\]

---

## 3. Convert weighted gradient energy to weighted vorticity

For a divergence-free smooth rapidly decaying field,

\[
|\operatorname{curl}U|^2
=
|\nabla U|^2
-
\partial_iU_j\partial_jU_i
\]

after summing indices.

Therefore

\[
\int |Y||\Omega|^2
=
I-C,
\]

where

\[
C:=
\int |Y|\,\partial_iU_j\partial_jU_i.
\]

Integrate one derivative in the `j` index. Since `div U=0`,

\[
C
=
-
\int
U_i\,\partial_j|Y|\,\partial_iU_j.
\]

Because

\[
|\nabla|Y||=1,
\]

weighted Cauchy--Schwarz gives

\[
|C|
\le
J^{1/2}I^{1/2}.
\]

Hence

\[
\int |Y||\Omega|^2
\ge
I-\sqrt{IJ}.
\]

Write

\[
x:=I/J.
\]

The Hardy--Leray inequality gives `x>=5/3`. Since `x-sqrt(x)` is increasing for `x>=5/3`,

\[
\boxed{
\int |Y||\Omega|^2
\ge
c_{HL,\omega}
\int\frac{|U|^2}{|Y|},
}
\]

where

\[
\boxed{
c_{HL,\omega}
:=
\frac53-\sqrt{\frac53}
\approx0.3756722179.
}
\]

This is the required pressure-free velocity-to-vorticity bridge.

Status: **PROVED from the Hardy--Leray input and elementary integration by parts.**

---

## 4. Insert the W1 Type-I envelope

On the late W1 Type-I corridor, the shell envelope is

\[
\boxed{
|U(Y,s)|
\le
\frac{A_0}{|Y|}
}
\]

through the normalized shell range used in the Barker--Prange recovery.

Therefore pointwise

\[
|U|^3
\le
\frac{A_0}{|Y|}|U|^2,
\]

and hence on any union of those shells

\[
\boxed{
\int\frac{|U|^2}{|Y|}
\ge
\frac1{A_0}
\int |U|^3.
}
\]

The direction is important: the Type-I upper amplitude converts cubic occupancy into a **lower** weighted-L2 charge.

---

## 5. Use the positive-density shell recovery on the actual prelimit orbit

The repository already proves that at sufficiently late Leray time `s`, for dyadic shells

\[
A_k=\{R_k<|Y|<2R_k\},
\qquad
R_k=2^kR_0,
\]

up to the Barker--Prange admissible outer radius,

\[
\boxed{
\sum_{k=0}^{N(s)-1}
\int_{A_k}|U(Y,s)|^3dY
\ge
a_0N(s),
}
\]

with fixed `a0>0`.

The admissible radius was chosen so that

\[
K(s)\asymp e^{\delta s}
\]

for one fixed `delta>0`. Consequently

\[
\boxed{
N(s)
=
\frac{\delta}{\log2}s+O(1).
}
\]

Combining the shell lower bound with the Type-I bridge gives

\[
\int\frac{|U|^2}{|Y|}
\ge
\frac{a_0}{A_0}N(s).
\]

Then the weighted curl inequality gives

\[
\boxed{
\mathcal M_1^\Omega(s)
:=
\int |Y||\Omega|^2dY
\ge
\frac{c_{HL,\omega}a_0}{A_0}
N(s).
}
\]

Therefore

\[
\boxed{
\mathcal M_1^\Omega(s)
\ge
c_{M1}\,s-C,
}
\]

where

\[
\boxed{
c_{M1}
:=
\frac{c_{HL,\omega}a_0\delta}
{A_0\log2}
>0.
}
\]

This is a theorem-level lower bound on the **actual smooth prelimit orbit**, conditional only on the already retained W1/Barker--Prange inputs.

---

## 6. Physical scaling

Use standard backward Leray variables

\[
\tau=T^*-t=e^{-s},
\qquad
Y=\frac{x-X_*}{\sqrt\tau},
\]

\[
u(x,t)=\tau^{-1/2}U(Y,s),
\qquad
\omega(x,t)=\tau^{-1}\Omega(Y,s).
\]

Then

\[
dx=\tau^{3/2}dY,
\qquad
|x-X_*|=\tau^{1/2}|Y|.
\]

Thus the first weighted enstrophy is exactly scale invariant:

\[
\boxed{
\int |x-X_*||\omega(x,t)|^2dx
=
\int |Y||\Omega(Y,s)|^2dY.
}
\]

Therefore the prelimit lower bound becomes

\[
\boxed{
\int |x-X_*||\omega(x,t)|^2dx
\ge
c_{M1}
\log\frac1{T^*-t}
-C.
}
\]

So a W1 singular survivor must make the physical first weighted enstrophy diverge at least logarithmically.

This is stronger than the earlier qualitative statement that a persistent critical conveyor would *suggest* linear shell accumulation.

---

## 7. Consequence for integrated strain

The earlier exact weighted-enstrophy evolution audit gave, on a material-center/no-center-turnover lane,

\[
M_1'(t)
\le
3\|S(t)\|_\infty M_1(t),
\]

and hence

\[
M_1(t)
\le
M_1(t_0)
\exp\left(
3\int_{t_0}^{t}\|S(\tau)\|_\infty d\tau
\right).
\]

Combine this upper bound with

\[
M_1(t)
\ge
c_{M1}\log\frac1{T^*-t}-C.
\]

For sufficiently late time,

\[
\boxed{
\int_{t_0}^{t}\|S(\tau)\|_\infty d\tau
\ge
\frac13
\log\log\frac1{T^*-t}
-O(1).
}
\]

Thus W1 requires at least a double-logarithmically divergent strain-sup action.

This is a necessary condition, not a contradiction.  It is compatible with Type-I growth and with the Beale--Kato--Majda scale of singular behavior.

---

## 8. DSD interpretation

The same critical memory is now visible in three different descriptions:

\[
\boxed{
M_{crit}>0
}
\]

as cubic mass per log shell,

\[
\boxed{
\mathcal S_B(\infty)=\mathscr R_3/6>0
}
\]

as Bernoulli scale surplus, and

\[
\boxed{
\mathcal M_1^\Omega(s)\gtrsim s
}
\]

as pressure-free first-weighted-enstrophy growth on the actual prelimit orbit.

These are not three independent branches. They are three descriptors of the same critical memory.

The new value of the vorticity descriptor is that it lives on the prelimit and avoids pressure gauge issues.

---

## 9. Audit limits

This note does **not** prove a contradiction.

In particular:

1. finite kinetic energy does not uniformly bound `M1`;
2. finite time-integrated enstrophy does not uniformly bound an instantaneous first spatial moment;
3. logarithmic `M1` growth is integrable in physical time after the shrinking-time weight is restored;
4. the double-log strain-action lower bound is compatible with known blow-up necessary conditions.

Therefore no regularity claim follows solely from this lower bound.

What it does prove is that any W1 endpoint closure may equivalently target the impossibility of logarithmic first-weighted-enstrophy creation on the prelimit.

---

## 10. Updated endpoint target

The single W1 endpoint can now be attacked without pressure through the statement

\[
\boxed{
\liminf_{t\uparrow T^*}
\frac{1}{\log(1/(T^*-t))}
\int |x-X_*||\omega(x,t)|^2dx
=0.
}
\]

Any theorem of this form contradicts the W1 lower bound above.

Equivalently, one may still prove `Mcrit=0` or `S_B(infinity)=0`.

The three targets are different analytic routes to the same DSD endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
