# DSD M5-67 — Levelwise Pressure-Variance Payer

Date: 2026-08-27

Status: **SHARPENED INCOMPRESSIBILITY/PRESSURE AUDIT / THE PRESSURE PUMP IS INSENSITIVE TO THE LEVELWISE CONSTANT PART OF PRESSURE BECAUSE THE NET VELOCITY FLUX THROUGH EVERY BOUNDED AMPLITUDE SUPERLEVEL BOUNDARY IS ZERO / THE M5-56/M5-66 PAYER CAN BE REPLACED BY A STRICTLY SMALLER CONDITIONAL PRESSURE-VARIANCE PAYER / A ROBUST UPSTROKE REQUIRES PRESSURE OSCILLATION ALONG AMPLITUDE LEVEL SETS, NOT MERELY LARGE PRESSURE MAGNITUDE / GLOBAL REGULARITY UNPROVED.**

## 1. Zero unweighted flux through an amplitude level

Let

\[
a=|U|,
\qquad
\Omega_\lambda:=\{y:a(y)>\lambda\}.
\]

For a positive regular amplitude level in the localized W1 pump cell, the relevant superlevel region is bounded because the outer `1/r` tail eventually falls below the fixed positive band.

Since

\[
\nabla\cdot U=0,
\]

the divergence theorem gives

\[
\boxed{
\int_{\partial\Omega_\lambda}
U\cdot n_{out}\,dS
=0.
}
\]

Up to orientation convention for the level normal `n_lambda`, this is

\[
\boxed{
\int_{\Sigma_\lambda}
U\cdot n_\lambda\,dS
=0.
}
\]

This remains true if the superlevel has several connected components, provided all boundary components are included with the induced orientation.

---

## 2. Subtract any levelwise pressure constant

The threshold pressure flux is

\[
J_P(\lambda)
=
\int_{\Sigma_\lambda}
P\,U\cdot n_\lambda\,dS.
\]

For any scalar `c(lambda,t)` constant on the whole level boundary,

\[
\begin{aligned}
J_P(\lambda)
&=
\int_{\Sigma_\lambda}
(P-c)U\cdot n_\lambda\,dS\\
&+c
\int_{\Sigma_\lambda}U\cdot n_\lambda\,dS.
\end{aligned}
\]

The second term vanishes. Hence

\[
\boxed{
J_P(\lambda)
=
\int_{\Sigma_\lambda}
(P-c(\lambda,t))
U\cdot n_\lambda\,dS.
}
\]

Therefore the levelwise constant pressure mode does no threshold work.

---

## 3. Optimal weighted level mean

The M5-37 surface Cauchy payer uses the measure

\[
d\mu_\lambda
:=
\frac{dS}{|\nabla a|}.
\]

Choose `m_P(lambda,t)` to minimize

\[
\int_{\Sigma_\lambda}
|P-c|^2d\mu_\lambda.
\]

Thus

\[
\boxed{
m_P(\lambda,t)
=
\frac{
\int_{\Sigma_\lambda}
P|\nabla a|^{-1}dS
}{
\int_{\Sigma_\lambda}
|\nabla a|^{-1}dS
}
}
\]

whenever the denominator is finite and nonzero.

Define the conditional levelwise pressure variance density

\[
\boxed{
V_P(\lambda,t)
:=
\int_{\Sigma_\lambda}
\frac{|P-m_P(\lambda,t)|^2}{|\nabla a|}dS.
}
\]

By optimality,

\[
V_P(\lambda,t)
\le
\int_{\Sigma_\lambda}
\frac{|P|^2}{|\nabla a|}dS
=
-\partial_\lambda Q_P(\lambda,t).
\]

Thus this is a strictly sharper payer unless the optimal level mean happens to vanish.

---

## 4. Sharpened single-level pressure Cauchy inequality

Subtract `m_P(lambda,t)` in the pressure flux and repeat the weighted surface Cauchy inequality:

\[
|J_P(\lambda)|^2
\le
V_P(\lambda)
\int_{\Sigma_\lambda}
(U\cdot n_\lambda)^2|\nabla a|dS.
\]

Since `|U|=lambda` on `Sigma_lambda`, this implies

\[
\boxed{
|J_P(\lambda)|^2
\le
\lambda^2V_P(\lambda)B(\lambda).
}
\]

Retaining the crossing angle gives the corresponding sharper normal-component payer rather than replacing it by the full `lambda^2 B` term.

---

## 5. Amplitude-mollified variance payer

Define

