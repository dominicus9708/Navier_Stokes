# DSD M5-308 — Parent-Morrey Local Energy Visibility Radius and Reduced Expanding-Window Target

Date: 2026-08-30

Parents:
- `DSD_M5_307_GENERAL_GROWTH_VISIBILITY_RATIO_AND_ENERGY_SHIELD_LAW_2026-08-30.md`
- `DSD_M5_305_PARENT_CAMPANATO_AGGREGATE_MONOPOLE_BOUND_AND_O_L_MINUS_ONE_MAIN_CORE_STRAIN_DECAY_2026-08-30.md`

Status: **ANCESTRY TARGET IMPROVEMENT / ON THE NO-CAMPANATO-TURNOVER CORRIDOR, A SATELLITE BALL OF NORMALIZED RADIUS `A << L=qd` LIES INSIDE A MAIN-CENTERED BALL OF PHYSICAL RADIUS `O(d)`, SO THE SATELLITE-SCALED KINETIC ENERGY AVAILABLE THERE IS ONLY `O(M L)` / AN `R^alpha` DETACHED GROWTH MODE WOULD THEREFORE BECOME ENERGETICALLY VISIBLE BY RADIUS `(M L)^{1/(2alpha+3)}`, REDUCING THE AFFINE TARGET FROM THE GLOBAL FIFTH-ROOT `(qE0)^{1/5}` TO `L^{1/5}` / HOWEVER FIXED-R COMPACTNESS DOES NOT AUTOMATICALLY GIVE CONVERGENCE ON THIS GROWING WINDOW, SO THE RESULT IS A SHARPER EXPANDING-WINDOW BRIDGE, NOT A CLOSURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Geometry

Let a satellite have natural scale

\[
\ell=q^{-1}
\]

and physical distance `d` from the tracked main core.

Define

\[
\boxed{L=qd=d/\ell\to\infty.}
\]

A satellite-scaled ball `B_A` corresponds to physical radius

\[
r_{phys}=A\ell=A/q.
\]

If

\[
A\le cL
\]

with fixed small `c`, then

\[
r_{phys}\le cd
\]

and the satellite ball is contained in a main-centered ball of radius `C d`.

---

## 2. Parent Morrey energy

Assume the no-`T_Campanato` corridor gives the centered local-energy/Morrey estimate

\[
\boxed{
\int_{B_{Cd}(X_*)}|u|^2dx
\le M_*d.
}
\]

Under satellite scaling

\[
\widetilde u(z)=q^{-1}u(x_{sat}+z/q),
\]

kinetic energy scales by a factor `q`:

\[
\int_{B_A}|\widetilde u|^2dz
=q
\int_{B_{A/q}(x_{sat})}|u|^2dx.
\]

Hence for every `A<=cL`,

\[
\boxed{
\int_{B_A}|\widetilde u|^2dz
\le
C M_* qd
=C M_*L.
}
\]

This is much smaller than the global scaled bound `qE0` whenever the late-stage scale makes `qE0 >> L`.

---

## 3. Local visibility radius for `R^alpha` growth

Suppose the detached profile has coherent mean-free growth

\[
\int_{B_R}|U-c_R|^2dy
\ge c_\alpha R^{2\alpha+3}
\]

on the radii under consideration.

If prelimit convergence were valid out to radius `R`, then the parent-Morrey energy ceiling would require

\[
c_\alpha R^{2\alpha+3}
\lesssim M_*L.
\]

Define the local-Morrey visibility radius

\[
\boxed{
R_{\alpha,M}
:=(M_*L)^{1/(2\alpha+3)}.
}
\]

For `alpha>-1`,

\[
\frac{R_{\alpha,M}}{L}
=M_*^{1/(2\alpha+3)}
L^{\frac1{2\alpha+3}-1}
\to0.
\]

Thus there is a large geometric gap between the energy visibility radius and the main-core separation radius.

---

## 4. Affine case

For `alpha=1`,

\[
\boxed{
R_{1,M}
\sim(M_*L)^{1/5}.
}
\]

Therefore a nonzero affine detached profile would be excluded if one could propagate the satellite approximation on any growing window satisfying

