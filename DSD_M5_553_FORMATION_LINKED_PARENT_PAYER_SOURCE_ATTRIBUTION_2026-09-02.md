# DSD M5-553 — Formation-linked source attribution extracts a recurrent ordered parent--payer edge or a self-lineage transverse reservoir

Date: 2026-09-02

Status: **FORMATION-LINKED SOURCE ATTRIBUTION / M5-552 SHOWS THAT AN ARBITRARY PERSISTENT DUAL PAIR DOES NOT FORCE CROSS-STRAIN COERCIVITY, SO THE M5-455 PRODUCTIVE FORMATION RELATION MUST BE RETAINED / AT EACH FIRST-HITTING PRODUCTIVE EVENT THE POSITIVE AXIAL STRAIN AT THE PARENT MARKER IS DECOMPOSED LINEARLY AMONG THE FINITELY MANY SATURATED LINEAGE SOURCE PIECES, A RESIDUAL CORE, AND THE REMOTE TAIL / THE REMOTE TAIL IS UNIFORMLY NEGLIGIBLE, WHILE A RECURRENT ORDER-ONE RESIDUAL CONTRIBUTION WOULD, BY SMOOTH THICKENING AND L2 CALDERON--ZYGMUND CONTROL, CONTAIN FIXED VORTICITY MASS AND THEREFORE REENTER THE M5-497 NEW-PAYER SATURATION FORK / ON THE SATURATED QUIET BRANCH A FINITE LINEAGE MUST PAY A FIXED POSITIVE SHARE OF THE PARENT STRAIN / FINITE PIGEONHOLE EXTRACTION PRODUCES A RECURRENT ORDERED PARENT--PAYER EDGE / THE PAYER MAY EQUAL THE PARENT, LEAVING A SELF-LINEAGE TRANSVERSE-RESERVOIR BRANCH, OR BE DISTINCT, GIVING A GENUINE CROSS-LINEAGE BIOT--SAVART EDGE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Productive parent event

Use the M5-455 first-hitting block on the compact quiet branch.

At a productive event choose the active parent marker

\[
x_a,
\qquad
 e_a:=\xi_a(x_a),
\]

so that the longitudinal strain has a fixed positive pointwise lower mark after the M5-453/455 time-selection and continuity audit:

\[
\boxed{
q_a
:=
e_a^T\Sigma(x_a)e_a
\ge q_*>0.
}
\]

The constants are generation-independent on the retained compact corridor.

Analyticity gives a fixed spatial/time neighborhood on which the corresponding productive strain remains quantitatively nonzero unless an already typed derivative/remote exit occurs.

---

## 2. Saturated finite source family

M5-497 gives a saturated finite persistent lineage family

\[
\boxed{
\mathcal L_{sat}
=
\{L_1,\ldots,L_N\},
\qquad
N\le N_{max}.
}
\]

For the current event choose smooth genealogical cutoffs

\[
\chi_1,\ldots,\chi_N
\]

around the coherent representatives of these lineages in the fixed active core.

Set

\[
W_\ell:=\chi_\ell W.
\]

The cutoffs are bookkeeping partitions of the common source; the individual `W_l` need not themselves be globally divergence-free vorticities.

The strain operator is linear, so this source attribution is still exact after adding the residual pieces.

---

## 3. Exact scalar source attribution

Let

\[
\mathcal T_{e_a}[F](x)
:=
e_a^T\mathcal R_{strain}[F](x)e_a.
\]

Then

\[
q_a
=
\sum_{\ell=1}^{N}q_{a\leftarrow\ell}
+q_{a\leftarrow res}
+q_{a\leftarrow tail},
\]

where

\[
\boxed{
q_{a\leftarrow\ell}
:=
\mathcal T_{e_a}[W_\ell](x_a).
}
\]

The arrow denotes **source attribution**, not material transfer:

\[
L_\ell\to L_a
\quad\text{means that lineage }\ell\text{ contributes to the axial strain sampled by parent }a.
\]

It is distinct from the M5-498 flux-transfer graph.

---

## 4. The remote attributed source is negligible

M5-534 and M5-552 give uniform far-strain smallness.

