# Current DSD-assisted Navier–Stokes route

Date: 2026-08-12

Status: **ACTIVE PROOF-CHALLENGE MAP — GLOBAL REGULARITY NOT PROVED**.

This file records only the currently active route.  Exploratory/failed branches remain in `PROOF_MAP.md`, notes, and Git history.

---

## 1. Baseline problem

The equation is unchanged:

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad
\nabla\cdot u=0,
\qquad
x\in\mathbb R^3,
\quad \nu>0,
\quad f=0.
\]

DSD is used as a representation / aggregation / proof-audit layer, not as an added force law.

---

# 2. Primary physical-scale track: moving weighted mean sphere

For a smooth scale kernel/cutoff `phi_ell`, choose the center by the local weighted mean velocity,

\[
\dot X_\ell(t)
=
\frac{\int\phi_\ell(x-X_\ell)u(x,t)dx}{\int\phi_\ell dx},
\]

and define

\[
v=u-\dot X_\ell.
\]

Then

\[
\int\phi_\ell(x-X_\ell)v\,dx=0.
\]

### Derived lemma

For the whole-space finite-energy suitable class, the moving weighted variance satisfies

\[
\begin{aligned}
&\frac12\int\varphi(t)|v(t)|^2
+\nu\int_s^t\int\varphi|\nabla u|^2\\
&\le
\frac12\int\varphi(s)|v(s)|^2
+\int_s^t\int\frac{|v|^2}{2}v\cdot\nabla\varphi\\
&\quad+
\int_s^t\int p\,v\cdot\nabla\varphi
+\frac\nu2\int_s^t\int|v|^2\Delta\varphi.
\end{aligned}
\]

A generalized time-dependent translation maps this moving window to an ordinary suitable cylinder.

### External gate

A published pressure-free epsilon-regularity criterion can therefore be fed by the critical internal-velocity norm rather than by the coherent local translation.

### Current requirement

A hypothetical singularity must retain non-small internal oscillation/dissipation at arbitrarily small endpoint scales.

---

# 3. One-step physical-scale closure

At parent radius `R=4 ell`, define

\[
C_R=R^{-1}\int_{B_R}|u-(u)_{B_R}|^2,
\qquad
E_R=R\int_{B_R}|\nabla u|^2.
\]

The relative advection and near pressure satisfy

\[
\boxed{
A_\phi,\ P_{\rm near}
\lesssim
(C_RE_R)^{3/4},
}
\]

while the cutoff-viscous term satisfies

\[
\boxed{
B_\phi\lesssim\nu C_R.
}
\]

After subtracting its dynamically irrelevant affine part, the genuinely remote pressure obeys

\[
\boxed{
\mathfrak H_\ell
\lesssim
\sum_{j\ge3}2^{-4j}M_{2^{j+1}\ell}.
}
\]

Thus macroscopically remote pressure cannot inject order-one affine-free pressure directly into arbitrarily small scales.

### Current requirement

A singular cascade must be mainly **locally sustained in physical scale**.

---

# 4. Vorticity occupancy / sparseness track

At the natural vorticity scale

\[
r\sim\|\omega\|_\infty^{-1/2},
\]

define

\[
\mathcal W_r
=r\int_{B_r}|\omega|^2dx.
\]

For an intense-vorticity set `S subset B_r`, the exact geometry lemma is

\[
\boxed{
\inf_d\rho_{\rm line}(d)
\le
\rho_{\rm vol}^{1/3}.
}
\]

Small local enstrophy therefore forces a sparse direction and can feed an external geometric regularity theorem.

### Time-window channel

\[
\boxed{
\mathcal Z_\omega(t)
=
\|\omega(t)\|_\infty^{1/2}
\int_{I_t}\|\omega(s)\|_2^2ds.
}
\]

A residual singularity must keep this channel non-small on arbitrarily late dangerous natural windows.

---

# 5. Direction–strain competition

Where `omega != 0`,

\[
\rho=|\omega|,
\qquad
\xi=\omega/|\omega|,
\qquad
\gamma=\xi^TS\xi.
\]

The exact magnitude equation is

\[
\boxed{
(\partial_t+u\cdot\nabla-\nu\Delta)\rho
=
\rho(\gamma-\nu|\nabla\xi|^2).
}
\]

