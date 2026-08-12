# Factorial nonlinear forcing majorant for the S-chain

Date: 2026-08-13

Status: **DERIVED FACTORIAL FORCING CONVOLUTION / OPEN DYNAMIC-RADIUS CLOSURE**.

This note puts the nonlinear derivative-forcing channel

\[
L_k
=
\left(
\frac{\sum_{|I|=k}\|F_I\|_2^2}{E_k}
\right)^{1/2}
\]

into the same factorial derivative bookkeeping used by the V-chain.

The purpose is to determine the correct common normalization rather than guessing an extra factor of `(k+1)`.

## 1. Schematic differentiated vorticity forcing

For

\[
F_I
=\partial_I(S\omega)-[\partial_I,u\cdot\nabla]\omega,
\]

Leibniz gives two schematic families:

\[
D^mS\,D^{k-m}\omega,
\]

and, for the commutator,

\[
D^m u\,D^{k-m+1}\omega,
\qquad 1\le m\le k.
\]

The exact tensor contractions and the finite number of coordinate-component sums are absorbed into norm-dependent constants. The derivative-order combinatorics are retained exactly.

## 2. Factorial amplitudes

Fix a physical scale `ell>0` and define

\[
\boxed{
W_k
=\frac{\ell^k}{k!}
\|D^{(k)}\omega\|_2,
}
\]

\[
\boxed{
G_m
=\frac{\ell^m}{m!}
\|D^{(m)}S\|_\infty,
}
\]

and for `m>=1`,

\[
\boxed{
U_m
=\frac{\ell^{m-1}}{m!}
\|D^{(m)}u\|_\infty.
}
\]

For the forcing amplitude define

\[
\boxed{
F_k^{\#}
=\frac{\ell^k}{k!}
\|D^{(k)}\text{(vorticity nonlinearity)}\|_2.
}
\]

Here the notation is schematic for the ordered derivative family used in the covariance chain; component multiplicities only modify a universal dimensional constant.

## 3. Stretching-product convolution

For the stretching family,

\[
\frac{\ell^k}{k!}
\binom{k}{m}
\|D^mS\|_\infty
\|D^{k-m}\omega\|_2
=G_mW_{k-m}.
\]

Therefore

\[
\boxed{
F_{k,\mathrm{stretch}}^{\#}
\lesssim
\sum_{m=0}^kG_mW_{k-m}.
}
\]

## 4. Commutator convolution and the derivative generator

For the commutator family,

\[
\frac{\ell^k}{k!}
\binom{k}{m}
\|D^m u\|_\infty
\|D^{k-m+1}\omega\|_2.
\]

Let

\[
n=k-m+1.
\]

Then

\[
\frac{\ell^{n}}{(n-1)!}
\|D^n\omega\|_2
=nW_n.
\]

Hence

\[
\boxed{
F_{k,\mathrm{comm}}^{\#}
\lesssim
\sum_{m=1}^{k}
U_m\,(k-m+1)W_{k-m+1}.
}
\]

The apparently troublesome derivative-order factor is therefore exactly the coefficient sequence of the generating-function derivative.

## 5. Generating-function form

Define

\[
\mathcal W(z)=\sum_{k\ge0}W_kz^k,
\]

\[
\mathcal G(z)=\sum_{m\ge0}G_mz^m,
\]

\[
\mathcal U(z)=\sum_{m\ge1}U_mz^{m-1},
\]

and

\[
\mathcal F(z)=\sum_{k\ge0}F_k^{\#}z^k.
\]

Since

\[
z\partial_z\mathcal W(z)
=\sum_{n\ge1}nW_nz^n,
\]

the differentiated forcing obeys the schematic majorant

\[
\boxed{
\mathcal F(z)
\lesssim
\mathcal G(z)\mathcal W(z)
+
\mathcal U(z)\partial_z\mathcal W(z)
}
\]

up to the harmless indexing convention for the power of `z` in `U`.

Equivalently, with a shifted definition of `U(z)`, the second term may be written `U(z) z W'(z)`. The essential point is invariant: the commutator is a Cauchy product with the **derivative generator** of the factorial vorticity series.

## 6. Relation to the coefficientwise S-channel

At derivative order `k`,

\[
\sqrt{E_k}=\|D^{(k)}\omega\|_2
\]

for the ordered derivative norm convention.

Since both numerator and denominator carry the same factorial/scale factor,

\[
\boxed{
L_k
=\frac{F_k^{\#}}{W_k}
}
\]

whenever `W_k>0`.

Thus dividing `L_k` by `(k+1)` would not be the natural common normalization. The correct factorial object is the forcing coefficient `F_k^#`; the extra derivative-order growth resides in `z W'(z)`.

## 7. Why a direct coefficientwise sum is awkward

The projective S-term is

\[
\sqrt{J_k}L_k
=
\sqrt{J_k}\frac{F_k^{\#}}{W_k}.
\]

Therefore a sum of coefficientwise normalized projective equations contains the reciprocal amplitude `1/W_k`.

This is not naturally controlled by the Cauchy-product majorant, especially if some derivative coefficient is small.

This identifies a structural obstruction:

\[
\boxed{
\text{coefficientwise }J_k
\text{ is not the ideal object for summing the S-chain.}
}
\]

The natural next object should carry derivative-energy weight so that `W_k` multiplies rather than divides the forcing coefficient.

## 8. Energy-weighted projective candidate

A first candidate is

\[
\boxed{
\mathfrak D_\ell
=\sum_{k\ge0}W_k^2J_k
=\sum_{k\ge0}
\frac{\ell^{2k}E_k}{(k!)^2}J_k.
}
\]

In the projective equation, multiplying the S-channel by `W_k^2` produces

\[
W_k^2\sqrt{J_k}L_k
=
W_k\sqrt{J_k}F_k^{\#},
\]

which is compatible with Cauchy--Schwarz / generating-function estimates and no longer contains a reciprocal derivative coefficient.

However differentiating `D_ell` also differentiates `W_k^2` and, if `ell=ell(t)`, the dynamic radius itself. These additional terms must be included exactly before any closure claim.

## 9. Revised common-majorant target

The S/V problem is therefore better reformulated as an energy-weighted projective generating functional rather than a bare sum of `J_k` equations.

The next target is to derive

\[
\frac d{dt}
\sum_{k\ge0}
\frac{\ell(t)^{2k}E_k(t)}{(k!)^2}J_k(t)
\]

and check whether

1. the S contribution is controlled by the factorial Cauchy products `G W` and `U W'`;
2. the V contribution telescopes or yields a coercive neighboring-covariance term;
3. a suitable decreasing dynamic radius `ell(t)` absorbs the derivative-generator contribution.

This is the first formulation in which the S and V chains share the same factorial energy weight without an artificial coefficientwise division.

Status: **OPEN ENERGY-WEIGHTED PROJECTIVE GENERATING FUNCTION**.
