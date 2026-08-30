# DSD M5-306 — Detached Ancient Polynomial-Growth Descriptor and General Finite-Energy Visibility Shield

Date: 2026-08-30

Parents:
- `DSD_M5_282_DETACHED_SATELLITE_INHERITANCE_AND_FIFTH_ROOT_ENERGY_VISIBILITY_AUDIT_2026-08-30.md`
- `DSD_M5_305_PARENT_CAMPANATO_AGGREGATE_MONOPOLE_BOUND_AND_O_L_MINUS_ONE_MAIN_CORE_STRAIN_DECAY_2026-08-30.md`

Status: **FORMATION GROWTH-HIERARCHY AUDIT / GENERAL 3D SUBLINEAR ANCIENT LIOUVILLE IS NOT AVAILABLE AS A CLOSURE TOOL, SO DETACHED SATELLITES ARE CLASSIFIED BY THEIR LARGE-RADIUS VELOCITY GROWTH / THE FIFTH-ROOT AFFINE VISIBILITY LAW EXTENDS TO A GENERAL `R_alpha=(qE0)^{1/(2alpha+3)}` LAW FOR `|u-c|~R^alpha` GROWTH / THIS IDENTIFIES EXACTLY WHAT EXPANDING-WINDOW ANCESTRY MUST BEAT TO EXCLUDE EACH POLYNOMIAL GROWTH CLASS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why a growth descriptor is needed

M5-281 isolated detached ancient satellite limits with nonzero bounded vorticity but without an inherited global weak-`L3` bound.

M5-285 gave the exact affine countermodel

\[
u(x)=Ax
\]

(up to an appropriate pressure) showing that local bounded-vorticity compactness does not imply a Liouville contradiction.

Known sublinear-growth Liouville results are available in special classes such as 2D or axisymmetric Navier–Stokes, but not as a general 3D theorem sufficient for the present detached class.

Therefore large-radius velocity growth must be retained as an explicit Formation coordinate.

---

## 2. Mean-free polynomial growth descriptor

For an ancient detached velocity `U`, define on a time slice

\[
\boxed{
\mathcal E(R)
:=
\inf_{c\in\mathbb R^3}
\int_{B_R}|U-c|^2dy.
}
\]

For a growth exponent `alpha`, define

\[
\boxed{
\mathfrak G_\alpha(R)
:=
R^{-(2\alpha+3)}\mathcal E(R).
}
\]

A field with typical mean-free size

\[
|U-c_R|\sim R^\alpha
\]

on `B_R` has

\[
\mathcal E(R)\sim R^{2\alpha+3}
\]

and therefore `G_alpha(R)~1`.

Important examples:

- affine/linear growth: `alpha=1`, energy `~R^5`;
- bounded nonconstant growth: `alpha=0`, energy `~R^3`;
- critical `1/R` tail: formally `alpha=-1`, energy `~R`.

Thus weak-critical velocity growth sits four powers of `R` below the affine obstruction at the energy level.

---

## 3. Prelimit satellite energy budget

Let the satellite point-picking vorticity frequency be

\[
q=|\omega|^{1/2}.
\]

Under the satellite scaling

\[
\widetilde u(z)=q^{-1}u(x_*+z/q),
\]

the original finite physical kinetic energy gives the global scaled budget

\[
\boxed{
\|\widetilde u\|_2^2
\le qE_0
}
\]

(up to the repository viscosity normalization).

Therefore a detached profile exhibiting order-one `alpha`-growth through radius `R` requires

\[
\boxed{
R^{2\alpha+3}
\lesssim qE_0.
}
\]

---

## 4. General visibility radius

Define

\[
\boxed{
R_\alpha(q)
:=(qE_0)^{1/(2\alpha+3)}
}
\]

for `2alpha+3>0`, i.e. `alpha>-3/2`.

If the point-picking/ancestry window reaches radii

\[
R\gg R_\alpha(q),
\]

then an order-one `R^alpha` growth profile on that whole window is incompatible with the finite-energy prelimit.

Thus

\[
\boxed{
\text{visible expanding window beyond }R_\alpha
\Longrightarrow
\text{exclusion of persistent }\alpha\text{-growth}.
}
\]

