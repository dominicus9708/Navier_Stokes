# DSD M17-013 — Great-circle branch has a closed label-plane flow whose divergence is exactly kappa

Date: 2026-09-03
Canonical ID: **M17-013**

Status: **INTERNAL NON-AXISYMMETRIC HYSTERESIS REDUCTION / THE M17-004 SEMILINEAR GREAT-CIRCLE SYSTEM IMPLIES AN EXACT CLOSED MATERIAL DYNAMICS FOR THE PAIR `(q,x_3)`. WRITING `U_3=G(q,x_3,theta)` AND `Delta q=F(q,x_3,theta)`, ONE GETS `D_B q=H(q,x_3,theta)` WITH `H_q=kappa-G_3-1/2`, WHILE `D_B x_3=G+x_3/2`. CONSEQUENTLY THE TWO-DIMENSIONAL LABEL-FLOW VECTOR FIELD `(H,G+x_3/2)` HAS DIVERGENCE EXACTLY `kappa=F_q`. ITS JACOBIAN DETERMINANT THEREFORE OBEYS `J'=kappa J`, IDENTICAL TO THE M5 CURRENT-FLUX AMPLIFICATION LAW `a'=kappa a`. THE M5-685 KAPPA-ZERO HYSTERESIS IS THUS AN AREA-JACOBIAN HYSTERESIS OF THE REDUCED LABEL FLOW. THIS SCALAR/LABEL REDUCTION DOES NOT DISTINGUISH AXISYMMETRIC FROM GENUINELY NON-AXISYMMETRIC GEOMETRY, SO HYSTERESIS ALONE CANNOT CLOSE THE RANK-ONE BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Semilinear great-circle input

Use the canonical M17-004 system, originally written provisionally as M16-027.
Choose the fixed great-circle frame

\[
W=(W_1,W_2,0),
\qquad
W_h=J\nabla_h q,
\]

with

\[
U_h=\nabla_h\phi.
\]

On a regular connected branch,

\[
\boxed{
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q(q,x_3,\theta),
}
\]

and the strain-eigenline condition gives

\[
\boxed{
U_3=G(q,x_3,\theta).
}
\]

Here explicit `theta` dependence is restored because the recurrent similarity flow is time dependent.

Set

\[
B=U+\frac12 y,
\qquad
D_B=\partial_\theta+B\cdot\nabla.
\]

---

## 2. Gradient transport for q

Let

\[
p:=\nabla_h q.
\]

Since

\[
W_h=Jp
\]

and CE-H gives

\[
D_BW=\gamma W,
\qquad
\gamma=\sigma+\kappa-1,
\]

we have

\[
D_B(Jp)=\gamma Jp.
\]

For a scalar,

\[
D_B(\partial_a q)
=\partial_a(D_Bq)-(\partial_a B_j)\partial_jq,
\qquad a=1,2.
\]

Therefore

\[
\nabla_h(D_Bq)
-(\nabla_hB_h)^Tp
-q_3\nabla_hB_3
=\gamma p.
\]

---

## 3. Use the common q-level geometry

Because

\[
B_h=\nabla_h\phi+\frac12y_h,
\]

we have

\[
\nabla_hB_h=\nabla_h^2\phi+\frac12I_2.
\]

M17-004 gives

\[
(\nabla_h^2\phi)(Jp)=\sigma(Jp).
\]

Since the horizontal Hessian is symmetric, the orthogonal direction `p` is its other eigenvector.
Let its eigenvalue be `tau`.
Then

\[
\tau+\sigma=\Delta_h\phi.
\]

Incompressibility gives

\[
\Delta_h\phi+\partial_3U_3=0.
\]

With

\[
U_3=G(q,x_3,\theta),
\]

its full spatial derivative is

\[
\partial_3U_3=G_q q_3+G_3,
\]

where `G_3` means the partial derivative at fixed `q`.
Hence

\[
\boxed{
\tau=-G_qq_3-G_3-\sigma.
}
\]

