# DSD M17-162 — Backward fixed-lag mass explosion splits into a stronger local packet or diverging spatial packet multiplicity

Date: 2026-09-05  
Canonical ID: **M17-162**

Status: **BACKWARD-MASS DICHOTOMY / THE MASS EXIT NEEDED TO EVADE THE M17-158 ETERNAL-`L2` OU CONTRADICTION IS FUNDAMENTALLY A BACKWARD EXIT: AT SOME FIXED NEGATIVE LAG THE AMPLITUDE-NORMALIZED ANCESTOR MASS MUST BECOME UNBOUNDED. COVER THE TRANSLATED REMOTE SHELL BY UNIT-SCALE BALLS. IF ONE BALL CARRIES AN UNBOUNDED NORMALIZED MASS, BOUNDED-`kappa` ELLIPTIC LOCALIZATION PRODUCES A POINT WHOSE AMPLITUDE IS UNBOUNDED RELATIVE TO THE PRESENT NORMALIZATION, SO RECENTERING GIVES A STRONGER LOW-AMPLITUDE OU PACKET CANDIDATE. IF EVERY UNIT BALL HAS UNIFORMLY BOUNDED NORMALIZED MASS, THEN THE TOTAL MASS EXPLOSION REQUIRES A NUMBER OF OCCUPIED SPATIALLY SEPARATED UNIT PACKETS TENDING TO INFINITY. THUS THE SURVIVING MASS GENEALOGY IS AN EXPLICIT CONCENTRATION-VERSUS-MULTIPLICITY DICHOTOMY, NOT AN UNTYPED HIGH-JET ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The genuinely relevant mass exit is backward

At the M17-155 observation time normalize by

\[
a_j=|W(p_j,0)|,
\qquad
|V_j(0,0)|=1.
\]

The relative-thick selection gives

\[
\frac{E_j(0)}{a_j^2}\le C_0.
\]

Forward OU evolution from an `L2` datum is automatically `L2` at every positive time.
The obstruction in M17-158 is the existence of `L2` ancestors for arbitrarily large backward lags.

Hence, to evade M17-158 while retaining the quiet bounded-`kappa` local OU limit, there must exist some fixed `T_0>0` and a subsequence such that

\[
\boxed{
M_j^-:=
\frac{E_j(-T_0)}{a_j^2}
\to\infty.
}
\]

This is the **backward fixed-lag mass explosion**.

---

## 2. Cover the ancestor shell by unit balls

At time `-T_0`, translate by the material center `p_j(-T_0)`.
The corresponding retained remote shell has radius comparable to `R_j` and can be covered by a bounded-overlap family of unit balls

\[
\{B_1(x_{j,m})\}_{m\in\mathcal I_j}.
\]

Define normalized local masses

\[
\boxed{
\mu_{j,m}
:=
\frac1{a_j^2}
\int_{B_1(x_{j,m})}|W(y,-T_0)|^2dy.
}
\]

Bounded overlap gives

\[
\boxed{
M_j^-
\asymp
\sum_{m\in\mathcal I_j}\mu_{j,m}
}
\]

up to a fixed covering constant.

---

## 3. Concentration alternative

Suppose

\[
\boxed{
\max_m\mu_{j,m}\to\infty.
}
\]

Choose `m_j` attaining the maximum.
Then

\[
\int_{B_1(x_{j,m_j})}|W|^2
\gg a_j^2.
\]

By the elementary average bound there exists `q_j in B_1(x_{j,m_j})` such that

\[
|W(q_j,-T_0)|^2
\ge c
\int_{B_1(x_{j,m_j})}|W|^2.
\]

Therefore

\[
\boxed{
\frac{|W(q_j,-T_0)|}{a_j}
\to\infty.
}
\]

Under the quiet shell ceiling and bounded-potential elliptic localization, this stronger amplitude still tends to zero in absolute units.

Recenter and renormalize by

\[
b_j:=|W(q_j,-T_0)|.
\]

This gives a new low-amplitude, stronger-normalization packet and returns to the M17-155 local OU extraction mechanism.

Call this branch

