# DSD M17-230 — Geometric mass loss makes naive palinstrophy summation along scale ladders summable

Date: 2026-09-06  
Canonical ID: **M17-230**

Status: **FALSE-CLOSURE PRUNING / THE SCALE-RETURN GATE OF M17-229 CANNOT BE OBTAINED MERELY BY SAYING THAT SMALLER CARRIERS HAVE LARGER `1/ell^2` PALINSTROPHY DENSITY. ON THE STRICT MEAN-DOMINATED DESCENT, THE CARRIER MASS MAY DECREASE GEOMETRICALLY AT THE SAME TIME AS THE SCALE SHRINKS. IN THE MODEL EXTREMAL RECURRENCE `M_n=theta^n M_0`, `ell_n=theta^(n/4) ell_0`, THE POINCARE PALINSTROPHY FLOOR `M_n/ell_n^2` IS `theta^(n/2) M_0/ell_0^2` AND IS SUMMABLE IN SCALE DEPTH. THE PARABOLIC ACTION OVER ONE OWN-SCALE LIFETIME IS OF ORDER `M_n`, WHICH IS EVEN MORE DIRECTLY SUMMABLE. THEREFORE STRICT SCALE DESCENT BY ITSELF DOES NOT FORCE A NONSUMMABLE LOWER-ORDER COST. ANY VALID SCALE-RETURN GATE MUST USE AN ADDITIONAL AMPLITUDE-SCALE, NUMERATOR-RETENTION, GENEALOGY, OR COEFFICIENT RELATION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The tempting but invalid argument

M17-228 gives, for a mean-zero fluctuation in a ball of scale `ell`,

\[
\int|\nabla W|^2dy
\gtrsim
\ell^{-2}M,
\]

where `M` is the fluctuation `L2` mass.

Since a strict microcarrier ladder has

\[
\ell_n\to0,
\]

one might try to conclude informally that the palinstrophy floor must diverge and hence the ladder is impossible.

This ignores the simultaneous decay of `M_n`.

---

## 2. Extremal geometric descent model

Take the exact model allowed by the M17-228 threshold bookkeeping:

\[
\boxed{
M_n=\theta^nM_0,
\qquad
0<\theta<1,
}
\]

and

\[
\boxed{
\ell_n=\theta^{n/4}\ell_0.
}
\]

This saturates the scale relation

\[
\ell_{n+1}=\theta^{1/4}\ell_n.
\]

Then

\[
\ell_n^2
=\theta^{n/2}\ell_0^2.
\]

---

## 3. Instantaneous Poincare palinstrophy floor is summable

The scale-`ell_n` mean-zero Poincare floor is

\[
P_n^{min}
\sim
\frac{M_n}{\ell_n^2}.
\]

Substituting the model gives

\[
\boxed{
P_n^{min}
\sim
\theta^{n/2}
\frac{M_0}{\ell_0^2}.
}
\]

Therefore

\[
\boxed{
\sum_{n=0}^\infty P_n^{min}
<\infty.
}
\]

So even the instantaneous lower bound decreases geometrically despite the shrinking physical scale.

The factor `ell_n^-2` is more than offset by the loss of carrier mass.

---

## 4. Own-parabolic-lifetime action is also summable

The natural lifetime of scale `ell_n` is

\[
\Delta\theta_n\sim\ell_n^2.
\]

Multiplying the palinstrophy floor by that time gives

\[
\Delta\theta_n P_n^{min}
\sim
\ell_n^2
\frac{M_n}{\ell_n^2}
=M_n.
\]

Hence

\[
\boxed{
\mathcal A_n^{min}
\sim M_n
=\theta^nM_0.
}
\]

Therefore

\[
\boxed{
\sum_{n=0}^\infty\mathcal A_n^{min}
\le
\frac{M_0}{1-\theta}
<\infty.
}
\]

Thus even assigning one full parabolic action to every scale level does not create a divergent cost.

---

## 5. Allowing partial numerator retention does not automatically help

Suppose the retained raw Laplacian numerator also changes geometrically,

\[
H_n=\gamma^nH_0,
\qquad
0<\gamma\le1.
\]

Then

\[
\ell_n
=\left(\frac{M_n}{H_n}\right)^{1/4}
=\left(\frac\theta\gamma\right)^{n/4}\ell_0.
\]

The Poincare floor becomes

\[
\frac{M_n}{\ell_n^2}
=\sqrt{M_nH_n}
=(\theta\gamma)^{n/2}\sqrt{M_0H_0}.
\]

Hence whenever

\[
\theta\gamma<1,
\]

it is again geometrically summable.

Even perfect numerator retention `gamma=1` leaves

\[
P_n^{min}\sim\theta^{n/2}.
\]

Thus retaining the `H2` numerator alone does not generate the required non-summability.

---

## 6. Consequence for the Scale-Return Gate

The following implication is false in general:

\[
\boxed{
\ell_n\to0
\quad\not\Rightarrow\quad
\sum_n\text{palinstrophy cost}=\infty.
}
\]

A successful SRG must contain more information than scale shrinkage.

At least one additional mechanism is required, for example:

1. a lower bound preventing geometric loss of carrier mass;
2. an amplitude-scale relation tying `M_n` to `ell_n` more strongly than `M_n\sim ell_n^4H_n`;
3. a time-genealogy theorem preventing every scale level from using a new disjoint tiny mass budget;
4. a coefficient equation forcing an amplitude-independent cost as `ell_n->0`;
5. a return to a nodal/rank structure with a fixed quantitative charge.

---

## 7. Relation to M17-207 divergent shell packing

M17-207 preserves a nonsummable critical defect over globally tempered **remote shells**.

That does not automatically transfer to the internal scale depth `n` of one shell packet.

Shell index and microcarrier depth are different coordinates.

Therefore one cannot multiply the M17-207 shell divergence by an assumed infinite internal scale cost.

For a valid contradiction one would need a theorem showing that a fixed fraction of the shell defect survives to a lower-order payment uniformly through the internal descent.

That theorem is precisely a form of SRG and remains open.

---

## 8. Relation to the finite derivative-witness audit

This calculation mirrors the earlier derivative-order audit.

Repeated local escalation may look stronger at every step while the associated formed charge becomes smaller.

Therefore

\[
\boxed{
\text{strict local escalation}
\neq
\text{nonsummable global cost}.
}
\]

A proof must track the charge magnitude, not only the scale or derivative label.

---

## 9. Updated SRG target

The useful target is now more precise.

One needs an estimate of the form

\[
\boxed{
\text{finite scale ladder}
\Longrightarrow
\mathcal B_{low}
\ge
c\,\mathcal D_{shell}
}
\]

where

- `mathcal D_shell` is a fixed fraction of the M17-207 shell defect;
- `mathcal B_low` is a lower-order formed channel with a known or potentially summable spacetime ledger;
- `c>0` is independent of the internal ladder depth and carrier mass loss.

Without depth-independent preservation of shell charge, the microcarrier ladder remains a legitimate concentration-compactness escape.

---

## 10. DSD audit

- The mass decay is included explicitly rather than hidden behind `ell^-2` growth.
- Palinstrophy is not assigned a fictitious finite global budget.
- Scale depth is not summed as if it were shell index or time generation.
- Numerator retention alone is shown insufficient for a nonsummable cost.
- The SRG remains open and is now stated with the required depth-independent shell-charge preservation.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
