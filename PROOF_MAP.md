# Proof / verification map

This file records the **current** route of the DSD-assisted 3D incompressible Navier–Stokes proof challenge. Older exploratory states remain recoverable from Git history.

## Status vocabulary

- **NAVIER–STOKES INPUT** — original PDE/problem setting.
- **DSD BRIDGE DEFINITION** — application-specific typed representation.
- **DERIVED IDENTITY** — exact algebra/calculus under stated hypotheses.
- **DERIVED LEMMA** — proof-level internal lemma under the stated function class.
- **COMPUTATIONAL CHECK** — symbolic/numerical benchmark only.
- **EXTERNAL REGULARITY ANCHOR** — published theorem used as an implication/target.
- **CONDITIONAL NECESSARY CONDITION** — follows conditionally from a regularity gate; not a contradiction.
- **FAILED-ROUTE CANDIDATE** — computationally contradicted but not analytically excluded.
- **FAILED ROUTE** — algebraically/analytically excluded as the proposed mechanism.
- **OPEN PROOF OBLIGATION** — required before global smoothness.
- **NOT CLAIMED** — explicitly not established.

---

# A. Original problem and baseline

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
x\in\mathbb R^3,
\quad \nu>0,
\quad f=0.
\]

| Item | Support | Status |
|---|---|---|
| Whole-space `R^3` problem; no physical container | baseline | NAVIER–STOKES INPUT |
| Observation spheres/cutoffs are not physical boundaries | baseline | DSD BRIDGE DEFINITION |
| Gaussian double-curl benchmark is smooth, rapidly decaying, divergence-free | exact symbolic audit | COMPUTATIONAL CHECK |
| `x/y/z` rotated benchmarks agree up to rotation | coordinate symmetry | DERIVED IDENTITY |
| Radial channel at `r=0` is undefined/inapplicable, not defined zero | coordinate definition + DSD typing | DSD BRIDGE DEFINITION |
| Global finite-energy weak track has `L^2` energy control | Leray/suitable theory | EXTERNAL/STANDARD INPUT |

---

# B. Primary proof object: weighted mean-flow moving sphere

Choose a nonnegative smooth compactly supported radial cutoff

\[
\phi_\ell(x)=\phi(x/\ell).
\]

Let

\[
\mathcal U_\ell(X,t)
=
\frac{\int\phi_\ell(x-X)u(x,t)dx}
{\int\phi_\ell dx}
\]

and solve

\[
\boxed{
\dot X_\ell(t)=\mathcal U_\ell(X_\ell(t),t).
}
\]

Define

\[
\bar U_\ell=\dot X_\ell,
\qquad
v=u-\bar U_\ell,
\qquad
\varphi(x,t)=\phi_\ell(x-X_\ell(t)).
\]

Then

\[
\boxed{
\int\varphi vdx=0.
}
\]

| Item | Support | Status |
|---|---|---|
| Weighted mean field is bounded and Lipschitz in `X` for fixed `ell` | global energy + smooth convolution | DERIVED LEMMA |
| Center ODE has unique AC solution forward or backward on finite intervals | Caratheodory ODE | DERIVED LEMMA |
| Moving cutoff obeys `partial_t varphi=-Ubar·grad varphi` a.e. | AC chain rule | DERIVED IDENTITY |
| Mean-zero internal velocity | center definition | DERIVED IDENTITY |
| Smooth hard-sphere analogue and asymmetric flux audits | deterministic computations | COMPUTATIONAL TRACK |

---

# C. Moving weighted-variance local-energy lemma

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

Proof: `notes/2026-08-12-weighted-variance-lemma-completion.md`.

The proof uses the ordinary suitable local-energy inequality, the weak momentum equation with the same moving cutoff, and the variance identity

\[
\frac12\int\varphi|v|^2
=
\frac12\int\varphi|u|^2
-
\frac{M_\ell}{2}|\bar U|^2.
\]

No `X''` is needed for this local-energy lemma.

Status: **DERIVED LEMMA**.

## Critical typed channels

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

All have the correct critical scaling.  DSD typing keeps oscillation, dissipation, relative advection, pressure redistribution, and cutoff diffusion separate.

---

# D. Generalized Galilean suitable-solution lemma

The weighted mean momentum identity gives

\[
\bar U_\ell'\in L^{3/2}_{loc}(dt),
\qquad
X_\ell\in W^{2,3/2}_{loc}(dt).
\]

For any

\[
X\in W^{2,3/2}_{loc},
\]

define

\[
y=x-X(t),
\]

\[
v(y,t)=u(y+X(t),t)-\dot X(t),
\]

\[
q(y,t)=p(y+X(t),t)+\ddot X(t)\cdot y.
\]

