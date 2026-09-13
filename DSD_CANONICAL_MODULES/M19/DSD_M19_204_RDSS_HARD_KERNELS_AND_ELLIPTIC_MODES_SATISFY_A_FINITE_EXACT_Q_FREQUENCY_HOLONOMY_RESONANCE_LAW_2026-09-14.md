# M19-204 — RDSS hard kernels and elliptic modes satisfy a finite exact q-frequency/holonomy resonance law

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / FINITE RESONANCE REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Twisted return condition

For an RDSS state with log-scale step \(L\) and rotational holonomy \(Q_*\), a hard Floquet mode with multiplier

\[
\mu=e^{i\vartheta}
\]

has scattering perturbation \(B\) satisfying

\[
\boxed{
B(q+L)=\mu^{-1}Q_*^{-1}B(q).
}
\]

## 2. Insert the finite Bohr spectrum

By M19-203, hard scattering perturbations have a finite q-spectrum. Consider one frequency/angular eigencomponent

\[
B(q,\omega)=e^{i\kappa q}b(\omega),
\]

and write the angular holonomy phase as

\[
Q_*^{-1}b=e^{i\phi}b.
\]

Then the twisted return law becomes

\[
e^{i\kappa L}=e^{-i\vartheta}e^{i\phi}.
\]

Equivalently,

\[
\boxed{
\kappa L+\vartheta-\phi=2\pi n,
\qquad n\in\mathbb Z.
}
\]

This convention-independent formula is the exact resonance law.

## 3. Kernel and elliptic cases

For a fixed-moduli kernel, \(\mu=1\) and \(\vartheta=0\), hence

\[
\boxed{
\kappa L-\phi=2\pi n.
}
\]

For a nonsymmetry elliptic unit mode,

\[
\boxed{
\kappa L+\vartheta-\phi=2\pi n,
\qquad \vartheta\not\equiv0\pmod{2\pi}.
}
\]

Exact rotation-symmetry phases are removed before classifying nonsymmetry modes.

## 4. Finite resonance set on bounded-period low-mode corridors

On the bounded-period hard corridor, both the interior hard fiber and the tail low-mode set are finite-dimensional. Therefore only finitely many relevant \(\kappa\)- and angular-holonomy channels occur in any fixed compact spectral window.

Hence kernel/elliptic degeneracy is confined to a finite family of exact resonance relations rather than an infinite small-divisor cascade.

## 5. What this does not prove

A finite resonance set can still contain genuine Navier--Stokes kernel states. The resonance law localizes the degeneracy but does not establish its absence.

Thus the remaining bounded-period theorem is a finite Fredholm/resonance rigidity problem.