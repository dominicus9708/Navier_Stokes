# DSD M5-75 — Elliptic/Dynamic Locking of the Endpoint Mean Slope

Date: 2026-08-27

Status: **EXACT VELOCITY-ONLY NECESSARY CONDITION ON A REGULAR NESTED LEVEL BRANCH / THE SAME PRESSURE-MEAN SLOPE `m_a` IS RECOVERED INDEPENDENTLY FROM PRESSURE-POISSON FLUX AND FROM THE AMPLITUDE EQUATION / THEIR DIFFERENCE IS A SCALE-INVARIANT ENDPOINT DEFECT / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

Let

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a.
\]

Fix a smooth nested connected superlevel branch

\[
\Omega_{\lambda,k}:=\{a>\lambda\}\cap k
\]

with regular closed boundary

\[
\Gamma_{\lambda,k}:=\partial\Omega_{\lambda,k}.
\]

Use

\[
n:=\frac{\nabla a}{|\nabla a|}
\]

pointing toward increasing \(a\). The outward unit normal of the superlevel set is therefore \(-n\).

At exact M5-70 saturation,

\[
P=m_k(a,t)+2\nu b.
\]

Write

\[
\beta(\lambda,k,t):=m_{k,a}(\lambda,t).
\]

---

## 2. Elliptic recovery of beta from pressure Poisson

Pressure Poisson is

\[
-\Delta P
=Q_U,
\qquad
Q_U:=\partial_iU_j\,\partial_jU_i.
\]

Integrating over \(\Omega_{\lambda,k}\),

\[
-\int_{\Omega_{\lambda,k}}\Delta P\,dy
=
\int_{\Omega_{\lambda,k}}Q_U\,dy.
\]

Because the outward normal is \(-n\),

\[
-\int_{\Omega}\Delta P\,dy
=
\int_{\Gamma}\partial_nP\,dS.
\]

The endpoint representation gives

\[
\partial_nP
=
\beta|\nabla a|
+2\nu\partial_nb.
\]

Hence

\[
\beta
\int_{\Gamma_{\lambda,k}}|\nabla a|\,dS
+
2\nu
\int_{\Gamma_{\lambda,k}}\partial_nb\,dS
=
\int_{\Omega_{\lambda,k}}Q_U\,dy.
\]

Since the regular level has \(|\nabla a|>0\), define

\[
A_1(\lambda,k,t)
:=
\int_{\Gamma_{\lambda,k}}|\nabla a|\,dS>0.
\]

Then the elliptically recovered mean slope is

\[
\boxed{
\beta_E
:=
\frac{
\displaystyle\int_{\Omega_{\lambda,k}}Q_U\,dy
-
2\nu\displaystyle\int_{\Gamma_{\lambda,k}}\partial_nb\,dS
}{
\displaystyle\int_{\Gamma_{\lambda,k}}|\nabla a|\,dS
}.
}
\]

Exact endpoint compatibility requires

\[
\boxed{m_{k,a}=\beta_E.}
\]

This formula contains no pressure.

---

## 3. Dynamical recovery of beta from the amplitude equation

M5-74 gives

\[
F=\beta b,
\]

where

\[
F
=
\nu\Delta a
-\nu\frac{|\nabla U|^2-|\nabla a|^2}{a}
-\partial_ta
-ab
-\frac{2\nu}{a}U\cdot\nabla b.
\]

On a genuinely crossing level, \(b\not\equiv0\). Using the coarea inner product

\[
\langle f,g\rangle_\Gamma
:=
\int_{\Gamma_{\lambda,k}}
f g\,\frac{dS}{|\nabla a|},
\]

exact compatibility yields

\[
\boxed{
\beta_A
:=
\frac{\langle F,b\rangle_\Gamma}
{\langle b,b\rangle_\Gamma}
=m_{k,a}.
}
\]

Again, \(\beta_A\) is determined entirely by velocity and its derivatives.

---

## 4. Elliptic/dynamic coefficient locking

An exact M5-70 endpoint must satisfy both reconstructions simultaneously.

Therefore

\[
\boxed{\beta_E=\beta_A.}
\]

