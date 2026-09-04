# DSD M17-069 — The global l=3 lock has an exact kappa-flux lift; bridging to M5 hysteresis requires a joint crossing covariance

Date: 2026-09-04
Canonical ID: **M17-069**

Status: **INTERNAL l=3 HYSTERESIS FLUX LIFT / M17-068 GIVES A MATERIAL SCALAR `m_3=v_vartheta-n_vartheta` WITH `D_Bm_3=Pi_3^prod+Pi_3^rel`. LIFT THIS OBSERVABLE INTO THE SAME KAPPA-LABEL TRANSPORT USED BY THE M5 AMPLIFICATION FACTOR `a`, WHERE `a'=kappa a` AND `h=kappa'`. DEFINING `F_3(k)=int m_3 a delta(k-kappa)dmu_0`, `G_3(k)=int m_3 h a delta(k-kappa)dmu_0`, AND `S_3(k)=int Pi_3 a delta(k-kappa)dmu_0`, DIRECT DIFFERENTIATION GIVES THE EXACT SOURCEFUL CONTINUITY LAW `partial_theta F_3 + partial_k G_3 = k F_3 + S_3`. AT `k=0`, RECURRENCE GIVES `mean partial_k G_3(0)=mean S_3(0)`. MORE IMPORTANTLY, THE ZERO-CROSSING CURRENT ITSELF IS `G_3(0)=int m_3 h a delta(kappa)dmu_0 = int (v_vartheta-n_vartheta) h a delta(kappa)dmu_0`. M5-685 CONTROLS ONLY THE SCALAR CURRENT `G_Phi(0)=int h a delta(kappa)dmu_0`, WHOSE LONG-TIME MEAN IS NEGATIVE. ON THE POSITIVE SIMPLE-CROSSING MEASURE `dnu_0=a|h|delta(kappa)dmu_0dtheta`, THESE ARE RESPECTIVELY THE MOMENTS OF `sgn h` AND `m_3 sgn h`. THEREFORE THE MISSING BRIDGE IS EXACTLY THE JOINT CROSSING COVARIANCE `Cov_nu0(m_3,sgn h)`; THE NEGATIVE SCALAR HYSTERESIS SIGN ALONE CANNOT DETERMINE THE l=3 CURRENT. THIS CLOSES THE MEASURE-SUBSTITUTION SHORTCUT AND IDENTIFIES THE PRECISE EXTRA CORRELATION NEEDED FOR A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material observables on the marked recurrent ensemble

Use the same label ensemble notation as the M5 kappa-flux ledger.
For every retained material label `lambda`, let

\[
\kappa_\lambda(\theta)
\]

be the CE-H multiplier and define

\[
\boxed{
h_\lambda:=D_B\kappa_\lambda.}
\]

Let the amplification factor be

\[
\boxed{
a_\lambda(\theta)
=\exp\left(\int\kappa_\lambda\,d\theta\right),}
\]

so

