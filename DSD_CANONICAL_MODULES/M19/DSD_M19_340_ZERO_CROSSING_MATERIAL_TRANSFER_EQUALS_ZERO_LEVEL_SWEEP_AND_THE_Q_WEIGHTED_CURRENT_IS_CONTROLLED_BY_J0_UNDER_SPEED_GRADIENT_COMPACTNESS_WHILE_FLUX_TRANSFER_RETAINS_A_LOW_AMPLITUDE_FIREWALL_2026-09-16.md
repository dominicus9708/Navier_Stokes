# DSD M19-340 — Zero-crossing material transfer is a zero-level sweep; the q-weighted current is controlled by J0 under speed/gradient compactness while raw flux transfer retains a low-amplitude firewall

Date: 2026-09-16  
Canonical ID: **M19-340**

Status: **ACTIVE ZERO-SWEEP BRIDGE / CONDITIONAL MATERIAL-CURRENT TO J0 REDUCTION / LOW-AMPLITUDE FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-339

M19-339 defines the signed material sign-transfer currents

\[
C_0^\Phi
=\int\delta(\kappa)h\,d\Phi,
\qquad
C_0^Q
=\int\delta(\kappa)h q\,d\Phi,
\]

where

\[
h=D_t\kappa,
\qquad
q=r^2\rho.
\]

These currents exchange material labels between the \(\kappa>0\) and \(\kappa<0\) sectors and cancel from the total M17-442 flux/quadratic currencies.

M17-459 instead uses the positive zero-level diffusion current

\[
J_0
=\int\rho^2\delta(\kappa)|\nabla\kappa|^2dx
=\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|dS.
\]

M19-339 correctly retained a firewall between these objects. The present module gives a conditional geometric bridge.

## 2. Regular transverse cross-section

Fix a coherent regular vortex-tube chart and a transverse cross-section \(A(t)\) whose normal is the retained positive vorticity direction.

Exact CE-H gives

\[
D_\xi\kappa=0,
\]

so at regular points the coefficient gradient is transverse to the vortex line. Let

\[
Z_A(t):=A(t)\cap\{\kappa=0\}
\]

be the regular zero curve in the cross-section.

The positive material flux measure on \(A\) is

\[
d\Phi=\rho\,dA.
\]

Failure of the coherent transverse chart or of regularity of the zero set is retained as an explicit chart/interface/critical-level exit.

## 3. Material-relative normal speed of the zero level

Along a material trajectory, a point on the zero level satisfies

\[
\kappa=0.
\]

If the zero level moves relative to the material coordinates with transverse normal speed \(v_0\), the level-set kinematic identity is

\[
0=h+v_0|\nabla\kappa|.
\]

Therefore

\[
\boxed{
v_0=-\frac{h}{|\nabla\kappa|}.
}
\]

This is the exact coefficient-sign crossing speed in material coordinates.

## 4. Coarea representation of the sign-transfer flux current

On the cross-section,

\[
C_{0,A}^\Phi
:=\int_A\delta(\kappa)h\rho\,dA.
\]

By the two-dimensional coarea formula and the transverse-gradient identity,

\[
\boxed{
C_{0,A}^\Phi
=
\int_{Z_A}\frac{h\rho}{|\nabla\kappa|}d\ell
=
-\int_{Z_A}\rho v_0\,d\ell.
}
\]

Thus the signed flux transfer is literally the positive vorticity-flux density swept by the moving coefficient-zero curve.

## 5. Coarea representation of the q-weighted current

Likewise

\[
C_{0,A}^Q
:=\int_A\delta(\kappa)h q\rho\,dA.
\]

Since \(q=r^2\rho\),

\[
\boxed{
C_{0,A}^Q
=
r^2\int_{Z_A}\frac{h\rho^2}{|\nabla\kappa|}d\ell
=
-r^2\int_{Z_A}\rho^2v_0\,d\ell.
}
\]

This current has the same quadratic amplitude weight as the M17-459 zero-current density and is therefore much closer to \(J_0\) than \(C_0^\Phi\) is.

## 6. Cross-sectional positive zero-current density

Define

\[
\boxed{
j_{0,A}
:=
\int_{Z_A}\rho^2|\nabla\kappa|\,d\ell.
}
\]

Under a regular flux-line foliation with bounded chart Jacobians, integrating \(j_{0,A}\) along the represented line/arclength coordinate reconstructs the corresponding portion of

\[
J_0
=
\int_{\{\kappa=0\}}\rho^2|\nabla\kappa|dS
\]

up to the certified chart-comparability constants.

This disintegration is conditional on the coherent zero sheet / transverse-chart representation and is not asserted across chart degeneration or line reconnection.

## 7. q-weighted transfer is controlled by j0 under speed/gradient compactness

Assume on the regular zero curve

