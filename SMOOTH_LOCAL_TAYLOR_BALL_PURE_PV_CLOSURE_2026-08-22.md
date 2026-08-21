# Smooth Local Taylor-Ball Pure-P_V Closure — 2026-08-22

Status: **DIRECT SMOOTH LOCAL S-CLOSURE OF A RADIUS-FREE PURE POSITIVE-MIDDLE SUBCORRIDOR / GLOBAL REGULARITY NOT PROVED.**

This note removes the remaining dependence on a large global common-core radius. The proof stays on a finite smooth running first-hitting stage and uses only a moving ball centered at a current normalized vorticity maximum.

## 1. Running first-hitting stage

Use the running vorticity envelope `M(t)` and normalized variables

\[
\Omega=M^{-1}\omega,
\qquad
U=M^{-1/2}u,
\qquad
\Sigma=M^{-1}S,
\]

with normalized time `s` satisfying `ds/dt=M`. Let

\[
b=\frac{d\log M}{ds}\ge0,
\qquad
\int_I b\,ds=\log q
\]

on one geometric stage `I` with `M_j -> q M_j`.

The normalized vorticity cap is

\[
\|\Omega(s)\|_\infty\le1.
\]

Fix the Clay-data analytic derivative ceiling

\[
K_{2,+}=\frac4{\rho_0^2}
\]

for the `M0=2` restart. As before, replace the analyticity denominator by `c_*(2)=max(c(2),1)` if needed, so

\[
\rho_0^2=\frac{\nu/2}{c_*(2)^2},
\qquad
\nu K_{2,+}=8c_*(2)^2\ge8.
\]

## 2. Persistent local-amplitude branch

Define

\[
m(s)=\|\Omega(s)\|_\infty.
\]

The pure persistent local branch is

\[
\boxed{m(s)\ge\theta:=\frac12\quad\text{for every }s\in I.}
\]

If `m(s)<1/2` somewhere, the tracked normalized record core has lost at least half of its amplitude before the next record level and the stage leaves the persistent pure lane; this is typed as amplitude/shape turnover.

At each `s`, choose a current maximizing point `y_*(s)` and set

\[
\xi(s)=\frac{\Omega(y_*(s),s)}{m(s)}.
\]

At the maximum,

\[
\nabla |\Omega|^2(y_*)=0
\quad\Longrightarrow\quad
(\nabla\Omega(y_*))^T\xi=0.
\]

For

\[
g(y)=\xi\cdot\Omega(y),
\]

we therefore have

\[
g(y_*)=m\ge\theta,
\qquad
\nabla g(y_*)=0.
\]

Taylor's theorem and the stagewise Hessian bound give

\[
g(y_*+h)\ge m-\frac12K_{2,+}|h|^2.
\]

Choose the fixed Taylor-ball radius

\[
\boxed{R_\theta=\sqrt{\frac\theta{K_{2,+}}}.}
\]

Then for `|h|<=R_theta`,

\[
\boxed{
g(y_*+h)\ge\theta\left(1-\frac{|h|^2}{2R_\theta^2}\right).}
\]

## 3. Exact circulation lower bound for the ball variance

Let `B_theta(s)=B_{R_theta}(y_*(s))` and let

\[
\bar U_\theta=|B_\theta|^{-1}\int_{B_\theta}U,
\qquad
V_\theta=\int_{B_\theta}|U-\bar U_\theta|^2.
\]

Use cylindrical coordinates around the axis `xi`. Write

\[
z=R_\theta\zeta,
\qquad
\rho=R_\theta r,
\qquad
r^2+\zeta^2\le1.
\]

For every transverse disk of radius `rho` at axial position `z`, Stokes' theorem and the Taylor lower bound give the signed vorticity flux

\[
\Phi(r,\zeta)
\ge
\theta R_\theta^2\pi
\left[
 r^2\left(1-\frac{\zeta^2}{2}\right)-\frac{r^4}{4}
\right].
\]

The constant vector `bar U_theta` has zero circulation around each circle, so Cauchy-Schwarz yields

\[
\oint |U-\bar U_\theta|^2d\ell
\ge
\frac{\Phi^2}{2\pi\rho}.
\]

Integrating the nested circles over the ball gives the exact constant

\[
\boxed{
V_\theta
\ge
\frac{157\pi}{1890}\,\theta^2R_\theta^5.
}
\]

The dimensionless integral is

