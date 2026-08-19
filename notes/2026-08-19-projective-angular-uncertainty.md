# Projective angular uncertainty for the strain-gradient field

Date: 2026-08-19

Status: **DERIVED EXACT/SHARP-SCALE UNCERTAINTY BRIDGE / H-OR-T REDUCTION / GLOBAL REGULARITY NOT PROVED**.

This note closes the extreme spectral-axis-concentration subbranch left by `2026-08-19-gradient-covariance-fourier-bridge.md`.

---

## 1. Principal gradient axis

Let

\[
P_S=\|\nabla S\|_2^2,
\qquad
A_S=\|S\|_2^2,
\]

and let

\[
\mathsf C_{\nabla S}
=\frac{1}{P_S}
\int k\otimes k\,|\widehat S(k)|_F^2\,dk
\]

be the normalized global strain-gradient covariance.

Let `n` be its principal eigenvector and write

\[
\Pi_{\nabla S}=1-\mu_1.
\]

Then exactly

\[
\boxed{
\|\nabla_{n^\perp}S\|_2^2
=P_S\Pi_{\nabla S},
}
\]

where

\[
\nabla_{n^\perp}
=(I-n\otimes n)\nabla.
\]

The projective dispersion satisfies

\[
\boxed{
\frac12\mathcal J_{\nabla S}
\le
\Pi_{\nabla S}
\le
\frac32\mathcal J_{\nabla S}.
}
\]

---

## 2. Transverse Heisenberg inequality

Fix an arbitrary spatial center `X` and define the transverse second moment

\[
M_\perp(n,X)
=
\int
\left|P_{n^\perp}(x-X)\right|^2
|S(x)|^2dx.
\]

For each scalar strain component `S_ab`, integration by parts in the two transverse directions gives

\[
\|S_{ab}\|_2^2
\le
\|P_{n^\perp}(x-X)S_{ab}\|_2
\|\nabla_{n^\perp}S_{ab}\|_2.
\]

Summing over the strain components and applying Cauchy--Schwarz yields

\[
\boxed{
A_S^2
\le
M_\perp(n,X)
\|\nabla_{n^\perp}S\|_2^2.
}
\]

Therefore

\[
\boxed{
M_\perp(n,X)
\ge
\frac{A_S^2}{P_S\Pi_{\nabla S}}.
}
\]

---

## 3. Projective angular uncertainty

Define the transverse rms strain radius

\[
R_\perp^2(n,X)
=
\frac{M_\perp(n,X)}{A_S}.
\]

Then

\[
\boxed{
R_\perp^2(n,X)
\ge
\frac{A_S}{P_S\Pi_{\nabla S}}.
}
\]

Using `Pi <= 3 J / 2`,

\[
\boxed{
R_\perp^2(n,X)
\ge
\frac{2A_S}{3P_S\mathcal J_{\nabla S}}.
}
\]

Equivalently,

\[
\boxed{
\mathcal J_{\nabla S}
\ge
\frac{2}{3}
\frac{A_S}{P_S R_\perp^2(n,X)}.
}
\]

This is the desired physical/Fourier angular uncertainty relation.

The dimensionless combination

\[
\boxed{
\mathfrak U_{\nabla S}
=R_\perp^2\frac{P_S}{A_S}
}
\]

therefore obeys

\[
\boxed{
\mathfrak U_{\nabla S}
\ge
\frac{2}{3\mathcal J_{\nabla S}}.
}
\]

---

## 4. Consequence for spectral-axis concentration

If

\[
\mathcal J_{\nabla S}\to0,
\]

then necessarily

\[
\boxed{
R_\perp^2\frac{P_S}{A_S}\to\infty.
}
\]

Thus at least one of the following must occur:

1. **spatial transverse spreading**
   \[
   R_\perp\to\infty,
   \]
   which is a spatial non-tightness / transport `T` mechanism;

2. **derivative concentration**
   \[
   P_S/A_S\to\infty,
   \]
   which is an `H` mechanism.

Therefore extreme projective Fourier collimation is not a free advection-saturation state:

\[
\boxed{
\mathcal J_{\nabla S}\to0
\Longrightarrow
H\ \text{or}\ T.
}
\]

---

## 5. Exact zero-dispersion rigidity in finite energy

If formally

\[
\mathcal J_{\nabla S}=0
\]

with `P_S>0`, then the derivative-energy measure in Fourier space is supported projectively on a single line `R n`.

For an `L2` strain field on `R3`, a nonzero Fourier transform cannot be supported on a one-dimensional Lebesgue-null set. Hence the exact finite-energy `J=0` state is trivial:

\[
\boxed{
\mathcal J_{\nabla S}=0
\quad\Longrightarrow\quad
P_S=0
}
\]

within the ordinary `L2/H1` class.

This does not give a positive uniform lower bound on `J`; finite-energy wave packets may concentrate in arbitrarily narrow cones. The quantitative uncertainty inequality above describes the price of approaching that limit.

---

## 6. Reduced advection-H angular window

The advection-anisotropy estimate from the preceding note shows that the opposite extreme

\[
\mathcal J_{\nabla S}\to\frac23,
\qquad
\mathcal V_C\to0
\]

kills the strain-gradient contraction.

The present uncertainty estimate shows that

\[
\mathcal J_{\nabla S}\to0
\]

forces `H` or `T`.

Therefore a genuinely new, spatially tight, derivative-nonconcentrating advection-saturated survivor must keep the global Fourier angular dispersion away from both endpoints:

\[
\boxed{
0<j_-\lesssim
\mathcal J_{\nabla S}
\lesssim j_+<\frac23,
}
\]

unless the spatial covariance variance `V_C` itself is non-small.

Thus the unresolved advection branch is reduced to an **interior angular-dispersion window and/or spatial covariance segregation** rather than arbitrary anisotropy.

---

## 7. Next theorem target

The remaining route is now:

\[
\boxed{
\text{advection saturation}
\Longrightarrow
\begin{cases}
\text{interior projective angular window},\\
\text{or spatial covariance segregation},\\
\text{or }H/T.
\end{cases}
}
\]

The next useful result should show that repeated first-hitting pulses cannot keep both

\[
\mathcal J_{\nabla S}
\]

inside a fixed interior interval and

\[
\mathcal V_C
\]

non-negligible without paying a summable higher-derivative or multicore/material-turnover cost.

Status: **EXTREME SPECTRAL-AXIS CONCENTRATION REDUCED TO H/T; FINAL INTERIOR-ANGLE / COVARIANCE-SEGREGATION PACKING STEP OPEN**.
