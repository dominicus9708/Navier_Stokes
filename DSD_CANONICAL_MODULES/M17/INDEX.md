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
- **M17-015** — on a vertical genuinely non-axisymmetric regular core, the matrix compatibility law `(G_q-1)Q=lambda_3 I` holds. Every non-scalar critical Hessian `Q` therefore forces `G_q=1` and `partial_3 lambda=0` at the core, adding an exact vertical-velocity and strain constraint to the non-axisymmetric branch.
- **M17-016** — for a vertical filament centered on the candidate symmetry axis, the angular defect `chi=(x_1 partial_2-x_2 partial_1)q` satisfies the same real-potential equation `Delta chi=kappa chi`. Within the retained finite-energy/decay class, `chi≡0` is equivalent to the axisymmetric no-swirl firewall. A conformal positive first-order core with `chi!=0` must expose non-axisymmetry at a finite higher angular jet; compactness gives a finite-order/jet-floor dichotomy on branches uniformly separated from the firewall.
- **M17-017** — with `psi=L phi`, the angular defect satisfies the exact coupled material-elliptic system `D_B chi=(kappa-partial_3U_3-1/2)chi-grad_h psi·grad_h q`, `partial_3 psi=(G_q-1)chi`, `Delta_h psi=-partial_3(G_q chi)`, together with `Delta chi=kappa chi`. On vertical non-scalar cores `G_q=1`, so the axial potential-defect source vanishes at the core. This is the first direct PDE coupling between the M17-013 hysteresis channel and non-axisymmetric shape.

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

### Rank one — first-order nodal shape channel
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

- `G_conf+^core`: positive-index conformal first-order core (`A=1`).
- `G_aniso+^core`: positive winding but `A>1`; cannot become axisymmetric while regular.
- `G_index-^core`: negative-index simple zero; cannot become the positive-index axisymmetric core while regular.

### Vertical non-axisymmetric compatibility
For the latter two classes on a vertical filament,

\[
\boxed{
G_q=1,
\qquad
\partial_3\lambda=0.
}
\]

Thus their reduced label flow must sustain the required hysteresis with the exact unit q-sensitivity

\[
K_q=1
\]

at the core.

### Higher-jet angular defect
Define

\[
\boxed{
\chi=\mathcal Lq,
\qquad
\mathcal L=x_1\partial_2-x_2\partial_1.
}
\]

Then

\[
\boxed{
\Delta\chi=\kappa\chi.
}
\]

Within the centered vertical finite-energy branch,

\[
\boxed{
\chi\equiv0
\iff
G_{axis/no\text{-}swirl}.
}
\]

Thus a conformal positive core splits further:

\[
\boxed{
G_{conf+}^{core}
\Longrightarrow
G_{axis/no\text{-}swirl}
\ \lor\ 
A_{high\text{-}jet}^{nonaxis}.
}
\]

On a compact branch uniformly separated from the firewall, `A_high-jet^nonaxis` has a uniformly finite angular-defect order and nonzero jet floor.

### Exact shape-hysteresis PDE coupling
With

\[
\psi=\mathcal L\phi,
\]

we now have

\[
\boxed{
\begin{aligned}
\Delta\chi
&=\kappa\chi,\\
D_B\chi
&=\left(\kappa-\partial_3U_3-\frac12\right)\chi
-\nabla_h\psi\cdot\nabla_hq,\\
\partial_3\psi
&=(G_q-1)\chi,\\
\Delta_h\psi
&=-\partial_3(G_q\chi).
\end{aligned}
}
\]

The scalar hysteresis and geometric non-axisymmetry channels are therefore no longer merely compared; they are coupled by an exact PDE system.

## DSD audit conclusion through M17-017

The rank-one branch has passed through three descriptor levels:

\[
\boxed{
\text{scalar }(\kappa,h,a)
\to
\text{first nodal shape }G_h
\to
\text{higher angular defect }(\chi,\psi).
}
\]

At each level a shortcut was removed:

- scalar hysteresis does not distinguish axisymmetry;
- conformal first-order shape does not prove axisymmetry;
- pointwise `chi=0` on the axis does not prove symmetry because the information lies in jets.

The exact firewall is now `chi≡0`, while the genuinely non-axisymmetric branch is a finite-order nonzero defect governed by the coupled system above.

## Current rank-one hard classes

After preserving the known regular firewall, the genuinely non-axisymmetric regular classes are

\[
\boxed{
G_{index-}^{core},
\qquad
G_{aniso+}^{core},
\qquad
A_{high\text{-}jet}^{nonaxis}.
}
\]

Each must satisfy simultaneously

\[
\boxed{
\langle\kappa_0\rangle=\frac32,
\qquad
Q_+\ge Q_*>0,
\qquad
Q_-\ge P+Q_*,
\qquad
\overline G_\Phi(0)<0,
}
\]

plus the angular-defect PDE system.

## Next target — Signed Angular-Defect Transfer Gate (SADTG)

The next calculation is to seek a signed integral or q-level-set identity for

\[
\nabla_h\psi\cdot\nabla_hq
\]

using

\[
\Delta_h\psi=-\partial_3(G_q\chi),
\qquad
\Delta q=F(q,x_3,\theta).
\]

The aim is to decide whether the nonzero angular defect is forced into the same negative-`kappa` payer required by M17-012, or whether a closed regular shape-hysteresis cycle remains possible.

A second independent branch remains open throughout: `R_2^{director-area}`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
