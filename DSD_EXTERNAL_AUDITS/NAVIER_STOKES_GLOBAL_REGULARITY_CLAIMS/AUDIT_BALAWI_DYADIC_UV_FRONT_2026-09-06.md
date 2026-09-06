# DSD Audit — Balawi Dyadic Shape / UV Front / Windowed Duhamel–Grönwall

Date: 2026-09-06
Source: Ammar Balawi, *Global Regularity for 3D Navier–Stokes via Dyadic Shape, UV Front Barrier, and Windowed Duhamel–Grönwall*, DOI 10.5281/zenodo.17298965, Oct 2025.
Audit status: **CORE PARAPRODUCT LOCALIZATION HINGE FAIL**

## 1. Claimed proof chain

The manuscript uses:

1. shell energy identities;
2. a shape drift inequality driven only by a width-3 neighboring shell budget;
3. a UV-front jump-spacing/logarithmic barrier;
4. a windowed Duhamel estimate with only width-3 forcing;
5. a banded Grönwall contraction;
6. a vorticity-window estimate and global BKM summation.

All later steps depend on the claimed finite-band nonlinear localization.

## 2. Displayed root lemma

Appendix A.3 states, schematically,

\[
\|P_j\mathbb P\nabla\cdot(f\otimes g)\|_2
\le C_{par}\sum_{|m|\le3}
\Bigl(\|f_{j+m}\|_2\|\nabla g_{j+m}\|_\infty
+\|g_{j+m}\|_2\|\nabla f_{j+m}\|_\infty\Bigr),
\]

and in particular

\[
\|P_j\mathbb P\nabla\cdot(u\otimes u)\|_2^2
\le C_{par}\sum_{|m|\le3}\varepsilon_{j+m}.
\]

The text explains this by saying that after applying `P_j`, only interactions with indices within 3 of j survive.

## 3. Bony decomposition audit: low–high interactions

The standard paraproduct contains terms of the form

\[
T_u u=\sum_k S_{k-1}u\,\Delta_k u.
\]

After output projection at frequency `j`, the high factor has `k≈j`, but the low factor is

\[
S_{j-1}u=\sum_{\ell<j-1}\Delta_\ell u,
\]

which contains **all lower frequencies**, not just `j±3`.

Thus a correct shell estimate has a low-frequency factor such as

\[
\|S_{j-1}u\|_\infty\,2^j\|u_j\|_2,
\]

or an equivalent sum over lower shells. It cannot in general be replaced by a constant depending only on the finitely many neighboring shell energies.

A simple amplitude test shows the obstruction. Let a fixed low-frequency divergence-free mode have amplitude `A` and a high mode near `2^j` have amplitude `B`. The low–high output near `2^j` scales like

\[
A\,B\,2^j.
\]

Its squared L2 size is of order

\[
A^2B^2 4^j,
\]

whereas the proposed neighboring-shell right side is of order

\[
B^2 4^j
\]

with a data-independent constant. Taking `A` arbitrarily large contradicts such an estimate whenever the interaction coefficient is nonzero.

## 4. High–high to low audit

The Bony remainder contains comparable high-frequency interactions. Two large Fourier modes `p,q` can satisfy

\[
|p|\sim|q|\gg2^j,
\qquad
p+q\sim2^j,
\]

through near cancellation. Therefore low output can receive contributions from arbitrarily high shells.

So the stronger assertion

\[
\text{output shell }j\Rightarrow\text{both inputs lie in }j\pm3
\]

is false in both low–high and high–high directions.

## 5. Propagation through the manuscript

The same width-3 statement is used in:

- Section 3 shell/shape drift;
- Lemma 5.1 windowed Duhamel inequality;
- Lemma 5.3 banded Grönwall;
- the UV-front jump ledger;
- the vorticity window estimate leading to BKM finiteness.

Thus this is a root dependency rather than an isolated appendix typo.

## 6. Version-history note

A related later abstract describes the method as yielding closure only under governing assumptions and says highly intermittent within-window concentration remains an obstruction. That weaker formulation is materially more defensible than the version claiming unconditional global regularity. The audit should preserve this distinction.

## 7. Surviving ideas

Potentially useful components include:

- dyadic shape observables;
- front/stopping-time bookkeeping;
- heat-semigroup damping on fixed frequency bands;
- a Duhamel ledger that keeps **all** low–high/high–high forcing terms explicitly;
- finite-overlap packing after a valid interaction estimate is established.

## 8. Regression test for the internal M17 chain

M17-300 must never replace the localized forcing `F_j` by a purely nearest-neighbor band without proving a symbol-level estimate. In particular:

\[
\boxed{\text{low–high and high–high→low leakage must remain explicit.}}
\]

This external failure is therefore a direct DSD regression test for the current growing-lag LAG attempt.

## 9. DSD verdict

\[
\boxed{
\text{The finite width-3 nonlinear closure used by the global argument is false.}
}
\]

Consequently the shape/front/Duhamel/BKM chain does not establish unconditional global regularity as written.

Global regularity remains unproved.
