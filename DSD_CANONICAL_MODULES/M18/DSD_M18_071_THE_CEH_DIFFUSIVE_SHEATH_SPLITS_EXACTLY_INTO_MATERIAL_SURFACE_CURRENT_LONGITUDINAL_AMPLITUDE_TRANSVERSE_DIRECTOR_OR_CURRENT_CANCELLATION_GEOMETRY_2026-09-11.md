# M18-071 — The CE-H diffusive sheath splits exactly into material-surface current, longitudinal amplitude, transverse director, or current-cancellation geometry

**Date:** 2026-09-11  
**Status:** MATERIAL-SURFACE CURRENT AUDIT / EXACT PALINSTROPHY CHANNEL DECOMPOSITION / ANTI-SHORTCUT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-070 proves that the diffusion-depletion branch contains a quantitative lower-amplitude derivative sheath and a higher-amplitude lower-diffusion core.

A tempting shortcut is

\[
\text{derivative sheath}
\Longrightarrow
\text{material-surface current}
\Longrightarrow
\text{marker migration}.
\]

That implication is too strong.

The derivative sheath may be carried by longitudinal amplitude variation, director deformation, or a geometric cancellation invisible to the surface current.

The present module derives the exact CE-H decomposition and identifies precisely which part is seen by the M5-520--522 material-current machinery.

For \(p=2\) the decomposition is an exact orthogonal identity.

## 2. CE-H transverse material cross-sections

On CE-H,

\[
W=\rho\xi,
\qquad
\Sigma\xi=\sigma\xi,
\qquad
D_B\xi=0.
\]

Let \(\Sigma(\theta)\) be a material surface transported by

\[
B=U+\frac12y
\]

whose normal initially satisfies

\[
n=\xi.
\]

The material normal evolves by the standard rule

\[
D_Bn
=
-P_n^\perp(\nabla B)^Tn.
\]

Now

\[
\nabla B
=\Sigma+A+\frac12I.
\]

Since the antisymmetric velocity-gradient part has rotation axis parallel to the vorticity,

\[
A\xi=0.
\]

Therefore

\[
(\nabla B)^T\xi
=(\Sigma-A+\tfrac12I)\xi
=(\sigma+\tfrac12)\xi.
\]

Its transverse projection vanishes, so

\[
\boxed{
D_Bn=0
\quad\text{when}\quad n=\xi.
}
\]

Because also \(D_B\xi=0\), an initially vortex-transverse material cross-section remains vortex-transverse throughout the retained CE-H interval.

Thus the M5-520 surface-current law may be evaluated with

\[
\boxed{n=\xi.}
\]

## 3. Exact surface-current formula

M5-520--521 define

\[
J_\Sigma
:=(\nabla\times W)\times n.
\]

Set \(n=\xi\) and use

\[
W=\rho\xi.
\]

Then

\[
\nabla\times W
=\nabla\rho\times\xi
+\rho\nabla\times\xi.
\]

Hence

\[
J_\Sigma
=(\nabla\rho\times\xi)\times\xi
+\rho(\nabla\times\xi)\times\xi.
\]

Define

\[
\partial_\parallel\rho
:=\xi\cdot\nabla\rho,
\]

\[
\nabla_\perp\rho
:=(I-\xi\otimes\xi)\nabla\rho,
\]

and the vortex-line curvature vector

\[
\boxed{
\mathcal K_\xi
:=(\xi\cdot\nabla)\xi.
}
\]

The vector identities

\[
(\nabla\rho\times\xi)\times\xi
=-\nabla_\perp\rho
\]

and, because \(|\xi|=1\),

\[
(\nabla\times\xi)\times\xi
=(\xi\cdot\nabla)\xi
=\mathcal K_\xi
\]

give

\[
\boxed{
J_\Sigma
=-\nabla_\perp\rho
+\rho\mathcal K_\xi.
}
\]

This is the exact CE-H material-surface current on a vortex-transverse material cross-section.

## 4. Current-visible and current-cancelled transverse modes

Set

\[
a:=\nabla_\perp\rho,
\qquad
b:=\rho\mathcal K_\xi.
\]

Then

\[
\boxed{J_\Sigma=b-a.}
\]

Define the complementary transverse combination

\[
\boxed{
C_\Sigma:=a+b
=\nabla_\perp\rho+\rho\mathcal K_\xi.
}
\]

The elementary parallelogram identity gives

\[
\boxed{
|a|^2+|b|^2
=
\frac12|J_\Sigma|^2
+
\frac12|C_\Sigma|^2.
}
\]

Thus transverse amplitude-gradient plus vortex-line-curvature energy has two orthogonal algebraic modes:

1. the material-surface-current mode \(J_\Sigma\);
2. the current-cancelled mode \(C_\Sigma\).

When \(J_\Sigma\) is small but \(|a|^2+|b|^2\) is large, one necessarily has

\[
a\approx b,
\]

that is,

\[
\boxed{
\nabla_\perp\rho
\approx
\rho\mathcal K_\xi.
}
\]

