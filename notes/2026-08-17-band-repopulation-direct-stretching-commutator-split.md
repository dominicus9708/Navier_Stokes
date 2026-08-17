# Exact band-repopulation split: direct stretching versus scale-mixing commutators

Date: 2026-08-17

Status: **EXACT OPERATOR DECOMPOSITION. THE NONLINEAR PRODUCTION THAT REPOPULATES A GAUSSIAN/HEAT BAND HAS ONLY TWO COMPONENTS: DIRECT STRETCHING OF THE BAND VORTICITY AND SCALE-MIXING COMMUTATORS. DIRECT STRETCHING HAS A SCALE-CRITICAL `L_t^2L_x^3` STRAIN COST ON A REPOPULATION INTERVAL; THE COMMUTATOR LANE IS THE REMAINING CROSS-SCALE TRANSFER CHANNEL. GLOBAL REGULARITY NOT PROVED.**

---

## 1. Start from the exact band equation

For the positive heat-semigroup band operator

\[
Q_k=H_{a_k}-H_{a_{k-1}},
\]

the band enstrophy obeys

\[
\frac12E_k'+\nu D_k=\Pi_k,
\]

with

\[
E_k=\langle\omega,Q_k\omega\rangle,
\qquad
D_k=\langle\nabla\omega,Q_k\nabla\omega\rangle,
\]

and

\[
\Pi_k
=
\frac12\langle[(u\cdot\nabla),Q_k]\omega,\omega\rangle
+\langle(\omega\cdot\nabla)u,Q_k\omega\rangle.
\]

Let

\[
\boxed{P_k:=Q_k^{1/2}}
\]

and

\[
\boxed{\eta_k:=P_k\omega.}
\]

Then

\[
E_k=\|\eta_k\|_2^2,
\qquad
D_k=\|\nabla\eta_k\|_2^2.
\]

---

## 2. Factor the advection commutator exactly

Write

\[
A=u\cdot\nabla.
\]

Since `div u=0`, `A` is skew-adjoint on `L2`. Since `P_k` is self-adjoint,

\[
[A,P_k]^*=[A,P_k].
\]

Also

\[
[A,Q_k]
=[A,P_k^2]
=[A,P_k]P_k+P_k[A,P_k].
\]

Therefore

\[
\boxed{
\frac12\langle[A,Q_k]\omega,\omega\rangle
=
\langle[A,P_k]\omega,\eta_k\rangle.
}
\]

Thus the advective part is purely a scale-mixing commutator. If `u` were spatially constant, it would vanish exactly. For rigid rotation and a radial Gaussian/heat operator, the skew affine part also commutes after the appropriate rotating frame; the remaining affine commutator is symmetric deformation.

---

## 3. Factor the stretching term exactly

For incompressible three-dimensional flow,

\[
(\omega\cdot\nabla)u=(\nabla u)\omega=S\omega,
\]

because the antisymmetric part acts as one half of `omega cross` and hence annihilates `omega` itself.

Then

\[
\begin{aligned}
\langle S\omega,Q_k\omega\rangle
&=\langle P_k(S\omega),P_k\omega\rangle\\
&=\langle S\eta_k,\eta_k\rangle
+\langle[P_k,S]\omega,\eta_k\rangle.
\end{aligned}
\]

Hence

\[
\boxed{
\Pi_k
=
\mathcal L_k+\mathcal C_k,
}
\]

where

\[
\boxed{
\mathcal L_k
:=\langle S\eta_k,\eta_k\rangle
}
\]

is **direct stretching of the vorticity already in band `k`**, and

\[
\boxed{
\mathcal C_k
:=
\left\langle
[A,P_k]\omega+[P_k,S]\omega,
\eta_k
\right\rangle
}
\]

is the **scale-mixing commutator channel**.

No third nonlinear source remains.

---

## 4. Repopulation dichotomy inside one band

On a half-to-full band first-hitting interval `I=[t1,t2]`,

\[
E_k(t_1)=b/2,
\qquad
E_k(t_2)=b,
\]

and the exact band equation gives

\[
\boxed{
\int_I\Pi_kdt
=
\frac b4
+\nu\int_ID_kdt.
}
\]

Therefore at least one of the following holds:

### Direct-stretch lane

\[
\boxed{
\int_I\mathcal L_kdt
\ge
\frac12
\left(
\frac b4+\nu\int_ID_kdt
\right).
}
\]

