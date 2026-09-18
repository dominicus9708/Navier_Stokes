# M19-421 — The mixed-leading spectral gap splits exactly into radial/poloidal activity or higher-toroidal activity

Date: 2026-09-19  
Canonical ID: **M19-421**  
Status: **HODGE CHANNEL REFINEMENT / M19-420 MIXED-LEADING GAP IS EXACTLY THE ORTHOGONAL SUM OF RADIAL-POLoidal STRUCTURE AND TOROIDAL l>=2 STRUCTURE / A FIXED SYNDETIC LOWER BOUND CAN BE ASSIGNED TO ONE OF THESE FORMED CHANNELS / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-041 and M19-420

M19-041 gives the exact divergence-free Hodge normal form for the leading critical trace:
\[
A
=
A_r\omega
-
\nabla_{S^2}\Delta_{S^2}^{-1}(\partial_q+1)A_r
+
\omega\times\nabla_{S^2}\psi,
\]
with
\[
\int_{S^2}A_r,d\omega=0.
\]

The first two terms form the radial/poloidal channel, while the last term is toroidal.

M19-420 gives the compact spectral-compensation fork
\[
A_{mix}^{syndetic}
\lor
C_{l=3}^{syndetic,critical},
\]
where
\[
A_{mix}
=
(I-\Pi_{tor,1})A.
\]

## 2. Split the toroidal scalar by harmonic degree

Write
\[
\psi
=
\psi_1
+
\psi_{\ge2},
\]
where \(\psi_1\) is the spherical-harmonic degree-one part and \(\psi_{\ge2}\) contains all \(l\ge2\) modes.

Define
\[
A_{tor,1}
:=
\omega\times\nabla_{S^2}\psi_1,
\]
and
\[
A_{tor,\ge2}
:=
\omega\times\nabla_{S^2}\psi_{\ge2}.
\]

Define the radial/poloidal field
\[
\boxed{
A_{RP}
:=
A_r\omega
-
\nabla_{S^2}\Delta_{S^2}^{-1}(\partial_q+1)A_r.
}
\]

Then
\[
\boxed{
A
=
A_{RP}
+
A_{tor,1}
+
A_{tor,\ge2}.
}
\]

The pure-toroidal-l1 manifold of M19-419--420 is exactly
\[
A_{RP}=0,
\qquad
A_{tor,\ge2}=0.
\]

Hence
\[
\boxed{
A_{mix}
=
A_{RP}
+
A_{tor,\ge2}.
}
\]

## 3. Exact L2 orthogonality

For each fixed \(q\),

- the radial vector \(A_r\omega\) is orthogonal to every tangential field;
- the tangential gradient field
  \[
  -\nabla_{S^2}\Delta_{S^2}^{-1}(\partial_q+1)A_r
  \]
  is Hodge-orthogonal to every toroidal field;
- distinct toroidal spherical degrees are orthogonal.

Therefore
\[
\boxed{
\|A_{mix}\|_{L^2(S^2)}^2
=
\|A_{RP}\|_{L^2(S^2)}^2
+
\|A_{tor,\ge2}\|_{L^2(S^2)}^2.
}
\]

After integration over any fixed log window \(I\),
\[
\boxed{
\|A_{mix}\|_{L^2(I\times S^2)}^2
=
\|A_{RP}\|_{L^2(I\times S^2)}^2
+
\|A_{tor,\ge2}\|_{L^2(I\times S^2)}^2.
}
\]

Thus there is no cross-term ambiguity in the M19-420 mixed-leading gap.

## 4. Quantitative two-channel split

If on one fixed normalized window
\[
\|A_{mix}\|_{L^2(I\times S^2)}
\ge
\eta_A,
\]
then at least one of
\[
\boxed{
\|A_{RP}\|_{L^2(I\times S^2)}
\ge
\frac{\eta_A}{\sqrt2}
}
\]
or
\[
\boxed{
\|A_{tor,\ge2}\|_{L^2(I\times S^2)}
\ge
\frac{\eta_A}{\sqrt2}
}
\]
must hold.

Therefore M19-420 refines to
\[
\boxed{
C_{l=3}
\lor
A_{RP}
\lor
A_{tor,\ge2}.
}
\]

