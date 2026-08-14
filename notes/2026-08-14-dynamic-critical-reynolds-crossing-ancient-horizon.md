# Dynamic critical-Reynolds crossing and automatic ancient horizon

Date: 2026-08-14

Status: **DERIVED ON THE BOUNDED-CONDITION TERMINAL GAUSSIAN HISTORY. EVERY SURVIVING LARGE-REYNOLDS RESIDUAL PULSE PASSES THROUGH A CANONICAL SCALE-TIME POINT WITH `B R^4 = 1`, AND THE ADAPTIVE PRECURSOR GIVES AN ANCIENT HORIZON AFTER RESCALING AT THAT CROSSING. THE REMAINING OBSTRUCTION IS THE AFFINE/ROTATION BACKGROUND IN THE LIMIT EQUATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Terminal Gaussian history

Use backward normalized time

\[
\tau=-s\ge0
\]

and the matched bounded-condition Gaussian covariance. Its characteristic radius obeys

\[
\boxed{R(\tau)\asymp_K\sqrt\tau.}
\]

Let

\[
B(\tau)=\mathcal B_{\gamma(\tau)}
\]

be the residual-gradient variance.

Define the Gaussian local Reynolds number

\[
\boxed{
\mathcal R_G(\tau)
:=R(\tau)^2\sqrt{B(\tau)}.
}
\]

## 2. Terminal endpoint is subcritical

At every finite first-hitting checkpoint the solution is smooth. As the Gaussian covariance collapses,

\[
B(\tau)\to0
\qquad(\tau\downarrow0).
\]

The sharper terminal-collapse estimate gives

\[
B(\tau)\lesssim_K\tau.
\]

Therefore

\[
\mathcal R_G(\tau)
\lesssim_K
\tau\sqrt\tau
=\tau^{3/2}
\to0.
\]

Hence

\[
\boxed{
\mathcal R_G(0)=0
}
\]

in the limiting sense.

## 3. Surviving source interval is supercritical

On a surviving residual pulse,

\[
m=W^{-1/3}\Lambda\to0
\]

and the order-one mean/source creation time is at least

\[
\tau_m\asymp m^{-1}.
\]

At a responsible point in this interval,

\[
B\asymp m
\]

up to fixed dyadic localization constants. Since

\[
R(\tau_m)^2\asymp m^{-1},
\]

we obtain

\[
\boxed{
\mathcal R_G(\tau_m)
\asymp
m^{-1}\sqrt m
=m^{-1/2}
\to\infty.
}
\]

Thus every surviving large-Reynolds pulse connects a terminal state with `R_G << 1` to a responsible state with `R_G >> 1`.

## 4. Canonical Reynolds-one crossing

For a smooth pre-singular solution and smoothly varying Gaussian frame, `B(tau)` and `R(tau)` are continuous. Therefore by the intermediate value theorem there exists

\[
\boxed{
0<\tau_c<\tau_m
}
\]

such that

\[
\boxed{
\mathcal R_G(\tau_c)=1.
}
\]

Let

\[
R_c=R(\tau_c).
\]

Then, up to bounded-condition constants,

\[
\boxed{
B(\tau_c)R_c^4\asymp1.
}
\]

In the isotropic normalization one may choose the crossing so that

\[
\boxed{B_cR_c^4=1.}
\]

This supplies dynamically the exact critical spatial power that the static finite-energy estimate could not provide.

## 5. Critical residual `L3` bound

The local Gaussian Sobolev estimate gives

\[
\|r\|_{L^3(B_{CR})}
\lesssim_K
R^2\sqrt B.
\]

At the crossing,

\[
\boxed{
\|r(\tau_c)\|_{L^3(B_{CR_c})}
\lesssim_K1.
}
\]

If the crossing state is near the nontrivial second-Hermite/low-curvature sector, the finite-dimensional lower norm equivalence gives the complementary bound

