# M18-060 — CE-H amplitude-moment coboundary: kappa is globally dissipative and recurrent recharge is strain-paid, but no bounded monotone contradiction follows

**Date:** 2026-09-11  
**Status:** SIGNED-OBSERVABLE AUDIT / EXACT AMPLITUDE-MOMENT BALANCE / KAPPA-RECHARGE COLLAPSE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-059 shows that no currently available **unsigned additive** payer simultaneously has

- a finite original-parent total;
- event additivity;
- nonsummable first-hitting homogeneity;
- and a fixed recurrent positive payment.

M16-016 therefore points to the signed route: find a bounded state observable whose generator has a strict one-way sign, or show that every compensating recharge consumes a separately finite resource.

M16-017--018 supply the exact CE-H material-amplitude law

\[
D_B\log\rho=\sigma+\kappa-1.
\]

The present module derives the full \(L^p\) amplitude-moment balance and asks whether it yields the desired bounded coboundary contradiction.

It yields a strong structural simplification — \(\kappa\) is globally dissipative for every \(p\ge2\), so recurrent amplitude maintenance is necessarily strain-paid in the invariant mean — but the source and sinks exactly balance on a recurrent component. Thus no monotone contradiction appears.

## 2. Similarity CE-H setting

Work in the viscosity-one similarity normalization used by M16. Let

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

with

\[
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W.
\]

The similarity material field is

\[
B=U+\frac12y,
\qquad
\nabla\cdot B=\frac32.
\]

M16-017 gives

\[
\boxed{
D_B\rho=(\sigma+\kappa-1)\rho.
}
\]

Write

\[
g:=\sigma+\kappa-1.
\]

## 3. Exact \(p\)-amplitude moment balance

For every finite \(p\ge2\), define

\[
\boxed{
M_p(\theta):=\int_{\mathbb R^3}\rho(y,\theta)^pdy.
}
\]

On the retained compact smooth branch, \(M_p<\infty\) because

\[
M_p\le\|\rho\|_\infty^{p-2}M_2.
\]

The material law gives

\[
D_B(\rho^p)=pg\rho^p.
\]

Using

\[
\partial_\theta(\rho^p)
+\nabla\cdot(B\rho^p)
=
\left(pg+\frac32\right)\rho^p,
\]

and integrating over \(\mathbb R^3\),

\[
\boxed{
M_p'
=
\frac32M_p
+p\int g\rho^pdy.
}
\]

Equivalently,

\[
\boxed{
\frac1pM_p'
=
\int(\sigma+\kappa)\rho^pdy
-\left(1-\frac{3}{2p}\right)M_p.
}
\]

Define

\[
c_p:=1-\frac{3}{2p}>0
\qquad(p\ge2).
\]

Then

\[
\boxed{
\frac1pM_p'
=
\int\sigma\rho^pdy
+
\int\kappa\rho^pdy
-c_pM_p.
}
\]

## 4. Exact weighted-kappa integration identity

Multiply

\[
\Delta W=\kappa W
\]

by

\[
\rho^{p-2}W
\]

and integrate.

The right side is

\[
\int\kappa\rho^pdy.
\]

For the left side,

\[
\int\rho^{p-2}W\cdot\Delta W
=-\int\nabla(\rho^{p-2}W):\nabla W.
\]

Since

\[
W\cdot\partial_iW
=
\rho\,\partial_i\rho,
\]

one obtains

\[
\boxed{
\int\kappa\rho^pdy
=
-\int\rho^{p-2}|\nabla W|^2dy
-(p-2)\int\rho^{p-2}|\nabla\rho|^2dy.
}
\]

Define the nonnegative weighted diffusion functional

\[
\boxed{
D_p
:=
\int\rho^{p-2}|\nabla W|^2dy
+(p-2)\int\rho^{p-2}|\nabla\rho|^2dy.
}
\]

Then

\[
\boxed{
\int\kappa\rho^pdy=-D_p\le0.
}
\]

This holds for every finite \(p\ge2\).

For \(p=2\), it reduces to the known identity

\[
\int\kappa\rho^2=-P.
\]

## 5. Exact source-sink form

Substituting Section 4 into the amplitude-moment equation gives

\[
\boxed{
\frac1pM_p'
=
A_p-D_p-c_pM_p,
}
\]

where

\[
\boxed{
A_p:=\int\sigma\rho^pdy.
}
\]

Thus the three terms have exact roles:

- \(A_p\): strain source;
- \(D_p\): CE-H Laplacian/amplitude-direction diffusion sink;
- \(c_pM_p\): similarity-damping/volume-expansion sink.

There is no positive global \(\kappa\)-source term.

## 6. Invariant recurrence forces exact strain payment

Let \(\mu\) be an invariant probability measure on the compact recurrent CE-H component.

Because \(M_p\) is a bounded state observable for every fixed finite \(p\), invariance gives

\[
\left\langle M_p'\right\rangle_\mu=0.
\]

Therefore

\[
\boxed{
\left\langle A_p\right\rangle
=
\left\langle D_p\right\rangle
+c_p\left\langle M_p\right\rangle.
}
\]

In particular, on every nontrivial component with \(\langle M_p\rangle>0\),

\[
\boxed{
\left\langle\int\sigma\rho^pdy\right\rangle
\ge
\left(1-\frac{3}{2p}\right)
\left\langle\int\rho^pdy\right\rangle
>0.
}
\]

Thus recurrent amplitude maintenance is globally strain-paid.

## 7. Positive kappa cannot be a net recharge source

M16-018 allowed an individual upward recharge segment to be locally paid by either

\[
\sigma>0
\]

or

\[
\kappa>0,
\]

