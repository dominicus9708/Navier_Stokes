# DSD W1 Velocity-Direction / Lamb Geometric Certificate

Date: 2026-08-26

Status: **POSITIVE ENDPOINT SOURCE CONVERTED TO A RECURRENT VELOCITY-DIRECTION DIVERGENCE FLOOR + SOLENOIDAL LAMB-FORCE FLOOR / LAMB VECTOR DECOMPOSED INTO TRANSVERSE AMPLITUDE GRADIENT AND STREAMLINE CURVATURE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The W1 endpoint has been reduced to one solenoidal nonlinear force

\[
L_s=\mathbb P(\Omega\times U)
\]

whose p=3 critical work remains strictly positive after invariant averaging.

This note translates that abstract Hodge/cascade statement into the geometry of the velocity amplitude and direction.

---

## 2. Amplitude and direction

Write, away from the zero set of `U`,

\[
\boxed{
a:=|U|,
\qquad
n:=\frac{U}{|U|}.
}
\]

Thus

\[
U=an,
\qquad |n|=1.
\]

Since `div U=0`,

\[
0=\nabla\cdot(an)
=n\cdot\nabla a+a\,\nabla\cdot n.
\]

Hence

\[
\boxed{
n\cdot\nabla a
=-a\,\nabla\cdot n.
}
\]

Equivalently,

\[
\boxed{
U\cdot\nabla a
=-a^2\,\nabla\cdot n.
}
\]

At zeros of `U` the identities may be understood by regularizing `a=(|U|^2+epsilon^2)^(1/2)` and then passing to the limit wherever the corresponding direction norm is finite.

---

## 3. The large-scale p=3 source is direction-divergence work

At the large-radius endpoint the Gaussian multiplier tends to one and the source is

\[
F_\infty
=-\int aU\cdot\nabla B\,dY.
\]

The W1 tail bounds make the boundary term at infinity vanish in the integration by parts below. Thus

\[
F_\infty
=
\int B\,\nabla\cdot(aU)dY.
\]

Because `div U=0`,

\[
\nabla\cdot(aU)
=U\cdot\nabla a
=-a^2\nabla\cdot n.
\]

Therefore

\[
\boxed{
F_\infty
=-\int B a^2\,\nabla\cdot n\,dY.
}
\]

This is an exact geometric representation of the endpoint projection-conversion work.

---

## 4. Positive invariant direction-deformation floor

The invariant p=3 endpoint gives

\[
\boxed{
\langle F_\infty\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6}
=:f_*>0.
}
\]

W1 contains a uniform global `L6` bound on the compact recurrent class. Pressure Calderon--Zygmund control gives

\[
\|P\|_3
\lesssim
\|U\|_6^2.
\]

Hence

\[
\|B\|_3
\lesssim
\|U\|_6^2
\]

and

\[
\boxed{
\|Ba^2\|_{3/2}
\le
\|B\|_3\|U\|_6^2
\le C_M<\infty.
}
\]

If `div n` belongs to `L3`, Holder gives

\[
|F_\infty|
\le
C_M\|\nabla\cdot n\|_3.
\]

Therefore invariant averaging yields

\[
\boxed{
\left\langle
\|\nabla\cdot n\|_{L^3}
\right\rangle_\mu
\ge
\frac{f_*}{C_M}
=:c_{dir}>0.
}
\]

If `div n` fails to belong to `L3` on a recurrent state, that is already a stronger velocity-direction singularity and the displayed finite-norm alternative is not needed.

Thus a W1 survivor cannot approach a streamline-amplitude-isometric direction field.

---

## 5. Solenoidal Lamb-force floor

The same endpoint source has the pressure-free Lamb representation

\[
F_\infty
=-\int aU\cdot L_s\,dY.
\]

On the W1 compact class, `U` is globally bounded by the Type-I tail envelope plus local compact smoothness, while `Omega in L2`. Thus `L=Omega x U` and `L_s` belong to `L2`.

Also `U in L4`, so

