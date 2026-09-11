# M19-067 — Time translation is an exact linearized center mode, but quotienting by the full orbit erases the scattering translation, so rigidity requires simple center spectrum plus transverse contraction

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / PHASE-MODULATION FIREWALL / CENTER-SPECTRUM REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-066 showed that a nontrivial recurrent similarity state must sustain order-one mean vortex stretching, while the best linear gap in the polynomial \(A_2\) family is below \(1/5\).

This suggests that absolute contraction may be asking too much: part of the recurrent strain may sustain motion **along** the recurrent trajectory rather than separation **between** trajectories.

The first natural step is therefore to remove the exact time-translation tangent mode.  This module derives that mode and the corresponding modulated difference equation.

However a crucial firewall appears immediately.  The scattering map itself intertwines similarity-time translation with log-radius translation,

\[
\mathscr S(\sigma_tY)=T_{-t/2}\mathscr S(Y).
\]

Hence quotienting states by arbitrary time shifts also quotients out the very \(q\)-translation whose aperiodicity must be controlled.  Orbital distance alone cannot prove rigidity.

The useful surviving target is stronger and more precise:

\[
\boxed{
\text{time translation must be the only center direction, and every transverse direction must contract.}
}
\]

## 2. Autonomous similarity flow and its linearization

Write the incompressible similarity equation schematically as

\[
\partial_\theta U=\mathcal F(U),
\]

where

\[
\mathcal F(U)
=
\nu\Delta U
-\frac12U
-\frac12(y\cdot\nabla)U
-(U\cdot\nabla)U
-\nabla P[U].
\]

Let \(V(\theta)\) be a complete smooth trajectory.  Differentiating the equation in \(\theta\) gives

\[
\boxed{
\partial_\theta Z
=D\mathcal F(V)Z,
\qquad
Z:=\partial_\theta V.
}
\]

More explicitly,

\[
\boxed{
\begin{aligned}
\partial_\theta Z
={}&
\nu\Delta Z
-\frac12Z
-\frac12(y\cdot\nabla)Z\\
&-(V\cdot\nabla)Z
-(Z\cdot\nabla)V
-\nabla Q_Z,
\qquad \nabla\cdot Z=0.
\end{aligned}
}
\]

Thus similarity-time translation generates an exact variational solution.  It is the canonical center/tangent direction of every nonstationary orbit.

## 3. Modulated difference equation

Let \(U(\theta)\) and \(V(\theta)\) be two complete trajectories and introduce a phase function \(\tau(\theta)\).  Set

\[
\boxed{
\widetilde V(\theta):=V(\theta+\tau(\theta)),
\qquad
W:=U-\widetilde V.
}
\]

Because the similarity equation is autonomous,

