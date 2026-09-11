# M18-073 — Frobenius audit corrects the material-cross-section shortcut and splits CE-H curl energy into transverse current or director twist

**Date:** 2026-09-11  
**Status:** AUDIT CORRECTION / FROBENIUS INTEGRABILITY FIREWALL / TRANSVERSE-CURRENT VERSUS DIRECTOR-TWIST SPLIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose and correction

M18-071 introduced the algebraic field

\[
(\nabla\times W)\times\xi
\]

and interpreted it as the current on a material cross-section with normal \(n=\xi\).

The algebra is correct whenever such a surface exists.

However, a finite two-dimensional surface patch whose normal equals a prescribed director field \(\xi\) does **not** exist automatically.

The orthogonal plane distribution

\[
\xi^\perp
\]

must satisfy the Frobenius integrability condition.

Therefore the unconditional object should first be defined algebraically by

\[
\boxed{
\mathcal J_\perp
:=(\nabla\times W)\times\xi
}
\]

on \(\{\rho>0\}\).

It becomes the M5-520 material-surface current \(J_\Sigma\) only on a vortex-transverse material surface whose normal actually satisfies \(n=\xi\).

This module records that firewall and shows that failure of the surface construction is itself a quantitative director-twist channel.

## 2. Frobenius condition for vortex-transverse surfaces

Associate to \(\xi\) the one-form

\[
\alpha:=\xi\cdot dy.
\]

The plane field \(\ker\alpha=\xi^\perp\) is locally tangent to a family of surfaces if and only if

\[
\alpha\wedge d\alpha=0.
\]

In three dimensions this is equivalent to

\[
\boxed{
\tau_\xi
:=
\xi\cdot(\nabla\times\xi)
=0.
}
\]

Thus

\[
\boxed{
\tau_\xi=0
\iff
\text{the vortex-orthogonal plane distribution is locally surface-integrable}
}
\]

at regular points, with the standard local Frobenius interpretation.

If

\[
\tau_\xi\ne0,
\]

there is no local finite surface patch whose tangent plane is everywhere \(\xi^\perp\).

## 3. Exact longitudinal curl component

Write

\[
W=\rho\xi.
\]

Then

\[
\nabla\times W
=
\nabla\rho\times\xi
+
\rho\nabla\times\xi.
\]

Dot with \(\xi\):

\[
\xi\cdot(\nabla\rho\times\xi)=0,
\]

so

\[
\boxed{
\xi\cdot(\nabla\times W)
=
\rho\,\tau_\xi.
}
\]

Therefore director twist is exactly the longitudinal component of \(\operatorname{curl}W\) per unit vorticity amplitude.

## 4. Exact transverse-current / twist decomposition

For any vector \(C\) and unit vector \(\xi\),

\[
|C|^2
=
|C\times\xi|^2
+(C\cdot\xi)^2.
\]

Set

\[
C=\nabla\times W.
\]

Using Sections 1 and 3,

\[
\boxed{
|\nabla\times W|^2
=
|\mathcal J_\perp|^2
+
\rho^2\tau_\xi^2.
}
\]

For divergence-free whole-space \(W\),

\[
\|\nabla\times W\|_2^2
=
\|\nabla W\|_2^2
=:P.
\]

Hence the global palinstrophy has the exact two-channel split

\[
\boxed{
P
=
P_{\perp J}
+
P_{twist},
}
\]

where

\[
\boxed{
P_{\perp J}
:=
\int|\mathcal J_\perp|^2dy,
}
\]

and

\[
\boxed{
P_{twist}
:=
\int\rho^2\tau_\xi^2dy.
}
\]

Both are nonnegative.

## 5. Relation to the non-Beltrami defect

M5-618--619 use

\[
J_B
:=
W\times(\nabla\times W).
\]

Since

\[
W=\rho\xi,
\]

we have unconditionally on the active set

\[
\boxed{
J_B=-\rho\mathcal J_\perp.
}
\]

Thus M18-072's identity and active-amplitude localization remain valid **algebraically**, without assuming an actual cross-section surface:

\[
\boxed{
|J_B|^2
=
\rho^2|\mathcal J_\perp|^2.
}
\]

What must be corrected is only the unconditional use of the phrase `material-surface current`.

The correct terminology is:

- \(\mathcal J_\perp\): algebraic transverse-curl current;
- \(J_\Sigma\): actual M5-520 surface current on a material surface;
- \(\mathcal J_\perp=J_\Sigma\) when a vortex-transverse surface with \(n=\xi\) exists.

## 6. Integrable branch

Suppose

\[
\tau_\xi=0
\]

on an active open patch.

Then Frobenius gives a local family of surfaces tangent to \(\xi^\perp\), so their unit normals can be chosen as

\[
n=\xi.
\]

On CE-H,

\[
D_B\xi=0,
\]

and

\[
(\nabla B)^T\xi
=(\sigma+\tfrac12)\xi.
\]

The material-normal equation

\[
D_Bn
=-P_n^\perp(\nabla B)^Tn
\]

therefore gives

\[
D_Bn=0
\]

when \(n=\xi\).

Hence an initially integrable vortex-transverse material patch remains vortex-transverse for as long as the smooth CE-H description and the patch remain valid.

On this branch,

\[
\boxed{
J_\Sigma
=
\mathcal J_\perp.
}
\]

The M5-520--522 surface-current machinery is then legitimately available.

## 7. Nonintegrable branch

Suppose instead

\[
\tau_\xi\ne0
\]

on a set of positive weighted measure.

Then a vortex-orthogonal surface foliation is unavailable there.

But the failure is itself priced by

\[
\boxed{
\rho^2\tau_\xi^2,
}
\]

