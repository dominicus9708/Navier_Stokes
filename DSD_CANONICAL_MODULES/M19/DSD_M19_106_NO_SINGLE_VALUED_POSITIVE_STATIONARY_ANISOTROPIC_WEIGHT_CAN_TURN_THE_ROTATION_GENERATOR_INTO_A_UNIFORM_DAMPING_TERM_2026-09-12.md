# DSD M19-106 — No single-valued positive stationary anisotropic weight can turn the rotation generator into a uniform damping term

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / CLOSED-ROTATION-ORBIT OBSTRUCTION TO STATIC ANISOTROPIC COERCIVITY / BREAKING RADIAL SYMMETRY CHANGES THE ROTATION ENERGY TERM BUT CANNOT GIVE IT A GLOBAL DEFINITE SIGN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. General positive weight

Let

\[
w(y)>0
\]

be a smooth, single-valued stationary weight, not necessarily radial.

For the rotation generator

\[
\mathcal J_AF
=AF-(Ay)\cdot\nabla F,
\qquad A^T=-A,
\]

we have

\[
F\cdot AF=0.
\]

Therefore

\[
\begin{aligned}
\langle F,\mathcal J_AF\rangle_w
&=-\frac12\int (Ay)\cdot\nabla(|F|^2)w\,dy\\
&=\frac12\int |F|^2\nabla\cdot(Ayw)\,dy.
\end{aligned}
\]

Since

\[
\nabla\cdot(Ay)=0,
\]

this becomes

\[
\boxed{
\langle F,\mathcal J_AF\rangle_w
=\frac12\int |F|^2(Ay\cdot\nabla w)\,dy.
}
\]

Equivalently,

\[
\boxed{
\langle F,\mathcal J_AF\rangle_w
=\frac12\int |F|^2w\,(Ay\cdot\nabla\log w)\,dy.
}
\]

---

## 2. What uniform damping would require

Suppose one wanted

\[
\langle F,\mathcal J_AF\rangle_w
\le-c\|F\|_{L^2(w)}^2
\]

for every localized vector field `F`, with

\[
c>0.
\]

Localization then forces the pointwise inequality

\[
\boxed{
Ay\cdot\nabla\log w(y)
\le-2c
}
\]

throughout the region in which the estimate is claimed.

---

## 3. Closed rotation-orbit obstruction

Fix a point not on the rotation axis and follow its rotation orbit

\[
y(\varphi)=e^{\varphi A}y_0.
\]

Along the orbit,

\[
\frac d{d\varphi}\log w(y(\varphi))
=
Ay(\varphi)\cdot\nabla\log w(y(\varphi)).
\]

After one full geometric period `T_A`,

\[
y(T_A)=y(0).
\]

Because the weight is single-valued,

\[
\int_0^{T_A}
Ay(\varphi)\cdot\nabla\log w(y(\varphi))\,d\varphi
=0.
\]

But the proposed uniform damping condition would give

\[
0
\le
-2cT_A<0,
\]

which is impossible.

Hence

\[
\boxed{
\text{no smooth positive stationary single-valued weight can make }\mathcal J_A
\text{ uniformly negative.}
}
\]

The same argument excludes a uniformly positive sign.

---

## 4. Consequence

An anisotropic weight may make the rotation term locally positive in some angular sectors and negative in others, but the signed contribution has zero orbit-average at the level of the logarithmic weight derivative.

Thus

\[
\boxed{
\text{static anisotropic weighting}
\not\Rightarrow
\text{global rotation damping}.
}
\]

This is a geometric obstruction independent of the detailed Navier--Stokes nonlinear terms.

---

## 5. Time-dependent co-rotating weights

One might instead let the weight rotate with the frame.

However if

\[
w_s(y)=w_0(e^{-s\alpha A}y),
\]

the time derivative of the weight contributes exactly the transport needed to cancel the same angular motion.

Such a co-rotating choice does not create free damping; it mainly transfers the skew rotation between the operator and the metric.

Therefore it does not evade the closed-orbit obstruction automatically.

---

## 6. Updated moderate-rotation menu

M19-105--106 eliminate two simple strategies:

1. radial weighted coercivity cannot see `alpha` at all;
2. a stationary anisotropic positive weight cannot give the rotation generator a uniform sign.

Hence a genuine moderate-rotation closure must use something beyond direct one-multiplier energy coercivity, for example:

- parameter-dependent resolvent information;
- noncommuting background-coupling structure;
- rapid/slow rotation averaging;
- Floquet index/topological information;
- or a nonlinear Liouville identity not reducible to the sign of `J_A` in one weighted norm.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