with the latter requiring negative-\(\kappa\) compensation elsewhere.

Section 4 strengthens the global statement:

\[
\boxed{
\text{for every }p\ge2,
\quad
\int\kappa\rho^p\le0
\text{ at each time}.
}
\]

Therefore local positive-\(\kappa\) recharge can never be a net source for any global \(p\)-amplitude moment.

Its positive contribution is always overcompensated by weighted negative-\(\kappa\)/gradient structure in the same state.

Consequently the invariant recurrent source is not

\[
\text{strain or kappa};
\]

it is, globally,

\[
\boxed{
\text{strain source only, with kappa entirely on the sink side}.
}
\]

## 8. Regular-threshold signed current as a bounded-state coboundary

Let \(\chi\in C^1([0,\infty))\) satisfy

\[
0\le\chi\le1,
\qquad
\chi(\rho)=0\text{ for }\rho\le a_-,
\]

with \(\chi'\ge0\) supported in a fixed amplitude collar.

Define the bounded high-amplitude volume observable

\[
\boxed{
F_\chi
:=
\int\chi(\rho)dy.
}
\]

Because \(\rho\ge a_-\) on its support,

\[
F_\chi\le a_-^{-2}M_2\le a_-^{-2}Z_*.
\]

The material law gives

\[
D_B\chi(\rho)
=
\chi'(\rho)\rho g.
\]

Using \(\nabla\cdot B=3/2\),

\[
\boxed{
F_\chi'
=
\frac32F_\chi
+J_\chi,
}
\]

where the signed amplitude-current is

\[
\boxed{
J_\chi
:=
\int\chi'(\rho)\rho(\sigma+\kappa-1)dy.
}
\]

Invariant averaging gives

\[
\boxed{
\left\langle J_\chi\right\rangle
=-\frac32\left\langle F_\chi\right\rangle.
}
\]

Thus on every nontrivial recurrent high-amplitude component,

\[
\boxed{
\langle J_\chi\rangle<0.
}
\]

There is a strict net **downward** signed material current through every active high-amplitude transition collar.

## 9. Why the negative current is not a contradiction

The identity

\[
F_\chi'
=
\frac32F_\chi+J_\chi
\]

has exactly the M16-016 coboundary form.

The negative threshold current is balanced by the positive similarity material-volume expansion term

\[
\frac32F_\chi.
\]

Hence the state can recur while

- high-amplitude material continually exits downward;
- new/re-amplified material enters upward;
- the similarity material flow expands volume;
- the bounded high-amplitude occupancy remains statistically stationary.

This is a genuine signed balance, not a one-way monotone state drift.

In particular,

\[
\boxed{
\langle J_\chi\rangle<0
\not\Rightarrow
\text{finite-event exhaustion}.
}
\]

## 10. Relation to hysteretic recharge cycles

M16-018 proves that a completed up/down amplitude cycle satisfies

\[
\int_{cycle}|\sigma+\kappa-1|d\theta
\ge2\Delta_a.
\]

The present module explains why arbitrarily many such cycles remain compatible with compact recurrence:

- the path variation is unbounded but is not a state observable;
- \(F_\chi\) is bounded but its generator contains the compensating \(3F_\chi/2\) term;
- global positive-\(\kappa\) recharge is unavailable, but positive strain can continually replenish the dissipative sinks.

Thus the remaining loop is sharpened to

\[
\boxed{
\text{strain-paid recharge}
\to
\text{amplitude occupancy}
\to
\text{net downward threshold current/diffusion}
\to
\text{strain-paid recharge}.
}
\]

## 11. A useful high-amplitude consequence

The invariant identity holds for every finite \(p\ge2\):

\[
\frac{\langle A_p\rangle}{\langle M_p\rangle}
=
 c_p
+
\frac{\langle D_p\rangle}{\langle M_p\rangle}
\ge c_p.
\]

Since

\[
c_p=1-\frac{3}{2p}\uparrow1,
\]

higher-amplitude-weighted moments require increasingly strong average aligned strain.

This does not by itself give a contradiction, but it identifies the remaining CE-H recharge hard core as an increasingly high-amplitude **strain-support problem**, not a kappa-source problem.

## 12. DSD verdict

### Certified

1. For every \(p\ge2\),
   \[
   \int\kappa\rho^p=-D_p\le0.
   \]
2. Recurrent global amplitude moments are necessarily maintained by aligned strain.
3. Local positive-\(\kappa\) recharge is globally overcompensated and is not an independent net source.
4. A bounded high-amplitude volume observable has exact signed current
   \[
   F_\chi'=\frac32F_\chi+J_\chi,
   \qquad
   \langle J_\chi\rangle=-\frac32\langle F_\chi\rangle<0.
   \]
5. The signed threshold current is exactly compensated by similarity-volume expansion, so no bounded monotone contradiction follows.

### Not certified

- a finite nonreplenishable resource consumed by the strain-paid recharge loop;
- a one-sign bounded-state drift after the \(3F_\chi/2\) compensation;
- a global constraint preventing repeated positive aligned-strain recharge;
- closure of the critical/remote roots;
- global regularity.

## 13. Next target

The unsigned and simple signed routes are now both sharply constrained.

The next high-value audit is the **aligned-strain source itself**:

\[
A_p=\int\sigma\rho^p.
\]

One should test whether the exact strain-eigenline condition, incompressibility, and Biot--Savart nonlocality force this recurrent positive strain source to draw from a bounded or scale-critical state resource, or whether it too is a freely rechargeable compact-hull source.

Equivalently: can the strain-paid recharge loop be closed by a bounded state coboundary, or must it be accepted as the remaining CE-H recurrent source mechanism?