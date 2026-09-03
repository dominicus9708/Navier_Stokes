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
- **M17-006** — great-circle winding is a complex real-potential Schrödinger nodal-defect problem `Delta f = kappa f`; weighted phase energy is not topologically quantized near analytic zeros.
- **M17-007** — regular codimension-two winding zeros admit analytic extension of `kappa` and are material nodal filaments; winding topology is frozen unless a degenerate nodal event occurs.
- **M17-008** — axisymmetric Navier--Stokes without swirl is an exact known-regular model of the material great-circle/winding CE-H geometry; winding itself is a firewall, not a contradiction.
- **M17-009** — nodal creation/reconnection cannot evade through arbitrarily flat zeros; compactness plus analyticity gives a uniform finite nodal-jet order `m_*` and nonzero jet floor.
- **M17-010** — a regular winding core forces transverse strain isotropy `spec Sigma={lambda,lambda,-2lambda}`. Nodal Jacobian multiplier laws imply recurrent regular horizontal Jacobian has `⟨kappa⟩_nodal=3/2`; a persistent slanted derivative also forces `⟨lambda⟩=0`.
- **M17-011** — the regular nodal skeleton is enstrophy-measure-thin: `int_{D_r} kappa|W|^2=O(r^4)` per unit filament length. The correct zero-set descriptor is the first jet `G=grad W`, which obeys `Delta G=kappa_0 G` on the filament.
- **M17-012** — compact hard-hull bounds upgrade positive nodal mean to a positive-density set of strongly positive `kappa_0` phases; uniform regularity then creates a fixed finite-radius positive-`kappa` sheath and the global identity forces a fixed negative-`kappa` payer.
- **M17-013** — the semilinear great-circle system closes material dynamics in `(q,x_3)`: `q'=H`, `x_3'=K=G+x_3/2`, and `H_q+K_3=kappa`. The reduced label-area Jacobian equals the M5 amplification factor `a=exp int kappa`; M5-685 hysteresis is therefore label-area hysteresis.
- **M17-014** — `D_B G_h=(kappa-3/2)G_h` freezes the normalized nodal-Jacobian shape. Winding sign, singular-value ratio and anisotropy are material invariants, so negative-index or anisotropic positive-index cores cannot enter the axisymmetric firewall while regular.
- **M17-015** — on a vertical non-axisymmetric regular core, `(G_q-1)Q=lambda_3 I`; every non-scalar critical Hessian forces `G_q=1` and `partial_3 lambda=0`.
- **M17-016** — the angular defect `chi=(x_1 partial_2-x_2 partial_1)q` obeys `Delta chi=kappa chi`. Under the retained finite-energy/decay class, `chi identically 0` is the axisymmetric no-swirl firewall; a non-axisymmetric conformal core must expose a finite higher angular jet.
- **M17-017** — with `psi=L phi`, the exact shape-hysteresis system is `D_B chi=(kappa-partial_3U_3-1/2)chi-grad_h psi dot grad_h q`, `partial_3 psi=(G_q-1)chi`, `Delta_h psi=-partial_3(G_q chi)`, together with `Delta chi=kappa chi`.
- **M17-018** — the Signed Angular-Defect Transfer Gate closes at energy level: `int kappa chi^2=-int|grad chi|^2<0` for every nonzero finite-energy defect, including separately on each `chi` nodal domain. Also `int|grad_h psi|^2=int G_q(1-G_q)chi^2`, so nonzero defect cannot keep `G_q` identically at the vertical-core value one.
- **M17-019** — the first nonzero transverse angular-defect jet is harmonic: `P_m=r^m(A cos mtheta+B sin mtheta)`, producing `2m` alternating local sectors. Every global defect lobe emerging from a positive-`kappa` core sector must contain `kappa<0` and therefore a same-lobe `kappa=0` crossing.
- **M17-020** — on a regular `chi=0` boundary, the material-relative normal velocity is `T/|grad chi|`, `T=grad_h psi dot grad_h q`. A bounded recurrent signed lobe satisfies `V_s'=3V_s/2-s int_boundary T/|grad chi|`; hence strict signed material turnover is mandatory.
- **M17-021** — at `chi=kappa=0`, the common intersection velocity solves `grad chi dot w=T`, `grad kappa dot w=-h`. Transverse intersections are algebraically compatible for arbitrary finite currents. At tangency `grad kappa=lambda grad chi`, smooth persistence requires the exact law `h=-lambda T`; otherwise the double-zero network must separate/reconnect or lose rank.
- **M17-022** — every bounded angular-defect lobe has a spectral negative payer: `⟨kappa⟩_{chi^2,Omega}<=-lambda_1(Omega)<=-C_FK|Omega|^{-2/3}`. On a compact branch separated from the firewall, the angular-jet floor yields a fixed absolute negative defect-payer gap.
- **M17-023** — at a simple semilinear root `F_qq!=0`, horizontal `kappa=0` components are `q`-level contours. Since `chi=Lq=x_h dot W_h=r W_r`, double zeros are radial extrema of those contours; transversality is a nondegenerate radial extremum and double-zero tangency is a degenerate radial-extremum event. At the root, `h=F_qq V_q` is the material crossing of the `q` label through the root contour.
- **M17-024** — for a nonhorizontal regular filament, the slope `p=tau_h/tau_3=-G_h^{-1}G_3=-Q^{-1}grad_hq_3` obeys `D_B p=3lambda p`. Its horizontal azimuth is material invariant, while recurrent bounded nonzero slant independently forces `⟨lambda⟩=0`.
- **M17-025** — the tangent-covariant slanted-core law is `(p dot grad_h)H_phi+(G_q-1)Q=(D_s lambda)I`. Its trace-free part forces `TF[(p dot grad_h)H_phi]=-(G_q-1)Q_TF`; a nonconformal slanted core survives only on an exact tensor-alignment submanifold. The vertical `G_q=1` law is the `p=0` limit.
- **M17-026** — rank two has a canonical divergence-free director-area current `J_xi=* xi^*(omega_{S^2})`, with `(J_xi dot grad)xi=0` and `j_xi=J_xi dot xi`. It is frozen-in: `D_B J_xi=(grad B)J_xi-3J_xi/2`. After removing scalar amplification, `W_tilde=W/a` obeys exactly the same Cauchy law, so `J_xi` and `W_tilde` are a co-frozen flux pair. Rank two splits materially into `J_xi parallel W` and oblique branches.
- **M17-027** — `Delta rho=(kappa+|grad xi|^2)rho` and `|grad xi|^2>=2|J_xi|` on rank two. Therefore a positive vorticity-amplitude maximum in a rank-two region satisfies `kappa<=-|grad xi|^2<=-2|J_xi|<0`. Globally, director area contributes a coercive negative-`kappa` cost.
- **M17-028** — with `c=a j_xi/rho`, `D_Bc=0`; the transverse obliquity vector `K_xi=J_xi-cW_tilde` is itself co-frozen and orthogonal to `xi`. A recurrent bounded obliquity ratio forces `⟨sigma_K⟩=⟨sigma⟩`; if `j_xi` also recurs bounded away from zero then `⟨sigma⟩=⟨sigma_K⟩=1` and the third quadratic strain has mean `-2`. If raw amplitude also recurs, `⟨kappa⟩=0`.
- **M17-029** — the parallel rank-two branch has `(xi dot grad)xi=0`, so active vortex-direction integral curves are straight lines. The transverse director gradient obeys the exact linewise Riccati law `A'=-A^2`, giving `A(s)=A_0(I+sA_0)^{-1}`, `Delta_perp=det(I+sA_0)`, and `rho,j_xi proportional Delta_perp^{-1}`. A complete smooth rank-two line requires `det A_0>0` and `(tr A_0)^2<4det A_0`, i.e. a twist-dominated skew-line congruence with no real focal root.

