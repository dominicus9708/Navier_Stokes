# DSD M5-283 — First-Hitting Diagonal Energy Shield and Expanding-Window Reopening

Date: 2026-08-30

Parent: `DSD_M5_282_DETACHED_SATELLITE_INHERITANCE_AFFINE_ANTI_MODEL_AND_ENERGY_VISIBILITY_SPLIT_2026-08-30.md`

Status: **ANTI-PROOF CORRECTION / THE FIFTH-ROOT ENERGY-VISIBILITY SPLIT OF M5-282 IS EXACT, BUT THE ENERGY-VISIBLE SIDE CANNOT BE FORCED BY THE PRESENT ANCIENT DIAGONAL COMPACTNESS / IN FIRST-HITTING VARIABLES THE VISIBILITY RATIO CONTAINS A FACTOR `r_j^{1/5}` AND CAN BE DRIVEN TO ZERO BY TAKING THE PRELIMIT STAGE LATER / FIXED-WINDOW LOCAL CONVERGENCE THEREFORE ALLOWS AN AFFINE OR OTHER NON-WEAK-`L^3` DETACHED LOCAL LIMIT TO BE HIDDEN BEHIND AN OUTER TRANSITION SCALE TENDING TO INFINITY / A GENUINE EXPANDING-WINDOW OR COHERENT-RESTART INHERITANCE IS REQUIRED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Translate the satellite variables back to a first-hitting stage

Work in viscosity-normalized units for scaling clarity.

At first-hitting stage `j`, let

\[
r_j=W_j^{-1/2}.
\]

Suppose a remote satellite in the stage-`j` normalized variables occurs at distance

\[
R_n=|Y_n|
\]

from the tracked main core and has normalized vorticity amplitude

\[
\mu_n:=|\Omega_j(Y_n)|.
\]

Its physical vorticity-natural frequency and distance are

\[
\boxed{
q_{phys,n}
=r_j^{-1}\mu_n^{1/2},
}
\]

and

\[
\boxed{
d_{phys,n}=r_jR_n.
}
\]

Therefore the scale-invariant satellite separation parameter is

\[
\boxed{
L_n:=q_{phys,n}d_{phys,n}
=R_n\mu_n^{1/2}.
}
\]

The remote-satellite condition is

\[
L_n\to\infty.
\]

---

## 2. First-hitting form of the M5-282 visibility ratio

M5-282 defines

\[
\Xi_n
=E_0^{-1/5}q_{phys,n}^{4/5}d_{phys,n}.
\]

Substitution gives

\[
\Xi_n
=E_0^{-1/5}
(r_j^{-1}\mu_n^{1/2})^{4/5}
(r_jR_n).
\]

Hence

\[
\boxed{
\Xi_n
=E_0^{-1/5}
 r_j^{1/5}
 \mu_n^{2/5}
 R_n.
}
\]

Taking the fifth power,

\[
\boxed{
\Xi_n^5
=
\frac{r_j\mu_n^2R_n^5}{E_0}.
}
\]

Equivalently, the M5-282 shield condition becomes

\[
\boxed{
r_j\mu_n^2R_n^5\lesssim E_0.}
\]

---

## 3. Why diagonal extraction can always strengthen the shield

The historical/ancient diagonal procedure has the following order:

1. choose a finite normalized observation region or a finite remote-shell set;
2. then choose a sufficiently late first-hitting stage `j` so that the prelimit solution approximates the desired ancient object on that region.

For fixed finite `R_n` and `mu_n`, one has

\[
r_j\to0
\qquad(j\to\infty).
\]

Therefore

\[
\boxed{
\Xi_n\to0
}
\]

if the prelimit index is taken sufficiently late while the normalized satellite geometry is held fixed.

More generally, after selecting any finite normalized satellite witness `(R_n,mu_n)`, one may choose the diagonal index `j_n` sufficiently large that

\[
\boxed{
r_{j_n}\mu_n^2R_n^5\ll E_0.}
\]

provided no quantitative rate of convergence ties `j_n` to `R_n`.

The current fixed-window suitable compactness has no such quantitative rate.

Thus

\[
\boxed{
\text{finite physical energy does not force }\Xi_n\to\infty
\text{ on the ancient diagonal.}
}
\]

---

## 4. Correction to the interpretation of M5-282

M5-282 remains correct as a **conditional geometric split**:

\[
A_{detached}
\Longrightarrow
A_{visible}
\lor
S_{shield}.
\]

However the present note corrects the possible stronger reading

\[
\text{remote satellite}
\Longrightarrow
A_{visible}.
\]

That implication is RED.

The first-hitting scale factor `r_j` allows finite global energy to become invisible after blow-up normalization.

This is exactly the familiar concentration-compactness phenomenon: a sequence with finite physical energy may converge locally, after increasingly singular rescaling, to a profile whose global energy or growth is infinite.

