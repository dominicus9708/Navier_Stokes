# M19-033 — Off-center remote packets need linear-in-eccentricity multiplicity to form a critical Morrey shell

**Date:** 2026-09-11  
**Status:** CALCULATION / R-REMOTE TO R-AC OR R-CRITICAL / OFF-CENTER MULTIPLICITY THRESHOLD

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Off-center geometry from M19-032

Let \(x_\infty\) be a finite physical accumulation point.

Consider first-hitting packets indexed by \(a\) whose centers lie in a radial shell

\[
\frac d2<|x_a-x_\infty|<2d
\]

and whose natural scales are comparable:

\[
r_a\asymp r,
\qquad
r\ll d.
\]

Define the shell eccentricity

\[
\boxed{\eta:=\frac dr\gg1.}
\]

Assume the selected packet balls \(B_{Cr}(x_a)\) have bounded overlap. If bounded overlap fails, record a clustering/multicore event rather than double counting kinetic variance.

## 2. One packet carries natural critical-scale variance

The certified first-hitting velocity-variance floor gives for every packet

\[
\boxed{
\inf_c
\int_{B_{Cr}(x_a)}|u-c|^2dx
\ge
v_*\nu^2r.
}
\]

Thus one packet contributes physical kinetic variance of order \(\nu^2r\).

Relative to the larger radial shell scale \(d\), its normalized Morrey contribution is only

\[
\boxed{
\frac{\nu^2r}{d}
\asymp
\frac{\nu^2}{\eta}.
}
\]

Hence a single increasingly eccentric packet becomes invisible in the common-center critical Morrey normalization.

## 3. M packets in one radial shell

Suppose there are \(M\) bounded-overlap comparable packets in the same radial shell at the same selected time/event layer.

After using a common shell-scale constant or a standard finite-dimensional variance decomposition, the sum of packet variances gives, up to bounded-overlap constants and a possible common-mode defect,

\[
\boxed{
\mathcal E_{shell}(d)
\gtrsim
M\nu^2r
}
\]

unless the packet velocity differences are canceled by a shell-wide common-mode/affine organization. Such cancellation is recorded separately as a projective/harmonic common-mode branch and is not silently treated as additive energy.

Ignoring only that explicitly separated cancellation branch, the shell Morrey quantity obeys

\[
\frac1d\mathcal E_{shell}(d)
\gtrsim
\nu^2\frac{Mr}{d}
=
\nu^2\frac M\eta.
\]

Therefore

\[
\boxed{
M\gtrsim\eta
\Longrightarrow
\text{order-one critical Morrey shell activity}.
}
\]

This is the exact linear multiplicity threshold.

## 4. Super-threshold multiplicity routes to R-critical

If on infinitely many terminally aligned shrinking radial shells

\[
\boxed{
M_m\ge c\eta_m,
}
\]

then

\[
\boxed{
\frac1{d_m}
\inf_c
\int_{A_{d_m}(x_\infty)}|u-c|^2dx
\ge c_*>0.
}
\]

Hence the off-center cascade produces a critical Morrey stack at the common physical point and enters

\[
\boxed{\mathcal R_{critical}.}
\]

The packet centers themselves need not satisfy bounded eccentricity individually; sufficient shell multiplicity compensates for eccentricity.

## 5. Sub-threshold multiplicity is a sparse-incidence branch

If instead

\[
\boxed{
\frac{M_m}{\eta_m}\to0
}
\]

on the shell family carrying the remote cascade, then the common-center Morrey contribution of those packets vanishes:

\[
\frac1{d_m}\mathcal E_{shell}(d_m)
\to0
\]

modulo separately typed common-mode effects.

The local first-hitting witnesses have not disappeared. They have become sparse relative to the radial-shell occupancy needed to survive at the parent critical scale.

This is precisely an occupancy/incidence deficiency.

Hence

\[
\boxed{
M_m=o(\eta_m)
\Longrightarrow
G_{sparse\ shell\ incidence}.
}
\]

