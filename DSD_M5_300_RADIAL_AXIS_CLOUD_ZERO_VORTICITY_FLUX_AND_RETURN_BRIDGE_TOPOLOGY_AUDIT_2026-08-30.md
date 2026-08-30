# DSD M5-300 — Radial-Axis Cloud Zero-Vorticity-Flux and Return-Bridge Topology Audit

Date: 2026-08-30

Parents:
- `DSD_M5_295_RADIAL_AXIS_ALIGNMENT_DYNAMIC_MISMATCH_AND_TANGENTIAL_STRETCHING_CANCELLATION_GATE_2026-08-30.md`
- `DSD_M5_299_DENSE_CANCELLING_CLOUD_DYNAMIC_TENSOR_BALANCE_AND_SYMMETRY_FIREWALL_2026-08-30.md`

Status: **FORMATION/AXIS TOPOLOGICAL REDUCTION / THE VORTICITY FLUX THROUGH EVERY CLOSED SPHERE IS EXACTLY ZERO / A COHERENT RADIAL-AXIS CLOUD MUST THEREFORE BE SIGN-BALANCED OR PAID BY BACKGROUND FLUX / UNDER VORTEX-TUBE COHERENCE, SIGNED RADIAL FLUX CAN CLOSE ONLY BY THREADING THE INNER CORE OR BY REMOTE RETURN STRUCTURES THAT NECESSARILY PASS THROUGH NONRADIAL/TANGENTIAL AXIS STATES / THIS ROUTES THE PURE RADIAL-INVISIBILITY SUBCLASS BACK TO CORE LINEAGE, AXIS-BENDING, OR NONRADIAL CLOUD STRUCTURE, BUT DOES NOT YET GIVE A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact zero flux of vorticity through closed spheres

For every smooth Navier–Stokes velocity field,

\[
\omega=\nabla\times u,
\qquad
\nabla\cdot\omega=0.
\]

Hence for every ball `B_R(X)` contained in a smooth time slice,

\[
\boxed{
\int_{\partial B_R(X)}\omega\cdot n\,dS
=0.
}
\]

This follows directly from the divergence theorem and is also consistent with the fact that vorticity is a curl.

This identity is exact and independent of viscosity.

---

## 2. Packet flux decomposition

Suppose a sphere intersects coherent radial-axis satellite caps `C_i`.

Define their signed vorticity fluxes

\[
\boxed{
\Phi_i
:=
\int_{C_i}\omega\cdot n\,dS.
}
\]

Let `Phi_bg` denote the flux through the complement of the selected caps.

Then

\[
\boxed{
\sum_i\Phi_i+\Phi_{bg}=0.
}
\]

Therefore a radial-axis cloud cannot carry a net one-sign flux unless an unselected/background field carries the opposite amount.

---

## 3. Fixed-flux occupied packets

For a coherent natural packet with

\[
|\omega|\sim\ell^{-2}
\]

on a cap of area `~ell^2` and with

\[
|\xi\cdot n|\ge c_{rad}>0,
\]

the natural flux scale is order one:

\[
|\Phi_i|\sim1
\]

up to the packet occupancy/alignment constants.

If a selected class has a fixed lower flux floor

\[
|\Phi_i|\ge\Phi_*>0,
\]

then, whenever the background flux is quiet,

\[
|\Phi_{bg}|\le C_{bg},
\]

the positive and negative radial populations must balance quantitatively.

In the equal-flux idealization,

\[
\boxed{
|N_+-N_-|\lesssim C_{bg}/\Phi_*.
}
\]

The exact statement for unequal fluxes is the signed sum identity rather than a count identity.

---

## 4. Formation meaning: radial packets are not independent endpoints

The zero-flux identity means that outward and inward radial packets must belong to a globally closed vorticity-flux structure.

At a fixed time there are three possibilities:

1. **background closure** — the selected radial cloud is balanced by diffuse/unselected flux;
2. **core-threading closure** — vortex-line/tube structure passes through the inner/core region and emerges with opposite radial sign elsewhere;
3. **remote-return closure** — flux turns around outside the inner core and returns through another radial cap.

Thus

\[
\boxed{
C_{radial}
\Longrightarrow
C_{background}
\lor C_{core-thread}
\lor C_{remote-return}.
}
\]

This is a structural partition, not yet a regularity theorem.

---

## 5. Core-threading branch

A vortex tube that closes the signed radial flux by passing through the tracked inner region is not dynamically detached from the main core.

It creates a direct historical/material lineage connecting the remote satellite population to the singular core.

Therefore this branch leaves the purely passive detached-cloud topology and returns to existing material-return/replenishment ledgers:

\[
\boxed{
C_{core-thread}
\to
R_{lineage}/T_{material}/H_{historical}.
}
\]

