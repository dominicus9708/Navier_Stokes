# M19-205 — If nonsymmetry unit kernels are removed, long-period RDSS cannot shadow isolated relative-periodic attractors and merges into aperiodic or compactness loss

**Date:** 2026-09-14  
**Status:** CONDITIONAL BRANCH MERGER / LONG-PERIOD REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

The retained hard-cocycle analysis provides:

1. essential transverse growth strictly below zero;
2. no positive hard Lyapunov exponents on the scattering-observable bundle;
3. finite-dimensional unit/zero hard spectrum.

Assume additionally the remaining bounded-period theorem:

\[
\boxed{
\text{after time/rotation quotient, no nonsymmetry unit multiplier exists.}
}
\]

## 2. Relative-periodic orbit becomes transversely attracting

Under this assumption every non-symmetry transverse multiplier of a bounded-period RSS/RDSS orbit lies strictly inside the unit circle. Therefore, after fixing the symmetry gauge, the relative-periodic orbit is a locally attracting isolated periodic orbit of the quotient semiflow.

In particular there is a neighborhood \(\mathcal N\) such that any orbit entering sufficiently deeply into \(\mathcal N\) remains in the attracting basin and converges to that periodic orbit. It cannot spend an arbitrarily long time shadowing the orbit and then leave along an unaccounted neutral/unstable direction.

## 3. Long-period invariant-measure limit

Let \(\mathcal O_n\) be relative-periodic quotient orbits with periods

\[
S_n\to\infty
\]

inside a compact corridor, and let \(\mu_n\) be their normalized orbit measures. Any weak-* limit \(\mu\) is invariant.

Suppose every ergodic component of \(\mu\) were supported on bounded-period relative-periodic orbits satisfying the above kernel rigidity. Those periodic orbits are isolated attractors in the quotient.

Compactness plus isolation prevents an infinite family of distinct such orbits from accumulating inside the same compact solution set without producing a new degeneracy. Thus only finitely many can lie in the retained compact stratum.

A distinct long periodic orbit cannot spend asymptotically full fractions of its period near these attracting cycles and repeatedly exit their attracting neighborhoods. Hence such a measure cannot arise from \(S_n\to\infty\) unless one of the assumptions fails.

## 4. Conditional long-period reduction

Therefore

\[
\boxed{
S_n\to\infty
\Longrightarrow
\begin{cases}
\text{genuinely aperiodic invariant ergodic component},\\
\text{nonsymmetry unit/kernel degeneracy},\\
\text{compactness/spectral-bundle degeneration}.
\end{cases}
}
\]

If the bounded-period kernel theorem and compactness corridor are certified, this simplifies to

\[
\boxed{
S_n\to\infty
\Longrightarrow
\text{aperiodic invariant component}.
}
\]

## 5. Main consequence

The long-period branch is not an independent final analytic theorem once the two harder ingredients are available:

- aperiodic recurrent hard dynamics is excluded;
- bounded-period nonsymmetry unit kernels are excluded.

Thus the active analytic frontier can be reduced from three nominal branches to two coupled theorem problems, plus compactness/root certification.