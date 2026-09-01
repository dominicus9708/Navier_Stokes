# DSD M5-547 — Anchored transverse strain-diffusion cancellation exactly recycles projected palinstrophy dissipation

Date: 2026-09-01

Status: **CROSS-CHANNEL SIGN AUDIT / ON THE M5-516 ANCHORED BRANCH, THE TRANSVERSE STRAIN VECTOR `A=P_perp Sigma W` AND PROJECTED LAPLACIAN `B=P_perp Delta W` SATISFY `B=-A` / IN THE PALINSTROPHY IDENTITY OBTAINED BY PAIRING THE VORTICITY EQUATION WITH `-Delta W`, THE STRETCHING-DIFFUSION CROSS TERM IS `-Sigma W dot Delta W`; ITS TRANSVERSE PART THEREFORE CONTRIBUTES `+|A|^2`, WHILE THE PALINSTROPHY DISSIPATION `|Delta W|^2` CONTAINS THE IDENTICAL `|B|^2=|A|^2` / THESE TWO TERMS CANCEL EXACTLY / THUS THE ANCHORED PROJECTED-DIFFUSION CHARGE IS NOT AN UNPAID EXCESS; IT IS RECYCLED INTO DERIVATIVE PRODUCTION BY THE EXACT STRAIN-DIFFUSION BALANCE / THE REMAINING ANCHORED OBSTRUCTION IS PURELY PARALLEL/ADVECTIONAL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact anchored relation

On one anchored persistent lineage, write

\[
W=\rho\xi,
\qquad
|\xi|=1.
\]

M5-516 gives

\[
D_B\xi=0
\]

and hence

\[
\boxed{
(I-\xi\otimes\xi)(\Sigma W+\Delta W)=0.
}
\]

Define the transverse vectors

\[
\boxed{
A
:=(I-\xi\otimes\xi)\Sigma W
=\rho\tau,
}
\]

and

\[
\boxed{
B
:=(I-\xi\otimes\xi)\Delta W
=\rho\mathcal D_\xi.
}
\]

Then the anchored relation is exactly

\[
\boxed{B=-A.}
\]

---

## 2. Parallel/transverse decomposition

Set

\[
a:=\xi\cdot\Sigma W=\rho\sigma,
\]

and

\[
b:=\xi\cdot\Delta W.
\]

Then

\[
\Sigma W=a\xi+A,
\]

and

\[
\Delta W=b\xi+B.
\]

Orthogonality gives

\[
A\perp\xi,
\qquad
B\perp\xi.
\]

Thus

\[
\Sigma W\cdot\Delta W
=ab+A\cdot B.
\]

On the anchored branch,

\[
A\cdot B=-|A|^2.
\]

Therefore

\[
\boxed{
-\Sigma W\cdot\Delta W
=
-ab+|A|^2.
}
\]

This is the key sign identity.

---

## 3. Palinstrophy equation in `-Delta W` form

The similarity vorticity equation is

\[
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
=
\Sigma W+\Delta W.
\]

Pair it with

\[
-\Delta W
\]

and integrate over the localized active core, with the M5-544 cutoff errors suppressed as `o_R(1)`.

The time and linear similarity terms give

\[
\frac12P_R'
+
\frac34P_R.
\]

The Laplacian gives the positive palinstrophy dissipation

\[
H_R
:=
\int\chi_R|\Delta W|^2dy.
\]

Hence

\[
\boxed{
\frac12P_R'
+
\frac34P_R
+
H_R
=
-\int\chi_R\Sigma W\cdot\Delta Wdy
-
\int\chi_R(U\cdot\nabla W)\cdot(-\Delta W)dy
+o_R(1).
}
\]

The second term is the transport derivative-production contribution.

---

## 4. Dissipation decomposition

Because

\[
\Delta W=b\xi+B,
\]

we have

\[
\boxed{
|\Delta W|^2
=b^2+|B|^2.
}
\]

On the anchored branch `B=-A`, so

\[
\boxed{
|\Delta W|^2
=b^2+|A|^2.
}
\]

Thus the projected-diffusion charge identified in M5-500 is exactly the transverse part

\[
\boxed{|A|^2=|B|^2.}
\]

of the full second-derivative dissipation.

---

## 5. Exact transverse recycling

The stretching-diffusion cross term contributes

\[
-\Sigma W\cdot\Delta W
=-ab+|A|^2.
\]

