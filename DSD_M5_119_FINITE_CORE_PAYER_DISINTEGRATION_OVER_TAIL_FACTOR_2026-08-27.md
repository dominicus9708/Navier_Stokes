# DSD M5-119 — Finite-Core Payer Disintegration over the Canonical Tail Factor

Date: 2026-08-27

Status: **FINITE-CORE PRESSURE/STRAIN PAYER DECOMPOSED MEASURE-THEORETICALLY OVER THE CANONICAL TAIL FACTOR / POSITIVE MEAN PAYER DESCENDS AS A NONNEGATIVE CONDITIONAL FACTOR OBSERVABLE / THE REMAINING FIBER FLUCTUATION HAS ZERO CONDITIONAL MEAN AND MUST NOT BE DOUBLE-COUNTED AS A SECOND POSITIVE COST / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inputs

Fix an ergodic invariant probability measure `mu` on the compact minimal W1 set `M` for which the cubic residue is positive:

\[
\boxed{\mathscr R_3(\mu)>0.}
\]

Let

\[
\pi:=\mathfrak T:M\to\mathcal T
\]

be the continuous canonical tail factor and

\[
\nu:=\pi_\#\mu.
\]

By M5-118, `nu` is ergodic for log-radius translation and

\[
\boxed{
\mathscr R_3
=\int_{\mathcal T}\mathfrak c(T)d\nu(T),
\qquad
\mathfrak c(T)=\int_{S^2}|\Phi_T(0,\theta)|^3d\theta.
}
\]

Let `H_R(V)>=0` denote the fixed-core component-free payer chosen in M5-109, with one sufficiently large fixed `R=R_*` so that

\[
\boxed{
\int_M H_R(V)d\mu(V)
\ge
\kappa_\nu\,\mathscr R_3
}
\]

for an explicit positive constant `kappa_nu` inherited from M5-108/M5-109 (for the normalization used there one may take the recorded positive multiple such as `nu/12`; only positivity is needed below).

Since `M` is compact and `H_R` is a local smooth continuous functional,

\[
0\le H_R\le H_{max}<\infty.
\]

---

## 2. Formation chain: disintegrate only after the tail factor exists

Because `pi` is a genuine measurable factor map, disintegrate `mu` over `nu`:

\[
\boxed{
\mu
=\int_{\mathcal T}\mu_T\,d\nu(T),
}
\]

where `mu_T` is supported on the fiber

\[
\pi^{-1}(T)
\]

for `nu`-almost every `T`.

Define the tail-conditional payer

\[
\boxed{
\overline H(T)
:=\int_{\pi^{-1}(T)}H_R(V)d\mu_T(V).
}
\]

Then

\[
\overline H(T)\ge0
\]

and

\[
\boxed{
\int_{\mathcal T}\overline H(T)d\nu(T)
=\int_MH_R(V)d\mu(V)
\ge\kappa_\nu\mathscr R_3>0.
}
\]

Thus a positive part of the finite-core payer descends to the tail factor in the precise conditional-expectation sense.

---

## 3. Static aggregation: the fiber remainder is signed

Define

\[
\boxed{
H_{fib}(V)
:=H_R(V)-\overline H(\pi(V)).
}
\]

Then for `nu`-almost every tail state,

\[
\boxed{
\int_{\pi^{-1}(T)}H_{fib}(V)d\mu_T(V)=0.
}
\]

Consequently

\[
\int_MH_{fib}d\mu=0.
\]

This is the exact DSD bookkeeping rule:

\[
\boxed{
H_R
=\overline H\circ\pi
+H_{fib},
}
\]

but only the first term is nonnegative as a factor observable.

The second term is a signed within-fiber fluctuation.  It is **not** an additional positive payer and cannot be added to `overline H` as a second resource.

---

## 4. Positive-measure payer-coded tail states

Let

\[
m_H:=\int\overline H d\nu.
\]

Then

\[
m_H\ge\kappa_\nu\mathscr R_3>0.
\]

Since `0<=overline H<=H_max`, choose

\[
\delta:=m_H/2.
\]

If

\[
E_\delta:=\{T:\overline H(T)\ge\delta\},
\]

