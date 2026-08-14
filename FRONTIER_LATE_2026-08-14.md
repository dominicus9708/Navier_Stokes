# Late Frontier — 2026-08-14

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This file records the late-2026-08-14 reduction after the quadratic translation-gauge correction and the exact-adjoint-kernel analysis. Earlier frontier files remain part of the audit trail.

---

## 1. Fixed setting

The PDE is the ordinary incompressible Navier--Stokes system on all of `R^3`.

At terminal first hitting,

\[
W=\|\omega(T)\|_\infty,
\qquad
r_W=W^{-1/2},
\]

and

\[
U(y,s)=r_Wu(x_*+r_Wy,T+r_W^2s),
\qquad
\Omega=r_W^2\omega.
\]

Then

\[
\|\Omega(s)\|_\infty\le1,
\qquad
|\Omega(0,0)|=1.
\]

The surviving intermediate residual peak is parameterized by

\[
\boxed{
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\qquad
m\to0.
}
\]

---

# 2. Closed or reclassified branches

## 2.1 Pure affine inheritance

In co-affine Cauchy coordinates, pure time-dependent affine transport/stretch plus viscosity is exactly anisotropic Gaussian heat. On the bounded accumulated-affine branch, previous-checkpoint inheritance is `o(m)`.

Thus a surviving pulse must be freshly produced or imported during the current step.

## 2.2 Gaussian drift is not a physical source

The exact adjoint Markov representation is

\[
\Omega(x_*,T)
=P_{s_0,T}\Omega(s_0)(x_*)
+
\int_{s_0}^TP_{s,T}(S\Omega)(x_*)ds.
\]

Transport and viscosity are contained in the transition kernel. The former Gaussian drift term is only an observation-weight mismatch.

## 2.3 Frozen mean-vorticity linear coupling is skew redistribution

For constant mean vorticity `Omega0`,

\[
K_{\Omega_0}\eta
=(\Omega_0\cdot\nabla)r
\]

has Fourier symbol

\[
-\frac{\Omega_0\cdot k}{|k|^2}(k\times\cdot).
\]

Hence

\[
K_{\Omega_0}^*=-K_{\Omega_0}
\]

and it commutes with isotropic heat.

Therefore it cannot create global residual enstrophy or globally integrated fixed-scale Gaussian variance. Any local gain is spatial/spectral import.

## 2.4 Quadratic `Ab` is translation gauge

For the quadratic velocity / first-chaos vorticity core,

\[
w_\gamma=Q-b,
\qquad
\eta=Az,
\]

and the old constant-shift source is

\[
Ab=(b\cdot\nabla)\eta.
\]

Switching from the Gaussian-mean center to the material/Taylor center changes the center velocity by `-b` and cancels this term exactly.

Thus

\[
\boxed{
J_{Ab}\text{ is translation/import, not material-center vorticity creation.}
}
\]

The older projective-`Ab` dissipation notes remain algebraically correct in the Gaussian-mean gauge but are superseded as a physical amplification classification on the exact quadratic core.

## 2.5 Quadratic trace action collapses on the full terminal interval

For the degree-two coefficient `Y2`, terminal collapse gives

\[
|Y_2(\tau)|
\lesssim
\sqrt{\min\{m,\tau\}}.
\]

The exact trace telescoping identity therefore yields

\[
\boxed{
\left|\int_0^{c/m}J_{\rm tr}d\tau\right|
\lesssim
\sqrt m(1+|\log m|)
\to0.
}
\]

No `W^(1/10)` lower-radius restriction is needed.

## 2.6 Exact rapid-rotation quadratic resonance does not reopen the lane

The divergence-free SO(2)-equivariant homogeneous quadratic core is

\[
Q_{\alpha,\beta,\chi}
=
(\alpha zx-\beta zy,
\alpha zy+\beta zx,
\chi(x^2+y^2)-\alpha z^2).
\]

Its material-center resonant mean source is

\[
J_{\rm res}
=(0,0,-2\beta(\alpha+4\chi)),
\]

while

\[
\|N_2\|_\gamma^2
=8\beta^2(2\alpha^2+\beta^2+8\chi^2).
\]

Hence

\[
\boxed{
|J_{\rm res}|
\le\frac{\sqrt5}{2}\|N_2\|_\gamma.
}
\]

Thus exact low-Hermite fast-rotation resonance still forces second chaos, which is already subject to full-terminal trace collapse.

Conclusion:

\[
\boxed{
\text{bounded affine + asymptotically low Hermite}
\Longrightarrow
\text{no order-one material-center amplification}
}
\]

provided the explicitly retained nonquadratic/transport/frame remainders are controlled.

---

# 3. Mean-vorticity occupancy and finite-energy barriers

A terminal order-one Gaussian mean with residual source cap `B<=m` needs time

\[
\tau_m\asymp m^{-1}
\]

and radius

\[
R_m=m^{-1/2}.
\]

The normalized enstrophy occupancy gives

\[
\int E_\omega d\tau
\gtrsim m^{-5/2},
\]

so physical dissipation obeys

