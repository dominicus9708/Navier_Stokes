# DSD W1 Intermediate-Scale Amplitude--Vorticity--Direction Co-localization

Date: 2026-08-26

Status: **AMPLITUDE BMO/D3 WITNESS SHOWN TO FORCE DIRECTION-DIVERGENCE, WEIGHTED-VORTICITY, OR DIRECTION-CURL COST ON THE SAME INTERMEDIATE SCALE / COMPLETE SPATIAL SEGREGATION OF AMPLITUDE AND VORTICITY-DIRECTION ACTIVITY REMOVED / GLOBAL REGULARITY UNPROVED.**

## 1. Input

The current W1 endpoint provides a recurrent intermediate-scale ball `B` satisfying

\[
D_{3,amp}(B)
:=
2\int_B a|\nabla a|^2dY
\ge d_*>0,
\qquad a:=|U|,
\]

with the ball radius bounded above and below by fixed normalized constants.

Write

\[
U=a n,
\qquad |n|=1
\]

on the nonzero-velocity set.

The purpose of this note is to determine whether this amplitude-gradient cost can remain spatially disjoint from vorticity/direction geometry.

---

## 2. Longitudinal/transverse amplitude split

Decompose

\[
\nabla a
=
(n\cdot\nabla a)n+\nabla_\perp a.
\]

Incompressibility gives

\[
0=\nabla\cdot(an)
=n\cdot\nabla a+a\nabla\cdot n,
\]

hence

\[
\boxed{
n\cdot\nabla a=-a\nabla\cdot n.
}
\]

Therefore

\[
\boxed{
\int_B a|n\cdot\nabla a|^2
=
\int_B a^3(\nabla\cdot n)^2.
}
\]

---

## 3. Transverse amplitude is tied to vorticity or direction curl

The kinematic identity

\[
\Omega=\nabla\times(an)
=\nabla a\times n+a\nabla\times n
\]

reduces to

\[
\nabla_\perp a\times n
=\Omega-a\nabla\times n.
\]

Since cross product with the unit vector `n` preserves the norm of a vector perpendicular to `n`,

\[
|\nabla_\perp a|
\le
|\Omega|+a|\nabla\times n|.
\]

Thus

\[
\boxed{
\int_B a|\nabla_\perp a|^2
\le
2\int_B a|\Omega|^2
+2\int_B a^3|\nabla\times n|^2.
}
\]

---

## 4. Same-scale trichotomy

Let

\[
A_{\parallel}:=
\int_B a|n\cdot\nabla a|^2,
\qquad
A_{\perp}:=
\int_B a|\nabla_\perp a|^2.
\]

Then

\[
D_{3,amp}(B)=2A_{\parallel}+2A_{\perp}\ge d_*.
\]

Hence either

\[
A_{\parallel}\ge \frac{d_*}{4}
\]

or

\[
A_{\perp}\ge \frac{d_*}{4}.
\]

In the first case,

\[
\boxed{
\int_B a^3(\nabla\cdot n)^2
\ge
\frac{d_*}{4}.
}
\]

In the second case, the transverse estimate gives

\[
\int_B a|\Omega|^2
+
\int_B a^3|\nabla\times n|^2
\ge
\frac{d_*}{8},
\]

and therefore at least one of

\[
\boxed{
\int_B a|\Omega|^2
\ge
\frac{d_*}{16}
}
\]

or

\[
\boxed{
\int_B a^3|\nabla\times n|^2
\ge
\frac{d_*}{16}
}
\]

holds.

Thus every recurrent amplitude-BMO/D3 witness ball satisfies

\[
\boxed{
D_{3,amp}(B)\ge d_*
\Longrightarrow
\begin{cases}
\displaystyle \int_B a^3(\nabla\cdot n)^2\ge d_*/4,\\[2mm]
\text{or }\displaystyle \int_B a|\Omega|^2\ge d_*/16,\\[2mm]
\text{or }\displaystyle \int_B a^3|\nabla\times n|^2\ge d_*/16.
\end{cases}
}
\]

---

## 5. Relation to the directional part of `D3`

The exact polar decomposition of the first `D3` term is

\[
\int a|\nabla U|^2
=
\int a|\nabla a|^2
+
\int a^3|\nabla n|^2.
\]

Both

\[
|\nabla\cdot n|^2
\]

and

\[
|\nabla\times n|^2
\]

are controlled by `|nabla n|^2` up to universal dimensional constants. Hence the first and third branches directly force a fixed directional `D3` cost on the same intermediate scale.

The second branch forces fixed weighted-vorticity mass there. Since pointwise

\[
|\Omega|^2\le 2|\nabla U|^2,
\]

it is likewise controlled by the local critical `D3` scale.

Therefore the amplitude critical activity cannot be isolated from the direction/vorticity geometry.

---

## 6. DSD interpretation

The previous proof map allowed the logical possibility

\[
\text{amplitude-active core}
\quad\text{spatially disjoint from}\quad
\text{vorticity/direction-active core}.
\]

The present identity removes that possibility at the scale of the BMO witness.

A recurrent critical amplitude contrast must carry, on the same normalized intermediate ball, at least one of:

1. longitudinal direction compression/expansion;
2. weighted vorticity;
3. direction-field curl.

Thus the correct structural object is one co-localized formation cell rather than separate amplitude and vorticity cores.

---

## 7. What this does not prove

The trichotomy is a same-scale co-localization lemma, not yet a nonrepeatability theorem.

Each branch has scale-critical size and can in principle recur without violating ordinary kinetic-energy or enstrophy budgets.

The next task is to insert the pressure--stretch relative ratio

\[
\mathcal R_{vu}=\log\frac{|\Omega|^2}{|U|^4}
\]

and determine whether recurrent formation cells can keep that ratio bounded while repeatedly paying one of the three co-localized costs.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