This is structurally an R-AC endpoint.

## 6. Intermediate threshold and weighted version

The sharp quantity is not literally packet count when packet scales or strengths vary.

Let packet \(a\) in shell \(m\) have scale \(r_{m,a}\) and normalized variance weight \(w_{m,a}\asymp1\). Define

\[
\boxed{
\mathfrak O_m
:=
\frac1{d_m}
\sum_a w_{m,a}r_{m,a}.
}
\]

Then the shell criticality criterion is

\[
\boxed{
\mathfrak O_m\gtrsim1.
}
\]

For comparable \(r_{m,a}\asymp r_m\), this reduces to

\[
\mathfrak O_m\asymp\frac{M_m}{\eta_m}.
\]

Thus \(\mathfrak O_m\) is the correct scale-weighted shell occupancy variable.

## 7. Geometric packing is not the obstruction

A shell of volume \(O(d^3)\) can geometrically contain up to order

\[
\left(\frac dr\right)^3
=\eta^3
\]

bounded-overlap \(r\)-packets.

The critical threshold requires only order \(\eta\) packets.

Therefore there is no geometric packing contradiction:

\[
\boxed{
\eta\ll\eta^3.
}
\]

The issue is actual dynamical occupancy, not available spatial capacity.

This parallels M19-009, where parabolic time supplied enough theoretical slots and the real issue was their actual occupation.

## 8. Space-time duality of the R-AC obstruction

M19-008--010 produced the temporal threshold

\[
M_k^{time}\gtrsim K_k^2J_k^{1/2}.
\]

The present off-center calculation produces the spatial shell threshold

\[
M_m^{space}\gtrsim\eta_m.
\]

Both have the same DSD structure:

\[
\boxed{
\text{geometric opportunity is abundant}
\quad\text{but certified occupancy may be deficient}.}
\]

Thus the remaining ancestry theorem should control a joint space-time incidence measure, not time return alone.

## 9. Updated remote routing

The off-center nested remote branch now satisfies

\[
\boxed{
G_{off\text{-}center\ remote}
\Longrightarrow
\begin{cases}
G_{shell\ occupancy\ critical}\to\mathcal R_{critical},\\
G_{sparse\ shell\ incidence}\to\mathcal R_{AC},\\
G_{common\text{-}mode/projective\ cancellation}\to\text{typed projective/remote channel}.
\end{cases}
}
\]

Thus no new independent local resource is exposed by off-center geometry.

## 10. Refined R-AC theorem frontier

M19-033 suggests that the true missing R-AC theorem is joint in space and time.

A useful formulation is

\[
\boxed{
\mathcal T_{AC}^{joint}:
\text{cubic-mass-bearing first-hitting genealogy}
\Rightarrow
\text{sufficient joint radial-shell occupancy and ancestral time return}
\lor
\text{typed replacement/export/deformation exit}.
}
\]

The previously separated temporal return deficiency and off-center spatial sparsity are two projections of the same incidence problem.

## 11. Next calculation

M19-034 should define a joint incidence measure

\[
\mathfrak I_{m}
\sim
\frac1{d_m}
\sum_{a,\ell}
r_{m,a}\,
\frac{\tau_{m,a,\ell}}{r_{m,a}^2}
\times
\text{amplitude/overlap weight},
\]

with exact dimensionless normalization.

The objective is to combine the spatial threshold \(M/\eta\) and temporal return threshold \(K^{-2}\) into one representation-safe ancestry quantity. If such a measure has a finite parent ledger and a lower bound on cubic-mass-bearing shells, it could close \(\mathcal T_{AC}\); if not, the remaining missing inequality will be stated in one scalar variable.

---

\[
\boxed{\text{M19-033 COMPLETE; OFF-CENTER REMOTE GEOMETRY REDUCES TO CRITICAL OCCUPANCY OR R-AC SPARSITY.}}
\]
