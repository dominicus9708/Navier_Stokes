# DSD M17-015 — A vertical non-axisymmetric regular core forces G_q = 1 and axial stationarity of the repeated-plane strain

Date: 2026-09-03
Canonical ID: **M17-015**

Status: **INTERNAL NODAL SHAPE–VELOCITY COMPATIBILITY / ON A VERTICAL REGULAR WINDING FILAMENT, `grad_h q=0` AND THE M17-010 CORE STRAIN ISOTROPY GIVES `nabla_h^2 phi=lambda I`. THE M17-004 IDENTITY `q=U_3-partial_3 phi` WITH `U_3=G(q,x_3,theta)` IMPLIES AT THE FILAMENT `(G_q-1)nabla_h^2q=(partial_3 lambda)I`. IF THE NODAL CRITICAL-POINT HESSIAN IS NOT A SCALAR MULTIPLE OF THE IDENTITY — INCLUDING EVERY NEGATIVE-INDEX CORE AND EVERY ANISOTROPIC POSITIVE-INDEX CORE — MATRIX INDEPENDENCE FORCES `G_q=1` AND `partial_3 lambda=0`. THUS A VERTICAL GENUINELY NON-AXISYMMETRIC REGULAR CORE HAS A FIXED UNIT q-SENSITIVITY IN THE VERTICAL VELOCITY LAW AND A LOCALLY AXIALLY STATIONARY REPEATED-PLANE STRAIN. THIS IS A NEW EXACT COMPATIBILITY CONDITION, NOT A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vertical material nodal filament

Use the fixed great-circle frame with

\[
n=e_3,
\qquad
W_h=J\nabla_hq.
\]

Consider a regular nodal filament which is locally vertical in this frame.
After centering horizontal coordinates on it,

\[
\boxed{
\nabla_hq(0,0,x_3,\theta)=0
}
\]

along a local filament segment.

Define its horizontal critical-point Hessian

\[
\boxed{
Q:=\nabla_h^2q|_\Gamma.
}
\]

Regularity means

\[
\det Q\neq0.
\]

Since the horizontal nodal point is fixed along the local vertical filament,

\[
\partial_3(\nabla_hq)|_\Gamma=0.
\]

Equivalently,

\[
q_{13}=q_{23}=0
\]

on the filament.

---

## 2. M17-010 strain isotropy at the core

At a regular winding zero, M17-010 gives

\[
\operatorname{spec}\Sigma
=\{\lambda,\lambda,-2\lambda\}
\]

in the great-circle frame.
Because `W=0`, the antisymmetric part of `nabla U` also vanishes at the nodal core.
Therefore

\[
\boxed{
\nabla U|_\Gamma
=\operatorname{diag}(\lambda,\lambda,-2\lambda).
}
\]

Since

\[
U_h=\nabla_h\phi,
\]

we obtain

\[
\boxed{
\nabla_h^2\phi|_\Gamma
=\lambda I_2.
}
\]

Differentiate this identity along the vertical filament:

\[
\boxed{
\partial_3\nabla_h^2\phi|_\Gamma
=(\partial_3\lambda)I_2.
}
\]

---

## 3. Differentiate the q reconstruction law

M17-004 gives

\[
\boxed{
q=U_3-\partial_3\phi
}
\]

and

\[
\boxed{
U_3=G(q,x_3,\theta).
}
\]

Hence

\[
\partial_3\phi
=G(q,x_3,\theta)-q.
\]

Take two horizontal derivatives:

\[
\nabla_h^2(\partial_3\phi)
=
(G_q-1)\nabla_h^2q
+G_{qq}\nabla_hq\otimes\nabla_hq.
\]

At the nodal filament,

\[
\nabla_hq=0,
\]

so

\[
\boxed{
\partial_3\nabla_h^2\phi
=(G_q-1)Q.
}
\]

Combine this with the differentiated strain-isotropy identity:

\[
\boxed{
(G_q-1)Q
=(\partial_3\lambda)I_2.
}
\]

This is the exact vertical-core compatibility matrix law.

---

## 4. Non-scalar nodal Hessian forces G_q = 1

Suppose

\[
Q\notin\{cI_2:c\in\mathbb R\}.
\]

Then a scalar multiple of `Q` can equal a scalar multiple of `I_2` only if both coefficients vanish.
Therefore

\[
\boxed{
G_q=1
}
\]

and

\[
\boxed{
\partial_3\lambda=0
}
\]

on the vertical nodal filament.

This applies to both genuinely non-axisymmetric first-order core classes from M17-014:

### Negative-index core

If

\[
\det Q<0,
\]

