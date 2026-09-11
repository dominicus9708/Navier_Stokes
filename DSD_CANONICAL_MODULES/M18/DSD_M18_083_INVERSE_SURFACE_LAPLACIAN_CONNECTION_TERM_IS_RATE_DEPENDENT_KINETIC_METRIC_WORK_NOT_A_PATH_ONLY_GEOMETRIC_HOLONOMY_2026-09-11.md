# M18-083 — The inverse-surface-Laplacian connection term is rate-dependent kinetic-metric work, not a path-only geometric holonomy

**Date:** 2026-09-11  
**Status:** OPERATOR-CONNECTION AUDIT / GEOMETRIC-PHASE SHORTCUT RETIRED / RATE-DEPENDENCE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-082 rewrites the controlled CE-H redistribution current energy as

\[
\boxed{
\mathcal E_\psi
=
\frac12
\langle q',L_\theta^{-1}q'\rangle,
}
\]

where

\[
q:=q_\Sigma=\rho A_\Sigma
\]

is material surface flux density and

\[
L_\theta
\]

is the positive pulled-back Dirichlet surface Laplacian.

The remaining signed compensation comes from evolution of the surface metric/operator.

A tempting interpretation is that a closed recurrent loop in

\[
(q,L)
\]

might carry a rate-independent geometric phase or holonomy.

The present audit computes the exact operator connection term and shows that, at the level currently available, it is **rate-dependent kinetic work**, not a path-only Berry-type phase.

Thus no new topological signed cocycle follows from the inverse-Laplacian variation alone.

---

## 2. Operator notation

Set

\[
\boxed{G_\theta:=L_\theta^{-1}.}
\]

Then

