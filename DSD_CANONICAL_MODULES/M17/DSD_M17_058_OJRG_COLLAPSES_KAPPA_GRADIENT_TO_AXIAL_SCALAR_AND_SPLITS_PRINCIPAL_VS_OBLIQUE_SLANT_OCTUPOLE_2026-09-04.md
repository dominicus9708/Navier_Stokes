# DSD M17-058 — OJRG collapses the kappa gradient to one axial scalar and splits principal versus oblique slant octupole coupling

Date: 2026-09-04
Canonical ID: **M17-058**

Status: **INTERNAL OCTUPOLE JET REDUCTION / ON THE REGULAR SLANTED GREAT-CIRCLE NODAL BRANCH, USING THE SAME SEMILINEAR NODAL EXTENSION ALREADY USED IN M17-015, `Delta q=F(q,x_3,theta)` AND `kappa=F_q` IMPLY `grad_h kappa=0` AT `grad_h q=0`. THUS `grad kappa=kappa_3 e_3`. THE FULL FIRST VORTICITY JET IS NOT FREE EITHER: `W_h=J grad_h q`, `Q=grad_h^2 q`, AND THE NODAL SLOPE LAW `p=-Q^{-1}grad_h q_3` GIVE `A x=JQ(x_h-p x_3)` AND `A^TA=L_p^TQ^2L_p`. THE KAPPA-GRADIENT PART OF THE LOCAL L=3 PAYER MISMATCH THEREFORE HAS THE EXACT DSAIG PROJECTION `o_kappa=(4/15) kappa_3 |p| (E_Q phat)·Q^2 phat`. AFTER NORMALIZATION BY `|Q|_F^2`, THIS GEOMETRIC FACTOR IS PURELY THE FROZEN SLANT AZIMUTH RELATIVE TO THE PRINCIPAL AXES OF Q; IN A PRINCIPAL FRAME IT IS `±sin(2vartheta)/(2sqrt2)`. HENCE PRINCIPAL-AXIS SLANT KILLS THE ENTIRE KAPPA-GRADIENT OCTUPOLE PROJECTION, WHILE OBLIQUE SLANT RETAINS IT. THE REMAINING VORTICITY-CURVATURE OCTUPOLE IS LINEAR IN THE THIRD STREAMFUNCTION JET `H=grad^3 q`; THE HORIZONTAL SEMILINEAR DERIVATIVES GIVE TWO TRACE CONSTRAINTS, LEAVING SEVEN PHYSICALLY RELEVANT H-COMPONENTS. DIFFERENTIATING `Delta W=kappa W` DOES NOT REMOVE THESE SECOND-VORTICITY/THIRD-q JETS; ITS FIRST DERIVATIVE CONSTRAINS THE NEXT VORTICITY JET AND ITS SECOND DERIVATIVE THE ONE AFTER THAT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Scope: semilinear nodal extension

M16-027 first derives on regular horizontal level regions

\[
\Delta q=F(q,x_3,\theta),
\qquad
\kappa=F_q(q,x_3,\theta).
\]

The present module uses the same smooth/analytic extension of this semilinear representation to the regular nodal filament that is already used in M17-015 and subsequent nodal modules.

This scope is essential. We do not claim that an arbitrary critical point of an unrelated semilinear chart automatically carries this extension.

At the regular winding filament,

\[
\boxed{\nabla_h q=0.}
\]

Therefore

\[
\nabla_h\kappa
=F_{qq}\nabla_hq
=0.
\]

Hence

\[
\boxed{
\nabla\kappa
=\kappa_3 e_3,
\qquad
\kappa_3:=\partial_3\kappa.
}
\]

So the three-component vector `k=grad kappa` appearing in M17-057 collapses to one scalar on this branch.

---

## 2. The first vorticity jet is determined by Q and the nodal slope

Use

\[
W_h=J\nabla_hq.
\]

At the node define

\[
\boxed{Q:=\nabla_h^2q.}
\]

M17-024 gives for a genuinely slanted filament

\[
\boxed{
p=-Q^{-1}c,
\qquad
c:=\nabla_h q_3,
}
\]

or

\[
\boxed{c=-Qp.}
\]

Let

\[
x=(x_h,x_3).
\]

The first vorticity jet therefore acts as

\[
\begin{aligned}
Ax
&=J(Qx_h+c x_3)\\
&=JQ(x_h-px_3).
\end{aligned}
\]

Define the `2 x 3` map

\[
L_p x:=x_h-px_3.
\]

Then

\[
\boxed{A=JQL_p}
\]

and, because `J` is orthogonal,

\[
\boxed{
C:=A^TA
=L_p^TQ^2L_p.
}
\]

Thus the positive-semidefinite metric tensor `C` in M17-057 is fully determined by the horizontal nodal Hessian `Q` and the slope vector `p`.

Its null direction is exactly the filament tangent `(p,1)`.

---

## 3. Exact kappa-gradient cubic before STF projection

