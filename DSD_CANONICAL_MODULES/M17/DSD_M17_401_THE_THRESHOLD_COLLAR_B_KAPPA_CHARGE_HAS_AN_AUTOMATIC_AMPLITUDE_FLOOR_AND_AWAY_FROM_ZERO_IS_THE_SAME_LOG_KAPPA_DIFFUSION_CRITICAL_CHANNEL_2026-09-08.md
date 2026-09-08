# DSD M17-401 — The threshold-collar `B_kappa` charge has an automatic amplitude floor and away from zero is the same log-`kappa` diffusion critical channel

Date: 2026-09-08  
Canonical ID: **M17-401**

Status: **ACTIVE THRESHOLD-COEFFICIENT CLASSIFICATION / AMPLITUDE-FIREWALL REMOVAL / LOG-DIFFUSION RETURN**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-196/398/400

M17-196 introduces the coefficient-gradient amplitude-collar charge

\[
\boxed{
B_\kappa
:=
\int
\chi'(\rho)e^{2\kappa}
\rho^3|\nabla\kappa|^2dy
\ge0.
}
\]

M17-398 shows that the other bulk/collar gradient payers `D_sigma`, `P_W`, `B_rho`, and `B_sigma` return to normalized palinstrophy and hence the M17-307 inverse-record-scale firewall.

M17-400 returns the remaining `kappa`-phase-tilt strain-residence payer to the raw-`H2` firewall.

Thus `B_kappa` is the last distinct positive gradient charge in the M5-688 threshold architecture.

## 2. The cutoff collar has an automatic amplitude floor

The cutoff `chi` is fixed once and for all and transitions only on a compact positive-amplitude interval.

Therefore there exist constants

\[
0<a_-<a_+<\infty
\]

such that

\[
\operatorname{supp}\chi'
\subset
\{a_-\le\rho\le a_+\}.
\]

Hence every point contributing to `B_kappa` satisfies

\[
\boxed{
\rho\ge a_->0.
}
\]

This is crucial: unlike the remote low-amplitude M17-235 packet branch, the threshold-collar coefficient charge cannot make its vorticity weight vanish by sending `rho->0` while remaining inside the same collar.

Therefore the old low-amplitude packet-mass firewall is absent **on the support of `B_kappa` itself**.

## 3. Remove harmless amplitude and exponential weights on the compact hull

On the compact recurrent CE-H hull,

\[
|\kappa|\le K_*.
\]

On the cutoff collar,

\[
a_-\le\rho\le a_+.
\]

Therefore

\[
e^{-2K_*}a_-^3
\le
e^{2\kappa}\rho^3
\le
e^{2K_*}a_+^3.
\]

The only additional factor is the fixed nonnegative `chi'(rho)`.

Thus `B_kappa` is quantitatively a fixed-collar coefficient-gradient occupancy:

