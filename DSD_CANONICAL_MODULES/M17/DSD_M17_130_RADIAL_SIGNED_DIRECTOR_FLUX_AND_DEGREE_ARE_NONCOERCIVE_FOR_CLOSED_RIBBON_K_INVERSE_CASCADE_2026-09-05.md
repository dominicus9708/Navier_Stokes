# DSD M17-130 — Radial signed director flux and degree are noncoercive for the closed-ribbon K^-1 cascade

Date: 2026-09-05
Canonical ID: **M17-130**

Status: **AUDIT FIREWALL / THE DIVERGENCE-FREE DIRECTOR-AREA CURRENT DOES GIVE EXACT RADIALLY WEIGHTED SIGNED FLUX IDENTITIES, BUT THESE IDENTITIES CONTROL ONLY `J_xi·rhat` WITH SIGN. THE RIBBON CRITICAL STACK OF M17-129 IS BUILT FROM POSITIVE INTERNAL TUBE-FLUX AMOUNTS. CLOSED KERNEL-FLUX LOOPS CAN CARRY NONZERO POSITIVE TUBE FLUX WHILE CONTRIBUTING ZERO NET FLUX THROUGH EVERY ENCLOSING SPHERE. LIKEWISE, THE DEGREE OF `xi|S_R` QUANTIZES ONLY THE TOTAL SIGNED CLOSED-SURFACE AREA FLUX WHEN THE DIRECTOR IS DEFINED ON THE WHOLE SPHERE; DEGREE ZERO DOES NOT CONTROL INTERNAL TOTAL VARIATION. THEREFORE DIV-J, RADIAL MOMENTS, OR DEGREE ALONE CANNOT BOUND `sum(K_k Phi_k)^(3/2)` OR EXCLUDE `Phi_k~K_k^-1`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Radially weighted divergence identity

On a smooth Rank-2 director region,

\[
\boxed{\nabla\cdot J_\xi=0.}
\]

For any smooth radial weight `f(r)`,

\[
\boxed{
\nabla\cdot(f(r)J_\xi)
=f'(r)J_\xi\cdot\widehat r.
}
\]

Hence on an annulus `A_{R_1,R_2}`,

\[
\boxed{
\int_{A_{R_1,R_2}}
f'(r)J_\xi\cdot\widehat r\,dV
=
 f(R_2)\int_{S_{R_2}}J_\xi\cdot n\,dA
-
 f(R_1)\int_{S_{R_1}}J_\xi\cdot n\,dA.
}
\]

This is exact but signed.

---

## 2. Ribbon flux is an internal positive tube measure

M17-122/M17-129 use

\[
\boxed{d\Phi_J}
\]

as the positive flux amount of an oriented local `J_xi` tube.
For a ribbon bundle,

\[
\Phi_k=\int d\Phi_J>0.
\]

The critical stack is

\[
\boxed{
\sum_k(K_k\Phi_k)^{3/2}=\infty.
}
\]

This quantity contains total-variation information that is absent from a signed closed-surface flux.

---

## 3. Closed ribbon loop invisibility

A complete critical-ribbon kernel fiber may close inside one annular region.
A thin divergence-free flux tube following such a closed loop has no endpoints.
If it does not cross an enclosing sphere, it contributes exactly zero to that sphere's flux.
If it crosses a surface several times, orientations can cancel in the algebraic total.

Thus one can have

\[
\boxed{
\Phi_{tube}>0
}
\]

while

\[
\boxed{
\int_{S_R}J_\xi\cdot n\,dA=0
}
\]

for every sphere outside the loop.

Consequently no estimate of the form

\[
\Phi_k
\lesssim
\left|
\int_{S_R}J_\xi\cdot n\,dA
\right|
\]

can hold without additional geometric transversality/no-return hypotheses.

---

## 4. Why radial weighting does not restore coercivity

Replacing the constant weight by `f(r)` changes only the signed radial moment

\[
f'(r)J_\xi\cdot\widehat r.
\]

It does not replace it by

\[
|J_\xi|
\quad\text{or}\quad
|J_\xi\cdot\widehat r|.
\]

Hence positive inward/outward crossings and closed-loop circulation may cancel.

The exact divergence identity therefore cannot control the positive tube-flux stack needed by M17-129.

---

## 5. Degree/topological charge scope

When `xi` is smooth on a closed sphere and the normalization of `J_xi` is chosen canonically, the signed area-current flux represents the degree of

\[
\xi|_{S_R}:S^2\to S^2
\]

up to the fixed target-sphere area factor.

This quantizes

\[
\int_{S_R}J_\xi\cdot n\,dA.
\]

But it does **not** quantize the internal positive total variation

\[
\int_{S_R}|J_\xi\cdot n|dA
\]

nor the sum of fluxes of closed tubes contained inside the sphere.

In particular,

\[
\boxed{
\deg(\xi|_{S_R})=0
}
\]

is fully compatible with nontrivial paired or closed director-area flux structures.

If `W=0` intersects the sphere, even the global degree requires a punctured/defect treatment and cannot be inserted silently.

---

## 6. Kinematic firewall for the K^-1 model

The sharp M17-129 scaling

\[
\Phi_k\sim K_k^{-1}
\]

has finite unweighted total flux.
One may kinematically place successively smaller divergence-free closed flux tubes in disjoint remote annuli with these fluxes.
Each tube is invisible to the total flux of sufficiently large enclosing spheres.

This does not prove that every such kinematic current is realizable as a CE-H director-area current, but it proves the narrower audit statement:

\[
\boxed{
\nabla\cdot J_\xi=0
\text{ and closed-surface signed flux identities alone are insufficient.}
}
\]

Any exclusion must use additional director realization, weighted-harmonic, material, or Navier–Stokes structure.

---

## 7. DSD audit

### Audit A — replacing signed flux by absolute flux

Rejected. Divergence theorem does not commute with absolute value.

### Audit B — using degree to count every internal flux tube

Rejected. Degree measures algebraic closed-surface charge, not internal total variation.

### Audit C — assuming every ribbon crosses radial shell boundaries monotonically

Rejected. Complete critical ribbons are closed kernel loops and are the explicit countergeometry.

### Audit D — kinematic loop example proves CE-H existence

Rejected. It only demonstrates insufficiency of the divergence/topology-only argument.

### Audit E — proof status

The proposed radial signed-flux closure route is pruned unless a new no-cancellation/transversality theorem is added.

---

## 8. Updated tail target

The ribbon critical stack

\[
\boxed{
\sum(K_k\Phi_k)^{3/2}=\infty
}

cannot be closed using only unweighted charge, divergence-free transport, radial signed moments, or degree.

The next viable routes are narrower:

1. a **positive weighted director-energy/palinstrophy** estimate that sees internal flux magnitude;
2. a CE-H realization rigidity for the critical `Phi_k~K_k^-1` ribbon cascade;
3. Liouville/tail decoupling that does not require summing positive ribbon flux directly.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
