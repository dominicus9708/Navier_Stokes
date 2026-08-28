# DSD M5-188 — Pressure-Free Exterior Backward Uniqueness Is Standard

Date: 2026-08-28

Status: **P1_B FLAT-FIBER / PRESSURE-FREE EXTERIOR BRANCH GREEN / ON EVERY FIXED PHYSICAL EXTERIOR DOMAIN THE W1 TYPE-I COEFFICIENTS BECOME UNIFORMLY BOUNDED UP TO THE TERMINAL TIME, SO THE CLASSICAL ESCURIAZA–SEREGIN–ŠVERÁK EXTERIOR BACKWARD-UNIQUENESS THEOREM APPLIES TO A VECTOR HEAT SYSTEM ONCE THE PRESSURE/NONLOCAL VELOCITY RECONSTRUCTION TERMS ARE ABSENT / THE ONLY GENUINE OBSTRUCTION IS THE STOKES/OSEEN COUPLING, NOT THE EXTERIOR HEAT CARLEMAN ITSELF / GLOBAL REGULARITY UNPROVED.**

---

## 1. Physical same-tail difference

Let `V,W` be two states in the same canonical-tail fiber and let

\[
Z=u^V-u^W
\]

be the difference of their physical inverse-Leray realizations.

M5-145 gives equality of every algebraic Fuchsian coefficient.  Therefore on every fixed punctured region

\[
|x-x_*|\ge R>0
\]

we have terminal flatness

\[
\boxed{
\partial_t^m Z(x,T_*)=0
\qquad \forall m\ge0.
}
\]

In particular,

\[
\boxed{Z(x,T_*)=0.}
\]

The same holds for the relative vorticity

\[
\eta:=\nabla\times Z.
\]

---

## 2. Fixed exterior removes the Type-I coefficient singularity

The W1 physical Type-I bounds have the scale-covariant form

\[
|u(x,t)|\le \frac{C}{|x-x_*|+\sqrt{T_*-t}},
\]

\[
|\nabla u(x,t)|+|\omega(x,t)|
\le
\frac{C}{|x-x_*|^2+(T_*-t)}.
\]

Hence on

\[
\Omega_R:=\{|x-x_*|>R\}
\]

there are finite constants `C_R,C_R'` such that, uniformly for `t<T_*`,

\[
\boxed{|u|\le C_R,\qquad |\nabla u|+|\omega|\le C_R'.}
\]

Thus the Type-I singularity is a center phenomenon and disappears on every fixed exterior domain.

---

## 3. Classical pressure-free backward uniqueness

The classical exterior-domain backward-uniqueness theorem for the backward heat operator states, schematically:

if a smooth vector field `f` on

\[
(\mathbb R^3\setminus \overline{B_R})\times[0,T]
\]

satisfies

\[
\boxed{
|(\partial_\tau+\nu\Delta)f|
\le C_R(|f|+|\nabla f|),
}
\]

has at most Gaussian spatial growth, and

\[
f(\cdot,0)=0
\]

in the exterior domain, then

\[
\boxed{f\equiv0}
\]

throughout that exterior spacetime cylinder.

This is the exact mechanism used in the Escauriaza–Seregin–Šverák regularity argument after vorticity has been reduced to a heat-type inequality.

No artificial boundary value on `|x|=R` is required by this exterior heat theorem.

---

## 4. Consequence for the present branch

Therefore, if the same-tail relative field could be reduced on `Omega_R` to either

\[
|(\partial_\tau+\nu\Delta)Z|
\le C_R(|Z|+|\nabla Z|)
\]

or

\[
|(\partial_\tau+\nu\Delta)\eta|
\le C_R(|\eta|+|\nabla\eta|),
\]

then terminal zero would imply

\[
Z\equiv0
\quad\text{or}\quad
\eta\equiv0
\]

on the exterior cylinder.

Spatial analyticity/unique continuation at any positive preterminal time would then propagate the equality inward.

Hence:

\[
\boxed{
\text{pressure-free exterior flat fiber}=0.
}
\]

This is GREEN.

---

## 5. Why the actual relative equation is not yet in that form

The velocity difference obeys

\[
\partial_tZ-\nu\Delta Z
+(u^V\cdot\nabla)Z
+(Z\cdot\nabla)u^W
+\nabla q=0,
\qquad \nabla\cdot Z=0.
\]

The pressure term prevents a componentwise heat inequality.

Taking curl removes pressure but gives

\[
\begin{aligned}
\partial_t\eta-\nu\Delta\eta
&+(u^V\cdot\nabla)\eta
-(\eta\cdot\nabla)u^V\\
&+(Z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)Z=0.
\end{aligned}
\]

The last two terms contain `Z` and `nabla Z`, not only `eta` and `nabla eta`.

Thus the missing implication is

\[
\boxed{
(\eta,Z)\text{ coupled Oseen--Stokes}
\Longrightarrow
\text{local heat-type inequality for }\eta
}
\]

or an equivalent pressure-compatible backward estimate.

---

## 6. DSD audit

### Formation — GREEN

The exterior region and relative fields already exist in the W1 physical realization.

### Axis — GREEN

Center Type-I singularity, fixed-exterior boundedness, and terminal time are not conflated.

### Static aggregation — GREEN

The bounded exterior coefficients are not promoted to global bounded coefficients.

### Dynamics — GREEN / ONE EXPLICIT MISSING COUPLING

The pressure-free theorem is standard.  The actual Stokes/Oseen reduction remains open.

### Cross-audit — GREEN

This does not use Straughan's obstacle-domain theorem, does not assume equality on the artificial sphere, and does not treat Biot–Savart as a local operator.

---

## 7. Frontier reduction

The first remaining large gate is no longer

\[
\text{construct an exterior heat Carleman estimate}.
\]

It is precisely

\[
\boxed{
\text{remove/control pressure and velocity reconstruction in the relative Oseen--Stokes system.}
}
\]

The next node audits a whole-space polynomial-weight route where the Leray/Calderón–Zygmund operator is retained instead of eliminated.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
