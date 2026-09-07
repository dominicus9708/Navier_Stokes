# DSD M17-336 — Conditional record transfer: finite flux mass cannot absorb R-squared zero current below any fixed positive kappa threshold

Date: 2026-09-08  
Canonical ID: **M17-336**

Status: **ACTIVE CONDITIONAL CROSS-GENERATION TRANSFER THEOREM / GENEALOGY BRIDGE EXPLICIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input and scope

M5-681 works on one **finite retained material-flux ensemble** and, after recurrent averaging, gives

\[
\partial_k\overline G=k\overline F,
\qquad
\overline F\ge0.
\]

M17-314 strengthens the bounded-length high-amplitude branch to

\[
\boxed{
-\overline G(0)\ge d>0.
}
\]

Let the total recurrent flux mass be

\[
\boxed{
M:=\int\overline F(k)dk<\infty.
}
\]

This module asks what happens **if the same material-flux ensemble and its stationary current pair are genuinely transported by an exact record blow-down**.

That cross-generation identification is an explicit hypothesis, not an already closed theorem.

## 2. Exact scaling of the kappa distribution

Under a parabolic record scaling by `R`, assume the same-label correspondence gives

\[
\kappa_R=R^2\kappa,
\qquad
h_R=D_B\kappa_R=R^4h,
\]

and the oriented material flux weight is scale invariant:

\[
d\mu_R=d\mu.
\]

Then the pushed `kappa` distribution is

\[
\begin{aligned}
\overline F_R(k)
&=
\int\delta(k-R^2\kappa_\lambda)d\mu\\
&=
R^{-2}\overline F(k/R^2).
\end{aligned}
\]

Hence

\[
\boxed{
\overline F_R(k)=R^{-2}\overline F(k/R^2).
}
\]

Its total mass is exactly invariant:

\[
\boxed{
M_R
:=
\int\overline F_R(k)dk
=M.
}
\]

## 3. Exact scaling of the material current

Similarly,

\[
\begin{aligned}
\overline G_R(k)
&=
\int R^4h_\lambda
\delta(k-R^2\kappa_\lambda)d\mu\\
&=
R^2\overline G(k/R^2).
\end{aligned}
\]

Therefore

\[
\boxed{
\overline G_R(k)=R^2\overline G(k/R^2).
}
\]

In particular,

\[
\boxed{
-\overline G_R(0)
=R^2[-\overline G(0)]
\ge R^2d.
}
\]

This is consistent with M17-326: the **per-time** current scales by `R^2`, while its spacetime zero-crossing currency becomes critical after the time Jacobian `R^{-2}` is included.

## 4. A fixed positive corridor has only finite absorption capacity

For any fixed numerical threshold `a>0`, the stationary current identity gives

\[
-\overline G_R(a)
=
-\overline G_R(0)
-
\int_0^a k\overline F_R(k)dk.
\]

Since `0<=k<=a` in this corridor,

\[
\int_0^a k\overline F_R(k)dk
\le
 a\int_0^a\overline F_R(k)dk
\le aM.
\]

Therefore

\[
\boxed{
-\overline G_R(a)
\ge
R^2d-aM.
}
\]

This is the central estimate.

## 5. Consequence at the resonant level

Take

\[
a=\frac32.
\]

Then

\[
\boxed{
-\overline G_R\!\left(\frac32\right)
\ge
R^2d-\frac32M.
}
\]

Hence whenever

\[
R^2\ge\frac{3M}{d},
\]

we obtain

\[
\boxed{
-\overline G_R\!\left(\frac32\right)
\ge
\frac12R^2d>0.
}
\]

Thus, under genuine same-ensemble record transfer, a finite flux population cannot use the fixed corridor

\[
0<\kappa<\frac32
\]

to absorb an `R^2`-amplified zero-level current for arbitrarily large record factors.

A strong downward current must pass the fixed `3/2` level in the rescaled representation.

## 6. Equivalent ancestor-corridor form

Using

\[
\overline G_R(3/2)
=R^2\overline G\!\left(\frac{3}{2R^2}\right),
\]

the same statement is

\[
-\overline G\!\left(\frac{3}{2R^2}\right)
\ge
 d-\frac{3M}{2R^2}.
\]

Thus in ancestor coordinates a fixed fraction of the zero current survives beyond the shrinking corridor

\[
0<\kappa<\frac{3}{2R^2}.
\]

This is exactly the scale-correct version of the intuitive corridor argument.

## 7. Why this does not contradict M17-330

M17-330 says `kappa=3/2` is not a record-scale-fixed level.

The present theorem does not claim that it is.

Instead it explicitly transforms the threshold:

\[
\frac32
\quad\leftrightarrow\quad
\frac{3}{2R^2}.
\]

The conclusion is that a finite flux mass cannot absorb the scaled current in that shrinking transformed corridor.

Thus M17-330 is used, not bypassed.

## 8. The exact genealogy/transfer firewall

The argument requires all of the following to refer to the **same transported ensemble**:

1. the material label set;
2. the oriented flux measure;
3. the zero-level current lower bound;
4. the recurrent/stationary `kappa` distribution;
5. the record blow-down map.

If the M17 late descendant ensemble is reselected, replaced, repartitioned, or not the exact pushforward of the ancestor ensemble, the theorem cannot be imported.

That failure is precisely the existing open bridge

\[
\boxed{
G_{parent/ancestor\to M17\ scale\text{-}map/domain/genealogy}.
}
\]

## 9. DSD-theory role

The useful DSD heuristic is to compare the capacity of a channel after the representation map is applied, rather than compare fixed numerical thresholds across incompatible representations.

The standard mathematical translation is:

- total material flux mass is invariant under the exact scaling;
- the zero-level per-time current scales like `R^2`;
- a fixed positive `kappa` corridor can absorb at most `aM`.

No DSD axiom is used as a PDE hypothesis.

## 10. Updated cross-generation frontier

Conditionally on exact same-ensemble record transfer,

\[
\boxed{
\text{fixed zero-level current}
+\text{ finite flux mass}
\Longrightarrow
\text{current survives past every fixed positive threshold for large }R.
}
\]

In particular, for large `R`, the rescaled ensemble has a definite downward current across `kappa=3/2`.

Therefore the remaining alternatives are now sharper:

\[
\boxed{
H_{large\ resonant\text{-}level\ current}
\lor
G_{ensemble/genealogy\ transfer\ failure}.
}
\]

The next target is to determine whether the first branch can be converted to a scale-critical spacetime currency or a finite PDE resource, while the second remains one of the already registered major open bridges.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
