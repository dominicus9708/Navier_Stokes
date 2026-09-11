# M19-057 — Every fixed-degree local polynomial moment of momentum has a two-order resonant transport gap and its first stress information coincides with the invertible r^-3 correction sector

**Date:** 2026-09-12  
**Status:** CALCULATION / R-CRITICAL GENERAL MOMENT FIREWALL / LOCAL POLYNOMIAL-MOMENT NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-055 treated scalar energy and M19-056 treated angular momentum.  Both showed the same pattern:

1. the leading critical \(r^{-1}A\) contribution is pure similarity transport;
2. genuine Navier--Stokes stress enters two powers of radius lower;
3. the \(r^{-3}B\) correction contributes at exactly that lower order.

This module proves that the same scaling mechanism holds for **every fixed-degree local polynomial moment of momentum**.

The result removes an entire family of candidate local tensor/spherical moments as automatic leading rigidity laws for the recurrent weak-critical scattering datum.

## 2. Similarity momentum equation

Use

\[
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+\nabla\cdot T=0,
\]

with symmetric stress

\[
T=U\otimes U+PI-2\nu D(U).
\]

Let \(\Phi_m(y)\) be a fixed smooth homogeneous polynomial vector field of degree \(m\ge0\):

\[
\boxed{
\Phi_m(\lambda y)=\lambda^m\Phi_m(y).
}
\]

Define the localized polynomial momentum moment on

\[
\mathcal A_R=\{R<|y|<\lambda R\}
\]
by

\[
\boxed{
\mathcal M_{\Phi_m,R}(\theta)
:=
\int_{\mathcal A_R}\Phi_m(y)\cdot U(y,\theta)\,dy.
}
\]

Angular momentum is included by choosing \(\Phi_1(y)=a\times y\).  Ordinary momentum corresponds to \(m=0\).

## 3. Exact weak moment identity

Multiply the similarity momentum equation by \(\Phi_m\) and integrate over \(\mathcal A_R\).

The stress term gives

\[
\int_{\mathcal A_R}\Phi_m\cdot(\nabla\cdot T)dy
=
\int_{\partial\mathcal A_R}\Phi_m\cdot Tn\,dS
-
\int_{\mathcal A_R}\nabla\Phi_m:T\,dy.
\]

For the similarity drift,

\[
\int\Phi_m\cdot(y\cdot\nabla U)dy
=
\int_{\partial\mathcal A_R}(y\cdot n)\Phi_m\cdot U\,dS
-
\int\bigl(3\Phi_m+y\cdot\nabla\Phi_m\bigr)\cdot U\,dy.
\]

Homogeneity gives

\[
y\cdot\nabla\Phi_m=m\Phi_m.
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal M_{\Phi_m,R}'
-
\frac{m+2}{2}\mathcal M_{\Phi_m,R}
&+
\frac12
\int_{\partial\mathcal A_R}
(y\cdot n)\Phi_m\cdot U\,dS\\
&+
\int_{\partial\mathcal A_R}\Phi_m\cdot Tn\,dS
-
\int_{\mathcal A_R}\nabla\Phi_m:T\,dy
=0.
\end{aligned}
}
\]

For special Killing fields such as \(a\times y\), the bulk stress moment vanishes because \(\nabla\Phi_m\) is antisymmetric while \(T\) is symmetric.  For a general polynomial moment it remains, but its scaling is the same as the boundary stress term.

## 4. Leading critical moment scales as R^(m+2)

Let

\[
U_0=r^{-1}A(q,\omega),
\qquad q=\log r-\theta/2.
\]

Write

\[
\Phi_m(r\omega)=r^m\Phi_m(\omega).
\]

Then

\[
\Phi_m\cdot U_0
=r^{m-1}\Phi_m(\omega)\cdot A(q,\omega).
\]

After multiplying by the volume factor \(r^2drd\omega\),

\[
\boxed{
\mathcal M_{\Phi_m,R}^{(0)}
=O(R^{m+2}).
}
\]

The similarity-drift boundary term has exactly the same size:

\[
(y\cdot n)\Phi_m\cdot U_0\,dS
\sim
r\,r^m\,r^{-1}\,r^2
=O(r^{m+2}).
\]

Because \(U_0\) solves the homogeneous similarity transport equation exactly, the entire leading \(O(R^{m+2})\) moment balance is a transport/storage identity for arbitrary admissible \(A\).

No Navier--Stokes nonlinearity, pressure, or viscosity is needed to enforce that leading balance.

## 5. Genuine stress information scales as R^m

For the critical leading field,

\[
T_0
=
U_0\otimes U_0+P_0I-2\nu D(U_0)
=O(r^{-2}).
\]

The boundary stress moment satisfies

\[
\Phi_m\cdot T_0n\,dS
\sim
r^m\,r^{-2}\,r^2
=O(r^m).
\]

Thus

\[
\boxed{
\int_{S_r}\Phi_m\cdot T_0n\,dS
=O(r^m).
}
\]

