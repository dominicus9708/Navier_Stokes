# DSD M17-057 — The local kappa-payer octupole has an explicit STF tensor in grad kappa, grad W, and grad^2 W

Date: 2026-09-04
Canonical ID: **M17-057**

Status: **INTERNAL LOCAL OCTUPOLE TENSOR GATE / M17-056 IDENTIFIES THE FIRST LOCAL CUBIC PAYER DENSITY `F_3=(k·x)(x^T C x)+kappa_0(Ax)·B[x,x]`, WITH `k=grad kappa`, `A=grad W`, `C=A^T A`, AND `B=grad^2 W`. WRITING `F_3=T_{ijk}x_ix_jx_k`, THE SYMMETRIC COEFFICIENT IS THE SUM OF `T^(k)=(1/3)sym(k tensor C)` AND `T^(W)=(kappa_0/3)sym(A_{a·} tensor B_{a··})`. ITS TRACE VECTORS ARE `t^(k)=(1/3)(2Ck+(tr C)k)` AND `t^(W)=(kappa_0/3)grad|A|_F^2`, WHERE THE LAST IDENTITY USES `Delta W(0)=0`. THE LOCAL l=3 PAYER TENSOR IS THE UNIQUE STF PROJECTION `O_loc=T-(1/5)sym(delta tensor t)`. THUS THE FIRST CUBIC PAYER ORIENTATION IS A COMPLETELY EXPLICIT THIRD-JET OBJECT AND CAN BE CONTRACTED DIRECTLY WITH THE FROZEN SLANT/ANISOTROPY PAIR `(phat,E_Q)`. NO SIGN OR NONZERO LOWER BOUND FOLLOWS FROM REGULARITY ALONE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-056

At a regular nodal point,

\[
W(x)=Ax+\frac12B[x,x]+O(|x|^3),
\]

\[
\kappa(x)=\kappa_0+k\cdot x+O(|x|^2),
\]

where

\[
\boxed{
A=\nabla W(0),
\qquad
B=\nabla^2W(0),
\qquad
k=\nabla\kappa(0).
}
\]

Set

\[
\boxed{C:=A^TA.}
\]

The first odd/cubic part of the weighted payer density is

\[
\boxed{
F_3(x)
=(k\cdot x)(x^TCx)
+\kappa_0(Ax)\cdot B[x,x].
}
\]

Its l=3 part is the STF cubic component.

---

## 2. Symmetric tensor for the multiplier-gradient term

Write

\[
F_3^{(\kappa)}
=(k\cdot x)(x^TCx).
\]

The symmetric rank-three coefficient tensor satisfying

\[
F_3^{(\kappa)}
=T^{(\kappa)}_{ijk}x_ix_jx_k
\]

is

\[
\boxed{
T^{(\kappa)}_{ijk}
=\frac13
\left(
 k_iC_{jk}
+k_jC_{ik}
+k_kC_{ij}
\right).
}
\]

This is the fully symmetrized product of `k` and the positive semidefinite metric tensor `C=A^TA`.

---

## 3. Trace vector of the multiplier-gradient tensor

Define

\[
 t^{(\kappa)}_k
:=T^{(\kappa)}_{iik}.
\]

Then

\[
\begin{aligned}
 t^{(\kappa)}_k
&=\frac13
\left(
2C_{ik}k_i
+(\operatorname{tr}C)k_k
\right).
\end{aligned}
\]

Therefore, vectorially,

\[
\boxed{
 t^{(\kappa)}
=\frac13
\left(
2Ck+(\operatorname{tr}C)k
\right).
}
\]

Since

\[
\operatorname{tr}C=|A|_F^2,
\]

this depends only on the first vorticity jet and the multiplier gradient.

---

## 4. Symmetric tensor for the vorticity-curvature term

The second cubic term is

\[
F_3^{(W)}
=\kappa_0(Ax)\cdot B[x,x].
\]

In components,

\[
F_3^{(W)}
=\kappa_0 A_{ai}B_{ajk}x_ix_jx_k.
\]

Because `B_{ajk}=B_{akj}`, the fully symmetric coefficient is

\[
\boxed{
T^{(W)}_{ijk}
=\frac{\kappa_0}{3}
\left(
 A_{ai}B_{ajk}
+A_{aj}B_{aik}
+A_{ak}B_{aij}
\right),
}
\]

with summation over the vorticity output index `a`.

---

## 5. Trace vector of the vorticity-curvature tensor

Take the trace:

\[
 t^{(W)}_k
:=T^{(W)}_{iik}.
\]

Then

\[
 t^{(W)}_k
=\frac{\kappa_0}{3}
\left(
2A_{ai}B_{aik}
+A_{ak}B_{aii}
\right).
\]

M17-056 uses the nodal elliptic equation

\[
\Delta W(0)=0,
\]

so

\[
\boxed{B_{aii}=0.}
\]

Hence

\[
\boxed{
 t^{(W)}_k
=\frac{2\kappa_0}{3}A_{ai}B_{aik}.
}
\]

But

\[
\partial_k|A|_F^2
=2A_{ai}\partial_kA_{ai}
=2A_{ai}B_{aik}.
\]

Therefore

\[
\boxed{
 t^{(W)}
=\frac{\kappa_0}{3}\nabla|A|_F^2.
}
\]

---

## 6. Total cubic coefficient and trace

Define

\[
\boxed{
T:=T^{(\kappa)}+T^{(W)}.
}
\]

