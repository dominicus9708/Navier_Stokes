# Smooth Adaptive Taylor-Ball Amplitude-Free Closure — 2026-08-22

Status: **SMOOTH LOCAL PURE-P_V S-CLOSURE UNIFORM IN THE WITHIN-STAGE PEAK AMPLITUDE / GLOBAL REGULARITY NOT PROVED.**

This note strengthens `SMOOTH_LOCAL_TAYLOR_BALL_PURE_PV_CLOSURE_2026-08-22.md`. The fixed-amplitude threshold `m(s)>=1/2` is unnecessary. By shrinking the Taylor ball together with the minimum normalized peak, the same finite-stage contradiction survives uniformly for every completed first-hitting stage with positive vorticity.

## 1. Minimum normalized peak on one completed smooth stage

Let

\[
m(s)=\|\Omega(s)\|_\infty,
\qquad 0<m(s)\le1
\]

on one completed smooth stage `I=[s0,s1]` with `M_j -> 2 M_j`.

Because the stage is finite and smooth, `m(s)` is continuous. If `m` vanished at an interior time, then `omega` would vanish identically at that time; for a smooth rapidly decaying incompressible whole-space solution this would force the decaying velocity field to be trivial and the later record increase could not occur. Hence

\[
\boxed{
\theta:=\min_{s\in I}m(s)>0.
}
\]

No fixed numerical lower threshold on `theta` is assumed.

## 2. Adaptive Taylor radius

Let

\[
\boxed{
\beta(\theta)=\min\{1,2\theta\}.
}
\]

Choose

\[
\boxed{
R_\theta^2
=\frac{\beta(\theta)\theta}{K_{2,+}}.
}
\]

At every time choose a current vorticity-maximizing point `y_*(s)` and direction

\[
\xi(s)=\Omega(y_*,s)/m(s).
\]

The corrected maximum condition is

\[
(\nabla\Omega(y_*))^T\xi=0.
\]

For `g=xi dot Omega`, Taylor's theorem gives

\[
g(y_*+h)
\ge
m(s)-\frac12K_{2,+}|h|^2
\ge
\theta\left(
1-\frac{\beta(\theta)}2\frac{|h|^2}{R_\theta^2}
\right).
\]

Thus on the adaptive unit ball `|h|<=R_theta`, after `h=R_theta x`, the dimensionless scalar lower profile is

\[
\boxed{
\theta\left(1-\frac\beta2|x|^2\right).
}
\]

Since `0<beta<=1`, this profile remains strictly positive on the whole ball.

## 3. Exact beta-dependent circulation variance constant

For a transverse circle at dimensionless axial coordinate `zeta` and radius `r`, Stokes' theorem gives the circulation lower bound

\[
\Phi_\beta(r,\zeta)
\ge
\theta R_\theta^2\pi
\left[
 r^2\left(1-\frac\beta2\zeta^2\right)
-\frac\beta4r^4
\right].
\]

Integrating the circlewise Cauchy-Schwarz estimate over the ball yields

\[
\boxed{
V_\theta
\ge
C_V(\beta)\,\theta^2R_\theta^5,
}
\]

where the exact coefficient is

\[
\boxed{
C_V(\beta)
=
\frac\pi{1890}
\left(13\beta^2-108\beta+252\right).
}
\]

At `beta=1` this reduces to

\[
C_V(1)=157\pi/1890.
\]

The corresponding enstrophy lower coefficient is also explicit:

\[
\boxed{
\int_{B_\theta}|\Omega|^2
\ge
\frac\pi{105}
\left(15\beta^2-84\beta+140\right)
\theta^2R_\theta^3.
}
\]

## 4. Uniform velocity-variance ratio under inactive outer strain

Keep the same inactive outer-strain condition as in the previous note:

\[
\sup_{I,B_\theta}
|\Sigma_{out}^{(\ge K_{2,+}^{-1/2})}|
\le0.4.
\]

The second-Taylor near-strain constant is

\[
A_0=3\sqrt2/8.
\]

Hence

\[
|\nabla U|^2
\le
B_1^2
:=
\left(A_0+0.4\right)^2+\frac12
\approx1.3655140687119285.
\]

As before,

\[
V_\theta
\le
\frac{4\pi}{5}B_1^2R_\theta^5.
\]

Therefore

\[
\boxed{
\Lambda_\theta(\beta)
\le
\frac{1512B_1^2}
{(13\beta^2-108\beta+252)\theta^2}.
}
\]

## 5. Adaptive moving-ball stage ceiling

Use the same low boundary/material-turnover corridor

\[
\eta\le\frac12,
\qquad
f=F_0/V_-\le1,
\qquad
\delta=|V_1-V_0|/V_-\le1.
\]

The moving-ball variance identity and Payne-Weinberger give

