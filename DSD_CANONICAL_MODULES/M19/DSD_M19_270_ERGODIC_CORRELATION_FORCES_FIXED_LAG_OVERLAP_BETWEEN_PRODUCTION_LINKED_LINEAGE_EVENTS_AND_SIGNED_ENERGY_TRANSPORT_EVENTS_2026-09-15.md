# DSD M19-270 — Ergodic correlation forces fixed-lag overlap between production-linked lineage events and signed energy-transport events

Date: 2026-09-15  
Canonical ID: **M19-270**  
Status: **ACTIVE OVERLAP REDUCTION / SAME-COMPONENT POSITIVE-MEASURE EVENTS UPGRADED TO FIXED FINITE-LAG OVERLAP / SAME-TIME COUPLING STILL OPEN / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Production-linked event set is already constructed

M5-589 thickens the M5-587 finite-depth production sphere into a fixed annular spacetime event with positive invariant frequency.

M5-590 then applies finite-payer saturation and extracts one fixed persistent material-flux lineage that pays a fixed positive share of that annular production on a positive-measure recurrent event set.

M5-591 adds a same-time noncollinear companion geometry, and M5-592 packages the result into a positive-measure event set

\[
\boxed{\mathcal E_{pd}}
\]

on which the following are co-located:

1. finite-depth annular vortex-stretching production;
2. a fixed persistent production-paying lineage;
3. a fixed noncollinear companion geometry;
4. either positive projective action or exact strain-diffusion anchoring.

Thus

\[
\boxed{\mu(\mathcal E_{pd})>0.}
\]

The historical enstrophy/material-lineage overlap problem is therefore already solved on the retained quiet compact branch.

---

## 2. Signed energy-transport observable from M19-269

On the M19-267 residual-payer branch, M19-269 constructs a finite wedge depth \(z_E>0\) at which

\[
\mathscr E'(z_E)=0,
\]

\[
\mathscr D(z_E)>rac{c_3}{M_A},
\]

and

\[
\boxed{
\mathscr G'(z_E)
>
\gamma_*
:=
\frac{c_3}{2M_A\sqrt{z_E}}
>0,
}
\]

where

\[
\mathscr G(z)=\sqrt z\,\mathscr J(z).
\]

For a hull state \(Y\), define the instantaneous finite-depth observable

\[
\boxed{
\Gamma_E(Y)
:=
\left.
\frac{d}{dz}
\left(
\sqrt z
\int_{S^2}\mathcal J_{r,Y}(z,\omega)\,d\omega
\right)
\right|_{z=z_E}.
}
\]

Uniform smooth compactness on fixed wedge depth makes \(\Gamma_E\) a bounded continuous observable on the retained compact hull.

Its invariant mean is

\[
\boxed{
\langle\Gamma_E\rangle_\mu
=
\mathscr G'(z_E)
>\gamma_*>0.
}
\]

---

## 3. Positive-measure signed-energy event set

Let

\[
M_E:=\sup_{Y\in\mathfrak H}|\Gamma_E(Y)|<\infty.
\]

Define

\[
\boxed{
\mathcal E_E
:=
\{Y:\Gamma_E(Y)\ge\gamma_*/2\}.
}
\]

If \(\mu(\mathcal E_E)=0\), then \(\Gamma_E<\gamma_*/2\) almost everywhere and its invariant mean could not exceed \(\gamma_*\).

More quantitatively, using boundedness gives a fixed positive lower measure depending only on \(\gamma_*\) and \(M_E\).

Therefore

\[
\boxed{\mu(\mathcal E_E)>0.}
\]

Thus the residual branch carries a positive-measure set of actual finite-depth signed energy-transport events, not only a positive averaged derivative.

---

## 4. Ergodic fixed-lag overlap lemma

Let \((\mathfrak H,\sigma_t,\mu)\) be the retained ergodic similarity flow.

For measurable positive-measure sets \(A,B\subset\mathfrak H\), the mean ergodic theorem gives

\[
\frac1T
\int_0^T
\mu\bigl(A\cap\sigma_{-t}B\bigr)\,dt
\longrightarrow
\mu(A)\mu(B)>0.
\]

Apply this with

\[
A=\mathcal E_{pd},
\qquad
B=\mathcal E_E.
\]

Therefore there exists at least one finite

\[
\boxed{h_*\ge0}
\]

such that

\[
\boxed{
\mu\bigl(
\mathcal E_{pd}
\cap
\sigma_{-h_*}\mathcal E_E
\bigr)>0.
}
\]

Equivalently, on a positive-measure set of recurrent states:

