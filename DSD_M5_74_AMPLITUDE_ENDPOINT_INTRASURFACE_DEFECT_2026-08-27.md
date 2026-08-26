# DSD M5-74 — Amplitude-Equation Intrasurface Endpoint Defect

Date: 2026-08-27

Status: **EXACT NECESSARY DYNAMICAL COMPATIBILITY CONDITION FOR M5-70 / THE NAVIER--STOKES AMPLITUDE EQUATION INDEPENDENTLY RECOVERS THE SAME LEVELWISE SCALAR `m_a` FROM VELOCITY DATA / A PRESSURE-FREE MEAN-ZERO IDENTITY FOLLOWS / GLOBAL REGULARITY UNPROVED.**

## 1. Starting equations

Let

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a
=\frac{U\cdot\nabla a}{a}.
\]

The exact amplitude equation is

\[
\partial_t a
+U\cdot\nabla a
+\frac Ua\cdot\nabla P
=
\nu\left[
\Delta a
-
\frac{|\nabla U|^2-|\nabla a|^2}{a}
\right].
\]

Define the nonnegative directional defect

\[
C:=|\nabla U|^2-|\nabla a|^2\ge0.
\]

At the M5-70 endpoint,

\[
P=m_k(a,t)+2\nu b.
\]

Write

\[
\beta:=m_{k,a}(a,t).
\]

Then

\[
\nabla P=\beta\nabla a+2\nu\nabla b.
\]

---

## 2. Eliminate pressure from the amplitude equation

Because

\[
U\cdot\nabla a=ab,
\]

we have

\[
\frac Ua\cdot\nabla P
=
\beta b
+\frac{2\nu}{a}U\cdot\nabla b.
\]

Hence

\[
\partial_ta
+ab
+\beta b
+\frac{2\nu}{a}U\cdot\nabla b
=
\nu\Delta a-\nu\frac Ca.
\]

Define the velocity-only scalar

\[
\boxed{
F
:=
\nu\Delta a
-\nu\frac Ca
-\partial_t a
-ab
-\frac{2\nu}{a}U\cdot\nabla b.
}
\]

Then exact endpoint dynamics requires

\[
\boxed{F=\beta b.}
\]

---

## 3. One scalar must fit an entire speed surface

Fix a regular connected level component

\[
\Gamma_{\lambda,k}.
\]

Because \(\beta=m_{k,a}(\lambda,t)\) depends only on the fixed level and branch, it is constant over \(\Gamma_{\lambda,k}\).

Therefore

\[
\boxed{
F(y)=\beta_{\lambda,k}b(y)
\quad
\text{for every }y\in\Gamma_{\lambda,k}.
}
\]

For any two points \(y_1,y_2\) on the same component,

\[
\boxed{
F(y_1)b(y_2)-F(y_2)b(y_1)=0.
}
\]

At any point where

\[
b=0,
\]

exact endpoint compatibility forces

\[
\boxed{F=0.}
\]

This is a purely velocity-based necessary test.

---

## 4. Integrated amplitude defect

Define

\[
\boxed{
K_A(\lambda,k,t)
:=
\inf_{\beta\in\mathbb R}
\int_{\Gamma_{\lambda,k}}
|F-\beta b|^2
\frac{dS}{|\nabla a|}.
}
\]

Then

\[
K_A\ge0,
\]

and exact M5-70 compatibility requires

\[
\boxed{K_A(\lambda,k,t)=0}
\]

for almost every active regular level.

Thus a positive amplitude defect on a positive-measure set of active levels excludes exact minimal-payer saturation there.

---

## 5. A pressure-free level-average identity

M5-72 and incompressibility give

\[
\int_{\Gamma_{\lambda,k}}
b\,\frac{dS}{|\nabla a|}
=
\frac1\lambda
\int_{\Gamma_{\lambda,k}}U\cdot n\,dS
=0.
\]

Integrating

\[
F=\beta b
\]

over the same coarea measure therefore yields the necessary condition

\[
\boxed{
\int_{\Gamma_{\lambda,k}}
F\,\frac{dS}{|\nabla a|}=0.
}
\]

Since the term \(ab\) also has zero coarea mean on a fixed level, this can be written as

\[
\boxed{
\int_{\Gamma_{\lambda,k}}
\left[
\nu\Delta a
-\nu\frac Ca
-\partial_t a
-\frac{2\nu}{a}U\cdot\nabla b
\right]
\frac{dS}{|\nabla a|}
=0.
}
\]

This identity contains no pressure and no unknown mean coefficient.

---

## 6. Sign-change consequence on a crossing level

If \(b\) is continuous on a connected closed regular level component and is not identically zero, then its coarea mean is zero.

Therefore it must take both positive and negative values and hence vanish somewhere on the component.

At exact endpoint saturation:

\[
P-m_k=2\nu b
\]

and

\[
F=\beta b.
\]

Thus on every such genuinely crossing level there are points where simultaneously

\[
\boxed{b=0,\qquad P=m_k,\qquad F=0.}
\]

This is a useful geometric anchor, but not yet a contradiction.

---

## 7. Scaling audit

Under

\[
U_\Lambda(x,t)=\Lambda U(\Lambda x,\Lambda^2t),
\]

we have

\[
a_\Lambda=\Lambda a,
\qquad
b_\Lambda=\Lambda^2b,
\qquad
\beta_\Lambda=\Lambda\beta.
\]

Every term in \(F\) scales as \(\Lambda^3\), so

\[
F_\Lambda=\Lambda^3F
\]

and

\[
\beta_\Lambda b_\Lambda=\Lambda^3\beta b.
\]

Hence the zero-defect relation is scale covariant.

---

## 8. DSD audit

### GREEN

The amplitude equation and endpoint substitution give the exact relation \(F=m_ab\).

### GREEN

At fixed amplitude, \(m_a\) is one scalar over the entire connected level component, yielding the pairwise rank-one test.

### GREEN

The coarea zero-flux property removes \(m_a\) completely after level averaging.

### YELLOW

The formulas require \(a>0\) and a regular level branch. Zeros of velocity and critical speed levels need separate limiting treatment.

### YELLOW

The sign-change statement assumes a connected closed regular component and continuity of \(b\).

### RED

The existence of points with \(b=F=0\) is not itself enough to force triviality.

---

## 9. Next calculation

M5-73 and M5-74 independently determine the same levelwise coefficient

\[
\beta=m_{k,a}.
\]

The exact endpoint therefore requires:

- pressure-Poisson fit coefficient \(\beta_P\),
- amplitude-equation fit coefficient \(\beta_A\),
- and cross-level derivative relation \(m_{aa}=\partial_a m_a\)

to agree simultaneously.

This joint coefficient locking is the next rigidity condition.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
