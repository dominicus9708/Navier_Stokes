# M19-040 — Natural-time thickening solves dwell per contact but not nonreused historical return count

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC MULTIPLICITY RECOMPRESSION / M18-055 COMPATIBILITY / DISTINCT-RETURN FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-039 proves, conditionally on the quiet bounded weak-\(L^3\), shell-comparable, controlled-center branch, that one genuine material contact with an ancestor shell persists for its full ancestor natural time:

\[
\tau_{res}\gtrsim cR^2.
\]

This removes the old child-time loss

\[
r^2=K^{-2}R^2.
\]

M18-055, however, proves that a fixed annular record cell has only order-one capacity for independent fixed-thickness recurrent events.

The present module reconciles the two results and identifies the exact residual theorem.

## 2. Two different questions

M19-039 answers:

\[
\boxed{
\text{Given one genuine same-population contact, how long must it persist?}
}
\]

On the retained quiet branch,

\[
\boxed{
\tau_{contact}\gtrsim R^2.
}
\]

M18-055 answers a different question:

\[
\boxed{
\text{How many independent nonreused contacts can one fixed record annulus contain?}
}
\]

A fixed second-generation parent annulus has similarity-time width

\[
\Delta\theta=\log(b/a)=O(1).
\]

Once each contact has fixed/natural thickness, only order-one pairwise independent contacts fit in that cell.

Thus

\[
\boxed{
\text{longer dwell per contact}
\not\Rightarrow
\text{more independent contacts}.
}
\]

## 3. Return density after M19-039

Let \(\rho_k\) denote the physical ancestor shell radius relevant to age \(k\).

For distinct selected return intervals \(I_{k,\ell}\) satisfying

\[
|I_{k,\ell}|\ge c\rho_k^2,
\]

define

\[
N_k^{dist}
:=
\#\{\text{pairwise nonreused selected return episodes at age }k\}.
\]

Then the weighted physical return density satisfies

\[
\boxed{
\mathfrak R_k
\gtrsim
N_k^{dist}\rho_k.
}
\]

The cubic-tail sufficient condition

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

therefore becomes

\[
\boxed{
N_k^{dist}\rho_k
\gtrsim
J_k^{1/2}.
}
\]

This is exactly the old physical return-count threshold, but M19-039 now derives the natural-time duration of each retained episode rather than assuming it.

## 4. Why similarity-time positive density does not prove the count

A fixed record annulus samples only an \(O(1)\) interval in similarity time.

Positive ergodic density therefore supplies at most

\[
N_k^{dist}=O(1)
\]

certified independent event blocks in a single fixed annular record cell.

It may show the same material episode for a large fraction of the cell, but that is one episode, not many.

Therefore

\[
\boxed{
\text{positive similarity-time density}
+\text{M19-039 natural-time thickening}
\not\Rightarrow
N_k^{dist}\to\infty.
}
\]

M18-055 remains fully compatible with M19-039.

## 5. Rerecording firewall

Suppose the same material contact is visible at many nearby observation times or under several overlapping normalized windows.

This does not create additional \(N_k^{dist}\).

One physical contact interval is counted once unless one certifies either

1. disjoint physical-time support;
2. a completed exit and later re-entry of the same material population;
3. a distinct fixed-flux material population;
4. another nonreuse certificate.

Hence

\[
\boxed{
\text{many samples of one long contact}
\neq
\text{many ancestry returns}.
}
\]

## 6. Re-entry requires radial variation

For one persistent material population, let \(M_{i,R}^\chi(t)\) be the shell-localized enstrophy mark of M19-038.

A distinct return after a completed exit requires the mark to execute an excursion such as

\[
m_*\to \le \frac14m_*\to m_*.
\]

Therefore each completed exit/re-entry cycle forces order-one total variation of the localized mark:

\[
\operatorname{TV}(M_{i,R}^\chi;I_{cycle})
\gtrsim m_*.
\]

By the exact M19-038 balance, this variation must be supplied by

\[
C_{rad},\quad S,\quad D_{bulk},\quad C_{diff,R},\quad E_{pop}.
\]

On the fully quiet branch, only the radial current remains genuinely new.

Thus

\[
\boxed{
N_k^{dist}\text{ same-population returns}
\Longrightarrow
\int |C_{rad}|dt
\gtrsim
N_k^{dist}m_*
}
\]

modulo already typed source/diffusion/exchange payments.

This is a lower bound on required radial total variation, not a finite upper budget.

## 7. Weak-L3 controls speed, not total variation

M19-039 gives

\[
|C_{rad}|
\lesssim
\frac{M}{R^2}M_{i,R}^\chi
\]

on the shell-comparable bounded weak-\(L^3\) corridor.

This is an instantaneous speed/rate upper bound.

It implies a minimum time between completed exits and returns, but it does not give a finite total-variation budget over the entire historical interval.

A bounded-speed trajectory can oscillate arbitrarily many times given enough total time.

Therefore

\[
\boxed{
\text{weak-L3 radial speed control}
\not\Rightarrow
\text{finite number of historical returns}.
}
\]

Conversely it also does not force sufficiently many returns.

## 8. Enlarging the historical window is not free

One could search a longer and longer parent-time interval for more re-entries.

But M18-055 proves that enlarging the logarithmic record width increases cross-generation parent overlap by the same order and destroys the fixed bounded-overlap ledger.

Hence a count obtained only by expanding the observation window cannot be inserted into the finite parent budget for free.

## 9. Exact surviving R-AC theorem

All previously identified quiet-side reductions now leave one precise theorem-level target:

\[
\boxed{
\mathcal T_{count}^{dist}:
N_k^{dist}\rho_k
\gtrsim
J_k^{1/2}
\quad
\text{on a subset carrying }
\sum J_k^{3/2}=\infty.
}
\]

Here \(N_k^{dist}\) counts genuinely distinct physical historical return episodes, not normalized rerecordings.

Every known alternative failure has already been typed as one of:

- Hodge shell-boundary/harmonic defect;
- shell-amplitude concentration/noncomparability;
- center drift/turnover/export;
- material replacement/fresh population;
- stretching/palinstrophy or higher derivative payment;
- diffusive shell/population exchange;
- weak-\(L^3\) escalation / critical tail.

Thus the broad R-AC correlation problem has been reduced to a distinct historical return-count theorem.

## 10. What would close R-AC

Any one of the following would suffice on the cubic-divergent set:

1. direct proof of \(N_k^{dist}\rho_k\gtrsim J_k^{1/2}\);
2. a signed quantity whose variation across each distinct return telescopes against a finite parent budget without the \(\rho_k\) factor;
3. a rigidity theorem showing that persistent return deficiency forces one of the already typed exits;
4. a parent-time nonreuse theorem that extracts sufficiently many disjoint return cycles from the recurrent hull.

No such theorem is presently certified.

## 11. Audit conclusion

M19-039 removes the \(K^{-2}\) **duration defect per actual contact**.

M18-055 continues to block a false upgrade from recurrence density to scale-growing **independent multiplicity**.

Therefore the remaining ancestry-conversion obstruction is now narrower than before:

\[
\boxed{
R\text{-AC}
\longrightarrow
\mathcal T_{count}^{dist}
}
\]

modulo already typed exits.

---

\[
\boxed{\text{M19-040 COMPLETE; R-AC IS NOW A DISTINCT HISTORICAL RETURN-COUNT THEOREM.}}
\]