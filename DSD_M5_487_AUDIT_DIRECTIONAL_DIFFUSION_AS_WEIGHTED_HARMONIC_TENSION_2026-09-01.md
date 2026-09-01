# DSD M5-487 — Audit directional diffusion as weighted harmonic-map tension

Date: 2026-09-01

Status: **R2 SCOPE CORRECTION / THE PROJECTED DIFFUSION TERM IN THE VORTICITY-DIRECTION EQUATION IS NOT POINTWISE COERCIVE AGAINST `rho^2 |grad xi|^2`; IT IS THE WEIGHTED HARMONIC-MAP TENSION `D_xi = rho^-2 (I-xi⊗xi) div(rho^2 grad xi)` / NONTRIVIAL DIRECTION GRADIENT CAN HAVE ZERO PROJECTED DIFFUSION, SO M5-486 TARGET R2 CANNOT IDENTIFY DIRECTIONAL-DIFFUSION ACTION WITH DIRECTION DIRICHLET DISSIPATION / HOWEVER ON THE ACTIVE ANALYTIC CARRIER, ORDER-ONE MATERIAL DIRECTIONAL-DIFFUSION ACTION DOES FORCE A FIXED LOCAL SPACETIME WEIGHTED-TENSION L2 CHARGE / POSITIVE-DENSITY RATCHET THEREFORE SPLITS INTO A POSITIVE-DENSITY TILT CHARGE OR A POSITIVE-DENSITY WEIGHTED-TENSION CHARGE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity-direction equation

Use the M5-486 similarity vorticity

\[
W=\rho\xi,
\qquad
\rho=|W|,
\qquad
|\xi|=1
\]

on the active set `rho>0`.

Let

\[
\mathcal L
:=
\partial_\theta
+U\cdot\nabla
+\frac12 y\cdot\nabla.
\]

The similarity vorticity equation is

\[
\mathcal LW+W
=\Sigma W+\Delta W.
\]

Decompose

\[
\Sigma\xi
=\sigma\xi+\tau,
\qquad
\tau=(I-\xi\otimes\xi)\Sigma\xi.
\]

Projecting perpendicular to `xi` gives

\[
\boxed{
\mathcal L\xi
=\tau+\mathcal D_\xi,
}
\]

where

\[
\boxed{
\mathcal D_\xi
:=
\frac1\rho
(I-\xi\otimes\xi)\Delta W.
}
\]

This is the exact similarity version of the material-axis fork used in M5-471--485.

---

## 2. Exact decomposition of the projected diffusion term

Since

\[
\Delta(\rho\xi)
=
\xi\Delta\rho
+2\nabla\rho\cdot\nabla\xi
+\rho\Delta\xi,
\]

and

\[
\xi\cdot\Delta\xi
=-|\nabla\xi|^2,
\]

we obtain

\[
\boxed{
\mathcal D_\xi
=
2\nabla\log\rho\cdot\nabla\xi
+
\Delta\xi
+
|\nabla\xi|^2\xi.
}
\]

Equivalently,

\[
\boxed{
\mathcal D_\xi
=
\rho^{-2}
(I-\xi\otimes\xi)
\nabla\cdot(\rho^2\nabla\xi).
}
\]

Thus `mathcal D_xi` is a weighted harmonic-map tension field into `S^2`.

It measures failure of the direction field to be weighted-harmonic; it is not the direction gradient itself.

---

## 3. Anti-coercivity firewall

A direct estimate of the form

\[
|\mathcal D_\xi|
\ge c|\nabla\xi|^2
\]

or

\[
\rho^2|\mathcal D_\xi|^2
\ge c\rho^2|\nabla\xi|^2
\]

cannot hold pointwise in general.

Take locally

\[
\rho\equiv1,
\qquad
\xi(z)
=(\cos kz,\sin kz,0).
\]

Then

\[
|\nabla\xi|^2=k^2>0,
\]

while

