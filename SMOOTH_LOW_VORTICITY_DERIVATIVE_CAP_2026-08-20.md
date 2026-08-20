# Smooth Low-Vorticity Derivative Cap — 2026-08-20

Status: **S-LEVEL FINITE-TIME DERIVATIVE LOCALIZATION LEMMA. GLOBAL REGULARITY NOT PROVED.**

This note removes part of the apparent freedom in the record/H1 overlap fraction. On a smooth profile with bounded second vorticity derivative, a region that stays uniformly low in vorticity amplitude cannot carry arbitrarily large first-derivative density unless it lies close to a high-vorticity set.

## 1. High-amplitude set

Fix

\[
0<\theta<1
\]

and define

\[
\boxed{
A_\theta
=\{y:|\Omega(y)|>\theta\}.
}
\]

Let

\[
K_2=\|\nabla^2\Omega\|_\infty.
\]

Assume `K2>0`; if `K2=0`, a finite-energy whole-space vorticity field with bounded amplitude is affine and hence trivial.

Set

\[
\boxed{
\ell_\theta
=2\sqrt{\frac\theta{K_2}}.
}
\]

## 2. Reverse Taylor estimate

Let `y` satisfy

\[
\operatorname{dist}(y,A_\theta)\ge\ell_\theta.
\]

Then

\[
|\Omega(y+z)|\le\theta
\]

for every `|z|<=ell_theta`.

Choose a unit spatial direction `v` such that

\[
|D_v\Omega(y)|
\ge
\frac1{\sqrt3}|\nabla\Omega(y)|.
\]

If `D_v Omega(y) != 0`, choose a unit range vector

\[
a=\frac{D_v\Omega(y)}{|D_v\Omega(y)|}
\]

and define the scalar function

\[
f(t)=a\cdot\Omega(y+tv).
\]

Then

\[
|f(t)|\le\theta
\qquad(0\le t\le\ell_\theta),
\]

\[
f'(0)=|D_v\Omega(y)|,
\]

and

\[
|f''(t)|\le K_2.
\]

Taylor's theorem gives

\[
f(\ell)-f(0)
\ge
f'(0)\ell-rac12K_2\ell^2.
\]

The left side has magnitude at most `2 theta`, hence

\[
|D_v\Omega(y)|
\le
\frac{2\theta}{\ell}
+\frac12K_2\ell.
\]

Using

\[
\ell=2\sqrt{\theta/K_2},
\]

we obtain

\[
|D_v\Omega(y)|
\le2\sqrt{\theta K_2}.
\]

Therefore

\[
\boxed{
|\nabla\Omega(y)|^2
\le12\theta K_2.
}
\]

This is a reverse amplitude-to-derivative estimate on the interior of a low-vorticity region.

## 3. Single high-vorticity core

Suppose the non-turnover lane has one high-amplitude record core in the explicit sense

\[
\boxed{
A_\theta
\subset B_{R_\theta}(y_*),
}
\]

where `y_*` is a vorticity record point.

Then every point outside the enlarged ball

\[
B_{R_\theta+\ell_\theta}(y_*)
\]

has distance at least `ell_theta` from `A_theta`, so

\[
\boxed{
|\nabla\Omega|^2
\le12\theta K_2
\quad\text{outside }B_{R_\theta+\ell_\theta}.
}
\]

If the containment of `A_theta` fails because a second separated `theta`-high component appears, that is precisely a secondary-core / turnover event rather than a failure of the estimate.

## 4. Add finite-stage derivative tightness

Let a smooth non-H stage have a parent radius `R_P` satisfying

\[
\boxed{
\int_{|y-y_*|>R_P}|\nabla\Omega|^2dy
\le
\varepsilon_H Q,
\qquad
Q=\|\nabla\Omega\|_2^2,
}
\]

with `0<=epsilon_H<1`.

Assume

\[
R_P\ge R_\theta+\ell_\theta.
\]

Inside the parent ball but outside the enlarged high-vorticity core, the low-amplitude derivative cap gives

\[
\int_{B_{R_P}\setminus B_{R_\theta+\ell_\theta}}
|\nabla\Omega|^2dy
\le
12\theta K_2|B_{R_P}|.
\]

Thus

\[
\boxed{
\int_{B_{R_\theta+\ell_\theta}}
|\nabla\Omega|^2dy
\ge
(1-\varepsilon_H)Q
-16\pi\theta K_2R_P^3.
}
\]

This is the desired record-core derivative-overlap lower bound; no independent overlap parameter `alpha` is required.

## 5. Insert the smooth record-time palinstrophy floor

On the record-payment branch, the selected smooth record time satisfies

\[
\frac NP\ge\frac b8,
\]

and hence

\[
\boxed{
Q
\ge
Q_0
=
\frac\pi{30^{5/2}}
 b^{5/2}K_2^{-1/2}.
}
\]

Therefore the enlarged record core carries at least

\[
\boxed{
Q_{rec}
\ge
\left[
(1-\varepsilon_H)
\frac\pi{30^{5/2}}
 b^{5/2}K_2^{-1/2}
-
16\pi\theta K_2R_P^3
\right]_+.
}
\]

## 6. Fast-record threshold for forced derivative overlap

The lower bound is positive whenever

\[
(1-\varepsilon_H)
\frac\pi{30^{5/2}}
 b^{5/2}K_2^{-1/2}
>
16\pi\theta K_2R_P^3.
\]

Equivalently,

\[
\boxed{
 b
>
30
\left(
\frac{16\theta}{1-\varepsilon_H}
\right)^{2/5}
K_2^{3/5}R_P^{6/5}.
}
\]

Hence sufficiently fast normalized record growth cannot keep its derivative mass separated from the single high-vorticity core on a non-H/T stage.

If this inequality fails, the record growth rate itself is quantitatively slow relative to the analytic curvature and parent radius. That is a time-duration lane rather than a spatial-overlap freedom.

## 7. Feed back into record-ball capacity

Set

\[
R_{rec}=R_\theta+\ell_\theta.
\]

Whenever `Q_rec>0`, the record-ball capacity estimate gives

\[
\boxed{
\Delta_*
\ge
\nu
\left[
\sqrt{
\frac{3Q_{rec}}
{4\pi R_{rec}^3}
}
-K_2R_{rec}
\right]_+^2.
}
\]

Thus on the smooth non-H/T single-core lane, fast enough record growth gives an explicit record-slack floor with no separately assumed spatial H1-overlap coefficient.

## 8. Updated branch structure

At the selected smooth record time, one of the following must occur:

1. **secondary high-vorticity core:** `A_theta` is not contained in the record core -> `T`;
2. **derivative non-tightness:** the parent derivative-tail condition fails -> `H_remote`;
3. **slow record growth:** `b` lies below the explicit threshold;
4. **forced derivative overlap:** `Q_rec>0`, which feeds the record-capacity inequality and forces `Delta_*`, record radius, or curvature cost.

Thus vanishing record/derivative overlap is no longer an independent fifth escape mechanism.

Status: **BOUNDED SECOND DERIVATIVE PLUS ABSENCE OF A SECOND HIGH-VORTICITY CORE FORCES A POINTWISE DERIVATIVE CAP IN THE LOW-AMPLITUDE BULK. WITH DERIVATIVE TIGHTNESS, THIS CONVERTS THE RECORD-TIME PALINSTROPHY FLOOR INTO AN EXPLICIT RECORD-CORE OVERLAP LOWER BOUND. THE FREE OVERLAP PARAMETER IS REPLACED BY THE EXISTING H/T CONDITIONS.**