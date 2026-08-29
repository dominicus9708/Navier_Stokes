# DSD M5-212 — Interior Hodge–Caccioppoli Reduction and Route-Priority Audit

Date: 2026-08-29

Parent: `DSD_M5_211_DIVERGENCE_FREE_EXTERIOR_LOCALIZATION_AND_FLAT_FORCING_FIREWALL_2026-08-29.md`

Status: **POSITIVE LOCAL REDUCTION / ON EVERY NESTED FIXED EXTERIOR, THE DERIVATIVE COUPLING `∇Z` IN THE RELATIVE-VORTICITY EQUATION IS CONTROLLED BY `η=curl Z` PLUS A LOWER-ORDER `Z` TERM THROUGH AN EXACT LOCAL HODGE–CACCIOPPOLI ESTIMATE / THE ONLY GENUINE EXTERIOR HODGE FREEDOM LEFT IS THE ZEROTH-ORDER CURL-FREE/DIVERGENCE-FREE HARMONIC COMPONENT / THIS MAKES THE FIXED-EXTERIOR PARABOLIC–ELLIPTIC BU ROUTE STRICTLY NARROWER THAN THE WHOLE-SPACE ARBITRARY-HARDY-AMPLITUDE ROUTE / HOWEVER THE HARMONIC COMPONENT IS NOT YET ELIMINATED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Relative exterior system

Let

\[
\Omega_R:=\{|x-x_*|>R\}
\]

and

\[
Z=u^V-u^W,
\qquad
\eta=\nabla\times Z.
\]

Then

\[
\nabla\cdot Z=0
\]

and the relative vorticity equation is

\[
\boxed{
\eta_t-\nu\Delta\eta
+(u^V\cdot\nabla)\eta
-(\eta\cdot\nabla)u^V
+(Z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)Z
=0.
}
\]

On every fixed exterior the coefficients

\[
u^V,
\nabla u^V,
\omega^W,
\nabla\omega^W
\]

are bounded uniformly up to the terminal time.

The difficulty is the last two terms, which contain `Z` and `∇Z` rather than only `η`.

---

## 2. Exact whole-space Hodge identity after a cutoff

Choose

\[
R<R_1<R_2
\]

and a smooth cutoff `χ` such that

\[
\chi=0\quad\text{on }B_{R_1},
\qquad
\chi=1\quad\text{outside }B_{R_2},
\]

with

\[
|\nabla\chi|\le C(R_2-R_1)^{-1}.
\]

For a compactly supported smooth vector field `F` on `R^3`,

\[
\int_{\mathbb R^3}|\nabla F|^2
=
\int_{\mathbb R^3}
\bigl(|\nabla\times F|^2+|\nabla\cdot F|^2\bigr).
\]

Apply this to a large-radius truncation of `χZ` and pass to the limit using the finite-energy same-tail property. Since

\[
\nabla\times(\chi Z)
=
\chi\eta+\nabla\chi\times Z,
\]

and

\[
\nabla\cdot(\chi Z)
=
\nabla\chi\cdot Z,
\]

we obtain

\[
\|\nabla(\chi Z)\|_2^2
\le
2\|\chi\eta\|_2^2
+C\|\nabla\chi\,Z\|_2^2.
\]

Because `χ=1` on `Omega_(R2)`,

\[
\boxed{
\|\nabla Z\|_{L^2(\Omega_{R_2})}
\le
C\|\eta\|_{L^2(\Omega_{R_1})}
+
\frac{C}{R_2-R_1}
\|Z\|_{L^2(A_{R_1,R_2})}.
}
\]

Here

\[
A_{R_1,R_2}
:=
\{R_1<|x-x_*|<R_2\}.
\]

This is a boundary-condition-free interior/exterior Hodge–Caccioppoli estimate.

Status: **PROVED.**

---

## 3. Consequence for the vorticity equation

On `Omega_(R2)`, boundedness of the fixed-exterior coefficients gives

\[
\begin{aligned}
\|(\omega^W\cdot\nabla)Z\|_{L^2(\Omega_{R_2})}
&\le
\|\omega^W\|_{L^\infty(\Omega_{R_2})}
\|\nabla Z\|_{L^2(\Omega_{R_2})}\\
&\le
C_R\|\eta\|_{L^2(\Omega_{R_1})}
+C_R\|Z\|_{L^2(A_{R_1,R_2})}.
\end{aligned}
\]

