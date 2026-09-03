# DSD M5-635 — Zero-mean synchronized kappa forces the zero-level branch or positive-density amplitude-ridge detachment

Date: 2026-09-03

Status: **INTERNAL BRANCH REDUCTION / THE SYNCHRONIZED PERSISTENT FIXED-FLUX LEVEL SATISFIES `mean c_*=0`. IF `c_*` IS NOT IDENTICALLY ZERO, ITS POSITIVE SET HAS POSITIVE INVARIANT MEASURE. M5-634 PROVES THAT NO POSITIVE LOCAL MAXIMUM OF `rho=|W|` CAN LIE ON A POSITIVE-KAPPA LEVEL. THEREFORE EVERY POSITIVE `c_*` PHASE FORCES THE AMPLITUDE-DOMINANT VORTICITY RIDGE AWAY FROM THE PERSISTENT FLUX LEVEL. THE RELABELING SURVIVOR IS THUS REDUCED TO `c_* identically 0` OR POSITIVE-DENSITY AMPLITUDE-RIDGE/SHEATH DETACHMENT. THIS IS A GENUINE SPATIAL MIGRATION REQUIREMENT, NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Synchronized persistent level

M5-628 gives, on the relabeling branch,

\[
\kappa_1=\cdots=\kappa_N=c_*(\theta)
\]

for all persistent bounded nondegenerate fixed-flux lineages in the recurrent network.

M5-603/M5-628 give

\[
\boxed{\langle c_*\rangle=0.}
\]

---

## 2. Elementary zero-mean dichotomy

If

\[
c_*(\theta)\le0
\]

for almost every recurrent time, then zero mean implies

\[
\boxed{c_*(\theta)=0\quad\text{a.e.}}
\]

on the ergodic component.

Therefore every nontrivial synchronized history must have

\[
\boxed{\mu\{\theta:c_*(\theta)>0\}>0.}
\]

Likewise it must have a negative set of positive measure unless it is zero a.e.

---

## 3. Positive kappa cannot carry a vorticity maximum

M5-634 proves that at every positive spatial local maximum of

\[
\rho=|W|,
\]

one has

\[
\boxed{\kappa\le-|\nabla\xi|^2\le0.}
\]

Hence, whenever

\[
c_*(\theta)>0,
\]

no positive local maximum of `rho` can lie on the synchronized persistent level

\[
\kappa=c_*(\theta).
\]

In particular, the global vorticity maximum is carried by another kappa level at those times.

---

## 4. Positive-density amplitude-ridge detachment

If `c_*` is nontrivial, its positive phases have positive invariant measure.

At every such phase the amplitude-dominant ridge is spatially detached from the persistent fixed-flux level.

Therefore

\[
\boxed{
R_{relabel}
\Longrightarrow
Z_{\kappa=0}^{persistent}
\lor
M_{ridge}^{detach,+density}.
}
\]

Here

- `Z_{kappa=0}^persistent`: the synchronized persistent flux network lies on `kappa=0` for almost all recurrent times;
- `M_ridge^{detach,+density}`: at a positive-density set of times, the high-amplitude vorticity ridge lies on another kappa level.

---

## 5. Relation to the M5-630 covariance

A negative same-level covariance

\[
\langle c_*E_*\rangle<0
\]

requires larger active enstrophy during negative `c_*` phases than during positive phases.

M5-635 shows that the positive phases are not merely lower-weight phases in time: they are phases in which the synchronized persistent level is **forbidden from carrying a vorticity maximum**.

Thus the phase covariance has an unavoidable spatial manifestation:

\[
\boxed{
\text{flux skeleton and amplitude-dominant sheath separate during positive }c_*\text{ phases}.
}
\]

This supports the persistent-spine/renewing-sheath geometry found in M5-633.

---

## 6. Connection to migration audits

The vorticity maximum itself is an Eulerian feature and need not be one fixed material marker.

Therefore the detachment statement does not yet identify which material label moves.

The correct next audit is to distinguish:

1. the maximum/high-amplitude ridge moves between material labels on the same external kappa population;
2. a fixed material high-amplitude label changes its kappa history through the non-relabeling forcing branch `P_perp grad(D_B kappa) != 0`;
3. the persistent `kappa=0` flux spine remains while a three-dimensional enstrophy sheath is replaced.

All three are compatible with the current exact equations until further work.

---

## 7. Zero-level branch

The remaining no-detachment synchronized possibility is

\[
\boxed{c_*(\theta)\equiv0.}
\]

On each persistent line in this branch,

\[
\Delta W=0
\]

at the line points and the material vorticity flux is exactly constant:

\[
\boxed{\Phi'=0.}
\]

However this condition is currently known only on the persistent line/surface level, not on an open spatial set, so analyticity cannot yet globalize `Delta W=0` from it.

The zero-level branch must therefore be treated separately rather than declared harmonic/trivial.

---

## 8. Firewall

M5-635 does not assume that the persistent production payer is always the global vorticity maximum.

The rigorous statement is only that a positive synchronized kappa level cannot contain any positive local vorticity maximum.

If an argument needs the production carrier itself to be maximum-attached, that must be introduced as an explicit additional subbranch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]