# DSD M17-395 — Positive flux removes the low-amplitude firewall from the intrinsic log-`kappa` diffusion branch but returns the cost to entropy, strain, geometry, or interface sources

Date: 2026-09-08  
Canonical ID: **M17-395**

Status: **ACTIVE AMPLITUDE-RETURN ON POSITIVE-FLUX SUBBRANCH / LOG-DIFFUSION ESCALATION / SOURCE FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

M17-235 gives, on its intrinsic mean-dominated coefficient-gradient branch and absent a dimensionless pointwise gradient spike,

\[
\boxed{
\int_B
\rho^2|\nabla\kappa|^2dx
\gtrsim
M_B R^{-6},
}
\]

where

\[
M_B:=\int_B\rho^2dx
\]

and `R` is the intrinsic coefficient scale.

M17-394 converts this to

\[
\boxed{
D_{\log\kappa}(B)
:=
\int_B
\rho^2|\nabla\log|\kappa||^2dx
\gtrsim
M_B R^{-2}.
}
\]

The remaining M17-235/394 firewall is the possibility

\[
M_B\to0.
\]

The present module removes that firewall on a retained positive-flux tube subbranch.

## 2. Positive-flux own-scale geometry

Assume the same intrinsic scale-`R` cell contains a regular material vortex-tube segment with

\[
\ell_R\ge c_\ell R,
\qquad
A_R\le C_AR^2,
\]

and retained oriented vorticity flux

\[
|\Phi_R|\ge\Phi_*>0.
\]

M17-391 gives the snapshot enstrophy lower bound

\[
\boxed{
M_B
\ge
E_{tube}
\gtrsim
\frac{\Phi_*^2}{R}.
}
\]

This uses only Cauchy--Schwarz and the tube geometry.

If the positive flux, area, length, or tube identity is lost, retain the corresponding flux-thinning/geometry/interface/genealogy exit.

## 3. Positive flux removes the packet-mass factor

Insert the M17-391 lower bound into M17-394:

\[
D_{\log\kappa}(B)
\gtrsim
M_B R^{-2}
\gtrsim
\frac{\Phi_*^2}{R}R^{-2}.
\]

Therefore

\[
\boxed{
D_{\log\kappa}(B)
\gtrsim
\Phi_*^2R^{-3}.
}
\]

Equivalently, on the positive-flux subbranch,

\[
\boxed{
R^3D_{\log\kappa}(B)
\gtrsim
\Phi_*^2.
}
\]

Thus the low-amplitude firewall is absent on this branch.

The log-coefficient diffusion cannot be made cheap simply by shrinking the vorticity packet mass while fixed positive flux and own-scale tube geometry survive.

## 4. Own-scale time escalation

Assume the same scale-`R` diffusion/flux geometry persists on a physical interval

\[
|I_R|\ge c_t\frac{R^2}{\nu}.
\]

Then

\[
\int_{I_R}D_{\log\kappa}(B_t)dt
\gtrsim
\Phi_*^2R^{-3}|I_R|.
\]

Hence

\[
\boxed{
\nu
\int_{I_R}
D_{\log\kappa}(B_t)dt
\gtrsim
\Phi_*^2R^{-1}.
}
\]

This grows as `R -> 0`.

It is substantially stronger than the direct standard-energy flux cost from M17-391,

\[
\nu\int_{I_R}E_Tdt
\gtrsim
R\Phi_*^2.
\]

The derivative-level log-diffusion charge therefore escalates by two powers of the intrinsic scale relative to the standard-energy flux ledger.

## 5. Why this is not yet a contradiction

No globally finite first-generation budget has been certified for

\[
\int
\rho^2|\nabla\log|\kappa||^2dxdt.
\]

Therefore the lower bound

\[
\Phi_*^2R^{-1}
\]

cannot by itself be summed into a contradiction.

The next task is to use the exact M17-394 log-`kappa` identity to identify what must pay this growing derivative charge.

## 6. Intrinsic centered log coefficient

On a scale-`R` coefficient cell define

\[
\boxed{
\zeta_R
:=
\log(R^2|\kappa|).
}
\]

Since `R` is fixed during one scale-`R` accounting episode,

\[
\nabla\zeta_R
=
\nabla\log|\kappa|,
\qquad
D_t\zeta_R
=D_t\log|\kappa|.
\]

If

\[
c_\kappa R^{-2}
\le
|\kappa|
\le
C_\kappa R^{-2},
\]

then

\[
\boxed{
|\zeta_R|\le C_\zeta<\infty.
}
\]

This centered variable avoids inserting the irrelevant large offset `-2 log R` into the local entropy bookkeeping.

## 7. Centered log-entropy identity

Let `chi` be a material cutoff supported in the sign-preserving scale-`R` cell.

M17-394 gives, with `zeta_R` replacing `log |kappa|`,

\[
\boxed{
\begin{aligned}
\frac d{dt}
\int\chi\rho^2\zeta_Rdx
={}&
\int\chi\rho^2|\nabla\zeta_R|^2dx\\
&-
\int\rho^2\nabla\chi\cdot\nabla\zeta_Rdx\\
&+
\int\chi\rho^2
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}dx\\
&+
2\int\chi\rho^2(\sigma+\kappa)\zeta_Rdx.
\end{aligned}
}
\]

