# DSD M5-509 — The globally smooth compact marked hull is uniformly nonstationary

Date: 2026-09-01

Status: **DYNAMIC RIGIDITY ON THE M5-508 COMPACT BRANCH / THE MARKED RECORD SECTION RETAINS A FIXED NONTRIVIAL VORTICITY CARRIER, WHILE GLOBAL `L2` VORTICITY PUTS THE CANONICAL BIOT--SAVART VELOCITY IN `L6` / A STATIONARY BACKWARD-SIMILARITY STATE IN THIS CLASS WOULD BE A SMOOTH LERAY SELF-SIMILAR PROFILE IN `L6`, WHICH IS ZERO BY TSAI'S EXTERNAL LIOUVILLE THEOREM / HENCE NO MARKED COMPACT STATE IS STATIONARY / GLOBAL SMOOTH COMPACTNESS THEN UPGRADES POINTWISE NONSTATIONARITY TO A UNIFORM POSITIVE LOCAL SIMILARITY-TIME SPEED ON ONE FIXED BALL / THIS RULES OUT A NEAR-EQUILIBRIUM CLOSURE BUT DOES NOT RULE OUT PERIODIC OR APERIODIC RECURRENT MOTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-508

On the tight bounded-palinstrophy branch, M5-507--508 give a globally smooth compact similarity hull.

For every finite `m`,

\[
\sup_{\widehat{\mathfrak H}}
\|W\|_{H^m(\mathbb R^3)}
<\infty,
\]

and the hull is globally precompact in every finite `H^s` and every fixed `C^k` topology.

The M5-478--485 marked record construction also carries a nontrivial first-hitting vorticity carrier.  On the marked record section, after choosing a fixed ball containing all marked carrier centers, there are constants

\[
R_c<\infty,
\qquad
c_c>0
\]

such that

\[
\boxed{
\int_{B_{R_c}}|W_Y(y)|^2dy
\ge c_c
\qquad
\text{for every marked state }Y.
}
\]

Thus the zero state is excluded from the marked section uniformly.

M5-509 asks whether a marked state can nevertheless be stationary in similarity time.

---

## 2. Canonical velocity gauge

For each divergence-free vorticity state `W`, choose the canonical whole-space Biot--Savart velocity

\[
U
=\nabla\times(-\Delta)^{-1}W.
\]

This removes the spatially constant Galilean ambiguity.

The div--curl identity and Sobolev inequality give

\[
\|\nabla U\|_2
\lesssim
\|W\|_2,
\]

and hence

\[
\boxed{
\|U\|_6
\le C\|\nabla U\|_2
\le C\|W\|_2.
}
\]

Therefore every M5-508 state has canonical velocity

\[
\boxed{U\in L^6(\mathbb R^3).}
\]

All higher local and global derivative bounds follow from the corresponding vorticity bounds by Calderon--Zygmund theory.

---

## 3. External stationary-profile theorem

A stationary state in backward similarity variables solves the steady Leray system

\[
\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
=-\nabla\Pi+\Delta U,
\qquad
\nabla\cdot U=0.
\]

The classical self-similar Liouville theory gives:

- Necas--Ruzicka--Sverak: no nonzero smooth profile in the critical `L3` class;
- Tsai: the nonexistence extends to `L^p`, `3<p\le\infty`.

The current version of Pineau--Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619v2 (2026), Section 1.1, explicitly summarizes this Tsai theorem.

Since our canonical velocity satisfies

\[
U\in L^6,
\]

a smooth stationary state in the present class must obey

\[
\boxed{U\equiv0,\qquad W\equiv0.}
\]

This is the only external theorem used in the stationary exclusion below.

---

## 4. No marked state is stationary

Assume a marked state `Y` were stationary:

\[
\partial_\theta W_Y\equiv0.
\]

In the canonical Biot--Savart gauge, the corresponding `U_Y` is a stationary Leray profile in `L6`.

By the external Tsai theorem,

\[
W_Y\equiv0.
\]

But the marked carrier lower bound gives

\[
\int_{B_{R_c}}|W_Y|^2dy
\ge c_c>0.
\]

Contradiction.

Therefore

\[
\boxed{
\partial_\theta W_Y\not\equiv0
\qquad
\text{for every marked }Y.
}
\]

This is qualitative nonstationarity.

---

## 5. Why a global `L2` speed is not used

The similarity vorticity equation is

\[
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
=(W\cdot\nabla)U
+\Delta W.
\]

M5-508 provides unweighted Sobolev bounds, but it does not provide a global weighted moment such as

\[
\|y\cdot\nabla W\|_2<\infty.
\]

Therefore it would be an unaudited shortcut to claim that the similarity vector field is globally continuous into `L2` merely from the M5-508 Sobolev bounds.

M5-509 instead works on fixed balls, where `|y|` is bounded.

---

## 6. Local continuity of the similarity vector field

Fix `R<infinity`.

