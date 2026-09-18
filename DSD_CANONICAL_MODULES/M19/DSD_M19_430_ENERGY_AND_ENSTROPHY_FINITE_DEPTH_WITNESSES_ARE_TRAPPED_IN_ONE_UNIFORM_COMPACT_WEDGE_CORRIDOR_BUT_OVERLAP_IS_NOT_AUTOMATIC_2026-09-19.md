# M19-430 — Energy and enstrophy finite-depth witnesses are trapped in one uniform compact wedge corridor, but overlap is not automatic

Date: 2026-09-19  
Canonical ID: **M19-430**  
Status: **FINITE-DEPTH LOCALIZATION UPGRADE / ON THE POSITIVE RESIDUAL-SLOPE BRANCH THE M19-269 ENERGY MAXIMUM AND M5-587 ENSTROPHY-PRODUCTION MAXIMUM CANNOT ESCAPE TO z=0 OR z=INFINITY / COMPACT TERMINAL-JET CONTROL AND UNIFORM TYPE-I CENTER DECAY TRAP BOTH WITNESSES IN ONE COMPONENT-UNIFORM COMPACT DEPTH INTERVAL / THEIR ACTUAL SAME-DEPTH OR SAME-NEIGHBORHOOD OVERLAP IS NOT FORCED BY THE EXISTING ONE-DIMENSIONAL LEDGERS / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Work on the residual-slope master branch

M19-429 reduces one master branch to

\[
\boxed{
\mathscr E'(0)
=
\left\langle
\int A\cdot C
\right\rangle
\ge
\delta_E>0.
}
\]

M19-269 then gives an interior energy maximum

\[
z_E\in(0,\infty),
\qquad
\mathscr E'(z_E)=0,
\]

with

\[
\mathscr E(z_E)>\mathscr E(0)>0.
\]

Independently, M5-587 gives an interior maximum of

\[
\boxed{
\mathscr Y_\omega(z)
=
\frac12z^{1/2}\mathscr K_\omega(z)
+
z^{3/2}\mathscr J_\omega(z),
}
\]

at some

\[
z_\omega\in(0,\infty),
\]

where

\[
\boxed{
\mathscr Q_\omega(z_\omega)
-
\mathscr P_\omega(z_\omega)
=
\frac{\mathscr K_\omega(z_\omega)}
{2z_\omega}
>0.
}
\]

The question is whether the two depths can be localized uniformly.

## 2. Energy maximum cannot approach z=0

The compact smooth terminal-jet class gives a uniform bound on a fixed small depth interval:

\[
\boxed{
|\mathscr E''(z)|
\le
M_E
\qquad
0\le z\le z_0.
}
\]

At the terminal boundary,

\[
\mathscr E'(0)\ge\delta_E.
\]

Choose

\[
\boxed{
a_E
:=
\min\left\{
z_0,
\frac{\delta_E}{2M_E}
\right\}
}
\]

when \(M_E>0\).

Then for

\[
0\le z\le a_E,
\]

\[
\boxed{
\mathscr E'(z)
\ge
\frac{\delta_E}{2}
>0.
}
\]

Therefore an interior maximum cannot occur in this interval:

\[
\boxed{
z_E\ge a_E>0.
}
\]

Moreover

\[
\boxed{
\mathscr E(a_E)
\ge
\mathscr E(0)
+
\frac{\delta_Ea_E}{2}.
}
\]

Thus the energy witness gains a fixed positive amount before it is allowed to turn.

## 3. Energy maximum cannot escape to infinity

The smooth Type-I center asymptotics give, uniformly on the compact component,

\[
\boxed{
\mathscr E(z)
\le
C_Ez^{-1}
}
\]

for sufficiently large z.

Set

\[
e_*:=
\mathscr E(0)
+
\frac{\delta_Ea_E}{2}
>0.
\]

Choose \(b_E\) so large that

\[
C_Eb_E^{-1}<e_*.
\]

Since

\[
\mathscr E(z_E)
\ge
\mathscr E(a_E)
\ge
e_*,
\]

the global maximum cannot lie beyond \(b_E\).

Hence

\[
\boxed{
a_E
\le
z_E
\le
b_E.
}
\]

The constants depend only on the fixed compact hard component and its quantitative residual-slope floor.

## 4. Enstrophy-production maximum cannot approach z=0

M5-586 gives the terminal expansions

\[
\mathscr K_\omega(z)
=
K_0+O(z),
\qquad
K_0>0,
\]

and

\[
\mathscr J_\omega(z)
=
J_0+O(z).
\]

Therefore

\[
\mathscr Y_\omega(z)
=
\frac12K_0z^{1/2}
+
O(z^{3/2}).
\]

Differentiate:

\[
\boxed{
\mathscr Y_\omega'(z)
=
\frac14K_0z^{-1/2}
+
O(z^{1/2}).
}
\]

Compact terminal-jet control makes the remainder coefficient uniform on the component.

Since the hard terminal vorticity density has

\[
K_0
=
\frac12
\left\langle
\int|B_A|^2
\right\rangle
>0,
\]

there exists

\[
\boxed{
a_\omega>0
}
\]

such that

\[
\mathscr Y_\omega'(z)>0
\qquad
0<z\le a_\omega.
\]

Thus

\[
\boxed{
z_\omega\ge a_\omega>0.
}
\]

Also

\[
\boxed{
\mathscr Y_\omega(a_\omega)
\ge
y_*>0
}
\]

