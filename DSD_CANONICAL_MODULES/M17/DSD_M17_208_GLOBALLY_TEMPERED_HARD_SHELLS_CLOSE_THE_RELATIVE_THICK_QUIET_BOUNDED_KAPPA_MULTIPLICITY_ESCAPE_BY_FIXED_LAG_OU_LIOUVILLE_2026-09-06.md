# DSD M17-208 — Globally tempered hard shells close the relative-thick quiet bounded-kappa multiplicity escape by fixed-lag OU Liouville

Date: 2026-09-06  
Canonical ID: **M17-208**

Status: **RANK-2 MULTIPLICITY CLOSURE ON THE TEMPERED HARD-SHELL LANE / M17-205 SHOWS THAT OVER ANY FIXED MATERIAL LAG, ANCESTOR SHELL ENSTROPHY IS CONTROLLED BY FINITELY MANY CURRENT DYADIC NEIGHBORS ON THE COMPACT BOUNDED-KAPPA BRANCH. M17-207 SHOWS THAT THE NONSUMMABLE M5-526 CUBIC PACKING DEFECT CANNOT AVOID A GLOBALLY TEMPERED SUBFAMILY, ON WHICH EVERY FIXED FINITE NEIGHBORHOOD IS UNIFORMLY COMPARABLE TO THE CENTER SHELL. M17-155 RELATIVE THICKNESS GIVES `a_j^2 >= c E_j(0)`. THEREFORE FOR EVERY FIXED LAG `T`, BOTH BACKWARD AND FORWARD NORMALIZED PACKET/SHELL `L2` MASSES ARE UNIFORMLY BOUNDED BY A CONSTANT DEPENDING ONLY ON `T`. M17-158 THEN PRODUCES A NONZERO ETERNAL `L2` OU LIMIT WITH BOUNDED CE-H POTENTIAL, WHICH IS IMPOSSIBLE. HENCE A DIVERGENT HARD STACK CANNOT BE CARRIED ON THE RELATIVE-THICK, QUIET, BOUNDED-KAPPA RANK-2 LANE AT GLOBALLY TEMPERED SCALES. THE REMAINING EXITS ARE RANK REASSIGNMENT/NON-RANK-2 OCCUPANCY, RELATIVE-THIN/NODAL, UNBOUNDED KAPPA, NONQUIET CRITICAL SPACETIME, OR INTERFACE/DOMAIN FAILURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Hard dyadic sequence

Use the M5-526 critical shell costs

\[
\boxed{
b_k(\theta)=R_kE_k(\theta),\qquad R_k=2^kR_0,}
\]

where

\[
E_k(\theta)=\int_{A_k^*}|W(y,\theta)|^2dy
\]

or the equivalent vorticity critical shell mass furnished by the M17-121 Dirichlet/vorticity stack equivalence.

The non-`L^3` hard branch contains a bounded sequence with

\[
\boxed{\sum_k b_k^{3/2}=\infty.}
\]

M17-207 fixes `A>1`, `A^(3/2)>3`, and extracts globally tempered indices satisfying

\[
\boxed{b_{k+m}\le A^{|m|}b_k\qquad\forall m.}
\]

Moreover the tempered subfamily still carries divergent cubic mass.

---

## 2. Relative-thick Rank-2 packet normalization

Suppose a sequence of such tempered hard shells lies on the M17-155 relative-thick Rank-2 ribbon lane.

At time zero choose the M17-155 marked packet point and normalization

\[
\boxed{a_j=|W(p_j,0)|.}
\]

Relative thickness gives

\[
\boxed{a_j^2\ge c_*E_{k_j}(0)}
\]

for a fixed `c_*>0` on the compact nondegenerate packet class.

Therefore

\[
\boxed{
\frac{E_{k_j}(0)}{a_j^2}\le c_*^{-1}.
}
\]

This is the present-time normalized mass ceiling needed for the OU extraction.

---

## 3. Backward fixed-lag mass bound from M17-205

Fix an arbitrary finite lag

\[
T>0.
\]

Assume on the material corridor

\[
|\kappa|\le K_*,
\qquad
|\sigma|\le S_*.
\]

M17-205 supplies integers `s_T`, `M_T` and a finite constant `C_T` such that the ancestor shell mass obeys

\[
\boxed{
E_j(-T)
\le
C_T
\sum_{|m|\le M_T}
E_{k_j+s_T+m}(0).
}
\]

The precise fixed index shift is immaterial because global temperedness controls every integer offset.

For each offset `n=s_T+m`,

\[
E_{k_j+n}(0)
=\frac{b_{k_j+n}(0)}{R_{k_j+n}}
\le
A^{|n|}2^{-n}E_{k_j}(0).
\]

Since only finitely many `n` occur for this fixed `T`, there is a constant `C_{A,T}` with

\[
\boxed{
\sum_{|m|\le M_T}E_{k_j+s_T+m}(0)
\le
C_{A,T}E_{k_j}(0).
}
\]

Hence

\[
\boxed{
E_j(-T)
\le
C_T' E_{k_j}(0).
}
\]

Dividing by the packet normalization,

