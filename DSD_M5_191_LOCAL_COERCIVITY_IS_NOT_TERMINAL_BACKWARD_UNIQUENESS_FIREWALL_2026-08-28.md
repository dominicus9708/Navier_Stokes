# DSD M5-191 — Local Coercivity Is Not Terminal Backward Uniqueness: Firewall and Global Terminal Requirement

Date: 2026-08-28

Status: **LOGICAL FIREWALL: GREEN / LOCAL CRITICAL STOKES CARLEMAN DOES NOT BY ITSELF IMPLY TERMINAL BACKWARD UNIQUENESS / ANY VALID CLOSURE OF `P1_B` MUST USE GLOBAL SPATIAL GEOMETRY, A GENUINE TERMINAL-TIME CARLEMAN WEIGHT, OR THE EXACT FUCHSIAN COMPLETE-ORBIT STRUCTURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-190

M5-190 gives, uniformly on every fixed-width logarithmic annulus, the pressure-compatible critical Stokes coercivity

\[
\begin{aligned}
&\beta\int\varphi^2r^4|\nabla\eta|^2
+\beta^3\int\varphi^2r^2|\eta|^2\\
&\quad+
\beta^2\int\varphi^2r^2|\nabla Z|^2
+\beta^4\int\varphi^2|Z|^2
\lesssim
\text{cutoff errors}.
\end{aligned}
\]

All critical lower-order Oseen/Stokes terms have already been absorbed.

The only unresolved part of the first major gate is propagation from the terminal condition

\[
Z(\cdot,T_*)=0
\]

to earlier times.

---

## 2. Why a bounded cylinder is insufficient

Restrict a parabolic equation to a bounded spatial annulus.

Even for the scalar heat equation, terminal data

\[
u(\cdot,T)=0
\]

inside that annulus do not determine the earlier solution unless one also controls the lateral boundary values.

Information may enter through the lateral boundary during earlier times and be driven to zero at the final time.

Equivalently, parabolic boundary-control/null-controllability mechanisms provide the abstract countermodel to the implication

\[
\boxed{
\text{local terminal zero}
\Longrightarrow
\text{local past zero}
}
\]

without lateral information.

The artificial boundaries introduced by a spatial cutoff are therefore not harmless.

---

## 3. The time-cutoff term does not cure lateral influx

The Lin–Wang-type estimate contains a time-cutoff error of the form

\[
\int \varphi^2 r^6|\chi'(t)w|^2.
\]

Because the actual same-tail difference is flat to all terminal time orders on each fixed exterior compact set, this term can indeed be made small when the cutoff transition approaches `T_*`.

However this only controls the **time cutoff**.

Spatial cutoff commutators remain supported at the radial sides of the annulus for the whole earlier time interval.

Those terms contain the unknown past trace and cannot be discarded using terminal flatness.

Thus

\[
\boxed{
\text{terminal-flat time cutoff}
\not\Rightarrow
\text{removal of spatial boundary errors}.
}
\]

---

## 4. Why sending the cutoff radius to infinity is not automatically enough

Because a same-tail flat difference is superalgebraically small at large normalized radius, one may try to move the cutoff annulus to infinity.

But if the cutoff is chosen to retain only the exterior region, the retained field itself disappears from every fixed point as the cutoff radius tends to infinity.

If the cutoff is instead chosen to retain the interior/core region, the singular Type-I centre remains inside the equation.

Therefore a simple `R -> infinity` cutoff limit does not simultaneously

1. retain the core information to be proved zero, and
2. remove the critical centre.

This is another forbidden shortcut.

---

## 5. Legitimate terminal-backward routes

After M5-190, only three logically legitimate routes remain.

### Route T1 — global critical Oseen–Stokes backward Carleman

Prove a whole-space terminal estimate for

\[
Z_t-\nu\Delta Z+a\cdot\nabla Z+BZ+\nabla q=0,
\quad \operatorname{div}Z=0,
\]

under the Type-I structure

\[
|a|\lesssim\rho^{-1},
\qquad
|B|\lesssim\rho^{-2},
\qquad
\rho^2=r^2+T_*-t.
\]

This route must treat the singular centre as part of the global Carleman geometry rather than as an artificial boundary.

### Route T2 — exterior backward uniqueness plus a genuine centre-removability theorem

One may use bounded-coefficient backward uniqueness on every fixed exterior **only if** the missing centre is independently shown to carry no admissible terminal defect that can feed the exterior solution backward.

M5-142/145 remove algebraic point-supported multipoles but do not yet constitute this full dynamical removability theorem.

### Route T3 — exact Fuchsian complete-orbit uniqueness

Return to

\[
z=\frac{T_*-t}{r^2}
\]

and prove directly that the flat stable boundary condition at `z=0` admits no nonzero complete/recurrent W1 extension.

This is the spectral/Fuchsian route developed through M5-146--180.

---

## 6. Why M5-190 remains valuable

M5-190 is not lost by this firewall.

Any global critical Stokes Carleman or Fuchsian localization still needs to absorb the pressure/Oseen coupling at each spatial scale.

M5-190 proves exactly that this local critical coupling has no endpoint power-counting obstruction.

What it does **not** supply is the global direction of propagation.

---

## 7. DSD audit

### Formation — GREEN

Local cylinder data and global Cauchy data are treated as different objects.

### Axis — GREEN

Spatial cutoff, time cutoff, terminal hypersurface and blow-up centre remain separate geometric channels.

### Static aggregation — GREEN

Small terminal cutoff errors are not added to or confused with uncontrolled lateral-boundary errors.

### Dynamics — GREEN

No local unique-continuation inequality is relabeled as backward uniqueness.

### Cross-audit — GREEN

This explicitly prevents the next proof stage from feeding the desired terminal conclusion back into the local Carleman hypothesis.

---

## 8. Updated frontier

The pressure/coefficient part of the first major gate is now locally GREEN.

The actual remaining first-gate obligation is

\[
\boxed{
\text{GLOBAL terminal direction across the Type-I centre.}
}
\]

The next calculation should therefore target Route T1 first: a whole-space backward Carleman adapted to

\[
\rho^2=r^2+T_*-t,
\]

while reusing M5-190 only as the scale-local pressure absorption module.

If T1 fails by a genuine sign/countermodel obstruction, the work must return to T3 rather than claiming local coercivity has closed the fiber.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