for a component-dependent fixed lower bound \(y_*\).

## 5. Enstrophy-production maximum cannot escape to infinity

At the smooth Type-I center,

\[
G=O(z^{-1}),
\qquad
\mathscr K_\omega=O(z^{-2}),
\]

uniformly on the compact component.

The corresponding smooth-center flux estimate gives

\[
z^{3/2}\mathscr J_\omega(z)\to0
\]

uniformly along the compact hard component.

Therefore

\[
\boxed{
\mathscr Y_\omega(z)\to0
}
\]

uniformly as \(z\to\infty\).

Choose \(b_\omega\) so large that

\[
\sup_{z\ge b_\omega}
|\mathscr Y_\omega(z)|
<
\frac{y_*}{2}.
\]

But the maximum satisfies

\[
\mathscr Y_\omega(z_\omega)
\ge
\mathscr Y_\omega(a_\omega)
\ge
y_*.
\]

Hence

\[
\boxed{
a_\omega
\le
z_\omega
\le
b_\omega.
}
\]

## 6. One common compact depth corridor

Define

\[
\boxed{
a_*:=\min(a_E,a_\omega)>0,
}
\]

and

\[
\boxed{
b_*:=\max(b_E,b_\omega)<\infty.
}
\]

Then both forced finite-depth witnesses satisfy

\[
\boxed{
z_E,z_\omega
\in
[a_*,b_*].
}
\]

Thus neither event can hide

- arbitrarily close to the terminal singular boundary;
- nor arbitrarily deep in the smooth Type-I center.

Both are trapped in one fixed bounded/intermediate wedge-depth corridor.

This strengthens the earlier qualitative statement “there exists some finite depth.”

## 7. Physical interpretation

Since

\[
|y|=z^{-1/2},
\]

the common depth corridor corresponds to one compact annular range of similarity radii:

\[
\boxed{
b_*^{-1/2}
\le
|y|
\le
a_*^{-1/2}.
}
\]

Therefore both

- the energy-turning event;
- and the stretching-dominant enstrophy shell

occur in one uniformly bounded similarity annulus.

The hard branch can no longer evade their comparison by placing one witness at the terminal tail and the other arbitrarily near the center.

## 8. What this does not prove

The result does **not** prove

\[
z_E=z_\omega.
\]

Nor does it prove that the two positive-event neighborhoods intersect.

The energy maximum is defined by

\[
\mathscr E'(z_E)=0,
\]

while the enstrophy shell is defined by

\[
\mathscr Y_\omega'(z_\omega)=0.
\]

These are extrema of two different scalar functionals.

The exact energy and enstrophy ODEs do not currently provide an algebraic identity equating their zero sets.

Therefore

\[
\boxed{
\text{common compact corridor}
\not\Rightarrow
\text{same-event overlap}.
}
\]

## 9. Endpoint-shape firewall

The mere endpoint shapes are insufficient to force overlap.

For example, scalar profiles of the forms

\[
E_{model}(z)
=
(1+2z)e^{-z}
\]

and

\[
Y_{model}(z)
=
z^{1/2}e^{-z/8}
\]

have

\[
E_{model}'(0)>0,
\qquad
E_{model}\to0,
\]

and

\[
Y_{model}(0)=0,
\qquad
Y_{model}>0\text{ near }0,
\qquad
Y_{model}\to0,
\]

but their maxima occur at different finite depths.

This is only a scalar endpoint-shape witness, not a Navier--Stokes solution and not a full solution of the coupled wedge ledgers.

Its role is limited:

\[
\boxed{
\text{endpoint sign + compact-depth localization alone cannot prove overlap}.
}
\]

Any overlap theorem must use a genuine PDE coupling between the energy and vorticity systems.

## 10. Exact remaining overlap target

The former broad target

\[
\mathcal T_{tail}^{rigidity/overlap}
\]

can now be sharpened to

\[
\boxed{
\mathcal T_{overlap}^{E\omega}:
\text{use the Navier--Stokes relation }G=\operatorname{curl}_{wedge}F
\text{ to couple }\mathscr E'\text{ and }\mathscr Y_\omega'
\text{ inside }[a_*,b_*].
}
\]

Because the corridor is compact, all wedge coefficients and a fixed finite number of derivatives are uniformly controlled there.

Thus the problem is now a **bounded-domain observability/coupling problem**, not an endpoint or escaping-scale problem.

## 11. Next calculation

The next useful test is to derive a quantitative inequality on the compact corridor connecting

\[
\mathscr K_\omega(z)
\]

to

\[
\mathscr D(z)
\]

or to the energy-turning quantity

\[
\mathscr D(z)-\mathscr J(z)-2z\mathscr J'(z)
=
\mathscr E'(z).
\]

A direct curl/Poincare estimate may show that a large energy maximum necessarily carries nontrivial vorticity in the same neighborhood.

But to obtain actual overlap with

\[
\mathscr Q_\omega-\mathscr P_\omega>0,
\]

one additionally needs a stretching-versus-diffusion sign relation, not merely vorticity magnitude.

\[
\boxed{\text{M19-430 COMPLETE; BOTH FINITE-DEPTH WITNESSES ARE UNIFORMLY LOCALIZED TO ONE COMPACT WEDGE CORRIDOR, BUT SAME-EVENT OVERLAP REMAINS A GENUINE PDE COUPLING THEOREM.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
