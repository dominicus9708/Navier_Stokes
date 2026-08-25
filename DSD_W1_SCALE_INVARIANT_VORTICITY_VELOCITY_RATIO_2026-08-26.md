# DSD W1 Scale-Invariant Vorticity/Velocity Ratio

Date: 2026-08-26

Status: **EXACT SCALE-INVARIANT RATIO EQUATION / LERAY DAMPING CANCELS / PRESSURE-ACCELERATION AND VORTICITY-STRETCHING CORE CERTIFICATES COUPLED IN ONE CRITICAL VARIABLE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current finite-parent W1 survivor must recurrently realize two gauge-free core mechanisms:

1. pressure force acting in the velocity direction,

\[
-g_P:=n\cdot\nabla P<0,
\qquad n:=U/|U|,
\]

with fixed positive downhill magnitude on a fixed-volume core set;

2. vorticity stretching,

\[
\gamma:=\xi^TS\xi>1,
\qquad \xi:=\Omega/|\Omega|,
\]

on recurrent finite-core events.

Instead of treating overlap and non-overlap as unrelated branches, compare the two mechanisms with a variable whose Navier--Stokes scaling cancels exactly.

---

## 2. Squared velocity and vorticity equations

Let

\[
A:=|U|^2,
\qquad
W:=|\Omega|^2,
\]

and define

\[
\mathcal L
:=
\partial_s+U\cdot\nabla+\frac12Y\cdot\nabla-\nu\Delta.
\]

The Leray velocity equation gives

\[
\boxed{
\mathcal L A
=
-A-2\nu|\nabla U|^2-2U\cdot\nabla P.
}
\]

The Leray vorticity equation gives

\[
\boxed{
\mathcal L W
=
2\Omega\cdot S\Omega
-2W
-2\nu|\nabla\Omega|^2.
}
\]

On regions where `A>0` and `W>0`, write

\[
\gamma
:=
\frac{\Omega\cdot S\Omega}{W}.
\]

---

## 3. Exact cancellation of Leray scaling

For the operator `mathcal L`,

\[
\mathcal L\log f
=
\frac{\mathcal L f}{f}
+\nu|\nabla\log f|^2.
\]

Hence

\[
\mathcal L\log A
=
-1
-2\nu\frac{|\nabla U|^2}{A}
-2\frac{U\cdot\nabla P}{A}
+\nu|\nabla\log A|^2,
\]

and

\[
\mathcal L\log W
=
2\gamma-2
-2\nu\frac{|\nabla\Omega|^2}{W}
+\nu|\nabla\log W|^2.
\]

Define the scale-invariant ratio variable

\[
\boxed{
\mathcal R_{vu}
:=
\log\frac{W}{A^2}
=
\log\frac{|\Omega|^2}{|U|^4}.
}
\]

Under Navier--Stokes scaling,

\[
U\mapsto\lambda U,
\qquad
\Omega\mapsto\lambda^2\Omega,
\]

so `W/A^2` is exactly invariant.

Subtracting `2 log A` from `log W` cancels the Leray damping terms `-2` and `2(-1)` identically:

\[
\boxed{
\begin{aligned}
\mathcal L\mathcal R_{vu}
={}&
2\gamma
+4\frac{U\cdot\nabla P}{|U|^2}
\\
&
-2\nu\frac{|\nabla\Omega|^2}{|\Omega|^2}
+4\nu\frac{|\nabla U|^2}{|U|^2}
\\
&
+\nu|\nabla\log W|^2
-2\nu|\nabla\log A|^2.
\end{aligned}
}
\]

This is an exact critical-clock equation.

---

## 4. Direction/amplitude form

Write

\[
U=a n,
\qquad
\Omega=b\xi,
\qquad
|n|=|\xi|=1.
\]

Then

\[
\frac{|\nabla U|^2}{a^2}
=
|\nabla\log a|^2+|\nabla n|^2,
\]

\[
\frac{|\nabla\Omega|^2}{b^2}
=
|\nabla\log b|^2+|\nabla\xi|^2,
\]

\[
|\nabla\log A|^2=4|\nabla\log a|^2,
\qquad
|\nabla\log W|^2=4|\nabla\log b|^2.
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal L\mathcal R_{vu}
={}&
2\left(
\gamma
+2\frac{n\cdot\nabla P}{a}
\right)
\\
&+2\nu\Bigl[
|\nabla\log b|^2
-2|\nabla\log a|^2
-|\nabla\xi|^2
+2|\nabla n|^2
\Bigr].
\end{aligned}
}
\]

If

\[
g_P:=-n\cdot\nabla P>0,
\]

then the zeroth-order critical source is

\[
\boxed{
\mathcal K_0
:=
2\left(
\gamma-2\frac{g_P}{a}
\right).
}
\]

Thus vorticity stretching and pressure acceleration act in opposite directions on the scale-invariant ratio `|Omega|/|U|^2`.

---

## 5. DSD interpretation

The earlier two recurrent core certificates are no longer independent terminal descriptions.

- `gamma>1` amplifies vorticity relative to velocity amplitude.
- `g_P>0` accelerates velocity amplitude and therefore suppresses vorticity relative to `a^2`.

The exact balance threshold is

\[
\boxed{
\gamma
=2\frac{g_P}{a}.
}
\]

Hence an overlap region has only two structural possibilities for any fixed `delta>0`:

\[
\boxed{
\left|
\gamma-2g_P/a
\right|\le\delta
}
\]

(`pressure--stretch locking`), or

\[
\boxed{
\left|
\gamma-2g_P/a
\right|>\delta
}
\]

(`relative-vorticity forcing`).

In the second case, recurrence must compensate the order-one critical forcing by the derivative-geometric part

\[
2\nu\Bigl[
|\nabla\log b|^2
-2|\nabla\log a|^2
-|\nabla\xi|^2
+2|\nabla n|^2
\Bigr]
\]

and/or by transport/diffusion of `R_vu`.

In the first case, the survivor must maintain the rigid local law

\[
\boxed{
-g_P
\approx
\frac a2\gamma
}
\]

on the common active region.

---

## 6. Why this is stronger than the previous overlap/non-overlap split

The previous proof map treated

\[
\text{pressure-active blob}
\quad\text{and}\quad
\text{stretching-active blob}
\]

as two state-space events that might overlap or alternate.

The ratio equation shows that the correct DSD object is instead the **relative formation balance** between velocity amplification and vorticity amplification.

The Leray scaling terms cancel identically, so the comparison is not subject to the earlier positive-beta half-power barrier at the level of the local equation.

This is a genuine `beta=0` structural variable.

---

## 7. Regularization caveat

`R_vu` is singular at zeros of `U` or `Omega`.

For global/invariant integration one must either:

1. work on recurrent active subregions where `a>=a_*>0` and `b>=b_*>0`; or
2. use a regularized ratio such as

\[
\mathcal R_{\varepsilon}
=
\log(W+\varepsilon^2)
-2\log(A+\varepsilon),
\]

and retain the resulting lower-order regularization terms.

No global maximum-principle conclusion is claimed here without that audit.

---

## 8. Updated frontier

The core problem can now be routed as

\[
\boxed{
\text{W1 recurrent finite core}
\Longrightarrow
\begin{cases}
\text{pressure--stretch locking},\\
\text{critical relative-vorticity forcing/geometry}.
\end{cases}
}
\]

This replaces the cruder `overlap versus non-overlap` terminal split.

The next task is to determine whether the second branch forces a positive recurrent critical action in the derivative-geometric terms, and whether the locking branch is compatible with the pressure Poisson/Betchov constraints on the same finite parent core.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
