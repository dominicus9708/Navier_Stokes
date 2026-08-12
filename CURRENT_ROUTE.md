# Current DSD-assisted Navier–Stokes route

Date: 2026-08-13

Status: **ACTIVE PROOF-CHALLENGE MAP — GLOBAL REGULARITY NOT PROVED**.

This file records only the currently active route. Exploratory/failed branches remain in `PROOF_MAP.md`, notes, and Git history.

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

## 2. Primary physical-scale track: moving weighted mean sphere

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

**Current requirement:** a hypothetical singularity must retain non-small internal oscillation/dissipation at arbitrarily small endpoint scales.

---

## 3. One-step physical-scale closure

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

while

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

**Current requirement:** a singular cascade must be mainly **locally sustained in physical scale**.

---

## 4. Vorticity occupancy / sparseness track

At the natural vorticity scale

\[
r\sim\|\omega\|_\infty^{-1/2},
\]

define

\[
\mathcal W_r=r\int_{B_r}|\omega|^2dx.
\]

For an intense-vorticity set `S subset B_r`,

\[
\boxed{
\inf_d\rho_{\rm line}(d)
\le
\rho_{\rm vol}^{1/3}.
}
\]

The natural-window channel is

\[
\boxed{
\mathcal Z_\omega(t)
=
\|\omega(t)\|_\infty^{1/2}
\int_{I_t}\|\omega(s)\|_2^2ds.
}
\]

**Current requirement:** a residual singularity must remain non-sparse and keep this natural-window cost non-small on arbitrarily late dangerous windows.

---

## 5. Direction–strain competition

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

At a maximum-vorticity point with

\[
g=\gamma-\nu|\nabla\xi|^2>0,
\]

one has

\[
\boxed{
\lambda_2^+\ge g/2
\quad\text{or}\quad
\lambda_3a_3^2-\nu|\nabla\xi|^2\ge g/2.
}
\]

External anchors remain the direction-coherence criteria, middle-strain-eigenvalue criteria, and the 2026 log-BMO direction preprint only in its stated scope.

---

## 6. Occupancy / segregation / palinstrophy track

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

If both a substantial high-vorticity and low-vorticity region coexist,

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

## 7. Global vorticity-axis matrix

Define