M17-057 gives

\[
F_3^{(\kappa)}(x)
=(\nabla\kappa\cdot x)(x^TCx).
\]

Using Sections 1--2,

\[
\boxed{
F_3^{(\kappa)}(x)
=\kappa_3 x_3
\left(x_h-px_3\right)^TQ^2
\left(x_h-px_3\right).
}
\]

Thus this entire cubic channel is controlled by

\[
\boxed{
(\kappa_3,Q,p)
}
\]

rather than an arbitrary `grad kappa` and arbitrary rank-two `A`.

---

## 4. DSAIG projection of the kappa-gradient octupole

Let

\[
u:=\widehat p=\frac p{|p|}
\]

and let `E_Q` be a Frobenius-unit horizontal trace-free tensor perpendicular to the nonzero traceless nodal Hessian direction `Q_0=TF_h Q`.

M17-057 defines the local mismatch

\[
\mathfrak o_{loc}
=E_Q:TF_h[u\lrcorner\mathcal O_{loc}^{(3)}].
\]

For the kappa-gradient part, all fully horizontal components of the unprojected symmetric cubic tensor vanish because `grad_h kappa=0`.
The only contribution to the horizontal STF contraction comes from the three-dimensional STF trace subtraction.

The horizontal trace vector is

\[
\begin{aligned}
t_h^{(\kappa)}
&=\frac23(C\nabla\kappa)_h\\
&=-\frac23\kappa_3Q^2p.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathfrak o_{\kappa}
=\frac4{15}\kappa_3
(E_Qu)\cdot Q^2p
}
\]

or

\[
\boxed{
\mathfrak o_{\kappa}
=\frac4{15}\kappa_3|p|
(E_Qu)\cdot Q^2u.
}
\]

This is an exact scalar reduction of the multiplier-gradient part of the local payer octupole in the frozen DSAIG frame.

---

## 5. Pure angular coupling after normalization

Because M17-014 gives scalar material evolution of `Q` and M17-024 freezes `u`, define

\[
\boxed{
\gamma_{Qp}
:=
\frac{(E_Qu)\cdot Q^2u}{|Q|_F^2}.
}
\]

The scalar multiplier of `Q` cancels, so

\[
\boxed{D_B\gamma_{Qp}=0}
\]

on the regular slanted nonconformal branch.

Choose the principal basis of the symmetric Hessian,

\[
Q=\operatorname{diag}(q_1,q_2),
\]

and write

\[
u=(\cos\vartheta,\sin\vartheta).
\]

For Frobenius-unit `E_Q` perpendicular to `Q_0`,

