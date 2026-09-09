# DSD M17-447 — A robust low-amplitude separating bottleneck in a uniformly Poincare cross-section forces an order-one palinstrophy packet, so survival requires neck geometry or time-occupancy decompactification

Date: 2026-09-09  
Canonical ID: **M17-447**

Status: **ACTIVE LOW-AMPLITUDE BOTTLENECK REDUCTION / PALINSTROPHY RETURN / GEOMETRY-TIME OCCUPANCY FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-446

M17-446 shows that the weighted coefficient-gradient budget

\[
\int q^2|\nabla\kappa|^2
\]

cannot control pairwise coefficient contrast if the coefficient transition hides inside a low-amplitude bridge.

The present module asks whether a **robust** low-amplitude separating bridge is itself free.

Under uniform cross-sectional Poincare geometry, positive high-amplitude participation, and fixed normalized bottleneck thickness, it is not free: the amplitude transition pays ordinary vorticity palinstrophy.

## 2. Normalized transverse geometry

Work in one own-scale normalized tube chart. Let `A` be a connected normalized transverse cross-section with

\[
0<|A|\le M_A
\]

and a uniform Poincare inequality

\[
\boxed{
\int_A|f-\bar f_A|^2dA
\le
C_P\int_A|\nabla_\perp f|^2dA.
}
\]

Let

\[
q:=|W|=\widetilde\rho
\]

be normalized vorticity amplitude.

Assume two measurable subsets exist:

\[
A_+\subset A,
\qquad
A_-\subset A,
\]

with

\[
|A_+|\ge m_+>0,
\qquad
|A_-|\ge m_->0,
\]

and amplitude separation

\[
\boxed{
q\ge a_+>0\quad\text{on }A_+,
\qquad
q\le a_-<a_+\quad\text{on }A_-.
}
\]

The set `A_-` represents a low-amplitude separating bottleneck of fixed normalized transverse thickness. If its measure collapses, retain neck-thickness/geometry decompactification instead of using this module.

## 3. Two-population variance lower bound

For any constant `c`,

\[
\int_A|q-c|^2dA
\ge
\int_{A_+}|q-c|^2dA
+
\int_{A_-}|q-c|^2dA.
\]

Minimizing the right-hand side over `c` gives a positive lower bound depending only on the two masses and amplitude gap. In particular,

\[
\boxed{
\int_A|q-\bar q_A|^2dA
\ge
c_{var}(m_+,m_-,M_A)
(a_+-a_-)^2
=:v_*>0.
}
\]

Thus a robust high/low amplitude separation has fixed normalized variance.

## 4. Poincare forces amplitude-gradient energy

Apply the uniform cross-sectional Poincare inequality:

\[
v_*
\le
C_P\int_A|\nabla_\perp q|^2dA.
\]

Hence

\[
\boxed{
\int_A|\nabla_\perp q|^2dA
\ge
c_*:=v_*/C_P>0.
}
\]

Since

\[
q=|W|,
\]

we have pointwise where `q>0` and by weak extension generally,

\[
|\nabla q|\le|\nabla W|.
\]

Therefore

\[
\boxed{
\int_A|\nabla_\perp W|^2dA
\ge c_*>0.
}
\]

The low-amplitude bottleneck returns to vorticity palinstrophy rather than escaping through the `q^2` coefficient-gradient weight.

## 5. Lift from one cross-section to one own-scale tube segment

A single measure-zero cross-section is not yet a three-dimensional palinstrophy packet.

Assume the robust state margins of Sections 2--4 persist on a longitudinal normalized segment of length

\[
\ell_z\ge\ell_*>0
\]

with a uniformly regular tube chart.

Then Fubini gives

\[
\boxed{
\int_{T_{seg}}|\nabla W|^2dy
\ge
c_*\ell_*
=:p_*>0.
}
\]

If longitudinal persistence fails, retain longitudinal chart/geometry localization loss.

