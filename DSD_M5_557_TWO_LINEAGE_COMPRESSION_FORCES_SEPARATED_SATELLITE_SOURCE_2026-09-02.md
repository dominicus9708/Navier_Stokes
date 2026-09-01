# DSD M5-557 — If no third lineage pays connector compression, one of the two lineages must carry a separated recurrent satellite source

Date: 2026-09-02

Status: **TWO-LINEAGE SOURCE-SHAPE REDUCTION / M5-556 SHOWS THAT A CENTERED POINT-SOURCE STRAIN MODE HAS ZERO CONNECTOR-NORMAL COMPONENT / SPLITTING THE CONNECTOR INTO SHORT ENDPOINT LAYERS AND A FIXED INTERIOR SEGMENT MAKES THE ENDPOINT-LAYER CONTRIBUTION SMALL BY THE GLOBAL STRAIN CAP / SPLITTING EACH OF THE TWO LINEAGE SOURCES INTO A SMALL MARKER BALL AND ITS HALO MAKES THE SMALL-BALL CONTRIBUTION TO THE INTERIOR CONNECTOR NORMAL STRAIN SMALL BY THE RADIAL-KERNEL CANCELLATION AND THE `|GRAD K|~R^-4` ESTIMATE / THEREFORE, IF THE COMPRESSION PAYER FROM M5-556 IS RESTRICTED TO THE TWO ORIGINAL LINEAGES AND RESIDUAL/REMOTE SOURCES ARE ALREADY SATURATED AWAY, A FIXED NEGATIVE FRACTION OF CONNECTOR COMPRESSION MUST COME FROM A LINEAGE HALO A FIXED FRACTION OF THE PAIR SEPARATION AWAY FROM ITS REPRESENTATIVE MARKER / SMOOTH COMPACTNESS AND CALDERON--ZYGMUND CONTROL CONVERT THIS INTO A FIXED-AMPLITUDE COHERENT SATELLITE VORTICITY PACKET / THE TWO-LINEAGE EXCEPTION IS THUS A RECURRENT MULTI-CENTER SOURCE ARCHITECTURE, NOT A TWO-POINT VORTEX PAIR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Clean two-lineage compression branch

Take the M5-556 branch in which the recurrent connector-compression payer belongs to the two persistent parent/payer lineages:

\[
 c\in\{a,b\}.
\]

The pair separation satisfies

\[
\boxed{
0<d_-\le d(\theta)=|Y_a-Y_b|\le d_+<\infty.
}
\]

The exact mean connector strain is

\[
\boxed{
\langle s_{ab}\rangle=-\frac12,
\qquad
s_{ab}=
\int_0^1n^T\Sigma(Y_b+s r)n\,ds.
}
\]

Remote and recurrent residual compression sources have already been made arbitrarily small by M5-556 source saturation.

---

## 2. Remove short endpoint layers of the connector

The global smooth compact hull has a uniform strain cap

\[
\boxed{
\|\Sigma\|_{L^\infty}\le S_*<\infty.
}
\]

Fix `0<lambda<1/4` and define the interior connector

\[
I_\lambda=[\lambda,1-\lambda].
\]

The two endpoint layers have total parameter length `2 lambda`, hence

\[
\left|
\int_{[0,\lambda]\cup[1-\lambda,1]}
 n^T\Sigma(Y_b+s r)n\,ds
\right|
\le2\lambda S_*.
\]

Choose `lambda` once and for all so that

\[
\boxed{2\lambda S_*\le1/32.}
\]

Thus most of the invariant `-1/2` compression cannot be hidden in arbitrarily short endpoint layers.

---

## 3. Split each lineage into a small marker ball and a halo

Fix a small dimensionless `kappa>0`, later chosen in terms of the compact constants.

Define marker neighborhoods

\[
B_a^\kappa:=B_{\kappa d}(Y_a),
\qquad
B_b^\kappa:=B_{\kappa d}(Y_b).
\]

Using smooth source cutoffs inside the finite core, write

\[
W_a=W_a^{near}+W_a^{halo},
\]

\[
W_b=W_b^{near}+W_b^{halo},
\]

where the near pieces are supported in the respective marker balls.

The halo pieces contain the same-lineage source outside those balls.