Define

\[
\mathcal H_R(t)
:=
\int\chi\rho^2\zeta_Rdx.
\]

Integrating over `I_R` and taking absolute values yields

\[
\boxed{
\begin{aligned}
\int_{I_R}D_{\log\kappa}(t)dt
\le{}&
|\Delta\mathcal H_R|\\
&+
\left|
\int_{I_R}
\int\rho^2\nabla\chi\cdot\nabla\zeta_Rdxdt
\right|\\
&+
\left|
\int_{I_R}
\int\chi\rho^2
\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}dxdt
\right|\\
&+
2\left|
\int_{I_R}
\int\chi\rho^2(\sigma+\kappa)\zeta_Rdxdt
\right|.
\end{aligned}
}
\]

Thus the positive log-diffusion cannot disappear; it must be balanced by endpoint entropy, cutoff/interface transport, normalized strain/geometric source, or amplitude-growth entropy.

## 8. Quantitative payer dichotomy on the positive-flux branch

Section 4 gives

\[
\int_{I_R}D_{\log\kappa}dt
\gtrsim
\frac{\Phi_*^2}{\nu R}.
\]

Therefore at least one term on the right side of Section 7 must satisfy

\[
\boxed{
\text{payer}
\gtrsim
c\frac{\Phi_*^2}{\nu R}
}
\]

up to the finite number of channels.

Schematically,

\[
\boxed{
\begin{aligned}
H_{positive\ flux+M17\text{-}235\ diffusion}
\Longrightarrow{}&
H_{large\ centered\ log\text{-}entropy\ change}\\
&\lor H_{large\ cutoff/interface\ flux}\\
&\lor H_{large\ normalized\ strain/geometric\ source}\\
&\lor H_{large\ amplitude\text{-}growth\ entropy}\\
&\lor G_{positive\ flux/own\text{-}scale\ persistence\ loss}.
\end{aligned}
}
\]

The old low-amplitude escape is absent while the positive-flux tube remains retained.

## 9. Endpoint entropy size

Because `|zeta_R|<=C_zeta`,

\[
|\mathcal H_R(t)|
\le
C_\zeta
\int_{supp\chi}\rho^2dx.
\]

Thus the endpoint entropy is controlled by the local packet enstrophy, not by an additional logarithmic coefficient factor.

On the positive-flux branch

\[
M_B\gtrsim\Phi_*^2/R,
\]

so an endpoint entropy of order `Phi_*^2/R` is dimensionally capable of paying one own-scale diffusion episode.

Therefore M17-395 does **not** claim an immediate contradiction.

A recurrence or bounded-entropy-return theorem would be needed to suppress repeated endpoint payment.

## 10. Repeated scale episodes

Suppose a same-genealogy positive-flux branch produces many scale-`R_j` episodes with the M17-235 diffusion lower bound.

Each episode forces a derivative-level payment

\[
\gtrsim
\frac{\Phi_*^2}{R_j}
\]

in one of the M17-395 source/entropy channels.

Unlike the standard energy cost `R_j Phi_*^2`, this grows on small scales.

Therefore any future theorem that provides a **scale-uniform finite or bounded-overlap budget** for the centered entropy/source side would close this subbranch very strongly.

No such budget is currently certified.

## 11. Relation to M17-190/361

M17-190 and M17-361 establish positive-flux compact recurrent loop families with nontrivial strain-gradient/palinstrophy payers on their stated subbranches.

If such a family also enters the M17-235 intrinsic coefficient-gradient branch at scale `R`, M17-395 shows that the amplitude-weighted multiplier-diffusion charge can no longer vanish through packet-mass collapse.

The remaining difficulty is source/entropy control, not amplitude return.

This is a genuine narrowing of that intersection branch.

## 12. Remaining exits

M17-395 does not apply if

- flux thins below a scale-uniform lower bound;
- tube area or length loses scale comparability;
- the M17-235 mean-dominated packet hypotheses fail;
- a dimensionless `grad kappa` spike occurs instead of the diffusion branch;
- the coefficient crosses zero;
- interface/rank/domain/genealogy loss occurs;
- the scale-`R` episode is too short to accumulate one own-scale time.

These remain explicit branches.

## 13. DSD audit role

The DSD role is an amplitude-resource audit.

M17-235 retained the packet mass `M_B` correctly.

M17-395 does not cancel it algebraically; it supplies an independent physical lower bound on `M_B` from retained vorticity flux and own-scale geometry.

This is the legitimate way to remove the amplitude firewall on the positive-flux subbranch.

The rest is standard Cauchy--Schwarz flux geometry plus the exact M17-394 entropy identity.

## 14. Audit verdict

**PASS — amplitude firewall removed on the retained positive-flux M17-235 subbranch.**

The key new scale law is

\[
\boxed{
\nu
\int_{I_R}
\int_B
\rho^2|\nabla\log|\kappa||^2dxdt
\gtrsim
\Phi_*^2R^{-1}.
}
\]

This is not yet a contradiction because the centered entropy/source side has no certified finite ancestral budget.

The next highest-value target is therefore a **source-return/entropy-return gate**: determine whether compact recurrence, bounded coefficient geometry, or the M17-190/361 loop structure prevents the same endpoint/source architecture from paying `Phi_*^2/R` independently at every shrinking scale.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