Define the coefficient mismatch

\[
\boxed{
\delta_\beta
:=
\beta_E-\beta_A.
}
\]

Then

\[
\boxed{\delta_\beta=0}
\]

is a necessary endpoint condition on every active genuinely crossing regular level.

A single active regular level with \(\delta_\beta\ne0\) excludes exact M5-70 saturation there.

---

## 5. Scale-invariant form

Under Navier--Stokes scaling,

\[
\beta_{E,\Lambda}=\Lambda\beta_E,
\qquad
\beta_{A,\Lambda}=\Lambda\beta_A,
\qquad
\lambda_\Lambda=\Lambda\lambda.
\]

Therefore

\[
\boxed{
\mathfrak B
:=
\frac{\beta_E-\beta_A}{\lambda}
}
\]

is scale invariant:

\[
\boxed{\mathfrak B_\Lambda=\mathfrak B.}
\]

This is a new critical endpoint diagnostic.

It is not an energy budget by itself; its significance is that a saturating recurrent sequence must drive this dimensionless incompatibility to zero.

---

## 6. Scaling check of the elliptic formula

Under

\[
U_\Lambda(x,t)=\Lambda U(\Lambda x,\Lambda^2t),
\]

we have

\[
Q_{U,\Lambda}=\Lambda^4Q_U,
\qquad
dy_\Lambda=\Lambda^{-3}dy,
\]

so

\[
\int_{\Omega_\Lambda}Q_{U,\Lambda}\,dy
=\Lambda\int_\Omega Q_U\,dy.
\]

Also

\[
b_\Lambda=\Lambda^2b,
\qquad
\partial_{n_\Lambda}b_\Lambda=\Lambda^3\partial_nb,
\qquad
dS_\Lambda=\Lambda^{-2}dS,
\]

hence

\[
\int_{\Gamma_\Lambda}\partial_{n_\Lambda}b_\Lambda\,dS
=\Lambda\int_\Gamma\partial_nb\,dS.
\]

Finally,

\[
|\nabla a_\Lambda|=\Lambda^2|\nabla a|,
\]

so

\[
\int_{\Gamma_\Lambda}|\nabla a_\Lambda|\,dS
=
\int_\Gamma|\nabla a|\,dS.
\]

Thus \(\beta_E\) scales exactly as \(\Lambda\), as required.

---

## 7. Relation to M5-73

M5-73 imposes the stronger pointwise surface condition

\[
m_{aa}g_1+m_ag_2+g_3=0.
\]

M5-75 is obtained from an integrated elliptic flux identity and only recovers \(m_a\).

Therefore:

- \(\delta_\beta\ne0\) immediately rules out the endpoint;
- \(\delta_\beta=0\) does **not** imply the full M5-73 pointwise rank condition.

The scalar locking test is easier to audit but logically weaker than complete intralevel pressure-Poisson compatibility.

---

## 8. DSD audit

### GREEN

The elliptic reconstruction follows directly from pressure Poisson, the divergence theorem, and the M5-70 endpoint representation.

### GREEN

The amplitude reconstruction follows from M5-74 whenever \(b\not\equiv0\) on the level.

### GREEN

Their normalized mismatch \(\mathfrak B=(\beta_E-\beta_A)/\lambda\) is scale invariant.

### YELLOW

Nested smooth component structure is required for the componentwise superlevel integration. Critical/topology-changing levels remain separate.

### YELLOW

Levels with \(b\equiv0\) do not determine \(\beta_A\) through the quotient and require the degenerate-case audit.

### RED

No current argument proves \(\mathfrak B\ne0\) for every possible nontrivial recurrent endpoint.

---

## 9. Next calculation

When \(\delta_\beta=0\), the common velocity-derived coefficient

\[
\beta(\lambda,k,t)
\]

must still be the derivative of one pressure mean function. The M5-73 coefficient

\[
\alpha=m_{aa}
\]

must therefore satisfy

\[
\alpha=\partial_\lambda\beta.
\]

This cross-level integrability condition is scale invariant and gives the next pressure-free rigidity defect.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