## Current frontier

The director branch is still

\[
\boxed{
B_{dir}
\Longrightarrow
R_2^{director-area}
\ \lor\ 
R_1^{great-circle/winding}.
}
\]

Neither main branch is yet closed.

---

## Rank one — current state

### Scalar label/hysteresis channel

\[
\boxed{
q'=H,
\qquad
x_3'=K,
\qquad
\partial_qH+\partial_3K=\kappa,
\qquad
J_L'=\kappa J_L.
}
\]

Thus the M5 material flux amplification is the Jacobian of the reduced `(q,x_3)` label flow.

### Regular nodal shape channel

\[
\boxed{
D_BG_h=(\kappa-3/2)G_h.
}
\]

Therefore normalized nodal shape and winding index are frozen. Slanted slope additionally obeys

\[
\boxed{
D_Bp=3\lambda p,
\qquad
D_B\widehat p=0.
}
\]

A nonconformal slanted core must satisfy the persistent tensor-alignment condition

\[
\boxed{
TF[(p\cdot\nabla_h)H_\phi]
=-(G_q-1)Q_{TF}.
}
\]

### Angular-defect payer network

\[
\boxed{
\Delta\chi=\kappa\chi,
\qquad
\int_\Omega\kappa\chi^2
=-\int_\Omega|\nabla\chi|^2<0
}
\]

for every nontrivial defect lobe `Omega`.
At positive recurrent winding-core phases, every core-emergent lobe therefore contains

\[
\boxed{
\kappa>0
\to
\kappa=0
\to
\kappa<0
}
\]

inside the same connected defect channel.

For a bounded recurrent lobe,

\[
\boxed{
\left\langle
s\int_{\partial\Omega_s}
\frac{\nabla_h\psi\cdot\nabla_hq}{|\nabla\chi|}
\,dA
\right\rangle
=
\frac32\langle|\Omega_s|\rangle>0.
}
\]

Thus both a negative interior payer and signed boundary material turnover are mandatory.

