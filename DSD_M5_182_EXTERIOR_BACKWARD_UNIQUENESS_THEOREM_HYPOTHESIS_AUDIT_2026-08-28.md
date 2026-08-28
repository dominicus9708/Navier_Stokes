# DSD M5-182 — Exterior Backward-Uniqueness Theorem Hypothesis Audit

Date: 2026-08-28

Status: **W1-CONDITIONAL / PHYSICAL EXTERIOR REDUCTION GREEN / DIRECT EXTERNAL-THEOREM INSERTION YELLOW / NO BACKWARD-UNIQUENESS THEOREM IS COUNTED AS APPLIED UNTIL THE VELOCITY–PRESSURE OR VORTICITY–VELOCITY COUPLING AND ARTIFICIAL-BOUNDARY ISSUES ARE RESOLVED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Audited physical pair

Let `V,W` be same-tail states in the compact minimal W1 set and let `u^V,u^W` be their inverse-Leray physical realizations near the same terminal point `(x_*,T_*)`.

Set

\[
Z:=u^V-u^W,
\qquad q:=p^V-p^W.
\]

Then on every fixed exterior region

\[
\Omega_R:=\{x:|x-x_*|>R\},
\]

M5-145 and M5-181 give

\[
\boxed{
\partial_t^m Z(x,T_*)=0
\quad\forall m\ge0,\ x\in\Omega_R.
}
\]

In particular

\[
\boxed{Z(\cdot,T_*)=0\quad\text{on }\Omega_R.}
\]

The relative velocity-pressure system is

\[
\boxed{
\partial_t Z-\nu\Delta Z
+(u^V\!\cdot\nabla)Z
+(Z\!\cdot\nabla)u^W
+\nabla q=0,
\qquad \nabla\cdot Z=0.
}
\]

On every fixed `Omega_R`, the common tail estimates give uniform bounds up to `T_*` for `u^V,u^W` and all spatial derivatives needed below.

---

## 2. Hypothesis table

### H1 — terminal zero on the fixed exterior

**GREEN.**

The same-tail all-orders Fuchsian/Taylor equality gives exact terminal equality on every fixed punctured exterior region.

### H2 — smoothness and bounded lower-order coefficients on the fixed exterior

**GREEN.**

The Type-I singular scale is confined to the shrinking center.  For fixed `R>0`, the physical tail estimates give

\[
|\nabla_x^k u^{V,W}(x,t)|\le C_{k,R}
\]

for `t` sufficiently close to `T_*` and `x in Omega_R`.

Thus the Oseen coefficients in the relative velocity system are uniformly bounded on each fixed exterior cylinder.

### H3 — acceptable spatial growth at infinity

**GREEN.**

The W1 tail is `O(|x|^-1)` at the velocity level and the same-tail difference is stronger.  This is far below the Gaussian-growth allowances appearing in heat-type backward-uniqueness results.

### H4 — equality of traces on the artificial boundary `|x-x_*|=R`

**NOT AVAILABLE / YELLOW.**

`Omega_R` is an artificial cut, not a physical obstacle domain.  Same-tail equality at infinity and terminal equality do not imply

\[
Z|_{|x-x_*|=R}=0
\]

for all earlier times.

Therefore any exterior Navier–Stokes theorem whose formulation requires identical Dirichlet/no-slip data on the obstacle boundary cannot be inserted without an additional lemma.

### H5 — direct ESS-type scalar/vector heat inequality for relative vorticity

Let

\[
\eta:=\nabla\times Z.
\]

Then

\[
\begin{aligned}
\partial_t\eta-\nu\Delta\eta
&+(u^V\cdot\nabla)\eta-(\eta\cdot\nabla)u^V\\
&+(Z\cdot\nabla)\omega^W-(\omega^W\cdot\nabla)Z=0.
\end{aligned}
\]

The first two lower-order terms are local in `eta`, but the last two contain `Z` and `grad Z`.

A pointwise estimate

\[
|\partial_t\eta-\nu\Delta\eta|
\le C_R(|\eta|+|\nabla\eta|)
\]

has **not** been established from the present hypotheses because recovering `Z` from `eta` on an artificial exterior has a nonlocal/harmonic component.

Hence direct insertion of the Escauriaza–Seregin–Sverak heat-type backward-uniqueness theorem is **YELLOW**.

