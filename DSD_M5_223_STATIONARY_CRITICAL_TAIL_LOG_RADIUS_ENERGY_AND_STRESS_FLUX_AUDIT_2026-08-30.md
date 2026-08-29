# DSD M5-223 — Stationary Critical-Tail Log-Radius Energy and Stress-Flux Audit

Date: 2026-08-30

Parent: `DSD_M5_221_SMALL_STATIONARY_CRITICAL_TAIL_EXCLUSION_BY_LANDAU_ASYMPTOTICS_AND_MINIMALITY_2026-08-30.md`

Status: **EXACT FLUX IDENTITIES DERIVED / LARGE STATIONARY CRITICAL TAIL HAS A MONOTONE PHYSICAL ENERGY FLUX, BUT AFTER CRITICAL LOG-RADIUS RENORMALIZATION THE FLUX IS AN EXPONENTIAL MOVING AVERAGE OF A NONNEGATIVE RECURRENT DIRICHLET DENSITY / NONCONSTANT COMPACT RECURRENCE IS FULLY COMPATIBLE WITH THIS ODE / MOMENTUM-STRESS CHARGE IS EXACTLY CONSTANT BUT DOES NOT FORCE HOMOGENEITY / SIMPLE FLUX-MONOTONICITY CLOSURE IS THEREFORE RED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Stationary large-critical branch

Work with the surviving stationary tail from M5-221:

\[
\boxed{
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=0,
\qquad
\nabla\cdot T=0
}
\]

on `R^3\{0}`, with

\[
|T(x)|\lesssim |x|^{-1},
\qquad
|\nabla T(x)|\lesssim |x|^{-2},
\]

and a compact minimal dilation hull.

Write

\[
x=r\theta,
\qquad
y=\log r,
\]

and

\[
\boxed{
T(r\theta)=r^{-1}\Phi(y,\theta),
\qquad
P(r\theta)=r^{-2}\Pi(y,\theta)
}
\]

after fixing the pressure gauge compatible with the critical scaling.

The candidate is assumed nonhomogeneous:

\[
\partial_y\Phi\not\equiv0.
\]

---

## 2. Exact stationary kinetic-energy current

Let

\[
e:=\frac12|T|^2.
\]

Dot the stationary equation with `T`.

Using

\[
-T\cdot\Delta T
=-\Delta e+|\nabla T|^2,
\]

\[
T\cdot(T\cdot\nabla T)
=\nabla\cdot(eT),
\]

and

\[
T\cdot\nabla P
=\nabla\cdot(PT),
\]

one obtains

\[
\boxed{
\nabla\cdot J_E
=-\nu|\nabla T|^2,
}
\]

where

\[
\boxed{
J_E
:=-\nu\nabla e+(e+P)T.
}
\]

Thus the stationary tail has an exact dissipative energy current.

---

## 3. Physical radial energy flux is monotone

Define the outward radial flux

\[
\boxed{
F_E(r)
:=
\int_{|x|=r}J_E\cdot n\,dS.
}
\]

Integrating the divergence identity on an annulus gives

\[
\boxed{
F_E(R)-F_E(r)
=-\nu
\int_{r<|x|<R}|\nabla T|^2dx
\le0.
}
\]

Hence

