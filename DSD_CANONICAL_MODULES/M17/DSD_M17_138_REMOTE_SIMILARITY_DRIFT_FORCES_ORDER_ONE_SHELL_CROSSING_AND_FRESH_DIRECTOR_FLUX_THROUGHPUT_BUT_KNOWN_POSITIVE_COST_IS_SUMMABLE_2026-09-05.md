# DSD M17-138 — Remote similarity drift forces `O(1)` shell crossing and fresh director-flux throughput, but the known positive cost is summable

Date: 2026-09-05  
Canonical ID: **M17-138**

Status: **EXACT REMOTE-DRIFT / THROUGHPUT REDUCTION / ON THE BOUNDED-VELOCITY BRANCH, MATERIAL TRAJECTORIES CROSS EACH REMOTE DYADIC SIMILARITY SHELL IN ASYMPTOTIC TIME `2 log 2`. HENCE A RECURRENT FIXED-FRACTION RIBBON POPULATION IS NECESSARILY AN `O(1)`-TIME FRESH-DIRECTOR-FLUX THROUGHPUT. HOWEVER THE CURRENT POSITIVE AMPLITUDE-WEIGHTED DIRECTOR-GEOMETRY COST IS ONLY `O(R^{-1})` PER CRITICAL REMOTE RIBBON AND IS GEOMETRICALLY SUMMABLE. THE UNWEIGHTED DIRECTOR-AREA TOTAL VARIATION HAS NO KNOWN FINITE GLOBAL BUDGET. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity material velocity

The CE-H material velocity is

\[
\boxed{B=U+\frac12 y.}
\]

Let

\[
r(\theta):=|y(\theta)|
\]

along a material trajectory.
Then

\[
\frac{dr}{d\theta}
=B\cdot\hat r
=\frac r2+U\cdot\hat r,
\]

and therefore

\[
\boxed{
\frac d{d\theta}\log r
=\frac12+\frac{U\cdot\hat r}{r}.
}
\]

---

## 2. Uniformly bounded velocity makes the remote drift asymptotically radial

Retain the bounded-velocity branch used in the previous genealogy audit:

\[
\|U\|_{L^\infty}\le M_U.
\]

On a remote shell

\[
R\le r\le2R,
\]

we have

\[
\left|
\frac{U\cdot\hat r}{r}
\right|
\le
\frac{M_U}{R}.
\]

Hence

\[
\boxed{
\frac12-\frac{M_U}{R}
\le
\frac d{d\theta}\log r
\le
\frac12+\frac{M_U}{R}.
}
\]

For sufficiently large `R>2M_U`, the radial motion is strictly outward.

---

## 3. Exact asymptotic dyadic crossing time

Let `theta_in` and `theta_out` denote the first times at which one remote trajectory crosses radii `R` and `2R` while remaining in the annular corridor.
Integrating the preceding bound gives

\[
\frac{\log2}{\frac12+M_U/R}
\le
\Delta\theta_R
\le
\frac{\log2}{\frac12-M_U/R}.
\]

Therefore

\[
\boxed{
\Delta\theta_R
=2\log2+O(R^{-1}).
}
\]

In particular, there are constants `0<c_-<c_+<infinity`, independent of all sufficiently large `R`, such that

\[
\boxed{
c_-\le\Delta\theta_R\le c_+.}
\]

Thus a remote material carrier does not dwell for a time proportional to the shell radius in similarity coordinates.
The dilation drift transports it through every dyadic shell in `O(1)` similarity time.

---

## 4. Consequence for the M17-135 fresh-carrier branch

M17-133 and M17-135 reduce the fixed-fraction nondegenerate ribbon branch to low amplitude but order-one director flux:

\[
\Phi_R\ge c_\Phi>0,
\qquad
\rho_R^2\sim R^{-1}
\]

on the cheap critical scaling.

M17-117 excludes indefinitely persistent same-material compact ribbons, while the present calculation shows that the ambient similarity drift already transports any remote material object through one dyadic shell in `O(1)` time.

Hence an Eulerian recurrent ribbon population in a fixed remote annular band must be serviced by repeated material crossing/import:

\[
\boxed{
\text{recurrent remote ribbon population}
\Longrightarrow
\text{fresh material director-flux throughput on }O(1)\text{ time}.}
\]

If each occupied ribbon carries at least `c_Phi`, then the **positive** director-area throughput has order-one size per occupied replacement event.

---

## 5. Signed flux conservation does not bound positive throughput

The director-area current obeys

\[
\nabla\cdot J_\xi=0
\]

and the associated material 2-form is frozen.

This controls signed flux through material sections.
It does not control the positive total variation of flux crossing a fixed Eulerian annular boundary.

Closed tubes can enter and leave, and oppositely oriented flux pieces can cancel algebraically while retaining large positive total variation.

Therefore

\[
\boxed{
\text{order-one positive throughput}
\not\Rightarrow
\text{growth of a signed conserved charge}.
}
\]

This is the same signed-versus-unsigned firewall identified earlier for peak/fold populations, now in radial throughput form.

---

## 6. Known positive geometric cost per ribbon

