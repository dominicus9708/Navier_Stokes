# DSD M5-319 — Transition Vorticity-Flux Retention, Angular Thickness, and Critical-Tail-or-Satellite Routing

Date: 2026-08-30

Parent: `DSD_M5_318_TRANSITION_SHELL_VORTICITY_CHANGE_PALINSTROPHY_LOWER_BOUND_AND_DIFFUSIVE_SHARPNESS_2026-08-30.md`

Status: **FORMATION/AXIAL TRANSITION REFINEMENT / DIV OMEGA = 0 DOES NOT FORCE EVERY ROTOR FLUX LINE TO RETURN LOCALLY / A RETAINED OUTGOING FLUX MAY CONTINUE TO LARGER RADII / IF ITS ANGULAR CROSS-SECTION COLLAPSES, THE FIXED FLUX FORCES THE REMOTE-SATELLITE PARAMETER q r TO DIVERGE / IF ITS ANGULAR CROSS-SECTION REMAINS NONDEGENERATE, THE NATURAL SCALING IS OMEGA~r^-2 AND CIRCULATION/VELOCITY~r^-1, I.E. THE PREVIOUS CRITICAL DIFFUSE-TAIL FRONTIER / O(1) VISCOUS FLUX LOSS OR RETURN/BENDING ARE ALREADY TYPED TURNOVER CHANNELS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Scope correction: div omega = 0 does not imply local return

Because

\[
\nabla\cdot\omega=0,
\]

the total vorticity flux through every closed surface is zero.

However this does not mean that every outward flux tube must turn around in the same transition shell.

A coherent vorticity line may continue to larger radii, with inward compensation occurring elsewhere or on another part of the same global line structure.

Therefore the transition classification must include a persistent outgoing-flux branch.

---

## 2. Flux alternatives

For a coherent packet/tube family define a signed vorticity flux

\[
\Phi(r)
:=\int_{\Sigma_r}\omega\cdot n_{\Sigma}\,dA
\]

through a suitable cross-section `Sigma_r` intersecting the outgoing structure.

Over the transition history there are three primary possibilities:

\[
\boxed{
\text{O(1) flux change}
\lor
\text{return/bending}
\lor
\text{retained outgoing flux}.
}
\]

An O(1) change in `Phi` under viscosity/localization is a robust flux-change/turnover event already present in the T/H ledgers.

Return/bending is the axial/projective transition branch.

This note analyzes the retained outgoing case.

---

## 3. Angular thickness descriptor

At radius `r`, let the retained outgoing flux occupy a cross-sectional area

\[
\boxed{
A(r)=\vartheta(r)r^2,
}
\]

where `0<vartheta(r)<=C` is an angular-thickness descriptor.

Assume the flux remains nondegenerate,

\[
|\Phi(r)|\ge \Phi_0>0.
\]

Then

\[
\Phi_0
\le
\int_{\Sigma_r}|\omega|dA.
\]

Hence the cross-sectional average obeys

\[
\boxed{
\fint_{\Sigma_r}|\omega|dA
\ge
\frac{\Phi_0}{\vartheta(r)r^2}.
}
\]

Therefore some point in the section satisfies

\[
\boxed{
|\omega(x_r)|
\ge
c\frac{\Phi_0}{\vartheta(r)r^2}.
}
\]

---

## 4. Convert to the satellite parameter

Define the vorticity-natural inverse length

\[
q(r):=|\omega(x_r)|^{1/2}.
\]

Then

\[
q(r)r
\ge
c\Phi_0^{1/2}\vartheta(r)^{-1/2}.
\]

Thus if

\[
\vartheta(r_n)\to0
\]

along a sequence of outgoing radii,

\[
\boxed{
q(r_n)r_n\to\infty.
}
\]

This is exactly the remote-active-satellite separation parameter from M5-279--281.

Therefore

\[
\boxed{
\text{retained flux + angular collapse}
\Longrightarrow
S_{remote}.
}
\]

No new branch is created.

---

## 5. Angularly nondegenerate outgoing flux

Suppose instead

\[
\vartheta(r)\ge\vartheta_0>0
\]

on arbitrarily large relevant radii.

Then the retained flux naturally has the critical vorticity scaling