For sufficiently large fixed `R_core`,

\[
\boxed{
|q_{a\leftarrow tail}|
\le \varepsilon_{tail}
}
\]

with

\[
\varepsilon_{tail}\le q_*/16
\]

uniformly at every retained productive event.

The generation-integrated contribution is also arbitrarily small by M5-542.

Thus no productive parent event can be attributed primarily to the endpoint spectator tail.

---

## 5. Residual point contribution: the two alternatives

Fix

\[
\varepsilon_{res}:=q_*/16.
\]

At a productive event either

\[
|q_{a\leftarrow res}|<\varepsilon_{res},
\]

or

\[
|q_{a\leftarrow res}|\ge\varepsilon_{res}.
\]

The second case cannot be dismissed as a bookkeeping remainder.

Because the full compact hull has uniform high derivative bounds and the residual cutoff family is fixed-scale, the scalar residual strain field

\[
q_{res}(x)
:=e_a^T\mathcal R_{strain}[W_{res}](x)e_a
\]

has uniform local derivative bounds.

Hence a fixed point amplitude

\[
|q_{res}(x_a)|\ge\varepsilon_{res}
\]

thickens to a fixed ball on which

\[
|q_{res}|\ge c\varepsilon_{res}.
\]

Therefore

\[
\boxed{
\|q_{res}\|_{L^2(B_*)}
\ge c_*>0.
}
\]

---

## 6. Calderon--Zygmund converts residual strain into residual vorticity mass

The scalar operator `T_e` is a zero-order Calderon--Zygmund transform.

Thus

\[
\|q_{res}\|_2
\le C\|W_{res}\|_2.
\]

The preceding lower bound gives

\[
\boxed{
\|W_{res}\|_2
\ge c_W>0.
}
\]

on a fixed bounded source region.

Using the compact `L^infinity` derivative bounds exactly as in M5-497, a fixed residual `L2` mass contains a fixed-amplitude, fixed-radius coherent vorticity payer packet.

Hence a recurrent order-one residual strain source is a genuine M5-497 residual-payer event.

---

## 7. Residual recurrence reenters finite-memory saturation

If

\[
|q_{a\leftarrow res}|
\ge\varepsilon_{res}
\]

occurs recurrently on a positive-density set of productive events, the extracted coherent residual packet must either

1. be genealogically absorbed into one of the existing persistent lineages; or
2. create a fixed new/replacement flux label; or
3. trigger an already typed costed exit.

M5-397/M5-488 forbid indefinite quiet storage of genuinely new fixed-flux labels.

Therefore on the fully saturated no-exit branch we may refine the finite lineage representation so that

\[
\boxed{
|q_{a\leftarrow res}|<q_*/16
}
\]

at the retained recurrent productive events.

This is the source-attribution analogue of M5-497 saturation.

---

## 8. A finite lineage must pay a positive share

On the saturated branch,

\[
q_a
=
\sum_{\ell=1}^{N}q_{a\leftarrow\ell}
+O(q_*/8).
\]

Since

\[
q_a\ge q_*,
\]

we have

\[
\sum_{\ell=1}^{N}q_{a\leftarrow\ell}
\ge\frac78q_*.
\]

Therefore at least one lineage index `ell` satisfies

\[
\boxed{
q_{a\leftarrow\ell}
\ge
\frac{7q_*}{8N}
\ge
\frac{7q_*}{8N_{max}}
=:q_{pay}>0.
}
\]

This is a **positive signed contribution**, not merely an absolute-value lower bound.

Negative source contributions from other lineages only make the positive-share requirement stronger.

---

## 9. Finite ordered-pair pigeonhole

The parent label `a` belongs to the same finite persistent family, and the payer index `ell` also belongs to that family.

There are at most

\[
N_{max}^2
\]

ordered parent--payer pairs.

Because productive first-hitting blocks recur at fixed positive density on the retained component, after passing to a positive-density subsequence there exists one fixed ordered pair

\[
(a_*,b_*)
\]

such that

\[
\boxed{
q_{a_*\leftarrow b_*}
\ge q_{pay}>0
}
\]

at positive similarity/log-scale frequency.

