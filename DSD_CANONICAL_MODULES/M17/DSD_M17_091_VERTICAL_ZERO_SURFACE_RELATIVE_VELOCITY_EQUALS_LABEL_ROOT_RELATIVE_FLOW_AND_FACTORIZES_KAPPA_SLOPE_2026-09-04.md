# DSD M17-091 — Vertical zero-surface relative velocity equals label-root relative flow divided by root-normal slope

Date: 2026-09-04
Canonical ID: **M17-091**

Status: **INTERNAL LABEL/SPATIAL ZERO-CROSSING DESCRIPTOR EQUIVALENCE / M17-013 REPRESENTS A REGULAR KAPPA-ZERO AS A SEMILINEAR ROOT `F_q(q_*(x_3,theta),x_3,theta)=0` AND DEFINES THE LABEL-PLANE RELATIVE CROSSING VELOCITY `V_rel^label=H-q_{*,theta}-K q_{*,3}`, WITH `h=F_qq V_rel^label`. M17-090 INDEPENDENTLY REPRESENTS THE SAME VERTICAL ZERO SET AS A SPATIAL SURFACE `x_3=z_0(theta)` AND FINDS `h=(B_3-v_0)kappa_3`. AT THE VERTICAL CORE, `B_3=K`, `grad_h q=0`, AND DIFFERENTIATION OF THE ROOT EQUATION GIVES `kappa_3=F_qq(q_3-q_{*,3})`. DIFFERENTIATION OF THE ACTUAL CROSSING CONDITION `q(z_0,theta)=q_*(z_0,theta)` GIVES `B_3-v_0=V_rel^label/(q_3-q_{*,3})`. THUS THE TWO CROSSING DESCRIPTORS ARE EXACTLY THE SAME GEOMETRY IN LABEL AND SPATIAL COORDINATES. COMBINED WITH M17-090, `O_loc,333=-(1/5)|Q|^2F_qq(q_3-q_{*,3})` AND `h=F_qq V_rel^label`, SO THE M5 TEMPORAL CROSSING SIGN, THE LOCAL VERTICAL OCTUPOLE, AND THE ZERO-SURFACE MOTION ARE FACTORIZED INTO SEMILINEAR CURVATURE `F_qq`, ROOT-NORMAL SLOPE, AND LABEL-ROOT RELATIVE FLOW. NO SIGN OF THESE THREE FACTORS IS YET UNIVERSALLY FIXED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular semilinear kappa-zero root

On the great-circle semilinear branch,

\[
\boxed{
\kappa=F_q(q,x_3,\theta).
}
\]

Suppose a regular zero root can be written locally as

\[
\boxed{
F_q(q_*(x_3,\theta),x_3,\theta)=0
}
\]

with

\[
\boxed{F_{qq}\neq0.}
\]

The implicit function theorem gives

\[
\boxed{
q_{*,\theta}
=-\frac{F_{q\theta}}{F_{qq}},
\qquad
q_{*,3}
=-\frac{F_{q3}}{F_{qq}}.
}
\]

These are root-manifold derivatives in label space.

---

## 2. M17-013 label-plane relative crossing velocity

M17-013 gives the reduced material label flow

\[
\boxed{
D_Bq=H(q,x_3,\theta),
\qquad
D_Bx_3=K(q,x_3,\theta),
}
\]

with

\[
K=G+\frac12x_3.
\]

Define the relative flow through the zero-root graph

\[
\boxed{
V_{rel}^{label}
:=H-q_{*,\theta}-Kq_{*,3}.
}
\]

At `kappa=0`, M17-013 gives

\[
\boxed{
h=D_B\kappa
=F_{qq}V_{rel}^{label}.
}
\]

Thus temporal material crossing is semilinear root curvature times relative label flow.

---

## 3. Axial spatial slope of kappa

Differentiate

\[
\kappa=F_q(q,x_3,\theta)
\]

in the physical axial coordinate:

\[
\kappa_3
=F_{qq}q_3+F_{q3}.
\]

Use

\[
F_{q3}=-F_{qq}q_{*,3}.
\]

Then

