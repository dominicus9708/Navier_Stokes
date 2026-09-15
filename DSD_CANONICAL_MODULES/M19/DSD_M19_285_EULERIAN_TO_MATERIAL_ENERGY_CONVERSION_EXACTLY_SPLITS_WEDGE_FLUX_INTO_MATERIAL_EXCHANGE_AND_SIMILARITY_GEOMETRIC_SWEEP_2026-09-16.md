# M19-285 — Eulerian-to-material energy conversion exactly splits wedge flux into material exchange and similarity geometric sweep

**Date:** 2026-09-16  
**Status:** CALCULATION / EULERIAN-MATERIAL CONVERSION / RELATIVE-SWEEP DEFECT REMOVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-284 derives the kinetic-energy law for a cutoff transported by the similarity material velocity

\[
B=U+\frac12y.
\]

M19-283 instead localizes the M5-583 wedge energy current on fixed observation spheres/depths.

These geometries are different. The purpose of M19-285 is to derive the exact conversion and determine whether their mismatch creates a new untyped signed defect.

It does not. The mismatch is an explicit similarity geometric sweep.

## 2. Similarity conservation form

Let

\[
e=\frac12|U|^2.
\]

From M19-284,

\[
\partial_\theta e
+B\cdot\nabla e
+e
+\nabla\cdot(PU)
=\nu\Delta e-\nu|\nabla U|^2.
\]

Since

\[
\nabla\cdot B=\frac32,
\]

this becomes

\[
\boxed{
\partial_\theta e
+\nabla\cdot\mathcal F_B
=
\frac12e-\nu|\nabla U|^2,
}
\]

with the fixed-similarity-coordinate energy flux

\[
\boxed{
\mathcal F_B
:=
eB+PU-\nu\nabla e.
}
\]

Using \(B=U+y/2\),

\[
\boxed{
\mathcal F_B
=
\underbrace{(e+P)U-\nu\nabla e}_{J_0}
+
\frac12ey.
}
\]

The vector

\[
\boxed{J_0:=(e+P)U-\nu\nabla e}
\]

is the similarity representation of the physical local-energy current used by the wedge formulation.

Therefore

\[
\boxed{
\mathcal F_B-J_0=\frac12ey.
}
\]

## 3. Relation to M5-583 wedge current

At similarity radius

\[
R=|y|=z^{-1/2},
\]

the wedge variables satisfy

\[
F=RU,
\qquad
E_{wedge}=R^2e,
\qquad
H=R^2P.
\]

The M5-583 scale-normalized current

\[
\mathcal J=(E_{wedge}+H)F-\mathfrak G_2E_{wedge}
\]

is therefore

\[
\boxed{
\mathcal J
=R^3J_0
}
\]

with viscosity normalized consistently with the M5 convention.

Hence M19-283's radial wedge current is the physical current \(J_0\), not the full fixed-similarity flux \(\mathcal F_B\).

## 4. Material-population cutoff and fixed radial window

Let \(\eta(\theta,y)\) be a material population cutoff satisfying

\[
D_B\eta=0.
\]

Let \(\chi_R(y)\) be a fixed radial observation cutoff in similarity coordinates. Define

\[
\boxed{
E_{\eta,R}(\theta)
:=
\int\eta\chi_Re\,dy.
}
\]

A direct calculation gives

\[
\boxed{
\begin{aligned}
E_{\eta,R}'
={}&
\frac12E_{\eta,R}
-\nu\int\eta\chi_R|\nabla U|^2dy\\
&+\int\chi_R(PU-\nu\nabla e)\cdot\nabla\eta\,dy\\
&+\int\eta\mathcal F_B\cdot\nabla\chi_R\,dy.
\end{aligned}
}
\]

The three non-baseline channels are:

1. bulk dissipation;
2. pressure/viscous exchange across the material-population boundary;
3. energy flux through the fixed observation cutoff.

## 5. Sharp fixed-sphere form

For a sharp ball \(B_R\), with outward normal \(n\), define

\[
\Phi_B(R)
:=
\int_{S_R}\eta\mathcal F_B\cdot n\,dS,
\]

and

\[
\Phi_0(R)
:=
\int_{S_R}\eta J_0\cdot n\,dS.
\]

Since \(y\cdot n=R\),

\[
\boxed{
\Phi_B(R)
=
\Phi_0(R)
+
\frac R2
\int_{S_R}\eta e\,dS.
}
\]

Thus the relative Eulerian/material mismatch is the explicit nonnegative geometric shell term

\[
\boxed{
\Phi_{geom}(R)
:=
\frac R2\int_{S_R}\eta e\,dS.
}
\]

No unknown carrier-transport defect is hidden here.

## 6. Exact conversion formula

For the sharp material population inside \(B_R\), let

\[
X_\eta(R)
:=
\int_{B_R}(PU-\nu\nabla e)\cdot\nabla\eta\,dy.
\]

The local energy law gives

\[
E_{\eta,R}'
=
\frac12E_{\eta,R}
-\nu D_{\eta,R}
+X_\eta(R)
-\Phi_B(R),
\]

where

\[
D_{\eta,R}:=\int_{B_R}\eta|\nabla U|^2dy.
\]

Using \(\Phi_B=\Phi_0+\Phi_{geom}\),

\[
\boxed{
\Phi_0(R)
=
\frac12E_{\eta,R}
-\nu D_{\eta,R}
+X_\eta(R)
-E_{\eta,R}'
-\Phi_{geom}(R).
}
\]

This is the exact Eulerian-to-material conversion for the wedge-type radial energy current.

## 7. Recurrent invariant mean

If the marked localized energy is bounded/integrable on the recurrent hull,

\[
\langle E_{\eta,R}'\rangle=0.
\]

Hence

\[
\boxed{
\langle\Phi_0(R)\rangle
=
\frac12\langle E_{\eta,R}\rangle
-\nu\langle D_{\eta,R}\rangle
+\langle X_\eta(R)\rangle
-\langle\Phi_{geom}(R)\rangle.
}
\]

Therefore a recurrent mean radial wedge flux is paid only by already explicit channels:

- similarity energy baseline;
- bulk dissipation;
- signed material pressure/viscous exchange;
- nonnegative similarity geometric sweep.

## 8. Consequence for the finite-lag route

The Eulerian-to-material conversion does not generate a new mysterious remainder.

In particular,

\[
\boxed{
\text{fixed-depth wedge current}
-\text{material-carrier energy current}
=
\text{explicit similarity sweep/interface terms}.
}
\]

The geometric term is a state-local energy shell observable rather than a topological/index charge. Recurrent positivity of this term is another unsigned local payer and remains subject to the physical accumulation firewall.

Bulk dissipation is likewise unsigned.

Thus the only potentially high-value signed channel left in the same-population conversion is

\[
\boxed{X_\eta(R)=\text{pressure + viscous exchange across the material-population interface}.}
\]

It still requires a sign, finite-budget, or external-rigidity theorem.

## 9. Internal-interface cancellation preview

If the active core admits a compatible finite material partition, then on a shared interface the pressure/viscous exchange current

\[
(PU-\nu\nabla e)\cdot n
\]

changes sign when the normal is reversed.

Therefore internal energy exchanges should cancel pairwise when the full finite population network is summed, leaving only external/background exchange.

This is the direct kinetic-energy analogue of the M18-089 diffusion-current cancellation and is the next calculation.

---

\[
\boxed{\text{M19-285 COMPLETE; THE EULERIAN/MATERIAL MISMATCH IS AN EXPLICIT SIMILARITY GEOMETRIC SWEEP, NOT A NEW UNTYPED SIGNED DEFECT.}}
\]
