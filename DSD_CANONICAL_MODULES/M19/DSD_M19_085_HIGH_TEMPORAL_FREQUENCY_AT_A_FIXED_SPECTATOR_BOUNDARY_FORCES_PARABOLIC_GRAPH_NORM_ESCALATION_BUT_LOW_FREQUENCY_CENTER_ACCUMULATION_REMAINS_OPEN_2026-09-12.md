# DSD M19-085 — High temporal frequency at a fixed spectator boundary forces parabolic graph-norm escalation, but low-frequency center accumulation remains open

Date: 2026-09-12

Status: **CENTER-FREQUENCY AUDIT / ON A FIXED FINITE SPECTATOR REGION, LARGE TEMPORAL OSCILLATION OF A LINEARIZED CENTER WITNESS REQUIRES LARGE PARABOLIC GRAPH NORM—SECOND SPATIAL DERIVATIVES, FIRST-DERIVATIVE TRANSPORT, COEFFICIENT STRAIN, OR PRESSURE / THEREFORE A UNIFORM STRONG CORRIDOR CAN SUPPRESS HIGH TEMPORAL FREQUENCIES OR FORCE THEM INTO AN EXISTING DERIVATIVE/PRESSURE EXIT / THIS STATEMENT IS NOT GLOBAL IN RADIUS: AT REMOTE SCALES LOG-RADIAL TRANSPORT y·GRAD CARRIES q-FREQUENCY WITHOUT A FIXED PHYSICAL-DERIVATIVE COST / AFTER HIGH-FREQUENCY PRUNING, THE GENUINE RESIDUE IS A LOW-FREQUENCY/NEAR-ZERO CENTER SPECTRUM THAT MAY STILL BE QUASIPERIODIC OR APERIODIC / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Linearized equation on a fixed finite region

After rotation modulation, the linearized similarity equation is

\[
\partial_\theta W
=
\nu\Delta W
-\frac12y\cdot\nabla W
-\frac12W
-(U\cdot\nabla)W
-(W\cdot\nabla)U
-\nabla Q,
\]

\[
\nabla\cdot W=0.
\]

Fix a finite spectator region

\[
K\Subset K^+\Subset\mathbb R^3
\]

containing the sphere \(|y|=R_{spec}\).

On \(K^+\), the coefficient \(|y|\) is bounded by a fixed constant.

---

## 2. Local graph-norm estimate

Standard localization and pressure estimates give schematically

\[
\boxed{
\|\partial_\theta W\|_{L^2(K)}
\le
C_K\Big[
\nu\|D^2W\|_{L^2(K^+)}
+(1+\|U\|_{L^\infty(K^+)})\|\nabla W\|_{L^2(K^+)}
+\|\nabla U\|_{L^\infty(K^+)}\|W\|_{L^2(K^+)}
+\|\nabla Q\|_{L^2(K^+)}
\Big].
}
\]

Using the divergence constraint and the linearized pressure equation, the pressure term can itself be estimated by the appropriate local/nonlocal Calderon--Zygmund norm of

\[
U\otimes W+W\otimes U.
\]

Thus a large time derivative at the fixed spectator boundary cannot appear without a large parabolic graph norm somewhere in the controlled finite region or its pressure coupling.

---

## 3. Periodic or Bohr frequency interpretation

If a boundary component contains an approximately isolated temporal harmonic

\[
W(\theta)\sim e^{i\lambda\theta}\Phi
\]

on the fixed finite region, then

\[
\|\partial_\theta W\|
\sim
|\lambda|\|W\|.
\]

The graph estimate implies

\[
\boxed{
|\lambda|\|W\|_{L^2(K)}
\lesssim
\|W\|_{graph(K^+)}.
}
\]

Therefore a corridor with a uniform graph-norm-to-amplitude ratio bounds the admissible temporal frequencies.

Equivalently, if

\[
|\lambda_n|\to\infty
\]

while the boundary amplitude does not vanish fast enough, then one of the derivative/pressure quantities must escalate.

