# DSD M5-76 — Cross-Level Integrability Defect

Date: 2026-08-27

Status: **EXACT NECESSARY CLOSURE CONDITION AFTER M5-75 COEFFICIENT LOCKING / ONCE `m_a` IS RECOVERED FROM VELOCITY, PRESSURE-POISSON RECOVERS `m_aa`; THESE MUST BE RELATED BY ONE-DIMENSIONAL DIFFERENTIATION ALONG THE AMPLITUDE BRANCH / THE RESULTING DEFECT IS SCALE INVARIANT / GLOBAL REGULARITY UNPROVED.**

## 1. Common mean slope from M5-75

On an active genuinely crossing regular nested branch, exact endpoint saturation requires

\[
\beta_E=\beta_A.
\]

Write their common value as

\[
\boxed{\beta(\lambda,k,t)=m_{k,a}(\lambda,t).}
\]

The quantities used below are

\[
g_1:=|\nabla a|^2>0,
\]

\[
g_2:=\Delta a,
\]

and

\[
g_3:=2\nu\Delta b+\partial_iU_j\,\partial_jU_i.
\]

M5-73 requires

\[
\alpha g_1+\beta g_2+g_3=0
\]

on the entire level component, where

\[
\alpha=m_{k,aa}(\lambda,t).
\]

---

## 2. Once beta is fixed, only one elliptic scalar remains

Define the residual for a candidate \(\alpha\):

\[
R_\alpha(y)
:=
g_3(y)+\beta g_2(y)+\alpha g_1(y).
\]

Since \(g_1>0\) on a regular level, the exact endpoint requires one scalar \(\alpha\) to make this vanish everywhere.

Using the coarea inner product

\[
\langle f,g\rangle_\Gamma
:=
\int_{\Gamma_{\lambda,k}}fg\,\frac{dS}{|\nabla a|},
\]

the least-squares scalar is uniquely

\[
\boxed{
\alpha_P
:=
-
\frac{
\langle g_3+\beta g_2,g_1\rangle_\Gamma
}{
\langle g_1,g_1\rangle_\Gamma
}.
}
\]

Define the remaining intralevel Poisson defect

\[
\boxed{
K_\alpha
:=
\int_{\Gamma_{\lambda,k}}
|g_3+\beta g_2+\alpha_Pg_1|^2
\frac{dS}{|\nabla a|}.
}
\]

Then

\[
K_\alpha\ge0,
\]

and exact endpoint compatibility requires

\[
\boxed{K_\alpha=0.}
\]

When this holds,

\[
\boxed{\alpha_P=m_{k,aa}.}
\]

---

## 3. Cross-level derivative closure

The two coefficients are not independent because they must arise from one scalar mean function \(m_k(a,t)\):

\[
\beta=m_{k,a},
\qquad
\alpha_P=m_{k,aa}.
\]

Therefore, along every smooth regular nested branch,

\[
\boxed{
\alpha_P
=
\partial_\lambda\beta.
}
\]

Define the integrability defect

\[
\boxed{
\mathfrak I
:=
\alpha_P-\partial_\lambda\beta.
}
\]

Exact M5-70 saturation requires

\[
\boxed{\mathfrak I=0.}
\]

This condition is independent of the additive pressure gauge \(m_k\mapsto m_k+C(t)\).

---

## 4. Reconstruction interpretation

Suppose on one regular nested interval all of the following hold:

\[
\delta_\beta=0,
\qquad
K_A=0,
\qquad
K_\alpha=0,
\qquad
\mathfrak I=0.
\]

Then the velocity field determines a branch slope \(\beta(\lambda,t)\), and one can reconstruct

\[
\boxed{
m_k(\lambda,t)
=
C_k(t)
+
\int_{\lambda_0}^{\lambda}
\beta(s,k,t)\,ds.
}
\]

The cross-level condition ensures that the pressure-Poisson second derivative agrees with the derivative of this reconstructed slope.

Thus the endpoint pressure mean has been reduced to only one additive time-dependent branch gauge \(C_k(t)\).

The actual Navier--Stokes pressure and branch-gluing conditions must still determine whether those gauges are compatible globally.

---

## 5. Scaling audit

Under Navier--Stokes scaling,

\[
\beta_\Lambda(\lambda_\Lambda)
=
\Lambda\beta(\lambda),
\qquad
\lambda_\Lambda=\Lambda\lambda.
\]

Therefore

\[
\partial_{\lambda_\Lambda}\beta_\Lambda
=
\partial_\lambda\beta.
\]

Also

\[
\alpha_{P,\Lambda}=\alpha_P.
\]

Hence

\[
\boxed{\mathfrak I_\Lambda=\mathfrak I.}
\]

The cross-level integrability defect is exactly scale invariant.

This makes it particularly suitable for auditing a renormalized recurrent sequence.

---

## 6. A no-division version of the joint constraint

M5-74 gives

\[
F=\beta b.
\]

M5-73 gives

\[
\alpha g_1+\beta g_2+g_3=0.
\]

Multiplying the second equation by \(b\) and using \(\beta b=F\) eliminates \(\beta\):

\[
\boxed{
\alpha g_1b+g_2F+g_3b=0.
}
\]

Thus, defining

\[
R:=g_1b,
\qquad
H:=g_2F+g_3b,
\]

one scalar \(\alpha\) must satisfy

\[
\boxed{H=-\alpha R}
\]

over the entire level component.

This gives a pairwise rank-one test without dividing by \(b\), useful near the unavoidable zeros of the crossing field.

---

## 7. Rigidity ladder now obtained

An exact nontrivial M5-70 endpoint on a regular crossing branch must pass all of the following:

1. **M5-71 crossing dominance**
   \[
   T>B;
   \]
2. **M5-72 surface pressure lock**
   \[
   P-m=2\nu b;
   \]
3. **M5-74 amplitude rank-one condition**
   \[
   K_A=0;
   \]
4. **M5-75 elliptic/dynamic mean-slope locking**
   \[
   \delta_\beta=0;
   \]
5. **M5-76 remaining intralevel Poisson closure**
   \[
   K_\alpha=0;
   \]
6. **M5-76 cross-level integrability**
   \[
   \mathfrak I=0.
   \]

Failure of any one condition rules out exact minimal-payer saturation on that branch.

---

## 8. DSD audit

### GREEN

Once \(\beta\) is fixed, \(m_{aa}\) is the only remaining levelwise scalar in pressure Poisson.

### GREEN

The least-squares recovery of \(\alpha_P\) is unique on regular levels because \(g_1=|\nabla a|^2>0\).

### GREEN

The identity \(m_{aa}=\partial_am_a\) produces the exact scale-invariant defect \(\mathfrak I\).

### GREEN

The no-division equation \(\alpha g_1b+g_2F+g_3b=0\) remains meaningful at points where \(b=0\).

### YELLOW

Differentiation in \(\lambda\) requires a smooth nested component branch and sufficient regularity of the recovered coefficient \(\beta\).

### RED

The simultaneous zero set of these defects has not yet been proved empty.

---

## 9. Next calculation

The endpoint system has now been reduced almost entirely to velocity-only constraints on each regular branch.

The next audit should address the remaining global issue ignored by branch-local calculations:

- different connected superlevel branches carry additive gauges \(C_k(t)\);
- when branches are born, die, merge, or meet at critical amplitude levels, smoothness of one global pressure field forces those gauges to glue.

Critical-level branch gluing is therefore the next rigidity layer.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
