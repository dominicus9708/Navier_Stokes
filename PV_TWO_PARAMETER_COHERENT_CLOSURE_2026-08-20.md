# Two-Parameter Coherent P_V Closure Attempt — 2026-08-20

Overall status: **ACTIVE CLOSURE ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note turns the previous positive compatibility tax into a direct self-consistency inequality for the recurrent coherent `P_V` branch. It also improves the earlier fixed half-threshold/high-strain ball selection by introducing two free geometric parameters and optimizing the resulting tax.

## 1. Setup

Let

\[
E=\|S\|_2^2,
\qquad
L=\|\nabla S\|_\infty,
\qquad
P=\|\nabla S\|_2^2,
\]

\[
B_*=\left(\frac{24}{\pi}EL^3\right)^{1/5},
\qquad
q=\frac NP,
\qquad
C_H=\frac4{\sqrt6},
\]

and

\[
\boxed{\beta=\frac{q}{C_HB_*}}.
\]

A surviving branch must have `0 < beta <= 1` before compatibility taxes are inserted.

Choose two parameters

\[
0<h<1,
\qquad
0<a<1.
\]

The high-strain threshold is

\[
\boxed{\sigma=h\frac q{C_H}=h\beta B_*.}
\]

The localization radius is

\[
\boxed{r=a\frac\sigma L.}
\]

## 2. High-strain derivative-energy occupancy

Since

\[
\frac1P\int |S||\nabla S|^2\,dx
\ge\frac q{C_H}=\beta B_*,
\]

while `|S| <= B_*`, the set

\[
E_\sigma=\{|S|\ge\sigma\}
\]

carries derivative-energy fraction at least

\[
\boxed{
\mu_\sigma
\ge
\frac{\beta(1-h)}{1-h\beta}.
}
\]

## 3. Covering with an adjustable radius

Choose a maximal disjoint family

\[
B_{r/2}(x_i),
\qquad x_i\in E_\sigma.
\]

Then `B_r(x_i)` cover `E_sigma`.

On each disjoint small ball,

\[
|S|
\ge
\sigma-Lr/2
=\sigma(1-a/2).
\]

Hence one such ball contributes at least

\[
\sigma^2(1-a/2)^2
\frac{4\pi}{3}\left(\frac r2\right)^3
=\frac{\pi}{6}
 a^3(1-a/2)^2
\frac{\sigma^5}{L^3}
\]

to `E`.

Therefore

\[
N_{ball}
\le
\frac{6EL^3}
{\pi a^3(1-a/2)^2\sigma^5}.
\]

Using

\[
EL^3=\frac\pi{24}B_*^5,
\qquad
\sigma=h\beta B_*,
\]

we obtain

\[
\boxed{
N_{ball}
\le
\frac1{4a^3(1-a/2)^2h^5\beta^5}.
}
\]

Thus one covering ball has derivative-energy fraction

\[
\boxed{
\alpha(a,h,\beta)
\ge
4a^3(1-a/2)^2h^5\beta^6
\frac{1-h}{1-h\beta}.
}
\]

This strictly generalizes the previous fixed choice `h=a=1/2`.

## 4. Compatibility geometry on the selected ball

On a covering ball,

\[
|S|\ge\sigma(1-a).
\]

If the positive-middle sector persists there, then

\[
g=s_2-s_1\ge\frac{|S|}{\sqrt2}
\ge
\boxed{
\frac{(1-a)h q}{\sqrt2 C_H}.
}
\]

Also

\[
\chi=\frac{r^2L^2}{g^2}
\le
\boxed{
2\left(\frac a{1-a}\right)^2.
}
\]

Let `e` denote the annular compatibility leakage parameter. On the non-leakage branch `0 <= e < 1/6`, the localized compatibility gap gives

\[
\boxed{
\delta(a,e)
=
\left[
\sqrt{
\frac{72}{\pi^2}
\left(\frac a{1-a}\right)^2
+\frac19-\frac23e
}
-
\sqrt{
\frac{72}{\pi^2}
\left(\frac a{1-a}\right)^2
}
\right]^2.
}
\]

## 5. Compatibility tax as a fraction of actual production

The exact covariance decomposition supplies the local tax

\[
T_{comp}\ge3g\,\delta(a,e)\,P_r.
\]

Using the gap and occupancy bounds,

