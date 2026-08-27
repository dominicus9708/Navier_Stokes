# DSD M5-153 — Fixed-Leray-Time Inverse-Radius Averaged Vorticity Energy

Date: 2026-08-27

Status: **P1_B^S AXIS REFACTOR / ON THE STATISTICAL SAME-TAIL BRANCH, RETURNING FROM `(xi,eta)` TO `(xi,s)` REMOVES THE MIXED GENEALOGICAL NORMAL DERIVATIVE; PAIR INVARIANCE KILLS THE SOLE TIME-DERIVATIVE TERM WHEN THE VORTICITY EQUATION IS TESTED AGAINST THE VORTICITY ITSELF / THE M5-151 HIGH-ETA DERIVATIVE HIERARCHY IS THEREFORE NOT FUNDAMENTAL FOR THIS BRANCH / THE REMAINING GATE IS RADIAL TRANSPORT/STRETCHING COERCIVITY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why change axes again

M5-151 used the co-moving genealogical coordinate `eta` because it diagonalizes the canonical tail conveyor.

That form produced mixed terms such as

\[
\frac1\xi K_{\eta\xi}
\]

and led to the genuine audit warning M5-152: compact analyticity does not control genealogical derivative-to-amplitude ratios.

However Branch `P1_B^S` has an invariant pair measure.  For an **averaged normal-energy calculation**, it is more efficient to keep Leray time `s` itself as the dynamical axis.

This is an axis refactor, not a change of solution.

---

## 2. Fixed-time inverse-radius variables

Set

\[
\boxed{
\xi=r^2
}
\]

and write the relative Leray vorticity as

\[
\boxed{
\Omega_U-\Omega_V
=r^{-2}K(\xi,s,\theta).
}
\]

At fixed `s`,

\[
r\partial_r=2\xi\partial_\xi.
\]

For vorticity scaling `r^-2`, the passive Leray terms satisfy

\[
\boxed{
\left(
\partial_s+1+\frac12Y\cdot\nabla
\right)(r^{-2}K)
=r^{-2}\left(K_s+\xi K_\xi\right).
}
\]

The componentwise Laplacian is

\[
\boxed{
\Delta(r^{-2}K)
=r^{-4}
\left[
4\xi^2K_{\xi\xi}
-2\xi K_\xi
+(2+\Delta_{S^2})K
\right].
}
\]

---

## 3. Exact relative equation

Let `N_s` denote the scaled local relative transport/stretching term obtained from

\[
(U\cdot\nabla)\Omega_U-(\Omega_U\cdot\nabla)U
-
\left[(V\cdot\nabla)\Omega_V-(\Omega_V\cdot\nabla)V\right].
\]

It is linear in the pair difference `(K,Z)` once the backgrounds are fixed.

The exact scaled equation is

\[
\boxed{
K_s
+\xi K_\xi
-4\nu\xi K_{\xi\xi}
+2\nu K_\xi
-\frac\nu\xi(2+\Delta_{S^2})K
+\frac1\xi\mathcal N_s
=0.
}
\]

Divide by `xi` and reverse sign to expose the normal operator:

\[
\boxed{
\begin{aligned}
0={}&4\nu K_{\xi\xi}
-\left(1+\frac{2\nu}{\xi}\right)K_\xi
-\frac1\xi K_s\\
&+\frac\nu{\xi^2}(2+\Delta_{S^2})K
-\frac1{\xi^2}\mathcal N_s.
\end{aligned}
}
\]

The principal normal operator is again

\[
4\nu\partial_{\xi\xi}-\partial_\xi.
\]

There is no mixed `s-xi` derivative.

---

## 4. Invariant pair average eliminates time derivatives

On Branch `P1_B^S`, average over the invariant pair measure `rho` and the sphere.

Define

\[
\langle F\rangle
:=
\int_{\mathcal R}\int_{S^2}F\,d\theta\,d\rho.
\]

Pair-flow invariance gives

