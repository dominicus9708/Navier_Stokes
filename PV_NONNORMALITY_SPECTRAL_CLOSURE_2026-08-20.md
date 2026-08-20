# Nonnormality Spectral Closure Attempt for P_V — 2026-08-20

Overall status: **DIRECT SYSTEM-II SUBBRANCH CLOSURE ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note uses the exact vorticity-gradient representation directly, rather than the older static trace-free `4/sqrt(6)` ceiling. It produces a stronger universal H1 ceiling and a substantially larger strict gap on the positive-middle sector away from the middle-zero limit.

## 1. Exact pointwise spectral form

Let

\[
G=\nabla\omega.
\]

The exact H1 production is

\[
N
=\frac12\int S:(G^TG-GG^T)dx.
\]

At one point diagonalize the symmetric strain:

\[
S=\operatorname{diag}(s_1,s_2,s_3),
\qquad s_1\le s_2\le s_3.
\]

Then

\[
S:(G^TG-GG^T)
=
\sum_{k,i}(s_i-s_k)G_{ki}^2.
\]

Therefore

\[
\boxed{
\frac12S:(G^TG-GG^T)
\le
\frac12(s_3-s_1)|G|^2.
}
\]

For a trace-free positive-middle spectrum write

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\]

with

\[
0\le x:=d/m<1.
\]

Then

\[
|S|=\sqrt{2(3+x^2)}m
\]

and

\[
s_3-s_1=(3+x)m.
\]

Hence

\[
\boxed{
\frac{s_3-s_1}{\sqrt2|S|}
=
\Theta_{NN}(x)
:=
\frac{3+x}{2\sqrt{3+x^2}}.
}
\]

Thus

\[
\boxed{
\frac12S:(G^TG-GG^T)
\le
\frac1{\sqrt2}
\Theta_{NN}(x)|S||G|^2.
}
\]

The function `Theta_NN` increases from

\[
\Theta_{NN}(0)=\frac{\sqrt3}{2}
\]

to

\[
\Theta_{NN}(1)=1.
\]

Therefore maximal nonnormality production forces the strain spectrum toward the middle-zero limit, not toward max-mid.

## 2. Stronger universal H1 ceiling

Discarding the spectral factor gives

\[
N
\le
\frac1{\sqrt2}
\|S\|_\infty
\|\nabla\omega\|_2^2.
\]

Using the exact whole-space identity

\[
\|\nabla\omega\|_2^2
=2\|\nabla S\|_2^2
=2P,
\]

we obtain

\[
\boxed{
N\le\sqrt2\,\|S\|_\infty P.
}
\]

Thus

\[
\boxed{
q:=N/P
\le\sqrt2\,\|S\|_\infty.
}
\]

This universal ceiling is already stronger than the older static coefficient

\[
\frac4{\sqrt6}\approx1.63299,
\]

because

\[
\sqrt2\approx1.41421.
\]

The relative improvement is exactly

\[
\frac{\sqrt2}{4/\sqrt6}
=\frac{\sqrt3}{2}
\approx0.8660254.
\]

## 3. High-strain selection in vorticity-gradient measure

Let

\[
B_*=
\left(\frac{24}{\pi}EL^3\right)^{1/5}
\]

be the direct `L2 + Lipschitz` strain-amplitude ceiling, and define

\[
\boxed{
\beta=\frac{q}{\sqrt2 B_*}.
}
\]

Let

\[
Q=\|\nabla\omega\|_2^2=2P.
\]

The universal nonnormality bound implies

\[
\frac1Q\int |S||\nabla\omega|^2dx
\ge
\frac q{\sqrt2}
=\beta B_*.
\]

Choose

\[
\sigma=h\frac q{\sqrt2}=h\beta B_*
\]

with `0<h<1`, and define the high-strain set

\[
E_\sigma=\{|S|\ge\sigma\}.
\]

Exactly as in the previous covering argument, its `|grad omega|^2` occupancy satisfies

\[
\boxed{
\mu_\sigma^{(\omega)}
\ge
\frac{\beta(1-h)}{1-h\beta}.
}
\]

Choose covering radius

\[
r=a\frac\sigma L,
\qquad 0<a<1.
\]

The same `L2` packing count gives

\[
N_{ball}
\le
\frac1{4a^3(1-a/2)^2h^5\beta^5}.
\]

Hence one selected ball carries vorticity-gradient fraction

\[
\boxed{
\alpha(a,h,\beta)
\ge
4a^3(1-a/2)^2h^5\beta^6
\frac{1-h}{1-h\beta}.
}
\]

## 4. Spectral-loss branch