\[
\int_{-1}^{1}d\zeta
\int_0^{\sqrt{1-\zeta^2}}
\frac{\pi}{2r}
\left[
 r^2\left(1-\frac{\zeta^2}{2}\right)-\frac{r^4}{4}
\right]^2dr
=
\frac{157\pi}{1890}.
\]

Thus the persistent Taylor ball carries a definite local velocity-variance floor without a global common-core assumption.

## 4. Uniform local velocity-gradient ceiling on the inactive outer-strain branch

Split the strain at each point of the moving Taylor ball into

\[
\Sigma=\Sigma_{near}^{(<R_0)}+\Sigma_{out}^{(\ge R_0)},
\qquad
R_0=K_{2,+}^{-1/2}.
\]

The even, spherical-mean-zero Biot-Savart strain kernel cancels the constant and linear Taylor terms. The already-derived second-Taylor estimate therefore gives

\[
\boxed{
|\Sigma_{near}|_F
\le
A_0:=\frac{3\sqrt2}{8}
\approx0.5303300859.
}
\]

Define the **inactive outer-strain branch** by the uniform local condition

\[
\boxed{
\sup_{s\in I}
\sup_{y\in B_\theta(s)}
|\Sigma_{out}^{(\ge R_0)}(y,s)|_F
\le
\sigma_h:=0.4.
}
\]

Failure is an active parent/halo strain branch and is not counted as a pure local `P_V` stage.

On the inactive branch,

\[
|\Sigma|_F\le A_0+\sigma_h.
\]

Since the antisymmetric part of `grad U` has Frobenius square `|Omega|^2/2`,

\[
|\nabla U|_F^2
=|\Sigma|_F^2+\frac12|\Omega|^2
\le
B_1^2,
\]

where

\[
\boxed{
B_1^2
=
\left(\frac{3\sqrt2}{8}+0.4\right)^2+\frac12
\approx1.3655140687.
}
\]

The ball mean minimizes the `L2` error, hence

\[
V_\theta
\le
\int_{B_\theta}|U-U(y_*)|^2
\le
B_1^2\int_{B_\theta}|y-y_*|^2dy.
\]

Using

\[
\int_{B_R}|y|^2dy=\frac{4\pi}{5}R^5,
\]

we obtain

\[
\boxed{
V_\theta
\le
\frac{4\pi}{5}B_1^2R_\theta^5.
}
\]

Therefore

\[
\boxed{
\Lambda_\theta:=\frac{V_+}{V_-}
\le
\frac{1512}{157}\frac{B_1^2}{\theta^2}.
}
\]

For `theta=1/2`,

\[
\boxed{
\Lambda_\theta
\le
52.6027330418.
}
\]

No global enstrophy radius enters this estimate.

## 5. Moving-ball variance ceiling

For a smooth moving ball centered on the selected near-maximizing trajectory, the running-normalized velocity-variance identity is

\[
\boxed{
\frac12V_\theta'
+\nu D_\theta
=
\frac b4V_\theta
+\mathcal F_\theta,
}
\]

where

\[
D_\theta=\int_{B_\theta}|\nabla U|^2
\]

and `F_theta` contains only the actual boundary/material/pressure/center-motion flux through the moving ball. If no absolutely-continuous near-maximizer track can be maintained, or if center motion generates order-one boundary action, the stage leaves the pure local lane and is typed as turnover.

The Euclidean ball satisfies Payne-Weinberger:

\[
V_\theta
\le
\frac{4R_\theta^2}{\pi^2}D_\theta.
\]

Define the pure boundary corridor by

\[
\left|\int_I\mathcal F_\theta ds\right|
\le
\eta\nu\int_ID_\theta ds+F_0,
\qquad
\eta\le\frac12,
\]

and

\[
f:=F_0/V_-\le1,
\qquad
\delta:=|V_\theta(s_1)-V_\theta(s_0)|/V_-\le1.
\]

Integrating the variance identity gives

\[
L_I
\le
\frac{4R_\theta^2}{\pi^2(1-\eta)\nu}
\left[
\frac14(\log q)\Lambda_\theta+f+\frac12\delta
\right].
\]

For

\[
q=2,
\qquad
\theta=\frac12,
\qquad
\eta\le\frac12,
\qquad
f\le1,
\qquad
\delta\le1,
\]

and

\[
R_\theta^2/\nu
=\frac\theta{\nu K_{2,+}}
\le\frac\theta8,
\]

we obtain the fully explicit ceiling

\[
\boxed{
L_I
\le
0.5377803706.
}
\]

This bound is independent of the global common-core radius.

## 6. Anti-ribbon lower time