This is a geometric amplitude-curvature locking relation, not zero derivative activity.

## 5. Director-gradient decomposition

Decompose the full director gradient into the derivative along the vortex line and derivatives transverse to it.

Because

\[
(\xi\cdot\nabla)\xi
=\mathcal K_\xi,
\]

write

\[
\boxed{
|\nabla\xi|^2
=
|\mathcal K_\xi|^2
+|\nabla_\perp\xi|^2,
}
\]

where \(|\nabla_\perp\xi|^2\) denotes the squared Hilbert--Schmidt norm of derivatives in the two directions orthogonal to \(\xi\).

Also

\[
\boxed{
|\nabla\rho|^2
=
|\partial_\parallel\rho|^2
+|\nabla_\perp\rho|^2.
}
\]

## 6. Exact p=2 palinstrophy identity

For \(p=2\), M18-069 has

\[
\rho^2G_2
=|\nabla W|^2
=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
\]

Using Sections 4--5,

\[
\begin{aligned}
|\nabla W|^2
={}&
|\partial_\parallel\rho|^2
+|\nabla_\perp\rho|^2\\
&+
\rho^2|\mathcal K_\xi|^2
+
\rho^2|\nabla_\perp\xi|^2\\
={}&
|\partial_\parallel\rho|^2
+
\rho^2|\nabla_\perp\xi|^2\\
&+
\frac12|J_\Sigma|^2
+
\frac12|C_\Sigma|^2.
\end{aligned}
\]

Therefore

\[
\boxed{
|\nabla W|^2
=
|\partial_\parallel\rho|^2
+
\rho^2|\nabla_\perp\xi|^2
+
\frac12|J_\Sigma|^2
+
\frac12|C_\Sigma|^2.
}
\]

This is an exact nonnegative four-channel decomposition of palinstrophy density on CE-H.

## 7. Four possible realizations of the M18-070 sheath

Let \(\mathcal P_{sheath}\) be the lower-amplitude/high-diffusion population from M18-070.

A fixed positive palinstrophy payment on that population must be carried by at least one of the following four channels.

### Channel I — longitudinal amplitude variation

\[
\boxed{
G_{\parallel\rho}:
\quad
|\partial_\parallel\rho|^2
\text{ pays a fixed share.}
}
\]

This is amplitude variation along the same vortex line.

It does not by itself imply transverse material-label migration.

### Channel II — transverse director deformation

\[
\boxed{
G_{\perp\xi}:
\quad
\rho^2|\nabla_\perp\xi|^2
\text{ pays a fixed share.}
}
\]

This routes directly to the M16-023--028 director-area / rank / winding architecture.

### Channel III — material-surface current

\[
\boxed{
G_J:
\quad
|J_\Sigma|^2
\text{ pays a fixed share.}
}
\]

This is the only channel that directly enters the M5-520--522 material-surface current machinery.

Under the controlled material-surface geometry used there,

\[
G_J
\Longrightarrow
\text{surface-current throughput}
\Longrightarrow
\text{bulk palinstrophy after thickness}.
\]

If it corresponds to redistribution across persistent material-label regions, M5-521 prices the marker migration.

### Channel IV — current-cancelled amplitude-curvature locking

\[
\boxed{
G_C:
\quad
|C_\Sigma|^2
=|\nabla_\perp\rho+\rho\mathcal K_\xi|^2
\text{ pays a fixed share.}
}
\]

This channel can remain large while the actual material-surface current is small.

It represents a geometric locking of transverse amplitude gradient to vortex-line curvature.

## 8. Quantitative four-way split

Suppose on a recurrent sheath event family

\[
\int_{\mathcal P_{sheath}}|\nabla W|^2dy
\ge p_{sh}>0.
\]

Then the exact identity gives

\[
\boxed{
\begin{aligned}
p_{sh}
\le{}&
\int_{\mathcal P_{sheath}}|\partial_\parallel\rho|^2dy\\
&+
\int_{\mathcal P_{sheath}}\rho^2|\nabla_\perp\xi|^2dy\\
&+
\frac12\int_{\mathcal P_{sheath}}|J_\Sigma|^2dy\\
&+
\frac12\int_{\mathcal P_{sheath}}|C_\Sigma|^2dy.
\end{aligned}
}
\]

Therefore at least one term is bounded below by a fixed fraction of \(p_{sh}\).

For example one may route with the harmless constants

\[
\boxed{
G_{\parallel\rho}
\lor
G_{\perp\xi}
\lor
G_J
\lor
G_C.
}
\]

No surface-current conclusion may be drawn before this split.

## 9. Why longitudinal amplitude variation is already material information

On each CE-H vortex line, \(\kappa\) is spatially constant:

\[
\partial_\parallel\kappa=0.
\]

Therefore spatial variation of the net amplitude-growth field

\[
h=\sigma+\kappa
\]

along one vortex line is exactly axial-strain variation:

\[
\boxed{
\partial_\parallel h
=
\partial_\parallel\sigma.
}
\]

A recurrent longitudinal amplitude core/sheath pattern is therefore not an arbitrary scalar layer.

