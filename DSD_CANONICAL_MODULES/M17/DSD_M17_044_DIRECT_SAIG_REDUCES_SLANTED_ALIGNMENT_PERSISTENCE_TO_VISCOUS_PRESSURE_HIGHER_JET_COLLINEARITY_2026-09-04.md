# DSD M17-044 — Direct SAIG reduces slanted alignment persistence to viscous–pressure higher-jet collinearity

Date: 2026-09-04
Canonical ID: **M17-044**

Status: **INTERNAL DIRECT SLANTED-ALIGNMENT PDE FORCING / STARTING FROM THE SAME SIMILARITY NAVIER--STOKES NORMALIZATION THAT GIVES THE CANONICAL VORTICITY LAW `D_BW=(W·grad)U+Delta W-W`, THE VELOCITY-GRADIENT MATRIX SATISFIES `D_B A=Delta A-A-A^2-nabla^2P`. ITS SYMMETRIC PART OBEYS `D_B Sigma=Delta Sigma-Sigma-Sigma^2-Omega^2-nabla^2P`. AT A REGULAR NODAL CORE `W=0`, SO `Omega=0` AND `Sigma_h=lambda I`. DIRECTLY MATERIAL-DIFFERENTIATING THE SLANT COMPENSATOR `C_p=TF[(p·grad_h)Sigma_h]`, USING `D_Bp=3lambda p`, CAUSES ALL LAMBDA-DEPENDENT LOWER-ORDER TERMS TO CANCEL, LEAVING THE EXACT LAW `D_BC_p=-(3/2)C_p+TF[(p·grad_h)(Delta Sigma_h-nabla_h^2P)]`. COMPARISON WITH THE REQUIRED ALIGNMENT `C_p=-(G_q-1)Q_0`, `D_BQ_0=(kappa-3/2)Q_0`, YIELDS THE DIRECT PDE CONDITION `F_p:=TF[(p·grad_h)(Delta Sigma_h-nabla_h^2P)]=-[D_B(G_q-1)+kappa(G_q-1)]Q_0`. THUS THE PERPENDICULAR VISCOUS--PRESSURE HIGHER-JET FORCING MUST VANISH EXACTLY: `P^perp_{Q_0}F_p=0`. THIS IS THE FIRST DIRECT DYNAMIC TEST OF THE SLANTED ALIGNMENT MANIFOLD; IT IS NOT AUTOMATIC FROM THE STATIC THIRD-JET LAW. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity velocity equation and normalization check

Use the similarity velocity equation in the normalization already implicit in the M17/M5 vorticity law:

\[
\boxed{
D_BU
=\Delta U
-\frac12U
-\nabla P,
\qquad
B=U+\frac12y.
}
\]

Taking curl gives

\[
\boxed{
D_BW
=(W\cdot\nabla)U
+\Delta W
-W,
}
\]

which is exactly the canonical equation used in M5-682 and M17.

Thus the coefficient/sign convention is fixed internally.

---

## 2. Velocity-gradient equation

Let

\[
A:=\nabla U,
\qquad
A_{ij}=\partial_jU_i.
\]

Differentiate the velocity equation.
The material/spatial commutator gives

\[
D_BA_{ij}
=\partial_j(D_BU_i)
-(\partial_jB_k)A_{ik}.
\]

Since

\[
\partial_jB_k=A_{kj}+\frac12\delta_{kj},
\]

we obtain

\[
\boxed{
D_BA
=\Delta A
-A
-A^2
-\nabla^2P.
}
\]

The two `-A/2` contributions come respectively from the explicit similarity damping and the derivative of the similarity drift.

---

## 3. Symmetric strain equation

Write

\[
A=\Sigma+\Omega
\]

with `Sigma` symmetric and `Omega` antisymmetric.

The symmetric part of `A^2` is

\[
\operatorname{sym}(A^2)
=\Sigma^2+\Omega^2,
\]

because

\[
\Sigma\Omega+\Omega\Sigma
\]

is antisymmetric.

Therefore

\[
\boxed{
D_B\Sigma
=\Delta\Sigma
-\Sigma
-\Sigma^2
-\Omega^2
-\nabla^2P.
}
\]

---

## 4. Nodal-core simplification

At a regular winding nodal core,

\[
W=0.
\]

Hence the antisymmetric velocity-gradient part vanishes:

