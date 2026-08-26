# DSD M5-78 — Degenerate Tangential-Level Escape Closed for Positive Endpoint Pumps

Date: 2026-08-27

Status: **EXACT NECESSARY CONSEQUENCE OF M5-71/M5-70 / A POSITIVE MINIMAL ENDPOINT PUMP CANNOT BE SUPPORTED ONLY ON LEVELS WHERE `b = U dot grad log a` VANISHES / GENUINE CROSSING MUST OCCUR ON A POSITIVE WEIGHTED SET / INDIVIDUAL DEGENERATE LEVELS MAY STILL OCCUR / GLOBAL REGULARITY UNPROVED.**

## 1. Crossing variable

Let

\[
a:=|U|>0,
\qquad
b:=U\cdot\nabla\log a.
\]

Then

\[
U\cdot\nabla a=ab.
\]

The M5-70 crossing factor is

\[
T
=
\int
w(a)\frac{|U\cdot\nabla a|^2}{a}\,dy.
\]

Therefore

\[
\boxed{
T
=
\int a\,w(a)|b|^2\,dy.
}
\]

So `T` is exactly the weighted `L^2` mass of the streamline log-speed derivative.

---

## 2. If b vanishes on the active region, T vanishes

Suppose

\[
b=0
\]

almost everywhere on the support of the active weight `w(a)`.

Then

\[
\boxed{T=0.}
\]

But exact completed-square saturation gives, from M5-71,

\[
X_w=\nu(T-B),
\qquad
B=A_w+G_w\ge0.
\]

Hence

\[
X_w=-\nu B\le0.
\]

Therefore

\[
\boxed{
b=0\text{ a.e. on the active region}
\quad\Longrightarrow\quad
X_w\le0.}
\]

This is incompatible with a genuine rising endpoint pump

\[
X_w>0.
\]

---

## 3. Positive endpoint pumping requires genuine crossing mass

For an exact positive endpoint pump,

\[
X_w>0,
\]

M5-71 gives

\[
T>B\ge0.
\]

Therefore

\[
\boxed{T>0.}
\]

Equivalently,

\[
\boxed{
\int a\,w(a)|b|^2dy>0.
}
\]

Thus `b` is nonzero on a set of positive weighted volume measure.

Under the regular coarea decomposition, this requires a positive-measure family of active regular levels carrying nonzero crossing density, except for the usual caveat concerning critical-value sets.

Consequently the M5-75 dynamical recovery of `m_a` is not vacuous: a positive endpoint cannot hide exclusively in the `b identically 0` sector.

---

## 4. What happens on an individual degenerate level

An individual regular component may still satisfy

\[
b\equiv0
\quad\text{on }\Gamma_{\lambda,k}.
\]

Then M5-70 gives

\[
\boxed{P=m_k(\lambda,t)}
\]

on that entire level component.

So the pressure is tangentially constant there.

M5-74 also requires

\[
F=\beta b=0,
\]

hence

\[
\boxed{F\equiv0}
\]

on that degenerate level.

However `beta=m_a` is not determined by dividing or projecting against `b` on that particular component.

Such levels therefore remain admissible as isolated or lower-dimensional pieces of the active band, but they cannot carry the positive crossing budget required by M5-71.

---

## 5. Coarea crossing density

For a regular level component, define

\[
\tau(\lambda,k,t)
:=
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}
|U\cdot n|^2\,dS.
\]

Using coarea,

\[
\boxed{
T
=
\int
w(\lambda)
\sum_k\tau(\lambda,k,t)\,d\lambda.
}
\]

Thus a positive exact endpoint requires

\[
\int
w(\lambda)
\sum_k\tau(\lambda,k,t)\,d\lambda>0.
\]

This gives a levelwise form of the genuine-crossing requirement.

---

## 6. Relation to the exact pressure variance

At M5-70 saturation,

\[
P-m_k=2\nu b.
\]

Therefore

\[
S_{comp,w}
=
\int a\,w(a)|P-m_k|^2dy
=
4\nu^2
\int a\,w(a)|b|^2dy.
\]

Hence

\[
\boxed{S_{comp,w}=4\nu^2T.}
\]

The pressure variance and crossing mass are exactly the same endpoint degree of freedom up to the universal factor `4 nu^2`.

There is no separate large-pressure escape at exact saturation.

---

## 7. DSD audit

### GREEN

`T = integral a w(a) |b|^2` is an exact algebraic identity.

### GREEN

A positive exact endpoint requires `T>0`, hence genuine nonzero crossing on a positive weighted set.

### GREEN

The `b identically 0` sector cannot support the positive pump required by M5-71.

### YELLOW

Individual degenerate regular levels may still occur and need not be excluded.

### YELLOW

Turning positive weighted volume crossing into a uniform positive measure of regular amplitude levels requires quantitative coarea bounds not yet supplied.

### RED

This closes only the purely tangential escape; it does not prove the remaining crossing endpoint impossible.

---

## 8. Current endpoint bottleneck

A nontrivial exact positive endpoint must now simultaneously have:

\[
T>B,
\]

positive crossing mass,

\[
K_A=0,
\qquad
\delta_\beta=0,
\qquad
K_\alpha=0,
\qquad
\mathfrak I=0,
\]

plus any applicable branch-gluing/holonomy conditions.

The remaining endpoint is therefore a genuinely crossing, elliptic-dynamic locked configuration rather than a tangential degeneracy.

The next audit should determine whether the recurrence mechanism used earlier is recurrence of the **renormalized profile** or of the physical unforced Navier--Stokes flow, because only the latter would be immediately killed by the ordinary energy identity. This distinction must be explicit before any recurrence-based contradiction is attempted.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
