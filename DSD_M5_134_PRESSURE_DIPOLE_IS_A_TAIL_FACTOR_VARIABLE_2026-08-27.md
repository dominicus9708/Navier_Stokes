# DSD M5-134 — Pressure Dipole Is a Tail-Factor Variable

Date: 2026-08-27

Status: **NSE-SPECIFIC FIBER AUDIT / M5-133'S `ell=1` BOUNDED PRESSURE-POISSON RESONANCE IS NOT A FREE SAME-TAIL FIBER VARIABLE / TWO W1 STATES WITH THE SAME CANONICAL VELOCITY TAIL HAVE A STRONGER FINITE-LORENTZ PRESSURE DIFFERENCE, WHICH CANNOT CONTAIN ANY NONZERO `r^-2` CRITICAL PRESSURE MODE / THE DIPOLE MAY BE NONZERO BUT IS FIXED BY THE REALIZED TAIL FACTOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Same-tail states

Let `V,W` belong to the W1 compact minimal class and assume

\[
T_V=T_W=:T.
\]

M5-115 gives

\[
\boxed{Z:=V-W\in L^2\cap L^3.}
\]

The W1 states themselves remain uniformly bounded in the critical Lorentz class

\[
V,W\in L^{3,\infty}.
\]

---

## 2. Pressure difference

Fix the whole-space pressure normalization through the Riesz representation

\[
P_V=\mathcal R_i\mathcal R_j(V_iV_j),
\qquad
P_W=\mathcal R_i\mathcal R_j(W_iW_j)
\]

up to the ordinary time-dependent additive gauge, which is irrelevant to spatial critical tails.

Then

\[
V_iV_j-W_iW_j
=
Z_iV_j+W_iZ_j.
\]

Lorentz Hölder/O'Neil multiplication gives schematically

\[
L^{3}\cdot L^{3,\infty}
\subset
L^{3/2,q_*}
\]

for a finite Lorentz index `q_*` (one may take the natural finite index inherited from the strong `L3` factor; the exact finite index is not essential below).

Calderon-Zygmund/Riesz operators are bounded on `L^{p,q}` for `1<p<infinity` and finite `q`.

Hence

\[
\boxed{
P_V-P_W
\in
L^{3/2,q_*}(\mathbb R^3)
\qquad(q_*<\infty).
}
\]

---

## 3. Critical `r^-2` pressure tails are excluded from finite-index Lorentz difference

A nonzero critical pressure tail

\[
P_c(Y)=r^{-2}\Psi(\log r,\theta)
\]

with a recurrent/bounded nontrivial angular-log profile has order-one `L^{3/2}` mass per logarithmic radial cell:

\[
|P_c|^{3/2}dY
\sim
r^{-3}\,r^2dr\,d\theta
=
\frac{dr}{r}\,d\theta.
\]

Therefore such a persistent critical tail is naturally weak-`L^{3/2}` and fails every finite-index borderline Lorentz condition that counts the logarithmic depth.

In particular, a nonzero rho-independent `ell=1` dipole

\[
P_{dip}=\frac{a\cdot Y}{|Y|^3}
\]

cannot belong to `L^{3/2,q}` for any finite `q` on the full critical radial range.

---

## 4. Consequence for same-tail fibers

Suppose `P_V` and `P_W` had different leading `r^-2` canonical pressure tails.

Their difference would contain a nonzero critical `r^-2` component and therefore could not lie in finite-index `L^{3/2,q_*}`.

This contradicts Section 2.

Hence

\[
\boxed{
\Psi_V=\Psi_W
}
\]

for the entire realized leading critical pressure coefficient, including the M5-133 `ell=1` dipole component.

Thus the pressure dipole is constant on each velocity-tail fiber.

---

## 5. Tail-factor pressure map

The realized W1 dynamics therefore induces a single-valued extended factor map

\[
\boxed{
T_V
\longmapsto
\Psi_{T_V}
}
\]

on the image of the canonical velocity-tail factor.

M5-133 still matters: the punctured Poisson equation alone determines `Psi` only modulo the bounded dipole kernel.

M5-134 adds the missing realization information:

\[
\boxed{
\text{W1 whole-space realization + strong same-tail fiber}
\Rightarrow
\text{the dipole coefficient is fixed on the factor fiber.}
}
\]

It does **not** prove that coefficient is zero.

---

## 6. DSD four-chain audit

### Formation — GREEN

The pressure tail is obtained from actual W1 pressures, not by choosing a homogeneous Poisson solution arbitrarily.

### Axis — GREEN

Ordinary pressure gauge constants are distinguished from the critical `r^-2, ell=1` dipole.

### Static aggregation — GREEN

The strong pressure difference is not added to the critical tail. It is used only to exclude a difference in the leading tail coefficient.

### Dynamics — GREEN

No recurrence or invariant averaging is needed.

### Cross-audit — GREEN

This does not reverse M5-133. The elliptic kernel remains mathematically present; W1 realization selects one coefficient on each velocity-tail state.

---

## 7. Consequence for P1/F split

Same-tail fiber dynamics can change strong-critical core/quotient variables, but it cannot change

- the canonical `r^-1` velocity tail;
- the full leading `r^-2` pressure tail;
- the pressure dipole coefficient;
- the cubic Abel residue.

Therefore all leading critical tail pressure geometry is genuinely factor-level data.

The remaining P1 freedom is confined to strong `L2 cap L3` corrections.

---

## 8. RED firewall

Do not infer

\[
\text{dipole fixed on tail factor}
\Rightarrow
\text{dipole}=0.
\]

A separate unforced-ancestry/stress argument would still be required to prove zero.

---

## 9. Next gate

With both leading velocity and pressure now factor-level variables, the next F-gate calculation is to treat the full log-cylinder NSE residual

\[
\mathfrak F[\Phi,\Psi]
\]

as a deterministic observable on the compact tail factor and audit whether its nonzero recurrent component can be canceled by a strong `L2 cap L3` quotient without generating an additional forbidden critical tail.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]