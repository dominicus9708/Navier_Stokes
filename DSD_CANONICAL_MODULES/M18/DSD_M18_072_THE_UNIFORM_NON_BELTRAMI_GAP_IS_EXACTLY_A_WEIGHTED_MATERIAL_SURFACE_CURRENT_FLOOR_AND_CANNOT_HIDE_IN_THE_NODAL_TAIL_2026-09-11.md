# M18-072 — The uniform non-Beltrami gap is exactly a weighted material-surface-current floor and cannot hide in the nodal tail

**Date:** 2026-09-11  
**Status:** M5-618/619 × M18-071 SYNTHESIS / ACTIVE-AMPLITUDE CURRENT LOCALIZATION / NODAL-TAIL FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-071 identifies the CE-H vortex-transverse material-surface current

\[
J_\Sigma
=(\nabla\times W)\times\xi
=-\nabla_\perp\rho+\rho(\xi\cdot\nabla)\xi.
\]

Independently, M5-618 uses the finite-energy Beltrami Liouville theorem as an explicit external dependency and, by compactness of the marked CE-H hull, proves a uniform positive non-Beltrami gap

\[
\boxed{
\|W\times(\nabla\times W)\|_2
\ge b_*>0.
}
\]

M5-619 decomposes that non-Beltrami vector into transverse magnitude gradient and vortex-line curvature.

The present module identifies the two objects exactly and proves that the mandatory current cannot be carried only in an arbitrarily low-amplitude/nodal region.

A fixed positive portion of the non-Beltrami current must live in a uniformly active amplitude region at every marked CE-H state.

## 2. Exact identity between the two currents

On the active set \(\rho>0\),

\[
W=\rho\xi.
\]

M18-071 defines

\[
J_\Sigma
=(\nabla\times W)\times\xi.
\]

M5-619 defines

\[
J_B
:=W\times(\nabla\times W).
\]

Since

\[
\xi\times(\nabla\times W)
=-((\nabla\times W)\times\xi),
\]

we have

\[
\boxed{
J_B=-\rho J_\Sigma.
}
\]

Equivalently,

\[
\boxed{
|J_B|^2
=\rho^2|J_\Sigma|^2.
}
\]

The M5-619 formula

\[
J_B
=\rho\nabla_\perp\rho
-\rho^2(\xi\cdot\nabla)\xi
\]

is therefore exactly \(-\rho\) times the M18-071 surface-current formula.

This is not a new independent geometric current. It is one and the same object viewed under two measures.

## 3. Uniform weighted material-current floor

M5-618 proves on the marked compact CE-H component

\[
\|J_B\|_2\ge b_*>0.
\]

Using Section 2,

\[
\boxed{
\int_{\{\rho>0\}}
\rho^2|J_\Sigma|^2dy
\ge b_*^2.
}
\]

Thus every marked CE-H state carries a fixed positive **amplitude-weighted material-surface-current density** in three-dimensional volume measure.

This statement is distinct from the two-dimensional surface action of M5-521:

\[
\int_{\Sigma(\theta)}|J_\Sigma|^2dA.
\]

The dimensions and measures are different and must not be identified without a trace/thickness argument.

## 4. Uniform palinstrophy ceiling

The marked compact CE-H hull has uniform smooth Sobolev bounds. In particular there exists

\[
\boxed{P_*<\infty}
\]

such that

\[
P(Y)
:=\int|\nabla W|^2dy
=\int|\nabla\times W|^2dy
\le P_*
\]

for every marked state \(Y\).

Since

\[
|J_\Sigma|
=|((\nabla\times W)\times\xi)|
\le|\nabla\times W|
\]

on the active set,

\[
\boxed{
\int|J_\Sigma|^2dy
\le P_*.
}
\]

Extend \(J_\Sigma\) by zero on the nodal set if desired; only the weighted identity \(\rho J_\Sigma=-J_B\) is canonical there.

## 5. The non-Beltrami current cannot hide at arbitrarily small amplitude