Also

\[
B_3=G(q,x_3,\theta)+\frac12x_3
\]

and

\[
\nabla_hB_3=G_qp.
\]

Substitute into the q-gradient transport law:

\[
\nabla_h(D_Bq)
=
\left[
\gamma+\tau+\frac12+q_3G_q
\right]p.
\]

Using

\[
\gamma=\sigma+\kappa-1
\]

causes the `sigma`, `G_qq_3`, and `q_3G_q` terms to cancel exactly:

\[
\boxed{
\nabla_h(D_Bq)
=
\left(\kappa-G_3-\frac12\right)\nabla_hq.
}
\]

---

## 4. Closed material law for q

On every regular connected region where `nabla_h q != 0`, the preceding relation means `D_Bq` is constant on connected horizontal q-level curves.
Thus there is a local scalar function

\[
\boxed{
D_Bq=H(q,x_3,\theta)
}
\]

with

\[
\boxed{
H_q
=
\kappa-G_3-\frac12.
}
\]

By analytic continuation this is the natural scalar law to use up to regular nodal limits.

The vertical coordinate simultaneously obeys

\[
\boxed{
D_Bx_3
=B_3
=G(q,x_3,\theta)+\frac12x_3.
}
\]

Therefore the material trajectory projects to the closed nonautonomous two-dimensional system

\[
\boxed{
\begin{aligned}
q'&=H(q,x_3,\theta),\\
x_3'&=K(q,x_3,\theta),
\end{aligned}
}
\]

where

\[
\boxed{
K:=G+\frac12x_3.
}
\]

No horizontal position variable appears in this reduced label dynamics.

---

## 5. Exact divergence identity

Differentiate the two reduced components at fixed label coordinates:

\[
H_q=\kappa-G_3-\frac12,
\]

and

\[
K_3=G_3+\frac12.
\]

Hence

\[
\boxed{
\partial_qH+\partial_3K
=\kappa.
}
\]

Equivalently, for the reduced label velocity

\[
V_L:=(H,K),
\]

we have

\[
\boxed{
\operatorname{div}_{(q,x_3)}V_L
=\kappa.
}
\]

Thus `kappa` is not merely an auxiliary CE-H multiplier in the great-circle branch.
It is exactly the instantaneous area-expansion rate of the material `(q,x_3)` label flow.

---

## 6. Label-flow Jacobian equals the M5 amplification factor

Let

\[
\Phi_{\theta_0}^{\theta}:(q_0,z_0)\mapsto(q(\theta),x_3(\theta))
\]

be the reduced label-flow map and let

\[
J_L(\theta)
:=
\det D\Phi_{\theta_0}^{\theta}.
\]

Liouville's formula gives

\[
\frac d{d\theta}\log J_L
=
\operatorname{div}V_L
=
\kappa.
\]

Therefore

\[
\boxed{
J_L(\theta)
=
J_L(\theta_0)
\exp\left(
\int_{\theta_0}^{\theta}\kappa(\tau)d\tau
\right).
}
\]

M5-685 defines the material current-flux amplification factor

\[
a(\theta)
:=
\exp\left(
\int_{\theta_0}^{\theta}\kappa(\tau)d\tau
\right).
\]

Hence, after normalizing the initial Jacobian,

\[
\boxed{
a=J_L.}
\]

This is an exact geometric identification on the great-circle branch.

---

## 7. Kappa-zero crossings are label-area extrema

Since

\[
a'=\kappa a,
\]

at a zero crossing

\[
\kappa=0
\]

we have

\[
a'=0.
\]

Writing

\[
h=D_B\kappa,
\]

we also have

\[
a''=(h+\kappa^2)a,
\]

and hence at the crossing

\[
\boxed{
a''=ha.}
\]

Because `a=J_L`, this becomes

\[
\boxed{
J_L'=0,
\qquad
J_L''=hJ_L
\qquad(\kappa=0).
}
\]

