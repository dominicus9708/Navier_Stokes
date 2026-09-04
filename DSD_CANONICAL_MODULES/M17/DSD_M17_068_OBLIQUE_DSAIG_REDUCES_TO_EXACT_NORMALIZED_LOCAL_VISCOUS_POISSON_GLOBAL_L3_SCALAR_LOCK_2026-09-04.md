# DSD M17-068 — Oblique DSAIG reduces to an exact normalized local-viscous / explicit-Poisson / global-l=3 scalar lock

Date: 2026-09-04
Canonical ID: **M17-068**

Status: **INTERNAL OBLIQUE GLOBAL LOCK REDUCTION / ON A GENUINE-OBLIQUE REGULAR NONCONFORMAL NODAL CORE, THE LOCAL POISSON SOURCE-GRADIENT SHARE OF DSAIG CAN BE COMPUTED EXACTLY. IN THE NODAL GAUGE, `Sigma_33=partial_3 U_3=G_q q_3+G_3`, WITH `q_a=q_3=0` AT THE MARKED NODE AND THE SLANTED FILAMENT IDENTITY `grad_h q_3=-Qp`; HENCE `grad_h Sigma_33=-G_q Qp`. SUBSTITUTION INTO M17-051 GIVES THE FORBIDDEN LOCAL PARTICULAR PRESSURE SCALAR `n_part = -eps_E (3 sqrt(2)/5) lambda G_q P^2 (tr Q) sin(2 vartheta)`. AFTER DIVIDING BY THE SLANT MAGNITUDE `P`, THE COMPLETE EXACT DSAIG PERPENDICULAR BALANCE IS `v_vartheta - n_vartheta = m_3`, WHERE `v_vartheta=E_Q:TF_h[(phat dot grad_h)Delta Sigma_h]`, `n_vartheta=n_part/P`, AND `m_3` IS THE NORMALIZED GLOBAL STF PRESSURE l=3 MISMATCH OF M17-054. THERE ARE NO ADDITIONAL HIGHER PRESSURE TAYLOR TERMS IN THIS POINTWISE THIRD-DERIVATIVE IDENTITY: THE RAW THIRD PRESSURE JET SPLITS EXACTLY INTO ITS POISSON TRACE/PARTICULAR PART PLUS THE STF GLOBAL HARMONIC TENSOR. CONSEQUENTLY `D_B(v_vartheta-n_vartheta)=Pi_3^prod+Pi_3^rel`, AND RECURRENCE REQUIRES ZERO MEAN OF THAT GLOBAL PROJECTED SOURCE/TRANSPORT PRODUCTION. THIS MAKES THE OBLIQUE GLOBAL LOCK ONE SCALAR COCYCLE WITH AN EXPLICIT LOCAL POISSON TAX, BUT NO SIGN CONTRADICTION IS YET OBTAINED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Frozen oblique frame

Use the material-invariant nonconformal nodal frame

\[
Q=\operatorname{diag}(q_1,q_2),
\]

and

\[
p=P(c,s),
\qquad
P=|p|>0,
\qquad
c=\cos\vartheta,
\qquad
s=\sin\vartheta.
\]

For genuine obliquity,

\[
\boxed{\sin2\vartheta\neq0.}
\]

Let the unit forbidden horizontal trace-free direction be

\[
\boxed{
E_Q
=\varepsilon_E\frac1{\sqrt2}
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
\varepsilon_E=\pm1.
}
\]

The sign only fixes orientation of the one-dimensional forbidden tensor line.

---

## 2. Exact local Poisson cubic from M17-051

M17-051 gives the DSAIG-visible particular cubic pressure tensor

\[
\boxed{
N_{part}
=\frac{6\lambda}{5}
TF_h\left[
 p\otimes\nabla_h\Sigma_{33}
+\nabla_h\Sigma_{33}\otimes p
\right].
}
\]

The only remaining task is to express

\[
\nabla_h\Sigma_{33}
\]

using the slanted nodal geometry.

---

## 3. Horizontal gradient of Sigma_33 on the nodal filament

The vertical velocity law is

\[
\boxed{U_3=G(q,x_3,\theta).}
\]

Since a diagonal strain component equals the corresponding velocity derivative,

\[
\Sigma_{33}=\partial_3U_3.
\]

Hence

\[
\boxed{
\Sigma_{33}
=G_q q_3+G_3.
}
\]

Use the same nodal gauge as M17-059--066:

\[
q=0
\]

along the marked filament.
At the marked core,

\[
\boxed{
q_1=q_2=q_3=0.
}
\]

Differentiate `Sigma_33` horizontally. For `a=1,2`,

\[
\partial_a\Sigma_{33}
=G_{qq}q_aq_3
+G_q q_{a3}
+G_{3q}q_a.
\]

The nodal gauge removes the first and third terms, giving

\[
\boxed{
\partial_a\Sigma_{33}=G_q q_{a3}.
}
\]

M17-024--025 give the slanted-filament tangent identity

\[
\boxed{
\nabla_h q_3=-Qp.
}
\]

Therefore

