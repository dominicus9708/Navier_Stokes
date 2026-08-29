# DSD M5-273 — Pineau–Vicol Weighted-Enstrophy / Invariant-Mean Generalization Audit

Date: 2026-08-30

Parent: `DSD_M5_272_RESIDUAL_HOMOGENEITY_TANGENT_PAIRING_AND_NONLINEAR_PRESSURE_FIREWALL_2026-08-30.md`

External anchor: B. Pineau and V. Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v2 (6 Aug 2026), especially Sections 5 and 7.

Status: **LITERATURE-MATCH / THE PINEAU--VICOL TIME-INDEPENDENT ADJOINT WEIGHT AND BERNOULLI IDENTITY EXTEND FORMALLY AND, UNDER THE RETAINED TYPE-I SMOOTHNESS, RIGOROUSLY TO AN INVARIANT STATISTICAL AVERAGE OF A COMPACT RECURRENT LERAY ORBIT / THE TOTAL TIME-DERIVATIVE TERM STILL VANISHES UNDER AN INVARIANT MEASURE, BUT THE RDSS PROOF'S DECISIVE SMALLNESS COMES FROM THE SHORT-PERIOD ESTIMATE `U-<U>=O(S)` (AND/OR SMALL ROTATION), WHICH IS ABSENT ON A GENERIC APERIODIC MINIMAL HULL / THE GENERAL RECURRENT IDENTITY THEREFORE BECOMES A NONTRIVIAL PRESSURE--FLUCTUATION COVARIANCE LAW AND A POSITIVE WEIGHTED ORBIT-VARIANCE FLOOR, NOT A LIOUVILLE CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Pineau--Vicol mechanism relevant here

For a time-periodic RDSS Leray profile `U(y,s)`, Pineau--Vicol define the time mean

\[
\bar U(y)=\langle U\rangle_s
\]

and fluctuation

\[
\widetilde U=U-\bar U.
\]

They introduce the time-independent operator

\[
\boxed{
\bar L
=-\Delta+
\left(\bar U+\frac12y\right)\cdot\nabla.
}
\]

Their Proposition 5.1 supplies a strictly positive Gaussian-type weight `w` satisfying

\[
\boxed{
\bar L^*w=0
}
\]

with upper/lower Gaussian bounds depending only on the Type-I coefficient class.

For the time-dependent Bernoulli/head-pressure

\[
\Pi
=P+\frac12|U|^2+\frac12y\cdot U,
\]

their equation (7.8), with rotation parameter `alpha`, is

\[
\bar L\Pi+|\Omega|^2
=-\widetilde U\cdot\nabla\Pi
+\frac12(\alpha\partial_\theta-\partial_s)
\left(|U|^2+y\cdot U\right).
\]

The weight is independent of `s`, so integrating over a time period removes the `partial_s` term.

The short period is then used through

\[
\boxed{
|\widetilde U|+|\nabla\widetilde U|
\lesssim S
}
\]

(up to the stated Type-I spatial weights), and this gives a small weighted enstrophy estimate of order `S+|alpha|`.

---

## 2. Current residual-active orbit

Let

\[
V(y,s)
\]

be the surviving compact recurrent W1 Leray orbit, with invariant probability measure `mu` on its compact minimal set.

No exact period is assumed.

Define the invariant mean profile

\[
\boxed{
\bar V(y)
:=\int_M V(y)\,d\mu(V).
}
\]

and the fluctuation

\[
\boxed{
\widetilde V:=V-\bar V.
}
\]

The retained uniform spatial Type-I/smoothness class passes to `bar V` by convex averaging.

Thus the same stationary drift operator

\[
\boxed{
\bar L
=-\Delta+
\left(\bar V+\frac12y\right)\cdot\nabla
}
\]

lies in the coefficient class for which the Pineau--Vicol adjoint-weight construction applies.

Hence there exists a fixed positive weight `w(y)`, independent of the orbit phase, with

\[
\boxed{
\bar L^*w=0
}
\]

and Gaussian upper/lower bounds depending only on the retained Type-I constants.

---

## 3. General time-dependent Bernoulli identity with no rotation

For an arbitrary smooth Leray trajectory

\[
V_s-\Delta V
+\frac12V
+\frac12y\cdot\nabla V
+(V\cdot\nabla)V
+\nabla P=0,
\]

set

\[
\Pi
=P+\frac12|V|^2+\frac12y\cdot V.
\]

The Pineau--Vicol computation with `alpha=0` gives

\[
\boxed{
\bar L\Pi+|\Omega|^2
=-\widetilde V\cdot\nabla\Pi
-\frac12\partial_s
\left(|V|^2+y\cdot V\right).
}
\]

This identity does not require periodicity. Periodicity was used only after the identity was derived.

---

## 4. Weighted spatial integration

Multiply by the fixed adjoint weight `w` and integrate over space.

Because

\[
\bar L^*w=0,
\]

one obtains

\[
\boxed{
\int_{\mathbb R^3}|\Omega|^2w\,dy
=-
\int\widetilde V\cdot\nabla\Pi\,w\,dy
-\frac12\frac d{ds}
\int\left(|V|^2+y\cdot V\right)w\,dy.
}
\]

The Gaussian weight makes all displayed integrals finite under the Type-I bounds.

---

## 5. Invariant measure removes the time derivative

Define the bounded smooth observable

