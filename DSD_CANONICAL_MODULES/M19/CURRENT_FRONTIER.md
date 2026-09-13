# M19 Current Frontier

**Date:** 2026-09-14  
**Current tip:** **M19-243**  
**Status:** ACTIVE CALCULATION / APERIODIC SIGNED-INVARIANT FRONTIER + BOUNDED-PERIOD CAVITY CORE + RADIAL-POLoidal BOUNDARY-SHELL RETURN FRONTIER / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical policy

M18 remains the frozen audit/reduction family. M19 is the active new-calculation/closure family. Historical modules remain authoritative for detailed derivations; this file records the latest theorem obligations and scope firewalls.

## 2. Aperiodic recurrent hard frontier

The certified recurrent hard machinery still forces

\[
\overline P_U\ge\mathcal P_*>0,
\qquad
\left\langle(K\Gamma W)^{3/2}\right\rangle\ge c_0\nu\mathcal P_*>0
\]

on the retained simultaneous W1 lane. M19-196--201 show that this does not yet yield an unsigned global contradiction. Therefore

\[
\boxed{\mathcal T_{aper}^{signed}}
\]

remains OPEN.

## 3. Finite hard resonance and physical-adjoint reduction — M19-211--230

On the complete hard bundle,

\[
B(q,\omega)=\sum_j e^{i\kappa_jq}b_j(\omega),
\qquad
\kappa L+\vartheta-m\alpha=2\pi n,
\]

with finite bounds

\[
|\kappa_j|\le K_q^*,
\qquad
|n|\le N_{res}.
\]

M19-211--223 establish parity/skew-crossing/Pfaffian/phase-gap reductions and the zero-q invariant-section firewalls.

M19-224--228 identify the critical primal/adjoint homogeneities

\[
W_{pr}\sim r^{-1}B,
\qquad
\Psi_{ad}\sim r^{-2}C,
\]

and exact Green flux

\[
\mathcal F_\infty=-\frac12\langle B,C\rangle_{S^2}.
\]

Arbitrary nonorthogonal adjoint-data solvability is Fredholm-circular. Remote transpose-scattering is invertible, but physical adjoint realization remains an interior problem.

M19-229--230 reduce that problem to the finite-spectator cavity Fredholm equation

\[
(I-\mathcal M_R^{ad})z_0=h_R,
\]

where \(\mathcal M_R^{ad}\) is compact. Large-R Poincare contraction does not follow.

## 4. Expanding-cavity dichotomy and fixed escape currency — M19-231--232

Normalized cavity unit modes satisfy

\[
\boxed{
\text{nonzero whole-space relative-periodic core limit}
\quad\lor\quad
\text{escape of all L2 mass from every fixed compact set}.}
\]

On the escape branch,

\[
\boxed{
\int_0^{S_j}\|\nabla w_j\|_2^2ds
\to\frac1{4\nu},
\qquad
\int_0^{S_j}\|\eta_j\|_2^2ds
\to\frac1{4\nu}.}
\]

Thus escape has a fixed H1/vorticity currency.

## 5. Vorticity boundary localization and shear payer — M19-233--235

Localized vorticity identities eliminate all intermediate radii \(1\ll r\ll R_j\). The double-zero weight gives

\[
\boxed{
|y|/R_j\to1
\text{ in the normalized vorticity-energy measure}.}
\]

The single-zero weight then yields

\[
\boxed{
\liminf_j\frac1{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2dSds
\ge\frac1{8\nu^2}.}
\]

So any escaping cavity obstruction requires a linearly growing no-slip shear payer.

## 6. Local layer is consistent; Rellich does not close it — M19-236--237

The natural dilation Rellich identity cancels pressure but leaves an O(R^2) dilation-action payer, so it gives no o(R) shear upper bound.

Near the boundary,

\[
z=\frac{R}{2\nu}(R-r)
\]

reduces the leading tangential layer to

\[
f_{zz}+f_z=0,
\qquad
f=1-e^{-z}.
\]

Hence the natural no-slip/vorticity thickness is

\[
\boxed{d_{BL}\asymp\nu/R.}
\]

This layer pays the exact H1 and shear scales found above. Local layer consistency is therefore not a contradiction.

## 7. Regular macroscopic bulk is closed — M19-238--239

With

\[
x=y/R_j,
\qquad
V_j=R_j^{3/2}w_j(R_jx),
\]

any regular macroscopic curl limit satisfies

\[
\partial_sZ+\frac12x\cdot\nabla Z+Z=0.
\]

Relative periodicity forces Z=0. The H(div) zero-normal-trace inherited from no-slip then forces every curl-free/divergence-free regular macroscopic weak limit to vanish as well.

Thus

\[
\boxed{\text{every nonzero regular macroscopic weak bulk limit is excluded}.}
\]

A survivor must use boundary concentration and/or scaled-derivative decompactification.

## 8. Velocity and vorticity boundary scales separate — M19-240

For a no-slip shell of physical thickness D,

\[
\int_{R-D<|y|<R}|w|^2
\le CD^2\int|\nabla w|^2.
\]

Under the fixed H1 currency, order-one velocity L2 mass cannot fit into D=o(sqrt(nu)). In particular it cannot collapse into the inner nu/R vorticity layer.

Thus a surviving weak-zero escape needs

\[
\boxed{
\text{outer velocity-carrying shell}
+\text{inner }\nu/R\text{ no-slip/vorticity sublayer}.}
\]

## 9. Bare toroidal cavity is uniformly stable — M19-241

For U=0, the toroidal pressure-free operator

\[
A_0=\nu\Delta-\frac12y\cdot\nabla-\frac12
\]

obeys the Gaussian conjugation

\[
\boxed{
e^{-|y|^2/(8\nu)}A_0e^{|y|^2/(8\nu)}
=\nu\Delta+\frac14-\frac{|y|^2}{16\nu}.}
\]

The harmonic-oscillator bound gives

\[
\boxed{\sup\sigma\le-1/2}
\]

uniformly in R. Hence no nonzero bare toroidal relative unit multiplier exists for any cavity radius, period, or rotational holonomy.

## 10. Full Gaussian energy isolates the true gap defects — M19-242

Let

\[
\rho=e^{-|y|^2/(4\nu)}.
\]

For the full background-coupled cavity equation,

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}\int\rho|w|^2
+\nu\int\rho|\nabla w|^2
+\frac12\int\rho|w|^2
={}&-\frac1{4\nu}\int\rho(U\cdot y)|w|^2\\
&-\int\rho w^TS_Uw\\
&-\frac1{2\nu}\int\rho\pi(y\cdot w).
\end{aligned}}
\]

