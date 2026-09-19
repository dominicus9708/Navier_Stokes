# M20-007 — The transverse pressure-Hessian commutator is a traceless Calderon--Zygmund critical channel, not a new noncritical resource

Date: 2026-09-20  
Canonical ID: **M20-007**  
Status: **PROJECTIVE PRESSURE-HESSIAN AUDIT / THE M20-006 PRESSURE REPLENISHMENT USES ONLY THE OFF-AXIS TRACELESS HESSIAN COMPONENT / ITS COMMUTATOR WITH THE VORTICITY PROJECTOR IS CONTROLLED BY THE STANDARD CALDERON--ZYGMUND PRESSURE SOURCE |S|^2-|omega|^2/2 / ON THE TERMINAL 1/r HARD TAIL THE PROJECTIVE PRESSURE-STRAIN CORRELATION HAS THE SAME R^-3 ANNULAR ANCESTRY WEIGHT AS THE EXISTING RAW-H2 CRITICAL FIREWALL / THERE IS NO NEW POWER GAIN OR AUTOMATIC SIGN / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Pressure channel isolated by M20-006

M20-006 identifies the signed pressure replenishment of projective strain as

\[
-\frac12
\langle[S,Q],[H_p,Q]\rangle_F,
\]

where

\[
H_p:=\nabla^2p,
\qquad
Q:=\xi\otimes\xi.
\]

Equivalently, with

\[
h_\perp:=P_\xi^\perp H_p\xi,
\]

the pressure work is

\[
-s_\perp\cdot h_\perp.
\]

The purpose of M20-007 is to determine whether \(h_\perp\) is a smaller resource than the full pressure Hessian.

## 2. Isotropic pressure curvature is invisible

Decompose

\[
H_p
=
H_p^\circ
+
\frac13(\Delta p)I,
\]

where

\[
\operatorname{tr}H_p^\circ=0.
\]

Because the identity matrix commutes with every projector,

\[
\boxed{
[H_p,Q]
=
[H_p^\circ,Q].
}
\]

Likewise,

\[
P_\xi^\perp
\left[
\frac13(\Delta p)I
\right]\xi
=
0.
\]

Thus the M20 pressure channel sees only anisotropic pressure curvature.

The scalar pressure-Poisson trace does not directly rotate the vorticity axis relative to strain.

## 3. Exact pointwise commutator norm

For any symmetric matrix H and rank-one projector

\[
Q=\xi\otimes\xi,
\]

let

\[
h_\perp=P_\xi^\perp H\xi.
\]

Then

\[
[H,Q]
=
h_\perp\otimes\xi
-
\xi\otimes h_\perp.
\]

Therefore

\[
\boxed{
\|[H,Q]\|_F^2
=
2|h_\perp|^2.
}
\]

In particular,

\[
\boxed{
\|[H_p,Q]\|_F
\le
\sqrt2\,|H_p^\circ|
\le
\sqrt2\,|H_p|.
}
\]

The projective pressure observable is a bounded algebraic projection of the standard pressure Hessian.

## 4. Pressure Poisson representation

For incompressible Navier--Stokes,

\[
-\Delta p
=
\partial_i u_j\,\partial_j u_i.
\]

Writing

\[
\nabla u=S+\Omega,
\]

one obtains

\[
\boxed{
-\Delta p
=
|S|^2-\frac12|\omega|^2.
}
\]

Define

\[
f
:=
|S|^2-\frac12|\omega|^2.
\]

Then

\[
H_p
=
\nabla^2(-\Delta)^{-1}f
\]

up to the fixed sign convention.

Hence the traceless Hessian is a matrix Calderon--Zygmund transform of f:

\[
\boxed{
H_p^\circ
=
\mathcal R^\circ f.
}
\]

## 5. Whole-space L2 estimate

Calderon--Zygmund boundedness gives

\[
\|H_p^\circ\|_2
\le
C\|f\|_2.
\]

Therefore

\[
\boxed{
\|[H_p,Q]\|_2
\le
C
\left\|
|S|^2-\frac12|\omega|^2
\right\|_2.
}
\]

Using the strain-vorticity singular-integral equivalence,

\[
\|S\|_4
\le
C\|\omega\|_4,
\]

we obtain

\[
\boxed{
\|[H_p,Q]\|_2
\le
C\|\omega\|_4^2.
}
\]

Thus the transverse projective pressure channel is controlled by the same quartic vorticity scale as the full Hessian.

## 6. First-hitting bounded-amplitude specialization

On a normalized first-hitting slice with

\[
\|\omega\|_\infty\le M_\infty,
\]

interpolation gives

\[
\|\omega\|_4^4
\le
M_\infty^2\|\omega\|_2^2.
\]

Hence

\[
\boxed{
\|[H_p,Q]\|_2^2
\le
C M_\infty^2\|\omega\|_2^2.
}
\]

This is the projective version of the earlier pressure-Hessian absorption into normalized enstrophy.

It does not create a new independent global pressure reservoir.

## 7. Correlation with projective strain

By Cauchy--Schwarz,

