# DSD M5-183 — Local Vorticity–Velocity Parabolic–Elliptic Backward Gate

Date: 2026-08-28

Status: **W1-CONDITIONAL / NONLOCAL BIOT-SAVART OBSTRUCTION IS REFORMULATED AS A LOCAL COUPLED PARABOLIC–ELLIPTIC SYSTEM / THIS MATCHES THE STRUCTURAL TYPE OF STOKES CARLEMAN UNIQUE-CONTINUATION ARGUMENTS BUT A TERMINAL-BACKWARD CARLEMAN ESTIMATE FOR THE PRESENT EXTERIOR OSEEN SYSTEM IS NOT YET PROVED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Relative physical system

On a fixed exterior cylinder

\[
Q_R:=\Omega_R\times(t_0,T_*),
\qquad
\Omega_R=\{|x-x_*|>R\},
\]

let

\[
Z=u^V-u^W,
\qquad
q=p^V-p^W.
\]

The velocity difference satisfies

\[
\boxed{
Z_t-\nu\Delta Z+(u^V\cdot\nabla)Z+(Z\cdot\nabla)u^W+\nabla q=0,
\qquad \nabla\cdot Z=0.
}
\]

All coefficients formed from `u^V,u^W` and their spatial derivatives are bounded on every fixed `Q_R` up to the terminal time.

M5-181 gives

\[
\boxed{Z(\cdot,T_*)=0\quad\text{on }\Omega_R.}
\]

---

## 2. Relative vorticity

Define

\[
\eta:=\nabla\times Z,
\qquad
\omega^{V,W}:=\nabla\times u^{V,W}.
\]

Taking curl gives

\[
\boxed{
\begin{aligned}
\eta_t-\nu\Delta\eta
&+(u^V\cdot\nabla)\eta
-(\eta\cdot\nabla)u^V\\
&+(Z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)Z
=0.
\end{aligned}}
\]

The pressure has disappeared.

The last line prevents immediate use of a scalar heat backward-uniqueness theorem because it contains `Z` and `grad Z`.

---

## 3. Local elliptic closure

Because

\[
\nabla\cdot Z=0,
\qquad
\nabla\times Z=\eta,
\]

we have the exact local identity

\[
\boxed{-\Delta Z=\nabla\times\eta.}
\]

Thus no global Biot–Savart inversion is needed if `Z` and `eta` are treated as one coupled system.

The flat-fiber problem is therefore a local system of the schematic form

\[
\boxed{
\begin{cases}
P\eta
= A_1\nabla\eta+A_0\eta+C_1\nabla Z+C_0Z,\\
-\Delta Z=\nabla\times\eta,\\
\nabla\cdot Z=0,
\end{cases}}
\]

where

\[
P:=\partial_t-\nu\Delta
\]

and

\[
A_1,A_0,C_1,C_0\in L^\infty(Q_R)
\]

for each fixed `R>0`.

This is the preferred local formulation of the remaining exterior gate.

---

## 4. Terminal data

Since `Z(.,T_*)=0` smoothly on the fixed exterior and all punctured terminal jets agree,

\[
\boxed{
\eta(\cdot,T_*)=0,
\qquad
Z(\cdot,T_*)=0
\quad\text{on }\Omega_R.
}
\]

Indeed all finite spatial derivatives of the terminal difference vanish on fixed compact subsets of `Omega_R`.

The problem is therefore backward uniqueness from exact terminal-zero data, not approximate continuation.

---

## 5. Carleman target

A sufficient internal estimate is the following.

Choose a terminal Carleman weight `Phi(x,t)` adapted to an exterior/half-space patch and a large parameter `s`.

### Parabolic component

Prove schematically

\[
\boxed{
\begin{aligned}
&s^3\|e^{s\Phi}\eta\|^2
+s\|e^{s\Phi}\nabla\eta\|^2\\
&\qquad\le
C\|e^{s\Phi}P\eta\|^2
+\text{controlled cutoff terms}.
\end{aligned}}
\]

### Elliptic component

On the same weighted patch, use

\[
-\Delta Z=\nabla\times\eta
\]

to obtain

\[
\boxed{
 s^2\|e^{s\Phi}Z\|^2
+\|e^{s\Phi}\nabla Z\|^2
\le
C\|e^{s\Phi}\eta\|_{H^1}^2
+\text{cutoff terms}.
}
\]

Then the bounded lower-order coefficients in the vorticity equation can be absorbed for sufficiently large `s`.

If the cutoff terms can be arranged away from the terminal-zero region exactly as in boundary-condition-free exterior heat Carleman arguments, the pair must vanish backward on a smaller exterior cylinder.

---

## 6. Relation to existing Stokes unique-continuation literature

Boulakia-type nonstationary Stokes results combine parabolic and elliptic Carleman estimates and obtain unique continuation without prescribing boundary conditions in the continuation statement.

Lin–Wang-type generalized Stokes results likewise use Carleman estimates to control velocity vanishing in the presence of lower-order coefficients.

These results support the **structure** of Section 5.

They are not counted as a proof of the terminal-backward estimate because their audited conclusions propagate spatial/spacetime vanishing rather than the exact terminal hypersurface condition required here.

---

## 7. Why this is preferable to pointwise Biot–Savart

A pointwise estimate

\[
|Z|+|\nabla Z|\le C(|\eta|+|\nabla\eta|)
\]

on an artificial exterior is false without controlling harmonic/exterior components.

The elliptic equation retains those components inside the local PDE system and allows a weighted elliptic Carleman estimate to control them together with the parabolic component.

Therefore the implication

\[
\text{Biot-Savart smoothing}\Rightarrow\text{local ESS inequality}
\]

remains RED, while the coupled parabolic–elliptic formulation is GREEN.

---

## 8. DSD four-chain audit

### Formation — GREEN

`Z` and `eta` are actual differences of two W1 physical realizations; no auxiliary physical degree of freedom is introduced.

### Axis — GREEN

Parabolic terminal-time propagation and elliptic spatial reconstruction are separated.

### Static aggregation — GREEN

The elliptic relation is not counted as an independent decay budget; it is a constraint coupling the two fields.

### Dynamics — YELLOW

The terminal Carleman estimate remains to be proved/matched.

### Cross-audit — GREEN

No artificial boundary equality, pointwise Biot–Savart bound, or terminal analyticity is assumed.

---

## 9. Closure consequence

If the coupled terminal Carleman gate is GREEN, then for each `R>0`

\[
Z=0
\]

on a nonempty backward exterior cylinder.

Spatial analyticity at any regular time extends equality to the connected whole space, so

\[
V=W.
\]

Hence the same lemma would eliminate both remaining flat branches:

\[
\boxed{P1_B^S=P1_B^P=\varnothing.}
\]

---

## 10. Next calculation

The next internal step is to test whether the weighted elliptic estimate can be paired with the standard boundary-free exterior backward-heat Carleman inequality without producing an uncontrolled artificial-boundary term.

If yes, the proof reduces to lower-order absorption.

If no, the exact obstruction must be recorded and the spectral-infinity action route remains necessary.

All conclusions remain W1-conditional.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
