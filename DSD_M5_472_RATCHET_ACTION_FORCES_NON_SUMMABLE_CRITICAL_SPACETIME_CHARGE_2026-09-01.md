# DSD M5-472 — Recurrent ratchet action forces non-summable critical spacetime charge

Date: 2026-09-01

Status: **CRITICAL-CHARGE IDENTIFICATION / ON THE BOUNDED PARENT-SCALE ANALYTIC CORRIDOR, AN ORDER-ONE MATERIAL-AXIS RATCHET CANNOT REMAIN A ZERO-VOLUME TRAJECTORY EVENT: TILT ACTION FORCES A FIXED `L^2_t L^3_x` STRAIN CHARGE, WHILE DIRECTIONAL-DIFFUSION ACTION FORCES A FIXED `L^2_t L^(3/2)_x` VORTICITY-GRADIENT CHARGE / BOTH CHARGES ARE EXACTLY SCALE CRITICAL AND THEREFORE NON-SUMMABLE OVER A POSITIVE DENSITY OF FIRST-HITTING GENERATIONS / THIS IDENTIFIES THE TRUE CRITICAL COST BUT DOES NOT YET CONTRADICT BLOW-UP, BECAUSE THESE CRITICAL NORMS ARE ALLOWED TO DIVERGE AT A SINGULAR TIME / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input: actual material-axis ratchet

Work on an active retained material carrier with

\[
|\Omega|\ge\eta>0
\]

in first-hitting normalized variables. The exact direction equation is

\[
D_\tau\xi
=\widetilde\tau
+\frac{(I-\xi\otimes\xi)\Delta\Omega}{|\Omega|}.
\]

An order-one projective change on one selected ratchet interval `J_j` gives

\[
\boxed{
\int_{J_j}|\widetilde\tau|d\tau
+\int_{J_j}
\frac{|(I-\xi\otimes\xi)\Delta\Omega|}{|\Omega|}d\tau
\ge\delta_0.
}
\]

Therefore at least one of the two terms contributes at least `delta0/2`.

The stage lengths are bounded above by a universal normalized constant `L_*` on the retained first-hitting corridor.

---

## 2. Tilt branch: spatial coherence from bounded source-scale mass

Suppose

\[
\int_{J_j}|\widetilde\tau(X_j(\tau),\tau)|d\tau
\ge\delta_0/2.
\]

On the bounded normalized-enstrophy corridor

\[
Z_j=\|\Omega_j\|_2^2\le Z_*,
\]

M5-392 supplies uniform bounds for every fixed spatial derivative of `Omega`.

The near/far Calderon--Zygmund split applied to `grad S` then gives

\[
\boxed{
\|\nabla_Y\Sigma_j\|_\infty\le C_{S,1}(Z_*).
}
\]

Indeed the near singularity is controlled by the fixed `C^2` vorticity bound and the far field by `Z_*^(1/2)`.

Since `|Omega|>=eta` on the active carrier and `grad Omega` is uniformly bounded, the direction gradient is uniformly bounded there. Consequently

\[
\boxed{
\|\nabla_Y\widetilde\tau_j\|_\infty\le C_\tau
}
\]

on the active natural neighborhood.

If `Z_j` is not bounded, the stage is already in the genuine strong mass/delocalization branch and the present bounded-ratchet calculation is unnecessary.

---

## 3. Tilt action occupies positive space-time volume

The same bounds give a uniform pointwise ceiling

\[
|\widetilde\tau|\le T_*.
\]

From

\[
\int_{J_j}|\widetilde\tau(X_j(\tau),\tau)|d\tau\ge\delta_0/2
\]

and `|J_j|<=L_*`, choose

\[
a_0:=\frac{\delta_0}{4L_*}.
\]

There is a time set `E_j` of fixed positive measure, depending only on `delta0,L_*,T_*`, such that

\[
|\widetilde\tau(X_j(\tau),\tau)|\ge a_0
\qquad(\tau\in E_j).
\]

For each such time, the spatial Lipschitz bound gives a fixed normalized radius

\[
\rho_\tau:=\frac{a_0}{2C_\tau}>0
\]

such that

\[
|\widetilde\tau(Y,\tau)|\ge a_0/2
\]

on a ball of radius `rho_tau` around the active point, after taking a fixed component/sign on a smaller ball if necessary.

Since `|Sigma|>=|tilde tau|`,

\[
\|\Sigma(\tau)\|_{L^3_Y}^2
\ge c_0>0
\qquad(\tau\in E_j).
\]

Hence

\[
\boxed{
\int_{J_j}\|\Sigma(\tau)\|_{L^3_Y}^2d\tau
\ge c_{tilt}>0.
}
\]

---

## 4. Physical scaling of the tilt charge

At natural scale `r_j`,

\[
S_{phys}=\frac{\nu}{r_j^2}\Sigma,
\qquad
dx=r_j^3dY,
\qquad
dt=\frac{r_j^2}{\nu}d\tau.
\]

Therefore

\[
\|S_{phys}(t)\|_{L^3_x}
=\frac{\nu}{r_j}\|\Sigma(\tau)\|_{L^3_Y},
\]

and

\[
\boxed{
\int_{J_j^{phys}}\|S(t)\|_{L^3_x}^2dt
=\nu
\int_{J_j}\|\Sigma(\tau)\|_{L^3_Y}^2d\tau
\ge c_{tilt}\nu.
}
\]

The natural scale has disappeared completely.

Thus every coherent tilt-ratchet stage pays a fixed amount of the critical strain norm