\[
\boxed{
\left|
\int
\langle[S,Q],[H_p,Q]\rangle_F\,dx
\right|
\le
\|[S,Q]\|_2
\|[H_p,Q]\|_2.
}
\]

Therefore

\[
\boxed{
\left|
\int
\langle[S,Q],[H_p,Q]\rangle_F
\right|
\le
C
\|[S,Q]\|_2
\|\omega\|_4^2.
}
\]

Since

\[
\|[S,Q]\|_F\le C|S|,
\]

one also has the coarse bound

\[
\left|
\int
\langle[S,Q],[H_p,Q]\rangle_F
\right|
\le
C
\|S\|_2
\|\omega\|_4^2.
\]

No sign is produced.

## 8. Terminal hard-tail scaling

On the terminal critical hard tail,

\[
u\sim r^{-1}A,
\]

so

\[
S\sim r^{-2},
\qquad
\omega\sim r^{-2},
\qquad
H_p=\nabla^2p\sim r^{-4}.
\]

The dimensionless projectors are order one.

Thus

\[
[S,Q]\sim r^{-2},
\]

and

\[
[H_p,Q]\sim r^{-4}.
\]

Their signed correlation density scales as

\[
\boxed{
\langle[S,Q],[H_p,Q]\rangle_F
\sim
r^{-6}.
}
\]

On a comparable annulus

\[
A(R,\Lambda R),
\]

the volume is \(O(R^3)\), so

\[
\boxed{
\int_{A(R,\Lambda R)}
\left|
\langle[S,Q],[H_p,Q]\rangle_F
\right|dx
=
O(R^{-3}).
}
\]

## 9. Ancestry summability

For geometrically separated recurrent radii

\[
R_m\sim\Lambda^m,
\]

the direct annular accumulation obeys

\[
\sum_m R_m^{-3}<\infty.
\]

Even a fixed positive normalized projective pressure event on every logarithmic scale gives only

\[
\boxed{
\sum_m O(R_m^{-3}),
}
\]

which is summable.

This is the same physical ancestry exponent as the M19-414 angular-residual/raw-H2 firewall.

Therefore

\[
\boxed{
P_{\rm off}^{projective}
\text{ is exactly critical, not supercritical.}
}
\]

## 10. No local sign from the Poisson source

Although

\[
-\Delta p
=
|S|^2-\frac12|\omega|^2
\]

is a local scalar source, the traceless Hessian

\[
H_p^\circ
\]

is nonlocal.

The off-axis component

\[
P_\xi^\perp H_p\xi
\]

can have either sign/orientation relative to

\[
s_\perp.
\]

Thus there is no implication

\[
s_\perp\neq0
\Longrightarrow
-s_\perp\cdot H_p\xi>0
\]

or its opposite.

The projective pressure channel is a signed nonlocal covariance.

## 11. Relation to M20-006

M20-006 gives

\[
\frac14D_t\|[S,Q]\|_F^2
+
\gamma\|[S,Q]\|_F^2
=
-\frac12
\langle[S,Q],[H_p,Q]\rangle_F
+\text{viscous terms}.
\]

M20-007 shows that the pressure term on the right is not a new noncritical payer.

It returns to the standard pressure/vorticity critical scale.

Therefore a persistent positive projective-strain event can be supported by a pressure-Hessian covariance without violating known ancestry budgets.

## 12. Projective pressure is still useful structurally

The absence of a new power gain does not make the projection useless.

The exact quantity

\[
[H_p,Q]
\]

is more sharply typed than the full Hessian:

- isotropic curvature is removed;
- only off-axis anisotropic pressure response remains;
- it is directly comparable to \([S,Q]\);
- strain eigenvector choices are unnecessary.

Thus future pressure analysis should use

\[
\boxed{
\langle[S,Q],[H_p,Q]\rangle_F
}
\]

rather than a full-Hessian norm whenever the target is vorticity-axis rotation.

## 13. Updated strain branch audit

The M20-006 alternative

\[
P_{\rm off}
\]

should now be annotated

\[
\boxed{
P_{\rm off}^{critical,CZ}.
}
\]

It is a structured signed pressure covariance, not an independent noncritical root.

The strain branch remains

\[
\boxed{
S_{\rm eig}
\Longrightarrow
S_{\gamma^-}
\lor
P_{\rm off}^{critical,CZ}
\lor
D_S
\lor
V_{S\xi}
\lor
R_{\rm material}.
}
\]

## 14. Next target

The other unresolved M20 tangent mechanism is the second-moment-silent reweighting branch

\[
R_{\rm silent}.
\]

A natural idea is to use higher projective moments.

Before doing so, one must audit whether any hierarchy of direction-only observables can detect a reweighting current that has zero conditional mean at fixed projective direction.

M20-008 should characterize the exact conditional-expectation kernel of projective reweighting.

\[
\boxed{\text{M20-007 COMPLETE; TRANSVERSE PROJECTIVE PRESSURE IS A TRACELESS CALDERON--ZYGMUND CRITICAL CHANNEL WITH NO NEW POWER GAIN.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
