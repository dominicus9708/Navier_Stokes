# DSD M5-164 — Amplification-Assisted Cascade and the Gaussian Spectral Threshold

Date: 2026-08-27

Status: **P1_B^S COUNTER-AUDIT / M5-162 AND M5-163 DO NOT BY THEMSELVES CLOSE THE STATISTICAL FLAT FIBER: A `1/j` FIRST-ORDER TRANSFER LOSS CAN BE RESTORED BY `j^2` IN-BAND BACKWARD-DIFFUSIVE AMPLIFICATION IN TIME `O((log j)/j^2)`, AND THESE TIMES ARE SUMMABLE / FOR A SPECTRAL ENVELOPE `exp(-a j^p)` THE INFINITE-CASCADE BLOCKING THRESHOLD IS `p>=2`; ORDINARY ANALYTICITY (`p=1`) IS BELOW THRESHOLD, WHILE GAUSSIAN SPECTRAL DECAY `exp(-a j^2)` IS CRITICAL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why the M5-161 product must be re-audited

M5-162 proves that shell `j` has principal second-order rate

\[
O(j^2)
\]

on its natural normal scale.

M5-163 proves that adjacent inter-band transfer has only first-order rate

\[
O(j).
\]

Thus one natural parabolic interval

\[
\Delta z_j\sim j^{-2}
\]

transfers only a fraction

\[
\sim j^{-1}.
\]

The original M5-161 multiplied these losses and obtained factorial suppression.

That multiplication is incomplete because after the transfer, the same shell may use the second-order principal dynamics to amplify the transferred amount before performing the next transfer.

---

## 2. One transfer plus recovery

Suppose shell `j+1` has amplitude `A_{j+1}`.

One adjacent transfer during a natural shell interval produces at most

\[
\frac{C}{j}A_{j+1}
\]

in shell `j`.

If the target shell envelope permits amplitude `A_j`, the principal `j^2` growth can restore the transfer loss.

The time needed for amplification factor `G_j` is

\[
\boxed{
\Delta z_j^{amp}
\sim
\frac{\log G_j}{c j^2}.
}
\]

For ordinary analytic envelopes this time is summable.

---

## 3. Ordinary analytic envelope is insufficient

Uniform cross-section analyticity gives a spectral envelope of the form

\[
\boxed{
A_j\lesssim e^{-a j}.
}
\]

Then

\[
\frac{A_j}{A_{j+1}/j}
\sim
j e^a.
\]

Therefore the amplification factor needed after one transfer is only

\[
G_j\sim j e^a,
\]

and

\[
\boxed{
\Delta z_j^{amp}
\sim
\frac{\log j+a}{c j^2}.
}
\]

But

\[
\boxed{
\sum_{j\ge N}\frac{\log j}{j^2}<\infty.
}
\]

Hence an infinite sequence

\[
\text{transfer}
\to
\text{in-band amplification}
\to
\text{transfer}
\to\cdots
\]

is not ruled out by a finite normal-depth argument under ordinary analyticity.

This is exactly the channel omitted by the old factorial product.

---

## 4. General spectral envelope

Assume more generally

\[
\boxed{
A_j\lesssim e^{-a j^p},
\qquad p>0.
}
\]

The amplitude ratio between adjacent permitted envelopes is

\[
\frac{A_j}{A_{j+1}}
\sim
\exp\left(a[(j+1)^p-j^p]\right).
\]

Including the raw transfer loss `1/j`, the required recovery factor is

\[
G_j
\sim
j\exp\left(a[(j+1)^p-j^p]\right).
\]

For large `j`,

\[
(j+1)^p-j^p
\sim p j^{p-1}.
\]

Hence

\[
\log G_j
\sim
ap j^{p-1}+\log j.
\]

The principal amplification time is therefore

\[
\boxed{
\Delta z_j^{amp}
\sim
C j^{p-3}
+
O\left(\frac{\log j}{j^2}\right).
}
\]

---

## 5. Exact cascade threshold

The infinite cascade is blocked by normal-depth divergence if

\[
\sum_j\Delta z_j^{amp}=\infty.
\]

Since

\[
\sum_j j^{p-3}
\]

diverges exactly when

\[
p-3\ge-1,
\]

the threshold is

\[
\boxed{p\ge2.}
\]

Thus:

### `0<p<2`

The amplification-assisted cascade timing is summable.  The envelope alone does not prevent spectral information from entering from infinity.

### `p=2`

The required amplification time is asymptotically

\[
\Delta z_j^{amp}\sim C/j,
\]

so the total time diverges logarithmically.

### `p>2`

The divergence is stronger.

Therefore the critical spectral regularity for this mechanism is

\[
\boxed{
A_j\lesssim e^{-a j^2}.
}

---

## 6. Terminology correction

The envelope

\[
e^{-a j}
\]

is ordinary analytic spectral decay.

The stronger envelope

\[
e^{-a j^2}
\]

is Gaussian spectral decay, often described as **ultra-analytic** or Gevrey class `1/2` in the convention where Gevrey-`s` Fourier decay is

\[
e^{-c|k|^{1/s}}.
\]

It should **not** be called Gevrey-2.

This distinction is fixed here for all subsequent work.

---

## 7. Relation to the earlier unique-continuation audit

M5-157 found that ordinary superalgebraic or exponential spatial decay is below the standard super-Gaussian hypotheses used in strong exterior parabolic unique-continuation results.

The present calculation independently reaches a related threshold from internal spectral-cascade bookkeeping:

\[
\boxed{
\text{ordinary analyticity is too weak to stop amplification-assisted spectral escape.}
}
\]

This agreement is structural, but the two arguments are not counted as independent costs or independent proofs.

---

## 8. What would close the statistical flat branch through this route

A sufficient new lemma would be any one of the following:

1. a uniform Gaussian cross-section spectral envelope

\[
\|Q_jK\|\le Ce^{-a j^2};
\]

2. a stronger transfer theorem showing that the principal `j^2` amplification cannot be repeatedly synchronized with the first-order transfer channel;

3. a monotonic/log-convex quantity coupling in-band amplification and inter-band transfer so that the two cannot be optimized independently;

4. a backward-uniqueness theorem adapted directly to the stable Fuchsian pair system.

Ordinary analytic-radius control alone is not sufficient.

---

## 9. DSD four-chain audit

### Formation — GREEN

The correction uses the same actual spectral shells and principal rates as M5-162/163.

### Axis — GREEN

In-band amplitude growth and inter-band motion are treated as separate sequential channels.

### Static aggregation — GREEN

The `1/j` transfer loss is no longer multiplied without accounting for later `j^2` amplification.

### Dynamics — GREEN

The summability calculation explicitly includes the time needed to restore the transferred amplitude before the next step.

### Cross-audit — GREEN

M5-162 and M5-163 remain valid.  Only their former use as a complete non-explosion proof is rejected.

---

## 10. Updated frontier

The Branch-S problem is no longer

\[
\text{prove first-order transfer is too slow}.
\]

That statement is insufficient by itself.

The correct next question is

\[
\boxed{
\text{does the same-tail relative equation possess a stronger-than-analytic spectral restriction,}
\text{ or a coupled amplification/transfer monotonicity, that reaches the }p=2\text{ threshold?}
}
\]

This is the next DSD calculation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