---

## 4. Interior connector stays away from both marker centers

For `s in I_lambda`,

\[
|Y_b+s r-Y_b|=sd\ge\lambda d,
\]

and

\[
|Y_b+s r-Y_a|=(1-s)d\ge\lambda d.
\]

Choose

\[
\kappa\le\lambda/4.
\]

Then every point of either near-marker source ball stays a distance at least

\[
\frac12\lambda d
\]

from every point of the interior connector.

Thus the corresponding kernel is smooth there.

---

## 5. Radial cancellation makes a small centered source ball higher order

Consider the `b` near-marker source and an interior connector point

\[
x_s=Y_b+s r.
\]

Its center-to-target direction is exactly `n`.

For any source vector `v`, M5-556 gives

\[
n^TK_S(sd\,n)v\,n=0.
\]

For a source point

\[
z=Y_b+\eta,
\qquad
|\eta|\le\kappa d,
\]

the mean-value theorem gives

\[
\boxed{
|n^T K_S(sd\,n-\eta)v\,n|
\le
C\frac{|\eta|}{(\lambda d)^4}|v|.
}
\]

Therefore

\[
\boxed{
|n^T\mathcal R_{strain}[W_b^{near}](x_s)n|
\le
C\frac{\kappa d}{(\lambda d)^4}
\|W_b^{near}\|_1.
}
\]

The same estimate holds for the `a` near-marker source.

---

## 6. Uniform smallness as `kappa -> 0`

Use the uniform vorticity amplitude cap

\[
|W|\le M_*.
\]

The near source ball has volume `O((kappa d)^3)`, so

\[
\|W_i^{near}\|_1
\le C M_*(\kappa d)^3.
\]

Hence on the interior connector

\[
|n^T\mathcal R_{strain}[W_i^{near}]n|
\le
C M_*
\frac{\kappa^4}{\lambda^4}.
\]

The bounds on `d` cancel exactly.

Thus

\[
\boxed{
\sup_{s\in I_\lambda}
|n^T\mathcal R_{strain}[W_a^{near}+W_b^{near}](x_s)n|
\le
C_*\kappa^4.
}
\]

Choose `kappa` sufficiently small that

\[
\boxed{C_*\kappa^4\le1/32.}
\]

This is the quantitative form of point-mode radial orthogonality for small marker balls.

---

## 7. The interior connector retains a fixed negative source requirement

The full invariant connector mean is `-1/2`.

Subtract

1. endpoint layers: at most `1/32`;
2. remote tail: at most `1/32` after M5-556;
3. saturated residual source: at most `1/32` in invariant mean;
4. the two small near-marker source balls on the interior: at most `1/32` after the fixed `kappa` choice.

Therefore the remaining two-lineage halo source satisfies a fixed negative invariant requirement

\[
\boxed{
\left\langle
\int_{I_\lambda}
 n^T
 \mathcal R_{strain}[W_a^{halo}+W_b^{halo}]
 (Y_b+s r)
 n\,ds
\right\rangle
\le-c_{halo}<0
}
\]

for a universal retained constant `c_halo` (for example one may keep any value below `3/8` after the bookkeeping margins).

Thus the two-lineage branch cannot consist only of two small centered source packets.

---

## 8. At least one lineage halo is a recurrent compression payer

There are only two halo sources.

Hence at least one, say `W_a^halo` after passing to a recurrent subbranch, satisfies

\[
\boxed{
\left\langle
\int_{I_\lambda}
 n^T\mathcal R_{strain}[W_a^{halo}]
 (Y_b+s r)n\,ds
\right\rangle
\le-\frac12c_{halo}.
}
\]

By ergodicity there is a positive-measure set of times on which the corresponding scalar is bounded above by a fixed negative threshold.

---

## 9. Halo compression gives a point strain mark

At each such time, averaging over `s in I_lambda` gives a connector point `x_*` with

\[
\boxed{
 n^T\mathcal R_{strain}[W_a^{halo}](x_*)n
 \le-c_1<0.
}
\]

The source `W_a^halo` is supported outside

\[
B_{\kappa d}(Y_a),
\]

so this fixed compression cannot be attributed to an arbitrarily small marker neighborhood.

