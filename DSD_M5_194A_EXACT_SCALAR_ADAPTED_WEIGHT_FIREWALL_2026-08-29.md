# DSD M5-194A — Exact Scalar Adapted-Weight Firewall

Date: 2026-08-29

Parent: `DSD_M5_194_LIN_WANG_EPSILON_LOSS_AND_W1_ENDPOINT_CANCELLATION_AUDIT_2026-08-28.md`

Status: **NEGATIVE FIREWALL / DIVERGENCE-FREE + ZERO SPHERICAL FLUX + CRITICAL `1/r` SCALING DO NOT BY THEMSELVES GUARANTEE A GLOBAL SMOOTH SCALAR CARLEMAN PHASE WITH BOTH EXACT STREAMLINE ADAPTATION `B_T·∇Psi=0` AND UNIFORM POSITIVE LOG-RADIAL SLOPE / PURELY TANGENTIAL TAILS REMAIN COMPATIBLE / SMALL RADIAL COMPONENT REMAINS A CONDITIONAL PERTURBATIVE BRANCH / PDE-SPECIFIC CANONICAL-TAIL RIGIDITY, APPROXIMATE ADAPTATION, MATRIX SYMMETRIZATION, AND THE VORTICITY CUTOFF-BACKWARD-UNIQUENESS ENDPOINT REMAIN OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Claim under audit

M5-194 left open the possibility of choosing a scalar Carleman phase adapted to the critical common tail,

\[
B_T\cdot\nabla\Psi=0,
\]

so that conjugation does not recreate the indefinite critical transport potential.

The present audit tests the strongest geometry-only version of that proposal:

> Does every divergence-free, zero-spherical-flux critical tail of order `1/r` admit a globally smooth scalar phase which is exactly constant along the tail flow while retaining the uniformly positive log-radial slope required of a radial Carleman phase?

The answer is **no** for the geometry-only class.

This is a mechanism-level firewall. It is **not** a claim that the actual canonical Navier--Stokes common tail realizes the counterexample geometry below.

---

## 2. Log-cylinder form of exact adaptation

Let

\[
y=-\log r,
\qquad
B_T(r,\theta)=\frac1r\bigl(\Phi_r(y,\theta)e_r+\Phi_\tau(y,\theta)\bigr).
\]

For a scalar phase `Psi=Psi(y,theta)`,

\[
\nabla\Psi
= -\frac1r\Psi_y e_r
 +\frac1r\nabla_{S^2}\Psi.
\]

Therefore

\[
B_T\cdot\nabla\Psi
=
\frac1{r^2}
\left(
-\Phi_r\Psi_y
+\Phi_\tau\cdot\nabla_{S^2}\Psi
\right).
\]

Exact streamline adaptation is thus the first-order equation

\[
\boxed{
-\Phi_r\Psi_y
+\Phi_\tau\cdot\nabla_{S^2}\Psi=0.
}
\]

If the Carleman architecture requires uniform positive log-radial slope, write schematically

\[
\boxed{
\Psi_y\ge c_0>0
}
\]

on the relevant exterior/log-radius region.

The question is whether both boxes can hold globally under only incompressibility, zero spherical flux, and critical scaling.

---

## 3. Explicit admissible geometry-only test tail

Use standard polar angle `theta` on `S^2` and define

\[
\Phi_r(\theta)=\cos\theta,
\qquad
\Phi_\tau(\theta)
=-\frac12\sin\theta\,e_\theta.
\]

Thus

\[
\boxed{
B_*(r,\theta)
=
\frac1r
\left(
\cos\theta\,e_r
-\frac12\sin\theta\,e_\theta
\right).
}
\]

This field is smooth on every sphere and has the critical `1/r` magnitude.

For a tail independent of `y`,

\[
\nabla\cdot B_*
=
\frac1{r^2}
\left(
\Phi_r+
\operatorname{div}_{S^2}\Phi_\tau
\right).
\]

Now

\[
\operatorname{div}_{S^2}
\left(-\frac12\sin\theta\,e_\theta\right)
=
\frac1{\sin\theta}
\partial_\theta
\left(-\frac12\sin^2\theta\right)
=-\cos\theta.
\]

Hence

\[
\boxed{\nabla\cdot B_*=0.}
\]

Its spherical radial flux also vanishes:

\[
\int_{S^2}\Phi_r\,dS
=
\int_{S^2}\cos\theta\,dS
=0.
\]

So this test field passes the geometry-only constraints being audited.

---

## 4. Pointwise pole obstruction

For `B_*`, the exact adaptation equation becomes

\[
-\cos\theta\,\Psi_y
-\frac12\sin\theta\,\Psi_\theta
=0,
\]

or equivalently

\[
\boxed{
2\cos\theta\,\Psi_y
+\sin\theta\,\Psi_\theta=0.
}
\]

At the north and south poles,

\[
\sin\theta=0,
\qquad
\cos\theta=\pm1.
\]

The tangential part vanishes there while the radial part does not. Therefore exact adaptation forces

\[
\boxed{
\Psi_y=0
}
\]

at both poles.

This contradicts any requirement of the form

