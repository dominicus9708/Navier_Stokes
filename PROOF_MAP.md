# Proof / verification map

This file is the current route map for the DSD-assisted 3D incompressible Navier–Stokes proof challenge.

It separates exact identities, derived bridge lemmas, external regularity anchors, computational checks, failed routes, and open proof obligations. Older exploratory states remain recoverable from Git history; this file records the **current** interpretation.

## Status vocabulary

- **NAVIER–STOKES INPUT** — part of the original PDE/problem setting.
- **DSD BRIDGE DEFINITION** — application-specific typed representation; not a new PDE theorem.
- **DERIVED IDENTITY** — exact algebra/calculus from stated hypotheses.
- **DERIVED LEMMA** — proof-level internal lemma under the stated function class.
- **COMPUTATIONAL CHECK** — symbolic/numerical benchmark only.
- **EXTERNAL REGULARITY ANCHOR** — published theorem used as a target or implication.
- **CONDITIONAL NECESSARY CONDITION** — follows if the bridge to an external criterion is invoked; not itself a contradiction.
- **FAILED-ROUTE CANDIDATE** — computationally contradicted but not fully analytically excluded.
- **FAILED ROUTE** — algebraically/analytically excluded as the proposed mechanism.
- **OPEN PROOF OBLIGATION** — required before any global-smoothness claim.
- **NOT CLAIMED** — explicitly outside current proof status.

---

# A. Original problem and invariant baseline

| Item | Support | Status |
|---|---|---|
| `R^3` incompressible Navier–Stokes, `nu>0`, `f=0` | repository baseline | NAVIER–STOKES INPUT |
| No physical container; spheres are observation/aggregation regions | baseline note | DSD BRIDGE DEFINITION |
| Gaussian double-curl seeds are smooth, rapidly decaying, divergence-free | exact SymPy | COMPUTATIONAL CHECK / exact symbolic |
| `x/y/z` seed rotations are equivalent | coordinate permutation | DERIVED IDENTITY |
| Radial readout at `r=0` is inapplicable rather than defined zero | spherical-coordinate definition + DSD typing | DSD BRIDGE DEFINITION |
| Pressure Poisson source `-Delta p = partial_i partial_j(u_i u_j)` | incompressibility | NAVIER–STOKES IDENTITY |
| Whole kinetic-energy inequality controls `||u(t)||_2` for finite-energy weak solutions | standard Leray energy inequality | EXTERNAL/STANDARD INPUT |

---

# B. Primary proof track: moving weighted mean sphere

The current primary local object is **not** a material cell and not a hard physical sphere. It is a smooth radial cutoff whose center follows the cutoff-weighted mean velocity.

For fixed `ell>0`,

\[
\phi_\ell(x)=\phi(x/\ell),
\qquad
\dot X_\ell(t)
=
\frac{\int\phi_\ell(x-X_\ell(t))u(x,t)dx}
{\int\phi_\ell dx}.
\]

Define

\[
\bar U_\ell(t)=\dot X_\ell(t),
\qquad
v=u-\bar U_\ell.
\]

Then

\[
\int\phi_\ell(x-X_\ell(t))v(x,t)dx=0.
\]

| Item | Support | Status |
|---|---|---|
| Weighted mean field is bounded/Lipschitz in center `X` at every fixed `ell` for global finite-energy `u` | Cauchy–Schwarz + smooth convolution | DERIVED LEMMA |
| Center ODE has a unique absolutely continuous solution | Carathéodory ODE theorem under preceding bounds | DERIVED LEMMA |
| Moving cutoff satisfies `partial_t phi = -Ubar·grad phi` a.e. | chain rule for AC path | DERIVED IDENTITY |
| Weighted internal velocity has zero mean | center definition | DERIVED IDENTITY |
| Moving weighted-variance local-energy inequality | local energy inequality + weak momentum + variance subtraction | DERIVED LEMMA |
| No `X''` or accelerating-frame pressure is required in the rigorous route | Eulerian moving-cutoff derivation | DERIVED LEMMA / ROUTE SIMPLIFICATION |
| Hard mean-flow sphere gives the same conceptual mean-removal but is retained mainly for diagnostics | exact mean subtraction + numerical budget | DSD BRIDGE / COMPUTATIONAL TRACK |

## B1. Derived weighted-variance inequality

For whole-space finite-energy suitable weak solutions, for a.e. Lebesgue times `s<t`,

