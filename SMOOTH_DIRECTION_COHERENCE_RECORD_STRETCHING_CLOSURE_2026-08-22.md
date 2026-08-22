# Smooth Direction-Coherence / Record-Stretching Closure — 2026-08-22

Status: **DIRECT SMOOTH LOCAL S-CLOSURE FOR DIRECTION-COHERENT RECORD CORES, INDEPENDENT OF THE SIGN OF THE MIDDLE STRAIN EIGENVALUE / GLOBAL REGULARITY NOT PROVED.**

This note adds the classical geometric depletion of vortex stretching to the adaptive Taylor-ball stage ceiling. It closes the coherent straight/axisymmetric negative-middle tube branch that avoids the positive-middle ribbon mechanism.

The integral representation used here goes back to Constantin's geometric formulation of vortex stretching and the Constantin-Fefferman direction-coherence program.

## 1. Stretching factor at a vorticity record point

At a current vorticity maximum, define

\[
\xi(x)=\frac{\Omega(x)}{|\Omega(x)|}
\]

and the normalized stretching factor

\[
\boxed{
\alpha(x)
:=
\xi(x)^T\Sigma(x)\xi(x).
}
\]

The vorticity-direction representation is

\[
\boxed{
\alpha(x)
=
\frac{3}{4\pi}\,\mathrm{p.v.}
\int_{\mathbb R^3}
D(\hat y,\xi(x+y),\xi(x))
\frac{|\Omega(x+y)|}{|y|^3}\,dy,
}
\]

where

\[
D(e_1,e_2,e_3)
=(e_1\cdot e_3)\det(e_1,e_2,e_3).
\]

The geometric factor obeys

\[
\boxed{
|D(\hat y,\xi(x+y),\xi(x))|
\le
|\sin\angle(\xi(x+y),\xi(x))|
\le
|\xi(x+y)-\xi(x)|.
}
\]

Thus local directional alignment weakens the singular stretching kernel.

## 2. Near/far split at the analytic derivative scale

Use

\[
R_0=K_{2,+}^{-1/2}.
\]

Split

\[
\alpha=\alpha_{near}+\alpha_{out}
\]

with `|y|<R0` and `|y|>=R0`.

Assume local directional Lipschitz coherence on the near ball:

\[
\boxed{
|\xi(x+y)-\xi(x)|
\le
\ell_\xi |y|,
\qquad |y|<R_0.
}
\]

Define the dimensionless directional variation

\[
\boxed{
\delta_\xi:=\ell_\xi R_0.
}
\]

Using `|Omega|<=1`,

\[
\begin{aligned}
|\alpha_{near}(x)|
&\le
\frac{3}{4\pi}
\int_{|y|<R_0}
\ell_\xi |y|\frac{dy}{|y|^3}\\
&=
\frac{3}{4\pi}
4\pi\ell_\xi\int_0^{R_0}dr.
\end{aligned}
\]

Hence

\[
\boxed{
|\alpha_{near}|
\le
3\delta_\xi.
}
\]

This is scale invariant.

## 3. Outer-strain contribution

The far part of the same Biot-Savart strain is bounded by the outer strain tensor:

\[
|\alpha_{out}|
\le
|\Sigma_{out}|_F.
\]

Keep the pure-local inactive-outer-strain threshold

\[
\boxed{
\sup_{I,B_\theta}|\Sigma_{out}|_F
\le h,
}
\]

with the benchmark

\[
h=0.4.
\]

Therefore at every current vorticity maximum on the inactive branch,

\[
\boxed{
\alpha
\le
3\delta_\xi+h.
}
\]

## 4. Record-growth lower time

At a current normalized vorticity maximum, the smooth maximum principle gives

\[
\boxed{
b+\nu|\nabla\Omega|^2
\le
\alpha.
}
\]

In particular,

\[
0\le b\le\alpha\le3\delta_\xi+h.
\]

On a geometric `q=2` running first-hitting stage,

\[
\int_I b\,ds=\log2.
\]

Thus the stage length satisfies

\[
\boxed{
L_I
\ge
\frac{\log2}{3\delta_\xi+h}.
}
\]

