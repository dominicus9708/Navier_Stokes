# DSD M19-355 — Away-from-zero coefficient sectors have nonthinning material flux on the scale-free bi-Lipschitz compact branch

Date: 2026-09-16  
Canonical ID: **M19-355**

Status: **ACTIVE COEFFICIENT-THRESHOLD FLUX THEOREM / M19-354 EXTENSION / ORIENTED-CURRENT UPGRADE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-458

On the persistent baseline diffuse good-time set \(G_R\), M17-458 gives

\[
K_+(t)\ge k_*>0,
\qquad
K_-(t)\ge k_*>0
\]

for retained late records, while total enstrophy satisfies

\[
E(t)=\int\rho^2dx\le E_*.
\]

On the compact coefficient branch assume

\[
\boxed{|\kappa|\le K_*<\infty.}
\]

The good-time occupation obeys

\[
|G_R|\ge\beta_*|J_R|
\asymp c\beta_*R^2.
\]

## 2. Extract fixed away-zero coefficient sectors

Choose

\[
\boxed{
\delta
:=
\frac{k_*}{2E_*}.
}
\]

For the positive sign,

\[
\int_{0<\kappa<\delta}
\kappa\rho^2dx
\le
\delta E_*
=
\frac{k_*}{2}.
\]

Hence

\[
\boxed{
\int_{\{\kappa\ge\delta\}}
\kappa\rho^2dx
\ge
\frac{k_*}{2}.
}
\]

Since \(\kappa\le K_*\), the enstrophy carried by this threshold sector satisfies

\[
\boxed{
E_{+,\delta}
:=
\int_{\{\kappa\ge\delta\}}\rho^2dx
\ge
\frac{k_*}{2K_*}
=:e_\delta>0.
}
\]

The same argument gives

\[
\boxed{
E_{-,\delta}
:=
\int_{\{\kappa\le-\delta\}}\rho^2dx
\ge e_\delta.
}
\]

Thus both away-zero coefficient sectors carry fixed enstrophy mass on every M17-458 good state.

## 3. They are line-label sectors

Exact CE-H gives

\[
D_\xi\kappa=0.
\]

Therefore \(\kappa\) is constant along each regular vortex line at a fixed time.

Hence the sets

\[
\boxed{
S_{+,\delta}:=\{\kappa\ge\delta\},
\qquad
S_{-,\delta}:=\{\kappa\le-\delta\}
}
\]

are unions of represented vortex-line labels.

The sparse-residence theorem M19-353/354 therefore applies to them exactly as it applied to sign sectors: the proof uses only line-label structure, a fixed sector enstrophy floor, material flux, and the transverse amplitude geometry.

## 4. Scale-free bi-Lipschitz compact branch

Assume the M19-354 retained geometry package:

1. baseline transverse size \(|A_R|\lesssim R\);
2. parent-length upper bound \(\ell_R\lesssim R\);
3. amplitude ceiling \(\rho\le M_\rho\);
4. size-normalized transverse chart
   \[
   F_R=\lambda_R\widetilde F_R,
   \qquad
   \lambda_R\asymp R^{1/2},
   \]
   with
   \[
   0<m_*\le s_i(D\widetilde F_R)\le M_*<\infty.
   \]

Then M19-354 supplies the uniform transverse log-Sobolev estimate required by M19-353.

## 5. Persistent threshold-flux thinning is impossible

Let

\[
\eta_{+,\delta}(t)
:=
\frac{\Phi_{+,\delta}(t)}{\Phi(t)}
\]

be the material-flux fraction carried by \(S_{+,\delta}\), and similarly for the negative threshold sector.

M19-353 applies with the fixed enstrophy floor \(e_\delta\).

If for some fixed small \(\eta_0>0\) the state

\[
\eta_{+,\delta}(t)\le\eta_0
\]

occupied a fixed positive fraction of \(G_R\) on infinitely many geometric records, then the ancestral palinstrophy lower bound would contain

\[
\gtrsim
\frac{1}{\eta_0^2\log R_m}
\]

per such record, whose sum diverges because \(\log R_m\asymp m\).