\[
\boxed{
S_{var,w}
:=
\int_0^\infty
w(\lambda)\lambda V_P(\lambda)d\lambda.
}
\]

By coarea, if we regard `m_P(a(y),t)` as the levelwise conditional mean,

\[
\boxed{
S_{var,w}
=
\int
 a\,w(a)
|P-m_P(a,t)|^2dy.
}
\]

Thus `S_var,w` is a finite-band volume quantity even though its definition subtracts the optimal pressure mean separately on each amplitude level.

Moreover

\[
\boxed{
0\le S_{var,w}\le S_w.
}
\]

---

## 6. The averaged flux depends only on the pressure fluctuation

The M5-56 averaged pressure flux is

\[
\bar J_w
=
\int w(a)P\,U\cdot\nabla a\,dy.
\]

Using coarea and the zero level flux,

\[
\int w(a)m_P(a)
U\cdot\nabla a\,dy
=
\int w(\lambda)m_P(\lambda)
\left[
\int_{\Sigma_\lambda}U\cdot n_\lambda dS
\right]d\lambda
=0.
\]

Therefore

\[
\boxed{
\bar J_w
=
\int
w(a)(P-m_P(a))
U\cdot\nabla a\,dy.
}
\]

The entire finite-band pump is powered by pressure variation relative to the amplitude level, not by the levelwise mean pressure.

---

## 7. Combine with the angular gap

Recall from M5-66

\[
T_w
=
D_w-A_w-G_w.
\]

Cauchy with the centered pressure gives

\[
\boxed{
|\bar J_w|^2
\le
S_{var,w}
(D_w-A_w-G_w).
}
\]

Since

\[
\bar J_w
=
\nu D_w+X_w,
\]

we obtain

\[
\boxed{
(\nu D_w+X_w)^2
\le
S_{var,w}
(D_w-A_w-G_w).
}
\]

Thus on every positive upstroke,

\[
\boxed{
S_{var,w}
\ge
\nu^2(A_w+G_w)
+4\nu X_w.
}
\]

This is strictly stronger than M5-66 because

\[
S_{var,w}\le S_w.
\]

---

## 8. Geometric meaning

A large pressure magnitude that is nearly constant over each amplitude level is useless for the threshold pump.

The pump requires the pressure field to distinguish different points on the same amplitude surface and to correlate those pressure fluctuations with the signed normal velocity crossing.

Schematically,

\[
\boxed{
\text{threshold pump}
\Longrightarrow
\text{levelwise pressure oscillation}
\times
\text{signed normal crossing}.
}
\]

This is a much more rigid condition than merely requiring a large nonlocal pressure tail.

It also removes any ambiguity associated with adding a purely time-dependent pressure gauge: such a gauge is automatically subtracted by `m_P`.

---

## 9. Relation to M5-51 localization

M5-51 showed that the order-one pressure payer at the pump core is generated by the core plus finitely many adjacent logarithmic shells; remote shells decay dyadically.

M5-67 sharpens what those local shells must generate:

\[
\boxed{
\text{not merely order-one pressure, but order-one pressure variation along finite-band amplitude level sets.}
}
\]

Therefore a direct rigidity theorem can focus on whether the localized pressure-Poisson source can repeatedly sustain the required conditional pressure variance while the same normalized pump geometry returns syndetically.

---

## 10. DSD audit

### GREEN

Zero total velocity flux through a bounded amplitude superlevel boundary follows exactly from incompressibility.

### GREEN

The pressure flux is invariant under subtraction of an arbitrary levelwise constant.

### GREEN

Choosing the optimal weighted level mean produces a payer no larger than the previous absolute pressure-square payer.

### GREEN

The M5-66 angular gap and M5-65 speed penalty survive with this sharper pressure-variance payer.

### YELLOW

To convert the required levelwise pressure variance into a contradiction one still needs either an upper bound from the pressure-Poisson/Hodge geometry or a finite critical temporal budget.

---

## 11. New direct-rigidity target

A recurrent robust upstroke must now satisfy simultaneously

\[
\boxed{
S_{var,w}
\ge
\nu^2(A_w+G_w)+4\nu X_w
}
\]

with

\[
X_w\ge c_1>0
\]

on a positive-width normalized interval.

The direct branch should therefore investigate the tangential/levelwise oscillation of `P` produced by

\[
-\Delta P
=
\partial_i\partial_j(U_iU_j)
\]

inside the core plus finite-neighbor-shell region.

The relevant next object is no longer the total pressure magnitude but the pressure component orthogonal to functions of the amplitude `a=|U|`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
