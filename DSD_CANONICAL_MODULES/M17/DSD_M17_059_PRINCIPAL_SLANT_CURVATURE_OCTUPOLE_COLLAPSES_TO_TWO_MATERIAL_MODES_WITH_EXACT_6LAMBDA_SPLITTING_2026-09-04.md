# DSD M17-059 — Principal-slant curvature octupole collapses to two material modes with exact 6-lambda splitting

Date: 2026-09-04
Canonical ID: **M17-059**

Status: **INTERNAL REDUCED OCTUPOLE PROJECTION DYNAMICS / ON THE PRINCIPAL-SLANT SUBBRANCH OF M17-058, CHOOSE THE FROZEN PRINCIPAL FRAME `Q=diag(q_1,q_2)`, `p=(P,0)`, `u=e_1`, AND `E_Q=±(e_1 tensor e_2+e_2 tensor e_1)/sqrt2`. THE KAPPA-GRADIENT OCTUPOLE PROJECTION VANISHES IDENTICALLY. THE VORTICITY-CURVATURE SHARE OF THE FORBIDDEN LOCAL OCTUPOLE DEPENDS ONLY ON THE SINGLE COMBINATION `Xi=(8q_1+7q_2)H_112+2Pq_1H_123+2q_2H_233`, WHERE `H=grad^3q`; ALL OTHER THIRD-q JETS DROP OUT OF THIS DSAIG PROJECTION. USING A LOCAL NODAL GAUGE WITH `grad q=0`, DIFFERENTIATING THE EXACT MATERIAL LABEL LAW `D_Bq=mathscr H(q,x_3,theta)` GIVES THREE SCALAR THIRD-JET EQUATIONS. AFTER INCLUDING THE KNOWN MATERIAL MULTIPLIERS `D_BQ=(kappa-3/2)Q` AND `D_BP=3lambda P`, `Xi` SPLITS INTO TWO EIGENMODES `X_-=(8q_1+7q_2)H_112` AND `X_+=2Pq_1H_123+2q_2H_233` WITH HOMOGENEOUS RATES `mu_- = 2kappa-G_3-7/2-3lambda` AND `mu_+ = 2kappa-G_3-7/2+3lambda`. THEIR RATE DIFFERENCE IS EXACTLY `6lambda`. THE INHOMOGENEOUS FORCING IS NOT A NEW ARBITRARY FOURTH-q JET: IN THIS PRINCIPAL FRAME THE `mathscr H_{q3}` TERMS VANISH AND THE REMAINING FORCING IS AN EXPLICIT CONTRACTION OF THE SECOND VELOCITY JET WITH THE NODAL q-HESSIAN; USING `U_h=grad_h phi` AND `U_3=G(q,x_3)`, IT REDUCES TO THREE THIRD-phi JETS. THUS THE PRINCIPAL-SLANT LOCAL OCTUPOLE IS A TWO-MODE MATERIAL SYSTEM FORCED BY THE THIRD VELOCITY-POTENTIAL JET, NOT A SEVEN-DIMENSIONAL FREE THIRD-q JET. NO SIGN CONTRADICTION FOLLOWS YET. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Principal-slant frame

Use the M17-058 principal-slant class. Because both the normalized Hessian shape and the slant azimuth are material invariants, choose once and for all the horizontal principal frame

\[
\boxed{
Q=\begin{pmatrix}q_1&0\\0&q_2\end{pmatrix},
\qquad
p=(P,0),
\qquad
P\ne0.
}
\]

Set

\[
\boxed{u=\widehat p=e_1.}
\]

For a Frobenius-unit trace-free tensor perpendicular to `Q_0`, choose the orientation

\[
\boxed{
E_Q
=\varepsilon_E\frac1{\sqrt2}
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\varepsilon_E\in\{+1,-1\}.
}
\]

M17-058 gives

\[
\boxed{\mathfrak o_\kappa=0}
\]

on this branch.

Hence the local payer octupole mismatch is entirely the vorticity-curvature / third-q-jet contribution.

---

## 2. Third-q jet and trace relation

Write

\[
\boxed{H_{ijk}:=\partial_i\partial_j\partial_k q.}
\]

It is fully symmetric.

The horizontal semilinear trace equation from M17-058 is

\[
H_{2 11}+H_{2 22}+H_{2 33}=0.
\]

Thus

\[
\boxed{H_{222}=-H_{112}-H_{233}.}
\]

This relation will remove the only extra component that appears in the raw STF trace subtraction.

