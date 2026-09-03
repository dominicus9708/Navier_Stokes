# DSD M5-657 — Every persistent fixed-flux lineage forces a same-component strongly-negative kappa payer

Date: 2026-09-03

Status: **INTERNAL GENERALIZATION OF M5-656 / THE PRODUCTIVE-ANNULUS INPUT OF M5-656 WAS ONLY USED TO CREATE A FIXED-AMPLITUDE BALL, BUT EVERY M5-488 PERSISTENT COHERENT FIXED-FLUX POPULATION ALREADY HAS A FIXED FLUX FLOOR INSIDE A FIXED BOUNDED NORMALIZED STORAGE REGION, WHICH BY AREA CONTROL AND SMOOTH COMPACTNESS CREATES THE SAME FIXED-AMPLITUDE BALL / THEREFORE AT EVERY RETAINED TIME, EVERY PERSISTENT FIXED-FLUX LINEAGE LIES IN A HIGH-AMPLITUDE CONNECTED SUPERLEVEL COMPONENT THAT ALSO CONTAINS A UNIFORM STRONGLY-NEGATIVE KAPPA PACKET / ANY PERSISTENT RELABELING LINEAGE CAN AVOID THE SAME-LAW FLUX-CONSUMPTION CLOSURE ONLY BY REPEATED HIGH-AMPLITUDE CROSS-SHEET PATCHING / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Persistent coherent fixed-flux input

On the compact no-export finite-memory corridor, M5-488 stores each persistent material population with a fixed scale-critical flux threshold

\[
\boxed{|\Phi_L|\ge\phi_0>0.}
\]

The coherent population is represented inside one fixed bounded normalized storage geometry.

After the finite angular-sector partition, choose a transverse material patch `S_L` whose area is bounded above by a fixed constant

\[
|S_L|\le A_0<\infty
\]

and whose directed vorticity flux satisfies

\[
\left|\int_{S_L}W\cdot n\,dA\right|
\ge\phi_0.
\]

---

## 2. Fixed flux gives a fixed amplitude point

By the area bound,

\[
\sup_{S_L}|W|
\ge
\frac{\phi_0}{A_0}
=:2\rho_0>0
\]

after harmlessly reducing constants for directional coherence.

The all-order compact hull gives a uniform `C^1` bound

\[
\|\nabla W\|_\infty\le M_1.
\]

Therefore there is a fixed radius

\[
\boxed{r_0>0}
\]

such that at every retained time and for every persistent lineage one can find a center `y_L` with

\[
\boxed{
\rho(y)=|W(y)|\ge\rho_0
\quad\text{on }B_{r_0}(y_L).
}
\]

Thus the amplitude-core input of M5-656 is automatic for every persistent fixed-flux lineage.

---

## 3. Fixed superlevel component

Set

\[
\boxed{a_0:=\rho_0/4.}
\]

Let `C_L` be the connected component of

\[
\{\rho>a_0\}
\]

containing the persistent carrier amplitude ball.

Because `rho->0` at infinity, `C_L` is bounded.

On the carrier ball,

\[
\rho-a_0\ge3\rho_0/4.
\]

---

## 4. Reuse the M5-656 weighted component identity

On every connected superlevel component,

\[
\boxed{
\int_{C_L}
\kappa\rho(\rho-a_0)dy
=
-
\int_{C_L}|\nabla\rho|^2dy
-
\int_{C_L}ho(\rho-a_0)|\nabla\xi|^2dy.
}
\]

The Sobolev/capacity argument applied to

\[
f=(\rho-a_0)_+\mathbf1_{C_L}
\]

and the fixed amplitude ball yields a uniform floor

\[
\boxed{
\int_{C_L}|\nabla\rho|^2dy
\ge d_0>0.
}
\]

Hence

\[
\boxed{
\int_{C_L}
\kappa w_Ldy
\le-d_0,
\qquad
w_L:=\rho(\rho-a_0).
}
\]

---

## 5. Uniform strongly-negative population in the same component

As in M5-656,

\[
0<w_L\le\rho^2,
\]

so

\[
\int w_L\le Z_*,
\qquad
\int\kappa^2w_L\le H_*.
\]

