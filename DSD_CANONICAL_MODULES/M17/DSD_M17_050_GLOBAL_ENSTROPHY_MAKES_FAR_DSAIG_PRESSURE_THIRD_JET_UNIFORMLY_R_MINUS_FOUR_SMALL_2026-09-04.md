# DSD M17-050 — Global enstrophy makes the far DSAIG pressure third jet uniformly R^-4 small

Date: 2026-09-04
Canonical ID: **M17-050**

Status: **INTERNAL FAR-PRESSURE TAIL REDUCTION / THE PRESSURE SOURCE `S_P=|Sigma|^2-rho^2/2` IS GLOBALLY L1 UNDER THE RETAINED WHOLE-SPACE ENSTROPHY BOUND. FOR DECAYING DIVERGENCE-FREE VELOCITY, `int|Sigma|^2=(1/2)int|W|^2`, SO `||S_P||_1<=int|W|^2<=Z_*`. THE THIRD DERIVATIVE OF THE NEWTONIAN KERNEL IS `O(|z|^-4)`, HENCE A FAR SOURCE OUTSIDE DISTANCE R PRODUCES `|nabla^3P_far(Y)|<=C Z_* R^-4`. ON A UNIFORMLY BOUNDED SLANTED BRANCH, THE FULL FAR DSAIG TENSOR SATISFIES `|N_p^far|<=C |p| Z_* R^-4`. THUS CUBIC-AND-HIGHER FAR PRESSURE CANNOT REMAIN AN ORDER-ONE INDEPENDENT SCREENING CHANNEL AS THE PARENT RADIUS IS ENLARGED; THE ALIGNMENT BURDEN LOCALIZES TO THE VISCOUS PLUS NEAR-PRESSURE SOURCE ARCHITECTURE, WITH A QUANTIFIED FAR ERROR. THIS REFINES, RATHER THAN CONTRADICTS, THE M17-045 FIREWALL THAT DISTANCE ALONE WITHOUT A GLOBAL SOURCE NORM DOES NOT PROVE SILENCE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Pressure source

M17-045 gives

\[
\boxed{
-\Delta P=S_P,
\qquad
S_P=|\Sigma|^2-\frac12\rho^2,
\qquad
\rho=|W|.
}
\]

The DSAIG pressure tensor is one derivative of the pressure Hessian:

\[
\nabla^3P.
\]

---

## 2. Whole-space strain/enstrophy identity

For a sufficiently decaying incompressible velocity field on `R^3`,

\[
\int_{\mathbb R^3}|\nabla U|^2dy
=
\int_{\mathbb R^3}|\operatorname{curl}U|^2dy
=
\int\rho^2dy.
\]

Write

\[
\nabla U=\Sigma+\Omega.
\]

The antisymmetric part satisfies pointwise

\[
|\Omega|^2=\frac12\rho^2.
\]

Hence

\[
\int|\Sigma|^2
=
\int|\nabla U|^2-\int|\Omega|^2
=
\frac12\int\rho^2.
\]

Therefore

\[
\boxed{
\int_{\mathbb R^3}|\Sigma|^2dy
=\frac12\int_{\mathbb R^3}\rho^2dy.
}
\]

---

## 3. L1 bound for the pressure source

By the triangle inequality,

\[
\begin{aligned}
\|S_P\|_{L^1}
&\le
\int|\Sigma|^2dy
+\frac12\int\rho^2dy\\
&=
\int\rho^2dy.
\end{aligned}
\]

Thus

\[
\boxed{
\|S_P\|_{L^1}
\le
\|W\|_{L^2}^2.
}
\]

On the retained compact hard hull assume the already used uniform global enstrophy bound

\[
\boxed{
\int\rho^2dy\le Z_*.
}
\]

Then

\[
\boxed{
\|S_P\|_{L^1}\le Z_*.
}
\]

---

## 4. Far pressure outside radius R

Let the marked core center be `Y` and define a far source supported in

\[
|y-Y|\ge R
\]

up to the smooth transition annulus used in M17-046.

The Newtonian representation is

\[
P_{far}(x)
=\frac1{4\pi}
\int
\frac{S_P^{far}(y)}{|x-y|}\,dy.
\]

At `x=Y`, the third derivative kernel satisfies

\[
\boxed{
\left|
\nabla_Y^3\frac1{|Y-y|}
\right|
\le C|Y-y|^{-4}.
}
\]

Therefore

\[
\begin{aligned}
|\nabla^3P_{far}(Y)|
&\le
C\int_{|y-Y|\ge R}
|S_P(y)|\,|Y-y|^{-4}dy\\
&\le
CR^{-4}\|S_P\|_{L^1}.
\end{aligned}
\]

Hence

\[
\boxed{
|\nabla^3P_{far}(Y)|
\le C Z_*R^{-4}.
}
\]