For any amplitude threshold \(a>0\),

\[
\begin{aligned}
\int_{\{0<\rho<a\}}
\rho^2|J_\Sigma|^2dy
&\le
 a^2
\int|J_\Sigma|^2dy\\
&\le
 a^2P_*.
\end{aligned}
\]

Choose

\[
\boxed{
 a_B
 :=
 \frac{b_*}{\sqrt{2P_*}}
}
\]

when \(P_*>0\). The case \(P_*=0\) is impossible because it would force \(J_B=0\), contradicting \(b_*>0\).

Then

\[
\int_{\{0<\rho<a_B\}}
\rho^2|J_\Sigma|^2dy
\le
\frac{b_*^2}{2}.
\]

Subtract from the global weighted current floor:

\[
\boxed{
\int_{\{\rho\ge a_B\}}
\rho^2|J_\Sigma|^2dy
\ge
\frac{b_*^2}{2}.
}
\]

This holds at every marked CE-H state.

Thus the mandatory non-Beltrami current cannot be supported solely by a sequence of ever-smaller-amplitude neighborhoods of the vorticity zero set.

## 6. Unweighted active-region current floor

Let the compact amplitude ceiling be

\[
\rho\le M_*<\infty.
\]

Then on \(\{\rho\ge a_B\}\),

\[
\rho^2|J_\Sigma|^2
\le
M_*^2|J_\Sigma|^2.
\]

Hence

\[
\boxed{
\int_{\{\rho\ge a_B\}}
|J_\Sigma|^2dy
\ge
\frac{b_*^2}{2M_*^2}
=:j_B>0.
}
\]

So every marked CE-H state has a fixed positive **bulk L2 transverse-current charge inside a uniformly active amplitude region**.

Again this is a three-dimensional volume statement, not yet a material-surface trace statement.

## 7. Relation to M18-070 core/sheath populations

M18-070 extracts, on the diffusion-depletion branch, two recurrent populations:

\[
\mathcal P_{core}
=\{\rho>a_*,\ G_p\le s_*\},
\]

and

\[
\mathcal P_{sheath}
=\{\rho\le a_*,\ G_p>s_*\}.
\]

M18-072 does **not** imply that the mandatory current is carried by one of these two particular threshold sets.

The current floor lives on

\[
\{\rho\ge a_B\}.
\]

Therefore the correct combined split is spatial/statistical:

\[
\boxed{
\text{mandatory active-region current}
\Longrightarrow
\text{core-associated current}
\lor
\text{intermediate/sheath-associated current}
\lor
\text{component/phase relocation}.
}
\]

A payer-location theorem is still required before identifying the current specifically with the low-amplitude derivative sheath.

## 8. Current-cancelled sheath cannot become a global CE-H state

M18-071 defines the current-cancelled transverse mode

\[
C_\Sigma
=\nabla_\perp\rho+ho(\xi\cdot\nabla)\xi.
\]

A local sheath may satisfy

\[
J_\Sigma\approx0
\]

while \(C_\Sigma\) remains large.

However, M5-618 and Sections 3--6 imply that the entire marked CE-H state cannot approach

\[
J_\Sigma\equiv0
\]

in the weighted/global sense.

Indeed

\[
J_\Sigma=0
\quad\text{a.e. on }\{\rho>0\}
\]

would give

\[
J_B=-\rho J_\Sigma=0,
\]

hence the exact Beltrami branch, which M5-618 excludes on the nonzero finite-energy marked component.

Therefore

\[
\boxed{
\text{current-cancelled local sheath}
\Rightarrow
\text{non-Beltrami current must be paid elsewhere in the same state}.
}
\]

## 9. A payer-location split

Fix the active threshold \(a_B\) from Section 5 and any measurable region \(S(Y)\subset\{\rho\ge a_B\}\) designated as the candidate sheath/current-cancelled carrier.

Then

