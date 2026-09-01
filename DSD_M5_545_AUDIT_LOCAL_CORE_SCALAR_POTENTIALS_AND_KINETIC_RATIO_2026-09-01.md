# DSD M5-545 — Local-core scalar-potential audit leaves one kinetic ratio but no strict cocycle

Date: 2026-09-01

Status: **LOCAL POTENTIAL AUDIT / AFTER M5-544 REMOVES ENDPOINT-TAIL ERRORS FROM THE ACTIVE LEDGERS, LOCAL ENSTROPHY AND PALINSTROPHY STILL FAIL AS LYAPUNOV FUNCTIONS BECAUSE THEIR CORE STRETCHING/NONLINEAR PRODUCTION TERMS HAVE INDEFINITE SIGN; MATERIAL FLUX/CIRCULATION AND PAIR-GRAM VARIABLES REMAIN EXACT OR BOUNDED OSCILLATORY COBoundaries / LOCAL KINETIC ENERGY IS DIFFERENT: NAVIER--STOKES NONLINEARITY IS INTERNALLY ENERGY CONSERVATIVE, SO WITH THE CUTOFF TRANSITION PLACED IN THE SMALL TAIL ONE GETS `1/2 K_R' - 1/4 K_R + D_R = o_R(1)` AND HENCE THE RECURRENT CORE MUST SATISFY `mean D_R = mean K_R/4 + o_R(1)` / THIS IS A NEW RIGID RATIO BUT NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-544 showed that spatial infinity is no longer the reason the obvious scalar observables fail.

The present note rechecks the main candidates on the finite active core with all cutoff errors kept explicitly.

The question is whether any previously sign-indefinite global identity becomes a strict local cocycle once the endpoint spectator tail is removed.

---

## 2. Local enstrophy remains non-monotone

M5-544 gives

\[
\frac12E_R'
+
\frac14E_R
+
P_R
=
Q_R
+o_R(1).
\]

The active component satisfies

\[
\langle Q_R\rangle>0.
\]

Thus the same term that obstructed global monotonicity survives **inside** the finite active core.

Therefore localized enstrophy is not the missing strict cocycle.

This failure is intrinsic to core vortex stretching, not a tail defect.

---

## 3. Local palinstrophy also remains non-monotone

Likewise

\[
\frac12P_R'
+
\frac34P_R
+
H_R
=
\mathcal N_{P,R}
+o_R(1).
\]

The derivative nonlinearity `N_(P,R)` has no fixed sign and the recurrent core uses it to regenerate positive `P_R` and `H_R`.

Hence localized palinstrophy is also not a strict potential.

The same conclusion persists at every fixed higher derivative level.

---

## 4. Material flux and circulation remain coboundaries

M5-489 and M5-513 already established for each persistent material lineage

\[
\Phi_{j+1}-\Phi_j=D_j,
\]

with zero invariant mean signed diffusion,

\[
\langle D\rangle=0.
\]

This identity is already material/local and does not rely on the remote endpoint tail.

Removing the tail therefore does not change its basic obstruction:

\[
\boxed{
\text{flux/circulation may oscillate indefinitely with zero net signed drift.}
}
\]

---

## 5. Relative angle and pair Gram remain bounded oscillatory variables

For a persistent dual pair,

\[
c_{ab}=\xi_a\cdot\xi_b
\]

satisfies the exact M5-491 identity

\[
c_{ab}'
=
R_{strain}+R_{diff}.
\]

On a recurrent component the signed mean derivative is zero.

M5-515--516 already separated nontrivial pair motion from the anchored exact-cancellation branch.

The endpoint tail was not responsible for the possibility of an orientation loop.

Therefore pair Gram variables remain recurrence observables rather than Lyapunov observables.

---

## 6. Localized kinetic-energy equation

The similarity velocity equation is

\[
\partial_\theta U
+
\frac12U
+
\frac12(y\cdot\nabla)U
+
(U\cdot\nabla)U
=
-\nabla\Pi+\Delta U,
\]

with

\[
\nabla\cdot U=0.
\]

Define

\[
K_R
:=
\int\chi_R|U|^2dy,
\]

and

\[
D_R
:=
\int\chi_R|\nabla U|^2dy.
\]

Take the `L2` pairing with `chi_R U`.

Inside the region where `chi_R=1`, the convection and pressure terms are exact divergences and produce no bulk kinetic-energy creation.

All failures of cancellation occur only where derivatives hit `chi_R`, namely in the transition shell `S_R`.

---

## 7. Similarity linear coefficient

The explicit `+U/2` term contributes

\[
\frac12K_R.
\]

The dilation term gives, modulo the cutoff shell,

\[
\frac12
\int\chi_R U\cdot(y\cdot\nabla U)
=
-\frac34K_R
+\text{shell error}.
\]

Thus the net bulk similarity coefficient is

