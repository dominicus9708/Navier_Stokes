# DSD M17-464 — The geometry-source antisymmetric channel is endpoint plus raw-H2, while the common-mode channel remains uncontrolled

Date: 2026-09-10  
Canonical ID: **M17-464**

Status: **ACTIVE ANTISYMMETRIC-SOURCE REDUCTION / RAW-H2 TYPING / COMMON-MODE FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Exact difference equation

M17-459 gives

\[
\boxed{
\dot P+2H_{\rm raw}
=G_D+2S_D,
}
\]

where

\[
G_D=G_--G_+,
\qquad
S_D=S_--S_+.
\]

Therefore

\[
\boxed{
G_D
=\dot P+2H_{\rm raw}-2S_D.
}
\]

This identity is exact in the common viscosity-one normalization used in M17-459.

## 2. The strain-difference term is raw-H2 controlled

Because

\[
S_D
=S_--S_+
=-\int\kappa\sigma\rho^2dx,
\]

Cauchy--Schwarz gives

\[
|S_D|
\le
\left(\int\kappa^2\rho^2dx\right)^{1/2}
\left(\int\sigma^2\rho^2dx\right)^{1/2}.
\]

Under the retained normalized amplitude ceiling `rho <= M_rho` and bounded enstrophy `E=||Omega||_2^2`, the same argument as M17-462 gives

\[
\boxed{
|S_D|
\lesssim
M_\rho E^{1/2}H_{\rm raw}^{1/2}.
}
\]

Thus `S_D` is not an independent source currency.

## 3. Integrated antisymmetric geometry-source identity

Integrating on `I=[t_0,t_1]` yields

\[
\boxed{
\int_I G_Ddt
=P(t_1)-P(t_0)
+2\int_IH_{\rm raw}dt
-2\int_IS_Ddt.
}
\]

Hence

\[
\left|\int_I G_Ddt\right|
\le
P(t_0)+P(t_1)
+2\int_IH_{\rm raw}dt
+2\int_I|S_D|dt.
\]

If `sup_I E <= E_*`, then

\[
\int_I|S_D|dt
\lesssim
M_\rho E_*^{1/2}|I|^{1/2}
\left(\int_IH_{\rm raw}dt\right)^{1/2}.
\]

Therefore

\[
\boxed{
\left|\int_I G_Ddt\right|
\lesssim
P(t_0)+P(t_1)
+\int_IH_{\rm raw}dt
+M_\rho E_*^{1/2}|I|^{1/2}
\left(\int_IH_{\rm raw}dt\right)^{1/2}.
}
\]

The antisymmetric geometry channel is thus completely typed by endpoint palinstrophy plus raw-H2.

## 4. Parent-window scaling

On a parent-normalized record interval

\[
|I_R|\asymp c_TR^2,
\]

suppose one attempted to maintain an order-one mean antisymmetric geometry source:

\[
\left|\int_{I_R}G_Ddt\right|
\gtrsim cR^2.
\]

If endpoint palinstrophy is not itself of order `R^2`, the integrated identity forces an order-`R^2` raw-H2 contribution up to the Cauchy term.

That charge enters the M17-405 ancestral ledger with weight `R^{-3}`, giving only

\[
\boxed{R^{-1}}
\]

per record, which is summable on geometric records.

If the endpoint `P` term itself grows to order `R^2`, that is a separate endpoint-palinstrophy concentration branch and must be tested against M17-307 / record placement rather than silently absorbed.

Therefore

\[
\boxed{
G_D\text{ is classified, but generic parent-time persistence returns to the raw-H2 cubic firewall.}
}
\]

## 5. Common-mode source is not constrained by this argument

Define

\[
G_A=G_-+G_+.
\]

M17-463 shows that `G_A` and `G_D` are independent sum/difference channels.

For example, `G_+=G_-=M` yields

\[
G_D=0,
\qquad
G_A=2M.
\]

Thus even complete control of `G_D` leaves a potentially large common-mode geometry source invisible to the palinstrophy difference.

The exact decomposition is

\[
\boxed{
G_-=\frac{G_A+G_D}{2},
\qquad
G_+=\frac{G_A-G_D}{2}.
}
\]

After M17-464, the only untyped geometry-source currency is therefore the sign-even/common-mode part `G_A`.

## 6. Updated source-return classification

The M17-459 absolute-moment balance is

\[
\dot A+2J_0
=-2C_{0\sigma}+G_A+2S_A+2\Delta Q.
\]

Current typing is

\[
\boxed{
\begin{aligned}
C_{0\sigma}
&\to \text{palinstrophy or trace/high-jet loss},\\
S_A
&\to \text{raw-H2 cubic firewall},\\
\Delta Q
&\to \text{sign-dependent coefficient-scale dispersion plus small }P,\\
G_D
&\to \text{endpoint }P + \text{ raw-H2},\\
G_A
&\to \text{common-mode geometry-source OPEN firewall}.
\end{aligned}
}
\]

Hence there is no longer an untyped **antisymmetric** geometry source.

## 7. DSD audit role

DSD is used only to separate sign-even and sign-odd source channels and attach each to the weakest certified resource. The derivation is elementary algebra from the exact M17-459 balance plus Cauchy--Schwarz and the M17-405/M17-307 resource ledgers.

## 8. Audit verdict

**PASS — the antisymmetric geometry-source channel is not independent.**

It is endpoint palinstrophy plus raw-H2 and strain-difference terms, with the latter also raw-H2 controlled. The unresolved geometry-source problem has therefore been compressed to the **common-mode sign-even source `G_A`**, whose exact termwise M17-339 formula must be recovered or independently bounded before further payer claims are allowed.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
