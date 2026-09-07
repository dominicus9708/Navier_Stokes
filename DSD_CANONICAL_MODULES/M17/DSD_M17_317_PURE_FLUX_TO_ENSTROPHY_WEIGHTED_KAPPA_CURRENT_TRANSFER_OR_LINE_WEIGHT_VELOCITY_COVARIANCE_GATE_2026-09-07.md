# DSD M17-317 — Pure-flux `kappa` current transfers to the enstrophy current or forces line-weight/material-velocity covariance

Date: 2026-09-07  
Canonical ID: **M17-317**

Status: **MEASURE-MISMATCH QUANTIFICATION / M17-314 PRODUCES A FIXED NEGATIVE PURE MATERIAL-FLUX CURRENT THROUGH `kappa=0`, WHILE M5-683/688 USE THE ENSTROPHY-WEIGHTED CURRENT. M5-683 ALREADY IDENTIFIES THE EXACT LINE WEIGHT `w_lambda=int chi(rho) rho ds` RELATING THE TWO MEASURES ON A REGULAR VORTEX-LINE FLOW BOX, AND M17-313 SUPPLIES THE MISSING EXPLICIT PROOF THAT `kappa` AND `h=D_B kappa` ARE LINE-CONSTANT. THE PRESENT MODULE DOES NOT IDENTIFY THE TWO CURRENTS. IN A MOLLIFIED ZERO BAND, `J_E=bar w J_Phi+Cov(w,h)`. IF THE PURE-FLUX CURRENT IS UNIFORMLY NEGATIVE AND `w` HAS A POSITIVE LOWER BOUND, THEN EITHER A FIXED NEGATIVE ENSTROPHY CURRENT TRANSFERS TO M5-683 OR THE LINE WEIGHT AND MATERIAL KAPPA VELOCITY HAVE A FIXED NONZERO COVARIANCE. CAUCHY--SCHWARZ TURNS FAILURE OF CURRENT TRANSFER INTO A QUANTITATIVE WEIGHT-DISPERSION / `h^2`-ACTIVITY GATE. THIS REMOVES THE ABSTRACT MEASURE MISMATCH AS AN UNTYPED ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Two exact currents

Let `lambda` be a retained material vortex-line/tube label with current oriented flux measure

\[
d\Phi_\theta(\lambda).
\]

M5-681 defines the pure material-flux distribution/current

\[
F_\Phi(k,\theta)
:=
\int\delta(k-\kappa_\lambda)d\Phi_\theta,
\]

\[
G_\Phi(k,\theta)
:=
\int h_\lambda
\delta(k-\kappa_\lambda)d\Phi_\theta,
\qquad
h_\lambda:=D_B\kappa_\lambda.
\]

M5-683 defines instead the high-amplitude enstrophy-weighted objects

\[
F_E^\chi(k,\theta)
:=
\int\delta(k-\kappa)
\chi(\rho)\rho^2dy,
\]

\[
G_E^\chi(k,\theta)
:=
\int h\delta(k-\kappa)
\chi(\rho)\rho^2dy.
\]

They are not the same measure.

---

## 2. Exact line weight

In a regular vortex-line flow box,

\[
\boxed{
dy=\frac{d\Phi_\theta\,ds}{\rho}.}
\]

M17-313 proves

\[
D_\xi\kappa=0,
\qquad
D_\xi h=0,
\]

so `kappa_lambda` and `h_lambda` are constant along each connected retained line segment.

Define the positive cutoff line weight

\[
\boxed{
w_\lambda(\theta)
:=
\int_{\Gamma_\lambda(\theta)}
\chi(\rho)\rho\,ds.
}
\]

Then exactly

\[
\boxed{
F_E^\chi(k,\theta)
=
\int
w_\lambda
\delta(k-\kappa_\lambda)
\,d\Phi_\theta,
}
\]

and

\[
\boxed{
G_E^\chi(k,\theta)
=
\int
w_\lambda h_\lambda
\delta(k-\kappa_\lambda)
\,d\Phi_\theta.
}
\]

Thus the entire measure mismatch is encoded by one line weight `w_lambda`.

---

## 3. Use a mollified zero band

A point value at `k=0` can hide regularity assumptions on the pushed-forward densities.

Choose a fixed nonnegative smooth mollifier

\[
\psi\in C_c^\infty((-1,1)),
\qquad
\int\psi=1,
\]

and define

\[
\boxed{
\psi_\delta(k)
:=\delta^{-1}\psi(k/\delta).
}
\]

For the recurrent space-time/label mean define the zero-band measure

\[
\boxed{
d\nu_\delta
:=
\psi_\delta(\kappa_\lambda(\theta))
\,d\Phi_\theta(\lambda)\,d\mathfrak t(\theta),}
\]

where `d mathfrak t` denotes the normalized invariant/recurrent time measure.

Set

\[
M_\delta:=\int d\nu_\delta.
\]

Define the mollified pure-flux and enstrophy currents

\[
\boxed{
J_\Phi^\delta
:=
\int h\,d\nu_\delta,
}
\]

and

\[
\boxed{
J_E^\delta
:=
\int wh\,d\nu_\delta.
}
\]

Equivalently,

\[
J_\Phi^\delta
=
\int\psi_\delta(k)\overline G_\Phi(k)dk,
\]

\[
J_E^\delta
=
\int\psi_\delta(k)\overline G_E^\chi(k)dk.
\]

This formulation remains meaningful even if pointwise current densities are not smooth at zero.

---

## 4. Quantitative pure-current input

M17-314 gives on its bounded-length high-amplitude branch

\[
\overline G_\Phi(0)
\le-d_{flux}<0.
\]

For a pointwise-continuous current this implies, for all sufficiently small fixed `delta`,