Then on bounded translated cylinders `(v,q)` is again a suitable weak solution.

Key facts:

1. the distributional momentum equation transforms exactly;
2. `X''·y` lies in local `L^{3/2}` because `X'' in L^{3/2}_t`;
3. the local energy defect transforms by

\[
\mathcal D[v,q]
=
\mathcal D[u,p]\circ(y+X)
-
\dot X\cdot\mathcal R[v,q],
\]

and `mathcal R[v,q]=0` distributionally.

Proof: `notes/2026-08-12-generalized-galilean-suitable-lemma.md`.

Status: **DERIVED LEMMA**.

## Consequence: fixed-cylinder transfer is closed

Given a candidate endpoint `(x_*,T)` and scale `ell`, solve the weighted center ODE **backward** with

\[
X_\ell(T)=x_*.
\]

The candidate point becomes `(0,T)` in the translated `y` coordinates, where `v` is suitable on an ordinary fixed parabolic cylinder.

Therefore the former requirement to geometrically cover a moving sphere by a fixed cylinder is no longer open.

---

# E. External pressure-free epsilon-regularity gate

Wang–Wu–Zhou prove a one-scale pressure-free criterion for suitable weak solutions: for every

\[
\delta>0,
\]

sufficiently small

\[
\iint_{Q(1)}|v|^{5/2+\delta}dxdt
\]

implies regularity in a smaller cylinder.

Status: **EXTERNAL REGULARITY ANCHOR**.

The proof track therefore uses a fixed exponent

\[
p=\frac52+\delta>\frac52.
\]

For `5/2<p<=3`, mean-zero interpolation gives

\[
\boxed{
A_p
\lesssim
(\sup C_\phi)^{\alpha(p)}
(\mathfrak E_\phi)^{\beta(p)},
}
\]

with

\[
\alpha(p)=\frac{6-p}{4},
\qquad
\beta(p)=\frac{3(p-2)}{4}.
\]

Examples:

\[
p=3:
\quad
(\alpha,\beta)=\left(\frac34,\frac34\right),
\]

\[
p=\frac{11}{4}:
\quad
(\alpha,\beta)=\left(\frac{13}{16},\frac{9}{16}\right),
\]

and

\[
p\downarrow\frac52:
\quad
(\alpha,\beta)\to\left(\frac78,\frac38\right).
\]

The epsilon threshold depends on `p`; there is no assumed uniform optimization in `p`.

---

# F. Current singularity concentration certificate

If `(x_*,T)` were singular, then for the backward weighted-mean path ending at `x_*`, the pressure-free epsilon criterion cannot be satisfied on every sufficiently small scale.

Consequently, for the selected exponent `p`, arbitrarily small critical scales must retain a non-small internal channel product of the schematic form

\[
\boxed{
(\sup C_\phi)^{\alpha(p)}
(\mathfrak E_\phi)^{\beta(p)}
\gtrsim c\varepsilon_p.
}
\]

Status: **CONDITIONAL NECESSARY CONDITION FOR A SINGULARITY**.

This is not yet a contradiction.

The Millennium-level problem has now been reduced, in this route, to showing that such persistent critical concentration is impossible for arbitrary admissible smooth initial data.

---

# G. Dynamics of the internal oscillation channel

For a hard mean-flow sphere, the smooth critical variance budget is

\[
\frac{\ell^2}{2}\frac{d}{dt}C_{\rm sph}
=-A_{\rm adv}-P_{\rm pressure}+V_{\rm viscous}.
\]

The weighted theorem-level version is Section C.

| Item | Support | Status |
|---|---|---|
| Mean subtraction removes coherent translation | exact | DERIVED IDENTITY |
| Relative advection generally remains | asymmetric audit | COMPUTATIONAL CHECK |
| Pressure redistribution generally remains | asymmetric audit | COMPUTATIONAL CHECK |
| `64^3 -> 80^3` moving-sphere budget convergence check passes | CI numerical audit | COMPUTATIONAL CHECK |
| Viscosity dominates the current asymmetric benchmark at `t=0` near `ell=1` | benchmark only | COMPUTATIONAL CHECK |
| Universal monotonic decay of local oscillation | none | NOT CLAIMED |

### Primary unresolved inequality

Control

\[
A_\phi+P_\phi+B_\phi
\]

well enough that the critical concentration certificate in Section F cannot persist down to arbitrarily small scales.

Status: **OPEN PROOF OBLIGATION**.

---

# H. Pressure localization: secondary dynamics tool

The pressure kernel is nonlocal, but spatial differences improve far-field decay:

- pressure kernel: degree `-3`;
- gradient: degree `-4`;
- next derivative: degree `-5`.

Thus for nearby points and far sources,