\[
\boxed{\Omega=0.}
\]

M17-010 gives

\[
\Sigma
=\operatorname{diag}(\lambda,\lambda,-2\lambda)
\]

in the fixed great-circle frame.

Its horizontal block is

\[
\boxed{
\Sigma_h=\lambda I_2.
}
\]

On the great-circle branch this horizontal block is exactly

\[
H_\phi=\nabla_h^2\phi.
\]

---

## 5. Slant compensator

Define

\[
\boxed{
C_p
:=TF[(p\cdot\nabla_h)\Sigma_h].
}
\]

M17-025 identifies this with the reconstruction compensator and requires

\[
\boxed{
C_p=-(G_q-1)Q_0.
}
\]

M17-024 gives the exact material slope law

\[
\boxed{
D_Bp=3\lambda p.
}
\]

---

## 6. Direct material derivative of C_p

Differentiate

\[
(p\cdot\nabla_h)\Sigma_h.
\]

We have

\[
D_B[(p\cdot\nabla_h)\Sigma_h]
=(D_Bp)\cdot\nabla_h\Sigma_h
+p_\ell D_B(\partial_\ell\Sigma_h).
\]

For a horizontal derivative,

\[
D_B(\partial_\ell\Sigma_h)
=\partial_\ell(D_B\Sigma_h)
-(\partial_\ell B_m)\partial_m\Sigma_h.
\]

At the nodal core,

\[
\partial_\ell B_m
=(\lambda+\tfrac12)\delta_{m\ell}
\]

for horizontal `ell`, with no horizontal-to-vertical off-diagonal term.

Therefore the commutator contribution is

\[
-(\lambda+\tfrac12)(p\cdot\nabla_h)\Sigma_h.
\]

The `D_Bp` contribution is

\[
3\lambda(p\cdot\nabla_h)\Sigma_h.
\]

---

## 7. Differentiate the strain PDE along p

At the core,

\[
D_B\Sigma_h
=\Delta\Sigma_h
-\Sigma_h
-(\Sigma^2)_h
-\nabla_h^2P,
\]

because `Omega=0` and the first derivative of `Omega^2` also vanishes at `Omega=0`.

Differentiate along `p`:

\[
(p\cdot\nabla_h)D_B\Sigma_h
=(p\cdot\nabla_h)(\Delta\Sigma_h-\nabla_h^2P)
-(p\cdot\nabla_h)\Sigma_h
-(p\cdot\nabla_h)(\Sigma^2)_h.
\]

At the isotropic horizontal core,

\[
\Sigma_h=\lambda I,
\]

and the horizontal block of the derivative of `Sigma^2` is

\[
\boxed{
(p\cdot\nabla_h)(\Sigma^2)_h
=2\lambda(p\cdot\nabla_h)\Sigma_h
}
\]

up to terms whose horizontal block vanishes because the core cross-strain entries are zero.

---

## 8. Exact cancellation of lambda-dependent lower-order terms

Collect the coefficients multiplying

\[
(p\cdot\nabla_h)\Sigma_h.
\]

They are

1. `+3lambda` from `D_Bp`;
2. `-1` from the linear strain term;
3. `-2lambda` from the quadratic strain term;
4. `-(lambda+1/2)` from the material/spatial commutator.

The sum is

\[
3\lambda-1-2\lambda-(\lambda+\tfrac12)
=-\frac32.
\]

Thus, after taking the trace-free horizontal part,

\[
\boxed{
D_BC_p
=-\frac32C_p
+F_p,
}
\]

where

\[
\boxed{
F_p
:=TF\left[
(p\cdot\nabla_h)
(\Delta\Sigma_h-\nabla_h^2P)
\right].
}
\]

All explicit `lambda` dependence cancels.

---

## 9. Compare with the required alignment evolution

Set

\[
g:=G_q-1.
\]

M17-043 gives

\[
C_p=-gQ_0
\]

and

\[
D_BQ_0
=(\kappa-\frac32)Q_0.
\]

Therefore differentiating the required alignment gives

\[
D_BC_p
=-\left[
D_Bg+(\kappa-\frac32)g
\right]Q_0.
\]

The direct PDE law gives

\[
D_BC_p
=\frac32gQ_0+F_p.
\]

Equate them:

\[
\frac32gQ_0+F_p
=-D_Bg\,Q_0-(\kappa-\frac32)gQ_0.
\]

