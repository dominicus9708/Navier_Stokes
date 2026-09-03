# DSD M5-672 — The CE-H global-vorticity maximum obeys an exact strain-viscous ledger and forces unit mean axial strain

Date: 2026-09-03

Status: **INTERNAL MAXIMUM-POINT LEDGER / AT A SPATIAL MAXIMUM OF `rho=|W|`, THE CE-H PARALLEL ELLIPTIC EQUATION GIVES `kappa <= -|grad xi|^2 <=0`; BECAUSE `grad rho=0`, THE MATERIAL AND EULERIAN AMPLITUDE DERIVATIVES COINCIDE THERE AND `(log ||W||_infty)'=sigma_*+kappa_*-1` AT ALMOST EVERY DIFFERENTIABLE TIME AFTER A DANSKIN-TYPE MAXIMIZER SELECTION / BOUNDED RECURRENCE THEN GIVES `<sigma_*>=1-<kappa_*> >= 1+<|grad xi_*|^2>` / THE MAXIMUM STRETCHING PAYER MUST THEREFORE BE TOP- OR MIDDLE-EIGENVALUE ALIGNED, NEVER BOTTOM-ALIGNED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Maximum amplitude

Define

\[
\boxed{
M(\theta):=\|W(\cdot,\theta)\|_{L^\infty(\mathbb R^3)}.
}
\]

The all-order compact hull gives uniform spatial and temporal smoothness, so `M(theta)` is locally Lipschitz.

At almost every `theta` it is differentiable.

Choose a maximizing point `y_*(theta)` among the active maximizers so that the usual envelope/Danskin derivative is realized.

Then

\[
\rho(y_*,\theta)=M(\theta),
\]

\[
\boxed{\nabla\rho(y_*,\theta)=0,}
\]

and

\[
\boxed{\Delta\rho(y_*,\theta)\le0.}
\]

---

## 2. Viscous multiplier at the maximum

CE-H gives the scalar parallel eigenfield equation

\[
\Delta\rho
=(\kappa+|\nabla\xi|^2)\rho.
\]

At the positive maximum, divide by `rho=M>0`:

\[
\kappa_*+|\nabla\xi_*|^2
=\frac{\Delta\rho_*}{\rho_*}
\le0.
\]

Hence

\[
\boxed{
\kappa_*
\le
-|\nabla\xi_*|^2
\le0.
}
\]

This strengthens the M5-634 maximum-sign observation by retaining the directional-gradient deficit.

---

## 3. Exact maximum growth law

CE-H amplitude transport is

\[
D_B\rho
=(\sigma+\kappa-1)\rho.
\]

At the spatial maximum,

\[
B\cdot\nabla\rho=0.
\]

Thus

\[
\partial_\theta\rho_*
=D_B\rho_*.
\]

At almost every differentiable time of `M`,

\[
M'
=(\sigma_*+\kappa_*-1)M.
\]

Therefore

\[
\boxed{
(\log M)'
=\sigma_*+\kappa_*-1.
}
\]

---

## 4. Recurrent mean

The compact marked hard component has

\[
0<M_-\le M(\theta)\le M_+<\infty
\]

on the retained nontrivial component after reducing to the carrier-supported invariant set.

Hence

\[
\frac{\log M(T)-\log M(0)}{T}\to0.
\]

Averaging the exact maximum ledger gives

\[
\boxed{
\langle\sigma_*\rangle
=1-\langle\kappa_*\rangle.
}
\]

Using the pointwise maximum inequality,

\[
\boxed{
\langle\sigma_*\rangle
\ge
1+\langle|\nabla\xi_*|^2\rangle
\ge1.
}
\]

---

## 5. Strain-eigenvalue classification at the maximum

CE-H gives

\[
\Sigma W=\sigma W.
\]

Thus `sigma_*` is one of the three strain eigenvalues at the vorticity maximum.

Because the strain is trace free, the bottom eigenvalue is always nonpositive.

The positive mean lower bound therefore implies that the recurrent maximum stretching payer must occupy, with positive frequency,

\[
\boxed{
\text{top-eigenvalue alignment}
\quad\lor\quad
\text{positive middle-eigenvalue alignment}.
}
\]

A bottom-aligned maximum cannot pay the recurrent amplitude balance.

---

## 6. Zero-kappa subcase

If

\[
\kappa_*=0
\]

at a maximum, then the maximum inequality forces

\[
|\nabla\xi_*|=0
\]

and

\[
\Delta\rho_*=0.
\]

Combined with `grad rho_*=0`, this reproduces the first-order-flat zero-level maximum structure already isolated in M5-637.

Then

\[
(\log M)'=\sigma_*-1.
\]

A fully zero-kappa recurrent maximum therefore requires mean `sigma_*=1` while all non-Beltrami/magnitude-direction costs are displaced away from the maximum point.

---

## 7. Nonzero negative-kappa subcase

If the maximum spends positive frequency with

\[
\kappa_*\le-\kappa_m<0,
\]

then on that frequency set

\[
\sigma_*
\ge1+\kappa_m
\]

is required merely to keep the maximum from decaying.

Thus strongly negative viscous multiplier at the dominant amplitude ridge requires correspondingly stronger axial strain.

This is the pointwise maximum analogue of the M5-651--670 high-amplitude production ledgers.

---

## 8. External middle-eigenvalue criterion audit

Known scale-critical regularity criteria involving the positive middle strain eigenvalue do not automatically close this branch.

A Type-I recurrent profile with order-one normalized positive middle eigenvalue produces the critical logarithmic divergence of those physical space-time norms rather than satisfying the finite criterion.

Therefore the top/middle split is structural but not itself a regularity theorem application.

---

## 9. Next use

The maximum ledger supplies a canonical high-amplitude point with:

\[
\kappa_*\le0,
\qquad
\langle\sigma_*\rangle\ge1.
\]

This point can be combined with the M5-671 spectral-gap compatibility:

- simple top alignment gives a positive transverse spectral-gap charge;
- top/middle eigenvalue collision enters the M5-624 pressure-viscous compensation branch;
- positive middle alignment enters the critical middle-strain branch.

The remaining question is whether these three mechanisms can recurrently alternate without forcing a strict frame/pressure or flux defect.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