then

\[
m_H
\le
\delta+H_{max}\nu(E_\delta),
\]

so

\[
\boxed{
\nu(E_\delta)
\ge
\frac{m_H}{2H_{max}}
\ge
\frac{\kappa_\nu\mathscr R_3}{2H_{max}}>0.
}
\]

Thus the tail factor contains a positive-measure set of states whose fibers carry a quantitatively positive **expected** core payer.

---

## 5. Dynamic chain: positive-density recurrence on the tail factor

Because `nu` is ergodic under log translation, Birkhoff applied to the indicator of `E_delta` gives for `nu`-almost every tail trajectory

\[
\boxed{
\lim_{L\to\infty}
\frac1L
\left|
\{0\le\rho\le L:
D_{2\rho}T\in E_\delta\}
\right|
=\nu(E_\delta)>0.
}
\]

Therefore the factor does not merely carry positive mean cubic density.  It also visits tail states whose conditional core payer is positive with positive logarithmic density.

This is a statistical tail/core coupling, not yet a pointwise deterministic reconstruction.

---

## 6. A better split than injective/noninjective alone

Tail injectivity is sufficient but not necessary for the payer itself to descend.

Define the conditional fiber variance

\[
\boxed{
\Sigma_H^2(T)
:=
\int_{\pi^{-1}(T)}
|H_R(V)-\overline H(T)|^2d\mu_T(V).
}
\]

Two distinct branches emerge.

### Branch P0 — payer-descending fiber

If

\[
\Sigma_H(T)=0
\quad\nu\text{-a.e.},
\]

then

\[
\boxed{
H_R(V)=\overline H(\pi(V))
\quad\mu\text{-a.e.}
}
\]

even if the full tail factor is noninjective.

The finite-core payer is then genuinely a tail-factor observable.

### Branch P1 — payer-fluctuating fiber

If

\[
\int\Sigma_H^2d\nu>0,
\]

then there exist same-tail states carrying different finite-core payer values.

Because M5-115 shows same-tail differences lie in strong `L2 cap L3`, this branch isolates a new precise question:

\[
\boxed{
\text{Can a compact recurrent strong-critical fiber modulate the core pressure/strain payer while carrying zero cubic residue?}
}
\]

This is sharper than the earlier injective/noninjective split.

---

## 7. Relation to the cubic factor density

The present argument proves only

\[
\int\overline H d\nu
\ge\kappa_\nu\int\mathfrak c d\nu.
\]

It does **not** prove the pointwise inequality

\[
\overline H(T)\ge\kappa_\nu\mathfrak c(T).
\]

Nor does it prove that high cubic-density slices coincide with high payer-coded slices.

That stronger correlation is a new forward problem.

This distinction is essential to prevent converting an invariant-average inequality into a pointwise statewise inequality.

---

## 8. DSD four-chain audit

### Formation — GREEN

The conditional decomposition is performed only after the canonical tail factor and invariant measure are already constructed.

### Axis — GREEN

Core payer, tail factor and within-fiber directions are typed as different channels.

### Static aggregation — GREEN

`overline H` is nonnegative; `H_fib` has zero conditional mean and is signed.  No double counting occurs.

### Dynamics — GREEN

Ergodicity is used only after the static conditional payer has been formed, to convert positive factor measure into positive log-time density.

### Cross-audit — GREEN

No tail recurrence is used to prove the upstream W1 compactness or the M5-109 core payer.

---

## 9. New frontier

The tail/core problem is now split more sharply:

\[
\boxed{
P0:\ H_R\text{ descends to the tail factor}
}
\]

versus

\[
\boxed{
P1:\ \text{same-tail strong-critical fibers modulate }H_R.
}
\]

For `P0`, the next target is a **correlation/cocycle theorem** between the log-cylinder cubic density `mathfrak c` and the descended payer `overline H`.

For `P1`, the next target is a **relative-energy / relative-pressure equation inside one tail fiber** proving either rigidity or a quantifiable fiber-production mechanism.

These two calculations may proceed in parallel under the DSD algorithm, but neither may be used to justify the other retroactively.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
