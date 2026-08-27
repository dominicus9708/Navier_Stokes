# DSD M5-123 — Log-Cylinder Rotational Countermodel and Factor-Rigidity Pruning

Date: 2026-08-27

Status: **EXPLICIT DIVERGENCE-FREE ZERO-FLUX LOG-CYLINDER COUNTERMODEL / ARBITRARY BOUNDED RECURRENT CUBIC-DENSITY DYNAMICS IS COMPATIBLE WITH ALL PURE TAIL-FACTOR GEOMETRIC CONSTRAINTS / FACTOR RIGIDITY REQUIRES A NAVIER--STOKES-SPECIFIC RESIDUAL/QUOTIENT COUPLING / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-122 reduced the non-exact critical anomaly to the tail-factor inequality

\[
\overline{\mathcal E}
-\frac{2\nu}{3}\mathcal L_D\overline{\mathcal K}
\ge\frac\nu3\mathfrak c.
\]

The tail cylinder also obeys

\[
\partial_\rho\Phi_r+\Phi_r+\operatorname{div}_{S^2}\Phi_\tau=0
\]

and zero spherical flux.

Before searching for a rigidity theorem from these relations alone, DSD requires a countermodel audit: can the pure factor constraints themselves support nontrivial recurrent positive cubic density?

The answer is yes.

---

## 2. A divergence-free rotational sphere mode

Fix a nonzero constant vector `a in R3` and define on the sphere

\[
\boxed{
F(\theta):=a\times\theta.
}
\]

Then `F` is tangent to `S2`:

\[
F\cdot\theta=0.
\]

It is a Killing/rotation field on the round sphere and therefore

\[
\boxed{
\operatorname{div}_{S^2}F=0.
}
\]

---

## 3. Arbitrary log-radius modulation

Let

\[
A:\mathbb R\to\mathbb R
\]

be any bounded smooth function and define

\[
\boxed{
\Phi_A(\rho,\theta):=A(\rho)F(\theta).
}
\]

Here

\[
(\Phi_A)_r=0,
\qquad
(\Phi_A)_\tau=\Phi_A.
\]

Therefore

\[
\partial_\rho(\Phi_A)_r
+(\Phi_A)_r
+\operatorname{div}_{S^2}(\Phi_A)_\tau
=0+0+A(\rho)\operatorname{div}_{S^2}F
=0.
\]

Hence the corresponding physical-space critical field

\[
\boxed{
T_A(Y)
=|Y|^{-1}
A(\log|Y|)
F(Y/|Y|)
}
\]

is divergence free on `R3\{0}`.

Because it is everywhere tangent to spheres,

\[
\boxed{
\int_{|Y|=r}T_A\cdot n\,dS=0
}
\]

identically.

If `A` is bounded, the Type-I critical envelope

\[
|T_A(Y)|\lesssim|Y|^{-1}
\]

also holds.

---

## 4. Cubic factor density

The one-slice cubic observable is

\[
\begin{aligned}
\mathfrak c_A(\rho)
&=\int_{S^2}|\Phi_A(\rho,\theta)|^3d\theta\\
&=|A(\rho)|^3
\int_{S^2}|a\times\theta|^3d\theta.
\end{aligned}
\]

Thus

\[
\boxed{
\mathfrak c_A(\rho)
=C_a|A(\rho)|^3,
\qquad C_a>0.
}
\]

Consequently the factor can carry essentially arbitrary bounded recurrent positive cubic-density patterns.

Examples include:

- periodic `A`, giving log-periodic/DSS-type density;
- quasiperiodic `A`;
- an aperiodic recurrent `A` obtained from any compact minimal translation hull of a smooth bounded scalar function.

No pure divergence-free or zero-flux obstruction removes these examples.

---

## 5. The factor residual inequality also does not close them by itself

The M5-122 inequality is an inequality among factor observables:

\[
\overline{\mathcal E}
-\frac{2\nu}{3}\mathcal L_D\overline{\mathcal K}
\ge\frac\nu3\mathfrak c.
\]

As an abstract translation-system constraint, it is compatible with the rotational examples: choose for instance a bounded `overline K` and any nonnegative `overline E` satisfying the displayed lower bound.

Therefore

\[
\boxed{
\text{translation dynamics}
+\text{divergence free}
+\text{zero flux}
+\text{nonnegative factor payer}
}
\]

do not constitute a rigidity theorem.

The missing information is that `overline E` and `overline K` are not arbitrary factor labels: they come from an actual Navier--Stokes W1 core and its canonical descendant construction.

---

## 6. DSD four-chain audit

### Formation — GREEN

The countermodel is formed directly as a punctured critical field; no claim is made that it is an NSE canonical tail.

### Axis — GREEN

It uses a purely tangential spherical channel, so zero radial flux is automatic rather than canceled by hidden source/sink pieces.

### Static aggregation — GREEN

Positive cubic density is carried by tangential amplitude and does not conflict with signed flux cancellation.

### Dynamics — GREEN

Arbitrary recurrent `A(rho)` shows that translation recurrence itself is not restrictive enough.

### Cross-audit — GREEN

The countermodel is used only to refute sufficiency of the reduced factor axioms.  It is not promoted to an NSE solution.

---

## 7. Permanent RED route

The following proof strategy is now closed:

\[
\boxed{
\text{positive log-cylinder cubic density}
+\text{divergence free}
+\text{zero spherical flux}
\Longrightarrow\text{contradiction}.
}
\]

It is false even inside a very simple rotational family.

Likewise, periodicity or aperiodic recurrence of the tail density alone cannot close W1.

---

## 8. What PDE information is still missing?

For an actual canonical tail `T`, the field is generated from W1 descendants and has a Navier--Stokes residual

\[
\boxed{
F_T
:=\nu\Delta T
-\mathbb P\nabla\cdot(T\otimes T).
}
\]

The finite-energy quotient `Q=V-B_T` is forced by the corresponding cutoff residual.

Therefore the next admissible rigidity input must involve at least one of:

1. the log-cylinder representation of `F_T`;
2. a stress/momentum-flux identity connecting `F_T` to the finite-core payer;
3. the forced `L2 cap L3` quotient equation;
4. the scale-infinity/prelimit condition that distinguishes actual canonical tails from arbitrary divergence-free critical fields.

Pure factor geometry is exhausted.

---

## 9. Next calculation

Compute `F_T` exactly in log-cylinder variables.

The leading field has the form

\[
T=r^{-1}\Phi(\rho,\theta),
\]

so

\[
F_T=r^{-3}\mathfrak F(\Phi,\partial_\rho\Phi,\nabla_{S^2}\Phi,\ldots).
\]

The next DSD target is to identify the scale-invariant sphere/log-radius stress functional `mathfrak F` and determine which part is:

- a log derivative/coboundary;
- a spherical divergence that integrates away;
- or a genuine nonzero momentum/pressure defect that must be supplied by the W1 quotient/core.

That is the first NSE-specific factor-rigidity gate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
