# DSD heuristic companion for M17-322 — channel separation for line-weight memory

Date: 2026-09-08  
Status: **HEURISTIC ONLY / NOT A PROOF ASSUMPTION**

## Scope firewall

This note records a DSD-theoretical heuristic used only to suggest a change of variables.  The canonical Navier–Stokes module M17-322 must be justified entirely by the standard mathematical identities written there.

No Formation Axiom, describability axiom, structural-gravity postulate, or other DSD theoretical statement is imported as a hypothesis of the PDE proof.

## DSD heuristic

A composite observable can hide cancellation between structurally distinct channels.  Before assigning a persistent contrast to one mechanism, split the observable into channels whose evolution laws have different sources.

For the late CE-H vortex-line bookkeeping, the composite line weight is

\[
l=\log L_\rho.
\]

The existing exact line laws suggest the channel variables

\[
u:=\log\Phi,
\qquad
z:=\log\frac{L_\rho}{\Phi},
\qquad
l=u+z.
\]

The intended interpretation is only heuristic:

- `u` tracks the material-flux/amplitude channel;
- `z` tracks the strain-residence channel;
- `l` is their composite observable.

## Standard-math translation target

The companion canonical module should verify directly that

\[
\dot u=\kappa,
\qquad
\dot z=2\bar\sigma_\rho-\frac12,
\qquad
\dot l=\kappa-\frac12+2\bar\sigma_\rho.
\]

Hence a pairwise line-weight contrast obeys

\[
\Delta l=\Delta u+\Delta z.
\]

A nonzero persistent line-weight contrast therefore cannot be attributed to an unspecified `memory` without first testing the two typed alternatives

\[
\text{flux-ratio memory}
\quad\lor\quad
\text{strain-residence-ratio memory}.
\]

## Audit rule

The DSD heuristic ends once the variables are proposed.  Every later implication must be proved from the displayed PDE/line identities.  In particular, neither type of memory is declared impossible merely because it is structurally distinct.
