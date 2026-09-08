# DSD M17-432 — Flux-weighted label-state occupation removes pure selected-label turnover only for flux-linear snapshot payers

Date: 2026-09-08  
Canonical ID: **M17-432**

Status: **ACTIVE LABEL-TURNOVER REDUCTION WITH QUADRATIC-PAYER FIREWALL / CORRECTED SCOPE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction notice

The first version of M17-432 correctly constructed a flux-weighted occupation measure, but it overextended the conclusion to the M17-413--420 raw-`H2` packet mechanism.

That extension is not valid without an additional anti-fragmentation hypothesis because the M17-413 segment payer is quadratic in flux:

\[
h_{seg}^{norm}\gtrsim c\phi^2.
\]

For fragmented label bands,

\[
\sum_i\phi_i^2
\neq
\left(\sum_i\phi_i\right)^2
\]

and may become arbitrarily small relative to the square of total retained flux.

Therefore the occupation theorem below is retained exactly for **flux-linear snapshot-additive currencies**. Its raw-`H2` application is quarantined unless quadratic flux concentration is separately controlled.

## 2. Material label space and positive flux measure

Let `Lambda` be a coherent material label space for regular CE-H vortex loops/tubes.

At similarity time `theta`, let

\[
d\Phi_\theta(\lambda)\ge0
\]

be the oriented positive flux measure on the retained label family, with

\[
\boxed{
0<\Phi_*
\le
\Phi_{tot}(\theta)
:=
\int_\Lambda d\Phi_\theta
<\infty.
}
\]

Normalize

\[
\boxed{
dp_\theta
=
\frac{d\Phi_\theta}{\Phi_{tot}(\theta)}.
}
\]

Then `p_theta` is a probability measure on the material label space.

## 3. Compact label-state bundle

Let

\[
Z_\lambda(\theta)
\]

be the represented state of label `lambda` and assume

\[
(\lambda,Z_\lambda(\theta))
\]

remains in a compact metric state bundle `K`.

If compactness fails, retain the corresponding amplitude, geometry, coefficient-scale, interface, genealogy, or domain decompactification exit.

## 4. Flux-weighted spacetime occupation probability

Define

\[
\boxed{
\mu_T
=
\frac1T
\int_0^T
(\lambda,Z_\lambda(\theta))_\#p_\theta\,d\theta.
}
\]

Every `mu_T` is a probability measure on compact `K`. Hence along a sequence

\[
T_j\to\infty
\]

we have

\[
\boxed{
\mu_{T_j}\rightharpoonup^*\mu
}
\]

for a probability measure `mu`.

## 5. Countable robust classes

Suppose

\[
K=\bigcup_{n\ge1}\mathcal G_n
\]

where each `G_n` is open and robust.

Because `mu(K)=1`, some fixed class satisfies

\[
\boxed{
\mu(\mathcal G_{n_*})=\beta_*>0.
}
\]

Portmanteau gives

\[
\boxed{
\liminf_{j\to\infty}
\mu_{T_j}(\mathcal G_{n_*})
\ge\beta_*.
}
\]

Therefore a fixed state class has positive flux-weighted time-label occupation even when every individual material label has zero asymptotic time density.

## 6. Exact theorem for flux-linear snapshot payers

Let a nonnegative snapshot payer have the form

\[
Q(\theta)
=
\int_\Lambda q(\lambda,Z_\lambda(\theta))\,d\Phi_\theta(\lambda)
\]

with

\[
q\ge q_{n_*}>0
\]

on `G_n*`.

Then

\[
Q(\theta)
\ge
q_{n_*}
\int_\Lambda
\mathbf1_{\mathcal G_{n_*}}
\,d\Phi_\theta.
\]

Since

\[
\Phi_{tot}(\theta)\ge\Phi_*,
\]

we obtain

\[
\boxed{
\liminf_{j\to\infty}
\frac1{T_j}
\int_0^{T_j}Q(\theta)d\theta
\ge
q_{n_*}\Phi_*\beta_*>0.
}
\]

