# DSD M5-235 — Recurrent Radial-Strain Identity and Radial/Strain Branch Merger

Date: 2026-08-30

Parent: `DSD_M5_234_PRESSURE_PAYER_SPHERICAL_HODGE_AND_H2_COEFFICIENT_FORK_2026-08-30.md`

Status: **POSITIVE STRUCTURAL MERGER / FOR A DEGREE `-1` RECURRENT CRITICAL TAIL THE RADIAL NORMAL STRAIN COEFFICIENT IS `Phi_{r,y}-Phi_r`, AND TRANSLATION-INVARIANT AVERAGING KILLS THE CROSS TERM EXACTLY / RADIAL VELOCITY THEREFORE CANNOT BE HIDDEN BY LOG-RADIAL DERIVATIVE CANCELLATION / A RADIAL-TRANSPORT PAYER FORCES A FIXED RECURRENT STRAIN-ENERGY FLOOR / THE PREVIOUS RADIAL AND STRAIN LARGE-COEFFICIENT BRANCHES CAN BE MERGED AT THE LEVEL OF STRAIN AMPLITUDE, THOUGH NOT AT THE LEVEL OF SIGNED COMPRESSIVE ALIGNMENT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Degree `-1` radial normal strain

Let

\[
T(r\theta)=r^{-1}\Phi(y,\theta),
\qquad y=\log r,
\]

and denote the radial velocity coefficient by

\[
\Phi_r:=\Phi\cdot\theta.
\]

The physical radial velocity is

\[
T_r=r^{-1}\Phi_r.
\]

For any smooth vector field, the radial-normal component of the symmetric strain is

\[
e_r^TS(T)e_r=\partial_rT_r.
\]

Hence

\[
\partial_r(r^{-1}\Phi_r)
=
r^{-2}(\partial_y\Phi_r-\Phi_r).
\]

Define the scale-normalized radial strain coefficient

\[
\boxed{
\Sigma_{rr}(y,\theta)
:=
r^2e_r^TS(T)e_r
=
\partial_y\Phi_r-\Phi_r.
}
\]

This identity is exact.

---

## 2. Translation-invariant mean removes the cross term

The compact minimal tail hull carries invariant probability measures for the log-translation flow. Equivalently, the same calculation may be made with long Følner averages in `y`.

For the bounded smooth observable

\[
|\Phi_r|^2,
\]

translation invariance gives

\[
\boxed{
\left\langle
\partial_y|\Phi_r|^2
\right\rangle
=0.
}
\]

Thus

\[
\boxed{
\left\langle
\Phi_r\partial_y\Phi_r
\right\rangle
=0.
}
\]

Expand the radial strain square:

\[
|\Sigma_{rr}|^2
=
|\partial_y\Phi_r|^2
+|\Phi_r|^2
-2\Phi_r\partial_y\Phi_r.
\]

After spherical and invariant-log averaging,

\[
\boxed{
\left\langle
\int_{S^2}|\Sigma_{rr}|^2d\theta
\right\rangle
=
\left\langle
\int_{S^2}
\left(
|\partial_y\Phi_r|^2
+|\Phi_r|^2
\right)d\theta
\right\rangle.
}
\]

In particular,

\[
\boxed{
\langle\|\Sigma_{rr}\|_2^2\rangle
\ge
\langle\|\Phi_r\|_2^2\rangle.
}
\]

---

## 3. Consequence: radial amplitude cannot be strain-cancelled recurrently

Pointwise one may have

\[
\partial_y\Phi_r\approx\Phi_r
\]

and hence small `Sigma_rr` over a short interval.

But maintaining this indefinitely would generate exponential behavior in `y`, incompatible with compact recurrence.

The invariant-mean identity makes this precise:

\[
\boxed{
\text{recurrent radial velocity energy}
\le
\text{recurrent radial strain energy}.
}
\]

Thus the radial branch cannot evade strain merely by tuning its log-radial derivative.

---

## 4. Quantitative input from the radial-transport payer

M5-233 gives, on a radial-paying finite dilation,

\[
\left\langle
\int|\Psi_h|^2(\Phi_h)_r
\right\rangle
\ge
\frac{2\nu}{3}\mathcal D_h.
\]

Let

\[
M_\Psi
:=
\|\Psi_h\|_{L^\infty(cyl)}.
\]

Compactness of the critical tail hull gives one finite uniform ceiling; for a finite difference one may take, safely,

\[
M_\Psi\le2M_\Phi.
\]

By Cauchy-Schwarz,

