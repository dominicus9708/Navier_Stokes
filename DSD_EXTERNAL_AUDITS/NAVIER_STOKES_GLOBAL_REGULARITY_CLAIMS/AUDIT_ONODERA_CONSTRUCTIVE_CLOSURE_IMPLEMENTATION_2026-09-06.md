# DSD Audit — Onodera Fully Constructive Closure: Public Implementation Package

Date: 2026-09-06
Author/program: Hiroaki Onodera, `hironodera/navier-stokes-global-regularity-proof`, linked by the repository to Zenodo record 15605346.
Audit status: **IMPLEMENTATION CERTIFICATE FAILS; PUBLIC CODE DOES NOT IMPLEMENT AN ALL-ORDER UNIFORM NSE CLOSURE**

## 1. Scope

The repository presents itself as a full implementation package associated with the claimed constructive global-regularity proof. This audit addresses the public implementation. It does not by itself refute every theorem that may appear in an analytical PDF unavailable to the audit.

## 2. Concentration surrogate has the wrong sign for suppression

`src/concentration_control.py` evolves

\[
C_{n+1}=C_n+\Delta t\,K C_n^{3/2}.
\]

For positive `K`, the continuous analogue

\[
C'=KC^{3/2}
\]

has finite-time Riccati growth:

\[
C(t)=\frac{C_0}{\left(1-\frac K2\sqrt{C_0}\,t\right)^2}
\]

up to its blow-up time.

Therefore the implemented concentration law is not a suppression mechanism. If the analytical proof contains an additional negative term, invariant region, stopping rule, or comparison argument that changes this conclusion, that mechanism is not represented by this module.

The initial `C0` is also only a simplified proxy: the code estimates it by the mean of sampled squared gradients.

## 3. High-order recurrence worsens with derivative order

`src/energy_recursion.py` advances formal energy levels by

\[
E_k^{n+1}=E_k^n+\Delta t\left[
-\frac\nu2 D_{k+1}
+\frac{C_k^\sharp}{\nu}C E_k
\right],
\]

with

\[
C_k^\sharp
=\frac{k}{4}\frac{2^k}{\nu}+2.
\]

Hence

\[
C_k^\sharp\sim \frac{k2^k}{4\nu}
\qquad(k\to\infty).
\]

So the public recurrence does not contain an all-order uniform constant. Its positive coupling coefficient gets rapidly worse with `k`, while the same concentration variable `C` grows under the positive Riccati law.

This does not logically rule out finite-order Sobolev control if stronger dissipation estimates are proved elsewhere, but it directly contradicts any claim that the code itself demonstrates a closed, order-uniform `H^\infty` hierarchy.

## 4. The driver truncates at derivative order three

`src/main_driver.py` fixes

```python
max_order = 3
```

and builds `Ck_sharp_list` only for these finitely many levels.

Thus the implementation cannot computationally instantiate a claim of control for every derivative order. A finite list of ODE surrogates is not an `H^\infty` proof certificate.

Formally,

\[
\boxed{
\text{verification for }k\le3
\not\Rightarrow
\sup_{k\ge0}\text{ a closed Sobolev hierarchy.}
}
\]

## 5. Decisive issue: the velocity field is never advanced

The driver creates synthetic initial data, transforms it, and stores the divergence-free Fourier array `u0_hat_proj`.

Inside every time step it computes

```python
grad_norms = compute_grad_norm_dict(u0_hat_proj, solver, max_order)
```

from that same unchanged initial array.

It then advances only:

- `ConcentrationControl`;
- `EnergyRecursion`;
- `SpatialDecay`.

No new `u_hat(t+dt)` is produced by an NSE time step and assigned back to the state.

Therefore the computed derivative norms do not represent the derivatives of an evolving Navier-Stokes solution.

\[
\boxed{
\text{surrogate recursion driven by fixed }u_0
\neq
\text{Navier-Stokes evolution }u(t).
}
\]

## 6. Stability monitoring is a stop condition, not a continuation theorem

The loop stops when a surrogate becomes large:

```python
if C_current > 1e6 or np.any([v > 1e10 for v in energy_module.Ek.values()]):
    break
```

Terminating a simulation at a threshold does not prove that the PDE cannot reach that threshold. A valid regularity proof requires an a priori estimate showing the actual PDE trajectory remains in the admissible region.

## 7. DSD hierarchy audit

The implementation consumes four facts that it does not itself establish:

1. the scalar `C` must faithfully represent an NSE concentration functional;
2. the displayed Riccati comparison must provide an upper bound useful for all time;
3. supplied `grad_norms` must come from the current PDE state;
4. the `k`-dependent recurrence must close uniformly enough to justify arbitrary-order regularity.

None of these is certified by the current public driver.

## 8. Verdict

The public code cannot serve as computational verification of an unconditional global-regularity theorem.

\[
\boxed{
\text{IMPLEMENTATION FAIL: no NSE time evolution, growing Riccati surrogate, finite-order truncation, no uniform-in-}k\text{ closure.}
}
\]

The associated analytical manuscript remains a separate object. If it contains a rigorous PDE derivation that repairs these issues independently of the code, it must be audited on its own merits.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