---

## 5. Centered Morrey does not by itself repair the diagonal issue

Suppose the original main-core ancient corridor has the centered critical Morrey bound

\[
\rho^{-1}\int_{B_\rho(0)}|U|^2\le M_*.
\]

For a satellite at distance `D_n` with satellite frequency `q_n`, put

\[
L_n=q_nD_n.
\]

A satellite-centered ball of radius `cL_n` corresponds to an old-frame ball of radius `cD_n` and lies inside a fixed multiple of `B_{D_n}(0)`.

Therefore after satellite scaling one gets an outer-scale estimate

\[
\boxed{
(cL_n)^{-1}
\int_{B_{cL_n}}
|\widetilde U_n|^2
\le C M_*.
}
\]

This is useful ancestry information at the **expanding outer radius** `R~L_n`.

But fixed-window convergence only controls every fixed `R` before `n -> infinity`.

It does not imply convergence, or even uniform structural similarity, on radii increasing with `L_n`.

Hence one can still have a schematic sequence that:

- looks increasingly affine/noncritical on every fixed satellite ball;
- changes character on an intermediate radius `R_{tr,n} -> infinity`;
- satisfies the outer Morrey constraint by the time `R~L_n` is reached.

The local limit may then be affine even though no prelimit field is globally affine.

Thus

\[
\boxed{
\text{outer critical Morrey control at }R\sim L_n
\not\Rightarrow
\text{critical Morrey control of the detached local limit}
}
\]

without an expanding-window passage.

---

## 6. Exact affine anti-model remains a valid local compactness warning

The solid-rotation solution

\[
u=Ax,
\qquad A^T=-A,
\]

from M5-282 is an exact ancient Navier--Stokes solution with

\[
|\omega|\equiv\text{const}>0
\]

and linear velocity growth.

The present audit does not claim that one can truncate this field arbitrarily and retain an exact Navier--Stokes solution.

Its role is narrower and rigorous:

> the **local PDE properties inherited in M5-281** do not themselves exclude the affine ancient profile.

Any exclusion must therefore use information that survives from the approximating family on radii tending to infinity, or a restart/coherence property stronger than local convergence.

---

## 7. Relation to the old Expanding-Window Gate

Earlier in the W1 tail analysis, M5-248 showed that a **fixed local tail certificate** could be transferred back to a fixed finite RG depth without proving full expanding-window convergence.

The detached satellite problem is fundamentally different.

Here the obstruction is precisely a possible mismatch between:

\[
\text{fixed satellite windows}
\]

and

\[
\text{the expanding radius where finite-energy/Morrey ancestry becomes visible}.
\]

Therefore the earlier shortcut does not apply.

For `A_detached`, an expanding-window question genuinely reappears.

---

## 8. Two possible repairs

The detached branch can now be attacked in two conceptually different ways.

### A. Expanding-window inheritance

Prove that for some radii

\[
R_n\to\infty,
\qquad
R_n=o(L_n),
\]

the satellite-centered solutions converge/control strongly enough on `B_{R_n}` to transfer the finite-energy or centered-Morrey ancestry into the limit.

This would rule out hidden affine/noncritical transitions.

### B. Coherent restart inheritance

Avoid spatial expanding-window convergence and prove instead that at a backward sequence of satellite times the profile is a weak-`L^{3,\infty}` solution in the Barker--Seregin--Sverak sense:

\[
\text{heat evolution of critical initial data}
+
\text{global energy-class correction}.
\]

Such a structure could potentially replace global mildness in an Albritton--Barker style Liouville argument.

This route is closer to concentration-compactness/stability theory and may survive even when global norms are not tight under recentering.

---

## 9. Updated master frontier

The current chain is

\[
\boxed{
\text{singular tower}
\Longrightarrow
T_{dynamic}
\lor H_{ambient}
\lor A_{detached}.
}
\]

For the detached branch,

\[
\boxed{
A_{detached}
\Longrightarrow
\text{expanding-window inheritance}
\lor
\text{coherent-restart inheritance needed}.
}
\]

Finite physical energy alone is not a third closure mechanism because its visibility can be suppressed by the first-hitting diagonal factor `r_j^{1/5}`.

---

## 10. DSD verdict

### PROVED

- exact first-hitting formula
  \[
  \Xi^5=E_0^{-1}r_j\mu^2R^5;
  \]
- fixed-window diagonal extraction can drive the finite-energy visibility ratio to zero;
- main-centered Morrey gives useful ancestry only at an expanding satellite radius `R~L`, not automatically on the fixed windows defining the detached local limit;
- M5-282's visibility split is conditional and cannot by itself close `A_detached`.

### REOPENED AS GENUINE BRIDGE

- expanding-window satellite inheritance;
- or a weak-critical coherent-restart theorem stable under recentering.

### NOT PROVED

- exclusion of detached ancient satellites;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]