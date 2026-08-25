# DSD All-Age Erosion Budget and Finite-Age Tightness Gate

Date: 2026-08-25

Status: **ALL-AGE UNWEIGHTED SHELL CHARGE SHOWN INSUFFICIENT FOR UNIFORM EROSION COST / NECESSARY FINITE-AGE TIGHTNESS CONDITION ISOLATED / EXPONENTIAL AGE-MOMENT SUFFICIENT CRITERION DERIVED / DIRECT GLOBAL MOMENT ROUTE CONFLICTS WITH A CRITICAL 1/R VELOCITY TAIL / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`DSD_WEIGHTED_FIXED_SHELL_QUANTIFICATION_AND_DEMHCT_AGE_OBSTRUCTION_2026-08-25.md` converted the qualitative fixed-shell extraction into an explicit age-dependent lower floor.

The remaining question is whether one can avoid choosing one shell and instead sum all shell ages directly against a single spacetime derivative budget.

This note shows that the present unweighted remote-shell charge is insufficient for that purpose because the erosion-cost coefficient tends to zero with shell age.

It then isolates the additional tightness information that would be sufficient.

---

## 2. Remote shell charge

On the recurrent remote-witness set `A_rw`, define

\[
a_k(s)=(R_km_k(s))^{3/2},
\qquad
I_k=\int_{A_{rw}}a_k(s)d\mu(s).
\]

The established shell ledger is

\[
\boxed{
\sum_{k=0}^{\infty}I_k\ge A_*d_{rw}>0.
}
\]

On the bounded normalized-enstrophy branch,

\[
\boxed{
a_k(s)\le M_k=(R_kZ_+)^{3/2}.}
\]

No age moment or finite-age tightness estimate has yet been proved.

---

## 3. Linear coefficient attached to an E-branch shell integral

For a fixed age `k`, the quantitative threshold extraction gives a shell-set density proportional to

\[
I_k/M_k.
\]

If the E branch is the selected finite-partition survivor, the previous DEMHCT event packing gives schematically

\[
\overline R_L
\ge
c_k I_k,
\]

with the explicit coefficient

\[
\boxed{
c_k
:=
\frac{H_{L,eros}(k)}
{6M_kS_{fix}(k)}.
}
\]

Here

\[
M_k=(R_0Z_+)^{3/2}q^{3k/4},
\]

and

\[
H_{L,eros}(k)
=
C_{eros}
\frac{q^{-9k-3/2}
\exp[-5A_{st}(k+1)L_+]}
{T_{fix}(k)^4}.
\]

Therefore

\[
\boxed{
c_k
=
C_c
\frac{
q^{-39k/4}
\exp[-5A_{st}(k+1)L_+]
}
{S_{fix}(k)T_{fix}(k)^4},
}
\]

for a fixed positive constant `C_c`.

In particular,

\[
\boxed{c_k\to0\qquad(k\to\infty).}
\]

---

## 4. Abstract all-age obstruction lemma

Let `c_k>0` with `c_k -> 0`.

Consider nonnegative shell charges `I_k` satisfying only

\[
\sum_k I_k\ge A>0.
\]

Then there is no universal positive lower bound for

\[
\sum_k c_kI_k.
\]

Indeed, for every `epsilon>0`, choose `K` so large that

\[
c_K<\epsilon/A.
\]

Set

\[
I_K=A,
\qquad
I_k=0\quad(k\ne K).
\]

Then

\[
\sum_kI_k=A
\]

but

\[
\sum_kc_kI_k
=c_KA<\epsilon.
\]

In the present shell ledger this test sequence is compatible with the pointwise ceiling for all sufficiently large `K`, because

\[
M_K=(R_KZ_+)^{3/2}\to\infty.
\]

Hence the existing shell upper bound does not repair the obstruction.

Status: **PROVED.**

---

## 5. Consequence for direct all-age erosion summation

Even if one could organize the E-branch contributions additively over all shell ages, the current information

\[
\sum_kI_k\ge A_*d_{rw}
\]

would not imply

\[
\sum_kc_kI_k\ge c_*>0.
\]

The remote-witness charge may, at the level of the present estimates, be concentrated at arbitrarily large age where `c_k` is arbitrarily small.

Thus the proposed direct all-age spacetime budget does not close from the current unweighted shell ledger alone.

This is a structural information deficit, not merely a poor numerical constant.

---

## 6. Finite-age tightness is sufficient

A sufficient replacement is the existence of fixed constants

\[
K<\infty,
\qquad
\eta>0
\]

such that

\[
\boxed{
\sum_{k=0}^{K}I_k
\ge
\eta A_*d_{rw}.
}
\]

Then at least one `k<=K` satisfies

\[
\boxed{
I_k
\ge
\frac{\eta A_*d_{rw}}{K+1}.
}
\]

Since the set of ages `0,...,K` is finite,

\[
\boxed{
c_{min,K}:=
\min_{0\le k\le K}c_k>0.}
\]

Consequently an E-dominant finite partition on that low-age charge would force a uniform positive mean hyperpalinstrophy floor of order

\[
\boxed{
\overline R_L
\gtrsim
c_{min,K}
\frac{\eta A_*d_{rw}}{K+1}.
}
\]

This can then be compared numerically with the existing finite mean-R cap.

Call this the **Finite-Age Tightness Gate (FATG)**.

Status: **PROVED SUFFICIENT REDUCTION.**

---

## 7. A growing age moment implies FATG

Suppose there exists `Gamma>1` and a finite uniform constant `M_Gamma` such that

