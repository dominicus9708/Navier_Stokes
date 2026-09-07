# M17-321 — Recurrent-hull cocycle no-go and refresh-excursion ledger

Date: 2026-09-08
Status: rigorous no-go for state-cocycle drift; conditional excursion ledger; no global closure
Parents: M17-320, M07 recurrent-hull/cocycle audit

## 1. Purpose

M17-320 leaves the branch

\[
H_{\rm ancient\ line\text{-}weight\ carrier},
\]

meaning that a nontrivial line-weight ratio can persist on arbitrarily long backward intervals without paying a fixed finite-age cost.

The natural next question is whether recurrence of the similarity hull itself kills this branch.  The answer is **no** for any bounded state-function cocycle.  Recurrence only forces signed cancellation of the cocycle.  It does not force the instantaneous cocycle to vanish and does not provide a positive cost.

A useful positive statement survives only when the ancient carrier repeatedly *refreshes* its contrast through finite-age threshold excursions.  Those excursions can be counted, but their normalized costs still require physicalization before they can be used globally.

## 2. State-observable versus path-observable split

Let `H` be a compact recurrent similarity hull with flow (or semiflow on the available interval)

\[
\Phi^t:\mathcal H\to\mathcal H.
\]

Assume first that the selected line pair is encoded by the state strongly enough that

\[
q(x)=\log\frac{L_{\rho,\lambda}(x)}{L_{\rho,\mu}(x)}
\]

is a bounded continuous observable on the relevant hull sector.

Along an orbit `x_t=Phi^t x`, assume `q(x_t)` is absolutely continuous and

\[
F(x_t):=\frac{d}{dt}q(x_t)
=\Delta\kappa(x_t)+2\Delta\bar\sigma(x_t),
\]

where

\[
\Delta\kappa=\kappa_\lambda-\kappa_\mu,
\qquad
\Delta\bar\sigma
=\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}.
\]

If the identity of the line pair cannot be reconstructed from the current state alone, then `q` is not a state observable on `H`; it belongs to a lifted/path-dependent genealogy.  That failure is not an error but an explicit branch:

\[
G_{\rm path/genealogy\ lift}.
\]

This matches the M07 audit: bounded static state observables cannot by themselves create a strict recurrence contradiction; the viable obstruction must live in material genealogy, a path-dependent lift, or replacement/migration.

## 3. Recurrent-return cancellation lemma

Let `x` be recurrent.  Thus there are times

\[
T_n\to\infty
\]

such that

\[
\Phi^{T_n}x\to x.
\]

Continuity of `q` gives

\[
q(\Phi^{T_n}x)-q(x)\to0.
\]

But by the cocycle identity,

\[
q(\Phi^{T_n}x)-q(x)
=\int_0^{T_n}F(\Phi^t x)dt.
\]

Therefore

\[
\boxed{
\int_0^{T_n}
\bigl(\Delta\kappa+2\Delta\bar\sigma\bigr)(\Phi^t x)dt
\longrightarrow0.
}
\]

This is a **signed cancellation statement only**.

It does not imply

\[
F=0,
\]

nor does it imply

\[
\int_0^{T_n}|F|^2dt\to0.
\]

## 4. Invariant-measure version

Let `mu` be a `Phi^t`-invariant probability measure on the recurrent hull.  If `q` lies in the domain of the flow generator `A`, then

\[
F=Aq.
\]

Invariance gives

\[
\int_{\mathcal H}q(\Phi^t x)d\mu(x)
=\int_{\mathcal H}q(x)d\mu(x).
\]

Differentiating at `t=0` under the generator-domain hypothesis,

\[
\boxed{
\int_{\mathcal H}F\,d\mu=0.
}
\]

Again, this does not imply zero variance:

\[
\int_{\mathcal H}|F|^2d\mu
\]

may be strictly positive.

A model anti-example is the circle rotation with

\[
q(t)=\sin t,
\qquad
F(t)=\cos t.
\]

The orbit returns exactly after each `2 pi`, the signed cocycle over a full period is zero, but

\[
\frac1{2\pi}\int_0^{2\pi}|F|^2dt=\frac12.
\]

Thus recurrence plus zero cocycle mean is not a contradiction mechanism.

## 5. Bounded state-function strict-drift no-go

Define the additive state cocycle

\[
C_T(x):=q(\Phi^T x)-q(x).
\]

Because `q` is bounded,

\[
|C_T(x)|\le2\|q\|_{L^\infty(\mathcal H)}.
\]

Therefore no estimate of the form

\[
C_T(x)\ge cT-C_0,
\qquad c>0,
\]

can hold for all large `T` on a recurrent bounded-state branch.

Hence a proposed contradiction based on strict one-sided growth of a bounded line-weight state function is structurally impossible.

This is the M17 realization of the M07 bounded-state cocycle no-go.

## 6. What recurrence can still pay: fresh threshold excursions

Fix `0<eta<1` and the M17-319 contrast threshold `c_L>0`.

Consider a family of pairwise disjoint intervals

\[
I_j=[a_j,b_j]
\]

such that on each interval:

1. the same two line labels are trackable;
2. `|q(a_j)|=eta c_L`;
3. `|q(b_j)|>=c_L`;
4. `q` has fixed sign on `(a_j,b_j]`;
5. the curvature exposure obeys

\[
K_j:=\int_{I_j}
\max(|\kappa_\lambda|,|\kappa_\mu|)dt
\le\frac{(1-\eta)c_L}{4};
\]

6. the interval length satisfies

\[
|I_j|\le T_{\max};
\]

