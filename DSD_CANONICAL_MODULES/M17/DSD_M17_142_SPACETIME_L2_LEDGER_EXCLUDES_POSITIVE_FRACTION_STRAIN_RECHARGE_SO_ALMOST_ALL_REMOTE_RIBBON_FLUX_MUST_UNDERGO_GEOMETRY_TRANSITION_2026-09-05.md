# DSD M17-142 — Spacetime `L^2` ledger excludes positive-fraction strain recharge, so almost all remote ribbon flux must undergo geometry transition

Date: 2026-09-05  
Canonical ID: **M17-142**

Status: **POSITIVE-FRACTION RECHARGE BRANCH CLOSED ON A QUIET CRITICAL SPACETIME BLOCK / IF THE SCALE-CRITICAL SHELL DIRICHLET BOUND `rho int |grad U|^2 <= J_*` HOLDS UNIFORMLY THROUGH A FIXED FINITE BLOCK OF REMOTE DYADIC SHELLS AND A FIXED `O(1)` SIMILARITY-TIME CORRIDOR, THEN A POSITIVE FRACTION OF AN ORDER-ONE-FLUX COMPACT RIBBON POPULATION CANNOT REMAIN IN THE COMPACT `c_J <= |J_xi| <= C_J` CLASS WHILE USING KERNEL STRAIN TO PREVENT BACKWARD DIRECTOR-JACOBIAN GROWTH. THE REQUIRED ORDER-ONE MATERIAL STRAIN ACTION WOULD COST ORDER-ONE SPACETIME `L^2` STRAIN, BUT THE ENTIRE REMOTE BLOCK HAS ONLY `O(R^{-1})` BUDGET. HENCE, EXCEPT FOR A VANISHING FLUX/VOLUME FRACTION, EACH REMOTE RIBBON CARRIER MUST ENCOUNTER A COMPACT-GEOMETRY/TYPE EXIT WITHIN A UNIFORMLY BOUNDED INWARD LOG-RADIUS DISTANCE, UNLESS THE CRITICAL SPACETIME SHELL BOUND ITSELF FAILS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Choose a fixed inward block long enough to require positive strain action

Let an outer remote compact ribbon satisfy

\[
\boxed{
|J_\xi|_{out}\ge c_J>0
}
\]

and suppose a material point can be followed backward through `m` dyadic shell passages while remaining in a compact Rank-2 corridor with

\[
\boxed{
|J_\xi|\le C_J<\infty.
}
\]

The exact material law is

\[
D_B\log|J_\xi|=\sigma_k-1.
\]

Let the total forward similarity time across those `m` shells be `Delta theta_m`.
By M17-138,

\[
\Delta\theta_m
=2m\log2+o_R(1)
\]

for fixed `m` as the outer radius `R -> infinity`.

Integrating from the inner endpoint to the observed outer endpoint,

\[
\int_I\sigma_kd\theta
=
\Delta\theta_m
+
\log\frac{|J_\xi|_{out}}{|J_\xi|_{in}}.
\]

Using

\[
|J_\xi|_{out}\ge c_J,
\qquad
|J_\xi|_{in}\le C_J,
\]

we obtain

\[
\boxed{
\int_I\sigma_kd\theta
\ge
\Delta\theta_m-\log(C_J/c_J).
}
\]

Choose once and for all `m_0` so large that

\[
2m_0\log2-\log(C_J/c_J)\ge2a_0
\]

for some fixed `a_0>0`.
Then for all sufficiently remote shells,

\[
\boxed{
\int_I\sigma_kd\theta\ge a_0
}
\]

for every material point whose backward history remains inside the compact bounded-`J_xi` corridor for the whole `m_0`-shell block.

---

## 2. Each such material point pays a fixed `L^2` strain action

The block duration

\[
T_0:=\sup_R|I|<\infty
\]

is a fixed constant because `m_0` is fixed.

By Cauchy--Schwarz,

\[
a_0^2
\le
|I|\int_I\sigma_k^2d\theta
\le
T_0\int_I\sigma_k^2d\theta.
\]

Therefore every through-compact material point satisfies

\[
\boxed{
\int_I\sigma_k^2d\theta
\ge
\frac{a_0^2}{T_0}
=:q_0>0.
}
\]

Thus the required recharge cannot be made arbitrarily cheap along an individual material history merely by concentrating it in time.

---

## 3. Similarity-flow volume distortion over the fixed block is bounded

The similarity material field is

\[
B=U+\frac12y,
\]

with

\[
\nabla\cdot B=\frac32.
\]

Hence the flow-map Jacobian over a time gap `tau` is

\[
\boxed{
\det D\Phi=e^{3\tau/2}.
}
\]

Since the block duration is bounded by `T_0`, material volume at any two times in the block differs by at most the fixed factor

\[
\boxed{e^{3T_0/2}.}
\]

Thus a positive-volume subset at the observed outer time remains a comparable positive material volume when transported through the finite block.

---

## 4. Positive-fraction recharge forces order-one spacetime strain cost

Let `F_R` be the subset of the observed outer ribbon `T_R` whose material histories remain in the compact bounded-`J_xi` corridor throughout the entire `m_0`-shell backward block.

Integrating the trajectory lower bound over `F_R` at the outer time gives

\[
q_0|F_R|
\le
\int_{F_R}
\int_I\sigma_k(\Phi_{\theta,\theta_{out}}^{-1}y,\theta)^2
\,d\theta\,dy.
\]

Changing variables to the material images and using the bounded similarity volume distortion yields

\[
\boxed{
q_0|F_R|
\le
C(T_0)
\int_I\int_{\mathcal B_R(\theta)}|\Sigma|^2dy\,d\theta,
}
\]

