# DSD M5-592 — Production-linked dual event: projective action or exact anchoring

Date: 2026-09-03

Status: **M5-591 PROVIDES A POSITIVE-MEASURE SET OF FINITE-DEPTH PRODUCTIVE EVENTS CARRYING SAME-TIME NONCOLLINEAR DUAL GEOMETRY. ON THAT EVENT SET, THE NONNEGATIVE MATERIAL-DIRECTION ACTION HAS ONLY TWO INVARIANT-MEASURE POSSIBILITIES: POSITIVE PRODUCTION-LINKED PROJECTIVE ACTION, OR ZERO ACTION ALMOST EVERYWHERE, WHICH FORCES EXACT LOCAL STRAIN-DIFFUSION ANCHORING `tau_i + D_i = 0` ON THE PRODUCTIVE EVENT SET. THIS LOCALIZES THE OLD M5-515/M5-516 DICHOTOMY TO THE ACTUAL PRODUCTION WINDOWS. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Production-linked dual event set

From M5-590/M5-591, after finite-label pigeonhole extraction there is a positive invariant-measure event set

\[
\mathcal E_{pd}
\]

on which

1. a fixed persistent parent lineage \(L_{\alpha_*}\) pays a fixed positive finite-depth annular production share;
2. a fixed noncollinear companion geometry is present at the same similarity time;
3. on the cross-lineage branch the companion is a fixed persistent lineage \(L_{\beta_*}\), \(\beta_*\ne\alpha_*\);
4. on the internal branch the companion is a fixed coherent material subpacket of \(L_{\alpha_*}\).

In either case there are two tracked active material directions

\[
\xi_a,\qquad\xi_b
\]

with

\[
\boxed{|\xi_a\times\xi_b|\ge s_0>0}
\]

on \(\mathcal E_{pd}\).

The event set has

\[
\boxed{\mu(\mathcal E_{pd})>0}
\]

for the inherited invariant suspension measure \(\mu\).

## 2. Exact material direction velocities

M5-487/M5-491 give along each tracked material representative

\[
\boxed{
\xi_i'
=
\tau_i+\mathcal D_i,
\qquad i=a,b,
}
\]

where

\[
\tau_i
=
(I-\xi_i\otimes\xi_i)\Sigma_i\xi_i,
\]

and

\[
\mathcal D_i
=
\rho_i^{-1}
(I-\xi_i\otimes\xi_i)\Delta W_i.
\]

Both vectors are tangent to the unit sphere at \(\xi_i\).

## 3. Production-linked projective-action observable

Define

\[
\boxed{
\mathfrak A_{pd}
:=
\mathbf 1_{\mathcal E_{pd}}
\left(
|\xi_a'|^2+|\xi_b'|^2
\right).
}
\]

Equivalently,

\[
\boxed{
\mathfrak A_{pd}
=
\mathbf 1_{\mathcal E_{pd}}
\left(
|\tau_a+\mathcal D_a|^2
+
|\tau_b+\mathcal D_b|^2
\right).
}
\]

This is a bounded, measurable, nonnegative observable on the compact marked hull.

Therefore exactly one of the following holds.

## 4. Branch P — positive projective action on productive events

If

\[
\boxed{
\langle\mathfrak A_{pd}\rangle_\mu>0,
}
\]

then the finite-depth production event and material-direction motion overlap on a set of positive invariant measure.

Thus

\[
\boxed{
\text{finite-depth production}
+
\text{noncollinear persistent geometry}
+
\text{positive projective action}
}
\]

occur in the same recurrent spacetime subsystem.

This is stronger than the old global statement that ratchet and production merely occur in the same ergodic component.

The action is now localized to the production-linked marked event set itself.

Because

\[
|\xi_i'|^2
\le
2|\tau_i|^2+2|\mathcal D_i|^2,
\]

positive \(\langle\mathfrak A_{pd}\rangle\) forces a positive same-event transverse-strain/projected-diffusion charge.

## 5. Branch A — zero action forces exact anchoring on the event set

If

\[
\boxed{
\langle\mathfrak A_{pd}\rangle_\mu=0,
}
\]

then nonnegativity implies

\[
\mathfrak A_{pd}=0
\qquad\mu\text{-a.e.}
\]

on the marked hull.

Since \(\mu(\mathcal E_{pd})>0\), on almost every production-linked dual event,

\[
\boxed{
\xi_a'=0,
\qquad
\xi_b'=0.
}
\]

Hence, exactly on the productive event set,

\[
\boxed{
\tau_a=-\mathcal D_a,
\qquad
\tau_b=-\mathcal D_b.
}
\]

This is the anchored strain-diffusion cancellation previously isolated abstractly in M5-516/M5-517, now localized to the actual finite-depth production windows.

## 6. Relative-angle consequence

M5-491 gives

\[
c=\xi_a\cdot\xi_b,
\]

\[
c'
=
(\tau_a+\mathcal D_a)\cdot\xi_b
+
\xi_a\cdot(\tau_b+\mathcal D_b).
\]

Therefore on Branch A,

\[
\boxed{c'=0}
\]

almost everywhere on \(\mathcal E_{pd}\).

Thus the productive dual pair is instantaneously rigid there, not merely zero-drift on average.

## 7. Same-lineage internal branch

If M5-591's transverse companion belongs to the same persistent lineage, choose two coherent material submarkers carrying the separated flux sectors.

The same nonnegative action observable and the same dichotomy apply to those two submarkers.

Therefore the conclusion does not depend on whether the dual geometry is cross-lineage or internal-satellite:

\[
\boxed{
\mathcal E_{pd}
\Longrightarrow
P_{pd}^{projective}
\lor
A_{pd}^{anchored}.
}
\]

## 8. DSD audit: what is and is not gained

The positive-action branch is **not yet a contradiction**. A recurrent system can repeatedly pay unsigned projective action.

The anchored branch is also **not yet a contradiction**. M5-547/M5-548 already showed that transverse projected-diffusion cost can be recycled into derivative production along an anchored trajectory.

The gain is localization:

previously the production, dual geometry, and anchoring/ratchet information could occur at different times or in different regions;

now they satisfy the exact same-event dichotomy

\[
\boxed{
\text{production-linked dual geometry}
\Longrightarrow
\text{same-event projective action}
\lor
\text{same-event exact strain-diffusion anchoring}.
}
\]

## 9. Next target

The next efficient calculation is to combine this local dichotomy with the finite-depth production surplus.

For Branch P, ask whether the same-event projective action must consume a non-recyclable part of the shell's derivative budget.

For Branch A, use

\[
(I-\xi_i\otimes\xi_i)(\Sigma_iW_i+\Delta W_i)=0
\]

inside the positive-production event and derive the remaining scalar/parallel budget.

The latter is especially narrow because all transverse strain/diffusion terms are already locked together.

Status: **PRODUCTION, DUAL GEOMETRY, AND PROJECTIVE/ANCHORED DYNAMICS ARE NOW CO-LOCATED IN THE SAME POSITIVE-MEASURE RECURRENT EVENT SET. THE REMAINING HARD CORE IS A SAME-EVENT ENERGY/DERIVATIVE BUDGET PROBLEM, NOT A GENEALOGICAL-OVERLAP PROBLEM. GLOBAL REGULARITY REMAINS UNPROVED.**