\[
\boxed{-\frac14K_R.}
\]

Viscosity gives

\[
\boxed{D_R}
\]

plus a shell commutator.

Hence

\[
\boxed{
\frac12K_R'
-
\frac14K_R
+
D_R
=
\mathcal E_R^{kin}.
}
\]

---

## 8. Kinetic cutoff error tends to zero

The shell error contains terms of the schematic forms

\[
\int_{S_R}
|U|^3|\nabla\chi_R|,
\]

\[
\int_{S_R}
|\Pi||U||\nabla\chi_R|,
\]

\[
\int_{S_R}
|U||\nabla U||\nabla\chi_R|,
\]

and

\[
\int_{S_R}
|U|^2|y\cdot\nabla\chi_R|.
\]

M5-508, M5-523, the pressure Calderon--Zygmund decomposition, and the adaptive velocity-tail control from M5-541 imply that these transition-shell quantities tend to zero after choosing the cutoff shell sufficiently far out, with a standard good-radius smoothing if needed for pressure traces.

Therefore

\[
\boxed{
\sup_{Y\in\widehat{\mathfrak H}}
|\mathcal E_R^{kin}(Y)|
\to0.
}
\]

The pressure statement here is only a cutoff-shell estimate; no global finite kinetic energy is assumed.

---

## 9. Recurrent kinetic ratio

For each fixed `R`, `K_R` is bounded on the compact hull.

Invariant averaging gives

\[
\langle K_R'\rangle=0.
\]

Hence

\[
\boxed{
\langle D_R\rangle
=
\frac14\langle K_R\rangle
+o_R(1).
}
\]

This is qualitatively different from the enstrophy identity because there is no bulk nonlinear production term on the right.

The recurrent similarity core must maintain exactly the kinetic-energy/dissipation ratio required by scaling.

---

## 10. Why the ratio is not yet a contradiction

The coefficient `-1/4 K_R` represents similarity-scale energy injection.

A recurrent core can in principle satisfy

\[
\langle D_R\rangle
\approx
\frac14\langle K_R\rangle
\]

without violating any sign law.

Thus kinetic energy is not itself a strict Lyapunov function in similarity variables.

The physical Navier--Stokes energy decreases, but one normalized similarity generation corresponds to a different physical scale, and the scale factor precisely supplies the `K_R/4` term.

This is the earlier summability barrier in a local recurrent form.

---

## 11. Quantitative Poincare branch

If one could establish an approximate zero-boundary Poincare inequality on the active core of the form

\[
K_R
\le C_P R_{eff}^2D_R
+o_R(1),
\]

then the recurrent ratio would require

\[
\frac1{C_PR_{eff}^2}
\lesssim
\frac14.
\]

Equivalently, a recurrent core would need a minimum effective spatial size.

This does not currently contradict the normalized carrier geometry, but it provides a new quantitative geometric constraint.

No no-slip boundary condition is silently assumed; any future use of this route must derive the approximate Poincare condition from the actual low-tail boundary data.

---

## 12. Verdict on the natural scalar candidates

After tail localization:

- enstrophy: **fails intrinsically by axial stretching**;
- palinstrophy/higher Sobolev energies: **fail intrinsically by derivative production**;
- flux/circulation: **exact signed coboundaries**;
- pair angle/Gram: **bounded oscillatory coboundaries**;
- kinetic energy: **gives a rigid recurrent ratio, but similarity scaling prevents monotonicity**.

Therefore the missing final rigidity observable cannot be obtained merely by removing the endpoint tail from one of the old scalar candidates.

---

## 13. Updated core-cycle frontier

The finite active core is now an intrinsically recurrent similarity system satisfying simultaneously

\[
\boxed{
\begin{aligned}
&\langle Q_R\rangle>0,\\
&\langle P_R\rangle>0,\\
&\text{positive dual/ratchet marks},\\
&\langle D_R\rangle
=\frac14\langle K_R\rangle+o_R(1),\\
&\text{zero signed flux drift},\\
&\text{zero signed pair-angle drift over recurrence}.
\end{aligned}
}
\]

This is the present finite-core hard object.

---

## 14. Highest-value next target

Because all scalar one-state observables have now been audited, the next candidate should be a **two-time or cycle action** rather than another instantaneous norm.

A promising form is a scale-compensated action over one full generation,

\[
\mathcal A_{cycle}
:=
\int_{\theta_j}^{\theta_{j+1}}
\left[
D_R-\frac14K_R
\right]d\theta,
\]

augmented by the persistent pair/flux variables so that exact endpoint differences are subtracted.

The kinetic identity makes the bare action a small boundary coboundary; combining it with unavoidable ratchet/pair dissipation may expose whether one recurrent cycle must pay a strictly positive **excess over similarity scaling**.

That excess, rather than a one-state norm, is now the natural strict-cocycle target.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]