\[
\boxed{
\begin{aligned}
&\frac12\int\varphi(t)|v(t)|^2dx
+\nu\int_s^t\int\varphi|\nabla u|^2dxdt'\\
&\le
\frac12\int\varphi(s)|v(s)|^2dx\\
&\quad+
\int_s^t\int\frac{|v|^2}{2}v\cdot\nabla\varphi\,dxdt'\\
&\quad+
\int_s^t\int p\,v\cdot\nabla\varphi\,dxdt'\\
&\quad+
\frac\nu2\int_s^t\int|v|^2\Delta\varphi\,dxdt'.
\end{aligned}
}
\]

Internal proof: `notes/2026-08-12-weighted-variance-lemma-completion.md`.

## B2. Scale-critical typed channels

Define schematically

\[
C_\phi=\ell^{-1}\int\varphi|v|^2,
\]

\[
D_\phi=\nu\ell\int\varphi|\nabla u|^2,
\]

\[
A_\phi=\ell\int\frac{|v|^2}{2}v\cdot\nabla\varphi,
\]

\[
P_\phi=\ell\int p\,v\cdot\nabla\varphi,
\]

\[
B_\phi=\frac{\nu\ell}{2}\int|v|^2\Delta\varphi.
\]

All are compatible with Navier–Stokes parabolic scaling.

DSD typing:

- `q_osc` — internal velocity oscillation `C_phi`;
- `q_diss` — viscous local dissipation `D_phi`;
- `q_adv` — relative nonlinear transport `A_phi`;
- `q_pres` — pressure redistribution `P_phi`;
- `q_cut` — cutoff/viscous boundary-layer term `B_phi`.

These channels must remain separate; their signed cancellations are part of the dynamics.

---

# C. Bridge to established epsilon regularity

## C1. Mean-zero interpolation

For a rigid or weighted mean-zero local velocity, Poincaré–Sobolev and interpolation yield the critical family, for

\[
\frac52<p\le3,
\]

\[
\boxed{
A_p
\lesssim
(\sup C_{\rm sph})^{\alpha(p)}
(\mathfrak E_{\rm sph})^{\beta(p)},
}
\]

with

\[
\alpha(p)=\frac{6-p}{4},
\qquad
\beta(p)=\frac{3(p-2)}{4}.
\]

Representative exponents:

\[
p=3:\quad(\alpha,\beta)=\left(\frac34,\frac34\right),
\]

\[
p=\frac{11}{4}:\quad
(\alpha,\beta)=\left(\frac{13}{16},\frac{9}{16}\right),
\]

and as `p downarrow 5/2`,

\[
(\alpha,\beta)\to\left(\frac78,\frac38\right).
\]

| Item | Support | Status |
|---|---|---|
| Critical exponent interpolation family | Poincaré–Sobolev + Hölder | DERIVED IDENTITY / BRIDGE |
| Pressure-free one-scale criterion for every exponent `5/2+delta`, `delta>0` | Wang–Wu–Zhou, arXiv:1811.09927 | EXTERNAL REGULARITY ANCHOR |
| Classical one-scale `L^3` velocity + `L^{3/2}` pressure smallness criterion | standard epsilon-regularity literature | EXTERNAL REGULARITY ANCHOR |
| `L^infty_t L^3_x` boundedness excludes finite-time singularity | Escauriaza–Seregin–Šverák | EXTERNAL REGULARITY ANCHOR |

## C2. Current target

The preferred final gate is pressure-free:

\[
\boxed{
\ell^{p-5}
\iint_{Q_\ell}|v|^p
<\varepsilon_p,
\qquad
p>\frac52.
}
\]

The pressure channel remains essential for **evolving** `C_phi`, but it does not have to appear in the final epsilon-smallness criterion.

## C3. Conditional singularity certificate

Once the weighted moving-window quantity is transferred to the fixed-cylinder hypothesis of the published theorem, a candidate singularity must prevent the DSD channel product from becoming small at arbitrarily fine scales:

\[
(\sup C_\phi)^{\alpha(p)}
(\mathfrak E_\phi)^{\beta(p)}
\gtrsim c\,\varepsilon_p.
\]

Status: **CONDITIONAL NECESSARY CONDITION**, not a contradiction.

The central unsolved task is to prove that DSD-resolved dynamics makes such persistent critical concentration impossible.

---

# D. Current dynamical obstruction inside the moving sphere

For the hard mean-flow sphere, the exact smooth instantaneous critical oscillation budget is

