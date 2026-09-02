# DSD M5-600 — Global double-eigenline exact consequences and Burgers firewall

Date: 2026-09-03

Status: **CONDITIONAL ON THE M5-599 ANALYTICITY GLOBALIZATION. THE GLOBAL CE-H CLASS SATISFIES `Sigma W = sigma W` AND `Delta W = kappa W`. DIVERGENCE-FREENESS THEN MAKES `kappa` A VORTEX-LINE FIRST INTEGRAL, WHILE THE ANTISYMMETRIC PART OF `grad U` ANNIHILATES `W`, SO `(W·grad)U = sigma W`. THE WEIGHTED-HARMONIC DIRECTION EQUATION AND A NEGATIVE GLOBAL ENSTROPHY-WEIGHTED MEAN OF `kappa` FOLLOW EXACTLY. THESE ARE STRONG OVERDETERMINED CONSTRAINTS BUT NOT YET A CONTRADICTION; BURGERS-TYPE VORTICES SHOW THAT THE LOCAL ALIGNMENT ALGEBRA ITSELF IS CONSISTENT WITH NAVIER--STOKES. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Global double eigenline system

Assume the M5-599 branch. Then for all space-time points, in cross-product form,

\[
W\times\Sigma W=0,
\qquad
W\times\Delta W=0.
\]

On the open set

\[
\Omega_W:=\{(y,\theta):W(y,\theta)\ne0\},
\]

define

\[
\boxed{
\sigma:=\frac{W\cdot\Sigma W}{|W|^2},
\qquad
\kappa:=\frac{W\cdot\Delta W}{|W|^2}.
}
\]

Then

\[
\boxed{
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W.
}
\]

## 2. Viscous eigenvalue is constant along vortex lines

Because

\[
\nabla\cdot W=0,
\]

we also have

\[
\nabla\cdot\Delta W=\Delta(\nabla\cdot W)=0.
\]

Using

\[
\Delta W=\kappa W,
\]

we obtain

\[
0
=\nabla\cdot(\kappa W)
=W\cdot\nabla\kappa
+\kappa\nabla\cdot W.
\]

Hence

\[
\boxed{
W\cdot\nabla\kappa=0.
}
\]

Equivalently,

\[
\boxed{
\xi\cdot\nabla\kappa=0
}
\]

where \(W=\rho\xi\).

Thus the scalar by which viscosity acts on the vorticity is a first integral of the instantaneous vortex-line foliation.

## 3. Stretching eigenline equals a directional-derivative eigenline

Decompose

\[
\nabla U=\Sigma+\mathcal R,
\]

where \(\mathcal R\) is antisymmetric.

Since

\[
W=\nabla\times U,
\]

one has

\[
\mathcal R v=\frac12W\times v.
\]

Therefore

\[
\mathcal RW=\frac12W\times W=0.
\]

Hence

\[
( W\cdot\nabla)U
=(\nabla U)W
=\Sigma W
=\sigma W.
\]

Thus

\[
\boxed{
(W\cdot\nabla)U=\sigma W,
}
\]

or, after dividing by \(\rho\),

\[
\boxed{
(\xi\cdot\nabla)U=\sigma\xi.
}
\]

The velocity derivative along a vortex line has no transverse component.

## 4. Exact scalar/vector decomposition

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Expand

\[
\Delta W
=(\Delta\rho)\xi
+2\nabla\rho\cdot\nabla\xi
+\rho\Delta\xi.
\]

Because

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

the parallel part gives

\[
\boxed{
\kappa
=\frac{\Delta\rho}{\rho}-|\nabla\xi|^2.
}
\]

The transverse part gives

\[
\boxed{
\Delta\xi
+2\nabla\log\rho\cdot\nabla\xi
+|\nabla\xi|^2\xi=0.
}
\]

Equivalently,

\[
\boxed{
(I-\xi\otimes\xi)
\nabla\cdot(\rho^2\nabla\xi)=0.
}
\]

This recovers the M5-487 weighted-harmonic direction equation, now globally.

## 5. Divergence-free amplitude constraint

Since

\[
\nabla\cdot(\rho\xi)=0,
\]

