# DSD W1 Critical Gaussian Bernoulli Replenishment Collapse

Date: 2026-08-26

Status: **FORMER A--E ENDGAME COLLAPSED TO ONE SCALE-CRITICAL GAUSSIAN BERNOULLI-REPLENISHMENT GATE / H2 TAIL RETIRED AS AN INDEPENDENT TERMINAL BRANCH / EXACT WEIGHTED p=3 IDENTITY DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The preceding Gaussian relative-variance note reduced the former A/B/D/E recurrent-core questions to one positive-mean mechanical replenishment requirement, leaving the remote critical H2 tail C as a separate proof-management branch.

The remaining mismatch was that the Gaussian L2 relative-energy ledger is not scale critical in physical variables. A fixed normalized event at Leray time s carries only physical energy of order exp(-s/2), so infinitely many such events are compatible with finite kinetic energy. This is the familiar half-power barrier.

The correct common observable is the p=3 Gaussian ledger. It is scale critical and remains meaningful irrespective of whether the far H2 critical quantity is bounded or unbounded.

This note derives that ledger and shows that the apparent material and pressure source terms collapse further to one Bernoulli-gradient source.

---

## 2. Leray equation and Gaussian critical mass

Use

\[
\partial_sU-
u\Delta U+(U\cdot\nabla)U
+\frac12U+\frac12(Y\cdot\nabla)U+\nabla P=0,
\qquad \nabla\cdot U=0.
\]

For a>0 let

\[
\phi_a(Y)=e^{-a|Y|^2}.
\]

Define

\[
E_{3,a}(U):=\int_{\mathbb R^3}\phi_a|U|^3\,dY
\]

and

\[
D_{3,a}(U):=
\int\phi_a\left[
|U||\nabla U|^2
+|U|^{-1}\sum_j(U\cdot\partial_jU)^2
\right]dY.
\]

At U=0 the second integrand is interpreted by its continuous nonnegative extension, bounded by |U||grad U|^2.

---

## 3. Exact weighted p=3 identity

Test the Leray equation with

\[
\phi_a f_3,
\qquad
f_3:=|U|U.
\]

The time term is

\[
\frac13\frac d{ds}E_{3,a}.
\]

The viscous term is

\[
\nu D_{3,a}
-\frac\nu3\int(\Delta\phi_a)|U|^3.
\]

The convection term is

\[
-\frac13\int |U|^3U\cdot\nabla\phi_a.
\]

The +U/2 and dilation terms cancel at the unweighted p=3 critical exponent, leaving only

\[
-\frac16\int |U|^3Y\cdot\nabla\phi_a.
\]

The pressure term is

\[
-\int P\,\nabla\cdot(\phi_a|U|U).
\]

Therefore

\[
\boxed{
\frac13E_{3,a}'
+\nu D_{3,a}
+\int\left[
-\frac\nu3\Delta\phi_a
-\frac16Y\cdot\nabla\phi_a
\right]|U|^3
=\mathcal F_{3,a},
}
\]

where

\[
\boxed{
\mathcal F_{3,a}
:=
\frac13\int |U|^3U\cdot\nabla\phi_a
+\int P\,\nabla\cdot(\phi_a|U|U).
}
\]

The pressure contribution is gauge invariant because the integral of the divergence of the rapidly decaying vector field phi_a |U| U vanishes.

---

## 4. Match the Gaussian to viscosity and Leray dilation

For the Gaussian,

\[
\Delta\phi_a=(-6a+4a^2|Y|^2)\phi_a,
\qquad
Y\cdot\nabla\phi_a=-2a|Y|^2\phi_a.
\]

Hence

\[
-\frac\nu3\Delta\phi_a
-\frac16Y\cdot\nabla\phi_a
=
\left[
2a\nu+
\frac a3(1-4a\nu)|Y|^2
\right]\phi_a.
\]

Thus every

\[
0<a\le\frac1{4\nu}
\]

gives a nonnegative confinement potential.

Choose the same matched value as in the Gaussian L2 ledger,

\[
\boxed{a=\frac1{8\nu}.}
\]

Then

\[
2a\nu=\frac14,
\qquad
\frac a3(1-4a\nu)=\frac1{48\nu}.
\]

The exact identity becomes

\[
\boxed{
\frac13E_{3,a}'
+\nu D_{3,a}
+\frac14E_{3,a}
+\frac1{48\nu}\int |Y|^2\phi_a|U|^3dY
=\mathcal F_{3,a}.
}
\]

Every term on the left except the time derivative is nonnegative.

---

## 5. Material and pressure collapse to Bernoulli work

Use the vector identity

\[
(U\cdot\nabla)U
=\omega\times U+\nabla\frac{|U|^2}{2}.
\]

Because f_3=|U|U is parallel to U,

\[
f_3\cdot(\omega\times U)=0.
\]

Define the Bernoulli scalar

\[
\boxed{B:=P+\frac12|U|^2.}
\]

The convection and pressure contributions therefore combine exactly into

\[
\boxed{
\mathcal F_{3,a}
=\int B\,\nabla\cdot(\phi_a|U|U)dY
=-\int\phi_a|U|U\cdot\nabla B\,dY.
}
\]

Thus the final critical source is not two independent material/pressure mechanisms. It is one gauge-invariant Bernoulli-gradient work channel.

The vortex-force part of the nonlinearity is exactly orthogonal to the p=3 test direction and cannot pay this ledger directly.

---

## 6. Positive critical-mass floor on a nontrivial minimal W1 set

Let M be a nontrivial compact minimal W1 invariant set.

For every U in M,

