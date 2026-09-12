# M19 Current Frontier

**Date:** 2026-09-12  
**Current tip:** **M19-130**  
**Status:** ACTIVE CALCULATION / FINITE-DIMENSIONAL TRANSVERSE SPECTRUM + RSS/RDSS TWISTED TAIL + FINITE OBSERVABILITY / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase policy

M18 remains frozen as the analysis/audit family. M19 is the active calculation/closure family.

\[
\boxed{\text{M18 certified analysis}\Longrightarrow\text{M19 calculation}\Longrightarrow\text{closure or explicit theorem frontier}.}
\]

## 2. Retained reduction through M19-118

The quiet CE-H/current, remote and cubic ancestry-conversion survivors have been reduced, at their certified scope, to the recurrent weak-critical scattering complex.

The pressure-free linearized-vorticity identity has the exact quarter-gap

\[
\frac12\frac d{ds}\|\eta\|_2^2+\nu\|\nabla\eta\|_2^2+\frac14\|\eta\|_2^2=\mathcal C_U[W].
\]

Critical-tail coefficients are relatively compact perturbations of the bare similarity-vorticity generator, hence

\[
\boxed{\lambda_{ess}\le-1/4<0,\qquad \dim E^{\ge0}<\infty.}
\]

Thus the formal infinite-dimensional scattering center is reduced to a finite-dimensional interior spectral problem.

For RSS/RDSS, principal intrinsic variables are

\[
\boxed{S=2\log\lambda,\qquad \beta=\operatorname{Angle}(Q_*)\in[-\pi,\pi].}
\]

The twisted monodromy

\[
\mathcal M_S^{tw}=Q_*^{-1}\mathcal U(s+S,s)
\]

inherits

\[
\boxed{r_{ess}(\mathcal M_S^{tw})\le e^{-S/4}<1.}
\]

## 3. Long-period invariant-measure reduction — M19-119

For a long-period sequence \(S_n\to\infty\), use the quotient-periodic invariant measures

\[
\mu_n=\frac1{S_n}\int_0^{S_n}\delta_{[U_n(s)]}\,ds.
\]

On a compact corridor, subsequential limits are invariant probabilities. Their ergodic components are RSS, finite-period relative-periodic components, genuinely aperiodic recurrent components, or arise only after compactness loss.

## 4. Authoritative dynamical correction — M19-120

The previous shortcut

\[
E^c_{extra}=0\Longrightarrow\text{RSS/RDSS only}
\]

is **not valid in general**. A hyperbolic recurrent flow may have one-dimensional center equal to the flow tangent and still possess stable/unstable directions and aperiodic recurrence.

The correct transverse target is stronger:

\[
\boxed{E_{\perp}^{\ge0}=0}
\]

or equivalently

\[
\boxed{\lambda_{top}^{\perp}<0.}
\]

This correction supersedes any use of M19-103 that inferred RSS/RDSS solely from the absence of an extra zero center.

## 5. Transverse Ky-Fan/Morse budget — M19-121--123

For the top \(m\) transverse Lyapunov directions,

\[
\boxed{
\sum_{j=1}^m\lambda_j^{\perp}
\le
-\frac m4
-\nu\left\langle\sum_{j=1}^m\|\nabla\eta_j\|_2^2\right\rangle
+\left\langle\sum_{j=1}^m\lambda_j^+(s)\right\rangle.
}
\]

Hence any nonnegative transverse spectrum needs compact-core amplification of at least \(m/4\) on average. The immediate spectral problem is to rule out a second quarter-gap-compensating channel after the time/rotation symmetry directions are removed.

Long-period RDSS complexity and aperiodic recurrence therefore share the same transverse-spectral obstruction rather than forming independent roots.

## 6. RSS torque and exact spiral tail — M19-124--127

For RSS, similarity-time symmetry plus scattering covariance forces

\[
\boxed{\partial_qA=-2\alpha\mathcal R_\omega A,}
\]

hence

\[
\boxed{A(q)=e^{-2\alpha q\mathcal R_\omega}A(0).}
\]

The radial derivative square contains the exact positive anisotropy cost

\[
\boxed{\|\partial_qA-A\|_2^2=\|A\|_2^2+4\alpha^2\|\mathcal R_\omega A\|_2^2.}
\]

Tail rotational anisotropy is observable at a finite spectator annulus because the scattering derivative is near identity, but a quantitative reverse estimate from the compact core to the leading tail remains nontrivial.

## 7. RDSS twisted log-radius spectrum — M19-128--129

RDSS scattering obeys

\[
\boxed{A(q+L)=Q_*^{-1}A(q).}
\]

After untwisting by principal holonomy \(\beta\), log-Fourier/angular modes have mismatch

\[
\boxed{\delta_{n,m}(\beta)=2\pi n-m\beta}
\]

and radial frequency

\[
\boxed{\frac{2\pi n-m\beta}{L}.}
\]

Thus the critical shell charge contains a positive term comparable to

\[
1+\frac{(2\pi n-m\beta)^2}{L^2}+c_{ang}\ell(\ell+1).
\]

On bounded-period corridors with a shell-H1 ceiling and a positive mean cubic-tail floor, high modes cannot carry all critical cubic mass. A nontrivial finite-dimensional low-mode tail core remains.

## 8. Finite-dimensional interior-to-tail observability — M19-130

Let \(E_F\) be the finite-dimensional interior hard Floquet/spectral space. Under the retained parabolic unique-continuation application gate, a mode that vanishes on an open finite spectator spacetime cylinder vanishes identically. Hence the spectator observation is injective on \(E_F\).

Composing with the near-identity scattering derivative preserves injectivity. Because \(E_F\) is finite-dimensional, finitely many scattering observables can be selected so that

\[
\boxed{\mathbf O:E_F\to\mathbb C^M}
\]

has full column rank for a fixed background.

The remaining observability issue is **uniformity over the compact recurrent/periodic corridor**:

\[
\boxed{\sigma_{min}(\mathbf O)\ge c_{obs}>0.}
\]

## 9. Current live analytic problems after M19-130

1. **Transverse spectral theorem**
   \[
   \boxed{E_{\perp}^{\ge0}=0}
   \]
   by excluding a second compact-core quarter-gap compensation channel.

2. **Moderate RSS/RDSS nonlinear hard core**: exclude finite-amplitude relative-periodic survivors in the intrinsic \((S,\beta)\) variables, using the spiral/twisted tail structure and finite-dimensional Floquet reduction.

3. **Uniform observability**: upgrade pointwise finite-dimensional injectivity to a corridor-uniform lower singular-value bound, or isolate the exact spectral-bundle degeneration that prevents it.

4. **External theorem applicability**: certify Type-I, pressure-annulus and unique-continuation hypotheses before importing external regularity/Liouville results into the global root chain.

## 10. Final proof-chain certification remains open

Even if the active analytic problems close, global regularity still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness and remaining alignment/nonreuse checks;
3. full beginning-to-end independent audit.

## 11. Permanent corrections/firewalls

\[
\boxed{\text{symmetry-only center}\neq\text{symmetry-only recurrent dynamics}},
\]

\[
\boxed{\text{orbit period/group drift}\neq\text{free external PDE parameter}},
\]

\[
\boxed{\text{augmented nondegeneracy}\neq\text{periodic-orbit nonexistence}},
\]

\[
\boxed{\text{pointwise injectivity}\neq\text{uniform observability}},
\]

\[
\boxed{\text{root-class merger}\neq\text{analytic closure}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-130.}}
\]
