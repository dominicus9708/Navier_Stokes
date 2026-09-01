# DSD M5-546 — Cycle-action audit isolates the missing excess-dissipation inequality

Date: 2026-09-01

Status: **FINAL-CYCLE REDUCTION / ON THE FINITE ACTIVE CORE, THE KINETIC, ENSTROPHY, PALINSTROPHY, AND HIGHER SOBOLEV BALANCE RESIDUALS ARE ALL ENDPOINT COBoundaries UP TO ARBITRARILY SMALL CUTOFF ERROR / THEREFORE NO FIXED LINEAR COMBINATION OF THE ALREADY KNOWN ENERGY LEDGERS CAN HAVE STRICT POSITIVE INVARIANT MEAN / THE POSITIVE RATCHET/DUAL ACTION CAN CLOSE THE RECURRENT HULL ONLY IF ONE PROVES A genuinely NEW COERCIVE `EXCESS` INEQUALITY SHOWING THAT SOME PORTION OF THE PROJECTIVE/DIFFUSIVE COST CANNOT BE FULLY PAID BY THE AXIAL AND DERIVATIVE PRODUCTION TERMS / THIS IDENTIFIES THE PRECISE REMAINING CORE-RIGIDITY LEMMA RATHER THAN ANOTHER COMPACTNESS OR TAIL PROBLEM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Local core balances

Fix the M5-543 active radius and then enlarge the cutoff radius so that every transition-shell error is below a prescribed `epsilon>0`.

M5-544--545 give, schematically,

\[
\boxed{
\frac12K_R'
-
\frac14K_R
+
D_R
=
\varepsilon_K,
}
\]

\[
\boxed{
\frac12E_R'
+
\frac14E_R
+
P_R
-
Q_R
=
\varepsilon_E,
}
\]

\[
\boxed{
\frac12P_R'
+
\frac34P_R
+
H_R
-
\mathcal N_{P,R}
=
\varepsilon_P,
}
\]

and for every fixed higher order `m`,

\[
\boxed{
\frac12D_{m,R}'
+c_mD_{m,R}
+D_{m+1,R}
-
\mathcal N_{m,R}
=
\varepsilon_m,
}
\]

with

\[
\sup|\varepsilon_*|\to0
\qquad(R\to\infty).
\]

---

## 2. Define the scale-compensated residuals

Set

\[
\boxed{
\mathfrak R_K
:=
D_R-rac14K_R,
}
\]

and

\[
\boxed{
\mathfrak R_E
:=
P_R+rac14E_R-Q_R.
}
\]

Then

\[
\boxed{
\mathfrak R_K
=
-\frac12K_R'
+
\varepsilon_K,
}
\]

and

\[
\boxed{
\mathfrak R_E
=
-\frac12E_R'
+
\varepsilon_E.
}
\]

Likewise define

\[
\mathfrak R_P
:=
H_R+rac34P_R-\mathcal N_{P,R},
\]

so that

\[
\boxed{
\mathfrak R_P
=
-\frac12P_R'
+
\varepsilon_P.
}
\]

Thus each familiar dissipative excess is already an endpoint derivative once the corresponding production term is included.

---

## 3. One-generation cycle actions

For one roof interval

\[
I_j=[\theta_j,\theta_{j+1}],
\]

define

\[
\mathcal A_K(j)
:=
\int_{I_j}\mathfrak R_Kd\theta.
\]

Then

\[
\boxed{
\mathcal A_K(j)
=
-\frac12
\left[
K_R(\theta_{j+1})-K_R(\theta_j)
\right]
+
O(\varepsilon\Theta_+).
}
\]

Similarly,

\[
\boxed{
\mathcal A_E(j)
=
-\frac12
\left[
E_R(\theta_{j+1})-E_R(\theta_j)
\right]
+
O(\varepsilon\Theta_+),
}
\]

and

\[
\boxed{
\mathcal A_P(j)
=
-\frac12
\left[
P_R(\theta_{j+1})-P_R(\theta_j)
\right]
+
O(\varepsilon\Theta_+).
}
\]

Therefore on an exact recurrent cycle these actions telescope to zero up to the chosen cutoff error.

---

## 4. No fixed linear combination of old ledgers can close the hull

Take arbitrary fixed coefficients

\[
a_0,a_1,\ldots,a_M.
\]

Any finite combination of the first `M` balance residuals has the form

\[
\sum_{m=0}^Ma_m\mathfrak R_m
=
-\frac12\frac d{d\theta}
\left(
\sum_{m=0}^Ma_mD_{m,R}
\right)
+
O(\varepsilon).
\]

Hence its invariant mean is

\[
\boxed{
\left\langle
\sum_{m=0}^Ma_m\mathfrak R_m
\right\rangle
=O(\varepsilon).
}
\]

Letting the cutoff radius grow gives zero.

Thus no **fixed linear combination of already known scalar energy ledgers** can dominate the positive ratchet mark by a uniform positive constant.

If it did, invariant averaging would already contradict recurrence.

The absence of such a contradiction is not a tail defect; it is a structural coboundary fact.

