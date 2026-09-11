# M18-058 — Composite first-hitting-to-record scaling cancels the apparent positive-R standard-energy gain unless a genuinely fixed finite-energy parent is certified

**Date:** 2026-09-11  
**Status:** AC COMPOSITE-SCALE FIREWALL / LOWER-ORDER-DESCENT SCOPE CORRECTION / FIXED-PARENT REQUIREMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-056 proves a correct cellwise lower-order descent:

\[
q_P\le q_0^{1/2}q_H^{1/2},
\qquad
q_P\le q_0^{2/3}q_{D3}^{1/3},
\qquad
q_H\le q_0^{1/3}q_{D3}^{2/3}.
\]

If a record family already sits inside one **fixed finite-energy parent** with large record factors \(R_m\to\infty\), then

\[
\sum_m R_m q_{0,m}<\infty
\]

is a strong positive-\(R\) standard-energy ledger.

The present module audits whether the actual first-hitting \(\to\) first ancient \(\to\) second-generation record construction automatically supplies such a fixed parent.

It does not.

The large second-generation factor \(R_m\) is composed with a shrinking first-generation base scale. In original physical variables the composite scale is the old first-hitting own scale, and fixed normalized standard-energy events remain geometrically summable.

This is a scope correction, not a retraction of M18-056.

## 2. First-hitting scale ladder

Write

\[
W_j=q^jW_0,
\qquad
r_j=\sqrt{\nu/W_j},
\qquad q>1.
\]

For age \(m\),

\[
R_m:=q^{m/2},
\]

so

\[
\boxed{
r_{j-m}=R_m r_j.
}
\]

Thus an \(m\)-generation-old stage is large by factor \(R_m\) in the finer stage-\(j\) normalization, but its physical length scale is still only \(r_{j-m}\).

## 3. First-generation normalization

Suppress harmless translations and viscosity constants for the scaling audit.

At stage \(j\), define

\[
\Omega_j(y,s)
=
 r_j^2\,\omega(X_j+r_jy,t_j+r_j^2s).
\]

The first ancient element is obtained from a limit of such stage-\(j\) normalized solutions.

A second-generation record blow-down of the stage-\(j\) representative has the form

\[
\Omega_{j,m}^{(2)}(z,\sigma)
=
R_m^2
\Omega_j(R_mz,R_m^2\sigma).
\]

Substituting the first normalization gives

\[
\boxed{
\Omega_{j,m}^{(2)}(z,\sigma)
=
(r_jR_m)^2
\omega(
X_j+r_jR_m z,
 t_j+r_j^2R_m^2\sigma
).
}
\]

Therefore the actual composite physical scale is

\[
\boxed{
\rho_{j,m}:=r_jR_m=r_{j-m}.
}
\]

The second-generation large-\(R_m\) factor is not an additional physical scale gain after composition with the original solution.

## 4. General composite resource law

For the spacetime derivative resource

\[
q_k
:=
\int\|D^k\Omega\|_2^2 ds,
\]

a normalization at physical length scale \(\rho\) obeys

\[
q_k^{norm}
=
\rho^{2k-1}q_k^{phys},
\]

or equivalently

\[
\boxed{
q_k^{phys}
=
\rho^{1-2k}q_k^{norm}.
}
\]

For the composite first-hitting/record cell,

\[
\boxed{
q_{k,jm}^{phys}
=
(r_jR_m)^{1-2k}
q_{k,jm}^{(2)}
=
r_{j-m}^{\,1-2k}
q_{k,jm}^{(2)}.
}
\]

This is the correct original-parent weight.

## 5. Standard-energy case

For \(k=0\),

\[
\boxed{
q_{0,jm}^{phys}
=
r_{j-m}
q_{0,jm}^{(2)}.
}
\]

Thus if lower-order descent gives a fixed recordwise payment

\[
q_{0,jm}^{(2)}\ge e_*>0,
\]

the corresponding original physical energy-dissipation cost is only

