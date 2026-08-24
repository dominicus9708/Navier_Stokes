# DSD Direct Betchov Recurrent Frequency Barrier

Date: 2026-08-25

Status: **TAIL-INDEPENDENT / TYPE-I-CONSTANT-INDEPENDENT RECURRENT FREQUENCY BARRIER DERIVED / EXPLICIT ENSTROPHY THRESHOLD DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

Work on any nonzero recurrent Leray state for which

\[
0<Z(s):=\|W(s)\|_2^2\le Z_+<\infty,
\]

with sufficient smoothness/decay for the whole-space Betchov identity. The critical `1/r` velocity tail is allowed because its strain and vorticity decay fast enough for the cubic derivative integrals and boundary terms below.

Set

\[
Q(s):=\|\nabla W(s)\|_2^2.
\]

No global velocity `L3` bound is assumed.

---

## 2. Exact recurrent enstrophy balance

In backward Leray variables,

\[
\boxed{
\frac12Z_s
+\frac14Z
+\nu Q
=\mathcal P,
}
\]

where

\[
\mathcal P
:=
\int_{\mathbb R^3}W^T\Sigma W\,dy.
\]

On an invariant recurrent average, the bounded derivative term vanishes:

\[
\boxed{
\frac14\overline Z
+\nu\overline Q
=\overline{\mathcal P}.
}
\]

The active-core recurrence guarantees

\[
\overline Z>0.
\]

---

## 3. Use the full Betchov identity, not the residual split

For a smooth whole-space incompressible field,

\[
\boxed{
\mathcal P
=-4\int_{\mathbb R^3}\det\Sigma\,dy.
}
\]

For a symmetric trace-free `3 x 3` matrix `S` with eigenvalues summing to zero,

\[
\boxed{
|\det S|
\le
\frac1{3\sqrt6}|S|^3.
}
\]

Equality is attained by an axisymmetric max-mid/extreme spectrum proportional to

\[
(-2,1,1)
\]

up to sign/permutation.

Therefore

\[
\boxed{
\mathcal P
\le
\frac4{3\sqrt6}
\int|\Sigma|^3dy.
}
\]

This controls the **entire** enstrophy production, rather than only the negative-middle residual.

---

## 4. Sharp Sobolev interpolation

Use

\[
\|f\|_6
\le
C_S\|\nabla f\|_2,
\qquad
C_S
=
\frac1{\sqrt3}
\left(\frac2\pi\right)^{2/3}.
\]

Interpolation gives

\[
\|\Sigma\|_3^3
\le
\|\Sigma\|_2^{3/2}
\|\Sigma\|_6^{3/2}
\le
C_S^{3/2}
\|\Sigma\|_2^{3/2}
\|\nabla\Sigma\|_2^{3/2}.
\]

Whole-space Fourier identities yield

\[
\|\Sigma\|_2^2=\frac12Z,
\qquad
\|\nabla\Sigma\|_2^2=\frac12Q.
\]

Thus

\[
\|\Sigma\|_3^3
\le
\frac{C_S^{3/2}}{2^{3/2}}
Z^{3/4}Q^{3/4}.
\]

Combining with Betchov,

\[
\boxed{
\mathcal P
\le
C_D Z^{3/4}Q^{3/4},
}
\]

where

\[
\boxed{
C_D
:=
\frac{C_S^{3/2}}{3\sqrt3}
=
\frac{2}{\pi 3^{9/4}}
\approx0.05374738014.
}
\]

This coefficient is one quarter of the coefficient that appeared in the previous full-gradient Betchov-residual estimate because the present argument uses the trace-free strain determinant directly.

---

## 5. Recurrent weighted Jensen reduction

Define

\[
\lambda(s):=\frac{Q(s)}{Z(s)},
\qquad
\bar\lambda:=\frac{\overline Q}{\overline Z}.
\]

Then

\[
Z^{3/4}Q^{3/4}
=Z^{3/2}\lambda^{3/4}
\le
Z_+^{1/2}Z\lambda^{3/4}.
\]

Using the probability weight proportional to `Z(s) ds` and concavity of `x^(3/4)`,

\[
\frac{\overline{Z\lambda^{3/4}}}{\overline Z}
\le
\left(
\frac{\overline{Z\lambda}}{\overline Z}
\right)^{3/4}
=
\bar\lambda^{3/4}.
\]

Hence