Thus

- `h<0`: the reduced material label area is at a local maximum;
- `h>0`: it is at a local minimum.

The M5-685 condition that downward crossings are flux-heavier than upward crossings is therefore exactly a **label-area hysteresis**.

---

## 8. Regular zero root representation

Suppose a regular zero of `kappa=F_q` can locally be written as

\[
q=q_*(x_3,\theta),
\]

with

\[
F_q(q_*,x_3,\theta)=0,
\qquad
F_{qq}\neq0.
\]

Implicit differentiation gives

\[
q_{*,\theta}
=-\frac{F_{q\theta}}{F_{qq}},
\qquad
q_{*,3}
=-\frac{F_{q3}}{F_{qq}}.
\]

Along a material trajectory,

\[
h=D_B(F_q)
=F_{q\theta}+F_{qq}D_Bq+F_{q3}D_Bx_3.
\]

Therefore at the regular zero root,

\[
\boxed{
h
=F_{qq}
\left[
H-q_{*,\theta}-Kq_{*,3}
\right].
}
\]

Define the relative root-crossing velocity

\[
V_{rel}
:=
H-q_{*,\theta}-Kq_{*,3}.
\]

Then

\[
\boxed{h=F_{qq}V_{rel}.}
\]

So the required hysteresis can be generated only through the product of

1. the curvature `F_qq` of the semilinear level law;
2. material motion relative to the moving zero-root curve.

This is a considerably narrower constitutive description than an arbitrary scalar oscillator.

---

## 9. DSD analysis

### 9.1 Dimensional reduction of the descriptor
The full three-dimensional CE-H evolution projects to a two-dimensional label dynamics for `(q,x_3)`.
The horizontal geometry remains in the reconstruction of q-level curves, but the scalar amplification channel is completely described by the label flow.

### 9.2 Kappa acquires a structural meaning
In this branch,

\[
\kappa
=
\operatorname{div}V_L.
\]

Thus positive and negative `kappa` are respectively label-area expansion and contraction.
The M17-012 positive sheath / negative payer pair becomes a recurrent expansion/contraction redistribution in label space.

### 9.3 Hysteresis is not intrinsically non-axisymmetric
The reduced equations use `F`, `G`, and `H`, but no horizontal contour-shape invariant appears in

\[
\operatorname{div}V_L=\kappa.
\]

Therefore the same scalar hysteresis mechanism can occur in an axisymmetric/no-swirl-compatible reconstruction or in a genuinely non-axisymmetric reconstruction.

This prevents the scalar hysteresis condition alone from serving as the final non-axisymmetric contradiction.

---

## 10. DSD audit

### Audit A — treating h as arbitrary
Closed.
At a regular zero root,

\[
h=F_{qq}V_{rel}.
\]

### Audit B — confusing current amplification with an abstract weight
Closed on the great-circle branch.
The amplification factor is the Jacobian determinant of the reduced material label flow.

### Audit C — claiming hysteresis itself is contradictory
Rejected.
A bounded/recurrent two-dimensional flow can contain local expansion and contraction regions and recurrent area-Jacobian hysteresis.

### Audit D — claiming hysteresis distinguishes axisymmetry
Rejected.
The reduced scalar law contains no horizontal nodal-shape discriminator.
A separate geometric invariant is required.

### Audit E — proof status
No global contradiction is obtained.
Global regularity remains unproved.

---

## 11. Updated non-axisymmetric target

The old target

\[
H_{CE-H}^{nonaxis}
\]

must now be split into

\[
\boxed{
H_{CE-H}
+
A_{nodal},
}
\]

where

- `H_CE-H` is the reduced label-area hysteresis described above;
- `A_nodal` is a genuinely horizontal geometric discriminator capable of distinguishing the axisymmetric firewall from a non-axisymmetric regular nodal core.

The natural next candidate is the normalized nodal-Jacobian shape inherited from the M17-010 multiplier law.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