Then

\[
F_3(x)=T_{ijk}x_ix_jx_k.
\]

Its trace vector is

\[
\boxed{
 t
=\frac13
\left[
2Ck+(\operatorname{tr}C)k
+\kappa_0\nabla|A|_F^2
\right].
}
\]

---

## 7. Explicit STF octupole tensor

For a symmetric rank-three tensor in three dimensions, the STF projection is

\[
\boxed{
(STF_3T)_{ijk}
=T_{ijk}
-\frac15
\left(
\delta_{ij}t_k
+\delta_{ik}t_j
+\delta_{jk}t_i
\right).
}
\]

Define the local payer octupole tensor

\[
\boxed{
\mathcal O_{loc}^{(3)}
:=STF_3T.
}
\]

Thus explicitly

\[
\boxed{
\begin{aligned}
(\mathcal O_{loc}^{(3)})_{ijk}
={}&\frac13
\left(
 k_iC_{jk}+k_jC_{ik}+k_kC_{ij}
\right)\\
&+\frac{\kappa_0}{3}
\left(
 A_{ai}B_{ajk}+A_{aj}B_{aik}+A_{ak}B_{aij}
\right)\\
&-\frac15
\left(
\delta_{ij}t_k
+\delta_{ik}t_j
+\delta_{jk}t_i
\right),
\end{aligned}
}
\]

with `t` given in Section 6.

This tensor is symmetric and trace free on every pair of indices.

---

## 8. Polynomial interpretation

Every homogeneous cubic polynomial has the decomposition

\[
F_3(x)
=H_3(x)+|x|^2L_1(x),
\]

where `H_3` is harmonic cubic.

The tensor `O_loc^(3)` is exactly the coefficient tensor of `H_3`:

\[
\boxed{
H_3^{payer}(x)
=(\mathcal O_{loc}^{(3)})_{ijk}x_ix_jx_k.
}
\]

Thus M17-057 is the tensor version of the spherical projection `Pi_{l=3}F_3` in M17-056.

---

## 9. Direct DSAIG/octupole contraction

Let `E_Q` be the unit horizontal trace-free tensor perpendicular to the frozen nodal anisotropy `Q_0`, and let `phat` be the frozen slant direction.

Define the local cubic payer mismatch

\[
\boxed{
\mathfrak o_{loc}
:=
E_Q:
TF_h[\widehat p\lrcorner\mathcal O_{loc}^{(3)}].
}
\]

This is now an explicit polynomial in

\[
\boxed{
\nabla\kappa,
\quad
\nabla W,
\quad
\nabla^2W,
\quad
\kappa_0,
\quad
\widehat p,
\quad
E_Q.
}
\]

No spherical-harmonic basis is required to compute it.

---

## 10. No generic sign or nonzero lower bound

Even with

\[
\kappa_0>0
\]

and a uniformly nondegenerate `A`, the two STF tensors

\[
STF_3\,sym(k\otimes C)
\]

and

\[
STF_3\,sym(A\cdot B)
\]

can have either relative orientation.

They may reinforce or cancel in the single DSAIG projection `mathfrak o_loc`.

Therefore

\[
\boxed{
\kappa_0>0,
\quad
\det G_h\ne0
\not\Rightarrow
\mathfrak o_{loc}\ne0.
}
\]

This is a genuine higher-jet freedom, not a failure of the lower-order estimates.

---

## 11. DSD analysis

The l=3 payer descriptor has now passed through three equivalent representations:

\[
\boxed{
\text{spherical }Y_{3m}
\leftrightarrow
\text{harmonic cubic polynomial}
\leftrightarrow
\text{STF rank-three tensor}.
}
\]

The last is best suited for comparison with the already frozen tensor pair `(Q_0,p)`.

---

## 12. DSD audit

### Audit A — omitting symmetrization
Avoided. Both cubic coefficient tensors are fully symmetrized before STF projection.

### Audit B — omitting the trace of B
Correctly removed using `Delta W(0)=0`.

### Audit C — identifying the trace vector with the octupole
Rejected. The trace vector is precisely the l=1 part removed by STF projection.

### Audit D — claiming positive C=A^T A gives positive octupole
Rejected. An STF rank-three tensor has no positivity order analogous to a quadratic form.

### Audit E — proof status
The local cubic payer is now explicitly computable but remains sign-indefinite.

---

## 13. Updated local Rank-1 moment gate

The local l=3 contribution to pressure-source production can now be tested directly using

\[
\boxed{
\mathcal O_{loc}^{(3)}
=STF_3\left[
\frac13sym(k\otimes A^TA)
+\frac{\kappa_0}{3}sym(A\cdot B)
\right],
}
\]

with the detailed coefficient convention of Sections 2--7.

The remaining pressure lock must combine this explicit local tensor with mesoscopic/global STF source moments and the viscous/strain/pressure-Hessian production terms of M17-053--054.

---

## 14. Next target — use nodal multiplier equations to reduce k and B

The next useful calculation is to differentiate

\[
\Delta W=\kappa W
\]

at the node and combine

\[
\nabla\Delta W=\kappa_0\nabla W
\]

from M17-011 with the slanted semilinear/nodal equations.

The aim is to determine which components of `grad kappa` and `grad^2W` entering `O_loc^(3)` are genuinely free and which are fixed by the third vorticity jet, nodal Hessian shape and material recurrence.

This is the **Octupole Jet Reduction Gate (OJRG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
