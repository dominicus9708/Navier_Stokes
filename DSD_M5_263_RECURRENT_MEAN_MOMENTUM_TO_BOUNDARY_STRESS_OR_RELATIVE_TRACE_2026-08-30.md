# DSD M5-263 — Recurrent Mean Momentum to Boundary-Stress / Relative-Trace Fork

Date: 2026-08-30

Parent: `DSD_M5_262_LOCAL_LERAY_ENERGY_CURRENT_AND_MEAN_DRIFT_FLOOR_2026-08-30.md`

Status: **EXACT MEAN-MOMENTUM REDUCTION / THE LOCAL BALL MEAN IN BACKWARD-LERAY VARIABLES SATISFIES `m'=m+b_phys+b_sim`; THE SIMILARITY GEOMETRY DOES NOT PROVIDE A FREE RECURRENT MEAN MODE, BECAUSE ITS CONSTANT-MEAN PART IS `-3m/2` / AFTER INVARIANT AVERAGING, A NONZERO MEAN-DRIFT FLOOR MUST BE PAID EITHER BY PHYSICAL MOMENTUM-STRESS CORRELATION OR BY A MEAN-FREE BOUNDARY-TRACE/GRADIENT CORRELATION / THUS THE NEW MEAN CORRIDOR FROM M5-262 REJOINS BOUNDARY TURNOVER OR DERIVATIVE/VARIANCE STRUCTURE WITHOUT USING NET CENTER DISPLACEMENT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Ball momentum

On the fixed ball `B_R`, define

\[
P_R(s):=\int_{B_R}V(Y,s)dY,
\qquad
M_R:=|B_R|=\frac{4\pi}{3}R^3,
\]

and

\[
\boxed{m_R:=P_R/M_R.}
\]

The backward-Leray equation is

\[
V_s
=\nu\Delta V
-\frac12V
-\frac12(Y\cdot\nabla)V
-(V\cdot\nabla)V
-\nabla P.
\]

---

## 2. Exact integrated momentum equation

Integrate on `B_R`.

The linear similarity term satisfies

\[
\int_{B_R}
\left[-\frac12V-\frac12Y\cdot\nabla V\right]dY
=
P_R-rac R2\int_{\partial B_R}VdS.
\]

Therefore

\[
\boxed{
P_R'
=P_R
+\int_{\partial B_R}
\left[
\nu\partial_nV
-(V\otimes V)n
-Pn
-\frac R2V
\right]dS.
}
\]

Divide by `M_R`:

\[
\boxed{
m_R'=m_R+b_{phys}+b_{sim},}
\]

where

\[
\boxed{
 b_{phys}
:=
\frac1{M_R}
\int_{\partial B_R}
\left[
\nu\partial_nV
-(V\otimes V)n
-Pn
\right]dS,
}
\]

and

\[
\boxed{
 b_{sim}
:=-\frac{R}{2M_R}
\int_{\partial B_R}VdS.
}
\]

`b_phys` is the genuine momentum-stress boundary flux. `b_sim` is deterministic similarity geometry.

---

## 3. Recurrent mean-energy identity

Take the scalar product with `m_R`:

\[
\frac12(|m_R|^2)'
=|m_R|^2+m_R\cdot b_{phys}+m_R\cdot b_{sim}.
\]

On an invariant recurrent measure,

\[
\boxed{\left\langle(|m_R|^2)'\right\rangle=0.}
\]

Hence

\[
\boxed{
\langle|m_R|^2\rangle
=-\langle m_R\cdot b_{phys}\rangle
-\langle m_R\cdot b_{sim}\rangle.
}
\]

Thus a nonzero recurrent mean cannot survive without a compensating boundary/geometric action.

---

## 4. Separate constant mean from relative boundary trace

Write

\[
V=m_R+w_R,
\qquad
\int_{B_R}w_RdY=0.
\]

Then

\[
\int_{\partial B_R}VdS
=4\pi R^2m_R
+\int_{\partial B_R}w_RdS.
\]

Since

\[
\frac{R}{2M_R}4\pi R^2=\frac32,
\]

we obtain

\[
\boxed{
 b_{sim}
=-\frac32m_R
-\frac{3}{8\pi R^2}
\int_{\partial B_R}w_RdS.
}
\]

Therefore

\[
\boxed{
-m_R\cdot b_{sim}
=
\frac32|m_R|^2
+
\frac{3}{8\pi R^2}
 m_R\cdot\int_{\partial B_R}w_RdS.
}
\]

The constant mean part of the similarity geometry is **damping**, not a free positive payer.

---

## 5. Exact recurrent correlation identity

Insert the previous formula into the recurrent mean-energy balance:

\[
\langle|m_R|^2\rangle
=
-\langle m_R\cdot b_{phys}\rangle
+
\frac32\langle|m_R|^2\rangle
+
\frac{3}{8\pi R^2}
\left\langle
m_R\cdot\int_{\partial B_R}w_RdS
\right\rangle.
\]

Rearrange:

\[
\boxed{
\left\langle m_R\cdot b_{phys}\right\rangle
-
\frac{3}{8\pi R^2}
\left\langle
m_R\cdot\int_{\partial B_R}w_RdS
\right\rangle
=
\frac12\langle|m_R|^2\rangle.
}
\]

This is the main exact identity.

---

## 6. Finite payer fork

By the triangle inequality, at least one of

\[
\boxed{
\left|\langle m_R\cdot b_{phys}\rangle\right|
\ge
\frac14\langle|m_R|^2\rangle
}
\]

or

\[
\boxed{
\frac{3}{8\pi R^2}
\left|
\left\langle
m_R\cdot\int_{\partial B_R}w_RdS
\right\rangle
\right|
\ge
\frac14\langle|m_R|^2\rangle
}
\]

must hold.

Hence the persistent mean-drift corridor from M5-262 splits into

\[
\boxed{
T_{mom-stress}
\quad\lor\quad
T_{rel-trace}.
}

---

## 7. Relative trace is controlled by gradient/variance

Use Cauchy--Schwarz on the sphere:

\[
\left|
\int_{\partial B_R}w_RdS
\right|^2
\le
4\pi R^2
\int_{\partial B_R}|w_R|^2dS.
\]

A standard trace inequality on the ball gives

\[
\int_{\partial B_R}|w_R|^2dS
\le
C_{tr}
\left[
R^{-1}\int_{B_R}|w_R|^2dY
+R\int_{B_R}|\nabla V|^2dY
\right].
\]

Since `w_R` has zero ball mean, Poincare yields

\[
\int_{B_R}|w_R|^2
\le
\frac{4R^2}{\pi^2}D_R.
\]

Therefore

\[
\boxed{
\left|
\int_{\partial B_R}w_RdS
\right|^2
\le
C_*R^3D_R
}
\]

for a universal ball trace constant `C_*`.

Consequently

\[
\boxed{
\frac{3}{8\pi R^2}
\left|
\left\langle
m_R\cdot\int_{\partial B_R}w_RdS
\right\rangle
\right|
\le
C_{R,tr}
\langle|m_R|^2\rangle^{1/2}
\langle D_R\rangle^{1/2},
}
\]

with

\[
C_{R,tr}\asymp R^{-1/2}.
\]

Thus if the relative-trace branch pays a fixed fraction of the mean tax, it forces a quantitative lower bound on local gradient/relative-variance energy.

---

## 8. Combine with the M5-262 mean floor

For `R<pi sqrt(nu)`, M5-262 gives

\[
\boxed{
\langle|m_R|^2\rangle
\ge
\frac{3j_R}{\pi R^3}.
}
\]

Hence in the physical momentum-stress branch,

\[
\boxed{
\left|\langle m_R\cdot b_{phys}\rangle\right|
\ge
\frac{3j_R}{4\pi R^3}.
}
\]

This is a strict normalized momentum-boundary correlation floor inherited from the stationary tail.

In the relative-trace branch, the same mean floor combines with the trace inequality to force a positive local derivative/variance floor.

---

## 9. Relation to existing turnover ledgers

The physical boundary term `b_phys` contains only

\[
\nu\partial_nV,
\qquad
-(V\otimes V)n,
\qquad
-Pn.
\]

These are the momentum analogues of the existing

- viscous boundary leakage;
- material/convective crossing;
- pressure boundary work.

Thus `T_mom-stress` is not a new mysterious mechanism; it is a vector momentum-stress version of the already tracked boundary turnover family.

The relative-trace branch is likewise controlled by the existing relative-variance/gradient reservoir.

---

## 10. What is not yet closed

The current result gives a positive normalized payer floor, but the repository's no-T thresholds were originally formulated mostly for scalar energy/enstrophy boundary actions, not for the signed vector correlation

\[
\langle m_R\cdot b_{phys}\rangle.
\]

Therefore one more comparison is required before declaring the stationary endpoint excluded:

\[
\boxed{
\text{momentum-stress correlation floor}
\stackrel{?}{>}
\text{existing no-T boundary-action ceiling}.
}
\]

If the scalar absolute-action bounds dominate the vector correlation, the comparison may be immediate after matching normalization. Otherwise a dedicated momentum-turnover threshold must be added.

---

## 11. DSD verdict

### PROVED

Persistent recurrent mean drift satisfies the exact finite fork

\[
\boxed{
\text{mean drift}
\Longrightarrow
T_{mom-stress}\lor T_{rel-trace}.
}
\]

### IMPORTANT CORRECTION

Similarity geometry does not let a constant local mean survive freely; its constant-mean contribution is `-3m/2` and must itself be compensated on a recurrent orbit.

### UPDATED STATIONARY BRANCH

Combining M5-260--263,

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
T_{var/bdry}
\lor
T_{mom-stress}
\lor
T_{rel-trace}.
}

All three are finite-scale boundary/relative-structure channels.

### NEXT TARGET

Compare the momentum-stress correlation with the existing **absolute-action** turnover gate, which already sums material, pressure, and viscous boundary actions without cancellation. If that gate bounds the three components in the same normalized units, `T_mom-stress` can be absorbed without inventing a new T definition.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