we have

\[
\boxed{
\xi\cdot\nabla\log\rho
=-\nabla\cdot\xi.
}
\]

Thus amplitude variation along vortex lines is not independent of the geometry of the direction field.

## 6. Material evolution becomes scalar multiplication

The similarity vorticity equation is

\[
D_BW
=(\Sigma-I)W+\Delta W.
\]

Using both eigenline relations,

\[
\boxed{
D_BW
=(\sigma+\kappa-1)W.
}
\]

Thus

\[
\boxed{
D_B\xi=0,
}
\]

and

\[
\boxed{
D_B\log\rho
=\sigma+\kappa-1.
}
\]

The whole viscous/stretching evolution changes only the scalar vorticity magnitude.

## 7. Global weighted mean of the viscous eigenvalue

Because \(W\in H^1\cap L^2\), integration by parts gives

\[
\int_{\mathbb R^3}W\cdot\Delta W\,dy
=-\int_{\mathbb R^3}|\nabla W|^2dy.
\]

Therefore

\[
\boxed{
\int\kappa|W|^2dy=-P.
}
\]

If \(W\not\equiv0\), then

\[
\boxed{
\frac{\int\kappa|W|^2}{\int|W|^2}
=-\frac PE<0.
}
\]

Hence \(\kappa\) cannot be nonnegative on the whole active vorticity set unless the solution is trivial.

The recurrent payer marker may still sample a positive or less-negative subset; this global weighted negativity is not by itself incompatible with the M5-596 marker balance.

## 8. Combined global stretching-diffusion multiplier

Define

\[
\lambda:=\sigma+\kappa.
\]

Then

\[
D_BW=(\lambda-1)W.
\]

The global enstrophy ledger gives

\[
\frac12E'+\frac14E+P=Q,
\]

with

\[
Q=\int\sigma|W|^2,
\qquad
-P=\int\kappa|W|^2.
\]

Hence

\[
\boxed{
\int\lambda|W|^2dy
=Q-P
=\frac12E'+\frac14E.
}
\]

On an invariant recurrent average,

\[
\boxed{
\left\langle\int\lambda|W|^2\right\rangle
=\frac14\langle E\rangle.
}
\]

This is a global enstrophy-weighted multiplier constraint.

It should not be confused with the same-marker return identity \(\langle\lambda\rangle_{marker}=1\); the two use different measures.

## 9. Burgers-type firewall

The local algebra

\[
S\omega\parallel\omega,
\qquad
\Delta\omega\parallel\omega
\]

is known to occur in stretched-vortex constructions such as the classical Burgers vortex: the axial vorticity is a strain eigenvector while viscous diffusion balances the stretching.

Therefore no argument may claim that the double-eigenline equations are locally inconsistent with Navier--Stokes.

The current branch is substantially narrower because it also requires

\[
W\in L^2,
\qquad
U\in L^6,
\qquad
\Sigma\in L^2,
\]

and recurrent ancient dynamics on all of \(\mathbb R^3\), whereas the standard Burgers background strain does not decay and has infinite whole-space energy/strain norm.

The next rigidity target must use these global normalization properties.

## 10. Next target: commutator compatibility

The two equations

\[
D_BW=(\lambda-1)W,
\qquad
\Delta W=\kappa W
\]

must be mutually compatible.

Commuting the material derivative with the Laplacian yields a new overdetermined tensor identity involving \(\nabla U\), \(\nabla^2W\), \(\nabla\lambda\), and \(\nabla\times W\).

Unlike another positive-charge estimate, that identity is an exact PDE compatibility condition and is the correct next branch.

Status: **THE GLOBAL CE-H CLASS IS NOW AN OVERDETERMINED DOUBLE-EIGENLINE SYSTEM WITH A VORTEX-LINE FIRST INTEGRAL `kappa`, PURELY SCALAR MATERIAL VORTICITY EVOLUTION, AND A STRICTLY NEGATIVE GLOBAL ENSTROPHY-WEIGHTED MEAN OF `kappa`. NO CONTRADICTION HAS YET BEEN DERIVED. GLOBAL REGULARITY REMAINS UNPROVED.**