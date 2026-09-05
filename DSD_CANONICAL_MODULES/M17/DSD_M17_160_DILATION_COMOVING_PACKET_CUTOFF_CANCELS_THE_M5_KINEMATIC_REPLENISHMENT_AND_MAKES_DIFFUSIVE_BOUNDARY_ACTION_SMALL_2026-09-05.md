# DSD M17-160 — A dilation-comoving packet cutoff cancels kinematic replenishment and makes diffusive boundary action small

Date: 2026-09-05  
Canonical ID: **M17-160**

Status: **BOUNDARY-ACTION REFINEMENT / M5-564 CORRECTLY SHOWS THAT A FIXED SIMILARITY SHELL CAN BE REPLENISHED AT ORDER ONE BY PURE KINEMATIC DILATION, SO FIXED-SHELL BOUNDARY FLUX CANNOT BE CHARGED AS PHYSICAL TURNOVER. THE M17 OU PACKET IS DIFFERENT: CENTER THE PACKET ON A MATERIAL TRAJECTORY AND CHOOSE A CUTOFF WHOSE RADIUS GROWS EXACTLY LIKE `L(tau)=L0 exp(tau/2)`. THEN `(partial_tau + (z/2)·grad)chi=0` IDENTICALLY. THE BASE SIMILARITY DILATION IS ALREADY BUILT INTO THE OU SEMIGROUP AND PRODUCES NO CUTOFF ACTION. THE ONLY VORTICITY LOCALIZATION REMAINDERS ARE RESIDUAL-VELOCITY TRANSPORT, STRAIN, AND VISCOUS CUTOFF COMMUTATORS. ON A RELATIVE-THICK BOUNDED-`kappa` PACKET, CACCIoppoli/ELLIPTIC CONTROL MAKES THE VISCOUS COMMUTATOR `O(L0^-1)` RELATIVE TO PACKET `L2` MASS; REMOTE TYPE-I VELOCITY AND THE QUIET STRAIN LEDGER MAKE THE OTHER INTERIOR TERMS `o(1)`. HENCE STRONG FIXED-LAG FORGETTING CANNOT BE PAID BY PURE DILATION OR BY A QUIET THICK DIFFUSIVE BOUNDARY. IT MUST EXIT TO NEARBY MASS MULTIPLICITY/RELATIVE-THINNESS, UNBOUNDED `kappa`, A CRITICAL SPACETIME BURST, OR A TRUE DOMAIN/INTERFACE EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Translated remote packet equation

Use the M17-155 material center `p_j(tau)` and normalized vorticity packet

\[
V_j(z,\tau)
=
\frac{W(p_j(\tau)+z,\theta_j+\tau)}{a_j}.
\]

Then

\[
\boxed{
\partial_\tau V_j
=
\mathcal L_{OU}V_j
-\delta U_j\cdot\nabla V_j
+\Sigma_jV_j,
}
\]

where

\[
\mathcal L_{OU}=\Delta-\frac12z\cdot\nabla-1,
\]

and

\[
\delta U_j(z,\tau)
:=U(p_j+z,\theta_j+\tau)-U(p_j,\theta_j+\tau).
\]

---

## 2. Dilation-comoving cutoff

Choose a fixed radial cutoff `chi` with

\[
\chi=1\text{ on }B_1,
\qquad
\chi=0\text{ outside }B_2.
\]

For a parameter `L0>>1`, define

\[
L(\tau):=L_0e^{\tau/2},
\]

and

\[
\boxed{
\chi_{L_0}(z,\tau)
:=
\chi\left(\frac{z}{L(\tau)}\right).
}
\]

Since

