# M19 Current Frontier

**Date:** 2026-09-13  
**Current tip:** **M19-177**  
**Status:** ACTIVE CALCULATION / RECURRENT HARD-DIMENSION THRESHOLD + RELATIVE-PERIODIC HARD CORE / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase policy

M18 remains frozen as the analysis/audit family. M19 is the active calculation/closure family.

\[
\boxed{\text{M18 certified analysis}\Longrightarrow\text{M19 calculation}\Longrightarrow\text{closure or explicit theorem frontier}.}
\]

## 2. Retained reduction through M19-156

The quiet remote/ancestry/weak-critical survivors have been reduced, at their certified scope, to the recurrent critical-scattering complex.

The linearized-vorticity identity is

\[
\frac12\frac d{ds}\|\eta\|_2^2
+\nu\|\nabla\eta\|_2^2
+\frac14\|\eta\|_2^2
=\mathcal C_U[W].
\]

Critical-tail coupling is relatively compact with respect to the bare similarity-vorticity generator, so

\[
\boxed{\lambda_{ess}\le-1/4<0.}
\]

Uniform scattering observability plus differentiated scattering covariance remove positive hard Lyapunov exponents. The remaining complete hard dynamics is finite-dimensional and zero/unit-growth.

The exact time/rotation symmetry representation must be quotiented before classifying unit multipliers. Moderate RSS and bounded-period RDSS are compact finite-amplitude low-mode hard sets; long period `S->infinity` remains a separate invariant-measure escape.

## 3. Kernel becomes a finite compact-core Hermitian problem — M19-157--161

Abstract quasi-compactness and isometry do **not** imply kernel rigidity.

For a hard perturbation define the period/mean damping-minus-compensation form

\[
\overline H
=\nu\overline D+\frac14\overline G-\overline C.
\]

Kernel rigidity is a finite-dimensional smallest-eigenvalue/sign problem after symmetry quotient.

Compact hard fibers also give a uniform vorticity Poincare ratio

\[
\boxed{
\int\|\nabla\eta\|_2^2
\ge\lambda_P\int\|\eta\|_2^2,
\qquad\lambda_P>0,
}
\]

raising the neutral compensation threshold to

\[
\boxed{\Lambda_{hard}=1/4+\nu\lambda_P>1/4.}
\]

For a fixed `mu=1` eigenspace, every extra nonsymmetry kernel direction consumes an additional compact-core compensation eigenchannel above this threshold.

The compensation operator splits into

\[
\boxed{
\mathcal C_U[W]
=\int\eta\cdot S_U\eta
+\mathcal C_{\nabla\Omega}[W].
}
\]

Trace-free strain does not force a one-channel rank bound. Every superthreshold channel is nevertheless localized to a finite compact core; the `r^-2` critical strain tail is unthresholded-CLR borderline but cannot itself sustain a strict superthreshold channel.

## 4. Collective anisotropy tensor and the 5/4 gap — M19-162--167

For a hard family define

\[
\Gamma=\sum_j\eta_j\otimes\eta_j,
\qquad
Q=\Gamma-\frac{\operatorname{tr}\Gamma}{3}I.
\]

Incompressibility removes the isotropic strain trace:

\[
\boxed{
\sum_j\int\eta_j\cdot S_U\eta_j
=\int S_U:Q.
}
\]

The exact traceless tensor evolution has bare damping

\[
\boxed{
\frac12\frac d{ds}\|Q\|_2^2
+\nu\|\nabla Q\|_2^2
+\frac54\|Q\|_2^2
=\text{anisotropy sources},
}
\]

and the local rotation commutator contributes zero to this energy.

The forcing tuple is

\[
\boxed{
\Sigma_E=(\rho S,\mathcal G^\circ,\mathcal F^\circ).
}
\]

Scalar density alone does not determine `Q`. For a fixed full source tuple the tensor response is linear and its homogeneous tensor cocycle is quasi-compact with

\[
\boxed{\lambda_{ess,Q}\le-5/4.}
\]

However scattering/fiber orthogonality does not cancel polarized cross-tensor forcing, so the tensor gap is an auxiliary coercive structure rather than a direct kernel proof.

## 5. Real hard monodromy and the dimension-one target — M19-168--174

After exact symmetry quotient, the real hard twisted monodromy is orthogonal in the scattering pullback metric:

\[
\boxed{\mathcal M_q^{tw}\in O(N).}
\]

A genuinely irrational elliptic block requires a two-dimensional real invariant plane. Hence

\[
\boxed{N:=\dim_{\mathbb R}E_q^{hard}\le1}
\]

eliminates all genuinely irrational elliptic neutral dynamics; the only residual one-dimensional unit behavior is a finite-iterate kernel (`+1` or `-1`).

More importantly, on a one-dimensional-or-smaller quotient center, the local recurrent return is an interval homeomorphism. Orientation-preserving recurrence is fixed and orientation-reversing recurrence has period at most two. Thus

\[
\boxed{
N\le1
\Longrightarrow
\text{recurrent hard dynamics is relative-periodic after at most two quotient returns}.
}
\]

Therefore full kernel rigidity is **not** required before eliminating aperiodic recurrence.

## 6. Collective trace is sublinear in hard dimension — M19-169--172

For the whole quotient hard family, orthogonal/unitary return gives the exact total compensation trace identity. The local strain trace obeys the Lieb--Thirring estimate

