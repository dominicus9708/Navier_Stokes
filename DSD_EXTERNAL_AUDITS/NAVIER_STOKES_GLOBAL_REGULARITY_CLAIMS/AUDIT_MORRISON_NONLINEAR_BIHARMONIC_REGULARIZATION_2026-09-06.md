# DSD Audit — Morrison Nonlinear Biharmonic Dissipative Regularization

Date: 2026-09-06
Source family: Kemar Armando Morrison, *A Rigorous Proof of Global Existence and Smoothness for the 3D Incompressible Navier-Stokes Equations via Non-Linear Dissipative Regularization*, Zenodo DOI family including 18364704 / 18371207 / 18371254, Jan 2026.
Audit status: **MODIFIED PDE / VANISHING-REGULARIZATION BRIDGE REQUIRED**

## 1. Public mechanism

The abstract states that the proof introduces a new nonlinear dissipative regularization involving a biharmonic operator, derives global energy/enstrophy bounds for the regularized system, and then uses spectral/Galerkin/compactness methods to conclude global regularity.

## 2. Problem-definition audit

The classical Clay equation has viscosity

\[
-\nu\Delta u
\]

and no additional biharmonic/hyperviscous stabilizer.

If the proof studies instead an equation schematically of the form

\[
\partial_tu+(u\cdot\nabla)u+\nabla p
=\nu\Delta u-\varepsilon\mathcal R_4(u),
\]

where `\mathcal R_4` contains fourth derivatives or another positive high-frequency damping term, then for each fixed `ε>0` the problem is a **regularized/hyperdissipative model**.

Global smoothness of that modified model does not itself prove global smoothness at `ε=0`.

## 3. Required vanishing-regularization theorem

To recover the classical NSE one must prove estimates

\[
\|u_\varepsilon\|_X\le C
\]

in a regularity space `X` strong enough to imply smoothness, with `C` **independent of ε**, and then pass `ε→0` strongly enough to preserve the nonlinear term and the desired critical/higher norm.

Ordinary energy estimates often remain uniform and yield a Leray weak solution. The open Millennium difficulty is precisely the lack of an ε-independent estimate preventing concentration of higher derivatives/vorticity in the limit.

Thus:

\[
\boxed{
\text{smooth for every }\varepsilon>0
\not\Rightarrow
\text{smooth at }\varepsilon=0.
}
\]

## 4. Spectral-tail audit

An exponential high-frequency tail produced by a biharmonic term may depend on ε through a dissipation scale. If the analyticity radius or spectral-decay constant shrinks to zero as `ε→0`, it cannot close the classical equation.

Therefore every claimed exponential tail must be audited for **uniformity in the regularization parameter**.

## 5. Galerkin compactness audit

Faedo–Galerkin + energy + Aubin–Lions can provide convergence to weak solutions. To conclude global strong/smooth convergence, one needs uniform higher-order compactness beyond what the classical energy inequality already gives.

The extra regularizer may supply this only with constants diverging as it is removed.

## 6. DSD verdict

The regularized equation is a legitimate mathematical model and may well be globally smooth. But an unconditional solution of the Clay problem requires a separate vanishing-regularization bridge with ε-independent strong bounds.

\[
\boxed{
\text{Fixed positive biharmonic regularization solves a modified problem, not automatically classical 3D NSE.}
}
\]

Until that bridge is proved, the Clay-level conclusion is a **SCOPE_MISMATCH / OPEN LIMIT GATE**.

Global regularity remains unproved.
