# M19-070 — The zero-background similarity Stokes operator has no imaginary-axis modes, but aperiodic recurrent interiors require a linear-cocycle center spectrum, not a fixed-frequency resolvent test

**Date:** 2026-09-12  
**Status:** CALCULATION / FINITE-BOUNDARY REALIZABILITY / SPECTRAL FORMULATION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-069 moved the realizability problem from the far tail to the finite spectator boundary/interior interface.  A tempting next step is to decompose a boundary history into temporal harmonics \(e^{i\lambda\theta}\) and test whether the whole-space interior resolvent admits nonzero imaginary-axis frequencies.

This works for a stationary background.  It does **not** directly apply to the surviving aperiodic recurrent background because the linearized coefficients depend on similarity time.

This module makes that distinction exact.

## 2. Zero-background similarity Stokes operator

At \(U=0\), a divergence-free perturbation \(W\) satisfies

\[
\boxed{
\partial_\theta W
=
\mathcal L_0W-
\nabla Q,
\qquad
\mathcal L_0
:=
\nu\Delta
-\frac12y\cdot\nabla
-\frac12.
}
\]

If \(\nabla\cdot W=0\), then taking divergence gives

\[
\Delta Q=0.
\]

Under the usual admissible decay/integrability gauge, \(\nabla Q=0\).  Hence the divergence-free zero-background dynamics are governed by \(\mathcal L_0\).

## 3. Gaussian spectrum

In the Gaussian space

\[
L^2(\gamma_\nu dy),
\qquad
\gamma_\nu(y)
\propto
 e^{-|y|^2/(4\nu)},
\]

the Ornstein--Uhlenbeck operator

\[
\nu\Delta-rac12y\cdot\nabla
\]

is self-adjoint nonpositive with Hermite spectrum

\[
\boxed{
0,-\frac12,-1,-\frac32,\ldots.
}
\]

The additional velocity similarity term \(-\frac12\) shifts this to

\[
\boxed{
\operatorname{spec}(\mathcal L_0)
=
\left\{
-\frac{n+1}{2}:n=0,1,2,\ldots
\right\}
}
\]

on the corresponding vector Hermite sectors, restricted further by incompressibility.

Therefore

\[
\boxed{
\operatorname{spec}(\mathcal L_0)
\cap i\mathbb R
=\varnothing.
}
\]

The zero background has no neutral or oscillatory imaginary-axis interior mode.

## 4. Stationary nonzero background: genuine resolvent problem

If \(V(y)\) is stationary in similarity time, the linearized operator

\[
\mathcal L_V
=
\mathcal L_0
-(V\cdot\nabla)
-(\,\cdot\,\nabla)V
-\nabla\mathcal P_V
\]

is time independent.

Then an ansatz

\[
W(y,\theta)=e^{i\lambda\theta}\phi(y)
\]

leads to the legitimate resolvent/eigenvalue problem

\[
\boxed{
(i\lambda-\mathcal L_V)\phi=0.
}
\]

The weighted estimates of M19-063--064 imply absence of such modes under the quantitative gap condition, but that smallness is not established in the large recurrent corridor.

## 5. Periodic background: Floquet problem

If \(V(\theta+T)=V(\theta)\), the coefficients are periodic rather than constant.

The correct object is the period map

