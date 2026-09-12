# DSD M19-094 — Quarter-gap derivative activity remains ancestry-summable and cannot close extra center by unsigned P/H ledgers

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT REINSERTION OF PALINSTROPHY AND RAW-H2 ANCESTRY WEIGHTS / MIXED P-H COMPENSATION HAS A GEOMETRICALLY SUMMABLE MINIMAL PARENT COST / UNSIGNED DERIVATIVE LEDGERS DO NOT CLOSE THE EXTRA CENTER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M19-093

An extra zero-center direction requires persistent background derivative activity of the form

\[
C_1\nu^{-1}Z^{1/2}P^{1/2}
+C_2P^{1/4}H^{1/4}
\gtrsim 1,
\]

where

\[
P=\|\nabla\Omega\|_2^2,
\qquad
H=\|D^2\Omega\|_2^2.
\]

A strong-compensation event therefore forces either a palinstrophy floor or a mixed condition

\[
PH\gtrsim c>0.
\]

The question is whether repeated such events contradict the fixed-parent derivative ledgers.

---

## 2. Parent ancestry weights

For a descendant record whose physical scale is `r`, equivalently dilation factor

\[
R=r^{-1},
\]

M17/M18 established the spacetime ancestry weights

\[
\boxed{
q_P^{parent}=R^{-1}q_P^{record}=r\,q_P^{record},
}
\]

and

\[
\boxed{
q_H^{parent}=R^{-3}q_H^{record}=r^3q_H^{record}.
}
\]

Thus a normalized `O(1)` palinstrophy payment costs only `O(r)` in the old physical parent, while a normalized raw-H2 payment costs `O(r^3)`.

---

## 3. Fixed normalized activity is geometrically summable

Along a similarity-time sequence

\[
\theta_k\to+\infty,
\]

the corresponding physical scale is

\[
\boxed{
r_k\asymp e^{-\theta_k/2}.}
\]

If the recurrence gaps are bounded below in similarity time, then `r_k` decreases geometrically.

Hence even a fixed normalized palinstrophy charge `p_*>0` at every recurrent event gives

\[
\sum_k r_k p_*<\infty.
\]

Likewise

\[
\sum_k r_k^3 h_*<\infty.
\]

Therefore positive-density normalized derivative activity is not by itself a finite-parent contradiction.

---

## 4. Optimize the mixed P-H parent cost

The more interesting branch is

\[
PH\ge c>0.
\]

Let `p,h>0` denote the normalized charges attached to one event. Its parent derivative cost is

\[
\mathcal C_r(p,h)
:=rp+r^3h.
\]

Under the sharp constraint

\[
ph=c,
\]

write

\[
h=\frac c p.
\]

Then

\[
\mathcal C_r(p)
=rp+r^3\frac c p.
\]

Differentiate:

\[
\mathcal C_r'(p)
=r-r^3\frac c{p^2}.
\]

The minimizer is

\[
\boxed{
p_*=r\sqrt c,}
\]

with

\[
\boxed{
h_*=\frac{\sqrt c}{r}.}
\]

The minimal parent cost is

\[
\boxed{
\min_{ph=c}\bigl(rp+r^3h\bigr)
=2r^2\sqrt c.
}
\]

---

## 5. Consequence

On geometric scales,

\[
\sum_k r_k^2<\infty.
\]

Therefore even the optimally cheapest realization of a fixed mixed `P-H` compensation condition is completely compatible with finite fixed-parent derivative resources:

\[
\boxed{
\sum_k
\min_{p_kh_k=c}
\left(r_kp_k+r_k^3h_k\right)
<\infty.
}
\]

Thus the M19-093 compensation floor does not revive an ancestry-divergence contradiction.

---

## 6. Interpretation

The quarter-gap program has produced a genuine interior spectral requirement:

\[
\text{extra center}
\Longrightarrow
\text{persistent derivative compensation}.
\]

But the physical scaling of that compensation is still subcritical with respect to summation over generations.

Hence

\[
\boxed{
\text{extra center derivative support}
\not\Rightarrow
\text{unsigned parent-ledger divergence}.
}
\]

The center problem cannot be closed by simply reusing the old positive `P/H` ancestry sums.

---

## 7. Relation to M18-059

M18-059 concluded that the certified unsigned additive payer family does not contain a resource that is simultaneously

1. finite in the old physical parent; and
2. forced to pay a non-summable fixed amount at every first-hitting generation.

M19-094 shows that the new center-compensation descent obeys the same structural limitation.

The finite-dimensional center reduction changes the spectral geometry, but it does not change the scaling arithmetic of the old unsigned derivative ledgers.

---

## 8. New implication for strategy

The next successful center argument must use information not captured by positive `P/H` magnitude alone.

Candidates include:

- sign or orientation of the compact compensation operator;
- symmetry-transverse spectral ordering;
- a finite-dimensional index/Morse-type count;
- a genuinely signed cocycle;
- or a rigidity property of the recurrent compact-core dynamics.

Repeating unsigned ancestry conversion is no longer a productive direction.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
