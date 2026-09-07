# DSD M17-335 — L1 three-halves phase locking forces zero-density negative-kappa time and sublinear renormalized-flux variation

Date: 2026-09-08  
Canonical ID: **M17-335**

Status: **ACTIVE SAME-LABEL PHASE-LOCKING REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-332

On the phase-locking branch for one material genealogy,

\[
\boxed{
V_T
:=
\frac1T\int_0^T
\left|\kappa(\theta)-\frac32\right|d\theta
\to0.
}
\]

Set

\[
q:=\kappa-\frac32.
\]

## 2. Negative-kappa time has zero density

Whenever

\[
\kappa\le0,
\]

we have

\[
|q|
=
\left|\kappa-\frac32\right|
\ge\frac32.
\]

Therefore

\[
\frac32
\left|\{\theta\in[0,T]:\kappa(\theta)\le0\}\right|
\le
\int_0^T|q|d\theta.
\]

Dividing by `T`,

\[
\boxed{
\frac1T
\left|\{\kappa\le0\}\cap[0,T]\right|
\le
\frac23V_T
\to0.
}
\]

More generally, for every fixed `delta>0`,

\[
\boxed{
\frac1T
\left|\left\{\kappa\le\frac32-\delta\right\}\cap[0,T]\right|
\le
\frac{V_T}{\delta}
\to0.
}
\]

Thus the same phase-locked label spends asymptotically all of its time in every fixed neighborhood of the resonant level.

## 3. Renormalized flux law

M17-329 defined

\[
\widehat\Phi=e^{-3\theta/2}\Phi
\]

and proved

\[
\boxed{
D_B\log\widehat\Phi
=
\kappa-\frac32
=q.
}
\]

Hence the total logarithmic variation of the renormalized flux satisfies

\[
\operatorname{Var}_{[0,T]}\bigl(\log\widehat\Phi\bigr)
\le
\int_0^T|q|d\theta.
\]

Consequently

\[
\boxed{
\frac1T
\operatorname{Var}_{[0,T]}\bigl(\log\widehat\Phi\bigr)
\to0.
}
\]

The phase-locked carrier is therefore asymptotically quiescent in normalized-flux logarithmic variation.

## 4. Signed drift is also sublinear

Independently,

\[
\log\frac{\widehat\Phi(T)}{\widehat\Phi(0)}
=
\int_0^Tq\,d\theta.
\]

Thus

\[
\boxed{
\frac1T
\left|
\log\frac{\widehat\Phi(T)}{\widehat\Phi(0)}
\right|
\le V_T\to0.
}
\]

Therefore

\[
\widehat\Phi(T)/\widehat\Phi(0)=e^{o(T)}.
\]

This means **subexponential** drift, not boundedness.

The stronger inference

\[
\boxed{
e^{o(T)}=O(1)}
\]

is rejected.

## 5. Compact-lift consequence for deep excursions

If the same-label lifted hull is compact, continuity gives a finite bound

\[
|h|=|D_B\kappa|\le H_*.
\]

A visit to `kappa<=0` requires the trajectory to travel a distance at least `3/2` from the resonant level.

Any collection of deep negative excursions separated by a fixed time distance therefore consumes a fixed amount of the `L1` resonant-deviation budget per excursion.

Since that budget is `o(T)`, the number of such separated deep excursions is `o(T)`.

Thus a compact phase-locked label cannot support a bounded-gap, positive-frequency sequence of deep zero-level excursions.

This statement is about separated excursion episodes, not arbitrary clustered/tangential zero contacts.

## 6. Relation to the M17-323 zero-level turnover ledger

M17-323 gives a persistent **ensemble pure-flux** downward zero-level activity.

M17-335 shows that a same-label `L1`-phase-locked resonant carrier has

\[
\boxed{
\text{zero-density negative-}kappa\text{ residence}
}
\]

and sublinear normalized-flux variation.

Therefore the following identification is not available for free:

\[
\boxed{
\text{M17-323 zero-level turnover population}
=
\text{M17-335 phase-locked resonant genealogy}.
}
\]

If both structures persist, one needs an explicit material-label bridge.  Otherwise they are dynamically segregated populations.

## 7. DSD-theory role

The useful DSD heuristic is to distinguish a persistent global transition channel from a carrier that is asymptotically locked to another structural state.

The standard mathematical translation is the elementary `L1` occupancy estimate and the exact renormalized-flux cocycle.

No DSD axiom is used as a PDE hypothesis.

## 8. Updated phase-locking frontier

The phase-locking branch now becomes

\[
\boxed{
H_{L^1\ lock\ at\ 3/2}
\Longrightarrow
H_{zero\text{-}density\ negative\ kappa}
\cap
H_{sublinear\ normalized\text{-}flux\ variation}.
}
\]

To combine this carrier with the persistent zero-level current, the proof now requires one of:

1. a material genealogy exchange theorem between the resonant and negative-current populations;
2. a proof that the two populations must lie in the same invariant component;
3. or a separate contradiction within one of the two populations.

Without such a bridge, ensemble coexistence is not same-label coexistence.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
