# DSD Audit: Barker--Prange cubic logarithmic rate correction

Date: 2026-08-26

Status: **CRITICAL AUDIT CORRECTION / THE PREVIOUS BOUNDED-Z + UNIFORM WEAK-L3 EXCLUSION GATE IS INVALID / THE COHERENT PERMANENT-EXPORT BRANCH CLOSED THROUGH THAT GATE IS REOPENED / INTERNAL WEAK-L3 AND SHELL ESTIMATES REMAIN USABLE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

This note audits the use of Barker--Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Commun. Math. Phys. 385 (2021), 717--792.

The repository previously recorded the external lower bound as though it were

\[
\|u(t)\|_{L^3(B_R)}\gtrsim C(M)\log\frac1{T^*-t}.
\]

That reading is too strong.

The theorem-level quantitative formula is a lower bound for the **cubic integral**

\[
\boxed{
\int_{B_R}|u(x,t)|^3\,dx
\gtrsim
c(M)\log\frac1{T^*-t}
}
\]

on an admissible ball with radius slightly larger than the parabolic scale under the Type-I hypothesis

\[
\|u\|_{L_t^\infty L_x^{3,\infty}}\le M.
\]

Equivalently,

\[
\boxed{
\|u(t)\|_{L^3(B_R)}
\gtrsim
c(M)^{1/3}
\left(\log\frac1{T^*-t}\right)^{1/3}.
}
\]

The paper also states that this logarithmic cubic growth is optimal for a class of potential nonzero backward discretely self-similar scenarios.

## 2. Internal weak-L3 upper bound

The previous endpoint-gate note correctly derived the distribution estimate

\[
\mu_E(\lambda)
\le
\min\{|E|,M^3\lambda^{-3}\}
\]

from a weak-L3 ceiling

\[
\|U\|_{L^{3,\infty}}\le M.
\]

With an independent pointwise ceiling

\[
\|U\|_\infty\le K_\infty,
\]

layer cake gives

\[
\boxed{
\int_E|U|^3
\le
M^3+3M^3
\log\left(\frac{K_\infty |E|^{1/3}}{M}\right)_+.
}
\]

For a ball of normalized radius R,

\[
\boxed{
\int_{B_R}|U|^3
\lesssim
C(M,K_\infty)(1+\log R).
}
\]

This internal calculation remains valid.

## 3. Correct comparison of logarithmic orders

For the Barker--Prange admissible physical radius

\[
\mathcal R(t)
=O((T^*-t)^{1/2-\delta}),
\]

the corresponding Leray radius obeys

\[
R(t)\lesssim (T^*-t)^{-\delta}.
\]

Therefore

\[
\log R(t)
\lesssim
\delta\log\frac1{T^*-t}+O(1).
\]

The internal weak-L3 upper bound is consequently

\[
\boxed{
\int_{B_{R(t)}}|U|^3
\lesssim
C(M,Z_+)
\log\frac1{T^*-t}.
}
\]

The external singularity lower bound is

\[
\boxed{
\int_{B_{R(t)}}|U|^3
\gtrsim
c(M)
\log\frac1{T^*-t}.
}
\]

These have the **same logarithmic order**.

There is no exponent contradiction.

No inequality between the two constants has been proved that would force a contradiction.

Hence

\[
\boxed{
\text{uniform weak-}L^3
+
\text{bounded normalized enstrophy}
\not\Rightarrow
\text{contradiction by Barker--Prange alone}.
}
\]

## 4. Why the old contradiction appeared

The previous note compared

\[
\|u(t)\|_{L^3}
\lesssim (\log(1/(T^*-t)))^{1/3}
\]

against an incorrectly transcribed lower bound

\[
\|u(t)\|_{L^3}
\gtrsim \log(1/(T^*-t)).
\]

The correct lower bound after taking the cube root is also of order

\[
(\log(1/(T^*-t)))^{1/3}.
\]

Thus the apparent gap was created entirely by confusing

\[
\int |u|^3
\]

with

\[
\|u\|_3.
\]

This is a theorem-transcription error, not a defect in Barker--Prange.

## 5. Dependency audit

The following conclusions are therefore invalidated if their only terminal closure was the erroneous endpoint gate:

1. `DSD_BOUNDED_Z_WEAK_L3_ENDPOINT_EXCLUSION_GATE_2026-08-25.md` -- terminal exclusion invalid.
2. `DSD_COHERENT_PERMANENT_EXPORT_WEAK_L3_CLOSURE_2026-08-25.md` -- the final S-closure step is invalid; the preceding flux/coherence/overlap estimates remain useful.
3. Any later branch marked closed solely because it produced a uniform weak-L3 bound must be reopened until an independent closure is supplied.

The following ingredients survive the audit:

- bounded vorticity amplitude + bounded enstrophy implies a velocity Linfinity ceiling;
- weak-L3 + Linfinity implies at most logarithmic growth of the cubic integral on large balls;
- coherent bounded-flux separated critical cohorts can produce a uniform weak-L3 field;
- positive-density critical shell towers are compatible with logarithmic cubic growth;
- Barker--Prange gives a matching logarithmic **lower** scale for a Type-I singularity.

## 6. Consequence for the W1 periodic survivor

The periodic canonical tail

\[
T(Y,s)
=|Y|^{-1}
\Phi\left(\widehat Y,\log|Y|-s/2\right)
\]

is therefore not in conflict with Barker--Prange merely because

\[
T\in L^{3,\infty}\setminus L^3.
\]

Indeed one DSS log cell carries order-one cubic mass, so a tower of N cells gives

\[
\int |T|^3\sim N
\sim \log R,
\]

which is exactly the logarithmic order appearing in the quantitative Type-I theorem.

Thus the critical DSS tail is an endpoint saturation model, not something excluded by that theorem.

## 7. Corrected frontier

The proof attempt must return to a genuinely dynamical obstruction.

The currently valid periodic reduction is

\[
\boxed{
U=B_R+Q_R,
\qquad
B_R\sim r^{-1},
\qquad
Q_R\in L^2\cap L^3,
}
\]

with the canonical tail and forced quotient described in the 2026-08-26 quotient notes.

But uniform weak-L3 of the tail is no longer a contradiction.

The remaining routes must instead use at least one of:

\[
\boxed{
\begin{aligned}
&\text{core--tail injection rigidity},\\
&\text{nonlinear interface/turnover cost},\\
&\text{a valid critical functional with a one-sided dynamical bound},\\
&\text{a Liouville/backward-uniqueness theorem whose hypotheses actually include the W1 endpoint},\\
&\text{or an independent exclusion of periodic/aperiodic recurrent Leray dynamics.}
\end{aligned}
}
\]

## 8. DSD audit verdict

This correction is beneficial to the proof audit even though it reopens a branch.

The DSD rule here is straightforward:

\[
\boxed{
\text{same symbol family or same qualitative word ``logarithmic''}
\not\Rightarrow
\text{same mathematical quantity}.
}
\]

The external theorem's object, power, domain, and scaling must be preserved exactly before it is inserted into an internal ledger.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]