# M19-074 — Approximate spectator recurrence propagates to approximate scattering periods, but unique continuation only rigidifies an exact fixed period and does not turn changing almost-periods into periodicity

**Date:** 2026-09-12  
**Status:** CALCULATION / FINITE-BOUNDARY HISTORY / RECURRENCE-VERSUS-UNIQUENESS FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-073 ruled out a simple unsigned physical-budget contradiction for recurrent spectator-boundary packets.  A different possibility is to compare the same recurrent trajectory at two similarity times.

At a fixed spectator radius, recurrence can make

\[
U(\cdot,\theta+T_n)-U(\cdot,\theta)
\]

arbitrarily small on compact spatial sets along some sequence \(T_n\to\infty\).

Could parabolic uniqueness or unique continuation upgrade this approximate recurrence to an exact period, after which the old DSS rigidity would apply?

The answer is no from the currently available information.  Exact equality at one fixed shift is rigid, but a sequence of different shifts with errors tending to zero is exactly the behavior of an aperiodic almost-periodic/quasiperiodic orbit.

## 2. Fixed-spectator profile

Fix one sufficiently large spectator radius \(R_{spec}\) and define the critical rescaled boundary/annulus profile

\[
\boxed{
B(\theta)
:=
R_{spec}
U(R_{spec}\,\cdot,\theta)
}
\]

in the strong fixed-annulus norm \(X\) used by the spectator Duhamel construction.

For a shift \(T\), define

\[
\boxed{
D_T(\theta)
:=
\|B(\theta+T)-B(\theta)\|_X.
}
\]

## 3. Recurrence gives changing approximate periods

Let \(Y\) belong to a compact recurrent similarity hull.  By definition there exists a sequence

\[
T_n\to\infty
\]

such that

\[
\sigma_{T_n}Y\to Y
\]

in the local hull topology.

Because the spectator annulus is a fixed finite spatial region in similarity coordinates, continuity of the observation map gives, for every fixed finite time window,

\[
\boxed{
D_{T_n}(\theta)\to0
}
\]

uniformly or strongly enough on that window, at the level certified by the hull topology.

Thus recurrence already gives arbitrarily good **almost-periods** for the spectator profile.

## 4. Near-identity scattering propagates the same almost-periods

M19-069 shows that on the quiet strong spectator branch the outward scattering map is identity plus \(O(R_{spec}^{-2})\) and, conditionally on the strong linearized bound, locally bi-Lipschitz.

Since

\[
q=\log R_{spec}-\theta/2,
\]

a time shift \(T_n\) corresponds to log-radius translation

\[
q\mapsto q-T_n/2.
\]

Hence spectator recurrence implies the corresponding scattering recurrence

\[
\boxed{
A(q-T_n/2,\omega)
-A(q,\omega)
\to0
}
\]

in the matching local/strong scattering topology, modulo the controlled spectator Duhamel error.

This is not a new restriction; it is the boundary representation of recurrent translation dynamics.

## 5. Exact period would be rigid

Suppose for one fixed nonzero \(T\) we had exact equality

\[
\boxed{
U(y,\theta+T)=U(y,\theta)
}
\]

on a sufficiently rich open spacetime set or globally in the state topology.

Then autonomy plus uniqueness/unique continuation can identify the two shifted solutions and produce a genuine periodic similarity orbit.

The scattering datum would satisfy

\[
A(q-T/2)=A(q),
\]

so the tail is discretely self-similar.  The repository already has a separate DSS rigidity/closure route for that exact case.

Thus

\[
\boxed{
\text{exact fixed period is a qualitatively stronger object than recurrence.}
}
\]

## 6. Why approximate recurrence does not imply one exact period

For each \(n\), define the shifted difference

\[
W_n(y,\theta)
:=
U(y,\theta+T_n)-U(y,\theta).
\]

Each \(W_n\) satisfies a difference equation, but with a different shift \(T_n\).

Recurrence gives

\[
\|W_n\|_{local}\to0.
\]

Unique continuation statements have the logical form

\[
\boxed{
W_n=0\text{ on an appropriate open set}
\Longrightarrow
W_n\equiv0.
}
\]

