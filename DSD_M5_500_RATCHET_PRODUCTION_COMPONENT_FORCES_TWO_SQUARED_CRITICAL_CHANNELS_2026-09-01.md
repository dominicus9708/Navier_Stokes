# DSD M5-500 — Ratchet-production component forces two recurrent squared critical channels

Date: 2026-09-01

Status: **RATCHET-COMPONENT SHARPENING / M5-499 SHOWS EVERY POSITIVE-RATCHET ERGODIC COMPONENT ALSO HAS STRICTLY POSITIVE MEAN AXIAL VORTEX-STRETCHING PRODUCTION / CAUCHY--SCHWARZ UPGRADES THIS TO A POSITIVE MEAN VORTICITY-WEIGHTED AXIAL-STRAIN-SQUARE CHARGE `int rho^2 sigma^2` / THE RATCHET ACTION ITSELF SPLITS: A POSITIVE-MEAN TILT BRANCH THICKENS TO A POSITIVE MEAN WEIGHTED TRANSVERSE-STRAIN-SQUARE CHARGE `int rho^2 |tau|^2`, WHILE A POSITIVE-MEAN DIRECTIONAL-DIFFUSION BRANCH THICKENS TO A POSITIVE MEAN PROJECTED-LAPLACIAN-SQUARE CHARGE `int |(I-xixi) Delta W|^2` ON ACTIVE CARRIERS / THUS EVERY RATCHET+PRODUCTION COMPONENT SUSTAINS TWO DISTINCT RECURRENT CRITICAL/HIGHER-DERIVATIVE CHANNELS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Directional decomposition

On the active set write

\[
W=\rho\xi,
\qquad
|\xi|=1.
\]

Decompose the similarity strain action on the vorticity direction as

\[
\boxed{
\Sigma\xi
=
\sigma\xi+\tau,
}
\]

where

\[
\sigma
:=
\xi\cdot\Sigma\xi
\]

is longitudinal stretching and

\[
\tau
:=
(I-\xi\otimes\xi)\Sigma\xi
\]

is projective tilt.

The enstrophy-production density is

\[
\rho^2\sigma.
\]

The direction equation along the similarity material velocity is

\[
\boxed{
D_\theta\xi
=
\tau+
\mathcal D_\xi,
}
\]

with

\[
\mathcal D_\xi
:=
\frac1\rho
(I-\xi\otimes\xi)\Delta W.
\]

---

## 2. Positive production forces axial-strain-square charge

Define

\[
A_{ax}(\theta)
:=
\int_{\mathbb R^3}
\rho^2\sigma^2dy.
\]

Since

\[
Q
=
\int\rho^2\sigma dy,
\]

Cauchy--Schwarz gives

\[
|Q|^2
\le
\left(\int\rho^2dy\right)
\left(\int\rho^2\sigma^2dy\right).
\]

But

\[
\int\rho^2dy=E\le Z_*.
\]

Therefore

\[
\boxed{
A_{ax}
\ge
\frac{Q^2}{Z_*}.
}
\]

Average on a positive-ratchet ergodic component `nu`.

M5-499 gives

\[
\langle Q\rangle_\nu>0.
\]

Hence by Jensen,

\[
\boxed{
\langle A_{ax}\rangle_\nu
\ge
\frac{\langle Q^2\rangle_\nu}{Z_*}
\ge
\frac{\langle Q\rangle_\nu^2}{Z_*}
=:a_{ax}>0.
}
\]

Thus every nonzero recurrent ratchet component pays a fixed mean squared longitudinal-strain charge weighted by vorticity intensity.

---

## 3. Ratchet mean splits into tilt or directional diffusion

Let the retained material ratchet action be represented by nonnegative observables

\[
r_{tilt},
\qquad
r_{diff}
\]

with

\[
r
\le r_{tilt}+r_{diff}.
\]

If

\[
\langle r\rangle_\nu>0,
\]

then at least one of

\[
\boxed{
\langle r_{tilt}\rangle_\nu>0
}
\]

or

\[
\boxed{
\langle r_{diff}\rangle_\nu>0
}
\]

holds.

The two branches are treated separately.

---

## 4. Tilt branch thickens to transverse-strain-square charge

Suppose

\[
\langle r_{tilt}\rangle_\nu>0.
\]

At each retained tilt event, the active material carrier satisfies

\[
\rho\ge\rho_a>0
\]

on the marked trajectory interval and pays fixed order-one action

\[
\int_J|\tau(Y(\theta),\theta)|d\theta
\ge\delta_t>0
\]

on a fixed-length normalized interval.

By the same trajectory-to-spacetime thickening logic used in M5-487, local smoothness gives fixed spatial and temporal radii on which a fixed fraction of the tilt persists.

Thus every retained tilt event pays

\[
\boxed{
\int_{I_t}\int_{B_t}
\rho^2|\tau|^2dy\,d\theta
\ge c_t>0.
}
\]

Positive invariant event frequency and bounded overlap then imply

\[
\boxed{
\left\langle
A_{tr}
\right\rangle_\nu
>0,
}
\]

where

\[
A_{tr}(\theta)
:=
\int\rho^2|\tau|^2dy.
\]

Therefore the tilt-driven ratchet component carries simultaneously