---

## 3. Exact principal-slant contraction of the curvature octupole

M17-057 gives

\[
T^{(W)}_{ijk}
=\frac{\kappa_0}{3}
\left(
 A_{ai}B_{ajk}
+A_{aj}B_{aik}
+A_{ak}B_{aij}
\right),
\]

with

\[
B_{aij}=J_{a\alpha}H_{\alpha ij}.
\]

M17-058 gives

\[
A=JQL_p.
\]

Contract the STF tensor with `u=e_1` and `E_Q`.
The direct symmetric-tensor term is

\[
\frac{\sqrt2\,\varepsilon_E\kappa_0}{3}
(2q_1+q_2)H_{112}.
\]

The three-dimensional STF trace correction contributes

\[
\frac{2\sqrt2\,\varepsilon_E\kappa_0}{15}
\left(
-q_1H_{112}
+Pq_1H_{123}
-q_2H_{222}
\right).
\]

Use

\[
H_{222}=-H_{112}-H_{233}.
\]

After collecting terms,

\[
\boxed{
\mathfrak o_W
=
\varepsilon_E\frac{\sqrt2\,\kappa_0}{15}
\Xi,
}
\]

where

\[
\boxed{
\Xi
:=(8q_1+7q_2)H_{112}
+2Pq_1H_{123}
+2q_2H_{233}.
}
\]

Therefore seven nominally free third-q-jet components have collapsed to **one scalar combination in the forbidden principal-slant octupole projection**.

---

## 4. Local nodal gauge for material differentiation

The horizontal streamfunction is defined up to an additive function of `(x_3,theta)`.
Along a local filament written as a graph over `x_3`, choose this gauge so that

\[
\boxed{q=0}
\]

on the filament.

Because

\[
\nabla_hq=0
\]

there, differentiation along the filament then gives

\[
\boxed{q_3=0}
\]

at the marked nodal point.

Thus in this local gauge

\[
\boxed{\nabla q=0}
\]

at the node.

This gauge does not change `Q`, `p`, or any third derivative carrying at least one horizontal index, including `H_112,H_123,H_233`.

---

## 5. Differentiate the material label law three times

M17-013 gives

\[
\boxed{
D_Bq=\mathscr H(q,x_3,\theta),
}
\]

where we use `mathscr H` to avoid confusion with the third-q tensor `H`.

Let

\[
V:=B=U+\frac12y
\]

be the similarity material velocity and

\[
L:=\nabla V.
\]

For a scalar `q`, direct commutator differentiation gives at a point with `grad q=0`

\[
\boxed{
\begin{aligned}
D_BH_{ijk}
={}&\partial_{ijk}\mathscr H
-L_{ai}H_{ajk}
-L_{aj}H_{aik}
-L_{ak}H_{aij}\\
&-(\partial_{ij}V_a)q_{ak}
-(\partial_{ik}V_a)q_{aj}
-(\partial_{jk}V_a)q_{ai}.
\end{aligned}
}
\]

The term containing `partial_{ijk}V_a q_a` vanishes because `grad q=0` in the nodal gauge.

---

## 6. Third derivative of the label RHS

At `grad q=0`, for any component not equal to `333`,

\[
\boxed{
\partial_{ijk}\mathscr H
=\mathscr H_qH_{ijk}
+\mathscr H_{q3}
\left(
q_{ij}\delta_{k3}
+q_{ik}\delta_{j3}
+q_{jk}\delta_{i3}
\right).
}
\]

M17-013 gives

\[
\boxed{
\mathscr H_q
=\kappa-G_3-\frac12,
}
\]

where `G_3` is the partial derivative of the vertical velocity law `G(q,x_3,theta)` at fixed `q`.

At the regular nodal core, M17-010 gives

\[
\boxed{
L
=\operatorname{diag}
\left(
\lambda+\frac12,
\lambda+\frac12,
-2\lambda+\frac12
\right).
}
\]

Hence a third-q component with `r` vertical derivative slots has homogeneous rate

\[
\boxed{
\mu_r^{(H)}
=\kappa-G_3-2-3\lambda(1-r).
}
\]

Explicitly,

\[
\begin{aligned}
\mu_0^{(H)}&=\kappa-G_3-2-3\lambda,\\
\mu_1^{(H)}&=\kappa-G_3-2,\\
\mu_2^{(H)}&=\kappa-G_3-2+3\lambda.
\end{aligned}
\]

---

## 7. Principal alignment removes the label-Hessian forcing from the three relevant modes

