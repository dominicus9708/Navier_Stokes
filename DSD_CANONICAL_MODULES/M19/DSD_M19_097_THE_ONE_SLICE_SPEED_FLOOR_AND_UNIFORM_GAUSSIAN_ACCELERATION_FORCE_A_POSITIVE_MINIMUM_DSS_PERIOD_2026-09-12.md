# DSD M19-097 — The one-slice speed floor and uniform Gaussian acceleration force a positive minimum DSS period

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT PERIOD-LOWER-BOUND CONSEQUENCE OF M19-096 PLUS SMOOTH-CORRIDOR TIME-ACCELERATION CONTROL / EXCLUDES ARBITRARILY SMALL DSS PERIODS ON THE CERTIFIED APPLICATION LANE / DOES NOT EXCLUDE ARBITRARY LARGE-PERIOD DSS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M19-096

On a singular Type-I branch satisfying the Pineau--Vicol pressure-annulus application gate, M19-096 gives a late-time speed floor

\[
\boxed{
\|\partial_sU(s)\|_{X_G}\ge v_*>0
\qquad (s\ge s_0),
}
\]

where one may take the Gaussian-weighted Banach norm

\[
\|F\|_{X_G}
:=
\int_{\mathbb R^3}|F(y)|(1+|y|)e^{-|y|^2/8}dy.
\]

The theorem itself gives the lower bound on the growing physical-domain image `B_{e^{s/2}}`; the full Gaussian norm is no smaller, so the displayed full-space lower bound is safe.

---

## 2. Smooth-corridor acceleration bound

On an exact DSS survivor in the retained smooth compact recurrent corridor, the similarity profile is smooth and periodic in `s`.

The equation and the retained uniform higher-derivative bounds give a finite Gaussian acceleration bound

\[
\boxed{
A_*
:=
\sup_s
\|\partial_s^2U(s)\|_{X_G}
<\infty.
}
\]

This is an internal smooth-corridor bound. No universal value for `A_*` is asserted.

---

## 3. Periodicity identity

Let the exact DSS similarity period be

\[
S>0.
\]

Then

\[
U(s+S)=U(s),
\]

hence

\[
\boxed{
\int_0^S\partial_sU(s+\tau)d\tau=0.
}
\]

Fix any sufficiently late `s`.

Subtract `partial_s U(s)` inside the integral:

\[
S\,\partial_sU(s)
=-
\int_0^S
\left[
\partial_sU(s+\tau)-\partial_sU(s)
\right]d\tau.
\]

Take the `X_G` norm.

---

## 4. Acceleration controls turning of the velocity vector

By the fundamental theorem of calculus,

\[
\|\partial_sU(s+\tau)-\partial_sU(s)\|_{X_G}
\le
A_*\tau.
\]

Therefore

\[
S\|\partial_sU(s)\|_{X_G}
\le
\int_0^S A_*\tau d\tau
=
\frac12A_*S^2.
\]

Since the singular survivor obeys

\[
\|\partial_sU(s)\|_{X_G}\ge v_*,
\]

we obtain

\[
\boxed{
S\ge\frac{2v_*}{A_*}.
}
\]

Thus a periodic singular survivor cannot traverse an arbitrarily short loop in similarity time while maintaining the one-slice speed floor and a bounded acceleration.

---

## 5. Lower bound for the DSS scaling factor

For backward DSS,

\[
S=2\log\lambda.
\]

Hence

\[
\boxed{
\log\lambda\ge\frac{v_*}{A_*},
}
\]

or

\[
\boxed{
\lambda\ge\exp\left(\frac{v_*}{A_*}\right)>1.
}
\]

This reproduces, at the structural level, why sufficiently near-one DSS periods are incompatible with the one-slice regularity mechanism.

It does not supply the sharp constants of the external near-one DSS theorem.

---

## 6. Relation to Pineau--Vicol Theorem 1.7

Pineau--Vicol prove a direct RDSS/DSS Liouville theorem when the scaling factor is sufficiently close to one under their Type-I hypotheses, with parameter ranges stated in Theorem 1.7.

M19-097 is not a replacement for that theorem.

It records the internal dynamical reason visible from Theorem 1.9:

\[
\boxed{
\text{singular survivor speed floor}
+
\text{bounded turning rate}
\Longrightarrow
\text{minimum recurrent period}.
}
\]

---

## 7. What remains

The hard DSS branch is now restricted to periods

\[
S\ge S_*:=2v_*/A_*>0.
\]

Equivalently its nonzero log-periodic critical tail has period

\[
L=S/2\ge v_*/A_*.
\]

But there is no upper bound on `S`, and nothing in this argument excludes a finite or large-period log-periodic orbit.

Therefore

\[
\boxed{
\text{small-period DSS removed}
\neq
\text{arbitrary DSS removed}.
}
\]

---

## 8. Firewall

The estimate uses a uniform `X_G` bound on `partial_s^2 U`.

It must not be applied to a noncompact or derivative-decompactifying branch without first certifying that bound.

Failure of the acceleration bound is itself a time-derivative/compactness exit, not a silent contradiction.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