The left side dissipation contributes

\[
b^2+|A|^2.
\]

Therefore the transverse terms are identical on the two sides:

\[
\boxed{
+|A|^2
\quad\text{production}
\leftrightarrow
+|A|^2
\quad\text{dissipation}.
}
\]

They cancel exactly when the anchored identity is inserted into the palinstrophy budget.

This is not an inequality and does not lose constants.

---

## 6. Reduced anchored palinstrophy ledger

After canceling the transverse pair, the anchored contribution reduces schematically to

\[
\boxed{
\frac12P_R'
+
\frac34P_R
+
\int\chi_R b^2dy
=
-\int\chi_R ab\,dy
+
\mathcal T_{adv,R}
+
o_R(1),
}
\]

where

\[
\mathcal T_{adv,R}
:=-
\int\chi_R(U\cdot\nabla W)\cdot(-\Delta W)dy
\]

with the understood full localized decomposition and cutoff commutators.

Thus the projected transverse channel has disappeared from the **net** derivative ledger.

The genuinely unpaid terms are now

1. parallel diffusion `b^2`;
2. parallel strain-diffusion cross work `-ab`;
3. advective derivative transfer.

---

## 7. Why M5-501 did not see this cancellation

M5-501 bounded the full derivative nonlinearity by

\[
|\mathcal N_P|
\le
CE^{1/4}P^{3/4}H^{1/2}.
\]

That estimate treats all directional channels together and therefore cannot expose exact cancellation between one transverse part of `H` and one transverse part of nonlinear production.

M5-547 uses the much stronger anchored vector identity

\[
P_\perp(\Sigma W+\Delta W)=0
\]

before estimating.

Thus there is no contradiction between the two results.

The new decomposition is a branch-specific sharpening of the earlier coarse bound.

---

## 8. Consequence for the M5-546 excess strategy

M5-546 proposed searching for an excess showing that projected-diffusion ratchet cost cannot be fully paid by derivative production.

On the anchored branch, that particular hope fails in the strongest possible way:

\[
\boxed{
\text{transverse projected dissipation}
=
\text{transverse derivative production}
}
\]

pointwise in the channel decomposition.

Therefore the projected transverse charge itself cannot supply the missing positive excess.

This candidate must be retired for the anchored branch.

---

## 9. Physical interpretation within the audit

The anchored direction does not remain fixed because diffusion is absent.

Instead, transverse strain attempts to rotate the vorticity direction while projected viscosity produces exactly the opposite directional change.

The same equality that prevents directional motion also returns the associated projected Laplacian cost into the derivative-production side of the palinstrophy ledger.

Thus the anchored state is a genuine dynamically balanced mechanism, not a static or free configuration.

---

## 10. Two-lineage anchored pair

For the anchored noncollinear pair `(a,b)`, the calculation applies separately to each lineage:

\[
B_a=-A_a,
\qquad
B_b=-A_b.
\]

Hence both projected-diffusion charges are individually recycled.

Noncollinearity alone does not prevent this because the two lineages generally sample different strain tensors and different Laplacians.

The M5-491 same-tensor firewall remains essential.

---

## 11. New narrow frontier

The anchored branch is no longer a generic two-channel balance.

After exact transverse cancellation, its unresolved derivative ledger is concentrated in

\[
\boxed{
\text{parallel strain/diffusion}
+
\text{advective derivative transfer}.
}
\]

Equivalently, the next variables are

\[
a=\rho\sigma,
\qquad
b=\xi\cdot\Delta W,
\]

and the transport term involving

\[
U\cdot\nabla W.
\]

This is substantially narrower than the M5-500 axial/projected-diffusion split.

---

## 12. Highest-value next target

Use the anchored amplitude equation to rewrite the parallel combination.

Since

\[
D_BW+W=\Sigma W+\Delta W
\]

and the anchored direction is fixed along the lineage, the parallel scalar equation is

\[
\boxed{
D_B\rho+\rho=a+b.
}
\]

Equivalently,

\[
\boxed{
b=D_B\rho+\rho-a.}
\]

Substitute this exact scalar identity into

\[
b^2+ab
\]

or the corresponding reduced palinstrophy ledger.

The next audit should determine whether the remaining parallel diffusion/cross term is also an exact amplitude coboundary, or whether it leaves a genuine positive excess after recurrent averaging.

If it is also fully recyclable, the only remaining channel will be advective derivative transfer.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]