\[
\boxed{
J_\Phi^\delta
\le-\frac34d_{flux}.
}
\]

More generally, without assuming continuity, the present module may be entered on any sequence `delta_n->0` satisfying the weaker band input

\[
\boxed{
J_\Phi^{\delta_n}\le-d_0<0.
}
\]

The latter is the DSD-safe hypothesis used below.

---

## 5. Compact line-weight corridor

Assume on the retained band population

\[
\boxed{
0<w_*\le w_\lambda\le w^*<\infty.}
\]

A positive lower bound follows on a uniformly high-amplitude line segment with a positive capture-length floor.

A finite upper bound follows on the bounded-capture-length compact-amplitude branch.

Failure is exported as

\[
\boxed{
G_{line\ weight\ degeneration/decompactification}.
}
\]

Define the zero-band mean line weight

\[
\boxed{
\bar w_\delta
:=
\frac1{M_\delta}
\int w\,d\nu_\delta
}
\]

when `M_delta>0`.

Then

\[
\boxed{w_*\le\bar w_\delta\le w^*.}
\]

---

## 6. Exact current decomposition

Write

\[
w
=\bar w_\delta+(w-\bar w_\delta).
\]

Then

\[
\begin{aligned}
J_E^\delta
&=
\int wh\,d\nu_\delta\\
&=
\bar w_\delta
\int h\,d\nu_\delta
+
\int(w-\bar w_\delta)h\,d\nu_\delta.
\end{aligned}
\]

Therefore

\[
\boxed{
J_E^\delta
=
\bar w_\delta J_\Phi^\delta
+\mathcal C_{wh}^\delta,
}
\]

where

\[
\boxed{
\mathcal C_{wh}^\delta
:=
\int(w-\bar w_\delta)h\,d\nu_\delta.
}
\]

This is an exact identity.

---

## 7. Current transfer or covariance

Assume

\[
J_\Phi^\delta\le-d_0<0.
\]

Then

\[
\bar w_\delta J_\Phi^\delta
\le-w_*d_0.
\]

Hence either

\[
\boxed{
J_E^\delta
\le-rac12w_*d_0
}
\]

or necessarily

\[
\boxed{
\mathcal C_{wh}^\delta
\ge\frac12w_*d_0.
}
\]

Thus failure of the negative current to transfer into the M5-683 measure requires a **positive correlation between line weight and material `kappa` velocity** large enough to cancel at least half of the pure-flux current.

---

## 8. Cauchy--Schwarz factorization of the covariance escape

Define

\[
\boxed{
V_w^\delta
:=
\int|w-\bar w_\delta|^2d\nu_\delta,
}
\]

and

\[
\boxed{
H_h^\delta
:=
\int|h|^2d\nu_\delta.
}
\]

Cauchy--Schwarz gives

\[
\boxed{
|\mathcal C_{wh}^\delta|
\le
(V_w^\delta H_h^\delta)^{1/2}.
}
\]

Therefore on the non-transfer branch,

\[
\boxed{
V_w^\delta H_h^\delta
\ge
\frac14w_*^2d_0^2.
}
\]

For any chosen threshold `v_0>0`, this yields the explicit dichotomy

\[
\boxed{
V_w^\delta\ge v_0
\quad\lor\quad
H_h^\delta
\ge
\frac{w_*^2d_0^2}{4v_0}.
}
\]

Thus the measure mismatch is no longer an untyped escape.

It is either strong line-weight dispersion or strong material multiplier-speed activity near the zero level.

---

## 9. If line weights are asymptotically coherent, the current transfers

Suppose along the recurrent zero-band sequence

\[
V_w^{\delta_n}\to0
\]

and `H_h^(delta_n)` remains uniformly bounded.

Then

\[
\mathcal C_{wh}^{\delta_n}\to0.
\]

Hence the exact decomposition gives

\[
\boxed{
J_E^{\delta_n}
\le
-w_*d_0+o(1)<0.
}
\]

Thus **weight coherence closes the measure mismatch** and passes a fixed negative current directly into the M5-683 constitutive law.

---

## 10. If the current does not transfer, a new dynamical payer is forced

On the covariance branch, one has

\[
\boxed{
V_w^\delta H_h^\delta
\gtrsim1.
}
\]

The two factors have concrete meanings:

- `V_w`: dispersion of the high-amplitude enstrophy-per-flux line weight among near-zero multiplier labels;
- `H_h`: squared material speed with which those labels move through `kappa`-space.

The next target is to derive the material law for `w_lambda` and decide whether persistent large covariance itself requires strain, cutoff/nodal flux, or boundary/line-replacement work.

---

## 11. Relation to M5-683

M5-683 already states the exact constitutive identity

\[
\boxed{
G_E^\chi
=
\partial_k(A_{\kappa\kappa}+A_{\kappa\sigma})
-kF_E^\chi
+\mathcal R_\chi.
}
\]

At the zero level, the drift term `-kF_E` vanishes formally.

Therefore on the current-transfer branch the fixed negative band current must be supplied by the variation of the **transverse** diffusion/mixed-strain profile or by the explicit remainder.

M17-316 ensures no longitudinal `D_xi kappa` recharge is available.

---

## 12. DSD audit

- Pure-flux and enstrophy-weighted currents are never identified directly.
- The exact line weight from M5-683 is retained.
- A mollified zero band avoids silently assuming a smooth density at `k=0`.
- Pointwise M17-314 current is used only with continuity, otherwise a band-current hypothesis is explicit.
- Failure of sign transfer is quantified as covariance, not called arbitrary cancellation.
- Covariance is split into line-weight variance and `h^2` activity.
- No global finite budget for either factor is assumed.
- No external theorem is used.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
