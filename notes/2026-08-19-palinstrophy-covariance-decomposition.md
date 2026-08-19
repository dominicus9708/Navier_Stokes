# Exact palinstrophy covariance decomposition of the strain-gradient projective state

Date: 2026-08-19

Status: **DERIVED EXACT AXIS-RESOLVED IDENTITY + MAGNITUDE/DIRECTION COVARIANCE SPLIT / GLOBAL REGULARITY NOT PROVED**.

This note refines the remaining interior angular-dispersion branch.

---

## 1. Axis-resolved strain/vorticity derivative identity

For divergence-free velocity, Fourier space gives pointwise in wave number

\[
|\widehat S(k)|_F^2
=\frac12|\widehat\omega(k)|^2.
\]

Therefore for every pair of spatial directions `j,k`, Plancherel gives

\[
\boxed{
\int
\partial_jS:\partial_kS\,dx
=
\frac12
\int
\partial_j\omega\cdot\partial_k\omega\,dx.
}
\]

Consequently the global gradient covariance matrices satisfy

\[
\boxed{
\mathsf G_S
=
\frac12\mathsf G_\omega,
}
\]

where

\[
\mathsf G_\omega
=
\sum_i\int
\nabla\omega_i\otimes\nabla\omega_i\,dx.
\]

Since also

\[
\|\nabla S\|_2^2
=\frac12\|\nabla\omega\|_2^2,
\]

the normalized projective states are exactly identical:

\[
\boxed{
\mathsf C_{\nabla S}
=
\mathsf C_{\nabla\omega}.
}
\]

Hence

\[
\boxed{
\mathcal J_{\nabla S}
=
\mathcal J_{\nabla\omega}.
}
\]

The remaining advection angular channel is therefore simultaneously a palinstrophy-direction channel.

---

## 2. Magnitude/direction decomposition of the vorticity gradient

Where

\[
\rho=|\omega|>0,
\qquad
\xi=\omega/\rho,
\]

one has

\[
\nabla\omega_i
=
\xi_i\nabla\rho
+\rho\nabla\xi_i.
\]

Since

\[
\sum_i\xi_i\nabla\xi_i
=\frac12\nabla|\xi|^2=0,
\]

the cross terms cancel exactly and

\[
\boxed{
\mathsf G_\omega(x)
=
\nabla\rho\otimes\nabla\rho
+
\rho^2
\sum_i\nabla\xi_i\otimes\nabla\xi_i.
}
\]

Taking traces recovers

\[
\boxed{
|\nabla\omega|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
}
\]

Thus palinstrophy has two orthogonal typed sectors:

1. vorticity-magnitude interface/segregation;
2. vorticity-direction variation.

---

## 3. Two normalized covariance channels

Define

\[
P_\rho
=\int|\nabla\rho|^2dx,
\]

and

\[
P_\xi
=\int\rho^2|\nabla\xi|^2dx.
\]

Then

\[
P_\omega=P_\rho+P_\xi.
\]

When the corresponding denominator is nonzero, define

\[
\boxed{
\mathsf C_\rho
=
\frac{\int\nabla\rho\otimes\nabla\rho\,dx}{P_\rho},
}
\]

and

\[
\boxed{
\mathsf C_\xi
=
\frac{
\int\rho^2\sum_i
\nabla\xi_i\otimes\nabla\xi_i\,dx
}{P_\xi}.
}
\]

Let

\[
\theta=\frac{P_\rho}{P_\omega}.
\]

Then exactly

\[
\boxed{
\mathsf C_{\nabla S}
=
\mathsf C_{\nabla\omega}
=
\theta\mathsf C_\rho
+(1-\theta)\mathsf C_\xi.
}
\]

This is an exact DSD-style channel aggregation, not a heuristic decomposition.

---

## 4. Exact projective-dispersion mixture identity

Define

