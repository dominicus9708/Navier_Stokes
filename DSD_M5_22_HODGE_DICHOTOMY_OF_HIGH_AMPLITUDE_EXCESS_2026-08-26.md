# DSD M5-22 — Hodge Dichotomy of the High-Amplitude Excess

Date: 2026-08-26

Status: **DERIVED PHASE-SPACE DICHOTOMY / POSITIVE W1 `K` DEFECT FORCES EITHER A SOLENOIDAL CRITICAL EXCESS OR A GRADIENT/HODGE DIRECTION-COMPRESSION EXCESS AT THE SAME `k ~ L` SCALE / NO CONTRADICTION YET / GLOBAL REGULARITY UNPROVED.**

## 1. Input from M5-21

For a physical threshold `L`, define

\[
z=L(x-X_*),
\qquad
V(z)=L^{-1}u(X_*+z/L,t),
\]

and the natural high-amplitude excess

\[
W(z)
:=
\mathcal T(V(z))
=
\left(1-\frac1{|V(z)|}\right)_+V(z).
\]

Along a W1 defect sequence with

\[
K_L^{phys}(t)\ge\delta>0,
\]

M5-21 gives fixed constants

\[
q_*>0,
\qquad
c_*>0,
\]

such that

\[
\boxed{
\|P_{>q_*}W\|_2^2\ge c_*.
}
\]

One `z`-frequency unit corresponds to physical wavenumber of order `L`, so this is a `k ~ L` phase-space certificate.

## 2. Exact Hodge split

Use the whole-space Helmholtz decomposition

\[
W=\mathbb PW+\mathbb QW,
\]

where

\[
\mathbb P
=I-\nabla\Delta^{-1}\operatorname{div},
\qquad
\mathbb Q
=\nabla\Delta^{-1}\operatorname{div}.
\]

Both are orthogonal Fourier multipliers, and both commute with the radial Fourier cutoff `P_{>q_*}`.

Therefore

\[
\boxed{
\|P_{>q_*}W\|_2^2
=
\|P_{>q_*}\mathbb PW\|_2^2
+
\|P_{>q_*}\mathbb QW\|_2^2.
}
\]

Hence at least one of the following holds:

\[
\boxed{
\|P_{>q_*}\mathbb PW\|_2^2
\ge\frac{c_*}{2}
}
\]

or

\[
\boxed{
\|P_{>q_*}\mathbb QW\|_2^2
\ge\frac{c_*}{2}.
}
\]

This is the canonical M5-22 dichotomy.

## 3. Solenoidal branch

Suppose

\[
\|P_{>q_*}\mathbb PW\|_2^2
\ge\frac{c_*}{2}.
\]

Since all frequencies in this part satisfy `|q|>q_*`,

\[
\|\mathbb PW\|_{\dot H^{1/2}}^2
\ge
q_*\|P_{>q_*}\mathbb PW\|_2^2.
\]

Therefore

\[
\boxed{
\|\mathbb PW\|_{\dot H^{1/2}}^2
\ge
c_{sol}>0.
}
\]

Thus a positive high-amplitude defect can force a genuine divergence-free critical component at the same phase-space scale.

Because `mathbb P W` is divergence free, it admits the helical decomposition

\[
\widehat{\mathbb PW}
=w_+h_+ + w_-h_-.
\]

The positive critical content splits as

\[
\|\mathbb PW\|_{\dot H^{1/2}}^2
=
\int |q|(|w_+|^2+|w_-|^2)dq.
\]

At least one helical sector therefore carries a fixed critical floor. A two-sector floor does not follow from this step alone.

## 4. Gradient branch: exact amplitude-direction identity

Now suppose

\[
\|P_{>q_*}\mathbb QW\|_2^2
\ge\frac{c_*}{2}.
\]

Write

\[
a=|V|,
\qquad
n=\frac{V}{|V|}
\]

on the active region `a>1`.

There

\[
W=f(a)V,
\qquad
f(a)=1-a^{-1}.
\]

Because `div V=0`,

\[
\operatorname{div}W
=
\nabla f(a)\cdot V.
\]

Since

\[
f'(a)=a^{-2},
\]

we get

\[
\operatorname{div}W
=
\frac{V\cdot\nabla a}{a^2}.
\]

Using

\[
V=an
\]

and incompressibility

\[
n\cdot\nabla a+a\operatorname{div}n=0,
\]