The `3/2` terms cancel, leaving

\[
\boxed{
F_p
=-\left(D_Bg+\kappa g\right)Q_0.
}
\]

Equivalently,

\[
\boxed{
TF[(p\cdot\nabla_h)(\Delta\Sigma_h-\nabla_h^2P)]
=-\left[
D_B(G_q-1)+\kappa(G_q-1)
\right]Q_0.
}
\]

---

## 10. Direct perpendicular forcing gate

The right side lies entirely in the one-dimensional tensor line `span{Q_0}`.
Therefore the direct Navier--Stokes PDE must satisfy

\[
\boxed{
P_{Q_0}^{\perp}F_p=0.
}
\]

That is,

\[
\boxed{
P_{Q_0}^{\perp}
TF[(p\cdot\nabla_h)(\Delta\Sigma_h-\nabla_h^2P)]
=0.
}
\]

This is the direct DSAIG compatibility condition.

A nonzero perpendicular viscous-pressure forcing is incompatible with persistence of a regular nonconformal slanted CE-H core.

---

## 11. Scalar compensation evolution

Project Section 9 onto `Q_0`:

\[
\boxed{
D_Bg+\kappa g
=-\frac{F_p:Q_0}{|Q_0|^2}.
}
\]

Thus the departure

\[
g=G_q-1
\]

is not freely prescribed.
It is driven by the component of the viscous-pressure higher-jet forcing along the frozen nodal anisotropy line.

This is a closed scalar material equation once `F_p` is known.

---

## 12. Vertical limit

If

\[
p=0,
\]

then

\[
F_p=0,
\qquad
C_p=0.
\]

For a nonconformal core,

\[
g=0
\]

by M17-015.

The scalar law becomes

\[
0=0,
\]

so the direct forcing gate reduces consistently to the vertical result.

---

## 13. Why this is stronger than codimension counting

M17-025 said only that the third-jet tensor `C_p` must align with `Q_0`.
M17-044 now identifies the actual **PDE forcing** that must preserve that line:

\[
\boxed{
F_p
=TF[(p\cdot\nabla_h)(\Delta\Sigma_h-\nabla_h^2P)].
}
\]

The branch survives only if this viscous-pressure higher-jet forcing is aligned at every retained time.

Thus the problem has become an explicit pressure/viscous collinearity question rather than an abstract invariant-manifold question.

---

## 14. DSD audit

### Audit A — sign of the similarity damping
Checked internally by recovering the canonical M17/M5 vorticity equation after taking curl.

### Audit B — forgetting derivative of Omega^2
At the nodal core `Omega=0`, so the first spatial derivative of `Omega^2` vanishes exactly.

### Audit C — treating the pressure Hessian as local
Rejected. `nabla^2P` is nonlocal through the pressure Poisson equation; the gate is a genuine local/nonlocal compatibility condition.

### Audit D — claiming generic nonalignment is already proved
Rejected. The formula identifies the forbidden component but does not show it must be nonzero for every non-axisymmetric solution.

### Audit E — proof status
The slanted Rank-1 branch is sharply constrained but not yet closed.

---

## 15. Updated slanted Rank-1 frontier

A regular nonconformal slanted core must now satisfy simultaneously

\[
\boxed{
\begin{aligned}
C_p&=-(G_q-1)Q_0,\\
F_p&=-[D_B(G_q-1)+\kappa(G_q-1)]Q_0,\\
P_{Q_0}^{\perp}F_p&=0,\\
D_BQ_0&=(\kappa-3/2)Q_0,\\
D_Bp&=3\lambda p.
\end{aligned}
}
\]

Thus both the third-jet compensation and the fourth-order viscous/pressure forcing are confined to the same frozen traceless-tensor line.

---

## 16. Next target

The natural next step is the pressure decomposition.
Use

\[
-\Delta P
=\partial_iU_j\partial_jU_i
=\operatorname{tr}(A^2)
\]

and the CE-H eigenframe to split `F_p` into

1. a local viscous fourth-jet term;
2. a nonlocal Calderon--Zygmund pressure contribution generated by the whole active core.

The question is whether the perpendicular part can vanish persistently without forcing an additional symmetry/reduction of the finite source architecture.

This is the **Pressure–Viscous Alignment Gate (PVAG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
