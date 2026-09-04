# DSD M17-062 — Principal slant DSAIG reduces to an exact local-viscous versus global-l=3 scalar lock

Date: 2026-09-04
Canonical ID: **M17-062**

Status: **INTERNAL PRINCIPAL GLOBAL-OCTUPOLE LOCK REDUCTION / AFTER M17-061, THE ONLY UNIFORMLY RECURRENT PRINCIPAL-SLANT SURVIVOR HAS ZERO LOCAL KAPPA-RHO^2 PAYER-OCTUPOLE MISMATCH. THE EXACT DSAIG PRESSURE THIRD JET STILL SPLITS INTO A POISSON TRACE/PARTICULAR PIECE AND THE GLOBAL STF HARMONIC L=3 PIECE. IN THE PRINCIPAL NODAL GAUGE `q_2=q_3=q_23=0`, SO `Sigma_33=partial_3U_3=G_3` AND `partial_2Sigma_33=0`. BECAUSE `p=P e_1` AND THE FORBIDDEN TENSOR `E_Q` IS OFF-DIAGONAL, M17-051'S PARTICULAR PRESSURE TENSOR HAS ZERO FORBIDDEN PROJECTION. THEREFORE THE FULL PERPENDICULAR DSAIG BALANCE IS EXACTLY `E_Q:V_p=M_3`, WHERE `M_3=E_Q:N_harm`. DIVIDING BY `P` ELIMINATES SLANT AMPLITUDE AND GIVES `v_*:=E_Q:TF_h[e_1 dot grad_h Delta Sigma_h]=m_3:=M_3/P`. IN COMPONENTS `v_*=±sqrt2 partial_1 Delta Sigma_12`. M17-054 THEN IMPLIES THE SAME TWO-CHANNEL GLOBAL MOMENT LAW FOR THIS PURELY LOCAL VISCOUS SCALAR: `D_B v_*=Pi_3^prod+Pi_3^rel`, WITH RECURRENT MEAN ZERO FOR THE RIGHT-HAND SIDE. THUS THE RECURRENT PRINCIPAL BRANCH HAS BEEN REDUCED TO A SINGLE SCALAR LOCAL/GLOBAL LOCK; LOCAL POISSON TRACE SCREENING AND LOCAL PAYER-OCTUPOLE SCREENING ARE BOTH SILENT IN THE FORBIDDEN DIRECTION. THIS IS NOT YET A CONTRADICTION BECAUSE `partial_1 Delta Sigma_12` CAN BE NONZERO EVEN THOUGH THE LOWER JET `partial_1Sigma_12=0`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Principal recurrent input

Use the principal frame

\[
Q=\operatorname{diag}(q_1,q_2),
\qquad
p=P e_1,
\qquad
P\ne0.
\]

Choose