\[
\boxed{
\mathcal U_V(T,0)
}

of the linearized equation.

Neutral modes correspond to Floquet multipliers on the unit circle, not directly to eigenvalues \(i\lambda\) of one time-independent operator.

The time tangent \(V_\theta\) supplies the multiplier \(1\).

Extra unit-circle multipliers would represent additional center directions.

## 6. Aperiodic recurrent background: linear skew-product cocycle

For the actual surviving frontier, \(V(\theta)\) may be recurrent but aperiodic.  The linearized equation is

\[
\boxed{
\partial_\theta W
=
\mathcal L_{V(\theta)}W.
}
\]

Let

\[
\mathcal U_V(\theta,s)
\]

be its evolution operator.

The pair

\[
\boxed{
(V,W)
\mapsto
(\sigma_tV,\mathcal U_V(t,0)W)
}
\]

is a linear skew-product cocycle over the recurrent hull.

There is no global separation

\[
W=e^{i\lambda\theta}\phi(y)
\]

unless the base trajectory has additional stationarity/periodicity.

Therefore the correct center object is a cocycle spectrum: Lyapunov exponents, Sacker--Sell spectrum, exponential dichotomy spectrum, or an equivalent bounded-entire-solution space.

## 7. Exact time tangent gives one zero center exponent

M19-067 established

\[
Z(\theta):=V_\theta(\theta)
\]

as an exact solution of the linearized equation.

On a bounded recurrent trajectory, this mode is bounded along the hull.  It is the canonical candidate for zero exponential growth:

\[
\boxed{\lambda_{center}=0.}
\]

Thus the full cocycle cannot be uniformly strictly contracting on all directions.

The center-simplicity problem is precisely whether there are any other bounded entire linearized solutions / zero exponents independent of \(V_\theta\).

## 8. Weighted energy estimate gives only an upper bound on the top exponent

The M19-064 weighted estimate implies schematically

\[
\frac d{d\theta}\log\|W\|_w
\lesssim
-c_{gap}+\Lambda_{NL}(\theta).
\]

Hence any upper Lyapunov exponent satisfies

\[
\boxed{
\lambda_+(W)
\le
-c_{gap}
+\limsup_{T\to\infty}
\frac1T\int_0^T\Lambda_{NL}(\theta)d\theta.
}
\]

Because the time tangent has zero exponent, every nonstationary recurrent trajectory necessarily lies at or beyond the threshold at which this crude unsigned estimate loses strict negativity.

This is consistent with M19-066: nontrivial recurrence requires order-one stretching.

The unsigned estimate therefore cannot distinguish the tangent zero exponent from possible extra center exponents.

## 9. Correct refined theorem frontier

The finite-boundary realizability problem can now be stated spectrally:

\[
\boxed{
\mathcal T_{center}^{cocycle}:
\text{the linearized NS cocycle over the retained recurrent ancient hull has exactly one center direction, generated by time translation.}
}
\]

Equivalently, every bounded entire linearized solution modulo \(V_\theta\) should have a nonzero exponential rate or enter a previously typed compactness/remote exit.

If this theorem held with a uniform negative transverse exponent, the M19-067 projected-contraction route would become viable.

## 10. What zero-background stability does and does not imply

The strict zero-background spectrum is useful because it identifies the source of all possible center modes:

\[
\boxed{
\text{extra center dynamics must be created by the nonzero recurrent background, not by the bare similarity operator.}
}
\]

But it does not bound how many such modes a large recurrent background can create.

Therefore one must not infer

\[
\operatorname{spec}(\mathcal L_0)\cap i\mathbb R=\varnothing
\quad\Longrightarrow\quad
\text{simple center for }\mathcal L_{V(\theta)}.
\]

That would be exactly the unproved nonlinear spectral step.

## 11. Certified / not certified

### Certified

1. Zero-background similarity Stokes has strictly negative Gaussian spectrum.
2. Fixed-frequency resolvent analysis is valid for stationary backgrounds and Floquet theory for periodic backgrounds.
3. Aperiodic recurrent backgrounds require a linear skew-product cocycle.
4. Time translation supplies one exact center direction.
5. Existing unsigned weighted energy estimates do not distinguish that tangent mode from additional center modes.

### Not certified

1. One-dimensionality of the center cocycle.
2. Absence of additional bounded entire linearized modes.
3. Uniform transverse exponential contraction.
4. Global weak-critical scattering rigidity.
5. Global 3D Navier--Stokes regularity.

## 12. Next target

M19-071 should test a standard dynamical-systems refinement: instead of bounding the **largest** Lyapunov exponent, estimate the growth of **two-dimensional perturbation volumes**.

If the time tangent supplies one zero exponent while one can prove

\[
\boxed{
\lambda_1+\lambda_2<0,
}
\]

for every two-dimensional linearized subspace, then necessarily

\[
\lambda_2<0
\]

and the center is one-dimensional.

The corresponding calculation is the trace of the linearized generator on an orthonormal perturbation pair in the M19-063 weighted geometry.  Incompressibility and the trace-free nature of strain may provide cancellation invisible in the one-vector estimate.

If no such improvement occurs, the cocycle center theorem remains a genuinely new spectral rigidity problem.

---

\[
\boxed{\text{M19-070 COMPLETE; THE LAST INTERIOR REALIZABILITY FRONTIER IS A LINEAR-COCYCLE CENTER-SPECTRUM PROBLEM, NOT A FIXED-FREQUENCY RESOLVENT PROBLEM.}}
\]