\[
\boxed{
\sum_{k=0}^{\infty}\Gamma^k I_k
\le M_\Gamma.
}
\]

Then for every `K`,

\[
\sum_{k>K}I_k
\le
\Gamma^{-(K+1)}M_\Gamma.
\]

Choose `K` so that

\[
\Gamma^{-(K+1)}M_\Gamma
\le
\frac12A_*d_{rw}.
\]

Using the total lower bound,

\[
\boxed{
\sum_{k=0}^{K}I_k
\ge
\frac12A_*d_{rw}.
}
\]

Thus FATG holds with

\[
\eta=1/2.
\]

An explicit admissible age ceiling is

\[
\boxed{
K
\ge
\frac{
\log\left(2M_\Gamma/(A_*d_{rw})\right)
}{\log\Gamma}-1.
}
\]

Status: **PROVED.**

---

## 8. Spatial interpretation of the age moment

Because

\[
a_k=(R_km_k)^{3/2}
\]

and `m_k<=Z_+`,

\[
a_k
\le
Z_+^{1/2}R_k^{3/2}m_k.
\]

Hence

\[
\sum_k\Gamma^ka_k
\le
Z_+^{1/2}
\sum_k\Gamma^kR_k^{3/2}m_k.
\]

Since

\[
R_k=R_0\lambda^k,
\qquad
\lambda=\sqrt q,
\]

write

\[
\Gamma^kR_k^{3/2}
=R_0^{3/2}
\lambda^{pk},
\]

where

\[
\boxed{
p
=\frac32+
\frac{\log\Gamma}{\log\lambda}
>\frac32.
}
\]

Therefore a uniform recurrent bound on a spatial vorticity moment of the schematic form

\[
\boxed{
\int |y|^p|\Omega(y,s)|^2dy
\le C_p,
\qquad p>3/2,
}
\]

would imply a growing age moment and hence FATG.

This identifies one concrete analytic route to finite-age tightness.

---

## 9. Critical-tail obstruction to the naive global moment route

The surviving passive critical velocity tail has the formal scale

\[
|V(y)|\sim |y|^{-1},
\qquad
|W(y)|\sim |y|^{-2}.
\]

Then

\[
|W|^2dy
\sim r^{-4}r^2dr
=r^{-2}dr.
\]

A weighted vorticity moment behaves as

\[
\int^\infty r^p|W|^2dy
\sim
\int^\infty r^{p-2}dr,
\]

which converges only for

\[
\boxed{p<1.}
\]

But the FATG moment route above requires

\[
p>3/2.
\]

Therefore a **global** weighted-vorticity moment strong enough to force FATG is incompatible with an actual nonzero critical `1/r` velocity tail.

Status: **CONDITIONAL SCALING OBSTRUCTION for the critical-tail survivor.**

This does not rule out a weighted moment for a defect obtained after separating a canonical passive critical tail from the active recurrent core.

---

## 10. Defect-moment route

The previous section suggests that the correct target is not

\[
\int |y|^p|W|^2dy<\infty
\]

for the whole recurrent field.

Instead, if one can identify a canonical passive tail `W_tail` and write

\[
W=W_{tail}+W_{def},
\]

then a bound

\[
\boxed{
\int |y|^p|W_{def}|^2dy
\le C_{def,p},
\qquad p>3/2,
}
\]

could force finite-age tightness for the **active defect charge** while allowing the passive critical tail itself to remain non-integrable at that weight.

No such canonical tail subtraction or defect-moment estimate is currently proved.

Status: **NEW REDUCTION / OPEN.**

---

## 11. Relation to the R and T_multi branches

FATG is only needed to prevent the E branch from escaping to arbitrarily old ancestry under the current material-retention estimate.

If instead large-age remote witnesses are necessarily classified as

\[
R\quad\text{or}\quad T_{multi},
\]

then an independent closure of those branches may bypass FATG.

Thus the proof tree now has two coherent continuations:

\[
\boxed{
\text{E route: prove finite-age tightness / defect moment}
}
\]

or

\[
\boxed{
\text{replacement route: close R and }T_{multi}
\text{ strongly enough that large-age drift cannot survive.}
}
\]

---

## 12. DSD audit

The calculation separates:

- total remote shell charge;
- shell age;
- age-dependent erosion cost;
- finite-age tightness;
- global critical tail;
- active defect relative to that tail.

The failure of one channel to control another is recorded explicitly rather than hidden inside a positive-density statement.

---

## 13. Updated frontier

The immediate E-branch frontier is now

\[
\boxed{
\text{FATG: force a positive fraction of active remote charge into bounded shell age.}
}
\]

A naive whole-field weighted-vorticity moment is not compatible with the passive critical-tail survivor, so the most plausible E-side refinement is a **core/tail defect decomposition** with a weighted moment on the active defect only.

In parallel, the R/contact and T_multi replacement branches remain available as a route that may bypass material age entirely.

---

## 14. Audit verdict

### PROVED

- the fixed-age E cost coefficient tends to zero with age;
- unweighted all-age shell positivity cannot force a uniform positive erosion cost;
- finite-age tightness is sufficient to restore a finite minimum cost;
- a growing age moment implies finite-age tightness;
- the corresponding direct spatial moment would require order `p>3/2`.

### CONDITIONAL / STRUCTURAL

- a genuine `1/r` velocity tail makes whole-field vorticity moments with `p>=1` divergent, so the naive global moment route cannot coexist with that survivor.

### NOT DERIVED

- FATG for the active recurrent charge;
- canonical passive-tail subtraction;
- weighted moment of the active defect;
- E-branch closure;
- R/contact closure;
- T_multi closure;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
