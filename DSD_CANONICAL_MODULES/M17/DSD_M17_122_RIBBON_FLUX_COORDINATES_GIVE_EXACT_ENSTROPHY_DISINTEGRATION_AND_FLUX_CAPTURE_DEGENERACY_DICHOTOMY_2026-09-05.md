# DSD M17-122 — Ribbon flux coordinates give exact enstrophy disintegration and a flux-capture degeneracy dichotomy

Date: 2026-09-05
Canonical ID: **M17-122**

Status: **EXACT FLUX DISINTEGRATION / ON A REGULAR PURE-KERNEL RANK-TWO RIBBON BUNDLE, DIRECTOR-AREA FLUX COORDINATES GIVE `dV=dPhi_J ds/|J_xi|`. HENCE THE RIBBON VORTICITY ENERGY IS EXACTLY THE DIRECTOR-AREA FLUX INTEGRAL OF THE PER-TUBE WEIGHT `W_J=int rho^2/|J_xi| ds`. ON A COMPLETE CRITICAL RIBBON `L=2pi/|q|`. UNIFORM UPPER AMPLITUDE, LOWER DIRECTOR-AREA DENSITY, AND LOWER KERNEL-CIRCLE CURVATURE GIVE THE DESIRED UPPER FLUX-CAPTURE BOUND. FAILURE OF THAT BOUND, WITH AMPLITUDE STILL NORMALIZED, MUST APPEAR THROUGH DIRECTOR-AREA DEGENERATION, KERNEL-CIRCLE FLATTENING/DECOMPACTIFICATION, OR LOSS OF THE COMPLETE-RIBBON COVER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pure-kernel flux tube

Work on the regular pure-transverse-kernel Rank-2 branch

\[
J_\xi=|J_\xi|k\ne0,
\qquad
D_k\xi=0.
\]

Let `Lambda` label an infinitesimal family of `J_xi`-flux tubes and let

\[
\boxed{d\Phi_J}
\]

be the frozen director-area flux carried by a tube.
If `ds` is arc length along its kernel line, then the cross-sectional area normal to `J_xi` is

\[
dA_\perp=\frac{d\Phi_J}{|J_\xi|}.
\]

Therefore

\[
\boxed{
dV
=dA_\perp ds
=\frac{d\Phi_J\,ds}{|J_\xi|}.
}
\]

This is the exact local flux-coordinate volume element.

---

## 2. Exact vorticity-energy disintegration

Write

\[
W=\rho\xi,
\qquad |W|=\rho.
\]

For a ribbon bundle `T`,

\[
\begin{aligned}
E_T^\omega
&:=\int_T|W|^2dV\\
&=\int_\Lambda
\left[
\int_{\Gamma_\lambda}
\frac{\rho^2}{|J_\xi|}ds
\right]d\Phi_J.
\end{aligned}
\]

Define the exact per-flux enstrophy weight

\[
\boxed{
\mathcal W_J(\lambda)
:=
\int_{\Gamma_\lambda}
\frac{\rho^2}{|J_\xi|}ds.
}
\]

Then

\[
\boxed{
E_T^\omega
=\int_\Lambda\mathcal W_J(\lambda)d\Phi_J.
}
\]

Thus total director-area flux alone does not determine the enstrophy; the missing descriptor is precisely `mathcal W_J`.

---

## 3. Complete critical ribbon

On the analytic critical-ribbon branch of M17-114/M17-115,

\[
D_kk=q\,n,
\qquad
D_kq=0.
\]

For a complete nondegenerate closed kernel fiber, `q` is constant along the fiber and the fiber is a circle of radius `1/|q|`. Therefore

\[
\boxed{
L_\lambda
=\frac{2\pi}{|q_\lambda|}.
}
\]

Hence

\[
\mathcal W_J(\lambda)
=
\oint_{\Gamma_\lambda}
\frac{\rho^2}{|J_\xi|}ds.
\]

---

## 4. Uniform compact nondegeneracy gives two-sided flux capture

Suppose on the ribbon bundle

\[
0<c_\rho\le\rho\le C_\rho,
\]

\[
0<c_J\le|J_\xi|\le C_J,
\]

and

\[
0<c_q\le|q|\le C_q.
\]

Then

\[
\boxed{
\frac{2\pi c_\rho^2}{C_JC_q}
\le
\mathcal W_J(\lambda)
\le
\frac{2\pi C_\rho^2}{c_Jc_q}.
}
\]

Let

\[
\Phi_T:=\int_\Lambda d\Phi_J.
\]

Therefore

\[
\boxed{
\frac{2\pi c_\rho^2}{C_JC_q}\Phi_T
\le
E_T^\omega
\le
\frac{2\pi C_\rho^2}{c_Jc_q}\Phi_T.
}
\]

