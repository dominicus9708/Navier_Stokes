# M17-483 — Amplitude-normal zero-flux variation is paid by palinstrophy or preserves level flux without dividing by rho

**Date:** 2026-09-10  
**Status:** ACTIVE NODAL-SAFE ZERO-FLUX THEOREM / AMPLITUDE-NORMAL BRANCH REDUCTION

## 1. Purpose

M17-482 reduced the exact regular level-flux derivative to
\[
F'(s)
=
\int_{\Sigma_s}
\left[
2\rho\partial_n\rho
+\rho^2\frac{\Delta\kappa}{g}
\right]dS,
\qquad
g:=|\nabla\kappa|.
\]

The remaining amplitude term seemed to require the relative ratio \(\partial_n\rho/\rho\), which is singular at vorticity nodes.

This module avoids that division completely. A weighted Cauchy--Schwarz estimate sends rapid amplitude-normal variation to the bulk palinstrophy ledger; if that palinstrophy payment is small, the level flux persists quantitatively.

Thus **nodal amplitude-ratio degeneration is not an independent zero-flux payer in this estimate**.

## 2. Coefficient relative-Laplacian ceiling

Work in a regular transported coefficient tube and assume
\[
0<g=|\nabla\kappa|\le G_*.
\]
Assume also the coefficient ratio ceiling
\[
\boxed{
\left|\frac{\Delta\kappa}{g^2}\right|
\le L_\kappa.
}
\]
Then the coefficient contribution satisfies
\[
\left|
\int_{\Sigma_s}
\rho^2\frac{\Delta\kappa}{g}dS
\right|
\le
L_\kappa
\int_{\Sigma_s}\rho^2g\,dS
=L_\kappa F(s).
\]

## 3. Nodal-safe control of the amplitude-normal term

Define
\[
\boxed{
N(s):=
\int_{\Sigma_s}
\frac{|\partial_n\rho|^2}{g}\,dS.
}
\]
Weighted Cauchy--Schwarz gives
\[
\begin{aligned}
\left|
2\int_{\Sigma_s}\rho\partial_n\rho\,dS
\right|
&\le
2
\left(\int_{\Sigma_s}\rho^2g\,dS\right)^{1/2}
\left(\int_{\Sigma_s}\frac{|\partial_n\rho|^2}{g}\,dS\right)^{1/2}\\
&=2F(s)^{1/2}N(s)^{1/2}.
\end{aligned}
\]
Therefore M17-482 becomes
\[
\boxed{
|F'(s)|
\le
2F(s)^{1/2}N(s)^{1/2}
+L_\kappa F(s).
}
\]

No division by \(\rho\) occurs.

At vorticity nodes one may justify the calculation by the regularization
\[
\rho_\varepsilon=(|\Omega|^2+\varepsilon^2)^{1/2}
\]
and pass \(\varepsilon\downarrow0\). The Kato inequality gives
\[
|\nabla\rho|\le|\nabla\Omega|
\]
almost everywhere.

## 4. Square-root flux differential inequality

Let
\[
Z(s):=F(s)^{1/2}.
\]
Where \(F(s)>0\), Section 3 gives
\[
\boxed{
|Z'(s)|
\le
N(s)^{1/2}
+\frac{L_\kappa}{2}Z(s).
}
\]
The same estimate follows by regularizing \(F\) if a zero value is encountered.

For \(s\ge0\), the lower differential inequality is
\[
Z'(s)+\frac{L_\kappa}{2}Z(s)
\ge
-N(s)^{1/2}.
\]
Hence
\[
Z(s)
\ge
 e^{-L_\kappa s/2}Z(0)
-
 e^{-L_\kappa s/2}
\int_0^s e^{L_\kappa r/2}N(r)^{1/2}dr.
\]
By Cauchy--Schwarz,
\[
\int_0^s e^{L_\kappa r/2}N(r)^{1/2}dr
\le
 e^{L_\kappa s/2}s^{1/2}
\left(\int_0^sN(r)dr\right)^{1/2}.
\]
Therefore
\[
\boxed{
Z(s)
\ge
 e^{-L_\kappa s/2}J_0^{1/2}
-
s^{1/2}
\left(\int_0^sN(r)dr\right)^{1/2}.
}
\]
The analogous estimate holds for negative \(s\) using \(|s|\).

## 5. Coarea converts N into bulk palinstrophy

