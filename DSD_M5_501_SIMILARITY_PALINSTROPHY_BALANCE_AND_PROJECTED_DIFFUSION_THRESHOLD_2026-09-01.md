# DSD M5-501 — Similarity palinstrophy balance constrains the projected-diffusion ratchet component

Date: 2026-09-01

Status: **SECOND-DERIVATIVE LEDGER / DIFFERENTIATING THE BACKWARD-SIMILARITY VORTICITY EQUATION GIVES THE EXACT PALINSTROPHY BALANCE `1/2 P' + 3/4 P + H = N_P`, WITH `H=||Delta W||_2^2` AND A SIGN-INDEFINITE DERIVATIVE NONLINEARITY / CALDERON--ZYGMUND AND SOBOLEV INTERPOLATION GIVE `|N_P| <= C E^(1/4) P^(3/4) H^(1/2)`, HENCE AFTER YOUNG `1/2 P' + 3/4 P + 1/2 H <= C E^(1/2) P^(3/2)` / THE M5-500 PROJECTED-DIFFUSION BRANCH HAS `mean(H)>0`, SO A RECURRENT COMPONENT MUST MAINTAIN A NONTRIVIAL DERIVATIVE-NONLINEARITY CAPACITY; UNDER A BOUNDED PALINSTROPHY CAP THIS PRODUCES A QUANTITATIVE `E*P` THRESHOLD / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity vorticity equation

Use

\[
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
=
(W\cdot\nabla)U
+\Delta W,
\]

with

\[
\nabla\cdot U=0,
\qquad
\nabla\cdot W=0.
\]

Define

\[
E:=\|W\|_2^2,
\qquad
P:=\|\nabla W\|_2^2,
\qquad
H:=\|\Delta W\|_2^2.
\]

On whole space, `H` is equivalent to the full `L2` Hessian norm by Fourier identities.

---

## 2. Differentiate the equation

Write the nonlinear vorticity term as

\[
\mathcal N
:=(W\cdot\nabla)U-(U\cdot\nabla)W.
\]

Then

\[
\partial_\theta W
+W
+\frac12y\cdot\nabla W
-\Delta W
=
\mathcal N.
\]

Take one spatial derivative and the global `L2` inner product with `grad W`.

The time term gives

\[
\frac12P'.
\]

---

## 3. Linear similarity coefficient

The explicit `+W` term contributes

\[
P.
\]

For the dilation term,

\[
\frac12
\int
\nabla W:
\nabla(y\cdot\nabla W)dy.
\]

Since

\[
\nabla(y\cdot\nabla W)
=
\nabla W+y\cdot\nabla(\nabla W),
\]

and

\[
\int y\cdot\nabla|\nabla W|^2dy
=-3P,
\]

we obtain

\[
\frac12
\int
\nabla W:
\nabla(y\cdot\nabla W)dy
=
-\frac14P.
\]

Thus the net linear coefficient is

\[
P-\frac14P
=
\boxed{\frac34P}.
\]

The Laplacian contributes

\[
\boxed{H}.
\]

---

## 4. Exact similarity-palinstrophy identity

Define

\[
\boxed{
\mathcal N_P
:=
\int
\nabla\mathcal N:
\nabla W\,dy.
}
\]

Then

\[
\boxed{
\frac12P'
+
\frac34P
+
H
=
\mathcal N_P.
}
\]

Unlike the linear damping and fourth-order dissipation, `mathcal N_P` has no definite sign.

---

## 5. Structure of the derivative nonlinearity

Expanding one derivative of

\[
(W\cdot\nabla)U-(U\cdot\nabla)W
\]

produces terms of schematic forms

\[
\nabla W\,\nabla U\,\nabla W
\]

and

\[
W\,\nabla^2U\,\nabla W.
\]

By Holder,

\[
|\mathcal N_P|
\le
C
\left(
\|\nabla U\|_3
\|\nabla W\|_3^2
+
\|W\|_3
\|\nabla^2U\|_3
\|\nabla W\|_3
\right).
\]

Calderon--Zygmund gives

\[
\|\nabla U\|_3
\le C\|W\|_3,
\]

and

\[
\|\nabla^2U\|_3
\le C\|\nabla W\|_3.
\]

Therefore

\[
\boxed{
|\mathcal N_P|
\le
C\|W\|_3
\|\nabla W\|_3^2.
}
\]

---

## 6. Critical interpolation

As in M5-494,

\[
\|W\|_3
\le
C E^{1/4}P^{1/4}.
\]

For the gradient,

\[
\|\nabla W\|_3
\le
\|\nabla W\|_2^{1/2}
\|\nabla W\|_6^{1/2}.
\]

Sobolev and the whole-space Hessian/Laplacian equivalence give

\[
\|\nabla W\|_6
\le C\|\nabla^2W\|_2
\le C H^{1/2}.
\]

Hence

\[
\boxed{
\|\nabla W\|_3
\le
C P^{1/4}H^{1/4}.
}
\]

Substituting,

\[
\boxed{
|\mathcal N_P|
\le
C E^{1/4}P^{3/4}H^{1/2}.
}
\]

This is the scale-compatible derivative-production estimate.

