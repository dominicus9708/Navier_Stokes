# M19-005 — First-hitting clock is an exact discounted parent coboundary and cannot remove the ancestry weight

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC SIGNED-ROUTE TEST / EXACT DISCOUNTED COBBOUNDARY / CLOCK SHORTCUT CLOSED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-053--059 shows that the unsigned ancestry route has a budget-scaling mismatch. The next M19 target is therefore a signed fixed-parent conversion.

The most natural bounded signed candidate on the first-hitting Type-I corridor is the remaining-time clock

\[
\Theta_j:=W_j(T^*-t_j),
\]

where the first-hitting amplitudes satisfy

\[
W_{j+1}=qW_j,
\qquad q>1.
\]

Define the normalized stage duration

\[
L_j:=W_j(t_{j+1}-t_j).
\]

This module computes the exact relation between \(L_j\) and the parent clock \(\Theta_j\).

The result is a strict firewall:

\[
\boxed{
\text{the first-hitting clock is already an exact geometrically discounted coboundary.}
}
\]

Thus it cannot convert order-one stage payments into a nonsummable fixed-parent signed drift.

## 2. Exact clock recursion

By definition,

\[
\Theta_{j+1}
=W_{j+1}(T^*-t_{j+1}).
\]

Using

\[
W_{j+1}=qW_j
\]

and

\[
T^*-t_{j+1}
=(T^*-t_j)-(t_{j+1}-t_j),
\]

we obtain

\[
\begin{aligned}
\Theta_{j+1}
&=qW_j\big[(T^*-t_j)-(t_{j+1}-t_j)\big]\\
&=q(\Theta_j-L_j).
\end{aligned}
\]

Hence

\[
\boxed{
L_j
=\Theta_j-q^{-1}\Theta_{j+1}.
}
\]

This is exact and uses only the first-hitting amplitude ratio.

## 3. Parent-discounted telescoping identity

Multiply by \(q^{-j}\):

\[
q^{-j}L_j
=q^{-j}\Theta_j-q^{-(j+1)}\Theta_{j+1}.
\]

Summing from \(j=0\) to \(N\),

\[
\boxed{
\sum_{j=0}^{N}q^{-j}L_j
=\Theta_0-q^{-(N+1)}\Theta_{N+1}.
}
\]

On a Type-I corridor where

\[
0<\Theta_-\le\Theta_j\le\Theta_+<\infty,
\]

we obtain

\[
q^{-(N+1)}\Theta_{N+1}\to0,
\]

and therefore

\[
\boxed{
\sum_{j=0}^{\infty}q^{-j}L_j
=\Theta_0<\infty.
}
\]

Thus the order-one normalized stage duration is exactly compatible with a finite parent total because the parent embedding contributes the geometric factor \(q^{-j}\).

## 4. Physical-time interpretation

Since

\[
W_j=q^jW_0,
\]

we have

\[
q^{-j}L_j
=q^{-j}W_j(t_{j+1}-t_j)
=W_0(t_{j+1}-t_j).
\]

Therefore

\[
\sum_{j=0}^{N}q^{-j}L_j
=W_0(t_{N+1}-t_0).
\]

Taking \(N\to\infty\) and \(t_j\uparrow T^*\),

\[
\boxed{
\sum_{j\ge0}q^{-j}L_j
=W_0(T^*-t_0)
=\Theta_0.
}
\]

The discounted coboundary identity is therefore nothing more and nothing less than the exact conversion back to the original parent physical time.

It is representation-safe.

## 5. Why the undiscounted sum is not a parent charge

The lower stage-duration bound from M18 gives

\[
L_j\ge L_->0.
\]

Hence

\[
\sum_jL_j=\infty.
\]

But this divergence lives in the sequence of stage-normalized clocks.

It is not an additive physical-parent time budget.

The correct parent conversion is

\[
L_j\mapsto q^{-j}L_j,
\]

and

\[
\sum_jq^{-j}L_j<\infty.
\]

Thus

\[
\boxed{
\text{divergent normalized stage time}
\neq
\text{divergent parent physical time}.
}
\]

This is the signed-clock analogue of the M18-058--059 unsigned scaling firewall.

## 6. Bounded signed potential does not create a one-way drift

The recursion may also be written

\[
qL_j=q\Theta_j-\Theta_{j+1}.
\]

Thus a positive stage duration is paid by a **discounted** decrease of a bounded clock state, not by an ordinary difference

\[
\Theta_j-\Theta_{j+1}.
\]

The factor \(q\) is essential.

If one incorrectly drops it, one would obtain a false monotone exhaustion argument.

The correct dynamics has a built-in multiplicative recharge induced by the change of normalization between adjacent first-hitting stages.

## 7. General lesson for signed R-AC candidates

A signed observable sampled in stage-normalized variables must be returned to one fixed parent before telescoping is used.

If the observable has a nonzero scaling homogeneity, the parent conversion generally inserts a geometric weight.

Therefore the desired signed R-AC mechanism cannot be merely

\[
\boxed{
\text{bounded normalized state}
+\text{ positive stage increment}.
}
\]

It must additionally have one of the following:

1. exact scale-criticality under parent embedding;
2. a parent-fixed bounded state whose increments are the actual event increments without geometric discount;
3. a finite total-variation/defect budget that prices the compensating reverse increments;
4. a genuinely monotone parent observable.

The first-hitting remaining-time clock satisfies none of these in the needed form.

## 8. Interaction with M18-054 return deficiency

M18-054 proves on a surviving R-AC branch that the divergent cubic shell mass concentrates on shells with vanishing return ratio

\[
a_k=\frac{\mathfrak R_k}{J_k^{1/2}}
\]

in cubic-mass density.

The present clock identity does not repair that deficiency.

A current-epoch order-one stage duration remains parent-discounted by the exact age/scale factor. Hence clock recurrence alone cannot force

\[
\mathfrak R_k\gtrsim J_k^{1/2}.
\]

The missing return-weight mechanism must come from a scale-critical parent observable or an additional material/genealogical theorem, not from the first-hitting clock itself.

## 9. M19-005 verdict

### Closed shortcut

\[
\boxed{
\text{use bounded Type-I remaining-time clock as the missing signed R-AC contradiction}
}
\]

is closed.

### Exact retained identity

\[
\boxed{
L_j=\Theta_j-q^{-1}\Theta_{j+1},
\qquad
\sum_jq^{-j}L_j=\Theta_0.
}
\]

### Next target

The next signed candidate should therefore be genuinely scale critical.

The natural candidate is persistent material vorticity flux, which is scale invariant under Navier--Stokes parabolic scaling.

M19-006 should compute its fixed-parent telescoping law and determine exactly what recurrent fixed-size flux variation would require: one-sign exhaustion, sign-reversing total variation, replacement/export, or a finite diffusive defect budget.

---

\[
\boxed{\text{M19-005 COMPLETE; R-AC REMAINS OPEN.}}
\]
