# DSD M5-207 — Transverse Matrix-Metric Curvature Freedom Firewall

Date: 2026-08-29

Parent: `DSD_M5_206_L1_VORTICITY_MODE_RECONSTRUCTION_AND_NONLINEAR_NSE_EXCLUSION_AUDIT_2026-08-29.md`

Status: **ANTI-PROOF FIREWALL / THE CHARACTERISTIC MATRIX-SYMMETRIZER EQUATION IS FIRST ORDER ALONG THE CRITICAL DRIFT AND DOES NOT CONTROL TRANSVERSE SECOND DERIVATIVES OF THE METRIC / EVEN WITH ZERO RADIAL OBSTRUCTION, IDENTITY FLOQUET MONODROMY, UNIT DETERMINANT, AND UNIFORM ELLIPTICITY, ONE CAN BUILD SMOOTH EXACT CHARACTERISTIC SYMMETRIZERS WITH `||Delta_S H||_infinity -> infinity` / THEREFORE ELLIPTIC MONODROMY CANNOT BY ITSELF CONTROL THE DIFFUSION COMMUTATOR IN M5-205 / ANY LOCAL MATRIX CARLEMAN METHOD NEEDS AN INDEPENDENT TRANSVERSE-REGULARITY CONSTRUCTION OR A NONLOCAL METRIC / GLOBAL REGULARITY UNPROVED.**

---

## 1. First-order character of the symmetrizer equation

The full-gradient determinant-one metric equation has the form

\[
(a\cdot D)G_H
=
-G_H\mathcal G
-
\mathcal G^TG_H.
\]

For fixed coefficients, this equation propagates metric data **along characteristics of `a`**.

It does not contain transverse elliptic derivatives of `G_H`.

Thus specifying `G_H` on one transversal determines it along the flow, but the variation of that initial data across the transversal is not controlled by the characteristic ODE alone.

This already suggests that Floquet control is insufficient for the `Delta H` term from M5-205.

---

## 2. Abstract favorable transport model

Use spherical coordinates and take the purely azimuthal Killing transport

\[
\boxed{a=\partial_\varphi.}
\]

Then

\[
\operatorname{div}_{S^2}a=0,
\qquad
\Phi_r=0.
\]

Take the simplest full-gradient cocycle

\[
\boxed{\mathcal G=0.}
\]

The exact determinant-one symmetrizer equation reduces to

\[
\boxed{
\partial_\varphi H=0.
}
\]

Every smooth axisymmetric positive metric is therefore an exact symmetrizer.

Each characteristic is a latitude circle with identity monodromy.

This is deliberately an abstract coefficient model: its role is to test what follows from characteristic/Floquet structure alone, not to claim an NSE realization with `G=0`.

---

## 3. High-frequency transverse metric family

Let

\[
P_N(z)
\]

be the degree-`N` Legendre polynomial and fix

\[
0<\varepsilon<1.
\]

Set

\[
\boxed{
f_N(\theta)
:=
\varepsilon P_N(\cos\theta).}
\]

Define the Cartesian matrix field

\[
\boxed{
H_N(\theta)
:=
\begin{pmatrix}
 e^{f_N(\theta)}&0&0\\
 0&e^{-f_N(\theta)}&0\\
 0&0&1
\end{pmatrix}.
}
\]

Because `f_N` is axisymmetric,

\[
\boxed{
\partial_\varphi H_N=0.}
\]

Hence every `H_N` solves the exact characteristic symmetrizer equation in the model.

---

## 4. Unit determinant and uniform ellipticity

The determinant is exactly

\[
\boxed{\det H_N=1.}
\]

The classical Legendre bound on `[-1,1]` is

\[
|P_N(z)|\le1.
\]

Thus

\[
|f_N|\le\varepsilon.
\]

Therefore all eigenvalues of `H_N` lie in

\[
[e^{-\varepsilon},e^{\varepsilon}].
\]

Hence

\[
\boxed{
e^{-\varepsilon}I
\le H_N\le
e^{\varepsilon}I
}
\]

uniformly in `N`.

So the family has

- exact symmetrization;
- identity monodromy;
- zero radial determinant defect;
- determinant one;
- uniform positive ellipticity.

---

## 5. Spherical metric curvature grows without bound

Legendre harmonics satisfy

\[
\boxed{
-\Delta_{S^2}P_N(\cos\theta)
=N(N+1)P_N(\cos\theta).}
\]

Thus

\[
\Delta_S f_N
=-\varepsilon N(N+1)P_N(\cos\theta).
\]

For the first diagonal entry,

\[
\Delta_S e^{f_N}
=e^{f_N}
\left(
\Delta_Sf_N+|\nabla_Sf_N|^2
\right).
\]

For the second,

\[
\Delta_S e^{-f_N}
=e^{-f_N}
\left(
-\Delta_Sf_N+|\nabla_Sf_N|^2
\right).
\]

At the north pole,

\[
P_N(1)=1,
\qquad
\nabla_SP_N=0.
\]

Therefore

\[
\left|
\Delta_S e^{f_N}
\right|_{\theta=0}
=
 e^\varepsilon\varepsilon N(N+1).
\]

Hence

\[
\boxed{
\|\Delta_SH_N\|_{L^\infty(S^2)}
\ge
 e^\varepsilon\varepsilon N(N+1)
\to\infty.
}
\]

The metric curvature diverges quadratically while ellipticity and monodromy remain perfectly controlled.

---

## 6. First metric derivatives also become large

Likewise

\[
\nabla_SH_N
\]

contains the factor

\[
\nabla_Sf_N,
\]

whose natural size grows with spherical frequency.

Thus the first-derivative quadratic commutator from M5-205,