This is the exact quantitative form of ribbon flux capture on a compact nondegenerate class.

---

## 5. Critical-shell form

At first-hitting stage `j`, an age-`k` shell has similarity radius `K_k` and physical radius

\[
R_{j,k}^{phys}=r_jK_k.
\]

In similarity variables define

\[
J_{k,T}^\omega
:=K_kE_{T_k}^\omega.
\]

Then Section 4 gives

\[
\boxed{
J_{k,T}^\omega
\asymp
K_k\Phi_k
}
\]

with constants determined only by the compact ribbon bounds.

In particular,

\[
\boxed{
J_{k,T}^\omega
\lesssim K_k\Phi_k
}
\]

is no longer an extra hypothesis once the ribbon family is uniformly nondegenerate.

---

## 6. Exact failure modes of upper flux capture

Without the compact lower bounds, the exact formula shows why flux capture can fail.
Assume the normalized amplitude remains uniformly bounded above,

\[
\rho\le C_\rho.
\]

Then large `mathcal W_J` requires at least one of:

1. director-area density becomes small somewhere on the contributing tube,
   \[
   \inf_{\Gamma_\lambda}|J_\xi|\to0;
   \]
2. the complete kernel fiber becomes arbitrarily long;
3. the geometry ceases to be represented by a complete critical-ribbon fiber.

On the complete critical-ribbon class, item 2 is exactly

\[
\boxed{
|q_\lambda|\to0,
}
\]

because

\[
L_\lambda=2\pi/|q_\lambda|.
\]

Therefore the normalized complete-ribbon dichotomy is

\[
\boxed{
\text{uniform flux capture}
\ \lor\
|J_\xi|\to0
\ \lor\
|q|\to0
\ \lor\
\text{ribbon-cover exit}.
}
\]

---

## 7. Scale-invariant director-area ratio

Because physical vorticity amplitude and director-area current both scale as `r^{-2}`, define

\[
\boxed{
\eta_J:=\frac{|J_\xi|}{\rho}.
}
\]

This descriptor is invariant under the Navier–Stokes similarity rescaling.
Then

\[
\boxed{
\frac{\rho^2}{|J_\xi|}
=\frac{\rho}{\eta_J}.
}
\]

Thus under normalized upper amplitude and lower `|q|`, upper flux capture is equivalent to a lower control of `eta_J` in the relevant flux-weighted sense.

---

## 8. DSD interpretation

M17-119 used total director-area flux as the geometric carrier.
M17-122 identifies the missing measure conversion exactly:

\[
\boxed{
\text{director-area flux}
\xrightarrow{\ \mathcal W_J\ }
\text{vorticity enstrophy}.
}
\]

`mathcal W_J` is not an arbitrary comparison constant. It is a geometrically defined per-flux enstrophy density.

This prevents two descriptor substitutions:

- nonzero `J_xi` is not the same as a uniform lower bound for `|J_xi|`;
- finite director-area flux is not by itself an upper bound for vorticity energy.

---

## 9. DSD audit

### Audit A — using M17-104 as a uniform lower bound

Rejected. M17-104 proves that a nonzero `J_xi` cannot hit zero along one regular finite-time material trajectory. It does not give a stage-uniform lower bound over an infinite sequence of fresh carriers.

### Audit B — assuming complete ribbon length is uniformly bounded

Rejected unless `|q|>=c_q>0` is retained. The exact circle length is `2pi/|q|`.

### Audit C — identifying ribbon vorticity energy with the full M5 shell number

Rejected. M17-121 converts the total M5 Dirichlet stack to a total vorticity stack, but a separate branch-allocation argument is still needed to show which director class carries its divergent portion.

### Audit D — proof status

Uniform nondegenerate ribbon bundles satisfy the desired flux-capture estimate. The remaining issue is whether the divergent M5 vorticity stack is carried by such bundles, or escapes through `J_xi` degeneration, `q` flattening, another director branch, or interfaces.

---

## 10. Updated frontier

For the Rank-2 complete-ribbon contribution,

\[
\boxed{
R_2^{ribbon}
\Longrightarrow
F_{capture}^{nondeg}
\ \lor\
D_J^{area-degeneration}
\ \lor\
D_q^{kernel-flattening}
\ \lor\
T_{ribbon-cover}.
}
\]

On `F_capture^{nondeg}`,

\[
\boxed{
J_{k,ribbon}^\omega\asymp K_k\Phi_k.
}
\]

The next target is to determine how the divergent total vorticity critical stack from M17-121 must distribute among the finite director-geometry branches and whether repeated flux-capture failure forces accumulation on the already isolated Rank-1/interface classes.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
