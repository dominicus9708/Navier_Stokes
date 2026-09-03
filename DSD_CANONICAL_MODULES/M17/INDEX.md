# M17 — Material director geometry, weighted-harmonic rank, and nodal topology

Canonical continuation split from M16 after M16-023.

## Independent question
Once the M16 kappa/residence audit forces same-tube axial strain heterogeneity, can the CE-H material director field sustain a recurrent nontrivial spatial geometry under `D_B xi = 0` and the weighted harmonic-director equation?

## Canonical reassignment
The following files were first written provisionally under M16 and are now canonically reassigned:

- **M17-001** = provisional M16-024 — axial strain channels collapse to same-tube director geometry.
- **M17-002** = provisional M16-025 — frozen transverse director deformation and material director-area invariant.
- **M17-003** = provisional M16-026 — rank-one weighted-harmonic director collapses to a great-circle phase.
- **M17-004** = provisional M16-027 — great-circle branch reduces to a semilinear 2.5D streamfunction system.
- **M17-005** = provisional M16-028 — bounded phase lift is trivial; nonzero rank-one survivor requires winding around the vorticity zero set.

The provisional M16 source files are retained for provenance and are superseded by these canonical IDs.

## Native M17 continuation
- **M17-006** — great-circle winding rewritten as a complex real-potential Schrödinger nodal-defect problem `Delta f = kappa f`; weighted phase energy is not topologically quantized near analytic zeros.
- **M17-007** — regular codimension-two winding zeros admit analytic extension of `kappa` and are material nodal filaments; winding topology is frozen unless a degenerate nodal event occurs.
- **M17-008** — axisymmetric Navier--Stokes without swirl is an exact known-regular model of the material great-circle/winding CE-H geometry; winding itself is therefore a firewall, not a contradiction.
- **M17-009** — nodal creation/reconnection cannot evade through arbitrarily flat zeros; compactness plus analyticity gives a uniform finite nodal-jet order `m_*` and nonzero jet floor.
- **M17-010** — a regular winding core forces transverse strain isotropy `spec Sigma = {lambda,lambda,-2lambda}`. The nodal Jacobian obeys exact multiplier laws; recurrent regular horizontal Jacobian forces `⟨kappa⟩_nodal = 3/2`, while a persistent slanted derivative additionally forces `⟨lambda⟩_nodal = 0`.
- **M17-011** — the regular nodal skeleton is enstrophy-measure-thin: `∫_{D_r} kappa|W|^2 = O(r^4)` per unit filament length, while transverse gradient energy and radial boundary flux are both `O(r^2)` with the same leading coefficient. Hence the positive nodal mean does not force an infinitesimal sign contradiction. Differentiating `Delta W = kappa W` at the zero gives the exact third-jet law `Delta G = kappa_0 G` for `G=∇W`, and the recurrent nodal constraint becomes a normalized Jacobian-curvature mean of `3/2`.
- **M17-012** — compact hard-hull bounds upgrade the recurrent nodal mean to a positive-density set of strongly positive `kappa_0` phases. Uniform Jacobian nondegeneracy plus derivative bounds produce a fixed finite-radius positive-`kappa` sheath with `∫ kappa|W|^2 >= Q_* > 0`; the global signed identity then forces a fixed-size negative-`kappa` payer. The pure measure-zero escape is therefore closed on the uniformly regular recurrent-filament branch, linking M17 directly to the M5 zero-level/sheath-turnover and flux-hysteresis mechanisms.

## Current frontier

The director branch has split into rank two and rank one:

\[
\boxed{
B_{dir}
\Longrightarrow
R_2^{director-area}
\ \lor\ 
R_1^{great-circle/winding}.
}
\]

### Rank two
`R_2` carries a nonzero pullback of the `S^2` area 2-form. In material coordinates the director-area charge is exactly conserved. This is not yet a contradiction; the remaining question is its compatibility with finite transverse vorticity flux and recurrent material cross-sections.

### Rank one
The uniformly regular recurrent great-circle branch is now

\[
\boxed{
R_{nodal}^{uniform}
\Longrightarrow
P_{tube}^{+}
\Longrightarrow
N_{bulk}^{-}
\Longrightarrow
Z_\kappa
\ \lor\ 
D_\kappa^{sing}
\ \lor\ 
G_{axis/no\text{-}swirl}
\ \lor\ 
H_{CE-H}^{nonaxis}.
}
\]

- `P_tube^+`: positive-density finite-radius positive-`kappa` sheath forced by `⟨kappa_0⟩=3/2`, compactness, and the nodal Jacobian lower bound.
- `N_bulk^-`: compensating negative weighted payer with fixed lower bound on every strongly positive nodal phase.
- `Z_kappa`: regular zero-level/sheath-turnover channel, linking to M5-638.
- `D_kappa^{sing}`: singular or critical zero-level geometry, rank loss, or finite-jet nodal turnover.
- `G_axis/no-swirl`: known regular axisymmetric no-swirl firewall model.
- `H_CE-H^{nonaxis}`: genuinely non-axisymmetric recurrent constitutive hysteresis branch, linking to M5-685.

The broader rank-one branch still contains `T_nodal^{finite-jet}` and non-uniform regularity exits outside the M17-010 bounded-Jacobian hypothesis.

## DSD audit conclusion through M17-012

The former apparent sign conflict

\[
\langle\kappa\rangle_{nodal}=\frac32
\quad\text{versus}\quad
\int\kappa|W|^2=-P<0
\]

cannot be closed at infinitesimal radius because the nodal `|W|^2` measure is quartically thin.
However, compactness and uniform regularity prevent the positive nodal signal from remaining measure-zero forever:

\[
\boxed{
W=0
\to
G=\nabla W\neq0
\to
|W|\gtrsim |z|
\to
Q_+\ge Q_*>0
\to
Q_-\ge P+Q_*.
}
\]

Thus the infinitesimal sign-contradiction route is pruned, while the pure measure-zero escape is also pruned on the uniformly regular recurrent subbranch.
The problem has become a finite-radius payer/zero-crossing/hysteresis classification problem.

## Next target — non-axisymmetric constitutive hysteresis gate

The highest-value next calculation is to combine the M17 recurrent core/sheath constraints

\[
\boxed{
\langle\kappa_0\rangle_{nodal}=\frac32,
\qquad
Q_-\ge Q_*>0
}
\]

with the M5-685 zero-crossing constitutive law

\[
\boxed{
h
=L_\rho\kappa+L_\rho\sigma+\mathcal R_{geom}
\qquad(\kappa=0),
}
\]

and determine whether a recurrent **non-axisymmetric** great-circle field can generate the required negative flux-weighted crossing bias

\[
\overline G_0(0)=0,
\qquad
\overline G_\Phi(0)<0
\]

without

\[
\boxed{
\text{rank loss}
\ \lor\ 
\text{finite-jet turnover}
\ \lor\ 
\text{axisymmetric/no-swirl reduction}.
}
\]

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
