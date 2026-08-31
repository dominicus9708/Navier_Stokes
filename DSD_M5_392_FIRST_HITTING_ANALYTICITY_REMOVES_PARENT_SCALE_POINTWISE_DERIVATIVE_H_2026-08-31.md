# DSD M5-392 — First-hitting analyticity removes parent-scale pointwise derivative H

Date: 2026-08-31

Status: **SCOPE CORRECTION / THE STAGE-WIDE FIRST-HITTING ANALYTICITY THEOREM ALREADY GIVES UNIFORM `L-infinity` BOUNDS FOR EVERY FIXED NORMALIZED VORTICITY DERIVATIVE ON EACH LATE FIRST-HITTING STAGE / THEREFORE PARENT-SCALE `grad^m Omega -> infinity`, THE THIN-CENTER ALTERNATIVE OF M5-377, AND THE UNBOUNDED LAPLACIAN EXPOSURE SUBCASE OF M5-391 ARE NOT GENUINE SURVIVORS ON THE ORIGINAL SMOOTH FIRST-HITTING CORRIDOR / THE REMAINING H FRONTIER MUST BE INTERPRETED AS SCALE-CRITICAL DERIVATIVE MASS/OCCUPANCY OVER GROWING SPATIAL WINDOWS, RELATIVE INTERNAL-SCALE SEPARATION INSIDE REMOTE PACKETS, OR NONLOCAL CZ/HARMONIC VELOCITY-GRADIENT ESCALATION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

Several recent reduction notes route difficult geometry to symbols such as

\[
H_{der,\infty},
\qquad
H_{high-der},
\qquad
H_{micro/freq/cap}.
\]

Those labels were deliberately broad.

The fixed-lag packet theorem contains a stronger smooth first-hitting fact that now needs to be propagated through the master tree:

**bounded vorticity up to the next first-hitting threshold gives a fixed natural analyticity radius and uniform bounds for every fixed normalized vorticity derivative throughout the stage.**

Therefore not every derivative-H label remains a genuine pointwise escape on the original physical first-hitting normalization.

---

## 2. Stage-wide analyticity theorem

On stage `j`, for

\[
t\in[t_j,t_{j+1}),
\]

the next-threshold definition gives

\[
\|\omega(t)\|_\infty<W_{j+1}=qW_j.
\]

Restart the standard short-time vorticity analyticity theorem at

\[
t^- = t-\theta_{an}/W_{j+1}
\]

with fixed sufficiently small `theta_an>0`.

The resulting physical analyticity radius is comparable to

\[
\sqrt{\frac{\nu}{W_{j+1}}}
\asymp r_j.
\]

In parent normalized variables

\[
y=\frac{x-X_j}{r_j},
\qquad
\Omega_j=\frac{\omega}{W_j},
\]

there is therefore a fixed stage-wide analytic radius

\[
\rho_{stage}>0
\]

and, for every fixed integer `m>=0`,

\[
\boxed{
\sup_{t\in[t_j,t_{j+1})}
\|\nabla_y^m\Omega_j(\cdot,t)\|_\infty
\le C_{m,stage}<\infty.
}
\]

The constants depend on the fixed first-hitting ratio, viscosity convention, analytic theorem constants, and derivative order, but not on the late stage index `j`.

This estimate is global in the parent spatial variables, not only at the tracked maximum.

---

## 3. Central continuity radius cannot collapse

M5-377 defined a central continuity radius `rho_j` at a normalized vorticity maximum and allowed the formal alternative

\[
\rho_j\to0
\Longrightarrow
\|\nabla_Y\Omega_j\|_\infty\to\infty.
\]

But the stage-wide `m=1` bound gives

\[
\|\nabla_Y\Omega_j\|_\infty\le C_1.
\]

For any fixed `epsilon0>0`, the mean-value theorem therefore guarantees

\[
|\Omega_j(Y)-\Omega_j(0)|\le\epsilon_0
\]

whenever

\[
|Y|\le \epsilon_0/C_1.
\]

Thus

\[
\boxed{
\rho_j\ge c(\epsilon_0,C_1)>0.
}
\]

The thin-center branch is removed on the actual smooth first-hitting stage.

Consequently a fixed-fraction natural productive shell from M5-377 always enters the **thick-center** Poincare alternative and gives local normalized palinstrophy occupancy rather than pointwise derivative blowup.

---

## 4. Unbounded normalized Laplacian exposure is impossible

M5-391 defined

\[
\mathcal D_j
=
\int_{\widehat I_j}
\sup_{\widehat A_j(\tau)}
|\Delta_Y\Omega_j|d\tau.
\]

The stage-wide `m=2` analytic estimate gives

\[
\sup_{\widehat I_j}
\|\Delta_Y\Omega_j\|_\infty
\le C_2.
\]

With the existing normalized stage ceiling

\[
|\widehat I_j|\le L_*,
\]

one obtains

\[
\boxed{
\mathcal D_j
\le L_*C_2.
}
\]

Therefore

\[
\boxed{
\mathcal D_j\to\infty
}
\]

cannot occur on the retained smooth first-hitting corridor.

The diffusion part of “genuinely unformed exposure” in M5-391 is automatically bounded at the parent natural scale.

---

## 5. The same holds for every fixed pointwise vorticity derivative

More generally, for every fixed `m`,

\[
\boxed{
\sup_j\sup_{\widehat I_j}
\|\nabla_Y^m\Omega_j\|_\infty
<\infty.
}
\]

Thus a branch described literally as

\[
\|\nabla_Y^m\Omega_j\|_\infty\to\infty
\]

is incompatible with the original first-hitting parent normalization.

If such a divergence appears in a later extracted similarity/Euler/satellite representation, its relation to the original parent scale must be audited explicitly; one must not silently identify it with a sub-natural physical derivative blowup inside a stage.