Likewise

\[
\|(Z\cdot\nabla)\omega^W\|_{L^2(\Omega_{R_2})}
\le
C_R\|Z\|_{L^2(\Omega_{R_2})}.
\]

Hence the derivative coupling is no longer independent:

\[
\boxed{
\|P\eta\|_{L^2(\Omega_{R_2})}
\le
C_R\bigl(
\|\nabla\eta\|_{L^2(\Omega_{R_1})}
+
\|\eta\|_{L^2(\Omega_{R_1})}
+
\|Z\|_{L^2(\Omega_{R_1})}
\bigr)
}
\]

up to a harmless adjustment of the nested radii.

Thus the only genuinely non-vorticity quantity still present is **zeroth-order `Z`**.

---

## 4. Why zeroth-order Z cannot be removed by local Hodge alone

If

\[
\eta=0,
\qquad
\nabla\cdot Z=0
\]

on an exterior domain, then

\[
-\Delta Z=0.
\]

There are nonzero finite-energy exterior harmonic vector fields.

For example, away from the origin,

\[
Z_h=\nabla\frac1{|x-x_*|}
\]

satisfies

\[
\nabla\times Z_h=0,
\qquad
\nabla\cdot Z_h=0,
\qquad
Z_h\in L^2(\Omega_R).
\]

Therefore no estimate of the form

\[
\boxed{
\|Z\|_{L^2(\Omega_{R_2})}
\le
C_R\|\eta\|_{L^2(\Omega_{R_1})}
}
\]

can hold without an additional condition controlling the exterior harmonic sector.

This is the exact residual Hodge obstruction.

---

## 5. Terminal flatness does not remove the harmonic sector dynamically

M5-145 gives, on every fixed punctured compact set,

\[
\|Z(t)\|_{C^k}
=O((T_*-t)^N)
\quad\text{for every }N.
\]

This forces every fixed-annulus harmonic coefficient to be terminal-flat if such a decomposition is made.

It does **not** imply that those coefficient functions vanish at earlier times.

A nonzero coefficient `c(t)` can be flat at `T_*`.

Hence

\[
\boxed{
\text{terminal-flat harmonic amplitude}
\not\Rightarrow
\text{zero harmonic amplitude}.
}
\]

The velocity equation or a genuine terminal-backward Stokes estimate is still needed.

---

## 6. Route comparison

### Route A — whole-space polynomial/CZ

Advantages:

- no artificial boundary;
- Leray pressure/CZ is controlled;
- transport-weight commutator is zeroth order.

Remaining obstruction:

\[
\boxed{
\text{arbitrary-amplitude Hardy-critical common-tail stretching}.
}
\]

This is a scale-critical principal-operator problem.

### Route B — fixed-exterior parabolic–elliptic/Stokes

Advantages:

- all background coefficients are bounded;
- the `1/r` / `1/r^2` critical amplitude disappears as a coefficient-size issue;
- `∇Z` is already reduced to `η+Z` by Section 2.

Remaining obstruction:

\[
\boxed{
\text{zeroth-order exterior harmonic velocity sector / terminal Stokes coupling}.
}
\]

This is a finite-radius boundary-free continuation problem rather than an arbitrary-amplitude critical-form problem.

Therefore the proof-tree priority is

\[
\boxed{
\text{Route B first.}
}
\]

---

## 7. Minimal remaining exterior lemma

The M5-183 target can now be sharpened.

It is enough to prove a terminal backward uniqueness estimate for the pair `η,Z` where

\[
P\eta
=A_1\nabla\eta+A_0\eta+C_0Z
\]

after the `∇Z` term is absorbed by the nested Hodge–Caccioppoli estimate, together with

\[
-\Delta Z=\nabla\times\eta,
\qquad
\nabla\cdot Z=0,
\]

and exact terminal zero.

The only role of the elliptic component that is not already elementary is to control the harmonic kernel represented by the zeroth-order `Z` term.

---

## 8. DSD audit

### Formation — GREEN

The cutoff Hodge identity is standard and uses only actual finite-energy fields.

### Axis — GREEN

Derivative reconstruction and harmonic reconstruction are separated.

### Static aggregation — GREEN

Control of `∇Z` is not promoted to control of `Z`.

### Dynamics — YELLOW

The terminal evolution of the harmonic sector remains open.

### Cross-audit — GREEN

This refines rather than contradicts M5-183 and M5-208.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]