# DSD W1 Periodic DSS Literature-Boundary Audit

Date: 2026-08-26

Status: **PERIODIC W1 TERMINAL CLASS PLACED AGAINST KNOWN DSS / WEAK-L3 RESULTS / NEAR-IDENTITY DSS FACTORS ARE COVERED BY EXISTING REMOVAL RESULTS, BUT THE ARBITRARY-FACTOR LARGE WEAK-L3 BACKWARD DSS SCENARIO IS NOT GENERALLY CLOSED BY THE LITERATURE CHECKED HERE / GLOBAL REGULARITY UNPROVED.**

## 1. W1 periodic terminal class

The current periodic branch yields a canonical physical trace

\[
u_*(x)
=
\frac1{|x-X_*|}
\Phi\bigl(\widehat{x-X_*},\log|x-X_*|\bigr),
\]

with a discrete factor

\[
\lambda=e^{S/2}>1.
\]

It is locally

\[
u_*\in L^2_{loc}\cap L^{3,\infty}_{loc},
\]

but for a nonzero occupied log-periodic tail

\[
u_*\notin L^3_{loc},
\qquad
u_*\notin H^1_{loc}.
\]

Thus strong-`L3` endpoint removal theorems do not apply directly.

---

## 2. Near-identity DSS removal

Chae and Wolf, *Removing discretely self-similar singularities for the 3D Navier--Stokes equations* (Communications in Partial Differential Equations, 2017), prove removal of the DSS singularity when the scaling parameter `lambda` is sufficiently close to `1` under their scenario.

Therefore the W1 periodic branch is already incompatible with that theorem if its derived

\[
\lambda=e^{S/2}
\]

falls inside the near-identity exclusion regime together with the theorem's hypotheses.

However W1 currently only gives

\[
S>h_0,
\qquad
\lambda>e^{h_0/2},
\]

and does not force `lambda` into the near-1 regime.

So this result closes only a subrange of the periodic factor space, not the full W1 periodic branch.

---

## 3. Arbitrary-factor backward DSS remains the relevant open boundary

Barker and Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration* (Communications in Mathematical Physics, 2021), explicitly analyze potential nonzero backward discretely self-similar solutions and use them to show sharpness of a Type-I spatial-concentration lower bound under specified decay/integrability assumptions.

Their discussion treats the existence of nonzero backward DSS solutions as an open scenario rather than a generally excluded class.

This is consistent with the W1 endpoint:

\[
\boxed{
\text{arbitrary-factor backward DSS}
+
\text{critical weak-`L3` behavior}
}
\]

is precisely where the present periodic branch resides after all stronger tails have been removed.

---

## 4. Large weak `L3` does not automatically imply regularity

Known results for

\[
L_t^\infty L_x^{3,\infty}
\]

provide substantial local information and singular-point restrictions, but the large weak-`L3` endpoint is not the same as the strong `L3` endpoint of Escauriaza--Seregin--Sverak.

The W1 terminal trace is therefore not removed merely by observing

\[
u_*\in L^{3,\infty}_{loc}.
\]

Its exact `1/r` behavior is a genuine endpoint obstruction.

---

## 5. DSD consequence

The literature boundary confirms that the current proof obligation is not an already-solved stationary or strong-`L3` Liouville problem.

The unresolved object is more specific:

\[
\boxed{
\text{an arbitrary-factor critical DSS trace}
\text{ dynamically attached to one unforced finite-energy parent}.
}
\]

This validates the internal DSD routing toward a **parent/interface theorem** rather than another far-tail Liouville theorem.

A successful result must use information absent from a standalone backward DSS profile, such as

- finite-energy ancestry;
- exact core--trace matching;
- terminal convergence rate;
- the Lamb projection--cascade identity;
- or a nonrepeatability property of the finite-energy quotient.

---

## 6. Current proof map

The periodic branch can now be summarized as

\[
\boxed{
P_{DSS}^{long}
\Longrightarrow
\begin{cases}
\text{canonical }1/r\text{ log-periodic terminal trace},\\
\text{strong convergence on fixed punctured annuli},\\
\text{finite local }L^2\text{ but critical weak }L^3,\\
\text{finite-energy divergence-free quotient},\\
\text{critical Lamb projection/amplitude/frequency cascade}.
\end{cases}
}
\]

Existing near-identity DSS removal results do not cover the arbitrary-factor endpoint in general.

Therefore the remaining periodic proof target is

\[
\boxed{
\text{finite-energy parent} + \text{critical DSS trace}
\Longrightarrow
\text{contradiction}
}
\]

under the exact W1 interface data.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
