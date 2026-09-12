# DSD M19-084 — Temporal analyticity can decay high-frequency boundary coefficients but cannot exclude quasiperiodic or aperiodic recurrent scattering factors

Date: 2026-09-12

Status: **TEMPORAL-ANALYTICITY AUDIT / POSITIVE-TIME PARABOLIC REGULARITY CAN, UNDER UNIFORM STRONG-NORM CONTROL, GIVE ANALYTICITY OF FINITE-RADIUS BOUNDARY OBSERVABLES IN SIMILARITY TIME AND EXPONENTIAL DECAY OF APPROPRIATE FOURIER/BOHR COEFFICIENTS / BUT ANALYTICITY DOES NOT FORCE A SINGLE FREQUENCY, A FINITE FREQUENCY SET, OR AN EXACT PERIOD / EVEN TWO INCOMMENSURATE ANALYTIC FREQUENCIES ALREADY PRODUCE A NONPERIODIC RECURRENT HISTORY, AND UNIFORMLY ANALYTIC ALMOST-PERIODIC FUNCTIONS MAY HAVE COUNTABLY MANY DECAYING FREQUENCIES / THEREFORE TEMPORAL ANALYTICITY REGULARIZES THE LOG-DIFFUSE BRANCH BUT DOES NOT CLOSE THE FACTOR-RIGIDITY PROBLEM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Boundary-history observable

Fix a spectator radius

\[
R_{spec}<\infty.
\]

Let

\[
B(\theta)
\]

denote any finite collection of smooth boundary trace observables of the recurrent similarity solution or of a linearized center witness on \(|y|=R_{spec}\).

The scattering dictionary is

\[
\boxed{
q
=\rho_{spec}-\frac{\theta}{2},
\qquad
\rho_{spec}=\log R_{spec}.
}
\]

Thus temporal frequency at the spectator boundary becomes log-radius oscillation of the scattering datum.

---

## 2. What parabolic analyticity can plausibly provide

For a smooth solution of a parabolic equation with uniformly controlled coefficients on a compact spatial region, positive-time analytic-semigroup theory gives time analyticity in suitable Banach spaces.

Therefore, **conditional on a uniform strong-norm corridor sufficient to keep the analytic radius positive**, one may have a strip

