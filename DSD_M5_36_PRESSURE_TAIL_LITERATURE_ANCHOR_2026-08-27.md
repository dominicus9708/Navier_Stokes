# DSD M5-36 — Weighted Pressure-Tail Literature Anchor

Date: 2026-08-27

Status: **LITERATURE AUDIT / THE WEIGHTED PRESSURE QUANTITY `int |u| p^2` IS AN EXISTING VELOCITY--PRESSURE REGULARITY OBJECT, NOT A NEW ENDPOINT INVENTED BY THIS REPOSITORY / GLOBAL REGULARITY UNPROVED.**

## 1. Repository result being audited

M5-34 derived

\[
|F_P|
\le
\frac\nu2D_3
+
\frac1{2\nu}
\int |u|\,|p|^2dx,
\]

and routed the threshold-Hodge formation source to the scale-critical weighted pressure tail

\[
\boxed{
\int |u|\,|p|^2dx.
}
\]

M5-35 then showed that generic Lorentz/Calderon--Zygmund control routes this quantity back to the large weak-`L3` endpoint.

## 2. Existing pressure--velocity correlation literature

Tran, Yu and Dritschel, *Velocity--pressure correlation in Navier--Stokes flows and the problem of global regularity*, Journal of Fluid Mechanics 911 (2021), A18, DOI 10.1017/jfm.2020.1033, explicitly study weighted pressure--velocity correlations.

For the `q=3` critical case they state a criterion of the form

\[
\int_{\Omega}p^2|u|dx
\le
C^{-1}\|u\|_{L^9}^3,
\]

with a specified constant in their normalization, and discuss its relation to critical `1/r` singular profiles.

The paper derives this from the `L^q` evolution and treats the degree of velocity--pressure correlation as a regularity mechanism.

## 3. Consequence for the DSD proof search

The appearance of

\[
\int |u|p^2
\]

in M5-34 is therefore not evidence that the repository has crossed the known endpoint barrier.

The correct interpretation is

\[
\boxed{
\text{threshold--Hodge commutator audit}
\Longrightarrow
\text{a known pressure--velocity critical criterion}.
}
\]

This is a useful structural derivation because it explains **why** that weighted pressure quantity appears: it is the coarea remainder left after viscous half-absorption of the amplitude-boundary pressure flux.

But proving that the criterion always holds for arbitrary finite-energy 3D Navier--Stokes would still be a global-regularity theorem.

## 4. Audit lock

Do not promote the weighted pressure-tail estimate itself as a new closing theorem.

Future work on this route is useful only if it exploits genuinely W1-specific information that improves the known pressure--velocity criterion, for example:

1. phase-space localization to the `|u|~1/r` recurrent cell;
2. a strict pressure--velocity misalignment forced by W1 geometry;
3. a threshold-surface cancellation unavailable in the generic criterion;
4. a compactness theorem making the weighted pressure criterion automatically small on the W1 prelimit.

Absent such an improvement, the route is a re-expression of known regularity criteria.

## 5. Current status

The literature comparison strengthens the repository's negative audit:

\[
\boxed{
\text{generic pressure-tail control does not close M5.}
}
\]

The live target must use additional W1/DSD structure beyond the generic velocity--pressure correlation inequality.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
