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
- **M17-013** — the semilinear great-circle system closes the material dynamics of `(q,x_3)` as `q'=H`, `x_3'=G+x_3/2`, with `H_q=kappa-G_3-1/2`. Hence the reduced label-flow divergence is exactly `kappa`, and its area Jacobian equals the M5 amplification factor `a=exp∫kappa`. At a regular `kappa=0` root, `h=F_qq V_rel`; M5-685 hysteresis is therefore label-area hysteresis, not an arbitrary oscillator. Scalar hysteresis alone does not distinguish axisymmetric from non-axisymmetric geometry.
- **M17-014** — the M17-010 law `D_B G_h=(kappa-3/2)G_h` freezes the normalized nodal-Jacobian shape. The winding sign, singular-value ratio, determinant-normalized shape tensor, and anisotropy index are material invariants. A regular axisymmetric no-swirl axis has positive winding and equal singular values. Therefore a negative-index or anisotropic positive-index regular filament cannot enter the axisymmetric firewall without nodal rank loss/degeneration.

## Current frontier

The director branch remains

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

### Rank one — scalar label dynamics
On every regular great-circle region,

\[
\boxed{
\begin{aligned}
q'&=H(q,x_3,\theta),\\
x_3'&=K(q,x_3,\theta),\\
K&=G+\frac12x_3,\\
\partial_qH+\partial_3K&=\kappa.
\end{aligned}
}
\]

Thus

\[
\boxed{
J_L'=\kappa J_L,
\qquad
J_L=a,
}
\]

so the M5-685 flux-weighted `kappa=0` hysteresis is exactly an expansion/contraction hysteresis of the reduced material label area.

### Rank one — nodal shape channel
For every uniformly regular recurrent winding filament,

\[
\boxed{
D_BG_h
=\left(\kappa-\frac32\right)G_h.
}
\]

Therefore

\[
\boxed{
\operatorname{sgn}\det G_h,
\quad
\widehat C=
\frac{G_h^TG_h}{|\det G_h|},
\quad
\mathcal A=\frac12\operatorname{tr}\widehat C
}
\]

are material invariants.

The regular nodal core splits into

\[
\boxed{
R_{nodal}^{uniform}
\Longrightarrow
G_{conf+}^{core}
\ \lor\ 
G_{aniso+}^{core}
\ \lor\ 
G_{index-}^{core}.
}
\]

- `G_conf+^core`: positive-index conformal first-order core (`A=1`), locally compatible with the axisymmetric firewall but not sufficient for global axisymmetry.
- `G_aniso+^core`: positive winding but `A>1`; cannot become axisymmetric while regular.
- `G_index-^core`: negative-index simple zero; cannot become the positive-index axisymmetric core while regular.

For `G_aniso+^core` and `G_index-^core`, an axisymmetric/no-swirl escape requires rank loss or finite-jet nodal degeneration first.

## DSD audit conclusion through M17-014

Two formerly conflated channels are now separated:

\[
\boxed{
\text{scalar amplification/hysteresis}
\quad\neq\quad
\text{horizontal nodal shape}.
}
\]

The scalar channel is described by

\[
(\kappa,h,a)
\]

and reduces to the two-dimensional label flow.
The geometric channel is described by

\[
(\operatorname{sgn}\det G_h,\widehat C).
\]

A proof attempt that tracks only `kappa` can reproduce the known regular axisymmetric firewall and a genuinely non-axisymmetric core with identical scalar history, so it cannot close the branch by itself.

## Current rank-one chain

On the uniformly regular recurrent subbranch,

\[
\boxed{
R_{nodal}^{uniform}
\Longrightarrow
P_{tube}^{+}
\Longrightarrow
N_{bulk}^{-}
\Longrightarrow
H_{label}
\quad+
A_{nodal}.
}
\]

Here

- `H_label` is the M17-013/M5-685 area-Jacobian hysteresis requirement;
- `A_nodal` is the M17-014 fixed nodal-shape class.

The remaining exits are

\[
\boxed{
\text{rank loss / finite-jet turnover}
\ \lor\ 
G_{conf+}^{core}\text{ higher-jet axisymmetry test}
\ \lor\ 
G_{aniso+}^{core}\text{ recurrent survivor}
\ \lor\ 
G_{index-}^{core}\text{ recurrent survivor}.
}
\]

## Next target — Nodal Shape–Hysteresis Compatibility Gate (NSHCG)

The highest-value next calculation is to combine

\[
\Delta q=F(q,x_3,\theta)
\]

with the materially fixed non-axisymmetric Hessian shape at the critical filament and the reduced label-area hysteresis.

The target descriptors are

1. third/fourth jets of `q` at the nondegenerate critical filament;
2. curvature and enclosed area of nearby q-level contours;
3. their material transport under `q'=H`, `x_3'=K`;
4. compatibility with the M17-012 finite-radius positive sheath / negative payer cycle.

The desired classification is

\[
\boxed{
\text{persistent non-axisymmetric shape+hysteresis}
\Longrightarrow
\text{finite-jet degeneration}
\ \lor\ 
\text{regular higher-jet model}
\ \lor\ 
\text{new signed incompatibility}.
}
\]

The rank-two director-area branch remains separately open and must be closed before any full proof claim.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