Combined with the material amplitude equation

\[
D_B\log\rho=h-1,
\]

and the M18-068 generalized residence baselines, persistent linewise amplitude segregation routes to

\[
\boxed{
\text{same-line strain heterogeneity}
\lor
\text{marker/residence turnover}.
}
\]

Thus Channel I reconnects to M16-022 rather than to M5-521.

## 10. Why transverse director deformation is not automatically current

The surface current sees the particular curvature combination

\[
\rho\mathcal K_\xi
=
\rho(\xi\cdot\nabla)\xi.
\]

It does not directly see all of

\[
\nabla_\perp\xi.
\]

Hence large transverse director shear/twist may exist even when \(J_\Sigma\) is small.

This is exactly why the director-rank/topology branch must remain separate.

The shortcut

\[
|\nabla\xi|\text{ large}
\Rightarrow
|J_\Sigma|\text{ large}
\]

is invalid.

## 11. The current-cancelled channel is a new sharp geometric target

If Channel IV dominates while Channel III is small, then

\[
\nabla_\perp\rho
\approx
\rho\mathcal K_\xi.
\]

Equivalently, where \(\rho>0\),

\[
\boxed{
\nabla_\perp\log\rho
\approx
\mathcal K_\xi.
}
\]

This relation ties the curvature of the vortex line directly to the transverse logarithmic amplitude profile.

It resembles the geometric identity for curvature of weighted line congruences, but no rigidity theorem is imported here.

The important point is only that a current-silent derivative sheath is not free: it must organize into this amplitude-curvature locking or pay one of the other channels.

## 12. Higher-p comparison

For general \(p\ge2\),

\[
\rho^pG_p
=
(p-1)\rho^{p-2}|\nabla\rho|^2
+
\rho^p|\nabla\xi|^2.
\]

The same geometric decomposition gives

\[
\begin{aligned}
\rho^pG_p
={}&
(p-1)\rho^{p-2}|\partial_\parallel\rho|^2
+
\rho^p|\nabla_\perp\xi|^2\\
&+
(p-1)\rho^{p-2}|a|^2
+
\rho^{p-2}|b|^2,
\end{aligned}
\]

with \(a=\nabla_\perp\rho\) and \(b=\rho\mathcal K_\xi\).

Because \(p-1\ge1\), the last two terms are comparable, up to \(p\)-dependent constants, to

\[
\rho^{p-2}|J_\Sigma|^2
+
\rho^{p-2}|C_\Sigma|^2.
\]

Thus the same four-channel routing persists for every fixed finite \(p\), although the \(p=2\) identity is the clean exact orthogonal decomposition.

## 13. Relation to the M5-521--522 migration ledger

M5-521 proves that a fixed amount of signed flux redistribution across a fixed material-label distance forces positive material-surface current action.

M5-522 thickens controlled surface-current action into bulk palinstrophy.

M18-071 establishes the converse firewall:

\[
\boxed{
\text{bulk/sheath palinstrophy}
\not\Rightarrow
\text{material-label migration current}.
}
\]

Only the \(G_J\) share of the sheath is directly visible to that ledger.

The remaining shares are separately typed geometric/material channels.

## 14. Audit verdict

### Certified

1. A vortex-transverse material cross-section remains transverse on CE-H.
2. Its exact current is
   \[
   J_\Sigma=-\nabla_\perp\rho+\rho(\xi\cdot\nabla)\xi.
   \]
3. For \(p=2\), palinstrophy density has the exact decomposition
   \[
   |\nabla W|^2
   =|\partial_\parallel\rho|^2
   +\rho^2|\nabla_\perp\xi|^2
   +\tfrac12|J_\Sigma|^2
   +\tfrac12|C_\Sigma|^2.
   \]
4. Therefore the M18-070 derivative sheath splits into longitudinal-amplitude, transverse-director, surface-current, or current-cancelled amplitude-curvature channels.
5. Only the surface-current channel directly invokes M5-521--522.
6. A current-silent transverse derivative sheath must support amplitude-curvature locking if the other invisible channels are small.

### Not certified

- that the sheath must have a positive surface-current share;
- that amplitude-curvature locking is impossible;
- that transverse director deformation necessarily produces flux migration;
- ancestry closure of any of the four channels;
- remote/critical closure;
- global regularity.

## 15. Next target

After this audit, the genuinely new sharp subbranch is

\[
\boxed{
G_C:
\quad
\nabla_\perp\log\rho
\approx
(\xi\cdot\nabla)\xi
}
\]

on a lower-amplitude derivative sheath with small material-surface current.

M18-072 should test this **amplitude-curvature locking** against the exact constraints

\[
\nabla\cdot W=0,
\qquad
\Delta W=\kappa W,
\qquad
W\cdot\nabla\kappa=0.
\]

The first question is whether the locking condition has an exact divergence/curvature interpretation that reduces the sheath to

- a weighted area-convergence law;
- a director-rank/topology branch;
- or a nonzero surface current after all.

This should be audited before differentiating the locking relation and escalating derivative order.