\[
\boxed{|T_{strain}|
\lesssim\|S_U\|_{5/2}P_N^{3/5}.}
\]

The nonlocal gradient-vorticity trace obeys, for `3/2<a<3`,

\[
\boxed{
|T_{nl}|
\lesssim
\|\nabla\Omega\|_a
Z_N^{\,11/6-5/(2a)}
P_N^{\,3/(2a)-1/2},
}
\]

with total collective degree

\[
\boxed{d(a)=\frac43-\frac1a<1.}
\]

As `a->3/2+`, `d(a)->2/3`, though the endpoint HLS constant degenerates.

Both local and nonlocal compensation traces are therefore collective-sublinear. This gives a uniform finite hard-dimension ceiling.

## 7. Authoritative recurrent extension — M19-175

The earlier period-based trace formulation must not be used circularly to prove periodicity.

For any compact recurrent hard component, transport a complete hard frame and define

\[
Z_N(s)=\sum_j\|\eta_j(s)\|_2^2,
\quad
P_N(s)=\sum_j\|\nabla\eta_j(s)\|_2^2,
\quad
T_N(s)=\sum_j\mathcal C_U[W_j(s)].
\]

Then

\[
\frac12Z_N'+\nu P_N+\frac14Z_N=T_N.
\]

Boundedness kills the long-time boundary term, giving on a general recurrent component

\[
\boxed{
\langle T_N\rangle
=\nu\langle P_N\rangle+\frac14\langle Z_N\rangle.
}
\]

Thus the dimension criterion applies **before** relative periodicity is known.

## 8. Cesaro vorticity-mean normalization — M19-176

On a finite recurrent hard fiber define the Cesaro pulled-back vorticity metric

\[
G_T
=\frac1T\int_0^T
\Phi_t^*(\operatorname{curl})^*(\operatorname{curl})\Phi_t\,dt.
\]

A positive subsequential mean metric `G_infinity` exists on each retained recurrent component. Choosing a `G_infinity`-orthonormal hard basis gives

\[
\boxed{\langle Z_N\rangle=N.}
\]

Hence the arbitrary lower normalization constant `g_-` disappears from the two-mode criterion.

The remaining intrinsic frame issue is the mean-to-instantaneous occupation/distortion constant

\[
\boxed{\kappa_{occ}.}
\]

## 9. Constant audit — M19-177

Most other constants descend to the already retained smooth background/tail package.

The hard derivative ratio can be bounded by

\[
\boxed{
\Lambda_P^+
\lesssim
\nu^{-2}Z_+^{1/2}P_+^{1/2}
+
\nu^{-1}P_+^{1/4}H_+^{1/4}.
}
\]

Critical strain satisfies

\[
\boxed{
M_{5/2}
\lesssim
Z_+^{7/20}P_+^{3/20}.
}
\]

For `2<=a<3`, `M_a=\sup\|\nabla\Omega\|_a` descends to `P_+,H_+`; for `3/2<a<2`, a core/tail split gives

\[
\boxed{
M_a
\lesssim
R^{3(1/a-1/2)}P_+^{1/2}
+
C_{tail}(3a-3)^{-1/a}R^{3/a-3}.
}
\]

Thus the cleanest genuinely new quantitative constant in the `N=2` test is currently `kappa_occ`; the other corridor bounds are known finite but generally not sharply numerical.

## 10. Current live analytic targets after M19-177

### A. Aperiodic branch — dimension-one threshold

The primary target is now

\[
\boxed{\mathcal T_{dim1}:\dim_{\mathbb R}E_q^{hard}\le1.}
\]

In the Cesaro normalization the exact sufficient test has the form

\[
\boxed{
\widetilde C_{str}2^{-2/5}
+\widetilde C_a2^{d(a)-1}
<\frac14
}
\]

for some `3/2<a<3`.

If this is certified, M19-173 reduces every recurrent hard survivor to RSS/RDSS after at most a two-fold quotient return.

The immediate quantitative obstruction is control of `kappa_occ` and sharpening of the symbolic corridor constants.

### B. Relative-periodic hard core

After the aperiodic reduction, the remaining RSS/RDSS branch is compact finite-amplitude/low-mode except for the already typed long-period `S->infinity` escape.

Fixed-moduli nonsymmetry kernel degeneracy remains the main local Fredholm obstruction for moderate compact components; rational elliptic phases reduce to finite-iterate kernels, while exact rotation-symmetry elliptic multipliers are quotiented.

### C. Long-period branch

`S->infinity` remains an invariant-measure/compactness problem and shares the same recurrent hard-dimension structure on its limiting compact components.

## 11. Final proof-chain certification remains open

Even if the active analytic targets close, global regularity still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness and remaining alignment/nonreuse checks;
3. full beginning-to-end independent audit.

## 12. Permanent firewalls

\[
\boxed{\text{finite hard dimension}\neq\text{dimension one}},
\]

\[
\boxed{\text{finite corridor bounds}\neq\text{constants small enough for }N<2},
\]

\[
\boxed{\text{mean normalization}\neq\text{instantaneous occupation control}},
\]

\[
\boxed{\text{tensor 5/4 gap}\neq\text{automatic tensor-source smallness}},
\]

\[
\boxed{\text{relative periodicity}\neq\text{relative-periodic nonexistence}},
\]

\[
\boxed{\text{root-class merger}\neq\text{analytic closure}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-177.}}
\]