\[
\boxed{
\langle A_{ax}\rangle>0,
\qquad
\langle A_{tr}\rangle>0.
}
\]

---

## 5. Algebraic relation of the two strain channels

Pointwise on the active set,

\[
|\Sigma\xi|^2
=
\sigma^2+|\tau|^2.
\]

Therefore

\[
\boxed{
A_{ax}+A_{tr}
=
\int\rho^2|\Sigma\xi|^2dy.
}
\]

A tilt-driven ratchet-production component thus requires persistent strain action in at least two orthogonal components relative to the vorticity direction: longitudinal magnitude production and transverse direction rotation.

This does not yet contradict incompressibility or the strain `L2` bound.

---

## 6. Directional-diffusion branch thickens to projected-Laplacian charge

Suppose instead

\[
\langle r_{diff}\rangle_\nu>0.
\]

M5-487 gives

\[
\mathcal D_\xi
=
\frac1\rho
(I-\xi\otimes\xi)\Delta W.
\]

Hence on the active set

\[
\boxed{
\rho^2|\mathcal D_\xi|^2
=
|(I-\xi\otimes\xi)\Delta W|^2.
}
\]

The M5-487 thickening argument turns each order-one trajectory diffusion action into a fixed local spacetime charge

\[
\int_{I_d}\int_{B_d}
|(I-\xi\otimes\xi)\Delta W|^2dy\,d\theta
\ge c_d>0.
\]

Positive invariant frequency yields

\[
\boxed{
\left\langle
H_{proj}
\right\rangle_\nu>0,
}
\]

where

\[
H_{proj}(\theta)
:=
\int_{active}
|(I-\xi\otimes\xi)\Delta W|^2dy.
\]

Thus the diffusion-driven ratchet component carries simultaneously

\[
\boxed{
\langle A_{ax}\rangle>0,
\qquad
\langle H_{proj}\rangle>0.
}
\]

---

## 7. M5-487 firewall remains essential

A positive projected-Laplacian charge does **not** imply a coercive lower bound on

\[
\int\rho^2|\nabla\xi|^2dy.
\]

Weighted harmonic-map configurations can have nonzero direction gradients while the projected tension vanishes.

Therefore M5-500 keeps

\[
H_{proj}
\]

as its own higher-derivative channel rather than renaming it direction Dirichlet dissipation.

---

## 8. Enstrophy threshold on the tilt branch

Since

\[
A_{ax}+A_{tr}
\le
\int\rho^2|\Sigma|^2dy
\le
M_*^2\int|\Sigma|^2dy,
\]

and Calderon--Zygmund gives

\[
\int|\Sigma|^2dy
\le C E,
\]

we have

\[
\boxed{
A_{ax}+A_{tr}
\le
C M_*^2E.
}
\]

Averaging,

\[
\langle E\rangle
\ge
\frac{
\langle A_{ax}\rangle+
\langle A_{tr}\rangle
}{CM_*^2}.
\]

Thus positive tilt recurrence produces another fixed lower critical-enstrophy requirement.

It is a threshold, not a contradiction, because the compact lane allows finite but non-small enstrophy.

---

## 9. Diffusion branch is a genuine higher-derivative survivor

The projected-Laplacian charge is of higher differential order than the Leray energy or enstrophy ledger.

No globally finite invariant quantity currently bounds

\[
\int|\Delta W|^2
\]

strongly enough to make

\[
\langle H_{proj}\rangle>0
\]

a contradiction.

Therefore the diffusion-driven component is accurately classified as a recurrent higher-derivative critical structure, not as a closed branch.

---

## 10. Ratchet-production component dichotomy

Every positive-ratchet recurrent component satisfies

\[
\boxed{
\mathcal C_{ratchet}
\Longrightarrow
\mathcal C_{ax+tilt}
\lor
\mathcal C_{ax+projdiff},
}
\]

where

\[
\mathcal C_{ax+tilt}:
\quad
\langle A_{ax}\rangle>0,
\quad
\langle A_{tr}\rangle>0,
\]

and

\[
\mathcal C_{ax+projdiff}:
\quad
\langle A_{ax}\rangle>0,
\quad
\langle H_{proj}\rangle>0.
\]

Both are strictly narrower than the original positive-density ratchet label.

---

## 11. Relation to the dual component

If a future component-coupling theorem shows that dual and ratchet activity coexist on one ergodic component, then that component would simultaneously carry

\[
\langle P\rangle>0,
\quad
\langle A_{ax}\rangle>0,
\]

plus either

\[
\langle A_{tr}\rangle>0
\]

or

\[
\langle H_{proj}\rangle>0.
\]

This would create a much more overdetermined recurrent critical element.

M5-500 does not assume that intersection.

---

## 12. Highest-value next targets

### Tilt component

Audit whether recurrent positive weighted axial and transverse strain-square charges can be realized by a finite persistent material-flux network without forcing additional strain eigenframe rotation or a third active lineage.

### Projected-diffusion component

Derive the exact similarity evolution/budget of

\[
\int|\nabla W|^2
\]

and determine how the projected `Delta W` charge enters the palinstrophy equation. A signed fourth-order dissipation term may provide a stronger ledger than the first enstrophy balance.

The second route is especially valuable because `H_proj` already contains a fixed portion of the Laplacian of vorticity.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
