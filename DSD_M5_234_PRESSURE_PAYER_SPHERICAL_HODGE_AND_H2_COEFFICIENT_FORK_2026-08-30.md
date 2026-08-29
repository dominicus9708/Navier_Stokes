# DSD M5-234 — Pressure Payer: Spherical Hodge Reduction and H2 / Large-Coefficient Fork

Date: 2026-08-30

Parent: `DSD_M5_233_RADIAL_TRANSPORT_OUTWARD_SECTOR_LOCKING_GATE_2026-08-30.md`

Status: **POSITIVE PRESSURE REDUCTION / THE NEGATIVE PRESSURE PAYMENT IS EQUIVALENT TO A NONZERO CORRELATION WITH THE MEAN-ZERO RADIAL RELATIVE MODE / SPHERICAL HODGE INVERSION CONVERTS IT INTO A TANGENTIAL PRESSURE-GRADIENT PAYMENT / IF PRESSURE PAYS ONE THIRD OF THE EXACT VISCOUS BALANCE THEN ITS TANGENTIAL GRADIENT HAS A FIXED L2 LOWER BOUND RELATIVE TO THE CELL DISSIPATION / THE TANGENTIAL RELATIVE EQUATION THEN ROUTES THIS TO EITHER A SECOND-DERIVATIVE H2 MODE OR A LARGE CRITICAL BACKGROUND-COEFFICIENT MODE / PRESSURE IS THEREFORE NOT A FREE FOURTH ENDPOINT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Pressure branch

Assume the pressure branch in the sharpened M5-232 trichotomy:

\[
\boxed{
\mathcal N_p
=-
\left\langle
\int_{S^2}
\pi\Psi_r\,d\theta
\right\rangle
\le
-\frac{\nu\mathcal D}{3}.
}
\]

Thus

\[
\boxed{
\left\langle
\int_{S^2}
\pi\Psi_r\,d\theta
\right\rangle
\ge
\frac{\nu\mathcal D}{3}.
}
\]

Here `Psi_r` denotes the **radial component** of the finite-dilate relative profile, not a radial derivative.

---

## 2. Zero spherical mean of the radial relative mode

Both stationary tails have zero spherical mass flux, hence

\[
\int_{S^2}(\Phi_h)_r\,d\theta
=
\int_{S^2}\Phi_r\,d\theta
=0.
\]

Therefore

\[
\boxed{
\int_{S^2}\Psi_r(y,\theta)d\theta=0
}
\]

for every `y`.

This permits exact inversion of the spherical Laplacian on `Psi_r`.

---

## 3. Spherical Hodge potential

For each `y`, let `chi(y,.)` be the unique zero-mean solution of

\[
\boxed{
-\Delta_{S^2}\chi
=
\Psi_r.
}
\]

Since the first nonzero scalar eigenvalue of `-Delta_(S2)` is `2`, spectral calculus gives

\[
\boxed{
\|\nabla_{S^2}\chi\|_{L^2(S^2)}
\le
\frac1{\sqrt2}
\|\Psi_r\|_{L^2(S^2)}.
}
\]

Integration by parts on the sphere yields

\[
\int_{S^2}\pi\Psi_r
=
\int_{S^2}
\nabla_{S^2}\pi\cdot\nabla_{S^2}\chi.
\]

Hence

\[
\boxed{
\mathcal N_p
=-
\left\langle
\int
\nabla_S\pi\cdot\nabla_S\chi
\right\rangle.
}
\]

Pressure has been converted from a scalar radial correlation to a tangential gradient correlation.

---

## 4. Pressure payer forces a tangential-gradient floor

By Cauchy-Schwarz in the invariant cell mean,

\[
\left|
\left\langle
\int
\nabla_S\pi\cdot\nabla_S\chi
\right\rangle
\right|
\le
\frac1{\sqrt2}
\mathcal P_\tau\,
\mathcal R_\Psi,
\]

where

\[
\mathcal P_\tau
:=
\left(
\left\langle
\int_{S^2}|\nabla_S\pi|^2
\right\rangle
\right)^{1/2},
\]

and

\[
\mathcal R_\Psi
:=
\left(
\left\langle
\int_{S^2}|\Psi_r|^2
\right\rangle
\right)^{1/2}.
\]

Since the radial component is controlled by the full cell field and M5-230 coercivity,

\[
\mathcal R_\Psi^2
\le
\left\langle\int|\Psi|^2\right\rangle
\le
C_{\rm sol}\mathcal D.
\]

Thus the pressure payment implies

\[
\frac{\nu\mathcal D}{3}
\le
\frac{\sqrt{C_{\rm sol}}}{\sqrt2}
\mathcal P_\tau\sqrt{\mathcal D}.
\]

Cancel `sqrt(D)`:

\[
\boxed{
\mathcal P_\tau
\ge
\frac{\sqrt2\,\nu}
{3\sqrt{C_{\rm sol}}}
\sqrt{\mathcal D}.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\int|\nabla_S\pi|^2
\right\rangle
\ge
\frac{2\nu^2}{9C_{\rm sol}}
\mathcal D.
}
\]

So a pressure-paying branch must carry a critical tangential pressure-gradient energy of the same order as viscosity.

---

## 5. Autonomous cylinder form of the tangential relative equation

Because