This estimate includes all cubic-and-higher harmonic modes at once.

---

## 5. DSAIG far tensor bound

M17-045 uses

\[
N_p^{far}
=TF_h[(p\cdot\nabla_h)\nabla_h^2P_{far}].
\]

This is a contraction of the pressure third derivative with the slant vector `p`.
Thus

\[
\boxed{
|N_p^{far}|
\le C|p|\,|\nabla^3P_{far}(Y)|.
}
\]

Therefore

\[
\boxed{
|N_p^{far}|
\le C|p|Z_*R^{-4}.
}
\]

On a uniformly recurrent slanted branch with

\[
|p|\le P_*,
\]

we obtain the uniform estimate

\[
\boxed{
|N_p^{far}|
\le C P_*Z_*R^{-4}.
}
\]

---

## 6. Higher pressure derivatives

The same argument gives for every integer `m>=1`

\[
\boxed{
|\nabla^mP_{far}(Y)|
\le C_m Z_*R^{-(m+1)}.
}
\]

In particular,

\[
|\nabla^2P_{far}|\lesssim Z_*R^{-3},
\]

\[
|\nabla^3P_{far}|\lesssim Z_*R^{-4},
\]

\[
|\nabla^4P_{far}|\lesssim Z_*R^{-5}.
\]

Thus each successive pressure-jet alignment hierarchy has a stronger far-tail decay.

---

## 7. Consequence for M17-045 alignment

The exact DSAIG gate is

\[
P_{Q_0}^{\perp}
\left[
V_p-N_p^{near}-N_p^{far}
\right]=0.
\]

Using the far bound,

\[
\boxed{
\left|
P_{Q_0}^{\perp}(V_p-N_p^{near})
\right|
\le C P_*Z_*R^{-4}.
}
\]

Therefore for arbitrarily large admissible parent radius `R`, the local-plus-near tensor must approach exact collinearity with `Q_0`:

\[
\boxed{
P_{Q_0}^{\perp}(V_p-N_p^{near})
\to0
\qquad(R\to\infty).
}
\]

Equivalently, the far field cannot supply a persistent order-one perpendicular screening tensor.

---

## 8. What this does and does not localize

This does **not** make pressure local.
As `R` grows, `P_near` contains a larger portion of the global pressure source.

The correct conclusion is narrower:

\[
\boxed{
\text{far-tail pressure jets are quantitatively negligible}
}
\]

while

\[
\boxed{
\text{the remaining pressure alignment is carried by the finite/mesoscopic source architecture}.
}
\]

Thus the SAIG branch is converted from an arbitrary whole-space far-cancellation problem into a localized/mesoscopic pressure-source alignment problem plus a controlled tail error.

---

## 9. Relation to M17-046

M17-046 decomposes the time derivative of the far cubic tensor into source production, shell turnover, and relative transport.

M17-050 shows that the tensor itself is `O(R^-4)` and its higher spatial moments decay even faster under the global enstrophy bound.

Therefore the three M17-046 channels may govern how the small far tensor changes, but they cannot maintain an order-one DSAIG cancellation at arbitrarily large `R` unless one of the retained uniform bounds fails.

---

## 10. DSD audit

### Audit A — using distance without a global source bound
Corrected. M17-045 was right to reject that shortcut. The present conclusion uses the additional `L1` pressure-source bound coming from global enstrophy.

### Audit B — bounding S_P by pointwise sign
Not used. Only its `L1` norm is controlled.

### Audit C — claiming near pressure is local
Rejected. The near region may be mesoscopic and grows with `R`.

### Audit D — claiming far pressure is identically zero
Rejected. It is quantitatively small, not absent.

### Audit E — proof status
The arbitrary far-screening escape is reduced, but the near/local pressure alignment branch remains open.

---

## 11. Updated slanted Rank-1 frontier

Persistent slanted alignment now reduces to

\[
\boxed{
P_{Q_0}^{\perp}
\left[
TF((p\cdot\nabla_h)\Delta\Sigma_h)
-
TF((p\cdot\nabla_h)\nabla_h^2P_{near})
\right]
=O(R^{-4})
}
\]

uniformly on the recurrent bounded-slant branch.

Thus the genuine hard gate is a **near-field viscous-pressure tensor alignment**, not an uncontrolled far-pressure multipole escape.

---

## 12. Next target — near-source localization gate

The next calculation should split `P_near` into

1. the immediate analytic core around the nodal filament;
2. an intermediate annulus/source architecture.

The aim is to determine whether the perpendicular pressure third jet generated by the immediate core is fixed by the local nodal jet, leaving only a mesoscopic annular turnover tensor to cancel the viscous forcing.

This is the **Near-Source Alignment Localization Gate (NSALG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