### H6 — nonstationary Stokes unique continuation without boundary conditions

Boulakia-type nonstationary Stokes Carleman results establish interior/boundary unique continuation and logarithmic stability without imposing boundary conditions in the continuation statement.

However the audited statements propagate vanishing from a spacetime open set or Cauchy data; they are not, as presently recovered, a theorem saying that terminal velocity zero on an exterior cylinder implies backward zero for the generalized Oseen–Stokes pair.

Therefore these results are **relevant but insufficient as a direct terminal-backward theorem**.

### H7 — generalized nonstationary Stokes strong unique continuation

Lin–Wang-type results treat generalized nonstationary Stokes systems with lower-order coefficients and give quantitative spatial vanishing-order / strong unique continuation results involving the velocity.

Their proved continuation direction is spatial vanishing, not the missing terminal-time backward propagation.

Thus this route is **YELLOW** rather than a completed bridge.

### H8 — Straughan exterior Navier–Stokes backward uniqueness

The classical paper

`Backward uniqueness and unique continuation for solutions to the Navier-Stokes equations on an exterior domain`, J. Math. Pures Appl. 62 (1983), 49–62

is a directly relevant precedent.

However the exact theorem statement and all boundary/solution-class hypotheses have not been recovered at sufficient fidelity in the present audit.  In particular we do not assume that a theorem formulated for a physical exterior obstacle can be transferred to the artificial cut `Omega_R`.

Therefore **the theorem is not counted as applied**.

---

## 3. DSD classification

### Formation — GREEN

The physical exterior pair, its terminal data, and all coefficients are actual objects already produced by the W1 construction.

### Axis — GREEN

The physical terminal-time direction is kept separate from the previous Fuchsian normal direction and from spatial unique continuation.

### Static aggregation — GREEN

Multiple unique-continuation theorems are not combined as if their hypotheses were interchangeable.

### Dynamics — YELLOW

The exact terminal-backward propagation lemma for the coupled velocity-pressure system is still missing.

### Cross-audit — GREEN

No theorem title is used as a substitute for a verified theorem-hypothesis match.

---

## 4. RED theorem shortcuts

The following implications are forbidden:

1. `Straughan title mentions exterior Navier-Stokes => current artificial exterior pair satisfies the theorem` — RED.
2. `Boulakia gives Stokes unique continuation without boundary conditions => terminal backward uniqueness` — RED.
3. `Lin-Wang strong unique continuation in space => backward uniqueness in time` — RED.
4. `eta determines Z globally => pointwise local ESS inequality` without treating the exterior harmonic component — RED.
5. `terminal C-infinity flatness => terminal analyticity` — RED.

---

## 5. Exact internal lemma that would close both flat branches

It is enough to establish the following boundary-condition-free exterior Oseen–Stokes backward-uniqueness statement.

### Target BU-OS

Let `Omega_R={|x-x_*|>R}` and let `(Z,q)` be smooth on

\[
\Omega_R\times(t_0,T_*]
\]

with

\[
\nabla\cdot Z=0,
\]

and

\[
\partial_tZ-\nu\Delta Z+A(x,t)\cdot\nabla Z+B(x,t)Z+\nabla q=0.
\]

Assume

\[
A,B\in L^\infty,
\]

sufficient local regularity for the Stokes pressure, sub-Gaussian spatial growth, and

\[
Z(\cdot,T_*)=0\quad\text{in }\Omega_R.
\]

No boundary value on `|x-x_*|=R` is prescribed.

Prove

\[
\boxed{Z\equiv0\quad\text{on }\Omega_R\times(t_0,T_*].}
\]

If BU-OS is GREEN for the actual coefficient class, then for every same-tail pair `V,W` and every `R>0` the physical difference vanishes on an exterior open set.  Spatial analyticity at any regular Leray time then gives

\[
V=W.
\]

This would eliminate **both** statistical and proximal flat fibers:

\[
\boxed{P1_B^S=P1_B^P=\varnothing.}
\]

---

## 6. Current frontier

Until BU-OS is proved or matched to an existing theorem, the physical exterior route is

\[
\boxed{
\text{terminal-zero reduction: GREEN}
\quad\to\quad
\text{boundary-free Oseen-Stokes backward uniqueness: YELLOW}.
}
\]

The internal spectral-infinity action route remains independent and open.

All statements remain W1-conditional.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
