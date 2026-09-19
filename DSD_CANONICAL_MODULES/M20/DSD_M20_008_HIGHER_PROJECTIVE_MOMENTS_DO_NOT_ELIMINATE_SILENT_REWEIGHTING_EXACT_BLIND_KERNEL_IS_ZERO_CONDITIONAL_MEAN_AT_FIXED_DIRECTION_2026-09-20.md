# M20-008 — Higher projective moments do not eliminate silent amplitude reweighting: the exact blind kernel is zero conditional mean at fixed vorticity direction

Date: 2026-09-20  
Canonical ID: **M20-008**  
Status: **PROJECTIVE-OBSERVABILITY NO-GO / THE M20-003 SECOND-MOMENT-SILENT REWEIGHTING BRANCH MAY BE DETECTED BY HIGHER DIRECTION MOMENTS, BUT THERE IS AN EXACT INFINITE-HIERARCHY BLIND KERNEL / A CENTERED RELATIVE GROWTH FIELD phi=lambda-alpha IS INVISIBLE TO EVERY DIRECTION-ONLY OBSERVABLE IF AND ONLY IF E[phi|Q]=0 / NONZERO REWEIGHTING VARIANCE CAN LIVE ENTIRELY INSIDE FIBERS OF FIXED PROJECTIVE DIRECTION / CLOSURE REQUIRES A JOINT AMPLITUDE-SPATIAL-STRAIN LABEL, NOT PURE PROJECTIVE MOMENTS ALONE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Reweighting law from M20-003

At the terminal boundary define the normalized enstrophy probability

\[
d\pi_B
=
\frac{|B|^2}{b_2}d\mu.
\]

Let

\[
\lambda
=
\partial_z\log|G|\big|_{z=0},
\]

and

\[
\alpha
=
\mathbb E_{\pi_B}\lambda.
\]

Define the centered relative-growth field

\[
\boxed{
\phi:=\lambda-\alpha.
}
\]

Then

\[
\mathbb E_{\pi_B}\phi=0,
\]

and M20-003 gives

\[
\boxed{
\partial_zd\pi_z|_0
=
2\phi\,d\pi_B.
}
\]

The reweighting variance is

\[
\boxed{
\operatorname{Var}_{\pi_B}(\lambda)
=
\mathbb E_{\pi_B}\phi^2.
}
\]

## 2. Direction-only observables

Let

\[
Q:=\xi_B\otimes\xi_B
\]

be the projective vorticity-direction state.

For any bounded measurable function

\[
F=F(Q)
\]

that depends only on projective direction, its change caused purely by probability reweighting is

\[
\boxed{
\left.
\frac d{dz}
\mathbb E_{\pi_z}[F(Q)]
\right|_{\rm rw,\,z=0}
=
2\mathbb E_{\pi_B}[\phi F(Q)].
}
\]

Thus projective observability of reweighting is exactly a covariance problem.

## 3. Conditional expectation is the complete direction-only projection

Let

\[
\boxed{
m(Q)
:=
\mathbb E_{\pi_B}[\phi\mid Q].
}
\]

Then for every bounded measurable \(F(Q)\),

\[
\mathbb E[\phi F(Q)]
=
\mathbb E[m(Q)F(Q)].
\]

Therefore the entire direction-only effect of the reweighting current is determined by the single conditional-mean field

\[
m(Q).
\]

The orthogonal remainder

\[
\boxed{
\phi_{\rm fib}
:=
\phi-m(Q)
}
\]

satisfies

\[
\boxed{
\mathbb E[\phi_{\rm fib}\mid Q]=0.
}
\]

It is invisible to every direction-only first-order statistic.

## 4. Exact observability theorem

The following are equivalent:

### A

\[
\boxed{
\mathbb E[\phi\mid Q]=0
\quad\text{a.s.}
}
\]

### B

For every bounded measurable direction-only observable \(F(Q)\),

\[
\boxed{
\mathbb E[\phi F(Q)]=0.
}
\]

### C

Every bounded direction-only observable has zero first-order reweighting derivative:

\[
\boxed{
\left.
\frac d{dz}
\mathbb E_{\pi_z}[F(Q)]
\right|_{\rm rw,0}
=
0.
}
\]

Thus

\[
\boxed{
\ker(\text{all direction-only reweighting observations})
=
\{\phi:\mathbb E[\phi\mid Q]=0\}.
}
\]

## 5. Variance decomposition

The law of total variance gives

\[
\boxed{
\operatorname{Var}(\lambda)
=
\mathbb E[m(Q)^2]
+
\mathbb E[\phi_{\rm fib}^2].
}
\]

Because \(\mathbb E\phi=0\), the first term is

\[
\operatorname{Var}\bigl(\mathbb E[\lambda\mid Q]\bigr).
\]

Hence the M20 reweighting energy splits exactly into:

\[
\boxed{
\text{between-direction selection}
+
\text{within-direction-fiber reweighting}.
}
\]

More explicitly,

\[
\boxed{
V_{\rm reweight}
\Longrightarrow
R_{\rm direction}
\lor
R_{\rm fiber}.
}
\]

## 6. Relation to the M20-003 second-moment branch

M20-003 tests the covariance

\[
\operatorname{Cov}(\lambda,Q)
=
\mathbb E[\phi Q].
\]

If this is nonzero, the second projective moment changes.

If

\[
\mathbb E[\phi Q]=0
\]

but

\[
m(Q)\neq0,
\]

then the second moment is silent but some higher/nonlinear function of direction can still detect reweighting.

Therefore the M20-003 branch

