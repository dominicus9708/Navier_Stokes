# DSD M17-196 — The full M5-688 remainder collapses to palinstrophy-scale and amplitude-threshold gradient charges

Date: 2026-09-06  
Canonical ID: **M17-196**

Status: **FULL-REMAINDER REDUCTION / M5-683/688 USES `R_chi`, WHICH CONTAINS THE EXPLICIT CE-H `R_geom` PLUS THE DERIVATIVE OF THE HIGH-AMPLITUDE CUTOFF. M17-194--195 ALREADY COLLAPSE THE `R_geom` PART TO AMPLITUDE/DIRECTOR GRADIENTS, `D_kappa`, AND THE THRESHOLD COLLAR. THE REMAINING CUTOFF-DERIVATIVE TERM IS EXACTLY A SUM OF `grad rho dot grad kappa` AND `grad rho dot grad sigma` ON THE FIXED AMPLITUDE COLLAR AND IS CONTROLLED BY POSITIVE THRESHOLD GRADIENT CHARGES. CONSEQUENTLY THE FULL M5-688 `R_chi` HAS NO INDEPENDENT HESSIAN, CURL, OR NONLOCAL PRESSURE PAYER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Full M5-683 remainder

M5-683 defines, after pushing the constitutive law to `kappa`-space,

\[
\mathcal R_\chi(k)
=R_{geom}^\chi(k)
-\int\delta(k-\kappa)
\chi'(\rho)\rho^2
\nabla\rho\cdot\nabla(\kappa+\sigma)\,dy.
\]

Integrating with the M5-688 factor `exp(2k)` gives

\[
\boxed{
\mathcal R^{(2)}
=\mathfrak R_{geom}^{(2)}-T_{cut}^{(2)},
}
\]

where

\[
T_{cut}^{(2)}
=\int e^{2\kappa}\chi'(\rho)\rho^2
\nabla\rho\cdot\nabla(\kappa+\sigma)\,dy.
\]

---

## 2. Threshold gradient charges

Reuse

\[
B_\rho
=\int\chi'e^{2\kappa}\rho|\nabla\rho|^2dy\ge0.
\]

Define

\[
\boxed{
B_\kappa
:=\int\chi'e^{2\kappa}\rho^3|\nabla\kappa|^2dy\ge0,
}
\]

and

\[
\boxed{
B_\sigma
:=\int\chi'e^{2\kappa}\rho^3|\nabla\sigma|^2dy\ge0.
}
\]

All three are supported only on the fixed amplitude transition collar where `chi' != 0`.

---

## 3. Exact Cauchy--Schwarz control of the cutoff term

Split

\[
T_{cut}^{(2)}=T_{\rho\kappa}+T_{\rho\sigma}.
\]

Then

\[
\boxed{
|T_{\rho\kappa}|
\le\sqrt{B_\rho B_\kappa},
}
\]

because

\[
\chi'\rho^2|\nabla\rho||\nabla\kappa|
=
\sqrt{\chi'\rho|\nabla\rho|^2}
\sqrt{\chi'\rho^3|\nabla\kappa|^2}.
\]

Similarly,

\[
\boxed{
|T_{\rho\sigma}|
\le\sqrt{B_\rho B_\sigma}.
}
\]

Thus

\[
\boxed{
|T_{cut}^{(2)}|
\le
\sqrt{B_\rho B_\kappa}
+\sqrt{B_\rho B_\sigma}.
}
\]

---

## 4. Full remainder inequality

M17-195 gives

\[
|\mathfrak R_{geom}^{(2)}|
\le
2M_\Sigma(D_\rho+B_\rho+P_\xi)
+4M_\Sigma\sqrt{D_\kappa D_\rho}.
\]

Therefore

\[
\boxed{
\begin{aligned}
|\mathcal R^{(2)}|
\le{}&
2M_\Sigma(D_\rho+B_\rho+P_\xi)
+4M_\Sigma\sqrt{D_\kappa D_\rho}\\
&+\sqrt{B_\rho B_\kappa}
+\sqrt{B_\rho B_\sigma}.
\end{aligned}
}
\]

Using Young's inequality, for arbitrary positive epsilons, the mixed terms may be split into a chosen fraction of `D_kappa`, `B_kappa`, and `B_sigma`, plus multiples of `D_rho` and `B_rho`.

Hence a large positive or negative `R_chi` requires at least one positive fixed-order occupancy among

\[
\boxed{
D_\rho,
\quad P_\xi,
\quad B_\rho,
\quad B_\kappa,
\quad B_\sigma,
}
\]

apart from a chosen absorbable fraction of `D_kappa` itself.

---

## 5. Palinstrophy interpretation

Because

\[
|\nabla W|^2=|\nabla\rho|^2+\rho^2|\nabla\xi|^2,
\]

we have

\[
\boxed{
D_\rho+P_\xi
=\int\chi e^{2\kappa}|\nabla W|^2dy.
}
\]

Thus the bulk part of the full geometric remainder is controlled by the exponentially weighted **vorticity palinstrophy** plus the positive multiplier-diffusion charge.

The only additional pieces are fixed-amplitude threshold-gradient charges.

---

## 6. Updated M5-688 payer tree

After M17-191--196, the positive M5-687 multiplier-diffusion charge can be paid only through explicit fixed-order channels:

\[
\boxed{
D_\kappa>0
\Longrightarrow
D_\sigma
\lor
Q_\sigma^{(2)}
\lor
\text{high-}kappa\text{ threshold replenishment}
\lor
P_W^{(2)}
\lor
B_{threshold}
\lor
\text{component/interface segregation},
}
\]

where

\[
P_W^{(2)}:=D_\rho+P_\xi
\]

and `B_threshold` denotes the three collar gradient charges above.

The old catch-all `R_geom` branch is therefore removed as an independent category.

---

## 7. DSD audit

- Threshold charges are positive occupancies, not automatically finite cumulative costs.
- `B_kappa` is a collar multiplier-gradient charge and is not automatically controlled by the bulk `D_kappa` because `chi` may be small where `chi'` is active.
- No weighted Calderon--Zygmund theorem is assumed.
- The reduction is fixed-order and exact up to elementary Cauchy--Schwarz/Young estimates.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
