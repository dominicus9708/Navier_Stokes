# DSD M5-360 — High-Vorticity Half-Hölder Direction Defect as a Necessary Geometric Survivor

Date: 2026-08-31

Status: **THE CONSTANTIN--FEFFERMAN / BEIRAO-DA-VEIGA--BERSELLI GEOMETRIC REGULARITY CRITERION IS INSERTED AS AN AXIS-PROPERTY GATE / ANY SINGULAR SURVIVOR MUST DEVELOP A HIGH-VORTICITY HALF-HOLDER DIRECTION DEFECT / THIS DEFECT IS FRACTIONAL AND MUST NOT BE IDENTIFIED AUTOMATICALLY WITH H1 DIRECTIONAL DISSIPATION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The axis-property analysis has repeatedly produced affine/filament anti-models whose vorticity direction is highly coherent.

This note inserts the classical geometric regularity theorem directly into the proof tree.

Let

\[
 \xi(x,t)=\frac{\omega(x,t)}{|\omega(x,t)|}
\]

on the nonzero-vorticity set.

## 2. External theorem used

Beirao da Veiga--Berselli (2002), improving Constantin--Fefferman, proves regularity under a geometric condition on the angle between vorticity directions in the high-vorticity region.

A particularly transparent sufficient condition is: there exist fixed constants \(K>0\), \(C<\infty\), and a fixed local distance \(\delta>0\) such that whenever

\[
 |\omega(x,t)|\ge K,
 \qquad
 |\omega(y,t)|\ge K,
 \qquad
 |x-y|\le\delta,
\]

one has

\[
 \boxed{
 |\xi(x,t)\times\xi(y,t)|
 \le
 C|x-y|^{1/2}.
 }
\]

Then the weak solution is strong/regular on the interval.

Thus a singular solution must violate every such uniform late-time half-Holder coherence bound.

## 3. Direction-defect descriptor

For a high-vorticity threshold \(K\) and local radius \(\delta\), define

\[
 \boxed{
 \mathfrak D_{1/2}(t;K,\delta)
 :=
 \sup_{\substack{x,y:\ |\omega(x,t)|,|\omega(y,t)|\ge K\\0<|x-y|\le\delta}}
 \frac{|\xi(x,t)\times\xi(y,t)|}{|x-y|^{1/2}}.
 }
\]

The geometric regularity theorem implies the necessary blow-up condition

\[
 \boxed{
 \text{singularity at }T_*
 \Longrightarrow
 \sup_{t<T_*}\mathfrak D_{1/2}(t;K,\delta)=\infty
 }
\]

for every fixed admissible high-vorticity threshold/radius formulation that would otherwise satisfy the theorem hypotheses.

More operationally, along a singular sequence there must exist high-vorticity pairs \((x_j,y_j,t_j)\) with

\[
 \boxed{
 \frac{\sin\theta_j}{\ell_j^{1/2}}\to\infty,
 \qquad
 \ell_j=|x_j-y_j|\to0.
 }
\]

## 4. First-hitting normalization

At a first-hitting stage with natural length \(r_j\), write

\[
 x=X_j+r_jY,
 \qquad
 y=X_j+r_jZ.
\]

Then

\[
 \frac{\sin\theta(x,y)}{|x-y|^{1/2}}
 =
 r_j^{-1/2}
 \frac{\sin\theta(Y,Z)}{|Y-Z|^{1/2}}.
\]

Define the normalized axis defect

\[
 \boxed{
 \mathfrak d_j(R)
 :=
 \sup_{\substack{Y,Z\in B_R\\\text{high normalized vorticity}}}
 \frac{|\xi_j(Y)\times\xi_j(Z)|}{|Y-Z|^{1/2}}.
 }
\]

The physical seminorm is

\[
 \boxed{
 \mathfrak D_{1/2}^{\rm phys}
 =r_j^{-1/2}\mathfrak d_j.
 }
\]

Hence a normalized order-one directional variation on a fixed first-hitting cell strongly violates the physical half-Holder regularity bound as \(r_j\to0\).

## 5. Formation split by defect scale

Let \(\ell_j\) be a pair scale where the defect is witnessed.

Write

\[
 \rho_j:=\frac{\ell_j}{r_j}.
\]

There are three useful regimes.

### A. Sub-natural defect

