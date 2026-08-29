# DSD M5-195 — Radius-Normalization Projective-vs-Trace-Free Dominance Audit

Date: 2026-08-29

Parent: `DSD_M5_194Z_KI_ELIMINATION_TRACEFREE_TIGHTNESS_RADIUS_CLOSURE_2026-08-29.md`

Status: **BRANCH-PRIORITY PRUNING / AFTER CONVERTING THE PROJECTIVE CLOSURE RADIUS TO THE SAME `sqrt(nu)` NORMALIZATION, THE QUARTER-TAIL TRACE-FREE/TIGHTNESS/TIMING CERTIFICATE COVERS A STRICTLY LARGER COMMON-RADIUS INTERVAL / THE PROJECTIVE-ACTION CLOSURE THEREFORE DOES NOT EXTEND THE RADIUS ENVELOPE ON THE COMPATIBLE STRONG-TIGHTNESS PURE BRANCH, THOUGH IT REMAINS USEFUL ON OTHER GEOMETRIC CORRIDORS / THE SURVIVING PURE QUARTER-TAIL WINDOW STARTS BEYOND THE TRACE-FREE RADIUS, NOT IN A GAP BETWEEN THE TWO CERTIFICATES / GLOBAL REGULARITY UNPROVED.**

---

## 1. Two previously derived radius thresholds

### Trace-free / tightness / timing threshold

M5-194Z gives, for

\[
q=2,
\qquad
\varepsilon_Z=\frac14,
\]

on the pure low-turnover strong-tightness corridor,

\[
\boxed{
R_Z<1.19924130\sqrt\nu
\quad\Longrightarrow\quad
\text{branch closed}.
}
\]

### Projective-action / viscous-tax threshold

The smooth projective-action theorem gives, under the compatible quarter-tail projective corridor,

\[
\boxed{
r:=\frac{R_C}{\rho_0}<1.3030842670.}
\]

The radius variable is not the same one and must be converted before comparison.

---

## 2. Analytic restart radius normalization

The projective theorem uses

\[
\boxed{
\rho_0^2
=\frac{\nu/2}{c_*(2)^2},
}
\]

with the conservative bound

\[
\boxed{c_*(2)\ge1.}
\]

Therefore

\[
\boxed{
\rho_0
=\frac{\sqrt\nu}{\sqrt2\,c_*(2)}
\le
\frac{\sqrt\nu}{\sqrt2}.
}
\]

If the common projective/tightness core radius is identified as

\[
R_C=R_Z,
\]

the projective closure condition becomes

\[
R_Z
<
1.3030842670\,ho_0.
\]

Hence

\[
\boxed{
R_Z
<
\frac{1.3030842670}{\sqrt2\,c_*(2)}\sqrt\nu.
}
\]

---

## 3. Maximum projective physical-radius reach

The largest possible converted threshold occurs at the smallest allowed

\[
c_*(2)=1.
\]

Then

\[
\boxed{
\frac{1.3030842670}{\sqrt2}
\approx0.9214197217.
}
\]

Thus even in the most favorable conversion,

\[
\boxed{
R_Z<0.92141973\sqrt\nu
}
\]

is the largest common-radius interval closed by this specific projective certificate.

For

\[
c_*(2)>1,
\]

the converted radius is smaller still.

---

## 4. Compare with the trace-free envelope

The trace-free combined threshold is

\[
1.19924130\sqrt\nu.
\]

The maximal projective converted threshold is

\[
0.92141973\sqrt\nu.
\]

Therefore

\[
\boxed{
0.92141973
<
1.19924130.
}
\]

The difference is

\[
\boxed{
1.19924130-0.92141973
\approx0.27782158.
}
\]

Hence, on the branch where both sets of hypotheses hold at the same common radius,

\[
\boxed{
\text{projective closed radius}
\subset
\text{trace-free/tightness/timing closed radius}.
}
\]

---

## 5. Consequence for branch priority

There is no unresolved common-radius interval of the form

\[
R_{TF}<R_Z<R_{PA}
\]

because

\[
R_{PA}<R_{TF}.
\]

Therefore the projective radius certificate cannot close any additional large-radius portion after M5-194Z on the quarter-tail strong-tightness pure lane.

The radius frontier is simply

\[
\boxed{
R_Z\ge1.19924130\sqrt\nu
}
\]

for any survivor which remains in that pure lane.

---

## 6. Why the projective theorem remains useful

This dominance statement concerns only the **radius envelope under compatible strong-tightness hypotheses**.

The projective-action theorem remains valuable when

- stage-wide vorticity tightness is unavailable;
- the trace-free Dirichlet frequency floor cannot be formed;
- one needs to route recurrent anti-ribbon/eigenframe action to viscous cost;
- a turnover/projective event must be classified rather than bounded by radius;
- the analysis is performed on a different core radius than `R_Z`.

Thus the theorem is not redundant globally. It is redundant only as an additional radius-extension mechanism in the present strong-tightness quarter-tail intersection.

---

## 7. DSD pruning verdict

### CLOSED AS A REDUNDANT SUBROUTE

On the common-radius strong-tightness quarter-tail pure branch, there is no benefit in trying to use the `r<1.30308` projective certificate to extend the scalar radius closure beyond M5-194Z.

### SURVIVING LARGE-RADIUS BRANCH

Any pure survivor satisfies

\[
\boxed{
R_Z\ge1.19924130\sqrt\nu.
}
\]

At that radius, the current priority is no longer projective small-core closure. It is to determine whether such a large normalized enstrophy-support radius necessarily entails

- loss of strong vorticity tightness at a smaller useful radius;
- multicore occupancy;
- variance/boundary turnover;
- remote critical-tail mass;
- or a genuinely single broad coherent core.

---

## 8. Next audit target

The next stage should quantify the **single-broad-core versus multicore/tail dichotomy** at

\[
R_Z\ge1.19924\sqrt\nu.
\]

A useful quantity is the minimal radius containing a fixed enstrophy fraction, for example

\[
R_{1/2}(s)
:=
\inf\left\{
R:
\int_{B_R(X(s))}|\Omega|^2
\ge\frac12 Z(s)
\right\}.
\]

If a large quarter-tail radius is caused only by a small amount of remote enstrophy, `R_{1/2}` may remain small and the stronger tightness certificate can be re-applied at a different tail fraction.

If `R_{1/2}` is itself large, the active enstrophy is genuinely broad or multicore, which should interface with the variance/multiflux/turnover ledgers.

This quantile-radius audit is the next high-leverage scalar reduction.