Because \(s=\kappa(x)\) and \(g=|\nabla\kappa|\), the coarea formula gives
\[
\int_{-\delta}^{\delta}N(s)ds
=
\int_{\{|\kappa|<\delta\}}
|\partial_n\rho|^2dx.
\]
Since
\[
|\partial_n\rho|\le|\nabla\rho|
\le|\nabla\Omega|
\]
almost everywhere,
\[
\boxed{
\int_{-\delta}^{\delta}N(s)ds
\le
P_{0,\delta}
:=
\int_{\{|\kappa|<\delta\}}|\nabla\Omega|^2dx
\le P.
}
\]

Thus the full amplitude-normal variation across the coefficient slab is owned by the existing palinstrophy resource.

## 6. Persistence-versus-palinstrophy dichotomy

Fix a regular tube width \(\delta>0\). If
\[
\boxed{
\delta P_{0,\delta}
\le
\frac14e^{-L_\kappa\delta}J_0,
}
\]
then for every \(|s|\le\delta\), Sections 4--5 give
\[
Z(s)
\ge
 e^{-L_\kappa\delta/2}J_0^{1/2}
-
\delta^{1/2}P_{0,\delta}^{1/2}
\ge
\frac12e^{-L_\kappa\delta/2}J_0^{1/2}.
\]
Hence
\[
\boxed{
F(s)
\ge
\frac14e^{-L_\kappa\delta}J_0
\qquad(|s|\le\delta).
}
\]

If the small-palinstrophy condition fails, then directly
\[
\boxed{
P_{0,\delta}
>
\frac1{4\delta}e^{-L_\kappa\delta}J_0.
}
\]

Therefore
\[
\boxed{
G_{J_0}^{\rm regular\ tube}
\Longrightarrow
G_{\rm level\text{-}flux\ persistence}
\lor
G_{\rm palinstrophy}.
}
\]
provided the coefficient ratio \(|\Delta\kappa|/|\nabla\kappa|^2\) remains bounded.

## 7. Raw-H2 consequence in the persistence case

Under the coefficient-gradient ceiling \(g\le G_*\), coarea gives
\[
H_{0,\delta}
=
\int_{-\delta}^{\delta}
s^2
\left(\int_{\Sigma_s}\frac{\rho^2}{g}dS\right)ds
\ge
G_*^{-2}
\int_{-\delta}^{\delta}s^2F(s)ds.
\]
Using Section 6,
\[
\boxed{
H_{0,\delta}
\ge
\frac16
G_*^{-2}e^{-L_\kappa\delta}\delta^3J_0.
}
\]

Thus the full nodal-safe dichotomy is
\[
\boxed{
G_{J_0}^{\rm regular\ tube}
\Longrightarrow
G_{\rm raw\text{-}H^2}
\lor
G_{\rm palinstrophy}
\lor
G_{L_\kappa\text{-}decompactification}
\lor
G_{g\text{-}ceiling/tube\ loss}.
}
\]

## 8. What is removed

The following branch is no longer independently needed in the zero-current audit:
\[
G_{\partial_n\rho/\rho\text{ relative-jet / nodal degeneration}}.
\]
The amplitude term is controlled without dividing by \(\rho\). Nodes may still matter elsewhere in the CE-H proof tree, but they do not create an independent obstruction to the M17-483 level-flux estimate.

## 9. Ancestry audit

The two payment alternatives are already certified ledgers:
\[
H_{0,\delta}\subset H_{\rm raw}
\quad\text{with ancestry weight }R_m^{-3},
\]
\[
P_{0,\delta}\subset P
\quad\text{with ancestry weight }R_m^{-1}.
\]
Therefore a fixed normalized \(J_0\) event still does not contradict geometric ancestry. M17-473 remains the threshold firewall.

## 10. Remaining zero-current exit

After M17-483, the genuinely new regular-tube coefficient quantity is
\[
\boxed{
L_\kappa
=\sup
\left|\frac{\Delta\kappa}{|\nabla\kappa|^2}\right|.
}
\]
Together with critical-level/tube loss, this is now the narrow zero-current geometric exit.

The next audit should test whether \(L_\kappa\) decompactification can itself be converted to the existing coefficient-gradient/high-jet ledger, or whether the denominator \(|\nabla\kappa|^2\) leaves a genuine critical-level ratio branch.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
