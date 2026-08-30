# DSD M5-317 — Critical Screened-Rotor Saturation Anti-Model and Transition-Shell Target

Date: 2026-08-30

Parent: `DSD_M5_316_SCREENING_RADIUS_MATERIAL_COMPRESSION_AND_CONDITIONAL_DIFFUSIVE_COMMUNICATION_CLOCK_2026-08-30.md`

Status: **SHARPNESS / ANTI-PROOF AUDIT / THE EXPONENTS R~L^(1/5) AND THETA~L^(2/5) ARE SIMULTANEOUSLY SATURATED BY A SCREENED AFFINE/ROTATIONAL CORE WITH ORDER-ONE VORTICITY / PARENT MORREY ENERGY, INTERIOR GRADIENT COST, AND DIFFUSIVE COMMUNICATION ALL LIVE AT THE SAME L-SCALE / THEREFORE ENERGY+MORREY+DIFFUSION ALONE CANNOT CLOSE THE SCREENED BRANCH / THE NEXT NON-AFFINE INFORMATION MUST COME FROM THE TRANSITION VORTICITY/FLUX SHELL REQUIRED TO CONNECT THE ROTOR CORE TO A FINITE-ENERGY EXTERIOR / GLOBAL REGULARITY UNPROVED.**

---

## 1. Canonical screened rotor benchmark

Take the affine solid-rotation field

\[
u(x)=Ax,
\qquad
A^T=-A,
\]

with order-one vorticity

\[
|\omega|\sim1.
\]

Inside a ball `B_R`,

\[
|u(x)|\sim |x|.
\]

This is an exact stationary Navier--Stokes affine solution with a suitable quadratic pressure.

It is not globally finite energy, but it is the correct local anti-model for a screened detached core.

---

## 2. Kinetic energy scales like R^5

Inside `B_R`,

\[
\int_{B_R}|u|^2dx
\sim
\int_0^R r^2\,r^2dr
\sim R^5.
\]

Thus

\[
\boxed{E_{rot}(R)\asymp R^5.}
\]

M5-308/309 give the parent-Morrey satellite-frame capacity

\[
\int_{B_R}|U|^2\lesssim M L
\]

for `R<<L`.

Hence an order-one affine rotor can remain visible only while

\[
R^5\lesssim ML.
\]

Therefore

\[
\boxed{R\lesssim C(M)L^{1/5}.}
\]

The M5-309 affine-break exponent is therefore sharp against this benchmark.

---

## 3. Interior gradient cost scales like R^3

For affine rotation,

\[
\nabla u=A
\]

is constant. Thus

\[
\int_{B_R}|\nabla u|^2dx
\sim R^3.
\]

Although `Delta u=0` pointwise, a localized energy balance on `B_R` contains boundary flux terms that balance the positive interior gradient integral.

Therefore one must not incorrectly conclude that the localized viscous/dissipative ledger is zero merely because the affine field is harmonic.

---

## 4. Diffusive screening lifetime

If the affine rotor is connected to a different exterior state through a transition shell at radius `R`, then in the quiet no-pressure/no-transport-action corridor the natural communication time is

\[
\Theta_{diff}\sim R^2.
\]

During this interval, the integrated interior gradient budget has scale

\[
R^3\Theta_{diff}
\sim R^5.
\]

Thus at the maximal Morrey-visible radius

\[
R\sim L^{1/5},
\]

one has

\[
\boxed{
\Theta\sim L^{2/5},
\qquad
\int_0^\Theta\int_{B_R}|\nabla u|^2
\sim L.
}
\]

The kinetic and cumulative gradient budgets saturate the same parent-Morrey `L` scale.

---

## 5. Exact exponent matching

The three independent calculations give

\[
\boxed{
\begin{aligned}
E_{kin}&\sim R^5,\\
D_{time}&\sim R^3\Theta,\\
\Theta_{diff}&\sim R^2.
\end{aligned}
}
\]

Combining them yields

\[
D_{time}\sim R^5\sim E_{kin}.
\]

With parent capacity `~L`,

\[
\boxed{
R\sim L^{1/5},
\qquad
\Theta\sim L^{2/5}
}
\]

is the exact saturation regime.

This agrees with M5-282, M5-308, M5-309, and M5-316 from independent routes.

---

## 6. Consequence: current scalar budgets are sharp

The screened rotor demonstrates that the following information alone is insufficient to force a contradiction:

- centered Morrey kinetic capacity;
- finite physical energy ancestry;
- order-one local vorticity;
- bounded local strain/velocity after affine normalization;
- quiet diffusion over the screening radius;
- packetwise cumulative gradient cost at the corresponding natural lifetime.

All can be simultaneously saturated at the `1/5 -- 2/5` scaling.

Therefore any proof claiming contradiction from only these quantities is non-sharp.

---

## 7. What the affine rotor cannot provide globally

The exact affine rotor is not a finite-energy whole-space Navier--Stokes state.

A finite-energy realization must transition away from

\[
u=Ax
\]

at some finite radius.

Consequently there must be a transition region where at least one of the following changes:

\[
\boxed{
\text{vorticity amplitude},
\quad
\text{vorticity axis},
\quad
\text{strain/rotation ratio},
\quad
\text{affine matrix},
\quad
\text{pressure-Hessian matching}.
}
\]

This is precisely the affine-break shell from M5-309--311.

---

## 8. Transition vorticity shell is the next non-affine target

Inside the rotor,

\[
\omega\approx\omega_0\neq0.
\]

In a finite-energy far exterior, a globally persistent affine solid rotation cannot remain unchanged.

Hence the transition shell must either

1. reduce the vorticity amplitude;
2. bend/reorient the vorticity flux;
3. split into opposite-sign/returning flux populations;
4. generate a dense state-mismatch cloud as in M5-311;
5. or pay dynamic material/pressure/viscous turnover.

Thus

\[
\boxed{
C_{screened,critical}
\Longrightarrow
T_{transition}
\lor
H_{transition}
\lor
C_{dense,cancel/return}.
}
\]

---

## 9. Flux-topological observation

Since

\[
\nabla\cdot\omega=0,
\]

vorticity cannot simply terminate at the transition radius.

A rotor-like interior with a coherent vorticity axis must connect through

- return flux,
- axis bending,
- opposite signed populations,
- or diffuse redistribution.

Therefore the transition shell carries information not present in the pure affine interior anti-model.

This is the correct place to seek a non-affine, non-saturating invariant.

---

## 10. Updated target

The proof frontier should no longer attempt to beat the `R^5` energy scaling inside the screened rotor.

Instead the next target is:

> quantify the minimum transition-shell action needed to connect an order-one affine/rotational core of radius `R` to a finite-energy exterior while preserving incompressibility and `div omega=0`.

Candidate observables are

\[
\boxed{
\begin{aligned}
&\text{vorticity-flux bending/action},\\
&\text{radial/tangential axis turnover},\\
&\text{transition-shell palinstrophy},\\
&\text{pressure-Hessian mismatch},\\
&\text{return-flux multiplicity / finite-memory cost}.
\end{aligned}
}
\]

---

## 11. Audit verdict

### Established

- the `1/5` visibility exponent and `2/5` quiet lifetime exponent are jointly sharp against the affine-rotor benchmark;
- energy/Morrey/diffusion budgets alone cannot remove the screened branch;
- the finite-energy obstruction lies in the transition shell, not the affine interior.

### Open

- a quantitative lower bound for transition-shell vorticity bending/palinstrophy/return action;
- whether this transition cost is non-summable across a singular first-hitting tower;
- whether dense cancelling transition clouds reduce to previously typed H/T exits.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