\[
\boxed{
\nabla_h\Sigma_{33}
=-G_qQp.
}
\]

This is exact at the marked nodal core.

---

## 4. Compute the forbidden particular-pressure scalar

Define

\[
\boxed{n_{part}:=E_Q:N_{part}.}
\]

For any symmetric horizontal matrix, contraction with `E_Q` keeps only the off-diagonal component:

\[
E_Q:A
=\varepsilon_E\sqrt2\,A_{12}
\]

when `A` is trace free, and the off-diagonal part is unchanged by `TF_h`.

Set

\[
r:=\nabla_h\Sigma_{33}=-G_qQp.
\]

Then

\[
r_1=-G_qq_1Pc,
\qquad
r_2=-G_qq_2Ps.
\]

The off-diagonal component of

\[
p\otimes r+r\otimes p
\]

is

\[
\begin{aligned}
p_1r_2+p_2r_1
&=-G_qP^2cs(q_1+q_2)\\
&=-\frac12G_qP^2(q_1+q_2)\sin2\vartheta.
\end{aligned}
\]

Hence

\[
\boxed{
 n_{part}
=-\varepsilon_E
\frac{3\sqrt2}{5}
\lambda G_qP^2(q_1+q_2)\sin2\vartheta.
}
\]

Equivalently,

\[
\boxed{
 n_{part}
=-\varepsilon_E
\frac{3\sqrt2}{5}
\lambda G_qP^2(\operatorname{tr}Q)\sin2\vartheta.
}
\]

Thus the local source-gradient pressure share is not an arbitrary cubic coefficient on the oblique branch.
It is fixed by the repeated-plane strain, vertical label sensitivity, slant magnitude, Hessian trace, and frozen obliquity.

---

## 5. Normalize by the slant magnitude

Define

\[
\boxed{
\mathfrak n_\vartheta
:=\frac{n_{part}}P.
}
\]

Then

\[
\boxed{
\mathfrak n_\vartheta
=-\varepsilon_E
\frac{3\sqrt2}{5}
\lambda G_qP(\operatorname{tr}Q)\sin2\vartheta.
}
\]

This normalization is natural because the harmonic DSAIG share also carries one explicit factor of `P`.

The principal limit is immediate:

\[
\sin2\vartheta=0
\quad\Longrightarrow\quad
\boxed{\mathfrak n_\vartheta=0,}
\]

which recovers the particular-pressure silence used in M17-062.

---

## 6. Exact harmonic pressure share

M17-053 identifies the STF cubic pressure tensor

\[
\boxed{\mathcal H=STF_3(\nabla^3P).}
\]

Its DSAIG contraction is

\[
N_{harm}=TF_h[p\lrcorner\mathcal H].
\]

Define the forbidden scalar

\[
M_3:=E_Q:N_{harm}
\]

and its normalized version

\[
\boxed{m_3:=\frac{M_3}{P}.}
\]

M17-054 proves

\[
\boxed{
D_Bm_3
=\Pi_3^{prod}+\Pi_3^{rel}.
}
\]

---

## 7. Exact normalized viscous scalar

Define

\[
\boxed{
\mathfrak v_\vartheta
:=
E_Q:
TF_h\left[
(\widehat p\cdot\nabla_h)\Delta\Sigma_h
\right],
}
\]

where

\[
\widehat p=\frac pP.
\]

Equivalently, the unnormalized viscous forbidden scalar is

\[
P\mathfrak v_\vartheta
=E_Q:TF_h[(p\cdot\nabla_h)\Delta\Sigma_h].
\]

---

## 8. Full DSAIG gives one scalar equality

The direct slanted-alignment invariance gate M17-044 requires

\[
P_{Q_0}^{\perp}
TF_h\left[
(p\cdot\nabla_h)
(\Delta\Sigma_h-\nabla_h^2P)
\right]
=0.
\]

Contract with `E_Q`.
The pressure third jet splits exactly into

\[
\boxed{
\nabla^3P
=
\text{Poisson trace/particular part}
+
\mathcal H,
}
\]

where `mathcal H` is the STF tensor of M17-053.
Therefore

\[
\boxed{
P\mathfrak v_\vartheta
=n_{part}+M_3.
}
\]

Divide by `P>0`:

\[
\boxed{
\mathfrak v_\vartheta
-\mathfrak n_\vartheta
=m_3.
}
\]

This is the exact **oblique normalized DSAIG scalar lock**.

---

## 9. No hidden higher pressure Taylor remainder

It is important that Section 8 is a pointwise third-derivative identity.
For a symmetric rank-three pressure tensor in three dimensions, the decomposition into trace data and the STF part is algebraically complete.

Therefore the DSAIG pressure share at this order is exactly

\[
\boxed{
N_{part}+N_{harm}.
}
\]

There is no additional independent “higher pressure Taylor term” contributing to the same pointwise third derivative.
Higher spatial jets matter only after further differentiation or for different descriptors.

This closes an ambiguity left in the earlier schematic DSAIG bookkeeping.

---

## 10. Material evolution of the exact lock

Since

\[
\mathfrak v_\vartheta-\mathfrak n_\vartheta=m_3,
\]

