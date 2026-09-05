# DSD M17-141 — Order-one remote director ribbons require uniformly frequent recharge or compact-geometry entry in log radius

Date: 2026-09-05  
Canonical ID: **M17-141**

Status: **BOUNDED-SHELL BACKWARD GENEALOGY GATE / A MATERIAL Rank-2 TUBE WITH ORDER-ONE `|J_xi|` CANNOT BE EXPLAINED BY ARBITRARILY LONG PRECHARGED IMPORT THROUGH SUCCESSIVE QUIET COMPACT DYADIC SHELLS. BACKWARD THROUGH EACH LOW-STRAIN REMOTE PASSAGE, `|J_xi|` GROWS BY ASYMPTOTIC FACTOR `4`; THE UNIFORM COMPACT UPPER BOUND THEREFORE ALLOWS ONLY FINITELY MANY SUCH STEPS. EVERY ARBITRARILY REMOTE ORDER-ONE RIBBON MUST HAVE A STRAIN-RECHARGE/CONCENTRATION EVENT OR ENTER THE COMPACT RIBBON CLASS FROM A DIFFERENT GEOMETRIC REGIME WITHIN A UNIFORMLY BOUNDED NUMBER OF INWARD SHELLS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One-shell material identity

Along any regular pure-kernel Rank-2 material trajectory,

\[
\boxed{
D_B\log|J_\xi|=\sigma_k-1.
}
\]

Let one material tube cross a remote dyadic similarity annulus from radius `R` to `2R` in forward similarity time.
M17-138 gives, on the bounded-velocity branch,

\[
\boxed{
\Delta\theta_R
=2\log2+O(R^{-1}).
}
\]

Integrating the director-Jacobian law,

\[
\log\frac{|J_\xi|_{out}}{|J_\xi|_{in}}
=
\int_{I_R}\sigma_kd\theta
-\Delta\theta_R.
\]

Hence backward,

\[
\boxed{
|J_\xi|_{in}
=
|J_\xi|_{out}
\exp\left(
\Delta\theta_R-
\int_{I_R}\sigma_kd\theta
\right).
}
\]

---

## 2. Quiet passage gives an asymptotic factor four backward

Call the material passage `epsilon_R`-quiet when

\[
\boxed{
\int_{I_R}\sigma_kd\theta\le\epsilon_R,
\qquad
\epsilon_R\to0.
}
\]

Then

\[
\frac{|J_\xi|_{in}}{|J_\xi|_{out}}
\ge
\exp(2\log2-\epsilon_R+O(R^{-1})).
\]

Therefore

\[
\boxed{
\frac{|J_\xi|_{in}}{|J_\xi|_{out}}
\ge
4(1-o(1)).
}
\]

For all sufficiently remote shells one may fix any number `lambda_*<4`, for example `lambda_*=3`, and obtain

\[
\boxed{|J_\xi|_{in}\ge\lambda_*|J_\xi|_{out}.}
\]

This is a genealogy statement for one material tube; it is not a population-average substitution.

---

## 3. Uniform compact bounds permit only finitely many quiet inward steps

Retain the uniformly compact nondegenerate ribbon bounds

\[
\boxed{
0<c_J\le|J_\xi|\le C_J<\infty.
}
\]

Suppose an observed outer ribbon satisfies

\[
|J_\xi|_{out}\ge c_J
\]

and the same material Rank-2 tube can be traced inward through `m` successive dyadic passages, each remaining in the compact bounded-`J_xi` geometry and each `epsilon`-quiet as above.

Iterating,

\[
|J_\xi|_{m\,shells\ inward}
\ge
\lambda_*^m c_J.
\]

The compact upper bound requires

\[
\lambda_*^m c_J\le C_J.
\]

Thus

\[
\boxed{
m\le
m_*:=
\left\lfloor
\frac{\log(C_J/c_J)}{\log\lambda_*}
\right\rfloor.
}
\]

The integer `m_*` is independent of the remote radius.

---

## 4. Precharged import cannot be postponed indefinitely

Take an arbitrarily remote complete compact ribbon with order-one director Jacobian.
Trace its material Rank-2 carrier inward.
Within at most `m_*+1` dyadic shell steps, at least one of the hypotheses used above must fail.

Hence one must encounter at least one of:

\[
\boxed{
\begin{aligned}
R_J:&\quad
\int_{I_R}\sigma_kd\theta
\not\ll1
&&\text{(positive kernel-strain recharge/exposure)},\\
C_J:&\quad
|J_\xi|\text{ leaves the compact nondegenerate bounds}
&&\text{(director-geometry concentration/degeneration)},\\
G_R:&\quad
\text{the tube leaves/enters the complete compact-ribbon chart}
&&\text{(geometry/class transition)}.
\end{aligned}
}
\]

Therefore

\[
\boxed{
\text{remote order-one compact ribbon}
\Longrightarrow
R_J\lor C_J\lor G_R
\text{ within bounded inward log-radius distance}.
}
\]

---

## 5. Relation to M17-140 population strain decay

M17-140 shows that on a critical shell with `J_R=O(1)`, kernel strain tends to zero on `1-o(1)` of the compact ribbon population in director-flux/arclength measure.

Consequently, if `R_J` is the mechanism repeatedly preventing backward factor-four growth on a positive fraction of remote order-one ribbons, the recharge must be concentrated on the exceptional ribbon subset isolated in M17-140.

Thus the branch narrows to

\[
\boxed{
\text{frequent concentrated recharge}
\ \lor
\text{frequent compact-geometry transition}.
}
\]

The word `frequent` here means uniformly bounded spacing in dyadic log radius, not positive density in Euclidean radius.

---

## 6. Why fresh carriers do not evade this genealogy gate

Different remote stages may indeed be serviced by different material loops, as M17-135 requires.

The present argument does not identify those loops with one another.
It applies separately to **each** order-one ribbon carrier observed at a remote shell: its own prehistory cannot consist of arbitrarily many quiet compact passages.

Thus fresh-carrier replacement removes the invalid long-time same-marker resonance of M17-134, but it does not remove the bounded-shell origin question.
Every fresh carrier still needs a recent geometric origin/recharge.

---

## 7. No contradiction yet from event frequency

Because dyadic radii grow geometrically, an event every `O(1)` shell steps can still have amplitude-weighted cost

\[
\sim R^{-1}
\]

per event and therefore a summable total cost:

\[
\sum_kR_k^{-1}<\infty.
\]

Likewise signed director-area conservation does not bound positive total variation of repeated recharge/geometry events.

Hence

\[
\boxed{
\text{uniformly frequent recharge/transition}
}
\]

is a strong genealogy restriction but not yet a finite-budget contradiction.

---

## 8. DSD audit

### Audit A — M17-140 population-small strain implies every material passage is quiet

Rejected.
A specific material tube can intersect the exceptional concentrated-strain set.
The present conclusion therefore branches explicitly to recharge/concentration.

### Audit B — fresh-carrier turnover avoids backward genealogy

Rejected.
Each fresh carrier has its own backward genealogy and must itself originate/recharge within bounded shell distance.

### Audit C — backward growth of `|J_xi|` violates signed flux conservation

Rejected.
`|J_xi|` is density; cross-sectional material area changes so signed tube flux remains frozen.

### Audit D — the bounded-shell event frequency alone contradicts finite energy

Rejected.
Known amplitude-weighted event costs can remain geometrically summable.

### Audit E — compact upper bound may be continued through arbitrary geometry transitions

Rejected.
Leaving the compact chart is a genuine separate branch `G_R`, not something over which the bound may be silently propagated.

---

## 9. Updated Rank-2 hard frontier

The remote non-H fixed-fraction Rank-2 ribbon survivor has now been reduced to

\[
\boxed{
\begin{gathered}
\text{genuine }1/R\text{ cubic velocity bath},\\
\rho_R^2\sim R^{-1},\qquad\Phi_R\gtrsim1,\\
\text{fresh }O(1)\text{-time material throughput},\\
\text{typical ribbon strain }\to0,\\
\text{and within }O(1)\text{ dyadic shells backward:}\\
\text{concentrated strain recharge}
\ \lor\
\text{director/compact-ribbon geometry transition}.
\end{gathered}
}
\]

The highest-value next calculation is now the **concentrated-recharge cost gate**.
One must ask whether a vanishing ribbon-population subset can supply order-one positive kernel-strain action to order-one director flux throughput without forcing the existing `H_{2,crit}^{tail}` derivative branch, a pressure/strain nonlocal event, or a non-summable positive cost.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
