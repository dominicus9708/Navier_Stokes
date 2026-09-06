# DSD Audit — McCall Klein Topology and the Five Pillars

Date: 2026-09-06
Source: Timothy McCall, *Global Regularity for Navier-Stokes Equations via Klein Topology and the Five Pillars*, DOI 10.5281/zenodo.18237843, Jan 2026.
Audit status: **SYMMETRY-SUBSPACE INVARIANCE GATE FAILS UNLESS AN EXTRA CANCELLATION/PROJECTION THEOREM IS PROVED**

## 1. Public architecture

The manuscript introduces the affine involution

\[
\sigma(x,y,z)=(-x,-y,-z+\pi)
\]

on the torus and decomposes the velocity into Klein-odd and Klein-even components,

\[
u=u_P+u_Q.
\]

The public abstract claims:

- the vortex-stretching term vanishes identically for the Klein-odd component `u_P`;
- the even/unstable component `u_Q` decays exponentially by asymptotic symmetrization;
- the full solution converges to the regulated Klein-symmetric subspace.

The theorem is claimed for arbitrary smooth divergence-free initial data.

## 2. Equivariance audit

Let `S` denote the linear action on vector fields induced by the spatial involution, chosen so that the classical NSE is equivariant:

\[
S B(u,v)=B(Su,Sv),
\]

where `B(u,v)` denotes the projected bilinear convective term.

Suppose

\[
Su_P=-u_P,
\qquad
Su_Q=+u_Q.
\]

Then bilinearity gives

\[
S B(u_P,u_P)
=B(-u_P,-u_P)
=B(u_P,u_P).
\]

Therefore

\[
\boxed{B(u_P,u_P)\text{ lies in the even sector}.}
\]

Similarly,

\[
B(u_Q,u_Q)\in Q,
\]

while the mixed terms belong to the odd sector.

## 3. Consequence: the odd sector is not automatically invariant

If at some instant

\[
u_Q=0,
\]

the even component equation contains the forcing

\[
\partial_tu_Q
\supset -P_QB(u_P,u_P).
\]

Parity alone does not make this term vanish. Indeed parity says it belongs precisely to the even sector.

Thus:

\[
\boxed{
\text{Klein-odd initial data}
\not\Rightarrow
\text{Klein-odd evolution}
}
\]

unless the manuscript proves an additional identity

\[
P_QB(u_P,u_P)=0
\]

for the entire claimed subspace.

A statement that the **vortex-stretching scalar** vanishes on `u_P` is weaker than vanishing of the full even-sector quadratic velocity forcing.

## 4. Arbitrary-data audit

For arbitrary initial data the even component `u_Q(0)` is generally nonzero. Therefore global regularity requires a genuine dissipative estimate for the coupled system, not merely regularity of the odd subspace.

The crucial theorem must control

\[
\frac d{dt}\|u_Q\|^2
\]

against:

- self-interaction `B(u_Q,u_Q)`;
- forcing `B(u_P,u_P)`;
- mixed odd/even couplings;
- pressure/Leray projection effects.

Barbalat's lemma can convert integrability plus uniform continuity into convergence; it does not create the sign/coercive estimate needed to make `u_Q` integrable or decaying.

## 5. External topological constraint audit

The abstract describes the stable behavior as arising from an “external topological constraint.” Two cases must be separated:

### Case A — the constraint is a theorem of the original NSE

Then one must prove that every arbitrary NSE trajectory dynamically satisfies it despite the quadratic parity coupling above.

### Case B — the evolution is explicitly projected/regulated into the Klein-odd subspace

Then the equation has been modified. A projected dynamics may be globally regular but is not automatically equivalent to the unrestricted classical NSE.

## 6. Lean verification scope

Machine verification that a symbolic identity holds for `u_P` is valuable but only proves that identity under its formal hypotheses. It does not prove:

- invariance of the `P` subspace;
- decay of `Q`;
- applicability to arbitrary initial data;
- equivalence of a projected flow to classical NSE.

The global bridge remains a separate theorem.

## 7. Surviving value

Potentially useful results include:

- parity decomposition under affine torus symmetries;
- exact cancellation of selected stretching terms on symmetry classes;
- conditional regularity for symmetry-constrained data;
- estimates for odd/even transfer if derived with correct bilinear bookkeeping.

## 8. DSD verdict

The quadratic NSE coupling sends odd×odd interactions into the even sector. Therefore the regulated odd subspace is not invariant by symmetry alone.

\[
\boxed{
\text{The unconditional asymptotic-symmetrization bridge requires a missing/nontrivial coupling theorem.}
}
\]

If the paper enforces the symmetry by external projection rather than derives it, it addresses a modified evolution.

Global regularity remains unproved.