The nodal Hessian has

\[
Q=\operatorname{diag}(q_1,q_2)
\]

and

\[
q_{h3}=-Qp=(-q_1P,0).
\]

Therefore

\[
q_{12}=0,
\qquad
q_{23}=0.
\]

The explicit `mathscr H_{q3}` terms in the three relevant equations are:

- `H_112`: none;
- `H_123`: `mathscr H_{q3} q_12=0`;
- `H_233`: `2 mathscr H_{q3} q_23=0`.

Thus the semilinear label RHS contributes **no inhomogeneous second-Hessian source** to these three principal-slant octupole modes.

Only the velocity-second-jet commutator remains.

---

## 8. Exact forcing of H112, H123, H233

Let

\[
q_{33}=d.
\]

The full nodal Hessian in the chosen gauge is

\[
\boxed{
\nabla^2q
=
\begin{pmatrix}
q_1&0&-q_1P\\
0&q_2&0\\
-q_1P&0&d
\end{pmatrix}.
}
\]

Because second derivatives of the linear similarity drift vanish, `partial^2 V=partial^2 U`.

The three forcing terms are

\[
\boxed{
\begin{aligned}
\mathcal F_{112}
={}&-q_2\,\partial_{11}U_2
-2q_1\,\partial_{12}U_1
+2q_1P\,\partial_{12}U_3,\\
\mathcal F_{123}
={}&q_1P\,\partial_{12}U_1
-d\,\partial_{12}U_3
-q_2\,\partial_{13}U_2
-q_1\,\partial_{23}U_1
+q_1P\,\partial_{23}U_3,\\
\mathcal F_{233}
={}&2q_1P\,\partial_{23}U_1
-2d\,\partial_{23}U_3
-q_2\,\partial_{33}U_2.
\end{aligned}
}
\]

Now use

\[
U_h=\nabla_h\phi,
\qquad
U_3=G(q,x_3,\theta).
\]

At the nodal gauge point `grad q=0`, principal alignment gives

\[
\partial_{12}U_3=G_q q_{12}=0,
\qquad
\partial_{23}U_3=G_q q_{23}=0.
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal F_{112}
&=-(2q_1+q_2)\phi_{112},\\
\mathcal F_{123}
&=q_1P\phi_{112}-(q_1+q_2)\phi_{123},\\
\mathcal F_{233}
&=2q_1P\phi_{123}-q_2\phi_{233}.
\end{aligned}
}
\]

Thus the inhomogeneous dynamics is controlled by only three third derivatives of the horizontal velocity potential.

---

## 9. Material laws for the geometric coefficients

M17-010/M17-014 give

\[
\boxed{
D_Bq_i
=\left(\kappa-\frac32\right)q_i,
\qquad i=1,2,
}
\]

because the entire nodal Hessian `Q` changes by a common scalar multiplier.

M17-024 gives

\[
\boxed{D_BP=3\lambda P.}
\]

Define

\[
\boxed{
X_-:=(8q_1+7q_2)H_{112}
}
\]

and

\[
\boxed{
X_+:=2Pq_1H_{123}+2q_2H_{233}.
}
\]

Then

\[
\boxed{\Xi=X_-+X_+.}
\]

---

## 10. Exact two-mode dynamics

Using Sections 6--9, the homogeneous rates combine exactly to

\[
\boxed{
\mu_-
=2\kappa-G_3-\frac72-3\lambda,
}
\]

and

\[
\boxed{
\mu_+
=2\kappa-G_3-\frac72+3\lambda.
}
\]

Therefore

\[
\boxed{
D_BX_-
=\mu_-X_-+\mathcal S_-,
}
\]

\[
\boxed{
D_BX_+
=\mu_+X_++\mathcal S_+,
}
\]

where

\[
\boxed{
\mathcal S_-
=(8q_1+7q_2)\mathcal F_{112}
}
\]

and

\[
\boxed{
\mathcal S_+
=2Pq_1\mathcal F_{123}
+2q_2\mathcal F_{233}.
}
\]

The rate splitting is

\[
\boxed{
\mu_+-\mu_-=6\lambda.
}
\]

Thus repeated-plane strain does not merely change the slant magnitude; it is exactly the internal hyperbolic splitting between the two curvature-octupole modes.

---

## 11. Symmetric two-component form

Define

\[
\boxed{
\Delta X:=X_+-X_-,
\qquad
\mu:=2\kappa-G_3-\frac72.
}
\]

Then

