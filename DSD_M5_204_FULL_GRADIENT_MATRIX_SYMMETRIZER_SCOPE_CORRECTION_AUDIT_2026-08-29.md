# DSD M5-204 — Full-Gradient Matrix Symmetrizer Scope Correction

Date: 2026-08-29

Parent: `DSD_M5_203_ZERO_MEAN_RADIAL_MATRIX_MONODROMY_FLOQUET_CLASSIFICATION_AUDIT_2026-08-29.md`

Status: **SCOPE CORRECTION / THE M5-202--203 MATRIX ALGEBRA WAS WRITTEN FOR THE SYMMETRIC STRAIN PART, WHICH IS SUFFICIENT IN THE STANDARD SCALAR ENERGY BUT NOT FOR A NONSCALAR MATRIX METRIC / THE EXACT VORTICITY LOWER-ORDER OPERATOR USES THE FULL SCALED VELOCITY GRADIENT `G = Sigma + R`, INCLUDING ITS ANTISYMMETRIC ROTATION PART / REPLACING `Sigma` BY THE FULL TRACE-FREE GRADIENT LEAVES THE DETERMINANT COHOMOLOGY OBSTRUCTION AND THE MONODROMY/FLOQUET CLASSIFICATION EXACTLY INTACT, BUT CHANGES THE ANISOTROPIC COCYCLE THAT MUST BE TESTED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact vorticity-side lower-order matrix

For incompressible Navier--Stokes,

\[
\partial_t\omega
-\nu\Delta\omega
+(u\cdot\nabla)\omega
-(\omega\cdot\nabla)u
=0.
\]

The stretching term is

\[
(\omega\cdot\nabla)u
=(\nabla u)\omega.
\]

Thus the exact vector lower-order coefficient is the full velocity gradient

\[
\boxed{\mathcal G:=r^2\nabla B_T,}
\]

not only its symmetric part.

Decompose

\[
\boxed{\mathcal G=\Sigma+\mathcal R,}
\]

where

\[
\Sigma^T=\Sigma,
\qquad
\mathcal R^T=-\mathcal R.
\]

Incompressibility gives

\[
\boxed{\operatorname{tr}\mathcal G=\operatorname{tr}\Sigma=0.}
\]

---

## 2. Why the distinction is invisible for `H=I`

In the ordinary Euclidean energy,

\[
W^T\mathcal RW=0
\]

for every antisymmetric matrix `R`.

Hence

\[
W^T\mathcal GW
=W^T\Sigma W.
\]

This is why scalar energy estimates naturally speak only about strain.

However, for a non-scalar positive matrix metric `H`,

\[
W^TH\mathcal RW
\]

need not vanish.

Its symmetric contribution is governed by

\[
H\mathcal R-\mathcal RH,
\]

which is generally nonzero and symmetric.

Therefore any exact matrix symmetrizer must use the full `G`.

---

## 3. Correct matrix-weighted symmetric residual

Retain the cylinder transport

\[
T_\Phi=a\cdot D,
\qquad
\operatorname{div}_{cyl}a=-\Phi_r.
\]

Write the exact first-order vector operator schematically as

\[
\mathcal A W
=T_\Phi W-\mathcal GW.
\]

For a positive symmetric metric `H`, integration by parts gives

\[
2\langle HW,\mathcal AW\rangle
=
\int W^TK_H^{full}W,
\]

where

\[
\boxed{
K_H^{full}
=
-(a\cdot D)H
+
\Phi_rH
-
(H\mathcal G+\mathcal G^TH).
}
\]

Using

\[
\mathcal G=\Sigma+\mathcal R,
\]

this becomes

\[
\boxed{
K_H^{full}
=
-(a\cdot D)H
+
\Phi_rH
-
(H\Sigma+\Sigma H)
-
(H\mathcal R-\mathcal RH).
}
\]

The final commutator term is the piece omitted by the strain-only schematic form.

---

## 4. Correct exact symmetrizer equation

Exact skewness of the full first-order operator requires

\[
K_H^{full}=0.
\]

Thus

\[
\boxed{
(a\cdot D)H
=
\Phi_rH
-
H\mathcal G
-
\mathcal G^TH.
}
\]

Along a cylinder characteristic,

\[
\boxed{
H'
=
\Phi_rH
-
H\mathcal G
-
\mathcal G^TH.
}
\]

This is the exact matrix Lyapunov transport equation for the critical vorticity operator.

---

## 5. Determinant equation is unchanged

Multiply by `H^{-1}` and take trace:

\[
\frac d{ds}\log\det H
=
3\Phi_r
-
\operatorname{tr}\mathcal G
-
\operatorname{tr}\mathcal G^T.
\]

Since

\[
\operatorname{tr}\mathcal G=0,
\]

we obtain exactly

\[
\boxed{
\frac d{ds}\log\det H
=3\Phi_r.
}
\]

Therefore every determinant conclusion of M5-202 survives without modification:

\[
\boxed{
\langle\Phi_r\rangle_{orbit}=0
}
\]

is still necessary for a bounded periodic/recurrent exact symmetrizer.

The explicit polar counterexample from M5-194A remains valid.

---

## 6. Determinant-one equation with full gradient

Factor

\[
H=e^hG_H,
\qquad
\det G_H=1,
\]

with