\[
\boxed{
T_{comp}
\ge
\Gamma(a,h,\beta,e)\,qP,
}
\]

where

\[
\boxed{
\Gamma(a,h,\beta,e)
=
\frac{3\sqrt3}{4}(1-a)h\,
\delta(a,e)\,
\alpha(a,h,\beta).
}
\]

Equivalently,

\[
\Gamma
=
3\sqrt3\,a^3(1-a)(1-a/2)^2
h^6\beta^6
\frac{1-h}{1-h\beta}
\delta(a,e).
\]

## 6. Direct self-consistency inequality

Before the compatibility tax,

\[
N\le C_HB_*P.
\]

On the coherent compatible branch,

\[
N
\le
C_HB_*P-T_{comp}.
\]

Since `N=qP`, this yields

\[
q(1+\Gamma)\le C_HB_*.
\]

Therefore the surviving coherent branch must satisfy the direct closure inequality

\[
\boxed{
\beta\,[1+\Gamma(a,h,\beta,e)]\le1.
}
\]

This is the first explicit nonlinear self-consistency inequality obtained from the compatibility tax itself rather than from an abstract compactness gap.

## 7. Explicit fixed parameter choice

Take

\[
\boxed{a=0.235,\qquad h=0.995.}
\]

For zero annular compatibility leakage, solving

\[
\beta[1+\Gamma(0.235,0.995,\beta,0)]=1
\]

gives

\[
\boxed{
\beta_{max}(0)
\approx0.9998431096.
}
\]

Thus the coherent positive-middle branch obeys the strict ceiling

\[
\boxed{
q
\le
0.9998431096\,C_HB_*
}
\]

when `e=0`.

For representative leakage levels with the same fixed `(a,h)`:

\[
\begin{array}{c|c}
 e & \beta_{max}(e)\\
\hline
0 & 0.9998431096\\
0.01 & 0.9998602890\\
0.05 & 0.9999201860\\
0.10 & 0.9999730507\\
0.15 & 0.9999982667
\end{array}
\]

The ceiling approaches one as `e -> 1/6`, as expected because the compatibility gap is then consumed by annular leakage and the branch should instead be routed to `H/T`.

## 8. Improvement over the previous half-threshold choice

The old fixed choice `h=1/2`, `a=1/2` produced only a tax fraction of order `10^-6` near saturation.

Allowing the high-strain threshold to approach the production mean while shrinking the compatibility ball optimally increases the strict ceiling gap to approximately

\[
\boxed{
1-\beta_{max}(0)
\approx1.5689\times10^{-4}.
}
\]

This is still too small by itself to close the full recurrent problem, but it is over two orders of magnitude larger than the first unoptimized self-consistency gap.

## 9. Recurrent Leray closure criterion

At a Leray recovery/checkpoint time, recurrence requires

\[
q\ge q_-.
\]

Therefore the coherent branch is impossible whenever

\[
\boxed{
q_-
>
\beta_{max}(e_T)
C_H
\left(\frac{24E_+L_+^3}{\pi}\right)^{1/5},
}
\]

where `e_T < 1/6` is the non-turnover annular leakage ceiling.

This is now a literal theorem target with no unspecified efficiency defect. The remaining work is to sharpen or numerically instantiate `E_+`, `L_+`, and `q_-`, or to increase the compatibility tax further by using the spectral-transition and non-normality deficits simultaneously.

## 10. Parallel branch status

The selected high-strain ball still has three possibilities:

1. `e >= 1/6`: route to `H/T`;
2. positive-middle persists: obey the self-consistency ceiling above;
3. positive-middle fails at high amplitude: enter the spectral-transition/non-normality branch with the independent algebraic deficit `1-Theta_* ~= 0.0233729`.

The next System-II target is to convert the third branch's much larger algebraic deficit into a positive fraction of total `qP`, then combine it with the coherent closure inequality.

Status: **THE COHERENT POSITIVE-MIDDLE P_V BRANCH NOW SATISFIES AN EXPLICIT NONLINEAR SELF-CONSISTENCY INEQUALITY. A TWO-PARAMETER BALL SELECTION IMPROVES THE STRICT STATIC CEILING TO `beta <= 0.9998431096` AT ZERO ANNULAR LEAKAGE. GLOBAL REGULARITY REMAINS UNPROVED.**