# M19-216 — Compact hard scattering generator bounds the RDSS resonance integer uniformly

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / UNIFORM FINITE-RESONANCE INDEX REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Reuse the exact hard translation generator

M19-202--203 identify the q-translation action on every retained finite-dimensional hard scattering fiber as

\[
\rho_U(h)=e^{hA_U},
\qquad
A_U^T=-A_U.
\]

The complexified eigenvalues of \(A_U\) are

\[
 i\kappa_j(U),
\qquad
\kappa_j(U)\in\mathbb R.
\]

Work on the retained moderate bounded-period compact hard corridor \(\mathcal K\), and assume the certified finite-dimensional hard bundle and scattering identifications remain continuous there. Failure of this identification is already a compactness/bundle exit and is not silently absorbed into the present branch.

Compactness then gives a finite operator-norm ceiling

\[
\boxed{
K_q^*:=\sup_{U\in\mathcal K}\|A_U\|<\infty.
}
\]

Hence every exact hard q-frequency satisfies

\[
\boxed{
|\kappa_j(U)|\le K_q^*.
}
\]

This is the uniform version of the finite-frequency reduction of M19-203.

## 2. Bounded-period corridor

Let the RDSS log-step satisfy

\[
0<L_*\le L\le L^*<\infty.
\]

Let the physical rotational holonomy eigenphase on the relevant hard angular channel be represented by its principal value

\[
\phi_j\in[-\pi,\pi].
\]

M19-204 gives the kernel resonance law

\[
\boxed{
\kappa_jL-\phi_j=2\pi n,
\qquad n\in\mathbb Z.
}
\]

M19-214 further identifies \(e^{i\phi_j}\) with a physical integer-angular-momentum holonomy phase, but the principal phase \(\phi_j\) is the representation-safe quantity for the present estimate, including rational-angle aliasing.

## 3. Uniform bound on the resonance integer

At a kernel point,

\[
2\pi|n|
\le
|\kappa_j|L+|\phi_j|.
\]

Therefore

\[
2\pi|n|
\le
K_q^*L^*+\pi.
\]

Define

\[
\boxed{
N_{res}
:=
\left\lfloor
\frac{K_q^*L^*+\pi}{2\pi}
\right\rfloor.
}
\]

Then every nonsymmetry bounded-period kernel resonance must satisfy

\[
\boxed{
|n|\le N_{res}.
}
\]

Thus the infinite integer family in the formal resonance law is uniformly reduced to a finite integer box on the compact moderate hard corridor.

## 4. This is stronger than pointwise finiteness but weaker than kernel rigidity

M19-204 already showed that any fixed hard fiber has finitely many exact q-frequency/holonomy channels.

M19-216 adds a uniform statement across the retained compact family:

\[
\boxed{
\text{no kernel resonance can escape through }|n|\to\infty
\text{ while remaining in the same compact hard corridor.}
}
\]

Therefore an attempted surviving sequence of kernel-degenerate RSS/RDSS states must, after subsequence extraction, remain in a finite resonance-index sector.

If \(|n|\to\infty\) occurs, at least one retained assumption must fail:

- the q-generator norm decompactifies;
- the period \(L\) leaves the bounded-period corridor;
- the finite-dimensional hard-bundle identification fails.

These are existing compactness/long-period exits rather than a new kernel mechanism.

## 5. Relation to M19-145 mode cost

M19-145 independently showed that a unit Floquet channel with Bloch mismatch carries shell derivative cost containing

\[
1+\kappa^2
\]

and angular derivative cost. The compact hard-bundle estimate above is consistent with that result: unbounded \(|\kappa|\) would leave every fixed smooth finite-dimensional scattering norm corridor.

The current proof uses only the compact generator norm, so it does not require choosing a unique azimuthal integer \(m\) when rational holonomy angles alias several angular labels to the same eigenphase.

## 6. Remaining finite candidate problem

The kernel theorem is now reduced to a compact finite-index problem:

\[
\boxed{
\kappa_j(U)L(U)-\phi_j(U)=2\pi n,
\qquad
|n|\le N_{res},
}
\]

for finitely many hard spectral channels \(j\) on each finite-dimensional fiber.

This does not make the candidate set empty. It only forbids escape to arbitrarily high radial winding number inside the moderate compact corridor.

## 7. Next split: zero q-frequency versus nonzero q-frequency

The special case

\[
\kappa_j=0
\]

forces

\[
\phi_j=0
\]

for a kernel resonance in principal phase convention. Hence any zero-q kernel perturbation must be simultaneously

- invariant under log-radius translation in its scattering signature;
- fixed by the rotational holonomy;
- nonsymmetry after the complete time/rotation quotient.

This is a distinct static linearized scattering-rigidity subproblem.

All remaining kernel candidates have

\[
0<|\kappa_j|\le K_q^*.
\]

The next calculation should separate these two channels and audit whether earlier stationary-tail rigidity applies to the **linearized perturbation** problem rather than only to the nonlinear background tail.

The bounded-period branch remains OPEN.