\[
\boxed{
\langle K_s\cdot K\rangle
=\frac12\langle\partial_s|K|^2\rangle
=0.
}
\]

Thus testing the fixed-time equation against `K` removes the dynamical derivative exactly without any `eta`-frequency estimate.

---

## 5. Scalar normal energy identity

Set

\[
E(\xi):=\langle|K|^2\rangle,
\qquad
A(\xi):=\langle|K_\xi|^2\rangle,
\qquad
B_\theta(\xi):=\langle|\nabla_{S^2}K|^2\rangle.
\]

Use

\[
\langle K_{\xi\xi}\cdot K\rangle
=\frac12E''-A,
\]

\[
\langle K_\xi\cdot K\rangle
=\frac12E',
\]

and

\[
\langle\Delta_{S^2}K\cdot K\rangle
=-B_\theta.
\]

The exact averaged identity is

\[
\boxed{
\begin{aligned}
0={}&2\nu E''
-4\nu A
-\left(\frac12+\frac\nu\xi\right)E'\\
&+\frac\nu{\xi^2}(2E-B_\theta)
-\frac1{\xi^2}
\langle\mathcal N_s\cdot K\rangle.
\end{aligned}
}
\]

No genealogical derivative energy appears.

---

## 6. Scaling of the nonlinear term

At large `xi`, the W1 backgrounds have critical velocity/vorticity shell size

\[
H=O(1),
\qquad
K_{background}=O(1)
\]

in the scaled variables.

A radial derivative inside `N_s` enters through

\[
2\xi K_\xi
\]

or the corresponding velocity-difference derivative.

Because the energy identity carries the external factor `xi^-2`, the largest normal transport contribution has size schematically

\[
\boxed{
O(\xi^{-1})|K_\xi||K|,
}
\]

which is perturbative relative to the principal one-way drift/diffusion at sufficiently large `xi` after Young-type splitting.

Angular terms appear at `O(xi^-2)` and Biot--Savart recovers the velocity difference with one derivative gain.

Thus the critical common tail remains subprincipal in the normal-at-infinity channel.

---

## 7. Flat boundary condition

M5-145/M5-149 imply

\[
E,A,B_\theta\to0
\]

superalgebraically as `xi->infinity`.

Therefore the statistical flat branch is reduced to a scalar radial-energy problem with zero data at normal infinity.

The remaining question is whether the nonlinear radial transport/stretching term can sustain a nonzero superalgebraically decaying `E` despite the one-way normal operator.

This is strictly narrower than the M5-151 derivative hierarchy.

---

## 8. Relation to M5-152

M5-152 remains correct:

compact analytic regularity alone does not provide a tame genealogy derivative estimate.

The present note does **not** invalidate that audit.  It changes the axis used for Branch-S averaging so that the problematic derivative estimate is no longer needed in the first place.

This is precisely the intended role of the DSD axial cross-audit:

\[
\boxed{
\text{do not solve an artificial derivative hierarchy if another exact coordinate channel removes it.}
}
\]

---

## 9. DSD four-chain audit

### Formation — GREEN

`(xi,s)` is an exact rewriting of the same W1 relative vorticity field.

### Axis — GREEN

The coordinate is selected for the calculation being performed: `eta` for tail genealogy, `s` for invariant pair energy.

### Static aggregation — GREEN

No genealogical derivative is estimated by amplitude; it is eliminated exactly by invariant averaging.

### Dynamics — GREEN

Pair invariance is used only to kill the time derivative in the scalar energy identity.

### Cross-audit — GREEN

The principal normal sign agrees with M5-146–151 while removing the coordinate-induced high-frequency hierarchy from the main Branch-S path.

---

## 10. Updated Branch-S gate

The preferred `P1_B^S` problem is now:

\[
\boxed{
\text{prove that the scalar identity above has no nonzero superalgebraically decaying solution}
\text{ when the relative transport/stretching term has its audited }O(\xi^{-1})\text{ normal size.}
}
\]

This is the next calculation.

Branch `P1_B^P` remains untouched.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]