\[
\mathcal A(V)
:=
\int
\left(|V|^2+y\cdot V\right)w\,dy.
\]

For a flow-invariant probability measure `mu`, the mean derivative of every sufficiently smooth integrable observable is zero:

\[
\int_M \frac d{ds}\mathcal A(S(s)V)\big|_{s=0}\,d\mu(V)=0.
\]

Therefore the periodic-time integration in Pineau--Vicol has the following exact invariant-measure analogue:

\[
\boxed{
\int_M\int_{\mathbb R^3}
|\Omega|^2w\,dy\,d\mu
=
-
\int_M\int_{\mathbb R^3}
\widetilde V\cdot\nabla\Pi\,w\,dy\,d\mu.
}
\]

This is the weighted-enstrophy covariance identity for the general recurrent orbit.

---

## 6. Why the RDSS Liouville step does not transfer

In Pineau--Vicol's small-period RDSS argument,

\[
\|\widetilde U\|_{weighted}
\lesssim S,
\]

and therefore the right side of the weighted identity is small.

For the current aperiodic minimal hull there is no period parameter `S`, and no theorem gives

\[
\|V-\bar V\|\ll1.
\]

Indeed the earlier no-short-return / tail-conjugacy audits imply that a nontrivial aperiodic orbit must retain a definite amount of motion/phase spread.

Thus the step

\[
\text{weighted covariance}
\Longrightarrow
\text{small weighted enstrophy}
\]

is unavailable.

The Pineau--Vicol framework does not, by itself, exclude an order-one recurrent fluctuation.

---

## 7. Positive weighted enstrophy floor on a nontrivial compact minimal set

Define

\[
Z_w(V)
:=
\int|\Omega_V|^2w\,dy.
\]

This is continuous on the retained compact smooth W1 set.

If some state in the minimal set had

\[
Z_w(V)=0,
\]

then

\[
\Omega_V\equiv0.
\]

With `div V=0` and the retained decay/Type-I class, the velocity is a harmonic irrotational divergence-free field with the admissible decay and hence is zero.

A compact minimal set containing the zero equilibrium would be the zero singleton, contradicting the inherited nontrivial checkpoint/core witness.

Therefore

\[
\boxed{
Z_{w,-}
:=\min_{V\in M}Z_w(V)>0.
}
\]

---

## 8. Pressure-gradient bound gives an orbit-fluctuation floor

Let

\[
P_w(V)
:=
\int|\nabla\Pi_V|^2w\,dy.
\]

The retained Type-I derivative/pressure estimates and Gaussian weight give

\[
\boxed{
P_{w,+}:=\sup_{V\in M}P_w(V)<\infty.
}
\]

Apply Cauchy--Schwarz to the covariance identity:

\[
Z_{w,-}
\le
\left(
\int_M\int|\widetilde V|^2w
\right)^{1/2}
\left(
\int_M\int|\nabla\Pi|^2w
\right)^{1/2}.
\]

Thus

\[
\boxed{
\int_M\int_{\mathbb R^3}
|V-\bar V|^2w\,dy\,d\mu
\ge
\frac{Z_{w,-}^2}{P_{w,+}}
>0.
}
\]

So every surviving nontrivial recurrent W1 set has a **strict weighted statistical orbit-variance floor**.

This is a valid extension of the weighted framework, but it is the opposite of the small-period RDSS conclusion: the generic survivor must stay a fixed distance from its invariant mean.

---

## 9. Relation to the residual-active branch

After M5-268/M5-269 the stationary tail branch is absent, and the canonical tail has

\[
\mathbf F(T)\ge\varepsilon_{glob}>0.
\]

M5-273 adds an independent W1-level statistical requirement:

\[
\boxed{
\mathrm{Var}_w(M)
:=
\int_M\|V-\bar V\|_{L^2(w)}^2d\mu
\ge v_w^*>0.
}
\]

Thus the remaining endpoint is simultaneously

1. residual-active at scale infinity;
2. nontrivially spread around its invariant W1 mean in a Gaussian weighted core norm;
3. nonstationary at every tail phase;
4. still critically summable in the ordinary energy budgets by M5-270.

---

## 10. What would be needed to turn this into a contradiction

A contradiction would follow from an additional mechanism forcing the weighted orbit variance to be small, for example:

- a sufficiently short exact/approximate period;
- a spectral gap for the invariant flow generator on the relevant observable class;
- a quantitative almost-self-similarity theorem that controls `V-bar V`;
- or a strict dissipative identity for the weighted variance itself.

Minimal recurrence alone supplies none of these.

In particular,

\[
\boxed{
\text{compact recurrence}
\not\Rightarrow
\|V-\bar V\|_{L^2(w)}\ll1.
}
\]

---

## 11. DSD verdict

### TRANSFERS FROM PINEAU--VICOL

- time-independent adjoint Gaussian weight built from the mean drift;
- time-dependent Bernoulli identity;
- cancellation of the total time derivative under an invariant mean;
- weighted enstrophy / fluctuation-pressure covariance identity.

### DOES NOT TRANSFER

- the small-period estimate `U-<U>=O(S)`;
- the resulting small weighted enstrophy;
- the RDSS Liouville closure.

### NEW RECURRENT CERTIFICATE

\[
\boxed{
\mathrm{Var}_w(M)\ge v_w^*>0.
}
\]

This is a useful quantitative description of the residual-active minimal survivor, but not yet a contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
