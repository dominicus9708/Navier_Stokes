# Compactness-rigidity gap for sharp scalar Sobolev saturation

Date: 2026-08-13

Status: **CONDITIONAL COMPACTNESS-RIGIDITY LEMMA + CLASSICAL AUBIN--TALENTI EQUALITY ANCHOR**.

The source estimate for vorticity magnitude uses the critical scalar Sobolev inequality in three dimensions.  On a strongly `H1`-compact nontrivial cutoff family, this critical inequality cannot approach the whole-space sharp constant, because that would create a compactly supported sharp extremizer, whereas the classical whole-space extremizers are the Aubin--Talenti bubbles.

External anchor:

- Giorgio Talenti, *Best constant in Sobolev inequality*, Annali di Matematica Pura ed Applicata 110 (1976), 353--372, DOI 10.1007/BF02418013.

No new classification of Sobolev extremizers is claimed here.

---

## 1. Sharp scalar Sobolev ratio

In three dimensions let `S_*` denote the sharp whole-space constant in

\[
\boxed{
\|f\|_{L^6(\mathbb R^3)}
\le
S_*\|\nabla f\|_{L^2(\mathbb R^3)}.
}
\]

Choose a fixed normalized ball `B_R` and let

\[
f_j\in H_0^1(B_R),
\qquad f_j\not\equiv0.
\]

Extend `f_j` by zero to `R^3`.  Define

\[
\boxed{
\mathcal R_S[f_j]
=
\frac{\|f_j\|_6}
{S_*\|\nabla f_j\|_2}
\le1.
}
\]

---

## 2. Strong compactness plus saturation would produce an extremizer

Assume

\[
f_j\to f_\infty
\quad\text{strongly in }H_0^1(B_R)
\]

and

\[
\|f_j\|_2\ge c_0>0.
\]

Then

\[
f_\infty\not\equiv0.
\]

Strong `H1` convergence gives

\[
\nabla f_j\to\nabla f_\infty
\quad\text{in }L^2,
\]

and, by the continuous critical Sobolev embedding,

\[
f_j\to f_\infty
\quad\text{in }L^6.
\]

Suppose

\[
\mathcal R_S[f_j]\to1.
\]

Then

\[
\boxed{
\|f_\infty\|_6
=S_*\|\nabla f_\infty\|_2.
}
\]

Thus the zero extension of `f_infty` would be a nonzero whole-space sharp Sobolev extremizer.

---

## 3. Contradiction with the classical extremal family

The classical Aubin--Talenti sharp-extremal family on `R^3` is noncompactly supported; up to the standard symmetries it has bubble form

\[
f(x)
\propto
(1+\lambda^2|x-x_0|^2)^{-1/2}.
\]

A nonzero `H_0^1(B_R)` function extended by zero has compact support in the closed ball.  It therefore cannot belong to the nonzero Aubin--Talenti extremal family.

Hence the saturation assumption is impossible.

Therefore

\[
\boxed{
\limsup_{j\to\infty}
\mathcal R_S[f_j]
<1.
}
\]

Equivalently, there exists a family-dependent

\[
\delta_S>0
\]

such that eventually

\[
\boxed{
\|f_j\|_6
\le
(1-\delta_S)
S_*\|\nabla f_j\|_2.
}
\]

---

## 4. Why critical noncompactness is not a contradiction

The sharp constant for `H_0^1(B_R)` can still equal the whole-space sharp constant at the level of an **infimum/supremum**, because concentrating bubbles can shrink inside the ball.

Such a near-extremizing sequence is not strongly compact in `H1`; it concentrates.

Therefore the correct dichotomy is exactly the one already used by the DSD route:

\[
\boxed{
\text{strong compactness}
\Rightarrow
\text{uniform sharp-Sobolev gap},
}
\]

or

\[
\boxed{
\text{sharp-Sobolev near-saturation}
\Rightarrow
\text{loss of strong compactness / concentration}.
}
\]

Thus critical Sobolev noncompactness is not an obstacle hidden inside the proof; it becomes a typed concentration branch.

---

## 5. Apply to normalized vorticity magnitude

Let

\[
f_j=\chi|\Omega_j|
\]

with a fixed cutoff supported in a normalized buffered ball.

On the bounded V2 branch, the strong-local-vorticity compactness lemma gives

\[
\Omega_j\to\Omega_\infty
\quad\text{strongly in }L_s^2H_y^1
\]

on a smaller cylinder.  At almost every selected persistent source-active time, one can pass to strongly `H1`-convergent cutoff magnitude profiles.

If the cutoff vorticity mass is nontrivial, the sharp scalar Sobolev step then has a strict gap `delta_S>0`.

---

## 6. Combine with magnitude heterogeneity

The previous compactness-rigidity result also gives a strict interpolation factor

\[
\mathcal R_{\rm int}
\le1-\delta_{\rm int}
\]

on a compact nontrivial family.

Therefore the near nonlinear source carries at least the product deficit

\[
\boxed{
(1-\delta_S)^{3/2}
(1-\delta_{\rm int})
}
\]

relative to the corresponding chain using the sharp Sobolev and interpolation constants, before including the separate angular-palinstrophy deficit.

The power `3/2` comes from cubing the `L3` interpolation and the square-root use of the `L6` norm in `||omega||_3^3`.

When angular palinstrophy is retained, the full structural source factor is further multiplied by

\[
(1-\eta_{\rm ang})^{3/4}.
\]

---

## 7. Updated saturation dichotomy

A bounded nontrivial strong-compactness sequence cannot simultaneously saturate either

1. the enstrophy-weighted `L2-L3-L6` magnitude interpolation; or
2. the critical scalar Sobolev inequality for the cutoff magnitude.

If a residual singular sequence tries to drive both ratios to one, it must leave the strong compactness class by spatial concentration.

That failure is already typed as an unbounded/critical concentration branch in the renormalized proof map.

Status: **SECOND COMPACTNESS-RIGIDITY GAP DERIVED / LOCAL SOURCE CONSTANT TRACKING NEXT**.