\[
U=D_hT,
\qquad
V=T,
\qquad
W=r^{-1}\Psi,
\qquad
q=r^{-2}\pi,
\]

the degree bookkeeping converts the stationary relative equation into an autonomous cylinder system.

Its tangential component has the structural form

\[
\boxed{
\nabla_S\pi
=
\nu\,\mathcal V_2[\Psi]
+
\mathcal C_1[\Phi_h,\Phi;\Psi],
}
\]

where:

- `V_2` is a fixed linear second-order cylinder operator in `partial_y` and spherical derivatives;
- `C_1` is first order in `Psi`, with coefficients formed from `Phi_h`, `Phi`, and their first cylinder derivatives;
- all geometric lower-order coefficients are fixed universal constants.

No third derivative of `Psi` is present.

---

## 6. Define the H2 cell energy

Set

\[
\boxed{
\mathcal K
:=
\left\langle
\int_{S^2}
\left(
|\Psi_{yy}|^2
+|\nabla_S\Psi_y|^2
+|\nabla_S^2\Psi|^2
\right)d\theta
\right\rangle.
}
\]

Let the compact critical tail coefficient ceiling be

\[
\boxed{
C_{tail,1}
:=
\sup_{hull}
\left(
|\Phi|+|\nabla_{cyl}\Phi|
\right).
}
\]

Standard bounded-coefficient estimates on the compact cylinder cell give constants `C2,C1` depending only on the fixed geometry such that

\[
\boxed{
\mathcal P_\tau
\le
C_2\nu\sqrt{\mathcal K}
+
C_1(1+C_{tail,1})\sqrt{\mathcal D}.
}
\]

The `L2` zeroth-order terms are absorbed into `D` using `C_sol`.

---

## 7. Exact pressure fork

Combine Sections 4 and 6:

\[
\frac{\sqrt2\nu}
{3\sqrt{C_{sol}}}
\sqrt{\mathcal D}
\le
C_2\nu\sqrt{\mathcal K}
+
C_1(1+C_{tail,1})\sqrt{\mathcal D}.
\]

Therefore at least one of two events occurs.

### P-H2: second derivative payer

For any chosen `0<eta<1`, if

\[
C_1(1+C_{tail,1})
\le
(1-\eta)
\frac{\sqrt2\nu}{3\sqrt{C_{sol}}},
\]

then

\[
\boxed{
\mathcal K
\ge
\frac{\eta^2}{C_2^2}
\frac{2}{9C_{sol}}
\mathcal D.
}
\]

Thus pressure payment forces a recurrent H2 derivative mode of fixed strength relative to the first-derivative cell energy.

### P-L: large coefficient payer

Otherwise

\[
\boxed{
C_1(1+C_{tail,1})
>
(1-\eta)
\frac{\sqrt2\nu}{3\sqrt{C_{sol}}}.
}
\]

Hence the branch lies in an explicitly large critical background-coefficient regime.

---

## 8. Pressure is not an independent endpoint

The original M5-231 trichotomy was

\[
S^-\lor R^-\lor P^-.
\]

M5-234 refines the pressure branch to

\[
\boxed{
P^-
\Longrightarrow
H2_{rel}
\lor
L_{tail,1}.
}
\]

Thus pressure does not survive as an untyped free degree of freedom.

It either creates a higher-derivative relative mode or requires coefficients already at large critical amplitude.

The pressure Poisson/CZ representation remains compatible with this result: pressure is nonlocal but is generated by the velocity pair and cannot carry the payment without a corresponding velocity/derivative structure.

---

## 9. Relation to existing H audits

The `H2_rel` branch is a normalized derivative-frequency event for the finite-dilate relative mode.

It is structurally of the same kind as the repository's H2/hyperpalinstrophy exits, but one scope distinction remains:

- existing H budgets were primarily derived for the actual first-hitting solution or its vorticity;
- `Psi` is a difference of two dilates of the stationary endpoint.

Therefore one still needs an inheritance lemma before charging `K` directly to a finite prelimit H budget.

The present note does **not** silently identify those two objects.

---

## 10. DSD verdict

### PROVED

Pressure payer implies the quantitative floor

\[
\boxed{
\|\nabla_S\pi\|_{L^2(mean)}^2
\ge
\frac{2\nu^2}{9C_{sol}}\mathcal D.
}
\]

It then splits into

\[
\boxed{
H2_{rel}
\lor
\text{large critical coefficient}.
}
\]

### CORRECTED

Pressure remains sign-indefinite, but it is no longer an independent unstructured endpoint.

### OPEN

Transfer of the relative H2 payment back to a finite-stage H budget, and arbitrary-large coefficient exclusion.

---

## 11. Updated stationary negative-payment frontier

After M5-232--234, the large fixed-force stationary endpoint requires at least one of:

\[
\boxed{
\begin{aligned}
&S_C:\quad
\text{large compressive strain + relative-mode alignment},\\
&R_C:\quad
\text{large outward radial sector + scale-phase locking},\\
&P_H:\quad
\text{relative H2 derivative payment},\\
&P_L:\quad
\text{large critical background coefficient}.
\end{aligned}
}
\]

The next high-leverage calculation is to determine whether the first two large-coefficient branches can be merged by incompressibility/strain kinematics, leaving only **large derivative/large coefficient** as one common certificate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]