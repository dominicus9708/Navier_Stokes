# M19-241 — The bare toroidal similarity-Stokes cavity has a uniform negative Gaussian-conjugated spectral gap

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / BARE REMOTE TOROIDAL SPECTRAL RIGIDITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-237--240 show that a hypothetical escaping cavity unit mode must build a singular no-slip boundary structure. The next question is whether the remote **bare** similarity-Stokes operator itself can support a relative unit multiplier.

The toroidal sector is the cleanest place to test this because the pressure has no toroidal component.

In that sector there is an exact Gaussian conjugation to a self-adjoint harmonic-oscillator operator, yielding an R-independent negative spectral gap.

## 2. Bare similarity-Stokes operator

Set the background to zero. The linear similarity-Stokes system on \(B_R\) is

\[
\partial_sw
=
\nu\Delta w
-\frac12(y\cdot\nabla)w
-\frac12w
-\nabla\pi,
\qquad
\nabla\cdot w=0,
\qquad
w|_{S_R}=0.
\]

Define the componentwise bare operator

\[
\boxed{
A_0
:=
\nu\Delta
-\frac12y\cdot\nabla
-\frac12.
}
\]

## 3. Toroidal sector is pressure-free

Let

\[
\mathbf T_{\ell m}(\omega)
:=
\omega\times\nabla_{S^2}Y_{\ell m}(\omega),
\qquad \ell\ge1.
\]

A toroidal field has the form

\[
w(y,s)=f_{\ell m}(r,s)\mathbf T_{\ell m}(\omega).
\]

It is divergence free and tangent to every centered sphere. The radial drift, Laplacian, and radial scalar multiplication all preserve the toroidal subspace.

A gradient pressure has no toroidal component. Therefore the toroidal projection satisfies the closed pressure-free equation

\[
\boxed{
\partial_sw_T=A_0w_T.
}
\]

The no-slip condition is simply the Dirichlet condition on the toroidal radial amplitude at \(r=R\).

## 4. Exact Gaussian conjugation

Set

\[
\phi(y):=\frac{|y|^2}{8\nu}
\]

and write

\[
\boxed{w_T=e^{\phi}g.}
\]

A direct calculation gives

\[
\begin{aligned}
\nu\Delta(e^\phi g)
&=e^\phi\left[
\nu\Delta g
+\frac y2\cdot\nabla g
+\left(\frac34+\frac{|y|^2}{16\nu}\right)g
\right],\\
-\frac12y\cdot\nabla(e^\phi g)
&=e^\phi\left[
-\frac y2\cdot\nabla g
-\frac{|y|^2}{8\nu}g
\right].
\end{aligned}
\]

After including the \(-\frac12w\) term,

\[
\boxed{
e^{-\phi}A_0e^\phi
=
\nu\Delta
+\frac14
-\frac{|y|^2}{16\nu}.
}
\]

Call this self-adjoint Dirichlet operator \(H_R\).

Because the conjugating factor is radial, rotations commute with the conjugation and remain isometries in the conjugated L2 space.

## 5. Uniform harmonic-oscillator lower bound

For \(g\in H_0^1(B_R)\), extend \(g\) by zero to \(\mathbb R^3\). The three-dimensional harmonic oscillator satisfies

\[
\boxed{
\nu\|\nabla g\|_2^2
+\int\frac{|y|^2}{16\nu}|g|^2dy
\ge
\frac34\|g\|_2^2.
}
\]

Therefore

\[
\begin{aligned}
\langle g,H_Rg\rangle
&=
-\nu\|\nabla g\|_2^2
+\frac14\|g\|_2^2
-\int\frac{|y|^2}{16\nu}|g|^2\\
&\le
-\frac12\|g\|_2^2.
\end{aligned}
\]

Hence

\[
\boxed{
\sup\sigma(H_R)\le-\frac12
\qquad\text{for every }R>0.
}
\]

The bound is independent of the cavity radius.

The toroidal angular restriction can only improve the gap; the universal \(-1/2\) bound is sufficient here.

## 6. Uniform decay of the bare toroidal semigroup

For the conjugated toroidal solution,

\[
\partial_sg=H_Rg.
\]

Thus

\[
\boxed{
\|g(s+S)\|_2
\le e^{-S/2}\|g(s)\|_2
}
\]

for every \(S>0\).

Let \(Q\in SO(3)\) be any rotational holonomy. Since the radial Gaussian weight and the centered ball are rotation invariant,

\[
\|\mathcal R_Qg\|_2=\|g\|_2.
\]

A relative unit multiplier would require

\[
g(s+S)=\mathcal R_Qg(s),
\]

and therefore equal norms at the two endpoints. The strict decay gives

\[
\boxed{g\equiv0.}
\]

Consequently

\[
\boxed{
\text{the bare toroidal similarity-Stokes cavity has no nonzero relative unit multiplier for any }R,S,Q.
}
\]

## 7. Relation to the original toroidal critical channel

M19-041 identified toroidal scattering data as a genuine leading critical freedom, and M19-056 showed ordinary angular momentum does not remove it.

M19-241 shows a different fact: **a no-slip finite cavity with zero background cannot support an exact relative-periodic toroidal unit mode**, even at arbitrarily large radius.

This does not contradict the existence of formal/whole-space critical toroidal scattering data. The no-slip cavity boundary and Gaussian-conjugated remote operator supply additional structure.

## 8. Why this does not yet close the full escape branch

The actual cavity mode is linearized around \(U_j\neq0\). Background terms can couple toroidal and poloidal/potential sectors.

Although the physical coefficients satisfy

\[
U_j=O(R_j^{-1}),
\qquad
\nabla U_j=O(R_j^{-2})
\]

in the remote boundary region, the Gaussian conjugation has condition number growing exponentially with \(R_j^2/\nu\). Therefore an unweighted small perturbation cannot automatically be transferred into a uniformly small perturbation of the conjugated operator.

In particular,

\[
\boxed{
\text{bare toroidal spectral gap}
\neq
\text{uniform pseudospectral stability of the full cavity operator}.}
\]

This is the new scope firewall.

## 9. New leverage

Any escaping unit mode that is asymptotically pure toroidal in a norm compatible with the Gaussian-conjugated energy is excluded.

Therefore a surviving escape mode must use at least one of:

1. nontrivial toroidal--poloidal coupling generated by the background;
2. a potential/pressure-dominated boundary-shell component;
3. loss of uniform control under the Gaussian conjugation;
4. scaled-derivative/boundary concentration strong enough to exploit nonnormality.

This narrows the M19-240 shell residence problem.

## 10. Next calculation

The natural next audit is to derive the Gaussian-conjugated energy of the **full** linearized operator and identify exactly which background/pressure terms destroy the bare \(-1/2\) coercivity. If those defect terms are supported only in the already vanishing core or can be bounded by the remote scattering norm, the toroidal gap may extend beyond the bare model. Otherwise their size will identify the precise nonnormal coupling payer required by a surviving escape mode.

---

\[
\boxed{\text{M19-241 COMPLETE: THE BARE TOROIDAL CAVITY HAS AN R-INDEPENDENT NEGATIVE GAP AND NO RELATIVE UNIT MULTIPLIER.}}
\]