For `alpha=1`,

\[
R_1=(qE_0)^{1/5},
\]

recovering the fifth-root law from M5-282.

---

## 5. Growth-shield branch

If the detached limit has nonzero `alpha`-growth but no contradiction is visible in the prelimit, then the available coherent window must remain below the corresponding visibility scale:

\[
\boxed{
A_n
\lesssim
(q_nE_0)^{1/(2\alpha+3)}.
}
\]

This is the generalized **energy-shield law**.

It does not say such a growth profile exists. It says that finite energy can only fail to see it if compactness/ancestry breaks before the required radius.

---

## 6. Relative difficulty of growth classes

The visibility exponent decreases as `alpha` increases.

- linear growth `alpha=1`: `1/5`;
- bounded growth `alpha=0`: `1/3`;
- critical `alpha=-1`: `1`.

Thus a critical weak-`L3`-type profile requires ancestry out to a much larger scaled radius than an affine profile before finite energy alone can distinguish it.

This explains why eliminating the affine obstruction is substantially easier than recovering the full critical tail class.

---

## 7. Formation split of the detached class

Define the asymptotic growth exponent schematically by the smallest `alpha` for which

\[
\mathcal E(R)\lesssim R^{2\alpha+3}
\]

along large radii.

Then

\[
\boxed{
A_{detached}
\Longrightarrow
A_{linear}
\lor A_{sublinear}
\lor A_{critical/decaying}
\lor A_{irregular-growth}.
}
\]

The known affine fixed-point obstruction sits in `A_linear`.

The desired Albritton–Barker restart regime is much closer to the critical/decaying side.

No general theorem currently collapses the whole sublinear interval in 3D.

---

## 8. Connection to harmonic strain

The local div-curl decomposition from M5-281 writes

\[
\nabla U
=\mathcal R(\chi\omega)+H,
\]

where `H` is the harmonic/remote strain component on the inner region.

Persistent linear growth corresponds naturally to a nonzero constant/slowly varying large-scale harmonic-strain component.

Thus the growth descriptor can also be viewed as a large-radius version of the `H_ambient` variable.

The ancestry target becomes:

\[
\boxed{
\text{show that nonzero harmonic affine blow-down cannot persist on windows reaching }R_1(q).
}
\]

---

## 9. Relation to main-core decoupling

M5-305 shows that remote packets contribute only `O(L^{-1})` leading strain to the original main core under parent Campanato control.

Therefore the detached growth problem cannot be solved by asking the main core to feel the remote cloud strongly.

The missing information must travel through:

- expanding-window ancestry;
- coherent restart;
- global energy/growth visibility;
- or dynamic turnover linking the satellite back to the core.

This is now explicit.

---

## 10. External-theorem firewall

Special-class results show that sublinear growth can imply Liouville rigidity in 2D or axisymmetric settings, and linear growth admits counterexamples.

Those theorems do not justify the general implication

\[
\text{sublinear 3D ancient}
\Longrightarrow
\text{constant}.
\]

Therefore this route remains conditional unless additional symmetry emerges from the Axis/Formation analysis.

---

## 11. Next target

The highest-value ancestry question is the affine level first:

\[
\boxed{
\text{Can the satellite point-picking window be upgraded from }A_n\to\infty
\text{ to }A_n/(q_nE_0)^{1/5}\to\infty?
}
\]

If yes, all nonzero affine blow-downs are excluded.

If not, the failure itself defines a quantitative compactness-shield branch that can be compared with the remote distance `q_nd_n` and Type-II clock `Theta_n`.

---

## 12. Audit verdict

### DERIVED

General visibility radius

\[
\boxed{R_\alpha=(qE_0)^{1/(2\alpha+3)}}.
\]

### RECOVERS

Affine fifth-root scale `R_1=(qE0)^{1/5}`.

### FIREWALL

General 3D sublinear-growth ancient Liouville is not available as a blanket closure.

### OPEN

- affine-window ancestry upgrade;
- sublinear detached rigidity;
- critical weak-`L3` restart;
- dynamic turnover;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]