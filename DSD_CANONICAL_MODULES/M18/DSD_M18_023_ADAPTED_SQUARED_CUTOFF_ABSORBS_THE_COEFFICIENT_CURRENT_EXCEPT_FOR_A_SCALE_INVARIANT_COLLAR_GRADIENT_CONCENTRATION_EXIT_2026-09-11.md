# M18-023 — Adapted squared cutoff absorbs the coefficient current except for a scale-invariant collar-gradient concentration exit

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / CUTOFF-CURRENT ABSORPTION / COLLAR-CONCENTRATION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-022 reduced the temporal flux-shape problem to the bulk identity

\[
\begin{aligned}
\dot B_\phi
&+\int\phi\rho^2\left(|L_\rho\kappa|^2+|h|^2\right)dx\\
={}&2\int\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx\\
&-\int\phi'(\kappa)h\rho^2|\nabla\kappa|^2dx\\
&+\int\phi\rho^2|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx,
\end{aligned}
\]

where

\[
h:=D_t\kappa.
\]

The unresolved cutoff current is

\[
\boxed{
\mathcal C_\phi
:=-\int\phi'(\kappa)h\rho^2|\nabla\kappa|^2dx.
}
\]

This module tests whether \(\mathcal C_\phi\) is an independent payer.

The result is that with an adapted squared cutoff, \(\mathcal C_\phi\) is absorbed into the favorable \(\rho^2|h|^2\) rate term plus one explicit collar-gradient concentration term. Under a scale-invariant normalized gradient ceiling, that collar term is controlled by the existing first-coefficient-jet resource on a slightly larger collar.

## 2. Fixed fractional collar cutoff

Fix a record coefficient width

\[
\delta_0>0.
\]

Choose constants

\[
0<a<b<1
\]

independent of the record, and choose

\[
\chi_0\in C_c^1((-b,b)),
\qquad
0\le\chi_0\le1,
\qquad
\chi_0\equiv1\text{ on }[-a,a].
\]

Define the scaled cutoff

\[
\chi(s):=\chi_0\!\left(\frac{s}{\delta_0}\right),
\qquad
\phi(s):=\chi(s)^2.
\]

Then

\[
|\chi'(s)|\le \frac{C_\chi}{\delta_0},
\]

with \(C_\chi\) independent of the record.

The transition collar is

\[
\boxed{
\mathcal K
:=
\left\{x:
 a\delta_0<|\kappa(x)|<b\delta_0
\right\}.
}
\]

The key DSD rule is that \(a,b,\chi_0\) are fixed once and for all. A record-dependent collar made artificially thinner is not allowed to manufacture a current blow-up.

## 3. Squared-cutoff Young absorption

Because

\[
\phi'=2\chi\chi',
\]

we have

\[
|\mathcal C_\phi|
\le
2\int_{\mathcal K}
|\chi\rho h|\,|\chi'\rho|\nabla\kappa|^2|\,dx.
\]

For every \(\varepsilon>0\), Young's inequality gives

\[
2AB\le\varepsilon A^2+\varepsilon^{-1}B^2.
\]

Therefore

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon
\int\phi\rho^2|h|^2dx
+
\frac{C_\chi^2}{\varepsilon\delta_0^2}
\int_{\mathcal K}
\rho^2|\nabla\kappa|^4dx.
}
\]

Thus the cutoff current does not force a derivative of \(h\). The only remaining issue is a quartic first-coefficient-jet collar term.

## 4. Scale-invariant collar-gradient parameter

Write

\[
g:=|\nabla\kappa|.
\]

Under Navier--Stokes record scaling,

\[
g_R=R^3g,
\qquad
\delta_{0,R}=R^2\delta_0.
\]

Hence

\[
\boxed{
\Gamma_{\mathcal K}
:=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{g^2}{\delta_0^3}
}
\]

is scale invariant.

On \(\mathcal K\),

\[
\frac{g^4}{\delta_0^2}
=
\left(\frac{g^2}{\delta_0^3}\right)
\delta_0 g^2
\le
\Gamma_{\mathcal K}\,\delta_0g^2.
\]

Therefore

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon
\int\phi\rho^2|h|^2dx
+
\frac{C_\chi^2}{\varepsilon}
\Gamma_{\mathcal K}\,\delta_0
\int_{\mathcal K}\rho^2g^2dx.
}
\]