\[
\boxed{
\psi=Gq'.
}

and

\[
\boxed{
\mathcal E_\psi
=
\frac12\langle q',Gq'\rangle.
}
\]

The pairing is on the fixed material reference patch.

---

## 3. Exact inverse-operator derivative

Differentiate

\[
L_\theta G_\theta=I.
\]

Then

\[
L'G+LG'=0.
\]

Multiplying by \(G=L^{-1}\),

\[
\boxed{
G'
=-GL'G.
}
\]

This is exact whenever the controlled elliptic family remains invertible on the fixed Dirichlet reference space.

---

## 4. Exact kinetic-energy derivative

Differentiate

\[
\mathcal E_\psi
=
\frac12\langle q',Gq'\rangle.
\]

Using symmetry of \(G\),

\[
\boxed{
\mathcal E_\psi'
=
\langle q'',Gq'\rangle
+
\frac12\langle q',G'q'\rangle.
}
\]

Insert

\[
G'=-GL'G.
\]

Then

\[
\boxed{
\mathcal E_\psi'
=
\langle q'',Gq'\rangle
-
\frac12
\langle Gq',L'Gq'\rangle.
}
\]

Since

\[
Gq'=\psi,
\]

this becomes

\[
\boxed{
\mathcal E_\psi'
=
\langle\psi,q''\rangle
-
\frac12\langle\psi,L'\psi\rangle.
}
\]

This is the operator form of M18-080.

---

## 5. Identification with the earlier CE-H terms

M18-082 identifies

\[
\boxed{
\langle\psi,q''\rangle
=
G_{\kappa\text{-}src}.
}
\]

M18-080--081 identify

\[
\boxed{
-\frac12\langle\psi,L'\psi\rangle
=
G_{\perp\text{-}strain}
=
\int\mathring\Sigma_\perp(J_G,J_G)dA.
}
\]

Therefore no additional hidden term appears:

\[
\boxed{
\mathcal E_\psi'
=
G_{\kappa\text{-}src}
+G_{\perp\text{-}strain}.
}
\]

The inverse-operator connection is exactly the already identified transverse-strain work.

---

## 6. Closed-loop work identity

For a recurrent loop satisfying

\[
q(T)=q(0),
\qquad
q'(T)=q'(0),
\qquad
L(T)=L(0),
\]

one has

\[
\mathcal E_\psi(T)=\mathcal E_\psi(0).
\]

Hence

\[
\boxed{
\oint
\langle q'',Gq'\rangle\,d\theta
=
\frac12
\oint
\langle Gq',L'Gq'\rangle\,d\theta.
}
\]

Equivalently,

\[
\boxed{
\oint G_{\kappa\text{-}src}\,d\theta
=-
\oint G_{\perp\text{-}strain}\,d\theta.
}
\]

This is work exchange, not a monotone law.

---

## 7. Test for a path-only geometric phase

A rate-independent geometric phase should depend only on the oriented closed path

\[
\Gamma:\theta\mapsto(q(\theta),L(\theta))
\]

and not on how fast the path is traversed.

Consider a smooth reparametrization of the same path:

\[
\theta=\theta(s),
\qquad
\dot\theta>0.
\]

The state velocities scale as

\[
q_\theta'
\sim
\dot s\,q_s,
\]

and

\[
L_\theta'
\sim
\dot s\,L_s.
\]

Therefore the metric-work integrand

\[
\langle Gq',L'Gq'\rangle
\]

is cubic in traversal speed:

\[
\boxed{
\langle Gq',L'Gq'\rangle
\sim
(\dot s)^3.
}
\]

After multiplication by

\[
d\theta=ds/\dot s,
\]

the integrated work scales like

\[
\boxed{(\dot s)^2}
\]

under uniform speed rescaling.

Hence it is not invariant under time reparametrization.

---

## 8. Therefore it is not a Berry-type 1-form

A path-only 1-form contribution would be linear in the state velocity:

\[
\mathcal A(X)\cdot X'
\]

so that

\[
\int\mathcal A\cdot dX
\]

is independent of traversal speed.

The present connection term is instead quadratic in the redistribution velocity \(q'\) and linear in metric velocity \(L'\):

\[
\boxed{
\frac12
\langle Gq',L'Gq'\rangle.
}
\]

Thus it is a kinetic-metric deformation work term.

No Berry-phase/holonomy interpretation is certified by this expression alone.

---

## 9. Time reversal

Reverse a closed recurrent trajectory.

Then

\[
q'\mapsto-q',
\qquad
L'\mapsto-L'.
\]

The instantaneous metric-work integrand changes sign because it contains two copies of \(q'\) and one copy of \(L'\).

Thus the signed work reverses with path orientation, but its magnitude still depends on the traversal rate.

Orientation sensitivity alone is therefore insufficient to call it a geometric phase.

---

## 10. Fixed-metric limit

If

\[
L'=0,
\]

then

\[
\boxed{
G_{\perp\text{-}strain}=0
}
\]

and

\[
\mathcal E_\psi'
=
\langle q'',Gq'\rangle.
\]

Every closed fixed-metric loop satisfies

\[
\boxed{
\oint\langle q'',Gq'\rangle\,d\theta=0.
}
\]

Therefore there is no hidden fixed-metric cycle phase in this quadratic kinetic structure.

This confirms the reversible-loop model of M18-082.

---

## 11. What would be needed for a genuine geometric cocycle

A new geometric phase would require an additional term of the form

\[
\boxed{
\mathcal A(q,L)\cdot(q',L')
}
\]

whose closed-loop integral is reparametrization invariant and whose exterior curvature is nonzero.

No such linear connection term has appeared in the current CE-H surface-current derivation.

The existing metric derivative contributes only through kinetic energy deformation.

Thus a genuine cycle-sensitive cocycle must come from additional PDE structure, topology, or lineage realization, not from the inverse-Laplacian kinetic metric alone.

---

## 12. Consequence for the finite-lineage cycle problem

The M18-077 branches

\[
G_{cycle}^{mean},
\qquad
G_{cycle}^{rev}
\]

cannot be excluded merely by declaring the evolving H-minus-one metric to have nontrivial holonomy.

At the current level:

\[
\boxed{
\text{metric-coupled cycle work}
=
\text{rate-dependent reversible energy exchange}.
}
\]

It may support recurrent dynamics without secular drift.

---

## 13. Updated strategic frontier

The surface-current route has now eliminated several false shortcuts:

1. pure label-invisible current circulation is impossible on a controlled nonzero Frobenius CE-H patch;
2. amplitude-area potential differences do not orient lineage transfer;
3. the Poisson Dirichlet energy is not a Lyapunov function;
4. the inverse-Laplacian metric connection is not a path-only geometric phase.

The remaining branches are therefore genuinely dynamical:

\[
\boxed{
\begin{cases}
\text{reversible finite-state redistribution/breather},\\
\text{mean conservative lineage circulation},\\
\text{self-helicity/twist},\\
\text{surface/label geometry degeneration}.
\end{cases}
}
\]

---

## 14. Highest-value next target

The next calculation should not search for another formal potential.

The higher-value question is whether the **fixed-metric reversible branch** is compatible with the full CE-H Navier--Stokes dynamics rather than merely with the kinematic surface-current subsystem.

A useful target is to combine

\[
q'=\kappa q,
\]

\[
L\psi=q',
\]

and the CE-H strain/amplitude recurrence to test whether a nontrivial periodic or recurrent redistribution loop necessarily produces one of the already identified amplitude/strain covariance structures.

In particular, compare the loop with the M18-062--070 amplitude-moment covariance and sheath/core split rather than introducing a new unsigned action.

---

## 15. Audit verdict

### Certified

1. \(G'= -GL'G\).
2. The inverse-Laplacian kinetic-energy derivative exactly reproduces the kappa-source plus transverse-strain work balance.
3. Closed-loop metric work is rate dependent.
4. The metric-work integral scales with traversal speed and is not a path-only holonomy.
5. No Berry-type linear connection term is present in the current derivation.
6. Fixed-metric recurrent loops have zero net source-work cycle integral while retaining positive current action.
7. The finite-lineage cycle problem remains genuinely dynamical, not topologically closed by the kinetic metric.

### Still open

- full CE-H compatibility of reversible current breathers;
- mean conservative lineage circulation;
- self-helicity/twist;
- surface/label geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 16. Next target

M18-084 should reconnect the reversible-current branch to the existing amplitude-moment covariance chain M18-062--070.

The question is whether a nontrivial closed loop of

\[
q_\Sigma'=\kappa q_\Sigma
\]

with zero mean material \(\kappa\) can coexist with the globally required negative \(\rho^2\)-weighted coefficient bias without forcing the already identified low-amplitude high-diffusion sheath / high-amplitude low-diffusion core segregation on the same recurrent material lineage.
