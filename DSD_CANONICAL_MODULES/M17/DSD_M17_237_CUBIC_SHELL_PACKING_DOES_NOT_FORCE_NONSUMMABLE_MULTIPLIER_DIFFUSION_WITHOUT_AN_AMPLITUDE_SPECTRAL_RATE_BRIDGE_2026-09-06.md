# DSD M17-237 — Cubic shell packing does not force nonsummable multiplier diffusion without an amplitude/spectral-rate bridge

Date: 2026-09-06  
Canonical ID: **M17-237**

Status: **SHELL-SUMMATION FIREWALL / M17-207 PROVIDES A TEMPERED SUBFAMILY WITH `sum b_k^(3/2)=infinity`, WHERE `E_k=b_k/R_k`. M17-235 GIVES ON EACH BOUNDED-COEFFICIENT MEAN-DOMINATED INTRINSIC CELL A WEIGHTED MULTIPLIER-DIFFUSION FLOOR `D_i >= c H_i^(3/2) M_i^(-1/2)`. SUMMING CELLS AND USING HOLDER REMOVES FRAGMENTATION: `sum_i D_i >= c H_k^(3/2) E_k^(-1/2)`. WRITING `H_k=Lambda_k^2 E_k` GIVES ONLY `D_k >= c E_k Lambda_k^3 = c b_k Lambda_k^3/R_k`. THE DYADIC FACTOR `R_k^-1` IS NOT PRESENT IN M17-207'S CUBIC DEFECT. THEREFORE `sum b_k^(3/2)=infinity` AND EVEN `Lambda_k->infinity` DO NOT IMPLY `sum D_k=infinity`; AN EXPLICIT COUNTERMODEL IS `b_k~k^(-2/3)`, `R_k=2^k`, `Lambda_k~k^(1/10)`, FOR WHICH THE CUBIC DEFECT DIVERGES BUT THE DIFFUSION LOWER BOUNDS ARE SUMMABLE. THUS THE AMPLITUDE FIREWALL CANNOT BE REMOVED BY A FORMAL EXPONENT MATCH. AN ADDITIONAL RATE/GENEALOGY BRIDGE RELATING `Lambda_k`, `b_k`, AND `R_k` IS REQUIRED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Tempered shell variables

On the M17-207 tempered subfamily write

\[
\boxed{
E_k=\frac{b_k}{R_k},
\qquad
R_k=2^kR_0,
}
\]

with

\[
\sup_kb_k<\infty
\]

and

\[
\boxed{
\sum_{k\in G_{temp}}b_k^{3/2}=\infty.
}
\]

On the spectral branch define

\[
\boxed{
H_k:=\int_{C_k}|\Delta W|^2dy,
\qquad
\Lambda_k^2:=\frac{H_k}{E_k}.
}
\]

The hard spectral sequence has

\[
\Lambda_k\to\infty
\]

along a suitable subfamily.

---

## 2. Cell-level multiplier-diffusion floor

Partition one shell into finitely overlapping intrinsic cells indexed by `i`.

Let

\[
M_i
\]

be each selected cell's `L2` mass and

\[
H_i
\]

its retained raw Laplacian charge.

On the M17-235 bounded-gradient coefficient branch,

\[
\boxed{
D_i
:=\int_{B_i}|W|^2|\nabla\kappa|^2dy
\ge c\frac{H_i^{3/2}}{M_i^{1/2}}.
}
\]

This is just

\[
M_i\ell_i^{-6}
\]

with

\[
\ell_i^4=M_i/H_i.
\]

Coefficient-spike, palinstrophy, and nodal cells remain separate explicit branches and are not included in this lower bound.

---

## 3. Fragmentation cannot reduce the shell-level convex cost

For positive `M_i,H_i`, Holder gives

\[
\sum_iH_i
=\sum_i
\left(\frac{H_i^{3/2}}{M_i^{1/2}}\right)^{2/3}
M_i^{1/3}
\]

and therefore

\[
\sum_iH_i
\le
\left(
\sum_i\frac{H_i^{3/2}}{M_i^{1/2}}
\right)^{2/3}
\left(\sum_iM_i\right)^{1/3}.
\]

Raise to the power `3/2`:

