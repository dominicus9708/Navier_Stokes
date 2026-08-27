# DSD M5-100 — Homogeneous Mellin Weight and Trace-Free Domination

Date: 2026-08-27

Status: **NEW AMPLITUDE-WEIGHT ROUTE / HOMOGENEOUS WEIGHTS TOUCHING AMPLITUDE ZERO REMOVE THE COMPACT-MOLLIFIER ONSET GROWTH ZONE / FOR `1<alpha<=3/2` THE BULK TRACE-FREE STRAIN TERM DOMINATES THE NORMAL CROSSING TERM / ALL WEIGHTED QUANTITIES ARE FINITE ON THE RETAINED W1 CLASS BY THE EXISTING `p>3` AND `1/r` TAIL CONTROLS / A POSITIVE UPSTROKE FOR ONE SUCH WEIGHT IS THE NEXT REQUIRED INPUT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why change the weight

M5-88 proved that a positive exact minimal-payer endpoint requires crossing inside

\[
\chi_w(a)
:=a w(a)-\frac32W_<(a)>0,
\qquad
W_<(a)=\int_0^a w(\lambda)d\lambda.
\]

Every nonzero smooth compactly supported mollifier whose support begins at a positive amplitude has such a growth zone near its lower support edge.

The present audit removes that artificial onset by using a weight that begins at amplitude zero.

---

# 2. Homogeneous Mellin family

Fix

\[
1<\alpha\le\frac32
\]

and define

\[
\boxed{
w_\alpha(\lambda)=\lambda^{\alpha-1},
\qquad \lambda>0.
}
\]

Its cumulative weight is

\[
\boxed{
W_\alpha(a)
:=\int_0^a\lambda^{\alpha-1}d\lambda
=\frac{a^\alpha}{\alpha}.
}
\]

Hence

\[
\boxed{
\chi_\alpha(a)
=a^\alpha\left(1-\frac{3}{2\alpha}\right)
\le0.
}
\]

For `alpha<3/2` the inequality is strict for every `a>0`.

Thus this family has **no positive trace-free growth zone at any amplitude**.

---

# 3. The averaged threshold entropy is exactly an Lp moment

Use the quadratic positive-part threshold entropy

\[
E_\lambda[U]
:=\frac12\int_{\mathbb R^3}(|U|-\lambda)_+^2dY.
\]

Define

\[
\mathfrak E_\alpha[U]
:=\int_0^\infty
\lambda^{\alpha-1}E_\lambda[U]d\lambda.
\]

By Tonelli/Fubini,

\[
\begin{aligned}
\mathfrak E_\alpha
&=\frac12\int dY
\int_0^{a}
\lambda^{\alpha-1}(a-\lambda)^2d\lambda\\
&=\frac{1}{\alpha(\alpha+1)(\alpha+2)}
\int a^{\alpha+2}dY.
\end{aligned}
\]

Therefore with

\[
p=\alpha+2,
\qquad 3<p\le\frac72,
\]

we have

\[
\boxed{
\mathfrak E_\alpha
=\frac{1}{\alpha(\alpha+1)(\alpha+2)}
\|U\|_{L^p}^p.
}
\]

The retained W1 orbit is globally bounded/precompact in every `L^p`, `3<p<=6`.
Hence `mathfrak E_alpha` is finite and continuous on the W1 compact class.

The lower restriction `alpha>1` is exactly the condition `p>3` that avoids the logarithmically divergent critical endpoint.

---

# 4. Extension of the M5-56 ledger to the Mellin weight

The M5-56 identities were first written for compact positive-amplitude weights.
To avoid silently changing their domain, truncate the Mellin weight:

\[
w_{\alpha,\varepsilon,R}(\lambda)
=\lambda^{\alpha-1}\chi_{\varepsilon,R}(\lambda),
\]

where `chi_{epsilon,R}` is a smooth cutoff equal to one on `[2epsilon,R]` and supported in `[epsilon,2R]`.

For every `epsilon>0`, `R<infinity`, the M5-56 ledger applies exactly.

On the retained W1 class, the fixed-core analytic bounds plus the uniform critical `1/r` tail give a uniform global velocity bound, while normalized enstrophy is finite/uniform.
Consequently

\[
\int a^\alpha|\nabla U|^2dY<\infty.
\]

Using Kato,

\[
|\nabla a|\le|\nabla U|,
\]

all crossing/angular terms below are dominated by the same integrable quantity.
The M5-51 pressure localization/tail estimate gives finiteness of the corresponding pressure payer.

Therefore the cutoff identities pass by dominated/monotone convergence as