No new contradiction is claimed here; the significance is topological re-routing.

---

## 6. Remote-return branch forces a nonradial state

Assume a coherent vortex line/tube closes outside the inner core.

Along a continuous oriented vortex line let

\[
q(s):=\xi(s)\cdot n(s),
\]

where `xi=omega/|omega|` and `n` is the radial direction from the tracked center.

If the line crosses one radial cap outward and another inward, then for some portions

\[
q\ge c_{rad}>0
\]

and elsewhere

\[
q\le-c_{rad}<0.
\]

By continuity there exists an intermediate point with

\[
\boxed{
q=0.
}
\]

At that point

\[
\boxed{
\xi\perp n,
}
\]

so the vortex direction is tangential to the sphere.

Therefore a remote return cannot remain inside the pure radial-axis class everywhere.

---

## 7. Relation to the leading Biot–Savart invisibility condition

M5-294 showed that a packet is individually invisible to the leading `d^{-3}` main-core strain when its localized vorticity moment is radial:

\[
M\parallel n.
\]

A coherent return bridge containing a tangential-axis region instead has

\[
|n\times M|
\]

nonzero unless its localized moment degenerates/cancels.

Thus remote return creates at least one of:

\[
\boxed{
C_{nonradial}
\lor C_{M_0=0}
\lor C_{local-tensor-cancel}.
}
\]

In particular, the pure individual radial-invisibility mechanism cannot describe the entire closed flux structure.

---

## 8. Sharp versus broad return

The nonradial transition may occur in two qualitatively different ways.

### Sharp axis bending

If the transition from radial-outward to radial-inward occurs over spatial arclength `L_bend` much smaller than the outer return scale, then the vortex-direction gradient must be large:

\[
\int |(\xi\cdot\nabla)\xi|\,ds
\ge
\operatorname{angle\ variation}.
\]

A fixed angle change over a very short bridge therefore produces a derivative/axis-bending `H` candidate.

### Broad return bridge

If the bend is spread over a large region, then a substantial nonradial/tangential vorticity population persists over that region.

This is another satellite/cloud component and re-enters the interaction-density/multipole ledger.

Hence schematically

\[
\boxed{
C_{remote-return}
\Longrightarrow
H_{axis-bend}
\lor C_{broad-nonradial}.
}
\]

The threshold separating `sharp` and `broad` still requires an explicit scale choice.

---

## 9. Important geometric firewall: a straight core-threading line need not bend

One must not claim that opposite radial signs automatically force curvature of the vortex direction.

A straight line passing through the tracked center provides the counterexample:

- on one side its fixed direction is outward radial;
- on the opposite side the same fixed direction is inward radial;
- the vector direction itself does not bend.

This is precisely why the core-threading and remote-return cases must be separated.

Only a return that avoids the inner core is forced to develop a nonradial bridge.

---

## 10. Background-flux branch

If the selected radial packets carry substantial signed flux but closure is supplied by unselected background flux,

\[
|\Phi_{bg}|\gtrsim\sum_i|\Phi_i|_{unbalanced},
\]

then the background is not dynamically negligible.

This routes to the already isolated diffuse/background frontier:

\[
\boxed{
C_{background}
\to
H/T_{background/diffuse}.
}
\]

Again, a quantitative lower bound requires the packet flux floor and the chosen background descriptor.

---

## 11. Updated radial-axis frontier

The pure radial-alignment branch is therefore reduced to

\[
\boxed{
\begin{aligned}
C_{radial}
\Longrightarrow{}&
H/T_{background}\\
&\lor R_{core-thread}\\
&\lor H_{axis-bend}\\
&\lor C_{broad-nonradial}.
\end{aligned}
}
\]

This is meaningful because it removes the possibility of treating a large collection of radially invisible satellites as independent permanent objects with no closure geometry.

---

## 12. What remains

The next hard branch is the broad nonradial / dense-cancelling cloud.

At that point the useful quantities are no longer only packet counts. One needs either:

1. a satellite-centered Morrey/energy capacity;
2. an angular-tensor covariance law strong enough to control statistically cancelling populations;
3. ancestry showing that an affine/isotropic detached limit cannot arise from finite-energy data.

---

## 13. Audit verdict

### PROVED / EXACT

- zero vorticity flux through every closed sphere;
- signed packet flux balance;
- remote return from outward to inward radial orientation passes through a tangential/nonradial axis state.

### ROUTED

- core-threading return -> historical/material lineage;
- sharp remote return -> axis-derivative candidate;
- broad remote return -> nonradial cloud;
- large background closure -> diffuse/background branch.

### NOT PROVED

- quantitative exclusion of broad return bridges;
- a universal vortex-tube decomposition for diffuse vorticity;
- closure of the remaining cloud/ancestry branches;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]