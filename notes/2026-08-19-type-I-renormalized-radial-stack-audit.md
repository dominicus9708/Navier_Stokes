# Type-I renormalized radial-stack audit

Date: 2026-08-19

Status: **EXTERNAL-BOUNDARY + INTERNAL-SCALING AUDIT. THE MINIMAL DYADIC CRITICAL PACKET STACK PRODUCES THE SAME LOGARITHMIC L3-CUBIC GROWTH SCALE THAT APPEARS IN QUANTITATIVE TYPE-I CONCENTRATION THEORY. THIS CONFIRMS THAT THE REMAINING STACK IS A GENUINE TYPE-I-CRITICAL ADVERSARY, NOT A SCALAR-BOUND ARTIFACT. GLOBAL REGULARITY NOT PROVED.**

## 1. Type-I renormalized variables

Suppose a surviving critical genealogy follows the natural Type-I frequency rate

\[
K(t)\asymp(T^*-t)^{-1/2}.
\]

Introduce

\[
\tau=-\log(T^*-t),
\qquad
y=\frac{x-x_*}{\sqrt{T^*-t}},
\qquad
V(y,\tau)=\sqrt{T^*-t}\,u(x,t).
\]

Then

\[
K(t)\asymp e^{\tau/2}.
\]

The rescaled velocity solves the Leray evolution

\[
\boxed{
\partial_\tau V
+\frac12V
+\frac12y\cdot\nabla V
+V\cdot\nabla V
=-\nabla P+\nu\Delta V,
\qquad\nabla\cdot V=0.
}
\]

The rescaled vorticity is

\[
\Omega=(T^*-t)\omega.
\]

## 2. Number of active octaves

If the compact cascade has built one order-one critical packet per dyadic octave from a fixed lower frequency `K0` up to the current natural frequency `K(t)`, then

\[
M(t)
\asymp
\log_2\frac{K(t)}{K_0}
\asymp
c\tau.
\]

Each packet carries

\[
\|u_j\|_3^3\asymp1
\]

and order-one H^(1/2) band charge.

For nested bounded-overlap packet annuli the cubic L3 mass therefore scales as

\[
\boxed{
\|u(t)\|_3^3\asymp M(t)
\asymp
\log\frac1{T^*-t}.
}
\]

Thus

\[
\boxed{
\|u(t)\|_3
\asymp
\left(\log\frac1{T^*-t}\right)^{1/3}
}
\]

for the kinematic minimal stack.

## 3. Renormalized interpretation of old bands

A physical packet at frequency

\[
K_j=K(t)/R
\]

has, in the terminal Type-I variables,

\[
|V_j|\sim R^{-1},
\qquad
|\Omega_j|\sim R^{-2},
\qquad
\text{spatial radius}\sim R.
\]

Its L3 charge remains order one:

\[
(R^{-1})^3R^3\sim1.
\]

Hence the simultaneous radial stack is a record of prior critical packets that, in renormalized variables, populate successively larger spatial scales with successively smaller amplitude but fixed critical cubic charge.

This is a large-scale non-tightness mechanism in the renormalized flow, distinct from the earlier large-R *order-one-vorticity coherent crossing* lane.

## 4. Comparison with quantitative Type-I concentration theory

Barker and Prange, *Quantitative Regularity for the Navier-Stokes Equations Via Spatial Concentration* (Commun. Math. Phys. 385 (2021), 717-792), prove quantitative concentration lower bounds under a Type-I `L_t^infinity L_x^{3,infinity}` bound.

For a fixed macroscopic radius their lower bound on local L3 cubic mass grows logarithmically in the ratio between that radius and the parabolic singular scale; in particular the time dependence contains

\[
\log\frac1{T^*-t}
\]

up to constants depending strongly on the Type-I bound.

Therefore the internal minimal stack law

\[
\|u(t)\|_3^3\asymp\log\frac1{T^*-t}
\]

lies exactly at the same qualitative logarithmic concentration scale.

## 5. General Type-I boundary

General Type-I behavior is not eliminated in 3D Navier-Stokes merely by the natural parabolic rate.  Albritton and Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems* (2018/2019), characterize local Type-I singularity formation through nontrivial bounded ancient solutions satisfying a Type-I decay condition.

Known nonexistence results close more rigid subclasses, including self-similar/asymptotically self-similar profiles under additional integrability/tightness assumptions, and axisymmetric Type-I scenarios under additional hypotheses.

Thus the present modulated radial-stack wall is consistent with the external frontier.

## 6. Consequence for the DSD proof route

The current cascade cannot be rejected merely because it has

- parabolic frequency growth `K~(T-t)^-1/2`;
- BKM action growing like `log K`;
- L3 cubic mass growing like `log K`;
- one critical H^(1/2) charge per active octave.

Those are precisely Type-I-critical rates.

The remaining useful DSD information is the extra organization already derived:

1. finite-range radial reproduction after affine subtraction;
2. exact I/V ancestry;
3. projective hysteresis switching cost;
4. signed-tube termination versus projective/L3 uncertainty;
5. heterochiral radial transfer;
6. Betchov/positive-middle-strain compensation;
7. shape-modulation / derivative-covariance forcing.

A successful final theorem must exploit incompatibility among these structures, not merely improve a Type-I power count.

Status: **MINIMAL STACK MATCHES KNOWN TYPE-I LOGARITHMIC CONCENTRATION SCALE / POWER-COUNTING ROUTE EXHAUSTED / REMAINING TARGET = RIGIDITY OF MODULATED TYPE-I ANCIENT RADIAL REPRODUCTION.**