# DSD M5-412 — Formed material-flux export routes to remote/shell throughput or critical flux action

Date: 2026-08-31

Status: **EXPORT OF A FORMED SCALE-INVARIANT VORTICITY-FLUX CARRIER IS NOT AN INDEPENDENT QUIET TERMINAL / AFTER LEAVING A LOCAL NATURAL WINDOW, A FIXED-FLUX MATERIAL DESCENDANT MUST EITHER REMAIN A FORMED CARRIER ELSEWHERE, SPREAD TO A LARGER CROSS-SECTION/SHELL RESERVOIR, LOSE FLUX THROUGH THE EXACT VISCOUS MATERIAL-SURFACE IDENTITY, OR UNDERGO DIRECTION/FRAGMENTATION REORGANIZATION / THESE ROUTE RESPECTIVELY TO REMOTE CRITICAL CARRIER NOVELTY, DISTRIBUTED SHELL OCCUPANCY, VISCOUS-FLUX H, OR DIRECTION/CAPACITY H / THE ONLY EXPORT CONTENT NOT COVERED IS A PURE VELOCITY/PRESSURE REALIZATION DEFECT WITHOUT A FORMED VORTICITY-FLUX OBJECT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

After M5-411, the remaining interface notation is concentrated in

\[
T_{realization/boundary/pressure}
\]

plus export-like events.

The repository has already proved that natural first-hitting carriers and their M5-394 companions carry a fixed physical vorticity flux

\[
\Phi\asymp\nu.
\]

M5-393 further separated material identity from flux identity through the exact material-surface flux law.

This note asks whether a **formed flux carrier leaving the local observation window** must remain a distinct final `T_export` mechanism.

---

## 2. Material flux descendant

Let `S(t)` be a material cross-section descended from a formed carrier.

Its signed vorticity flux is

\[
\Phi(t)
:=
\int_{S(t)}\omega\cdot n\,dA.
\]

The exact Navier--Stokes material-surface identity is

\[
\boxed{
\frac d{dt}\Phi(t)
=
\nu\int_{S(t)}\Delta\omega\cdot n\,dA.
}
\]

Thus material transport alone does not erase flux. Any fixed change in the signed flux is a genuine viscous flux action.

Assume at formation

\[
|\Phi(t_0)|\ge\phi_0\nu.
\]

Track the descendant until it leaves the retained local natural window.

---

## 3. First fork: flux identity survives or not

Fix a later comparison time.

Either

\[
\boxed{
|\Phi(t)|\ge c_\phi\nu
}
\]

for a fixed `c_phi>0`, or a fixed fraction of the original flux has been lost.

In the loss case,

\[
|\Phi(t)-\Phi(t_0)|
\gtrsim\nu,
\]

and the exact identity gives

\[
\boxed{
\nu\int_{t_0}^{t}
\left|
\int_{S(s)}\Delta\omega\cdot n\,dA
\right|ds
\gtrsim\nu.
}
\]

Therefore

\[
\boxed{
\text{export with fixed flux loss}
\Longrightarrow
H_{viscous\ flux}^{crit}.
}
\]

No export label is needed for this branch.

---

## 4. Surviving flux plus bounded natural thickness forms another carrier

Assume the flux survives and, at the later time, remains concentrated in a coherent cross-section of characteristic radius `r_out` with

\[
|\omega|\lesssim C\frac\nu{r_{out}^2}
\]

and a fixed directed lower bound on a natural subdisk/ball.

Then it is simply another formed natural carrier.

If its center lies at target-normalized distance tending to infinity from the currently tracked first-hitting core, it is

\[
\boxed{S_{remote}^{formed}.}
\]

By M5-408--410 this is part of the common critical phase-space throughput ledger, not a passive export terminal.

If instead it remains in a bounded position-scale neighborhood of the current active core, it is a local carrier/contact/replacement object and returns to M5-393--398.

Thus

\[
\boxed{
\text{coherent surviving exported flux}
\Longrightarrow
S_{remote}^{formed}
\lor
H_{local/flux}^{crit}.
}
\]

---

## 5. Surviving flux that spreads to a larger cross-section

Suppose the material flux survives but no later small natural cross-section carries a fixed fraction of it.

Let the descendant occupy an effective transverse area `A(t)`.

Since

\[
|\Phi(t)|\ge c_\phi\nu,
\]

and the directed vorticity amplitude on the descendant is at most `M(t)`, one has the elementary area requirement

\[
\boxed{
A(t)
\gtrsim
\frac\nu{M(t)}.
}
\]

Relative to a current first-hitting natural scale

\[
r_*^2=\frac\nu{W_*},
\]

if the exported descendant amplitude is much smaller than `W_*`, then