\[
\boxed{
\kappa_3
=F_{qq}(q_3-q_{*,3}).
}
\]

Hence a spatially regular vertical zero crossing requires

\[
\boxed{
q_3-q_{*,3}\neq0
}
\]

as well as `F_qq!=0`.

The scalar

\[
\boxed{N_*:=q_3-q_{*,3}}
\]

is the root-normal slope of the actual q-field relative to the semilinear zero-root graph.

---

## 4. The actual spatial zero surface

At the centered vertical core, the actual `kappa=0` crossing is equivalently

\[
\boxed{
q(0,0,z_0(\theta),\theta)
=q_*(z_0(\theta),\theta).
}
\]

Let

\[
\boxed{v_0:=z_0'(\theta).}
\]

Differentiate the crossing condition:

\[
q_\theta+v_0q_3
=q_{*,\theta}+v_0q_{*,3}.
\]

Therefore

\[
\boxed{
q_\theta-q_{*,\theta}
+v_0(q_3-q_{*,3})=0.
}
\]

---

## 5. Material axial velocity equals K

At the vertical nodal filament,

\[
\nabla_hq=0.
\]

Therefore

\[
D_Bq
=q_\theta+B_3q_3.
\]

But M17-013 gives

\[
D_Bq=H
\]

and

\[
D_Bx_3=K.
\]

Hence at the vertical core

\[
\boxed{B_3=K}
\]

and

\[
\boxed{H=q_\theta+Kq_3.}
\]

---

## 6. Exact relation between spatial and label relative velocity

Use Section 4 to eliminate `q_theta-q_{*,theta}` from the label relative flow:

\[
\begin{aligned}
V_{rel}^{label}
&=H-q_{*,\theta}-Kq_{*,3}\\
&=q_\theta+Kq_3-q_{*,\theta}-Kq_{*,3}\\
&=(q_\theta-q_{*,\theta})
+K(q_3-q_{*,3})\\
&=(K-v_0)(q_3-q_{*,3}).
\end{aligned}
\]

Since `K=B_3`,

\[
\boxed{
V_{rel}^{label}
=(B_3-v_0)(q_3-q_{*,3}).
}
\]

For a spatially regular crossing `q_3-q_{*,3}!=0`,

\[
\boxed{
B_3-v_0
=\frac{V_{rel}^{label}}{q_3-q_{*,3}}.
}
\]

Thus M17-090's spatial relative velocity and M17-013's label-root relative flow are exact coordinate transforms of one crossing geometry.

---

## 7. Recover both h factorizations

Section 3 gives

\[
\kappa_3=F_{qq}(q_3-q_{*,3}).
\]

Section 6 gives

\[
V_{rel}^{label}
=(B_3-v_0)(q_3-q_{*,3}).
\]

Therefore

\[
F_{qq}V_{rel}^{label}
=(B_3-v_0)\kappa_3.
\]

Hence the two earlier expressions are identical:

\[
\boxed{
h
=F_{qq}V_{rel}^{label}
=(B_3-v_0)\kappa_3.
}
\]

This is a descriptor equivalence, not an additional equation.

---

## 8. Insert the vertical local octupole

M17-090 gives at a regular vertical `kappa=0` crossing

\[
(\mathcal O_{loc}^{(3)})_{333}
=-\frac15|Q|_F^2\kappa_3.
\]

Use Section 3:

\[
\boxed{
(\mathcal O_{loc}^{(3)})_{333}
=-\frac15|Q|_F^2
F_{qq}(q_3-q_{*,3}).
}
\]

Together with

\[
\boxed{
h=F_{qq}V_{rel}^{label},}
\]

the local crossing geometry factorizes into three signed scalars:

\[
\boxed{
F_{qq},
\qquad
N_*=q_3-q_{*,3},
\qquad
V_{rel}^{label}.
}
\]

The octupole uses `F_qq N_*`; the temporal crossing uses `F_qq V_rel^label`.

---

## 9. Sign table

At a regular crossing,

\[
\operatorname{sgn}h
=\operatorname{sgn}(F_{qq})
\operatorname{sgn}(V_{rel}^{label}),
\]

while

\[
\operatorname{sgn}\mathcal O_{loc,333}^{(3)}
=-\operatorname{sgn}(F_{qq})
\operatorname{sgn}(N_*).
\]

Therefore

\[
\boxed{
\operatorname{sgn}\left(h\,\mathcal O_{loc,333}^{(3)}\right)
=-\operatorname{sgn}(V_{rel}^{label}N_*).
}
\]

The semilinear curvature sign `F_qq` cancels from the product.

Equivalently,

\[
\boxed{
\operatorname{sgn}(h\,\mathcal O_{loc,333}^{(3)})
=-\operatorname{sgn}(B_3-v_0),
}
\]

because `B_3-v_0=V_rel^label/N_*`.

---

## 10. What must be controlled to bridge M5 to the octupole

M5-685 biases the flux-weighted crossing current toward

\[
h<0.
\]

M17-091 shows that this does not determine the octupole sign unless one additionally controls either

\[
\boxed{
\operatorname{sgn}(B_3-v_0)
}
\]

or equivalently the relative signs of

\[
\boxed{
V_{rel}^{label}
\quad\text{and}\quad
N_*=q_3-q_{*,3}.
}
\]

Thus the missing bridge variable has now been expressed entirely inside the reduced semilinear label geometry.

No external geometric descriptor is needed.

---

## 11. Degenerate exits

The factorization requires two regularity conditions:

\[
F_{qq}\neq0,
\qquad
q_3-q_{*,3}\neq0.
\]

If

\[
F_{qq}=0,
\]

the semilinear kappa root itself is degenerate.

If

\[
q_3-q_{*,3}=0,
\]

then

\[
\kappa_3=0
\]

and, because `grad_h kappa=0`, the spatial zero level is critical.

These are distinct degeneration exits and must not be absorbed into the regular sign ledger.

---

## 12. DSD analysis

M17-013 and M17-090 had apparently different relative-velocity descriptors:

- label-root relative flow `V_rel^label`;
- spatial zero-surface relative speed `B_3-v_0`.

M17-091 shows they are related by the root-normal slope `N_*`:

\[
\boxed{
V_{rel}^{label}
=(B_3-v_0)N_*.
}
\]

Thus the vertical crossing hierarchy is

\[
\boxed{
(q_*,F_{qq})
\to
N_*
\to
\kappa_3
\to
\mathcal O_{loc,333}^{(3)},
}
\]

and independently

\[
\boxed{
(q_*,F_{qq})
\to
V_{rel}^{label}
\to
h.
}
\]

The missing sign bridge is their relative orientation.

---

## 13. DSD audit

### Audit A — counting the two relative velocities as independent constraints
Rejected. They are coordinate representations of the same crossing motion.

### Audit B — replacing q_3-q_*3 by q_3
Rejected. The explicit x_3 dependence of `F` moves the zero-root graph and must be retained.

### Audit C — assuming F_qq sign cancels from h alone
Rejected. It cancels only in the product with the local octupole sign relation.

### Audit D — using the graph formula at a spatially critical zero
Rejected. `N_*=0` is a separate degenerate branch.

### Audit E — claiming M5 now fixes the octupole sign
Rejected. The sign of the root-relative spatial velocity remains unconstrained.

### Audit F — proof status
The crossing descriptors are unified but the sign/covariance firewall remains.

---

## 14. Updated vertical zero-crossing gate

At every regular vertical semilinear zero crossing,

\[
\boxed{
\begin{aligned}
\kappa_3&=F_{qq}N_*,\\
h&=F_{qq}V_{rel}^{label},\\
V_{rel}^{label}&=(B_3-v_0)N_*,\\
\mathcal O_{loc,333}^{(3)}&=-\frac15|Q|_F^2F_{qq}N_*.
\end{aligned}
}
\]

Therefore the vertical M5-to-octupole bridge is reduced to a signed joint distribution of

\[
\boxed{(V_{rel}^{label},N_*)}
\]

or equivalently `(h, B_3-v_0)` across the recurrent crossing population.

This is now a precise covariance target rather than an unspecified geometric gap.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
