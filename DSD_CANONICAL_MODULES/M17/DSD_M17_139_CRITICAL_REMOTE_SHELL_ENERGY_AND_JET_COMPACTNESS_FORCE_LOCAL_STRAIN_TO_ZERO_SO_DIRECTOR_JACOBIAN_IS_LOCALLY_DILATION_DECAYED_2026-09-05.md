# DSD M17-139 — Critical remote-shell energy plus jet compactness forces local strain to zero, so director Jacobian is locally dilation-decayed

Date: 2026-09-05  
Canonical ID: **M17-139**

Status: **LOCAL STRAIN-DECOUPLING GATE PROVED UNDER THE RETAINED COMPACT-JET RIBBON HYPOTHESES / IF THE CRITICAL REMOTE SHELL HAS `J_R=O(1)` AND THE FIRST SPATIAL DERIVATIVE OF STRAIN IS UNIFORMLY BOUNDED ON A FIXED NEIGHBORHOOD OF THE RIBBON, THEN `|Sigma|=O(R^{-1/5})` THERE. HENCE `D_B log|J_xi|=-1+o(1)`: THE REMOTE RIBBON'S ORDER-ONE DIRECTOR JACOBIAN IS NOT LOCALLY MAINTAINED BY STRAIN BUT IS BEING DILATION-DECAYED AND MUST BE IMPORTED ALREADY GEOMETRICALLY CHARGED. FAILURE OF THE JET BOUND IS A SEPARATE HIGH-JET/LOSS-OF-COMPACTNESS EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical shell energy scale

Let `C_R` be the fixed-shape enlarged remote annulus.
Define

\[
J_R:=R\int_{C_R}|\nabla U|^2dy.
\]

On the sharp non-H survivor considered in M17-135--138,

\[
\boxed{J_R\le J_*<\infty}
\]

uniformly along the selected remote shells.
Therefore

\[
\boxed{
\int_{C_R}|\nabla U|^2dy
\le
\frac{J_*}{R}.
}
\]

Since the strain tensor `Sigma` is the symmetric part of `grad U`,

\[
|\Sigma|\le|\nabla U|,
\]

so

\[
\boxed{
\int_{C_R}|\Sigma|^2dy
\le
\frac{J_*}{R}.
}
\]

---

## 2. Compact-jet hypothesis near the ribbon

Let `N_R` be a fixed-width neighborhood of the complete compact ribbon, contained a fixed positive distance from the boundary of `C_R` for all sufficiently large `R`.

Retain the compact analytic/hard-hull jet condition in the form

\[
\boxed{
\sup_{N_R}|\nabla\Sigma|
\le
M_\Sigma<\infty,
}
\]

with `M_Sigma` independent of `R`.

This is a genuine hypothesis and must not be inferred from the shell `L2` energy alone.
Its failure defines a distinct high-jet/loss-of-compactness exit.

---

## 3. Lipschitz-ball lower bound

Fix a point `p` on the ribbon and write

\[
A:=|\Sigma(p)|.
\]

If `M_Sigma>0`, then for

\[
r_A:=\min\left\{r_0,\frac{A}{2M_\Sigma}\right\},
\]

where `r_0>0` is a fixed geometric neighborhood radius, the Lipschitz bound gives

\[
|\Sigma(y)|\ge\frac A2
\qquad
(y\in B_{r_A}(p)).
\]

For all sufficiently large `R`, the shell energy tends to zero, so the case `r_A=r_0` cannot persist with `A` bounded below by a fixed positive constant.
Thus eventually

\[
r_A=\frac{A}{2M_\Sigma}.
\]

Then

\[
\int_{C_R}|\Sigma|^2dy
\ge
\int_{B_{r_A}(p)}|\Sigma|^2dy
\ge
c\,A^2r_A^3.
\]

Hence

\[
\boxed{
\int_{C_R}|\Sigma|^2dy
\ge
c\frac{A^5}{M_\Sigma^3}.
}
\]

---

## 4. Pointwise remote strain decay

Combining with the critical shell energy upper bound,

\[
c\frac{A^5}{M_\Sigma^3}
\le
\frac{J_*}{R}.
\]

Therefore

\[
\boxed{
A
\le
C
M_\Sigma^{3/5}
J_*^{1/5}
R^{-1/5}.
}
\]

Uniformly over the ribbon,

\[
\boxed{
\sup_{\mathcal T_R}|\Sigma|
\le
C_R^{strain}R^{-1/5}
\to0.
}
\]

The exponent `1/5` is not asserted to be sharp. What matters is the strict decay to zero obtained from `L2` smallness plus one uniformly bounded spatial derivative in three dimensions.

---

## 5. Kernel strain also vanishes

Let `k` be the pure-kernel unit direction and

\[
\sigma_k:=k\cdot\Sigma k.
\]

Then

\[
|\sigma_k|\le|\Sigma|.
\]

Hence

\[
\boxed{
\sup_{\mathcal T_R}|\sigma_k|
=O(R^{-1/5}).
}
\]