\[
\mathsf C_\omega
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

and the sufficient condition

\[
\boxed{
\sup_{t<T^*}\|\omega(t)\|_2\Pi_\omega(t)<\infty
\Longrightarrow
\text{no finite-time blowup}.
}
\]

---

## 8. Axis-choice-free projective dispersion

Define

\[
\boxed{
\mathcal J_\omega
=1-\operatorname{tr}(\mathsf C_\omega^2).
}
\]

Exactly,

\[
\boxed{
\mathcal J_\omega
=
\frac{
\iint|\omega(x)\times\omega(y)|^2dxdy
}{
\|\omega\|_2^4
}.
}
\]

Thus `J_omega` is a sign-free, eigenvector-free projective directional-dispersion channel.

It is uniformly equivalent to the principal-axis defect:

\[
\boxed{
\frac12\mathcal J_\omega
\le
\Pi_\omega
\le
\frac32\mathcal J_\omega.
}
\]

Hence a hypothetical blowup must also satisfy

\[
\boxed{
\|\omega\|_2^2\mathcal J_\omega
\notin L^2(0,T^*),
}
\]

and in particular

\[
\boxed{
\sup_{t<T^*}
\|\omega(t)\|_2\mathcal J_\omega(t)
=\infty.
}
\]

**Current requirement:** enstrophy concentration must retain genuine pairwise cross-axis content rather than collapsing rapidly to a one-axis covariance state.

---

## 9. Exact projective-dispersion dynamics

Let

\[
N=\int\omega\otimes\omega,
\qquad
A=\int(S\omega)\otimes\omega,
\]

\[
H=\sum_k\int(\partial_k\omega)\otimes(\partial_k\omega),
\]

with

\[
E=\operatorname{tr}N,
\quad
B=A/E,
\quad
G=H/E,
\quad
q=\operatorname{tr}B,
\quad
p=\operatorname{tr}G.
\]

Then

\[
\boxed{
\dot C
=B+B^T-2\nu G-2(q-\nu p)C.
}
\]

For

\[
J=1-\operatorname{tr}(C^2),
\]

\[
\boxed{
\dot J
=4\mathcal M_S+4\nu\mathcal M_\nu,
}
\]

where

\[
\mathcal M_S
=q\operatorname{tr}(C^2)-\operatorname{tr}(CB),
\]

\[
\mathcal M_\nu
=\operatorname{tr}(CG)-p\operatorname{tr}(C^2).
\]

Thus total enstrophy amplification is separated from directional mixing/demixing.

---

## 10. S/V projective mixing closure

Define

\[
\mathcal L_S
=
\left(\frac1E\int|S\omega|^2dx\right)^{1/2}.
\]

Then

\[
\boxed{
|\mathcal M_S|
\le
\sqrt{J(1-J)}\,\mathcal L_S.
}
\]

Moreover,

\[
\mathcal L_S^2
=
\frac1E\int|\omega|^2
\left[
\gamma^2+|P_{\xi^\perp}S\xi|^2
\right]dx.
\]

Thus large strain-driven directional mixing requires magnitude stretching and/or strain-gap axis conversion.

If

\[
C_\nabla=H/P,
\qquad
\Delta_\nu=\|C_\nabla-C\|_F,
\]

then

\[
\boxed{
|\mathcal M_\nu|
\le
\frac PE\sqrt{1-J}\,\Delta_\nu.
}
\]

Therefore

\[
\boxed{
\dot J
\le
4\sqrt{1-J}
\left[
\sqrt J\,\mathcal L_S
+\nu(P/E)\Delta_\nu
\right].
}
\]

This yields two active branches:

1. **S-branch:** strain exposure / magnitude stretching / axis conversion;
2. **V-branch:** palinstrophy-to-enstrophy ratio times vorticity-gradient covariance mismatch.

If `M_nu<=0`, raising `J` from `J0` to `J1` costs

\[
\boxed{
\int_s^t\mathcal L_S d\tau
\ge
\frac12
\left[
\arcsin\sqrt{J_1}
-
\arcsin\sqrt{J_0}
\right].
}
\]

No general finite bound on this regeneration cost has yet been proved.

---

## 11. Local vorticity covariance-axis lemma

Use the positive Student-type kernel

\[
\eta_r(z)=c_mr^{-3}(1+|z|^2/r^2)^{-m},
\qquad m>5/2.
\]

Define

\[
E_r=\eta_r*|\omega|^2,
\qquad
C_r=\frac{\eta_r*(\omega\otimes\omega)}{E_r}.
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
\delta_r\ge1-2\Pi_r,
}
\]

and for the principal axis `n_r`,

\[
\boxed{
r|\nabla n_r|
\le
m\frac{\sqrt{\mu_1\Pi_r}}{\delta_r}.
}
\]

Thus small local multi-axis defect automatically opens the eigenvalue gap and smooths the best local axis.

---

## 12. Local multi-axis dynamics and axis conversion

For

\[
D_\perp=E_r(1-\mu_1),
\]

the nonlinear production splits exactly as

\[
\boxed{
\omega_\perp\cdot S\omega
=
\omega_\perp\cdot S\omega_\perp
+(n\cdot\omega)\omega_\perp\cdot P_\perp Sn.
}
\]

In the strain eigenframe,

\[
\boxed{
|P_\perp Sn|^2
=
\sum_{i<j}b_i b_j(\lambda_i-\lambda_j)^2,
\qquad
b_i=(n\cdot e_i)^2.
}
\]

Thus local multi-axis content is maintained through off-axis self stretching, strain-gap weighted axis conversion, and relative physical-scale flux.

---

## 13. Higher derivative / physical-scale track

Keep physical scale and derivative order separate:

\[
\mathcal K_{j,k}.
\]

Factorial normalization removes Leibniz binomial coefficients and leaves the near-scale nonlinear derivative Cauchy convolution

\[
\boxed{
N_k^{\rm nl}
\lesssim
\sum_{m=0}^{k}A_mB_{k-m}.
}
\]

Affine-free remote derivative pressure satisfies

\[
\boxed{
H_{\ell,k}
\lesssim
\sum_{j\ge3}
2^{-(k+4)j}M_{2^{j+1}\ell}.
}
\]

Thus the unresolved high-order pressure/nonlinearity burden is local in physical scale and concentrated in the derivative convolution.

