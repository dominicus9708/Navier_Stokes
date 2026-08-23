# Terminal Thick Window / Action Overlap Gate — 2026-08-24

Status: **EXPLICIT TERMINAL THICK-TIME WINDOW + ACTION-CONCENTRATION FLOOR / GLOBAL REGULARITY NOT PROVED.**

This note addresses the remaining temporal-overlap question in the transverse covariance route:

\[
\text{can all transmitted transverse action occur only when the tracked high-vorticity core is thin?}
\]

On the smooth first-hitting analytic corridor, the answer is constrained by a terminal persistence window obtained directly from the normalized vorticity equation.

---

## 1. Normalized vorticity equation and record-growth rate

Use

\[
\Omega_s+U\cdot\nabla\Omega
+\frac b2y\cdot\nabla\Omega+b\Omega
=\Sigma\Omega+
u\Delta\Omega,
\]

and set

\[
V=U+\frac b2y.
\]

Then along a `V`-characteristic `Y(s)`,

\[
\boxed{
\frac d{ds}\Omega(Y(s),s)
=(\Sigma-bI)\Omega+
u\Delta\Omega.
}
\]

On a record first-hitting corridor the running maximum is nondecreasing, so

\[
b\ge0.
\]

At a spatial maximum of the vorticity magnitude, the exact magnitude equation gives the usual upper record-growth rate

\[
\frac d{dt}\log W
\le\|S\|_\infty.
\]

Since `ds/dt=W` and `Sigma=S/W`,

\[
\boxed{
0\le b\le\|\Sigma\|_\infty.
}
\]

Assume the smooth tight corridor supplies

\[
\boxed{
\|\Sigma\|_\infty\le B_+.
}
\]

Therefore

\[
0\le b\le B_+.
\]

---

## 2. Temporal persistence of the endpoint maximum

Assume on the relevant terminal normalized block the analytic derivative ceilings

\[
\boxed{
\|\nabla\Omega\|_\infty\le K_{1,+},
\qquad
\|\nabla^2\Omega\|_\infty\le K_{2,+}.
}
\]

If these ceilings fail, the stage has already exited to the derivative/analyticity branch.

Because the directional-second-derivative bound controls each coordinate second derivative,

\[
|\Delta\Omega|
\le3K_{2,+}.
\]

Also `|Omega|<=1` under dynamic first-hitting normalization.  Hence along the characteristic,

\[
\left|\frac d{ds}\Omega(Y(s),s)\right|
\le
2B_++3\nu K_{2,+}.
\]

Define

\[
\boxed{
C_T:=2B_++3\nu K_{2,+}.
}
\]

At the terminal first-hitting point `s_1`, choose

\[
|\Omega(Y(s_1),s_1)|=1.
\]

Then for

\[
0\le s_1-s\le\delta_T,
\qquad
\boxed{
\delta_T:=\frac1{4C_T},
}
\]

we have

\[
\boxed{
|\Omega(Y(s),s)|\ge\frac34.
}
\]

Thus the dangerous endpoint cannot appear from zero amplitude instantaneously on the smooth bounded-derivative lane.

---

## 3. Spatial thickening around the transported center

Set

\[
\boxed{
r_T:=\frac1{4K_{1,+}}.}
\]

For

\[
|y-Y(s)|\le r_T,
\]

we have

\[
|\Omega(y,s)|
\ge
|\Omega(Y(s),s)|
-K_{1,+}r_T
\ge
\frac34-rac14
=rac12.
\]

Hence on the terminal spacetime tube

\[
\boxed{
\mathcal T_T
=\{(y,s):s\in[s_1-\delta_T,s_1],\ |y-Y(s)|\le r_T\}
}
\]

one has

\[
\boxed{
|\Omega|\ge\frac12.
}
\]

The enstrophy density therefore satisfies

\[
\boxed{
\frac18\le e=\frac12|\Omega|^2\le\frac12
}
\]

throughout this tube.

---

## 4. Uniform covariance thickness on the terminal window

Normalize `e dy` on the ball `B_{r_T}(Y(s))` to a probability measure and let `Q(s)` be its centered covariance.

The density lower/upper ratio is

\[
\beta_T=\frac{1/8}{1/2}=\frac14.
\]

The uniform probability measure on a three-dimensional ball of radius `r_T` has covariance

\[
\frac{r_T^2}{5}I_3.
\]

By the positive-semidefinite covariance-of-mixtures formula,

\[
\boxed{
Q(s)\succeq
\frac{\beta_T r_T^2}{5}I_3
=
\frac{r_T^2}{20}I_3.
}
\]

Therefore for every transverse plane,

\[
\boxed{
q_\perp(s)
\ge q_{T,-}:=\frac{r_T^2}{20}
}
\]

throughout the terminal window.

Thus the thick-covariance hypothesis needed by the transverse shape gate holds automatically for a fixed terminal normalized time, provided the smooth amplitude/derivative ceilings hold.

---

## 5. Transverse action cannot avoid the thick window arbitrarily cheaply

Let `D_c(s)` denote the **actual transmitted/core** transverse trace-free strain along the tracked core lane, after uniform remote/near cancellation has already been removed by the canonical/effective classification.

Assume

\[
\boxed{
|D_c(s)|_F\le B_D
}
\]

