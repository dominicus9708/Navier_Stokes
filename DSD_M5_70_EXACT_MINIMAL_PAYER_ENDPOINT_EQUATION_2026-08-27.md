# DSD M5-70 — Exact Minimal-Payer Endpoint Equation

Date: 2026-08-27

Status: **EXACT EQUALITY-CASE CLASSIFICATION / SIMULTANEOUS SATURATION OF THE COMPONENTWISE PRESSURE CAUCHY INEQUALITY AND THE M5-69 COMPLETED-SQUARE ENVELOPE FORCES THE CENTERED PRESSURE FLUCTUATION TO EQUAL `2 nu` TIMES THE STREAMLINE DERIVATIVE OF LOG SPEED / THE MINIMAL RECURRENT PUMP ENDPOINT IS THEREFORE AN OVERDETERMINED PRESSURE--VELOCITY SYSTEM, NOT A FREE LARGE-PRESSURE CONFIGURATION / NO NONEXISTENCE THEOREM YET / GLOBAL REGULARITY UNPROVED.**

## 1. Variables from M5-69

Set

\[
B:=A_w+G_w,
\qquad
T:=D_w-B>0,
\]

and

\[
J:=\bar J_w
=\nu D_w+X_w.
\]

The componentwise-centered pressure inequality is

\[
\boxed{J^2\le S_{comp,w}T.}
\]

M5-69 rewrites its sharp lower envelope as

\[
\boxed{
S_{comp,w}
\ge
4\nu(\nu B+X_w)+H_w,
}
\]

with

\[
H_w
=
\frac{[\nu T-(\nu B+X_w)]^2}{T}.
\]

---

## 2. Equality in the weighted Cauchy step

In the finite amplitude band, write the componentwise centered pressure as

\[
\widetilde P
:=
P-m_{P,k}(a,t)
\]

on the nesting branch associated with the connected superlevel component containing the point.

The averaged pressure flux is

\[
J
=
\int w(a)\widetilde P\,U\cdot\nabla a\,dy.
\]

The two Cauchy factors are

\[
S_{comp,w}
=
\int a\,w(a)|\widetilde P|^2dy
\]

and

\[
T
=
\int
w(a)
\frac{|U\cdot\nabla a|^2}{a}dy.
\]

Equality in Cauchy--Schwarz requires linear dependence of the weighted factors. Therefore there is one scalar `c(t)` such that, almost everywhere on the active weighted region,

\[
\boxed{
\widetilde P
=
c(t)
\frac{U\cdot\nabla a}{a}.
}
\]

Equivalently,

\[
\boxed{
P-m_{P,k}(a,t)
=
c(t)
U\cdot\nabla\log a.
}
\]

---

## 3. The proportionality constant equals `J/T`

Under exact Cauchy saturation,

\[
J=cT
\]

and

\[
S_{comp,w}=c^2T.
\]

Hence

\[
\boxed{c=J/T.}
\]

At this stage `c` could still be state dependent.

---

## 4. Completed-square saturation fixes `c=2nu`

The M5-69 algebraic envelope is saturated exactly when

\[
H_w=0.
\]

Thus

\[
\boxed{
\nu T
=
\nu B+X_w.
}
\]

But

\[
D_w=T+B,
\]

so

\[
\begin{aligned}
J
&=
\nu D_w+X_w\\
&=
\nu T+\nu B+X_w\\
&=
\nu T+\nu T\\
&=2\nu T.
\end{aligned}
\]

Therefore

\[
\boxed{c=J/T=2\nu.}
\]

The exact minimal-payer endpoint satisfies the universal relation

\[
\boxed{
P-m_{P,k}(a,t)
=
2\nu
\frac{U\cdot\nabla a}{a}.
}
\]

or

\[
\boxed{
P-m_{P,k}(|U|,t)
=
2\nu
U\cdot\nabla\log|U|.
}
\]

The coefficient is fixed entirely by viscosity.

---

## 5. Streamline interpretation

At fixed time, let a streamline be parametrized by

\[
\frac{dY}{ds}=U(Y(s),t).
\]

Then