### Commutator-transfer lane

\[
\boxed{
\int_I\mathcal C_kdt
\ge
\frac12
\left(
\frac b4+\nu\int_ID_kdt
\right).
}
\]

This is stronger than merely saying `Pi_k` is positive: it specifies whether the band grows mainly by stretching its own vorticity or by importing/reorganizing scale content.

---

## 5. Direct-stretch lane has a critical `L_t^2L_x^3` strain cost

By Holder,

\[
|\mathcal L_k|
\le
\|S\|_3\,\|\eta_k\|_3^2.
\]

Three-dimensional interpolation gives

\[
\|\eta_k\|_3^2
\lesssim
\|\eta_k\|_2\,\|\nabla\eta_k\|_2
=E_k^{1/2}D_k^{1/2}.
\]

On the repopulation interval,

\[
E_k\le b.
\]

Hence

\[
\int_I\mathcal L_kdt
\lesssim
b^{1/2}
\left(\int_I\|S\|_3^2dt\right)^{1/2}
\left(\int_ID_kdt\right)^{1/2}.
\]

Set

\[
A_I:=\int_I\|S\|_3^2dt,
\qquad
X:=\int_ID_kdt.
\]

On the direct-stretch lane,

\[
\frac b8+\frac\nu2X
\lesssim
b^{1/2}A_I^{1/2}X^{1/2}.
\]

Write

\[
d=\frac{\nu X}{b}.
\]

After division by `b`,

\[
\frac18+\frac d2
\lesssim
\left(\frac{A_I}{\nu}\right)^{1/2}d^{1/2}.
\]

The left/right ratio has a strictly positive minimum over `d>0`. Consequently

\[
\boxed{
A_I
=\int_I\|S(t)\|_{L_x^3}^2dt
\gtrsim c\nu.
}
\]

Thus **every direct-stretch repopulation event pays an order-one scale-critical strain action independent of the band amplitude `b` and band index `k`.**

This is a standard critical strain/vorticity regularity scale, not a new criterion by itself.

---

## 6. Why viscosity cannot erase the critical cost

Large band dissipation does not weaken the lower bound. It appears on the same side as the required enstrophy rise:

\[
\frac b4+\nu X.
\]

The optimization over `X` is exactly what leaves the fixed positive lower bound on `A_I`.

Thus the direct-stretch lane cannot evade the critical action by making the band very thin in physical space and allowing large derivative dissipation.

---

## 7. Meaning of the commutator lane

The remaining term is

\[
\mathcal C_k
=
\langle[u\cdot\nabla,P_k]\omega,\eta_k\rangle
+
\langle[P_k,S]\omega,\eta_k\rangle.
\]

Both terms vanish when the relevant coefficient is perfectly constant at the band scale.

They therefore measure precisely the cross-scale mechanisms already tracked by the DSD analysis:

- non-affine velocity increments;
- spatial modulation of the strain eigenframe/amplitude;
- high-frequency derivative content;
- transport of vorticity between neighboring/distant bands.

On the large-radius coherent branch, the rigid skew rotation commutes with the radial Gaussian/heat scale, so it cannot supply `C_k`. The surviving affine contribution is symmetric deformation, already charged by the affine strain ledger.

The next theorem needed for this lane is a vector-valued commutator packing estimate showing that repeated positive `C_k` events on moving bands force either

\[
\int\|S\|_3^2dt=\infty
\]

in a quantitatively organized way, or a derivative/scale-nonlocality ledger that cannot remain summable.

---

## 8. Revised moving-band graph

Combining persistence/repopulation with the present decomposition gives

\[
\boxed{
\text{dangerous moving band}
\to
\begin{cases}
\text{persistence }(\int E_kdt),\\
\text{direct band stretching }(\int\|S\|_3^2dt\gtrsim c\nu),\\
\text{scale-mixing commutator transfer}.
\end{cases}
}
\]

The first is paid by physical dissipation. The second is paid by a standard scale-critical strain norm. The third is now the only genuinely scale-transfer-specific wall.

Overall status: **BAND REPOPULATION CAUSALITY REDUCED TO PERSISTENCE / DIRECT CRITICAL STRETCHING / SCALE-MIXING COMMUTATOR TRANSFER / COMMUTATOR PACKING REMAINS OPEN / GLOBAL REGULARITY NOT PROVED.**