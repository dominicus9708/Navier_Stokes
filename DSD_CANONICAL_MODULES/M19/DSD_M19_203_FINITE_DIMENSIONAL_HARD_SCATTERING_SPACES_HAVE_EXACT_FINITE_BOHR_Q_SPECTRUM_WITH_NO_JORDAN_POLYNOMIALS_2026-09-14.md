# M19-203 — Finite-dimensional hard scattering spaces have exact finite Bohr q-spectrum with no Jordan polynomials

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / FINITE-FREQUENCY REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Finite-dimensional translation representation

By M19-202, on a retained finite-dimensional hard scattering space the q-translation group is represented by

\[
\rho(h)=e^{hA},
\]

where \(A\) is real skew-symmetric in the scattering pullback metric.

Complexifying the hard space diagonalizes \(A\):

\[
A b_j=i\kappa_j b_j,
\qquad
\kappa_j\in\mathbb R.
\]

## 2. Exact q-dependence

The translation equation

\[
T_h B(q)=B(q+h)=\rho(h)B(q)
\]

therefore gives

\[
\boxed{
B(q,\omega)
=
\sum_{j=1}^J e^{i\kappa_j q}b_j(\omega),
}
\]

with a finite set of real frequencies \(\{\kappa_j\}\).

Real-valued signatures pair \(\kappa\) with \(-\kappa\).

## 3. No Jordan-polynomial factors

A general finite-dimensional translation representation could contain Jordan terms such as

\[
q^m e^{i\kappa q}.
\]

Here they are impossible because the representation is isometric/orthogonal. A nontrivial Jordan block would create polynomial norm growth in \(|q|\), contradicting the exact scattering norm preservation.

Hence the hard q-history is a genuine finite trigonometric/exponential sum, not merely an exponential polynomial.

## 4. Relation to earlier quasiperiodic reduction

M19-134 obtained a conditional finite-rank quasiperiodic picture at the nonlinear recurrent-hull level. The present result is exact at the certified **linear hard-bundle** level and follows directly from finite-dimensional scattering observability plus translation covariance.

## 5. Consequence for RDSS/RSS kernels

For a relative-periodic state with log-scale step \(L\) and rotational holonomy \(Q_*\), every hard kernel/elliptic mode can now be tested frequency by frequency against the twisted return condition. Thus bounded-period kernel rigidity becomes a finite exact resonance problem rather than an infinite small-divisor problem.

## 6. Next target

Write the exact resonance law by decomposing the angular action of \(Q_*\) simultaneously with the finite q-frequencies \(\kappa_j\).