we obtain the exact active-region formula

\[
\boxed{
\operatorname{div}W
=-\mathbf1_{\{a>1\}}\operatorname{div}n
}
\]

in the weak/a.e. sense. There is no additional surface delta at `a=1` because the truncation `W` vanishes continuously at the threshold.

Thus the gradient Hodge component is

\[
\boxed{
\mathbb QW
=
-\nabla\Delta^{-1}
\bigl(\mathbf1_{\{a>1\}}\operatorname{div}n\bigr).
}
\]

## 5. Exact Hodge-commutator representation

Since `V` itself is divergence free,

\[
\mathbb PV=V.
\]

Therefore

\[
[\mathbb P,f(a)]V
=
\mathbb P(f(a)V)-f(a)V
=-\mathbb QW.
\]

Hence

\[
\boxed{
\mathbb QW
=-[\mathbb P,(1-a^{-1})_+]V.
}
\]

This identifies the gradient branch with the same Hodge-commutator mechanism found earlier in the Bernoulli/amplitude analysis, now localized to the physical high-amplitude state boundary.

## 6. Quantitative direction-compression floor

Fourier-wise,

\[
\|P_{>q_*}\mathbb QW\|_2^2
=
\int_{|q|>q_*}
\frac{|\widehat{\operatorname{div}W}(q)|^2}{|q|^2}dq.
\]

Therefore the gradient-branch lower bound gives

\[
\boxed{
\|P_{>q_*}
(\mathbf1_{\{a>1\}}\operatorname{div}n)
\|_{\dot H^{-1}}^2
\ge
c_{grad}>0.
}
\]

Since `|q|>q_*` on this band,

\[
\|P_{>q_*}g\|_{\dot H^{-1}}
\le
q_*^{-1}\|P_{>q_*}g\|_2.
\]

Thus also

\[
\boxed{
\|\mathbf1_{\{a>1\}}\operatorname{div}n\|_2
\ge
c_{dir}>0.
}
\]

So if the high-amplitude excess does not carry enough solenoidal critical content, it must carry a fixed amount of direction compression in the active high-amplitude region.

## 7. Relation to amplitude transport

On `a>1`,

\[
V\cdot\nabla a
=-a^2\operatorname{div}n.
\]

Hence the gradient branch is equivalently a floor on the streamline amplitude-transport channel normalized by `a^2`:

\[
\operatorname{div}W
=
\frac{V\cdot\nabla a}{a^2}.
\]

This reconnects M5-22 directly to the earlier scalar input

\[
e=U\cdot\nabla|U|
\]

and to the amplitude Hodge/BMO branch, but now at the exact physical phase-space scale `|u|~L`, `|x-X_*|~L^{-1}`.

## 8. DSD reduction

The W1 `K` defect can no longer be treated as a purely scalar amplitude statistic. At each large threshold event it forces one of two geometrically typed channels:

\[
\boxed{
\begin{array}{c}
\text{positive }K\text{ defect}\\
\Downarrow\\
|k|\sim L\text{ excess content}\\
\Downarrow\\
\text{solenoidal critical excess}
\quad\lor\quad
\text{Hodge/direction-compression excess}.
\end{array}
}
\]

The first branch is the natural entry point for helical analysis. The second branch is the natural entry point for amplitude-direction/BMO analysis.

## 9. What is not yet proved

This dichotomy is not a contradiction.

In particular:

- `mathbb P W` is the solenoidal projection of the nonlinear high-amplitude excess, not the original Navier--Stokes solution itself;
- one helical-sector floor for `mathbb P W` is not yet the two-sector mixing floor needed to constrain a large critical cascade;
- the direction-compression floor in the gradient branch has not yet been shown to incur a nonintegrable physical-time cost.

Thus M5 remains open.

## 10. Next target

The next useful step is to compare the two branches with the actual Navier--Stokes nonlinear source:

1. **solenoidal branch:** estimate how much of the projected Lamb transfer at scale `k~L` must interact with `mathbb P W`, and whether M5-16 forces minority-helicity participation at the same scale;
2. **gradient branch:** use
   \[
   \operatorname{div}W
   =\frac{V\cdot\nabla|V|}{|V|^2}
   \]
   to connect the fixed direction-compression floor to the already known critical amplitude-transport saturation.

The goal is to determine whether these two branches are genuinely separate survivors or two projections of one unavoidable critical formation cell.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