where `B_R(theta)` is the finite remote shell block swept out by those histories.

---

## 5. Quiet critical shell corridor has only `O(R^{-1})` spacetime cost

Assume that throughout the block, on every one of the finitely many dyadic annuli involved,

\[
\boxed{
\rho\int_{C_\rho}|\nabla U(\theta)|^2dy
\le
J_*
}
\]

with the same fixed `J_*`.

All radii in the fixed `m_0`-shell block are comparable to the outer radius `R` up to a fixed factor `2^{m_0}`.
Hence, summing over the finite overlap family,

\[
\int_{\mathcal B_R(\theta)}|\Sigma|^2dy
\le
\int_{\mathcal B_R(\theta)}|\nabla U|^2dy
\le
\frac{C(m_0)J_*}{R}.
\]

Integrating over the fixed time interval,

\[
\boxed{
\int_I\int_{\mathcal B_R(\theta)}|\Sigma|^2dy\,d\theta
\le
\frac{C_*}{R}.
}
\]

Combining with the previous section,

\[
\boxed{
|F_R|\le\frac{C}{R}.
}
\]

---

## 6. Compare with the order-one ribbon volume floor

M17-140 gives

\[
|\mathcal T_R|\ge V_*>0.
\]

Therefore

\[
\boxed{
\frac{|F_R|}{|\mathcal T_R|}
\le
\frac{C}{V_*R}
\to0.
}
\]

Because `dV` and `dPhi_J ds` are uniformly equivalent on the nondegenerate ribbon branch,

\[
\boxed{
\frac{\nu_J(F_R)}{\nu_J(\mathcal T_R)}
=O(R^{-1})
\to0.
}
\]

Thus asymptotically **almost none** of the order-one ribbon population can remain in the compact bounded-`J_xi` class across the entire fixed inward block while paying the required recharge with ordinary kernel strain.

---

## 7. The actual branch implication

For a fixed-fraction remote compact ribbon population, one of two things must happen:

### A. Critical spacetime shell bound fails

At some shell/time in the bounded inward block,

\[
\boxed{
\rho\int_{C_\rho}|\nabla U|^2dy>J_*.
}
\]

This is a genuine dynamic critical-shell burst / `H_{1,crit}`-type exit and must be routed separately.

### B. Quiet critical block holds

Then, except for `o(1)` of the ribbon volume/flux-arclength population,

\[
\boxed{
\text{the material carrier leaves the compact bounded-}J_\xi\text{ ribbon class}
}
\]

within at most `m_0` inward dyadic shell steps.

Therefore

\[
\boxed{
R_{2,\rm ribbon}^{remote}
\Longrightarrow
H_{1,crit}^{spacetime}
\ \lor
G_{\rm frequent}^{almost\ all\ flux}.
}
\]

Here `G_frequent` is a frequent geometry/type transition, with uniformly bounded spacing in log radius, affecting asymptotically full ribbon carrier measure.

---

## 8. What happened to the concentrated-recharge branch

M17-140 allowed the logical possibility that a vanishing ribbon subset carries concentrated strain recharge.

This remains possible for a vanishing fraction of carriers.
But it cannot service a **positive fraction** of the order-one remote ribbon population under the quiet critical spacetime ledger.

The reason is measure-independent of recharge thickness:
concentrating an action `int sigma_k >= a_0` in time only increases the `L^2` action cost by Cauchy--Schwarz.

Thus

\[
\boxed{
\text{concentrated strain recharge cannot be the dominant population mechanism.}
}
\]

---

## 9. DSD audit

### Audit A — snapshot `J_R=O(1)` is enough for the spacetime conclusion

Rejected.
The quiet critical bound must hold throughout the fixed backward spacetime block. Failure is explicitly retained as `H_{1,crit}^{spacetime}`.

### Audit B — similarity material volume is conserved

Rejected.
`div B=3/2`; the flow expands similarity volume exponentially. Over a fixed block this gives only a fixed comparison factor, which is exactly what the proof uses.

### Audit C — every point in the outer ribbon must stay inside one complete ribbon chart backward

Rejected.
The set of points for which this fails is precisely the geometry-transition branch. The estimate shows that this branch has asymptotically full population measure on a quiet critical block.

### Audit D — a thin high-strain layer can recharge a positive flux population at arbitrarily small `L^2` cost

Rejected.
Fixed positive material action plus Cauchy--Schwarz forces fixed trajectory `L^2` action; integrating a positive material population gives order-one spacetime cost.

### Audit E — frequent geometry transitions are themselves singular

Not established. They may be smooth chart/type transitions. Their cost and compatibility are the next target.

---

## 10. Updated highest-value frontier

The low-amplitude strong-director ribbon branch is no longer primarily a strain-recharge problem.
On a quiet critical remote corridor, its dominant carrier population must repeatedly undergo **geometry/type transitions** at uniformly bounded dyadic spacing.

Thus the next question is:

\[
\boxed{
\text{Can asymptotically full order-one director-flux measure undergo infinitely many smooth}
\text{ compact-ribbon geometry transitions at bounded log-radius spacing}
}
\]

while keeping

\[
\rho_R^2\sim R^{-1},
\qquad
\int|\nabla U|^2\sim R^{-1},
\qquad
\int|\nabla W|^2\sim R^{-1},
\]

and satisfying the finite analytic type/jet architecture M17-085--M17-103?

The next efficient calculation is therefore to use the finite critical-type/top-jet atlas to determine whether repeated compact-ribbon entry/exit is merely a chart change with inherited flux, or requires a genuine degeneracy (`D_k g=0`, top-jet fold, rank/endpoint event) that carries a positive derivative or pressure cost.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
