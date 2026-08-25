# DSD W1 Periodic Tail: Physical Critical Trace and Nonresonant Correction

Date: 2026-08-26

Status: **ASYMPTOTIC LOG-PERIODIC DEFECT RATE DERIVED IN THE FAR BLOW-DOWN TOPOLOGY / PHYSICAL LEADING TRACE IDENTIFIED / STATIONARY-PROFILE OVERINTERPRETATION EXCLUDED / GLOBAL REGULARITY NOT PROVED.**

## 1. Starting point

For a periodic W1 Leray survivor of period `S`, the previous far blow-down note proves that the remote shell dynamics is governed at leading order by
\[
U_s+\frac12U+\frac12Y\cdot\nabla U=0,
\]
while nonlinear and viscous effects are smaller by `R^{-2}` after critical spatial blow-down.

Introduce logarithmic radius
\[
\rho=\log|Y|,
\qquad
Y=e^\rho\theta,
\qquad
\theta\in S^2,
\]
and the critical amplitude variable
\[
\boxed{
w(\rho,\theta,s):=e^\rho U(e^\rho\theta,s).
}
\]
For an ideal `1/R` tail, `w` is order one.

---

## 2. Linear Leray operator becomes log-radial transport

A direct calculation gives
\[
U=e^{-\rho}w,
\]
and
\[
\boxed{
U_s+\frac12U+\frac12Y\cdot\nabla U
=e^{-\rho}
\left(
\partial_sw+\frac12\partial_\rho w
\right).
}
\]
The exact cancellation of the zeroth-order `w` term is the critical `-1` homogeneity.

The Navier-Stokes nonlinearity, viscosity, and pressure gradient have physical homogeneity `-3`.  Consequently, after multiplying the Leray equation by `e^rho`, one obtains schematically
\[
\boxed{
\left(\partial_s+\frac12\partial_\rho\right)w
=e^{-2\rho}\mathcal N[w],
}
\]
where `N[w]` contains the angular/radial nonlinear, pressure, and viscous operators.

In the rigorous shell formulation of the far blow-down note, `N[w]` is uniformly bounded in the corresponding fixed-annulus `H^{-1}` topology because the rescaled fields are uniformly bounded in `H^1`.

**Status: PROVED in the fixed-annulus weak topology.**

---

## 3. Integrate one period along a dilation characteristic

The characteristics of
\[
D:=\partial_s+\frac12\partial_\rho
\]
are
\[
\rho(\tau)=\rho_0+\frac\tau2,
\qquad
s(\tau)=s_0+\tau.
\]
Integrating the exact equation from `tau=0` to `S`,
\[
\begin{aligned}
w(\rho+S/2,\theta,s+S)-w(\rho,\theta,s)
={}&
\int_0^S
 e^{-2(\rho+\tau/2)}
 \mathcal N[w](\rho+\tau/2,\theta,s+\tau)
 d\tau\\
={}&
e^{-2\rho}
\int_0^S e^{-\tau}
\mathcal N[w](\rho+\tau/2,\theta,s+\tau)d\tau.
\end{aligned}
\]
Because the full Leray solution is `S`-periodic,
\[
w(\rho,\theta,s+S)=w(\rho,\theta,s).
\]
Hence
\[
\boxed{
w(\rho+S/2,\theta,s)-w(\rho,\theta,s)
=e^{-2\rho}\mathcal R_S(\rho,\theta,s),
}
\]
where `R_S` is uniformly bounded in the rescaled annular `H^{-1}` topology.

Therefore
\[
\boxed{
w(\rho+S/2,s)-w(\rho,s)=O(e^{-2\rho}).
}
\]
Equivalently, with `R=e^rho`, the critical amplitude is log-periodic up to an `O(R^{-2})` correction.

Since `U=R^{-1}w`, the velocity correction is of order
\[
\boxed{O(R^{-3})}
\]
relative to the leading `R^{-1}` tail in the same weak annular topology.

**Status: PROVED.**

---

## 4. Physical interpretation of the characteristic coordinate

For standard backward Leray variables centered at the candidate singular point `X_*`,
\[
s=-\log(T^*-t),
\qquad
Y=\frac{x-X_*}{\sqrt{T^*-t}},
\qquad
U(Y,s)=\sqrt{T^*-t}\,u(x,t)
\]
(up to the fixed viscosity convention used elsewhere in the repository).