\[
|\delta\nabla p_{far}|
\lesssim
|x-y|
\int_{far}\frac{|u(z)|^2}{|z-X|^5}dz.
\]

Under a critical local `L^2`-Morrey bound, the dyadic far-pressure difference is scale-critically controlled.

Status: **DERIVED BRIDGE**.

Near pressure remains coupled to local nonlinear structure and is still an open dynamics channel.  Because the final epsilon gate is pressure-free, pressure is needed to control the **evolution** of `C_phi`, not the final regularity condition itself.

---

# I. Strain, vorticity, and off-diagonal DSD diagnostics

Retained exact/benchmark structures include:

\[
\operatorname{tr}S=0,
\]

\[
\omega^TS\omega,
\]

\[
\omega^TS\omega
=|\omega|^2\,\xi^TS\xi,
\]

and

\[
-\det S
\le
\frac12\lambda_2^+|S|^2.
\]

Two-seed audits show that nonlinear cross terms and cross stretching cannot be reconstructed from diagonal/self channels alone; DSD off-diagonal channels must be retained.

External anchors include Constantin–Fefferman-type vorticity-direction criteria and middle-strain-eigenvalue criteria.

The open task is to connect these structures to a quantitative decay/control of the moving weighted-sphere redistribution channels.

Status: **OPEN PROOF OBLIGATION**.

---

# J. Material/Lagrangian track: secondary diagnostics only

For the material flow map,

\[
\dot F=(\nabla u)F,
\qquad
\det F=1,
\]

and

\[
A=F^{-1}F^{-T}.
\]

Material coordinates remove explicit advection, but no new physical viscosity is generated. Exactly,

\[
(\nabla_aU)A(\nabla_aU)^T
=(\nabla_xu)(\nabla_xu)^T.
\]

Likewise, explicit `F^{-T}` factors in pulled-back boundary integrals are geometric representations, not independent energy sources.

Retained uses:

- follow the same fluid particles;
- inspect deformation/strain lineage;
- keep a fixed material reference domain;
- generate structural diagnostics.

Not retained as proof mechanisms:

- `F^{-T}` as an independent pressure amplification source;
- `det A=1` or `tr A>=3` as enhanced viscous coercivity;
- eigenvalues of `A` alone as physical weak/strong viscosity directions.

Status: **SECONDARY TRACK + FAILED ROUTES PRUNED**.

---

# K. Other routes pruned or demoted

| Route | Status | Reason |
|---|---|---|
| Global `L^3` universally decreases | FAILED-ROUTE CANDIDATE | stable asymmetric positive pressure-correlation audit |
| `Pi_3` bounded by a function of `T_3` alone | FAILED ROUTE for scale-compatible instantaneous closure | scaling mismatch |
| One-way outward pressure/advection flux at every radius | FAILED-ROUTE CANDIDATE | asymmetric sign changes |
| Fixed-origin shell family is translation complete | FAILED ROUTE | translated benchmark |
| Point-centered `sup_ell C_rel` as all-scale internal norm | REPAIRED | large-scale center/far-field drift artifact; mean centering fixes it |
| `lambda_2^+` alone controls material boundary geometry | FAILED ROUTE for geometric claim | trace-free `diag(-M,0,M)` countermodel |
| Accelerating-frame assumption needed for suitable bridge | DEMOTED | Eulerian weighted-variance lemma and generalized suitable translation are now derived |

---

# L. Remaining proof obligations, in priority order

1. **Critical concentration exclusion:** prove that the weighted internal velocity around every candidate singular endpoint cannot keep the pressure-free `L^{5/2+delta}` quantity above its epsilon threshold on arbitrarily small scales.
2. **Redistribution estimate:** obtain a non-circular multiscale estimate for `A_phi`, `P_phi`, and `B_phi` against oscillation/dissipation and DSD strain/alignment/cross channels.
3. **Multiscale migration:** prevent dangerous concentration from merely moving between nearby centers or adjacent scales while avoiding any one fixed-scale estimate.
4. **Arbitrary-data closure:** every final constant must depend only on admissible initial-data quantities and `nu`, not Gaussian symmetry or a posteriori smoothness.
5. **Global conclusion:** combine the concentration exclusion with the published pressure-free epsilon-regularity theorem to rule out every finite-time singularity.

\[
\boxed{
\text{Global smoothness is not currently proved.}
}
\]

---

# M. Reproducibility policy

Exact symbolic checks, deterministic numerical audits, and failed-route witnesses are executable through GitHub Actions.

A benchmark is never promoted to an arbitrary-data theorem without proof.  The successful CI run at the current bridge stage verifies the executable algebra/numerics; it is not evidence by itself for global regularity.
