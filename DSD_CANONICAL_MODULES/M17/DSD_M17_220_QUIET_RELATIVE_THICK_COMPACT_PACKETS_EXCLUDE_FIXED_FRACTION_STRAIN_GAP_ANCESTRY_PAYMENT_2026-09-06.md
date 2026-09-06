# DSD M17-220 — Quiet relative-thick compact packets exclude the fixed-fraction strain-gap ancestry payment

Date: 2026-09-06  
Canonical ID: **M17-220**

Status: **ACTION-BRANCH CLOSURE ON THE QUIET COMPACT LANE / M17-218 SHOWS THAT A FIXED-FRACTION HIGH-ANISOTROPY CARRIER WITH BOUNDED CARRIER-LOCAL RMS SPECTRAL RATIO EITHER HAS A HIGH-ANISOTROPY MATERIAL ANCESTOR OR PAYS A FIXED ENSTROPHY-WEIGHTED STRAIN-SPECTRAL-GAP ACTION. ON THE M17-155 RELATIVE-THICK COMPACT QUIET LANE, BOUNDED RMS `H2/L2` CONTROL GIVES A UNIFORM POINTWISE AMPLITUDE CEILING `rho^2 <= C E_R` ON THE FIXED-LAG MATERIAL PACKET, WHILE THE QUIET SHELL ESTIMATE GIVES `int int |Sigma|^2 <= C_T/R`. CHANGING VARIABLES ONLY WITH THE EXACT MATERIAL JACOBIAN AND APPLYING CAUCHY-SCHWARZ THEN BOUNDS THE SAME STRAIN-GAP ACTION BY `C E_R R^-1/2 = o(E_R)`, CONTRADICTING THE M17-218 LOWER BOUND `c E_R`. THUS THE STRAIN-GAP ALTERNATIVE CANNOT CARRY A FIXED SHELL FRACTION ON THIS LANE. THE SURVIVOR IS ANCESTOR ANISOTROPY, CARRIER-LOCAL SPECTRAL CONCENTRATION, OR AN EXPLICIT THIN/DECOMPACTIFICATION/INTERFACE EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-lag packet setup

Let `C_R(theta)` be a remote fixed-shape shell corridor and let `S(theta)` be a material Rank-2 subpacket over

\[
\theta\in[-T,0],
\qquad T<\infty.
\]

Write

\[
E_R:=\int_{C_R(0)}\rho^2dy.
\]

Assume the selected current carrier occupies a fixed enstrophy fraction and the M17-218 bounded-RMS branch holds:

\[
\boxed{
E_S(0)\ge c_0E_R,
\qquad
\sup_{-T\le\tau\le0}\Lambda_S(\tau)\le\Lambda_*<\infty.
}
\]

Here

\[
\Lambda_S^2(\tau)
=\frac{\int_{S(\tau)}|\Delta W|^2dy}
{\int_{S(\tau)}|W|^2dy}.
\]

Assume the packet remains in the relative-thick compact geometry and in the quiet remote corridor of M17-155.

---

## 2. Fixed-lag mass comparability

M17-211 gives

\[
e^{-C_*T}E_S(0)
\le E_S(\tau)
\le e^{C_*T}E_S(0)
\]

for all `tau in [-T,0]`, where `C_*` depends only on the compact strain hull and `Lambda_*`.

Thus

\[
\boxed{
E_S(\tau)\asymp_T E_R.
}
\]

The material volume also stays uniformly bounded because

\[
\det D\Phi=e^{3(\tau+T)/2}
\]

and the compact packet has bounded initial volume:

\[
\boxed{
|S(\tau)|\le V_T^*<\infty.
}
\]

---

## 3. Relative-thick RMS control gives an amplitude ceiling

On a fixed enlarged packet neighborhood, bounded `Lambda_S` gives

\[
\int |\Delta W|^2
\le\Lambda_*^2E_S(\tau).
\]

Together with the `L2` bound and a fixed cutoff/enlargement, standard local `H2` estimates give

\[
\|W(\tau)\|_{H^2(S(\tau))}^2
\le C_{T,\Lambda_*}E_R.
\]

In three dimensions,

\[
H^2\hookrightarrow L^\infty.
\]

Hence

\[
\boxed{
\sup_{S(\tau)}\rho^2
\le C_aE_R
\qquad(-T\le\tau\le0).
}
\]

In particular at the ancestor time,

\[
\boxed{
\rho_-^2(a)\le C_aE_R
\qquad(a\in S^-:=S(-T)).
}
\]

This is the RMS-spectral replacement for the pointwise-potential relative-thickness estimate used in the original M17-155 formulation.

---

## 4. M17-218 strain-gap lower bound

Suppose the selected M17-218 branch is the strain-gap branch.

Define

\[
I_T(a)
:=\int_{-T}^{0}
\Gamma_\Sigma(\Phi(a,\tau),\tau)d\tau,
\]

where

\[
\Gamma_\Sigma
:=\lambda_{max}(\Sigma)-\lambda_{min}(\Sigma).
\]

For a fixed `L>0`, M17-218 supplies a material subfamily with

\[
I_T\ge L
\]

and ancestor enstrophy

\[
E_-(S^-)
\ge c_0E_R.
\]

Therefore

\[
\boxed{
\mathcal A_T
:=\int_{S^-}\rho_-^2I_Tda
\ge c_0LE_R.
}
\]

This is the lower bound to be tested against quietness.

---

## 5. Rewrite the same action by the material map

Using the ancestor amplitude ceiling,

