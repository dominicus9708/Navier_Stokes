# DSD M5-66 — Angular/Hodge Gap in the Mollified Pressure Payer

Date: 2026-08-27

Status: **SHARPENED WEIGHTED CAUCHY AUDIT / RETAINING THE ANGLE BETWEEN VELOCITY AND AMPLITUDE GRADIENT PRODUCES AN ADDITIONAL NONNEGATIVE FORMATION GAP `G_w` / EVERY POSITIVE ENTROPY UPSTROKE OBEYS `S_w >= nu^2(A_w+G_w)+4 nu X_w` / NEAR-MINIMAL PRESSURE PAYMENT FORCES VELOCITY TO BECOME ALMOST NORMAL TO AMPLITUDE LEVEL SETS / GLOBAL REGULARITY UNPROVED.**

## 1. Notation

Let

\[
a=|U|,
\]

and retain the amplitude-mollified quantities

\[
E=\bar E_w,
\qquad
X=\dot E,
\qquad
D=\bar D_w,
\qquad
A=\bar A_w,
\qquad
S=\bar S_w.
\]

M5-56 gives

\[
D=A+C,
\]

where

\[
\boxed{
C
=
\int a\,w(a)|\nabla a|^2dy.
}
\]

The pressure flux is

\[
\boxed{
J
=
\int w(a)P\,U\cdot\nabla a\,dy
=
\nu D+X.
}
\]

---

## 2. Do not discard the crossing angle

The first weighted Cauchy step is

\[
|J|^2
\le
S\,T,
\]

where

\[
\boxed{
T
:=
\int
w(a)
\frac{|U\cdot\nabla a|^2}{a}\,dy.
}
\]

Previously we used only

\[
|U\cdot\nabla a|
\le
|U||\nabla a|
=a|\nabla a|,
\]

hence `T<=C`.

Retain the difference exactly.

---

## 3. Angular/Hodge formation gap

Define

\[
\boxed{
G
:=
C-T.
}
\]

Since `|U|=a`, pointwise

\[
\begin{aligned}
a|\nabla a|^2
-
\frac{|U\cdot\nabla a|^2}{a}
&=
\frac1a
\left(
a^2|\nabla a|^2
-|U\cdot\nabla a|^2
\right)\\
&=
\frac{|U\times\nabla a|^2}{a}.
\end{aligned}
\]

Therefore

\[
\boxed{
G_w
=
\int
\frac{w(a)}{a}
|U\times\nabla a|^2dy
\ge0.
}
\]

Equivalently, if `theta` is the angle between `U` and `grad a`,

\[
\boxed{
G_w
=
\int
 a\,w(a)|\nabla a|^2
\sin^2\theta\,dy.
}
\]

This is the exact amount discarded by replacing the normal amplitude-crossing component with the full amplitude gradient.

---

## 4. Sharpened pressure-flux inequality

Because

\[
T=C-G
=D-A-G,
\]

we obtain

\[
\boxed{
|J|^2
\le
S(D-A-G).
}
\]

Using the exact ledger `J=nu D+X`,

\[
\boxed{
(\nu D+X)^2
\le
S(D-A-G).
}
\]

For any nontrivial pressure-driven crossing the denominator is positive.

Thus

\[
\boxed{
S
\ge
\frac{(\nu D+X)^2}{D-A-G}.
}
\]

---

## 5. Upstroke lower bound with the angular gap

On a positive upstroke `X>=0`, expand as in M5-65:

\[
S
\ge
\nu^2\frac{D^2}{D-(A+G)}
+2\nu X\frac{D}{D-(A+G)}
+\frac{X^2}{D-(A+G)}.
\]

Let

\[
B:=A+G.
\]

Then

\[
\frac{D^2}{D-B}
=D+B+\frac{B^2}{D-B}
\ge D+B.
\]

Also

\[
\frac{D}{D-B}\ge1,
\qquad
\frac1{D-B}\ge\frac1D.
\]

Hence

\[
S
\ge
\nu^2(D+A+G)
+2\nu X
+\frac{X^2}{D}.
\]

Using

\[
\nu^2D+rac{X^2}{D}
\ge2\nu X,
\]

we obtain the sharpened speed penalty

\[
\boxed{
S
\ge
\nu^2(A+G)
+4\nu X.
}
\]

Thus the tangential/oblique part of the amplitude geometry is an additional pressure cost that cannot be hidden inside the surface payer.

---

## 6. Equality and near-equality geometry

If the pressure payer approaches the minimal lower envelope, then necessarily

\[
G\to0.
\]

Since

\[
G
=
\int
\frac{w(a)}{a}|U\times\nabla a|^2dy,
\]

this means on the finite amplitude band

\[
\boxed{
U\times\nabla|U|
\approx0.
}
\]

Thus velocity becomes approximately normal to the amplitude level sets wherever the weighted gradient content is significant.

At the same time M5-65 requires approximately

\[
D\approx X/\nu
\]

for the AM--GM step to saturate, and the pressure-flux Cauchy inequality itself must be nearly saturated.

Therefore a near-minimal recurrent pump is forced into a highly constrained geometry rather than merely a large-pressure regime.

---

## 7. Hodge interpretation

The decomposition

\[
\nabla a
=
\frac{U}{|U|^2}(U\cdot\nabla a)
+
\left[
\nabla a-
\frac{U}{|U|^2}(U\cdot\nabla a)
\right]
\]

splits the amplitude gradient into streamline-normal and transverse pieces relative to the velocity direction.

`T` measures the streamline crossing component.

`G` measures the transverse formation component lost by the pressure transport channel.

In DSD language, the pressure channel can pay only through the velocity-projected amplitude crossing; any transverse amplitude formation remains an additional geometric burden.

No claim is made that `G` is a new conserved invariant.

---

## 8. Incompressibility becomes relevant at the zero-gap endpoint

The formal endpoint

\[
G=0
\]

requires

\[
U\parallel\nabla a
\]

almost everywhere in the weighted amplitude band where `grad a` is nonzero.

For a divergence-free field this means that the flow crosses the amplitude level sets everywhere normally.

But for every bounded regular superlevel region,

\[
\int_{\partial\{a>\lambda\}}
U\cdot n\,dS
=0
\]

by incompressibility.

Hence an everywhere-normal nonzero crossing cannot have one uniform sign on a closed level boundary. The zero-gap endpoint must contain compensating inward/outward normal-crossing pieces, multiple boundary components, degeneracy, or another geometric mechanism.

This does not yet prove `G>=G_*>0`, but it gives a concrete topological/flux obstruction to exact Cauchy saturation.

---

## 9. Scaling audit

Under the covariant pump scaling,

\[
G_\Lambda(t)
=
\Lambda G(\Lambda^2t).
\]

Thus

\[
S\ge\nu^2(A+G)+4\nu X
\]

is scale covariant: every term has degree `+1`.

A normalized positive lower bound for `G` on the recurrent pump class would therefore persist at every scale and strengthen the critical pressure requirement without changing the endpoint exponent.

---

## 10. New rigidity gate

The direct branch is now reduced further.

Either recurrent pump states have a uniform angular gap

\[
\boxed{G_w\ge G_*>0,}
\]

which gives a strictly stronger pressure requirement on every return,

or there exists a sequence approaching

\[
\boxed{G_w\to0,}
\]

in which case compactness produces a limiting finite-band geometry with

\[
U\times\nabla|U|=0
\]

on the active weighted region.

The next audit should classify whether such a smooth divergence-free zero-angular-gap limit can coexist with a nontrivial bounded positive-amplitude pump cell and the pressure-Poisson equation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
