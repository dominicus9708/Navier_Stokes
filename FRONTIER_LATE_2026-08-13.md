# Navier–Stokes proof-challenge late frontier — 2026-08-13

Status: **ACTIVE DSD-ASSISTED ADAPTIVE FIRST-HITTING / GAUSSIAN RESIDUAL / SCALE-TIME ROUTE — GLOBAL REGULARITY NOT PROVED**.

This document records the latest frontier after the earlier affine-covariance/compression-diffusion stage.  Historical notes remain valid only within their stated claim boundaries; several broad branches have now been compressed by stronger exact identities and scale audits.

DSD is used as an adaptive representation/aggregation/audit layer.  The incompressible Navier--Stokes equation is unchanged.

---

## 1. Terminal first-hitting normalization

At a terminal first-hitting vorticity level

\[
W=\|\omega(T)\|_\infty,
\qquad
r=W^{-1/2},
\]

use

\[
U(y,s)=r u(x_*+ry,T+r^2s),
\qquad
\Omega=r^2\omega.
\]

Then

\[
\boxed{\|\Omega(s)\|_\infty\le1}
\]

throughout the available normalized past and

\[
|\Omega(0,0)|=1.
\]

This is the primary amplitude cap.

---

## 2. Self-consistent Gaussian affine state

For the endpoint affine heat kernel choose

\[
a'(s)=\int\gamma_su(a+y,s)dy,
\qquad
L(s)=\int\gamma_s\nabla u(a+y,s)dy,
\]

and

\[
r=u-a'-Ly.
\]

Exactly

\[
\int\gamma r=0,
\qquad
\int\gamma\nabla r=0.
\]

The unresolved residual-gradient variance is

\[
\boxed{
\mathcal B_\gamma
=\operatorname{Var}_\gamma(S)
+\frac12\operatorname{Var}_\gamma(\Omega)
}
\]

and has the exact four-channel split

\[
\boxed{
\mathcal B_\gamma
=D_{S,\rm shape}
+D_{S,\rm amp}
+\frac12D_{\omega,\rm proj}
+\frac12D_{\omega,\rm line}.
}
\]

---

## 3. Mean-vorticity cancellation makes the nonlinear residual quadratic

Because

\[
\int\gamma\nabla r=0,
\]

the Gaussian-mean vorticity does not contribute to the averaged residual source.  With

\[
\delta\Omega=\Omega-\bar\Omega_\gamma,
\]

exactly

\[
\int\gamma f_r
=
\int\gamma(\delta\Omega\cdot\nabla)r
+
\int\gamma\delta\Omega\,
(r\cdot\nabla\log\gamma).
\]

Hence

\[
\boxed{
\left|\int\gamma f_r\right|
\lesssim
(1+\sqrt{\kappa(\Sigma)})\mathcal B_\gamma.
}
\]

This linear dependence on `B_gamma` replaces the older square-root residual-source estimate.

---

## 4. Bounded-affine Riccati barrier closes the intermediate temporal lane

Let

\[
M(s)=\|\Omega(s)\|_\infty.
\]

On a uniformly bounded self-consistent affine/Gaussian branch,

\[
\operatorname{Var}_\gamma(S)\lesssim_KM(s)^2,
\qquad
\operatorname{Var}_\gamma(\Omega)\lesssim M(s)^2.
\]

Therefore

\[
\mathcal B_\gamma(s)\lesssim_KM(s)^2.
\]

The exact affine Duhamel formula yields

\[
\boxed{
M(t)
\le
K M(t_0)
+C_K\int_{t_0}^tM(s)^2ds.
}
\]

For a terminal-normalized amplification

\[
M(t_0)=q^{-1},
\qquad
M(T)=1,
\]

Riccati comparison gives

\[
\boxed{T-t_0\gtrsim_K q.}
\]

Thus

\[
\boxed{
1\ll\sigma\ll q
}
\]

is no longer an allowed bounded-affine residual route.  If such a fast relative step occurs, the affine/Gaussian geometry or another compactness channel must leave its bounded regime.

---

## 5. Gaussian residual has an exact multiscale curvature representation

For Gaussian convolution `P_Sigma` and

\[
g=\nabla U,
\]

\[
\mathcal B_\Sigma
=P_\Sigma|g|^2-|P_\Sigma g|^2.
\]

Exactly

\[
\boxed{
\mathcal B_\Sigma
=
\int_0^1
P_{t\Sigma}
\left[
\left|
\nabla P_{(1-t)\Sigma}g\,\Sigma^{1/2}
\right|^2
\right]dt.
}
\]

Thus every residual state is a positive square function of smoothed curvature across internal subscales.

For any fixed `0<delta<1/2`, an order-one residual either

1. concentrates its square-function mass near `t=0` or `t=1`, producing an endpoint high-derivative event; or
2. produces a curvature witness at a child scale satisfying

\[
\boxed{
\sqrt\delta R
\lesssim R_{\rm child}
\lesssim\sqrt{1-\delta}R.
}
\]

Hence the residual graph has fixed-ratio scale descent rather than arbitrary scale jumps.

---

## 6. Gaussian law of total variance removes scale double counting

For nested covariances

\[
\Sigma_p=\Sigma_c+\Delta\Sigma,
\]

exactly

\[
\boxed{
\mathcal B_{\Sigma_p}[g]
=
P_{\Delta\Sigma}\mathcal B_{\Sigma_c}[g]
+
\mathcal B_{\Delta\Sigma}[P_{\Sigma_c}g].
}
\]

The first term is inherited fine-scale residual.  Only

\[
\boxed{
\Delta\mathcal B
=\mathcal B_{\Delta\Sigma}[P_{\Sigma_c}g]
}
\]

