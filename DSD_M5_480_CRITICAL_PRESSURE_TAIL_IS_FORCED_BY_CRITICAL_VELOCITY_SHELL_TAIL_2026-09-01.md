# DSD M5-480 — Critical pressure tail is forced by a critical velocity shell tail

Date: 2026-09-01

Status: **TERMINAL-TAIL REDUCTION / FOR THE M5-474 MARKED ANCIENT ELEMENT, `Omega in L2` IMPLIES `V in L6` AND THE PRESSURE IS THE RIESZ TRANSFORM OF `V tensor V`; IF ALL SUFFICIENTLY LARGE DYADIC VELOCITY SHELLS HAVE VANISHING SCALE-CRITICAL `L3` MASS, THEN THE LOCAL, INNER-HARMONIC, AND OUTER-HARMONIC PARTS OF THE PRESSURE ALL HAVE VANISHING CRITICAL `L^(3/2)` OSCILLATION / THEREFORE A NONZERO TERMINAL PRESSURE TAIL CANNOT BE AN INDEPENDENT SURVIVOR: IT FORCES A NONZERO VELOCITY `L3` SHELL TAIL AT SOME COMPARABLE OR INTERMEDIATE SCALE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Terminal velocity class

At the marked terminal time of the M5-474 ancient element,

\[
\Omega(0)\in L^2\cap L^\infty.
\]

Hence

\[
\nabla V(0)\in L^2
\]

and Sobolev gives

\[
\boxed{V(0)\in L^6(\mathbb R^3).}
\]

The pressure is normalized by

\[
\boxed{
P=R_iR_j(V_iV_j)
}
\]

up to an irrelevant function of time.

Since `V^2 in L3`, the global pressure belongs to `L3`, although the scale-critical local pressure quantity is `L^(3/2)`.

---

## 2. Assume all large velocity shell tails vanish

Define

\[
\varepsilon(R)
:=
\sup_{\rho\ge R}
\int_{\rho<|x|<2\rho}|V(x,0)|^3dx.
\]

Assume

\[
\boxed{\varepsilon(R)\to0\qquad(R\to\infty).}
\]

We prove that the critical pressure oscillation on all large annuli also vanishes.

---

## 3. Shell L2 mass is sublinear

On a dyadic annulus `A_r`, Holder gives

\[
\begin{aligned}
\int_{A_r}|V|^2dx
&\le
|A_r|^{1/3}
\left(
\int_{A_r}|V|^3dx
\right)^{2/3}\\
&\le
Cr\,\varepsilon(R)^{2/3}
\end{aligned}
\]

whenever `r>=R`.

Sum dyadic shells from a fixed large `R0` to `R`. Since the radii form a geometric series,

\[
\sum_{2^kR_0\le R}2^kR_0
\lesssim R.
\]

Therefore

\[
\int_{B_R}|V|^2dx
\le C(R_0)+C\varepsilon(R_0)^{2/3}R.
\]

Divide by `R`, then first send `R->infinity` and next `R0->infinity`:

\[
\boxed{
\frac1R\int_{B_R}|V|^2dx\to0.
}
\]

Thus the cumulative terminal kinetic mass is strictly subcritical relative to the `O(R)` critical `1/r` tail scale if all velocity `L3` shell masses vanish.

---

## 4. Pressure decomposition on one large annulus

Fix

\[
A_R:=\{R<|x|<2R\}
\]

and a slightly enlarged annulus

\[
A_R^*:=\{R/2<|x|<4R\}.
\]

Split

\[
P=P_{loc}+P_{in}+P_{out},
\]

where the source `V tensor V` is restricted respectively to

1. `A_R^*`;
2. `|y|<R/2`;
3. `|y|>4R`.

Constants in `P_in,P_out` are irrelevant and will be removed by annular averaging.

---

## 5. Local pressure is controlled by local velocity L3

Calderon--Zygmund boundedness gives

