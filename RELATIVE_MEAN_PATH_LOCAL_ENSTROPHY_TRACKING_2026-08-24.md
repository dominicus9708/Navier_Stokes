# Relative-Mean Path Local-Enstrophy Tracking — 2026-08-24

Status: **CORE-TRACKING GAP REDUCED WITHOUT FOLLOWING A MAXIMUM-VORTICITY MATERIAL LABEL / GLOBAL REGULARITY NOT PROVED.**

`GALILEAN_RELATIVE_MEAN_ACCELERATION_AUDIT_2026-08-24.md` leaves one important issue: the self-consistent relative-mean path

\[
\dot a=m_\phi
\]

need not coincide with the path of a maximum-vorticity point.

It is unnecessary to prove such coincidence. For ancient compactness and recurrence it is enough to retain a fixed amount of **local vorticity mass** near the moving path. If that mass is lost, the exact localized enstrophy identity forces one of the already typed stretching/transport/viscous actions to pay for the loss.

---

## 1. Normalized vorticity equation

On a fixed inertial first-hitting scaling write

\[
\partial_s\Omega
+(U\cdot\nabla)\Omega
=S\Omega
+\nu\Delta\Omega,
\qquad
\nabla\cdot U=0.
\]

Set

\[
e=\frac12|\Omega|^2.
\]

Then

\[
\boxed{
\partial_se+U\cdot\nabla e
=
\Omega^TS\Omega
+\nu\Delta e
-\nu|\nabla\Omega|^2.
}
\]

The first-hitting history also supplies

\[
\|\Omega\|_\infty\le1.
\]

---

## 2. Self-consistent relative-mean path

Let

\[
\phi_a(y,s)
=
\Phi\!\left(\frac{y-a(s)}R\right)
\]

with fixed normalized radius `R`, and define the weighted velocity mean

\[
m(s)
=
\frac{\int\phi_aUdy}{\int\phi_ady}.
\]

Choose

\[
\boxed{a_s=m(s).}
\]

Set the relative velocity

\[
v=U-m.
\]

Then

\[
\phi_s=-m\cdot\nabla\phi.
\]

---

## 3. Exact moving local-enstrophy identity

Define

\[
E_\phi(s)
=
\int\phi_a e\,dy
=
\frac12\int\phi_a|\Omega|^2dy.
\]

Differentiating and integrating transport/diffusion by parts gives

\[
\boxed{
\begin{aligned}
E_\phi'
+\nu\int\phi_a|\nabla\Omega|^2dy
={}&
\int\phi_a\Omega^TS\Omega\,dy\\
&+
\int e\,v\cdot\nabla\phi_a\,dy\\
&+
\nu\int e\,\Delta\phi_a\,dy.
\end{aligned}
}
\]

There is no term involving the absolute drift `m`.

Define

\[
\mathcal I_\phi
:=\int\phi_a\Omega^TS\Omega,
\]

\[
\mathcal F_\phi
:=\int e\,v\cdot\nabla\phi_a,
\]

\[
\mathcal V_{bd,\phi}
:=\nu\int e\,\Delta\phi_a,
\]

and

\[
\mathcal D_\phi
:=\nu\int\phi_a|\nabla\Omega|^2.
\]

Then

\[
\boxed{
E_\phi'
=
\mathcal I_\phi
+
\mathcal F_\phi
+
\mathcal V_{bd,\phi}
-
\mathcal D_\phi.
}
\]

This is the core-tracking analogue of the moving relative-velocity ledger.

---

## 4. Fixed loss or rebuild forces fixed action

For an interval `I=[s_0,s_1]`,

\[
E_\phi(s_1)-E_\phi(s_0)
=
\int_I
(\mathcal I_\phi+\mathcal F_\phi+\mathcal V_{bd,\phi}-\mathcal D_\phi)ds.
\]

Therefore if

\[
|E_\phi(s_1)-E_\phi(s_0)|\ge\delta_E>0,
\]

then necessarily

\[
\boxed{
\int_I
\left(
|\mathcal I_\phi|
+|\mathcal F_\phi|
+|\mathcal V_{bd,\phi}|
+\mathcal D_\phi
\right)ds
\ge\delta_E.
}
\]

Hence at least one payer has action at least `delta_E/4`.

The payers have existing interpretations:

1. `I_phi`: local vortex-stretching / I-lane rebuild;
2. `F_phi`: material crossing relative to the mean path / `T_mat`;
3. `V_bd,phi`: viscous boundary leakage;
4. `D_phi`: local derivative/palinstrophy action.

Thus loss or creation of a fixed local vorticity packet is not a quiet change of coordinates.

---

## 5. Terminal packet seed

First-hitting analyticity gives a terminal thick core. For fixed constants `r_*` and `c_*>0`, after choosing `R` to contain that core,

\[
\boxed{
E_\phi(0)\ge z_*>0.
}
\]

Initialize the relative-mean path at the terminal core center:

\[
a(0)=X_j^{norm}.
\]

Consider the preceding first-hitting checkpoint in the same stage normalization.

There are two possibilities.

### A. Packet retention

\[
E_\phi(s_{j-1})\ge\theta z_*
\]

for a fixed `0<theta<1` after allowing the fixed one-step scaling factor `q^{-1/2}` in the comparison.

Then the earlier checkpoint contains a nontrivial local vorticity packet within the same moving mean frame. It is not necessary that this packet contain the global maximum.

### B. Packet loss/rebuild

\[
E_\phi(s_{j-1})<\theta z_*.
\]

Then

\[
|\Delta E_\phi|\ge (1-\theta)z_*
\]

up to the fixed `q` scaling adjustment, and the preceding action inequality forces an order-one stretching/transport/viscous payment during that stage.

Thus every stage either propagates a nontrivial packet backward in the mean frame or enters an already typed active branch.

---

## 6. Why this is better than tracking a maximum point

A maximum-vorticity point is not a material label and may switch between nearby structures. Requiring a continuous maximum path would create an artificial branch-selection problem.

The local-enstrophy observable is stable under such switching:

\[
\boxed{
\text{maximum changes identity but local vorticity mass persists}
\Longrightarrow
\text{same retained packet branch}.
}
\]

Only a genuine loss/replacement of local vorticity mass activates the action ledger.

This removes a DSD-specific risk of mistaking `which point is the maximum` for a dynamical degree of freedom.

---

## 7. Consequence for the Galilean compactness bridge

On a long corridor where

- relative Campanato remains bounded around the self-consistent mean path;
- drift acceleration is bounded by the exact relative-mean identity;
- pressure oscillation is controlled;
- the four local-enstrophy actions remain below their fixed turnover/rebuild thresholds;

one obtains a chain of retained local vorticity packets in the accelerated frame.

Thus the ancient limit extracted in that frame remains nontrivial without requiring

\[
\text{mean path} = \text{maximum-vorticity path}.
\]

If retention fails infinitely often, each failure contributes fixed action to one of the existing I/T/H/viscous ledgers.

The remaining issue is then an **aggregate summability/time-budget comparison**, not pointwise core tracking.

---

## 8. Relation to no-T center nesting

The existing first-hitting maximum centers still satisfy the no-T nesting estimate

\[
|X_{j+1}-X_j|\lesssim r_j.
\]

That result remains useful for identifying a single candidate physical singular point.

However the compactness frame need not be tied pointwise to those maximum centers. The relative-mean packet chain supplies a second, Galilean-safe center construction.

A mismatch between the two constructions is harmless while both retain nontrivial local vorticity mass in comparable natural neighborhoods; if the neighborhoods separate enough that one loses the packet, the local-enstrophy identity charges the separation to crossing/rebuild.

---

## 9. Remaining quantitative target

The next closure is now finite and explicit:

\[
\boxed{
\text{show that infinitely many fixed packet-loss/rebuild actions cannot fit inside the late first-hitting budget without activating H/T or violating the finite-stage upper-time ledger.}
}
\]

Equivalently, prove eventual packet retention on a pure no-H/T corridor.

This can use the already existing terminal natural-block persistence/rebuild trichotomy and the historical-shell forgetting machinery.

Status: **THE GALILEAN CORE-TRACKING PROBLEM NO LONGER REQUIRES A MAXIMUM-VORTICITY TRAJECTORY. LOCAL ENSTROPHY ALONG THE SELF-CONSISTENT MEAN PATH EITHER RETAINS A NONTRIVIAL PACKET OR PAYS A FIXED STRETCHING/MATERIAL/DIFFUSIVE/DERIVATIVE ACTION. THE REMAINING ISSUE IS AGGREGATE BUDGET CLOSURE OF REPEATED PACKET LOSS. GLOBAL REGULARITY REMAINS UNPROVED.**