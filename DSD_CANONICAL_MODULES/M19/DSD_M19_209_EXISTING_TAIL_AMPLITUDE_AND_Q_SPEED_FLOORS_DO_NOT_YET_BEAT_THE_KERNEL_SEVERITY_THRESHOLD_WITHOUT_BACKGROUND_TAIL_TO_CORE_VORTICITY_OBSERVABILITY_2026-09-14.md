# M19-209 — Existing tail-amplitude and q-speed floors do not yet beat the kernel-severity threshold without background tail-to-core vorticity observability

**Date:** 2026-09-14  
**Status:** EXPLICIT BRIDGE FRONTIER / NO OVERCLAIM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Two sides of the moderate kernel problem

The retained relative-periodic analysis supplies lower bounds on the critical tail, including:

- nonzero cubic critical-tail mass;
- nonzero q-speed on singular survivors;
- RSS rotational anisotropy/spiral charge;
- finite low-mode tail reduction on bounded-period corridors.

M19-208, on the other hand, says a nonsymmetry kernel requires

\[
\boxed{\frac{K\Gamma W}{\nu}\ge\chi_*>0.}
\]

## 2. Why the current tail floors do not immediately contradict the kernel threshold

The tail amplitude and q-speed bounds control the far-field scattering profile \(A\) and its q/angular derivatives. The quantity \(K=\|\Omega\|_\infty\) in the W1 kernel threshold is a background vorticity amplitude on the full similarity state.

A nonzero \(r^{-1}\) divergence-free tail necessarily has nonzero vorticity at finite radius, but converting the asymptotic tail norm into a **uniform quantitative lower bound** for the full/core \(K\) with constants strong enough to compare against \(\chi_*\) requires a background tail-to-core observability estimate.

M19-144 supplies such a quantitative equivalence for the **rotation tangent**

\[
\mathcal R U\leftrightarrow \mathcal R_\omega A,
\]

not for the background vorticity amplitude itself.

## 3. Additional constant issue

The threshold \(\chi_*\) also contains weighted Calderon--Zygmund and A2-gap constants. Their finiteness is certified, but the repository does not currently contain sharp enough numerical values to compare the existing tail lower bounds with \(\chi_*\).

## 4. Correct bridge statement

A sufficient bridge would have the form

\[
\boxed{
K\ge c_{bg}\,\mathcal N(A)
}
\]

for a suitable nonzero scattering-tail norm \(\mathcal N(A)\), uniformly over the moderate compact RSS/RDSS corridor, together with compatible quantitative bounds for \(\Gamma\) and \(W\).

If the resulting lower/upper constants placed every moderate state below the kernel-compensation threshold, kernel rigidity would follow. No such certified comparison is presently available.

## 5. Verdict

The moderate kernel hard core has therefore been reduced to a concrete quantitative bridge rather than an abstract spectral mystery, but it is not closed:

\[
\boxed{
\text{tail floors + finite resonance structure}
\quad\not\Rightarrow\quad
\text{kernel nonexistence}
}
\]

without background tail-to-core vorticity observability / sharp constant comparison.

This is now the principal bounded-period RSS/RDSS analytic frontier.