Define

\[
\boxed{
\kappa_0:=\frac{d_0}{2Z_*}>0.
}
\]

Then

\[
A_L^-:=\{y\in C_L:\kappa(y)\le-\kappa_0\}
\]

has weighted mass

\[
\boxed{
\int_{A_L^-}w_Ldy
\ge
m_0:=\frac{d_0^2}{4H_*}>0.
}
\]

Smooth thickening inside `rho>a_0` produces a fixed coherent subpacket with

\[
\boxed{
\rho\ge a_0/2,
\qquad
\kappa\le-\kappa_0/2,
\qquad
|\Phi_-|\ge\phi_->0.
}
\]

All constants are uniform over the marked compact hull and over the finite persistent-lineage family.

---

## 6. Persistent-lineage same-component payer theorem

Thus for every persistent lineage `L` and every retained time,

\[
\boxed{
L
\subset C_L
\supset
P_L^-,
}
\]

where `P_L^-` is a fixed-strength strongly-negative coherent `kappa` packet and the entire connecting component satisfies

\[
\rho>a_0.
\]

This is independent of whether `L` is the M5-590 production payer, a dual companion, or another saturated persistent label.

---

## 7. Consequence for a persistent relabeling reference

Suppose the persistent lineage has local relabeling history

\[
\kappa_L=c_L(\theta),
\qquad
\langle c_L\rangle=0
\]

from its bounded nondegenerate material flux.

At every time its connected amplitude component contains a packet with

\[
\kappa\le-\kappa_0/2.
\]

Therefore:

### A. Same-law payer

If the negative packet belongs to the same common scalar-law family as `L`, it can be compared through scalar ODE order preservation.

On the zero-reference subcase this enters M5-648.

On positive reference phases it enters the M5-649 relative-flux mechanism.

### B. Different-law payer

If it does not belong to the same common-law family, then a path inside the connected high-amplitude component from `L` to `P_L^-` must cross a relabeling-sheet patching locus.

Thus

\[
\boxed{
\text{persistent lineage}
\Longrightarrow
C_{same-law\ payer}
\lor
T_{high-amplitude\ cross-sheet}.
}
\]

---

## 8. Positive reference phases force an order-one relative gap

If at some time

\[
c_L(\theta)\ge c_+>0,
\]

then the same-component negative packet satisfies

\[
\boxed{
\kappa_- -c_L
\le
-\left(c_++\frac12\kappa_0\right).
}
\]

Hence on a same-law corridor there is an order-one lower relative level, exactly the setting required for finite relative-flux consumption.

If such positive phases occur with positive frequency, a same-law survivor is impossible by M5-649.

If the zero-mean reference never has positive phases, then it is identically zero almost everywhere and the same-law negative payer enters M5-648.

Thus in either case a **same-law** persistent corridor is closed.

---

## 9. Sharpened relabeling frontier

Combining the preceding observations with M5-655 gives

\[
\boxed{
R_{persistent\ relabeling}
\Longrightarrow
T_{high-amplitude\ cross-sheet\ patching}.
}

The conditional same-law branch no longer needs an external global payer attribution: M5-657 manufactures the required negative payer in the persistent lineage's own connected amplitude component at every time.

The remaining issue is only whether that same-component payer can consistently live on another local relabeling sheet.

---

## 10. Relation to M5-654

Because the entire path between the persistent carrier and its negative payer lies in

\[
\rho>a_0,
\]

the quotient-free force

\[
F=\rho^2\nabla\kappa
\]

has no nodal degeneracy along the path.

Thus every surviving cross-sheet patch must be realized by:

1. generalized-force rotation,
2. critical generalized-force creation,
3. or a differential-silent analytic multi-sheet branch point.

The next step should classify the third option and determine whether it can recur with fixed high-amplitude geometry.

---

## 11. Firewall

Connectedness of `C_L` still does not imply one global scalar law `h=f(kappa,theta)`.

The present theorem closes only the need to search globally for a negative payer: the payer is guaranteed in the same connected high-amplitude component.

The high-amplitude cross-sheet branch remains genuine.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]