\[
\Delta\xi=-k^2\xi.
\]

Therefore

\[
\boxed{
\mathcal D_\xi
=(I-\xi\otimes\xi)\Delta\xi=0.
}
\]

The corresponding local vorticity field

\[
W=(\cos kz,\sin kz,0)
\]

is divergence free.

This is only a local algebraic witness, not an ancient finite-enstrophy Navier--Stokes solution, but it is sufficient to invalidate any purely pointwise coercive identification of projected diffusion with direction Dirichlet density.

Hence M5-486 target R2 must be corrected.

---

## 4. What the direction Dirichlet part actually is

M5-486 already gives

\[
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
\]

Thus the orientation part of palinstrophy is

\[
\boxed{
P_{dir}
:=
\int\rho^2|\nabla\xi|^2dy.
}
\]

By contrast, the natural projected-diffusion tension ledger is

\[
\boxed{
T_{dir}
:=
\int\rho^2|\mathcal D_\xi|^2dy.
}
\]

These are different differential orders and neither controls the other without additional structure.

`P_dir` is first-order orientation roughness.

`T_dir` is a weighted second-order tension defect.

---

## 5. Active-carrier hypotheses inherited from the bounded lane

On each retained M5-471 ratchet interval, the marked material trajectory remains in an active carrier with

\[
\rho(Y(\theta),\theta)\ge\eta>0.
\]

The bounded/no-frequency-defect analytic corridor supplies fixed local derivative bounds on the normalized cell. In particular, after restricting to a fixed compact carrier window, there are constants

\[
M_0,M_1<\infty
\]

such that

\[
|\mathcal D_\xi|\le M_0,
\qquad
|\nabla\mathcal D_\xi|\le M_1,
\]

and a fixed spatial derivative bound for `rho`.

If these bounds fail along the selected sequence, the process is already routed to the strong relative-frequency/derivative branch and is not part of the compact endpoint.

---

## 6. From trajectory action to positive-time threshold occupancy

Suppose the directional-diffusion part of one ratchet event satisfies

\[
\boxed{
\int_J
|\mathcal D_\xi(Y(\theta),\theta)|d\theta
\ge\delta_d>0,
}
\]

with

\[
|J|\le L_*.
\]

Set

\[
h_*:=\frac{\delta_d}{2L_*}.
\]

Let

\[
E_*:=
\{\theta\in J:
|\mathcal D_\xi(Y(\theta),\theta)|\ge h_*\}.
\]

Using `|mathcal D_xi|<=M_0`,

\[
\delta_d
\le
h_*L_*
+M_0|E_*|.
\]

Hence

\[
\boxed{
|E_*|
\ge
\frac{\delta_d}{2M_0}>0.
}
\]

Thus order-one `L1` trajectory action forces a fixed positive amount of normalized time on which the tension amplitude exceeds a fixed threshold.

---

## 7. Spatial thickening of the tension event

For every `theta in E_*`, the Lipschitz bound gives

\[
|\mathcal D_\xi(y,\theta)|
\ge\frac{h_*}{2}
\]

throughout

\[
B_r(Y(\theta)),
\qquad
r:=\min\left\{r_0,\frac{h_*}{2M_1}\right\},
\]

for a fixed carrier radius `r_0`.

The active-vorticity lower bound and the derivative bound for `rho` allow `r` to be reduced, if necessary, so that

\[
\rho(y,\theta)
\ge\frac\eta2
\]

on the same ball.

Therefore

\[
\int_{B_r(Y(\theta))}
\rho^2|\mathcal D_\xi|^2dy
\ge
c\eta^2h_*^2r^3.
\]

Integrating over `E_*`,

\[
\boxed{
\int_J\int_{B_r(Y(\theta))}
\rho^2|\mathcal D_\xi|^2dy\,d\theta
\ge c_d>0,
}
\]

where `c_d` depends only on the retained compact-corridor constants and the ratchet threshold.

Thus:

