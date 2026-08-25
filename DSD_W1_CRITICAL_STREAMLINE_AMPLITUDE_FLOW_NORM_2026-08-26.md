# DSD W1 Critical Streamline-Amplitude Flow Norm

Date: 2026-08-26

Status: **THE W1 ENDPOINT FORCES A NONZERO CRITICAL STREAMLINE-AMPLITUDE FLOW AND LOGARITHMIC DIVERGENCE OF ITS PHYSICAL SCALE-INVARIANT SPACETIME NORM / THIS IDENTIFIES AN EXACT REGULARITY-CRITERION SATURATION MECHANISM BUT DOES NOT YET EXCLUDE THE SURVIVOR / GLOBAL REGULARITY UNPROVED.**

## 1. Input: positive critical Lamb/Bernoulli work

Let

\[
a:=|U|,
\qquad
n:=\frac{U}{|U|}
\]

where defined, and let

\[
B:=P+\frac12|U|^2.
\]

The W1 endpoint gives an invariant positive source

\[
\boxed{
\langle F_\infty\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6}
=:f_*>0.
}
\]

From incompressibility,

\[
\nabla\cdot(an)=0,
\]

so

\[
\boxed{
n\cdot\nabla a=-a\,\nabla\cdot n.
}
\]

Define the streamline-amplitude derivative

\[
\boxed{
h:=n\cdot\nabla a
}
\]

and the velocity-weighted amplitude flow

\[
\boxed{
e:=U\cdot\nabla a=a h.
}
\]

The endpoint pressure/Lamb identity can be written as

\[
\boxed{
F_\infty
=
\int B\,U\cdot\nabla a\,dY
=
\int B e\,dY.
}
\]

Thus the positive critical source is exactly a pairing between Bernoulli amplitude and streamline-amplitude flow.

---

## 2. A fixed lower bound in `L^(3/2)`

The W1 compact class has a uniform `H1` bound and therefore a uniform `L6` bound,

\[
\|U\|_6\le M_6.
\]

By the pressure Calderon-Zygmund estimate,

\[
\|P\|_3
\le C\|U\otimes U\|_3
\le C\|U\|_6^2.
\]

Hence

\[
\boxed{
\|B\|_3\le C_B M_6^2.
}
\]

Holder therefore gives

\[
|F_\infty|
\le
\|B\|_3\|e\|_{3/2}
\le
C_BM_6^2\|e\|_{3/2}.
\]

Averaging with the invariant measure,

\[
\boxed{
\left\langle
\|U\cdot\nabla|U|\|_{3/2}
\right\rangle_\mu
\ge
\frac{f_*}{C_BM_6^2}
=:c_E>0.
}
\]

Consequently, by Jensen,

\[
\boxed{
\left\langle
\|U\cdot\nabla|U|\|_{3/2}^2
\right\rangle_\mu
\ge c_E^2>0.
}
\]

This estimate avoids the singular direction field at velocity zeros: the product `U dot grad |U|` is defined directly from `U`.

---

## 3. Exact physical scaling

For a putative singular time `T_*`, write

\[
u(x,t)
=(T_*-t)^{-1/2}U(Y,s),
\qquad
Y=\frac{x-X_*}{\sqrt{T_*-t}},
\qquad
s=-\log(T_*-t).
\]

Then

\[
|u|=(T_*-t)^{-1/2}a,
\]

and

\[
\nabla_x|u|
=(T_*-t)^{-1}\nabla_Ya.
\]

Therefore

\[
\boxed{
 u\cdot\nabla_x|u|
=(T_*-t)^{-3/2}e(Y,s).
}
\]

Since `dx=(T_*-t)^(3/2)dY`,

\[
\boxed{
\|u\cdot\nabla|u|\|_{L_x^{3/2}}
=(T_*-t)^{-1/2}
\|e(s)\|_{L_Y^{3/2}}.
}
\]

Hence

\[
\begin{aligned}
\int^{T_*}
\|u\cdot\nabla|u|\|_{3/2}^2dt
&=
\int^∞
(T_*-t)^{-1}
\|e(s)\|_{3/2}^2
(T_*-t)ds\\
&=
\boxed{
\int^\infty
\|e(s)\|_{3/2}^2ds.
}
\end{aligned}
\]

Thus `L_t^2 L_x^(3/2)` is exactly scale invariant for `u dot grad |u|`.

---

## 4. W1 forces logarithmic divergence of the critical norm

On an invariant generic orbit, Birkhoff averaging gives

\[
\liminf_{S\to\infty}
\frac1S
\int_0^S
\|e(s)\|_{3/2}^2ds
\ge c_E^2.
\]

Therefore

\[
\boxed{
\int_0^S
\|U\cdot\nabla|U|\|_{3/2}^2ds
\ge c_E^2S-o(S).
}
\]

Returning to physical time,

\[
S\sim \log\frac1{T_*-t},
\]

so

\[
\boxed{
\int^{t}
\|u\cdot\nabla|u|\|_{3/2}^2d\tau
\gtrsim
c_E^2
\log\frac1{T_*-t}
}
\]

along the W1 recurrent corridor.

Thus any W1 singular survivor must violate finiteness of the exact critical `L_t^2 L_x^(3/2)` streamline-amplitude-flow norm by a logarithmic amount.

---

## 5. Relation to velocity-direction geometry

Because

\[
e
=U\cdot\nabla a
=-a^2\nabla\cdot n,
\]

we have

\[
\boxed{
U\cdot\nabla|U|
=-|U|^2\nabla\cdot\left(\frac U{|U|}\right).
}
\]

This is the same geometric mechanism behind velocity-direction regularity criteria: amplitude change along a streamline is equivalent to compression/expansion of the direction field.

The present result does not prove that the known sufficient direction criteria hold. It proves the opposite type of statement needed for singularity auditing: any W1 survivor must carry a fixed positive amount of this geometric deformation in the scale-critical flow norm.

---

## 6. DSD interpretation

The critical endpoint is no longer merely

\[
\text{positive pressure work}.
\]

It is

\[
\boxed{
\text{persistent streamline-amplitude conversion}
}
\]

with the exact scale-invariant certificate

\[
\boxed{
U\cdot\nabla|U|
\notin
L_s^2L_Y^{3/2}
\quad\text{over the infinite recurrent Leray-time tail}.
}
\]

Equivalently in physical variables,

\[
\boxed{
u\cdot\nabla|u|
\notin
L_t^2L_x^{3/2}
}
\]

and the failure is at least logarithmic under the invariant W1 corridor.

This is a genuine narrowing: the last nonlinear mechanism must not merely be nonzero but must saturate a critical spacetime channel indefinitely.

---

## 7. What this does not prove

A divergent critical norm is consistent with a singular solution and therefore is not itself a contradiction.

To close W1 one still needs a **nonrepeatability theorem** showing that an unforced finite-energy Navier--Stokes prelimit cannot maintain this critical streamline-amplitude conversion together with the already proved zero total nonlinear energy work and positive high-frequency Lamb transfer.

The next useful target is therefore a joint inequality involving

\[
\int U\cdot L_s=0,
\qquad
\int |U|U\cdot L_s<0,
\qquad
\int\Delta U\cdot L_s>0,
\]

or, equivalently, an amplitude-frequency transport inequality for the same signed nonlinear work density.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
