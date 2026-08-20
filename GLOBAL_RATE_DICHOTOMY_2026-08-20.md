# Global Rate Dichotomy — 2026-08-20

Overall status: **ACTIVE PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note combines the global stage clock with the local `P_V` action and moving-core variance estimates. The resulting conclusion is that an eventual non-`H`, non-`T` survivor must live at a Type-I first-hitting rate; the faster/slower normalized-rate branches are routed back to `H/T`.

---

## 1. Fixed action per geometric stage

For

\[
W_j=q^jW_0,
\qquad q>1,
\]

let `I_j` be the normalized-time interval for the first-hitting step `W_j -> qW_j`, and

\[
L_j=|I_j|.
\]

Since

\[
\int_{I_j}a(s)ds=\frac12\log q=:A_q,
\]

the mean normalized scale rate is

\[
\bar a_j=\frac{A_q}{L_j}.
\]

---

## 2. Lower stage-length bound from the P_V speed limit

From `GLOBAL_PV_ACTION_LINK_2026-08-20.md`,

\[
\frac{\|\mathcal V\|_2}{\|\Sigma\|_2}\le C_V.
\]

If the `P_V` branch carries a fixed amount `a_V>0` of projective action on each stage, then

\[
\boxed{
L_j\ge L_V:=a_V/C_V>0.
}
\]

Thus an eventual pure `P_V` branch cannot have `L_j -> 0`.

Equivalently,

\[
\boxed{
\bar a_j\le A_q/L_V=:a_+.
}
\]

---

## 3. Upper stage-length bound from bounded-radius recurrent variance

The moving-core variance estimate already established on the active route has the form

\[
\frac12V_R'+\nu D_R
=\frac a2V_R+\mathcal F_R,
\]

with weighted Poincare

\[
V_R\le C_PR^2D_R.
\]

On a bounded-radius recurrent core, if material/core turnover `T` is subdominant and the derivative/compactness controls do not fail, persistence through one geometric stage gives

\[
\boxed{
L_j\le L_R\sim R^2/\nu.
}
\]

Therefore

\[
\boxed{
\bar a_j\ge A_q/L_R=:a_->0.
}
\]

Hence an eventual branch avoiding both `H` and `T` and using `P_V` recurrence satisfies

\[
\boxed{
0<a_-\le\bar a_j\le a_+<\infty.
}
\]

---

## 4. Physical duration of one stage

Since `dt=W^{-1}ds` and

\[
W_j\le W(s)\le qW_j
\]

on `I_j`,

\[
\boxed{
\frac{L_j}{qW_j}
\le
\Delta t_j
\le
\frac{L_j}{W_j}.
}
\]

With `L_V <= L_j <= L_R`,

\[
\boxed{
\Delta t_j\asymp W_j^{-1}.
}
\]

If the same non-`H/T` regime persists for all sufficiently large `j`, then

\[
T^*-t_j
=\sum_{k\ge j}\Delta t_k
\asymp
\sum_{k\ge j}W_k^{-1}
\asymp
W_j^{-1}.
\]

Therefore along the first-hitting sequence,

\[
\boxed{
W_j(T^*-t_j)\asymp1.
}
\]

This is a Type-I-size vorticity growth law along the tracked first-hitting sequence.

---

## 5. Global rate dichotomy

The late singular evolution is therefore reduced to two qualitatively different possibilities.

### G-Type-II/compactness-defect side

If `L_j` escapes the bounded interval required above (very long or very short stages, loss of bounded-radius recurrence, loss of derivative compactness, or repeated core replacement), the route returns to

\[
\boxed{H\lor T_{bounded}.}
\]

### G-Type-I/projective side

If `H` and `T` are eventually avoided, the first-hitting stages have

\[
L_j\asymp1,
\qquad
\bar a_j\asymp1,
\qquad
W_j(T^*-t_j)\asymp1,
\]

and the remaining mechanism is a bounded-radius positive-rate projective recurrence driven by full-NS structure `P_V`.

Thus the non-`H/T` survivor is no longer an arbitrary blow-up-rate scenario.

---

## 6. Ancient-solution bridge

Known Type-I blow-up theory relates local Type-I singularities to non-trivial bounded mild ancient solutions satisfying corresponding Type-I scale bounds. A relevant primary reference is:

Dallas Albritton and Tobias Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, arXiv:1811.00502.

The present first-hitting rate estimate alone is not yet sufficient to invoke that theorem. To make the bridge rigorous for the tracked DSD-assisted core, one still has to verify uniform bounds on the local Type-I scale quantities (local energy, cubic velocity, pressure, and dissipation) after recentering/rescaling.

The existing moving-variance, near/remote-pressure, bounded-radius, and derivative-control estimates are designed to supply exactly these inputs, but the implication has not yet been written as a complete lemma.

---

## 7. New principal theorem target

Prove the **DSD first-hitting Type-I compactness lemma**:

If a late first-hitting sequence avoids `H` and `T`, and the `P_V` recurrent core remains bounded in normalized radius with the existing variance/pressure controls, then after recentering and parabolic rescaling it admits a non-trivial bounded mild ancient limit satisfying the local Type-I bounds.

Then the global problem splits cleanly into

\[
\boxed{
\text{singularity}
\Longrightarrow
(H\lor T)_{infinitely\ often}
\quad\lor\quad
\text{nontrivial Type-I ancient }P_V\text{ limit}.
}
\]

The next local/global bridge should then use the additional `P_V`, `G_Q`, max-mid-defect, and projective constraints to rule out this restricted ancient limit, rather than attempting to solve the unrestricted 3D ancient-solution conjecture.

Status: **EVENTUAL NON-H/T SURVIVOR REDUCED TO TYPE-I FIRST-HITTING RATE. NEXT GLOBAL BRIDGE = VERIFY LOCAL TYPE-I COMPACTNESS QUANTITIES AND EXTRACT THE RESTRICTED P_V ANCIENT LIMIT.**