Thus rough direction is dynamically penalized by diffusion; positive strain alignment must overcome this penalty to grow maximum vorticity.

At a maximum-vorticity point with positive excess

\[
g=\gamma-\nu|\nabla\xi|^2>0,
\]

one has the branch

\[
\boxed{
\lambda_2^+\ge g/2
\quad\text{or}\quad
\lambda_3a_3^2-\nu|\nabla\xi|^2\ge g/2.
}
\]

### External gates

- vorticity-direction coherence criteria;
- middle-strain-eigenvalue criteria;
- a recent 2026 preprint log-BMO direction gate, used only in its stated critical-point/Lorentz scope.

---

# 6. Occupancy / segregation / palinstrophy track

Danger channels are not tracked only by their scalar size.  Their spatial overlap is retained.

For intense vorticity

\[
V_a=\{|\omega|\ge aW\}
\]

and direction-gradient energy,

\[
\Sigma_{\xi V}
=
\frac{\int_{V_a}|\nabla\xi|^2}{\int_B|\nabla\xi|^2}.
\]

A residual flow must either let direction-gradient diffusion overlap the intense core, or spatially segregate the directional defects into lower-vorticity regions.

If both a substantial high-vorticity set and a substantial low-vorticity set coexist,

\[
\boxed{
\frac{r^2}{W^2}
\fint_{B_r}|\nabla|\omega||^2
\gtrsim
\rho_{\rm high}\rho_{\rm low}(a-b)^2.
}
\]

Using

\[
|\nabla\omega|^2
=|\nabla|\omega||^2+|\omega|^2|\nabla\xi|^2,
\]

spatial segregation pushes the residual burden into critical palinstrophy or an ultra-dense vorticity core.

---

# 7. Global vorticity-axis matrix

Define

\[
\mathsf C_\omega(t)
=
\frac{\int\omega\otimes\omega dx}{\|\omega\|_2^2},
\]

with eigenvalues

\[
\mu_1\ge\mu_2\ge\mu_3,
\qquad
\sum_i\mu_i=1.
\]

The optimal global constant axis satisfies

\[
\boxed{
\min_{|n|=1}\|n\times\omega\|_2^2
=\|\omega\|_2^2(1-\mu_1).
}
\]

Let

\[
\Pi_\omega=1-\mu_1.
\]

A corollary of the external locally-anisotropic criterion gives the necessary blowup certificate

\[
\boxed{
\int_0^{T^*}
[\|\omega\|_2^2\Pi_\omega]^2dt
=\infty.
}
\]

Combining this with finite energy dissipation gives the sufficient condition

\[
\boxed{
\sup_{t<T^*}
\|\omega(t)\|_2\Pi_\omega(t)<\infty
\Longrightarrow
\text{no finite-time blowup}.
}
\]

### Current requirement

Enstrophy growth in a residual singularity must retain enough **multi-axis directional participation**.

---

# 8. Local vorticity covariance-axis lemma

Use the positive Student-type kernel

\[
\eta_r(z)=c_mr^{-3}(1+|z|^2/r^2)^{-m},
\qquad m>5/2.
\]

Define

\[
E_r(x)=\eta_r*|\omega|^2,
\]

\[
C_r(x)
=
\frac{\eta_r*(\omega\otimes\omega)}{E_r(x)}.
\]

Let

\[
\Pi_r=1-\mu_1,
\qquad
\delta_r=\mu_1-\mu_2.
\]

Then

\[
\boxed{
\delta_r\ge1-2\Pi_r.
}
\]

For the principal axis `n_r`,

\[
\boxed{
r|\nabla n_r|
\le
m\frac{\sqrt{\mu_1\Pi_r}}{\delta_r}.
}
\]

Hence small local multi-axis defect automatically both opens the eigenvalue gap and smooths the best local axis.

A strong corollary through the external locally-anisotropic theorem is:

if

\[
\varepsilon(t)=\sup_x\Pi_{r(t)}(x,t)
\le\varepsilon_0<1/2,
\]

\[
r^{-1}\in L^\infty_{\rm loc}(0,T^*),
\]

and