\[
\begin{aligned}
\mathcal A_T
&=\int_{S^-}\rho_-^2(a)
\int_{-T}^{0}\Gamma_\Sigma(\Phi(a,\tau),\tau)d\tau\,da\\
&\le C_aE_R
\int_{-T}^{0}\int_{S^-}
\Gamma_\Sigma(\Phi(a,\tau),\tau)da\,d\tau.
\end{aligned}
\]

For the `B`-flow,

\[
\det D_a\Phi(\tau,-T,a)
=e^{3(\tau+T)/2}.
\]

Hence, with `x=Phi(a,tau)`,

\[
da=e^{-3(\tau+T)/2}dx
\le dx.
\]

Therefore

\[
\boxed{
\mathcal A_T
\le C_aE_R
\int_{-T}^{0}\int_{S(\tau)}
\Gamma_\Sigma(x,\tau)dx\,d\tau.
}
\]

No pointwise `kappa` bound and no transported enstrophy density comparison are used in this change of variables.

---

## 6. Quiet shell bound makes the action subcritical

Since `Sigma` is symmetric,

\[
\Gamma_\Sigma
\le2\|\Sigma\|_{op}
\le2|\Sigma|.
\]

Cauchy-Schwarz in spacetime gives

\[
\begin{aligned}
\int_{-T}^{0}\int_{S(\tau)}\Gamma_\Sigma
&\le
2\left(\int_{-T}^{0}|S(\tau)|d\tau\right)^{1/2}
\left(\int_{-T}^{0}\int_{S(\tau)}|\Sigma|^2dx\,d\tau\right)^{1/2}\\
&\le
2(TV_T^*)^{1/2}
\left(\int_{-T}^{0}\int_{C_R(\tau)}|\Sigma|^2dx\,d\tau\right)^{1/2}.
\end{aligned}
\]

The M17-155 quiet corridor satisfies

\[
\boxed{
\int_{-T}^{0}\int_{C_R(\tau)}|\Sigma|^2dx\,d\tau
\le\frac{C_T}{R}.
}
\]

Consequently

\[
\boxed{
\mathcal A_T
\le
C_{T,a,V}E_RR^{-1/2}.
}
\]

Thus

\[
\boxed{
\frac{\mathcal A_T}{E_R}\to0
\qquad(R\to\infty).
}
\]

---

## 7. Contradiction with a fixed strain-gap payment

The M17-218 action branch requires

\[
\frac{\mathcal A_T}{E_R}
\ge c_0L>0,
\]

whereas Section 6 gives

\[
\frac{\mathcal A_T}{E_R}
\le C R^{-1/2}\to0.
\]

Therefore, for sufficiently remote shells,

\[
\boxed{
H_{fixed\text{-}fraction\ strain\ spectral\ gap\ action}
\Longrightarrow\bot
}
\]

on the relative-thick compact quiet bounded-carrier-RMS lane.

---

## 8. Strengthened ancestry gate

Combining M17-218 with Section 7 gives

\[
\boxed{
G_{fixed\text{-}fraction\ high\ anisotropy}^{quiet,compact}
\Longrightarrow
G_{ancestor\ high\ anisotropy}
\lor
G_{carrier\text{-}local\ H2/L2\ spectral}
\lor
G_{thin/decompactification/interface}.
}
\]

The strain-gap action is no longer a terminal branch on this lane.

If the carrier-local spectral ratio stays bounded, only ancestor anisotropy survives.

---

## 9. Fixed divergent thresholds propagate backward

Suppose current fixed-fraction thresholds satisfy

\[
K_R\to\infty.
\]

For any fixed `L`, the ancestor branch gives

\[
K_R^-
\ge K_Re^{-L}
\to\infty.
\]

Thus a divergent fixed-fraction anisotropy threshold cannot be generated during one quiet fixed-lag passage.

It must already be present in the ancestor packet unless the carrier enters the spectral or geometric hard exits.

---

## 10. Relation to M17-219

M17-219 is required before applying this result.

If the divergent director-metric second moment is carried by a vanishing-enstrophy microcarrier, there is no fixed positive carrier fraction and the lower bound in Section 4 is unavailable.

Therefore the correct routing is

\[
\boxed{
G_{director\ metric^2}^{quiet,compact}
\Longrightarrow
G_{director\text{-}metric\ microcarrier}
\lor
G_{ancestor\ high\ anisotropy}
\lor
G_{carrier\text{-}local\ spectral}
\lor
G_{thin/decompactification/interface}.
}
\]

The first and third terms may overlap after further localization; they are not declared independent payers.

---

## 11. DSD analysis

### 11.1 Same quantity on both sides

The lower and upper estimates concern the identical material functional

\[
\int_{S^-}\rho_-^2I_Tda.
\]

No Eulerian strain integral is substituted for it without the exact flow-map change of variables.

### 11.2 Why the factor `R^-1/2` appears

Quietness supplies an `L2` spacetime strain cost of order `R^-1`.
The packet spacetime volume is `O(1)` on fixed lag.
Cauchy-Schwarz therefore gives an `L1` strain-gap action of order `R^-1/2`.
Relative thickness contributes only the common shell mass factor `E_R`.

### 11.3 Scope

The closure requires:

- fixed positive enstrophy fraction;
- compact packet volume on fixed lag;
- relative-thick amplitude ceiling;
- bounded carrier-local RMS spectral ratio;
- the M17-155 quiet strain estimate.

Failure of any item is exported explicitly rather than absorbed into the contradiction.

---

## 12. DSD audit

- No pointwise `kappa` ceiling is used.
- The material Jacobian, not an assumed incompressible similarity flow, is used; `div B=3/2` is retained exactly.
- `Gamma_Sigma` is bounded by the strain norm only after preserving the material-set integral.
- The microcarrier branch of M17-219 is not falsely closed by this fixed-fraction argument.
- Infinite backward ancestry is not claimed to be contradictory here.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