which is an exact nonnegative portion of palinstrophy.

Therefore the failed surface construction is not an untyped loophole:

\[
\boxed{
\text{no vortex-transverse surface}
\Longrightarrow
G_{director\ twist/Frobenius\ obstruction}.
}
\]

This is a director geometry/topology branch, not a reason to discard the derivative payment.

## 8. Quantitative current-or-twist split

Suppose a recurrent event or region carries palinstrophy

\[
\int_Q|\nabla\times W|^2dy
\ge p_Q>0.
\]

Then the exact decomposition gives

\[
\boxed{
\int_Q|\mathcal J_\perp|^2dy
\ge\frac{p_Q}{2}
\quad\lor\quad
\int_Q\rho^2\tau_\xi^2dy
\ge\frac{p_Q}{2}.
}
\]

Thus every palinstrophy-paying region has either

1. a transverse-current share, or
2. a director-twist share.

No surface geometry assumption is required for this dichotomy.

## 9. Relation to M18-071 four-channel split

M18-071's algebraic identity

\[
|\nabla W|^2
=
|\partial_\parallel\rho|^2
+
\rho^2|\nabla_\perp\xi|^2
+
\frac12|\mathcal J_\perp|^2
+
\frac12|C_\perp|^2
\]

remains an algebraic decomposition on the active set, where

\[
C_\perp
:=
\nabla_\perp\rho+ho(\xi\cdot\nabla)\xi.
\]

The correction is that \(\mathcal J_\perp\) must not be called an actual finite material-surface current unless the Frobenius branch is available.

The director-twist quantity

\[
\tau_\xi
=
\xi\cdot\nabla\times\xi
\]

is contained inside the transverse-director derivative sector and now receives its own geometric meaning.

## 10. A stronger routing theorem for the M18-070 sheath

The lower-amplitude derivative sheath of M18-070 must now be routed as

\[
\boxed{
G_{sheath}
\Longrightarrow
G_{\parallel\rho}
\lor
G_{director\ deformation}
\lor
G_{\perp current}
\lor
G_{amplitude\text{-}curvature\ locking}.
}
\]

The transverse-current branch further splits as

\[
\boxed{
G_{\perp current}
\Longrightarrow
\begin{cases}
G_{material\ surface\ current},&\tau_\xi=0\text{ on a controlled patch},\\
G_{director\ twist},&\text{surface integrability fails}.
\end{cases}
}
\]

The second line is schematic: if a controlled current-carrying region cannot be covered by integrable patches, the Frobenius obstruction must remain present and is separately paid in \(P_{twist}\).

## 11. Relation to the M18-072 active-current floor

M18-072 proves from M5-618 compactness that

\[
\int_{\rho\ge a_B}
|\mathcal J_\perp|^2dy
\ge j_B>0
\]

for every marked CE-H state.

This statement is valid without a surface foliation because \(\mathcal J_\perp\) is algebraically defined.

Therefore every marked state has a fixed active-region transverse-curl current.

To turn it into M5-521 material-label current action, one now has the exact additional requirement:

\[
\boxed{
\text{controlled Frobenius-integrable vortex-transverse patch family}.
}
\]

If that requirement fails systematically, the obstruction is director twist/topology rather than a silent gap.

## 12. What this changes in the next target

M18-072 proposed a direct bulk-to-surface coarea/thickness conversion.

The present audit shows the correct order is

\[
\boxed{
\text{bulk transverse current}
\to
\begin{cases}
\text{Frobenius-integrable patch family}
\to
\text{surface trace/thickness},\\
\text{Frobenius obstruction}
\to
\text{director twist/topology}.
\end{cases}
}
\]

Thus a coarea/Jacobian argument may be attempted only after the integrability branch is selected.

## 13. Audit verdict

### Certified

1. A finite surface with normal \(n=\xi\) is not automatic.
2. Local existence of vortex-orthogonal surfaces is governed by
   \[
   \tau_\xi=\xi\cdot\operatorname{curl}\xi=0.
   \]
3. The longitudinal curl satisfies
   \[
   \xi\cdot\operatorname{curl}W=\rho\tau_\xi.
   \]
4. Palinstrophy splits exactly as
   \[
   P=\int|\mathcal J_\perp|^2+\int\rho^2\tau_\xi^2.
   \]
5. The M5-618 non-Beltrami gap controls the algebraic transverse current regardless of surface integrability.
6. On Frobenius-integrable patches, the algebraic current is the actual M5-520 material-surface current and the material normal remains aligned with \(\xi\) on CE-H.
7. Failure of integrability is itself a director-twist derivative channel.

### Correction to earlier wording

The unconditional phrase `material-surface current J_Sigma=(curl W) x xi` in M18-071--072 must be read as the **algebraic transverse current** \(\mathcal J_\perp\) unless a Frobenius-integrable vortex-transverse material patch has been certified.

The algebraic formulas and non-Beltrami localization results remain valid.

### Not certified

- a global vortex-orthogonal foliation;
- a positive-area family of integrable patches carrying a fixed fraction of the bulk current;
- a bulk-to-surface trace lower bound;
- exclusion of persistent director twist;
- ancestry closure;
- remote/critical closure;
- global regularity.

## 14. Next target

M18-074 should analyze the two branches separately.

On the integrable branch, construct a controlled local Frobenius chart and derive the exact Jacobian needed to disintegrate

\[
\int|\mathcal J_\perp|^2dy
\]

into a family of transverse surface-current integrals.

On the nonintegrable branch, compare the twist charge

\[
\int\rho^2(\xi\cdot\operatorname{curl}\xi)^2dy
\]

with the existing M16-023--028 director-rank/winding topology to determine whether it is already absorbed or defines a sharper mandatory topology channel.
