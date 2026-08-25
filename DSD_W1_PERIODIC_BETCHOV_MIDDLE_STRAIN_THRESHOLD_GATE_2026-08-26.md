# DSD W1 Periodic Betchov / Middle-Strain Threshold Gate

Date: 2026-08-26

Status: **BETCHOV ROUTING DERIVED / POSITIVE PERIODIC VORTEX-STRETCHING PAYER CONVERTED TO AN ORIENTATION-FREE MIDDLE-STRAIN PAYER / UNIVERSAL LERAY THRESHOLD sup lambda_2^+ > 1/4 PROVED FOR EVERY NONTRIVIAL PERIODIC W1 ORBIT / FINITE-CORE WEIGHTED MIDDLE-STRAIN PAYER LOCALIZED / THIS SATURATES KNOWN MIDDLE-EIGENVALUE BLOWUP CRITERIA RATHER THAN CONTRADICTING THEM / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The preceding periodic enstrophy note proves

\[
\frac12 Z'(s)
+\frac14 Z(s)
+\nu P_\Omega(s)
=\mathcal S(s),
\]

where

\[
Z=\|\Omega\|_2^2,
\qquad
P_\Omega=\|\nabla\Omega\|_2^2,
\qquad
\mathcal S=\int\Omega^TS\Omega.
\]

On an S-periodic W1 orbit,

\[
\boxed{
\langle\mathcal S\rangle_S
=\frac14\langle Z\rangle_S
+\nu\langle P_\Omega\rangle_S>0.
}
\]

A difficulty with routing this through vorticity direction is that positive stretching can persist while the vorticity remains aligned with a positive strain eigendirection. Hence projective rotation is not compulsory.

This note removes the vorticity-direction variable from the payer by using the whole-space Betchov identity.

## 2. Strain notation

Let

\[
S=\frac12(\nabla U+\nabla U^T)
\]

with ordered eigenvalues

\[
\lambda_1\le\lambda_2\le\lambda_3.
\]

Incompressibility gives

\[
\boxed{
\lambda_1+\lambda_2+\lambda_3=0.
}
\]

The whole-space identities for a sufficiently regular divergence-free field with the present W1 tail decay are

\[
\boxed{
\|\Omega\|_2^2=2\|S\|_2^2
}
\]

and the Betchov identity

\[
\boxed{
\int\operatorname{tr}(S^3)
=-\frac34\int\Omega^TS\Omega.
}
\]

Since a trace-free 3 by 3 matrix satisfies

\[
\operatorname{tr}(S^3)=3\det S,
\]

we obtain the exact global routing

\[
\boxed{
\mathcal S
=-4\int\det S.
}
\]

Thus the positive vortex-stretching payer can be expressed entirely through strain eigenvalues.

## 3. Positive determinant sign is controlled by the middle eigenvalue

Because the strain is trace free, a nonzero strain state has

\[
\lambda_1<0<\lambda_3.
\]

If

\[
\lambda_2>0,
\]

then

\[
\det S=\lambda_1\lambda_2\lambda_3<0,
\]

whereas if

\[
\lambda_2<0,
\]

then

\[
\det S>0.
\]

Therefore the positive part of `-det S` is supported exactly on the positive-middle-eigenvalue region.

Write, on that region,

\[
a=\lambda_2>0,
\qquad
b=\lambda_3\ge a,
\qquad
\lambda_1=-(a+b).
\]

Then

\[
(-\det S)_+
=(a+b)ab.
\]

Also

\[
|S|^2
=(a+b)^2+a^2+b^2
=2(a^2+ab+b^2).
\]

Since

\[
b(a+b)
\le a^2+ab+b^2,
\]

we get the sharp elementary bound needed here:

\[
\boxed{
(-\det S)_+
\le
\frac12\lambda_2^+|S|^2.
}
\]

The constant 1/2 is approached as `b/a -> infinity`; no smaller universal constant follows from trace-free eigenvalue ordering alone.

## 4. Orientation-free upper gate for stretching

From Betchov,