\[
E_Q
=\varepsilon_E\frac1{\sqrt2}
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

M17-061 proves that every uniformly recurrent principal-slant branch satisfies

\[
\boxed{X_-=X_+=0}
\]

and therefore

\[
\boxed{\mathfrak o_{loc}=0}
\]

for the local `kappa rho^2` payer-octupole mismatch.

This does not yet set the pressure third jet to zero.

---

## 2. Exact pressure split at third order

M17-051/M17-053 give the exact decomposition of the pressure third derivative into

\[
\boxed{
\text{Poisson trace/particular part}
\quad+\quad
\text{STF harmonic }l=3\text{ part}.
}
\]

The DSAIG tensors are

\[
N_{part}
=\frac{6\lambda}{5}
TF_h\left[
 p\otimes\nabla_h\Sigma_{33}
+\nabla_h\Sigma_{33}\otimes p
\right]
\]

and

\[
N_{harm}
=TF_h[p\lrcorner\mathcal H],
\qquad
\mathcal H=STF_3(\nabla^3P).
\]

At the core there is no additional independent pressure-third-jet descriptor: the trace part plus STF part exhaust the symmetric third derivative.

---

## 3. Principal nodal geometry kills the forbidden particular-pressure projection

Use the nodal gauge from M17-059--061:

\[
q_2=q_3=0.
\]

Principal slant gives

\[
q_{23}=0.
\]

The vertical velocity is

\[
U_3=G(q,x_3,\theta).
\]

Hence

\[
\Sigma_{33}=\partial_3U_3
=G_q q_3+G_3
=G_3
\]

at the node.

Differentiate horizontally in the `e_2` direction:

\[
\begin{aligned}
\partial_2\Sigma_{33}
&=\partial_2(G_q q_3+G_3)\\
&=G_{qq}q_2q_3
+G_q q_{23}
+G_{3q}q_2.
\end{aligned}
\]

All three terms vanish, so

\[
\boxed{\partial_2\Sigma_{33}=0.}
\]

Since `p=P e_1`, only the `e_2` component of `grad_h Sigma_33` contributes to the off-diagonal `E_Q` contraction.
Therefore

\[
\boxed{E_Q:N_{part}=0.}
\]

Thus the explicit local pressure-source-gradient channel is silent in the forbidden principal direction.

---

## 4. Full perpendicular DSAIG balance

M17-044 gives the exact dynamic alignment condition

\[
P_{Q_0}^\perp(V_p-N_p)=0,
\]

with

\[
V_p=TF_h[(p\cdot\nabla_h)\Delta\Sigma_h].
\]

At the core

\[
N_p=N_{part}+N_{harm}.
\]

Contract with the unit perpendicular direction `E_Q`.
Section 3 gives zero particular share, hence

\[
\boxed{
E_Q:V_p
=E_Q:N_{harm}.
}
\]

Define

\[
\boxed{M_3:=E_Q:N_{harm}.}
\]

Then

\[
\boxed{E_Q:V_p=M_3.}
\]

This is the exact principal global-lock equation.

---

## 5. Normalize by the slant magnitude

Since

\[
p=P e_1,
\]

we have

\[
V_p
=P\,TF_h[\partial_1\Delta\Sigma_h].
\]

Define the local normalized viscous mismatch

\[
\boxed{
v_*
:=\frac{E_Q:V_p}{P}
=E_Q:TF_h[\partial_1\Delta\Sigma_h].
}
\]

M17-054 defines

\[
\boxed{m_3:=\frac{M_3}{P}.}
\]

Therefore DSAIG becomes simply

\[
\boxed{v_*=m_3.}
\]

All slant-amplitude growth has disappeared.

---

## 6. Component form

Because `E_Q` is the Frobenius-unit off-diagonal direction,

\[
E_Q:A
=\varepsilon_E\sqrt2\,A_{12}
\]

for every symmetric horizontal matrix `A`.

The trace-free operation does not change the off-diagonal component.
Thus

\[
\boxed{
v_*
=\varepsilon_E\sqrt2\,\partial_1\Delta\Sigma_{12}.
}
\]

Since

\[
\Sigma_{12}=\phi_{12},
\]

also

\[
\boxed{
v_*
=\varepsilon_E\sqrt2\,\partial_1\Delta\phi_{12}.
}
\]

This is a completely local fifth-derivative scalar of the horizontal velocity potential.

---

## 7. Lower-jet alignment does not force v_* = 0

M17-060 gives

\[
\boxed{\phi_{112}=\partial_1\Sigma_{12}=0}
\]

at the principal nodal core.

But

\[
\partial_1\Delta\Sigma_{12}
=\Delta(\partial_1\Sigma_{12})
\]

samples second spatial derivatives of that lower-jet alignment defect.
A smooth function may vanish at a point while its Laplacian there is nonzero.

Therefore

\[
\boxed{\partial_1\Sigma_{12}=0}
\]

does **not** imply

\[
\boxed{v_*=0.}
\]

This is the remaining local-viscous escape.

---

## 8. Global moment law transfers directly to the local viscous scalar

M17-054 gives

\[
\boxed{
D_Bm_3
=\Pi_3^{prod}+\Pi_3^{rel}.
}
\]

Because the exact DSAIG lock is

\[
v_*=m_3,
\]

we obtain

\[
\boxed{
D_Bv_*
=\Pi_3^{prod}+\Pi_3^{rel}.
}
\]

Thus the local fifth-derivative viscous scalar is forced to evolve exactly like the normalized global STF pressure-moment mismatch.

This is a genuine local/global compatibility law.

---

## 9. Recurrent mean law

On a compact uniformly recurrent principal-slant branch, `v_*` is bounded and recurrent.
Hence

\[
\boxed{
\left\langle
\Pi_3^{prod}+\Pi_3^{rel}
\right\rangle=0.
}
\]

This is the same recurrence obligation as M17-054, now reinterpreted as the no-drift condition for one explicit local viscous scalar.

No additional independent mean condition has appeared; DSD audit therefore counts this as one ledger, not two.

---

## 10. DSD analysis

The principal branch has undergone three successive descriptor eliminations:

\[
\boxed{
\text{local payer octupole}
\to0,
}
\]

\[
\boxed{
\text{local pressure trace mismatch}
\to0,
}
\]

leaving

\[
\boxed{
\text{local viscous scalar }v_*
\equiv
\text{global harmonic scalar }m_3.
}
\]

The remaining pressure escape is therefore no longer tensor-valued in the forbidden channel. It is a single signed scalar cocycle.

---

## 11. DSD audit

### Audit A — treating local payer octupole and pressure-source particular tensor as the same object
Rejected. They are distinct descriptors; both happen to be silent here for different structural reasons.

### Audit B — leaving a fictitious higher pressure-third-jet remainder
Rejected. At a point, symmetric pressure third derivatives split exactly into their trace-determined and STF parts.

### Audit C — inferring v_* = 0 from phi112 = 0
Rejected. Pointwise lower-jet silence does not imply Laplacian silence.

### Audit D — counting `v_*` and `m_3` as two recurrence ledgers
Rejected. DSAIG identifies them exactly on the retained branch.

### Audit E — proof status
PGOLG reduces the principal branch to one local/global scalar lock but does not exclude it.

---

## 12. Updated principal survivor

The recurrent principal-slant branch must satisfy

\[
\boxed{
\begin{aligned}
X_-&=X_+=0,\\
\mathfrak o_{loc}&=0,\\
E_Q:N_{part}&=0,\\
v_*&=m_3,\\
D_Bv_*&=\Pi_3^{prod}+\Pi_3^{rel},\\
\langle\Pi_3^{prod}+\Pi_3^{rel}\rangle&=0.
\end{aligned}
}
\]

Thus its only remaining DSAIG perpendicular freedom is the one scalar `v_*=m_3`.

---

## 13. Next target — viscous scalar recurrence versus analytic alignment

The sharpest next question is whether

\[
v_*=\varepsilon_E\sqrt2\partial_1\Delta\Sigma_{12}
\]

can remain recurrently nonzero while the lower alignment constraints

\[
\Sigma_{12}=0,
\qquad
\partial_1\Sigma_{12}=0
\]

hold at every material nodal time in the same frozen principal frame.

This requires differentiating the lower alignment constraints materially and spatially far enough to determine whether `v_*` is an independent fifth-jet degree of freedom or is forced into a finite-jet degeneration hierarchy.

This is the **Principal Viscous Scalar Jet Gate (PVSJG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