\[
\|aU\|_2
=\|U\|_4^2
\le C_{4,M}.
\]

Therefore

\[
|F_\infty|
\le
C_{4,M}\|L_s\|_2.
\]

Invariant averaging gives

\[
\boxed{
\left\langle
\|L_s\|_2
\right\rangle_\mu
\ge
\frac{f_*}{C_{4,M}}
=:c_L>0.
}
\]

Since the Helmholtz projector is an L2 contraction,

\[
\|L\|_2\ge\|L_s\|_2.
\]

Hence the full Lamb vector also has a positive recurrent mean floor.

---

## 6. Decompose the full Lamb vector geometrically

Using

\[
\Omega
=\nabla\times(an)
=\nabla a\times n+a\,\nabla\times n,
\]

we obtain

\[
L
=(\nabla a\times n)\times(an)
+a(\nabla\times n)\times(an).
\]

For the first term,

\[
(\nabla a\times n)\times n
=n(n\cdot\nabla a)-\nabla a
=-\nabla_\perp a,
\]

where

\[
\nabla_\perp a
:=
\nabla a-n(n\cdot\nabla a).
\]

For a unit vector field,

\[
(\nabla\times n)\times n
=(n\cdot\nabla)n.
\]

Therefore

\[
\boxed{
L
=-a\nabla_\perp a
+a^2(n\cdot\nabla)n.
}
\]

Define the streamline curvature

\[
\boxed{
\kappa:=(n\cdot\nabla)n.
}
\]

Then

\[
\boxed{
L=-a\nabla_\perp a+a^2\kappa.
}
\]

---

## 7. Amplitude-deformation or curvature necessity

By the triangle inequality,

\[
\|L\|_2
\le
\|a\nabla_\perp a\|_2
+
\|a^2\kappa\|_2.
\]

Since the invariant mean of `||L||2` is bounded below,

\[
\boxed{
\left\langle
\|a\nabla_\perp a\|_2
+
\|a^2\kappa\|_2
\right\rangle_\mu
\ge c_L>0.
}
\]

Thus at least one of the following mechanisms carries positive recurrent mean action:

\[
\boxed{
\text{transverse amplitude deformation}
}
\]

or

\[
\boxed{
\text{streamline curvature}.
}
\]

Together with the direction-divergence floor, every W1 survivor must therefore carry

\[
\boxed{
\nabla\cdot n\neq0
\quad\text{in critical mean},
}
\]

and

\[
\boxed{
\nabla_\perp a\neq0
\quad\lor\quad
(n\cdot\nabla)n\neq0
\quad\text{in recurrent mean}.
}
\]

---

## 8. Relation to known velocity-direction regularity criteria

There are known sufficient regularity criteria formulated in terms of the spatial variation of the velocity direction `u/|u|`. The present result does not satisfy those sufficient hypotheses; it gives the opposite kind of information: any W1 singular survivor must sustain a definite direction-deformation defect.

Thus the DSD calculation identifies a precise geometric way in which a hypothetical singularity must escape direction-regularity mechanisms.

No external direction criterion is claimed to close W1 here.

---

## 9. DSD endpoint geometry

The solenoidal Lamb-force endpoint may now be described without pressure or separate A--E branches:

\[
\boxed{
\text{W1 critical cascade}
\Rightarrow
\begin{cases}
\text{streamwise amplitude change / direction divergence},\\
\text{transverse amplitude change or streamline curvature},\\
\text{zero net nonlinear energy work},\\
\text{positive enstrophy-weighted spectral transfer}.
\end{cases}
}
\]

This is a necessary geometric certificate for the current survivor.

---

## 10. What remains

The certificate is not yet a contradiction. Three-dimensional Navier--Stokes dynamics can in principle sustain direction deformation and curvature while redistributing energy between scales.

A closure theorem would need to show that the above recurrent geometric certificate cannot be repeated indefinitely under the finite-energy prelimit constraints, or that it forces one of the known regularity criteria after all.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
