# Energy-weighted corollary of the optimal global vorticity-axis gate

Date: 2026-08-12

Status: **DERIVED SUFFICIENT REGULARITY COROLLARY / CONDITIONAL NECESSARY BLOW-UP CERTIFICATE**.

This note combines the optimal global-axis consequence of Miller's locally anisotropic theorem with the ordinary finite-energy dissipation bound.

## 1. Recall the optimal-axis quantity

Let

\[
E_\omega(t)=\|\omega(t)\|_2^2
\]

and let

\[
\Pi_\omega(t)=1-\mu_1(t)
\]

be the optimal global directional defect from the vorticity covariance matrix.

The preceding note derived

\[
\min_{|n|=1}\|n\times\omega\|_2^2
=E_\omega\Pi_\omega.
\]

Miller's theorem therefore implies that finite-time blowup requires

\[
\int_0^{T^*}
(E_\omega\Pi_\omega)^2dt
=\infty.
\]

## 2. Energy-level information

For the whole-space finite-energy smooth track,

\[
\int_0^{T^*}E_\omega(t)dt
<\infty.
\]

This is the ordinary kinetic-energy dissipation bound.

## 3. Pointwise geometric decay sufficient for regularity

Suppose that near the candidate endpoint there exists a finite constant `C` such that

\[
\boxed{
\Pi_\omega(t)
\le
\frac{C}{\|\omega(t)\|_2}
}
\]

whenever `||omega(t)||_2>0`.

Since

\[
E_\omega=\|\omega\|_2^2,
\]

we obtain

\[
(E_\omega\Pi_\omega)^2
\le
C^2E_\omega.
\]

Hence

\[
\int_0^{T^*}
(E_\omega\Pi_\omega)^2dt
\le
C^2
\int_0^{T^*}E_\omega dt
<\infty.
\]

The optimal-axis form of Miller's criterion then precludes finite-time blowup.

Therefore

\[
\boxed{
\sup_{t<T^*}
\|\omega(t)\|_2\Pi_\omega(t)<\infty
\quad\Longrightarrow\quad
\text{no blowup at }T^*.
}
\]

## 4. Necessary residual certificate

Contrapositively, a hypothetical finite singularity must satisfy

\[
\boxed{
\sup_{t<T^*}
\|\omega(t)\|_2
[1-\mu_1(t)]
=\infty.
}
\]

Equivalently, there must be times approaching the singular endpoint for which the global off-axis enstrophy fraction does **not** collapse as fast as the inverse `L^2` vorticity norm.

This is stronger than merely requiring

\[
\|\omega(t)\|_2\to\infty
\]

along some sequence: the growth must retain enough multi-axis directional content.

## 5. Power-law interpretation

Suppose, only as a descriptive asymptotic model, that

\[
\Pi_\omega
\sim
E_\omega^{-\theta}.
\]

Then

\[
(E_\omega\Pi_\omega)^2
\sim
E_\omega^{2(1-\theta)}.
\]

The energy-level information controls the time integral automatically whenever

\[
2(1-\theta)\le1,
\]

i.e.

\[
\boxed{
\theta\ge\frac12.
}
\]

Thus collapse of the directional defect like

\[
\Pi_\omega
\lesssim
E_\omega^{-1/2}
=\|\omega\|_2^{-1}
\]

is already sufficient to enter the regularity gate.

This is a scaling/energy comparison, not a claim that such a collapse actually occurs.

## 6. DSD interpretation

The global axis matrix now has two coupled channels:

\[
\boxed{
\left(
E_\omega,
\Pi_\omega
\right).
}
\]

A large magnitude channel can be rendered harmless if the axis-property defect decreases sufficiently quickly.

Therefore the residual singular class requires simultaneous growth of

- total enstrophy;
- and effective multi-axis participation.

This is an explicit example of why the DSD application should not track magnitude and axis structure independently.

## 7. Next target

The local moving-sphere analogue would replace the global covariance by a weighted local covariance and ask whether the same magnitude-versus-axis-defect tradeoff can be obtained at every dangerous physical scale.

That requires a smooth principal-axis field or a controlled eigenvalue-gap alternative.

Status: **OPEN LOCAL ENERGY-WEIGHTED AXIS COROLLARY**.