\[
\partial_\theta\widetilde V
=(1+\tau')\mathcal F(\widetilde V).
\]

Therefore

\[
\boxed{
\partial_\theta W
=
\mathcal F(U)-\mathcal F(\widetilde V)
-\tau' Z_{\widetilde V},
}
\]

where

\[
Z_{\widetilde V}:=\partial_\theta V(\theta+\tau).
\]

Relative to the unmodulated difference equation of M19-063--065, the only new term is

\[
\boxed{-\tau'Z_{\widetilde V}.}
\]

## 4. Local phase condition

In the polynomial \(A_2\) weighted inner product

\[
\langle f,g\rangle_w:=\int f\cdot g\,wdy,
\]

a standard local modulation condition would be

\[
\boxed{
\langle W,Z_{\widetilde V}\rangle_w=0.
}
\]

If

\[
\|Z_{\widetilde V}\|_{L^2(w)}\ge z_*>0
\]

and the phase map is sufficiently regular, the implicit-function theorem can locally determine \(\tau\).

Differentiating the orthogonality relation determines \(\tau'\) from the component of the difference dynamics along \(Z_{\widetilde V}\).

This is the natural way to remove one exact center direction from the weighted energy estimate.

## 5. Why full orbital distance is too coarse

Define the naive orbital pseudodistance

\[
\boxed{
 d_{orb}(Y_1,Y_2)
:=
\inf_{t\in\mathbb R}
 d(Y_1,\sigma_tY_2).
}
\]

For a minimal aperiodic compact flow, this pseudodistance can vanish between distinct states.

The irrational Kronecker flow on \(\mathbb T^2\) from M19-061 is the basic example: every orbit is dense, so

\[
\boxed{d_{orb}(x,y)=0}
\]

for all \(x,y\) in the minimal torus, even though the flow is genuinely quasiperiodic and two-dimensional.

Hence

\[
\boxed{
\text{contraction in full orbital pseudodistance does not exclude quasiperiodic recurrence.}
}
\]

## 6. Scattering makes the same firewall exact

The scattering map satisfies

\[
\mathscr S(\sigma_tY)
=T_{-t/2}\mathscr S(Y).
\]

Therefore quotienting the interior by arbitrary \(\sigma_t\) identifies boundary data that differ by arbitrary log translation:

\[
A(q,\omega)
\sim
A(q-t/2,\omega).
\]

But distinguishing these translated phases is precisely the content of the surviving weak-critical scattering dynamics.

Thus

\[
\boxed{
\text{the full time-orbit quotient erases the observable that the proof must control.}
}
\]

A successful phase modulation may be used locally in estimates, but it cannot by itself be the final rigidity statement.

## 7. What transverse contraction would actually prove

Suppose one could prove the following stronger dynamical statement on the compact recurrent hull:

1. the center bundle is exactly one-dimensional and spanned by \(Z=\partial_\theta V\);
2. every perturbation transverse to this bundle contracts uniformly in a phase-modulated weighted norm;
3. the center flow has no additional neutral transverse phase variable.

Then the recurrent invariant set would be locally one-dimensional along the similarity-time flow.  Any quasiperiodic torus such as the M19-061 anti-model would be excluded because it necessarily has an additional neutral direction transverse to the flow tangent.

The remaining recurrent possibilities would be reduced to a stationary state or a genuinely closed one-dimensional orbit, subject to the usual global topology/completeness conditions.

Thus the missing spectral statement is

\[
\boxed{
\mathcal T_{center}^{simple}:
\ker/\text{center}(D\Phi)
=
\operatorname{span}\{\partial_\theta V\}
\quad\text{on the recurrent hull},
}
\]

plus a uniform transverse gap.

## 8. The M19-063 linear gap does not prove center simplicity

The polynomial \(A_2\) weight gives a coercive gap for the **bare similarity linear operator**

\[
\nu\Delta-\frac12-rac12y\cdot\nabla.
\]

The actual variational operator is

\[
\boxed{
\mathcal L_V
=
\mathcal L_{lin}
-(V\cdot\nabla)
-(\,\cdot\,\nabla)V
-\nabla\mathcal P_V,
}
\]

where \(\mathcal P_V\) is the linearized pressure operator.

The exact tangent solution \(Z=V_\theta\) already proves that the full variational dynamics possesses a neutral direction even though the bare operator has a strict gap.

Therefore the nonlinear coefficients necessarily cancel the bare gap along at least one direction.

This is another reason why estimating the full strain only by its unsigned norm loses essential structure.

## 9. A refined target for the weighted method

The weighted contraction route should now be reformulated as a **projected coercivity** problem.

Let \(\Pi_V^\perp\) denote projection onto a complement of the tangent mode in the weighted space.  The desired estimate is schematically

\[
\boxed{
\frac12\frac d{d\theta}
\|\Pi_V^\perp W\|_w^2
+
\delta_\perp
\|\Pi_V^\perp W\|_w^2
\le
\text{higher-order modulation errors},
}
\]

with

\[
\delta_\perp>0.
\]

The key point is that one no longer tries to make the entire recurrent strain small.  One asks whether the strain needed to sustain the background trajectory acts primarily in the tangent direction while the transverse spectrum remains damped.

## 10. Certified / not certified

### Certified

1. \(Z=\partial_\theta V\) is an exact solution of the linearized similarity equation.
2. Phase modulation introduces exactly the forcing \(-\tau'Z\).
3. Full orbital pseudodistance can vanish on an aperiodic minimal compact flow and therefore cannot establish rigidity.
4. In this problem the same quotient explicitly removes log-radius scattering translation because of scattering equivariance.
5. The bare \(A_2\) spectral gap does not imply a gap for the full variational operator; the tangent mode is an explicit counterexample.
6. The useful remaining weighted target is simplicity of the center direction plus transverse coercivity.

### Not certified

1. One-dimensionality of the center bundle for Navier--Stokes recurrent ancient states.
2. Uniform transverse contraction.
3. Exclusion of periodic recurrent similarity states by this argument alone.
4. Global weak-critical scattering rigidity.
5. Global 3D Navier--Stokes regularity.

## 11. Next target

M19-068 should test the projected-coercivity idea on the **scattering side**, where the tangent direction is explicit:

\[
\partial_\theta A=-\frac12\partial_q A
\]

along pure translation.

The question is whether an independent infinitesimal deformation of the scattering datum can be propagated inward with finite weighted energy, or whether all bounded recurrent linearized tail modes are generated by \(\partial_qA\) plus already typed amplitude/remote exits.

If extra bounded tail modes exist explicitly, center simplicity fails at leading order and the projected-contraction route cannot close without a genuinely nonlinear interior condition.

---

\[
\boxed{\text{M19-067 COMPLETE; THE LAST WEIGHTED ROUTE IS A SIMPLE-CENTER PLUS TRANSVERSE-GAP PROBLEM, NOT FULL ORBITAL CONTRACTION.}}
\]