\[
\boxed{
D_B\Xi
=\mu\Xi+3\lambda\Delta X
+\mathcal S_-+\mathcal S_+,
}
\]

and

\[
\boxed{
D_B\Delta X
=\mu\Delta X+3\lambda\Xi
+\mathcal S_+-\mathcal S_-.
}
\]

Equivalently,

\[
\boxed{
D_B
\begin{pmatrix}\Xi\\\Delta X\end{pmatrix}
=
\begin{pmatrix}
\mu&3\lambda\\
3\lambda&\mu
\end{pmatrix}
\begin{pmatrix}\Xi\\\Delta X\end{pmatrix}
+
\begin{pmatrix}
\mathcal S_-+\mathcal S_+\\
\mathcal S_+-\mathcal S_-
\end{pmatrix}.
}
\]

The local principal-slant curvature octupole is therefore a forced **two-channel scalar system**, not a generic seven-component third-jet problem.

---

## 12. Consequence for recurrent slant

Uniform recurrent nonzero slant gives

\[
\boxed{\langle\lambda\rangle=0.}
\]

from M17-024.

Therefore the two homogeneous Lyapunov exponents have equal long-time means:

\[
\boxed{
\langle\mu_+\rangle
=\langle\mu_-\rangle
=
\left\langle2\kappa-G_3-\frac72\right\rangle.
}
\]

This is **not** a contradiction.
The instantaneous splitting `±3lambda` may be substantial while its recurrent mean vanishes.

Any closure must therefore use the signed forcing pair `(S_-,S_+)`, the global pressure moment, or an additional recurrence constraint; average strain splitting alone is insufficient.

---

## 13. Relation to the local octupole mismatch

On principal slant,

\[
\mathfrak o_\kappa=0.
\]

Hence

\[
\boxed{
\mathfrak o_{loc}
=
\varepsilon_E\frac{\sqrt2\kappa_0}{15}\Xi.
}
\]

The local forbidden octupole share is therefore controlled by `Xi` alone.

The orthogonal companion `Delta X` is invisible instantaneously to the DSAIG projection but feeds `Xi` dynamically through the `3lambda Delta X` term.

This is a useful DSD descriptor split:

- `Xi`: visible forbidden octupole channel;
- `Delta X`: hidden companion channel required for its material evolution.

---

## 14. DSD audit

### Audit A — claiming all seven H components are dynamically relevant
Rejected. Only one combination is visible; its dynamics needs one hidden companion, yielding a two-mode system.

### Audit B — dropping STF trace subtraction
Avoided. The coefficients `8,7,2,2` arise only after the full 3D STF trace correction and the semilinear trace relation.

### Audit C — confusing q-gauge with a physical restriction
Avoided. The nodal gauge changes only additive `(x_3,theta)` normalization; all displayed horizontal jet descriptors are unchanged.

### Audit D — ignoring commutators with the material velocity
Avoided. They are exactly the source of the velocity-second-jet forcing `F_ijk`.

### Audit E — treating `mathscr H_q3` as a generic new forcing
Rejected on principal slant. The relevant Hessian entries `q_12` and `q_23` vanish, so these terms cancel exactly.

### Audit F — claiming mean lambda zero closes the mode split
Rejected. It equalizes mean homogeneous rates but does not remove instantaneous exchange or forcing.

### Audit G — proof status
ROPDG sharply reduces the principal branch but does not yet exclude it.

---

## 15. Updated principal-slant frontier

\[
\boxed{
R_{principal}^{H_3}
\Longrightarrow
R_{2mode}^{\Xi,\Delta X}
\ \lor\
T_{nodal/rank}.
}
\]

The two-mode survivor must simultaneously satisfy

1. the M17-025/M17-044 strain-alignment hierarchy;
2. the local octupole relation `o_loc proportional kappa_0 Xi`;
3. the M17-053--054 global l=3 pressure-moment recurrence;
4. M17-018/022 negative-payer constraints;
5. M5-685 label-area hysteresis.

---

## 16. Next target — force the two-mode sources through the slanted strain-alignment law

The source pair is already reduced to

\[
\boxed{
(\phi_{112},\phi_{123},\phi_{233}).
}
\]

M17-025 gives an independent exact relation between the slant-direction third `phi` jet and the fixed nodal anisotropy `Q_0`.
On principal slant this should eliminate at least one of these three source components and identify which combination is already paid for by the scalar `G_q-1` compensation.

The next calculation is the **Principal-Slant Source Alignment Gate (PSSAG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