M17-054 immediately gives

\[
\boxed{
D_B(\mathfrak v_\vartheta-\mathfrak n_\vartheta)
=\Pi_3^{prod}+\Pi_3^{rel}.
}
\]

Thus the combination of

1. normalized local viscous fourth/fifth-velocity jet;
2. explicit local Poisson source-gradient correction;

is exactly the same scalar state as the global STF `l=3` pressure moment.

The global nonlocality is not a separate extra degree after the equality is imposed; it is the value which the local combination must track.

---

## 11. Recurrent production/transport balance

On a uniformly recurrent nonzero-slant compact branch with bounded third pressure jets, M17-054 gives

\[
\boxed{
\left\langle
\Pi_3^{prod}+\Pi_3^{rel}
\right\rangle=0.
}
\]

Hence the exact local combination also has zero long-time mean drift:

\[
\boxed{
\left\langle
D_B(\mathfrak v_\vartheta-\mathfrak n_\vartheta)
\right\rangle=0.
}
\]

This is a recurrence obligation, not a sign condition.

---

## 12. Relation to the local payer octupole

M17-065 gives a second scalar in the same frozen `(Q,p,E_Q)` frame:

\[
\mathfrak o_{loc}
=\varepsilon_E\frac{\sqrt2}{15}
\left[
\kappa\Xi_\vartheta
+\kappa_3P|Q|_F^2\sin2\vartheta
\right].
\]

The DSAIG lock is instead

\[
\mathfrak v_\vartheta-\mathfrak n_\vartheta=m_3.
\]

These are distinct descriptors:

- `o_loc` is the local `l=3` moment of the payer density `kappa |W|^2`;
- `m_3` is the global STF `l=3` pressure-source moment;
- `v_vartheta` is a local viscous higher-jet projection;
- `n_vartheta` is the exact local Poisson trace correction.

Their common tensor frame does not make them numerically interchangeable.

---

## 13. DSD analysis

The previous oblique pressure gate appeared to contain several tensor freedoms.
After nodal/slant reduction it is actually

\[
\boxed{
\text{one local viscous scalar}
-
\text{one explicit local Poisson scalar}
=
\text{one global l=3 scalar}.
}
\]

The explicit Poisson scalar is

\[
\boxed{
\mathfrak n_\vartheta
\propto
\lambda G_qP(\operatorname{tr}Q)\sin2\vartheta.
}
\]

Thus genuine obliquity adds a calculable local pressure tax which disappears continuously in the principal limit.

---

## 14. DSD audit

### Audit A — treating grad_h Sigma_33 as free
Closed.
On the nodal gauge/slanted branch,

\[
\nabla_h\Sigma_{33}=-G_qQp.
\]

### Audit B — dropping the particular pressure share as in principal slant
Rejected.
It vanishes only when the angular factor or another multiplicative factor vanishes.

### Audit C — adding an unspecified higher-pressure remainder to the third derivative
Rejected.
The trace + STF decomposition of `nabla^3P` is exact.

### Audit D — claiming the global harmonic scalar is independently free after DSAIG
Rejected.
DSAIG fixes it equal to the local combination `v_vartheta-n_vartheta`; its evolution is still globally generated through `Pi_3^prod+Pi_3^rel`.

### Audit E — identifying local payer octupole with pressure l=3
Rejected.
They live in the same angular representation but are different source/moment descriptors.

### Audit F — proof status
The oblique global lock is reduced to one scalar cocycle, but its recurrent signed source/transport balance is still viable.

---

## 15. Updated oblique global-lock frontier

The genuine-oblique recurrent branch must now satisfy simultaneously

\[
\boxed{
\mathfrak v_\vartheta
+\varepsilon_E
\frac{3\sqrt2}{5}
\lambda G_qP(\operatorname{tr}Q)\sin2\vartheta
=m_3,
}
\]

\[
\boxed{
D_Bm_3=\Pi_3^{prod}+\Pi_3^{rel},
\qquad
\langle\Pi_3^{prod}+\Pi_3^{rel}\rangle=0,
}
\]

and the M17-064--066 local recharge/hysteresis constraints.

The remaining OGLHG problem is therefore no longer a tensor-dimensionality problem. It is a compatibility problem between a finite list of scalar ledgers.

---

## 16. Next target — put the l=3 lock on the same kappa-flux ledger as M5-685

M5-685 weights zero crossings with the amplification factor

\[
a=\exp\int\kappa.
\]

M17-068 provides a material scalar observable

\[
m_3=\mathfrak v_\vartheta-\mathfrak n_\vartheta
\]

with exact material derivative

\[
D_Bm_3=\Pi_3^{prod}+\Pi_3^{rel}.
\]

The next useful calculation is to lift `m_3` into the same `(kappa,theta)` transport density/current used in M5-685 and derive its exact weighted zero-level flux equation.
That will determine precisely what extra joint correlation, beyond the scalar condition `overline G_Phi(0)<0`, is required to lock the global pressure octupole to the hysteretic crossing ensemble.

This is the **l=3 Hysteresis Flux Lift (L3HFL)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