then `Q` is indefinite and can never be a scalar multiple of `I_2`.
Thus

\[
\boxed{
G_q=1,
\qquad
\lambda_3=0.
}
\]

### Anisotropic positive-index core

If

\[
\det Q>0
\]

but its two singular/eigenvalue magnitudes are unequal, then again

\[
Q\neq cI_2,
\]

so the same pair is forced.

---

## 5. Meaning inside the reduced label flow

M17-013 defines

\[
K(q,x_3,\theta)
:=G(q,x_3,\theta)+\frac12x_3
\]

as the vertical component of the reduced `(q,x_3)` material label velocity.
Therefore

\[
K_q=G_q.
\]

On every vertical genuinely non-axisymmetric regular core,

\[
\boxed{
K_q=1.
}
\]

Thus a small perturbation of the q-label changes the vertical label velocity with an exact unit coefficient at the core.

The reduced label Jacobian matrix has the local form

\[
DV_L
=
\begin{pmatrix}
H_q&H_3\\
1&G_3+\frac12
\end{pmatrix}
\]

at the non-axisymmetric vertical core, with trace

\[
\operatorname{tr}DV_L=\kappa
\]

by M17-013.

This is an additional constraint on any recurrent area-hysteresis model.

---

## 6. Axial stationarity of lambda

The condition

\[
\boxed{\lambda_3=0}
\]

means the repeated horizontal strain eigenvalue cannot acquire first-order variation along the vertical filament direction at such a core.

This is stronger than M17-010 for a vertical-like filament, where recurrence alone did not force the time mean of `lambda` to vanish.

It does **not** say

\[
\lambda=0.
\]

It says only that the spatial axial derivative at the core vanishes.
Time variation and transverse variation remain possible.

---

## 7. Conformal positive-index exception

If

\[
Q=cI_2,
\qquad c\neq0,
\]

then

\[
(G_q-1)c
=\lambda_3
\]

is scalar and does not force either factor to vanish.

This is precisely the local positive-index conformal class identified in M17-014 as compatible with the axisymmetric no-swirl firewall.

Thus the matrix law automatically separates

\[
\boxed{
\text{conformal positive core}
\quad\text{from}\quad
\text{genuinely non-axisymmetric vertical core}.
}
\]

---

## 8. DSD analysis

The scalar label dynamics of M17-013 discarded horizontal shape.
M17-015 restores that missing channel through a compatibility map:

\[
\boxed{
Q
\longrightarrow
(G_q-1)Q=\lambda_3I.
}
\]

For scalar `Q`, the relation carries one scalar degree of freedom.
For non-scalar `Q`, independent matrix components overdetermine it and force both scalar coefficients to zero.

This is a clean example of a DSD structural distinction that is invisible in scalar averaging.

---

## 9. DSD audit

### Audit A — confusing vertical with slanted filaments
Avoided.
The derivation uses a local vertical filament, so that horizontal nodal coordinates remain fixed while differentiating in `x_3`.
Slanted filaments require a tangent-derivative version and remain separate.

### Audit B — claiming G_q=1 globally
Rejected.
The equality is obtained at the vertical genuinely non-axisymmetric nodal core.

### Audit C — claiming lambda=0
Rejected.
Only `partial_3 lambda=0` is forced here.

### Audit D — falsely excluding the axisymmetric firewall
Avoided.
The conformal positive core `Q=cI` does not force `G_q=1` and remains open to the no-swirl model.

### Audit E — proof status
No contradiction has been obtained.

---

## 10. Updated vertical non-axisymmetric branch

For a uniformly regular recurrent vertical filament,

\[
\boxed{
G_{nonaxis,vertical}^{core}
\Longrightarrow
\begin{cases}
G_q=1,\\
\lambda_3=0,\\
D_B\widehat C=0,\\
\operatorname{div}V_L=\kappa.
\end{cases}
}
\]

Thus the remaining vertical non-axisymmetric survivor must sustain M17-013/M5-685 label-area hysteresis subject to these additional exact core constraints.

---

## 11. Next target

Two complementary tasks remain:

1. **vertical conformal core:** detect higher-order angular non-axisymmetry beyond the isotropic Hessian;
2. **slanted core:** derive the tangent-covariant replacement of `(G_q-1)Q=lambda_3I` and combine it with the M17-010 mean `⟨lambda⟩=0` constraint.

For the first task, the natural object is the horizontal rotation defect

\[
\mathcal L q
=(x_1\partial_2-x_2\partial_1)q.
\]

Because `Delta q=F(q,x_3,theta)`, this defect obeys the same scalar Schrödinger equation `Delta(mathcal L q)=kappa(mathcal L q)`.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
