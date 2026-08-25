# DSD Pineau--Vicol Speed -> Invariant-Measure Channel Density

Date: 2026-08-25

Status: **FIVE-CHANNEL SPEED COVER LIFTED TO AN INVARIANT PROBABILITY MEASURE / AT LEAST ONE CHANNEL HAS MASS >= 1/5 / POSITIVE MEAN ABSOLUTE ACTION DERIVED / AMPLITUDE DRIFT DISTINGUISHED FROM CLOSED PHASE-SPACE CIRCULATION / GLOBAL REGULARITY UNPROVED.**

## 1. Input

On the pure locally precompact singular-survivor corridor, the previous note gives one fixed core ball `B_R`, one `sigma0>0`, and five closed threshold channels

\[
M,\quad SA,\quad SP,\quad VA,\quad VP
\]

such that every sufficiently late Leray state belongs to their union.

The orbit is locally precompact in the smooth topology supplied by the no-`H` analytic corridor.

---

## 2. Empirical invariant measures

Let `Phi_s` denote the Leray semiflow on the local smooth orbit closure `K`.

For `T>0`, define the empirical measure

\[
\mu_T:=\frac1T\int_{s_0}^{s_0+T}\delta_{\Phi_sU_0}\,ds.
\]

Local compactness gives a weak-* convergent subsequence

\[
\mu_{T_n}\rightharpoonup\mu.
\]

The standard Krylov--Bogolyubov shift argument gives

\[
\boxed{\mu\text{ is invariant under the Leray flow}.}
\]

Because every late state belongs to the five-channel cover,

\[
\boxed{
\mu(M\cup SA\cup SP\cup VA\cup VP)=1.
}
\]

Status: **PROVED.**

---

## 3. Deterministic tie-breaking partition

To avoid overlap ambiguity, order the channels

\[
M<SA<SP<VA<VP
\]

and assign each state to the first channel whose threshold is met.

This gives a measurable disjoint partition

\[
K_M, K_{SA}, K_{SP}, K_{VA}, K_{VP}
\]

with total measure one.

Therefore

\[
\boxed{
\max_X\mu(K_X)\ge\frac15.
}
\]

Thus at least one fixed mechanism survives with invariant frequency at least `1/5` along the selected recurrent invariant measure.

Status: **PROVED BY FINITE PIGEONHOLE.**

---

## 4. Action observables

Define the nonnegative instantaneous channel actions

\[
A_M:=|(U_s)_B|,
\]

\[
A_{SA}:=|\partial_s\|S\|_{L^2(B)}|,
\]

\[
A_{SP}:=\|S\|_{L^2(B)}
\left\|\partial_s\left(\frac S{\|S\|_{L^2(B)}}\right)\right\|_{L^2(B)},
\]

\[
A_{VA}:=|\partial_s\|\Omega\|_{L^2(B)}|,
\]

and

\[
A_{VP}:=\|\Omega\|_{L^2(B)}
\left\|\partial_s\left(\frac\Omega{\|\Omega\|_{L^2(B)}}\right)\right\|_{L^2(B)}.
\]

At zero amplitude use the continuous convention that nonzero derivative belongs to the amplitude channel.

The threshold construction gives fixed constants `sigma_X>0` with

\[
A_X\ge\sigma_X
\qquad\text{on }K_X.
\]

Hence

\[
\boxed{
\int A_X\,d\mu
\ge
\sigma_X\mu(K_X).
}
\]

For the channel selected by the `1/5` pigeonhole,

\[
\boxed{
\int A_X\,d\mu
\ge
\frac{\sigma_X}{5}>0.
}
\]

Equivalently, along the empirical sequence,

\[
\boxed{
\liminf_{n\to\infty}
\frac1{T_n}
\int_{s_0}^{s_0+T_n}A_X(s)ds
>0.
}
\]

Status: **PROVED.**

---

## 5. Signed amplitude derivatives average to zero

Let

\[
m(s):=(U)_B,
\qquad
a(s):=\|S\|_{L^2(B)},
\qquad
b(s):=\|\Omega\|_{L^2(B)}.
\]

On the compact orbit closure these observables are bounded.

For every component of `m`,

\[
\frac1T\int_{s_0}^{s_0+T}m_sds
=\frac{m(s_0+T)-m(s_0)}T\to0.
\]

Likewise

\[
\boxed{
\langle a_s\rangle_\mu=0,
\qquad
\langle b_s\rangle_\mu=0.
}
\]

Therefore positive mean absolute action in `M`, `SA`, or `VA` cannot represent secular one-way drift of a bounded observable. It necessarily represents repeated reversal/oscillation or boundary/material turnover.

In particular, if

\[
\int|a_s|d\mu>0,
\]

then the total variation of the local strain amplitude grows linearly in Leray time even though its net change is sublinear:

\[
\boxed{
TV(a;[0,T_n])\gtrsim T_n,
\qquad
|a(T_n)-a(0)|=O(1).
}
\]

The same holds for `b` and each bounded component of `m`.

Status: **PROVED.**

---

## 6. Consequence for amplitude channels

The preceding result eliminates a possible misinterpretation:

\[
\text{positive amplitude-speed density}
\not\Rightarrow
\text{unbounded amplitude}.
\]

A bounded recurrent orbit may oscillate forever.

Therefore a theorem-level closure of `M`, `SA`, or `VA` must charge **total variation**, not net change.

The exact mean and fixed-ball enstrophy balances from the previous note imply that every such oscillation requires repeated sign changes in the associated boundary/production/dissipation mismatch.

For example, for `VA`,

\[
(E_B)_s
=
\mathcal P_B-\mathcal D_B-\mathcal F_B,
\]

where `P_B` is local stretching production, `D_B` contains the positive similarity/viscous damping, and `F_B` collects fixed-ball radial/material/viscous boundary fluxes.

If `b>=b_->0` on the active recurrent support and `|b_s|>=sigma_VA` on a set of invariant measure `d_VA`, then

\[
\int|(E_B)_s|d\mu
\ge
b_-\sigma_{VA}d_{VA}>0.
\]

By the triangle inequality,

\[
\boxed{
\int\bigl(|\mathcal P_B|+|\mathcal D_B|+|\mathcal F_B|\bigr)d\mu
>0.
}
\]

Thus `VA` necessarily produces a positive mean typed local action. It is not a free scalar oscillation.

Analogous statements hold for `M`; `SA` requires the corresponding strain-energy/pressure-Hessian balance if one wants the same explicit payer decomposition.

Status: **PROVED FOR THE ABSTRACT ABSOLUTE BALANCE; UNIVERSAL NONSUMMABLE GLOBAL CONTRADICTION NOT YET DERIVED.**

---

## 7. Shape channels are genuine circulation

For `SP` and `VP`, the amplitude is divided out and the unit state moves on a bounded shape sphere.

Therefore positive mean action

\[
\int A_{SP}d\mu>0
\quad\text{or}\quad
\int A_{VP}d\mu>0
\]

is exactly a phase-space path-length density.

No scalar endpoint cancellation can remove it.

It may nevertheless be compatible with a periodic or quasiperiodic orbit. Hence compactness plus positive shape speed alone is not a contradiction.

The remaining PDE task is to convert this shape path length into one of the coercive Navier--Stokes ledgers:

\[
\boxed{
\text{projective H1 frequency tax}
\lor
\text{material/Cauchy turnover}
\lor
\text{derivative/eigenaxis roughness}.
}
\]

---

## 8. Combine with recurrent source geometry

The repository already proves on the residual-quiet recurrent lane that a nonzero recurrent core enters positive-middle source-active geometry on a positive invariant/time-density set, unless a Betchov/derivative/turnover exit is already active.

At such a source-active thick time, the transverse-ribbon theorem gives

\[
\boxed{
\text{viscous flux change}
\lor
\text{material replacement/nonaffinity}
\lor
\text{projective eigenframe reorganization}.
}
\]

The first branch has a finite-stage palinstrophy floor.

The second branch has finite multiflux memory and therefore positive-frequency costed exits if repeated.

Thus on a corridor that suppresses those two costed exits and `H`, the recurrent source-active set is forced into projective/eigenframe reorganization with positive invariant frequency.

This is a **conditional reduction**, because the transfer from the fixed-ball `SP/VP` field-shape action to the coherent local eigenframe action still needs a localization/coherence alternative.

Status: **CONDITIONAL BUT SHARP REDUCTION.**

---

## 9. Updated final core object

The final pure survivor is no longer described merely as a recurrent core with nonzero speed.

It must support a finite invariant measure with a positive mean action in at least one typed channel, and after excluding repeated flux/replacement/derivative exits the only unpriced pure motion is a coherent shape circulation:

\[
\boxed{
\text{positive-density projective/vorticity shape circulation}
}
\]

on a compact active core.

---

## 10. Audit verdict

### PROVED

- an invariant probability measure exists on the locally precompact orbit closure;
- the five speed channels cover it;
- one fixed channel has invariant mass at least `1/5`;
- that channel has a strictly positive long-time mean absolute action;
- bounded amplitude channels must oscillate rather than drift;
- local vorticity-amplitude oscillation has a positive mean typed payer action.

### OPEN

- a universal coercive lower bound converting every `SA`, `SP`, or `VP` circulation into a globally nonsummable viscous/turnover ledger;
- exclusion of a compact periodic/quasiperiodic shape orbit at the weak-`L3` tail endpoint;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