\[
E_{3,a}(U)>0.
\]

If E_{3,a}=0, positivity of phi_a gives U=0 everywhere, which is the excluded equilibrium.

The Gaussian weighted observable is continuous on the W1 compact topology: local smooth convergence handles bounded sets and the Gaussian suppresses the uniformly controlled p>3 tail.

Hence compactness gives

\[
\boxed{E_{3,a,*}:=\min_{U\in M}E_{3,a}(U)>0.}
\]

This conclusion does not require any assumption on the remote critical H2 shell quantity.

---

## 7. Invariant-measure critical replenishment

Let mu be any invariant probability measure supported on M. Averaging the exact p=3 Gaussian identity gives

\[
\boxed{
\langle\mathcal F_{3,a}\rangle_\mu
=
\nu\langle D_{3,a}\rangle_\mu
+\frac14\langle E_{3,a}\rangle_\mu
+\frac1{48\nu}
\left\langle\int |Y|^2\phi_a|U|^3dY\right\rangle_\mu.
}
\]

Therefore

\[
\boxed{
\langle\mathcal F_{3,a}\rangle_\mu
\ge\frac14E_{3,a,*}
=:c_{3,a}>0.
}
\]

Equivalently,

\[
\boxed{
-\left\langle
\int\phi_a|U|U\cdot\nabla B
\right\rangle_\mu
\ge c_{3,a}>0.
}
\]

Every nontrivial compact minimal W1 survivor must therefore sustain strictly positive mean critical Bernoulli-gradient replenishment in the finite Gaussian core.

---

## 8. Positive mean gives syndetic fixed critical-action events

On the smooth compact W1 class the Gaussian Bernoulli functional F_{3,a} is continuous after fixing any harmless pressure gauge. It is bounded on M.

Since its invariant mean is positive, a nonempty open state-space set exists on which

\[
\mathcal F_{3,a}>c_{3,a}/2.
\]

Minimality gives relatively dense returns of every orbit to that open set. Uniform local smooth compactness supplies a fixed short persistence time after a slightly stronger threshold is entered.

Hence every orbit in M has event intervals J_k with bounded Leray-time gaps and

\[
\boxed{
\int_{J_k}\mathcal F_{3,a}(s)ds
\ge A_{3,a}>0.
}
\]

Unlike the L2 Gaussian action, this p=3 action is scale critical under the inverse Navier--Stokes scaling. It is therefore the appropriate object for the final source-chain analysis.

This divergence of cumulative critical action is necessary for a singular survivor and is not, by itself, a contradiction with known regularity theory.

---

## 9. Collapse of the former A--E frontier

The former branches were:

A. principal-axis locking / positive-middle transition;
B. constant-vorticity-amplitude finite-order contact;
C. remote critical H2 derivative/subscale escape;
D. periodic finite renormalized core;
E. aperiodic minimal trajectory rigidity.

The critical Gaussian ledger requires none of these distinctions.

- A and B describe local geometry inside a state that must pay the same Bernoulli critical work.
- D and E describe the temporal topology of recurrence; minimality alone is sufficient for recurrent critical-action events.
- C describes one possible remote derivative failure. It does not evade the finite Gaussian p=3 ledger, so it is no longer a separate terminal proof obligation. It remains a useful H-diagnostic route if activated.

Therefore the W1 endgame is reorganized as

\[
\boxed{
W1_{min}^{nontrivial}
\Longrightarrow
\mathcal R_{B,3}^{crit},
}
\]

where

\[
\boxed{
\mathcal R_{B,3}^{crit}:
\quad
\text{syndetically recurrent fixed positive Gaussian Bernoulli-gradient action.}
}
\]

The former five terminal tasks are retired as independent endgame branches.

---

## 10. Relation to the old remote H2 / conveyor dichotomy

The old H2-critical tail branch and the coherent 1/r log-radius conveyor remain valid diagnostics of how a W1 survivor may organize its remote field.

They no longer define separate final obligations because the critical Gaussian Bernoulli gate is local, exact, and unavoidable in either case.

If the final Bernoulli source-chain forces activity to move outward, the old dichotomy can be reused downstream:

\[
\text{scale-coherent outward chain}
\to
\text{critical log-radius conveyor},
\]

while loss of scale coherence routes to

\[
H_{2,crit}^{tail}/\text{remote subscale derivative activity}.
\]

Thus H2 and the conveyor become two realizations of one source-chain endpoint rather than two independent primary branches.

---

## 11. Important anti-proof

Positive recurrent critical action is not already a contradiction.

Indeed the previously derived physical scaling gives

\[
\int D_{3,phys}(t)dt
=\int D_3(U(s))ds,
\]

and a singular survivor is expected to have divergent critical Serrin-type action. The present Gaussian identity supplies a sharper structural description of the required source of that divergence, not a proof that the divergence is impossible.

The remaining theorem must attack the Bernoulli source-chain itself.

---

## 12. New single frontier

The proof-management frontier is now one object:

\[
\boxed{
\mathcal R_{B,3}^{crit}.
}
\]

The next source-chain question is:

\[
\boxed{
\text{Can an unforced finite-energy prelimit Navier--Stokes blow-up corridor sustain}
\\
\text{syndetically recurrent fixed scale-critical inward Bernoulli work}
\\
\text{at every late Leray epoch, without the source chain becoming either}
\\
\text{a coherent critical log-radius conveyor or a remote derivative-subscale H event?}
}
\]

If one proves that every such source chain must enter one of those two endpoint geometries, the remaining task becomes a single endpoint rigidity problem rather than five independent local/dynamical problems.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