## 6. Own-time persistence

Assume the normalized state remains in the strict high/low amplitude and Poincare-geometry class for a fixed normalized time

\[
\Delta s\ge\tau_*>0.
\]

This follows from a strict compact state margin plus bounded normalized material/time derivatives; failure is retyped as time/high-jet decompactification.

Then

\[
\boxed{
\int_{I_{own}}
\int_{T_{seg}}|\nabla W|^2dyds
\ge
p_*\tau_*
=:\pi_*>0.
}
\]

Thus every robust low-amplitude separating bottleneck episode pays an order-one normalized palinstrophy packet.

## 7. Cross-generation ledger

M17-307 gives

\[
\boxed{
\sum_mR_m^{-1}
\int_I\|\nabla\Omega_m\|_2^2ds
<\infty.
}
\]

Suppose record `m` contains `N_m^{bot}` bounded-overlap bottleneck own-time packets of the type above. Then

\[
\boxed{
\sum_m
\frac{N_m^{bot}}{R_m}
<\infty.
}
\]

This is much more favorable than the M17-445 quintic coefficient-gradient firewall.

## 8. Parent-time occupancy threshold

Let `beta_m` be the fraction of one parent-normalized record time for which a robust bottleneck of this type is present on at least one retained own-scale segment.

One descendant own-time has parent duration `~R_m^{-2}`. Hence the number of time packets is

\[
N_m^{bot}
\gtrsim
c\beta_mR_m^2.
\]

Therefore the M17-307 ancestry contribution is

\[
\boxed{
R_m^{-1}N_m^{bot}
\gtrsim
c\beta_mR_m.
}
\]

Consequently finite ancestral palinstrophy requires

\[
\boxed{
\sum_m\beta_mR_m<\infty.
}
\]

For geometric `R_m`, any uniform positive bottleneck time fraction is impossible. More strongly, even

\[
\beta_m\gtrsim cR_m^{-1}
\]

on infinitely many records is at the nonsummable threshold.

Thus a surviving low-amplitude separator must be extremely sparse in parent time unless geometry or the robust packet hypotheses decompactify.

## 9. Relation to M17-441 amplitude collapse

M17-441 requires the flux-weighted normalized amplitude sequence to be summable on a retained positive-flux survivor.

M17-447 shows that one particular mechanism for maintaining strong coefficient segregation during that collapse — a robust finite-thickness low-amplitude separator between substantial high-amplitude populations — is expensive in palinstrophy if it persists for appreciable parent time.

Therefore the survivor must further refine to one or more of:

1. the low-amplitude bottleneck occupies vanishing transverse measure;
2. the Poincare constant blows up through a thin neck/disconnected geometry;
3. high-amplitude flux participation on one side vanishes;
4. bottleneck parent-time occupancy `beta_m` decays fast enough that `sum beta_m R_m < infinity`;
5. longitudinal/time persistence fails;
6. chart/topology/genealogy/interface compactness fails.

## 10. Important firewall: no claim from one instantaneous bottleneck

A single bottleneck snapshot per geometric record pays only one order-one normalized palinstrophy packet. Its ancestry cost is

\[
R_m^{-1},
\]

which is summable.

Thus M17-447 does **not** close sparse instantaneous bottlenecks.

The gain comes from robust time occupancy or record-linear multiplicity.

## 11. DSD audit role

DSD is used only to test whether a low-amplitude escape in one weighted resource becomes a payer in another resource. The mathematics is variance, Poincare, the Kato inequality `|nabla|W|| <= |nabla W|`, Fubini, and M17-307 scaling.

## 12. Audit verdict

**PASS — a robust finite-thickness low-amplitude separating bottleneck is an order-one palinstrophy payer.**

A surviving coefficient-redistribution branch must therefore make the separator geometrically thin/Poincare-degenerate, high-amplitude-flux poor, temporally sparse, or leave the retained chart/genealogy class.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
