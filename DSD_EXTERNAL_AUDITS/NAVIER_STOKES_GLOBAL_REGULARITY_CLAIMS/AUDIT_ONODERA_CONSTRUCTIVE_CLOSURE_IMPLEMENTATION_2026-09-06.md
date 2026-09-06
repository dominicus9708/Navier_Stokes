# DSD Audit — Onodera Fully Constructive Closure: Public Implementation Package

Date: 2026-09-06
Author/program: Hiroaki Onodera, `hironodera/navier-stokes-global-regularity-proof`, linked by the repository to Zenodo record 15605346.
Audit status: **COMPUTATIONAL VERIFICATION CLAIM FAILS IN PUBLIC CODE; ANALYTICAL MANUSCRIPT REQUIRES SEPARATE FULL-TEXT AUDIT**

## 1. Scope of this audit

The repository README describes the code as the “full implementation package of the global regularity proof” and says it is directly translatable from the analytical form.

This file audits that implementation claim. It does not claim to refute every theorem in the linked analytical PDF, which must be audited separately when its full text is available.

## 2. Concentration module

`src/concentration_control.py` evolves a scalar surrogate by

\[
C_{n+1}=C_n+\Delta t\,K C_n^{3/2}.
\]

For positive constant `K`, the continuous analogue

\[
C'=KC^{3/2}
\]

has finite-time Riccati-type growth rather than a regularizing bound. The module therefore does not itself establish concentration suppression.

The initial concentration is also estimated by a simple mean of sampled gradient squares and is explicitly described in code as a simplified proxy, not an exact PDE functional.

## 3. High-order energy module

`src/energy_recursion.py` advances formal energy levels using supplied gradient norms and the surrogate concentration value. This is a model recurrence; correctness requires that the supplied quantities come from the evolving Navier–Stokes solution and that the recurrence inequality has been proved analytically.

The code alone cannot establish those facts.

## 4. Main driver audit: velocity is not evolved

The decisive computational issue appears in `src/main_driver.py`.

The driver:

1. constructs synthetic initial data `u0_phys`;
2. Fourier transforms and projects it to `u0_hat_proj`;
3. enters a time loop;
4. at every step computes

```python
grad_norms = compute_grad_norm_dict(u0_hat_proj, solver, max_order)
```

using the **same initial projected array**;
5. updates only the scalar `ConcentrationControl`, `EnergyRecursion`, and `SpatialDecay` objects;
6. never replaces `u0_hat_proj` by a time-advanced Navier–Stokes state.

Thus the velocity field used for the norms is time-independent in the driver.

The presence of an `fft_solver` object does not change this unless its NSE time-advance is actually called. In the displayed loop, it is not.

## 5. Stability-monitoring audit

The loop terminates if a surrogate threshold is exceeded:

```python
if C_current > 1e6 or ...:
    break
```

This is a diagnostic/termination rule. It is not a theorem that the original PDE avoids the threshold. Stopping a computation when a quantity becomes large cannot prove that the true solution remains regular.

## 6. Consequence

The public package is therefore not a numerical integration/verification of the claimed global NSE trajectory. It simulates a collection of proxy recurrences driven by fixed initial-field derivative samples.

Formally:

\[
\boxed{
\text{surrogate recursion on fixed }u_0
\neq
\text{Navier–Stokes evolution }u(t).
}
\]

## 7. What remains open

The analytical paper may contain independent rigorous estimates. Those must be checked directly, especially:

- the derivation of the concentration differential inequality;
- whether its sign actually suppresses rather than permits Riccati growth;
- how high-order constants close uniformly in k;
- whether any “real-time stability monitoring” is a theorem of the PDE or an external adaptive rule;
- whether the computational package is intended only as an illustration rather than evidence.

## 8. DSD verdict

The public code cannot serve as computational certification of global regularity in its current form because it does not evolve the Navier–Stokes velocity field through time.

\[
\boxed{\text{IMPLEMENTATION CERTIFICATE NOT VALID AS NSE VERIFICATION.}}
\]

The analytical global-regularity claim remains **OPEN_DEEP_AUDIT**, not validated by this package.

Global regularity remains unproved.