## 5. Syndetic channel selection

The strict lower-bound sets for the three fixed finite-window channels are open in the smooth compact hull topology.

The finite detector family is again finite.

Minimality and the M5-52 return lemma imply that one fixed channel/window can be selected with bounded return gaps on every orbit.

Hence the hard hull has a syndetic witness of one of the following three types:

### R3 — first-residual cubic angular leakage
\[
\boxed{
\|\Pi_3C\|_{L^2(I_*)}
\ge
\eta_3.
}
\]

### RP — radial/poloidal leading critical structure
\[
\boxed{
\|A_{RP}\|_{L^2(I_*)}
\ge
\eta_{RP}.
}
\]

### T+ — higher-toroidal leading structure
\[
\boxed{
\|A_{tor,\ge2}\|_{L^2(I_*)}
\ge
\eta_T.
}
\]

Thus
\[
\boxed{
\mathcal T
\Longrightarrow
R3^{syndetic}
\lor
RP^{syndetic}
\lor
T_{\ge2}^{syndetic}.
}
\]

## 6. Radial/poloidal channel contains a genuine radial scalar

The radial/poloidal branch is not an arbitrary vector sector.

It is determined by the single mean-zero scalar \(A_r\):
\[
A_{RP}
=
A_r\omega
-
\nabla_S\Delta_S^{-1}(\partial_q+1)A_r.
\]

In particular
\[
\|A_{RP}\|_2^2
=
\|A_r\|_2^2
+
\left\|
\nabla_S\Delta_S^{-1}(\partial_q+1)A_r
\right\|_2^2.
\]

Therefore
\[
\boxed{
\|A_{RP}\|_2
\ge
\|A_r\|_2.
}
\]

A nonzero RP witness may thus be attacked through one scalar radial channel plus its forced poloidal completion.

The spherical mean of \(A_r\) remains zero, so this is not a mass-source mode.

## 7. Higher-toroidal channel has no l=1 degeneracy

On
\[
A_{tor,\ge2}
=
\omega\times\nabla_S\psi_{\ge2},
\]
the toroidal scalar has only \(l\ge2\).

Hence the scalar spherical spectral gap is
\[
\boxed{
\int_{S^2}|\nabla_S\psi_{\ge2}|^2d\omega
\ge
6
\int_{S^2}|\psi_{\ge2}|^2d\omega.
}
\]

This removes the \(l=1\) toroidal degeneracy at the level of the generating scalar.

However, as in M19-420, a larger fixed spectral constant does not change the physical critical power by itself.

## 8. Relation to previous firewalls

The three branches are structurally distinct.

### R3

Already known to remain raw-H2 critical under direct unsigned accumulation.

### RP

Cannot be dismissed by zero net radial flux because
\[
\int_{S^2}A_r=0
\]
allows nontrivial sign-changing radial structure.

It requires a signed/coarea/pressure or global observability argument.

### T>=2

Cannot be dismissed by the pure-l1 torque firewall because its toroidal generator lies above the lowest angular mode.

But finite angular eigenvalue alone still supplies only a numerical, not scaling, gain.

Thus no branch is yet closed merely by the decomposition.

## 9. Updated proof frontier

The residual hard core has now been reduced to the formed three-way spectral/Hodge fork

\[
\boxed{
R3^{syndetic,critical}
\lor
RP^{syndetic}
\lor
T_{\ge2}^{syndetic}.
}
\]

This is substantially narrower than the earlier generic residual gap.

The next highest-value calculation is to test the RP branch first, because it carries an actual radial scalar \(A_r\) and therefore can couple to exact sphere-flux/coarea identities that are invisible to the purely toroidal branch.

The target is:

\[
\boxed{
RP^{syndetic}
\Longrightarrow
\text{signed radial crossing / pressure-work / finite-depth witness}
}
\]

or a counterexample/firewall showing that the radial scalar can also recycle critically.

\[
\boxed{\text{M19-421 COMPLETE; THE MIXED-LEADING GAP IS RESOLVED INTO THREE FORMED SYNDETIC CHANNELS.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
