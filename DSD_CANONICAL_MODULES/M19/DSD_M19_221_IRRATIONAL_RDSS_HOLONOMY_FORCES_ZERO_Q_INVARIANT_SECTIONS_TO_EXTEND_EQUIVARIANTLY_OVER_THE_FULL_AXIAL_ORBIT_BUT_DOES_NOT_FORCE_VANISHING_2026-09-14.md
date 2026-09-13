# M19-221 — Irrational RDSS holonomy forces a zero-q invariant section to extend equivariantly over the full axial orbit, but does not force vanishing

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / DENSE-HOLONOMY EQUIVARIANCE REDUCTION + NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setup

Let an RDSS background satisfy

\[
\boxed{
\sigma_SU=Q_*U,
\qquad
Q_*=R_{\mathbf a}(\alpha),
}
\]

with

\[
\frac{\alpha}{2\pi}\notin\mathbb Q.
\]

Let \(B\) be a zero-q holonomy-fixed hard scattering label and let \(s_B\) be the invariant hard section constructed in M19-219:

\[
D\mathscr S_Ys_B(Y)=B,
\]

\[
\Phi_t(Y)s_B(Y)=s_B(\sigma_tY).
\]

By M19-220, irrational holonomy forces \(B\) to lie in the axial \(m=0\) sector, hence

\[
\boxed{
R_{\mathbf a}(\beta)B=B
\qquad\forall\beta\in\mathbb R.
}
\]

## 2. Integer period iterates generate a dense axial orbit

Iterating the RDSS relation gives

\[
\boxed{
\sigma_{nS}U=Q_*^nU=R_{\mathbf a}(n\alpha)U,
\qquad n\in\mathbb Z.
}
\]

Because \(\alpha/2\pi\) is irrational,

\[
\{n\alpha\bmod2\pi:n\in\mathbb Z\}
\]

is dense in the axial circle.

Since the retained hull is closed in the local compact topology and the physical rotation action is continuous,

\[
\boxed{
R_{\mathbf a}(\beta)U\in\mathcal H(U)
\qquad\forall\beta\in\mathbb R.
}
\]

Thus the recurrent hull contains the entire axial group orbit of the base state.

## 3. Rotation covariance of the scattering derivative

Physical rotation equivariance gives

\[
\boxed{
D\mathscr S_{RU}(Rv)
=
R\,D\mathscr S_Uv
}
\]

for every retained rotation \(R\).

Set

\[
v=s_B(U).
\]

Then for an axial rotation \(R_\beta:=R_{\mathbf a}(\beta)\),

\[
D\mathscr S_{R_\beta U}(R_\beta s_B(U))
=
R_\beta B
=
B.
\]

But M19-219 gives uniqueness of the hard vector carrying the label \(B\) in each retained hard fiber. Therefore

\[
\boxed{
 s_B(R_\beta U)
 =R_\beta s_B(U)
}
\]

for every axial angle for which the rotated state belongs to the hull.

By Section 2 this is every \(\beta\in\mathbb R\).

## 4. The invariant section is fully axial-equivariant

Hence irrational RDSS holonomy upgrades the discrete relation to the continuous equivariance law

\[
\boxed{
 s_B(R_{\mathbf a}(\beta)Y)
 =R_{\mathbf a}(\beta)s_B(Y)
}
\]

on the axial orbit closure of every retained base point for which the same continuous hard-bundle identification is used.

In particular, the dangerous zero-q candidate is not merely a vector fixed after one RDSS return. It is a coherent equivariant field over the full axial orbit inside the hull.

## 5. Infinitesimal covariance

Where the section is differentiable along the smooth axial group orbit, differentiate at \(\beta=0\).

Let

\[
Z_{rot}(Y)
:=
\left.\frac d{d\beta}\right|_{0}
R_{\mathbf a}(\beta)Y
\]

be the exact axial rotation tangent and let \(\mathcal R_{\mathbf a}\) be the induced infinitesimal rotation on hard tangent vectors. Then

\[
\boxed{
D s_B(Y)[Z_{rot}(Y)]
=
\mathcal R_{\mathbf a}s_B(Y).
}
\]

This is a covariance identity, not a vanishing identity.

## 6. Isotropy inheritance

Let the axial isotropy subgroup of a base point be

\[
H_Y
:=
\{R_{\mathbf a}(\beta):R_{\mathbf a}(\beta)Y=Y\}.
\]

For every \(R\in H_Y\), equivariance gives

\[
s_B(Y)=s_B(RY)=Rs_B(Y).
\]

Therefore

\[
\boxed{
H_Y\subseteq H_{s_B(Y)}.
}
\]

Any zero-q invariant section must inherit every axial isotropy of the background point.

If the background is fully axisymmetric, the section is fully axisymmetric as well. If the background has trivial axial isotropy, this observation imposes no pointwise vanishing condition.

## 7. Quotient interpretation

Because the section transforms equivariantly under the full axial action, it descends naturally to the symmetry-quotiented hard bundle over the axial-orbit quotient of the hull.

Thus the dense holonomy does not leave an uncontrolled angular phase. It removes that phase from the theorem target.

However an equivariant section over a group orbit or quotient need not be zero. A trivial product example already allows a nonzero constant vector in a fixed representation sector.

Therefore

\[
\boxed{
\text{dense irrational holonomy}
+\text{equivariance}
\not\Longrightarrow
s_B=0.
}
\]

## 8. Relation to exact symmetry directions

The axial rotation tangent itself is an exact Navier--Stokes symmetry direction and is removed in the complete symmetry quotient.

But the covariance law

\[
D s_B[Z_{rot}]=\mathcal R_{\mathbf a}s_B
\]

does not identify \(s_B\) with \(Z_{rot}\). It merely states that \(s_B\) is an equivariant section.

Hence one must not infer

\[
\boxed{
\text{axial-equivariant hard section}
=
\text{rotation symmetry tangent}.
}
\]

That identification is precisely part of the missing rigidity theorem.

## 9. Revised irrational-holonomy target

On the irrational RDSS subbranch the zero-q theorem sharpens to

\[
\boxed{
\mathcal T_{q0}^{irr}:
\text{every axial-equivariant invariant hard section with constant axisymmetric scattering label is an exact symmetry section.}
}
\]

After the complete symmetry quotient the target is simply absence of such a nonzero section.

This is narrower than the general rational/DSS zero-q problem, because the angular representation ambiguity has disappeared entirely.

## 10. Firewall and next step

M19-221 is a structural reduction, not a closure. Dense group generation supplies equivariance, not coercivity.

The next analytic question is whether the **full linearized Navier--Stokes PDE** admits a nontrivial invariant section in this equivariant \(m=0\) hard sector after all exact symmetry tangents are removed. A useful next test is to construct a signed bilinear pairing between the background and the section and check whether the period/rotation covariance makes its mean derivative sign-definite.

---

\[
\boxed{
\text{M19-221: IRRATIONAL HOLONOMY REMOVES ANGULAR PHASE FREEDOM BUT DOES NOT BY ITSELF REMOVE THE ZERO-Q SECTION.}
}
\]