\[
\boxed{
\frac{\overline{\mathcal P}}{\overline Z}
\le
C_DZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

The exact recurrent enstrophy balance now gives

\[
\boxed{
\frac14
+\nu\bar\lambda
\le
C_DZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

This is the **Direct Betchov Recurrent Frequency Barrier (DBRFB)**.

Notably, it contains neither

- the continuous Type-I constant `K_I`,
- first-hitting stage length `L_+`,
- velocity `L3`,
- critical tail amplitude,
- nor a Betchov residual fraction.

---

## 6. Exact algebraic frequency window

Set

\[
x:=\bar\lambda^{1/4}\ge0,
\qquad
b:=C_DZ_+^{1/2}.
\]

Then every recurrent survivor must satisfy

\[
\boxed{
F_D(x)
:=
\nu x^4-bx^3+\frac14
\le0.
}
\]

The unique positive critical point is

\[
\boxed{
x_D^*=\frac{3b}{4\nu}.}
\]

It is the global positive minimum.

At that point,

\[
F_D(x_D^*)
=
\frac14
-
\frac{27}{256}
\frac{b^4}{\nu^3}.
\]

Since

\[
C_D^4
=
\frac{16}{19683\pi^4},
\]

we obtain the exact simplification

\[
\boxed{
F_D(x_D^*)
=
\frac14
-
\frac{Z_+^2}
{11664\pi^4\nu^3}.
}
\]

---

## 7. Explicit recurrent-enstrophy threshold

A nonzero recurrent bounded-`Z` state can exist only if the algebraic window is nonempty. Therefore necessarily

\[
F_D(x_D^*)\le0.
\]

Hence

\[
\boxed{
Z_+^2
\ge
2916\pi^4\nu^3.
}
\]

Equivalently,

\[
\boxed{
Z_+
\ge
54\pi^2\nu^{3/2}.
}
\]

Numerically for `nu=1`,

\[
\boxed{
Z_+
\ge
54\pi^2
\approx532.958638.
}
\]

Thus:

\[
\boxed{
Z_+<54\pi^2\nu^{3/2}
\quad\Longrightarrow\quad
\text{no nonzero recurrent bounded-}Z\text{ Leray survivor}.
}
\]

This threshold follows from the full Betchov identity and recurrent similarity tax alone.

---

## 8. Interpretation

The mechanism is a strict scaling mismatch.

The recurrent Leray equation requires a mean production payment

\[
\frac14\overline Z+
u\overline Q.
\]

At high mean frequency, the required viscous payment grows linearly in

\[
\bar\lambda,
\]

whereas the strongest Betchov/Sobolev production available at bounded enstrophy grows only like

\[
Z_+^{1/2}\bar\lambda^{3/4}.
\]

At low frequency, the fixed similarity tax `1/4` cannot be paid.

Hence only a finite intermediate frequency window is possible, and that window disappears entirely below the explicit `Z_+` threshold.

---

## 9. Relation to previous Betchov residual window

The previous Young-free residual window was

\[
\nu\bar\lambda
+\frac14-\frac{K_I}{2}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4},
\]

with

\[
C_B=4C_D.
\]

The direct full-Betchov gate is stronger in the present recurrent whole-space setting:

\[
\boxed{
\frac14+
u\bar\lambda
\le
C_DZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

The residual split remains useful for localized/branchwise interpretations, but it is not the sharpest global recurrent scalar gate.

---

## 10. Compatibility with the critical tail

For the borderline passive tail

\[
|V(y)|\sim |y|^{-1},
\]

one has

\[
|\Sigma|\sim|y|^{-2},
\qquad
|W|\sim|y|^{-2}.
\]

Hence

\[
\int|\Sigma|^3<\infty,
\qquad
Z<\infty,
\qquad
Q<\infty.
\]

The Betchov boundary terms vanish at infinity at this decay rate. Therefore the critical non-`L3` velocity tail does not invalidate DBRFB.

It may help make `Z_+` large, but it cannot remove the frequency barrier.

---

## 11. DSD audit

DBRFB uses only the finite formed channels

\[
(Z,Q,\mathcal P,\det\Sigma),
\]

and a recurrent invariant average.

No infinite derivative hierarchy, global velocity `L3` object, or genealogy assumption enters the proof.

---

## 12. Updated frontier

The bounded-`Z` recurrent branch is now split quantitatively into

\[
\boxed{
Z_+<54\pi^2\nu^{3/2}
\Longrightarrow
\text{S-closed},
}
\]

and

\[
\boxed{
Z_+\ge54\pi^2\nu^{3/2}
\Longrightarrow
\text{large-normalized-enstrophy recurrent survivor only}.
}
\]

Therefore the remaining bounded-`Z` route is no longer an arbitrary finite-enstrophy recurrent class. It must carry a quantitatively large normalized enstrophy reservoir.

This aligns directly with the separately derived unbounded-`Z` moment/kinetic routing: **large normalized enstrophy is now the common quantitative obstruction on both sides of the bounded/unbounded split.**

The next high-leverage question is whether such a large `Z_+` can remain spatially/tail distributed while the first-hitting core stays analytic and recurrent without entering `H_remote` or `T`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