\[
L_I
\le
\frac{4R_\theta^2}{\pi^2(1-\eta)\nu}
\left[
\frac14(\log2)\Lambda_\theta+f+\frac12\delta
\right].
\]

Since

\[
R_\theta^2/\nu
=\frac{\beta\theta}{\nu K_{2,+}}
\le\frac{\beta\theta}{8}
\]

using `c_*(2)>=1`, we obtain the conservative explicit function

\[
\boxed{
L_I
\le
\mathcal L(\theta,\beta)
:=
\frac{\beta\theta}{\pi^2}
\left[
\frac{378(\log2)B_1^2}
{(13\beta^2-108\beta+252)\theta^2}
+\frac32
\right].
}
\]

Here `beta=beta(theta)=min(1,2theta)`.

### Case A: `1/2 <= theta <= 1`

Then `beta=1`, so

\[
\mathcal L(\theta,1)
=
\frac1{\pi^2}
\left[
\frac{378(\log2)B_1^2}{157\theta}
+\frac32\theta
\right].
\]

On `[1/2,1]` this is maximized at `theta=1/2`, giving

\[
\boxed{
\mathcal L\le0.5377803705715904.
}
\]

### Case B: `0 < theta <= 1/2`

Then `beta=2theta`. Therefore

\[
13\beta^2-108\beta+252
=52\theta^2-216\theta+252.
\]

The ceiling becomes

\[
\mathcal L(\theta,2\theta)
=
\frac1{\pi^2}
\left[
\frac{756(\log2)B_1^2}
{52\theta^2-216\theta+252}
+3\theta^2
\right].
\]

Both terms increase on `(0,1/2]`: the quadratic denominator decreases there and `theta^2` increases. Hence the maximum again occurs at `theta=1/2`.

Thus for **every** completed stage with `0<theta<=1`,

\[
\boxed{
L_I
\le
0.5377803705715904.
}
\]

The stage-length ceiling is uniform in the depth of the temporary normalized-vorticity collapse.

## 6. Combine with the anti-ribbon action gate

On the coherent positive-middle branch, if fixed-fraction transverse material replacement is excluded and the transverse strain-eigenframe action remains modest,

\[
\operatorname{TV}_I(\theta_e)\le2L_I,
\]

then the exact material-line angle inequality gives

\[
L_I/2+\operatorname{TV}(\theta_e)\ge\pi/2,
\]

hence

\[
\boxed{
L_I\ge\pi/5
\approx0.6283185307179586.
}
\]

But the adaptive Taylor-ball variance estimate gives, uniformly in `theta`,

\[
\boxed{
L_I\le0.5377803705715904.
}
\]

Therefore

\[
\boxed{
0.5377803705715904
<
0.6283185307179586,
}
\]

and the entire adaptive pure local lane is S-closed.

## 7. Consequence: amplitude collapse is not an independent escape

The previous local theorem listed

\[
\inf_I\|\Omega\|_\infty<1/2
\]

as an amplitude-turnover complement. The adaptive radius removes that complement from the **low-boundary-flux pure lane**.

Even if the normalized current maximum temporarily becomes arbitrarily small, the Taylor ball shrinks accordingly and the variance estimate retains the same uniform stage ceiling.

Hence a deep amplitude collapse can survive only if the shrinking Taylor ball itself experiences one of the typed complement mechanisms, most notably a large normalized boundary/material flux.

The remaining pure-local complement list is therefore reduced to:

1. active outer/parent strain above the `0.4` threshold;
2. large moving-ball boundary/material/pressure/center-motion flux;
3. strong transverse eigenframe action `TV(theta_e)>2L`;
4. fixed-fraction transverse material replacement/non-affine turnover;
5. loss of coherent positive-middle geometry.

## 8. Interpretation

This is a localization gain rather than a stronger global norm estimate.

As the normalized peak decreases, the proof does **not** attempt to keep observing the old analytic-scale ball. It reduces the observation radius so that

\[
\text{Taylor circulation floor}
\quad\text{and}\quad
\text{Poincare viscous rate}
\]

remain balanced.

The price is that the allowed absolute boundary flux shrinks rapidly with the ball. Therefore the only way a deep amplitude-collapse episode can evade the contradiction is to become boundary/transport active at some smaller scale, which is exactly the intended `T` routing.

Status: **AMPLITUDE TURNOVER HAS BEEN REMOVED AS A FREE PURE-P_V ESCAPE. UNDER INACTIVE OUTER STRAIN AND LOW NORMALIZED MOVING-BALL FLUX, THE SMOOTH POSITIVE-MIDDLE ANTI-RIBBON LANE IS S-CLOSED UNIFORMLY FOR EVERY WITHIN-STAGE NORMALIZED PEAK DEPTH.**