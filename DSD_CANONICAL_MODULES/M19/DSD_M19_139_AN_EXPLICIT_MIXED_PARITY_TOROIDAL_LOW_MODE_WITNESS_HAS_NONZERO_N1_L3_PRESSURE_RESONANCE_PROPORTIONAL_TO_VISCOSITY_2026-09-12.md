# DSD M19-139 — An explicit mixed-parity toroidal low-mode witness has nonzero n=1,l=3 pressure resonance proportional to viscosity

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE FIRST PRESSURE-RESONANCE FUNCTIONAL OF M19-136 IS SHOWN NOT TO VANISH IDENTICALLY ON THE MIXED-PARITY LOW-MODE SPACE / AN EXPLICIT AXISYMMETRIC TOROIDAL l=1 PLUS l=2 CRITICAL DATUM PRODUCES A NONZERO l=3 ORDER-1 PRESSURE SOURCE WITH COEFFICIENT -1344 nu / 5 IN THE STATED CORRECTION CONVENTION / THE OBSTRUCTION IS VISCOUS FOR THIS WITNESS / LOG-FREE ASYMPTOTIC COMPATIBILITY REMAINS A SEPARATE GATE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Explicit divergence-free critical datum

Let

\[
r=|x|,\qquad \mu=z/r.
\]

Take the two axisymmetric toroidal homogeneous degree `-1` fields

\[
T_1
=
\left(
\frac{y}{r^2},
-\frac{x}{r^2},
0
\right),
\]

and

\[
T_2
=
\left(
\frac{6yz}{r^3},
-\frac{6xz}{r^3},
0
\right).
\]

They arise from the toroidal scalar harmonics

\[
\psi_1=\mu,
\qquad
\psi_2=3\mu^2-1.
\]

Both are divergence free.
Their antipodal parities are opposite:

\[
T_1(-x)=-T_1(x),
\qquad
T_2(-x)=T_2(x).
\]

Set

\[
\boxed{U_0=T_1+T_2.}
\]

This is a q-independent mixed-parity critical datum.

---

## 2. Leading pressure

Let `P_l(mu)` denote the Legendre polynomial of degree `l`.
The leading pressure solves

\[
-\Delta P_0
=\partial_i\partial_j(U_{0i}U_{0j}).
\]

For the above datum the pressure may be written

\[
\boxed{
P_0
=
r^{-2}
\left(
-\frac{41}{15}P_0(\mu)
-\frac{158}{21}P_2(\mu)
-\frac{12}{5}P_3(\mu)
-\frac{96}{35}P_4(\mu)
\right).
}
\]

The `l=1` coefficient is absent, in agreement with the structural M19-135 cancellation.

---

## 3. First velocity correction

Use the correction convention

\[
\boxed{
B_1
=
-\nu\Delta U_0
+(U_0\cdot\nabla)U_0
+\nabla P_0.
}
\]

An overall opposite sign convention for the correction changes the sign of the final resonance coefficient but not its nonvanishing.

The order-1 pressure stress is

\[
T^{(1)}
=
U_0\otimes B_1+B_1\otimes U_0,
\]

and the corresponding source is

\[
F_1
=
\partial_i\partial_jT^{(1)}_{ij}.
\]

---

## 4. l=3 projection

Project `F_1` on the axisymmetric degree-three harmonic

\[
P_3(\mu)
=
\frac12(5\mu^3-3\mu).
\]

Direct symbolic differentiation and exact spherical integration give

\[
\boxed{
\frac{
\displaystyle\int_{S^2}F_1(\omega)P_3(\mu)\,d\omega
}{
\displaystyle\int_{S^2}P_3(\mu)^2\,d\omega
}
=
-\frac{1344}{5}\,\nu.
}
\]

Therefore, for every

\[
\nu>0,
\]

this coefficient is nonzero.

---

## 5. The contribution is genuinely mixed-parity

For the same example, the coefficient vanishes in the formal inviscid value `nu=0` under the stated first-correction convention.

Thus the explicit nonzero moment comes from the interaction of viscosity with the mixed odd/even critical geometry.

This is consistent with M19-138:

- pure odd parity makes every odd pressure resonance vanish;
- mixing odd and even modes permits an odd resonant pressure source.

---

## 6. Consequence for the finite low-mode hard core

The first pressure-resonance functional

\[
\mathfrak M_3[A]
\]

is therefore **not identically zero** on the mixed-parity finite low-mode space.

Hence, on any finite-dimensional low-mode parameter family where the log-free asymptotic gate is imposed, the condition

\[
\boxed{\mathfrak M_3[A]=0}
\]

is a genuine proper analytic/algebraic constraint rather than a tautological identity.

Generically, mixed-parity low-mode data do not satisfy it.

---

## 7. Important firewall

This module does **not** yet eliminate the explicit witness as a possible Navier--Stokes asymptotic state.

A nonzero resonant moment may generate a polyhomogeneous correction

\[
r^{-4}\log r\,Y_3
\]

in the pressure rather than an outright contradiction.

Therefore the actual force of `M_3[A] != 0` depends on whether the certified spectator asymptotic class forbids such logarithmic corrections.
That issue must be audited before treating `M_3[A]=0` as a mandatory physical closure condition.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