Therefore, apart from a time-occupancy thinning set whose weighted series is summable, there exists a fixed

\[
\boxed{\eta_*>0}
\]

such that on asymptotically full M17-458 good-time density,

\[
\boxed{
\eta_{+,\delta}(t)\ge\eta_*,
\qquad
\eta_{-,\delta}(t)\ge\eta_*.
}
\]

If this conclusion fails, one of the explicit M19-354 geometry/size/length/amplitude/genealogy exits must occur.

## 6. Flux-weighted coefficient actions are now order one

Define the sign-resolved material-flux coefficient actions

\[
A_+^\Phi(t)
:=
\int_{\{\kappa>0\}}
\kappa\,d\Phi,
\]

\[
A_-^\Phi(t)
:=
\int_{\{\kappa<0\}}
(-\kappa)\,d\Phi.
\]

On the threshold sectors,

\[
\kappa\ge\delta
\]

or

\[
-\kappa\ge\delta.
\]

Thus on the nonthinning threshold-flux times,

\[
A_+^\Phi
\ge
\delta\Phi_{+,\delta}
\ge
\delta\Phi_-\eta_*,
\]

and similarly

\[
A_-^\Phi
\ge
\delta\Phi_-\eta_*.
\]

Hence

\[
\boxed{
A_+^\Phi\ge a_*>0,
\qquad
A_-^\Phi\ge a_*>0
}
\]

on asymptotically full good-time density, where

\[
a_*:=\delta\Phi_-\eta_*.
\]

This is stronger than mere sign-flux nonthinning.

## 7. Upgrade of the M19-346 current

M19-339 gives

\[
\dot\Phi_+
=
\nu A_+^\Phi+C_0^\Phi,
\]

\[
\dot\Phi_-
=
-\nu A_-^\Phi-C_0^\Phi.
\]

M19-346 observed that recurrent nontrivial sign actions require an oriented zero-crossing current.

M19-355 now upgrades the compact branch: the coefficient actions are not merely nonzero in an averaged qualitative sense. They are bounded below by a fixed constant on a positive parent-time fraction.

Therefore, on every late record where the compact geometry branch survives,

\[
\boxed{
\int_{J_R}A_+^\Phi dt
\gtrsim R^2,
\qquad
\int_{J_R}A_-^\Phi dt
\gtrsim R^2,
}
\]

up to the explicitly quantified vanishing exceptional-time fraction.

## 8. Scope firewall

The result depends on the scale-free bi-Lipschitz compact branch through M19-354.

It is invalid to infer threshold-flux nonthinning from M17-458 sign moments alone. Without the transverse log-Sobolev geometry, a fixed enstrophy/coefficient moment can hide in a flux-thin high-residence subpopulation exactly as in M19-348.

Thus the alternatives are

\[
\boxed{
\begin{aligned}
G_{\rm away\text{-}zero\ coefficient\ sector}
\Longrightarrow{}&
G_{\rm nonthinning\ threshold\ material\ flux}\\
&\lor G_{\rm scale\text{-}free\ transverse\ distortion}\\
&\lor G_{\rm transverse\ size/line\ length\ excess}\\
&\lor G_{\rm amplitude/high\text{-}jet\ loss}\\
&\lor G_{\rm threshold\ state\ time\ thinning}\\
&\lor G_{\rm common\ section/genealogy/interface\ loss}.
\end{aligned}
}
\]

## 9. Audit verdict

**PASS — on the size-normalized bi-Lipschitz compact branch, both away-zero coefficient signs carry fixed material flux on typical M17-458 good times.**

The enstrophy-weighted sign moments can no longer be hidden in flux-thin high-residence subpopulations. Consequently the material-flux coefficient actions \(A_\pm^\Phi\) are order one on positive parent-time density, forcing an order-one integrated oriented zero-crossing current through the exact sign-flux balance.

The next step is to integrate that balance over one parent record and obtain a direct spacetime lower bound on the zero-level sweep currency

\[
\int dt\int_{\kappa=0}\rho|v_0|d\ell.
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