\[
\boxed{
\sum_i\frac{H_i^{3/2}}{M_i^{1/2}}
\ge
\frac{(\sum_iH_i)^{3/2}}
{(\sum_iM_i)^{1/2}}.
}
\]

Thus splitting the spectral charge among many small packets does not lower the aggregate convex diffusion cost.

If the partition retains fixed fractions of shell numerator and has a finite-overlap denominator ceiling,

\[
\sum_iH_i\ge c_HH_k,
\qquad
\sum_iM_i\le C_ME_k,
\]

then

\[
\boxed{
D_{\kappa,k}^{agg}
\ge c\frac{H_k^{3/2}}{E_k^{1/2}}.
}
\]

---

## 4. Express the shell lower bound by the spectral ratio

Since

\[
H_k=\Lambda_k^2E_k,
\]

we have

\[
\frac{H_k^{3/2}}{E_k^{1/2}}
=\Lambda_k^3E_k.
\]

Therefore

\[
\boxed{
D_{\kappa,k}^{agg}
\ge c\Lambda_k^3E_k
=c\frac{b_k}{R_k}\Lambda_k^3.
}
\]

This is the strongest direct shell aggregation supplied by the present intrinsic coefficient analysis.

---

## 5. Why the 3/2 exponent does not match M17-207 automatically

M17-207 controls

\[
\sum b_k^{3/2}.
\]

The multiplier-diffusion floor contains instead

\[
\frac{b_k}{R_k}\Lambda_k^3.
\]

No established theorem gives

\[
\frac{\Lambda_k^3}{R_k}
\gtrsim b_k^{1/2}.
\]

Without such a rate bridge, the two sequences are independent enough that one may diverge while the other remains summable.

---

## 6. Explicit abstract countermodel

Take

\[
R_k=2^k,
\qquad
b_k=(k+1)^{-2/3},
\qquad
\Lambda_k=(k+1)^{1/10}.
\]

Then

\[
\boxed{
\Lambda_k\to\infty.
}
\]

Also

\[
b_k^{3/2}=(k+1)^{-1},
\]

so

\[
\boxed{
\sum_kb_k^{3/2}=\infty.
}
\]

But the diffusion lower-bound sequence is

\[
\frac{b_k}{R_k}\Lambda_k^3
=
2^{-k}(k+1)^{-2/3+3/10}
=
2^{-k}(k+1)^{-11/30}.
\]

Hence

\[
\boxed{
\sum_k\frac{b_k}{R_k}\Lambda_k^3<\infty.
}
\]

This is a logical counterexample to the proposed implication based only on the currently proved scalar sequence properties.

It is not asserted to be realized by a Navier--Stokes solution.

---

## 7. Consequence for the Amplitude-Return Gate

The route

\[
\text{M17-207 cubic defect}
+
\text{M17-235 local multiplier diffusion}
\Longrightarrow
\text{nonsummable global diffusion cost}
\]

is invalid without an additional theorem.

The missing input must relate at least two of

\[
\boxed{
b_k,\quad R_k,\quad\Lambda_k,\quad\text{material genealogy}.}
\]

A sufficient rate bridge would be, for example,

\[
\Lambda_k^3
\gtrsim R_kb_k^{1/2}
\]

on a nonsummable shell subfamily.

No such estimate is currently derived.

---

## 8. What kind of bridge remains plausible

The remaining legitimate routes are narrower:

1. **material genealogy:** prove that a high-`Lambda` packet cannot be newly replaced independently on every remote shell;
2. **amplitude persistence:** obtain a lower bound on packet mass relative to intrinsic scale that rules out the abstract countermodel;
3. **coefficient spike return:** show that slow `Lambda` growth forces repeated dimensionless `kappa`/`grad kappa` spikes with a separate cost;
4. **nodal/replenishment return:** prove that the sign-balanced coefficient packet must cross a formed low-amplitude or replacement event at positive rate.

Pure spatial shell summation is insufficient.

---

## 9. DSD audit

- Cell fragmentation is handled by a genuine convex Holder inequality before the shell comparison.
- The dyadic radius factor is retained; it is not absorbed into `b_k` twice.
- The abstract countermodel proves a non-implication only from the current inequalities; it is not claimed as a physical solution.
- `Lambda_k->infinity` supplies no quantitative growth rate by itself.
- The cubic exponent coincidence is not treated as a proof.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