The bulk stress moment obeys

\[
\nabla\Phi_m=O(r^{m-1}),
\qquad
T_0=O(r^{-2}),
\]

so

\[
\nabla\Phi_m:T_0\,dy
\sim
r^{m-1}r^{-2}r^2dr
=r^{m-1}dr.
\]

Over a fixed-ratio annulus,

\[
\boxed{
\int_{\mathcal A_R}\nabla\Phi_m:T_0\,dy
=O(R^m)
}
\]

for \(m>0\), while for \(m=0\) the term vanishes because \(\nabla\Phi_0=0\).  Hence the first genuine stress information always sits two powers below the leading transport moment:

\[
\boxed{
R^{m+2}\quad\longrightarrow\quad R^m.
}
\]

## 6. The r^-3 correction moment is exactly R^m

M19-035 gives

\[
U_1=r^{-3}B(q,\omega),
\qquad
\mathcal L_{sim}U_1=-r^{-3}B.
\]

Then

\[
\Phi_m\cdot U_1
\sim r^m r^{-3}=r^{m-3}.
\]

Including volume measure,

\[
\Phi_m\cdot U_1\,dy
\sim r^{m-1}dr.
\]

Therefore on a fixed-ratio annulus,

\[
\boxed{
\mathcal M_{\Phi_m,R}^{(1)}=O(R^m)
}
\]

for every \(m\ge0\), interpreting \(m=0\) as the scale-invariant \(O(1)\) logarithmic annulus contribution.

Thus

\[
\boxed{
\text{first stress moment order}
=
\text{first }r^{-3}B\text{ correction-moment order}.
}
\]

## 7. Consequence: no fixed-degree polynomial moment gives an automatic leading solvability condition

At the first nontrivial moment order, one is taking a linear functional of the same vector correction equation

\[
-B+\mathbb P\mathcal F(A,\Pi)=0
\]

that already determines the invertible \(r^{-3}\) correction.

Therefore, absent an additional global identity or a special adjoint-kernel structure not present in the local calculation,

\[
\boxed{
\text{fixed-degree polynomial momentum moments do not create a new Fredholm condition on }A.
}
\]

This includes:

- ordinary momentum;
- angular momentum;
- centered first moments;
- higher tensor moments built from homogeneous polynomials;
- spherical-harmonic moments obtained by restricting homogeneous harmonic polynomials to spheres.

## 8. What this does and does not rule out

The result rules out the naive strategy

\[
\boxed{
\text{take successively higher local polynomial moments}
\Longrightarrow
\text{eventually constrain the recurrent }q\text{-history}.
}
\]

Every fixed degree preserves the same two-order gap.

However this does **not** rule out:

1. a genuinely nonlocal moment coupling infinitely many radii;
2. a scale-dependent test field whose degree/order grows with radius;
3. a global adjoint mode tied to the full recurrent hull;
4. a topological or material invariant not expressible as a fixed local polynomial moment;
5. a unique-continuation theorem linking the interior core and the full boundary scattering history.

## 9. Relation to the toroidal anti-model

M19-041 exhibited a purely toroidal aperiodic leading datum satisfying all currently certified leading-order constraints.

M19-056 shows angular momentum does not remove it.  M19-057 strengthens this:

\[
\boxed{
\text{no fixed finite hierarchy of local polynomial momentum moments removes it by leading-order scaling alone.}
}
\]

Thus the remaining rigidity problem is increasingly global in the logarithmic-radius variable \(q\).

## 10. Certified / not certified

### Certified

1. Exact weak polynomial-moment identity for homogeneous polynomial test fields.
2. Leading critical moment size \(O(R^{m+2})\).
3. Exact leading transport/storage character inherited from \(\mathcal L_{sim}U_0=0\).
4. Genuine stress moment size \(O(R^m)\).
5. \(r^{-3}B\) correction moment size \(O(R^m)\).
6. Therefore no generic fixed-degree local polynomial momentum moment supplies an independent first solvability condition on \(A\).

### Not certified

1. Failure of all nonlocal or infinite-degree observables.
2. Failure of helicity-like signed differential pairings.
3. Global rigidity of recurrent weak-critical scattering.
4. Global 3D Navier--Stokes regularity.

## 11. Next calculation

The next candidate should not be another finite polynomial momentum moment.  A natural structurally different observable is **helicity**, because it is signed, scale-critical at the annular level, and couples velocity directly to vorticity:

\[
H_R(\theta)
:=
\int_{\mathcal A_R}U\cdot\Omega\,dy.
\]

M19-058 should test whether the leading critical helicity history yields a finite-variation or coercive \(q\)-cocycle, or whether its first nontrivial Navier--Stokes content again falls into the invertible correction sector.

---

\[
\boxed{\text{M19-057 COMPLETE; THE ENTIRE FIXED-DEGREE LOCAL POLYNOMIAL MOMENT FAMILY SHARES THE SAME CORRECTION-ORDER FIREWALL.}}
\]