\[
|v_0|\le V_*,
\qquad
|\nabla\kappa|\ge g_*>0.
\]

Then

\[
\int_{Z_A}\rho^2d\ell
\le
\frac1{g_*}j_{0,A}.
\]

Therefore

\[
\boxed{
|C_{0,A}^Q|
\le
r^2\frac{V_*}{g_*}j_{0,A}.
}
\]

In own-scale normalized coordinates the prefactor is dimensionless after the corresponding normalized speed/gradient variables are used.

Hence persistent large amplitude-weighted sign transfer cannot remain independent of the positive zero-current unless either the zero-level crossing speed decompactifies, the regular-level gradient degenerates, or the chart representation fails.

## 8. Raw flux transfer has an additional amplitude firewall

For the unweighted sign-transfer flux current,

\[
|C_{0,A}^\Phi|
\le
V_*\int_{Z_A}\rho\,d\ell.
\]

The positive current \(j_{0,A}\) controls \(\rho^2\), not \(\rho\).

If the zero curve also has an amplitude floor

\[
\rho\ge\rho_*>0,
\]

then

\[
\rho\le\frac{\rho^2}{\rho_*},
\]

and therefore

\[
\boxed{
|C_{0,A}^\Phi|
\le
\frac{V_*}{\rho_*g_*}j_{0,A}.
}
\]

Without such an amplitude floor, this implication is false in general. A long low-amplitude zero corridor may carry substantial material label transfer relative to its \(\rho^2\)-weighted \(J_0\) cost.

Thus the exact firewall is

\[
\boxed{
C_0^\Phi\to J_0
\text{ requires zero-level amplitude retention in addition to speed/gradient compactness.}
}
\]

## 9. Cauchy--Schwarz version without pointwise speed bound

The flux-transfer identity also yields

\[
|C_{0,A}^\Phi|^2
\le
\left(
\int_{Z_A}\rho^2|\nabla\kappa|d\ell
\right)
\left(
\int_{Z_A}\frac{h^2}{|\nabla\kappa|^3}d\ell
\right).
\]

Hence

\[
\boxed{
|C_{0,A}^\Phi|^2
\le
j_{0,A}\,\mathcal V_{0,A},
\qquad
\mathcal V_{0,A}
:=
\int_{Z_A}\frac{h^2}{|\nabla\kappa|^3}d\ell.
}
\]

This gives an alternative exact split:

\[
\text{large signed material transfer}
\Longrightarrow
\text{large positive zero-current}
\lor
\text{large zero-level speed/high-jet currency}.
\]

The second factor is not yet assigned to a finite ancestral budget.

## 10. Relation to M17-339 and M17-470

M17-339 gives

\[
h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom}.
\]

Thus loss of the speed bound \(|v_0|=|h|/|\nabla\kappa|\) is itself a concrete constitutive exit through weighted coefficient diffusion, strain trace, geometry source, or critical-level gradient degeneration.

M17-470 shows that, under uniform zero-tube level-current stability and a coefficient-gradient ceiling,

\[
J_0\lesssim H_{\rm raw}.
\]

Therefore, on the fully compact zero-tube/speed/gradient/amplitude branch,

\[
\boxed{
C_0^Q\ \text{and}\ C_0^\Phi
\quad\text{are reduced to the already known }J_0/raw\text{-}H^2\text{ architecture.}
}
\]

This remains cubic-ancestry summable by M17-467/472 and is a branch compression, not a contradiction.

## 11. Updated zero-transfer frontier

The M19-339 amplitude-biased crossing branch now splits as

\[
\boxed{
\begin{aligned}
G_{\rm zero\text{-}crossing\ sign\ transfer}
\Longrightarrow{}&
G_{J_0/raw\text{-}H^2}^{R^{-3}\ \rm summable}\\
&\lor G_{\rm low\text{-}amplitude\ zero\ corridor}\\
&\lor G_{\rm zero\text{-}level\ speed/high\text{-}jet}\\
&\lor G_{\rm critical\text{-}level/gradient\ degeneration}\\
&\lor G_{\rm chart/interface/genealogy\ loss}.
\end{aligned}
}
\]

Thus the difficult survivor is again not generic zero crossing. It is low-amplitude or high-speed/degenerate zero-level transport, or an ancestry-summability problem.

## 12. Audit verdict

**PASS — the signed material sign-transfer current is geometrically identified as zero-level sweep.**

The amplitude-weighted current \(C_0^Q\) is controlled by the positive zero-current under speed/gradient compactness. The raw flux current \(C_0^\Phi\) needs the additional zero-level amplitude floor; failure is the precise low-amplitude corridor escape.

The result does not overturn the cubic ancestry firewall. It identifies the exact new survivor to attack: persistent low-amplitude zero-level transport versus sign-resolved flux-amplitude collapse.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
