# Smooth Record-Overlap Closure Criterion — 2026-08-20

Status: **S-LEVEL CONDITIONAL CLOSURE INEQUALITY ON ONE FINITE SMOOTH STAGE. GLOBAL REGULARITY NOT PROVED.**

This note combines four smooth ingredients:

1. finite-stage cross-order tightrope ledger;
2. temporal record/plateau gate;
3. Hardy--Biot--Savart instantaneous palinstrophy bound;
4. record-ball derivative capacity.

No ancient limit or recurrent compact profile is used.

## 1. Select an actual record-growth time

On the record-time branch of `SMOOTH_TEMPORAL_RECORD_PLATEAU_GATE_2026-08-20.md`, assume the positive-middle determinant sector so that `A>=0` on the typed interval. Then

\[
\int_{R_j}\left(\frac NP\right)_+ds
\ge\frac18\log q.
\]

Since

\[
\int_{R_j}b(s)ds=\log q,
\]

there exists an actual smooth record-growth time `s_*` with

\[
\boxed{
\frac NP(s_*)\ge\frac18 b(s_*).
}
\]

Write simply

\[
b=b(s_*),
\qquad
K_2=\|\nabla^2\Omega(s_*)\|_\infty,
\qquad
Q=\|\nabla\Omega(s_*)\|_2^2.
\]

## 2. Instantaneous palinstrophy floor

The Hardy--Biot--Savart estimate is pointwise in time:

\[
\frac NP
\le
\frac{15}{4}\pi^{-2/5}K_2^{1/5}Q^{2/5}.
\]

Together with `N/P >= b/8`,

\[
Q^{2/5}
\ge
\frac{b}{8}
\frac4{15}\pi^{2/5}K_2^{-1/5}.
\]

Therefore

\[
\boxed{
Q
\ge
Q_0
:=
\frac{\pi}{30^{5/2}}
\,b^{5/2}K_2^{-1/2}.
}
\]

This is a finite-stage instantaneous lower bound; the old recurrent lower threshold `q_-` is not needed.

## 3. Spatial H1 overlap forces derivative overlap

Let

\[
n_{H1}(y)
=\frac12\Sigma:(G^TG-GG^T),
\qquad G=\nabla\Omega.
\]

Define the global positive H1 density integral

\[
N_{sp}^+
=\int_{\mathbb R^3}(n_{H1})_+dy.
\]

Since the signed production `N` is positive at `s_*`,

\[
N_{sp}^+\ge N.
\]

Let `B_r` be a record ball centered at a vorticity maximizer. Suppose it captures a fraction `alpha` of positive H1 production:

\[
\boxed{
N_r^+
:=\int_{B_r}(n_{H1})_+dy
\ge\alpha N_{sp}^+,
\qquad 0<\alpha\le1.
}
\]

Then

\[
N_r^+
\ge
\alpha N
\ge
\frac{\alpha b}{8}P.
\]

The whole-space strain-vorticity derivative isometry gives

\[
Q=2P.
\]

Hence

\[
N_r^+
\ge
\frac{\alpha b}{16}Q.
\]

On the record ball let

\[
B_r^S=\|\Sigma\|_{L^\infty(B_r)}.
\]

The local Bottcher--Wenzel estimate gives

\[
N_r^+
\le
\frac{B_r^S}{\sqrt2}Q_r,
\qquad
Q_r=\int_{B_r}|\nabla\Omega|^2dy.
\]

Therefore

\[
\boxed{
\frac{Q_r}{Q}
\ge
\theta_r
:=
\frac{\alpha b}{8\sqrt2\,B_r^S}.
}
\]

Thus spatial H1 overlap automatically forces spatial palinstrophy overlap.

## 4. Insert the instantaneous palinstrophy floor

Since `Q >= Q0`,

\[
Q_r
\ge
\theta_rQ_0.
\]

Explicitly,

\[
\boxed{
Q_r
\ge
\frac{\alpha\pi}{8\sqrt2\,30^{5/2}}
\frac{b^{7/2}}{B_r^S}
K_2^{-1/2}.
}
\]

## 5. Record-ball capacity forces record slack

At the same record point define

\[
\Delta_*
=s_3-b-\delta_{align}
\ge0.
\]

The record-ball capacity lemma gives

\[
Q_r
\le
\frac{4\pi}{3}r^3
\left(
\sqrt{\frac{\Delta_*}{\nu}}+K_2r
\right)^2.
\]

Combining with the lower bound on `Q_r` yields

\[
\boxed{
\Delta_*
\ge
\nu
\left[
C_*
\frac{\alpha^{1/2}b^{7/4}}
{(B_r^S)^{1/2}K_2^{1/4}r^{3/2}}
-K_2r
\right]_+^2,
}
\]

where

\[
\boxed{
C_*
=
\sqrt{
\frac{3}
{32\sqrt2\,30^{5/2}}
}
\approx0.00366713224.
}
\]

This is the first explicit finite-smooth-stage record-overlap closure inequality in the present route.

## 6. Meaning of the inequality

Recall

\[
\Delta_*
=s_3-b-\delta_{align}.
\]

A small `Delta_*` is the efficient-amplification regime:

- vorticity is close to the strongest extensional eigendirection;
- record growth nearly uses the available extensional strain;
- vorticity-gradient diffusion at the maximizer is small.

The new inequality says that this regime cannot simultaneously carry

- a fixed record-time H1 production rate;
- a fixed spatial H1-overlap fraction `alpha`;
- a small record radius `r`;
- and bounded analytic curvature `K2`.

At least one quantity must leave that regime.

## 7. Direct branch split

Fix proposed smooth non-H/T bounds

\[
\Delta_*\le\Delta_0,
\qquad
B_r^S\le B_0,
\qquad
K_2\le K_{2,0}.
\]

Then any record ball carrying overlap `alpha` must satisfy

\[
C_*
\frac{\alpha^{1/2}b^{7/4}}
{B_0^{1/2}K_{2,0}^{1/4}r^{3/2}}
\le
K_{2,0}r
+\sqrt{\frac{\Delta_0}{\nu}}.
\]

Therefore the smooth mainline splits into:

### S-R1 — overlap failure

`alpha` becomes small. H1 production is spatially separated from the vorticity record core, feeding the spatial derivative non-tightness / turnover lane.

### S-R2 — record inefficiency

`Delta_*` is bounded below. The record point pays alignment/diffusion slack and leaves the efficient-amplification lane.

### S-R3 — large record core

`r` must be large enough to carry the derivative packet. This can be compared directly with the already derived analytic/natural core scales.

### S-R4 — curvature growth

`K2` becomes large, which is a directly typed higher-derivative event on the smooth solution.

No additional abstract survivor class is introduced.

## 8. Current status

The record-growth branch is no longer described only qualitatively. One finite smooth stage now yields the explicit chain

\[
\boxed{
\text{cross-order payment}
\Rightarrow
\frac NP\ge\frac b8
\Rightarrow
Q\ge Q_0
\Rightarrow
\text{overlap}\Rightarrow\Delta_*\text{ floor}.
}
\]

The next calculation is to compare the minimum record radius forced here with the independently available analytic/natural radius and with the non-turnover parent-core radius. If those scales cross, the record-time branch becomes S-closed; if they do not, the remaining numerical scale interval is the next literal target.

Status: **FINITE SMOOTH RECORD-TIME P_V PAYMENT PLUS SPATIAL OVERLAP FORCES AN EXPLICIT RECORD-SLACK / RADIUS / CURVATURE TRADEOFF. NEXT = RADIUS CROSSING TEST.**