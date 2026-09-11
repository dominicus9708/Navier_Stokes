# M19-064 — A2 coercivity controls transport and pressure and reduces global factor rigidity to one explicit weighted gap-versus-L3-strain inequality

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / CONDITIONAL STRICT-CONTRACTION THEOREM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-063 constructed a regularized polynomial weight

\[
w(y)=(1+\kappa|y|^2)^{-a/2}
\]

with

\[
\frac52<a<3,
\qquad
\frac1{6a}<\beta:=\nu\kappa
\le\frac{a-2}{2a(a-1)},
\]

for which

1. \(w\in A_2(\mathbb R^3)\);
2. the linear similarity difference operator has a uniform gap
   \[
   C_w(y)\le-c_{gap}<0.
   \]

This module prices the nonlinear transport, pressure, and strain defects in the same weighted norm.

The first two are controlled by the same bounded-velocity quantity.  The strain term is controlled by \(L^3\) strain plus part of the weighted gradient dissipation.  Hence the full factor-rigidity problem reduces to one explicit quantitative inequality between the linear gap and the recurrent corridor's velocity/strain size.

## 2. Full weighted difference identity

Let \(U,V\) be two complete similarity solutions in the retained corridor, with

\[
W:=U-V,
\qquad
Q:=P_U-P_V.
\]

M19-063 gives

\[
\boxed{
\begin{aligned}
\frac12\frac d{d\theta}E_w
+\nu G_w
+c_{gap}E_w
\le
I_{tr}+I_{str}+I_p,
\end{aligned}
}
\]

where

\[
E_w:=\int|W|^2wdy,
\qquad
G_w:=\int|\nabla W|^2wdy.
\]

Also define

\[
\boxed{
L_w:=\|\nabla\log w\|_\infty
\le\frac{a\sqrt\kappa}{2}
=\frac a2\sqrt{\frac\beta\nu}.
}
\]

## 3. Transport defect

Because \(\nabla\cdot U=0\),

\[
\begin{aligned}
I_{tr}
&=-\int W\cdot(U\cdot\nabla W)wdy\\
&=\frac12\int |W|^2U\cdot\nabla w\,dy.
\end{aligned}
\]

Therefore

\[
\boxed{
|I_{tr}|
\le
\frac{L_w}{2}\|U\|_\infty E_w.
}
\]

Thus weighted transport is lower order in the same norm and costs no derivative of \(W\).

## 4. Weighted pressure control

The pressure difference obeys

\[
\boxed{
-\Delta Q
=\partial_i\partial_j
\left(
U_iW_j+W_iV_j
\right).
}
\]

Since \(w\in A_2\), the double Riesz transform is bounded on \(L^2(w)\).  Let \(C_{CZ}(a)\) denote a valid weighted Calderon--Zygmund constant; the \(A_2\) characteristic is invariant under the spatial dilation \(y\mapsto\sqrt\kappa y\), so this constant depends on the weight shape parameter \(a\) and not on the scale \(\kappa\).

Hence

\[
\boxed{
\|Q\|_{L^2(w)}
\le
C_{CZ}(a)
\left(\|U\|_\infty+\|V\|_\infty\right)
E_w^{1/2}.
}
\]

Integrating the pressure term by parts,

\[
I_p
=-\int W\cdot\nabla Q\,wdy
=
\int Q\,W\cdot\nabla w\,dy,
\]

so

\[
\boxed{
|I_p|
\le
C_{CZ}(a)L_w
\left(\|U\|_\infty+\|V\|_\infty\right)
E_w.
}
\]

Thus the pressure obstruction that killed the Gaussian norm is controlled in the polynomial \(A_2\) norm.

## 5. Velocity L-infinity from bounded vorticity amplitude and enstrophy

Suppose the retained compact corridor supplies

\[
\|\Omega_U\|_\infty,
\|\Omega_V\|_\infty
\le M_\Omega,
\]

and

\[
\|\Omega_U\|_2^2,
\|\Omega_V\|_2^2
\le Z_*.
\]

The Biot--Savart representation gives, for any \(R>0\),

\[
|U(x)|
\lesssim
M_\Omega R
+Z_*^{1/2}R^{-1/2}.
\]

Optimizing in \(R\),

\[
\boxed{
\|U\|_\infty
\lesssim
M_\Omega^{1/3}Z_*^{1/3}.
}
\]

The same holds for \(V\).

Define for convenience

\[
\boxed{
M_U
:=C_B M_\Omega^{1/3}Z_*^{1/3}.
}
\]

Then

\[
\|U\|_\infty,
\|V\|_\infty\le M_U.
\]

If the corridor fails either the vorticity-amplitude or enstrophy bound used here, that failure is outside the present compact branch and must be routed through the already typed escalation exits.

## 6. L3 strain bound

Let

\[
S_V:=\frac12(\nabla V+\nabla V^T).
\]

Calderon--Zygmund theory gives

\[
\|S_V\|_3
\lesssim
\|\Omega_V\|_3.
\]

Interpolation between \(L^2\) and \(L^\infty\) yields

\[
\|\Omega_V\|_3^3
\le
\|\Omega_V\|_\infty
\|\Omega_V\|_2^2
\le
M_\Omega Z_*.
\]

Therefore

\[
\boxed{
\|S_V\|_3
\le
M_S
:=C_S(M_\Omega Z_*)^{1/3}.
}
\]

This is a uniform size bound, not a smallness theorem.

## 7. Weighted strain estimate

Only the symmetric part of \(\nabla V\) contributes:

