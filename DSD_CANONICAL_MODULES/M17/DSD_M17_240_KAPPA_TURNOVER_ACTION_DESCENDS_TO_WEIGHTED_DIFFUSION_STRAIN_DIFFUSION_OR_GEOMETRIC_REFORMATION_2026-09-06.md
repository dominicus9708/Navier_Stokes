# DSD M17-240 — Kappa turnover action descends to multiplier diffusion, strain diffusion, or geometric reformation

Date: 2026-09-06  
Canonical ID: **M17-240**

Status: **CONSTITUTIVE TURNOVER DESCENT / M17-239 PRODUCES AN AMPLITUDE-INDEPENDENT OWN-SCALE MATERIAL TURNOVER ACTION `T_kappa=ell^-1 int int |D_B kappa|`. ON THE ACTIVE CE-H SET THE EXACT CONSTITUTIVE LAW IS `D_B kappa=L_rho kappa+L_rho sigma-kappa+R_geom`, WITH `L_rho=Delta+2 grad log rho·grad`. OVER ONE PARABOLIC TIME `O(ell^2)` AND A VOLUME `O(ell^3)`, THE BARE REACTION TERM `-kappa` CONTRIBUTES ONLY `O(ell^2)` TO THE NORMALIZED TURNOVER ACTION ON THE DIMENSIONLESS-KAPPA-BOUNDED BRANCH. THEREFORE A FIXED TURNOVER CHARGE MUST BE PAID BY MULTIPLIER DIFFUSION, STRAIN DIFFUSION, OR THE EXPLICIT GEOMETRIC REFORMATION TERM. THIS DOES NOT YET GIVE A FINITE GLOBAL BUDGET; IT IDENTIFIES THE FORMED PAYER CHANNELS AND PREVENTS `D_B kappa` FROM REMAINING AN UNTYPED EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input turnover charge

M17-239 defines, on an intrinsic packet of radius \(\ell\) and parabolic lifetime

\[
\tau_\ell=c_t\ell^2,
\]

the scale-critical material turnover action

\[
\boxed{
\mathcal T_\kappa(\ell)
:=
\ell^{-1}
\int_0^{\tau_\ell}
\int_{P(\tau)}|D_B\kappa|dy\,d\tau.
}
\]

On the turnover branch,

\[
\boxed{\mathcal T_\kappa(\ell)\ge c_T>0.}
\]

The transported set has volume \(O(\ell^3)\) because

\[
\det D\Phi_\tau=e^{3\tau/2}=1+O(\ell^2).
\]

---

## 2. Exact CE-H constitutive law

On the active set \(\rho=|W|>0\), the previously derived law is

\[
\boxed{
D_B\kappa
=L_\rho\kappa
+L_\rho\sigma
-\kappa
+\mathcal R_{geom},
}
\]

where

\[
\boxed{
L_\rho f
:=
\rho^{-2}\nabla\cdot(\rho^2\nabla f)
=
\Delta f+2\nabla\log\rho\cdot\nabla f.
}
\]

The geometric remainder is

\[
\mathcal R_{geom}
=-\frac2\rho\Sigma:\nabla^2\rho
+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi
+(\nabla\times W)\cdot\nabla\log\rho.
\]

No sign is assigned to these terms.

---

## 3. Normalize each payer

Define

\[
\boxed{
\mathcal A_{\kappa,diff}
:=
\ell^{-1}
\int_0^{\tau_\ell}
\int_{P(\tau)}|L_\rho\kappa|dy\,d\tau,
}
\]

\[
\boxed{
\mathcal A_{\sigma,diff}
:=
\ell^{-1}
\int_0^{\tau_\ell}
\int_{P(\tau)}|L_\rho\sigma|dy\,d\tau,
}
\]

and

\[
\boxed{
\mathcal A_{geom}
:=
\ell^{-1}
\int_0^{\tau_\ell}
\int_{P(\tau)}|\mathcal R_{geom}|dy\,d\tau.
}
\]

The reaction contribution is

\[
\mathcal A_{react}
:=
\ell^{-1}
\int_0^{\tau_\ell}
\int_{P(\tau)}|\kappa|dy\,d\tau.
\]

---

## 4. The bare reaction term is parabolically lower order

On the non-kappa-spike branch,

