# DSD M17-104 — Nonzero director-area current cannot vanish on a regular material trajectory in finite similarity time

Date: 2026-09-05
Canonical ID: **M17-104**

Status: **INTERNAL RANK-2 MATERIAL CARRIER NONVANISHING GATE / THE REMAINING CARRIER-LEVEL EXIT LIST AFTER M17-103 INCLUDES `J_xi=0`. M17-026 ALREADY GIVES THE EXACT HOMOGENEOUS CAUCHY LAW `D_B J_xi=[grad B-(3/2)I]J_xi`. ALONG ANY REGULAR MATERIAL TRAJECTORY THIS IS A LINEAR HOMOGENEOUS ODE WITH AN INVERTIBLE FUNDAMENTAL MATRIX. CONSEQUENTLY A MATERIAL MARKER WITH `J_xi(theta_0)!=0` CANNOT REACH `J_xi=0` AT ANY FINITE LATER OR EARLIER SIMILARITY TIME WHILE THE COEFFICIENT FIELD REMAINS REGULAR/INTEGRABLE. EQUIVALENTLY, FULL DIRECTOR RANK TWO IS FINITE-TIME MATERIAL-INVARIANT INSIDE THE ACTIVE `rho>0` DIRECTOR CHART. EULERIAN RANK CHANGE AT A FIXED SPATIAL POINT IS NOT EXCLUDED BECAUSE DIFFERENT MATERIAL LABELS MAY PASS THROUGH THAT POINT, AND ASYMPTOTIC `|J_xi|->0` OR EXIT THROUGH `rho=0`, LOSS OF THE DIRECTOR CHART, OR LOSS OF REGULARITY REMAINS POSSIBLE. THUS `J_xi=0` IS REMOVED AS AN ORDINARY FINITE-TIME INTERNAL TURNOVER CHANNEL OF A PERSISTENT MATERIAL CARRIER. THE RANK-2 SIGNED-FLUX FRONTIER CONTRACTS TO ENDPOINT/ACTIVE-DOMAIN/CHART-INTERFACE EXITS AND ASYMPTOTIC DEGENERATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact director-area Cauchy law

M17-026 gives

\[
\boxed{
D_BJ_\xi
=(\nabla B)J_\xi
-\frac32J_\xi.
}
\]

Define

\[
\boxed{
A(\theta)
:=\nabla B(X(\theta),\theta)-\frac32I
}
\]

along a material trajectory

\[
\dot X=B(X,\theta).
\]

Then the director-area current satisfies the finite-dimensional linear ODE

\[
\boxed{
\frac d{d\theta}J_\xi(X(\theta),\theta)
=A(\theta)J_\xi(X(\theta),\theta).
}
\]

---

## 2. Fundamental matrix is invertible

Let `Phi(theta,theta_0)` solve

\[
\frac d{d\theta}\Phi
=A(\theta)\Phi,
\qquad
\Phi(\theta_0,\theta_0)=I.
\]

On every finite interval where `A` is integrable, the fundamental matrix exists and is invertible.

Liouville's formula gives

\[
\boxed{
\det\Phi(\theta,\theta_0)
=
\exp\left(
\int_{\theta_0}^{\theta}
\operatorname{tr}A(s)\,ds
\right)
\neq0.
}
\]

Therefore

\[
\boxed{
J_\xi(\theta)
=\Phi(\theta,\theta_0)J_\xi(\theta_0).
}
\]

---

## 3. Finite-time nonvanishing

If

\[
J_\xi(\theta_0)\neq0,
\]

then invertibility of `Phi` implies

\[
\boxed{
J_\xi(\theta)\neq0
}
\]

for every finite `theta` in the same regular material interval.

Hence

\[
\boxed{
J_\xi\neq0
\quad\Longrightarrow\quad
\text{no finite-time material transition to }J_\xi=0
}
\]

inside the regular active chart.

This conclusion is exact and does not depend on the sign of any strain component.

---

## 4. Scalar magnitude law on the pure-kernel branch

On the pure-transverse-kernel branch M17-033 gives

\[
\boxed{
D_B\log|J_\xi|
=\sigma_k-1.
}
\]

Therefore

\[
\boxed{
|J_\xi(\theta)|
=|J_\xi(\theta_0)|
\exp\left(
\int_{\theta_0}^{\theta}(\sigma_k-1)\,ds
\right).
}
\]

This makes the nonvanishing transparent:
for every finite interval on which the strain is integrable, the exponential is strictly positive.

Thus `|J_xi|` may become very small but cannot become exactly zero in finite regular material time.

---

## 5. Rank interpretation

For a smooth map

\[
\xi:\Omega\to S^2,
\]