\[
\boxed{F_E'(r)=-\nu\int_{|x|=r}|\nabla T|^2dS\le0}
\]

for almost every `r`.

Because `J_E=O(r^-3)`, one has

\[
F_E(r)\to0
\qquad(r\to\infty).
\]

Therefore

\[
\boxed{
F_E(r)
=
\nu\int_{|x|>r}|\nabla T|^2dx
\ge0.
}
\]

This is an exact exterior Dirichlet-energy identity.

---

## 4. Critical log-radius normalization

For the log representation,

\[
e(r\theta)
=
\frac1{2r^2}|\Phi|^2.
\]

Hence

\[
\partial_re
=
\frac1{r^3}
\left(
-|\Phi|^2+\Phi\cdot\partial_y\Phi
\right).
\]

Let

\[
\Phi_r:=\Phi\cdot\theta
\]

be the radial component.

Then

\[
J_E\cdot n
=
\frac1{r^3}
\left[
\nu
\left(
|\Phi|^2-\Phi\cdot\Phi_y
\right)
+
\left(
\frac12|\Phi|^2+\Pi
\right)
\Phi_r
\right].
\]

Therefore

\[
\boxed{
F_E(r)=r^{-1}f_E(y),
}
\]

with

\[
\boxed{
f_E(y)
:=
\int_{S^2}
\left[
\nu(|\Phi|^2-\Phi\cdot\Phi_y)
+
\left(\frac12|\Phi|^2+\Pi\right)
\Phi_r
\right]d\theta.
}
\]

---

## 5. Dirichlet density on the log cylinder

The gradient has the exact critical scaling

\[
\nabla T=r^{-2}\mathcal G[\Phi],
\]

where `mathcal G` is the full radial/angular first-derivative tensor on the cylinder.

Define

\[
\boxed{
A_D(y)
:=
\int_{S^2}|\mathcal G[\Phi](y,\theta)|^2d\theta
\ge0.
}
\]

Then

\[
\int_{|x|=r}|\nabla T|^2dS
=r^{-2}A_D(y).
\]

Since

\[
F_E'(r)
=r^{-2}(f_E'(y)-f_E(y)),
\]

the exact flux law becomes

\[
\boxed{
f_E'(y)-f_E(y)=-\nu A_D(y).
}
\]

Equivalently,

\[
\boxed{
f_E'(y)=f_E(y)-\nu A_D(y).
}
\]

This is the correct scale-renormalized energy-flux ODE.

---

## 6. Exact exponential-future-average formula

From the exterior energy identity,

\[
F_E(e^y)
=
\nu
\int_y^\infty
 e^{-z}A_D(z)dz.
\]

Multiplying by `e^y` gives

\[
\boxed{
f_E(y)
=
\nu
\int_y^\infty
 e^{-(z-y)}A_D(z)dz
}
\]

or, setting `a=z-y`,

\[
\boxed{
f_E(y)
=
\nu
\int_0^\infty e^{-a}A_D(y+a)da.
}
\]

Thus the critical energy-flux coefficient is simply a one-sided exponentially weighted moving average of the nonnegative log-radius Dirichlet density.

---

## 7. Why physical monotonicity does not kill log-radius recurrence

Suppose the stationary tail belongs to a compact recurrent dilation hull. Then `A_D(y)` may be bounded, uniformly continuous, recurrent, and nonconstant.

The formula above produces a bounded recurrent `f_E(y)` solving

\[
f_E'-f_E=-\nu A_D.
\]

There is no contradiction.

For example, if

\[
A_D(y)=a_0+a_1\cos y,
\qquad
a_0>|a_1|>0,
\]

then

\[
f_E(y)
=
\nu a_0
+
\frac{\nu a_1}{2}(\cos y+\sin y),
\]

which is bounded, positive for sufficiently small `|a1|/a0`, and periodic.

Yet the physical flux

\[
F_E(r)=r^{-1}f_E(\log r)
\]

can still be monotone decreasing because the exact ODE enforces

\[
F_E'(r)=-\nu r^{-2}A_D(\log r)\le0.
\]

Therefore

\[
\boxed{
\text{monotone physical energy flux}
\not\Rightarrow
\text{constant log-radius profile}.
}
\]

This closes the naive monotonicity shortcut.

---

## 8. Momentum/stress flux is exactly constant

Write the stationary equation in divergence form.

One convenient stress tensor is

\[
\boxed{
\mathbb S
:=
-\nu(\nabla T+\nabla T^T)
+T\otimes T
+P I.
}
\]

Since `div T=0`,

\[
\boxed{\nabla\cdot\mathbb S=0.}
\]

Hence the momentum/stress charge

\[
\boxed{
b(r):=\int_{|x|=r}\mathbb S n\,dS}
\]

is independent of `r`:

\[
\boxed{b(r)\equiv b.}
\]

Because each term of `mathbb S` scales like `r^-2`, this is also a scale-critical log-radius invariant.

It is the same constant vector that labels the Landau leading term in the small-amplitude exterior asymptotic theorem.

---

## 9. Constant stress charge still does not force homogeneity

The condition

\[
b(y)\equiv b
\]

is only a finite-dimensional integral constraint on the angular profile.

A nonhomogeneous recurrent `Phi(y,theta)` can in principle preserve the same stress charge while redistributing higher angular modes.

Likewise the zero spherical mass flux

\[
\int_{S^2}\Phi_r(y,\theta)d\theta=0
\]

removes only the degree-zero radial mass-flux mode.

Therefore

\[
\boxed{
\text{constant stress charge}
+
\text{zero mass flux}
\not\Rightarrow
\partial_y\Phi=0
}
\]

without a rigidity theorem.

---

## 10. Vorticity/enstrophy identity has no sign closure

For completeness, the stationary vorticity equation is

\[
-\nu\Delta\Omega
+(T\cdot\nabla)\Omega
-(\Omega\cdot\nabla)T=0.
\]

Pairing with `Omega` introduces the stretching term

\[
\int\Omega^TS_T\Omega,
\]

which has no fixed sign.

Thus the vorticity analogue does not restore a monotone log-radius functional on the generic large-amplitude branch.

---

## 11. DSD verdict

### PROVED

- exact stationary kinetic-energy current;
- monotone physical radial energy flux;
- exact exterior Dirichlet-energy representation;
- critical log-radius ODE
  \[
  f_E'-f_E=-\nu A_D;
  \]
- exponential moving-average formula for `f_E`;
- constant momentum/stress charge.

### FIREWALL

The following shortcut is false:

\[
\boxed{
\text{stationary dissipation}
+
\text{monotone radial flux}
\Longrightarrow
\text{homogeneous tail}.
}
\]

After critical renormalization, bounded recurrent nonconstant `A_D` is perfectly compatible with the exact flux law.

---

## 12. Updated large-stationary frontier

The surviving stationary branch is therefore not removed by first-order flux monotonicity.

It is now characterized more sharply by

\[
\boxed{
\begin{cases}
F_T=0,\\
A_* > \varepsilon_{KS},\\
\partial_y\Phi\ne0,\\
A_D(y)\ge0\text{ recurrent},\\
f_E=\nu e^{-\cdot}*_{+}A_D,\\
b\text{ constant},\\
\text{compact minimal translation hull.}
\end{cases}}
\]

The next useful stationary test must therefore use more than scalar energy flux: e.g. a scale-Mellin/Pohozaev identity sensitive to `partial_y Phi`, a large-data exterior rigidity theorem, or a higher tensor/angular-mode balance.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]