\[
\boxed{
|\omega|_{avg}\gtrsim r^{-2}.
}
\]

A circulation loop linking the retained flux satisfies by Stokes' theorem

\[
\Gamma=\oint u\cdot dl=\Phi
\]

for a compatible cross-section.

If the linking loop has length `O(r)`, then

\[
\boxed{
\fint_{loop}|u|dl
\gtrsim
\frac{\Phi_0}{r}.
}
\]

Thus the associated velocity scale is the critical

\[
\boxed{u\sim r^{-1}}
\]

rather than an affine or faster-growth scale.

This is a lower-scale/topological indication; converting it to a full shell `L^3` bound requires the retained thickness/coherence hypotheses and must not be inferred from a single loop alone.

---

## 6. Relation to the existing critical-tail frontier

On the corridor where H/Campanato escalation is excluded, the existing annular machinery gives the weak-critical velocity control used in M5-276.

Therefore an angularly thick retained outgoing flux does not need a new endgame:

- if the corresponding shell velocity remains in the no-H/no-T weak-`L^3` class, it belongs to the Albritton--Barker/Liouville corridor;
- if weak-`L^3` control fails, the failure itself routes back to H-frequency or Campanato turnover by M5-276--280.

Hence

\[
\boxed{
\text{retained flux + angular thickness}
\Longrightarrow
\text{critical diffuse-tail corridor}
\lor
H/T.
}
\]

---

## 7. Viscous flux loss is a typed transition

Navier--Stokes viscosity allows vortex flux/circulation to change.

Therefore fixed flux cannot be assumed without audit.

If over one natural transition episode

\[
|\Phi(t_1)-\Phi(t_0)|\ge c_\Phi>0,
\]

then the branch has paid a robust viscous/boundary flux-change action.

This is the existing

\[
T_{visc/flux}
\]

or derivative/palinstrophy exit depending on the localization used.

Thus flux decay does not silently erase the transition problem.

---

## 8. Return/bending branch

If flux is retained but does not continue outward, then it must bend, split, reverse, or join compensating flux populations.

This returns to

\[
T_{axis},\quad
T_{projective},\quad
T_{multi-flux},\quad
T_{export/reentry}
\]

and their finite-memory/positive-frequency ledgers.

---

## 9. Updated transition routing

Combining the alternatives gives

\[
\boxed{
T_{transition}^{vort}
\Longrightarrow
T_{visc/flux}
\lor
T_{return/bend}
\lor
S_{remote}
\lor
C_{crit-tail}
\lor
H/T_{weakL3-fail}.
}
\]

Thus the vorticity transition shell does not generate an entirely new terminal topology.

It reconnects to already isolated frontiers.

---

## 10. Formation significance

The useful descriptor is not merely `flux exists` but the pair

\[
\boxed{
(\Phi(r),\vartheta(r)).
}
\]

- `Phi` records retained signed circulation/vorticity content;
- `vartheta` records how much angular support carries that content.

The two extreme technical outcomes are then automatic:

\[
\vartheta\downarrow0
\Rightarrow
\text{concentration/satellite},
\]

\[
\vartheta\gtrsim1
\Rightarrow
\text{critical diffuse scaling}.
\]

This is a clean formation split that is independent of DSD audit terminology.

---

## 11. Audit verdict

### Proved structural routing

- local return is not forced solely by `div omega=0`;
- retained nonzero flux through cross-sectional area `vartheta r^2` forces a pointwise vorticity lower bound `~1/(vartheta r^2)`;
- angular collapse forces the remote-satellite parameter `q r` to diverge;
- angularly thick retained flux has the natural critical `omega~r^-2`, circulation/velocity `~r^-1` scale;
- O(1) viscous flux loss and return/bending are already typed T/H channels.

### Scope firewall

- a circulation lower bound on one linking loop is not by itself a full shell `L^3` lower bound;
- the weak-`L^3` endgame still requires the existing no-H/no-T annular control.

### Remaining transition target

The genuinely difficult cases remain

\[
\boxed{
T_{dynamic}
\lor
S_{remote}/A_{detached}
\lor
C_{critical}\text{ when weak-critical ancestry is not yet coherent}.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
