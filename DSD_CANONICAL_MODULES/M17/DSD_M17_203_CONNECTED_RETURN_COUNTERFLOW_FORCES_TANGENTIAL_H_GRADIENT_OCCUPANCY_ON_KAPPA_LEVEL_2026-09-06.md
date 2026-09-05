# DSD M17-203 — Connected return-current counterflow forces tangential `h`-gradient occupancy on the kappa level

Date: 2026-09-06  
Canonical ID: **M17-203**

Status: **COUNTERFLOW-TO-GRADIENT GATE / M17-202 SHOWS THAT FAILURE OF VOLUME-TO-ENSTROPHY SIGN TRANSFER REQUIRES A FIXED POSITIVE `h>0` COUNTERFLOW ON THE SAME REGULAR `kappa=k0` LEVEL THAT HAS NEGATIVE NET RETURN CURRENT. ON A CONNECTED COMPACT LEVEL COMPONENT WITH UNIFORM COAREA WEIGHT AND POINCARE CONSTANT, THIS SIGN COEXISTENCE FORCES A STRICT POSITIVE LOWER BOUND ON THE TANGENTIAL `|grad_T h|^2` OCCUPANCY. SINCE CE-H GIVES BOTH `W dot grad kappa=0` AND `W dot grad h=0`, THIS IS A CROSS-VORTEX MULTIPLIER-ACCELERATION GRADIENT, NOT VARIATION ALONG THE VORTEX LEAF. DISCONNECTED COMPONENTS/INTERFACES REMAIN THE ALTERNATIVE ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-202

Let `Gamma` be one connected regular portion of

\[
\{\kappa=k_0\}\cap\{\rho\ge a\}.
\]

Use

\[
\boxed{d\nu=\frac{dS}{|\nabla\kappa|}.}
\]

Assume its net volume return current is

\[
\boxed{\int_\Gamma h\,d\nu=-A<0.}
\]

On the M17-202 counterflow branch,

\[
\boxed{H_+:=\int_\Gamma h_+d\nu\ge c_0A}
\]

for a fixed `c0>0` determined by the amplitude-band ratio.

---

## 2. Uniform compact level geometry

Assume

\[
\boxed{\nu(\Gamma)\le N_*<\infty}
\]

and a uniform weighted Poincare inequality

\[
\boxed{
\int_\Gamma|f-\bar f_\nu|^2d\nu
\le C_P\int_\Gamma|\nabla_Tf|^2d\nu.
}
\]

This follows, for example, on a compact family of connected regular level components with `|grad kappa|` bounded above and below and uniformly controlled intrinsic geometry.

---

## 3. Counterflow forces variance

The weighted mean is

\[
\bar h_\nu
=\frac1{\nu(\Gamma)}\int_\Gamma h\,d\nu
=-\frac{A}{\nu(\Gamma)}<0.
\]

On the positive set `{h>0}`,

\[
h-\bar h_\nu\ge h.
\]

Therefore

\[
\int_\Gamma(h-\bar h_\nu)^2d\nu
\ge\int_{h>0}h^2d\nu.
\]

By Cauchy--Schwarz,

\[
\int_{h>0}h^2d\nu
\ge\frac{H_+^2}{\nu(\Gamma)}.
\]

Hence

\[
\boxed{
\int_\Gamma(h-\bar h_\nu)^2d\nu
\ge\frac{c_0^2A^2}{N_*}.
}
\]

---

## 4. Tangential gradient lower bound

Apply weighted Poincare:

\[
\boxed{
\int_\Gamma|\nabla_Th|^2d\nu
\ge
\frac{c_0^2A^2}{C_PN_*}.
}
\]

Thus a quantitative measure-sign reversal cannot be achieved by a spatially flat `h` field on a connected regular return level.

---

## 5. CE-H line-constancy sharpens the interpretation

Existing CE-H identities give

\[
\boxed{W\cdot\nabla\kappa=0}
\]

and for the material multiplier velocity

\[
\boxed{W\cdot\nabla h=0.}
\]

Therefore the vortex direction `xi` lies tangent to the `kappa` level and also annihilates `h`.

The tangential derivative detected above is consequently transverse to the vortex-line direction inside the `kappa` level.
It is a genuine **cross-vortex multiplier-acceleration gradient**.

---

## 6. Branch split

Hence the M17-202 measure mismatch becomes

\[
\boxed{
\text{negative volume return}
\Longrightarrow
\text{negative enstrophy return}
\lor
G_{\nabla_T h}
\lor
G_{component/interface}.
}
\]

The new `G_gradT h` branch is fixed-order but one derivative above the original scalar current. It should not be blindly differentiated again unless a new coercive budget is available.

---

## 7. DSD audit

- The Poincare lower bound is conditional on connected compact regular level geometry.
- If positive and negative `h` populations live on disconnected components, the gradient conclusion need not follow; that is kept as an explicit interface/component branch.
- A positive `|grad h|^2` occupancy is not yet a finite cumulative dissipation cost.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
