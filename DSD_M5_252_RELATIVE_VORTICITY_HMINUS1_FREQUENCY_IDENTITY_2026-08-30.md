# DSD M5-252 — Relative-Vorticity H^{-1} Frequency Identity

Date: 2026-08-30

Parent: `DSD_M5_251_QUOTIENT_TIGHTNESS_RADIUS_AND_ANTI_DAMPING_FREQUENCY_GATE_2026-08-30.md`

Status: **EXACT SAME-QUOTIENT REFORMULATION / FOR THE DIVERGENCE-FREE FINITE-ENERGY QUOTIENT `Q`, THE M5-250 DIRICHLET FREQUENCY IS EXACTLY THE RELATIVE-VORTICITY `L2 / H^{-1}` FREQUENCY: `D_Q=||eta||_2^2` AND `E_Q=||eta||_{dot H^{-1}}^2` / THIS EXPOSES THE ANTI-DAMPING BRANCH AS A GENUINE LOW-SPATIAL-FREQUENCY RELATIVE-VORTICITY SURVIVOR, NOT A TOTAL-VORTICITY TIGHTNESS STATEMENT / A NEW RELATIVE-ENSTROPHY RADIUS GIVES A SAFE FREQUENCY FLOOR VIA HLS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Relative vorticity

Use the finite-energy quotient from M5-250,

\[
Q=V-B,
\qquad \nabla\cdot Q=0,
\qquad Q\in H^1(\mathbb R^3)\cap L^2(\mathbb R^3).
\]

Define

\[
\boxed{
\eta:=\nabla\times Q
=\Omega-\nabla\times B.
}
\]

This is the **relative vorticity** after canonical-tail subtraction.

It must not be identified with the total vorticity `Omega`.

---

## 2. Exact gradient identity

For divergence-free `Q in H1(R3)`,

\[
\int|\nabla Q|^2
=
\int|\nabla\times Q|^2
+
\int|\nabla\cdot Q|^2.
\]

Therefore

\[
\boxed{
D_Q
:=\|\nabla Q\|_2^2
=
\|\eta\|_2^2.
}
\]

---

## 3. Exact H^{-1} identity

In Fourier variables,

\[
\widehat\eta(\xi)
=i\xi\times\widehat Q(\xi),
\qquad
\xi\cdot\widehat Q=0.
\]

Hence

\[
|\widehat\eta(\xi)|^2
=|\xi|^2|\widehat Q(\xi)|^2.
\]

Thus

\[
\begin{aligned}
\|\eta\|_{\dot H^{-1}}^2
&:=
\int_{\mathbb R^3}
\frac{|\widehat\eta(\xi)|^2}{|\xi|^2}d\xi\\
&=
\int|\widehat Q(\xi)|^2d\xi\\
&=\boxed{\|Q\|_2^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
E_Q=\|\eta\|_{\dot H^{-1}}^2.
}
\]

---

## 4. Exact quotient-frequency interpretation

M5-250's mean frequency is therefore

\[
\boxed{
\bar\lambda_Q
=
\frac{\langle\|\eta\|_2^2\rangle}
{\langle\|\eta\|_{\dot H^{-1}}^2\rangle}.
}
\]

This is a genuine relative-vorticity frequency.

The anti-damping-dominant branch

\[
\bar\lambda_Q\le\frac{3}{4\nu}
\]

means that the relative vorticity maintains sufficiently large negative-order mass compared with its enstrophy.

Equivalently, it is a **low-frequency relative-vorticity branch**.

---

## 5. HLS/Sobolev form

The Biot--Savart/Riesz-potential estimate gives

\[
\boxed{
\|\eta\|_{\dot H^{-1}}
\le C_{HLS}\|\eta\|_{L^{6/5}}.
}
\]

Hence

\[
\boxed{
\frac{D_Q}{E_Q}
\ge
\frac{\|\eta\|_2^2}
{C_{HLS}^2\|\eta\|_{6/5}^2}.
}
\]

