# DSD M5-643 — Material volume is generation-summable; scale-invariant vorticity flux is not generation-discounted

Date: 2026-09-03

Status: **DSD RESOURCE AUDIT / M5-642 LOCALIZES ALL FUTURE CORE PACKET LABELS TO ONE FINITE INNER MATERIAL RESERVOIR, BUT FINITE RESERVOIR VOLUME DOES NOT CONTRADICT INFINITE REPLACEMENT: PULLBACK VOLUMES OF FIXED-SIZE FUTURE PACKETS ARE DISCOUNTED BY `exp(-3 Delta theta/2)` AND CAN FORM A CONVERGENT GEOMETRIC SERIES. BY CONTRAST, VORTICITY FLUX IS NAVIER--STOKES CRITICAL AND A NEGATIVE-KAPPA MATERIAL LABEL HAS NONINCREASING FORWARD FLUX, SO A FUTURE PACKET WITH `|Phi|>=phi_*` REQUIRES AT LEAST THE SAME FLUX IN THE PAST, WITH NO GENERATION DISCOUNT. A TRUE FINITE-RESOURCE CONTRADICTION WOULD THEREFORE REQUIRE A GLOBAL TRANSVERSAL/ADDITIVITY LEMMA BOUNDING THE TOTAL ABSOLUTE FLUX OF DISJOINT PAST PACKET LABELS. NO SUCH LEMMA HAS YET BEEN PROVED, SO THIS IS THE NEW PRECISE HARD GAP. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Future coherent packet generations

M5-641 gives a sequence of coherent strongly-negative packet generations with fixed extraction-scale bounds

\[
|\Phi_j(\theta_j)|\ge\phi_*>0.
\]

The coherent extraction also gives a fixed positive Eulerian volume scale

\[
v_j(\theta_j)\gtrsim v_*>0
\]

for a thickened packet at its extraction time.

M5-642 ensures that all future packet labels originate inside one fixed ball at any earlier reference time `theta_0`.

---

## 2. Pullback material volume

Material volume obeys

\[
D_B\log dV=\frac32.
\]

Therefore

\[
\boxed{
v_j(\theta_0)
=v_j(\theta_j)
 e^{-\frac32(\theta_j-\theta_0)}.
}
\]

If packet generations occur at times with linear lower growth, for example after selecting a separated subfamily

\[
\theta_j-\theta_0\ge j\tau
\]

for some `tau>0`, then

\[
\sum_j v_j(\theta_0)
\lesssim
v^*\sum_j e^{-\frac32j\tau}<\infty.
\]

Thus a finite initial material volume can in principle contain preimages of infinitely many later fixed-size packet generations.

---

## 3. Volume-resource contradiction is invalid

Consequently the argument

\[
\text{finite initial reservoir volume}
+
\text{infinitely many packet replacements}
\Longrightarrow\bot
\]

is invalid.

The similarity material expansion discounts later generations strongly enough to make their initial volume costs summable.

This mirrors the earlier M5-598 observation that some physical dissipation costs become geometrically summable across generations.

---

## 4. Vorticity flux behaves differently

For each negative-kappa material packet,

\[
\frac d{d\theta}\log|\Phi|
=\bar\kappa_\Phi<0
\]

on the zero-level relabeling side.

Hence forward flux is nonincreasing.

Therefore if a future coherent packet has

\[
|\Phi_j(\theta_j)|\ge\phi_*,
\]

then at every earlier time for which that material flux surface is defined,

\[
\boxed{
|\Phi_j(\theta_0)|
\ge
|\Phi_j(\theta_j)|
\ge\phi_*.
}
\]

There is **no factor**

\[
e^{-3(\theta_j-\theta_0)/2}
\]

in the flux resource.

This is because vorticity flux is Navier--Stokes scale invariant.

---

## 5. Why this still does not close the argument

To convert the non-discounted flux lower bound into a finite-resource contradiction, one would need to show that the infinitely many distinct future packet labels pull back to past flux objects whose absolute fluxes are additively countable against one finite quantity.

A schematic desired estimate would be

\[
\boxed{
\sum_j |\Phi_j(\theta_0)|
\le \mathcal F_{tot}(\theta_0)<\infty.
}
\]

Then the lower bound `|Phi_j|>=phi_*` would immediately exclude infinitely many generations.

However no such estimate is currently available.

---

## 6. Missing geometric ingredient: a global flux transversal

Vorticity flux is naturally measured through two-dimensional surfaces transverse to vortex lines.

Different packet generations may pull back to:

- different transverse surfaces;
- nested or topologically linked vortex tubes;
- surfaces with no common global cross-section;
- signed fluxes with cancellation;
- spatially overlapping projections even when their material labels are distinct.

`W in L2` bounds enstrophy, not the global total variation of the vorticity two-form.

In the present critical tail class, a naive `L1` vorticity/absolute-flux bound is not available.

Therefore the required additive resource inequality cannot be assumed.

---

## 7. Exact new hard gap

The replacement conveyor has now been reduced to the following resource problem:

\[
\boxed{
\begin{array}{c}
\text{infinitely many distinct material packet labels}\
\text{each carry past flux at least }\phi_*>0,\\
\text{all originate inside one finite similarity reservoir},\\
\text{but no common finite absolute-flux transversal has been proved.}
\end{array}
}
\]

Thus the next high-value target is either:

1. construct a bounded transversal/current norm that counts these packet fluxes additively; or
2. prove that absence of such a transversal forces a topological/linked recurrent vortex architecture that can be analyzed separately.

---

## 8. Relation to DSD strategy

This step is important because it prevents returning to a false finite-volume counting argument.

The correct critical resource is not three-dimensional material volume but the scale-invariant vorticity-flux content carried by distinct material lineages.

Accordingly, future finite-memory audits should count **flux labels/current**, not packet volume.

---

## 9. Firewall

No claim is made that the future packet preimages are pairwise disjoint in a simple Euclidean cross-section.

No global `L1` vorticity bound is imported.

No absolute-flux additivity is assumed without proof.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]