\[
 \rho_j\to0.
\]

If the angle change is \(\theta_j\), a smooth connecting path has typical directional gradient

\[
 |\nabla\xi|\gtrsim\frac{\theta_j}{\ell_j}.
\]

The directional viscous damping in the vorticity-magnitude equation is

\[
 \nu|\omega||\nabla\xi|^2.
\]

Relative to the natural derivative scale \(r_j^{-1}\), the factor is

\[
 \left(\frac{r_j}{\ell_j}\right)^2\theta_j^2.
\]

Thus sufficiently sharp sub-natural direction changes route to directional-diffusion/high-frequency H unless compensated by equally strong stretching/reformation.

### B. Natural-scale projective defect

\[
 \rho_j\asymp1.
\]

Then order-one or persistent angular mismatch is directly a same-scale projective/partner/axis-turning event already represented in the finite-stage projective ledgers.

### C. Supra-natural / inter-packet defect

\[
 \rho_j\to\infty
\]

inside a larger controlled parent window.

Then the failure concerns the relative orientation of distinct high-vorticity packets rather than roughness inside one natural core. It routes to the packet-network / spatial-turnover / remote-satellite geometry.

## 6. Critical firewall: half-Holder failure is not automatically H1 blow-up

One must not infer

\[
 \mathfrak D_{1/2}\to\infty
 \Longrightarrow
 \int|\nabla\xi|^2=\infty.
\]

For example, at a length \(\ell\), an angular variation

\[
 \theta(\ell)=\ell^{1/4}
\]

satisfies

\[
 \theta(\ell)\to0
\]

but

\[
 \frac{\theta(\ell)}{\ell^{1/2}}=\ell^{-1/4}\to\infty.
\]

Thus the geometric theorem exposes a genuinely fractional direction defect, not automatically an integer-derivative H event.

## 7. Existing average directional-dissipation estimate

For sufficiently decaying smooth initial data with integrable initial vorticity, Constantin--Fefferman also give the global estimate

\[
 \boxed{
 \nu\int_0^T\!\int |\omega|\,|\nabla\xi|^2\,dxdt
 \le C(u_0,\omega_0).
 }
\]

This proves that arbitrary directional bending cannot fill space-time without cost.

However, a highly localized fractional defect can have small H1 capacity in three dimensions. Therefore this finite weighted budget does not by itself contradict the required half-Holder failure.

It is best used as a packing constraint once the defect occupies a positive-capacity packet family.

## 8. Axis-property interpretation

The singular survivor must now satisfy an explicit geometric alternative:

\[
 \boxed{
 \text{high-vorticity axis coherence}
 \Longrightarrow
 \text{regularity},
 }
\]

so

\[
 \boxed{
 \text{singular survivor}
 \Longrightarrow
 D_{\xi,1/2}^{\rm frac}.
 }
\]

This is separate from the DSD audit and follows from a standard external regularity theorem.

The formation role is to determine where the fractional defect lives:

- within one natural core;
- between neighboring natural packets;
- across a remote packet network.

The axis-property role is to resolve the defect into amplitude-neutral axis turning, projective mismatch, or directional-diffusion compensation.

## 9. Updated master routing

Combining the current circulation and axis ledgers gives

\[
 \boxed{
 \text{singular survivor}
 \Longrightarrow
 H_{\rm strain/freq}
 \lor
 T_{\rm material/spatial}
 \lor
 D_{\xi,1/2}^{\rm frac}.
 }
\]

The new direction-defect leaf is not claimed independent forever. The next target is to prove that persistent/high-occupancy fractional defects either consume the finite weighted directional-dissipation budget or force the existing projective/turnover branches.

## 10. Audit verdict

### EXTERNAL STANDARD RESULT

- uniform high-vorticity half-Holder direction coherence implies regularity.

### DERIVED

- any singular survivor must violate such uniform coherence;
- defect scale splits naturally into sub-natural, natural, and inter-packet regimes;
- sub-natural sharp defects amplify directional viscous damping;
- natural defects overlap existing projective ledgers.

### FIREWALL

- half-Holder failure alone does not imply H1 divergence of \(\xi\).

### OPEN

- capacity/packing lower bound for a persistent family of fractional direction defects;
- conversion of that packing into a non-summable H/T charge;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