\[
E_Q
=\pm\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Then

\[
(E_Qu)\cdot Q^2u
=\pm\frac{q_1^2+q_2^2}{2\sqrt2}\sin2\vartheta.
\]

Since

\[
|Q|_F^2=q_1^2+q_2^2,
\]

we obtain

\[
\boxed{
\gamma_{Qp}
=\pm\frac1{2\sqrt2}\sin2\vartheta.
}
\]

Hence the normalized coupling depends only on the frozen angle between slant azimuth and the nodal-Hessian principal axes.

---

## 6. Principal-slant versus oblique-slant split

### Principal-slant class

If

\[
\vartheta=0
\quad\text{or}\quad
\frac\pi2
\pmod{\pi},
\]

then

\[
\boxed{\gamma_{Qp}=0}
\]

and therefore

\[
\boxed{\mathfrak o_{\kappa}=0.}
\]

Thus **the entire kappa-gradient contribution to the forbidden local octupole projection disappears**.

This does not mean the total octupole vanishes; the vorticity-curvature / third-q-jet channel remains.

### Oblique-slant class

If

\[
\sin2\vartheta\ne0,
\]

then

\[
\boxed{
\mathfrak o_{\kappa}
=\pm\frac{2}{15\sqrt2}
\kappa_3|p||Q|_F^2\sin2\vartheta.
}
\]

The angular factor has fixed nonzero sign along the marked regular filament once the orientation convention for `E_Q` is fixed.
Only the signed scalar `kappa_3` and positive amplitudes can change its sign/magnitude.

Because `(Qhat,phat)` is material invariant, a regular filament cannot move from principal to oblique slant without leaving the assumed branch.

---

## 7. Reduce the vorticity-curvature term to the third streamfunction jet

Let

\[
\boxed{H:=\nabla^3q}
\]

be the symmetric third derivative tensor of `q`.

Since

\[
W_a=J_{a\alpha}q_\alpha,
\qquad \alpha\in\{1,2\},
\]

we have

\[
\boxed{
B_{aij}
=J_{a\alpha}H_{\alpha ij}.
}
\]

Therefore the second cubic density from M17-057 becomes

\[
\boxed{
F_3^{(W)}(x)
=\kappa_0
\big[Q(x_h-px_3)\big]_\alpha
H_{\alpha ij}x_ix_j.
}
\]

Thus `B=grad^2 W` is not an independent tensor on the great-circle branch; it is the horizontal-output projection of one symmetric scalar third jet `H=grad^3q`.

---

## 8. Semilinear trace constraints on H

Differentiate

\[
\Delta q=F(q,x_3,\theta)
\]

in a horizontal direction `alpha=1,2`.
At the node `q_alpha=0`, hence

\[
\partial_\alpha\Delta q
=F_q q_\alpha
=0.
\]

Therefore

\[
\boxed{
H_{\alpha11}+H_{\alpha22}+H_{\alpha33}=0,
\qquad \alpha=1,2.
}
\]

These are exactly the two output trace constraints corresponding to

\[
\Delta W(0)=0.
\]

A symmetric rank-three tensor in three variables has ten scalar components.
The component `H_333` never enters `B_{aij}` because the vorticity output is horizontal.
Hence nine components are physically visible to `B`, and the two trace constraints reduce these to

\[
\boxed{7}
\]

independent third-q-jet components at this level.

No further reduction follows solely from the semilinear elliptic equation without introducing higher jets or filament-curvature data.

---

## 9. Why differentiating Delta W=kappa W does not eliminate H or kappa_3

At the node,

\[
W=0.
\]

One derivative gives

\[
\boxed{
\partial_j\Delta W
=\kappa_0\partial_jW,
}
\]

which constrains the **third derivative of W**, equivalently a fourth derivative of `q`.
It does not constrain `B=grad^2W` beyond the already used trace condition.

Two derivatives give

\[
\boxed{
\partial_{ij}\Delta W
=\kappa_i\partial_jW
+\kappa_j\partial_iW
+\kappa_0\partial_{ij}W,
}
\]

which constrains the **fourth derivative of W**, equivalently a fifth derivative of `q`.

Thus it is incorrect to use these identities to algebraically solve away `kappa_3` or the seven-component third-q jet `H` at the current order.
They instead determine compatibility with the next layers of the analytic jet hierarchy.

---

## 10. DSD analysis

M17-057 used the descriptor set

\[
(\nabla\kappa,A,B).
\]

OJRG replaces it, on the slanted semilinear nodal branch, by

\[
\boxed{
(\kappa_3,Q,p,H^{(7)}).
}
\]

Moreover the multiplier-gradient share factorizes as

\[
\boxed{
\mathfrak o_\kappa
=\text{signed axial scalar}
\times\text{positive amplitudes}
\times\text{frozen angular invariant}.
}
\]

This makes the previously generic STF orientation dependence into a transparent material geometry.

---

## 11. DSD audit

### Audit A — extending F through the node silently
Avoided. The same semilinear nodal-extension assumption already used in M17-015 is stated explicitly.

### Audit B — claiming grad kappa vanishes completely
Rejected. Only the horizontal components vanish; `kappa_3` remains free.

### Audit C — treating A as generic rank-two matrix
Rejected. Great-circle streamfunction and the slant kernel give `A=JQL_p` exactly.

### Audit D — treating B as generic
Rejected. `B` is the projection of the symmetric third streamfunction jet `H` and obeys two trace constraints.

### Audit E — overusing differentiated elliptic equations
Rejected. They constrain higher jets rather than eliminating the current octupole variables.

### Audit F — claiming principal slant kills the whole octupole
Rejected. It kills only the `grad kappa` contribution in the forbidden DSAIG projection; the third-q-jet contribution and global pressure moment remain.

### Audit G — proof status
This is a genuine finite-dimensional reduction and branch split, not a contradiction.

---

## 12. Updated Rank-1 local octupole frontier

The regular nonvertical nonconformal slanted branch now splits as

\[
\boxed{
R_1^{slant,nonconf}
\Longrightarrow
R_{principal}^{H_3}
\ \lor\ 
R_{oblique}^{\kappa_3+H_3}
\ \lor\ 
T_{nodal/rank}.
}
\]

- `R_principal^(H3)`: the kappa-gradient octupole projection vanishes identically; only the seven-component constrained third-q jet, local pressure particular term, global l=3 pressure moment, and viscous forcing remain.
- `R_oblique^(kappa3+H3)`: the same channels remain plus the explicit nonzero angular multiplier of `kappa_3`.
- `T_nodal/rank`: rank loss, horizontal-Jacobian failure, or finite-jet turnover.

---

## 13. Next target

The highest-value next calculation is to derive the material evolution of the reduced third-q-jet projection that actually enters

\[
\mathfrak o_{loc}.
\]

Because `Qhat` and `phat` are frozen, only a small number of scalar contractions of `H` are relevant.
The target is to determine whether these contractions have scalar multiplier laws, are forced by `kappa_3`, or require new fourth-jet forcing.

This is the **Reduced Octupole Projection Dynamics Gate (ROPDG)**.

In parallel, the principal-slant class is especially sharp because it has no `grad kappa` octupole screening channel at all.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
