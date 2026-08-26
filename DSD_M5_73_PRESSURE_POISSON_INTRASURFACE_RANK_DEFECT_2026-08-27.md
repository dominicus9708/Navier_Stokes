# DSD M5-73 — Pressure-Poisson Intrasurface Rank Defect

Date: 2026-08-27

Status: **EXACT NECESSARY COMPATIBILITY TEST FOR THE M5-70 ENDPOINT ON REGULAR LEVEL BRANCHES / THE UNKNOWN COMPONENTWISE PRESSURE MEAN IS REDUCED TO TWO LEVELWISE SCALARS, PRODUCING A POINTWISE RANK-TWO CONDITION OVER EACH WHOLE SPEED SURFACE / NO UNIVERSAL NONEXISTENCE THEOREM YET.**

## 1. Endpoint representation

Let

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a.
\]

On a regular connected level branch M5-70 gives

\[
P=m_k(a,t)+2\nu b,
\]

where \(m_k\) denotes the componentwise coarea pressure mean identified in M5-72.

Assume locally in the active regular amplitude interval that the branch can be followed smoothly enough that

\[
m_{k,a},\quad m_{k,aa}
\]

exist.

---

## 2. Substitute into pressure Poisson

For incompressible Navier--Stokes,

\[
-\Delta P
=
\partial_iU_j\,\partial_jU_i.
\]

Because \(m_k=m_k(a,t)\),

\[
\Delta m_k(a,t)
=
m_{k,aa}|\nabla a|^2
+m_{k,a}\Delta a.
\]

Therefore exact endpoint compatibility requires

\[
-\left[
m_{k,aa}|\nabla a|^2
+m_{k,a}\Delta a
+2\nu\Delta b
\right]
=
\partial_iU_j\,\partial_jU_i.
\]

Equivalently,

\[
\boxed{
m_{k,aa}|\nabla a|^2
+m_{k,a}\Delta a
+2\nu\Delta b
+\partial_iU_j\,\partial_jU_i
=0.
}
\]

---

## 3. Three surface fields and only two scalar freedoms

Fix one regular level component

\[
\Gamma_{\lambda,k}.
\]

Define on that surface

\[
g_1:=|\nabla a|^2,
\]

\[
g_2:=\Delta a,
\]

and

\[
g_3:=2\nu\Delta b
+\partial_iU_j\,\partial_jU_i.
\]

Since \(a=\lambda\) is fixed over the whole component,

\[
\alpha_{\lambda,k}:=m_{k,aa}(\lambda,t),
\qquad
\beta_{\lambda,k}:=m_{k,a}(\lambda,t)
\]

are two scalars, not arbitrary functions of position on \(\Gamma_{\lambda,k}\).

Hence the full endpoint pressure-Poisson equation becomes

\[
\boxed{
\alpha_{\lambda,k}g_1(y)
+\beta_{\lambda,k}g_2(y)
+g_3(y)=0
\quad
\text{for every }y\in\Gamma_{\lambda,k}.
}
\]

This is the first direct elimination of the free pressure field from the endpoint problem.

---

## 4. Point-triple determinant test

Choose any three regular points \(y_1,y_2,y_3\) on the same connected level component.

The same vector

\[
(\alpha_{\lambda,k},\beta_{\lambda,k},1)
\]

must annihilate the three rows

\[
(g_1(y_j),g_2(y_j),g_3(y_j)).
\]

Therefore a necessary condition is

\[
\boxed{
\det
\begin{pmatrix}
g_1(y_1)&g_2(y_1)&g_3(y_1)\\
g_1(y_2)&g_2(y_2)&g_3(y_2)\\
g_1(y_3)&g_2(y_3)&g_3(y_3)
\end{pmatrix}
=0.
}
\]

Consequently, finding even one point triple on one active regular component with nonzero determinant rules out exact M5-70 saturation on that component.

This is a diagnostic obstruction, not yet proof that such a triple must always exist.

---

## 5. Integrated rank defect

A coordinate-free practical residual is

\[
\boxed{
K_{P}(\lambda,k,t)
:=
\inf_{\alpha,\beta\in\mathbb R}
\int_{\Gamma_{\lambda,k}}
|g_3+\alpha g_1+\beta g_2|^2
\frac{dS}{|\nabla a|}.
}
\]

Then

\[
K_P\ge0
\]

and exact M5-70 + pressure-Poisson compatibility requires

\[
\boxed{K_P(\lambda,k,t)=0}
\]

for almost every active regular amplitude level on the branch.

Thus \(K_P>0\) on any positive-measure set of active levels gives a strict obstruction to exact saturation.

---

## 6. Why this is stronger than saying the system is overdetermined

M5-70 stated that the endpoint is overdetermined.

M5-73 identifies the concrete algebraic content of that statement:

- the three spatially varying surface fields \(g_1,g_2,g_3\) must lie in one fixed two-parameter relation;
- only \(m_a\) and \(m_{aa}\) are available to fit the entire two-dimensional level component;
- all point triples must satisfy the determinant-zero condition.

The obstruction no longer refers to the unknown pressure itself.

---

## 7. Scaling audit

Under Navier--Stokes scaling

\[
U_\Lambda(x,t)=\Lambda U(\Lambda x,\Lambda^2t),
\]

we have

\[
a_\Lambda=\Lambda a,
\qquad
b_\Lambda=\Lambda^2 b.
\]

Hence

\[
g_{1,\Lambda}=\Lambda^4g_1,
\qquad
g_{2,\Lambda}=\Lambda^3g_2,
\qquad
g_{3,\Lambda}=\Lambda^4g_3.
\]

Meanwhile

\[
m_{a,\Lambda}=\Lambda m_a,
\qquad
m_{aa,\Lambda}=m_{aa}.
\]

Therefore all three terms

\[
m_{aa}g_1,
\quad
m_ag_2,
\quad
g_3
\]

scale as \(\Lambda^4\). The zero-rank compatibility condition is scale covariant.

---

## 8. DSD audit

### GREEN

The pressure-Poisson substitution and chain rule are exact on a smooth regular branch.

### GREEN

At fixed amplitude, \(m_a\) and \(m_{aa}\) are levelwise scalars, yielding the rank-two condition.

### GREEN

The point-triple determinant gives a pressure-mean-free necessary endpoint test.

### YELLOW

The branch label \(k\) may change at critical values or topology changes. The calculation is local to regular nested intervals and must not be extended through critical levels without additional work.

### YELLOW

\(K_P=0\) is only intralevel compatibility. It does not yet guarantee that the fitted coefficients \(\alpha,\beta\) arise from one differentiable mean function \(m_k(a,t)\) across neighboring levels.

### RED

No argument currently proves \(K_P>0\) for every nontrivial smooth recurrent endpoint.

---

## 9. Next calculation

There are now two additional exact conditions to impose:

1. cross-level integrability
   \[
   \alpha_{\lambda,k}=\partial_\lambda\beta_{\lambda,k};
   \]
2. the Navier--Stokes amplitude equation, which independently contains the same scalar \(\beta=m_a\).

Combining those should produce a second pressure-free compatibility defect and then lock the elliptic and dynamical fits to the same coefficient.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