\[
\varepsilon\downarrow0,
\qquad R\uparrow\infty.
\]

Thus the amplitude-averaged ledger extends to `w_alpha` in the integrated/distributional sense needed below.

---

# 5. Exact weighted channels

The bulk formation term is

\[
\boxed{
A_\alpha
=\int W_\alpha(a)|\nabla U|^2dY
=\frac1\alpha\int a^\alpha|\nabla U|^2dY.
}
\]

The normal crossing channel is

\[
\boxed{
T_\alpha
=\int
\frac{w_\alpha(a)}a
|U\cdot\nabla a|^2dY
=\int a^\alpha b^2dY,
}
\]

where

\[
b=U\cdot\nabla\log a
\]

on `a>0` and the nonsingular original integrand defines the value through `a=0`.

The angular channel is

\[
\boxed{
G_\alpha
=\int a^{\alpha-2}|U\times\nabla a|^2dY
\ge0.
}
\]

The apparent negative powers at `a=0` are harmless because

\[
|U\cdot\nabla a|^2
\le a^2|\nabla a|^2,
\]

and

\[
|U\times\nabla a|^2
\le a^2|\nabla a|^2.
\]

Hence both integrands are bounded by

\[
a^\alpha|\nabla a|^2.
\]

As before,

\[
D_\alpha=A_\alpha+T_\alpha+G_\alpha.
\]

---

# 6. Three-dimensional trace-free strain dominates crossing

M5-88 proved pointwise

\[
|\nabla U|^2\ge\frac32b^2.
\]

Multiply by `a^alpha/alpha` and integrate:

\[
\boxed{
A_\alpha
\ge
\frac{3}{2\alpha}T_\alpha.
}
\]

Therefore for

\[
1<\alpha\le\frac32,
\]

\[
\boxed{
A_\alpha\ge T_\alpha.
}
\]

For `1<alpha<3/2`,

\[
\boxed{
A_\alpha-T_\alpha
\ge
\left(\frac{3}{2\alpha}-1\right)T_\alpha>0
}
\]

whenever `T_alpha>0`.

This is the precise realization of the M5-88 weight-design criterion.

---

# 7. Consequence for a positive exact endpoint — conditional only on Xalpha>0

The M5-69--71 algebra depends only on finiteness of the weighted channels and therefore extends from truncated weights to the Mellin limit.

At exact minimal-payer saturation the balance condition is

\[
\boxed{
X_\alpha
=\nu(T_\alpha-A_\alpha-G_\alpha).
}
\]

But the trace-free estimate gives

\[
T_\alpha-A_\alpha-G_\alpha\le -G_\alpha\le0.
\]

Hence

\[
\boxed{
X_\alpha\le0
}
\]

at every exact endpoint for this weight family.

Therefore:

\[
\boxed{
X_\alpha>0
\quad\Longrightarrow\quad
\text{exact minimal-payer saturation is impossible.}
}
\]

No R1/R2 surface topology is used.

---

# 8. DSD four-chain audit

## Formation

The Mellin observable is formed from the entire positive-amplitude hierarchy, including arbitrarily small amplitudes, but remains finite because `alpha>1` places it in the already proved W1 `L^p`, `p>3`, class.

**GREEN.**

## Axis

The same normal/tangential decomposition `T+G` is retained. No new physical channel is introduced.

**GREEN.**

## Static aggregation

The trace-free matrix inequality compares the bulk strain channel and the crossing channel with the exact coefficient `3/(2alpha)`.
For `alpha<=3/2`, crossing cannot exceed bulk formation even before adding `G`.

**GREEN.**

## Dynamics

No recurrence has yet been used to assert `X_alpha>0`.
The present memo only states the conditional exclusion if a positive Mellin-weight upstroke exists.

**GREEN / next input open.**

---

# 9. Circularity firewall

The following reverse inference is forbidden:

\[
\text{narrow-band pump is positive}
\not\Rightarrow
X_\alpha>0
\]

for a Mellin weight.

The Mellin weight must obtain its own positive upstroke from an independent forward argument.
This prevents the new route from silently importing the narrow-mollifier conclusion that it is meant to replace.

---

# 10. Next calculation

Use the already prior W1 recurrence and the exact inverse-Leray scaling between a complete recurrent W1 profile and its standard Navier--Stokes ancient cell.

For `p=alpha+2>3`, the standard-cell `L^p` moment carries an explicit scale factor. A sufficiently accurate positive-time return of the W1 profile should therefore generate a strict increase of the standard-cell Mellin observable even if the normalized `L^p` norm itself is nearly recurrent.

This will be audited without using any pressure-payer or endpoint conclusion.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
