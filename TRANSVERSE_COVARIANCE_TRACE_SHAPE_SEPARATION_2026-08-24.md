# Transverse Covariance Trace / Shape Separation — 2026-08-24

Status: **EXACT SIZE-VERSUS-ANISOTROPY SPLIT / TEMPORAL THICKNESS REBUILD COST IDENTIFIED / GLOBAL REGULARITY NOT PROVED.**

This note complements `TRANSVERSE_REMOTE_STRAIN_COVARIANCE_GATE_2026-08-24.md`. The purpose is to determine whether an active transverse trace-free strain can evade the shape ledger simply by making the packet covariance size `q_perp` small during the action-carrying part of a stage.

The answer is structural: `D` drives transverse **shape**, while transverse **size** is controlled by a different scalar ledger. A collapse/rebuild of size therefore cannot be attributed for free to the same `D` channel.

---

## 1. Exact localized covariance equation

Use

\[
Q'=A_fQ+QA_f^T+2\nu I+\mathcal R_Q.
\]

Relative to the tracked vorticity direction `xi`, let

\[
P=I-\xi\otimes\xi,
\]

\[
Q_\perp=PQP=q_\perp P+E_\perp,
\qquad
q_\perp=\frac12\operatorname{tr}(PQP),
\]

with

\[
\operatorname{tr}E_\perp=0.
\]

For the symmetric affine strain write

\[
\Sigma_f
=a\,\xi\otimes\xi
+\xi\otimes b+b\otimes\xi
-\frac a2P
+D,
\]

where

\[
D=PDP,
\qquad
\operatorname{tr}D=0.
\]

Let

\[
h=PQ\xi.
\]

Projector motion, antisymmetric affine rotation, non-affine/local velocity, cutoff/source moments, and any part not written explicitly below are collected in scalar/tensor residuals.

---

## 2. Exact transverse size equation

Take one half of the transverse trace of the covariance equation. The symmetric affine contribution satisfies

\[
\frac12\operatorname{tr}_\perp
(\Sigma_fQ+Q\Sigma_f)
=
-aq_\perp
+\langle D,E_\perp\rangle_F
+b\cdot h.
\]

The isotropic bulk diffusion contributes

\[
\frac12\operatorname{tr}_\perp(2\nu I)=2\nu.
\]

Hence the exact scalar form is

\[
\boxed{
q_\perp'
=
-aq_\perp
+\langle D,E_\perp\rangle_F
+b\cdot h
+2\nu
+\mathcal R_q.
}
\]

Here `R_q` contains the transverse trace of projector-motion, antisymmetric/cross-plane, local/non-affine, cutoff, and localized source terms.

---

## 3. Exact transverse shape equation

The transverse trace-free projection is

\[
\boxed{
E_\perp'
=2q_\perp D+\mathcal R_\perp.
}
\]

The bulk diffusion term disappears exactly:

\[
\operatorname{dev}_\perp(2\nu I)=0.
\]

Therefore the two ledgers have complementary roles:

\[
\boxed{
\begin{array}{ccl}
q_\perp &:& \text{packet transverse size / thickness},\\
E_\perp &:& \text{packet transverse anisotropy / ribbon shape}.
\end{array}
}
\]

---

## 4. Why transverse D cannot hide by shrinking q for free

If the packet is nearly transverse-isotropic,

\[
|E_\perp|_F\le\varepsilon q_\perp,
\]

then

\[
|\langle D,E_\perp\rangle_F|
\le
\varepsilon |D|_Fq_\perp.
\]

Thus the trace-free transverse strain `D` has only an `epsilon`-suppressed direct effect on the scalar size ledger while its leading shape forcing remains

\[
2q_\perp D.
\]

In particular, in a shape-persistent corridor `D` cannot simply drive `q_perp -> 0` and thereby switch off its own covariance forcing without assistance from the separate terms

\[
\boxed{
-aq_\perp,
\quad b\cdot h,
\quad 2\nu,
\quad \mathcal R_q,
\quad \text{or prior large }E_\perp.
}
\]

Those mechanisms are already distinguishable as longitudinal stretch/contraction, tilt/cross-covariance, viscous rebuild, local/non-affine/cutoff turnover, or shape turnover.

---

## 5. Positive-middle specialization

For the **full** aligned positive-middle strain with `xi ~= e3`,

\[
a=s_3\ge0.
\]

