# Half-Amplitude Ball Shape Bound — 2026-08-20

Overall status: **EXPLICIT POSITIVE-MIDDLE CORE SHAPE REDUCTION — GLOBAL REGULARITY NOT PROVED.**

This note removes the unknown local Lipschitz scale from the compatibility/coherence parameter

\[
\chi=\frac{R^2P_\infty}{g_-^2}
\]

on a positive-middle strain core.

---

## 1. Positive-middle spectral gap

Write the positive-middle strain spectrum as

\[
(s_1,s_2,s_3)=(-2m,m-d,m+d),
\qquad 0\le d\le m.
\]

Then

\[
g:=s_2-s_1=3m-d,
\]

and

\[
|S|^2=6m^2+2d^2.
\]

A direct calculation gives

\[
\boxed{
g\ge\frac{|S|}{\sqrt2}.}
\]

Equality occurs at the middle-zero endpoint `d=m`.

---

## 2. Build a half-amplitude ball around a strain maximum

Let

\[
B=\|S\|_{L^\infty}
\]

on the compact active profile and choose a point `x_*` where `|S(x_*)|=B`.

Let

\[
L=\|\nabla S\|_{L^\infty}.
\]

For a nonzero finite-energy profile, `L>0`. By the Lipschitz estimate,

\[
|S(x)|
\ge
B-L|x-x_*|.
\]

Hence on

\[
\boxed{
R_{1/2}=\frac{B}{2L},
}
\]

we have

\[
\boxed{|S|\ge\frac B2.}
\]

If the positive-middle branch persists throughout this ball, then

\[
\boxed{
g_-\ge\frac{B}{2\sqrt2}.}
\]

Also

\[
P_\infty
=\|\nabla S\|_{L^\infty(B_{R_{1/2}})}^2
\le L^2.
\]

---

## 3. Universal shape parameter

Insert these bounds into

\[
\chi
=\frac{R^2P_\infty}{g_-^2}.
\]

Then

\[
\chi
\le
\frac{(B/2L)^2L^2}{B^2/8}
=2.
\]

Therefore

\[
\boxed{\chi_{1/2}\le2.}
\]

The unknown derivative amplitude `L` cancels exactly.

Consequently

\[
\boxed{
C_{coh}^{ball}
\le
\frac{72}{\pi^2}
\approx7.295125222.
}
\]

---

## 4. Explicit compatibility gap on the half-amplitude ball

Let

\[
e=\mathcal E_A(R_{1/2})
\]

be the localized annular compatibility leakage from `PV_LOCALIZED_COMPATIBILITY_COVARIANCE_CAP_2026-08-20.md`.

For

\[
0\le e<\frac16,
\]

define

\[
a(e)=\frac19-\frac23e.
\]

Then the half-amplitude core satisfies

\[
\boxed{
\delta_{cov,1/2}(e)
\ge
\left[
\sqrt{
\frac{72}{\pi^2}+a(e)
}
-
\sqrt{
\frac{72}{\pi^2}
}
\right]^2.
}
\]

At zero annular error,

\[
\boxed{
\delta_{cov,1/2}(0)
\ge
0.0004198881604.
}
\]

For reference:

\[
\begin{array}{c|c}
e & \delta_{cov,1/2}(e)\\ \hline
0 & 4.1988816\times10^{-4}\\
0.01 & 3.7118089\times10^{-4}\\
0.05 & 2.0621126\times10^{-4}\\
0.10 & 6.7487338\times10^{-5}\\
0.15 & 4.2275786\times10^{-6}
\end{array}
\]

The gap vanishes continuously as `e -> 1/6`, exactly where the annulus itself enters the H/T leakage branch.

---

## 5. Local H1 tax

On the half-amplitude ball,

\[
g_-\ge\frac{B}{2\sqrt2}.
\]

Therefore the local covariance tax obeys

\[
3g_-\delta_{cov,1/2}P_R
\ge
\boxed{
\frac{3B}{2\sqrt2}
\delta_{cov,1/2}(e)P_R.
}
\]

At zero annular error the coefficient is at least

\[
\boxed{
4.1988816\times10^{-4}
\times\frac{3}{2\sqrt2}
\approx4.4536\times10^{-4}
}
\]

times `B P_R`.

This is small but explicit and universal on the half-amplitude positive-middle ball.

---

## 6. General amplitude fraction

More generally, for `0<theta<1`, use

\[
R_\theta
=\frac{(1-\theta)B}{L}.
\]

Then

\[
|S|\ge\theta B,
\qquad
g_-\ge\frac{\theta B}{\sqrt2},
\]

and

\[
\boxed{
\chi_\theta
\le
2\left(\frac{1-\theta}{\theta}\right)^2.
}
\]

Thus the compatibility gap can be optimized against the derivative-energy occupancy of the chosen amplitude ball.

A smaller ball (`theta -> 1`) improves the shape/coherence constant but may contain less of the total strain-gradient energy; a larger ball captures more geometry but weakens the coherence constant.

---

## 7. Branch if positive-middle persistence fails

The estimate above assumes the positive-middle sector persists through the chosen amplitude ball.

If it fails before `|S|` falls to `B/2`, the profile undergoes an order-one spectral-shape transition while retaining order-one strain amplitude. This exits the coherent max-mid branch and enters the middle-zero/non-normality transition branch analyzed in `PV_DOUBLE_SATURATION_SPECTRAL_TRADEOFF_2026-08-20.md`.

Thus the half-amplitude construction gives a clean branch split:

\[
\boxed{
\text{positive-middle persists}
\Rightarrow
\chi\le2\text{ and explicit compatibility tax},
}

or

\[
\boxed{
\text{positive-middle fails at high amplitude}
\Rightarrow
\text{spectral transition/non-normality branch}.
}

---

## 8. Remaining occupancy input

This note does **not** yet claim a fixed fraction of the total

\[
P=\|\nabla S\|_2^2
\]

lies in the half-amplitude ball. To promote the local compatibility tax to a whole-profile Leray tax one needs

\[
\alpha_{1/2}
:=
\frac{P_{R_{1/2}}}{P}
>0
\]

quantitatively along the recurrent class.

That derivative-energy occupancy is the next localization target. If `alpha_{1/2}` degenerates, the active H1 production must be carried outside the high-strain core, which itself creates a new core/halo separation to analyze.

Status: **ON A POSITIVE-MIDDLE HALF-AMPLITUDE STRAIN BALL, THE COHERENCE SHAPE PARAMETER IS UNIVERSALLY BOUNDED BY `CHI <= 2`, INDEPENDENT OF THE UNKNOWN STRAIN LIPSCHITZ CONSTANT. THE ONLY REMAINING INPUT NEEDED TO TURN THIS LOCAL GAP INTO A GLOBAL LERAY TAX IS THE DERIVATIVE-ENERGY OCCUPANCY OF THE HIGH-STRAIN CORE.**