---

## 5. Positive active charge

Let

\[
\mathcal R_{act}(\theta)\ge0
\]

be a smoothed local active charge that contains the retained pair/ratchet event, for example a fixed combination of

\[
\int_{B_{R_core}}\rho^2|\tau|^2dy,
\]

\[
\int_{B_{R_core}}
|(I-\xi\otimes\xi)\Delta W|^2dy,
\]

and the persistent dual-pair mark.

M5-514--516 and the active-carrier thickening give on the selected ergodic component

\[
\boxed{
\langle\mathcal R_{act}\rangle
=:r_*>0.
}
\]

The remote endpoint tail changes this mean by an arbitrarily small amount only.

---

## 6. What would close the proof core

A sufficient new estimate would be a bounded local observable `Phi_core` and constants

\[
c_*>0,
\qquad
\varepsilon<c_*r_*/4,
\]

such that

\[
\boxed{
\frac d{d\theta}\Phi_{core}
\ge
c_*\mathcal R_{act}
-
\varepsilon_{remote}.
}
\]

Equivalently on one generation,

\[
\boxed{
\Phi_{core}(\theta_{j+1})
-
\Phi_{core}(\theta_j)
\ge
c_*\int_{I_j}\mathcal R_{act}d\theta
-
\varepsilon_{remote}\Theta_+.
}
\]

Invariant averaging would then give

\[
0
\ge
c_*r_*
-
\varepsilon_{remote}
>0,
\]

a contradiction.

This is exactly the M5-485 strict-cocycle mechanism, now localized to the finite active core.

---

## 7. Equivalent excess-production formulation

Instead of finding `Phi_core` directly, it is enough to prove that some unavoidable part of the active charge cannot be paid by the known production channels.

A model target is

\[
\boxed{
\mathcal R_{act}
\le
C_1
\left(
Q_R-rac14E_R-P_R
\right)
+
C_2
\left(
\mathcal N_{P,R}-\frac34P_R-H_R
\right)
+
\frac d{d\theta}\Psi
+
\varepsilon,
}
\]

with a sign arrangement that yields a strictly positive invariant remainder.

Because the bracketed terms are themselves derivatives by the PDE balances, any genuine positive remainder would contradict recurrence.

The essential content must therefore be a **coercive mismatch** between ratchet geometry and the production terms, not another energy identity.

---

## 8. Why current estimates do not provide the excess

Existing estimates give only statements such as

\[
\mathcal R_{tilt}
\lesssim
\int\rho^2|\Sigma|^2,
\]

or

\[
\mathcal R_{projdiff}
\le
H_R,
\]

while axial production satisfies

\[
Q_R
=
\int\rho^2\sigma.
\]

These inequalities show that the active charge costs strain or derivatives, but they do **not** show that those costs exceed the amount already regenerated by `Q_R` or `N_(P,R)`.

Hence the positive ratchet may presently be fully paid by the recurrent nonlinear production ledger.

That is the exact remaining obstruction.

---

## 9. Relation to the anchored-pair branch

On the M5-516 anchored branch,

\[
\tau_i=-\mathcal D_i.
\]

This is the sharpest place to seek an excess inequality because two nominally distinct channels are forced into exact vector opposition.

If one can show that maintaining

\[
\tau_i+\mathcal D_i=0
\]

while also sustaining positive axial production requires strictly more `H_R`, palinstrophy, flux variation, or strain energy than the recurrent production identities can supply, the anchored branch closes.

The moving-pair branches already have positive configuration action and can be treated by the same excess framework.

---

## 10. Final core-rigidity obligation

The remaining finite-core problem can now be stated without tail language:

> **Core excess lemma.** A nonzero globally smooth compact recurrent similarity Navier--Stokes core carrying the common positive production/dual/ratchet package cannot satisfy all kinetic, enstrophy, palinstrophy, flux, and pair-angle balances with zero net excess on every generation.

Proving this lemma, or a stronger known theorem implying it, would remove the finite recurrent active core.

The endpoint spectator tail would then no longer support a singular mechanism by M5-542--544.

---

## 11. DSD audit conclusion

The proof search has passed through three qualitatively different obstacles:

1. compactness/tail defects;
2. component-coupling defects;
3. intrinsic recurrent production-versus-dissipation balance.

M5-541--545 remove the first two from the active core.

M5-546 identifies the third as the actual remaining rigidity problem.

No claim is made that an existing inequality already proves the core excess lemma.

---

## 12. Highest-value next target

Work directly on the anchored exact-cancellation branch and derive the evolution of a **cross-channel observable** involving axial stretching and projected diffusion, rather than another pure Sobolev energy.

Natural candidates are

\[
\int\rho^2\tau\cdot\mathcal D_\xi,
\]

which equals `-int rho^2 |tau|^2` on the anchored branch, and a two-lineage sum of these cross terms.

The key question is whether its evolution or elliptic representation has a sign that cannot be absorbed into `Q_R` and `N_(P,R)`.

This is now more targeted than another generic scalar-norm search.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]