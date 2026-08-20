# Strict H1 Efficiency Gap on a Precompact Non-H/T Class — 2026-08-20

Overall status: **COMPACTNESS CONSEQUENCE OF FULL-SATURATION RIGIDITY — GLOBAL REGULARITY NOT PROVED.**

This note makes precise a consequence of `PV_H1_FULL_SATURATION_RIGIDITY_2026-08-20.md`: once the remaining normalized profile class is genuinely precompact, exact nonattainment of the sharp H1 production constant automatically becomes a strict uniform gap on that class.

---

## 1. Efficiency functional

For a nonzero compatible strain profile `S`, define

\[
\mathfrak E_{H1}(S)
=
\frac{
-\langle\mathcal R_{VI},-\Delta S\rangle
}{
\frac4{\sqrt6}\int|S||\nabla S|^2dx
}.
\]

The sharp trace-free range bound gives

\[
\boxed{
\mathfrak E_{H1}(S)\le1.
}
\]

The full-saturation rigidity theorem shows that equality cannot occur for a nonzero finite-energy whole-space strain profile.

---

## 2. A normalized compact class

Consider a set `K` of strain-compatible profiles satisfying, after fixing the first-hitting center and scale:

1. uniform whole-space tightness in `H1`;
2. a uniform `H2` bound;
3. a nontrivial normalization preventing convergence to zero, e.g. the associated vorticity satisfies
\[
\|\Omega\|_\infty=1;
\]
4. a fixed gauge/center eliminating translation drift.

The uniform `H2` bound plus tightness gives precompactness in `H^s` for every `s<2` after subsequence extraction. Choosing `s>3/2` gives strong local/uniform convergence of `S`, while `s>1` gives strong convergence of `grad S` in `L2`.

Hence both

\[
\int|S||\nabla S|^2
\]

and the exact covariance expression

\[
-\langle\mathcal R_{VI},-\Delta S\rangle
=-\int S:(M_{sp}+2M_{rg})
\]

are continuous along convergent sequences in this class.

---

## 3. Strict uniform gap

Suppose no strict gap existed. Then there would be a sequence `S_j in K` with

\[
\mathfrak E_{H1}(S_j)\to1.
\]

Precompactness gives a subsequence converging to `S_* in K`. Nontrivial normalization gives

\[
S_*\not\equiv0.
\]

Continuity then yields

\[
\mathfrak E_{H1}(S_*)=1,
\]

contradicting the full-saturation rigidity theorem.

Therefore

\[
\boxed{
\sup_{S\in K}\mathfrak E_{H1}(S)
\le1-\delta_K
}
\]

for some

\[
\boxed{\delta_K>0.}
\]

Thus a genuinely precompact non-H/T recurrent class has a uniform strict loss below the algebraic H1 production maximum.

---

## 4. What this does and does not prove

This result eliminates sequences that approach the algebraic H1 maximum while remaining in one compact non-H/T class.

However the physical regularity threshold is controlled by

\[
\eta_{VI}(S)
=
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{\|\Delta S\|_2^2},
\]

and finite-time blowup requires

\[
\limsup\eta_{VI}\ge\nu.
\]

The strict efficiency gap gives

\[
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
(1-\delta_K)
\frac4{\sqrt6}
\int|S||\nabla S|^2,
\]

but a separate estimate is still required to compare

\[
\int|S||\nabla S|^2
\]

with

\[
\|\Delta S\|_2^2.
\]

Therefore `delta_K>0` is not by itself enough to cross the viscosity threshold.

---

## 5. New final local variational target

On the compact normalized survivor class define

\[
\boxed{
\Lambda_K
=
\sup_{S\in K}
\frac{
-\langle\mathcal R_{VI},-\Delta S\rangle
}{
\|\Delta S\|_2^2
}.
}
\]

Because `K` is precompact and the denominator is bounded away from zero on a nontrivial tight class, this supremum is attained after closure.

The remaining local P_V problem can therefore be stated as the concrete variational question

\[
\boxed{
\Lambda_K<\nu\ ?
}
\]

If this strict inequality can be proved for every admissible non-H/T first-hitting compact class, the P_V ancient branch is eliminated directly by the exact H1 ledger.

If instead `Lambda_K >= nu`, any maximizing profile supplies a much more rigid elliptic/variational object to analyze than an arbitrary recurrent Navier--Stokes orbit.

Status: **FULL H1 SATURATION NONATTAINMENT UPGRADES TO A STRICT CLASS-DEPENDENT EFFICIENCY GAP ON ANY GENUINELY PRECOMPACT NON-H/T PROFILE CLASS. THE REMAINING LOCAL QUESTION IS THE ATTAINED VARIATIONAL THRESHOLD `Lambda_K < nu?`.**