\[
\boxed{
L^{1/5}\ll A(L)\ll L.
}
\]

For example a hypothetical window `A=L^{1/2}` would be more than sufficient.

This is substantially weaker than the earlier global-energy visibility demand involving `(qE0)^{1/5}`.

---

## 5. General growth classes

For any `alpha>-1`, a window with

\[
\boxed{
L^{1/(2\alpha+3)+\varepsilon}
\ll A(L)\ll L
}
\]

for any fixed small `epsilon>0` would energetically exclude a coherent `R^alpha` detached growth mode under the parent Morrey bound.

Examples:

- `alpha=1`: need slightly more than `L^{1/5}`;
- `alpha=0`: need slightly more than `L^{1/3}`;
- `alpha=-1/2`: need slightly more than `L^{1/2}`.

As `alpha -> -1^+`, the required power approaches `L`, reflecting the critical obstruction.

---

## 6. Critical boundary `alpha=-1`

For `alpha=-1`,

\[
2\alpha+3=1,
\]

so

\[
R_{-1,M}\sim M_*L.
\]

There is no asymptotic room between the visibility radius and separation radius.

Thus parent Morrey energy alone can potentially remove every polynomial growth class **strictly faster than `1/R`**, but it is exactly critical at `1/R`.

This matches the role of weak-`L3`/Besov endpoint theory in the earlier W1 closure.

---

## 7. Why this is not yet a proof

M5-281 provides convergence on every fixed satellite cylinder after diagonal extraction.

It does **not** automatically provide convergence on a radius `A_n` satisfying

\[
A_n\gtrsim L_n^{1/5}
\]

or any other prescribed power of the increasing separation `L_n`.

A diagonal convergence radius may grow arbitrarily slowly compared with `L_n`.

Therefore the implication

\[
\text{detached affine limit}
\Rightarrow
\text{prelimit affine energy on }B_{L^{1/5+epsilon}}
\]

is still an expanding-window bridge and must not be assumed.

---

## 8. New reduced ancestry target

The affine ancestry problem can now be stated sharply:

\[
\boxed{
\text{prove satellite compactness/coherence on some }A_n
\text{ with }
A_n/L_n^{1/5}\to\infty,
\quad A_n/L_n\to0.
}
\]

If this is achieved, the exact affine/solid-rotation countermodels are eliminated by parent Morrey energy.

More generally, to remove `alpha`-growth it suffices to beat

\[
\boxed{L^{1/(2\alpha+3)}}.
\]

---

## 9. Possible failure routing

If expanding-window coherence breaks before `L^{1/5}`, the failure must come from some loss of the local compactness inputs as radius grows:

- ambient/harmonic strain escalation;
- derivative-frequency escalation;
- pressure oscillation;
- local energy/Campanato loss;
- material/center turnover.

These are all already typed `H/T` mechanisms.

Thus the desired future lemma has the schematic form

\[
\boxed{
\text{either }A_n\gg L_n^{1/5}
\quad\text{or}\quad
H/T\text{ occurs before that radius}.
}
\]

This is now a concrete finite-power target rather than an unspecified full expanding-window theorem.

---

## 10. Formation significance

The Formation decomposition has reduced the ancestry question from

> recover the entire global detached tail

to

> recover only enough of the detached state to cross its energy visibility radius.

For affine growth this means `L^{1/5+epsilon}`, far short of the full separation scale `L`.

This is a substantial narrowing of the remaining bridge.

---

## 11. Audit verdict

### PROVED

Satellite-scaled local energy ceiling on `A<<L`:

\[
\boxed{
\int_{B_A}|\widetilde u|^2\le C M_*L.
}
\]

### DERIVED TARGET

Growth visibility radius

\[
\boxed{
R_{\alpha,M}=(M_*L)^{1/(2\alpha+3)}.
}
\]

### KEY AFFINE TARGET

\[
\boxed{
A_n/L_n^{1/5}\to\infty
}
\]

is sufficient to kill the affine detached obstruction under Morrey.

### OPEN

- prove the finite-power expanding-window compactness or route its failure to typed H/T;
- critical `alpha=-1` endpoint;
- dynamic turnover;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]