\[
\boxed{
\frac{\ell^2}{2}\frac{d}{dt}C_{\rm sph}
=-A_{\rm adv}-P_{\rm pressure}+V_{\rm viscous}.
}
\]

The weighted version is the corresponding smooth-cutoff inequality in Section B.

| Item | Support | Status |
|---|---|---|
| Mean subtraction eliminates coherent translation | exact mean identity | DERIVED IDENTITY |
| Uniform frame acceleration is absent from Eulerian weighted-variance lemma | moving-cutoff + momentum derivation | DERIVED LEMMA |
| Relative advection generally remains nonzero | asymmetric two-seed audit | COMPUTATIONAL CHECK |
| Pressure redistribution generally remains nonzero | asymmetric two-seed audit | COMPUTATIONAL CHECK |
| Mean-flow sphere budget is stable from `64^3` to `80^3` under the committed convergence test | deterministic FFT/mask audit | COMPUTATIONAL CHECK |
| Viscosity dominates the current asymmetric benchmark at `t=0` near `ell=1` | numerical benchmark only | COMPUTATIONAL CHECK |
| Universal sign/monotonicity of the moving oscillation channel | none | NOT CLAIMED |

### Main dynamical proof obligation

Derive a non-circular estimate that prevents

\[
A_\phi+P_\phi+B_\phi
\]

from sustaining the critical concentration required to keep the pressure-free epsilon criterion above threshold on every sufficiently small scale.

Status: **OPEN PROOF OBLIGATION**.

---

# E. Pressure localization as a secondary dynamics tool

Pressure is nonlocal, but differential/localized channels gain far-field kernel decay.

| Item | Support | Status |
|---|---|---|
| Pressure kernel degree `-3`, gradient degree `-4`, next derivative degree `-5` | Newtonian/Riesz kernel homogeneity | DERIVED IDENTITY |
| Difference of pressure gradients at nearby points gains one far-field decay power | mean-value theorem | DERIVED BRIDGE |
| Under critical local `L^2`-Morrey control, far differential pressure has scale-critical dyadic bound | shell summation | DERIVED BRIDGE |
| Near pressure remains coupled to local nonlinear/strain structure | no closed arbitrary-data bound | OPEN PROOF OBLIGATION |

Because the preferred final epsilon criterion is pressure-free, this pressure decomposition is now used mainly to understand/control the **evolution** of the oscillation channel rather than the final regularity threshold.

---

# F. Material-cell / Lagrangian track: secondary structural diagnostics

The deforming material cell remains useful for following the same fluid particles and for DSD structural lineage:

\[
\Omega_\ell^{\rm mat}(t)=\Phi_t(B_\ell(a)).
\]

Exact identities:

\[
\dot F=(\nabla u)F,
\qquad
J=\det F=1,
\]

\[
\dot C=2F^TSF,
\]

\[
n_t\,dS_t=F^{-T}n_0\,dS_0.
\]

Material coordinates use

\[
A=F^{-1}F^{-T},
\]

and

\[
\partial_tU
=-F^{-T}\nabla_aP
+\nu\operatorname{div}_a(A\nabla_aU).
\]

### Critical correction

The metric `A` is a coordinate representation, not a new physical viscosity mechanism. Since

\[
\nabla_aU=(\nabla_xu)F,
\]

\[
\boxed{
(\nabla_aU)A(\nabla_aU)^T
=(\nabla_xu)(\nabla_xu)^T.
}
\]

Likewise, explicit `F^{-T}` amplification in a pulled-back boundary integral is not an independent pressure-energy source; equivalent volume forms remove that explicit factor.

| Item | Current status |
|---|---|
| Material flow-map/Jacobian/shape identities | DERIVED IDENTITIES |
| Material-cell relative advection vanishes at a true material boundary | DERIVED IDENTITY |
| `F^{-T}` as geometry diagnostic | RETAINED DIAGNOSTIC |
| `F^{-T}` as independent pressure-amplification source | FAILED ROUTE |
| `det A=1` or `tr A>=3` as new viscous coercivity | FAILED ROUTE |
| Large/small eigenvalue of `A` alone as physical enhanced/weak viscosity | FAILED ROUTE |
| Lagrangian coordinates for removing explicit advection/fixing reference domain | RETAINED SECONDARY TRACK |

---

# G. Strain, vorticity, and off-diagonal interaction diagnostics

These remain possible mechanisms for estimating the moving-sphere redistribution channels.