\[
\frac{2\nu}{3}\mathcal D_h
\le
\left(
\left\langle\int|(\Phi_h)_r|^2\right\rangle
\right)^{1/2}
\left(
\left\langle\int|\Psi_h|^4\right\rangle
\right)^{1/2}.
\]

Use

\[
|\Psi_h|^4
\le
M_\Psi^2|\Psi_h|^2
\]

and M5-230 coercivity

\[
\left\langle\int|\Psi_h|^2\right\rangle
\le
C_{\rm sol}\mathcal D_h.
\]

Then

\[
\frac{2\nu}{3}\mathcal D_h
\le
M_\Psi
\sqrt{C_{\rm sol}\mathcal D_h}
\left(
\left\langle\int|(\Phi_h)_r|^2\right\rangle
\right)^{1/2}.
\]

Therefore

\[
\boxed{
\left\langle\int|(\Phi_h)_r|^2\right\rangle
\ge
\frac{4\nu^2}{9M_\Psi^2C_{\rm sol}}
\mathcal D_h.
}
\]

Since translation does not change the invariant mean,

\[
\langle\|(\Phi_h)_r\|_2^2\rangle
=
\langle\|\Phi_r\|_2^2\rangle.
\]

Hence

\[
\boxed{
\langle\|\Phi_r\|_2^2\rangle
\ge
\frac{4\nu^2}{9M_\Psi^2C_{\rm sol}}
\mathcal D_h.
}
\]

Using `D_h >= d_D^*` gives a fixed nonzero floor.

---

## 5. Radial payer forces a strain-energy floor

Combine Sections 2 and 4:

\[
\boxed{
\left\langle
\int|\Sigma_{rr}|^2
\right\rangle
\ge
\frac{4\nu^2}{9M_\Psi^2C_{\rm sol}}
\mathcal D_h.
}
\]

Therefore, since

\[
|\Sigma_{rr}|\le|\mathcal S_\Phi|,
\]

one obtains

\[
\boxed{
\left\langle
\int|\mathcal S_\Phi|^2
\right\rangle
\ge
\frac{4\nu^2}{9M_\Psi^2C_{\rm sol}}
\mathcal D_h.
}
\]

And hence, using the finite-dilate separation,

\[
\boxed{
\left\langle
\int|\mathcal S_\Phi|^2
\right\rangle
\ge
\frac{4\nu^2d_D^*}{9M_\Psi^2C_{\rm sol}}
>0.
}
\]

This is a genuine recurrent strain-energy certificate.

---

## 6. Relation to M5-232

M5-232's strain-negative payer gives something stronger in sign:

\[
\Psi^T\mathcal S_\Phi\Psi
\text{ has a fixed negative mean,}
\]

so the relative mode aligns with compression.

M5-235 shows that even if the negative payment is assigned to the radial-transport channel rather than directly to strain, the underlying recurrent tail still carries a fixed **strain amplitude**.

Thus the two branches merge as

\[
\boxed{
S_C\lor R_C
\Longrightarrow
\text{large recurrent critical strain amplitude},
}
\]

with the additional sublabels

\[
S_C:
\text{compressive relative-mode alignment},
\]

\[
R_C:
\text{outward scale-phase locking}.
\]

The sign/correlation information remains different, so the sublabels are not erased.

---

## 7. Trace-free consequence

The physical strain is trace free. Therefore any nonzero strain matrix has both nonpositive and nonnegative spectral directions unless it vanishes.

The recurrent strain floor therefore implies simultaneous extensional/compressive spectral content in the broad sense.

However it does **not** by itself imply

\[
\lambda_2>0
\]

or the Betchov source-favorable `(-2,1,1)` shape.

Hence

\[
\boxed{
\text{large strain amplitude}
\not\Rightarrow
\text{positive-middle/Betchov branch}
}
\]

without an additional eigenvalue-shape lemma.

---

## 8. DSD verdict

### PROVED

- exact recurrent radial-strain identity;
- radial velocity energy cannot hide behind `partial_y Phi_r` cancellation in invariant mean;
- radial-transport payment forces fixed recurrent strain energy;
- `S_C` and `R_C` merge at the amplitude level.

### STILL DISTINCT

- `S_C`: signed compressive alignment;
- `R_C`: outward-sector scale-phase locking.

### UPDATED LARGE-STATIONARY FRONTIER

The M5-234 endpoint may now be compressed to

\[
\boxed{
\text{large recurrent strain}
\lor
H2_{rel}
\lor
\text{large remaining critical coefficient}.
}
\]

The next calculation should determine whether the strain floor plus the fixed point-force condition controls the spherical stress charge strongly enough to force Landau-like strain shape, or whether large non-Landau strain remains a genuine stationary endpoint.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]