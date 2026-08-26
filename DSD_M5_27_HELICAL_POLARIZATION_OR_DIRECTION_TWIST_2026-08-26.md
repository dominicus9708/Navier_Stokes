# DSD M5-27 — Helical Polarization or Direction-Twist Split

Date: 2026-08-26

Status: **DERIVED FIRST-HIT SOLENOIDAL POLARIZATION DICHOTOMY / THE MANDATORY SOLENOIDAL CRITICAL CONTENT IS EITHER QUANTITATIVELY TWO-HELICITY MIXED OR IT CARRIES A FIXED ACTIVE-CELL DIRECTION-TWIST HELICITY / COMBINED WITH M5-26, EVERY FIRST-HIT CELL HAS DIRECTION COMPRESSION PLUS MIXING OR TWIST / GLOBAL REGULARITY UNPROVED.**

## 1. Input from M5-26

At every fixed positive first-hitting high-amplitude excess event, define

\[
W
=\left(1-\frac1{|V|}\right)_+V,
\qquad
Z:=\mathbb PW.
\]

M5-26 gives simultaneously

\[
\|\mathbf1_{\{|V|>1\}}\operatorname{div}n\|_2
\ge d_*>0
\]

and a solenoidal critical floor

\[
\|Z\|_{\dot H^{1/2}}^2
\ge c_H>0.
\]

Write the helical decomposition

\[
\widehat Z(q)=z_+(q)h_+(q)+z_-(q)h_-(q).
\]

Define

\[
X_+^Z
:=\frac12\int |q||z_+(q)|^2dq,
\qquad
X_-^Z
:=\frac12\int |q||z_-(q)|^2dq.
\]

Then

\[
S_Z:=X_+^Z+X_-^Z
\ge c_S>0
\]

up to the fixed normalization.

## 2. Helicity polarization parameter

The helicity of `Z` is

\[
H_Z
:=\int Z\cdot(\nabla\times Z)dz.
\]

In the helical basis,

\[
H_Z
=2(X_+^Z-X_-^Z)
\]

up to the same Fourier normalization convention.

Define the polarization ratio

\[
\rho_Z
:=
\frac{|X_+^Z-X_-^Z|}
{X_+^Z+X_-^Z}
\in[0,1].
\]

Fix one number

\[
0<\eta<1.
\]

Then exactly one of the two branches below holds.

## 3. Branch A: genuinely two-helicity mixed

If

\[
\rho_Z\le1-\eta,
\]

then

\[
\min\{X_+^Z,X_-^Z\}
=
\frac12
\left(
S_Z-|X_+^Z-X_-^Z|
\right).
\]

Hence

\[
\boxed{
\min\{X_+^Z,X_-^Z\}
\ge
\frac\eta2S_Z
\ge
c_{mix}>0.
}
\]

Thus both helical signs carry a fixed critical floor at the same normalized first-hitting cell.

In physical variables the associated solenoidal excess frequencies lie at

\[
|k|\sim L.
\]

This is the genuinely mixed helical branch.

## 4. Branch B: nearly homochiral

If

\[
\rho_Z>1-\eta,
\]

then

\[
|H_Z|
=2|X_+^Z-X_-^Z|
>2(1-\eta)S_Z.
\]

Therefore

\[
\boxed{
|H_Z|
\ge c_{hel}>0.
}
\]

To interpret this in physical-space geometry, use

\[
Z=\mathbb PW,
\qquad
W=Z+\mathbb QW.
\]

Because `curl(mathbb Q W)=0`,

\[
\nabla\times Z
=\nabla\times W.
\]

Moreover a gradient field is `L2`-orthogonal to a curl field, so

\[
\int Z\cdot(\nabla\times Z)
=
\int W\cdot(\nabla\times W).
\]

On the active set write

\[
V=an,
\qquad
W=(a-1)n.
\]

Then

\[
\nabla\times W
=
\nabla a\times n
+(a-1)\nabla\times n.
\]

Since

\[
n\cdot(\nabla a\times n)=0,
\]

we obtain the exact identity

\[
\boxed{
H_Z
=
\int_{a>1}
(a-1)^2
n\cdot(\nabla\times n)\,dz.
}
\]

Thus near homochirality of the solenoidal excess forces a fixed signed direction-twist helicity in the active high-amplitude cell.

## 5. Quantitative twist floor

The first-hitting excess energy is fixed:

\[
\frac12\int(a-1)^2dz
=g_0.
\]

By Cauchy--Schwarz,

\[
|H_Z|
\le
\left(
\int(a-1)^2dz
\right)^{1/2}
\left(
\int(a-1)^2
|n\cdot\nabla\times n|^2dz
\right)^{1/2}.
\]

Therefore the homochiral branch implies

\[
\boxed{
\int_{a>1}
(a-1)^2
|n\cdot\nabla\times n|^2dz
\ge
c_{twist}>0.
}
\]

Since

\[
|n\cdot\nabla\times n|
\le
|\nabla\times n|,
\]

also

\[
\boxed{
\int_{a>1}
(a-1)^2
|\nabla\times n|^2dz
\ge
c_{twist}>0.
}
\]

## 6. Simultaneous compression plus polarization/twist

M5-26 already gives at the same first-hitting event

\[
\boxed{
\|\mathbf1_{\{a>1\}}\operatorname{div}n\|_2
\ge d_*>0.
}
\]

Hence every first-hit cell satisfies

\[
\boxed{
\text{direction compression}
+
\left[
\text{two-helicity critical mixing}
\;\lor\;
\text{direction twist}
\right].
}
\]

This is a stronger same-cell geometry than the earlier global statements where compression, vorticity stretching and helicity were allowed to occur at unrelated positions/times.

## 7. Relation to vorticity alignment

Because

\[
\Omega_V
=\nabla\times(an)
=\nabla a\times n+a\nabla\times n,
\]

we have

\[
n\cdot\Omega_V
=a\,n\cdot\nabla\times n.
\]

Therefore

\[
\boxed{
H_Z
=
\int_{a>1}
\frac{(a-1)^2}{a}
\,n\cdot\Omega_V\,dz.
}
\]

The nearly homochiral branch may therefore also be read as a weighted velocity-direction/vorticity-alignment event inside the high-amplitude phase cell.

## 8. What is not yet excluded

Both branches are mathematically realizable in generic divergence-free fields:

- two-helicity mixing is the normal full-NS situation;
- simultaneous direction compression and twist is not kinematically forbidden.

Thus M5-27 is a structural reduction, not a contradiction.

The next useful question is whether one of these two branches is dynamically incompatible with the first-hitting pressure-source ledger:

1. **mixed branch:** can the two-helicity content be related to the actual projected Lamb transfer of the original velocity at `k~L`?
2. **twist branch:** does simultaneous compression plus near-homochiral twist suppress the solenoidal nonlinear transfer strongly enough that pressure cannot maintain the first-hitting formation balance?

This is the M5-28 audit target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
