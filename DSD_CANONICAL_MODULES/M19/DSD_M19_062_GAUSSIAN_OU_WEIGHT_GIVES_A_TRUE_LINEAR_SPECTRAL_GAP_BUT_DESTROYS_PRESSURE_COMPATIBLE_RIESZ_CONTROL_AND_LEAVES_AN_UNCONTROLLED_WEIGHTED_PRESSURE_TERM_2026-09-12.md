# M19-062 — Gaussian OU weight gives a true linear spectral gap but destroys pressure-compatible Riesz control and leaves an uncontrolled weighted pressure term

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / WEIGHTED-CONTRACTION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-061 reformulated the surviving weak-critical problem as exclusion of a nontrivial log-translation factor of a compact recurrent similarity-flow hull.

A natural PDE-specific mechanism would be strict contraction of two recurrent similarity trajectories.  The unweighted \(L^2\) difference identity is not contractive, so this module tests the Gaussian invariant measure of the Ornstein--Uhlenbeck part of the similarity operator.

The linear result is favorable: the Gaussian norm has a genuine spectral gap.  However the same Gaussian weight is not a Muckenhoupt \(A_2\) weight, so the pressure/Riesz machinery needed for incompressible nonlinear estimates is not compatible with this norm.  An explicit weighted pressure term remains.

## 2. Difference equation

Let \(U,V\) be two smooth divergence-free similarity solutions and set

\[
W:=U-V,
\qquad
Q:=P_U-P_V.
\]

Then

\[
\boxed{
\partial_\theta W
=\nu\Delta W
-\frac12W
-\frac12(y\cdot\nabla)W
-(U\cdot\nabla)W
-(W\cdot\nabla)V
-\nabla Q.
}
\]

Also

\[
\nabla\cdot W=0.
\]

## 3. Gaussian OU measure

Define

\[
\boxed{
\gamma_\nu(y)
:=
(4\pi\nu)^{-3/2}
\exp\left(-\frac{|y|^2}{4\nu}\right).
}
\]

Then

\[
\nabla\log\gamma_\nu
=-\frac{y}{2\nu}.
\]

The Ornstein--Uhlenbeck operator

\[
\mathcal L_{OU}:=\nu\Delta-\frac12y\cdot\nabla
\]

is symmetric dissipative in \(L^2(\gamma_\nu dy)\):

\[
\boxed{
\int f\,\mathcal L_{OU}f\,\gamma_\nu dy
=-\nu\int|\nabla f|^2\gamma_\nu dy.
}
\]

This identity holds componentwise for vector fields.

## 4. Exact weighted velocity-difference identity

Multiply the difference equation by \(W\gamma_\nu\) and integrate.

The linear part gives

\[
\boxed{
\int W\cdot
\left(
\nu\Delta W
-\frac12(y\cdot\nabla)W
-\frac12W
\right)
\gamma_\nu dy
=
-\nu\|\nabla W\|_{L^2(\gamma_\nu)}^2
-\frac12\|W\|_{L^2(\gamma_\nu)}^2.
}
\]

Thus

\[
\boxed{
\begin{aligned}
\frac12\frac d{d\theta}
\|W\|_{L^2(\gamma_\nu)}^2
&+
\nu\|\nabla W\|_{L^2(\gamma_\nu)}^2
+
\frac12\|W\|_{L^2(\gamma_\nu)}^2\\
&=
I_{tr}+I_{str}+I_p,
\end{aligned}
}
\]

with transport, strain, and pressure terms defined below.

## 5. Weighted transport defect

Since \(\nabla\cdot U=0\),

\[
\begin{aligned}
I_{tr}
&:=-\int W\cdot(U\cdot\nabla W)\gamma_\nu dy\\
&=-\frac12\int U\cdot\nabla(|W|^2)\gamma_\nu dy\\
&=\frac12\int |W|^2U\cdot\nabla\gamma_\nu dy.
\end{aligned}
\]

Hence

\[
\boxed{
I_{tr}
=-\frac1{4\nu}
\int (U\cdot y)|W|^2\gamma_\nu dy.
}
\]

This term has no fixed sign.

## 6. Strain defect

The second nonlinear term is

\[
\boxed{
I_{str}
:=-\int W_iW_j\,\partial_jV_i\,\gamma_\nu dy.
}
\]

Only the symmetric strain of \(V\) contributes to the quadratic form, but no sign is available in general.