---

## 6. What H can still mean

The derivative/frequency H frontier is **not** eliminated.

The analyticity bound is pointwise and fixed-order. Several scale-critical mechanisms remain possible.

### A. Critical derivative mass on growing windows

Even if

\[
|\nabla_Y\Omega_j|\le C_1,
\]

the integral

\[
R\int_{A_R}|\nabla U|^2
\]

or corresponding H1/H2 shell quantities may grow because the active region occupies more spatial volume or more remote shells.

This is a mass/occupancy/multiplicity escape, not a pointwise derivative-amplitude escape.

### B. Relative internal-scale separation

The remote H2/H1 audit defines

\[
\delta_R^2
=
\frac{\int|\nabla U|^2}{\int|\nabla^2U|^2}.
\]

The conclusion

\[
\delta_R/R\to0
\]

means that the internal active scale is small **relative to a large remote radius `R`**.

It does not require

\[
\delta_R\to0
\]

in parent natural units.

Thus the remote-satellite/frequency interpretation remains consistent with stage-wide analyticity.

### C. Nonlocal velocity-gradient escalation

A bounded vorticity field does not give an `L-infinity` bound on the full strain/velocity gradient.

The Calderon--Zygmund near/middle/far audit M5-371 gives

\[
|S(x)|
\lesssim
\int_0^\rho\frac{\omega_\Omega(x,r)}rdr
+
\|\Omega\|_\infty\log(R/\rho)
+
R^{-5/2}\|V\|_2.
\]

Stage-wide analyticity controls the genuinely local Dini part at parent scale.

Large `grad U` can still be generated by an increasing logarithmic scale range, remote active sources, or harmonic/affine strain.

Therefore similarity-gradient H is fundamentally nonlocal on this corridor.

---

## 7. Reinterpret M5-371--378 under analyticity

The old decomposition

\[
H_{\nabla,sim}
\Longrightarrow
H_\omega
\lor H_{Dini/dir}
\lor H_{angular,multiscale}
\lor T_{remote}
\]

remains a valid source ledger.

But stage-wide analyticity sharpens its physical interpretation:

- local parent-scale Dini derivative amplitudes are uniformly bounded;
- natural productive angular shells have positive center capacity;
- genuinely problematic accumulation must migrate into scale distribution/remote source/occupancy rather than an arbitrarily sharp local cusp at the current maximum.

Together with M5-376--377, the local natural source route becomes a **formed local palinstrophy/capacity occupancy**, while unbounded pointwise strain remains a remote/nonlocal source problem.

---

## 8. Reinterpret the current H label

After M5-392 the notation

\[
H_{micro/freq/cap}
\]

should not be read as one phenomenon.

A more accurate active split is

\[
\boxed{
H_{micro/freq/cap}
=
H_{crit\,mass/occupancy}
\lor
H_{remote\,relative-frequency}
\lor
H_{nonlocal\,strain}.
}

Here:

1. `H_crit mass/occupancy` = scale-critical derivative/enstrophy/palinstrophy content over formed sets/windows;
2. `H_remote relative-frequency` = active internal scale much smaller than its distance/observation radius, without violating the natural analytic floor;
3. `H_nonlocal strain` = CZ/harmonic strain escalation from broad or remote source structure.

This scope split prevents future calculations from chasing an impossible parent-scale derivative infinity.

---

## 9. Consequence for M5-391

M5-391 concluded that genuinely unbounded reformation exposure gives

\[
H_{micro/freq/cap}
\lor T_{remote/formed}.
\]

M5-392 sharpens this because the diffusion exposure cannot diverge.

Thus the only genuinely unbounded adjacent exposure is the velocity-gradient/Lipschitz side:

\[
\boxed{
T_{reformation}^{unbounded}
\Longrightarrow
H_{nonlocal\,strain}
\lor
T_{remote/formed}.
}

There is no independent parent-scale `Delta Omega` explosion on the smooth stage.

---

## 10. DSD audit

### Corrected

- `H_der,infinity` at the tracked natural-scale maximum is removed as a late physical first-hitting survivor;
- M5-377 thin-center branch is removed on the standard analytic corridor;
- M5-391 unbounded normalized Laplacian exposure is removed.

### Retained

- local derivative **occupancy** and scale-critical integral costs;
- remote relative-scale frequency concentration;
- nonlocal strain/harmonic escalation;
- later extracted limit profiles whose scale relation must be audited separately.

### Firewall

Analyticity does not give a global `L-infinity` bound on strain from bounded vorticity.

It also does not make integrated critical derivative mass finite on arbitrarily large normalized spatial domains.

Therefore this note narrows H but does not close it.

---

## 11. Updated frontier

Combining M5-390--392, the late smooth first-hitting problem is organized as

\[
\boxed{
H_{crit\,mass/occupancy}
\lor
H_{remote\,relative-frequency/nonlocal\,strain}
\lor
R_{contact}^{formed}
\lor
T_{replacement/export}^{formed}.
}

The next efficient target should therefore be **not** another pointwise derivative estimate.

It should connect the scale-invariant natural flux carrier/contact-replacement genealogy to the critical-mass/nonlocal-strain H ledger.

---

## 12. Audit verdict

### REMOVED

Parent-scale pointwise normalized vorticity derivative blowup as a first-hitting survivor.

### SHARPENED H FRONTIER

\[
\boxed{
H_{crit\,mass/occupancy}
\lor
H_{remote\,relative-frequency}
\lor
H_{nonlocal\,strain}.
}

### STILL OPEN

- global pricing of critical derivative occupancy;
- remote relative-frequency/nonlocal-strain branch;
- formed contact/replacement genealogy;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
