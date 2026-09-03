# DSD M5-678 — Late curvature-label activation requires exponentially small base flux and asymptotic kappa amplification rate at least 3/2

Date: 2026-09-03

Status: **INTERNAL LATE-ACTIVATION GATE / M5-677 FORCES A FIXED-STRENGTH CURVATURE PACKET AT EVERY RECURRENT CE-H STATE, WHILE M5-621 GIVES THE EXACT MATERIAL RATIO LAW `R=(rho|K|)/|phi|`, `R(theta)=R(theta0)e^{-3(theta-theta0)/2}` / THEREFORE A MATERIAL LABEL FIRST RETAINED AT A VERY LATE TIME MUST COME FROM AN EXPONENTIALLY SMALL BASE-SLICE FLUX ELEMENT AND MUST HAVE ACCUMULATED `int kappa >= (3/2) Delta theta - O(1)` TO REACH THE FIXED RETAINED FLUX THRESHOLD / THIS IDENTIFIES THE ONLY POSSIBLE INFINITE-REPLACEMENT MECHANISM AS A NESTED SMALL-FLUX POPULATION WITH CRITICAL 3/2 AMPLIFICATION / THE 3/2 RATE MATCHES THE SIMILARITY MATERIAL-VOLUME EXPANSION AND IS NOT BY ITSELF A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed curvature event thresholds

M5-677 gives uniform constants

\[
z_*>0,
\qquad
0<\phi_-\le\phi_+<\infty
\]

such that every retained curvature packet contains a material flux label at the event time `theta` satisfying

\[
\boxed{
Z_{curv}(\theta):=\rho|\mathcal K|(\theta)\ge z_*,
\qquad
\phi_-\le|\phi(\theta)|\le\phi_+.
}
\]

The compact all-order hull also gives

\[
\boxed{Z_{curv}(\tau)\le M_1}
\]

at every time on every active point/label while it is defined.

---

## 2. Strict material ratio law

M5-621 gives, for the same material vortex-tube label,

\[
R(\tau)
:=
\frac{Z_{curv}(\tau)}{|\phi(\tau)|},
\]

\[
\boxed{
R(\theta)
=R(\theta_0)
\exp\left[-\frac32(\theta-\theta_0)\right].
}
\]

At the retained event,

\[
R(\theta)
\ge
\frac{z_*}{\phi_+}.
\]

Therefore

\[
R(\theta_0)
\ge
\frac{z_*}{\phi_+}
\exp\left[\frac32(\theta-\theta_0)\right].
\]

---

## 3. Exponentially small base flux

At the base time,

\[
R(\theta_0)
=
\frac{Z_{curv}(\theta_0)}{|\phi(\theta_0)|}
\le
\frac{M_1}{|\phi(\theta_0)|}.
\]

Hence

\[
\frac{M_1}{|\phi(\theta_0)|}
\ge
\frac{z_*}{\phi_+}
\exp\left[\frac32(\theta-\theta_0)\right],
\]

so

\[
\boxed{
|\phi(\theta_0)|
\le
C_{base}
\exp\left[-\frac32(\theta-\theta_0)\right]
}
\]

with

\[
C_{base}:=\frac{M_1\phi_+}{z_*}.
\]

Thus very late curvature-active packets cannot originate from a fixed positive base-flux population.
They must come from successively smaller pieces of the fixed base transverse-flux resource of M5-647.

---

## 4. Required kappa amplification

The material flux law is

\[
\boxed{
\frac d{d\tau}\log|\phi|=\kappa.
}
\]

Therefore

\[
\int_{\theta_0}^{\theta}\kappa(\tau)d\tau
=
\log\frac{|\phi(\theta)|}{|\phi(\theta_0)|}.
\]

Using

\[
|\phi(\theta)|\ge\phi_-
\]

and the base-flux bound gives

\[
\boxed{
\int_{\theta_0}^{\theta}\kappa d\tau
\ge
\frac32(\theta-\theta_0)
-C_\kappa,
}
\]

where

\[
C_\kappa
:=
\log\frac{C_{base}}{\phi_-}.
\]

Consequently, for any sequence of first retained activations with

\[
\theta_j-\theta_0\to\infty,
\]

we have

\[
\boxed{
\liminf_{j\to\infty}
\frac{1}{\theta_j-\theta_0}
\int_{\theta_0}^{\theta_j}\kappa_j(\tau)d\tau
\ge\frac32.
}
\]

---

## 5. Why this is a real narrowing

M5-647 showed only that the total base transverse flux is finite.
A finite nonatomic measure can contain infinitely many smaller pieces.

M5-678 identifies exactly how small the base pieces must be if they are to become future fixed-strength curvature carriers:

\[
\boxed{
\phi_{0,j}\lesssim e^{-3\Delta\theta_j/2}.
}
\]

And it identifies the required compensating amplification:

\[
\boxed{
\langle\kappa\rangle_{[\theta_0,\theta_j]}
\gtrsim\frac32.
}
\]

Thus the last survivor is not arbitrary label turnover.
It is a **nested critical amplification cascade** in material flux space.

---

## 6. Relation to the material-volume exponent

A fixed positive material volume satisfies in similarity coordinates

\[
D_B\log dV=\frac32.
\]

Hence the backward preimage of a fixed-size event packet has volume

\[
dV(\theta_0)
=
dV(\theta)
\exp\left[-\frac32(\theta-\theta_0)\right].
\]

The exponent is exactly the same as the late-label base-flux estimate.

This equality is important for the audit:

\[
\boxed{
\text{the `3/2' late-activation rate is critical, not supercritical.}
}
\]

Therefore finite material volume and finite base flux do not by themselves contradict an infinite geometrically nested sequence.

---

## 7. Physical interpretation firewall

The similarity strict ratio in M5-621 should not be interpreted as a new physical dissipation without checking physical scaling.
The next audit explicitly performs that conversion.

At the present stage the valid conclusion is only:

\[
\boxed{
\text{arbitrarily late curvature activation}
\Longrightarrow
\text{exponentially small base flux + critical positive kappa amplification}.
}
\]

No contradiction is claimed here.

---

## 8. Updated target

The remaining cycle problem becomes:

\[
\boxed{
\text{Can CE-H elliptic dynamics }\Delta W=\kappa W
\text{ repeatedly amplify }e^{-3\theta/2}\text{-scale base flux populations}
\text{ into order-one curvature packets while the Eulerian hull remains smooth and recurrent?}
}
\]

This is narrower than the former arbitrary multi-sheet oscillator.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