---

## 4. High-frequency branch remerges with existing exits

Hence at fixed spectator radius,

\[
\boxed{
\text{persistent high temporal frequency}
\Longrightarrow
\text{high }D^2W
\lor
\text{high }D^1W
\lor
\text{coefficient/strain escalation}
\lor
\text{pressure escalation}.
}
\]

These are not new root types.

They return to the derivative-frequency, coefficient, or pressure branches already present in the historical M17--M19 audits.

Thus high temporal frequency is not expected to be the final weak-critical survivor on the compact strong corridor.

---

## 5. Global-radius firewall

The previous estimate is valid because \(K\) is fixed.

At remote radius \(R\), a log-radius mode

\[
B(q)\sim e^{i\mu q}
\]

has physical radial derivative

\[
\partial_r
\sim
\frac{i\mu}{r}.
\]

Meanwhile the similarity drift contains

\[
\frac12y\cdot\nabla
\sim
\frac12\partial_q.
\]

Thus temporal/log-scale frequency \(\mu\) can be order one while the physical gradient cost is only

\[
O(\left|\mu\right|/R).
\]

Even large \(\mu\) can be partially hidden by moving to larger \(R\).

Therefore one must not infer a global estimate

\[
|\lambda|\lesssim \|D^2W\|/\|W\|
\]

uniformly over all similarity radii.

This is exactly the remote q-translation firewall.

---

## 6. What uniform temporal analyticity adds

If M19-084's conditional uniform analytic strip is available at the fixed spectator boundary, then high-frequency coefficients decay exponentially.

M19-085 gives the PDE reason behind that behavior: large temporal frequency requires large graph norm, and analytic regularity controls the derivative hierarchy.

However neither statement excludes infinitely many frequencies accumulating in a bounded interval.

---

## 7. The remaining low-frequency problem

After pruning high frequencies, the center factor may still have frequencies

\[
\lambda_n\to0
\]

or several incommensurate bounded frequencies.

These do not force graph-norm escalation.

For example,

\[
B(\theta)=\cos\theta+\varepsilon\cos(\sqrt2\,\theta)
\]

is analytic, recurrent, nonperiodic, and uses only order-one frequencies.

More dangerously, a sequence of small frequencies can produce arbitrarily slow phase drift while remaining inside all fixed finite derivative bounds.

Hence

\[
\boxed{
\text{high-frequency pruning}
\not\Rightarrow
\text{factor rigidity}.
}

---

## 8. Spectral reformulation

The active center question can now be sharpened from arbitrary spectrum to the near-zero window.

Let \(\Sigma_c\) denote the rotation-transverse Sacker--Sell/Lyapunov center spectrum.

The derivative audit suggests that far from zero, spectral activity either decays or pays a strong derivative/pressure cost.

The genuine survivor is therefore

\[
\boxed{
\Sigma_c\cap[-\lambda_*,\lambda_*]
}

for a finite corridor-dependent \(\lambda_*\), with particular emphasis on accumulation at zero.

The known exact time tangent occupies zero.

The missing theorem is that no second independent zero/near-zero recurrent direction survives.

---

## 9. Certified conclusion

\[
\boxed{
\text{fixed-boundary high temporal frequency}
\Rightarrow
\text{parabolic graph-norm escalation or coefficient/pressure exit}.
}

But

\[
\boxed{
\text{low-frequency quasiperiodic/aperiodic center}
\text{ remains open}.
}

This is genuine progress because it localizes the spectral difficulty to the near-zero center rather than the entire temporal frequency axis.

---

## 10. Next calculation

M19-086 should test the \(\lambda\to0\) regime directly.

A sequence of normalized center witnesses with temporal frequency tending to zero should, after compact local extraction, approach a solution of the **frozen/zero-frequency linearized equation** along recurrent phases.

The key question is whether such a limit is an actual infinitesimal symmetry—time/rotation—or whether the nonautonomous background prevents freezing.

This is the most direct route to a center-gap theorem near zero.