If one had a sufficiently small weighted strain bound, this term could be absorbed by the Gaussian spectral gap.  Such a smallness estimate is not currently certified.

## 7. The pressure term does not vanish

In unweighted \(L^2\), incompressibility gives

\[
\int W\cdot\nabla Q\,dy=0.
\]

With the Gaussian weight,

\[
\begin{aligned}
I_p
&:=-\int W\cdot\nabla Q\,\gamma_\nu dy\\
&=
\int Q\,\nabla\cdot(W\gamma_\nu)dy\\
&=
\int Q\,W\cdot\nabla\gamma_\nu dy.
\end{aligned}
\]

Therefore

\[
\boxed{
I_p
=-\frac1{2\nu}
\int Q\,(W\cdot y)\gamma_\nu dy.
}
\]

This is an explicit obstruction to a naive Gaussian contraction proof.

## 8. Why ordinary weighted Riesz theory does not repair the pressure term

The pressure difference satisfies schematically

\[
-\Delta Q
=\partial_i\partial_j
\left(
U_iW_j+W_iV_j
\right).
\]

In an \(A_2\) weight, Calderon--Zygmund theory would provide weighted \(L^2\) control of \(Q\) by the quadratic source.

However the Gaussian weight

\[
\gamma_\nu(y)=e^{-c|y|^2}
\]

is not a Muckenhoupt \(A_2\) weight on \(\mathbb R^3\).  Its averages and reciprocal-weight averages on large balls grow incompatibly with the \(A_2\) condition.

Therefore one cannot invoke the standard weighted Riesz-transform theorem to estimate \(Q\) in the same Gaussian \(L^2\) norm.

The linear gap and the nonlinear pressure theory live naturally in different weighted categories.

## 9. Vorticity removes pressure but introduces a different nonlocal defect

One may instead difference the similarity vorticity equations.  This removes pressure and retains an even stronger linear OU damping because vorticity carries the additional \(+\Omega\) similarity term.

However the vorticity difference equation contains velocity-difference factors reconstructed from vorticity through Biot--Savart.  Gaussian weights are again poorly matched to the global singular integral / inverse-derivative mapping needed for that reconstruction.

Thus switching to vorticity moves the nonlocal obstruction; it does not automatically eliminate it.

## 10. What is gained

Despite the failure of the direct Gaussian proof, M19-062 establishes a useful structural fact:

\[
\boxed{
\text{the similarity linear operator itself has enough dissipation to contract recurrent differences in a natural weighted geometry.}
}
\]

The obstruction is specifically compatibility with the incompressible nonlinear/pressure structure, not absence of linear damping.

This suggests searching for a weight that simultaneously has

1. a positive similarity spectral gap;
2. Muckenhoupt \(A_2\) control for Riesz transforms;
3. manageable derivatives of the weight.

A polynomial weight is the natural next candidate.

## 11. Certified / not certified

### Certified

1. Exact Gaussian weighted difference identity.
2. Linear spectral gap \(\frac12\|W\|_{L^2(\gamma_\nu)}^2\).
3. Explicit weighted transport, strain, and pressure defects.
4. Gaussian weight is not an \(A_2\) weight, so standard weighted Calderon--Zygmund pressure control is unavailable.
5. Therefore Gaussian OU coercivity alone does not close the recurrent scattering factor.

### Not certified

1. Impossibility of every Gaussian-based incompressible estimate.
2. Smallness of the nonlinear defects.
3. A contracting metric for the full recurrent NS hull.
4. Global 3D Navier--Stokes regularity.

## 12. Next calculation

M19-063 should test polynomial weights

\[
w_{a,\kappa}(y)
=(1+\kappa|y|^2)^{-a/2},
\]

because for \(0<a<3\) they have \(A_2\)-type power behavior at infinity, while for suitable \(a>1\) the similarity drift can create damping.

The exact scalar coefficient

\[
\frac\nu2\frac{\Delta w}{w}
+\frac14\left(1+\frac{y\cdot\nabla w}{w}\right)
\]

should be computed and optimized.  If one can make it uniformly negative while retaining \(A_2\), then pressure-compatible linear coercivity exists and the remaining obstruction becomes purely nonlinear.

---

\[
\boxed{\text{M19-062 COMPLETE; GAUSSIAN OU COERCIVITY IS REAL BUT NOT PRESSURE-COMPATIBLE THROUGH STANDARD WEIGHTED RIESZ THEORY.}}
\]
