# DSD M5-140 — Local Terminal Taylor Recursion Leaves Odd Pressure Multipoles

Date: 2026-08-27

Status: **P1_A PRUNING / PUNCTURED TERMINAL SMOOTHNESS ELIMINATES NONINTEGER FUCHSIAN POWERS BUT DOES NOT SELECT THE REMAINING INTEGER ODD PRESSURE MULTIPOLES / AT EACH TERMINAL TAYLOR ORDER THE LOCAL PRESSURE POISSON PROBLEM IS UNIQUE ONLY MODULO A PUNCTURED HARMONIC MULTIPOLE, EXACTLY MATCHING THE FUCHSIAN `ell=2n+1` RESONANCE / LOCAL TAYLOR RECURSION ALONE CANNOT PROVE TAIL-FACTOR INJECTIVITY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Punctured terminal expansion

On every fixed physical annulus away from the center, write formally to arbitrary finite smooth order

\[
u(x,t)
=
b(x)
+
\sum_{n\ge1}\tau^n u_n(x),
\qquad
\tau=T_*-t,
\]

and

\[
p(x,t)
=
p_0(x)
+
\sum_{n\ge1}\tau^n p_n(x).
\]

M5-139 justifies integer terminal powers and excludes noninteger Puiseux powers on the realized smooth punctured branch.

---

## 2. Pressure recursion is elliptic only modulo harmonic functions

At each fixed time,

\[
-\Delta p
=
\partial_i u_j\partial_j u_i.
\]

Expanding in terminal powers gives for every integer `n>=0`

\[
\boxed{
-\Delta p_n
=F_n[b,u_1,\ldots,u_n],
}
\]

where `F_n` is determined by already appearing velocity coefficients at the corresponding order.

On a punctured annulus or punctured whole space this Poisson problem determines `p_n` only up to a harmonic function.

Thus local terminal recursion never fixes all pressure coefficients by itself.

---

## 3. The Fuchsian odd multipole is exactly the harmonic ambiguity

M5-137/M5-139 identify the smooth integer-sector pressure resonance at order `n` as

\[
\boxed{
p_n^{harm}(x)
=
|x-x_*|^{-(2n+2)}
Y_{2n+1}\!\left(\frac{x-x_*}{|x-x_*|}\right).
}
\]

This is harmonic away from the center because

\[
2n+2=(2n+1)+1.
\]

Hence

\[
\Delta p_n^{harm}=0
\qquad(x\ne x_*).
\]

Adding this term changes neither the local pressure Poisson source nor any lower Taylor coefficient.

Therefore the Fuchsian resonance and the local pressure-harmonic ambiguity are the same object in two coordinate descriptions.

---

## 4. Velocity recursion feels the free pressure coefficient one order later

The terminal Navier–Stokes equation gives schematically

\[
u_{n+1}
=
\mathcal A_n[b,u_1,\ldots,u_n]
-
\nabla p_n
\]

up to the conventional factorial/sign normalization of Taylor coefficients.

Thus a free harmonic component of `p_n` enters the next velocity coefficient through

\[
-\nabla p_n^{harm}.
\]

This produces the corresponding strong integer Fuchsian velocity correction.

Hence local smooth recursion propagates the multipole freedom rather than eliminating it.

---

## 5. Why terminal trace equality is insufficient

Suppose two same-tail W1 realizations have identical terminal velocity trace

\[
b_1=b_2=b
\]

on the punctured space.

M5-134 also fixes the leading critical pressure tail / `ell=1` dipole.

Nevertheless at higher orders one may have

\[
p_{n,1}-p_{n,2}
=
h_n,
\qquad
\Delta h_n=0
\]

on the punctured domain, with `h_n` an admissible faster-decaying odd multipole.

Then higher velocity Taylor coefficients can differ even though all lower data coincide.

Therefore

\[
\boxed{
\text{same terminal velocity trace}
\not\Rightarrow
\text{same full punctured Taylor jet}
}
\]

without a global pressure-selection principle.

---

## 6. DSD four-chain audit

### Formation — GREEN

The residual freedom comes from the actual kernel of the local pressure Poisson equation.

### Axis — GREEN

Terminal Taylor order, spherical multipole rank, and Fuchsian radial power are matched explicitly.

### Static aggregation — GREEN

The harmonic coefficient is not counted as a new external force; it is an undetermined local pressure component.

### Dynamics — GREEN

The coefficient affects later velocity terms through the actual pressure gradient in NSE.

### Cross-audit — GREEN

M5-139 eliminates noninteger sectors but does not imply local uniqueness of the remaining integer jet. M5-140 identifies the precise surviving kernel.

---

## 7. What can select the coefficient

The higher odd pressure multipoles must be selected, if at all, by information absent from a punctured local Taylor calculation, such as

1. the whole-space Riesz-transform pressure normalization;
2. distributional matching through the singular center;
3. finite-energy prelimit stress moments;
4. or a global backward-uniqueness theorem for the same-tail fiber.

These are all global center-matching inputs.

---

## 8. RED firewall

The following route is closed:

\[
\text{same tail}
+
\text{smooth terminal extension away from center}
\Rightarrow
\text{identical Taylor expansion}
\Rightarrow
\text{fiber zero}.
\]

The second implication fails because pressure Taylor coefficients retain punctured harmonic multipole freedom.

---

## 9. Revised P1 frontier

`P1_A` is now precisely a **global pressure-multipole selection problem**.

`P1_B` remains the Fuchsian-flat / backward-uniqueness problem after every algebraic multipole coefficient has been matched.

Thus same-tail injectivity requires both:

\[
\boxed{
\text{global selection of all odd multipoles}
+
\text{uniqueness of the flat remainder}.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]