\[
\boxed{
B_\kappa
\asymp
\int_{\operatorname{supp}\chi'}
\chi'(\rho)|\nabla\kappa|^2dy
}
\]

with constants depending only on the chosen cutoff and compact hull bounds.

No packet amplitude `M_B` appears.

## 4. Away-from-zero logarithmic coefficient corridor

Fix

\[
0<\delta<K_*.
\]

Split

\[
B_\kappa
=
B_\kappa^{near}(\delta)
+
B_\kappa^{away}(\delta)
\]

according to

\[
|\kappa|<\delta
\quad\text{or}\quad
|\kappa|\ge\delta.
\]

Define the away-from-zero collar log-diffusion charge

\[
\boxed{
B_{\log\kappa}^{away}(\delta)
:=
\int_{|\kappa|\ge\delta}
\chi'e^{2\kappa}\rho^3
|\nabla\log|\kappa||^2dy.
}
\]

Since

\[
|\nabla\log|\kappa||^2
=
\frac{|\nabla\kappa|^2}{\kappa^2},
\]

and

\[
\delta\le|\kappa|\le K_*,
\]

we get

\[
\boxed{
K_*^{-2}B_\kappa^{away}(\delta)
\le
B_{\log\kappa}^{away}(\delta)
\le
\delta^{-2}B_\kappa^{away}(\delta).
}
\]

Thus away from zero the threshold-collar coefficient-gradient charge is exactly the same logarithmic coefficient-diffusion channel as M17-394/397, up to fixed constants.

## 5. Fixed away-from-zero `B_kappa` gives a fixed normalized critical coefficient-diffusion payment

Suppose for some fixed `eta>0`

\[
B_\kappa^{away}(\delta)
\ge
\eta B_\kappa
\]

and

\[
B_\kappa\ge b_*>0.
\]

Then Section 4 gives

\[
\boxed{
B_{\log\kappa}^{away}(\delta)
\ge
K_*^{-2}\eta b_*>0.
}
\]

Hence the away-zero threshold-gradient branch returns to the M17-396/397 normalized coefficient/log-diffusion critical-charge architecture.

No new derivative currency is created by the amplitude threshold.

## 6. Near-zero threshold coefficient diffusion

If instead

\[
B_\kappa^{near}(\delta)
\ge
(1-\eta)B_\kappa,
\]

then a fixed portion of the threshold coefficient-gradient charge lies inside

\[
|\kappa|<\delta.
\]

This is a near-zero coefficient corridor.

The logarithmic coordinate must not be used through `kappa=0`.

The correct split is:

- if the zero level is regularly realized, route to M17-343/346 zero-level thickening/spatial charge;
- if the population remains one-sided and approaches zero, retain zero-approach/criticality;
- if the corridor is lost through amplitude cutoff topology, interface, rank, or domain change, record that explicit exit.

Thus the near-zero part is already part of the existing zero-corridor architecture rather than an independent threshold-gradient mechanism.

## 7. Why the amplitude firewall is genuinely absent here

M17-235 gave

\[
\int\rho^2|\nabla\kappa|^2
\gtrsim
M_B R^{-6},
\]

and the factor `M_B` could vanish on remote low-amplitude packets.

For `B_kappa`, by contrast, the contribution is supported where

\[
\rho\ge a_->0.
\]

Therefore if the geometric measure of the active collar-gradient population remains nondegenerate, its coefficient-gradient charge cannot be suppressed by amplitude collapse.

If the active collar population itself shrinks to zero measure, that is precisely an amplitude-threshold occupancy/cutoff-transition loss, not the old low-amplitude packet firewall.

## 8. Cross-generation status

The classification above is same-generation normalized mathematics.

It does **not** create a finite ancestral budget for `B_kappa` or `B_logkappa`.

Away from zero, M17-397 already shows that the corresponding multiplier/log-diffusion architecture is a recurrent cycle-work charge without a certified finite cross-generation total.

Near zero, M17-343/346 gives scale-critical crossing/spatial charges but likewise does not yet supply a finite ancestral total.

Therefore

\[
\boxed{
B_\kappa>0
\not\Rightarrow
\text{ancestral contradiction}
}
\]

at the present stage.

The advance is the removal of `B_kappa` as a distinct analytic resource type.

## 9. Revised M5-688 positive-gradient frontier

After M17-398--401, every positive gradient payer in the M5-688 architecture is classified:

\[
\boxed{
\begin{aligned}
D_\sigma,P_W,B_\rho,B_\sigma
&\to
\text{palinstrophy firewall},\\
\mathcal P_{\kappa\sigma}^{tilt}
&\to
\text{raw-`H2` firewall},\\
B_\kappa^{away}
&\to
\text{log-`kappa` diffusion critical firewall},\\
B_\kappa^{near}
&\to
\text{zero-corridor/crossing architecture}.
\end{aligned}
}
\]

Thus no broad positive-gradient category remains untyped.

## 10. What remains genuinely distinct

The remaining M5-688 exits are now source/topology channels rather than unidentified gradient norms:

1. amplitude-cutoff/threshold replenishment and occupancy transfer;
2. near-zero regularity/zero crossing where appropriate;
3. component/interface/rank/domain/genealogy loss;
4. cross-generation reuse of the already classified critical charges.

This is a major payer-tree compression.

## 11. DSD audit role

The DSD role is an amplitude-support audit.

A weighted coefficient-gradient term can appear to retain an amplitude firewall merely because it contains powers of `rho`.

Here the weight lives on a fixed positive-amplitude collar, so the support information itself supplies the amplitude floor.

The canonical proof is elementary support restriction and the identity `grad log|kappa|=grad kappa/kappa` away from zero.

## 12. Audit verdict

**PASS — `B_kappa` is no longer an independent unclassified M5-688 payer.**

Away from zero it is the same log-coefficient diffusion critical charge; near zero it enters the existing zero-corridor machinery.

The next highest-value target is therefore the **cutoff/threshold replenishment and occupancy-transfer source**, because it is now the last broad M5-688 payer category not already returned to a known palinstrophy, raw-`H2`, coefficient-diffusion, or zero-level firewall.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