is new between-scale residual and may be charged again.

This is the Gaussian scale analogue of ANOVA/martingale orthogonality.

---

## 7. Spatial scale ceilings from finite kinetic energy and total dissipation

At normalized Gaussian parent radius `R`, the current scale audits give:

### Pressure-Hessian variation

\[
\boxed{
R\gg W^{1/12}
\Longrightarrow
\operatorname{osc}\nabla^2P_{\rm far}\to0.
}
\]

### Coherent Gaussian affine mean

\[
|L_R|
\lesssim
\|u_0\|_2W^{1/4}R^{-5/2},
\]

so

\[
\boxed{
R\gg W^{1/10}
\Longrightarrow
L_R\to0.
}
\]

### Non-affine Gaussian residual history

The linear residual-source law and total dissipation give

\[
\mathfrak R_{\gamma,R_\gamma\ge R_0}
\lesssim_K
W^{1/2}R_0^{-3}.
\]

Hence

\[
\boxed{
R_0\gg W^{1/6}
\Longrightarrow
\mathfrak R_{\gamma,R_\gamma\ge R_0}\to0.
}
\]

Thus the largest endpoint-relevant bounded-affine residual scale is `W^(1/6+epsilon)`.

---

## 8. Adaptive one-step checkpoint alignment

Choose the previous threshold

\[
W_-=W^{2/3-2\varepsilon}.
\]

Then

\[
q=\frac{W}{W_-}=W^{1/3+2\varepsilon}
\]

and the previous natural length in terminal coordinates is

\[
\boxed{
\sqrt q
=W^{1/6+\varepsilon}.
}
\]

This equals the residual-memory cutoff scale.  The previous natural normalized time is

\[
\boxed q.
\]

Combined with the Riccati barrier, bounded-affine amplification by factor `q` requires at least a comparable `O(q)` normalized time.

Thus the adaptive state has effective one-step memory: older non-affine history is negligible in the endpoint residual and is represented through the previous resolved state/coherent evolution.

---

## 9. The current unresolved spatial band

Comparing the scale thresholds produces a particularly narrow band.

For

\[
R=W^\theta,
\]

- `theta>1/10`: coherent affine mean is negligible;
- `theta>1/12`: farther pressure-Hessian variation is negligible;
- `theta>=1/6`: order-one repeated residual action costs order-one physical dissipation per first-hitting scale and the residual tail itself is suppressed beyond this ceiling.

Therefore the most purely unresolved mesoscopic regime is

\[
\boxed{
W^{1/10+\varepsilon}
\ll R
\ll
W^{1/6-\varepsilon}.
}
\]

This is the **non-affine inertial mesoscopic window**.

Inside it, coherent affine and remote-pressure explanations have been removed, while scale-critical non-affine transport can still in principle be physically summable.

---

## 10. Shell transport and the logarithmic audit

Nested local `L^3` balances cannot simply be summed: the same interior source would be counted repeatedly.

A genuine logarithmic count survives only on disjoint shell transport.  If a fixed amount of critical mass must cross every dyadic parent annulus,

\[
\boxed{
\sum_k\int|\mathcal F_{3,k}|ds
\gtrsim cK
\sim c\log R.
}
\]

The advective part is represented by the critical weighted quantity

\[
\sum_kR_k^{-1}\int_{A_k}|V|^4
\sim
\int\frac{|V|^4}{|y|}dy.
\]

No finite universal budget for this weighted flux has yet been proved.

---

## 11. Current active branches

A hypothetical singular route must now use at least one of the following.

### A. Affine/Gaussian degeneration

The self-consistent affine transition or heat covariance loses a fixed condition bound.  Return to deformation, compression-diffusion, precursor-capacity, and pressure/eigenframe channels.

### B. Long bounded-affine step

The first-hitting duration satisfies

\[
\sigma\gtrsim q.
\]

This is no longer a rapid residual jump.  The remaining problem is to convert the long critical evolution into a non-summable physical/geometric budget or ancient rigidity.

### C. Non-affine inertial cascade

Residual action persists in

\[
W^{1/10}\ll R\ll W^{1/6}.
\]

Each active residual either descends by a fixed scale ratio or creates endpoint high-derivative concentration.  New residual across parent scales is measured by nonnegative total-variance increments.

### D. Critical-mass shell transport

Backward `L^3` tightness fails, so critical mass escapes to normalized infinity and returns through shell/pressure flux.  Pressure variation is mesoscopically localized; the remaining shell transport must pay a disjoint-annulus flux ledger.

### E. Compact ancient rigidity

If all the above channels remain compact/tight, extract an ancient limit.  Existing Liouville results, including the Albritton--Barker backward-`L^3` theorem in its exact applicable class, become potential final rigidity gates.

---

## 12. Immediate proof-producing target

The narrowest current target is a packing/contraction theorem in the non-affine inertial window:

\[
\boxed{
W^{1/10}\ll R\ll W^{1/6}.
}

A successful result would show one of:

1. Gaussian between-scale residual increments have a Carleson/almost-orthogonal spacetime packing bound;
2. fixed-ratio curvature witnesses force a derivative cost that cannot be repeated across adaptive first-hitting steps;
3. disjoint shell critical flux has a strict scale-ratio surplus beyond the critical weighted bound;
4. persistent inherited residual yields an ancient compact state excluded by a Liouville/rigidity theorem.

Until such a strict margin is proved, the route remains open.

Status: **INTERMEDIATE TIME LANE CLOSED ON BOUNDED-AFFINE BRANCH / ACTIVE FRONTIER = NON-AFFINE MESOSCOPIC PACKING OR AFFINE DEGENERATION / GLOBAL REGULARITY NOT PROVED**.
