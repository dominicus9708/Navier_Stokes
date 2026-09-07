# DSD M17-318 — Joint `(kappa, log line-weight)` continuity turns current-covariance escape into strain-residence transport

Date: 2026-09-07  
Canonical ID: **M17-318**

Status: **JOINT MEASURE DYNAMICS / M17-317 REDUCES FAILURE OF PURE-FLUX-TO-ENSTROPHY CURRENT TRANSFER TO COVARIANCE BETWEEN THE LINE WEIGHT `w=L_rho` AND MATERIAL MULTIPLIER VELOCITY `h=D_B kappa`. M5-684 GIVES THE EXACT MATERIAL LAW `D_theta log L_rho = kappa-1/2+2 sigma_bar_rho`. PUSHING THE CURRENT MATERIAL FLUX MEASURE TO THE JOINT VARIABLES `(k,l)=(kappa,log L_rho)` GIVES THE EXACT KINETIC EQUATION `partial_theta H + partial_k J_k + partial_l J_l = k H`, WITH `J_k` THE MATERIAL KAPPA CURRENT AND `J_l` THE STRAIN-RESIDENCE LINE-WEIGHT CURRENT. THE PURE-FLUX KAPPA CURRENT IS THE `l`-MARGINAL OF `J_k`, WHILE THE ENSTROPHY-WEIGHTED CURRENT IS ITS `e^l` MOMENT. THEREFORE THE M17-317 COVARIANCE ESCAPE IS EXACTLY NONTRIVIAL JOINT `(k,l)` PHASE ORGANIZATION, AND `l` CAN MOVE RELATIVE TO `k` ONLY THROUGH `2 sigma_bar_rho-1/2` AFTER THE COMMON KAPPA AMPLIFICATION IS REMOVED. THIS DOES NOT YET EXCLUDE PHASE LOCKING, BUT IT REMOVES LINE-WEIGHT DISPERSION AS AN INDEPENDENT DEGREE OF FREEDOM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material label variables

Let `lambda` denote one retained material vortex-line/tube label with current positive oriented flux measure

\[
d\Phi_\theta(\lambda).
\]

On exact regular CE-H, M17-313/M5-600/M5-611 give line-constant scalars

\[
\boxed{
k_\lambda(\theta):=\kappa_\lambda(\theta),}
\]

and

\[
\boxed{
h_\lambda(\theta):=D_B\kappa_\lambda(\theta).}
\]

For a genuinely material vortex-line segment define the M5-684 enstrophy line weight

\[
\boxed{
L_\lambda(\theta)
:=
\int_{\Gamma_\lambda(\theta)}\rho\,ds>0.
}
\]

Set

\[
\boxed{l_\lambda:=\log L_\lambda.}
\]

---

## 2. Exact scalar ODEs on each label

M5-681 gives the current flux-weight evolution

\[
\boxed{
\partial_\theta d\Phi_\theta
=k_\lambda d\Phi_\theta.
}
\]

By definition,

\[
\boxed{
\dot k_\lambda=h_\lambda.
}
\]

M5-684 gives

\[
\boxed{
\dot l_\lambda
=r_\lambda
:=
 k_\lambda-rac12+2\bar\sigma_{\rho,\lambda},
}
\]

where

\[
\boxed{
\bar\sigma_{\rho,\lambda}
:=
\frac{\int_{\Gamma_\lambda}\sigma\rho\,ds}
{\int_{\Gamma_\lambda}\rho\,ds}.
}
\]

Thus each material label carries the finite-dimensional state

\[
(k,l)
\]

with velocities

\[
(h,r).
\]

---

## 3. Joint pushed-forward flux measure

Define

\[
\boxed{
H(k,l,\theta)
:=
\int
\delta(k-k_\lambda)
\delta(l-l_\lambda)
\,d\Phi_\theta(\lambda).
}
\]

Define the joint currents

\[
\boxed{
J_k(k,l,\theta)
:=
\int
h_\lambda
\delta(k-k_\lambda)
\delta(l-l_\lambda)
\,d\Phi_\theta,
}
\]

and

\[
\boxed{
J_l(k,l,\theta)
:=
\int
r_\lambda
\delta(k-k_\lambda)
\delta(l-l_\lambda)
\,d\Phi_\theta.
}
\]

No closure assumption `h=h(k,l)` or `r=r(k,l)` is made.

---

## 4. Exact joint continuity equation

Let `varphi(k,l)` be a smooth compactly supported test function.

Differentiate

\[
\int\varphi(k_\lambda,l_\lambda)d\Phi_\theta.
\]

Using

\[
\dot k=h,
\qquad
\dot l=r,
\qquad
\dot{d\Phi}=k\,d\Phi,
\]

we obtain

\[
\frac d{d\theta}
\int\varphi\,d\Phi
=
\int
\left(
\partial_k\varphi\,h
+
\partial_l\varphi\,r
+
 k\varphi
\right)d\Phi.
\]

Therefore, distributionally,

\[
\boxed{
\partial_\theta H
+
\partial_kJ_k
+
\partial_lJ_l
=
 kH.
}
\]

This is the exact two-variable extension of M5-681.

---

## 5. Recover the pure-flux `kappa` equation

Integrate over `l`.

Define

\[
F_\Phi(k,	heta)
:=
\int H(k,l,	heta)dl,
\]

and

\[
G_\Phi(k,	heta)
:=
\int J_k(k,l,	heta)dl.
\]

Assuming no `l`-boundary current on the retained finite population, or using compactly supported truncation and then passing to the limit,

\[
\int\partial_lJ_l\,dl=0.
\]

Hence

