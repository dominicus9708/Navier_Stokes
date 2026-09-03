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
The great-circle branch is now

\[
\boxed{
R_1^{great-circle}
\Longrightarrow
R_{nodal}^{material}
\ \lor\ 
T_{nodal}^{finite-jet}
\ \lor\ 
G_{nonaxis}^{rank1}.
}
\]

- `R_nodal^material`: regular winding nodal filaments transported materially; every uniformly recurrent regular filament has `⟨kappa⟩_nodal = 3/2`.
- `T_nodal^{finite-jet}`: topology change through a uniformly bounded finite-order analytic nodal-jet event.
- `G_nonaxis^{rank1}`: persistent non-axisymmetric great-circle geometry without nodal topology turnover. The axisymmetric no-swirl class is a known regular submodel, so this is a classification gap rather than a topology-exclusion problem.

## Next target
The highest-value next calculation is the **nodal-skeleton / bulk-sheath compatibility**:

\[
\boxed{
\langle\kappa\rangle_{nodal}=\frac32
\quad\text{versus}\quad
\int\kappa|W|^2=-P<0.
}
\]

Determine whether the positive-`kappa` material winding skeleton can coexist recurrently with the negative enstrophy-weighted bulk without forcing a `kappa=0` sheet, nodal degeneration, or material turnover already audited in M14--M16.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