\[
\ell^2\|\kappa\|_\infty\le K_*.
\]

Hence

\[
\begin{aligned}
\mathcal A_{react}
&\le
\ell^{-1}
(K_*\ell^{-2})
(C\ell^3)
(c_t\ell^2)\\
&\le C K_*c_t\ell^2.
\end{aligned}
\]

Therefore

\[
\boxed{\mathcal A_{react}=o(1).}
\]

The linear \(-\kappa\) term cannot turn a critical \(O(\ell^{-2})\) multiplier population by a fixed fraction over its own parabolic lifetime.

---

## 5. Turnover payer trichotomy

The triangle inequality in the exact constitutive law gives

\[
\mathcal T_\kappa
\le
\mathcal A_{\kappa,diff}
+\mathcal A_{\sigma,diff}
+\mathcal A_{react}
+\mathcal A_{geom}.
\]

Since

\[
\mathcal T_\kappa\ge c_T
\]

and

\[
\mathcal A_{react}=o(1),
\]

for sufficiently small \(\ell\) at least one of

\[
\boxed{
\mathcal A_{\kappa,diff}\ge c,
\qquad
\mathcal A_{\sigma,diff}\ge c,
\qquad
\mathcal A_{geom}\ge c
}
\]

must hold.

Thus

\[
\boxed{
H_{\mathcal T_\kappa}
\Longrightarrow
H_{L_\rho\kappa}
\lor
H_{L_\rho\sigma}
\lor
H_{geom\ reformation}.
}
\]

---

## 6. Expand the multiplier-diffusion payer

The first payer is

\[
L_\rho\kappa
=
\Delta\kappa
+2\nabla\log\rho\cdot\nabla\kappa.
\]

Therefore

\[
\boxed{
H_{L_\rho\kappa}
\Longrightarrow
H_{\Delta\kappa}
\lor
H_{\nabla\log\rho\cdot\nabla\kappa}.
}
\]

This makes explicit that rapid multiplier turnover requires either

1. an additional multiplier derivative scale; or
2. coupling to a steep relative-amplitude geometry.

Neither is silently counted as the same M17-235 weighted diffusion charge.

---

## 7. Expand the strain-diffusion payer

Likewise

\[
L_\rho\sigma
=
\Delta\sigma
+2\nabla\log\rho\cdot\nabla\sigma.
\]

Thus

\[
\boxed{
H_{L_\rho\sigma}
\Longrightarrow
H_{\Delta\sigma}
\lor
H_{\nabla\log\rho\cdot\nabla\sigma}.
}
\]

This branch is a true higher spatial reformation of the strain field, not the same as the order-one integrated strain cancellation \(\mathcal S_\ell\) from M17-239.

---

## 8. Relation to M17-145 and M5-687

M17-145 derives a weighted diffusion/damping equation for a directional multiplier gradient, while M5-687 proves a positive high-amplitude multiplier-gradient diffusion charge on the compact CE-H hull.

M17-240 is complementary:

- M5-687/M17-145 use amplitude-weighted quadratic diffusion;
- M17-240 begins with an amplitude-independent material turnover action;
- the constitutive descent shows which higher coefficient/geometry channels must support that turnover.

No measure conversion between the two is asserted without an additional theorem.

---

## 9. Updated ARG dynamic branch

Combining M17-239 and M17-240,

\[
\boxed{
H_{critical\ sign\text{-}balanced\ \kappa}
\Longrightarrow
H_{palinstrophy}
\lor H_{strain\ action}
\lor H_{L_\rho\kappa}
\lor H_{L_\rho\sigma}
\lor H_{geom}
\lor G_{interface/deformation}.
}
\]

The formerly untyped alternative `kappa changes rapidly` is removed.

---

## 10. Remaining firewall

The new coefficient actions are amplitude independent after own-scale normalization, but there is no known finite global budget for

\[
\ell^{-1}\iint|L_\rho\kappa|,
\quad
\ell^{-1}\iint|L_\rho\sigma|,
\quad
\ell^{-1}\iint|\mathcal R_{geom}|.
\]

A derivative-order escalation or coefficient reformation chain is not a contradiction by itself.

The next audit must determine whether material replacement/finite-memory can price these events. In particular, it must first check whether the coefficient packets carry a fixed nonzero flux label; low amplitude may make their flux vanish.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