\[
D_{\rm phys}^{\rm mean}
\gtrsim
W^{-1/2}m^{-5/2}
=W^{1/3}\Lambda^{-5/2}.
\]

A repeated surviving cascade therefore requires

\[
\boxed{
\Lambda/W^{2/15}\to\infty.
}
\]

Instantaneously, curl duality gives

\[
\|U\|_2^2
\gtrsim
R^5|\bar\Omega_R|^2,
\]

and the Gaussian-tail refinement gives

\[
\|U\|_2^2
\gtrsim
R^5(\log R)^{5/2}
\]

for an order-one coherent affine rotation with `B<=CR^-2`.

Thus the surviving coherent core lies strictly below the old `W^(1/10)` radius up to logarithmic correction.

---

# 4. Exact-adjoint-kernel DSD state

Let

\[
K_s(x)=K(x,s;x_*,T)
\]

be the exact adjoint transition density and write `K`-expectations as `<>_K`.

Define

\[
L_K=\langle\nabla U\rangle_K,
\qquad
\bar S_K=\langle S\rangle_K,
\qquad
\bar\Omega_K=\langle\Omega\rangle_K.
\]

Then for any probability weight,

\[
\boxed{
B_K
=V_{S,K}+\frac12V_{\omega,K}.
}
\]

The physical stretching source decomposes exactly as

\[
\boxed{
\langle S\Omega\rangle_K
=\bar S_K\bar\Omega_K+J_K,
}
\]

with

\[
\boxed{
J_K
=\langle\delta S_K\,\delta\Omega_K\rangle_K,
\qquad
|J_K|\le\frac1{\sqrt2}B_K.
}
\]

Thus Gaussian comparability is **not** required for source completeness.

The loss caused by kernel deformation is functional geometry, not an untyped source.

---

# 5. Exact kernel cannot collapse below diffusive volume

In backward age `tau`, the adjoint density satisfies an incompressible Fokker--Planck equation.

Its entropy obeys

\[
h'=\nu I.
\]

Entropy power

\[
N_K
=\frac1{2\pi e}e^{2h/3}
\]

satisfies, by the entropy/Fisher isoperimetric inequality,