M17-131 gives the pointwise inequality

\[
2\rho^2|J_\xi|
\le
|\nabla W|^2.
\]

In flux coordinates on a compact complete ribbon,

\[
\int_{\mathcal T_R}|\nabla W|^2dy
\ge
2\int d\Phi_J
\oint\rho^2ds.
\]

For the M17-135 critical firewall scaling

\[
\Phi_R\asymp1,
\qquad
L_R\asymp1,
\qquad
\rho_R^2\asymp R^{-1},
\]

this positive lower cost has natural size

\[
\boxed{
P_R^{dir}
\gtrsim R^{-1}.
}
\]

For a uniformly scaled normalized profile, the matching upper size is also `O(R^{-1})`, as recorded in M17-135.

Thus the positive director-geometry cost can be exactly of order

\[
\boxed{P_R^{dir}\asymp R^{-1}.}
\]

---

## 7. Geometric shell spacing makes the positive cost summable

For first-hitting age shells,

\[
R_k=K_k=q^{k/2}
\]

is geometric.
Hence

\[
\boxed{
\sum_k R_k^{-1}<\infty.
}
\]

Therefore infinitely many order-one director-flux passages can coexist with

\[
\boxed{
\sum_kP_{R_k}^{dir}<\infty
}
\]

on the low-amplitude scaling.

This rules out the shortcut

\[
\text{infinitely many fresh ribbons}
\Rightarrow
\text{infinite ordinary amplitude-weighted geometric cost}.
\]

---

## 8. Why the unweighted director budget cannot be used

The natural unweighted geometric quantities include

\[
\int|J_\xi|dy,
\qquad
\int|\nabla\xi|^2dy.
\]

For one uniformly nondegenerate `O(1)` ribbon they are order one.
Thus an infinite remote stack can make their global sums diverge.

But finite Navier–Stokes energy/enstrophy does not control these amplitude-free director quantities.
Indeed

\[
W=\rho\xi
\]

allows

\[
\rho\to0
\]

while `xi` retains order-one spatial geometry.

The controlled differential quantity is amplitude weighted:

\[
|\nabla W|^2
=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
\]

Hence

\[
\boxed{
\text{divergent unweighted director variation}
}
\]

is not a contradiction with the current physical ledgers.

---

## 9. Interaction with the M17-137 `1/R` velocity bath

M17-137 proved that the non-H ribbon-captured branch carries genuine original-velocity cubic mass at shell scale:

\[
\int_{C_R}|U|^3dy\gtrsim J_R^{3/2}.
\]

For the sharp case `J_R\asymp1`, this is the `1/R` velocity bath.

The present drift estimate remains dominated by the similarity term:

\[
\frac{|U|}{R}
\ll1
\]

at the critical bath scaling, and even an `O(1)` bounded local velocity perturbation is negligible relative to `R/2` in the radial drift.

Therefore the critical bath does not provide long material residence that could evade the fresh-throughput conclusion.

---

## 10. DSD audit

### Audit A — remote material objects may remain indefinitely in one dyadic similarity shell

Rejected on the bounded-velocity branch.
The `y/2` drift gives `Delta theta_R=2 log 2+O(R^-1)`.

### Audit B — order-one fresh positive flux throughput violates `div J_xi=0`

Rejected.
Divergence-free conservation is signed; positive total variation can recycle through fixed boundaries.

### Audit C — each order-one flux event has order-one physical differential cost

Rejected.
The amplitude-weighted cost is reduced by `rho_R^2~R^-1`.

### Audit D — infinitely many order-one director-flux ribbons force infinite ordinary palinstrophy

Rejected by the critical scaling; the per-shell cost can be `O(R^-1)` and is geometrically summable.

### Audit E — an unweighted `int |J_xi|` divergence is a Navier–Stokes contradiction

Rejected. No finite global NS budget for the amplitude-free director total variation has been established.

---

## 11. Updated hard gate

The non-H fixed-fraction Rank-2 ribbon survivor is now constrained to

\[
\boxed{
\begin{gathered}
\text{genuine shell-scale }1/R\text{ cubic velocity bath},\\
\text{fresh }O(1)\text{-time material throughput},\\
\Phi_R\gtrsim1,\\
\rho_R^2\sim R^{-1},\\
\text{summable known amplitude-weighted director cost}.
\end{gathered}
}
\]

Thus a closure must supply a quantity stronger than ordinary energy/enstrophy/palinstrophy and stronger than signed director flux.

The next efficient question is whether the **full CE-H compatibility equations** forbid this low-amplitude/high-director-gradient import, rather than whether existing global positive budgets can pay for it.

A particularly sharp next gate is to compare the strain needed to transport an order-one director Jacobian with the strain that can be generated locally by the `1/R` bath plus an `R^{-1/2}` vorticity ribbon.
If local strain is `o(1)`, then

\[
D_B\log|J_\xi|=\sigma_k-1
\]

forces exponential director-area decay along each passage, so every order-one ribbon must enter the shell already geometrically charged.
Any failure of local strain smallness becomes a separate nonlocal-strain/pressure channel.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