This is the main cutoff-current inequality.

## 5. Outer-cutoff firewall

The factor \(\phi=\chi^2\) may be small on the transition collar, so the unweighted collar charge

\[
\int_{\mathcal K}\rho^2g^2dx
\]

must not be silently replaced by \(B_\phi\).

Choose a second cutoff \(\widetilde\chi\) satisfying

\[
\widetilde\chi\equiv1
\quad\text{on }\operatorname{supp}\chi',
\]

with support still contained in a fixed larger fraction of the same retained regular tube, and set

\[
\widetilde\phi:=\widetilde\chi^2.
\]

Then

\[
\boxed{
\int_{\mathcal K}\rho^2g^2dx
\le
B_{\widetilde\phi}(t)
:=
\int\widetilde\phi(\kappa)\rho^2g^2dx.
}
\]

Hence

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon H_\phi
+
C_{\chi,\varepsilon}
\Gamma_{\mathcal K}\,\delta_0
B_{\widetilde\phi},
}
\]

where

\[
H_\phi:=\int\phi\rho^2|h|^2dx.
\]

No division by \(\phi\) is used.

## 6. Compact-gradient consequence

Assume on a canonical normalized record family

\[
\boxed{
\Gamma_{\mathcal K}\le\Gamma_*<\infty,
\qquad
0<\delta_0\le\delta^*<\infty.
}
\]

Then

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon H_\phi
+C_*B_{\widetilde\phi},
}
\]

with \(C_*\) record independent in normalized coordinates.

Integrating over a normalized record interval \(I\),

\[
\boxed{
\int_I|\mathcal C_\phi|dt
\le
\varepsilon\int_IH_\phi dt
+C_*\int_I B_{\widetilde\phi}dt.
}
\]

The second term is a localized first-coefficient-jet spacetime charge and is therefore owned by the same M17-445/M18 inherited D3 resource whenever the outer cutoff remains inside the compact exact-CE-H coefficient bin used by that ledger.

Thus, on such a normalized compact family, the coefficient cutoff current is not an independent spacetime payer.

## 7. Ancestry firewall

The preceding conclusion is conditional on the canonical normalized family.

The instantaneous term \(\delta_0B_{\widetilde\phi}\) carries one extra coefficient/time scale relative to \(B_{\widetilde\phi}\). Therefore it must not be assigned an intrinsic \(R^{-5}\) ancestry class merely by dimensional naming.

What is certified is the recordwise domination

\[
\delta_{0,m}B_{\widetilde\phi,m}
\le
\delta^* B_{\widetilde\phi,m}
\]

under the explicit normalized compactness assumption \(\delta_{0,m}\le\delta^*\).

Consequently

\[
\sum_mR_m^{-5}
\int_I
\delta_{0,m}B_{\widetilde\phi,m}dt
\le
\delta^*
\sum_mR_m^{-5}
\int_I B_{\widetilde\phi,m}dt
<\infty
\]

whenever the inherited first-coefficient-jet genealogy applies.

This is an **effective inherited budget under normalized compactness**, not a new scale-homogeneous law for arbitrary rerecordings.

## 8. Explicit failure branch

If the cutoff current cannot be absorbed as above while the fixed-fraction collar and outer tube survive, then

\[
\boxed{
\Gamma_{\mathcal K}\to\infty.
}
\]

Equivalently,

\[
\boxed{
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}
\to\infty.
}
\]

This is a representation-safe normalized first-coefficient-jet concentration exit.

It is stronger than merely saying \(|\nabla\kappa|\to\infty\), because it compares the gradient to the natural coefficient width of the same record.

It is not yet an integrated payer. Pointwise/essential-sup gradient concentration still requires spatial or temporal thickness before it can be charged to the M17-445 ledger.

Hence

\[
\boxed{
G_{\rm coefficient\ cutoff\ current}
\Longrightarrow
G_{\rm absorbed\ rate+first\ jet}
\lor
G_{\rm normalized\ collar\ gradient\ concentration}
\lor
G_{\rm collar/tube/domain\ loss}.
}
\]

## 9. Differential inequality after absorption

Define

\[
A_\phi
:=
\int\phi\rho^2|L_\rho\kappa|^2dx,
\]

\[
R_\phi
:=
\int\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
\]

