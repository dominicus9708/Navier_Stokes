# M19-217 — Zero-q kernel signature is a linearized scattering-rigidity problem, not the nonlinear stationary-tail branch

**Date:** 2026-09-14  
**Status:** ACTIVE AUDIT / SCOPE FIREWALL + KERNEL-FRONTIER SPLIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Zero-q candidate left by M19-216

Let \(v\) be a nonsymmetry hard mode on the certified finite-dimensional symmetry quotient and let

\[
B:=D\mathscr S_Uv
\]

be its scattering perturbation.

M19-202--203 give a finite-dimensional q-translation representation on hard scattering signatures. Write its infinitesimal generator as

\[
\mathcal G_q^T=-\mathcal G_q.
\]

A zero-q hard channel is characterized by

\[
\boxed{
\mathcal G_qB=0,
}
\]

or equivalently

\[
\boxed{
\partial_qB=0
}
\]

in the scattering representation.

For a fixed-moduli RDSS kernel, M19-204/216 additionally require the principal holonomy phase to vanish. Hence

\[
\boxed{
Q_*^{-1}B=B.
}
\]

Thus the zero-q kernel sector is

\[
\boxed{
E_{q0}^{nsym}
:=
\left\{
 v\in H_{hard}^{nsym}:
 \partial_q(D\mathscr S_Uv)=0,
 \quad
 Q_*^{-1}D\mathscr S_Uv=D\mathscr S_Uv
\right\}.
}
\]

Uniform hard observability/injectivity of \(D\mathscr S_U\) means a nonzero \(v\) cannot be dismissed as an invisible tail perturbation.

## 2. Why this resembles a stationary tail

If

\[
B(q,\omega)=b(\omega),
\]

then the associated leading critical velocity perturbation has the homogeneous form

\[
W_{tail}(r,\omega)
\sim
r^{-1}b(\omega).
\]

This is q-stationary at the level of the **linearized scattering signature**.

That resemblance is useful for classification, but it does not make \(b\) a nonlinear stationary Navier--Stokes profile.

## 3. M5-268 does not apply automatically

M5-268 closes a different branch. Its hypotheses concern a **realized nonlinear canonical tail** \(T\) satisfying the stationary nonlinear equation

\[
\mathcal F(T)=0,
\]

and then use the exact realized RG recursion, all-order RG flatness, an Oseen difference equation, Carleman continuation, and smooth-core contradiction.

The present object \(B=D\mathscr S_Uv\) is instead the scattering image of a solution of the **linearized** equation along a generally nonstationary/relative-periodic background \(U\).

Nothing in M5-268 proves

\[
\partial_qB=0
\Longrightarrow
B=0
\]

for such a tangent mode.

Therefore

\[
\boxed{
\text{nonlinear realized stationary-tail rigidity}
\neq
\text{zero-q linearized scattering-kernel rigidity}.
}
\]

Importing M5-268 here without a new linearization/realization bridge would be a scope error.

## 4. M19-146 also does not apply to an arbitrary hard tangent

M19-146 proves, for the **background scattering datum** \(A_U\), the exact identity

\[
D\mathscr S_U(\partial_sU)
=-\frac12\partial_qA_U,
\]

and on the certified singular lane obtains a positive background q-speed floor

\[
\|\partial_qA_U\|_{X_{sc}}\ge v_q>0.
\]

This excludes a stationary or arbitrarily slow **background** scattering history on that lane.

But a general kernel tangent \(v\) has scattering perturbation

\[
B=D\mathscr S_Uv,
\]

and M19-146 does not imply

\[
\|\partial_qB\|>0.
\]

Indeed the exact time tangent is a special vector \(v=\partial_sU\); its derivative identity cannot be transferred to every hard tangent.

Hence

\[
\boxed{
\text{background q-speed floor}
\neq
\text{tangent q-frequency gap}.
}
\]

## 5. Exact zero-q theorem that is actually missing

The appropriate missing statement is a linearized scattering-rigidity theorem of the form

\[
\boxed{
\mathcal T_{q0}^{lin}:
E_{q0}^{nsym}=\{0\}.
}
\]

Equivalently: after quotienting the complete time/rotation symmetry representation, every hard tangent whose scattering signature is simultaneously q-invariant and holonomy-fixed must vanish.

This is narrower than the full finite-amplitude Fredholm theorem, but it is not supplied by the current nonlinear stationary-tail package.

## 6. Nonzero-q channel

The complement of the zero-q sector satisfies

\[
0<|\kappa_j|\le K_q^*
\]

and, by M19-216, any kernel resonance lies in the finite index box

\[
\kappa_jL-\phi_j=2\pi n,
\qquad
|n|\le N_{res}.
\]

Define this remaining subproblem as

\[
\boxed{
\mathcal T_{q\ne0}^{fin-res}:
\text{exclude the finitely indexed nonzero-q nonsymmetry resonant hard blocks.}
}
\]

Thus the bounded-period kernel frontier splits as

\[
\boxed{
\mathcal T_{kernel}^{finite-amp}
=
\mathcal T_{q0}^{lin}
\;\cup\;
\mathcal T_{q\ne0}^{fin-res}
}
\]

at the level of the remaining theorem obligations.

## 7. What could close the zero-q branch

A valid closure would require a new bridge such as one of the following:

1. derive the exact linearized critical-tail equation satisfied by q-invariant \(B\), including the q-dependent/relative-periodic background coefficients, and prove its nonsymmetry kernel is trivial;
2. prove a unique-continuation/Carleman theorem directly for the linearized hard mode using the scattering boundary condition \(\partial_qB=0\), rather than importing the nonlinear M5-268 argument;
3. identify every q-invariant holonomy-fixed hard signature with a differentiated exact symmetry and remove it in the complete quotient;
4. obtain a signed Fredholm pairing that is nonzero specifically on the q-invariant sector.

## 8. Audit verdict

### Certified

- zero-q plus kernel resonance implies a q-invariant, holonomy-fixed hard scattering perturbation;
- hard observability prevents a nonzero zero-q mode from hiding from the scattering map;
- M5-268 and M19-146 do not, by their present hypotheses, close this tangent sector;
- the remaining bounded-period kernel problem splits into a zero-q linearized-rigidity theorem and a nonzero-q finite-resonance theorem.

### Not certified

- \(E_{q0}^{nsym}=\{0\}\);
- exclusion of the finite nonzero-q resonance candidates;
- moderate RSS/RDSS kernel rigidity;
- global 3D Navier--Stokes regularity.

The bounded-period branch remains OPEN.