Then
\[
\rho
=\log|Y|
=\log|x-X_*|+\frac{s}{2},
\]
so the characteristic invariant is
\[
\boxed{
\eta:=\rho-\frac{s}{2}
=\log|x-X_*|.
}
\]
Thus an exact leading linear tail
\[
w(\rho,\theta,s)=F(\theta,\rho-s/2)
\]
corresponds in physical variables to
\[
\boxed{
u_{lead}(x,t)
=\frac1{|x-X_*|}
F\!\left(
\widehat{x-X_*},
\log|x-X_*|
\right).
}
\]
The leading passive Leray conveyor is therefore **time independent in physical coordinates**: the apparent outward drift in similarity coordinates is the coordinate representation of a fixed critical spatial trace near the singular point.

For a period-`S` Leray tail, `F` is periodic in its logarithmic radial variable with period `S/2`.  Equivalently, with
\[
\lambda=e^{S/2},
\]
\[
\boxed{
u_{lead}(X_*+\lambda x)
=\lambda^{-1}u_{lead}(X_*+x).
}
\]
Thus the physical leading trace is discretely homogeneous of degree `-1`.

---

## 5. Function-space location of the physical trace

A nonzero degree-`-1` velocity trace in three dimensions has the critical local behavior
\[
|u_{lead}(x)|\sim |x-X_*|^{-1}.
\]
Hence near the singular point,
\[
\boxed{
u_{lead}\in L^{3,\infty}_{loc}\setminus L^3_{loc},
}
\]
while its vorticity has degree `-2`,
\[
\boxed{
\omega_{lead}\in L^{3/2,\infty}_{loc}\setminus L^{3/2}_{loc}.
}
\]
The local kinetic energy is nevertheless finite because
\[
\int_0^{r_0}r^2r^{-2}dr<\infty.
\]
Thus finite physical energy does not remove this final-time trace.

---

## 6. Important anti-proof: the leading trace need not solve stationary Navier-Stokes

The leading physical trace is time independent, so it is tempting to insert it into the stationary Navier-Stokes equation and invoke a stationary Liouville theorem.  This is not justified.

The periodic tail has the expansion, schematically,
\[
U(Y,s)
=R^{-1}F(\eta,\theta)
+R^{-3}G(\eta,\theta,s)
+\cdots.
\]
Under the physical inverse transform, the correction behaves at fixed physical radius `r=|x-X_*|` as
\[
(T^*-t)^{-1/2}R^{-3}
\asymp
\frac{T^*-t}{r^3}.
\]
Although this correction itself tends to zero as `t->T*` for fixed `r>0`, its time derivative is order
\[
\boxed{r^{-3}},
\]
which is exactly the same order as
\[
u_{lead}\cdot\nabla u_{lead},
\qquad
\nu\Delta u_{lead},
\qquad
\nabla p_{lead}.
\]
Therefore a vanishing `O(T^*-t)` correction can carry an order-one-in-the-stationary-balance time derivative and cancel the nonlinear/viscous residual of the leading `1/r` trace.

Equivalently, in log-Leray variables the right-hand side is `e^{-2rho}N[w]`: it is nonresonant and produces the `R^{-2}` amplitude correction rather than imposing `N[F]=0` on the leading profile.

Hence
\[
\boxed{
\text{time-independent leading critical trace}
\not\Rightarrow
\text{stationary Navier-Stokes profile}.
}
\]

**Status: ANTI-PROOF PROVED.**

---

## 7. Consequence for long-period DSS rigidity

The periodic W1 branch is now sharper:
\[
\boxed{
\begin{gathered}
\text{nonzero recurrent inner core},\\
+\text{physical critical }1/r\text{ trace},\\
+\text{log-periodic spatial phase with factor }\lambda=e^{S/2},\\
+\text{Leray correction of relative order }R^{-2}.
\end{gathered}
}
\]

The leading trace cannot be excluded by strong-L3 theorems, finite energy, or stationary-profile Liouville theorems.  A successful rigidity theorem must control the **core/trace interface or the nonresonant correction dynamics**, not merely classify the leading tail.

---

## 8. Current next target

The most direct remaining route is to quantify the interface injection needed to maintain a positive-density family of occupied critical shells while the far tail self-interaction is only `O(R^{-2})`.

A desired lemma would have the form
\[
\boxed{
\text{positive-density critical trace replenishment}
\Longrightarrow
\text{positive-frequency finite-radius }H/T/\text{projective action}.
}
\]

The repository already has positive-frequency replacement/export and finite multiflux capacity results; the missing step is to identify the asymptotic log-periodic trace cohorts with those finite-radius injections without losing their critical shell mass.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