\[
\boxed{
\|r(\tau_c)\|_{L^3(B_{CR_c})}
\gtrsim_K1.
}
\]

Thus a low-curvature crossing produces a genuinely nontrivial scale-critical residual-velocity state.

If this lower bound fails because the state is not low curvature, the crossing is already in the high-Hermite/derivative branch.

## 6. Standard Navier--Stokes rescaling at the crossing

Recenter at the crossing space-time point and define

\[
\boxed{
V_c(z,\theta)
=R_c
U(a_c+R_cz,
 s_c+R_c^2\theta).
}
\]

This is the standard Navier--Stokes scaling. The affine-free residual rescales to critical amplitude because

\[
R_c^2\sqrt{B_c}\asymp1.
\]

Hence its local `L3` size on fixed `z`-balls is order one.

## 7. Adaptive precursor gives an ancient horizon

Let the previous adaptive first-hitting checkpoint be a normalized backward time `q` with

\[
q\asymp W^{1/3+2\varepsilon}.
\]

The crossing occurs no earlier than the responsible time in the sense

\[
R_c^2\asymp\tau_c
\le
C m^{-1}.
\]

Therefore the available backward horizon in crossing-scale variables satisfies

\[
\frac{q-\tau_c}{R_c^2}
\gtrsim
\frac{q}{R_c^2}-1
\gtrsim
qm-1.
\]

Since

\[
qm
=
W^{1/3+2\varepsilon}
W^{-1/3}\Lambda
=
W^{2\varepsilon}\Lambda
\to\infty,
\]

we obtain

\[
\boxed{
\frac{q-\tau_c}{R_c^2}
\to\infty.
}
\]

Thus every surviving pulse carries a canonical critical rescaling with an automatically diverging backward time horizon.

## 8. Why the standard ancient `L3` theorem is not yet directly applicable

The residual has critical `L3` size, but the full rescaled velocity contains the Gaussian affine representative.

At crossing scale, a coherent affine rotation/strain contributes a linear background

\[
R_c^2L_c z.
\]

This is not globally `L3(R3)` and cannot simply be subtracted while claiming that the residual still solves the standard Navier--Stokes system.

The skew rotation can be moved to a Coriolis operator by an orthogonal frame. Symmetric affine strain can be moved to a co-affine coordinate system at the cost of a uniformly elliptic time-dependent diffusion metric on the bounded-affine branch.

Therefore the precise missing bridge is

\[
\boxed{
\text{critical residual }L^3
+\text{ancient horizon}
+\text{bounded affine geometry}
\Longrightarrow
\text{an ancient rigidity theorem for the residual equation}.
}
\]

The classical ancient `L3` Liouville theorem cannot yet be cited for this transformed equation without proving such a bridge.

## 9. Revised H-branch dichotomy at the crossing

Every surviving high-Hermite branch now reaches one of:

### C1. Low-curvature critical crossing

\[
BR^4\asymp1,
\qquad
\|r\|_{L^3}\asymp1,
\qquad
\text{ancient horizon}\to\infty.
\]

This is a rigidity problem with bounded affine/Coriolis background.

### C2. High-curvature crossing

The state fails the low-curvature norm equivalence and is therefore already in the derivative/palinstrophy branch.

### C3. Spatial non-tightness

The critical residual loses the compact spatial mass needed for a nonzero ancient limit. This is the existing shell/critical-`L3` transport branch.

Thus the old missing-`1/R` problem is no longer absent at all scales: every large-Reynolds pulse **must cross the critical `BR^4=1` surface dynamically**. The remaining issue is compactness/rigidity at that crossing.

Status: **DYNAMIC `BR^4=1` CROSSING PROVED + ANCIENT HORIZON AUTOMATIC / ACTIVE SUBPROBLEM = BOUNDED-AFFINE ANCIENT `L3` RIGIDITY OR HIGH-DERIVATIVE/NON-TIGHT ESCAPE / GLOBAL REGULARITY NOT PROVED.**