### Double-zero geometry

At a transverse `chi=kappa=0` intersection, the two turnover currents coexist with a regular common intersection velocity.
Only tangency introduces the extra compatibility

\[
\boxed{
h=-\lambda T,
\qquad
T=\nabla_h\psi\cdot\nabla_hq.
}
\]

At a simple root, the double zeros are radial extrema of the internal `kappa=0` `q` contour; tangency is a degenerate radial-extremum event.

### Current rank-one hard exits

The remaining regular non-axisymmetric branch can persist only through a combination of

\[
\boxed{
\begin{array}{l}
\text{lobe-resolved negative-kappa payer},\\
\text{strict angular-boundary turnover},\\
\text{M5-685 flux-weighted kappa hysteresis},\\
\text{uniform double-zero transversality or compatible tangency},\\
\text{frozen nodal shape/slant orientation},\\
\text{exact slanted tensor alignment when nonvertical}.
\end{array}
}
\]

Otherwise it exits through rank loss, finite-jet reconnection/degeneration, unbounded tails, or the axisymmetric no-swirl firewall.

---

## Rank two — current state

Define the director-area current

\[
\boxed{
(J_\xi)^k
=\frac12\varepsilon^{kij}
\xi\cdot(\partial_i\xi\times\partial_j\xi).
}
\]

Then

\[
\boxed{
\nabla\cdot J_\xi=0,
\qquad
(J_\xi\cdot\nabla)\xi=0,
}
\]

and, with `D_Ba=\kappa a`,

\[
\boxed{
D_BJ_\xi=(\nabla B)J_\xi-\frac32J_\xi,
\qquad
D_B(W/a)=(\nabla B)(W/a)-\frac32(W/a).
}
\]

Thus `J_xi` and rescaled vorticity are co-frozen by the same deformation map.

### Rank-two payer

\[
\boxed{
\Delta\rho=(\kappa+|\nabla\xi|^2)\rho,
\qquad
|\nabla\xi|^2\ge2|J_\xi|.
}
\]

Rank-two amplitude ridges are therefore strictly negative-`kappa` structures, and rank-two area contributes coercively to the global negative multiplier budget.

### Parallel/oblique split

Let

\[
\boxed{
c=\frac{a j_\xi}{\rho},
\qquad
K_\xi=J_\xi-c(W/a).
}
\]

Then

\[
D_Bc=0,
\qquad
K_\xi\cdot\xi=0,
\qquad
D_BK_\xi=(\nabla B)K_\xi-\frac32K_\xi.
\]

Hence

\[
\boxed{
R_2^{separated}
\Longrightarrow
R_2^{parallel}
\ \lor\ 
R_2^{oblique}.
}
\]

- **Parallel:** `K_xi=0`. Vortex lines are straight. On a complete rank-two line, the transverse director gradient satisfies a Riccati focusing law and global smoothness requires a twist-dominated no-real-focus condition.
- **Oblique:** `K_xi!=0`. Bounded recurrent obliquity requires mean strain matching `⟨sigma_K⟩=⟨sigma⟩`; recurrent nonzero director-area density further gives the mean quadratic strain pattern `(1,1,-2)`.
- **Rank-loss approach:** `|J_xi| -> 0` returns the geometry toward the rank-one frontier already audited above.

---

## DSD audit conclusion through M17-029

Several tempting shortcuts have been removed:

1. positive nodal `kappa` does not directly contradict the negative global weighted mean;
2. nonzero winding is not singular because axisymmetric no-swirl is a regular firewall;
3. two directed zero-set currents are compatible when their zero surfaces remain transverse;
4. fixed radial-extremum count is not itself contradictory;
5. tensor codimension/alignment is not a contradiction unless dynamics fails to preserve it;
6. two co-frozen rank-two fluxes can coexist smoothly;
7. straight rank-two vortex lines can avoid focusing through twist-dominated skew-line geometry.

The gain is that every surviving branch now carries explicit quantitative obligations rather than qualitative freedom.

---

## Highest-value next calculations

### Rank one
**SAIG / persistent-alignment audit:** materially differentiate the slanted alignment defect

\[
\mathcal M_p
:=TF[(p\cdot\nabla_h)H_\phi]^{\perp Q_{TF}}
\]

and determine whether `\mathcal M_p=0` is dynamically invariant or forces another finite higher-jet condition.

In parallel, the double-zero/lobe network can be audited for whether a uniformly transverse compact recurrent cycle truly exists or inevitably reaches a finite-jet tangency/reconnection event.

### Rank two
**SLWHG / R2POCG:** substitute the exact straight-line Riccati profile of `R_2^{parallel}` into the weighted harmonic-director equation; separately test whether the recurrent oblique mean strain frame `(1,1,-2)` can remain compact without rank loss or flux turnover.

The overall proof cannot be completed until both rank-one and rank-two branches are either reduced to known regular classes or excluded.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