They do not have the form

\[
\|W_n\|\to0
\Longrightarrow
W_n\equiv0
\quad\text{for some }n.
\]

Without a quantitative lower bound separating every nonzero shifted difference from zero, arbitrarily small but nonzero \(W_n\) are allowed.

## 7. Quasiperiodic anti-model

Consider again

\[
b(\theta)
=
\sin\theta
+\frac12\sin(\sqrt2\,\theta).
\]

There exist shifts \(T_n\to\infty\) such that both phases

\[
T_n\pmod{2\pi},
\qquad
\sqrt2T_n\pmod{2\pi}
\]

approach zero simultaneously.

Hence

\[
\boxed{
\sup_\theta|b(\theta+T_n)-b(\theta)|\to0,
}
\]

but there is no nonzero exact period \(T\).

Thus even **uniform** approximate recurrence of a smooth analytic function does not force periodicity.

This abstract example exactly models the logical gap in the spectator-boundary argument.

## 8. Quantitative unique continuation would still need a uniform nonperiodicity gap

A three-cylinder, observability, or backward-uniqueness estimate might schematically give

\[
\|W_T\|_{large}
\le
C\|W_T\|_{small}^{\alpha}
\|W_T\|_{global}^{1-\alpha}.
\]

Such an estimate propagates smallness, but if \(\|W_{T_n}\|_{small}\to0\), it merely implies stronger global smallness of the same changing sequence.

To force an exact period one would additionally need a statement such as

\[
\boxed{
W_T\not\equiv0
\Longrightarrow
\|W_T\|_{obs}\ge c_*>0
}
\]

uniformly over all large admissible shifts \(T\).

But an aperiodic compact recurrent flow has no such uniform separation: its orbit returns arbitrarily close to itself by definition.

Therefore no continuity-based observability estimate alone can create the missing period.

## 9. Dynamical consequence

The final rigidity theorem cannot be merely

\[
\text{recurrence}+\text{unique continuation}.
\]

It must exclude a nontrivial compact recurrent factor **as a dynamical system**.

Equivalent useful forms remain:

- simple center plus transverse contraction;
- absence of extra zero Lyapunov/Sacker--Sell modes;
- a strict signed cocycle monotonicity incompatible with almost-periodic return;
- a PDE-specific theorem excluding quasiperiodic/minimal recurrent ancient similarity dynamics.

## 10. Certified / not certified

### Certified

1. Compact recurrence gives changing approximate periods at the fixed spectator boundary.
2. M19-069 transports those almost-periods to the scattering datum.
3. Exact equality at one fixed period is much stronger and enters the DSS route.
4. Approximate recurrence with \(T_n\to\infty\) does not imply any exact period.
5. Ordinary quantitative unique continuation propagates smallness but does not by itself supply a uniform nonperiodicity gap on a recurrent compact orbit.

### Not certified

1. Existence or nonexistence of quasiperiodic ancient NS similarity trajectories.
2. A uniform spectral separation of non-phase shifts.
3. Simple center of the recurrent cocycle.
4. Global weak-critical scattering rigidity.
5. Global 3D Navier--Stokes regularity.

## 11. Next target

M19-075 should test whether **autonomous unforced Navier--Stokes energy monotonicity**, when expressed on the recurrent similarity hull rather than one shell, supplies a strict Lyapunov function that rules out nonstationary compact recurrent dynamics.

This must be audited carefully: ordinary physical kinetic energy is not invariant under similarity rescaling and energy can escape to spatial infinity in similarity coordinates.  The calculation should derive the exact similarity evolution of a renormalized/global kinetic quantity and determine whether its monotonicity survives tail flux.

If every candidate Lyapunov functional has an uncontrolled flux at similarity infinity, that will explain why local recurrent hulls can evade the unforced physical energy monotonicity.

---

\[
\boxed{\text{M19-074 COMPLETE; APPROXIMATE RECURRENCE PLUS UNIQUE CONTINUATION DOES NOT UPGRADE AN APERIODIC HULL TO AN EXACT PERIOD.}}
\]