\[
L^2_tL^3_x.
\]

---

## 5. Directional-diffusion branch is automatically spatially coherent

Suppose instead

\[
\int_{J_j}
\frac{|(I-\xi\otimes\xi)\Delta\Omega|}{|\Omega|}d\tau
\ge\delta_0/2.
\]

Because `|Omega|>=eta`,

\[
\int_{J_j}
|(I-\xi\otimes\xi)\Delta\Omega|d\tau
\ge\eta\delta_0/2.
\]

M5-392 gives uniform normalized bounds for `Delta Omega` and `grad Delta Omega`. Therefore the same time-set argument yields a set of fixed positive normalized time measure on which, at the active point,

\[
|\Delta\Omega|\ge b_0>0.
\]

By the `grad Delta Omega` bound, after choosing a fixed vector component `e` and shrinking to a fixed normalized ball `B_rho`,

\[
e\cdot\Delta\Omega\ge b_0/4
\]

throughout that ball.

Take a smooth nonnegative cutoff `psi` supported in the ball and equal to one on a smaller ball. Integration by parts gives

\[
\int e\cdot\Delta\Omega\,\psi
=-\int e\cdot\nabla\Omega\cdot\nabla\psi.
\]

The left side has a fixed positive lower bound. Holder with exponents `3/2` and `3` then yields

\[
\boxed{
\|\nabla\Omega(\tau)\|_{L^{3/2}_Y(B_\rho)}
\ge c_{diff}>0.
}
\]

Hence

\[
\boxed{
\int_{J_j}
\|\nabla\Omega(\tau)\|_{L^{3/2}_Y}^2d\tau
\ge c'_{diff}>0.
}
\]

No parent-scale pointwise derivative blow-up is used; the charge comes from a coherent finite derivative action.

---

## 6. Physical scaling of the directional-diffusion charge

Because

\[
\nabla_x\omega
=\frac{\nu}{r_j^3}\nabla_Y\Omega,
\]

we have

\[
\|\nabla_x\omega\|_{L^{3/2}_x}
=\frac{\nu}{r_j}
\|\nabla_Y\Omega\|_{L^{3/2}_Y}.
\]

Therefore

\[
\boxed{
\int_{J_j^{phys}}
\|\nabla\omega(t)\|_{L^{3/2}_x}^2dt
=\nu
\int_{J_j}
\|\nabla\Omega(\tau)\|_{L^{3/2}_Y}^2d\tau
\ge c'_{diff}\nu.
}
\]

Again the scale cancels exactly.

---

## 7. Both are critical regularity quantities

The tilt quantity

\[
\int\|S\|_3^2dt
\]

is invariant under Navier--Stokes scaling and is a standard Serrin-type critical strain quantity.

For the diffusion quantity, homogeneous Sobolev gives

\[
\|\omega\|_3
\lesssim
\|\nabla\omega\|_{3/2},
\]

and Calderon--Zygmund gives

\[
\|S\|_3\lesssim\|\omega\|_3.
\]

Thus finiteness of

\[
\int\|\nabla\omega\|_{3/2}^2dt
\]

also places the flow inside the same critical strain/Serrin regularity regime.

Hence both ratchet mechanisms pay genuinely critical spacetime charges.

---

## 8. Positive generation density makes the critical charge non-summable

If the projective ratchet occurs on a positive fraction of infinitely many disjoint first-hitting stages, then one of the two mechanisms occurs on a positive-density subsequence. Consequently

\[
\boxed{
\int^{T_*}
\left[
\|S(t)\|_3^2
+\|\nabla\omega(t)\|_{3/2}^2
\right]dt
=\infty.
}
\]

More quantitatively, if `N(T)` is the number of selected ratchet stages before time `T<T_*`, then

\[
\int^{T}
\left[
\|S\|_3^2
+\|\nabla\omega\|_{3/2}^2
\right]dt
\ge c\nu N(T)-O(1).
\]

Since `W_j=q^jW_0`, this is equivalently a logarithmic lower rate in the first-hitting amplitude:

\[
\boxed{
\mathcal R_{crit}(t_j)
\gtrsim
c\nu\log_q\!\frac{W_j}{W_0}.
}
\]

---

## 9. Audit firewall: non-summable does not mean contradiction

The result is stronger than the ordinary energy charge of M5-471 because the stage cost no longer carries a factor `r_j`.

However a hypothetical singular solution is permitted to make a critical regularity quantity diverge. Indeed, finiteness of the `L2_t L3_x` strain norm would itself exclude the singularity.

Therefore

\[
\boxed{
A_{ratchet}^{dens}
\Longrightarrow
\mathcal R_{crit}(T_*)=\infty
}
\]

is a genuine quantitative reduction, but not a regularity proof.

The next step must use either

1. a logarithmic/quantitative improvement showing that the first-hitting geometry cannot sustain the required divergence rate; or
2. concentration-compactness/minimal-element extraction for a solution saturating this critical ratchet budget.

---

## 10. Updated master frontier

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{amp/freq}^{strong}
\lor
A_{ratchet}^{dens},
}

with

\[
\boxed{
A_{ratchet}^{dens}
\Longrightarrow
\int^{T_*}
\left(
\|S\|_3^2
+\|\nabla\omega\|_{3/2}^2
\right)dt
=\infty.
}
\]

The remaining question is no longer whether the ratchet has a scale-critical price; it does. The question is whether this price can be sustained by a finite-energy first-hitting singular tower.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