\[
I_{str}
=-\int W^TS_VW\,wdy.
\]

Set

\[
f:=W\sqrt w.
\]

Then

\[
|I_{str}|
\le
\|S_V\|_3\|f\|_3^2.
\]

By interpolation,

\[
\|f\|_3^2
\le
\|f\|_2\|f\|_6.
\]

The standard Sobolev inequality gives

\[
\|f\|_6
\lesssim
\|\nabla f\|_2.
\]

Also

\[
\nabla f
=\sqrt w\,\nabla W
+\frac12W\sqrt w\,\nabla\log w,
\]

so

\[
\|\nabla f\|_2
\le
G_w^{1/2}
+\frac{L_w}{2}E_w^{1/2}.
\]

Hence

\[
|I_{str}|
\lesssim
M_S E_w^{1/2}G_w^{1/2}
+M_SL_wE_w.
\]

Young's inequality yields

\[
\boxed{
|I_{str}|
\le
\frac\nu2G_w
+
C_1\nu^{-1}M_S^2E_w
+
C_2L_wM_SE_w.
}
\]

This is the decisive nonlinear estimate: no \(L^\infty\) strain bound is required, but the resulting zero-order coefficient need not be small.

## 8. The explicit contraction coefficient

Combining Sections 3, 4, and 7,

\[
\boxed{
\frac12E_w'
+\frac\nu2G_w
+\delta_*E_w
\le0,
}
\]

provided

\[
\boxed{
\begin{aligned}
\delta_*
:=c_{gap}
&-rac{L_w}{2}M_U
-2C_{CZ}(a)L_wM_U\\
&-C_1\nu^{-1}M_S^2
-C_2L_wM_S
>0.
\end{aligned}
}
\]

Equivalently, one sufficient quantitative factor-rigidity condition is

\[
\boxed{
\frac{L_w}{2}M_U
+2C_{CZ}(a)L_wM_U
+C_1\nu^{-1}M_S^2
+C_2L_wM_S
<c_{gap}.
}
\]

Every term is now expressed in already recognizable corridor quantities and the chosen weight parameters.

## 9. Strict contraction collapses a compact complete recurrent hull

If \(\delta_*>0\) uniformly for every pair of trajectories in a compact invariant complete hull, then

\[
\boxed{
E_w(\theta)
\le
E_w(0)e^{-2\delta_*\theta}
\qquad(\theta\ge0).
}
\]

Because time translation is surjective on a complete invariant hull, its weighted diameter satisfies

\[
\operatorname{diam}_w(\mathcal H)
=
\operatorname{diam}_w(\sigma_\theta\mathcal H)
\le
 e^{-\delta_*\theta}
\operatorname{diam}_w(\mathcal H).
\]

For any \(\theta>0\), this forces

\[
\boxed{\operatorname{diam}_w(\mathcal H)=0.}
\]

Therefore the recurrent hull is a singleton and its scattering factor cannot be nontrivially aperiodic.

Thus the weighted inequality above is a genuine sufficient theorem for the missing global factor rigidity.

## 10. Why this does not yet close the branch

The compact corridor supplies boundedness of the quantities used above, but the present repository does not certify the **smallness** required by

\[
\delta_*>0.
\]

In particular

\[
M_S\lesssim(M_\Omega Z_*)^{1/3}
\]

may be order one or large, while \(c_{gap}\) is a fixed dimensionless constant determined by the selected weight.

Hence

\[
\boxed{
\text{bounded strain size}
\neq
\text{strain small relative to the similarity spectral gap}.}
\]

M19-064 therefore converts the formerly qualitative global-factor problem into a precise quantitative obstruction rather than solving it.

## 11. Certified / not certified

### Certified

1. Transport defect is controlled by \(L_w\|U\|_\infty E_w\).
2. \(A_2\) weighted pressure is controlled in the same norm.
3. Bounded vorticity amplitude plus bounded enstrophy imply bounded velocity \(L^\infty\).
4. They also imply bounded strain in \(L^3\).
5. The strain defect can be absorbed into half the weighted gradient dissipation plus an explicit zero-order term.
6. The displayed condition \(\delta_*>0\) implies strict contraction.
7. Uniform strict contraction collapses a compact complete recurrent hull to one point.

### Not certified

1. The required smallness \(\delta_*>0\) on the retained corridor.
2. Optimality of the chosen weight or constants.
3. Global factor rigidity without the smallness condition.
4. Global 3D Navier--Stokes regularity.

## 12. Next calculation

M19-065 should ask whether pointwise smallness can be replaced by an **average-in-similarity-time gap condition**.

The relevant quantity is the time-dependent nonlinear coefficient

\[
\Lambda_{NL}(\theta)
\sim
L_w\|U(\theta)\|_\infty
+\nu^{-1}\|S_V(\theta)\|_3^2
+L_w\|S_V(\theta)\|_3.
\]

If recurrence plus the existing enstrophy/palinstrophy ledgers force

\[
\limsup_{T\to\infty}
\frac1T\int_0^T\Lambda_{NL}(\theta)d\theta
<c_{gap},
\]

then the same diameter argument gives exponential contraction on average and closes the factor without pointwise strain smallness.

The next step is therefore to translate the known physical-time enstrophy/palinstrophy budgets into similarity-time averages and check whether they are strong enough.

---

\[
\boxed{\text{M19-064 COMPLETE; FACTOR RIGIDITY IS REDUCED TO ONE EXPLICIT QUANTITATIVE GAP-VERSUS-STRAIN CONDITION.}}
\]
