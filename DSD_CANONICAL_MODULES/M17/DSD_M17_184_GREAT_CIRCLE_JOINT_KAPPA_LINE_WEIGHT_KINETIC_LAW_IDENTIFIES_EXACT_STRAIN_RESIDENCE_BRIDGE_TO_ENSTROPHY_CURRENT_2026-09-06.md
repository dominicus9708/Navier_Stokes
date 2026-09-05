# DSD M17-184 — Great-circle joint `(kappa,L_rho)` kinetics identifies the exact strain-residence bridge from flux current to enstrophy current

Date: 2026-09-06  
Canonical ID: **M17-184**

Status: **REGULAR M5 CONVEYOR / LINE-WEIGHT KINETIC LIFT / M17-179 IDENTIFIES THE REGULAR GREAT-CIRCLE CURRENT FLUX MEASURE WITH `dq dx_3`. M5-684 IDENTIFIES THE ENSTROPHY LINE WEIGHT `L_rho=int_Gamma rho ds` AND ITS MATERIAL LAW `L_rho'=(kappa-1/2+2 sigma_bar_rho)L_rho`. LIFTING THE CURRENT FLUX POPULATION TO THE JOINT STATE `(kappa,L_rho)` GIVES THE EXACT KINETIC EQUATION `partial_theta P+partial_k G_k+partial_l G_l=kP`. ITS FIRST `L_rho` MOMENT IS `partial_theta F_E+partial_k G_E=(2k-1/2)F_E+2S_rho`, WHERE `S_rho` IS THE `rho`-WEIGHTED LINE-STRAIN MOMENT. THUS THE M5-681 PURE-FLUX CONVEYOR AND M5-683 ENSTROPHY-WEIGHTED PDE CURRENT DIFFER BY ONE EXPLICIT STRAIN-RESIDENCE CHANNEL, NOT AN UNDEFINED MEASURE ERROR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Great-circle regular line geometry

On the regular Rank-1 great-circle branch,

\[
W=(J\nabla_hq,0).
\]

A connected vortex line lies at fixed

\[
q=\text{const},
\qquad
x_3=\text{const}.
\]

For a closed regular component `Gamma_(q,z)`,

\[
\rho=|W|=|\nabla_hq|.
\]

Define the enstrophy line weight

\[
\boxed{
L_\rho(q,z,\theta)
:=\oint_{\Gamma_{q,z}(\theta)}\rho\,ds
=\oint_{\Gamma_{q,z}(\theta)}|\nabla_hq|\,ds.
}
\]

By M17-179, the current transverse flux measure on regular labels is

\[
\boxed{d\Phi=dq\,dz.}
\]

---

## 2. Exact material law for the line weight

M5-684 gives for a material vortex-line segment

\[
\boxed{
L_\rho'
=\left(\kappa-\frac12\right)L_\rho
+2S_\rho^{line},
}
\]

where

\[
S_\rho^{line}
:=\oint_\Gamma\sigma\rho\,ds.
\]

Define

\[
\boxed{
\bar\sigma_\rho
:=\frac{S_\rho^{line}}{L_\rho}.
}
\]

Then

\[
\boxed{
L_\rho'
=\alpha L_\rho,
\qquad
\alpha:=\kappa-\frac12+2\bar\sigma_\rho.
}
\]

The current transverse flux itself obeys