\[
\boxed{G_{ancestor\ concentration}.}
\]

---

## 4. Multiplicity alternative

Suppose instead that there is a fixed `M_*<infinity` such that

\[
\boxed{
\mu_{j,m}\le M_*
\qquad\forall m,j.
}
\]

Since

\[
\sum_m\mu_{j,m}\to\infty,
\]

the number of occupied balls must diverge.

For any fixed threshold `0<mu_*<M_*`, define

\[
N_j(\mu_*)
:=
\#\{m:\mu_{j,m}\ge\mu_*\}.
\]

If `N_j(mu_*)` were uniformly bounded for every fixed threshold in a dyadic decomposition of `[0,M_*]`, the total sum of `mu_{j,m}` could not diverge without pushing all mass to arbitrarily tiny per-ball values. More canonically, choose a dyadic level

\[
2^{-\ell_j-1}M_*<\mu_{j,m}\le2^{-\ell_j}M_*
\]

carrying at least a logarithmic fraction of the total mass.
Then the number `N_j` of balls in that level satisfies

\[
\boxed{
N_j\,\mu_j
\gtrsim
\frac{M_j^-}{1+\log(M_*/\mu_{min,j})},
}
\]

where `mu_j` is the common dyadic size.

In particular, after passing to a useful occupied level, one obtains a family of spatially separated packet cores whose cardinality tends to infinity unless the per-ball mass scale itself tends to zero so fast that the mass is diffuse over the entire remote shell.

Thus the nonconcentrated branch is a genuine **packet-multiplicity / diffuse-volume branch**.

Symbolically:

\[
\boxed{G_{ancestor\ multiplicity}.}
\]

---

## 5. Disjointization

The unit-ball cover has bounded overlap. By a standard finite-coloring/Vitali selection, one may retain a fixed fraction of the occupied balls whose half-balls are pairwise disjoint.

Therefore the multiplicity is not merely a covering artifact.
It can be represented by genuinely spatially separated packet regions.

---

## 6. Exact dichotomy

The backward mass exit is reduced to

\[
\boxed{
G_{mass}^{backward}
\Longrightarrow
G_{ancestor\ concentration}
\ \lor\ 
G_{ancestor\ multiplicity/diffuse}.
}
\]

The first branch returns to a stronger local OU packet after recentering.
The second branch is a scale-critical occupancy problem over the growing remote shell.

This matches the older first-hitting analyticity audit: fixed-order pointwise derivative blowup is not the only hard mechanism; critical mass/occupancy over growing windows can remain large even when every local packet is individually tame.

---

## 7. Relation to Rank-1 / Rank-2 structure

The recentered ancestor packet need not remain on the original Rank-2 ribbon.
Therefore after recentering one must reclassify:

\[
\boxed{
B_{dir}
\Longrightarrow
R_1\lor R_2
}
\]

at the new center.

- Rank-1 recentering is routed to the existing angular-defect / global-pressure firewall.
- Rank-2 recentering returns to the M17-155–160 packet gate.

The multiplicity branch may contain both ranks and should not be assigned one director measure without further evidence.

---

## 8. What remains

The high-value next question is now quantitative:

> Can a quiet bounded-`kappa` remote shell support a diverging number of spatially separated low-amplitude packet cores, each individually below the OU concentration threshold, while maintaining the non-`L3` critical shell stack?

Possible controlling resources are:

1. shell `L2` vorticity mass;
2. shell palinstrophy / bounded-potential spectral ratio;
3. director-area flux only on the Rank-2 subpopulation;
4. finite analytic radius / zero-count only on fixed normalized local boxes;
5. packing geometry of the remote annulus.

No contradiction is claimed yet.

---

## 9. DSD audit

1. A stronger ancestor packet is not assumed to preserve the original director rank.
2. The shell cover is a measure bookkeeping device; director-flux measure is not substituted for it.
3. Diverging occupancy can come from many very small packets; a fixed positive per-ball mass floor is not assumed.
4. The branch is an occupancy/multiplicity problem, consistent with M5-392's analyticity firewall.
5. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