\[
\mathcal S
=4\int(-\det S).
\]

Dropping the negative contribution of `-det S`,

\[
\mathcal S
\le4\int(-\det S)_+.
\]

Using the previous pointwise bound,

\[
\boxed{
\mathcal S(s)
\le
2\int_{\mathbb R^3}
\lambda_2^+(Y,s)|S(Y,s)|^2\,dY.
}
\]

This estimate contains no vorticity-direction or alignment variable.

Hence a perfectly fixed vorticity direction cannot evade the new payer by making projective action zero.

## 5. Periodic weighted middle-strain payer

Average over one period:

\[
\frac14\langle Z\rangle_S
+\nu\langle P_\Omega\rangle_S
=\langle\mathcal S\rangle_S
\le
2\left\langle
\int\lambda_2^+|S|^2
\right\rangle_S.
\]

Therefore

\[
\boxed{
\left\langle
\int\lambda_2^+|S|^2
\right\rangle_S
\ge
\frac18\langle Z\rangle_S
+\frac\nu2\langle P_\Omega\rangle_S.
}
\]

If the inherited occupied-core structure gives

\[
\langle Z\rangle_S\ge z_*>0,
\]

then

\[
\boxed{
\left\langle
\int\lambda_2^+|S|^2
\right\rangle_S
\ge z_*/8>0.
}
\]

This is a fixed positive middle-strain payer on every period.

## 6. Universal pointwise threshold for a nontrivial periodic Leray orbit

Suppose, for contradiction, that

\[
\lambda_2^+(Y,s)\le\frac14
\]

for every `Y` and every periodic phase `s`.

Then

\[
\mathcal S(s)
\le
2\frac14\|S(s)\|_2^2
=\frac12\|S(s)\|_2^2.
\]

Since

\[
Z=2\|S\|_2^2,
\]

this is

\[
\mathcal S(s)\le\frac14Z(s).
\]

Period averaging and the exact enstrophy identity give

\[
\frac14\langle Z\rangle_S
+\nu\langle P_\Omega\rangle_S
\le
\frac14\langle Z\rangle_S.
\]

Thus

\[
\boxed{
\langle P_\Omega\rangle_S=0.
}
\]

Because `P_Omega>=0`,

\[
\nabla\Omega\equiv0.
\]

But the W1 periodic vorticity lies in L2(R3), so a spatially constant vorticity must be zero:

\[
\Omega\equiv0.
\]

A divergence-free, curl-free W1 velocity in the global Lp class with `p>3` must also be zero.

This contradicts the nontrivial periodic W1 survivor.

Therefore every nonzero periodic W1 orbit obeys

\[
\boxed{
\sup_{(Y,s)\in\mathbb R^3\times[0,S]}
\lambda_2^+(Y,s)
>\frac14.
}
\]

The constant `1/4` is tied to the standard backward Leray normalization

\[
U_s+\frac12U+\frac12Y\cdot\nabla U+\cdots=\nu\Delta U.
\]

It is not asserted to be invariant under arbitrary rescaling conventions of Leray time.

## 7. The threshold crossing occurs in a finite recurrent core

The W1 critical tail has

\[
|S(Y,s)|\lesssim |Y|^{-2}
\]

and therefore

\[
\lambda_2^+(Y,s)\lesssim |Y|^{-2}
\]

on sufficiently remote shells.

Hence for one sufficiently large finite radius `R_lambda`,

\[
\sup_{|Y|>R_\lambda,\,s\in[0,S]}
\lambda_2^+(Y,s)<\frac14.
\]

Consequently the universal threshold crossing

\[
\lambda_2^+>\frac14
\]

must occur inside

\[
\boxed{B_{R_\lambda}.}
\]

Thus the threshold is a finite-core recurrent event, not something paid by the passive far 1/r memory.

## 8. Finite-core integrated payer

The tail integrand scales as

\[
\lambda_2^+|S|^2
\sim r^{-2}r^{-4}=r^{-6}.
\]

On a shell of volume scale `R^3`,

