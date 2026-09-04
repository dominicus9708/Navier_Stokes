# DSD M17-043 — Slanted alignment invariance forces the next-jet material collinearity condition

Date: 2026-09-04
Canonical ID: **M17-043**

Status: **INTERNAL SLANTED ALIGNMENT INVARIANCE / ON A REGULAR NONCONFORMAL SLANTED WINDING CORE, M17-025 REQUIRES `C_p=-(G_q-1)Q_0`, WHERE `Q_0=TF(nabla_h^2 q)` AND `C_p=TF[(p·grad_h)H_phi]`. BECAUSE `W_h=J grad_h q`, THE NODAL HORIZONTAL JACOBIAN LAW OF M17-010 IMPLIES THE EXACT HESSIAN MULTIPLIER `D_B Q_0=(kappa-3/2)Q_0`; THE ANISOTROPY TENSOR LINE IS THEREFORE MATERIALLY FIXED. DIFFERENTIATING THE ALIGNMENT IDENTITY GIVES `D_B C_p=-[D_B(G_q-1)+(kappa-3/2)(G_q-1)]Q_0`. CONSEQUENTLY THE MATERIAL DERIVATIVE OF THE THIRD-JET COMPENSATOR MUST ITSELF BE COLLINEAR WITH `Q_0`: `P_{Q_0}^perp(D_B C_p)=0`. THIS IS A NEW NEXT-JET COMPATIBILITY CONDITION. IT SHOWS THAT THE SLANTED ALIGNED MANIFOLD IS NOT CERTIFIED BY THE STATIC THIRD-JET RELATION ALONE; PERSISTENCE REQUIRES ITS PDE EVOLUTION TO REMAIN ON THE SAME ONE-DIMENSIONAL TRACELESS-TENSOR LINE. HOWEVER CODIMENSION/HIERARCHY ALONE IS NOT A CONTRADICTION: A TRUE INVARIANT MANIFOLD COULD SATISFY ALL SUCH CONDITIONS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Nodal Hessian and horizontal vorticity Jacobian

On the great-circle branch,

\[
W_h=J\nabla_hq
\]

with constant planar quarter-turn matrix `J`.

At a nodal point,

\[
\nabla_hq=0.
\]

Hence the horizontal vorticity Jacobian is

\[
\boxed{
G_h=JQ,
\qquad
Q:=\nabla_h^2q.
}
\]

M17-010 gives

\[
D_BG_h
=\left(\kappa-\frac32\right)G_h.
\]

Since `J` is constant,

\[
\boxed{
D_BQ
=\left(\kappa-\frac32\right)Q.
}
\]

Taking the trace-free part,

\[
\boxed{
D_BQ_0
=\left(\kappa-\frac32\right)Q_0,
\qquad
Q_0:=TF(Q).
}
\]

Thus the full signed anisotropy tensor changes by a scalar only.

---

## 2. Static slanted alignment from M17-025

For a nonconformal slanted core,

\[
Q_0\ne0.
\]

Define

\[
C_p
:=TF\left[(p\cdot\nabla_h)H_\phi\right].
\]

M17-025 gives

\[
\boxed{
C_p
+(G_q-1)Q_0
=0.
}
\]

Write

\[
\boxed{g:=G_q-1.}
\]

Then

\[
\boxed{C_p=-gQ_0.}
\]

---

## 3. Material derivative of the alignment identity

Differentiate along the material nodal filament:

\[
D_BC_p
=-(D_Bg)Q_0-gD_BQ_0.
\]

Use the Hessian multiplier from Section 1:

\[
D_BQ_0
=\left(\kappa-\frac32\right)Q_0.
\]

Therefore

\[
\boxed{
D_BC_p
=-\left[
D_Bg
+\left(\kappa-\frac32\right)g
\right]Q_0.
}
\]

Equivalently,

\[
\boxed{
D_BC_p
=-\left[
D_B(G_q-1)
+\left(\kappa-\frac32\right)(G_q-1)
\right]Q_0.
}
\]

---

## 4. Next-jet collinearity condition

The right-hand side of Section 3 lies entirely in

\[
\operatorname{span}\{Q_0\}
\]

inside the two-dimensional traceless symmetric matrix space.

Therefore a persistent regular slanted core must satisfy

\[
\boxed{
P_{Q_0}^{\perp}(D_BC_p)=0.
}
\]

Here

\[
P_{Q_0}^{\perp}X
:=X-\frac{X:Q_0}{|Q_0|^2}Q_0.
\]

This is the exact **Slanted Alignment Invariance Gate** condition.

---

## 5. Tensor direction of C_p is materially frozen

If

\[
g\ne0,
\]

then `C_p` is nonzero and parallel to `Q_0`.
Because the direction of `Q_0` is materially fixed,

\[
\boxed{
D_B\left(\frac{C_p}{|C_p|}\right)=0
}
\]

up to the fixed sign convention while `g` does not cross zero.

