# DSD M19-174 — The integer dimension-one threshold reduces to a single dimensionless compensation inequality evaluated at the two-mode level

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / INTEGER DIMENSION THRESHOLD / NUMERICAL-CONSTANT TARGET EXPOSED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-173 showed that

\[
\boxed{
\dim_{\mathbb R}E_q^{hard}\le1
}
\]

is already enough to remove genuinely aperiodic recurrent hard dynamics and reduce the survivor to relative periodicity after at most a two-fold iterate.

M19-170--172 give the collective trace inequality

\[
\frac14\mathfrak Z_q
\le
C_{str}\mathfrak Z_q^{3/5}
+
C_a\mathfrak Z_q^{d(a)},
\]

where

\[
\boxed{
 d(a)=\frac43-\frac1a,
\qquad
\frac32<a<3,
\qquad
\frac23<d(a)<1.
}
\]

The present module turns this into a sharp integer threshold test at `N=2`.

## 2. Dimension lower bound

Uniform hard-mode vorticity observability gives

\[
\boxed{
\mathfrak Z_q
\ge
N g_-,
}
\]

where

\[
N=\dim_{\mathbb R}E_q^{hard}.
\]

Define the normalized total hard mass

\[
\boxed{
X
:=
\frac{\mathfrak Z_q}{g_-}.
}
\]

Then

\[
\boxed{X\ge N.}
\]

## 3. Normalize the collective trace inequality

Divide

\[
\frac14\mathfrak Z_q
\le
C_{str}\mathfrak Z_q^{3/5}
+
C_a\mathfrak Z_q^{d}
\]

by `mathfrak Z_q`.

This gives

\[
\frac14
\le
C_{str}\mathfrak Z_q^{-2/5}
+
C_a\mathfrak Z_q^{d-1}.
\]

Substitute

\[
\mathfrak Z_q=g_-X.
\]

Define the dimensionless corridor constants

\[
\boxed{
\widehat C_{str}
:=
C_{str}g_-^{-2/5},
}
\]

and

\[
\boxed{
\widehat C_a
:=
C_ag_-^{d-1}.
}
\]

Then every hard survivor must satisfy

\[
\boxed{
\frac14
\le
\widehat C_{str}X^{-2/5}
+
\widehat C_aX^{d-1}.
}
\]

## 4. Monotonicity in X

Because

\[
-\frac25<0
\]

and

\[
d-1<0,
\]

both terms on the right decrease strictly as `X` increases.

Therefore for all

\[
X\ge2,
\]

we have

\[
\widehat C_{str}X^{-2/5}
+
\widehat C_aX^{d-1}
\le
\widehat C_{str}2^{-2/5}
+
\widehat C_a2^{d-1}.
\]

Hence the worst possible point for excluding all `N>=2` states is exactly the two-mode threshold `X=2`.

## 5. Exact sufficient criterion for N<=1

If

\[
\boxed{
\widehat C_{str}2^{-2/5}
+
\widehat C_a2^{d(a)-1}
<
\frac14,
}
\]

then no hard state with

\[
X\ge2
\]

can satisfy the exact trace inequality.

But

\[
N\ge2
\Longrightarrow X\ge2.
\]

Therefore

\[
\boxed{
\widehat C_{str}2^{-2/5}
+
\widehat C_a2^{d(a)-1}
<
\frac14
\Longrightarrow
N\le1.
}
\]

This is the desired integer dimension-one criterion.

## 6. Optimized criterion over a

Because the nonlocal exponent family is available for every

\[
\frac32<a<3,
\]

it suffices that there exist one exponent `a` such that

\[
\boxed{
\inf_{3/2<a<3}
\left[
\widehat C_{str}2^{-2/5}
+
\widehat C_a2^{1/3-1/a}
\right]
<
\frac14.
}
\]

Here

\[
d(a)-1
=
\frac13-\frac1a<0.
\]

This formula cleanly separates the exponent gain from the deterioration of the HLS constant hidden in `widehat C_a`.

## 7. Corridor constants made explicit

Up to universal vector-valued Sobolev/Lieb--Thirring constants and the uniformly bounded Gram-conditioning factors, M19-170 gives schematically

\[
\boxed{
C_{str}
\sim
C_{LT}^{3/5}
S_+^{2/5}
M_{5/2}
(\Lambda_P^+)^{3/5},
}
\]

where

\[
M_{5/2}
=
\sup_s\|S_U(s)\|_{5/2}.
\]

M19-172 gives schematically

\[
\boxed{
C_a
\sim
C_{HLS}(a)C_{CZ}(a)
M_a
S_+^{1-d(a)}
(\Lambda_P^+)^{\,3/(2a)-1/2},
}
\]

where

\[
M_a
=
\sup_s\|\nabla\Omega(s)\|_a.
\]

Thus the dimension-one criterion is no longer qualitative. It depends on the explicit corridor package

\[
\boxed{
\left(
g_-,
\Lambda_P^+,
S_+,
M_{5/2},
M_a,
C_{LT},
C_{HLS}(a),
C_{CZ}(a)
\right).
}
\]

## 8. Why the test is representation-safe

A rescaling of the scattering norm changes both

\[
g_-
\]

and the normalization used to define the collective trace constants.

The normalized combinations

\[
\widehat C_{str}
=C_{str}g_-^{-2/5},
\]

\[
\widehat C_a
=C_ag_-^{d-1}
\]

are the quantities entering the actual dimension test.

Therefore the decision criterion is tied to the normalized hard bundle rather than to an arbitrary choice of units for the scattering norm.

## 9. Relation to recurrence closure

If the two-mode inequality holds, then

\[
N\le1.
\]

M19-173 immediately gives

\[
\boxed{
\text{recurrent critical hard orbit}
\Longrightarrow
\text{relative-periodic after at most two quotient returns}.
}
\]

Thus the entire aperiodic hard branch would be closed without first proving full kernel rigidity.

## 10. What is still missing

The project currently establishes uniform boundedness of all corridor quantities appearing above, but it does not yet provide sharp numerical constants proving

\[
\widehat C_{str}2^{-2/5}
+
\widehat C_a2^{d-1}
<\frac14.
\]

Hence the dimension-one theorem is **not yet certified**.

The missing step is now concrete:

\[
\boxed{
\text{sharpen or compute the normalized compact-corridor constants.}
}
\]

## 11. Audit verdict

### Proved

1. The `N<=1` target reduces to one explicit dimensionless inequality.
2. Because the normalized compensation ratio decreases with total hard mass, testing the two-mode threshold is sufficient for excluding all larger dimensions.
3. The relevant constants are now explicitly identified.

### Not proved

1. The numerical strict inequality at `N=2`.
2. `N<=1` on the full hard corridor.
3. Relative-periodic nonexistence.
4. Global regularity.

## 12. Next target

M19-175 should audit which constants in the two-mode criterion are already quantitatively bounded by the repository and which are only known qualitatively.

The highest-value candidates for sharpening are

\[
 g_-,
\quad
M_{5/2},
\quad
M_a,
\quad
\Lambda_P^+.
\]

If exact numeric control is unavailable analytically, this criterion also defines a precise target for a future computer-assisted compact-corridor verification without changing the proof architecture.