This lower bound does not use the sign of `s2` and does not require a positive-middle ribbon argument.

## 5. Adaptive Taylor-ball upper time

From `SMOOTH_ADAPTIVE_TAYLOR_BALL_AMPLITUDE_FREE_CLOSURE_2026-08-22.md`, under the same low normalized moving-ball boundary/material-flux corridor and the same inactive outer-strain amplitude `h`, the stage ceiling is uniform in the temporary normalized peak depth.

For general `h`, define

\[
B_1^2(h)
=
\left(\frac{3\sqrt2}{8}+h\right)^2+\frac12.
\]

The worst adaptive Taylor-ball ceiling occurs at `theta=1/2` and equals

\[
\boxed{
L_*(h)
=
\frac{756\log2}{157\pi^2}B_1^2(h)
+\frac{3}{4\pi^2}.
}
\]

For

\[
h=0.4,
\]

this gives

\[
\boxed{
L_I
\le
L_*(0.4)
=0.5377803705715904.
}
\]

## 6. Direction-coherence S-closure curve

Combining the lower and upper times, the pure local stage is impossible whenever

\[
\frac{\log2}{3\delta_\xi+h}
>
L_*(h).
\]

Equivalently,

\[
\boxed{
\delta_\xi
<
\delta_*(h)
:=
\frac13
\left[
\frac{\log2}{L_*(h)}-h
\right].
}
\]

When the right side is positive, this is a direct smooth S-closure criterion.

For the benchmark `h=0.4`,

\[
\boxed{
\delta_*(0.4)
\approx
0.2963012774299293.
}
\]

Thus

\[
\boxed{
\delta_\xi<0.2963012774,
\quad
|\Sigma_{out}|\le0.4
\quad\Longrightarrow\quad
\text{the low-boundary-flux record stage is S-closed}.
}
\]

The numerical margin is independent of the global common-core radius and independent of the sign of the middle strain eigenvalue.

## 7. Negative-middle axisymmetric tube consequence

The main motivation is the negative-middle spectrum

\[
s_1\le s_2<0<s_3.
\]

Near the axisymmetric-extensional limit

\[
(s_1,s_2,s_3)\approx(-m,-m,2m),
\]

the transverse cross-section can contract almost isotropically, so the positive-middle ribbon tax becomes weak or irrelevant.

However, a straight direction-coherent vortex tube has a depleted self-stretching factor. The criterion above shows quantitatively that if its vorticity direction changes by less than about `0.2963` in Lipschitz scale across `R0`, and outer strain is below `0.4`, then it cannot double the running vorticity level before the adaptive moving-ball variance budget expires.

Therefore the negative-middle coherent-tube survivor must activate at least one of:

1. order-one vorticity-direction variation on the analytic scale;
2. active outer/parent strain;
3. large moving-ball boundary/material flux;
4. loss of the smooth Taylor/analytic corridor.

The first item is precisely the geometric direction-turnover/depletion complement rather than a quiet coherent tube.

## 8. Relation to the single-core P_V reduction

The local proof tree now has two independent closures:

### Positive-middle coherent record core

Anti-ribbon geometry plus adaptive Taylor-ball variance closes the low-action pure stage.

### Direction-coherent record core of either middle-eigenvalue sign

Geometric depletion plus adaptive Taylor-ball variance closes the stage whenever

\[
\delta_\xi<\delta_*(h).
\]

Hence a negative-middle record core can remain a candidate only by becoming directionally rough at the analytic scale or by importing outer strain/transport action.

This further reduces the quiet autonomous `P_V` survivor and strengthens the routing to the System-I complement tree.

Status: **A DIRECTION-COHERENT RECORD CORE CANNOT SUSTAIN THE q=2 SMOOTH FIRST-HITTING STAGE UNDER LOW OUTER STRAIN AND LOW MOVING-BALL FLUX. THE NEGATIVE-MIDDLE AXISYMMETRIC-TUBE ESCAPE THEREFORE REQUIRES ORDER-ONE DIRECTION TURNOVER OR OUTER/BOUNDARY ACTION.**