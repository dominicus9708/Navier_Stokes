# DSD M17-025 — A slanted non-axisymmetric core requires exact tensor alignment to compensate G_q departure from one

Date: 2026-09-03
Canonical ID: **M17-025**

Status: **INTERNAL SLANTED CORE COMPATIBILITY / PARAMETRIZING A NONHORIZONTAL REGULAR FILAMENT BY `x_3` GIVES THE TANGENT DERIVATIVE `D_s = partial_3 + p dot grad_h`, WITH `p=-Q^{-1}grad_h q_3`. CORE STRAIN ISOTROPY GIVES `H_phi=lambda I` ON THE FILAMENT, WHILE THE RECONSTRUCTION LAW GIVES `partial_3 H_phi=(G_q-1)Q`. DIFFERENTIATING `H_phi=lambda I` ALONG THE SLANTED FILAMENT YIELDS THE EXACT MATRIX LAW `(p dot grad_h)H_phi+(G_q-1)Q=(D_s lambda)I`. ITS TRACELESS PART REQUIRES `C_p:=TF[(p dot grad_h)H_phi]=-(G_q-1)Q_TF`. THUS FOR A NONCONFORMAL CORE, DEPARTURE `G_q != 1` IS POSSIBLE ONLY IF THE SLANT-DIRECTION STRAIN-HESSIAN GRADIENT IS EXACTLY COLLINEAR WITH THE FIXED NODAL ANISOTROPY TENSOR. A MISALIGNED TENSOR IS LOCALLY INCOMPATIBLE WITH A REGULAR SLANTED CE-H CORE. THE VERTICAL M17-015 LAW IS THE SPECIAL CASE `p=0`, WHERE THE COMPENSATOR VANISHES AND `G_q=1` IS FORCED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Slanted filament chart

Use M17-024 and assume

\[
\tau_3\ne0.
\]

Write the slope

\[
\boxed{
p=\frac{\tau_h}{\tau_3}.}
\]

Using `x_3` as a local filament parameter, the tangent derivative is

\[
\boxed{
D_s
:=\partial_3+p\cdot\nabla_h.
}
\]

Along the nodal filament,

\[
\nabla_hq=0.
\]

Differentiating this condition along the filament gives

\[
D_s(\nabla_hq)=0.
\]

With

\[
Q:=\nabla_h^2q,
\qquad
c:=\nabla_hq_3,
\]

we recover

\[
\boxed{
c+Qp=0,}
\]

or

\[
\boxed{p=-Q^{-1}c.}
\]

---

## 2. Core horizontal strain Hessian

At every regular winding zero, M17-010 gives

\[
\nabla U
=\operatorname{diag}(\lambda,\lambda,-2\lambda)
\]

in the fixed great-circle frame.
Since

\[
U_h=\nabla_h\phi,
\]

the horizontal Hessian is

\[
\boxed{
H_\phi
:=\nabla_h^2\phi
=\lambda I_2
}
\]

at every point of the filament.

Because this identity holds **along** the slanted filament,

\[
\boxed{
D_sH_\phi
=(D_s\lambda)I_2.
}
\]

---

## 3. Vertical derivative from the reconstruction law

M17-004 gives

\[
\partial_3\phi
=G(q,x_3,\theta)-q.
\]

Take two horizontal derivatives:

\[
\partial_3H_\phi
=(G_q-1)Q
+G_{qq}\nabla_hq\otimes\nabla_hq.
\]

At the nodal core,

\[
\nabla_hq=0,
\]

so

\[
\boxed{
\partial_3H_\phi
=(G_q-1)Q.
}
\]

---

## 4. Tangent-covariant compatibility matrix

Expand the tangent derivative:

\[
D_sH_\phi
=\partial_3H_\phi
+(p\cdot\nabla_h)H_\phi.
\]

Insert the reconstruction identity and core isotropy derivative:

\[
(G_q-1)Q
+(p\cdot\nabla_h)H_\phi
=(D_s\lambda)I_2.
\]

Therefore the exact slanted-core matrix law is

\[
\boxed{
(p\cdot\nabla_h)H_\phi
+(G_q-1)Q
=(D_s\lambda)I_2.
}
\]

This is the tangent-covariant replacement of M17-015.

---

## 5. Trace-free alignment law

For a symmetric `2x2` matrix define

\[
\operatorname{TF}A
:=A-\frac12(\operatorname{tr}A)I_2.
\]

Set

\[
\boxed{
Q_0:=\operatorname{TF}Q,
}
\]

and

\[
\boxed{
C_p
:=\operatorname{TF}\left[(p\cdot\nabla_h)H_\phi\right].
}
\]

Taking the trace-free part of the compatibility matrix gives

\[
\boxed{
C_p
+(G_q-1)Q_0
=0.
}
\]

Thus

\[
\boxed{
C_p=-(G_q-1)Q_0.
}
\]

---

## 6. Nonconformal core: exact tensor collinearity

Suppose

\[
Q_0\ne0.
\]

This includes both

1. anisotropic positive-index cores;
2. negative-index cores.

Then the compensation tensor `C_p` must lie in the one-dimensional span of `Q_0` inside the two-dimensional space of traceless symmetric `2x2` matrices:

\[
\boxed{
C_p\parallel Q_0.
}
\]

The coefficient is fixed:

\[
\boxed{
G_q-1
=-\frac{C_p:Q_0}{|Q_0|^2}.
}
\]

Moreover the Frobenius-orthogonal component must vanish:

\[
\boxed{
C_p^\perp
:=C_p
-\frac{C_p:Q_0}{|Q_0|^2}Q_0
=0.
}
\]

This is a genuine local compatibility restriction.

---

## 7. Generic misalignment is excluded

The traceless symmetric matrix space in two dimensions has dimension two.
The nodal anisotropy `Q_0` selects one line in this space.

A generic transverse strain-Hessian gradient `C_p` has two independent components and need not lie on that line.

Therefore

\[
\boxed{
C_p^\perp\ne0
\Longrightarrow
\text{no regular slanted CE-H core with the assumed data}.
}
\]

The slanted branch survives only on the aligned submanifold

\[
\boxed{C_p^\perp=0.}
\]

This is a stronger classification than the scalar recurrence constraints alone.

---

## 8. Vertical limit recovers M17-015

For a vertical filament,

\[
p=0.
\]

Then

\[
C_p=0.
\]

The trace-free law becomes

\[
(G_q-1)Q_0=0.
\]

For a nonconformal core `Q_0 != 0`,

\[
\boxed{G_q=1.}
\]

The trace part simultaneously recovers

\[
\partial_3\lambda=0.
\]

Thus M17-015 is exactly the zero-slope limit of the tangent-covariant law.

---

## 9. A slanted compensation branch

If

\[
G_q\ne1
\]

at a nonconformal slanted core, then necessarily

\[
\boxed{
C_p\ne0.
}
\]

Hence departure from the vertical unit-sensitivity condition requires a nonzero trace-free horizontal strain gradient in precisely the slant direction.

Symbolically,

\[
\boxed{
G_q-1
\longleftrightarrow
-\frac{C_p:Q_0}{|Q_0|^2}.
}
\]

This identifies the previously missing escape channel in M17-015.

---

## 10. Frozen material orientation makes the alignment persistent

M17-014 gives the normalized nodal shape as a material invariant.
M17-024 gives the slant azimuth as a material invariant.
Therefore the normalized directions of

\[
Q_0
\]

and

\[
p
\]

are frozen along the marked regular filament.

The survivor must repeatedly regenerate a strain-Hessian gradient whose trace-free projection remains aligned with this fixed material anisotropy direction:

\[
\boxed{
C_p^\perp=0
\quad\text{for all retained regular times}.
}
\]

This converts a pointwise compatibility into a persistent tensor-alignment requirement on a recurrent branch.

---

## 11. Trace equation

Taking the trace of the full matrix law gives

\[
\boxed{
\operatorname{tr}[(p\cdot\nabla_h)H_\phi]
+(G_q-1)\operatorname{tr}Q
=2D_s\lambda.
}
\]

This determines the tangent derivative of the repeated-plane strain once the scalar trace and compensation coefficient are known.

It does not force

\[
D_s\lambda=0
\]

on a slanted core.
That vertical conclusion was special to `p=0` plus the nonconformal matrix independence.

---

## 12. DSD interpretation

### 12.1 Extra descriptor exposed by slant
The vertical calculation did not need transverse derivatives of the strain Hessian.
Slant activates precisely that previously invisible descriptor.

### 12.2 Scalar escape requires tensor payment
The scalar freedom `G_q-1` is not free: it must be paid for by an aligned trace-free third spatial derivative of the velocity potential.

### 12.3 Generic versus retained structure
Most arbitrary slanted nonconformal jets fail the alignment condition.
The remaining hard branch is a lower-dimensional aligned tensor family.

---

## 13. DSD audit

### Audit A — extending G_q=1 from vertical to slanted cores
Rejected.
The extra tensor `C_p` can compensate `G_q-1`.

### Audit B — claiming any C_p can compensate
Rejected.
Only the component parallel to `Q_0` is allowed; the orthogonal component must vanish exactly.

### Audit C — treating alignment codimension as a contradiction
Rejected.
Navier-Stokes dynamics may preserve a constrained invariant manifold.
Codimension alone is not exclusion.

### Audit D — assuming D_s lambda=0
Rejected.
The trace equation leaves tangent variation of `lambda` possible.

### Audit E — proof status
Global regularity remains unproved.

---

## 14. Updated slanted-core branch

For a regular nonconformal slanted filament,

\[
\boxed{
\begin{aligned}
D_B\widehat p&=0,\\
D_B\widehat C&=0,\\
C_p^\perp&=0,\\
G_q-1&=-\frac{C_p:Q_0}{|Q_0|^2},\\
\langle\lambda\rangle&=0
\quad\text{under uniform recurrent slant}.
\end{aligned}
}
\]

The branch is therefore reduced to a rigid normalized core geometry with one aligned scalar compensation amplitude.

---

## 15. Next target — evolution of the alignment defect

Define the forbidden misalignment descriptor

\[
\boxed{
\mathcal M_p:=C_p^\perp.
}
\]

The regular slanted branch requires

\[
\mathcal M_p=0.
\]

The next useful calculation is to differentiate this condition materially and determine whether the CE-H equations preserve the alignment manifold automatically or impose a new higher-jet compatibility condition.

This is the **Slanted Alignment Invariance Gate (SAIG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