7. the line weights satisfy `L_{rho,alpha}>=L_*>0`.

M17-320 gives

\[
A_j
:=\bigl((1-\eta)c_L-2K_j\bigr)_+
\ge\frac{(1-\eta)c_L}{2}.
\]

Therefore each qualified excursion pays

\[
\begin{aligned}
\mathcal P_{\perp,j}
&:=
\int_{I_j}\sum_{\alpha\in\{\lambda,\mu\}}
\int_{\gamma_\alpha}
\rho|P_{\perp,\alpha}\Sigma P_{\perp,\alpha}|_F^2
\,ds\,dt\\
&\ge
\frac{L_*A_j^2}{16|I_j|}\\
&\ge
\boxed{
\frac{L_*(1-\eta)^2c_L^2}{64T_{\max}}
=:p_*>0.
}
\end{aligned}
\]

Thus if `N(T)` pairwise disjoint qualified refresh excursions occur before time `T`, then

\[
\boxed{
\mathcal P_\perp([0,T])\ge N(T)p_*.
}
\]

This is an event-counting theorem, not yet a physical dissipation theorem.

## 7. Frequency is an additional theorem, not recurrence

If one could independently prove a positive refresh frequency

\[
\liminf_{T\to\infty}\frac{N(T)}{T}\ge f_*>0,
\]

then

\[
\liminf_{T\to\infty}
\frac1T\mathcal P_\perp([0,T])
\ge f_*p_*>0.
\]

But ordinary recurrence does **not** imply this frequency bound.

Return gaps may be arbitrarily large.  Even infinitely many refresh events can have

\[
\frac{N(T)}{T}\to0.
\]

Therefore a bounded-gap, syndetic-return, positive-frequency, or invariant-measure event-frequency theorem would be an additional hypothesis/result and must not be inserted silently.

## 8. Ancient carrier subcases after the recurrence audit

The recurrent ancient carrier now splits into four mathematically distinct mechanisms.

### 8.1 Static/high-state carrier

The contrast remains above the threshold for very long or all ancient times:

\[
|q(t)|>\eta c_L.
\]

No repeated creation occurs, so the finite-age payer cannot be recharged.

### 8.2 Slow-refresh carrier

Threshold crossings occur, but their creation durations grow:

\[
|I_j|\to\infty.
\]

The M17-320 payment can decay like `1/|I_j|`.

### 8.3 Sparse-refresh carrier

There are infinitely many bounded-age refresh events, but their temporal density vanishes:

\[
N(T)/T\to0.
\]

The event count grows without providing a positive time-average rate.

### 8.4 Path/genealogy carrier

The current state does not identify the same line pair through the return.  The correct observable is path-dependent and must be lifted to a material genealogy space.

These cases cannot be merged without losing the quantifier structure.

## 9. Physicalization firewall

Even in the strongest bounded-age, positive-frequency subcase, the payer above is normalized in the similarity/line-weight variables.

The implication

\[
N(T)p_*\to\infty
\]

is not yet

\[
\int_0^{T_*}\int_{\mathbb R^3}|\nabla u|^2dxdt=\infty
\]

or any other forbidden physical budget.

A valid global contradiction still needs:

1. the exact rescaling factor from the normalized line payment to a physical quantity;
2. bounded multiplicity/overlap across lines, scales, and generations;
3. a finite physical resource with which the accumulated payments conflict.

This is the R21/R33/R38 firewall.

## 10. Corrected M17-321 frontier

The ancient carrier branch is therefore reduced to

\[
\boxed{
\begin{aligned}
H_{\rm ancient\ line\text{-}weight\ carrier}
\Longrightarrow{}&
H_{\rm static/high\text{-}state\ carrier}\\
&\lor H_{\rm slow\text{-}refresh\ carrier}\\
&\lor H_{\rm sparse\text{-}refresh\ carrier}\\
&\lor H_{\rm qualified\ refresh\ ledger}\\
&\lor G_{\rm path/genealogy\ lift}\\
&\lor G_{\rm curvature}\\
&\lor G_{\rm amplitude/line\text{-}weight}.
\end{aligned}
}
\]

For the qualified-refresh branch,

\[
\boxed{
\mathcal P_\perp([0,T])\ge N(T)p_*.
}
\]

For the recurrence cocycle itself,

\[
\boxed{
\int_0^{T_n}
(\Delta\kappa+2\Delta\bar\sigma)dt\to0,
}
\]

which is cancellation, not coercivity.

## 11. DSD audit

- **M07 consistency:** bounded static state cocycles cannot produce strict recurrence drift.
- **R21 / R33:** normalized event payments are not physical nonsummability.
- **R27 / R38:** same-line recurrence requires a genealogy coverage theorem; otherwise use the lifted path branch.
- **R25 / R37:** one recurrent orbit/selected scale does not control all finer scales.
- **Frequency quantifier:** infinitely many returns is weaker than positive return frequency.
- **No hidden monotonicity:** `q`, its variance, and the signed cocycle are not assumed monotone.

## 12. Result and next target

M17-321 rules out recurrence itself as the missing contradiction.  It also identifies the precise circumstance in which recurrence is useful: repeated finite-age refresh events generate a countable ledger of fixed normalized transverse-strain payments.

The remaining useful targets are therefore:

1. find a nonnegative material-genealogy production quantity that does not collapse to a bounded state-function coboundary; or
2. physicalize the qualified-refresh ledger with a bounded-multiplicity theorem; or
3. rule out the static/slow/sparse carrier subbranches by an independent compactness, diffusion, or finite-resource argument.

No unconditional global-regularity conclusion follows at this stage.