---

## 14. Derivative-order projective covariance chain

Use ordered derivative words `I in {1,2,3}^k` and define

\[
N_k
=\sum_I\int(\partial_I\omega)\otimes(\partial_I\omega)dx,
\]

\[
E_k=\operatorname{tr}N_k,
\qquad
C_k=N_k/E_k,
\qquad
J_k=1-\operatorname{tr}(C_k^2).
\]

For

\[
F_I
=\partial_I(S\omega)-[\partial_I,u\cdot\nabla]\omega,
\]

let

\[
A_k=\sum_I\int F_I\otimes\partial_I\omega dx.
\]

Then viscosity nests exactly into the next derivative covariance:

\[
\boxed{
\dot N_k
=A_k+A_k^T-2\nu N_{k+1}.
}
\]

Writing

\[
B_k=A_k/E_k,
\quad
q_k=\operatorname{tr}B_k,
\quad
r_k=E_{k+1}/E_k,
\]

we obtain

\[
\boxed{
\frac14\dot J_k
=
\mathcal M_{N,k}
+
u r_k
\left[
\operatorname{tr}(C_kC_{k+1})
-\operatorname{tr}(C_k^2)
\right].
}
\]

Define

\[
\Delta_k=\|C_{k+1}-C_k\|_F
\]

and

\[
L_k
=\left(
\frac{\sum_I\|F_I\|_2^2}{E_k}
\right)^{1/2}.
\]

Then

\[
\boxed{
|\mathcal M_{N,k}|
\le
\sqrt{J_k(1-J_k)}L_k,
}
\]

\[
\boxed{
\left|
\operatorname{tr}[C_k(C_{k+1}-C_k)]
\right|
\le
\sqrt{1-J_k}\,\Delta_k,
}
\]

and therefore

\[
\boxed{
\dot J_k
\le
4\sqrt{1-J_k}
\left[
\sqrt{J_k}L_k
+\nu r_k\Delta_k
\right].
}
\]

The previous V-branch is exactly the first link `k=0 -> 1`:

\[
C_1=C_\nabla,
\qquad
r_0=P/E.
\]

Hence the active structure is now

\[
\boxed{
\text{physical scale }j
\times
\text{derivative order }k
\times
\text{directional covariance }C_k.
}
\]

---

## 15. Current residual singularity class

Any hypothetical singularity surviving the current route must simultaneously exhibit:

1. critical moving-frame internal velocity oscillation at arbitrarily small scales;
2. locally sustained scale cascade rather than direct remote-pressure feeding;
3. non-sparse intense vorticity at natural vorticity scales;
4. non-small natural-window enstrophy cost;
5. failure of applicable direction-coherence/log-BMO gates;
6. enough positive strain/extensional alignment to beat direction diffusion;
7. Miller-critical positive-middle-strain behavior;
8. enough global and local multi-axis vorticity participation to evade optimal-axis gates;
9. non-integrable pairwise projective cross-axis enstrophy `E J`;
10. persistent positive projective mixing through the S-branch and/or V-branch;
11. sustained off-axis self stretching and/or strain-gap axis conversion;
12. critical palinstrophy / dense-core structure when danger channels segregate;
13. survival of higher-derivative sparseness/analyticity restrictions;
14. near-scale nonlinear derivative convolution strong enough to continue the cascade;
15. derivative covariance mismatch `r_k Delta_k` that remains active whenever viscous directional regeneration is used.

No contradiction among all fifteen has yet been proved.

---

## 16. Principal open target

The remaining problem has been reduced to an intersection of two chains:

\[
\boxed{
\textbf{S-chain:}
\quad
\sqrt{J_k}L_k
\ \longleftrightarrow\ 
\text{nonlinear derivative convolution / strain-alignment gates},
}
\]

\[
\boxed{
\textbf{V-chain:}
\quad
\nu r_k\Delta_k
\ \longleftrightarrow\ 
\text{neighboring derivative covariance mismatch / palinstrophy hierarchy}.
}
\]

A proof-producing next step would show that these two chains cannot both remain active through arbitrarily small physical scales and arbitrarily high derivative orders while respecting the known finite-energy and geometric/sparseness constraints.

Until such a uniform closure is proved, global smoothness remains **NOT CLAIMED**.