\[
\boxed{
\partial_\theta F_\Phi
+
\partial_kG_\Phi
=
 kF_\Phi,
}
\]

which is exactly M5-681.

---

## 6. Recover the enstrophy-weighted distribution and current

Because

\[
L_\lambda=e^{l_\lambda},
\]

the uncut material-segment enstrophy distribution is the exponential `l` moment

\[
\boxed{
F_E(k,	heta)
:=
\int e^lH(k,l,	heta)dl.
}
\]

Likewise

\[
\boxed{
G_E(k,	heta)
:=
\int e^lJ_k(k,l,	heta)dl.
}
\]

Thus pure flux and enstrophy-weighted currents are not two unrelated measures.

They are respectively the zeroth and exponential first moments in the same joint distribution.

This is the exact structural meaning of M17-317's line weight.

---

## 7. Exponential moment equation

Multiply the joint continuity equation by `e^l` and integrate in `l`.

Integration by parts gives

\[
\int e^l\partial_lJ_l\,dl
=-
\int e^lJ_l\,dl.
\]

Therefore

\[
\boxed{
\partial_\theta F_E
+
\partial_kG_E
=
 kF_E
+
R_E,
}
\]

where

\[
\boxed{
R_E(k,	heta)
:=
\int e^lJ_l(k,l,	heta)dl.
}
\]

Using the definition of `r`,

\[
R_E
=
\int
\left(
 k-rac12+2\bar\sigma_\rho
\right)
L_\lambda
\delta(k-k_\lambda)d\Phi.
\]

Hence

\[
\boxed{
R_E
=
\left(k-rac12\right)F_E
+2S_E,
}
\]

where

\[
\boxed{
S_E(k,	heta)
:=
\int
\bar\sigma_{\rho,\lambda}
L_\lambda
\delta(k-k_\lambda)d\Phi.
}
\]

Thus

\[
\boxed{
\partial_\theta F_E
+
\partial_kG_E
=
\left(2k-rac12\right)F_E
+2S_E.
}
\]

This is the no-cutoff material-segment version of the M5-688 enstrophy-weight continuity law.

---

## 8. Remove common `kappa` amplification from the line weight

M5-684 gives for the material tube flux

\[
\dot\Phi/\Phi=k.
\]

Define the relative line residence variable

\[
\boxed{
z_\lambda
:=
\log\frac{L_\lambda}{\Phi_\lambda}.}
\]

Then

\[
\boxed{
\dot z_\lambda
=
2\bar\sigma_{\rho,\lambda}-\frac12.
}
\]

This is crucial:

\[
\boxed{
\text{relative line-weight dynamics contain no }kappa.
}
\]

The multiplier `kappa` amplifies/consumes both line enstrophy weight and material flux in the same way.

Only strain residence changes their ratio.

---

## 9. Interpretation of the M17-317 covariance

M17-317's covariance is schematically

\[
\operatorname{Cov}_{k\approx0}(L,h).
\]

The joint equation shows that `L` is not an arbitrary hidden label weight.

Its logarithm evolves through

\[
\dot l
=k-rac12+2\bar\sigma_\rho,
\]

and its value relative to pure flux evolves entirely through

\[
\dot z
=2\bar\sigma_\rho-rac12.
\]

Therefore persistent cancellation of the pure negative current by line weighting requires **joint phase organization of `h` with integrated strain residence**.

The measure-mismatch escape becomes

\[
\boxed{
H_{current\ covariance}
\Longrightarrow
H_{h\text{-}strain\text{-}residence\ phase\ locking}
\lor
G_{threshold/end/repartition}.
}
\]

---

## 10. Recurrent bounded relative line weight

Suppose one same-material label remains in a compact relative-weight corridor

\[
0<c_z
\le
L_\lambda/\Phi_\lambda
\le C_z<\infty
\]

for a long interval of duration `T`.

Integrating the exact `z` law gives

\[
\left|
\int_0^T
\left(2\bar\sigma_\rho-\frac12\right)d\theta
\right|
\le
\log(C_z/c_z).
\]

Therefore

\[
\boxed{
\left\langle
\bar\sigma_\rho
\right\rangle_T
=
\frac14+O(T^{-1}).
}
\]

Thus bounded recurrent line/enstrophy weight relative to flux forces the quarter-strain residence already identified geometrically in M17-185/186.

This conclusion uses the **same material label**, not an ensemble substitution.

---

## 11. Next exact obstruction

The M17-317 non-transfer branch now requires two simultaneous properties near the zero level:

1. fixed covariance between `h` and `L`;
2. line-weight evolution compatible with
   \[
   \dot z=2\bar\sigma_\rho-rac12.
   \]

On a compact recurrent same-label family this forces the average quarter-strain condition

\[
\bar\sigma_\rho\approx\frac14
\]

while the `h` phase must remain correlated with deviations of `z`/`L` strongly enough to reverse the pure current.

The next target is therefore a joint covariance identity linking

\[
\operatorname{Cov}(h,L)
\]

to

\[
\operatorname{Cov}
\left(
 h,
2\bar\sigma_\rho-rac12
\right)
\]

or to threshold/end flux.

---

## 12. DSD audit

- The joint kinetic equation is derived on material labels before any averaging.
- `h` and strain residence are allowed to be multi-valued conditional on `(k,l)`; no scalar closure is assumed.
- Pure-flux and enstrophy measures are recovered as different moments of one joint measure.
- Boundary terms in `l` require compact/truncated support and are explicit.
- The clean line-weight law applies to material segments; Eulerian threshold segments require cutoff/end currents.
- Quarter-strain recurrence is same-label and does not replace a spatial average.
- No sign contradiction is claimed.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