On `B_R`, all coefficients in the similarity equation are bounded, and the all-order global compactness implies strong convergence of `W`, `U`, and all required derivatives on `B_R`.

Hence the map

\[
Y
\mapsto
\partial_\theta W_Y
\]

is continuous from the M5-508 compact marked section into

\[
L^2(B_R).
\]

Equivalently, for each fixed `R`,

\[
Y\mapsto
\|\partial_\theta W_Y\|_{L^2(B_R)}
\]

is continuous.

---

## 7. Compactness upgrades nonstationarity to a uniform local speed floor

For each marked state `Y`, qualitative nonstationarity means there exists some finite radius `R_Y` for which

\[
\|\partial_\theta W_Y\|_{L^2(B_{R_Y})}
>0.
\]

Choose `epsilon_Y>0` such that

\[
\|\partial_\theta W_Y\|_{L^2(B_{R_Y})}
>2\epsilon_Y.
\]

By continuity, there is an open neighborhood `N_Y` in the marked compact hull such that every `Z in N_Y` satisfies

\[
\|\partial_\theta W_Z\|_{L^2(B_{R_Y})}
>\epsilon_Y.
\]

Compactness gives a finite subcover

\[
N_{Y_1},\ldots,N_{Y_N}.
\]

Set

\[
R_{dyn}
:=
\max_iR_{Y_i},
\]

and

\[
\delta_{dyn}
:=
\min_i\epsilon_{Y_i}>0.
\]

Since enlarging the ball cannot decrease the `L2` norm,

\[
\boxed{
\inf_{Y\in\mathfrak H_{mark}}
\|\partial_\theta W_Y\|_{L^2(B_{R_{dyn}})}
\ge
\delta_{dyn}>0.
}
\]

This is the quantitative conclusion of M5-509.

---

## 8. Interpretation

The globally smooth compact survivor cannot approach a stationary self-similar profile at the marked record times.

Its recurrent dynamics must retain a fixed amount of local similarity-time motion:

\[
\boxed{
\text{marked recurrence}
+\text{global smooth compactness}
\Longrightarrow
\text{uniformly dynamic recurrence}.
}
\]

This is stronger than the earlier statement that the hull is merely nonzero.

It says that the remaining compact branch is genuinely a recurrent dynamical object rather than a sequence converging toward one steady Leray profile.

---

## 9. DSD audit: this is not a strict cocycle

A positive phase-space speed is not a signed drift.

A periodic orbit can satisfy

\[
\|\partial_\theta W\|\ge\delta>0
\]

for all time and still return exactly to its starting state.

Therefore

\[
\boxed{
\text{uniform nonstationarity}
\not\Longrightarrow
\text{strict Lyapunov/cocycle drift}.
}
\]

M5-509 closes only the **near-equilibrium** escape route.

It does not close periodic, discretely self-similar, rotated, or aperiodic recurrent dynamics.

---

## 10. Relation to Pineau--Vicol 2026

Pineau--Vicol also prove a one-slice approximate-self-similarity regularity criterion under a stronger local spatial Type-I bound of the form

\[
|u(x,t)|
\le
\frac{C}{\sqrt{-t}+|x|}.
\]

M5-478 supplies only the amplitude Type-I control

\[
\|u(t)\|_\infty
\lesssim
(-t)^{-1/2},
\]

and M5-508 supplies global smooth compactness in unweighted Sobolev spaces.

Neither statement automatically implies the spatial Type-I decay

\[
|u(x,t)|
\lesssim
(\sqrt{-t}+|x|)^{-1}.
\]

Therefore their approximate-self-similarity theorem is **not** imported into the proof line at M5-509.

The only external result imported here is the older stationary `L^p`, `p>3`, Liouville theorem.

---

## 11. Updated compact frontier

On the globally smooth compact branch,

\[
\boxed{
\mathcal C_{smooth}^{global}
\Longrightarrow
\mathcal C_{dyn}^{uniform-marked},
}
\]

where

\[
\mathcal C_{dyn}^{uniform-marked}
:
\quad
\exists R_{dyn},\delta_{dyn}>0
\text{ such that }
\inf_{\mathfrak H_{mark}}
\|\partial_\theta W\|_{L^2(B_{R_{dyn}})}
\ge\delta_{dyn}.
\]

Combining with M5-508,

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-Sob}
\lor
H_{tail}^{remote-E}
\lor
\mathcal C_{dyn}^{uniform-marked}.
}
\]

---

## 12. Highest-value next target

The next audit should examine the missing spatial decay needed to turn the smooth compact Type-I-amplitude hull into the stronger spatial Type-I class.

The key question is whether M5-508 compactness forces

\[
\sup_y(1+|y|)|U(y)|<\infty,
\]

or whether a low-frequency velocity tail can remain despite all-order vorticity compactness.

This must be answered before importing stronger one-slice self-similarity regularity criteria.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