Thus **pure selected-label turnover cannot erase a flux-linear snapshot-additive payer** on a compact positive-flux label-state bundle.

This applies directly to the flux-linear zero-crossing/current currencies of M17-323/326/340/346/358 when their uniform per-label hypotheses hold.

## 7. Quadratic raw-H2 firewall

The M17-413 loop raw-`H2` packet is not flux-linear.

For disjoint flux bands with fluxes `phi_i`, the normalized segment payments add as

\[
\boxed{
H^{norm}_{packet}
\gtrsim
c\sum_i\phi_i^2.
}
\]

Define the effective flux participation number

\[
\boxed{
N_{eff}
:=
\frac{\left(\sum_i\phi_i\right)^2}
{\sum_i\phi_i^2}
\ge1.
}
\]

Then

\[
\boxed{
\sum_i\phi_i^2
=
\frac{\Phi_{tot}^2}{N_{eff}}.
}
\]

Therefore fixed total positive flux does **not** give a uniform quadratic raw-`H2` lower bound unless `N_eff` is controlled.

As `N_eff -> infinity`, the raw-`H2` packet may be diluted by arbitrarily fine flux fragmentation even though the flux-linear occupation measure remains nondegenerate.

## 8. Corrected application to M17-420

M17-420 remains valid for its stated retained single-loop positive-flux branch.

The present M17-432 does **not** automatically extend that raw-`H2` contradiction to an arbitrarily fragmented positive-flux family.

Such an extension requires at least one additional hypothesis, for example:

\[
\boxed{N_{eff}\le N_*<\infty,}
\]

or an equivalent lower bound on quadratic flux concentration, or a fixed positive-flux band carrying positive occupation.

Without such an input, `selected-label turnover + flux fragmentation` remains a genuine quadratic-payer escape even though pure turnover for linear currencies is closed.

## 9. History-dependent payer firewall

The occupation theorem also does not automatically apply to a history-dependent one-label identity such as M17-188 covariance.

M17-429--431 remain the correct treatment of that branch.

Thus there are now three distinct cases:

\[
\boxed{
\begin{aligned}
\text{flux-linear snapshot payer}
&\Rightarrow \text{turnover neutral},\\
\text{flux-quadratic snapshot payer}
&\Rightarrow N_{eff}\text{ dilution possible},\\
\text{history-dependent payer}
&\Rightarrow \text{same-label history required}.
\end{aligned}
}
\]

## 10. Corrected surviving exits

The selected-label branch is therefore

\[
\boxed{
\begin{aligned}
G_{selected\ label\ turnover}
\Longrightarrow{}&
G_{label/state\ noncompactness}\\
&\lor G_{positive\ total\ flux\ thinning/loss}\\
&\lor G_{quadratic\ flux\ dilution}\;(N_{eff}\to\infty)\\
&\lor G_{payer\ class/scale\ mismatch}\\
&\lor G_{history\ coherence\ loss}\\
&\lor G_{material\ genealogy/interface/CEH/domain\ loss}.
\end{aligned}
}
\]

Pure turnover alone is neutral only in the flux-linear snapshot case.

## 11. Relation to parent-to-record closure

This module remains a second-generation occupation theorem.

Any first-generation contradiction still requires a representation-safe parent-to-record map, bounded overlap, and the appropriate M17-307 or M17-405 ancestry weight.

Those dependencies remain OPEN.

## 12. DSD role

DSD is used only to separate linear measure additivity from quadratic concentration and from history-dependent lineage information.

The mathematics is ordinary measure normalization, weak-* compactness, Portmanteau, and the elementary identity defining `N_eff`.

## 13. Audit verdict

**PASS after scope correction.**

The flux-weighted occupation theorem is valid for flux-linear snapshot-additive currencies. The raw-`H2` extension requires a separate quadratic flux-concentration theorem and is not claimed here.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
