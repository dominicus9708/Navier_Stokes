# Corrected Low-Mode Spectral Toy Search for the P_V Threshold Quotient — 2026-08-20

Overall status: **NUMERICAL DIAGNOSTIC ONLY — NOT A PROOF.**

This note records a reproducible periodic low-mode search using `scripts/pv_threshold_spectral_search.py`.

---

## 1. Quantity tested

On the `2*pi`-periodic three-torus, random divergence-free velocity Fourier modes are generated and normalized so that

\[
\|\omega\|_\infty=1.
\]

The diagnostic quotient is

\[
\boxed{
\eta_{VI}
=
\frac{-\int S:(M_{sp}+2M_{rg})}
{\int|\Delta S|^2}.
}
\]

This is the periodic analogue of the local H1 threshold quotient used in the proof attempt.

---

## 2. Corrected derivative convention

The periodic domain is

\[
[0,2\pi)^3,
\]

so Fourier wave numbers are the integer vectors `k in Z^3`, and differentiation multiplies mode `k` by `i k`.

An earlier informal diagnostic value mentioned in chat (`~0.0759`) used an inconsistent domain/derivative normalization and was not reproducible. It should be discarded.

The present script fixes the convention explicitly and is the reproducible baseline.

---

## 3. Baseline random search

Parameters used in the current diagnostic run:

- grid: `10^3`;
- Fourier cutoff: `|k_i| <= 2`;
- random nonzero divergence-free mode count: between 4 and 15;
- samples: 2500;
- RNG seed: 42;
- normalization: `max_x |omega(x)| = 1`.

The observed best value was approximately

\[
\boxed{
\eta_{VI}^{toy}\approx0.02096.
}
\]

The empirical upper percentiles were approximately

\[
99\%:\ 0.00439,
\qquad
99.9\%:\ 0.00946.
\]

These values are specific to this small random periodic ensemble and have no theorem-level significance.

---

## 4. Interpretation

The search currently provides no evidence that generic low-mode divergence-free configurations approach the viscous threshold `eta >= nu` when `nu=1` is used as a dimensionless reference.

However, this cannot be used as a regularity argument because:

1. the domain is periodic rather than `R^3`;
2. the mode cutoff is extremely low;
3. random search does not approximate the variational supremum;
4. the first-hitting tightness/moment class is not imposed exactly;
5. viscosity normalization and the admissible initial-data class matter.

Its role is only to search for candidate geometries and to test algebraic formulas.

---

## 5. Important scaling lesson

For pure coordinate dilation

\[
S_b(x)=S(bx)
\]

with amplitude unchanged,

\[
\eta(S_b)=b^{-2}\eta(S).
\]

Therefore a variational search that does not fix spatial scale can artificially enlarge the quotient simply by broadening the field. This is why the theorem-level compact class must include non-T tightness/moment normalization.

The periodic toy domain fixes this scale automatically by the box and discrete wave numbers, which is one reason its raw values cannot be compared directly with an unconstrained whole-space search.

---

## 6. Next numerical step

The next useful diagnostic is not more random sampling. It is constrained optimization over a fixed low-mode basis while monitoring:

- `eta_VI`;
- `||omega||_infty`;
- strain middle-eigenvalue occupancy;
- the `7/9` covariance defect;
- max-mid defect;
- spatial moment / effective radius.

This could reveal whether high-efficiency toy states simultaneously approach the analytic rigidity conditions already identified in the proof route.

Status: **THE PREVIOUS INFORMAL 0.0759 TOY VALUE IS WITHDRAWN. UNDER A CONSISTENT 2*pi-PERIODIC FOURIER CONVENTION, A 2500-SAMPLE LOW-MODE RANDOM SEARCH FOUND A BEST eta_VI ABOUT 0.02096. THIS IS A DIAGNOSTIC ONLY AND DOES NOT ENTER THE PROOF.**