Hence the scalar affine term is

\[
-aq_\perp\le0.
\]

So coherent positive-middle stretching contracts transverse covariance size rather than rebuilding it.

If, during the same interval,

\[
|E_\perp|_F\le\varepsilon q_\perp,
\qquad
|b\cdot h|+|\mathcal R_q|
\le r_q,
\]

then

\[
\boxed{
q_\perp'
\le
(-a+\varepsilon|D|_F)q_\perp
+2\nu+r_q.
}
\]

Therefore a packet that becomes very thin under positive-middle deformation and is nevertheless Taylor-thick again at the next first-hitting endpoint must recover its size through

1. isotropic viscous spreading `2 nu`;
2. tilt/cross-covariance transfer;
3. local/non-affine/cutoff/source action;
4. or a prior order-one anisotropy episode.

It cannot be rebuilt solely by the same trace-free `D` while staying shape-small.

---

## 6. Finite rebuild inequality

Let `s_* < s_1` and suppose

\[
q_\perp(s_*)=q_{thin},
\qquad
q_\perp(s_1)=q_{thick}>q_{thin}.
\]

Integrating the exact scalar equation gives

\[
\boxed{
\begin{aligned}
q_{thick}-q_{thin}
&=
-\int_{s_*}^{s_1}a q_\perp ds
+\int_{s_*}^{s_1}\langle D,E_\perp\rangle ds\\
&\quad+
\int_{s_*}^{s_1}b\cdot h\,ds
+2\nu(s_1-s_*)
+\int_{s_*}^{s_1}\mathcal R_qds.
\end{aligned}
}
\]

On the positive-middle shape-small lane,

\[
-aq_\perp\le0,
\qquad
|\langle D,E_\perp\rangle|
\le\varepsilon |D|q_\perp.
\]

Thus a fixed rebuild

\[
q_{thick}-q_{thin}\ge\Delta q_*>0
\]

forces the quantitative alternative

\[
\boxed{
\Delta q_*
\le
\varepsilon\int |D|q_\perp ds
+\int|b\cdot h|ds
+2\nu\Delta s
+\int|\mathcal R_q|ds.
}
\]

This is the precise cost of the temporal-thickness loophole.

---

## 7. Interpretation with the existing persistence/rebuild notes

The repository already contains:

- a terminal natural-block packet persistence versus I/V rebuild trichotomy;
- a finite material-flux-change/palinstrophy gate;
- oriented-flux persistence budgets.

The scalar covariance identity shows exactly where those mechanisms must enter the new transverse route.

If an endpoint Taylor-thick packet is also thick during the remote `D` action, the shape/projective covariance gate applies.

If it is thin during most of that action but thick again at the endpoint, the finite rebuild inequality forces one of

\[
\boxed{
\text{viscous rebuild}
\lor
\text{tilt/cross transfer}
\lor
\text{non-affine/boundary/source turnover}
\lor
\text{prior anisotropy}.
}
\]

The first three are precisely the kinds of I/V/T/H costs already tracked elsewhere; the fourth returns to the shape ledger.

What is still missing is a sharp numerical comparison showing that these rebuild terms cannot repeatedly pay the required `Delta q_*` on every surviving stage.

---

## 8. Current transverse remote-H reduction

The active remote transverse branch is now organized as

\[
\boxed{
\begin{aligned}
D_{rem}\text{ active}
\Longrightarrow\;&
\text{thick action time}
\to
\text{shape/projective gate}\\
&\lor\\
\text{thin action time}
\to
\text{finite covariance rebuild cost}\\
&\lor\\
\text{near/local compensation}
\to
\text{residual branch}.
\end{aligned}
}
\]

This does not close the branch numerically, but it removes the possibility that `q_perp -> 0` is a cost-free way to make `2 q_perp D_rem` disappear.

Status: **TRANSVERSE SIZE AND TRANSVERSE SHAPE NOW HAVE SEPARATE EXACT LEDGERS. TRACE-FREE REMOTE STRAIN CANNOT BOTH REMAIN SHAPE-INVISIBLE AND MAKE THE PACKET THIN FOR FREE. A THIN-THEN-THICK ESCAPE REQUIRES VISCOUS, TILT, NON-AFFINE/BOUNDARY, OR PRIOR-ANISOTROPY REBUILD ACTION. GLOBAL REGULARITY REMAINS UNPROVED.**