\[
\int_{\rho\ge a_B}
\rho^2|J_\Sigma|^2
=
\int_{S(Y)}\rho^2|J_\Sigma|^2
+
\int_{\{\rho\ge a_B\}\setminus S(Y)}
\rho^2|J_\Sigma|^2.
\]

Since the total is at least \(b_*^2/2\), at least one term is at least \(b_*^2/4\).

Thus

\[
\boxed{
G_{active\ current}
\Longrightarrow
G_{current\ on\ selected\ carrier}
\lor
G_{current\ relocation}.
}
\]

This is a simple but important nonreuse rule: a current-silent local construction does not eliminate the global non-Beltrami obligation; it relocates it.

## 10. Relation to M5-619 divergence law

M5-619 gives the exact signed divergence law

\[
\boxed{
\nabla\cdot J_B
=|\nabla\times W|^2+\kappa|W|^2.
}
\]

Using

\[
J_B=-\rho J_\Sigma,
\]

we may equivalently write on the active set

\[
\boxed{
-\nabla\cdot(\rho J_\Sigma)
=|\nabla\times W|^2+\kappa\rho^2.
}
\]

The whole-space integral vanishes and reproduces the Rayleigh identity, so no global sign contradiction follows.

But locally this identity says that the active material current transports the mismatch between

- curl/palinstrophy density, and
- negative coefficient/Rayleigh density.

This makes payer location, rather than current existence, the next relevant question.

## 11. External-theorem firewall

The positive constant \(b_*\) ultimately depends on the exact Beltrami exclusion in M5-618, which imports Nadirashvili's finite-energy Beltrami Liouville theorem.

The logical chain is

\[
\boxed{
\text{external exact Beltrami Liouville}
+
\text{internal compactness/nonzero mark}
\Longrightarrow
\text{uniform non-Beltrami gap}
\Longrightarrow
\text{active-region current floor}.
}
\]

No quantitative stability theorem for near-Beltrami fields is imported.

The quantitative gap arises from compactness plus exclusion of the exact zero-defect limit.

## 12. Audit verdict

### Certified

1. The M5-619 non-Beltrami vector and M18-071 material cross-section current satisfy
   \[
   J_B=-\rho J_\Sigma.
   \]
2. The M5-618 uniform non-Beltrami gap is exactly a weighted bulk material-current floor:
   \[
   \int\rho^2|J_\Sigma|^2\ge b_*^2.
   \]
3. Uniform palinstrophy bounds prevent this current from hiding entirely at \(\rho\to0\).
4. There is a fixed amplitude threshold \(a_B>0\) with
   \[
   \int_{\rho\ge a_B}\rho^2|J_\Sigma|^2\ge b_*^2/2.
   \]
5. Hence every marked CE-H state carries a fixed positive bulk L2 transverse current in a uniformly active region.
6. A locally current-cancelled sheath is possible only if the mandatory current is relocated elsewhere in the same state.

### Not certified

- conversion of the bulk current floor to a two-dimensional material-surface current action;
- localization of the current specifically to the M18-070 sheath or core;
- a finite nonreplenishable resource consumed by recurrent current;
- ancestry closure of the current/palinstrophy payment;
- remote/critical closure;
- global regularity.

## 13. Next target

The remaining gap is now a **bulk-to-material-surface trace/thickness problem**.

M5-521 prices actual material-label flux redistribution by

\[
\int_I\int_{\Sigma(\theta)}|J_\Sigma|^2dA\,d\theta,
\]

whereas M18-072 guarantees a three-dimensional active-region lower bound

\[
\int_{\rho\ge a_B}|J_\Sigma|^2dy\ge j_B.
\]

M18-073 should audit whether the existing coherent tube foliation supplies a coarea/disintegration theorem that converts the bulk current floor into a positive family of vortex-transverse material cross-sections with nontrivial current action.

The conversion must preserve the firewall:

\[
\text{bulk }L^2\text{ current}
\not\Rightarrow
\text{one fixed material-surface current}
\]

without a controlled tube-coordinate Jacobian and surface-family thickness.