\[
\boxed{
e_* r_{j-m}.
}
\]

The apparent positive record weight \(R_m\) has been multiplied by the shrinking base factor \(r_j\):

\[
\boxed{
r_jR_m=r_{j-m}.
}
\]

## 6. Chronological first-hitting costs remain summable

Since

\[
r_n\asymp q^{-n/2},
\]

we have

\[
\boxed{
\sum_{n\ge n_0}r_n<\infty.
}
\]

Therefore one fixed normalized standard-energy payment attached to each distinct chronological first-hitting generation is entirely compatible with finite physical kinetic-energy dissipation:

\[
\boxed{
\sum_n r_n e_*<\infty.
}
\]

This recovers the M5-598/M18-048 own-scale summability firewall from the full two-generation composition.

## 7. Diagonal record families split into summability or reuse

Consider a diagonal family of finite-stage representatives

\[
(j_\ell,m_\ell),
\]

and define the corresponding chronological ancestor index

\[
n_\ell:=j_\ell-m_\ell.
\]

There are two cases.

### A. \(n_\ell\to\infty\)

Then the physical scales satisfy

\[
r_{n_\ell}\to0.
\]

For distinct increasing chronological generations,

\[
\sum_\ell r_{n_\ell}<\infty.
\]

Hence fixed normalized \(q_0\) payments remain standard-energy summable.

### B. \(n_\ell\) stays bounded

After a subsequence, one chronological stage index \(n_*\) repeats.

Then infinitely many second-generation descriptions are being pulled back into one fixed coarse physical stage/window.

A fixed-thickness event family cannot automatically be counted infinitely many times there. Unless independent disjoint events inside that finite parent window are separately certified, this is rerecording/reuse rather than new ancestry multiplicity.

Thus

\[
\boxed{
\text{diagonal composition}
\Longrightarrow
\text{summable shrinking-stage cost}
\lor
\text{reuse/nonindependence}.
}
\]

## 8. Why M18-056 remains correct

M18-056 states its positive-\(R\) conclusions under a **correctly aligned, nonreused, bounded-overlap record family with a certified standard-energy parent ledger**.

That theorem remains valid.

The present correction is that the repository's first-hitting/ancient/second-generation construction does not automatically provide such a fixed finite-energy parent merely because the second-generation factor satisfies

\[
R_m\to\infty.
\]

One must additionally prove that the base normalization does not shrink in a way that cancels the record factor when mapped to the actual finite-energy solution.

## 9. Generic similarity-hull ancient solutions do not repair the standard-energy budget

For a complete similarity orbit with uniformly bounded normalized enstrophy,

\[
\|W(\theta)\|_2^2\le C,
\]

the inverse physical ancient solution satisfies

\[
\|\Omega(s)\|_2^2
\lesssim
(-s)^{-1/2}.
\]

Hence at backward infinity

\[
\int_{-\infty}^{-1}
\|\Omega(s)\|_2^2ds
\]

is not forced to be finite; the model rate \((-s)^{-1/2}\) is nonintegrable.

By contrast, palinstrophy scales like \((-s)^{-3/2}\) under the same bounded similarity derivative class and can be backward-integrable.

Therefore choosing a \(\mu\)-generic complete similarity orbit as a new parent may supply the M17-307 inverse-\(R\) palinstrophy ledger, but it does **not** automatically supply the positive-\(R\) standard-energy ledger sought in M18-056.

## 10. LOG-ALIGN is not the only AC obligation

M18-039 isolates a time/event placement problem between terminal similarity production and backward record annuli.

The present module shows a logically later requirement:

\[
\boxed{
\text{EVENT-ANNULAR / LOG-ALIGN}
\neq
\text{finite-energy-parent certification}.
}
\]

Even if a terminal payer is perfectly phase-aligned with infinitely many record cells, one still must know which fixed physical parent owns those cells and what the total parent budget is after full scale composition.

Define the latter requirement as

\[
\boxed{\text{FE-PARENT}}.
\]