Thus the trace-free third-jet compensation tensor has a frozen normalized orientation, not merely an instantaneous alignment.

---

## 6. Relative compensation amplitude

Define

\[
\boxed{
\mu
:=\frac{C_p:Q_0}{|Q_0|^2}.
}
\]

The static law gives

\[
\boxed{
\mu=-g=1-G_q.
}
\]

Hence

\[
\boxed{
D_B\mu
=-D_BG_q.
}
\]

Also from Section 3,

\[
D_BC_p
=\left[
D_B\mu
+\left(\kappa-\frac32\right)\mu
\right]Q_0.
\]

Thus all allowed evolution of `C_p` is reduced to one scalar amplitude `mu` on a fixed tensor line.

---

## 7. What D_B C_p contains at PDE level

The compensator is

\[
C_p
=TF[p_\ell\partial_\ell H_\phi].
\]

Material differentiation contains

1. `D_Bp`, already fixed by M17-024 as `3lambda p`;
2. material derivatives of the spatial third jet `partial_l H_phi`;
3. commutators of `D_B` with spatial differentiation.

Through the Navier--Stokes velocity-gradient equation, these terms involve the next spatial derivative level of the viscous/pressure system.

Therefore

\[
P_{Q_0}^{\perp}(D_BC_p)=0
\]

is genuinely a **next-jet PDE compatibility condition**, not a restatement of the static matrix equality in lower-order variables.

No claim is made here that its perpendicular component is generically nonzero for actual solutions; that requires the explicit higher-jet evolution audit.

---

## 8. Vertical limit

If

\[
p=0,
\]

then

\[
C_p=0.
\]

For a nonconformal core M17-025 gives

\[
g=0
\]

so

\[
G_q=1.
\]

The next-jet alignment condition is then vacuous at the exact vertical point, consistent with M17-015.

Thus the new hierarchy is specific to the genuinely slanted compensation branch.

---

## 9. Crossing G_q=1

Suppose along a slanted branch

\[
g=G_q-1
\]

crosses zero.
Then

\[
C_p=0
\]

at the crossing even though

\[
Q_0\ne0,
\qquad
p\ne0.
\]

The derivative law becomes

\[
\boxed{
D_BC_p=-(D_Bg)Q_0
}
\]

at the crossing.

Therefore the compensator can pass through zero regularly only with its first material derivative still exactly aligned with `Q_0`.
The forbidden perpendicular component remains zero through the crossing.

---

## 10. Potential hierarchy

If one repeatedly differentiates the exact identity while the regular slanted branch persists, every material derivative satisfies a tensor-line constraint of the schematic form

\[
\boxed{
P_{Q_0}^{\perp}(D_B^mC_p)=0
\quad(m\ge0),
}
\]

after lower-order scalar multiplier contributions are removed.

This suggests an aligned higher-jet hierarchy.

However, the existence of such a hierarchy is **not** by itself a contradiction. Analytic invariant manifolds can carry infinitely many derivative identities generated by one underlying symmetry/reduction.

---

## 11. DSD interpretation

The static descriptor

\[
C_p^\perp=0
\]

only tests one time slice.
The correct dynamic descriptor is whether the material vector field of the PDE is tangent to that alignment manifold:

\[
\boxed{
P_{Q_0}^{\perp}(D_BC_p)=0.
}
\]

Thus SAIG converts a geometric codimension statement into an invariance/tangency question.

---

## 12. DSD audit

### Audit A — declaring codimension a contradiction
Rejected.

### Audit B — assuming Q_0 direction is merely approximately fixed
Rejected; it obeys an exact scalar material multiplier.

### Audit C — claiming D_B C_p is automatically aligned from lower-order data alone
Not claimed. Alignment is a necessary condition whose PDE verification lies at the next jet level.

### Audit D — counting every differentiated identity as independent evidence
Rejected. They may be generated by one invariant manifold.

### Audit E — proof status
The slanted branch is sharpened but not closed.

---

## 13. Updated slanted Rank-1 frontier

The regular nonconformal slanted branch must satisfy

\[
\boxed{
\begin{aligned}
C_p&=-(G_q-1)Q_0,\\
D_BQ_0&=(\kappa-3/2)Q_0,\\
P_{Q_0}^{\perp}(D_BC_p)&=0,\\
D_B\widehat p&=0,\\
D_Bp&=3\lambda p.
\end{aligned}
}
\]

Thus only one scalar compensation amplitude remains free at the first two tensor levels.

---

## 14. Next target

To decide whether the alignment manifold is truly invariant, the next step is to compute the perpendicular component of `D_B C_p` directly from the Navier--Stokes velocity-gradient/pressure-Hessian evolution, rather than from differentiating the already-assumed alignment identity.

If the direct PDE formula contains a generically nonzero perpendicular forcing not cancelled by another retained structure, the slanted branch would be forced into a new symmetry/reduction or finite-jet degeneration.

This is the **Direct SAIG Forcing Gate (DSAIG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