\[
\boxed{
\text{order-one material directional-diffusion action}
\Longrightarrow
\text{fixed local spacetime weighted-tension L2 charge}.
}
\]

This implication is legitimate on the analytic/no-frequency-defect branch.

---

## 8. Tilt branch has an analogous thickened charge

If instead

\[
\int_J|\tau(Y(\theta),\theta)|d\theta
\ge\delta_t>0,
\]

then the same bounded-derivative thickening argument gives

\[
\boxed{
\int_J\int_{B_r(Y(\theta))}
\rho^2|\tau|^2dy\,d\theta
\ge c_t>0.
}
\]

The factor `rho^2` is harmless on the active carrier because `rho>=eta/2` there.

Thus both pieces of the projective ratchet fork can be converted from one-trajectory action into a genuine local spacetime charge.

---

## 9. Positive-density ratchet splits into two positive-density subchannels

Each retained M5-471 event satisfies schematically

\[
\int_J|\tau|d\theta
+
\int_J|\mathcal D_\xi|d\theta
\ge\delta_0.
\]

Hence every event belongs to at least one of

\[
A_{tilt}:\quad
\int_J|\tau|d\theta\ge\delta_0/2,
\]

or

\[
A_{diff}:\quad
\int_J|\mathcal D_\xi|d\theta\ge\delta_0/2.
\]

Since the union occurs with positive generation density, at least one subchannel has positive lower/Banach density along an extracted sequence.

Applying the M5-485 invariant-hull construction yields an invariant component satisfying either

\[
\boxed{
\langle C_{tilt}\rangle>0
}
\]

or

\[
\boxed{
\langle C_{tension}\rangle>0,
}
\]

where the charges are the thickened local spacetime `rho^2 |tau|^2` and `rho^2 |mathcal D_xi|^2` observables over one generation cell.

---

## 10. Relation to the M5-486 axial channel

M5-486 independently proved

\[
\boxed{
\langle Q\rangle
=
\frac14\langle E\rangle
+
\langle P\rangle
>0.
}
\]

Therefore every surviving compact marked invariant component must carry

\[
\boxed{
\text{positive mean axial stretching}
+
\left(
\text{positive mean thickened tilt}
\ \lor\
\text{positive mean weighted tension}
\right).
}
\]

This is sharper than the previous informal two-channel description because the projective branch is now represented by actual spacetime observables rather than only one-dimensional trajectory variation.

---

## 11. Why this still does not close the hull

No globally finite similarity-time ledger for

\[
\int\rho^2|\mathcal D_\xi|^2
\]

has been proved.

Likewise the similarity flow may recurrently regenerate direction gradients and weighted tension through strain and advection.

Therefore positive invariant mean tension charge is not by itself a contradiction.

The correct conclusion is not

\[
A_{diff}\Rightarrow P_{dir}\text{ diverges},
\]

but rather

\[
\boxed{
A_{diff}^{dens}
\Rightarrow
\text{recurrent weighted-tension production}.
}
\]

---

## 12. Literature firewall

Classical geometric regularity theory, beginning with Constantin--Fefferman type vorticity-direction criteria and later refinements, shows that sufficient coherence of the vorticity direction can deplete stretching and imply regularity.

Those results control spatial direction coherence/Hölder behavior or related geometric quantities; they do not identify the projected Laplacian tension `mathcal D_xi` with `|grad xi|^2`.

The M5-487 anti-coercivity correction is therefore consistent with the known geometric picture: direction roughness and projected diffusion tension are related but distinct descriptors.

---

## 13. Corrected R2 output

M5-486 target R2 is replaced by

\[
\boxed{
R2^*:\quad
\text{directional-diffusion ratchet}
\Longrightarrow
\text{positive recurrent weighted-tension charge},
}
\]

not by a direct lower bound on orientation Dirichlet energy.

The next high-value step is to combine this corrected charge with the finite-memory material-flux genealogy of M5-393--397 and M5-455--456.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