A useful AC chain is now

\[
\boxed{
\text{payer recurrence}
\xrightarrow{\rm LOG\text{-}ALIGN}
\text{record placement}
\xrightarrow{\rm NONREUSE}
\text{independent record events}
\xrightarrow{\rm FE\text{-}PARENT}
\text{finite-energy parent charge}.
}
\]

M18-056 only becomes globally contradictory after all three bridges are certified.

## 11. Exact chronological standard-energy threshold

Let \(e_n\) denote the normalized spacetime-enstrophy payment associated with chronological first-hitting scale \(r_n\).

The original finite-energy budget can only contradict the event family if

\[
\boxed{
\sum_n r_ne_n=\infty.
}
\]

For geometric

\[
r_n\asymp q^{-n/2},
\]

fixed or polynomial-in-\(n\) payments are insufficient.

A power-law diagnostic

\[
e_n\asymp q^{\gamma n}
\]

requires roughly

\[
\boxed{
\gamma\ge\frac12
}
\]

at the pointwise exponential threshold, with the usual nonsummability refinement at equality.

Thus lower-order descent to a merely order-one \(q_0\) payer does not by itself defeat chronological scale summability.

## 12. Consequence for the four non-CE-H branches

M18-040 and M18-056 price

\[
CP\!-E,
\quad CP\!-S,
\quad CE\!-T,
\quad Migration
\]

by palinstrophy/raw-H2 and then potentially by standard energy.

The local pricing remains useful.

But a fixed standard-energy payment per production event does not close those branches globally unless FE-PARENT produces a nonsummable original-parent charge.

Therefore the correct current status is

\[
\boxed{
\text{non-CE-H local payer identified}
\neq
\text{global ancestry contradiction}.
}
\]

Their remaining global issue is still AC economics.

## 13. DSD audit rule

For any multi-generation normalization chain, never read the ancestry weight from the last rescaling factor alone.

If the chain contains scale factors

\[
\rho_1,\rho_2,\dots,\rho_N,
\]

the physical parent weight must be computed from the **composite scale**

\[
\boxed{
\rho_{tot}=\prod_{i=1}^N\rho_i
}
\]

before any finite-budget argument is made.

A positive weight at one intermediate level may be exactly cancelled by a shrinking scale inherited from an earlier level.

## 14. Audit verdict

### Certified

1. The first-hitting plus second-generation composite scale is
   \[
   r_jR_m=r_{j-m}.
   \]
2. A fixed second-generation spacetime-enstrophy payment has original physical cost
   \[
   r_{j-m}q_0.
   \]
3. One order-one payment per chronological first-hitting generation remains geometrically summable.
4. A diagonal family either moves to ever-finer chronological stages, where the standard-energy weights are summable, or repeatedly references boundedly many coarse stages, where nonreuse is not automatic.
5. A generic complete similarity ancient orbit does not automatically have finite total spacetime enstrophy at backward infinity.
6. M18-056 remains valid conditionally on a genuinely fixed finite-energy parent; that parent is not supplied automatically by the current record construction.

### Still open

- LOG-ALIGN / orbit-to-record placement;
- NONREUSE after full finite-stage realization;
- FE-PARENT with a nonsummable composite charge;
- a theorem forcing normalized standard-energy payment growth faster than chronological scale shrinkage;
- scale-invariant signed/monotone/rigidity mechanisms avoiding additive ancestry economics;
- the remote and critical roots;
- global 3D Navier--Stokes regularity.

## 15. Next target

M18-059 should audit the **budget-versus-scaling compatibility of every currently available unsigned resource**.

The question is whether any resource simultaneously has:

1. a finite original-parent total;
2. a non-summable own-scale weight on the geometric first-hitting ladder;
3. a certified fixed normalized payment on the surviving branch.

If no current resource satisfies all three, then the AC route has reached a structural unsigned-payer firewall and future work must target either quantitative payer growth, a signed/monotone critical observable, or a new finite budget.