\[
\mathcal J_\rho
=1-\operatorname{tr}(\mathsf C_\rho^2),
\qquad
\mathcal J_\xi
=1-\operatorname{tr}(\mathsf C_\xi^2).
\]

For any two trace-one symmetric covariance matrices, the quadratic trace gives the exact mixture identity

\[
\boxed{
\mathcal J_{\nabla S}
=
\theta\mathcal J_\rho
+(1-\theta)\mathcal J_\xi
+
\theta(1-\theta)
\|\mathsf C_\rho-\mathsf C_\xi\|_F^2.
}
\]

Therefore interior projective dispersion cannot remain an untyped scalar. It is supplied by at least one of:

1. magnitude-gradient angular dispersion `J_rho`;
2. vorticity-direction-gradient angular dispersion `J_xi`;
3. covariance-axis mismatch `||C_rho-C_xi||_F`;
4. a nontrivial mixture fraction `theta(1-theta)`.

---

## 5. Consequence for direction-coherent near-M states

The reduced `M` branch tends toward projective vorticity alignment with the principal extensional strain axis. If, in addition, the magnitude-weighted direction variation is asymptotically small,

\[
\boxed{
P_\xi/P_\omega\to0,
}
\]

then

\[
\theta\to1
\]

and therefore

\[
\boxed{
\mathsf C_{\nabla S}-\mathsf C_\rho\to0,
}
\]

with

\[
\boxed{
\mathcal J_{\nabla S}-\mathcal J_\rho\to0
}
\]

under the bounded covariance geometry above.

Hence an interior angular survivor with coherent vorticity direction must place essentially all of its projective angular complexity into the geometry of the vorticity-magnitude gradients.

Conversely, if

\[
P_\xi/P_\omega
\not\to0,
\]

then a fixed fraction of palinstrophy is already paid directly by magnitude-weighted direction variation, an `H`/direction-coherence cost.

Thus the interior branch splits as

\[
\boxed{
\text{interior }\mathcal J_{\nabla S}
\Longrightarrow
\begin{cases}
\text{non-negligible direction-variation palinstrophy},\\
\text{or magnitude-interface angular geometry},\\
\text{or covariance-axis mismatch}.
\end{cases}
}
\]

---

## 6. Coarea interpretation of the magnitude channel

Where `rho` is regular and `n_rho=nabla rho/|nabla rho|`,

\[
\nabla\rho\otimes\nabla\rho
=|\nabla\rho|^2n_\rho\otimes n_\rho.
\]

The coarea formula gives

\[
\boxed{
\int\nabla\rho\otimes\nabla\rho\,dx
=
\int_0^\infty
\int_{\{\rho=a\}}
|\nabla\rho|
\,n_\rho\otimes n_\rho
\,d\mathcal H^2\,da.
}
\]

Thus `C_rho` and `J_rho` measure the projective orientation distribution of normals to vorticity-magnitude level surfaces, weighted by interface strength.

The remaining coherent-direction interior branch is therefore a geometric problem about repeated multiaxial magnitude interfaces / level-set normals, not an arbitrary Fourier-angle state.

---

## 7. Revised interior angular target

A tight first-hitting survivor that avoids the endpoint reductions must now sustain

\[
\mathcal J_{\nabla S}\in[j_-,j_+]\Subset(0,2/3),
\]

and then either:

1. spend a non-negligible fraction of palinstrophy on `rho^2|nabla xi|^2`;
2. maintain genuinely multiaxial vorticity-magnitude interfaces;
3. maintain a non-negligible covariance mismatch between the magnitude and direction sectors.

The next useful theorem target is a packing/occupancy estimate showing that repeated multiaxial magnitude-interface pulses at first-hitting scales force either a summable dissipation cost or spatial multicore/non-tightness.

Status: **INTERIOR ANGULAR DISPERSION REDUCED TO MAGNITUDE-INTERFACE / DIRECTION-VARIATION / COVARIANCE-MISMATCH CHANNELS; GLOBAL PACKING STEP OPEN**.
