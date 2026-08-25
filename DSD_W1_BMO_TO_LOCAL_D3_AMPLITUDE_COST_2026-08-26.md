# DSD W1 BMO-to-Local-D3 Amplitude Cost

Date: 2026-08-26

Status: **THE RECURRENT INTERMEDIATE-SCALE BMO AMPLITUDE WITNESS FORCES A FIXED LOCAL AMPLITUDE COMPONENT OF `D3` ON THE SAME SCALE / CRITICAL WORK AND CRITICAL DISSIPATION CO-LOCALIZED IN THE AMPLITUDE CHANNEL / GLOBAL REGULARITY UNPROVED.**

## 1. Input

From the Hodge-commutator/BMO note, every recurrent critical-work event contains a ball

\[
B=B_r(Y_0),
\qquad
r_-\le r\le r_+,
\]

such that

\[
\boxed{
\fint_B
|a-a_B|\,dY
\ge c_{osc}>0,
\qquad
a:=|U|.
}
\]

The radii `r_-` and `r_+` are fixed on the compact W1 class.

---

## 2. Exact amplitude/direction decomposition of `D3`

Write

\[
U=a n,
\qquad |n|=1.
\]

Then

\[
|\nabla U|^2
=|\nabla a|^2+a^2|\nabla n|^2,
\]

and

\[
U\cdot\partial_jU
=a\,\partial_ja.
\]

Hence the endpoint dissipation density is

\[
\begin{aligned}
D_3
&=
\int a|\nabla U|^2
+\int a^{-1}\sum_j(U\cdot\partial_jU)^2
\\
&=
\boxed{
2\int a|\nabla a|^2
+\int a^3|\nabla n|^2.
}
\end{aligned}
\]

Set

\[
w:=a^{3/2}.
\]

Then

\[
|\nabla w|^2
=\frac94a|\nabla a|^2,
\]

so

\[
\boxed{
D_3
=
\frac89\int|\nabla w|^2
+\int a^3|\nabla n|^2.
}
\]

The first term is the amplitude component `D_{3,amp}` and the second is the direction component `D_{3,dir}`.

---

## 3. Pairwise oscillation passes from `a` to `a^(3/2)`

For all `x,y>=0`, convexity/superadditivity gives

\[
\boxed{
|x^{3/2}-y^{3/2}|
\ge |x-y|^{3/2}.
}
\]

Let `X,Y` be independent uniform points in `B`. Jensen gives

\[
\mathbb E|a(X)-a(Y)|
\ge
\mathbb E|a(X)-a_B|
\ge c_{osc}.
\]

Therefore

\[
\mathbb E|a(X)-a(Y)|^3
\ge c_{osc}^3.
\]

Using the preceding pointwise inequality,

\[
\mathbb E|w(X)-w(Y)|^2
\ge c_{osc}^3.
\]

The pairwise-variance identity gives

\[
\frac1{|B|}
\int_B|w-w_B|^2dY
=
\frac12
\mathbb E|w(X)-w(Y)|^2.
\]

Hence

\[
\boxed{
\int_B|w-w_B|^2dY
\ge
\frac12|B|c_{osc}^3.
}
\]

---

## 4. Poincare gives a fixed local critical dissipation floor

Poincare on `B_r` gives

\[
\int_B|w-w_B|^2
\le
C_Pr^2\int_B|\nabla w|^2.
\]

Thus

\[
\int_B|\nabla w|^2
\ge
\frac{|B|}{2C_Pr^2}c_{osc}^3.
\]

Since `|B|=c_3r^3` and `r>=r_->0`,

\[
\boxed{
\int_B|\nabla w|^2
\ge
c_w r_- c_{osc}^3
=:d_w>0.
}
\]

Consequently

\[
\boxed{
D_{3,amp}(B)
:=
2\int_B a|\nabla a|^2
=
\frac89\int_B|\nabla w|^2
\ge
 d_*>0.
}
\]

This floor is uniform on the recurrent W1 critical-work events.

---

## 5. DSD consequence

The positive `p=3` Hodge/pressure work cannot be realized by a nearly constant-amplitude core with all dissipation occurring elsewhere.

Instead

\[
\boxed{
F_3\text{ critical event}
\Longrightarrow
\text{fixed intermediate-scale amplitude oscillation}
\Longrightarrow
D_{3,amp}(B)\ge d_*.
}
\]

Thus the critical source and a definite part of the critical dissipation are co-localized at one normalized scale bounded away from both zero and infinity.

This removes another possible segregation loophole.

---

## 6. Relation to the scale-invariant vorticity/velocity ratio

The same ball contains a fixed amplitude-gradient cost. The ratio equation

\[
\mathcal R_{vu}
=
\log\frac{|\Omega|^2}{|U|^4}
\]

shows that pressure acceleration and vorticity stretching can avoid changing this relative formation variable only through pressure--stretch locking plus derivative-geometric compensation.

The BMO-to-`D3` result means that the amplitude derivative part of that compensation cannot vanish on the critical-work events.

A remaining rigidity question is whether pressure--stretch locking can coexist with this fixed amplitude-gradient cost without forcing either:

1. a fixed vorticity-gradient/palinstrophy cost on the same ball; or
2. a fixed direction-field cost `int a^3|grad n|^2`.

No contradiction is asserted here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