Fix a spectral threshold

\[
0<x_0<1.
\]

Suppose the selected high-strain ball remains in the positive-middle sector and satisfies

\[
\boxed{x=d/m\le x_0}
\]

throughout its derivative-active part.

Since

\[
|S|\ge(1-a)\sigma
\]

on the covering ball, the nonnormality spectral loss relative to the universal ceiling is at least

\[
\Delta_{NN}(x_0)
:=1-\Theta_{NN}(x_0)>0.
\]

The lost production is therefore

\[
\begin{aligned}
T_{NN}
&\ge
\frac1{\sqrt2}
\Delta_{NN}(x_0)
(1-a)\sigma
\int_{B_r}|\nabla\omega|^2dx\\
&\ge
\boxed{
\Gamma_{NN}(a,h,\beta,x_0)\,qP,
}
\end{aligned}
\]

with

\[
\boxed{
\Gamma_{NN}
=(1-a)h\,\Delta_{NN}(x_0)\,\alpha(a,h,\beta).
}
\]

## 5. Direct self-consistency inequality

Before the spectral tax,

\[
N\le\sqrt2 B_*P.
\]

On the `x <= x0` subbranch,

\[
N\le\sqrt2B_*P-T_{NN}.
\]

Thus

\[
q(1+\Gamma_{NN})\le\sqrt2B_*.
\]

Equivalently,

\[
\boxed{
\beta
\left[1+\Gamma_{NN}(a,h,\beta,x_0)\right]
\le1.
}
\]

This is a direct nonlinear closure inequality for the non-middle-zero spectral branch.

## 6. Natural double-saturation threshold

The earlier static/non-normality trade-off curves meet at

\[
\boxed{
x_*
=\frac{3(\sqrt3-1)}4
\approx0.5490381057.}
\]

At this value

\[
\Theta_{NN}(x_*)
=
\frac{15+6\sqrt3}{26}
\approx0.9766271094,
\]

so

\[
\boxed{
\Delta_{NN}(x_*)
\approx0.02337289056.
}
\]

Thus the spectrum `x <= x_*` carries at least a `2.337%` pointwise nonnormality coefficient loss before localization occupancy is included.

## 7. Explicit optimized fixed choice

Take the simple fixed parameters

\[
\boxed{
a=\frac23,
\qquad
h=0.979,
\qquad
x_0=x_*.}
\]

Solving

\[
\beta
[1+\Gamma_{NN}(2/3,0.979,\beta,x_*)]
=1
\]

gives

\[
\boxed{
\beta_{NN,*}
\approx0.9969095157.
}
\]

Therefore this subbranch satisfies

\[
\boxed{
q
\le
0.9969095157\,\sqrt2 B_*.
}
\]

This is a much larger strict gap than the compatibility-only positive-middle ceiling.

## 8. New spectral split of System II

The recurrent `P_V` branch now divides into

\[
\boxed{
\text{P_V-A: }x\le x_*
}
\]

and

\[
\boxed{
\text{P_V-B: }x>x_*.
}
\]

### P_V-A

The explicit nonnormality spectral self-consistency ceiling above applies.

### P_V-B

The strain spectrum is forced toward the middle-zero/shear side. This branch no longer resembles the old max-mid H1 saturation geometry. It must be analyzed using

- the middle-strain depletion `s_2 -> 0`;
- the Betchov/enstrophy determinant deficit;
- rank-one nonnormality geometry of `grad omega`;
- strain/vorticity differential compatibility.

This is now the principal direct-proof branch.

## 9. Recurrent closure criterion for P_V-A

If the Leray recurrence floor satisfies

\[
q_-
>
0.9969095157\sqrt2
\left(\frac{24E_+L_+^3}{\pi}\right)^{1/5},
\]

then `P_V-A` is eliminated.

The second-order Biot--Savart ceiling from `PV_BIOTSAVART_SECOND_ORDER_CLOSURE_2026-08-20.md` can replace the amplitude estimate where it is sharper.

Status: **THE EXACT NONNORMALITY REPRESENTATION LOWERS THE UNIVERSAL STATIC H1 CEILING FROM `4/sqrt(6)` TO `sqrt(2)`. AFTER HIGH-STRAIN SELECTION, THE ENTIRE POSITIVE-MIDDLE SUBBRANCH `x <= x_*` SATISFIES THE STRICT SELF-CONSISTENCY CEILING `q <= 0.9969095157 sqrt(2) B_*`. THE REMAINING DIRECT-PROOF TARGET IS THE MIDDLE-ZERO/NONNORMALITY BRANCH `x > x_*`.**