\[
\boxed{
\frac{E_j(-T)}{a_j^2}
\le
\frac{C_T'}{c_*}.
}
\]

Thus the backward normalized mass cannot explode at this arbitrary fixed lag.

---

## 4. Forward fixed-lag bound

The same argument applies to the inverse material comparison.

Indeed the exact material enstrophy factor in M17-205 has both upper and lower fixed-lag bounds when `|sigma|` and `|kappa|` are bounded.
The inverse flow maps a current fixed-shape shell into finitely many future dyadic neighbors with a finite index shift.
Global temperedness again controls all those neighbors.

Therefore, for every fixed `T`,

\[
\boxed{
\sup_{|\tau|\le T}
\frac{E_j(\tau)}{a_j^2}
\le C_T''<\infty.
}
\]

Equivalently, using `E_j(0)/a_j^2 <= c_*^-1`,

\[
\boxed{
\sup_{|\tau|\le T}
\frac{E_j(\tau)}{E_j(0)}
\le \widetilde C_T<\infty.
}
\]

The constants may grow arbitrarily fast with `T`; M17-158 explicitly allows this.

---

## 5. M17-158 applies

The remaining hypotheses of the present lane are exactly those of the M17-155/158 OU extraction:

1. relative-thick local normalization;
2. quiet remote spacetime strain;
3. bounded CE-H potential `|kappa|<=K_*` on the expanding packet regions;
4. remote Type-I velocity so the residual translated drift disappears;
5. finite normalized `L2` mass for every fixed lag, supplied above.

Hence a diagonal subsequence produces an eternal limit

\[
\boxed{
\partial_\tau V+\frac12 z\cdot\nabla V=\Delta V-V,
}
\]

with

\[
\boxed{V(\tau)\in L^2(\mathbb R^3)\quad\forall\tau\in\mathbb R,}
\]

and

\[
\boxed{|V(0,0)|=1.}
\]

The bounded CE-H multiplier passes to

\[
\Delta V=\kappa_\infty V,
\qquad
|\kappa_\infty|\le K_*.
\]

M17-158 proves that the only eternal `L2` OU solution with this bounded-potential spectral ratio is

\[
\boxed{V\equiv0.}
\]

This contradicts the normalization.

Therefore

\[
\boxed{
R_{2,ribbon}^{relative\text{-}thick,\ quiet,\ bounded\text{-}\kappa,\ tempered}
\Longrightarrow\bot.
}
\]

---

## 6. Effect on the M17-162/163 multiplicity escape

M17-162 introduced backward mass explosion as the escape from the eternal-`L2` OU gate and split it into concentration or multiplicity/diffuse occupancy.

M17-163 left the diffuse multiplicity lane open because raw shell volume can accommodate `O(R^3)` unit packets.

The present result bypasses packet counting:

\[
\boxed{
\text{tempered finite-neighbor shell control}
+\text{material enstrophy comparability}
\Longrightarrow
\text{no fixed-lag mass explosion}.
}
\]

Thus the **diffuse multiplicity escape is closed on the tempered relative-thick quiet bounded-kappa Rank-2 lane**.

---

## 7. How to use the M17-207 extraction globally

A logical subtlety is mandatory.
M17-207 applies to the full bounded critical shell sequence `b_k`.
Its tempered terminal index need not remain on the original Rank-2 subbranch if the director type changes between shells.

Therefore the correct global consequence is a dichotomy:

1. the divergent hard mass has a divergent tempered subfamily that remains on the present relative-thick Rank-2 lane — contradiction by Sections 2--5;
2. a non-negligible part of the charging is routed to tempered shells where the Rank-2 hypotheses fail — this is a **rank reassignment / thin / unbounded-kappa / nonquiet / interface exit**, not a surviving Rank-2 multiplicity mechanism.

Thus one must not claim that M17-208 by itself closes the whole M5 hard stack.
It closes the specific Rank-2 lane and forces the hard cubic mass into another named frontier.

---

## 8. Updated Rank-2 hard frontier

The previous

\[
G_{critical\ multiplicity/occupancy}
\]

is no longer a terminal escape on the relative-thick quiet bounded-kappa tempered lane.

The hard Rank-2 mass must instead route to

\[
\boxed{
G_{relative\text{-}thin/nodal}
\lor
G_{\kappa,\infty}
\lor
H_{1,crit}^{spacetime}
\lor
G_{rank\ reassignment}
\lor
G_{component/interface/domain}.
}
\]

A concentration recentering also immediately re-enters the global `R_1 \lor R_2` rank classification at the stronger packet center.

---

## 9. DSD audit

### Audit A — unknown lag circularity
Removed by M17-207 globally tempered extraction, which controls every fixed finite neighbor width simultaneously.

### Audit B — treating an Eulerian shell as material
M17-205 first materializes the ancestor set and then compares its image to finitely many Eulerian current shells.

### Audit C — assuming every tempered shell is Rank-2
Rejected. Failure of Rank-2 on the tempered charged mass is retained as rank reassignment / another explicit branch.

### Audit D — uniform-in-time mass bound
Not assumed. Constants depend on the fixed lag `T`, exactly as permitted by M17-158.

### Audit E — proof status
A major Rank-2 multiplicity lane is closed, but several hard exits remain and global regularity is not proved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