\[
\frac{L'}L=\frac12,
\]

we have exactly

\[
\boxed{
\left(
\partial_\tau+\frac12z\cdot\nabla
\right)
\chi_{L_0}=0.
}
\]

Thus the cutoff is transported by the **pure similarity dilation**.

This is the key difference from a fixed similarity shell.

---

## 3. Exact localized OU equation

Let

\[
f_j:=\chi_{L_0}V_j.
\]

Using the product rule for `L_OU` and the exact cancellation above,

\[
\boxed{
\begin{aligned}
(\partial_\tau-\mathcal L_{OU})f_j
={}&
-\chi_{L_0}\delta U_j\cdot\nabla V_j
+\chi_{L_0}\Sigma_jV_j\\
&-2\nabla\chi_{L_0}\cdot\nabla V_j
-(\Delta\chi_{L_0})V_j.
\end{aligned}
}
\]

There is **no order-one kinematic dilation cutoff term**.

In particular M5-564's fixed-shell dilation replenishment is already part of the base OU flow and cannot be reused to pay the present remainder.

---

## 4. Size of the cutoff derivatives

On every fixed `|tau|<=T`,

\[
L(\tau)\asymp_TL_0.
\]

Hence

\[
\boxed{
|\nabla\chi_{L_0}|
\le\frac{C_T}{L_0},
\qquad
|\Delta\chi_{L_0}|
\le\frac{C_T}{L_0^2}.
}
\]

The transition collar is the dilation-comoving annulus

\[
L(\tau)\lesssim|z|\lesssim2L(\tau).
\]

For fixed `T,L0`, this remains inside the same remote shell for all sufficiently large `R_j` provided

\[
L_0e^{T/2}=o(R_j).
\]

---

## 5. Bounded `kappa` gives Caccioppoli control of the collar gradient

On the bounded CE-H potential branch,

\[
\Delta V_j=\kappa_jV_j,
\qquad
|\kappa_j|\le K_0.
\]

A standard cutoff multiplication gives on nested collars

\[
\boxed{
\int_{A_{L_0}}|\nabla V_j|^2
\le
C(K_0,T)
\int_{A_{L_0}^+}|V_j|^2.
}
\]

If the relative-thick fixed-fraction packet remains non-multiplicity dominated on the enlarged collar, its normalized mass obeys

\[
\boxed{
\int_{A_{L_0}^+}|V_j|^2
\le C_T
\|f_j(0)\|_2^2.
}
\]

Failure of this comparison is exactly the nearby-mass / relative-thin / multiplicity exit.

---

## 6. Diffusive cutoff action is `O(L0^-1)`

Using Sections 4--5,

\[
\begin{aligned}
\|2\nabla\chi_{L_0}\cdot\nabla V_j\|_2
&\le
\frac{C_T}{L_0}
\|\nabla V_j\|_{L^2(A_{L_0})},\\
\|(\Delta\chi_{L_0})V_j\|_2
&\le
\frac{C_T}{L_0^2}
\|V_j\|_{L^2(A_{L_0})}.
\end{aligned}
\]

Therefore, over a fixed lag `T`,

\[
\boxed{
\int_0^T
\left\|
2\nabla\chi_{L_0}\cdot\nabla V_j
+(\Delta\chi_{L_0})V_j
\right\|_2d\tau
\le
\frac{C_T}{L_0}
\|f_j(0)\|_2
}
\]

up to the stated collar-mass comparability constant.

Thus this action can be made arbitrarily small by choosing `L0` large **before** taking the remote limit.

---

## 7. Residual drift is small

Remote Type-I velocity gives

\[
\sup_{|z|\le2L(\tau)}|\delta U_j|
\to0
\]

for fixed `T,L0` as `R_j->infinity`.

With the bounded-potential collar gradient estimate,

\[
\boxed{
\int_0^T
\|\chi_{L_0}\delta U_j\cdot\nabla V_j\|_2d\tau
=o_j(1)
\|f_j(0)\|_2.
}
\]

---

## 8. Quiet strain action is small

The M17-142 spacetime ledger gives

\[
\int_0^T\int_{packet}|\Sigma_j|^2
\to0.
\]

Relative-thick normalized packet bounds imply

\[
\boxed{
\int_0^T
\|\chi_{L_0}\Sigma_jV_j\|_2d\tau
=o_j(1)
\|f_j(0)\|_2.
}
\]

---

## 9. Combine with the OU forgetting tax

M17-159 says strong fixed-lag forgetting below

\[
\eta_{OU}(T,K_0)
\]

requires an order-one Duhamel action.

But on the present branch, after first choosing `L0` large and then `j` large, the total action in Sections 6--8 is arbitrarily small.

Therefore

\[
\boxed{
\text{strong fixed-lag forgetting is impossible}
}
\]

on the quiet relative-thick bounded-`kappa`, bounded-collar-mass branch.

---

## 10. Exact surviving exits

The strong mass-genealogy exit of M17-158 is further reduced to

\[
\boxed{
G_{mass}^{strong}
\Longrightarrow
G_{nearby\ mass/multiplicity}
\lor
G_{relative-thin/nodal}
\lor
G_{\kappa,\infty}
\lor
H_{1,crit}^{spacetime}
\lor
G_{domain/interface}.
}
\]

Pure similarity dilation is **not** an additional exit here; it is exactly canceled by the dilation-comoving packet gauge.

---

## 11. DSD audit

1. M5-564 remains correct for fixed similarity shells.
2. The present cutoff is deliberately not fixed: it follows the base dilation and therefore removes only kinematic replenishment, not physical residual transport.
3. The `O(L0^-1)` boundary estimate requires normalized mass control on an enlarged collar. Failure is retained as a nearby-mass/multiplicity exit.
4. `L0` is chosen large but fixed before the remote limit; one does not identify an infinite packet with one finite shell.
5. The result closes strong forgetting only on the relative-thick bounded-collar branch.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
