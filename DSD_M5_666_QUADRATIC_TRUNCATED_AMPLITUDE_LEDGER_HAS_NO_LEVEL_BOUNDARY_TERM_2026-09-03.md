# DSD M5-666 — The quadratic truncated-amplitude ledger has no amplitude-level boundary term

Date: 2026-09-03

Status: **INTERNAL FIXED-THRESHOLD LEDGER / FOR `N_a=(1/2)int(rho-a)_+^2`, THE CE-H MATERIAL AMPLITUDE EQUATION AND THE PARALLEL ELLIPTIC EIGENFIELD EQUATION GIVE THE EXACT BALANCE `N_a' + (1/2)N_a + a M_a + D_a^(2) = Q_a^(2)` WITH `D_a^(2)=int_{rho>a}|grad rho|^2 + int_{rho>a}rho(rho-a)|grad xi|^2` AND `Q_a^(2)=int_{rho>a}sigma rho(rho-a)` / BECAUSE THE TEST FACTOR VANISHES ON `rho=a`, NO AMPLITUDE-LEVEL SURFACE TERM APPEARS / THIS IS THE BOUNDED TEMPORAL VERSION OF THE M5-656--657 WEIGHTED COMPONENT IDENTITY AND IS NATURALLY COLOCATED WITH THE FIXED-THRESHOLD SHEATH/CROSSING ACTIVITY OF M5-665 / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Quadratic truncated amplitude

For `a>0`, define

\[
q_a:=(\rho-a)_+
\]

and

\[
\boxed{
N_a(\theta)
:=
\frac12\int_{\mathbb R^3}q_a^2dy.
}
\]

Also recall the linear truncated mass

\[
\boxed{
M_a:=\int q_a dy.
}
\]

Since `q_a<=rho` and `E<=Z_*`, `N_a` is bounded on every fixed positive threshold under the compact all-order hull.

---

## 2. Material derivative

On CE-H,

\[
D_B\rho
=(\sigma+\kappa-1)\rho
\]

and

\[
\nabla\cdot B=\frac32.
\]

On the superlevel `rho>a`,

\[
D_B q_a=D_B\rho.
\]

Therefore

\[
D_B\left(\frac12q_a^2\right)
=
q_a D_B\rho.
\]

For an integrable scalar `F`,

\[
\frac d{d\theta}\int Fdy
=
\int D_BFdy
+
\int F\nabla\cdot Bdy.
\]

Hence

\[
\boxed{
N_a'
=
\int_{\rho>a}
q_a(\sigma+\kappa-1)\rho\,dy
+
\frac32N_a.
}
\]

---

## 3. Weighted kappa identity with vanishing boundary factor

The CE-H parallel elliptic equation is

\[
\boxed{
\Delta\rho
=(\kappa+|\nabla\xi|^2)\rho.
}
\]

Equivalently,

\[
\kappa\rho
=
\Delta\rho-ho|\nabla\xi|^2.
\]

Multiply by `q_a=(rho-a)_+` and integrate.

Because `q_a=0` on the regular level boundary `rho=a`, integration by parts gives no boundary term:

\[
\int q_a\Delta\rho
=-\int_{\rho>a}|\nabla\rho|^2dy.
\]

Thus

\[
\boxed{
\int_{\rho>a}
\kappa\rho q_a dy
=
-
\int_{\rho>a}|\nabla\rho|^2dy
-
\int_{\rho>a}\rho q_a|\nabla\xi|^2dy.
}
\]

Define

\[
\boxed{
D_a^{(2)}
:=
\int_{\rho>a}|\nabla\rho|^2dy
+
\int_{\rho>a}\rho(\rho-a)|\nabla\xi|^2dy.
}
\]

Then

\[
\boxed{
\int_{\rho>a}\kappa\rho(\rho-a)dy
=-D_a^{(2)}.
}
\]

---

## 4. Exact temporal ledger

Insert the weighted kappa identity into the material derivative formula:

\[
N_a'
=
\int_{\rho>a}\sigma\rho q_a dy
-
\int_{\rho>a}\rho q_a dy
-
D_a^{(2)}
+
\frac32N_a.
\]

Now

\[
\rho q_a
=(q_a+a)q_a
=q_a^2+aq_a.
\]

Hence

\[
\int\rho q_a
=2N_a+aM_a.
\]

