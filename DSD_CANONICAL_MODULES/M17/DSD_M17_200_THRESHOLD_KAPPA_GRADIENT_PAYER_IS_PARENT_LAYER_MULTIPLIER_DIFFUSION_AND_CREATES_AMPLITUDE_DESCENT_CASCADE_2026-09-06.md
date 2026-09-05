# DSD M17-200 — Threshold kappa-gradient payment is parent-layer multiplier diffusion and creates an amplitude-descent cascade

Date: 2026-09-06  
Canonical ID: **M17-200**

Status: **NESTED-CUTOFF REDUCTION / THE M17-196 THRESHOLD CHARGE `B_kappa = int chi' exp(2kappa) rho^3 |grad kappa|^2` IS SUPPORTED ON A FIXED POSITIVE-AMPLITUDE COLLAR. CHOOSE A SLIGHTLY LOWER-AMPLITUDE PARENT CUTOFF `tilde chi` THAT IS IDENTICALLY ONE ON `supp chi'`. THEN `B_kappa[chi] <= C D_kappa[tilde chi]`. THUS THE THRESHOLD MULTIPLIER-GRADIENT PAYER IS NOT A NEW KIND OF CHARGE; IT IS THE SAME M5-687 MULTIPLIER-DIFFUSION CHARGE VIEWED IN THE NEXT LOWER AMPLITUDE LAYER. REPEATED USE PRODUCES AN AMPLITUDE-DESCENT CASCADE WHOSE ONLY GENUINELY NEW TERMINAL ESCAPES ARE LOW-AMPLITUDE/NODAL OR INTERFACE/COMPONENT TRANSITIONS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Child cutoff and threshold charge

Let `chi(rho)` be the M5-683 high-amplitude cutoff. Its multiplier-gradient collar charge is

\[
\boxed{
B_\kappa[\chi]
=\int\chi'(\rho)e^{2\kappa}\rho^3|\nabla\kappa|^2dy.
}
\]

Assume the transition collar is contained in

\[
\boxed{
a_-\le\rho\le a_+}
\]

with fixed

\[
0<a_-<a_+<\infty.
\]

---

## 2. Parent cutoff

Choose another smooth monotone cutoff `tilde chi` with lower activation threshold so that

\[
\boxed{
\widetilde\chi(\rho)=1
\quad\text{for every }\rho\in\operatorname{supp}\chi'.
}
\]

Define the parent-layer multiplier-diffusion charge

\[
\boxed{
D_\kappa[\widetilde\chi]
:=\int\widetilde\chi e^{2\kappa}\rho^2|\nabla\kappa|^2dy.
}
\]

---

## 3. Exact domination

On the support of `chi'`,

\[
\rho\le a_+,
\qquad
\widetilde\chi=1.
\]

Therefore

\[
\begin{aligned}
B_\kappa[\chi]
&\le
\|\chi'\|_\infty a_+
\int_{\operatorname{supp}\chi'}
 e^{2\kappa}\rho^2|\nabla\kappa|^2dy\\
&\le
\|\chi'\|_\infty a_+
D_\kappa[\widetilde\chi].
\end{aligned}
\]

Hence

\[
\boxed{
B_\kappa[\chi]
\le C_{\chi,a_+}D_\kappa[\widetilde\chi].
}
\]

No derivative comparison, quotient estimate, or new PDE theorem is needed.

---

## 4. Interpretation

If the child high-amplitude multiplier-diffusion charge is paid mainly by `B_kappa`, that payment has not disappeared.
It has moved into the multiplier-diffusion charge of a slightly larger amplitude layer.

Thus

\[
\boxed{
D_\kappa[\chi_j]
\xrightarrow{\text{threshold }B_\kappa}
D_\kappa[\chi_{j+1}],
}
\]

where `chi_{j+1}` activates at a lower amplitude than `chi_j`.

The correct geometry is therefore an **amplitude-descent cascade**, not an independent threshold-diffusion sink.

---

## 5. Finite nested atlas and terminal branches

For any finite family of positive thresholds

\[
a_0>a_1>\cdots>a_N>0,
\]

choose nested cutoffs so each parent equals one on the preceding transition collar.
Repeated threshold-gradient payment can then be propagated downward through the finite hierarchy.

It must eventually do one of the following:

1. be paid by bulk palinstrophy/strain architecture at some positive amplitude layer;
2. be paid by high-`kappa` amplitude replenishment/current segregation;
3. cross a component/interface boundary;
4. continue toward amplitudes where no fixed positive lower cutoff remains.

The fourth case is precisely the low-amplitude/nodal frontier, where scalar quotient `kappa` itself loses the uniform high-amplitude regularity used by M5-683.

Thus

\[
\boxed{
B_\kappa\text{-dominant escape}
\Longrightarrow
G_{bulk}
\lor G_{replenish}
\lor G_{interface}
\lor G_{low\ amplitude/nodal}.
}
\]

---

## 6. DSD audit

### Audit A — infinite cutoff cascade
No claim is made that one may pass to infinitely many thresholds with uniform constants. The result is a finite-level reduction; the low-amplitude limit is retained as an explicit terminal branch.

### Audit B — calling parent `D_kappa` a new payment
Rejected. It is the same multiplier-diffusion descriptor on a larger retained set.

### Audit C — nodal extrapolation
No scalar `kappa` formula is extrapolated through `rho=0`.

---

## 7. Updated threshold frontier

The genuinely distinct regular threshold branch is now mainly

\[
\boxed{
\text{high-}kappa\text{ upward amplitude replenishment}
}

plus component/interface turnover.

The multiplier-gradient collar itself is a nested-layer form of the already known positive diffusion charge.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