\[
\boxed{
|\operatorname{Im}\theta|<\rho_*>0
}

on which the boundary observable extends holomorphically with a uniform bound.

This is stronger than mere \(C^\infty\) regularity.

However the existence of a uniform strip for the entire recurrent hull must itself be certified from the corridor norms; it is not assumed automatically here.

---

## 3. Periodic case: exponential Fourier decay but no frequency collapse

If a boundary history is periodic with period \(T\), write

\[
B(\theta)
=\sum_{k\in\mathbb Z}\widehat B_k e^{2\pi ik\theta/T}.
\]

Analyticity in a strip of width \(\rho_*\) gives the standard exponential envelope

\[
\boxed{
|\widehat B_k|
\lesssim
 e^{-2\pi\rho_*|k|/T}.
}
\]

But infinitely many nonzero Fourier modes remain compatible with analyticity.

Thus even in the periodic case, analyticity does not reduce the solution to one temporal harmonic.

---

## 4. Quasiperiodic analytic countermodel

Take two incommensurate frequencies

\[
\omega_1/\omega_2\notin\mathbb Q
\]

and define

\[
\boxed{
B(\theta)
=a_1\cos(\omega_1\theta)
+a_2\cos(\omega_2\theta).
}
\]

This function is entire in \(\theta\), bounded on every finite horizontal strip, recurrent, and nonperiodic.

Therefore

\[
\boxed{
\text{analytic}+	ext{bounded}+	ext{recurrent}
\not\Rightarrow
\text{periodic}.
}
\]

Through

\[
q=\rho_{spec}-\theta/2,
\]

this gives an analytic quasiperiodic q-profile.

---

## 5. Infinitely many analytic recurrent frequencies are also possible

More generally, choose frequencies \(\{\lambda_n\}\) and coefficients \(a_n\) with

\[
\sum_n|a_n|e^{\rho_*|\lambda_n|}<\infty.
\]

Then

\[
\boxed{
B(\theta)
=\sum_na_ne^{i\lambda_n\theta}
}
\]

converges uniformly in the strip

\[
|\operatorname{Im}\theta|<\rho_*.
\]

With an appropriate frequency module this can be uniformly almost periodic and recurrent while having a countably infinite Bohr spectrum.

Hence a positive analytic strip can force coefficient decay but does not force a finite-dimensional temporal frequency module.

---

## 6. General recurrent dynamics is even broader than almost periodicity

A compact recurrent Navier--Stokes hull need not be equicontinuous or almost periodic merely because each trajectory is analytic in time.

Analytic finite-dimensional flows can contain complicated recurrent invariant sets, and analytic regularity of the orbit map does not imply pure-point temporal spectrum.

Therefore one must not silently replace

\[
\text{recurrent}
\]

by

\[
\text{quasiperiodic/almost periodic}.
\]

The latter are useful countermodels, not an exhaustive classification.

---

## 7. Effect on the log-diffuse branch

Temporal analyticity can penalize **high temporal frequencies**.

Under the q dictionary, a temporal mode

\[
e^{i\lambda\theta}
\]

becomes

\[
\boxed{
e^{-2i\lambda q}}
\]

up to a constant phase from \(\rho_{spec}\).

Thus an analytic strip gives decay of large-q-frequency coefficients in settings where a Fourier/Bohr expansion is legitimate.

But the M19-083 log-diffuse branch is not necessarily a high-frequency branch.

It may spread mass over many q-locations/phases using low or moderate frequencies, or even two incommensurate frequencies.

Therefore

\[
\boxed{
\text{frequency decay}
\not\Rightarrow
\text{log-radius concentration}.
}
\]

---

## 8. Analyticity does not create an order-one inter-q diffusion

M19-083 identified the missing mechanism as an order-one coupling that mixes different q-labels.

Time analyticity is a regularity property, not such a mixing term.

The leading critical equation still transports q as a characteristic invariant, and the actual remote correction remains \(R^{-2}\)-suppressed.

Therefore analyticity does not alter the leading factor dynamics

\[
A_{\sigma_tY}(q)=A_Y(q-t/2).
\]

---

## 9. What analyticity can safely add to the corridor

If a uniform analytic strip is certified, it can be used to:

1. obtain quantitative temporal derivative bounds;
2. control truncation error of finite temporal-frequency approximations;
3. prevent arbitrarily large high-frequency temporal oscillation at fixed amplitude;
4. strengthen local compactness of boundary histories.

It cannot, by itself, certify:

1. exact periodicity;
2. finite Bohr spectrum;
3. one-dimensional center;
4. absence of an aperiodic translation factor.

---

## 10. Revised diffuse-factor firewall

\[
\boxed{
\text{uniform temporal analyticity}
\neq
\text{temporal spectral discreteness of finite rank}
}
\]

and

\[
\boxed{
\text{exponential high-frequency decay}
\neq
\text{periodicity or q-concentration}.
}
\]

This blocks a common shortcut from parabolic smoothing to finite-dimensional recurrent dynamics.

---

## 11. What kind of new theorem would actually help

To reduce the factor one needs a PDE-specific statement about the **frequency module or recurrent spectrum**, not merely coefficient decay.

For example, any one of the following would be genuinely new:

\[
\boxed{
\text{all nonzero temporal spectral values of the rotation-transverse cocycle have Re}\,\lambda<0,
}
\]

or

\[
\boxed{
\text{the center Sacker--Sell spectrum consists only of the symmetry value }0,
}
\]

or an observability theorem forcing every nontrivial recurrent boundary history to pay a resource incompatible with the original parent.

None is currently certified.

---

## 12. Next calculation

M19-085 should return to the linear cocycle and test whether the time derivative hierarchy itself creates a quantitative center-frequency penalty.

For a hypothetical oscillatory center component with temporal scale \(\lambda\), the equation gives

\[
\partial_\theta W=L(\theta)W.
\]

Repeated time derivatives can be converted into spatial derivatives and coefficient commutators. The audit should determine whether a high temporal-frequency center necessarily escalates into the already controlled high-spatial-derivative branch, while leaving low-frequency quasiperiodic center as the genuine residue.