on the stage.  For a pointwise full-strain transverse projection one may take conservatively

\[
B_D\le B_+.
\]

Let the stage carry fixed transmitted transverse action

\[
\boxed{
A_D(I_j)
=\int_{I_j}|D_c(s)|_Fds
\ge a_D>0.
}
\]

Let

\[
I_T
=I_j\cap[s_1-\delta_T,s_1].
\]

If `L_j<=delta_T`, the whole stage lies in the thick terminal window.

If `L_j>delta_T`, the action outside the thick window is at most

\[
B_D(L_j-\delta_T).
\]

Hence the action that **must** overlap the thick window satisfies

\[
\boxed{
A_D(I_T)
\ge
\left[
a_D-B_D(L_j-\delta_T)_+
\right]_+.
}
\]

Using a stage ceiling `L_j<=L_var`,

\[
\boxed{
A_D(I_T)
\ge
\left[
a_D-B_D(L_{var}-\delta_T)_+
\right]_+.
}
\]

This is the direct action-thickness overlap lower bound.

---

## 6. Minimum time needed to hide all action outside the thick window

To make the terminal thick-window action vanish, one must have

\[
a_D
\le
B_D(L_j-\delta_T)
\]

with `L_j>delta_T`.  Therefore complete action/thickness separation requires

\[
\boxed{
L_j
\ge
L_{avoid}
:=
\delta_T+rac{a_D}{B_D}.
}
\]

Consequently, if the moving-variance stage ceiling satisfies

\[
\boxed{
L_{var}<L_{avoid},
}
\]

then a fixed transmitted transverse action cannot be placed entirely outside the automatically thick terminal window.

A positive part of the action is forced onto times with

\[
q_\perp\ge q_{T,-}>0.
\]

---

## 7. What happens on the thick overlap

On the thick window there are now only two cases.

### Spatially coherent transmitted strain

If the transverse strain is approximately affine/coherent across `B_{r_T}`, then the covariance shape equation applies with

\[
q_-
=q_{T,-}
=rac{r_T^2}{20}
\]

and with action at least the overlap amount

\[
A_{D,T}
=
\left[
a_D-B_D(L_{var}-\delta_T)_+
\right]_+.
\]

This feeds directly into the existing covariance/projective-action gate.

### Spatially nonuniform transmitted strain

If the core-average/effective action is small while order-one total transverse strain survives on a fixed fraction of `B_{r_T}`, the preceding `REMOTE_NEAR_CANCELLATION_PALINSTROPHY_GATE_2026-08-24.md` gives

\[
Q(s)\gtrsim r_T|D|^2
\]

and hence a finite-stage palinstrophy/time floor.

Thus spatial incoherence during the terminal thick overlap is already an `H`-tax rather than a new escape.

---

## 8. If the terminal persistence estimate fails

The terminal thick window used only

\[
\|\Sigma\|_\infty\le B_+,
\qquad
\|\nabla\Omega\|_\infty\le K_{1,+},
\qquad
\|\nabla^2\Omega\|_\infty\le K_{2,+}.
\]

Therefore failure of the window forces failure of one of the already typed smooth first-hitting controls:

\[
\boxed{
\text{strain-amplitude escape}
\lor
\text{first-derivative escape}
\lor
\text{second-derivative/analyticity escape}.
}
\]

There is no additional temporal-thickness branch hidden inside the derivation.

---

## 9. Updated transverse remote-action route

The transmitted transverse lane is now

\[
\boxed{
\begin{aligned}
A_D\ge a_D
\Longrightarrow\;&
L_j\ge L_{avoid}
\\
&\lor\
\text{positive action overlaps an automatic Taylor/analytic thick window}.
\end{aligned}
}
\]

The first line can be compared directly with the existing moving-variance upper stage time.  The second line enters the covariance/projective or spatial-oscillation/palinstrophy gates.

Thus the temporal overlap issue is reduced to an explicit finite comparison involving

\[
\boxed{
B_+,\ K_{1,+},\ K_{2,+},\ \nu,\ a_D,\ L_{var}.
}
\]

---

## 10. Scope

This note does not assert that the entire first-hitting stage is thick.  It proves only a fixed terminal thick window whose size depends on already tracked smooth bounds.

The characteristic center may move; this causes no problem because the spatial ball is transported with `Y(s)`.  If the intended tracked center departs by an order-one natural-scale amount from this transported core, that is the already typed center-turnover branch.

Status: **A FIRST-HITTING ENDPOINT WITH BOUNDED STRAIN AND ANALYTIC DERIVATIVES CARRIES AN AUTOMATIC TERMINAL SPACETIME TUBE WITH `|Omega|>=1/2`, `q_perp>=r_T^2/20`, AND DURATION `delta_T=1/[4(2B_++3nu K2,+)]`. A FIXED TRANSMITTED TRANSVERSE ACTION CAN AVOID THIS THICK WINDOW ONLY IF THE STAGE LASTS AT LEAST `L_avoid=delta_T+a_D/B_D`; OTHERWISE POSITIVE ACTION MUST OVERLAP THE THICK COVARIANCE AND ENTER THE EXISTING PROJECTIVE/PALINSTROPHY GATES. GLOBAL REGULARITY REMAINS UNPROVED.**