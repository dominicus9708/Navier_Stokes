# Ancient Critical Tail — Dyadic Shell Necessity — 2026-08-24

Status: **SHARP DYADIC NECESSARY CONDITION FOR THE REMAINING LOW-FREQUENCY TAIL / GLOBAL REGULARITY NOT PROVED.**

The previous ancient notes show that any nontrivial restricted survivor must evade the global-`L3` Liouville theorem through a critical large-scale velocity tail, while its vorticity satisfies

\[
\|\Omega(\tau)\|_2^2
\lesssim |\tau|^{-1/2}.
\]

This note quantifies what such an `L3` tail must look like on dyadic shells.

---

## 1. Dyadic annuli

Fix a time `tau<0` and let

\[
A_R=\{y:R<|y|<2R\}.
\]

Let

\[
a_R=(U)_{A_R}
\]

be the annular mean and define

\[
G_R
=\int_{A_R}|U-a_R|^3dy,
\]

\[
e_R
=\int_{A_R}|\nabla U|^2dy.
\]

The mean-free quantity isolates the genuine shell variation from a nearly constant drift.  A spatially constant drift is not a vorticity/strain tail and is excluded from the active shell mechanism.

---

## 2. Scale-sharp annular Poincare-Sobolev estimate

On a unit annulus, mean-zero `H1` controls both `L2` and `L6`.  Scaling to `A_R` gives

\[
\|U-a_R\|_{L^2(A_R)}
\le C R\|\nabla U\|_{L^2(A_R)},
\]

and

\[
\|U-a_R\|_{L^6(A_R)}
\le C\|\nabla U\|_{L^2(A_R)}.
\]

Interpolating `L3` between `L2` and `L6`,

\[
\boxed{
\|U-a_R\|_{L^3(A_R)}
\le
C R^{1/2}e_R^{1/2}.
}
\]

Therefore

\[
\boxed{
G_R
\le
C R^{3/2}e_R^{3/2}.
}
\]

Equivalently,

\[
\boxed{
G_R^{2/3}
\le
C R e_R.
}
\]

This is exactly saturated by a critical shell `U~R^{-1}` for which `e_R~R^{-1}` and `G_R~1`.

---

## 3. Necessary weighted-Dirichlet divergence

Take dyadic radii

\[
R_k=2^kR_0.
\]

If the mean-free global critical tail has divergent cubic mass,

\[
\sum_{k=0}^\infty G_{R_k}=\infty,
\]

then the preceding upper bound implies necessarily

\[
\boxed{
\sum_{k=0}^\infty
(R_ke_{R_k})^{3/2}
=\infty.
}
\]

Thus a nontrivial ancient survivor cannot evade global `L3` rigidity using arbitrarily weak large-radius shells.  Its weighted shell Dirichlet numbers

\[
\boxed{
x_k:=R_ke_{R_k}}
\]

must fail to belong to `ell^{3/2}`.

---

## 4. Compatibility with finite total enstrophy

At the same time,

\[
\sum_ke_{R_k}
\le
\|\nabla U(\tau)\|_2^2
=
\|\Omega(\tau)\|_2^2
\lesssim|\tau|^{-1/2}.
\]

There is no contradiction because the dyadic radii grow geometrically.

The critical model

\[
e_{R_k}\sim R_k^{-1}
\]

has

\[
\sum_ke_{R_k}<\infty,
\qquad
x_k=R_ke_{R_k}\sim1,
\]

and hence

\[
\sum_kx_k^{3/2}=\infty.
\]

Therefore the finite-enstrophy budget allows precisely the critical `1/r` stack.

---

## 5. Backward scaling of the required shell stack

At backward time

\[
T=|\tau|,
\]

the active similarity radius is

\[
R_0\sim\sqrt T.
\]

The ancient enstrophy decay is

\[
\|\Omega(\tau)\|_2^2
\lesssim T^{-1/2}.
\]

A critical tail beginning at `R_0` has

\[
\sum_{R_k\ge R_0}e_{R_k}
\sim
\sum_{R_k\ge R_0}R_k^{-1}
\sim R_0^{-1}
\sim T^{-1/2},
\]

which exactly saturates the available global enstrophy budget.

Thus the surviving tail cannot be substantially stronger without consuming more enstrophy than the first-hitting scaling permits, and cannot be substantially weaker on too many shells if it is to keep the global `L3` norm unbounded.

---

## 6. Palinstrophy scaling

For the same model,

\[
|\Omega|\sim R^{-2},
\qquad
|\nabla\Omega|\sim R^{-3},
\]

so the shell palinstrophy is

\[
q_R
:=
\int_{A_R}|\nabla\Omega|^2
\sim R^{-3}.
\]

Summing from `R_0~sqrt T`,

\[
\sum q_R
\sim R_0^{-3}
\sim T^{-3/2},
\]

which matches the derivative decay sequence and the integrated palinstrophy budget derived in `ANCIENT_BACKWARD_ENSTROPHY_PALINSTROPHY_DECAY_2026-08-24.md`.

The same shell stack therefore saturates **both** remaining global derivative budgets.

---

## 7. Relation to the historical-shell calculations

The previously routed historical shell had the same scaling:

\[
|U|\sim R^{-1},
\qquad
|\Omega|\sim R^{-2}.
\]

The distinction is now conceptual:

- a shell that must be rebuilt, transported, or recycled toward the active core is routed to `H/T` by the historical-recycling calculations;
- a shell that remains dynamically passive may survive as part of the global low-frequency ancient tail.

Therefore the last ancient obstruction is not **historical recycling**.  It is an asymptotically passive critical stack whose weighted shell Dirichlet numbers remain non-summable in the `ell^{3/2}` sense while their ordinary enstrophy is summable.

---

## 8. Mean/drift caveat

A global `L3` failure could in principle also be contaminated by annular means `a_R`.  However the ancient limit lies in global `L6`, so a nonzero spatially constant parasitic field is excluded.  Large slowly varying annular means must change across scales and hence generate gradient energy in the transition shells.

A complete low-frequency rigidity theorem should therefore control both

\[
\{R_ke_{R_k}\}
\]

and the telescoping annular means.  The mean-free estimate above identifies the genuinely vortical part of the critical obstruction.

---

## 9. Final shell-level target

The remaining Liouville problem may now be stated as follows.

Can a nontrivial ancient Navier-Stokes solution satisfy simultaneously

\[
\|\Omega(\tau)\|_\infty\lesssim T^{-1},
\]

\[
\|\Omega(\tau)\|_2^2\lesssim T^{-1/2},
\]

\[
\int_{-\infty}^{-T}\|\nabla\Omega\|_2^2d\tau
\lesssim T^{-1/2},
\]

and, for every large backward time, carry a dynamically passive dyadic stack with

\[
\boxed{
\sum_k(R_ke_{R_k})^{3/2}=\infty
}
\]

while maintaining the recurrent active similarity-scale core?

No contradiction from the present energy/enstrophy/palinstrophy budgets alone rules out this exact critical stack.

Status: **THE NECESSARY ANCIENT LOW-FREQUENCY TAIL IS NOW SHELL-QUANTIFIED. GLOBAL `L3` FAILURE REQUIRES A DYADIC WEIGHTED-DIRICHLET STACK WITH `sum (R e_R)^(3/2)=infinity`, WHILE ORDINARY ENSTROPHY `sum e_R` REMAINS FINITE. THE MODEL `e_R~1/R` SATURATES ALL CURRENT BUDGETS. THIS IS THE SHARP REMAINING LOW-FREQUENCY OBSTRUCTION. GLOBAL REGULARITY REMAINS UNPROVED.**