Global smooth derivative bounds thicken the scalar strain mark to a fixed spatial neighborhood.

---

## 10. Calderon--Zygmund forces fixed halo vorticity mass

As in M5-553 and M5-556,

\[
\|n^T\mathcal R_{strain}[W_a^{halo}]n\|_2
\le C\|W_a^{halo}\|_2.
\]

The thickened point mark therefore yields

\[
\boxed{
\|W_a^{halo}\|_{L^2(B_{R_{core}})}
\ge e_{halo}>0.
}
\]

The halo lies a distance at least

\[
\kappa d_-
\]

from the representative marker center `Y_a` wherever the cutoff is one.

Thus a fixed amount of same-lineage vorticity mass is recurrently stored at a fixed positive normalized separation from its primary marker.

---

## 11. Extract a coherent separated satellite packet

The halo is contained in the finite active core and the global derivative bounds are uniform.

Fixed `L2` mass in a fixed-volume region gives a point `Z_a` with

\[
|W_a(Z_a)|\ge w_{sat}>0.
\]

A fixed spatial shrinking then yields a coherent satellite ball

\[
B_{r_{sat}}(Z_a)
\]

with

\[
\boxed{
|W|\ge\frac12w_{sat}
}
\]

and controlled direction variation.

Its center obeys

\[
\boxed{
|Z_a-Y_a|
\ge c_{sep}>0
}
\]

on the clean cutoff branch.

Therefore one persistent material lineage has at least two separated recurrent coherent source centers.

---

## 12. The satellite carries fixed directed flux

As in M5-497/555, choose a small cross-sectional disk normal to the satellite's coherent direction.

Then

\[
\boxed{
|\Phi_{sat}|\ge\phi_{sat}>0.
}
\]

If this satellite cannot be genealogically absorbed into the broad existing lineage, it becomes a separate fixed-flux label and returns to finite-memory/new-lineage saturation.

If it is absorbed, the genuine two-lineage branch contains a **multi-center material lineage**.

---

## 13. Finite spatial-packet saturation

Every disjoint fixed-radius, fixed-amplitude coherent satellite costs a fixed amount of enstrophy.

Since

\[
E\le Z_*<\infty,
\]

the finite core can store only finitely many pairwise separated packets of the retained threshold at one time.

Thus repeated halo extraction cannot create an unbounded number of simultaneously separated fixed packets.

After finite spatial refinement, the two-lineage branch saturates to a finite recurrent coherent-packet architecture inside the already finite material-lineage architecture.

This is a **spatial packet saturation**, distinct from but compatible with M5-488 finite material-label memory.

---

## 14. What this does and does not prove

M5-557 rules out the cartoon of two point-like persistent vortices paying all cross-stretching and connector compression.

The survivor must contain an order-one extended/multi-center source geometry.

However a smooth finite-width vortex structure can recurrently carry such a spatial moment without creating infinitely many material labels.

Therefore spatial-packet saturation is not a contradiction.

It produces a more faithful finite-core object:

\[
\boxed{
\text{finite material-lineage network}
+\text{finite recurrent coherent source-center architecture}.
}
\]

---

## 15. Updated new hard core

Outside the already typed internal-dual self branch and the third-lineage compression branch, the two-lineage exception now satisfies

\[
\boxed{
\begin{aligned}
&\text{two persistent material lineages},\\
&\text{positive recurrent cross-stretching},\\
&\text{mean connector compression }-1/2,\\
&\text{and at least one lineage with a recurrent separated satellite source packet}.
\end{aligned}
}
\]

Thus the remaining issue is no longer merely pairwise interaction; it is a finite **source-shape recurrence** problem.

---

## 16. Highest-value next target

Track the lowest nontrivial spatial moment of each saturated lineage source around its representative material marker.

The point/central mode does not contribute connector-normal strain, so recurrent compression is carried by the first nontrivial off-center source moment.

The next audit should determine whether viscosity forces a one-sign evolution of this source-width/first-moment observable after subtracting material transport and similarity dilation.

If no one-sign law exists, construct the exact signed moment balance and identify which production term recycles the spatial source shape.

This directly tests whether the final multi-center architecture has a strict dissipative obstruction or another recurrent recycling mechanism.

---

## 17. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
