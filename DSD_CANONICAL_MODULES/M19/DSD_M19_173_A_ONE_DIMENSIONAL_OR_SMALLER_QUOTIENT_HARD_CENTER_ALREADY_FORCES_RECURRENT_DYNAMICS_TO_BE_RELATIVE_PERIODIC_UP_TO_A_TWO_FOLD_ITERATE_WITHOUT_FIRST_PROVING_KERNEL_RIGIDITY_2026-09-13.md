# DSD M19-173 — A one-dimensional-or-smaller quotient hard center already forces recurrent dynamics to be relative-periodic up to a two-fold iterate, without first proving kernel rigidity

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / RECURRENT-DYNAMICS REDUCTION FROM DIMENSION <= 1 / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-168 showed that genuine irrational elliptic neutral dynamics requires at least two real symmetry-quotient hard dimensions.
M19-169--172 turned the hard dimension into a quantitative collective compensation problem.

The present module sharpens the dynamical consequence:

\[
\boxed{
\dim_{\mathbb R}E_q^{hard}\le1
}
\]

is already sufficient to eliminate **aperiodic recurrent quotient dynamics**.

One does not need to prove the remaining one-dimensional kernel multiplier is absent before reducing recurrence to relative periodicity.

## 2. Quotient Poincare section

Work on the compact recurrent hard corridor after quotienting the exact spatial rotation group and removing the flow/time tangent by a local Poincare section.

The positive Lyapunov directions have already been excluded by M19-132--133.
The essential spectrum is strictly stable.

Thus the only noncontracting transverse directions lie in the finite real quotient hard space

\[
E_q^{hard}.
\]

Assume

\[
\boxed{
N:=\dim_{\mathbb R}E_q^{hard}\le1.
}
\]

The stable directions are slaved to the local center dynamics by the standard finite-dimensional invariant-manifold reduction on the retained smooth compact corridor.

## 3. Case N=0

If

\[
N=0,
\]

there is no transverse neutral direction.

The local quotient return map is strictly contracting in every transverse direction.

A recurrent point must therefore be the local fixed point of the quotient return map.

Lifting the rotation quotient gives

\[
\boxed{
U(s+S)=Q_*U(s),
}
\]

so the orbit is RDSS/RSS/DSS/SS according to the holonomy and period.

## 4. Case N=1

Now suppose

\[
N=1.
\]

After stable slaving, the local quotient return dynamics is a one-dimensional `C1` map on an interval-like center coordinate:

\[
P:I\to I.
\]

On the complete observable center branch, the scattering representation gives two-sided bounded/invertible center dynamics, so locally `P` is a homeomorphism/diffeomorphism of its recurrent center interval.

There are two orientation cases.

## 5. Orientation-preserving one-dimensional return

Suppose

\[
P\text{ is orientation preserving}.
\]

Then `P` is monotone increasing.

If at a point `x`

\[
P(x)>x,
\]

then monotonicity gives

\[
x<P(x)\le P^2(x)\le\cdots,
\]

with strict forward displacement until a fixed point is reached.
Such a point cannot return arbitrarily close to its initial value unless it is itself fixed.

Likewise if

\[
P(x)<x,
\]

its forward orbit is monotone in the opposite direction.

Therefore every recurrent point of an orientation-preserving interval homeomorphism is fixed:

\[
\boxed{
P(x)=x.
}
\]

Hence quotient recurrence is periodic.

## 6. Orientation-reversing one-dimensional return

If `P` reverses orientation, then

\[
P^2
\]

is orientation preserving.

A recurrent point for `P` is recurrent for `P^2`.
By the previous argument,

\[
P^2(x)=x.
\]

Thus the point has period one or two:

\[
\boxed{
P(x)=x
\quad\text{or}\quad
P^2(x)=x.
}
\]

Therefore the only residual one-dimensional recurrent dynamics is a finite iterate of a quotient periodic orbit.

## 7. Lift back to the Navier--Stokes orbit

A quotient fixed point lifts to

\[
U(s+S)=Q_*U(s).
\]

A quotient two-cycle lifts, after two returns, to

\[
U(s+2S)=Q_{**}U(s),
\]

with the accumulated holonomy

\[
Q_{**}=Q_*(s+S)Q_*(s)
\]

in the representation-safe notation.

Thus

\[
\boxed{
N\le1
\Longrightarrow
\text{recurrent hard orbit is relative-periodic after at most a two-fold iterate}.
}
\]

## 8. Relation to the +/-1 monodromy picture

M19-168 found that a real one-dimensional quotient monodromy can only be

\[
+1
\quad\text{or}\quad
-1.
\]

The present nonlinear return-map argument is the dynamical counterpart:

- `+1` corresponds to the orientation-preserving/parabolic kernel case;
- `-1` corresponds to the orientation-reversing case, whose square is a kernel return.

Neither case permits genuinely aperiodic one-dimensional recurrence.

## 9. Important correction to the workflow

The previous workflow treated

\[
\text{kernel rigidity}
\]

as a prerequisite for reducing recurrent dynamics to RSS/RDSS.

The present result shows that the weaker statement

\[
\boxed{
\dim E_q^{hard}\le1
}
\]

is sufficient for that reduction.

Kernel rigidity remains important for the **nonexistence/structure of the resulting relative-periodic branch**, but it is no longer required to eliminate aperiodic recurrence first.

## 10. New primary target

The primary aperiodic-closure target is now

\[
\boxed{
\mathcal T_{dim1}:
\dim_{\mathbb R}E_q^{hard}\le1.
}
\]

M19-169 gives the sufficient trace condition

\[
\boxed{
\mathfrak T_q<2g_-\Lambda_P.
}
\]

M19-170--172 supply sublinear PDE estimates for both the local and nonlocal compensation traces and a quantitative dimension ceiling.

Thus the remaining task is to sharpen the constants enough to reach the integer threshold `N<2`, rather than to prove a full zero-dimensional spectral gap immediately.

## 11. Scope firewall

The one-dimensional recurrence statement uses a local finite-dimensional center/return reduction on the retained compact smooth corridor.

It should not be applied directly to arbitrary weak W1 states before the hard-bundle and invariant-manifold gates are certified.

Also,

\[
\boxed{
\dim E_q\le1
\Longrightarrow
\text{relative periodicity},
}

not

\[
\dim E_q\le1
\Longrightarrow
\text{trivial solution}.
\]

The resulting RSS/RDSS orbit still requires a Liouville/nonexistence argument.

## 12. Audit verdict

### Proved conditionally on the retained center-manifold/return-map gate

\[
\boxed{
\dim E_q^{hard}\le1
\Longrightarrow
\text{no genuinely aperiodic recurrent hard dynamics}.
}
\]

The orbit is relative-periodic after at most two quotient returns.

### Not proved

1. The numerical dimension-one bound itself.
2. Nonexistence of the resulting moderate RSS/RDSS orbit.
3. Global regularity.

## 13. Next target

The strategic order should therefore change.

M19-174 should prioritize the **integer dimension threshold** rather than full kernel positivity:

\[
\boxed{
N<2.
}
\]

The natural route is to turn the optimized collective trace ceiling from M19-172 into a normalized dimensionless inequality and identify which corridor constants must be sharpened to cross the threshold exactly.

Only after the aperiodic branch is reduced to RSS/RDSS should the remaining one-dimensional finite-iterate kernel be revisited as part of the relative-periodic Liouville problem.