---

## 7. Absorb half of the fourth-order dissipation

Young's inequality gives

\[
C E^{1/4}P^{3/4}H^{1/2}
\le
\frac12H
+
C_1E^{1/2}P^{3/2}.
\]

Thus

\[
\boxed{
\frac12P'
+
\frac34P
+
\frac12H
\le
C_1E^{1/2}P^{3/2}.
}
\]

This is the audited second-derivative inequality.

---

## 8. Invariant average

On a recurrent invariant component, boundedness/integrability of the retained palinstrophy observable gives

\[
\langle P'\rangle=0.
\]

Therefore

\[
\boxed{
\frac34\langle P\rangle
+
\frac12\langle H\rangle
\le
C_1
\left\langle
E^{1/2}P^{3/2}
\right\rangle.
}
\]

With the enstrophy cap

\[
E\le Z_*,
\]

this becomes

\[
\boxed{
\frac34\langle P\rangle
+
\frac12\langle H\rangle
\le
C_1Z_*^{1/2}
\langle P^{3/2}\rangle.
}
\]

The right side involves a higher palinstrophy moment and is not controlled by `mean(P)` alone.

---

## 9. Projected-diffusion ratchet supplies positive `H`

M5-500 gives on the projected-diffusion branch

\[
\left\langle
H_{proj}
\right\rangle
>0,
\]

where

\[
H_{proj}
:=
\int
|(I-\xi\otimes\xi)\Delta W|^2dy.
\]

Since orthogonal projection cannot increase norm,

\[
H_{proj}\le H.
\]

Therefore

\[
\boxed{
\langle H\rangle
\ge
\langle H_{proj}\rangle
=:h_{proj}>0.
}
\]

Thus a projected-diffusion ratchet component must continuously regenerate second derivatives against the explicit fourth-order dissipation ledger.

---

## 10. Bounded-palinstrophy subbranch

Suppose the recurrent component also has a uniform global palinstrophy cap

\[
\boxed{
P(\theta)\le P_*<\infty.
}
\]

Then

\[
P^{3/2}
\le
P_*^{1/2}P.
\]

Hence

\[
\boxed{
\frac34\langle P\rangle
+
\frac12\langle H\rangle
\le
C_1(Z_*P_*)^{1/2}
\langle P\rangle.
}
\]

Because the left contains a strictly positive `H` term, the product `Z_*P_*` cannot be arbitrarily small.

In particular, dropping `H` but keeping `mean(P)>0` gives the necessary condition

\[
\boxed{
C_1(Z_*P_*)^{1/2}
\ge\frac34.
}
\]

Thus

\[
\boxed{
Z_*P_*
\ge
\frac{9}{16C_1^2}
=:K_{EP}>0.
}
\]

The projected-diffusion branch obeys an even stronger inequality once `h_proj` is retained.

---

## 11. Explicit projected-diffusion threshold

Using

\[
\langle P\rangle\le P_*
\]

and

\[
\langle H\rangle\ge h_{proj},
\]

we obtain

\[
\frac12h_{proj}
\le
C_1Z_*^{1/2}P_*^{3/2}.
\]

Therefore

\[
\boxed{
P_*
\ge
\left(
\frac{h_{proj}}{2C_1Z_*^{1/2}}
\right)^{2/3}.
}
\]

Equivalently a fixed projected-diffusion recurrence forces a quantitative palinstrophy-amplitude threshold at any fixed enstrophy cap.

---

## 12. Unbounded-palinstrophy alternative

If no finite `P_*` exists on the component, then

\[
\boxed{
\sup_\theta P(\theta)=\infty.
}
\]

This is a genuine scale-critical derivative-mass/frequency escalation in the similarity representation.

It should be classified separately from the M5-392 parent-scale pointwise derivative firewall: M5-392 excludes unbounded fixed-order **pointwise normalized derivatives on one first-hitting stage**, whereas global similarity palinstrophy can diverge through spatial occupancy/tail/frequency mass.

Thus

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{P}^{global}
\lor
\{Z_*P_*\ge K_{EP}\text{ and }P_*\ge P_{min}^{proj}\}.
}
\]

---

## 13. DSD ledger interpretation

The first enstrophy ledger was

\[
\text{axial stretching}
\to
\text{enstrophy maintenance + palinstrophy}.
\]

The projected-diffusion ratchet activates the next ledger:

\[
\text{derivative nonlinearity}
\to
\text{palinstrophy maintenance + fourth-order dissipation}.
\]

The survivor must therefore pay a nested hierarchy of critical costs rather than merely repeat one projective event.

---

## 14. Highest-value next targets

### H2 route

If global `P` is bounded, derive the similarity evolution of

\[
H=\|\Delta W\|_2^2
\]

to determine whether recurrent projected diffusion forces a third derivative ledger with an absorbable positive `||grad Delta W||_2^2` term.

### Tail route

If `P` is unbounded through remote spatial occupancy rather than local amplitude, reconnect this derivative-mass escape to M5-496's remote-tail concentration-compactness branch.

A successful iteration of the derivative ledger could either close bounded derivative hierarchies or isolate an explicit infinite Sobolev-cascade endpoint.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
