# M19-400 — Smooth compactness does not give a minimum flux for arbitrary material sub-tubes

Date: 2026-09-18

Status: **CANONICAL NO-GO / THE REMOTE-PAST ZERO-FLUX SEED OF M19-399 CANNOT BE EXCLUDED MERELY FROM SMOOTHNESS, ANALYTICITY, TUBULAR REACH OF A LARGER COHERENT CARRIER, OR UNIFORM AMPLITUDE BOUNDS. ANY REGULAR POSITIVE-FLUX MATERIAL TUBE CAN BE SUBDIVIDED INTO ARBITRARILY SMALL POSITIVE-FLUX MATERIAL SUB-TUBES WITHOUT CHANGING THE EULERIAN FIELD. THEREFORE A LOWER BOUND ON FLUX/VOLUME OF AN ARBITRARY MATERIAL LABEL IS IMPOSSIBLE WITHOUT A CANONICAL PDE-DEFINED COHERENCE OR MINIMAL-FEATURE CONDITION. THE ZERO-FLUX ANCIENT-SEED SURVIVOR IS THUS A MATERIAL-LABEL SUBPARTITION PROBLEM, NOT AN ORDINARY SMOOTHNESS PROBLEM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let a regular active vortex tube cross a smooth transversal \(A\), with

\[
W=\rho\xi,
\qquad
0<\rho_-\le \rho\le \rho_+<\infty
\]

on the relevant compact patch.

The oriented vorticity-flux measure on the transversal is

\[
d\Phi = W\cdot n\,dA.
\]

After orienting the chart consistently,

\[
d\Phi>0.
\]

Assume the larger carrier has all the regularity used in M17-420:

- positive total flux;
- finite-jet compactness;
- tubular reach / bounded-overlap charts;
- analytic regularity;
- representation-safe genealogy.

---

## 2. Arbitrary material subdivision

Choose any measurable subregion

\[
A_\varepsilon\subset A
\]

with positive area and

\[
|A_\varepsilon|\to0.
\]

Let \(\mathcal T_\varepsilon\) be the material vortex-tube subfamily obtained by following exactly those vortex lines intersecting \(A_\varepsilon\).

Its initial flux is

\[
\Phi_\varepsilon
=
\int_{A_\varepsilon}W\cdot n\,dA.
\]

Because \(W\cdot n\) is bounded on the regular chart,

\[
0<\Phi_\varepsilon
\le C|A_\varepsilon|
\to0.
\]

Thus

\[
\boxed{
\inf_{\text{positive material sub-tubes}}\Phi=0
}
\]

even though the ambient Eulerian field and the parent tube remain perfectly smooth and nondegenerate.

---

## 3. Volume and enstrophy also admit arbitrary subdivision

If the represented line-segment length is bounded by a finite chart length \(\ell_*\), then

\[
|\mathcal T_\varepsilon|
\lesssim
|A_\varepsilon|\ell_*
\to0.
\]

With \(\rho\le\rho_+\),

\[
E_\varepsilon
:=
\int_{\mathcal T_\varepsilon}\rho^2\,dV
\le
\rho_+^2|\mathcal T_\varepsilon|
\to0.
\]

Hence neither smoothness nor a positive ambient amplitude gives a positive lower bound for the volume or enstrophy of an **arbitrarily chosen material subpopulation**.

---

## 4. Why tubular reach of the parent does not help

M17-420 assumes tubular reach or bounded-overlap segmentation for the retained coherent loop family.

That controls the geometry of the **parent represented structure**.

It does not imply a minimum transverse diameter for every measurable material subset of that structure.

Inside one regular tube of radius \(r_*\), one may choose nested sub-tubes with transverse radii

\[
r_n\downarrow0.
\]

All such sub-tubes inherit the same smooth ambient field.

Therefore

\[
\boxed{
\text{parent tubular reach}
\not\Rightarrow
\text{minimum material sub-tube flux}.
}
\]

---

## 5. Consequence for the critical ancient seed

M19-399 isolates a critical seed history with

\[
\Phi(\theta)\to0
\qquad
(\theta\to-\infty)
\]

while later reaching order-one carrier flux.

A proposed shortcut

\[
\text{smooth compact core}
\Rightarrow
\Phi\ge\phi_*>0
\]

for every material ancestor is invalid.

The field may remain order-one while the selected material cross-section becomes arbitrarily small.

At the M19-365 critical lock,

\[
D_B\log\Phi\approx\frac32,
\]

so backward in time

\[
\Phi(\theta_0-T)
\sim
\Phi(\theta_0)e^{-3T/2}.
\]

This is geometrically compatible with a nested sequence of ever-thinner material sub-tubes inside a regular Eulerian carrier.

---

## 6. Canonicality is the missing ingredient

A useful minimum-size theorem must not be stated for arbitrary labels.

It must attach to a structure selected canonically by the PDE or by the first-hitting construction, for example:

1. a connected component of a robust amplitude superlevel;
2. a fixed-margin jet packet;
3. a component carrying a prescribed fraction of local enstrophy;
4. a first-hitting carrier with a canonical maximal/minimal selection rule;
5. a topologically or dynamically indivisible material component.

Only such a definition can prevent arbitrary subpartition from defeating a size lower bound.

---

## 7. Sharp survivor split

The M19-399 zero-flux branch therefore refines to

\[
\boxed{
G_{remote-past/zero-flux}^{reset}
\Longrightarrow
G_{canonical\ coherent\ seed}^{vanishing}
\lor
G_{arbitrary\ material\ subpartition}.
}
\]

The second branch is not yet a physical singular mechanism.

It may simply reflect that the same smooth carrier has been represented by an ever-smaller material label subset.

The first branch is the genuinely dangerous one and should be attacked by compactness/thickening.

---

## 8. DSD audit verdict

**NO-GO for a naive minimum material-seed flux theorem.**

Smoothness controls the field; it does not quantize material labels.

The next theorem must answer:

\[
\boxed{
\mathcal T_{canonical}^{seed}:
\text{is the critical future carrier forced to have a canonical robust ancestor rather than an arbitrarily chosen sub-tube?}
}
\]

Only after canonicality is established can compactness produce a meaningful lower-size estimate.

---

\[
\boxed{\text{M19-400 COMPLETE; ARBITRARY MATERIAL SUBDIVISION DEFEATS ANY SMOOTHNESS-ONLY MINIMUM-FLUX ARGUMENT.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
