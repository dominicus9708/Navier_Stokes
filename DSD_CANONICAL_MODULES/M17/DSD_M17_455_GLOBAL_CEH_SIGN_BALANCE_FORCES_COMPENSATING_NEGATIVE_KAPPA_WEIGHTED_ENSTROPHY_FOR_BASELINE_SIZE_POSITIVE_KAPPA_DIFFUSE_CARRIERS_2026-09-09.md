# DSD M17-455 — Global CE-H sign balance forces compensating negative-kappa weighted enstrophy for baseline-size positive-kappa diffuse carriers

Date: 2026-09-09  
Canonical ID: **M17-455**

Status: **ACTIVE SIGN-BALANCE THEOREM / DIFFUSE-CARRIER REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Whole-space CE-H identity

On the whole-space exact CE-H branch,

\[
\Delta\Omega_R=\kappa_R\Omega_R
\]

with sufficient decay for integration by parts.

Therefore

\[
\int\Omega_R\cdot\Delta\Omega_Rdx
=-\int|\nabla\Omega_R|^2dx.
\]

Hence

\[
\boxed{
P_R
:=\int|\nabla\Omega_R|^2dx
=-\int\kappa_R\rho_R^2dx.
}
\]

Define

\[
K_{-,R}:=\int(\kappa_R)_-\rho_R^2dx,
\qquad
K_{+,R}:=\int(\kappa_R)_+\rho_R^2dx.
\]

Then

\[
\boxed{
P_R=K_{-,R}-K_{+,R}.
}
\]

Since `P_R>=0`,

\[
\boxed{
K_{-,R}\ge K_{+,R}.
}
\]

This is an exact global sign-balance constraint.

## 2. Positive-kappa diffuse carrier

Consider a retained parent-length positive-flux carrier with

\[
\ell_R\ge c_\ell R,
\qquad
\Phi_R\ge\Phi_*>0.
\]

Assume that on the carrier

\[
\boxed{
\kappa_R\ge\kappa_*>0.
}
\]

Assume also a baseline-size transverse upper bound on the relevant coherent cross-sections,

\[
\boxed{
\mathfrak A_R(z)\le C_A R S_R,
}
\]

where `S_R>=1` measures area growth beyond the M17-450 record-linear baseline.

## 3. Enstrophy lower bound from flux and area

At each cross-section,

\[
Q_R(z)
:=\int_{A_z}\rho_R^2dA
\ge
\frac{\Phi_R^2}{\mathfrak A_R(z)}.
\]

Therefore

\[
E_{carrier,R}
\gtrsim
\int_{\Gamma_R}Q_R(z)dz
\gtrsim
\frac{\Phi_R^2\ell_R}{C_AR S_R}.
\]

Using the flux and length floors,

\[
\boxed{
E_{carrier,R}
\ge
\frac{c_E}{S_R}.
}
\]

For the minimal baseline `S_R=O(1)`, the diffuse carrier necessarily holds order-one enstrophy despite its low pointwise amplitude.

## 4. Positive coefficient moment

Since `kappa_R>=kappa_*` on the carrier,

\[
K_{+,R}
\ge
\int_{carrier}\kappa_R\rho_R^2dx
\ge
\kappa_*E_{carrier,R}.
\]

Hence

\[
\boxed{
K_{+,R}
\ge
\frac{c_+}{S_R}.
}
\]

The global CE-H sign identity then forces

\[
\boxed{
K_{-,R}
\ge
K_{+,R}
\ge
\frac{c_+}{S_R}.
}
\]

Thus a positive-kappa diffuse carrier cannot exist in isolation: it requires compensating negative-kappa weighted enstrophy elsewhere.

## 5. Baseline-size consequence

If

\[
S_R\le S_*<\infty,
\]

then

\[
\boxed{
K_{-,R}\ge c_->0.
}
\]

So every baseline-size positive-kappa diffuse record contains a fixed amount of negative-kappa weighted enstrophy somewhere in the whole-space CE-H profile.

This converts the negative-coefficient branch from a coefficient-only statement into an amplitude-weighted one under the positive-carrier hypotheses.

## 6. Combine with M17-454

M17-454 shows that a negative-kappa region with

\[
\kappa\le-\kappa_*<0,
\]

fixed enstrophy mass, and mesoscopic own-scale transverse thickness forces order-one palinstrophy and is ancestrally forbidden if persistent.

Therefore a baseline-size positive-kappa diffuse carrier can survive only if its required compensating negative weighted enstrophy escapes M17-454 through one or more of

\[
\boxed{
\begin{aligned}
&G_{negative\ mass\ confined\ to\ own\text{-}scale/thin\ regions},\\
&G_{negative\ coefficient\ magnitude\ approaching\ zero},\\
&G_{negative\ weighted\ mass\ concentrated\ in\ highly\ localized\ amplitude\ structures},\\
&G_{rapid\ zero/sign\ fragmentation},\\
&G_{time\ occupation\ thinning},\\
&G_{high\text{-}jet/chart/interface/genealogy\ loss}.
\end{aligned}
}
\]

Alternatively the positive carrier can avoid an order-one compensation requirement by taking

\[
S_R\to\infty,
\]

i.e. transverse area growth beyond the M17-450 baseline, so that its own positive coefficient moment falls like `1/S_R`.

## 7. Relation to the amplitude firewall

M17-367 remains important: a large negative coefficient alone does not imply a large amplitude-weighted payment.

M17-455 does not violate that firewall.

The weighted negative mass lower bound arises only because a baseline-size positive-kappa positive-flux carrier first forces an order-one positive weighted coefficient moment, and the exact whole-space CE-H integration-by-parts identity then demands compensation.

## 8. Updated sign split

\[
\boxed{
\begin{aligned}
H_{baseline\ diffuse\ positive\ flux}
\Longrightarrow{}&
H_{kappa\ near\ zero/zero\ corridor}\\
&\lor H_{negative\text{-}kappa\ carrier}\\
&\lor H_{positive\text{-}kappa\ carrier\ plus\ compensating\ negative\ weighted\ mass}\\
&\lor G_{extra\ transverse\ size\ dilution}\;(S_R\to\infty)\\
&\lor G_{coefficient/jet/interface/genealogy\ loss}.
\end{aligned}
}
\]

The third line is now constrained by M17-454 whenever the compensating negative mass becomes mesoscopically thick.

## 9. Audit verdict

**PASS — exact global CE-H sign balance couples positive and negative coefficient populations.**

A baseline-size positive-kappa diffuse carrier with fixed positive flux forces a fixed compensating negative-kappa weighted enstrophy mass somewhere in the profile. Persistent survival therefore pushes the negative mass toward thin/localized/fragmented structures or forces additional transverse size dilution.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