This is the relative-vorticity version of M5-251.

---

## 6. Relative-enstrophy tightness radius

For `0<epsilon<1`, define a relative-enstrophy radius `R_eta(epsilon)` by

\[
\boxed{
\int_{B_{R_\eta}}|\eta|^2
\ge
(1-\varepsilon)\|\eta\|_2^2.
}
\]

On the inner ball,

\[
\|\eta\|_{L^{6/5}(B_R)}
\le
|B_R|^{1/3}\|\eta\|_{L^2(B_R)}.
\]

The outer part requires an explicit tail estimate in `L^{6/5}`; mere `L2` tightness is not enough on an infinite-volume complement.

Therefore the safe relative-vorticity tightness input is the strengthened condition

\[
\boxed{
\|\eta\|_{L^{6/5}(|Y|>R_\eta)}
\le
\delta_\eta\|\eta\|_2
}
\]

with a dimensionally appropriate fixed `delta_eta`.

Under this input,

\[
\|\eta\|_{6/5}
\le
\left(\frac{4\pi}{3}\right)^{1/3}R_\eta\|\eta\|_2
+\delta_\eta\|\eta\|_2.
\]

Thus

\[
\boxed{
\frac{D_Q}{E_Q}
\ge
\frac{1}
{C_{HLS}^2\left[(4\pi/3)^{1/3}R_\eta+\delta_\eta\right]^2}.
}
\]

---

## 7. Anti-damping radius consequence

If anti-damping dominates as in M5-250, then

\[
\frac{1}
{C_{HLS}^2\left[(4\pi/3)^{1/3}R_\eta+\delta_\eta\right]^2}
\le
\frac{3}{4\nu}.
\]

Therefore

\[
\boxed{
(4\pi/3)^{1/3}R_\eta+\delta_\eta
\ge
\frac{2\sqrt\nu}{\sqrt3\,C_{HLS}}.
}
\]

Again the survivor requires a relative-vorticity scale of order `sqrt(nu)` unless the `L^{6/5}` outer tail itself remains large.

---

## 8. New safe fork

The anti-damping branch is therefore refined to

\[
\boxed{
\text{broad relative-vorticity scale}
\quad\lor\quad
\text{non-negligible relative }L^{6/5}\text{ tail}.
}
\]

The second branch is a low-frequency tail obstruction specific to the tail-subtracted field and is distinct from the total-vorticity critical `L^{3/2,\infty}` tail already present elsewhere in the repository.

---

## 9. Core nontriviality under an interior-vanishing tail extension

If the canonical divergence-free extension `B` is chosen to vanish on a fixed core ball containing the normalized first-hitting witness, then on that core

\[
\eta=\Omega.
\]

Since the recurrent W1 corridor carries a nontrivial core vorticity witness, this gives

\[
\boxed{
\|\eta\|_2>0
}
\]

for every state in the corresponding minimal hull, and compactness then supplies a positive lower bound.

This conclusion is conditional on fixing such an interior-vanishing canonical extension convention and must be checked against the actual extension construction before it is used numerically.

---

## 10. DSD verdict

### EXACT

\[
\boxed{
D_Q=\|\eta\|_2^2,
\qquad
E_Q=\|\eta\|_{\dot H^{-1}}^2.
}
\]

Hence the quotient frequency is exactly a relative-vorticity `L2/H^{-1}` frequency.

### CORRECTED

Total-vorticity tightness `R_Z` is not the same as relative-vorticity tightness `R_eta`.

### NEW FORK

Anti-damping dominance requires either a broad relative-vorticity structure or a persistent low-frequency `L^{6/5}` relative tail.

### OPEN

- compare the actual canonical extension with the interior-vanishing convention;
- quantify the relative `L^{6/5}` tail;
- strain-work payer;
- signed residual-work payer;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