\[
\sum_\mu
(\partial_\mu H)H^{-1}(\partial_\mu H),
\]

also cannot be controlled by ellipticity and monodromy alone.

So both equivalent diffusion formulations fail at the same structural point.

---

## 7. Why determinant normalization does not rescue the method

One might try to remove scalar transverse freedom by imposing

\[
\det H=1.
\]

The family `H_N` already has determinant one.

Therefore the bad transverse curvature is not merely a scalar determinant gauge artifact.

It lives in the anisotropic determinant-one metric sector itself.

Hence

\[
\boxed{
\det H=1
+
\text{elliptic monodromy}
\not\Longrightarrow
\text{bounded metric curvature}.
}

---

## 8. General transversal-data interpretation

For a first-order characteristic equation, pick a transversal `Sigma_0` to the flow of `a`.

The metric on `Sigma_0` is free initial data subject to positivity and any algebraic normalization.

The cocycle propagates this data along characteristics but does not smooth it transversely.

Thus arbitrarily oscillatory smooth transverse data remain arbitrarily oscillatory after propagation, modulo multiplication by the bounded cocycle.

This is the general mechanism behind the explicit Legendre example.

No Floquet theorem can supply missing transverse regularity because Floquet theory is itself characteristic/orbitwise.

---

## 9. Consequence for the M5-205 diffusion identity

M5-205 contains the exact term

\[
-\frac\nu2
\int W^T(\Delta_cH)W.
\]

Uniform ellipticity gives no universal estimate of the form

\[
\|\Delta_cH\|_\infty
\le C(c,C,\text{Floquet data}).
\]

The family above disproves such an implication at the abstract symmetrizer level.

Therefore the metric-curvature term cannot be absorbed merely by saying that the monodromy is elliptic or that `H` is bounded.

---

## 10. Scope: abstract no-go, not an NSE-tail counterexample

The explicit model uses

\[
a=\partial_\varphi,
\qquad
\mathcal G=0,
\]

which is not asserted to arise from one critical Navier--Stokes velocity field.

Its logical role is narrower and rigorous:

> The characteristic symmetrizer equation, incompressible determinant condition, bounded ellipticity, and Floquet classification alone do not imply the spatial metric regularity needed by the PDE diffusion estimate.

An NSE-specific relation between `a` and `G` could in principle impose more structure.

Such a relation would have to be used explicitly; it cannot be imported from the abstract matrix algebra.

---

## 11. Actual NSE coefficient relation does not look elliptic in `H`

For a critical velocity tail,

\[
a
=(-\Phi_r,\Phi_\tau)
\]

and

\[
\mathcal G
=\mathcal G(\Phi,D\Phi)
\]

are linked by first angular/log derivatives of the same profile.

Substituting this relation into

\[
(a\cdot D)H
=
\Phi_rH-H\mathcal G-\mathcal G^TH
\]

still gives a first-order nonlinear coefficient equation for `H`.

No second-order elliptic operator acting on `H` appears.

Thus there is presently no internal mechanism that would automatically upgrade characteristic control to `H^2`/`C^2` metric control.

---

## 12. Local matrix route now requires an independent construction

A usable local matrix Carleman scheme must therefore do at least one of the following:

1. prescribe `H` by an elliptic/nonlocal equation in addition to characteristic symmetrization;
2. construct `H` from a globally regular frame with explicit transverse derivative estimates;
3. use a finite-window metric whose derivative growth is balanced quantitatively by the Carleman parameter;
4. abandon pointwise matrix metrics for a pseudodifferential/nonlocal symmetrizer.

The simple strategy

\[
\text{elliptic Floquet monodromy}
\Rightarrow
\text{bounded matrix metric}
\Rightarrow
\text{good PDE energy}
\]

is therefore invalid.

---

## 13. Updated local-matrix status

The three gates of M5-205 are now joined by a fourth:

\[
\boxed{
\begin{aligned}
1.&\ \text{radial determinant cohomology},\\
2.&\ \text{full-gradient elliptic monodromy},\\
3.&\ \text{bounded positive metric},\\
4.&\ \text{independent transverse metric regularity}.
\end{aligned}
}
\]

Gate 4 does not follow from Gates 1--3.

This substantially lowers the priority of a universal local matrix symmetrizer as the generic endpoint strategy.

---

## 14. DSD verdict

### PROVED

- the matrix symmetrizer equation is characteristic-first-order and leaves transverse data uncontrolled;
- an explicit `det H=1` uniformly elliptic identity-monodromy family has arbitrarily large `Delta_S H`;
- bounded Floquet data do not control first or second metric derivatives;
- determinant normalization does not remove the obstruction;
- the M5-205 diffusion commutator therefore requires an independent PDE-level metric-regularity input.

### NOT CLAIMED

- that the explicit abstract coefficient model is an NSE critical tail;
- that no specially constructed NSE-adapted matrix metric can ever work.

### OPEN

- finite-window Carleman metrics;
- nonlocal/pseudodifferential symmetrizers;
- NSE-specific transverse regularity mechanisms;
- generic critical backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 15. Next target

The universal pointwise local-matrix route has now accumulated four independent gates and an explicit transverse-curvature firewall.

The next highest-value move is to return to **backward uniqueness itself** rather than continue designing more local metrics.

A focused audit should compare the current critical drift class

\[
|B(x,t)|\lesssim |x|^{-1},
\qquad
|\nabla B(x,t)|\lesssim |x|^{-2},
\]

with the sharpest available backward-uniqueness / unique-continuation theorems for parabolic systems with critical lower-order coefficients, especially weak-L3 / Lorentz / Morrey endpoint formulations.

The question is whether the current tail belongs to a known endpoint class that already has BU, or whether the radial critical drift is genuinely beyond the present theorem hypotheses.