\[
U\cdot\nabla\log a
=
\frac d{ds}
\log a(Y(s),t).
\]

Thus the endpoint equation becomes

\[
\boxed{
P-m_{P,k}(a,t)
=
2\nu
\frac d{ds}
\log|U(Y(s),t)|.
}
\]

So the pressure fluctuation relative to the componentwise amplitude-level mean is exactly proportional to the spatial logarithmic acceleration/deceleration of speed along the streamline.

This is much more restrictive than requiring pressure merely to be large or oscillatory.

---

## 6. Compatibility with zero component flux

The componentwise mean definition is automatically compatible with the endpoint relation.

Indeed on a regular level boundary `a=lambda`,

\[
\frac{U\cdot\nabla a}{a|\nabla a|}
=
\frac{U\cdot n}{\lambda}.
\]

Therefore the weighted mean of the right-hand side with respect to `dS/|grad a|` is proportional to

\[
\int_{\Gamma_{\lambda,k}}U\cdot n\,dS,
\]

which vanishes by incompressibility.

Hence the endpoint equation is **not** excluded merely by the centering condition. A stronger pressure-Poisson/dynamical argument is required.

---

## 7. Pressure-Poisson compatibility equation

For an incompressible smooth solution,

\[
-\Delta P
=
\partial_i\partial_j(U_iU_j)
=
\partial_iU_j\,\partial_jU_i.
\]

On a regular component branch where `m_{P,k}(a,t)` can be regarded as a scalar function of the amplitude, the minimal-payer relation gives formally

\[
P
=
m_{P,k}(a,t)
+2\nu U\cdot\nabla\log a.
\]

Substituting into pressure Poisson yields the overdetermined compatibility condition

\[
\boxed{
-\Delta
\left[
m_{P,k}(a,t)
+2\nu U\cdot\nabla\log a
\right]
=
\partial_iU_j\,\partial_jU_i.
}
\]

This is to be imposed simultaneously with

\[
\nabla\cdot U=0
\]

and the Navier--Stokes evolution.

No claim is made here that this overdetermined system has only the zero solution; that is the next rigidity question.

---

## 8. Relation to the amplitude equation

Dotting Navier--Stokes with `U/a` gives the exact smooth amplitude equation

\[
\boxed{
\partial_t a
+U\cdot\nabla a
+
\frac{U}{a}\cdot\nabla P
=
\nu
\left[
\Delta a
-
\frac{|\nabla U|^2-|\nabla a|^2}{a}
\right].
}
\]

The last nonnegative defect numerator

\[
|\nabla U|^2-|\nabla a|^2
\ge0
\]

measures directional variation of the vector field not visible in the scalar speed alone.

At the minimal-payer endpoint, `P` is no longer independent in this equation: its amplitude-level fluctuation is fixed by the streamline logarithmic derivative.

Thus the endpoint combines an elliptic pressure constraint and a scalar amplitude evolution constraint with one common velocity field.

---

## 9. DSD audit

### GREEN

Exact Cauchy saturation forces `P-m` to be proportional to `(U dot grad a)/a`.

### GREEN

Exact completed-square saturation fixes the proportionality constant uniquely to `2 nu`.

### GREEN

The resulting relation is compatible with the componentwise zero-flux centering, so no false contradiction is claimed there.

### YELLOW

The endpoint is an overdetermined pressure-Poisson + amplitude-evolution + incompressibility system. Its nonexistence or rigidity has not yet been established.

### RED

It would be invalid to conclude global regularity merely from the unusual form of the endpoint equation.

---

## 10. Next rigidity split

The recurrent pump class now has a clean compactness dichotomy.

Either it stays a uniform distance away from exact minimal-payer saturation, producing a fixed positive Cauchy/balance surplus on every returned pump,

or a saturating sequence converges to a limiting pump satisfying

\[
\boxed{
P-m_{P,k}(|U|,t)
=
2\nu U\cdot\nabla\log|U|
}
\]

on the finite active band together with pressure Poisson and incompressibility.

The next direct calculation should test this exact endpoint system before attempting more general pressure estimates.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
