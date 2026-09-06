# DSD Audit — Zhang Weak-Regularity / Mollifier–Galerkin Double-Limit Framework

Date: 2026-09-06
Source: JiaHong Zhang, *Global Smooth Solutions to the 3D Incompressible Navier-Stokes Equations: Weakly Regular Framework and Multi-Scenario Adaptation*, Preprints 202601.0992.v1, Jan 2026.
Source DOI: 10.20944/preprints202601.0992.v1
Audit status: **FAIL_ROOT AT HIGH-ORDER SMOOTHNESS UPGRADE; ENERGY/WEAK-COMPACTNESS PART SURVIVES**

## 1. Public claim

The manuscript claims global smoothness and uniqueness for initial data ranging from high Sobolev regularity down to merely `L^2`, using compactly supported mollification, Galerkin approximation, uniform double-limit energy estimates, and a high-order bootstrap.

The approximation-level energy/compactness argument is conceptually standard and is not the open problem. The decisive issue is the transition from the Leray-level limit

\[
u\in L^\infty_tL^2_x\cap L^2_tH^1_x
\]

to global `H^\infty` regularity.

## 2. What the manuscript actually establishes before the smoothness step

Section 3.2 gives approximation-uniform energy estimates of the form

\[
\sup_{N,\varepsilon}\sup_{t\in[0,T]}\|u_{N,\varepsilon}(t)\|_2^2<\infty,
\]

and

\[
\sup_{N,\varepsilon}\int_0^T\|\nabla u_{N,\varepsilon}(t)\|_2^2dt<\infty.
\]

Section 3.3 then invokes Aubin-Lions and obtains a limit in the standard weak-energy class

\[
 u\in L^\infty([0,\infty);L^2)\cap L^2_{loc}([0,\infty);H^1).
\]

This is a legitimate weak-compactness level, subject to the usual approximation details. It does not itself imply regularity.

## 3. Root gap A — the high-order induction does not have its stated base case

Section 4.1.1 claims to prove

\[
\partial_t^m\nabla^k u\in L^\infty([\delta,T];L^2)
\]

for all `m,k` by double induction.

The manuscript lists as basis cases:

- `m=0,k=0`: `L^2` boundedness;
- `m=0,k=1`: previously established `L^2_loc`-integral boundedness.

But the induction statement requires for `k=1`

\[
\nabla u\in L^\infty([\delta,T];L^2),
\]

whereas the earlier energy estimate gives only

\[
\nabla u\in L^2([0,T];L^2).
\]

These are different assertions:

\[
\boxed{
L^2_tH^1_x\not\Rightarrow L^\infty_tH^1_x.
}
\]

Thus the stated induction begins with a base property that has not been established.

This is not a cosmetic omission: obtaining uniform-in-time `H^1` control for arbitrary large 3D data is already a regularity-level estimate.

## 4. Root gap B — differentiating an `L^2` forcing term

The weak-regularity setup assumes only

\[
f\in L^2([0,\infty);L^2(\mathbb R^3)).
\]

But in the inductive step Section 4.1.1 says to apply

\[
\partial_t^M\nabla^K
\]

to both sides of the Navier-Stokes equation and then states that the external-force term is directly controlled by the `L^2` assumption.

For `M+K>0`, this operation produces derivatives such as

\[
\partial_t^M\nabla^K f,
\]

which are not defined or controlled under the stated `L^2_tL^2_x` hypothesis.

Therefore the claimed high-order induction does not close under the paper's own weak-force assumptions:

\[
\boxed{
f\in L^2_tL^2_x
\not\Rightarrow
\partial_t^M\nabla^K f\in L^2.
}
\]

For the unforced Clay problem `f=0`, this particular obstruction disappears, but Root gap A remains.

## 5. Root gap C — commutator uniformity is asserted after the missing regularity

Section 4.3 states

\[
\sup_{N,\varepsilon}
\|\operatorname{Comm}_k(u_{N,\varepsilon},u_{N,\varepsilon})\|_2
\le C_k.
\]

The stated Moser/Gagliardo-Nirenberg control consumes quantities such as `||grad u||_infinity` and higher Sobolev norms. Those are precisely the quantities the preceding induction is supposed to establish.

A bound independent of `N,epsilon` must be derived from already-available uniform norms; it cannot be declared after assuming the strong norms needed to estimate the commutator.

Thus the manuscript needs an independent, noncircular estimate that upgrades the Leray-level bounds to a continuation norm.

## 6. Finite-dimensional ODE boundedness does not repair the continuum gap

Section 4.4 correctly uses the energy cancellation of the Galerkin convective term to show a fixed finite-dimensional coefficient vector has bounded `L^2` energy and the approximate ODE extends globally.

However

\[
\boxed{
\text{global finite-dimensional Galerkin trajectory}
\not\Rightarrow
\text{uniform high-Sobolev bound as }N\to\infty.
}
\]

This is exactly why Galerkin approximations already yield global Leray weak solutions without resolving 3D regularity.

## 7. Additional notation/embedding issue

The manuscript writes an embedding in the form `H^s(R^3) subset C^infty(R^3)` for `s>3/2`. A fixed finite Sobolev exponent above `3/2` gives continuity/Hölder-type control appropriate to the precise exponent, not `C^infty`. Smoothness follows only if one has all sufficiently high Sobolev norms, which is again the missing induction conclusion.

This issue is secondary to the two root gaps above but points in the same direction: finite Sobolev regularity is being promoted too quickly to arbitrary smoothness.

## 8. DSD inheritance audit

The valid chain reaches

\[
\text{regularized/Galerkin smooth approximants}
\to
\text{uniform }L^2_tH^1_x\text{ energy control}
\to
\text{weak-energy limit}.
\]

The manuscript then attempts

\[
\text{weak-energy limit}
\to
L^\infty_tH^1_x
\to
H^k\ \forall k
\to
C^\infty.
\]

The first arrow is not established, and the later differentiated-force argument exceeds the stated hypotheses.

## 9. Verdict

The global smoothness claim in this version does not follow from the displayed proof.

\[
\boxed{
\text{FAIL_ROOT: high-order regularity bootstrap consumes an unproved }L^\infty_tH^1_x\text{ base and unavailable force derivatives.}
}
\]

Surviving portion:

\[
\boxed{
\text{mollifier/Galerkin energy compactness remains a weak-solution construction framework.}
}
\]

This verdict is version-specific and does not judge the author. A revised proof would need a genuinely approximation-uniform critical/higher-order estimate that supplies the missing `L^\infty_tH^1_x` base without assuming regularity.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
