# DSD M5-71 — Endpoint Crossing-Dominance Rigidity

Date: 2026-08-27

Status: **EXACT CONSEQUENCE OF M5-70 ENDPOINT SATURATION / A POSITIVE MINIMAL RECURRENT PUMP REQUIRES THE STREAMLINE SPEED-CROSSING CHANNEL TO EXCEED THE ENTIRE COMPLEMENTARY BULK+ANGULAR CHANNEL / NO GLOBAL-REGULARITY CLAIM.**

## 1. Starting point

M5-70 uses

\[
B:=A_w+G_w,\qquad T:=D_w-B>0,
\]

and

\[
X_w:=\bar J_w-\nu D_w.
\]

Exact completed-square saturation means

\[
H_w=0,
\]

hence

\[
\nu T=\nu B+X_w.
\]

Therefore

\[
\boxed{X_w=\nu(T-B).}
\]

This identity is specific to the exact minimal-payer endpoint.

---

## 2. Positive pump forces crossing dominance

If the returned pump is on a genuine rising interval,

\[
X_w>0.
\]

Since \(\nu>0\), the endpoint identity gives

\[
\boxed{T>B.}
\]

Equivalently, because

\[
D_w=T+B,
\]

we obtain

\[
\boxed{T>\frac12D_w.}
\]

Thus more than one half of the weighted derivative budget must lie in the speed-crossing channel represented by \(T\).

The endpoint cannot support a positive pump when the complementary bulk/angular channel dominates.

---

## 3. Geometric meaning of T

From M5-70,

\[
T
=
\int w(a)\frac{|U\cdot\nabla a|^2}{a}\,dy.
\]

On a regular speed level \(a=\lambda\), with unit normal

\[
n=\frac{\nabla a}{|\nabla a|},
\]

we have

\[
U\cdot\nabla a
=|\nabla a|\,U\cdot n.
\]

Hence \(T\) measures the weighted squared normal crossing of velocity through its own speed level sets.

By contrast,

\[
B=A_w+G_w
\]

contains the complementary formation/angular cost retained in M5-69.

Therefore the exact rising endpoint is not isotropic: it requires a quantitative directional bias toward crossing the speed foliation.

---

## 4. Fraction form

Define

\[
\theta:=\frac{T}{D_w}\in(0,1].
\]

Then

\[
B=D_w-T=(1-\theta)D_w,
\]

and

\[
X_w
=\nu(2T-D_w)
=\nu D_w(2\theta-1).
\]

Thus

\[
\boxed{
\frac{X_w}{\nu D_w}=2\theta-1.
}
\]

For a positive endpoint pump,

\[
\boxed{\theta>\frac12.}
\]

This gives a dimensionless endpoint anisotropy criterion.

---

## 5. Pressure payer at the endpoint

Exact Cauchy saturation in M5-70 gives

\[
S_{comp,w}=4\nu^2T.
\]

Using \(T=B+X_w/\nu\),

\[
\boxed{
S_{comp,w}
=4\nu^2B+4\nu X_w.
}
\]

Thus every unit of positive pump increment carries an exact additional pressure-variance cost \(4\nu X_w\) above the baseline complementary channel cost at the minimal endpoint.

This is an equality-case statement, not an independent global budget.

---

## 6. A useful dichotomy

For any exact M5-70 rising endpoint, one of the following must hold:

1. \(B>0\), in which case
   \[
   \frac{T}{B}=1+\frac{X_w}{\nu B}>1;
   \]
2. \(B=0\), in which case
   \[
   X_w=\nu T>0
   \]
   and the entire derivative budget is in the crossing channel.

The second case is a highly degenerate geometry and should be audited separately if it survives the pressure-Poisson test.

---

## 7. DSD audit

### GREEN

The identity \(X_w=\nu(T-B)\) follows algebraically from \(H_w=0\).

### GREEN

Positive endpoint pumping forces \(T>B\), equivalently \(T>D_w/2\).

### GREEN

This yields a dimensionless directional criterion \(X_w/(\nu D_w)=2T/D_w-1\).

### YELLOW

Crossing dominance is necessary but not yet contradictory. Smooth incompressible fields can have substantial normal crossing through local speed level sets while maintaining zero total component flux.

### RED

It would be invalid to infer nonexistence merely from \(T>B\).

---

## 8. Next calculation

Use the exact pressure relation

\[
P-m_{P,k}(a,t)=2\nu\,U\cdot\nabla\log a
\]

on each regular connected level branch to derive:

- the exact normal-flux/pressure relation on \(\Gamma_{a,k}\),
- the tangential pressure-gradient condition,
- and then a levelwise pressure-Poisson compatibility constraint in which the unknown mean \(m_{P,k}\) can be eliminated.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
