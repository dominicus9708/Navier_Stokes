# DSD M5-152 — Genealogical High-Frequency Derivative-Hierarchy Escape

Date: 2026-08-27

Status: **AUDIT CORRECTION FOR M5-151 / COMPACT C-INFINITY OR UNIFORM ANALYTIC REGULARITY OF THE W1 CLASS DOES NOT BY ITSELF GIVE A TAME ESTIMATE OF GENEALOGICAL DERIVATIVES BY THE BASE FLAT-VORTICITY NORM / HIGH-ETA-FREQUENCY MODES CAN HAVE EXPONENTIALLY SMALL AMPLITUDE WHILE DERIVATIVE-TO-AMPLITUDE RATIOS DIVERGE / THE M5-151 STATISTICAL ENERGY IDENTITY IS VALID BUT ITS DERIVATIVE-HIERARCHY CLOSURE REMAINS A SEPARATE SPECTRAL GATE / GLOBAL REGULARITY UNPROVED.**

---

## 1. The tempting but invalid shortcut

M5-151 leaves terms such as

\[
B_\eta=\langle|K_\eta|^2\rangle
\]

in the `O(xi^-2)` normal-energy remainder.

Because the W1 pair class is locally smooth/analytic and compact, it is tempting to assert a uniform inequality

\[
\|K_\eta\|\le C\|K\|.
\]

Compactness/analyticity alone does not imply such a proportional estimate near the zero difference.

---

## 2. Explicit analytic compact counterexample

Consider on a periodic genealogical coordinate

\[
\boxed{
f_n(\eta):=e^{-n}\sin(n\eta).}
\]

For every fixed integer `k`,

\[
\|\partial_\eta^k f_n\|_\infty
\le n^ke^{-n}\to0.
\]

Hence

\[
f_n\to0
\]

in `C^infinity`.

The family

\[
\{0,f_1,f_2,\ldots\}
\]

is therefore compact in the Frechet `C^infinity` topology.

Moreover the functions are entire in `eta`; on every fixed strip of sufficiently small width their amplitudes remain uniformly bounded.

Yet

\[
\boxed{
\frac{\|f_n'\|_\infty}{\|f_n\|_\infty}=n\to\infty.
}
\]

Thus no constant `C` follows from compact smooth/analytic regularity alone.

---

## 3. DSD interpretation

The genealogical channel can hide high frequency behind very small amplitude.

This matters precisely in a flat fiber because the amplitude is already superalgebraically small in the normal coordinate.

A closure that replaces

\[
\xi^{-2}\|K_\eta\|^2
\]

by

\[
C\xi^{-2}\|K\|^2
\]

without a separately proved spectral bound would conflate

\[
\text{small state amplitude}
\]

with

\[
\text{small genealogical frequency}.
\]

That is an Axis/Static-aggregation error in the DSD audit.

---

## 4. Why the high-frequency channel is still constrained

The counterexample does not construct a Navier--Stokes flat fiber.

In the actual inverse-Fuchsian vorticity equation, genealogical derivatives enter as

\[
\frac{4\nu}{\xi}K_{\eta\xi}
\]

and

\[
\frac{\nu}{\xi^2}K_{\eta\eta}.
\]

Thus a genealogical frequency `k` only competes with the principal normal operator when roughly

\[
k\gtrsim \xi.
\]

For every fixed spectral frequency, the one-way normal operator still dominates as `xi->infinity`.

Therefore any surviving statistical flat fiber would need an increasingly high genealogical-frequency channel correlated with normal depth.

This is a much narrower escape than generic derivative loss.

---

## 5. New spectral gate

A sufficient next input would be one of:

1. a uniform spectral-tail estimate for the pair-flow generator `A_eta` strong enough to make
   \[
   \|1_{|A_\eta|\gtrsim\xi}K(\xi)\|
   \]
   negligible relative to the normal energy;

2. an analytic/Gevrey estimate in an invariant Hilbert norm that controls the generator without amplitude-ratio loss;

3. a frequency-localized version of the M5-151 normal energy identity, treating low and high genealogical frequencies separately.

The third route is the most direct because low frequencies are perturbative automatically for large `xi`.

---

## 6. DSD four-chain audit

### Formation — GREEN

The counterexample tests only the missing estimate, not the Navier--Stokes equation itself.

### Axis — GREEN

Amplitude and genealogical frequency are separated explicitly.

### Static aggregation — GREEN

Analytic compactness is retained as a regularity ceiling, not reinterpreted as a relative spectral gap.

### Dynamics — GREEN

The pair-flow generator must be handled dynamically/spectrally if M5-151 is to close.

### Cross-audit — GREEN

The exact M5-151 energy identity remains valid; only the proposed easy closure by compactness is rejected.

---

## 7. Updated Branch-S frontier

`P1_B^S` is now reduced to a **frequency-localized flat-vorticity uniqueness problem**:

\[
\boxed{
\text{low genealogical frequencies: normal operator dominates};
\qquad
\text{high genealogical frequencies: need a spectral-tail estimate.}
}
\]

No contradiction is yet claimed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]