The remote strain is genuinely lower order, but

\[
U\cdot y=A_r(q,\omega)+O(r^{-2})
\]

can remain order one in the critical radial channel. Pressure is also nonorthogonal in the Gaussian metric when radial/poloidal content is present.

Moreover the Gaussian weight exponentially suppresses the unweighted boundary shell, so a weighted spectral gap alone cannot exclude unweighted shell concentration.

## 11. Pressure defect reduces to radial/poloidal coupling — M19-243

Taking divergence of the linearized equation gives the exact bulk pressure source

\[
\boxed{
\Delta\pi
=-2\partial_iU_j\partial_jw_i.}
\]

Thus bulk pressure is not an independent forcing channel; it is generated by coefficient-gradient coupling.

At the no-slip boundary, normal momentum gives the pressure Neumann data schematically as

\[
\partial_n\pi
=\nu n\cdot\Delta w
-n\cdot\left(\frac y2+U\right)\cdot\nabla w,
\]

so the harmonic pressure component is driven by the same boundary derivatives already forced in M19-235--237.

Therefore the full Gaussian defect menu compresses to

\[
\boxed{
\text{critical radial transport }A_r
\quad\lor\quad
\text{radial/poloidal no-slip boundary-layer coupling}.}
\]

Pressure does not form an independent third branch.

A small remote bulk pressure source does not imply small cavity pressure because boundary Neumann data may remain large.

## 12. Current bounded-period frontier

The M19-230 cavity obstruction is now reduced to:

### B1. Core branch

\[
\boxed{
\mathcal T_{cav}^{core}:
\text{classify/exclude nonzero whole-space relative-periodic core limits and establish any hard-bundle membership bridge}.}
\]

### B2. Radial/poloidal boundary-shell return

\[
\boxed{
\mathcal T_{shell}^{rad-pol}:
\begin{array}{l}
\text{exclude a normalized weak-zero velocity shell that feeds the }\nu/R\text{ sublayer}\\
\text{and survives an O(1) relative period through critical radial transport }A_r\\
\text{or radial/poloidal boundary-pressure coupling.}
\end{array}}
\]

Pure bare toroidal return is closed by M19-241.

### B3. Scaled-derivative decompactification

\[
\boxed{
\mathcal T_{scaled-deriv}:
\text{control/reclassify loss of macroscopic scaled-curl compactness on interior annuli}.}
\]

## 13. Live theorem complex

\[
\boxed{
\mathcal T_{aper}^{signed}}
\]

remains OPEN for the aperiodic branch.

For bounded period,

\[
\boxed{
\mathcal T_{cav}^{core}
\cup
\mathcal T_{shell}^{rad-pol}
\cup
\mathcal T_{scaled-deriv}}
\]

remains OPEN.

The long-period branch conditionally merges into these or compactness loss by M19-205.

## 14. Final proof-chain certification remains open

Even if the live M19 theorem complex closes, global regularity still requires:

1. arbitrary-singularity entry certification (`ROOT-CERT`);
2. historical non-CE-H branches `CP-E`, `CP-S`, `CE-T`, `Migration`;
3. parent-to-late-branch alignment/nonreuse checks;
4. full beginning-to-end independent audit.

## 15. Permanent firewalls through M19-243

\[
\boxed{\text{cavity core limit}\neq\text{certified hard kernel without a membership bridge}},
\]
\[
\boxed{\text{relative vorticity boundary localization}\neq\text{velocity mass in the same thin layer}},
\]
\[
\boxed{\text{local }\nu/R\text{ layer consistency}\neq\text{global unit multiplier existence}},
\]
\[
\boxed{\text{zero regular macroscopic weak limit}\neq\text{strong L2 compactness}},
\]
\[
\boxed{\text{bare toroidal spectral gap}\neq\text{uniform stability of the full background-coupled cavity operator}},
\]
\[
\boxed{\text{Gaussian weighted gap}\neq\text{unweighted boundary-shell exclusion}},
\]
\[
\boxed{\text{small remote bulk pressure source}\neq\text{small cavity pressure defect}},
\]
\[
\boxed{\text{root-class merger}\neq\text{analytic closure}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-243.}}
\]