Thus the compact hard core carries a recurrent **formation-linked Biot--Savart source edge**.

---

## 10. Source edge versus transfer edge

The new edge

\[
b_*\rightsquigarrow a_*
\]

must not be confused with the material-transfer edge of M5-498.

It means

\[
\boxed{
 e_{a_*}^T
 \mathcal R_{strain}[W_{b_*}](x_{a_*})
 e_{a_*}
 \ge q_{pay}.
}
\]

The lineage `b_*` may remain materially distinct from `a_*` while repeatedly supplying positive axial strain to it through the common velocity field.

This is the first retained graph edge that comes directly from the PDE kernel rather than genealogy bookkeeping.

---

## 11. Two exact subbranches

There are now two possibilities.

### A. Genuine cross-lineage payer

\[
\boxed{
b_*\ne a_*.}
\]

Then one persistent lineage repeatedly supplies a positive order-one Biot--Savart stretching contribution to another persistent lineage.

This produces a genuine directed interaction edge

\[
L_{b_*}\rightsquigarrow L_{a_*}.
\]

### B. Self-lineage payer

\[
\boxed{b_*=a_*.}
\]

Then the productive parent repeatedly pays a fixed share of its own axial strain through the vorticity source assigned to its own material lineage.

This is not a trivial aligned self-field.

The directional-depletion identity underlying M5-454 annihilates a source exactly parallel to `e_a`; therefore the self-payer contribution requires a fixed transverse/angular reservoir somewhere in that lineage's source representation.

Hence the self branch becomes

\[
\boxed{
\text{persistent lineage}
+\text{recurrent internal transverse source reservoir}.
}
\]

---

## 12. Relation to the M5-455 companion

M5-455 already extracted a coherent noncollinear companion packet from the transverse source forced by productive strain.

M5-553 does **not** assert that the payer `b_*` is automatically identical to that selected companion label.

The depletion inequality is a collective source relation, and several finite packets can contribute with different signs.

The correct statement is weaker and rigorous:

\[
\boxed{
\text{productive strain}
\Rightarrow
\text{at least one recurrent finite source payer}
}
\]

plus the independently retained recurrent noncollinear companion geometry.

Identifying the payer with the companion requires an additional source-localization theorem and is not assumed.

---

## 13. DSD audit of source partitions

Three distinctions must remain explicit.

1. `W_l=chi_l W` is a linear source partition, not necessarily an autonomous vorticity solution.
2. `b -> a` is a Biot--Savart source edge, not a material-flux transfer edge.
3. recurrent residual source cannot simply be discarded; it is routed back into M5-497 saturation before the finite-payer conclusion is used.

These prevent the finite graph from silently gaining PDE properties it has not proved.

---

## 14. Updated active-core frontier

The active recurrent core now carries

\[
\boxed{
\begin{aligned}
&\text{finite persistent material lineages},\\
&\text{positive axial production},\\
&\text{recurrent noncollinear dual geometry},\\
&\text{positive ratchet/projective activity},\\
&\text{and a recurrent ordered positive Biot--Savart payer edge}.
\end{aligned}
}
\]

The payer edge satisfies either

\[
\boxed{
\mathcal E_{cross}^{pay}
\lor
\mathcal E_{self}^{transverse}.
}
\]

This is strictly more informative than the M5-551 abstract graph.

---

## 15. Highest-value next target

Audit the two payer branches separately.

### P1 — cross-lineage reciprocity/geometry

For `b != a`, analyze the pair of interaction scalars

\[
q_{a\leftarrow b},
\qquad
q_{b\leftarrow a},
\]

from the exact strain kernel.

Determine whether persistent positive one-way stretching forces

- reverse strain of controlled sign;
- pair-frame motion;
- a third payer source;
- or an irreversible transfer/diffusion cost.

### P2 — self-lineage angular reservoir

For `b=a`, use the exact directional-depletion representation to quantify the amount and geometry of transverse vorticity required inside the same material lineage.

Determine whether that persistent internal angular reservoir must split into an independently stored fixed-flux descendant, or instead forces a recurrent direction-gradient/projective charge beyond the already recyclable threshold.

These are now the two concrete PDE branches.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