\[
(a\cdot D)h=\Phi_r.
\]

Then

\[
\boxed{
(a\cdot D)G_H
=
-G_H\mathcal G
-
\mathcal G^TG_H.
}
\]

Along a characteristic,

\[
\boxed{
G_H'
=
-G_H\mathcal G
-
\mathcal G^TG_H.
}
\]

Thus the relevant cocycle is the full velocity-gradient deformation cocycle.

---

## 7. Correct fundamental matrix

Let

\[
\boxed{
U'=\mathcal G U,
\qquad
U(0)=I.
}
\]

Because

\[
\operatorname{tr}\mathcal G=0,
\]

Liouville's formula gives

\[
\boxed{\det U(s)=1.}
\]

The metric solution is

\[
\boxed{
G_H(s)=U(s)^{-T}G_0U(s)^{-1}.
}
\]

This formula is exact even when the antisymmetric rotation part does not commute with the strain.

---

## 8. Periodic monodromy classification is unchanged in form

For a periodic characteristic of period `P`, define

\[
M:=U(P)\in SL(3,\mathbb R).
\]

A periodic positive metric exists iff

\[
\boxed{
M^TG_0M=G_0
}
\]

for some `G_0>0`.

Hence exactly as in M5-203,

\[
\boxed{
M\text{ must be similar to an orthogonal matrix}.
}
\]

Therefore the hyperbolic / Jordan / elliptic Floquet classification remains correct.

What changes is **which monodromy matrix must be computed**: it is the full deformation-gradient monodromy, not the strain-only time-ordered exponential.

---

## 9. Antisymmetric rotation can materially change Floquet type

Although `R` contributes no instantaneous Euclidean energy production, it can rotate the strain eigendirections and alter the ordered product defining `M`.

In general,

\[
[\Sigma(s_1),\mathcal R(s_2)]\ne0.
\]

Therefore one may not replace

\[
\mathcal T\exp\int(\Sigma+\mathcal R)ds
\]

by a product of independent strain and rotation exponentials without an additional commutation hypothesis.

A strain-only hyperbolic snapshot sequence can in principle be modified by rapid frame rotation, while a seemingly balanced strain history can become nonnormal under noncommuting rotations.

Thus the exact NSE Floquet problem is genuinely a **full-gradient noncommutative cocycle** problem.

---

## 10. Corrected status of the M5-203 countermodel

The abstract piecewise strain cycle

\[
S_0\to -S_0
\]

with identity monodromy remains a valid countermodel showing that trace-free symmetric stretching can cancel over a cycle.

However, it should not be read as a model of the full NSE gradient cocycle unless the antisymmetric part is separately specified, for example `R=0` in the abstract system.

Therefore its role is only the logical statement

\[
\boxed{
\text{nonzero strain alone does not force hyperbolic monodromy}.
}
\]

The exact NSE realizability problem remains open.

---

## 11. Full-gradient determinant obstruction is stronger conceptually

Because the determinant equation survives the inclusion of all rotational terms, the main M5-202 obstruction is not an artifact of discarding vorticity rotation.

It follows from only

1. critical cylinder divergence;
2. incompressibility `tr G=0`;
3. bounded positive metric recurrence.

Thus

\[
\boxed{
(a\cdot D)\log\det H=3\Phi_r
}
\]

is a robust invariant of the exact full-gradient symmetrization problem.

---

## 12. Implication for the next NSE energy audit

The correct first-order matrix cancellation to insert into the vorticity equation is

\[
(a\cdot D)H
=
\Phi_rH-H\mathcal G-\mathcal G^TH.
\]

After this cancellation, the remaining symmetric terms come from

- viscous cylinder diffusion;
- homogeneity zeroth-order terms created by factoring `r^{-2}` vorticity;
- derivatives of the matrix metric generated when diffusion is integrated by parts;
- time dependence if the tail is dynamic;
- core/tail residual forcing.

Therefore the next audit must not claim that exact first-order skewness leaves a purely positive Laplacian. A spatially varying `H` creates diffusion commutators.

---

## 13. DSD verdict

### CORRECTED / PROVED

- the exact vorticity coefficient is the full scaled gradient `G=Sigma+R`;
- antisymmetric rotation is invisible only for scalar Euclidean energy, not for a matrix metric;
- exact full-gradient matrix residual derived;
- determinant equation remains `a·grad log det H=3 Phi_r`;
- the monodromy criterion remains `M^T G M=G` but `M` is now the full-gradient deformation monodromy;
- hyperbolic/Jordan/elliptic classification survives in form;
- M5-203 strain-only countermodel is retained only as an abstract logical countermodel, not an exact NSE realization.

### OPEN

- exact full-gradient monodromy of NSE-compatible critical tails;
- diffusion commutator balance in a nonconstant metric;
- elliptic full-gradient monodromy compatibility with NSE residual;
- nonlocal backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 14. Next target

Derive the degree-`-2` vorticity cylinder operator exactly and compute the `H`-weighted diffusion identity.

For a Cartesian component

\[
\omega=r^{-2}W(y,\theta),
\qquad y=-\log r,
\]

the Laplacian has a nontrivial radial first- and zeroth-order part.

The next calculation should keep those terms and show precisely which metric-gradient commutators survive after the full-gradient first-order skew cancellation.