Therefore

\[
N_a'
=
Q_a^{(2)}
-2N_a-aM_a-D_a^{(2)}
+
\frac32N_a,
\]

where

\[
\boxed{
Q_a^{(2)}
:=
\int_{\rho>a}\sigma\rho(\rho-a)dy.
}
\]

Thus

\[
\boxed{
N_a'
+
\frac12N_a
+
aM_a
+
D_a^{(2)}
=
Q_a^{(2)}.
}
\]

This is the exact quadratic truncated-amplitude ledger.

---

## 5. Invariant-average form

On a recurrent invariant component, `N_a` is bounded, so its mean derivative vanishes.

Hence

\[
\boxed{
\langle Q_a^{(2)}\rangle
=
\frac12\langle N_a\rangle
+
a\langle M_a\rangle
+
\langle D_a^{(2)}\rangle.
}
\]

All terms on the right are nonnegative.

For a nontrivial retained high-amplitude population the mean weighted axial production is therefore strictly positive.

---

## 6. Relation to M5-656--657

M5-656--657 used, on one connected component `C_L` of `rho>a`, the elliptic identity

\[
\int_{C_L}\kappa\rho(\rho-a)
=
-
\int_{C_L}|\nabla\rho|^2
-
\int_{C_L}\rho(\rho-a)|\nabla\xi|^2.
\]

The present `D_a^(2)` is the sum of exactly these component deficits over the amplitude superlevel.

Thus M5-666 is not a new independent dissipation; it is the temporal bounded-observable ledger corresponding to the same elliptic component identity.

---

## 7. Why the quadratic choice is better for the current frontier

The linear truncated ledger M5-652 contains the surface quantity

\[
\int_{\rho=a}|\nabla\rho|dS.
\]

The quadratic multiplier `q_a` vanishes on the level set and removes this boundary term completely.

This is useful for M5-665 because the remaining dynamic mechanisms are already localized to a fixed high-amplitude threshold and may involve repeated crossing of that threshold.

The ledger does not double-count the geometric motion of the level surface.

---

## 8. Fixed-threshold carrier lower bounds

For the M5-657 persistent carrier choose the retained fixed threshold

\[
a=a_0.
\]

The fixed carrier ball has

\[
\rho\ge\rho_0>a_0
\]

on a fixed radius.

Therefore there are uniform constants

\[
\boxed{
n_0>0,
\qquad
m_0>0
}
\]

such that

\[
N_{a_0}\ge n_0,
\qquad
M_{a_0}\ge m_0
\]

on every retained persistent event.

M5-657's capacity argument also gives a fixed component contribution

\[
\boxed{
D_{a_0}^{(2)}\ge d_0>0
}
\]

on the corresponding retained component, hence globally as well.

---

## 9. Consequence: fixed-threshold production payer

After invariant averaging,

\[
\boxed{
\langle Q_{a_0}^{(2)}\rangle
\ge
\frac12n_0+a_0m_0+d_0
>0.
}
\]

Thus the recurrent CE-H survivor must carry a **strict fixed-threshold weighted axial-strain production payer** at the same amplitude scale where M5-665 forces repeated crossing/sheath activity.

This aligns the dynamic and elliptic mechanisms on one fixed amplitude layer.

---

## 10. Firewall

The equality remains an energy-type balance.

Positive `Q_a^(2)` can in principle pay the positive damping/deficit terms indefinitely on a recurrent compact state space.

Therefore the ledger alone is not a strict Lyapunov contradiction.

The remaining task is to determine whether the positive-rate force/higher-jet/sheath events of M5-665 force an additional one-sided change in `N_a` or in a related flux-normalized threshold observable that is **not** already contained in `Q_a^(2)`.

---

## 11. Updated target

The static cross-sheet geometry is exhausted.

At the fixed threshold `a0`, the hard branch now has simultaneously

\[
\boxed{
\langle Q_{a_0}^{(2)}\rangle>0
}
\]

and positive-rate activity in

\[
\boxed{
C_{rot}^{force}
\lor
C_{crit}^{higher-jet}
\lor
T_{sheath}^{rho=a_0}.
}
\]

The next calculation should attempt to build a flux-normalized version of `N_{a0}` or a sheet-cell version of the quadratic ledger to test whether one of these event types produces a genuine irreversible decrement.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]