\[
\|P_{loc}\|_{L^{3/2}(A_R)}
\le
C
\|V\otimes V\|_{L^{3/2}(A_R^*)}
=C\|V\|_{L^3(A_R^*)}^2.
\]

Therefore

\[
\boxed{
\int_{A_R}|P_{loc}|^{3/2}dx
\le
C
\int_{A_R^*}|V|^3dx
\le C\varepsilon(R/2)
\to0.
}
\]

---

## 6. Inner harmonic pressure is small after subtracting a constant

For `x in A_R` and `|y|<R/2`, the pressure kernel is smooth at scale `R`.

Subtract the value at one fixed annular point `x_R`. By the mean-value theorem for the degree `-3` pressure kernel,

\[
|K_P(x-y)-K_P(x_R-y)|
\le CR^{-3}
\]

for `x,x_R in A_R` after absorbing the fixed annular diameter into the derivative estimate.

Hence

\[
|P_{in}(x)-P_{in}(x_R)|
\le
CR^{-3}
\int_{B_{R/2}}|V(y)|^2dy.
\]

The sublinear kinetic-mass result gives

\[
\boxed{
\operatorname{osc}_{A_R}P_{in}
=o(R^{-2}).
}
\]

Therefore

\[
\boxed{
\int_{A_R}
|P_{in}-[P_{in}]_{A_R}|^{3/2}dx
=o(1),
}
\]

because `|A_R|~R^3`.

---

## 7. Outer harmonic pressure is also small

For `|y|>4R`, subtract an annular constant. The pressure-kernel gradient has degree `-4`, so

\[
\operatorname{osc}_{A_R}P_{out}
\lesssim
R
\int_{|y|>4R}|y|^{-4}|V(y)|^2dy.
\]

Split the exterior into dyadic shells `A_{2^kR}`, `k>=2`.

The shell `L2` estimate gives

\[
\int_{A_{2^kR}}|V|^2
\le
C(2^kR)\varepsilon(2^kR)^{2/3}
\le
C(2^kR)\varepsilon(4R)^{2/3}.
\]

Thus

\[
\begin{aligned}
\operatorname{osc}_{A_R}P_{out}
&\lesssim
R
\sum_{k\ge2}
(2^kR)^{-4}
(2^kR)
\varepsilon(4R)^{2/3}\\
&\lesssim
R^{-2}
\varepsilon(4R)^{2/3}
\sum_{k\ge2}2^{-3k}.
\end{aligned}
\]

Hence

\[
\boxed{
\operatorname{osc}_{A_R}P_{out}
=o(R^{-2})
}
\]

and therefore

\[
\boxed{
\int_{A_R}
|P_{out}-[P_{out}]_{A_R}|^{3/2}dx
=o(1).
}
\]

---

## 8. Pressure-tail consequence

Combining the three pieces,

\[
\boxed{
\int_{A_R}
|P-[P]_{A_R}|^{3/2}dx
\to0
\qquad(R\to\infty)
}
\]

whenever

\[
\sup_{\rho\ge R}
\int_{A_\rho}|V|^3dx\to0.
\]

Taking the contrapositive,

\[
\boxed{
\limsup_{R\to\infty}
\int_{A_R}|P-[P]_{A_R}|^{3/2}>0
\Longrightarrow
\limsup_{\rho\to\infty}
\int_{A_\rho}|V|^3>0.
}
\]

The velocity scale `rho` need not equal exactly the original pressure radius `R`; it may be a comparable or intermediate dyadic scale.

---

## 9. Updated M5-479 terminal split

The independent pressure terminal is removed:

\[
\boxed{
E_{ratchet}^{ancient}
\Longrightarrow
T_{L3}^{crit}
\lor
H_{terminal\ suitable}^{crit}.
}
\]

Thus only velocity critical occupancy and genuinely dynamical failure of terminal suitable compactness remain.

---

## 10. Firewall

The result is a terminal time-slice pressure reduction. It does not by itself control space-time pressure concentration in the `s<0` blow-down cylinders if terminal suitable compactness fails.

That dynamic branch must be audited separately.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