Likewise every strain eigenvalue/component on the compact ribbon is `o(1)` under the same branch hypotheses.

---

## 6. Exact director-Jacobian material law becomes pure dilation decay

On the pure-kernel Rank-2 branch,

\[
\boxed{
D_B\log|J_\xi|
=\sigma_k-1.
}
\]

Therefore on the remote critical ribbon,

\[
\boxed{
D_B\log|J_\xi|
=-1+O(R^{-1/5}).
}
\]

At each sufficiently remote observation point, the director Jacobian is instantaneously **decaying**, not being locally amplified or even maintained by strain.

Thus an order-one value

\[
|J_\xi|\asymp1
\]

seen in the remote ribbon must have been imported from an earlier location/time with at least comparable geometric charge.

The local critical `1/R` bath cannot replenish it through an `O(1)` kernel strain on this compact-jet branch, because such an `O(1)` strain would itself violate the shell `L2` Dirichlet budget once jet compactness converts it to positive volume.

---

## 7. Corridor version

Suppose the critical shell bound

\[
R\int_{C_R}|\nabla U(\theta)|^2dy\le J_*
\]

and the uniform strain-jet bound hold throughout one material shell-crossing corridor of length

\[
\Delta\theta_R=2\log2+O(R^{-1})
\]

from M17-138.

Then along any ribbon trajectory that remains in the controlled corridor,

\[
\begin{aligned}
\log\frac{|J_\xi|_{out}}{|J_\xi|_{in}}
&=
\int_{\theta_{in}}^{\theta_{out}}(\sigma_k-1)d\theta\\
&=
-\Delta\theta_R+O(R^{-1/5}).
\end{aligned}
\]

Therefore

\[
\boxed{
\frac{|J_\xi|_{out}}{|J_\xi|_{in}}
=
\frac14\left(1+o(1)\right).
}
\]

Thus under a quiet critical corridor, one dyadic outward passage reduces director-Jacobian density by asymptotically a factor `4`.

This does **not** reduce the material tube's signed flux: the corresponding transverse material area expands so that frozen 2-form flux is conserved.

---

## 8. Geometry interpretation

For a material tube with flux

\[
\Phi_J=\int_SJ_\xi\cdot n\,dA
\]

conserved, a fourfold decrease in approximately uniform `|J_xi|` requires an approximately fourfold increase in the transverse material area carrying that flux.

Hence the remote similarity dilation naturally does the following:

\[
\boxed{
\text{director-density decay}
\leftrightarrow
\text{transverse area expansion}
}
\]

while leaving signed material flux unchanged.

This is consistent with the finite residence and fresh-carrier conclusions M17-117, M17-120, and M17-138.

---

## 9. New branch dichotomy

The remote fixed-fraction ribbon branch now has a sharper split:

\[
\boxed{
R_{2,\rm ribbon}^{remote}
\Longrightarrow
H_{\nabla\Sigma/jet}
\ \lor\
I_{\rm precharged\ director\ import}.
}
\]

Here

- `H_{grad Sigma/jet}` means the uniform strain-jet compactness required above fails;
- `I_precharged director import` means the ribbon enters the remote shell already carrying order-one director-area geometry, after which local dilation decreases its Jacobian density.

The second branch is not a local generation mechanism.
It is a genealogy/import branch.

---

## 10. DSD audit

### Audit A — small shell `L2` strain alone gives pointwise small strain

Rejected.
The uniform first-derivative bound is essential.
Without it, strain can concentrate on shrinking sets.

### Audit B — the compact hard hull may be silently interpreted as a physical spatial boundary

Rejected.
Only a local fixed-width neighborhood and jet bound are used; no compact physical support is inferred.

### Audit C — `J_xi` density decay means director flux is destroyed

Rejected.
The frozen material 2-form conserves signed tube flux; density decay is paid by cross-sectional expansion.

### Audit D — local strain decay closes fresh-carrier turnover

Rejected.
It proves only that fresh ribbons must be imported already geometrically charged, not that such import is impossible.

### Audit E — failure of the derivative bound is harmless

Rejected as a branch merger.
It must be routed separately to a high-jet/loss-of-compactness mechanism rather than hidden inside the compact ribbon class.

---

## 11. Updated highest-value gate

On the compact-jet critical lane, the hard survivor is now

\[
\boxed{
\text{precharged low-amplitude director geometry imported through remote shells}
+
\text{critical }1/R\text{ velocity bath}.
}
\]

Local strain cannot regenerate the order-one director Jacobian there.

The next calculation must therefore attack the **incoming precharged geometry** itself.
The natural question is whether an infinite sequence of incoming order-one director-area tubes with amplitude

\[
\rho_R^2\sim R^{-1}
\]

can be embedded in one divergence-free CE-H vorticity field while satisfying the common scalar-potential equation

\[
\Delta W=\kappa W
\]

and the global Biot-Savart/pressure coupling.

Any purely amplitude-weighted `L2` or palinstrophy budget remains too weak because its per-shell cost is geometrically summable.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