Suppose also the normalized strain-rate coefficient satisfies

\[
\boxed{
\frac{|\sigma|+|a_n|+\nu|\kappa|}{\delta_0}
\le M_*
}
\]

on the support of \(\phi\).

Then the strain term in M18-022 obeys

\[
\left|
2\int\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx
\right|
\le
C M_*\delta_0B_\phi.
\]

Combining this with Section 5 and choosing \(0<\varepsilon<1\),

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+A_\phi
+(1-\varepsilon)H_\phi\\
&\le
C M_*\delta_0B_\phi
+C_{\chi,\varepsilon}\Gamma_{\mathcal K}\delta_0B_{\widetilde\phi}
+R_\phi.
\end{aligned}
}
\]

Thus the cutoff current has disappeared as a separate channel.

The remaining genuinely new analytic obstruction is the source square \(R_\phi\), together with any loss of normalized strain/gradient/tube compactness.

## 10. Coefficient-time Gronwall form

Let

\[
d\vartheta:=\delta_0(t)dt.
\]

On a normalized family with bounded \(M_*\) and \(\Gamma_{\mathcal K}\), the preceding inequality has the schematic form

\[
\boxed{
\frac{d}{dt}B_\phi
+A_\phi+cH_\phi
\le
C\delta_0(B_\phi+B_{\widetilde\phi})+R_\phi.
}
\]

Hence, after controlling the nested first-jet observable on the same compact tube, the natural growth parameter is coefficient time \(\vartheta\), not raw physical time.

This is consistent with the invariant coefficient-time variable isolated in M18-021.

## 11. Relation to previous high-gradient exits

M18-019 already contained an upper-gradient/tube-loss branch when converting persistent level flux into raw-H2/enstrophy payment.

M18-023 sharpens the temporal version of that exit to the dimensionless collar parameter

\[
\Gamma_{\mathcal K}
=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}.
\]

Therefore the cutoff-current branch does not create a fundamentally new category. It returns to the already-recognized coefficient-gradient decompactification family, now with the correct record-scale normalization.

## 12. Updated local branch tree

Combining M18-019--023, the compact regular-tube robust-flux-loss branch becomes

\[
\boxed{
\begin{aligned}
G_{\rm robust\ flux\ loss}
\Longrightarrow{}&
G_{\rm spacetime\ palinstrophy}^{R^{-1}}\\
&\lor G_{\rm first\ coefficient\ jet/D3}^{R^{-5}}\\
&\lor G_{\rm second\ coefficient\ jet/D4}^{R^{-7}}\\
&\lor G_{\rm normalized\ collar\ gradient\ concentration}\\
&\lor G_{\rm strain/geometry\ source\ square}\\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\\
&\lor G_{\rm level\text{-}width/critical/tube/domain/genealogy\ loss}.
\end{aligned}
}
\]

The independent coefficient-cutoff-current branch is removed under the explicit adapted-cutoff and normalized-compactness hypotheses.

## 13. Audit verdict

### Certified

1. Choosing \(\phi=\chi^2\) permits direct Young absorption into the favorable \(\rho^2|D_t\kappa|^2\) term.
2. The residual collar term is exactly a quartic coefficient-gradient charge.
3. The dimensionless parameter \(|\nabla\kappa|^2/\delta_0^3\) is the correct scale-invariant collar-gradient compactness quantity.
4. Under a uniform bound on that parameter and a fixed fractional collar, the residual is controlled by a slightly larger first-coefficient-jet observable.
5. The cutoff current is therefore not an independent local channel on the compact normalized family.

### Not certified

1. An integrated payer from \(\Gamma_{\mathcal K}\to\infty\) without a thickness argument.
2. Control of the strain/geometry source square.
3. Control of strain/normal-stretch decompactification.
4. Any global ancestry contradiction.
5. Global 3D Navier--Stokes regularity.

## 14. Next target

The dominant unresolved term in the bulk rate identity is now

\[
\boxed{
R_\phi
=
\int\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
}
\]

M18-024 should audit this source square without violating the M17-463 provenance firewall.

The first question is whether the combination

\[
L_\rho\sigma+\mathcal R_{\rm geom}
\]

has an exact lower-order cancellation or divergence structure before any termwise estimate is attempted. Only if that fails should the source be decomposed into separately audited channels.
