# DSD M5-72 — Level-Surface Geometry of the Exact Endpoint

Date: 2026-08-27

Status: **EXACT REGULAR-LEVEL CONSEQUENCES OF M5-70 / PRESSURE FLUCTUATION IS IDENTICAL TO A VISCOSITY-WEIGHTED NORMAL CROSSING SPEED / THE COMPONENTWISE PRESSURE CENTER IS FORCED TO BE THE COAREA MEAN / TANGENTIAL PRESSURE GRADIENT IS LOCKED TO THE CROSSING FIELD / GLOBAL REGULARITY UNPROVED.**

## 1. Regular level component

Let

\[
a:=|U|>0
\]

and fix a regular value \(a=\lambda\) on a connected level component

\[
\Gamma_{\lambda,k}
:=\{y:a(y,t)=\lambda\}\cap k.
\]

Write

\[
n:=\frac{\nabla a}{|\nabla a|}
\]

for the unit normal.

Define the streamline logarithmic speed derivative

\[
b:=U\cdot\nabla\log a
=\frac{U\cdot\nabla a}{a}.
\]

M5-70 gives

\[
\boxed{P-m_{P,k}(a,t)=2\nu b.}
\]

---

## 2. Exact normal-crossing relation

On \(a=\lambda\),

\[
U\cdot\nabla a
=|\nabla a|\,U\cdot n,
\]

so

\[
b
=\frac{|\nabla a|}{\lambda}U\cdot n.
\]

Therefore the endpoint equation becomes

\[
\boxed{
P-m_{P,k}(\lambda,t)
=
2\nu\frac{|\nabla a|}{\lambda}U\cdot n.
}
\]

Equivalently,

\[
\boxed{
U\cdot n
=
\frac{\lambda}{2\nu|\nabla a|}
\bigl(P-m_{P,k}(\lambda,t)\bigr).
}
\]

Thus, on every regular connected speed surface, the centered pressure is not merely correlated with normal crossing: it is pointwise proportional to it.

Consequences:

- \(P>m_{P,k}\) exactly where \(U\cdot n>0\);
- \(P<m_{P,k}\) exactly where \(U\cdot n<0\);
- \(P=m_{P,k}\) wherever \(U\cdot n=0\).

---

## 3. Incompressibility fixes the pressure center

For a connected regular boundary component of a superlevel region, incompressibility gives

\[
\int_{\Gamma_{\lambda,k}}U\cdot n\,dS=0.
\]

Substituting the endpoint normal-crossing relation,

\[
0
=
\frac{\lambda}{2\nu}
\int_{\Gamma_{\lambda,k}}
\frac{P-m_{P,k}(\lambda,t)}{|\nabla a|}\,dS.
\]

Hence

\[
\boxed{
\int_{\Gamma_{\lambda,k}}
\frac{P-m_{P,k}(\lambda,t)}{|\nabla a|}\,dS=0.
}
\]

Whenever the denominator is finite and positive,

\[
\boxed{
m_{P,k}(\lambda,t)
=
\frac{
\displaystyle\int_{\Gamma_{\lambda,k}}
P\,\frac{dS}{|\nabla a|}
}{
\displaystyle\int_{\Gamma_{\lambda,k}}
\frac{dS}{|\nabla a|}
}.
}
\]

Thus the M5-70 componentwise center is exactly the coarea-weighted pressure mean on the regular level component.

This is a consistency result, not a contradiction.

---

## 4. Tangential pressure locking

Let \(\nabla_{\Gamma}\) denote the tangential gradient along \(\Gamma_{\lambda,k}\).

Since both \(a=\lambda\) and \(m_{P,k}(\lambda,t)\) are constant along the fixed level component,

\[
\nabla_{\Gamma}m_{P,k}(a,t)=0.
\]

Taking the tangential derivative of M5-70 gives

\[
\boxed{
\nabla_{\Gamma}P
=
2\nu\nabla_{\Gamma}b.
}
\]

Thus every tangential pressure variation is completely determined by the tangential variation of the normal-crossing/log-speed field.

There is no independent tangential pressure degree of freedom left at exact endpoint saturation.

---

## 5. Normal derivative is the remaining pressure freedom

Spatially,

\[
P=m_{P,k}(a,t)+2\nu b.
\]

Therefore

\[
\boxed{
\nabla P
=
(\partial_a m_{P,k})\nabla a
+2\nu\nabla b.
}
\]

Its tangential projection is already fixed by Section 4.

The only levelwise scalar freedom left in \(P\) is the normal branch coefficient

\[
\partial_a m_{P,k}(a,t).
\]

The pressure-Poisson equation must determine whether such one-dimensional branch data can fit the full three-dimensional field.

---

## 6. DSD audit

### GREEN

The endpoint pressure fluctuation is exactly proportional to normal crossing velocity on every regular speed level.

### GREEN

The zero-flux identity forces the pressure center to be the coarea-weighted component mean.

### GREEN

Tangential pressure variation is locked by \(\nabla_\Gamma P=2\nu\nabla_\Gamma b\).

### YELLOW

These relations require a regular level branch with \(|\nabla a|\ne0\). Critical speed levels must be treated by limiting/coarea arguments and cannot simply be divided by \(|\nabla a|\).

### RED

The zero-flux identity does not rule out the endpoint; it verifies its centering consistency.

---

## 7. Next calculation

Substitute

\[
P=m_{P,k}(a,t)+2\nu b
\]

into pressure Poisson and exploit the fact that, on each fixed regular level component, \(m_a\) and \(m_{aa}\) are scalars constant over the entire surface.

This should produce an intralevel rank/compatibility defect that eliminates the unknown pressure mean.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
