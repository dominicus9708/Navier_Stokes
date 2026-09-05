# DSD M17-195 — The geometric remainder is quantitatively dominated by existing multiplier, amplitude, director, and threshold-gradient charges

Date: 2026-09-06  
Canonical ID: **M17-195**

Status: **QUANTITATIVE PAYER REDUCTION / M17-194 REMOVES THE AMPLITUDE-HESSIAN AND CURL CHANNELS FROM THE `exp(2 kappa) chi rho^2`-WEIGHTED GEOMETRIC REMAINDER. UNDER THE COMPACT-HULL STRAIN BOUND `||Sigma||_infty <= M_Sigma`, THE REMAINDER IS BOUNDED BY THE AMPLITUDE-GRADIENT CHARGE, DIRECTOR-GRADIENT/PALINSTROPHY CHARGE, THE AMPLITUDE-THRESHOLD COLLAR, AND ONE MIXED `sqrt(D_kappa D_rho)` TERM. YOUNG'S INEQUALITY ALLOWS AN ARBITRARILY SMALL FRACTION OF THE POSITIVE M5-687 `D_kappa` CHARGE TO BE ABSORBED, LEAVING ONLY THE OTHER FIXED-ORDER POSITIVE OCCUPANCIES. THUS `R_geom` CANNOT BE A LARGE INDEPENDENT PAYER WHILE ALL AMPLITUDE/DIRECTOR/THRESHOLD GRADIENT CHARGES VANISH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Charges

Use the same weight as M17-194 and define

\[
D_\kappa
:=\int\chi e^{2\kappa}\rho^2|\nabla\kappa|^2dy,
\]

\[
\boxed{
D_\rho
:=\int\chi e^{2\kappa}|\nabla\rho|^2dy,
}
\]

\[
\boxed{
P_\xi
:=\int\chi e^{2\kappa}\rho^2|\nabla\xi|^2dy,
}
\]

and the transition-collar amplitude-gradient charge

\[
\boxed{
B_\rho
:=\int\chi'(\rho)e^{2\kappa}\rho|\nabla\rho|^2dy.
}
\]

For the usual monotone high-amplitude cutoff, `B_rho >= 0`.

Also, since

\[
|\nabla W|^2=|\nabla\rho|^2+\rho^2|\nabla\xi|^2,
\]

both `D_rho` and `P_xi` are pieces of the weighted palinstrophy architecture.

---

## 2. Compact strain bound

On the retained compact high-amplitude hull let

\[
\boxed{\|\Sigma\|_{L^\infty}\le M_\Sigma<\infty.}
\]

Apply this to the four exact terms of M17-194.

The pure amplitude-gradient term satisfies

\[
\left|
2\int\chi e^{2\kappa}\Sigma(\nabla\rho,\nabla\rho)
\right|
\le2M_\Sigma D_\rho.
\]

The threshold term satisfies

\[
\left|
2\int\chi'e^{2\kappa}\rho\Sigma(\nabla\rho,\nabla\rho)
\right|
\le2M_\Sigma B_\rho.
\]

The director metric satisfies

\[
\left|
2\int\chi e^{2\kappa}\rho^2
\Sigma_{ij}(\partial_i\xi\cdot\partial_j\xi)
\right|
\le2M_\Sigma P_\xi.
\]

---

## 3. Mixed multiplier-amplitude term

For

\[
4\int\chi e^{2\kappa}\rho\Sigma(\nabla\kappa,\nabla\rho),
\]

Cauchy--Schwarz gives

\[
\boxed{
\left|
4\int\chi e^{2\kappa}\rho\Sigma(\nabla\kappa,\nabla\rho)
\right|
\le
4M_\Sigma\sqrt{D_\kappa D_\rho}.
}
\]

Thus the complete instantaneous weighted geometric remainder obeys

\[
\boxed{
|\mathfrak R_{geom}^{(2)}|
\le
2M_\Sigma(D_\rho+B_\rho+P_\xi)
+4M_\Sigma\sqrt{D_\kappa D_\rho}.
}
\]

---

## 4. Young absorption

For every `epsilon>0`,

\[
4M_\Sigma\sqrt{D_\kappa D_\rho}
\le
\varepsilon D_\kappa
+\frac{4M_\Sigma^2}{\varepsilon}D_\rho.
\]

Therefore

\[
\boxed{
|\mathfrak R_{geom}^{(2)}|
\le
\varepsilon D_\kappa
+\left(2M_\Sigma+\frac{4M_\Sigma^2}{\varepsilon}\right)D_\rho
+2M_\Sigma(B_\rho+P_\xi).
}
\]

This is the useful payer inequality.

---

## 5. Consequence for the positive M5-687 diffusion charge

M5-687 supplies a statewise/recurrent positive lower bound

\[
D_\kappa\ge d_\kappa^{(2)}>0
\]

on the retained nonzero compact CE-H hull.

Choose, for example, `epsilon=1/4`.
If the geometric remainder contributes an order-one fraction of the payment of `D_kappa`, then at least one of

\[
\boxed{
D_\rho,
\qquad
P_\xi,
\qquad
B_\rho
}
\]

must carry a corresponding positive lower bound depending only on the compact-hull constants and the required payer fraction.

Thus

\[
\boxed{
\text{large geometric payment}
\Longrightarrow
\text{amplitude-gradient}
\lor
\text{director-gradient/palinstrophy}
\lor
\text{threshold-gradient payment}.
}
\]

The geometric remainder cannot remain order one if all three of these charges tend to zero while `D_kappa` stays uniformly positive.

---

## 6. What this does not close

The quantities `D_rho`, `P_xi`, and `B_rho` are positive occupancies but are not yet known to possess finite cumulative similarity-time budgets on the recurrent ancient branch.

Therefore the present theorem collapses the payer taxonomy but does not prove that the payments cannot be recycled indefinitely.

---

## 7. DSD audit

- No sign is assigned to `R_geom`; only its magnitude is controlled.
- No smallness of `M_Sigma` is assumed.
- The `epsilon D_kappa` absorption is bookkeeping, not a claim that the geometric term is dissipative.
- `P_xi` is a director-gradient part of palinstrophy, not an independent conserved charge.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