\[
\boxed{N_K'\ge2\nu.}
\]

Starting from the terminal delta,

\[
\boxed{N_K(\tau)\ge2\nu\tau.}
\]

Since the same-covariance Gaussian maximizes entropy,

\[
N_K\le(\det\Sigma_K)^{1/3}.
\]

Hence

\[
\boxed{
R_K:=(\det\Sigma_K)^{1/6}
\ge\sqrt{2\nu\tau}.
}
\]

Kernel deformation cannot be an all-direction volume collapse. It must be anisotropy, non-Gaussian shape, or spatial non-tightness.

---

# 6. Kernel anisotropy and non-Gaussianity are coupled exactly

Define the velocity-regression matrix

\[
M_K
=E_K[(U-\bar U_K)\otimes(X-m_K)]\Sigma_K^{-1}.
\]

Then

\[
\boxed{
\Sigma_K'
=-M_K\Sigma_K-\Sigma_KM_K^T+2\nu I.
}
\]

Let `G_K` be the Gaussian with the same mean/covariance as `K`, and define the relative score

\[
s_K=\nabla\log(K/G_K).
\]

For the kernel-mean affine residual

\[
r_K=U-\bar U_K-L_K(X-m_K),
\]

one has the exact Stein-type identity

\[
\boxed{
M_K-L_K
=E_K[r_K\otimes s_K].
}
\]

Thus covariance deformation beyond the physical mean gradient requires both residual velocity and non-Gaussian score.

Define

\[
\mathfrak D_K=D_{\rm KL}(K\|G_K),
\qquad
I_{\rm rel}=E_K|s_K|^2.
\]

Then

\[
\boxed{
\mathfrak D_K'
=-E_K[r_K\cdot s_K]-\nu I_{\rm rel}.
}
\]

Equivalently,

\[
\boxed{
\mathfrak D_K'
=
\frac1{4\nu}E_K|r_K|^2
-
\nu E_K\left|s_K+\frac{r_K}{2\nu}\right|^2.
}
\]

Kernel non-Gaussianity therefore has an exact residual-transport production / relative-Fisher dissipation ledger.

---

# 7. Kernel non-Gaussianity is bounded by critical weighted enstrophy

Use the velocity-regression affine reference, whose Gaussian law has exactly the same mean/covariance as the true kernel.

Let

\[
r_M=U-\bar U_K-M_K(X-m_K).
\]

It is the least-squares velocity residual, so

\[
E_K|r_M|^2\le E_K|U|^2.
\]

The kernel density ceiling and Sobolev give

\[
E_K|U|^2
\lesssim
(\nu\tau)^{-1/2}E_\omega(\tau).
\]

Hence

\[
\boxed{
\mathfrak D_K(\tau)
\lesssim
\nu^{-3/2}
\int_0^\tau
s^{-1/2}E_\omega(s)ds.
}
\]

Define

\[
\boxed{
\mathfrak Z_K(\tau)
=\int_0^\tau s^{-1/2}E_\omega(s)ds.
}
\]

This quantity is Navier--Stokes scale critical.

A fixed kernel shape defect therefore requires a fixed critical weighted global-enstrophy action.

---

# 8. Kernel deformation has only two temporal realizations

If a fixed fraction of `Z_K` lies on

\[
[\eta\tau,\tau]
\]

for fixed `eta>0`, then

\[
\boxed{
\int_{\eta\tau}^{\tau}E_\omega ds
\gtrsim
\sqrt{\eta\tau}.
}
\]

This is an ordinary enstrophy-time / kinetic-dissipation occupancy cost.

If instead a fixed action is pushed into a terminal layer `[0,ell]`, then

\[
\boxed{
\sup_{0<s<\ell}E_\omega(s)
\gtrsim
\ell^{-1/2}.
}
\]

As `ell->0`, this forces global enstrophy escalation.

The exact strain identity routes such escalation to

\[
\boxed{
\int\!\!\int\lambda_2^+|S|^2
\gtrsim
\Delta E_\omega.
}
\]

Thus terminal kernel deformation is merged into the positive-middle-strain critical branch.

---

# 9. High-Hermite physical source branch

For the Gaussian/Hermite branch,

\[
\delta
=\frac{K_H-B}{B}
=
\frac{\sum_{n\ge2}(n-1)B_n}{B}.
\]

The residual stretching source is diagonal in Hermite degree:

\[
J_{\rm str}=\sum_nJ_n,
\qquad
|J_n|\le B_n/\sqrt2.
\]

Therefore

\[
\boxed{
|J_{\ge2}|
\lesssim
\delta B.
}
\]

A repeated high-Hermite stretching survivor requires

\[
\boxed{
\Lambda^{3/5}\delta\to\infty.
}
\]

Pure first-chaos self-feed is parity-blocked, the quadratic material-center source is closed, and exact quadratic rotation resonance does not evade second-chaos production.

Hence **genuine physical residual creation on the bounded-affine branch is now a high-Hermite / derivative phenomenon.**

---

# 10. Remaining reduced branch tree

A hypothetical singular survivor must now activate at least one of the following.

## H — High-Hermite / higher-derivative creation

\[
\boxed{
\text{higher chaos, curvature surplus, palinstrophy, or derivative covariance cascade}
}
\]

must repeatedly regenerate the residual stretching source.

## M — Positive-middle-strain critical saturation

Global enstrophy escalation, including terminally concentrated kernel deformation, is routed to

\[
\boxed{
\lambda_2^+
}
\]

and the established critical middle-strain regularity channel.

## A — Unbounded symmetric-affine deformation

If accumulated coherent strain ceases to be bounded, the affine condition-number escape is already converted to local strain-energy concentration.

Rigid rotation is not charged here.

## T — Spatial non-tightness / shell transport

If exact-kernel second moments diverge or coherent residual mass continually escapes the tracked region, the route enters shell transport, multicore aggregation, material turnover, or critical `L3` influx.

These are transport/coverage mechanisms, not independent vorticity sources.

---

# 11. What has disappeared from the independent escape list

The following should no longer be listed as separate physical amplification branches on their stated hypotheses:

1. pure bounded-affine inheritance;
2. Gaussian drift;
3. frozen mean-vorticity skew coupling;
4. quadratic `Ab` projective source;
5. quadratic trace source;
6. exact low-Hermite fast-rotation resonance;
7. adjoint-kernel volume collapse;
8. kernel non-Gaussianity as an unspecified source.

Each is either closed or routed into `H`, `M`, `A`, or `T`.

---

# 12. Principal next theorem target

The bounded-affine proof route has reached the following critical target:

\[
\boxed{
\begin{gathered}
\text{Can an infinite first-hitting sequence repeatedly sustain}\
\text{high-Hermite residual stretching or positive-middle-strain action}\
\text{while every corresponding physical dissipation / derivative / transport}\
\text{cost remains globally summable?}
\end{gathered}
}
\]

Equivalently, one needs a **critical saturation nonrepeatability theorem** for the remaining `H/M` system.

A successful next step must produce at least one of:

1. a strict subcritical power/log gain in the high-Hermite source-versus-palinstrophy balance;
2. a packing theorem for derivative covariance/curvature pulses across disjoint first-hitting windows;
3. a rigidity theorem excluding repeated near-equality in the positive-middle-strain/Betchov--GN channel;
4. a proof that failure of all three forces spatial non-tightness already incompatible with the finite-energy/material-flux ledgers.

Status: **LOW-HERMITE BOUNDED-AFFINE AMPLIFICATION CLOSED; EXACT-KERNEL GEOMETRY REDUCED TO CRITICAL ENSTROPHY/TRANSPORT ACTION; ACTIVE ENDGAME = HIGH-HERMITE DERIVATIVE SATURATION OR POSITIVE-MIDDLE-STRAIN CRITICAL SATURATION / GLOBAL REGULARITY NOT PROVED.**
