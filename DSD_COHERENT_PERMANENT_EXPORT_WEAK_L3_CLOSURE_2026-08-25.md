# DSD Coherent Permanent Export: Weak-L3 Closure — REOPENED

Date: 2026-08-25

Audit correction: 2026-08-26

Status: **REOPENED / THE INTERNAL COHERENT-EXPORT ESTIMATES REMAIN VALID / THE FINAL CLOSURE THROUGH THE OLD BOUNDED-Z WEAK-L3 ENDPOINT GATE IS INVALID / SEE `DSD_AUDIT_BARKER_PRANGE_CUBIC_LOG_RATE_CORRECTION_2026-08-26.md` / GLOBAL REGULARITY UNPROVED.**

## 1. What survives

The original calculation established, on the stated coherent quiet corridor, the following useful implications.

A bounded normalized material vorticity flux together with derivative/directional coherence gives the critical vorticity envelope

\[
|\Omega|\lesssim R^{-2}
\]

for an exported cohort at normalized radius R.

The corresponding velocity contribution has the critical size

\[
|U_R|\lesssim R^{-1}.
\]

If separated export events remain passively ordered in logarithmic radius with bounded overlap, the coherent train satisfies

\[
\boxed{
|U_{train}(Y,s)|
\lesssim
(1+|Y|)^{-1}
}
\]

and hence

\[
\boxed{
\sup_s\|U_{train}(s)\|_{L^{3,\infty}}<\infty.
}
\]

Loss of bounded flux, derivative/directional coherence, or shell separation still routes naturally toward the previously typed viscous/projective/H/T mechanisms.

These structural estimates remain useful.

## 2. What does not survive

The original file then used

`DSD_BOUNDED_Z_WEAK_L3_ENDPOINT_EXCLUSION_GATE_2026-08-25.md`

to conclude that a bounded-Z singular survivor could not remain uniformly weak-L3.

That terminal implication was based on a transcription error in the Barker--Prange lower bound.

The correct external lower bound is logarithmic for

\[
\int|u|^3,
\]

not logarithmic for

\[
\|u\|_3
\]

itself.

Consequently a critical 1/R conveyor with fixed cubic mass per logarithmic shell has exactly the logarithmic cubic growth compatible with the quantitative theorem.

Therefore

\[
\boxed{
\text{coherent bounded-flux passive }1/R\text{ conveyor}
}
\]

is **not closed** merely because it is uniformly weak-L3.

## 3. Corrected status of the branch

The coherent conveyor should now be treated as an endpoint saturation model:

\[
\boxed{
|U|\sim R^{-1},
\qquad
|\Omega|\sim R^{-2},
\qquad
U\in L^{3,\infty},
\qquad
\int_{|Y|<R}|U|^3\sim c\log R.
}
\]

This is consistent with the periodic canonical-tail analysis developed on 2026-08-26.

Thus the branch is reopened and merges with the current W1 critical-memory frontier.

## 4. Valid failure routes

The following complements remain meaningful:

\[
\boxed{
\begin{aligned}
X_1&:\text{ cumulative material flux/circulation loses its ceiling}
\Rightarrow\text{ viscous-flux/H},\\
X_2&:\text{ directional or derivative coherence fails}
\Rightarrow\text{ projective/noncoherent/H},\\
X_3&:\text{ log-shell separation or bounded overlap fails}
\Rightarrow\text{ material/radial turnover},\\
X_4&:\text{ additional residual tail or amplitude hierarchy appears}
\Rightarrow\text{ separate endpoint analysis}.
\end{aligned}
}
\]

But the complement of X1--X4 is no longer automatically contradictory.

## 5. Correct next target

The quiet coherent branch now supplies a concrete asymptotic object rather than a closure:

\[
\boxed{
\text{critical log-radius memory / canonical }1/R\text{ tail}.
}
\]

A valid final argument must price the **generation, replenishment, or coupling** of that tail, rather than merely its weak-L3 membership.

This connects directly to the current periodic reduction

\[
U=B_R+Q_R,
\qquad
B_R\sim R^{-1},
\qquad
Q_R\in L^2\cap L^3.
\]

The original pre-correction content remains available in Git history.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]