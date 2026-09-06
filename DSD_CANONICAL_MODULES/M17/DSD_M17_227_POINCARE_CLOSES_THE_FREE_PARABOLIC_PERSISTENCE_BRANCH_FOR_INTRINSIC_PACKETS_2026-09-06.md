# DSD M17-227 — Poincare closes the free parabolic persistence branch for intrinsic packets

Date: 2026-09-06  
Canonical ID: **M17-227**

Status: **PERSISTENCE-BRANCH CLOSURE / M17-225 LEFT A FORMAL ALTERNATIVE IN WHICH A BUFFERED INTRINSIC PACKET RETAINS A FIXED FRACTION OF ITS LOCALIZED ENSTROPHY THROUGH A TIME OF ORDER `r_j^2` WITHOUT YET PAYING PALINSTROPHY OR INTERFACE TURNOVER. THAT ALTERNATIVE IS NOT ACTUALLY FREE. FOR THE COMPACTLY SUPPORTED FIELD `F_j=zeta_j W`, SCALE-`r_j` POINCARE GIVES `M_j=||F_j||_2^2 <= C r_j^2 D_j + C N_j`. INTEGRATING OVER A PARABOLIC INTERVAL ON WHICH `M_j >= c M_j(0)` YIELDS `int D_j + r_j^-2 int N_j >= c' M_j(0)`. COMBINED WITH M17-225, BOTH EARLY LOSS AND PERSISTENCE FORCE THE SAME FIXED NORMALIZED PAYMENT. THUS THE INTRINSIC SPECTRAL PACKET CANNOT SURVIVE AS A NO-COST HEAT-TANGENT BRANCH: IT MUST PAY LOCAL PALINSTROPHY, TRANSITION/INTERFACE TURNOVER, OR EXIT THROUGH A LOCAL COEFFICIENT SPIKE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Intrinsic packet notation

Retain the M17-224/225 packet

\[
F_j(y,\theta):=\zeta_j(y,\theta)W(y,\theta),
\]

where `zeta_j` is supported in a ball of radius `C r_j`,

\[
r_j\to0.
\]

Define

\[
M_j(\theta):=\|F_j(\theta)\|_2^2
=\int\zeta_j^2|W|^2dy,
\]

\[
D_j(\theta):=\int\zeta_j^2|\nabla W|^2dy,
\]

and

\[
N_j(\theta)
:=\int_{\operatorname{supp}\nabla\zeta_j}|W|^2dy.
\]

The cutoff satisfies

\[
|\nabla\zeta_j|\le C r_j^{-1}.
\]

---

## 2. Scale-`r_j` Poincare inequality

Because `F_j` is compactly supported in a ball of diameter `O(r_j)`, the ordinary Poincare inequality gives

\[
\boxed{
\|F_j\|_2^2
\le C_P r_j^2\|\nabla F_j\|_2^2.
}
\]

Now

\[
\nabla F_j
=\zeta_j\nabla W+W\otimes\nabla\zeta_j.
\]

Therefore

\[
\begin{aligned}
\|\nabla F_j\|_2^2
&\le2\int\zeta_j^2|\nabla W|^2dy
+2\int|\nabla\zeta_j|^2|W|^2dy\\
&\le2D_j+C r_j^{-2}N_j.
\end{aligned}
\]

Substitution gives the pointwise-in-time coercive estimate

\[
\boxed{
M_j(\theta)
\le
C_1 r_j^2D_j(\theta)
+C_2 N_j(\theta).
}
\]

Equivalently,

\[
\boxed{
D_j(\theta)+r_j^{-2}N_j(\theta)
\ge c r_j^{-2}M_j(\theta).
}
\]

This estimate uses no evolution equation.

---

## 3. Integrate on a persistent parabolic interval

Suppose the M17-225 persistence alternative holds on an interval

\[
I_j=[0,c_pr_j^2]
\]

with

\[
\boxed{
M_j(\theta)\ge c_M M_j(0)
\qquad
\forall\theta\in I_j,
}
\]

for a fixed `c_M>0`.

Integrating the pointwise Poincare estimate gives

\[
\int_{I_j}M_jd\theta
\le
C_1r_j^2\int_{I_j}D_jd\theta
+C_2\int_{I_j}N_jd\theta.
\]

The persistence lower bound gives

\[
\int_{I_j}M_jd\theta
\ge c_pc_Mr_j^2M_j(0).
\]

Hence

\[
\boxed{
\int_{I_j}D_jd\theta
+r_j^{-2}\int_{I_j}N_jd\theta
\ge c_*M_j(0),
}
\]

where `c_*>0` depends only on the fixed cutoff geometry and persistence constants.

Thus persistence itself pays the same parabolically normalized derivative/interface cost as early forgetting.