\[
R_{\rm silent}
\]

must be refined.

## 7. Higher tensor moments

For every integer \(k\ge1\), consider

\[
\boxed{
M_k
:=
\mathbb E_{\pi_B}[Q^{\otimes k}].
}
\]

Its pure reweighting derivative is

\[
\boxed{
(M_k)'_{\rm rw}
=
2\mathbb E[\phi Q^{\otimes k}].
}
\]

Thus a second-moment-silent current may still appear at some higher k.

This motivates the intermediate branch

\[
\boxed{
R_{\rm high}
:
\exists k\ge2
\text{ such that }
\mathbb E[\phi Q^{\otimes k}]\neq0.
}
\]

## 8. All projective moments are still not enough against the fiber kernel

The projective state space of rank-one unoriented projectors

\[
Q=\xi\otimes\xi
\]

is compact.

Polynomials in the matrix entries of Q separate projective directions and generate a dense algebra of continuous functions on this compact state space.

Therefore if

\[
\mathbb E[\phi Q^{\otimes k}]=0
\qquad
\forall k\ge0,
\]

then

\[
\mathbb E[\phi F(Q)]=0
\]

for every continuous \(F\), and hence

\[
\boxed{
\mathbb E[\phi\mid Q]=0
}
\]

in the direction-only sigma algebra.

Thus the infinite projective-moment hierarchy has the same exact blind kernel as Section 4.

## 9. Explicit anti-model

Let the projective direction be fixed:

\[
Q(x)\equiv Q_0.
\]

Let

\[
\phi(x)
\]

be any nonzero mean-zero scalar in \(L^2(\pi_B)\).

Then

\[
\operatorname{Var}(\lambda)
=
\mathbb E\phi^2>0,
\]

but for every direction-only observable,

\[
F(Q(x))=F(Q_0)
\]

is constant, so

\[
\mathbb E[\phi F(Q)]
=
F(Q_0)\mathbb E\phi
=
0.
\]

Hence

\[
\boxed{
\text{nonzero reweighting can be invisible to every projective moment}.
}
\]

This is a kinematic observability counterexample, not a Navier--Stokes solution.

## 10. More general fiber interpretation

Even when many directions are present, reweighting may occur inside each direction class with zero conditional mean:

\[
\mathbb E[\phi\mid Q]=0.
\]

Then:

- high-growth and low-growth states coexist within the same projective direction;
- their net direction-conditioned weight transfer cancels;
- the total enstrophy probability moves in the full state space;
- the marginal distribution of vorticity directions is stationary to first order.

Thus projective silence does not mean dynamical silence.

It means that the hidden current lies in variables discarded by the direction projection.

## 11. What labels can detect the fiber current

To observe

\[
R_{\rm fiber},
\]

one must enlarge the state beyond Q.

Candidate joint labels include:

\[
(q,\omega),
\]

local amplitude \(|B|\),

\[
\gamma=\xi^TS\xi,
\]

projective strain commutator

\[
[S,Q],
\]

viscous coefficient/derivative data,

or spatial/material lineage labels.

For a joint observable \(Y\), the relevant conditional mean is

\[
\boxed{
\mathbb E[\phi\mid Q,Y].
}
\]

A useful label is one for which this conditional mean is nonzero and tied to a controlled PDE channel.

## 12. Relation to M19-331--332

M19-331--332 already show that amplitude reweighting can persist as recurrent population selection without violating finite material population conservation.

M20-008 identifies the projective analogue of the same obstruction:

\[
\boxed{
\text{direction marginal}
\text{ can remain fixed while hidden amplitude selection cycles inside direction fibers}.
}
\]

Therefore replacing second projective covariance by an arbitrarily large hierarchy of direction moments does not automatically remove recurrent hysteresis.

## 13. Corrected reweighting architecture

The authoritative reweighting split is now

\[
\boxed{
V_{\rm reweight}
\Longrightarrow
R_{\rm high}
\lor
R_{\rm fiber}.
}
\]

Here:

- \(R_{\rm high}\): some direction-only observable or higher projective moment detects the selection current;
- \(R_{\rm fiber}\): \(\mathbb E[\lambda-\alpha\mid Q]=0\), so every direction-only observable is first-order blind.

The previous label \(R_{\rm silent}\) should be interpreted as containing both until this refinement is applied.

## 14. Strategic consequence

Pure projective hierarchy is not a complete state description for the reweighting branch.

The next useful step is not simply

\[
Q,\ Q^{\otimes2},\ Q^{\otimes3},\ldots
\]

without end.

One must attach at least one dynamical scalar/tensor label to Q.

The most natural candidate is the axial stretching scalar

\[
\gamma=\xi^TS\xi,
\]

because the vorticity magnitude equation directly couples amplitude growth to \(\gamma\), diffusion, and direction gradients.

## 15. Next target

M20-009 should derive the exact terminal-wedge formula for

\[
\lambda
=
\partial_z\log|G|\big|_0
\]

from the vorticity-magnitude equation.

This will decompose the reweighting current

\[
\phi=\lambda-\alpha
\]

into:

- relative axial stretching;
- scalar vorticity diffusion;
- direction-gradient damping;
- Eulerian transport/homogeneity terms.

That is the correct way to expose the hidden \(R_{\rm fiber}\) current to PDE structure.

\[
\boxed{\text{M20-008 COMPLETE; THE EXACT BLIND KERNEL OF ALL DIRECTION-ONLY REWEIGHTING OBSERVABLES IS }E[\lambda-\alpha\mid Q]=0.}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
