# DSD M17-462 — The strain-weighted absolute-kappa source is a raw-H2 payer, but it returns to the cubic ancestry firewall

Date: 2026-09-10  
Canonical ID: **M17-462**

Status: **ACTIVE SOURCE-RETURN REDUCTION / RAW-H2 PAYER / CUBIC FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-459--461

In viscosity-one normalization the exact absolute coefficient-moment balance is

\[
\dot A+2J_0
=-2C_{0\sigma}+G_A+2S_A+2\Delta Q,
\]

where

\[
S_A:=S_++S_-
=\int|\kappa|\sigma\rho^2dx.
\]

M17-460 types the zero-level strain trace as palinstrophy or trace/high-jet loss under regular finite-jet thickening.

M17-461 decomposes `Delta Q` into sign-dependent mean coefficient-magnitude dispersion plus the already small palinstrophy defect.

The present module classifies `S_A`.

## 2. Snapshot raw-H2 control

By Cauchy--Schwarz,

\[
|S_A|
\le
\left(\int\kappa^2\rho^2dx\right)^{1/2}
\left(\int\sigma^2\rho^2dx\right)^{1/2}.
\]

Exact CE-H gives

\[
\int\kappa^2\rho^2dx
=\|\Delta\Omega\|_2^2
=:H_{\rm raw}.
\]

Assume the retained normalized branch has an amplitude ceiling

\[
\rho\le M_\rho.
\]

Since `sigma` is a strain eigenvalue along the vorticity direction,

\[
|\sigma|\le|\Sigma|.
\]

The whole-space strain is an order-zero singular integral of vorticity, hence

\[
\|\Sigma\|_2\lesssim\|\Omega\|_2.
\]

Writing

\[
E:=\|\Omega\|_2^2,
\]

we obtain

\[
\int\sigma^2\rho^2dx
\le
M_\rho^2\|\sigma\|_2^2
\lesssim
M_\rho^2E.
\]

Therefore

\[
\boxed{
|S_A|
\lesssim
M_\rho E^{1/2}H_{\rm raw}^{1/2}.
}
\]

Thus the strain-weighted absolute coefficient source is not an independent currency.

## 3. Spacetime payer inequality

On an interval `I`, assume

\[
\sup_{t\in I}E(t)\le E_*.
\]

Then

\[
\int_I|S_A|dt
\lesssim
M_\rho E_*^{1/2}
|I|^{1/2}
\left(\int_IH_{\rm raw}dt\right)^{1/2}.
\]

Hence if positive strain-weighted replenishment satisfies

\[
\int_I(S_A)_+dt
\ge s_*|I|
\]

for some fixed `s_*>0`, then

\[
\boxed{
\int_IH_{\rm raw}dt
\gtrsim
\frac{s_*^2}{M_\rho^2E_*}|I|.
}
\]

Persistent order-one `S_A` source therefore pays order-one normalized raw-H2 per own time.

## 4. Cross-generation firewall

For a parent-normalized record window with duration

\[
|I_R|\asymp c_TR^2,
\]

persistent order-one `S_A` replenishment gives

\[
\int_{I_R}H_{\rm raw}dt
\gtrsim cR^2.
\]

M17-405 weights this charge by `R^{-3}`. Thus the ancestral contribution is only

\[
\boxed{
R^{-3}\int_{I_R}H_{\rm raw}dt
\gtrsim cR^{-1}.
}
\]

For geometric growing records, `sum R_m^{-1}<infinity`.

Therefore

\[
\boxed{
\text{persistent strain-weighted source alone}
\not\Rightarrow
\text{ancestral contradiction}.
}
\]

This route returns exactly to the cubic raw-H2 firewall.

## 5. What would strengthen it

To defeat the cubic firewall, one needs an additional factor beyond full parent-time residence, for example

1. record-linear independent spatial multiplicity;
2. super-parent-time repeated payer multiplicity;
3. a lower-order palinstrophy conversion;
4. a geometry theorem forcing the source on `O(R)` independent longitudinal/transverse packets.

None of these is asserted by M17-462 itself.

## 6. Updated source-return tree

After M17-460--462, the M17-459 balance has the resource typing

\[
\boxed{
\begin{aligned}
-2C_{0\sigma}
&\to
\text{palinstrophy}
\lor\text{trace/high-jet loss},\\
2S_A
&\to
\text{raw-H2 cubic firewall},\\
2\Delta Q
&\to
\text{sign-dependent coefficient-scale dispersion}
+\text{small palinstrophy defect},\\
G_A
&\to
\text{still to be decomposed}.
\end{aligned}
}
\]

Thus the only genuinely unclassified term in the lower-order absolute-moment source-return equation is now the geometry source `G_A` itself; the other terms are attached to certified resources or explicit decompactification branches.

## 7. DSD audit role

DSD is used only to classify the source by the weakest certified resource that pays for it. The proof is Cauchy--Schwarz, the exact CE-H identity `Delta Omega=kappa Omega`, the strain/vorticity singular-integral estimate, and the certified M17-405 ancestry scaling.

## 8. Audit verdict

**PASS — the strain-weighted absolute-kappa source is a raw-H2 payer, not an independent OPEN source.**

However its natural parent-time payment reaches only `R^{-1}` after the `R^{-3}` ancestry discount, which is summable on geometric records. The source is therefore typed but not closed.

The next narrow target is to decompose the geometry source `G_A` into already certified amplitude/direction/strain/coefficient resources and identify whether any component lands in the favorable `R^{-1}` palinstrophy ledger.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