\[
\boxed{a_\lambda'=\kappa_\lambda a_\lambda.}
\]

M17-013 identifies this `a` with the reduced label-area Jacobian on the great-circle branch.

For the genuine-oblique DSAIG lock, M17-068 gives

\[
\boxed{
m_{3,\lambda}
=\mathfrak v_{\vartheta,\lambda}
-\mathfrak n_{\vartheta,\lambda},}
\]

with exact material derivative

\[
\boxed{
m_{3,\lambda}'
=\Pi_{3,\lambda},}
\]

where

\[
\boxed{
\Pi_{3,\lambda}
:=\Pi_{3,\lambda}^{prod}
+\Pi_{3,\lambda}^{rel}.
}
\]

---

## 2. Lift the l=3 scalar into kappa-space

Let `dmu_0(lambda)` be the fixed base label measure.
Define the amplification-weighted `l=3` density

\[
\boxed{
F_3(k,\theta)
:=\int
m_{3,\lambda}a_\lambda
\delta(k-\kappa_\lambda)
\,d\mu_0(\lambda).
}
\]

Define its kappa-space current

\[
\boxed{
G_3(k,\theta)
:=\int
m_{3,\lambda}h_\lambda a_\lambda
\delta(k-\kappa_\lambda)
\,d\mu_0(\lambda).
}
\]

Finally define the projected pressure-production/transport source density

\[
\boxed{
S_3(k,\theta)
:=\int
\Pi_{3,\lambda}a_\lambda
\delta(k-\kappa_\lambda)
\,d\mu_0(\lambda).
}
\]

These three quantities live on the same `(k,theta)` state space as the M5 flux ledger.

---

## 3. Exact sourceful continuity equation

Differentiate `F_3`.
Using

\[
m_3'=\Pi_3,
\qquad
a'=\kappa a,
\qquad
\kappa'=h,
\]

and

\[
\partial_\theta\delta(k-\kappa)
=-h\,\partial_k\delta(k-\kappa),
\]

we get

\[
\begin{aligned}
\partial_\theta F_3
={}&\int \Pi_3a\delta(k-\kappa)d\mu_0
+\int m_3\kappa a\delta(k-\kappa)d\mu_0\\
&-\partial_k\int m_3ha\delta(k-\kappa)d\mu_0.
\end{aligned}
\]

On the support of the delta distribution,

\[
\kappa=k.
\]

Therefore

\[
\boxed{
\partial_\theta F_3
+\partial_kG_3
=kF_3+S_3.
}
\]

This is the exact **l=3 kappa-flux transport law**.

---

## 4. Zero-level differential balance

At

\[
k=0
\]

the amplification source term `kF_3` vanishes.
Hence

\[
\boxed{
\partial_\theta F_3(0,\theta)
+\partial_kG_3(0,\theta)
=S_3(0,\theta).
}
\]

If the lifted state is recurrent/bounded so that the long-time average of the total time derivative vanishes, then

\[
\boxed{
\overline{\partial_kG_3(0)}
=\overline{S_3(0)}.
}
\]

This is a derivative-of-current identity.
It does **not** by itself determine the sign of the current value `G_3(0)`.

---

## 5. The M5 scalar current

The M5 amplification-weighted scalar kappa current is

\[
\boxed{
G_\Phi(k,\theta)
:=\int
h_\lambda a_\lambda
\delta(k-\kappa_\lambda)
\,d\mu_0(\lambda).
}
\]

M5-685's surviving hysteresis branch requires

\[
\boxed{
\overline{G_\Phi(0)}<0.
}
\]

Thus amplification-weighted downward zero crossings dominate upward ones in the signed scalar current.

The l=3 current is instead

\[
\boxed{
G_3(0,\theta)
=\int
m_{3,\lambda}h_\lambda a_\lambda
\delta(\kappa_\lambda)
\,d\mu_0.
}
\]

The extra factor `m_3` is essential.

---

## 6. DSAIG converts the l=3 current into a local/global crossing lock

M17-068 gives at every retained oblique core

\[
\boxed{
m_3=\mathfrak v_\vartheta-\mathfrak n_\vartheta.}
\]

Therefore the zero-level l=3 current can be written exactly as

\[
\boxed{
G_3(0,\theta)
=\int
(\mathfrak v_\vartheta-\mathfrak n_\vartheta)
ha\,\delta(\kappa)
\,d\mu_0.
}
\]

Hence the global pressure `l=3` moment and the local viscous/Poisson scalar are not merely compared along one marker; they have identical amplification-weighted crossing currents once DSAIG is imposed.

This is the desired direct bridge between the global pressure lock and the M5 crossing ensemble.

---

## 7. Positive simple-crossing measure

To expose exactly what M5-685 controls, restrict first to simple temporal crossings

\[
\boxed{h\neq0\quad\text{when}\quad\kappa=0.}
\]

Degenerate events are retained as a separate transition class.

Define the positive crossing measure over labels and time by

\[
\boxed{
d\nu_0
:=a|h|\,\delta(\kappa)
\,d\mu_0\,d\theta.
}
\]

Let

\[
s_h:=\operatorname{sgn}h.
\]

Then the time-integrated scalar current is

\[
\boxed{
\int G_\Phi(0,\theta)d\theta
=\int s_h\,d\nu_0.
}
\]

Likewise

\[
\boxed{
\int G_3(0,\theta)d\theta
=\int m_3s_h\,d\nu_0.
}
\]

For an individual label with isolated simple zero times `theta_i`, the delta identity

\[
\delta(\kappa(\theta))
=\sum_i\frac{\delta(\theta-\theta_i)}{|h(\theta_i)|}
\]

shows that `dnu_0` counts crossings with the amplification weight `a`, while `s_h` distinguishes upward and downward direction.

---

## 8. Exact covariance decomposition

Normalize `nu_0` on a long recurrence window to a probability measure, whenever its total mass is nonzero.
Denote expectation and covariance by

\[
\mathbb E_{\nu_0}[\cdot],
\qquad
\operatorname{Cov}_{\nu_0}(\cdot,\cdot).
\]

Then

\[
\boxed{
\mathbb E_{\nu_0}[m_3s_h]
=
\mathbb E_{\nu_0}[m_3]\,
\mathbb E_{\nu_0}[s_h]
+
\operatorname{Cov}_{\nu_0}(m_3,s_h).
}
\]

M5-685 determines the sign of the scalar factor

\[
\boxed{
\mathbb E_{\nu_0}[s_h]<0
}
\]

on its surviving branch.

It does **not** determine either

\[
\mathbb E_{\nu_0}[m_3]
\]

or

\[
\operatorname{Cov}_{\nu_0}(m_3,s_h).
\]

Therefore the sign of the l=3 crossing current cannot be inferred from scalar hysteresis alone.

The missing information is exactly a joint angular/crossing correlation.

---

## 9. The same statement in local DSAIG variables

Since

\[
m_3=\mathfrak v_\vartheta-\mathfrak n_\vartheta,
\]

we have

\[
\boxed{
\operatorname{Cov}_{\nu_0}(m_3,s_h)
=
\operatorname{Cov}_{\nu_0}
(\mathfrak v_\vartheta-\mathfrak n_\vartheta,
\operatorname{sgn}h).
}
\]

M17-068 gives explicitly

\[
\mathfrak n_\vartheta
=-\varepsilon_E
\frac{3\sqrt2}{5}
\lambda G_qP(\operatorname{tr}Q)\sin2\vartheta.
\]

Thus the missing bridge can be decomposed further into

\[
\boxed{
\operatorname{Cov}_{\nu_0}(\mathfrak v_\vartheta,s_h)
-
\operatorname{Cov}_{\nu_0}(\mathfrak n_\vartheta,s_h).
}
\]

No currently established multiplier or sign law fixes either covariance.

---

## 10. Relation to the local payer-octupole at regular oblique crossings

M17-067 shows that a spatially regular genuine-oblique `kappa=0` event is necessarily local-octupole active:

\[
\mathfrak o_{loc}\neq0.
\]

At the zero event,

\[
\mathfrak o_{loc}
=\varepsilon_E\frac{\sqrt2}{15}
\kappa_3P|Q|_F^2\sin2\vartheta.
\]

This adds another crossing observable to the positive measure `nu_0`.
However the scalar M5 current depends on `sgn h`, while the local octupole sign depends on `kappa_3` times the frozen angular orientation.

No identity established so far fixes

\[
\operatorname{sgn}h
\quad\text{from}\quad
\operatorname{sgn}\kappa_3,
\]

or vice versa.

Therefore octupole activation at every regular oblique crossing still does not convert the scalar hysteresis bias into an `l=3` sign theorem.

---

## 11. Global source production cannot be localized by setting kappa(Y)=0

The projected source term `Pi_3^prod` comes from the global STF kernel pairing with

\[
D_BS_P+\frac32S_P.
\]

One contribution to that source is

\[
-\left(\sigma+\kappa-\frac14\right)\rho^2.
\]

At a marked crossing point `Y`, one may have

\[
\kappa(Y)=0.
\]

But `Pi_3^prod` integrates the source architecture over the full spatial variable `y`.
It is invalid to replace the global field `kappa(y)` by the local nodal value `kappa(Y)=0` inside that integral.

Thus no local-zero shortcut removes the global kappa-payer contribution from the `l=3` production channel.

---

## 12. Three different averages are now explicitly separated

The current frontier contains three distinct recurrence/flux statements:

### M5-685 crossing flux

\[
\boxed{
\overline{G_\Phi(0)}<0.
}
\]

This is an amplification-weighted signed **zero-crossing ensemble** statement.

### M17-064 same-marker axial recharge

On a uniformly nonzero-`kappa_3` recurrent oblique marker,

\[
\boxed{
\left\langle
\frac{\partial_3h}{\kappa_3}
\right\rangle_{time}
=\frac12.
}
\]

This is a **same-marker time average**.

### M17-054/M17-068 global l=3 production balance

\[
\boxed{
\langle\Pi_3^{prod}+\Pi_3^{rel}\rangle_{time}=0
}
\]

on a bounded recurrent marked branch.

This is a **global-kernel observable time average**.

These cannot be substituted for one another without a joint invariant/event measure.
M17-069 supplies the first exact lift that places `m_3` on the M5 crossing state space.

---

## 13. DSD analysis

The old apparent gap was between a scalar hysteresis condition and an angular global pressure condition.
The gap is now represented by one explicit probability-theoretic descriptor:

\[
\boxed{
\operatorname{Cov}_{\nu_0}
(m_3,\operatorname{sgn}h).
}
\]

Equivalently, using DSAIG,

\[
\boxed{
\operatorname{Cov}_{\nu_0}
(\mathfrak v_\vartheta-\mathfrak n_\vartheta,
\operatorname{sgn}h).
}
\]

Thus the missing bridge is no longer “some relation between local and global quantities.”
It is a precisely identified joint crossing correlation.

---

## 14. DSD audit

### Audit A — applying the M5 scalar sign directly to G_3
Rejected.
`G_3` contains the additional signed factor `m_3`.

### Audit B — confusing G_3(0) with partial_k G_3(0)
Rejected.
The zero-level continuity equation controls the derivative of current after recurrence, whereas M5-685 supplies the sign of the scalar current value.

### Audit C — replacing event averaging with marker-time averaging
Rejected.
The measures are different and are now written explicitly.

### Audit D — treating regular crossing activation as a sign relation between h and kappa_3
Rejected.
M17-067 gives nonvanishing, not sign locking.

### Audit E — setting the global source kappa to zero because the marked core has kappa=0
Rejected as a local/global substitution error.

### Audit F — claiming a covariance term can be neglected by symmetry
Rejected.
No symmetry theorem establishing that covariance has been proved.

### Audit G — proof status
The scalar/global hysteresis bridge is exact, but the required joint correlation remains unconstrained.

---

## 15. Updated OGLHG frontier

The genuine-oblique branch now has one common kappa-space ledger:

\[
\boxed{
\partial_\theta F_3+\partial_kG_3
=kF_3+S_3,
}
\]

with

\[
\boxed{
G_3(0)
=\int
(\mathfrak v_\vartheta-\mathfrak n_\vartheta)
ha\delta(\kappa)d\mu_0.
}
\]

M5-685 gives

\[
\boxed{
\overline{G_\Phi(0)}<0,
}
\]

but closing the `l=3` lock now requires control of

\[
\boxed{
\operatorname{Cov}_{\nu_0}
(m_3,\operatorname{sgn}h).
}
\]

This is the exact remaining scalar-to-octupole crossing gate.

---

## 16. Next target — can the covariance be constrained by the oblique local recharge equations?

M17-064--066 provide

\[
D_B\kappa_3
=\partial_3h+(2\lambda-1/2)\kappa_3,
\]

and the driven curvature-mode system for `Xi_vartheta`.
M17-067 fixes the nonvanishing local octupole at regular crossings.

The next useful question is whether these local equations constrain the sign or mean of

\[
m_3\operatorname{sgn}h
\]

on the crossing measure, either directly or through a correlation with `kappa_3`, `Xi_vartheta`, or the local pressure tax `n_vartheta`.

If not, the OGLHG path reaches a genuine measure-correlation firewall and the next highest-value work should return to the intrinsic Rank-2 survivor or seek a new conservation law.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
