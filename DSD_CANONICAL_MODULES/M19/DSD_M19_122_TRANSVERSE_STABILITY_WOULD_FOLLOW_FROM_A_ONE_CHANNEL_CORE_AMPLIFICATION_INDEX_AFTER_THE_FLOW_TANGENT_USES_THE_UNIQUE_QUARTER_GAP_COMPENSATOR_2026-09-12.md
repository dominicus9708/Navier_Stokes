# DSD M19-122 — Transverse stability would follow from a one-channel core-amplification index after the flow tangent uses the unique quarter-gap compensator

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE TRANSVERSE-LYAPUNOV PROBLEM REDUCED TO AN INDEX QUESTION FOR THE COMPACT CORE AMPLIFICATION OPERATOR / IF ONLY ONE NONNEGATIVE QUARTER-GAP-COMPENSATING CHANNEL EXISTS AND IT IS THE FLOW TANGENT, THEN ALL SYMMETRY-TRANSVERSE EXPONENTS ARE NEGATIVE / THE REQUIRED INDEX-ONE STATEMENT IS NOT YET PROVED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Flow tangent already supplies one zero-growth channel

For every nonstationary similarity orbit,

\[
Z_t:=\partial_sU
\]

solves the linearized equation.

Its vorticity

\[
\eta_t:=\partial_s\Omega
\]

has Lyapunov exponent zero along a bounded recurrent orbit.

Therefore the quarter-gap identity gives

\[
\boxed{
\left\langle
\frac{\mathcal C_U[Z_t]}{\|\eta_t\|_2^2}
\right\rangle
=
\frac14
+\nu
\left\langle
\frac{\|\nabla\eta_t\|_2^2}{\|\eta_t\|_2^2}
\right\rangle.
}
\]

Thus at least one compact-core amplification channel is dynamically used to neutralize the bare quarter-gap whenever the orbit is genuinely time-dependent.

For an equilibrium/RSS quotient state the analogous statement is interpreted after the symmetry/group tangent bookkeeping.

---

## 2. Spectral-count formulation

Let

\[
N_{\ge0}^{\perp}
\]

denote the number of symmetry-transverse nonnegative Lyapunov exponents counted with multiplicity.

M19-121 shows every such channel requires one quarter of compact-core Ky-Fan budget.

Suppose one can prove the **one-channel amplification-index statement**:

\[
\boxed{
\dim E^{\ge0}_{quot}=1
}
\]

for a nonstationary quotient orbit, where the unique nonnegative direction is the flow tangent.

Then immediately

\[
\boxed{
E^{\ge0}_{\perp}=\{0\},
\qquad
\lambda_{top}^{\perp}<0.
}
\]

This is exactly the corrected transverse-stability theorem of M19-120.

---

## 3. An operator-index sufficient condition

Let

\[
\mathcal B_s
:=
\mathcal K_s^{sym}
-\nu(-\Delta)_{form}
\]

schematically denote the compact-core symmetric amplification after the favorable gradient contribution is included at quadratic-form level.

The instantaneous vorticity growth form is

\[
\mathfrak q_s(\eta)
=
-\frac14\|\eta\|_2^2
+\langle\eta,\mathcal B_s\eta\rangle.
\]

If the long-time cocycle has only one independent direction whose averaged quadratic form can reach zero, then the flow tangent exhausts the nonnegative spectrum.

A strong sufficient instantaneous condition would be:

\[
\boxed{
\lambda_2(\mathcal B_s)<\frac14
\quad\text{uniformly in }s,
}
\]

where `lambda_2` is the second eigenvalue above the essential negative background after exact symmetries are accounted for.

Then every two-dimensional quotient plane has strictly negative area-growth contribution, and since one zero exponent is already present,

\[
\boxed{
\lambda_2^{Lyap}<0.
}
\]

Hence all transverse exponents are negative.

---

## 4. Averaged weaker condition

Uniform instantaneous ordering is stronger than necessary.

The natural weaker target is the two-channel Ky-Fan inequality

\[
\boxed{
\left\langle
\lambda_1^+(s)+\lambda_2^+(s)
\right\rangle
<
\frac12
+
u
\left\langle
\|\nabla\eta_1\|_2^2+\|\nabla\eta_2\|_2^2
\right\rangle
}
\]

for every invariant two-plane containing the flow tangent and one transverse candidate.

Because the time tangent has exponent zero, negativity of the two-volume exponent implies the second exponent is negative.

Thus only a **two-channel** estimate is needed to eliminate the first transverse unstable/neutral direction.

Once the top transverse exponent is negative, all lower transverse exponents are automatically negative.

---

## 5. Why incompressibility alone does not prove index one

The pointwise strain tensor is trace-free, but a trace-free `3 x 3` symmetric matrix may have two positive eigenvalues.

Therefore

\[
\operatorname{tr}S=0
\]

does not imply that only one perturbation direction can be amplified.

Moreover the full compact-core operator includes nonlocal Biot--Savart/gradient-of-vorticity couplings, so its spectral index is not simply the pointwise Morse index of `S`.

Hence

\[
\boxed{
\text{incompressibility}
\not\Rightarrow
\text{one-channel core amplification}.
}
\]

---

## 6. Relation to CE-H alignment

On the exact CE-H branch the base vorticity direction is a strain eigenvector and the transverse strain plane is invariant.

This provides additional geometry beyond generic incompressibility, but it still does not immediately imply an index-one linearized amplification operator.

The nonlocal terms and the possibility of one additional positive transverse strain eigenvalue must be retained.

Thus any CE-H-based index theorem must be proved at the **linearized operator** level, not inferred solely from the base-flow eigenframe.

---

## 7. Revised highest-value spectral target

The corrected aperiodic problem can now be stated as:

\[
\boxed{
\mathcal T_{index1}:
\text{after exact symmetry quotient, the nonnegative cocycle index is one, generated by }\partial_sU.
}
\]

Equivalent practical routes include:

1. prove a two-channel Ky-Fan average below the two-gap threshold;
2. prove the second compact-core amplification eigenvalue is uniformly below `1/4` after the viscous form is included;
3. derive an orientation/alignment law preventing two independent perturbations from simultaneously receiving quarter-gap compensation.

---

## 8. Firewall

The time tangent's existence does not by itself monopolize the leading positive instantaneous eigenchannel.

Different perturbations may receive amplification at different times and locations.

Therefore

\[
\boxed{
\text{one known zero exponent}
\neq
\text{only one nonnegative exponent}.
}
\]

The index-one statement remains a genuine theorem frontier.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