---

## 4. Combine with M17-225 early-loss gate

M17-225 proved that if the packet loses a fixed fraction of its mass before the end of the parabolic interval, then

\[
\boxed{
\int D_jd\theta
+r_j^{-2}\int N_jd\theta
\ge cM_j(0).
}
\]

M17-227 proves the same lower bound if the packet instead persists.

Therefore the exhaustive dynamical split is no longer

\[
\text{persistence}
\lor
\text{payment}.
\]

It is simply

\[
\boxed{
H_{buffered\ intrinsic\ packet}
\Longrightarrow
H_{local\ palinstrophy/interface\ payment}
\lor
G_{local\ coefficient\ spike}.
}
\]

Here

\[
H_{local\ palinstrophy/interface\ payment}
:
\quad
\int_{I_j}D_jd\theta
+r_j^{-2}\int_{I_j}N_jd\theta
\ge cM_j(0).
\]

---

## 5. Two-sided version

If one uses the symmetric M17-226 corridor

\[
I_j=[-c_pr_j^2,c_pr_j^2]
\]

and

\[
M_j(\theta)\ge c_MM_j(0)
\]

throughout it, the same calculation yields

\[
\boxed{
\int_{-c_pr_j^2}^{c_pr_j^2}D_jd\theta
+r_j^{-2}
\int_{-c_pr_j^2}^{c_pr_j^2}N_jd\theta
\ge c_{**}M_j(0).
}
\]

Consequently the hypothetical no-payment two-sided corridor of M17-226 is empty.

M17-226 remains useful as a directional bookkeeping theorem, but M17-227 supersedes its no-payment branch at the current frontier.

---

## 6. Why no heat-tangent compactness theorem is needed here

The previous frontier anticipated

\[
\text{two-sided persistence}
\to
\text{nonzero heat tangent}
\to
\text{Liouville test}.
\]

M17-227 shows that this route is unnecessarily long on the present compact intrinsic packet.

The scale-matched Poincare inequality already says:

\[
\boxed{
\text{nonzero compact packet for one parabolic lifetime}
\Longrightarrow
\text{order-one normalized gradient/interface action}.
}
\]

Thus an unforced, zero-cost persistent compact packet is impossible before any tangent limit is taken.

A heat tangent may still be useful for classifying the payment branch, but it is no longer required to eliminate a free persistence exit.

---

## 7. Relation to the spectral branch

M17-210--224 reduced the hard whole-shell spectral exit to a buffered intrinsic remote packet.

M17-225 converted early packet loss into local palinstrophy/interface payment.

M17-227 removes the complementary free-persistence alternative.

Hence on the bounded local-coefficient corridor,

\[
\boxed{
G_{tempered\ whole\text{-}shell\ H2/L2\ spectral}
\Longrightarrow
H_{intrinsic\ palinstrophy/interface\ action}.
}
\]

The former spectral/director recycling branch is therefore replaced by a genuine dynamical action branch.

---

## 8. What remains open

The new payment is local and normalized to the packet mass:

\[
\int D_jd\theta
+r_j^{-2}\int N_jd\theta
\gtrsim M_j(0).
\]

This is not yet a contradiction.

The next step is to determine whether repeated intrinsic packet payments can be summed or charged to the existing global/shell palinstrophy, turnover, or derivative-tail ledgers without unlimited reuse of the same action.

The principal audit questions are:

1. can disjoint or bounded-overlap intrinsic packets be selected from the divergent shell stack;
2. can their palinstrophy payments be charged injectively or with bounded multiplicity;
3. does the interface term represent true packet turnover that can be routed to an existing flux/occupancy ledger;
4. can one packet action be recycled across arbitrarily many shell witnesses.

---

## 9. DSD analysis

### 9.1 Static coercivity closes a dynamic-looking branch

The crucial estimate is spatial Poincare, not a new evolution inequality.

The packet lifetime supplies exactly the factor `r_j^2` needed to cancel the Poincare scale.

### 9.2 No double counting yet

M17-227 proves that a payment exists.
It does not yet prove that payments from distinct packets are independent.

The next module must address bounded-overlap charging before summing them.

### 9.3 Scope

The proof uses compact buffered packets.
It does not state that every noncompact heat packet pays the same local cost.

---

## 10. DSD audit

- Poincare is applied to the compact field `zeta_j W`, not to `W` on all space.
- The cutoff-gradient term is exactly the already-tracked transition mass `N_j`.
- The parabolic interval length is what converts `r_j^-2 M_j` into an order-`M_j` action.
- M17-226 is not deleted; its no-payment corridor is simply shown to be empty at the frontier.
- The payment is necessary but not yet globally budgeted.
- No heat-Liouville contradiction is claimed.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