\[
\boxed{d\Phi'=\kappa d\Phi.}
\]

---

## 3. Joint state-space distribution

Let `ell` denote the positive scalar state `L_rho`.

Define the joint distribution with respect to the **current flux measure**:

\[
\boxed{
P(k,\ell,\theta)
:=\int
\delta(k-\kappa_\lambda)
\delta(\ell-L_{\rho,\lambda})
\,d\Phi_\lambda.
}
\]

Define the two state-space currents

\[
\boxed{
G_k(k,\ell,\theta)
:=\int
h_\lambda
\delta(k-\kappa_\lambda)
\delta(\ell-L_{\rho,\lambda})
\,d\Phi_\lambda,
}
\]

and

\[
\boxed{
G_\ell(k,\ell,\theta)
:=\int
\alpha_\lambda L_{\rho,\lambda}
\delta(k-\kappa_\lambda)
\delta(\ell-L_{\rho,\lambda})
\,d\Phi_\lambda.
}
\]

---

## 4. Exact joint kinetic equation

For a smooth test function `psi(k,ell)`, material differentiation gives three contributions:

1. motion in `kappa` with velocity `h`;
2. motion in `L_rho` with velocity `alpha L_rho`;
3. growth of the current flux measure with rate `kappa`.

Therefore

\[
\boxed{
\partial_\theta P
+\partial_kG_k
+\partial_\ell G_\ell
=kP.
}
\]

This is the two-state lift of M5-681.

Integrating over `ell` recovers

\[
\partial_\theta F_\Phi+\partial_kG_\Phi=kF_\Phi.
\]

---

## 5. First line-weight moment

Define

\[
\boxed{
F_E(k,\theta)
:=\int_0^\infty \ell P(k,\ell,\theta)d\ell.
}
\]

By the flow-box identity `rho^2 dy=rho ds dPhi`, this is exactly the enstrophy-weighted `kappa` distribution on the retained regular line family.

Similarly define

\[
\boxed{
G_E(k,\theta)
:=\int_0^\infty \ell G_k(k,\ell,\theta)d\ell.
}
\]

This is the enstrophy-weighted material `kappa` current.

Multiply the joint kinetic equation by `ell` and integrate.
The `ell`-transport term gives

\[
\int_0^\infty
\ell\partial_\ell G_\ell d\ell
=-\int_0^\infty G_\ell d\ell
\]

under the no-through-boundary convention in the positive `ell` state.

Therefore

\[
\partial_\theta F_E+\partial_kG_E
=kF_E+\int G_\ell d\ell.
\]

---

## 6. Exact strain-residence source

At fixed `k`,

\[
\int G_\ell d\ell
=\int
\left(k-\frac12+2\bar\sigma_\rho\right)
L_\rho\delta(k-\kappa)d\Phi.
\]

Define

\[
\boxed{
S_\rho(k,\theta)
:=\int
\bar\sigma_\rho
L_\rho
\delta(k-\kappa)d\Phi.
}
\]

Then

\[
\boxed{
\int G_\ell d\ell
=\left(k-\frac12\right)F_E+2S_\rho.
}
\]

Hence the exact first-moment equation is

\[
\boxed{
\partial_\theta F_E
+\partial_kG_E
=\left(2k-\frac12\right)F_E
+2S_\rho.
}
\]

---

## 7. Recurrent stationary form

On a recurrent retained ensemble,

\[
\boxed{
\partial_k\overline G_E(k)
=\left(2k-\frac12\right)\overline F_E(k)
+2\overline S_\rho(k).
}
\]

If the `k` support is compact and `G_E` vanishes beyond the support, then

\[
\boxed{
\overline G_E(0)
=-\int_0^{K_*}
\left[
\left(2k-\frac12\right)\overline F_E(k)
+2\overline S_\rho(k)
\right]dk.
}
\]

Thus the enstrophy-current sign at zero is governed by a precise competition between multiplier residence and line strain.

---

## 8. Combine with the M5-683 PDE constitutive identity

On the high-amplitude region where the cutoff is identically one, M5-683 gives schematically

\[
\boxed{
G_E(k)
=\partial_k\left(A_{\kappa\kappa}+A_{\kappa\sigma}\right)
-kF_E(k)
+\mathcal R(k).
}
\]

Therefore at `k=0`, the stationary line-residence balance gives

\[
\boxed{
\partial_k\overline{\left(A_{\kappa\kappa}+A_{\kappa\sigma}\right)}(0)
+\overline{\mathcal R}(0)
=-\int_0^{K_*}
\left[
\left(2k-\frac12\right)\overline F_E
+2\overline S_\rho
\right]dk.
}
\]

This is an exact bridge between

1. `kappa`-space diffusion/mixed-gradient PDE architecture;
2. vortex-line strain-residence geometry.

It is stronger than merely saying the two measures differ.

---

## 9. Why no sign contradiction follows yet

The pure diffusion density

\[
A_{\kappa\kappa}\ge0
\]

is accompanied by

\[
A_{\kappa\sigma}
\]

with no fixed sign.

The new source

\[
S_\rho
\]

also has no fixed sign because `sigma` can change sign along the vortex line.

Therefore the joint kinetic lift does not make the current one-sign by itself.

The surviving regular conveyor requires a three-way correlation among

\[
\boxed{
\nabla\kappa,
\qquad
\nabla\sigma,
\qquad
\bar\sigma_\rho L_\rho.
}
\]

---

## 10. New high-value target

The next nonduplicate question is whether the great-circle strain-eigenline equations impose an independent identity on

\[
\bar\sigma_\rho
=\frac{\oint\sigma|\nabla_hq|ds}
{\oint|\nabla_hq|ds}
\]

for closed winding loops.

A sign or recurrence law for this weighted line strain would directly constrain the M5-683 measure bridge.

Blindly differentiating the constitutive law is lower value than attacking this geometric line average.

---

## 11. DSD audit

### Audit A — inventing a joint probability law
The joint measure is the actual current vorticity-flux measure lifted by two material observables.

### Audit B — forgetting flux-measure growth
The source `kP` is retained explicitly.

### Audit C — equating flux and enstrophy currents
Their difference is encoded in the `L_rho` moment and `S_rho` source.

### Audit D — sign of the mixed current
No sign is claimed.

### Audit E — proof status
The regular conveyor is more tightly coupled but remains open.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
