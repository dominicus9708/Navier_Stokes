# DSD M5-161 — First-Order Spectral Transfer Order Gap — AUDIT-CORRECTED

Date: 2026-08-27

Status: **AUDIT-CORRECTED / THE `j^-1` TRANSFER FRACTION PER PARABOLIC SHELL TIME IS VALID, BUT THE ORIGINAL FACTORIAL NON-EXPLOSION CONCLUSION IS NOT VALID BY ITSELF; SECOND-ORDER IN-BAND BACKWARD-DIFFUSIVE AMPLIFICATION CAN RESTORE THE `j^-1` LOSS IN TIME `O((log j)/j^2)`, AND THESE AMPLIFICATION TIMES ARE SUMMABLE / M5-162 AND M5-163 REMAIN VALID PACKAGING LEMMAS, BUT THEY DO NOT CLOSE `P1_B^S` WITHOUT A NEW CONTROL THAT COUPLES TRANSFER TO IN-BAND AMPLIFICATION / SEE M5-164 / GLOBAL REGULARITY UNPROVED.**

---

## 1. Facts retained as GREEN

The following parts of the original M5-161 analysis remain valid.

1. The principal constant-coefficient normal/viscous operators commute with cross-section spectral projectors.
2. True inter-band transfer comes only from the variable-coefficient relative transport/stretching/Biot--Savart operator.
3. That transfer operator is first order.
4. M5-162 proves a uniform principal shell propagator bound on the natural parabolic interval

\[
\Delta z_j\sim(1+j)^{-2}.
\]

5. M5-163 proves

\[
\|Q_k\mathcal NQ_j\|
\le
C(1+j)e^{-a|k-j|}.
\]

Hence over one natural shell interval the **raw adjacent transfer fraction** is indeed

\[
\boxed{
\varepsilon_j\lesssim\frac{C}{1+j}.
}
\]

This order-gap statement is GREEN.

---

## 2. Original conclusion that is withdrawn

The original note multiplied the raw transfer fractions:

\[
\prod_{j=N}^{M}\frac{C}{1+j}
\]

and concluded that the factorial decay by itself blocks information from entering from spectral infinity.

That conclusion omitted the fact that after a small amount is transferred into shell `j`, the **commuting second-order principal operator can amplify that already-transferred amount inside the same shell** at rate

\[
O(j^2).
\]

Although this amplification does not itself move spectral bands, it changes the size of the amount available for the next transfer step.

Therefore the transfer fractions cannot be multiplied independently of the intervening principal amplification.

The old implication

\[
\boxed{
\text{first-order transfer}
\Rightarrow
\text{factorial non-explosion}
}
\]

is withdrawn.

---

## 3. Amplification-assisted cascade scale

Suppose one adjacent transfer loses a factor `1/j`.

The principal shell dynamics can restore that factor by amplifying through a factor `j`.

Since the in-band growth rate is `O(j^2)`, the required amplification time is only

\[
\boxed{
\Delta z_j^{amp}
\sim
\frac{\log j}{j^2}.
}
\]

But

\[
\boxed{
\sum_{j\ge N}
\frac{\log j}{j^2}
<\infty.
}
\]

Hence an infinite sequence of

\[
\text{small first-order transfer}
\to
\text{second-order in-band amplification}
\to
\text{next transfer}
\]

is **not excluded by the original factorial product argument**.

This is the precise missing channel.

---

## 4. What M5-162 and M5-163 now mean

M5-162 and M5-163 remain GREEN.

They establish, respectively:

\[
\boxed{
\text{in-band principal rate }\sim j^2
}
\]

and

\[
\boxed{
\text{inter-band transfer rate }\sim j.
}
\]

But the pair of facts must be analyzed **together**, not by multiplying transfer fractions while ignoring the time available for in-band amplification.

The remaining question is now:

\[
\boxed{
\text{can the analytic/same-tail constraints prevent an amplification-assisted infinite cascade?}
}
\]

---

## 5. DSD correction

### Formation — GREEN

No object is deleted; only the logical strength of the path estimate is corrected.

### Axis — GREEN

Inter-band transfer and in-band amplification remain distinct channels.

### Static aggregation — CORRECTED

The old factorial product treated transfer losses as if no later shell amplification could restore them.  This was an invalid aggregation of sequential channel effects.

### Dynamics — YELLOW

The amplification-assisted cascade is now an explicit open dynamical branch.

### Cross-audit — GREEN

No later lemma is allowed to cite the old M5-161 factorial conclusion as a closure theorem.

---

## 6. Current meaning of M5-161

The valid output is only the differential-order decomposition:

\[
\boxed{
\text{inter-band transfer is first order, while in-band principal dynamics is second order.}
}
\]

Whether that order gap helps or hurts uniqueness depends on their **combined cascade timing**.

The next node M5-164 audits this combined timing and identifies the regularity threshold needed to block the cascade.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
