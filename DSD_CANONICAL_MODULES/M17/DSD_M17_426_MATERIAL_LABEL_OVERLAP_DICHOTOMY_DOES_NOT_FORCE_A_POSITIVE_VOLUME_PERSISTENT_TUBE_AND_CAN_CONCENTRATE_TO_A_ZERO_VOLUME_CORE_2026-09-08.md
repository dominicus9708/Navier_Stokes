# DSD M17-426 — Material-label overlap does not force a positive-volume persistent tube and may concentrate to a zero-volume core

Date: 2026-09-08  
Canonical ID: **M17-426**

Status: **ACTIVE LABEL-OVERLAP AUDIT / BOREL-CANTELLI FIREWALL / ZERO-VOLUME CORE REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-425

At record scale `R_m`, a selected regular positive-flux material tube band under the retained normalized amplitude and loop-length bounds needs physical material volume at least

\[
\boxed{
\mu(A_m)
\gtrsim cR_m^{-3},
}
\]

where `mu` is the fixed material-particle volume measure on a reference label space and `A_m` is the set of labels selected at record `m`.

For geometric records,

\[
\sum_mR_m^{-3}<\infty.
\]

Thus infinitely many essentially disjoint selections are compatible with finite total label volume.

The present question is whether strong overlap of the `A_m` forces one positive-volume material tube to persist, so that M17-424 applies.

It does not.

## 2. Multiplicity function

Define the material-label selection multiplicity

\[
N(a)
:=
\sum_m\mathbf 1_{A_m}(a).
\]

Then Tonelli gives

\[
\boxed{
\int N(a)d\mu(a)
=
\sum_m\mu(A_m).
}
\]

If the selected bands have only the critical cubic size

\[
\mu(A_m)\asymp R_m^{-3},
\]

then

\[
\sum_m\mu(A_m)<\infty.
\]

Hence

\[
\boxed{
N(a)<\infty
\quad\text{for }\mu\text{-a.e. }a.
}
\]

Equivalently, by the first Borel--Cantelli lemma,

\[
\boxed{
\mu(\limsup_mA_m)=0.
}
\]

Thus the critical cubic turnover regime does not even require a positive-measure set of labels to recur infinitely often.

## 3. Strong overlap may still leave only a zero-volume core

The opposite extreme also does not produce a positive-volume persistent tube.

Let the selected sets be nested:

\[
A_{m+1}\subset A_m,
\qquad
\mu(A_m)\asymp R_m^{-3}\to0.
\]

Then compactness/closedness may give a nonempty intersection

\[
A_\infty:=\bigcap_mA_m,
\]

but continuity from above gives

\[
\boxed{
\mu(A_\infty)
=
\lim_m\mu(A_m)
=0.
}
\]

Thus all record selections may concentrate around the same persistent material line or lower-dimensional label core while no fixed positive-volume tube survives.

M17-424 cannot be applied to a zero-volume core.

## 4. Permanent firewall

The inference

\[
\text{large overlap of selected tube bands}
\Longrightarrow
\text{one fixed positive-volume persistent material tube}
\]

is false.

The safe conclusion is only

\[
\boxed{
G_{label\ overlap}
\Longrightarrow
G_{positive\text{-}volume\ persistent\ tube}
\lor
G_{zero\text{-}volume\ material\ core\ concentration}.
}
\]

The first subbranch is sent by M17-424 to similarity spatial decompactification. The second requires a separate concentration analysis.

## 5. Label-overlap dichotomy

The selected-tube turnover branch can now be organized as

\[
\boxed{
\begin{aligned}
H_{record\text{-}dependent\ selected\ bands}
\Longrightarrow{}&
H_{summable\ essentially\ fresh\ label\ packing}
\\
&\lor H_{persistent\ positive\text{-}volume\ overlap}
\\
&\lor H_{nested/concentrated\ zero\text{-}volume\ core}
\\
&\lor G_{interface/genealogy\ bookkeeping\ loss}.
\end{aligned}
}
\]

The first branch is the M17-425 cubic firewall. The second is M17-424 spatial decompactification. The third is the only genuinely new overlap survivor.

## 6. Positive flux on a shrinking label set is not immediately contradictory

Suppose

\[
\mu(A_m)\asymp R_m^{-3}
\]

while each selected band carries

\[
\Phi_m\ge\Phi_*>0.
\]

Then its flux per unit material volume is of order

\[
\frac{\Phi_m}{\mu(A_m)}
\gtrsim cR_m^3.
\]

This is exactly the natural similarity scaling for a tube of physical length `R_m^{-1}` and physical vorticity magnitude `R_m^2`:

\[
\frac{|\Omega|}{\ell_{ph}}
\sim
R_m^2\cdot R_m
=R_m^3.
\]

Therefore concentration of positive flux onto cubic-shrinking material volume is scale-critical, not supercritical.

No contradiction follows from the density `R_m^3` alone.

## 7. Relation to raw-H2 cubic ancestry

The same exponent has now appeared in three independent descriptions:

1. raw-`H2` ancestral weight `R_m^{-3}`;
2. 3D material-volume similarity Jacobian `R_m^{-3}`;
3. minimum material-label volume of a bounded-normalized-amplitude positive-flux selected tube `R_m^{-3}`.

This agreement indicates that the zero-volume-core survivor is a genuinely scale-critical concentration branch rather than a bookkeeping defect.

## 8. What would close the zero-volume core

A closure requires a theorem stronger than finite material volume. Candidates include:

- a lower bound on the material-label thickness independent of `R_m`;
- a nonconcentration/doubling theorem for the material flux measure in label space;
- a persistent neighborhood theorem around a recurrent material line;
- a derivative/analyticity mechanism converting label-space concentration into spatial raw-`H2` or palinstrophy with a weaker ancestry discount;
- an interface theorem showing that indefinite shrinking of the selected label neighborhood itself pays a nonsummable turnover current.

None is currently certified.

## 9. Exact status of Borel--Cantelli

Only the first Borel--Cantelli implication is used:

\[
\sum_m\mu(A_m)<\infty
\Longrightarrow
\mu(\limsup A_m)=0.
\]

No independence assumption is required.

Conversely, divergence of `sum mu(A_m)` alone would not be enough to guarantee positive measure of the limsup without additional structure. Therefore no converse Borel--Cantelli shortcut is imported into the proof.

## 10. Revised material-label frontier

Combining M17-424--426:

\[
\boxed{
\begin{aligned}
G_{selected\ tube\ turnover}
\Longrightarrow{}&
G_{cubic\ fresh\text{-}label\ packing}\\
&\lor G_{fixed\ positive\text{-}volume\ tube\ spatial\ decompactification}\\
&\lor G_{zero\text{-}volume\ persistent\ material\ core}\\
&\lor G_{flux/amplitude/interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

## 11. Next target

The narrowest new survivor is

\[
\boxed{G_{zero\text{-}volume\ persistent\ material\ core}.}
\]

The next audit should test whether exact CE-H material multiplier transport and spatial analyticity around one persistent material vortex line can force a nonshrinking label neighborhood, or whether arbitrarily thin positive-flux neighborhoods remain compatible with the normalized equations.

This is M17-427.

## 12. DSD audit

DSD is used only to separate overlap of sets from persistence of positive measure. The mathematical argument is finite-measure theory, Tonelli, continuity from above, and Borel--Cantelli.

## 13. Audit verdict

**PASS-NO-GO.**

Material-label overlap alone does not produce a fixed positive-volume tube. The critical survivor may concentrate onto a zero-volume material line/core, so a genuine nonconcentration or interface-cost theorem is still needed.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
