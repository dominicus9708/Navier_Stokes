# Correction Notice — M17-144 through M17-147

Date: 2026-09-08  
Status: **ACTIVE CORRECTION NOTICE / READ BEFORE REUSING M17-144--147**

This notice preserves the historical modules unchanged while making the later exact CE-H correction explicit.

## Controlling identity

On exact CE-H,

\[
\Delta W=\kappa W,
\qquad
\nabla\cdot W=0.
\]

Taking divergence gives

\[
0=\nabla\cdot\Delta W
=\nabla\cdot(\kappa W)
=W\cdot\nabla\kappa.
\]

Thus on the active set

\[
\boxed{D_\xi\kappa=0,\qquad \nabla\kappa\perp W.}
\]

This is the M17-313 correction.

## M17-144

Historical statements that require a nonzero order-one `D_xi kappa` to recharge a quiet generic fold are **SUPERSEDED on exact CE-H**.

M17-143's exact fold coefficient survives:

\[
A_T=D_\xi(\sigma+\kappa),
\]

but under exact CE-H this becomes

\[
\boxed{A_T=D_\xi\sigma.}
\]

Hence under M17-144's quiet high-jet estimate `D_xi sigma -> 0`, a uniformly nondegenerate generic fold cannot persist through that branch.

## M17-145

The variable

\[
K_\xi=D_\xi\kappa
\]

is identically zero on exact CE-H. Its derived material equation must therefore be read as a compatibility identity, not as a dynamical nonzero fold-driver equation.

## M17-146

The projected commutator equation for `K_xi` cannot be used as an independent longitudinal order-one recharge mechanism on exact CE-H. Under the quiet reduction it becomes a compatibility condition.

## M17-147

The full-gradient equation for

\[
G=\nabla\kappa
\]

remains useful. The required scope correction is

\[
\boxed{G\perp W.}
\]

Therefore its current interpretation is transverse coefficient rigidity/transport, not support for a nonzero longitudinal fold driver. M17-315/316 give the active transverse continuation.

## Reading order

For active use, read:

1. M17-143 for the exact fold coefficient;
2. M17-313 for `D_xi kappa = 0`;
3. this correction notice;
4. M17-315/316 for transverse `grad kappa` dynamics;
5. `CURRENT_FRONTIER.md` for the latest M17 status.

The historical M17-144--147 files are intentionally not rewritten, so their original reasoning remains available for audit provenance.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