\[
\Psi_y\ge c_0>0
\]

uniformly on the sphere.

Therefore

\[
\boxed{
\text{geometry-only exact scalar adaptation}
+
\text{uniform positive radial Carleman slope}
\quad\text{cannot hold universally.}
}
\]

The obstruction is pointwise; no integration or spherical-flux cancellation can remove it.

---

## 5. Characteristic cross-check

The same conclusion can be checked by solving the adaptation equation away from the poles.

Characteristics satisfy

\[
\frac{dy}{d\theta}=2\cot\theta.
\]

Hence

\[
y-2\log(\sin\theta)=C,
\]

and local solutions have the form

\[
\boxed{
\Psi(y,\theta)
=F\!\left(y-2\log\sin\theta\right).
}
\]

Then

\[
\Psi_y=F'.
\]

If `Psi_y >= c_0 > 0`, the argument of `F` tends to `+infinity` as either pole is approached because

\[
-2\log\sin\theta\to+\infty.
\]

Thus the phase acquires unbounded angular variation on a fixed sphere instead of extending as the required globally smooth scalar weight.

This agrees with the pointwise pole obstruction.

---

## 6. Why M5-191 is not a counterexample to this firewall

M5-191 used a purely tangential rotational tail with

\[
\Phi_r=0.
\]

For any radial/log-radial phase `Psi=Psi(y)`,

\[
B_T\cdot\nabla\Psi=0
\]

holds automatically.

Therefore the M5-191 rotational tail belongs to a favorable subclass. It cannot be used to argue against scalar adaptation.

The present `B_*` test is needed precisely because it has a nonzero radial component while preserving incompressibility and zero net radial flux.

---

## 7. Residual for an ordinary radial phase

Take a standard log-radial phase

\[
\Psi(y)=\beta y,
\qquad \beta>0.
\]

Then

\[
\Psi_y=\beta,
\qquad
\nabla_{S^2}\Psi=0,
\]

so for a general critical tail

\[
\boxed{
B_T\cdot\nabla\Psi
=-\beta r^{-2}\Phi_r.
}
\]

This divides the endpoint geometry into three distinct cases.

### Case A — purely tangential tail

\[
\Phi_r=0.
\]

The radial phase is exactly adapted. This branch remains viable.

### Case B — quantitatively small radial component

If

\[
\|\Phi_r\|_{L^\infty}\le\varepsilon,
\]

then the recreated zeroth-order conjugation term is bounded by

\[
\varepsilon\beta r^{-2}.
\]

This may be absorbable if an endpoint Carleman estimate has a coercivity margin strictly larger than the corresponding constant. The required threshold is theorem-dependent and is **not** established here.

Thus this is a **CONDITIONAL** branch, not a completed estimate.

### Case C — generic order-one radial component

If `Phi_r` is order one, the residual is itself of the critical scale

\[
\beta r^{-2}.
\]

It is therefore at the same structural scale as the endpoint Carleman coercive terms that M5-194 is trying to protect. No small-constant absorption follows from scaling alone.

---

## 8. DSD audit verdict

### CLOSED at this layer

The following universal geometry-only shortcut is closed:

\[
\boxed{
\nabla\cdot B_T=0,
\quad
\int_{S^2}\Phi_r=0,
\quad
|B_T|\sim r^{-1}
\quad\Longrightarrow\quad
\exists\text{ global smooth scalar }\Psi
\text{ with }
B_T\cdot\nabla\Psi=0,
\ \Psi_y\ge c_0>0.
}
\]

The explicit field `B_*` disproves that implication.

### STILL OPEN

The firewall does **not** close any of the following stronger possibilities:

1. the actual canonical Navier--Stokes common tail obeys additional PDE-specific rigidity excluding the bad radial geometry;
2. `Phi_r` is quantitatively small in the region needed for backward uniqueness;
3. only approximate adaptation is needed and its residual can be absorbed;
4. a vector/matrix symmetrizer can exploit the vorticity-system structure where a scalar phase cannot;
5. a different endpoint Carleman architecture avoids exact streamline adaptation entirely;
6. the localized vorticity cutoff commutators can be closed strongly enough to invoke backward uniqueness.

---

## 9. Scope firewall

This note proves only a negative statement about a proposed **proof mechanism**.

It does not construct a Navier--Stokes singular solution.

It does not prove that a canonical Type-I common tail equals `B_*`.

It does not refute backward uniqueness for Navier--Stokes.

It does not prove global regularity.

Its role is to prevent an invalid inference from weak geometric tail constraints to the existence of an exact scalar adapted Carleman phase.

---

## 10. Next audit target

The next calculation should work on the surviving endpoint rather than reopen the closed scalar-universality branch:

\[
\boxed{
\text{Type-I vorticity equation}
\ +\ 
\text{radial/approximately adapted Carleman phase}
\ +\ 
\text{cutoff commutator terms}
}
\]

and determine whether the annular source terms and the critical radial-tail residual can be placed below a genuine endpoint coercivity margin.

If no scalar margin exists, the remaining structural route is to test a matrix/symmetrizer or PDE-specific canonical-tail rigidity.