- a production-linked persistent-lineage/dual event occurs at similarity time \(\theta\);
- the signed finite-depth energy event occurs at the fixed later time \(\theta+h_*\).

The lag \(h_*\) is one fixed finite number, independent of generation and physical scale.

---

## 5. Physical scale comparability of a fixed similarity lag

A finite similarity-time displacement corresponds to a fixed multiplicative scale factor.

Hence the two events occur at physical scales differing only by one constant factor depending on \(h_*\):

\[
\boxed{
\frac{r(\theta+h_*)}{r(\theta)}
\asymp e^{-h_*/2}.
}
\]

Thus the energy and production events cannot evade each other by an unbounded logarithmic scale separation.

The old arbitrary-scale overlap problem is reduced to a **bounded-lag / comparable-scale coupling problem**.

---

## 6. Persistent genealogy survives the finite lag

The M5-590 payer is a persistent material-flux lineage on the retained quiet compact branch.

Therefore its label remains defined across every fixed finite similarity-time interval for which the branch stays inside the retained compact genealogy.

Consequently, on the fixed-lag overlap set, the production-paying lineage at \(\theta\) has a well-defined descendant/continuation at \(\theta+h_*\).

This does **not** yet prove that this same lineage pays the signed energy event there.

But it removes the weaker failure mode

\[
\boxed{
\text{energy event and productive lineage occur only at unrelated generations/scales}.
}
\]

They now live in one bounded-lag recurrent cylinder of the same persistent genealogy.

---

## 7. Why fixed-lag overlap is not same-event overlap

The exact M5-592 same-event identities act at the productive time \(\theta\).

The energy event obtained above is at \(\theta+h_*\).

Ergodicity does not imply

\[
h_*=0.
\]

Nor does it imply that the local energy-flux derivative is carried by the same spatial packet/lineage as the production charge.

Therefore the following shortcut is invalid:

\[
\boxed{
\text{positive-measure production event}
+
\text{positive-measure energy event}
\not\Rightarrow
\text{same-time same-packet PDE incompatibility}.
}
\]

The missing object is a finite-lag transport identity preserving the relevant signed information.

---

## 8. New reduced gate

The former broad overlap target can now be replaced by

\[
\boxed{
\mathcal T_{tail}^{lag-coupling}:
\text{transport the signed energy event across the fixed lag }h_*
\text{ onto the production-linked persistent lineage/event without losing sign.}
}
\]

A sufficient theorem could take one of the following forms:

1. a bounded material/lineage observable whose increment over \([\theta,\theta+h_*]\) equals the signed energy-transport charge plus controlled coboundaries;
2. a finite-lag local-energy identity tied to the same persistent carrier;
3. a compactness theorem forcing the energy-event carrier to be one of the already saturated finite persistent payer labels;
4. an exact incompatibility between the M5-592 projective/anchored alternatives at \(\theta\) and the M19-269 signed energy event at \(\theta+h_*\).

Without such a theorem, fixed-lag correlation alone remains structural information rather than contradiction.

---

## 9. Updated overlap taxonomy

The following parts are **already certified**:

\[
\boxed{
\text{finite-depth enstrophy production}
\Rightarrow
\text{positive-volume annular event}
}
\]

(M5-589),

\[
\boxed{
\text{annular production}
\Rightarrow
\text{fixed persistent production-paying lineage}
}
\]

(M5-590),

\[
\boxed{
\text{productive lineage}
\Rightarrow
\text{same-time noncollinear companion}
}
\]

(M5-591),

and

\[
\boxed{
\text{productive dual event}
\Rightarrow
\text{same-event projective action}
\lor
\text{exact anchoring}
}
\]

(M5-592).

The M19-269 signed energy event additionally satisfies

\[
\boxed{
\text{signed energy event}
\stackrel{\rm ergodicity}{\Longleftrightarrow}
\text{production subsystem at one fixed finite lag }h_*
}
\]

in the positive-measure correlation sense.

The only new overlap gate is therefore the signed finite-lag coupling itself.

---

## 10. Verdict

M19-270 removes two apparent open problems:

1. arbitrary Eulerian-production vs material-lineage overlap;
2. unbounded scale separation between the signed energy witness and the productive genealogy.

Both are already controlled by historical M5 saturation plus ergodic correlation.

The hard core is now narrower:

\[
\boxed{
\mathcal T_{tail}^{lag-coupling}
\lor
\mathcal T_{tail}^{energy-defect}
\lor
\mathcal T_{aper}^{signed}.
}
\]

A new rigidity calculation should therefore act on one **fixed finite-lag recurrent block**, not search for another unrelated local payer.

Global 3D Navier--Stokes regularity remains unproved.