the director-area current is the Hodge dual of the pullback sphere-area two-form.

On the active branch,

\[
\boxed{
J_\xi\neq0
\iff
\operatorname{rank}d\xi=2.
}
\]

Therefore

\[
\boxed{
\operatorname{rank}d\xi=2
}
\]

is preserved along every finite regular material trajectory that remains inside the same `rho>0` director chart.

A material Rank-2 marker cannot smoothly become Rank 1 at finite time without leaving the hypotheses of the director Cauchy law.

---

## 6. Important Eulerian/material distinction

The statement is material, not Eulerian.

At a fixed spatial point `x`, the value

\[
J_\xi(x,\theta)
\]

may change because different material labels pass through `x`.

Therefore

\[
\boxed{
\text{Eulerian rank change at fixed }x
\not\equiv
\text{material rank loss of one carrier}.
}
\]

M17-104 closes only the latter.

This distinction is essential for DSD genealogy accounting.

---

## 7. What remains possible

The finite-time nonvanishing theorem does not exclude:

### asymptotic degeneration

\[
|J_\xi(\theta)|\to0
\quad\text{as }|\theta|\to\infty;
\]

### active-domain exit

\[
\rho\to0,
\]

where the director

\[
\xi=W/|W|
\]

ceases to define the same chart;

### endpoint/interface exit

The material tube may leave the compact region or the retained local coordinate/interface description;

### loss of regularity

If the coefficient matrix `A` ceases to be locally integrable, the present ODE continuation hypothesis fails.

None of these is silently converted into a contradiction.

---

## 8. Consequence for peak/type genealogy

M17-103 already shows that all finite interior peak/type/tangency genealogy is signed director-area-flux neutral as long as the same tube survives.

M17-104 now shows that the same tube cannot lose its nonzero director-area current at a finite regular material time.

Therefore the ordinary internal source classes reduce to

\[
\boxed{
\text{none at finite regular material time}
}
\]

at the carrier level.

Any genuine carrier loss must be associated with an active-domain/endpoint/interface exit, asymptotic degeneration, or failure of regularity.

---

## 9. Relation to the recurrent resonant frame

On a same-marker recurrent pure-kernel Rank-2 trajectory, M17-033 gives

\[
\langle\sigma_k\rangle=1.
\]

This is exactly the zero-mean logarithmic drift condition for `|J_xi|`:

\[
\left\langle
D_B\log|J_\xi|
\right\rangle=0.
\]

Thus recurrent nonzero area current is dynamically compatible with the Cauchy law.

M17-104 does not create a recurrence contradiction; it only forbids finite-time annihilation as a turnover mechanism.

---

## 10. DSD analysis

The former event label

\[
J_\xi\to0
\]

contained two distinct possibilities:

1. finite-time exact vanishing of a regular material carrier;
2. asymptotic or chart-boundary degeneration.

The first is impossible by the homogeneous Cauchy ODE.
The second remains open.

This split removes a false finite-time genealogy channel.

---

## 11. DSD audit

### Audit A — inferring nonvanishing from boundedness alone
Not needed. It follows from invertibility of the linear flow map.

### Audit B — claiming `J_xi` has constant magnitude
Rejected. Its magnitude evolves exponentially with `sigma_k-1`.

### Audit C — claiming Eulerian rank two is globally permanent at every fixed point
Rejected. The result is along material trajectories.

### Audit D — continuing through `rho=0`
Rejected. The director chart may fail there.

### Audit E — excluding asymptotic rank degeneration
Rejected. Only finite regular material time is closed.

### Audit F — proof status
One carrier-exit branch is removed from finite-time internal turnover, but endpoint/domain/interface/asymptotic assembly remains open.

---

## 12. Updated Rank-2 carrier frontier

On the regular active finite-order pure-kernel branch,

\[
\boxed{
\begin{aligned}
&\text{finite interior peak/type/tangency events}
&&\text{are algebraically recyclable},\\
&J_\xi(\theta_0)\neq0
&&\Longrightarrow J_\xi(\theta)\neq0
\text{ for finite regular material time}.
\end{aligned}
}
\]

Hence

\[
\boxed{
R_2^{persistent\ material\ carrier}
\Longrightarrow
R_2^{interior\ recyclable}
\ \lor\
E_{endpoint/active-domain/interface}
\ \lor\
E_{asymptotic}
\ \lor\
E_{loss\ of\ regularity}.
}
\]

The next high-value gate is the **active-domain endpoint flux gate**: determine whether a nonzero director-area carrier can repeatedly leave and re-enter the `rho>0` active peak hull through its endpoints/interfaces while preserving the global recurrent transport and finite-energy constraints, or whether such recycling requires a forbidden flux/current budget.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