\[
\boxed{
\sup_{t<T^*}
\varepsilon(t)\|\omega(t)\|_2<\infty,
}
\]

then finite-time blowup is excluded.

### Current requirement

A residual singularity must maintain dynamically significant local multi-axis participation strongly enough to violate this gate.

---

# 9. Dynamics of local multi-axis participation

For the moving local covariance block, define the optimal off-axis enstrophy

\[
D_\perp
=E_r(1-\mu_1).
\]

Its exact smooth budget is

\[
\begin{aligned}
\dot D_\perp
&+2\nu\int\varphi_r|\nabla\omega_\perp|^2\\
&=
2\int\varphi_r\omega_\perp\cdot S\omega\\
&\quad+
\int|\omega_\perp|^2(u-U)\cdot\nabla\varphi_r
+
u\int|\omega_\perp|^2\Delta\varphi_r.
\end{aligned}
\]

The nonlinear production splits exactly into

\[
\boxed{
\omega_\perp\cdot S\omega
=
\omega_\perp\cdot S\omega_\perp
+(n\cdot\omega)\omega_\perp\cdot P_\perp Sn.
}
\]

Thus multi-axis content is maintained by

1. off-axis self stretching;
2. principal-axis to off-axis conversion;
3. relative physical-scale flux.

---

# 10. Axis conversion = strain-eigenvalue variance

Let

\[
b_i=(n\cdot e_i)^2
\]

in the strain eigenframe.  Then

\[
\boxed{
|P_\perp Sn|^2
=
\sum_{i<j}
b_i b_j(\lambda_i-\lambda_j)^2.
}
\]

Therefore principal-to-off-axis vorticity conversion requires both

- mixing of the vorticity best axis across different strain eigendirections;
- and nonzero strain eigenvalue gaps.

This is a genuine off-diagonal axis-property channel already contained in NSE.

---

# 11. Higher derivative / two-index track

Keep physical scale and derivative order separate:

\[
\mathcal K_{j,k}.
\]

Factorial normalization of derivative channels removes Leibniz binomial coefficients:

\[
\boxed{
N_k\lesssim\sum_{m=0}^{k}A_mB_{k-m}.
}
\]

The generating functions therefore satisfy a Cauchy-product structure.

Meanwhile affine-free remote derivative pressure satisfies

\[
\boxed{
H_{\ell,k}
\lesssim
\sum_{j\ge3}
2^{-(k+4)j}M_{2^{j+1}\ell}.
}
\]

Thus at high derivative order the direct remote-pressure sector becomes increasingly weak; the unresolved high-order obstruction is the **near-scale nonlinear derivative convolution**.

The established Grujic--Xu higher-derivative sparseness framework is treated as an external anchor here, not as DSD novelty.

---

# 12. Current residual singularity class

Any hypothetical singularity surviving the current route must simultaneously exhibit:

1. critical moving-frame internal velocity oscillation at arbitrarily small scales;
2. locally sustained scale cascade rather than direct remote-pressure feeding;
3. non-sparse intense vorticity at natural vorticity scales;
4. non-small natural-window enstrophy cost;
5. failure of applicable direction-coherence/log-BMO gates;
6. enough positive strain/extensional alignment to beat direction diffusion;
7. Miller-critical positive-middle-strain behavior;
8. enough global and local multi-axis vorticity participation to evade optimal-axis gates;
9. sustained off-axis self stretching and/or strain-axis conversion;
10. critical palinstrophy / dense-core structure when danger channels segregate;
11. survival of higher-derivative sparseness/analyticity restrictions;
12. near-scale nonlinear derivative convolution strong enough to continue the cascade.

No contradiction among all twelve has yet been proved.

---

# 13. Principal open target

The most concentrated remaining target is now

\[
\boxed{
\text{persistent local multi-axis vorticity participation}
\quad\text{versus}\quad
\text{off-axis diffusion + strain-axis conversion cost}.
}
\]

A proof-level next step would derive a scale-critical estimate that makes

\[
\|\omega\|_2\sup_x\Pi_{r(t)}
\]

remain bounded, or else forces one of the already established sparseness / strain / higher-derivative regularity gates.

Until such a closure is proved, global smoothness remains **NOT CLAIMED**.