\[
\int_{A_R}\lambda_2^+|S|^2
=O(R^{-3}).
\]

The remote sum is therefore finite and tends to zero as the starting radius tends to infinity.

Choose a finite `R_M` such that

\[
\left\langle
\int_{|Y|>R_M}\lambda_2^+|S|^2
\right\rangle_S
\le z_*/16.
\]

Then the global lower bound from Section 5 gives

\[
\boxed{
\left\langle
\int_{B_{R_M}}\lambda_2^+|S|^2
\right\rangle_S
\ge z_*/16>0.
}
\]

This is the orientation-free finite-core replacement for the previous projective stretching payer.

## 9. Relation to the repository strain-alignment gate

The earlier computational/audit file

`src/strain_alignment_gate_baseline.py`

proved the exact pointwise linear-algebra gate

\[
\gamma_+
\le
[\lambda_2+(\lambda_3-\lambda_2)a_3]_+,
\]

where `gamma=xi^T S xi` and `a_3` is the squared alignment with the top strain eigenvector.

That gate remains correct, but it retained directional information and had no a-priori integral payer.

The present Betchov gate complements it:

\[
\boxed{
\text{positive periodic stretching}
\Longrightarrow
\text{positive weighted }\lambda_2^+\text{ payer}
}
\]

without requiring any direction change.

Thus the two possible descriptions are now separated cleanly:

- alignment gate: local mechanism of stretching;
- Betchov/middle-strain gate: global orientation-free period payer.

## 10. Comparison with known middle-eigenvalue regularity criteria

Known Navier--Stokes regularity criteria due to Neustupa--Penel and Miller state, in one standard formulation, that if a finite-time singularity occurs then the scale-critical spacetime norm of `lambda_2^+` must diverge; for exponents satisfying

\[
\frac2p+\frac3q=2,
\qquad
\frac32<q\le\infty,
\]

one has the necessary blowup condition

\[
\int_0^{T^*}
\|\lambda_2^+(t)\|_{L^q}^pdt
=\infty.
\]

The W1 periodic DSS survivor is consistent with this theorem.

Indeed in physical variables

\[
\lambda_{2,phys}^+(x,t)
=(T^*-t)^{-1}
\Lambda_2^+(Y,s),
\]

and periodic nontriviality plus the threshold above supplies a nonzero recurrent normalized middle-strain profile. At every critical exponent pair the physical norm accumulates logarithmically in Leray time toward `T*`.

Therefore the known criterion is saturated, not violated.

No external middle-eigenvalue theorem located in this audit excludes the arbitrary-factor weak-L3 periodic W1 endpoint merely from the finite normalized enstrophy/palinstrophy established here.

## 11. New periodic closure target

The periodic branch is now forced to sustain, in one finite recurrent core,

\[
\boxed{
\lambda_2^+>\frac14
}
\]

at some phase/point, and more robustly

\[
\boxed{
\left\langle
\int_{B_{R_M}}\lambda_2^+|S|^2
\right\rangle_S
\ge c_M>0.
}
\]

A final closure would require proving that such recurrent biaxial/extensional strain geometry must activate an already finite W1 loss channel or violate a separate one-sided budget.

This is sharper than asking merely for positive vortex stretching, because the vorticity-direction ambiguity has been removed.

No such one-sided finite budget is proved here.

## 12. Audit verdict

### PROVED

- Betchov converts global stretching to the cubic strain determinant;
- positive stretching is supported, in the positive sense, by positive middle strain;
- `(-det S)_+ <= (1/2) lambda_2^+ |S|^2`;
- periodic enstrophy forces a fixed positive weighted middle-strain payer;
- every nontrivial periodic W1 orbit must cross the universal normalized threshold `lambda_2^+ > 1/4`;
- both threshold crossing and weighted payer occur in a finite recurrent core because the critical far tail decays like `r^-2` in strain.

### NOT PROVED

- a finite global budget preventing repeated middle-strain threshold crossing;
- an implication from the middle-strain payer to H/T/projective loss;
- exclusion of the periodic W1 survivor;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]