On the coherent positive-middle branch, avoiding the fixed-fraction transverse material replacement from the previous ribbon lemma requires a transverse-axis swap. The exact material-line angle gate is

\[
\frac{L_I}{2}
+\operatorname{TV}_I(\theta_e)
\ge
\frac\pi2.
\]

Define the **modest local eigenframe-action branch** by

\[
\boxed{
\operatorname{TV}_I(\theta_e)
\le
2L_I.
}
\]

Failure means a stage-average transverse strain-eigenframe rotation rate above `2`; by the exact eigenframe equation this is a strong projective / pressure-Hessian / viscous-derivative action branch, not a pure low-action `P_V` stage.

On the modest-action branch,

\[
\frac{L_I}{2}+2L_I\ge\frac\pi2,
\]

hence

\[
\boxed{
L_I\ge\frac\pi5
\approx0.6283185307.
}
\]

But the moving Taylor-ball variance estimate gives

\[
L_I\le0.5377803706.
\]

Therefore

\[
\boxed{
0.5377803706
<
0.6283185307,
}
\]

which is a direct finite-smooth-stage contradiction.

## 7. Radius-free S-closure theorem for the pure local lane

For `q=2`, `M0=2`, the following simultaneous conditions cannot hold on one smooth stage:

1. persistent normalized peak
   \[
   \|\Omega(s)\|_\infty\ge1/2
   \quad\forall s\in I;
   \]
2. positive-middle coherent anti-ribbon geometry;
3. outer strain inactive on the Taylor ball
   \[
   \|\Sigma_{out}\|_F\le0.4;
   \]
4. low moving-ball boundary turnover
   \[
   \eta\le1/2,\quad f\le1,\quad\delta\le1;
   \]
5. modest transverse eigenframe action
   \[
   \operatorname{TV}(\theta_e)\le2L_I;
   \]
6. no fixed-fraction transverse material replacement.

Indeed conditions 1,3,4 imply

\[
L_I\le0.5377803706,
\]

while 2,5,6 imply

\[
L_I\ge\pi/5\approx0.6283185307.
\]

Hence this entire pure local lane is

\[
\boxed{\text{S-closed}}
\]

**independently of the global common-core radius.**

## 8. Exact complement routing

A surviving positive-middle stage must therefore activate at least one of:

### A. amplitude turnover

\[
\inf_I\|\Omega(s)\|_\infty<1/2;
\]

the normalized record core loses an order-one fraction of its amplitude before the next record level.

### B. active outer strain

\[
\sup_{I,B_\theta}|\Sigma_{out}|_F>0.4;
\]

an outer/parent halo supplies order-one strain to the analytic Taylor ball.

### C. moving-ball boundary / material turnover

At least one of

\[
\eta>1/2,
\qquad
f>1,
\qquad
\delta>1
\]

holds, or the maximizing center cannot be followed without order-one center-motion flux.

### D. strong transverse eigenframe action

\[
\operatorname{TV}(\theta_e)>2L_I.
\]

The exact eigenframe equation routes this to vorticity misalignment, pressure-Hessian action, or viscous `Delta Sigma` action.

### E. transverse material replacement / non-affine turnover

The stage avoids a complete anti-ribbon swap by replacing a fixed fraction of the next thick transverse section.

### F. positive-middle coherence fails

The spectrum/eigenframe leaves the coherent positive-middle lane, returning to the spectral-transition / nonnormality branch.

Thus the former `R_C > 1.455 rho0` large-core loophole is no longer a pure-radius escape. A large global core can survive only by activating one of these explicitly typed local mechanisms.

## 9. Significance

The proof mainline has changed from

\[
\text{small/moderate common core closed}
\quad+\quad
\text{large common core open}
\]

to

\[
\boxed{
\text{pure local positive-middle }P_V\text{ lane closed at every global radius}
}
\]

with the remaining work transferred entirely to explicit complement mechanisms: amplitude turnover, active outer strain, boundary/material turnover, strong eigenframe action, transverse replacement, or spectral transition.

No ancient limit, compact recurrent class, or global common-core upper radius is used in this closure.

Status: **THE PURE COHERENT POSITIVE-MIDDLE P_V LANE IS NOW S-CLOSED LOCALLY, INDEPENDENTLY OF GLOBAL CORE RADIUS, UNDER EXPLICIT FINITE-STAGE LOW-TURNOVER/LOW-OUTER-ACTION CONDITIONS. GLOBAL REGULARITY REMAINS OPEN BECAUSE THE COMPLEMENT MECHANISMS MUST STILL BE CLOSED OR PACKED.**