\[
\boxed{
A(t)\gg r_*^2.
}
\]

Thus fixed flux has not disappeared; it has become a broad spatial reservoir.

Such a state belongs to the distributed shell/occupancy problem rather than a point carrier.

Therefore

\[
\boxed{
\text{surviving flux with large spreading}
\Longrightarrow
H_{shell/distributed}^{crit}
\lor S_{remote}^{distributed}.
}
\]

Calling it `export` does not remove its critical source mass.

---

## 6. Fragmentation does not create a free export route

Suppose the surviving exported flux splits among many coherent fragments.

The M5-382--384 fragmentation audits apply once a fixed flux fraction must be represented by separated or multiscale pieces.

Regular sheet storage, separated fragments, and bounded-spatial multiscale microshape all force normalized palinstrophy/capacity cost unless the structure becomes remote/non-tight.

Hence

\[
\boxed{
\text{fragmented exported flux}
\Longrightarrow
H_{pal/cap}^{crit}
\lor S_{remote/non-tight}.
}
\]

No independent fragmentation-export leaf is introduced.

---

## 7. Directional reorganization of exported flux

If comparable signed flux survives but its material cross-section/axis changes by an order-one projective amount, M5-411 applies.

Either the same material active carrier persists and pays

\[
H_{\tau,act}^{crit}
\lor H_{dir\,diff}^{crit},
\]

or the active flux ancestry itself is replaced/reformed, returning to the M5-395--410 critical-carrier ledger.

Therefore

\[
\boxed{
\text{direction-changing export}
\Longrightarrow
H_{direction/flux}^{crit}
\lor S_{remote}^{new}.
}
\]

---

## 8. Local-window crossing is a bookkeeping event, not yet a mathematical payer

The mere statement

\[
\text{carrier crosses the boundary of a chosen observation ball}
\]

has no invariant mathematical content unless the later carrier state is recorded.

The boundary may be arbitrary or moving.

The invariant information is instead one of:

- the flux has changed;
- the flux remains and is localized elsewhere;
- the flux remains but has spread;
- the flux has fragmented;
- the axis/material ancestry has reorganized.

These are exactly Sections 3--7.

Thus DSD should not count `crossed our cutoff` as an independent physical event after the descendant has been classified.

---

## 9. Pressure does not directly destroy vorticity flux

Pressure affects the velocity and therefore the material flow map, but the curl of the pressure gradient vanishes.

The material vorticity-flux equation contains no direct pressure source term:

\[
\frac d{dt}\Phi
=
\nu\int_{S(t)}\Delta\omega\cdot n\,dA.
\]

Therefore a pressure-driven transport that merely carries an intact flux packet out of a local window is still classified by its later flux state as above.

What may remain genuinely outside the present carrier description is a **velocity/pressure realization defect** in a compactness or localization argument where no formed vorticity-flux object has yet been assigned.

That narrower issue remains under

\[
T_{realization/pressure}.
\]

---

## 10. Export master routing

For a formed natural flux carrier,

\[
\boxed{
T_{export}^{formed\ flux}
\Longrightarrow
H_{viscous\ flux}^{crit}
\lor
H_{shell/pal/direction}^{crit}
\lor
S_{remote}^{critical\ throughput}
\lor
H_{local/flux}^{crit}.
}
\]

M5-408--410 subsequently absorb the formed remote branch into critical phase-space novelty/shell throughput or local/interface action.

Therefore

\[
\boxed{T_{export}^{formed\ flux}}
\]

is no longer needed as an independent terminal label.

---

## 11. Remaining realization/pressure interface

The residual interface problem is now narrower:

\[
\boxed{
T_{interface}^{surviving}
=
T_{realization/pressure/localization}
}
\]

in situations where

- a global/local velocity compactness argument loses coherence;
- a cutoff/Bogovskii correction is large before a formed carrier decomposition is available;
- pressure oscillation or harmonic velocity data are required to pass a limit even though no specific vorticity-flux descendant has been assigned.

These are analytic realization issues, not a new material-flux mechanism.

---

## 12. Audit verdict

### DERIVED

- fixed exported flux loss is viscous-flux H;
- coherent surviving export is another local/remote natural carrier;
- dispersed surviving flux becomes shell/occupancy throughput;
- fragmented export enters existing palinstrophy/capacity routing;
- directional export enters M5-411;
- mere cutoff crossing is not an invariant terminal event.

### REMOVED AS INDEPENDENT TERMINAL

\[
\boxed{T_{export}^{formed\ flux}.}
\]

### STILL OPEN

- velocity/pressure realization defects not yet represented by a formed flux carrier;
- the common critical throughput itself;
- a non-summable or rigidity mechanism excluding critical throughput;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]