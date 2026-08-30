# DSD M5-318 — Transition-Shell Vorticity-Change Palinstrophy Lower Bound and Diffusive Sharpness

Date: 2026-08-30

Parent: `DSD_M5_317_CRITICAL_SCREENED_ROTOR_SATURATION_ANTIMODEL_AND_TRANSITION_SHELL_TARGET_2026-08-30.md`

Status: **TRANSITION-SHELL QUANTIFICATION / CONNECTING AN ORDER-ONE ROTOR VORTICITY CORE TO A DIFFERENT EXTERIOR STATE FORCES A POSITIVE PALINSTROPHY COST / FOR A SHELL OF RADIUS R AND WIDTH w THE MINIMAL COST IS OF ORDER R^2/w / EVEN THE CHEAPEST w~R TRANSITION COSTS ORDER R / THIS LOWER BOUND IS SHARP AT THE DIFFUSIVE R^2 LIFETIME AND THEREFORE DOES NOT BY ITSELF CONTRADICT THE R~L^(1/5) SCREENED-ROTOR SATURATION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Transition geometry

Consider a screened rotor-like core with characteristic radius `R` and order-one vorticity state

\[
\omega\approx\omega_{in},
\qquad
|\omega_{in}|\ge c_0>0
\]

on an inner region.

Assume that across an annular transition layer of width `w` the vorticity state changes by an order-one amount toward an exterior state `omega_out`, in the sense that along a positive fraction of radial/angular channels

\[
|\omega_{in}-\omega_{out}|\ge c_1>0.
\]

The change may be amplitude loss, axis bending, sign reversal, or a combination.

---

## 2. One-dimensional lower bound along a transition channel

Let `gamma` be one such radial/controlled crossing curve of length `O(w)` through the shell.

By the fundamental theorem of calculus and Cauchy--Schwarz,

\[
c_1
\le
\int_\gamma |\nabla\omega|ds
\le
w^{1/2}
\left(\int_\gamma|\nabla\omega|^2ds\right)^{1/2}.
\]

Therefore

\[
\boxed{
\int_\gamma|\nabla\omega|^2ds
\gtrsim
\frac{c_1^2}{w}.
}
\]

---

## 3. Coarea over a positive angular fraction

Suppose an angular fraction `theta_0>0` of the sphere undergoes such a transition.

The cross-sectional area is `~theta_0 R^2`.

Integrating the one-dimensional lower bound over these channels gives

\[
\boxed{
\int_{A_{R,w}}|\nabla\omega|^2dx
\gtrsim
c(\theta_0,c_1)\frac{R^2}{w}.
}
\]

This is the basic transition-shell palinstrophy floor.

---

## 4. Cheapest broad transition

The transition width cannot exceed the same radial order as the core radius without ceasing to be a localized `R`-scale connection.

Taking the cheapest admissible broad transition

\[
w\sim R
\]

gives

\[
\boxed{
\int_{A_R}|\nabla\omega|^2dx
\gtrsim cR.
}
\]

Thus an order-one rotor-to-exterior transition cannot have vanishing palinstrophy as the screening radius grows.

---

## 5. Amplitude and direction decomposition

Write where `omega!=0`

\[
\omega=\rho\,\xi,
\qquad
\rho=|\omega|,
\qquad
|\xi|=1.
\]

Then

\[
|\nabla\omega|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
\]

Therefore the transition cost splits into

\[
\boxed{
\text{amplitude-change palinstrophy}
\quad\lor\quad
\text{axis-bending palinstrophy},
}
\]

or both.

This is the standard-math realization of the axial-property split:

- loss/restoration of vorticity support;
- or directional closure/return of the vorticity axis.

---

## 6. Relation to div omega = 0

Because

\[
\nabla\cdot\omega=0,
\]

a coherent vorticity flux cannot terminate inside the shell.

If the amplitude does not substantially decay, the flux must bend, split, reverse, or return.

Hence the directional contribution

\[
\rho^2|\nabla\xi|^2
\]

is unavoidable on a positive set unless cancellation occurs through multiple signed populations.

Such population splitting returns to the finite-memory / replacement / export ledgers.

---

## 7. Enstrophy scale of the rotor core

The rotor core contains vorticity enstrophy of order

\[
Z_{core}
\sim
\int_{B_R}|\omega|^2dx
\sim R^3.
\]

The minimal broad-shell palinstrophy is

\[
Q_{trans}\gtrsim R.
\]

Therefore the associated diffusion frequency is

\[
\boxed{
\frac{Q_{trans}}{Z_{core}}
\gtrsim R^{-2}.
}
\]

This is exactly the diffusive frequency of a structure of radius `R`.

---

## 8. Diffusive lifetime and sharpness

The corresponding viscous erosion time is

\[
\Theta_{diff}\sim R^2/\nu.
\]

Over that time, the transition palinstrophy accumulates at scale

\[
Q_{trans}\Theta_{diff}
\gtrsim
R\cdot R^2
=R^3
\]

(up to viscosity normalization).

This matches the rotor-core enstrophy scale rather than exceeding it.

Thus the transition lower bound is **sharp for ordinary diffusion**.

It does not force an impossible loss rate.

---

## 9. Relation to the R~L^(1/5) shield

At the saturated screening radius

\[
R\sim L^{1/5},
\]

one has

\[
Q_{trans}\gtrsim L^{1/5},
\]

and

\[
\Theta_{diff}\sim L^{2/5}.
\]

The integrated transition palinstrophy scale is therefore

\[
\boxed{
Q_{trans}\Theta_{diff}
\gtrsim L^{3/5}.
}
\]

This remains below the `~L` parent kinetic/Morrey capacity identified in M5-317.

Hence no contradiction follows from this scalar lower bound alone.

---

## 10. What would be needed for closure

A stronger mechanism must exploit information beyond the scalar magnitude

\[
\int|\nabla\omega|^2.
\]

Candidates are

\[
\boxed{
\begin{aligned}
&\text{signed vorticity-flux closure},\\
&\text{axis-bending topology / return geometry},\\
&\text{positive-frequency rebuilding of the transition shell},\\
&\text{pressure-Hessian mismatch},\\
&\text{transition cost repeated across first-hitting generations}.
\end{aligned}
}
\]

The goal is to find a quantity whose cumulative cost is not merely the natural diffusive `R^{-2}` frequency.

---

## 11. Audit verdict

### Proved

- order-one vorticity-state transition across radius `R`, width `w` costs at least `c R^2/w` palinstrophy;
- the cheapest `w~R` transition costs `cR`;
- the cost splits exactly into amplitude-gradient and axis-bending contributions;
- the resulting `Q/Z~R^{-2}` is the natural diffusive scale.

### Firewall

- transition-shell palinstrophy alone does not close the screened rotor;
- at `R~L^(1/5)` it remains compatible with the `Theta~L^(2/5)` diffusive lifetime and the parent energy capacity.

### Next target

Use `div omega=0` and the axis decomposition to distinguish

\[
\boxed{
\text{amplitude-decay closure}
\lor
\text{return/bending closure}
\lor
\text{multi-population replacement/export}
}
\]

and seek a non-diffusive cumulative invariant.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