| Item | Support | Status |
|---|---|---|
| `tr S=0` | incompressibility | DERIVED IDENTITY |
| Vortex stretching `omega^T S omega` is locally sign-indefinite | exact benchmark + standard identity | DERIVED/CHECK |
| Signed global stretching can cancel while positive/negative parts are nonzero | exact Gaussian integration | COMPUTATIONAL CHECK / exact integral |
| Two-seed cross stretching is not sum of self terms | exact expansion | DERIVED IDENTITY |
| Cross stretching can reverse sign relative to self-term expectation | exact benchmark witness | COMPUTATIONAL CHECK / exact symbolic |
| Vorticity-direction factorization `sigma=|omega|^2 xi^T S xi` | spectral identity | DERIVED IDENTITY |
| `xi` is undefined where `|omega|=0` even if a quotient has removable extension | DSD typing | DSD BRIDGE DEFINITION |
| `-det S <= (1/2) lambda_2^+ |S|^2` | trace-free eigenvalue algebra | DERIVED IDENTITY |
| Middle-eigenvalue regularity criteria | Miller (2020) and related work | EXTERNAL REGULARITY ANCHOR |
| Vorticity-direction coherence criteria | Constantin–Fefferman line | EXTERNAL REGULARITY ANCHOR |
| Arbitrary-data bound forcing favorable alignment | none | OPEN PROOF OBLIGATION |

---

# H. Routes pruned or demoted

| Proposed route | Current status | Reason |
|---|---|---|
| Global `L^3` is universally monotone decreasing | FAILED-ROUTE CANDIDATE | stable asymmetric positive pressure-correlation benchmark |
| `Pi_3` can be controlled by `T_3` alone | FAILED ROUTE as instantaneous scale-compatible closure | `T_3` is scale invariant while `Pi_3` scales like `lambda^2` |
| One-way outward pressure/advection flux on every sphere | FAILED-ROUTE CANDIDATE | asymmetric sphere flux changes sign with radius |
| Fixed-origin sphere alone is translation complete | FAILED ROUTE | translated benchmark |
| Point-centered `sup_ell C_rel` is a good all-scale internal-difference norm | REPAIRED ROUTE | large cells count center-vs-far-field drift; mean centering fixes this |
| `lambda_2^+` alone controls material boundary geometry | FAILED ROUTE for that geometric claim | trace-free model `diag(-M,0,M)` has `lambda_2^+=0` while `||F^{-T}||` grows |
| `F^{-T}` is an independent energy-amplification source | FAILED ROUTE | surface/volume representation equivalence |
| Lagrangian `A` eigenvalues generate new enhanced viscosity | FAILED ROUTE | exact metric-gradient coordinate cancellation |
| Accelerating-frame pressure correction is required for the main rigorous bridge | DEMOTED | Eulerian moving-cutoff variance lemma avoids `X''` entirely |

---

# I. Current open proof obligations, in priority order

1. **Weighted moving-sphere dynamics:** obtain a non-circular estimate on `A_phi`, `P_phi`, and `B_phi` in terms of channels that prevent sustained critical concentration.
2. **Pressure-free epsilon threshold:** prove that for every candidate singular point there is a sufficiently small scale on which the moving weighted internal velocity satisfies one published pressure-free one-scale criterion.
3. **Fixed-cylinder transfer:** state carefully how the moving weighted window produces or is covered by the fixed parabolic cylinder required by the selected external theorem; use the Eulerian moving-cutoff lemma rather than an unjustified accelerating-frame assumption.
4. **Multiscale compatibility:** show that dangerous oscillation cannot simply move from one scale/center to another while avoiding the estimate.
5. **Strain/vorticity/off-diagonal mechanism:** determine whether these typed DSD channels force decay of the nonlinear/pressure redistribution terms or otherwise block persistent concentration.
6. **Arbitrary admissible data:** every final estimate must depend only on allowed initial-data quantities and `nu`, not on a benchmark symmetry or a posteriori smoothness.
7. **Global conclusion:** after all preceding bridges are rigorous, combine them with an established epsilon-regularity theorem to rule out every finite-time singularity.

Global smoothness is **not currently proved**.

---

# J. Benchmark / reproducibility policy

The repository intentionally contains exact symbolic checks, deterministic numerical audits, and failed-route witnesses. They are used to test bridge definitions and eliminate false shortcuts.

A benchmark result is never promoted to an arbitrary-data theorem without an analytic proof.

The GitHub Actions reproducibility workflow is the executable audit layer. `results/` records representative deterministic outputs; `notes/` records derivations and claim boundaries.
