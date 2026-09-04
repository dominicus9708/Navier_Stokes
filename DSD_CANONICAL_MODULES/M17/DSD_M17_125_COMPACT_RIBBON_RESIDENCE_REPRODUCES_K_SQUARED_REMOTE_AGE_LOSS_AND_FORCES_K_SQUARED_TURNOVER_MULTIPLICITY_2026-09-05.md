# DSD M17-125 — Compact ribbon residence reproduces the K^-2 current-stage remote-age loss; K^2 historical-turnover inference retracted

Date: 2026-09-05
Canonical ID: **M17-125**

Status: **AUDIT-CORRECTED SCALE/RESIDENCE RESULT / THE EXACT STATEMENT THAT SURVIVES IS `Delta t_carrier/rho_{j,k}^2 <= C K_k^-2` FOR ONE CARRIER ENTERING THE COMPACT RIBBON CLASS AT CURRENT FIRST-HITTING STAGE `j`. THE PREVIOUS DRAFT INCORRECTLY EXTENDED THIS TO `K_k^2` FRESH CARRIERS FOR AN ANCESTOR-SCALE HISTORICAL DWELL. THAT SCENARIO IS NOT AVAILABLE FORWARD OF `t_j`, BECAUSE ONLY `r_j^2` PHYSICAL TIME REMAINS BEFORE `T` WHILE `rho_{j,k}^2=r_j^2K_k^2`. OVER THE ACTUAL HISTORICAL INTERVAL `[theta_{j-k},theta_j]`, WHOSE SIMILARITY LENGTH IS `2 log K_k`, A UNIFORM PER-CARRIER SIMILARITY RESIDENCE BOUND `tau_*` IMPLIES ONLY AN ORDER-`log K_k` SEQUENTIAL-CARRIER LOWER COUNT IF ONE ASSUMES GAP-FREE COMPACT-RIBBON COVERAGE OF THE ENTIRE INTERVAL. NO `K_k^2` THROUGHPUT LAW IS DERIVED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity-to-physical time

Use

\[
r(\theta)=e^{-\theta/2},
\qquad
T-t=e^{-\theta}=r(\theta)^2.
\]

At stage `j`, if one material ribbon remains in the compact ribbon class for similarity duration `Delta theta`, then

\[
\boxed{
\Delta t
=r_j^2(1-e^{-\Delta\theta}).
}
\]

M17-117 gives

\[
0\le\Delta\theta\le\tau_*<\infty,
\]

hence

\[
\boxed{
\Delta t_{carrier}
\le
c_*r_j^2,
\qquad
c_*:=1-e^{-\tau_*}<1.
}
\]

---

## 2. Exact current-stage remote-age fraction

The ancestor-radius identity is

\[
\boxed{
\rho_{j,k}=r_jK_k=r_{j-k}.
}
\]

Therefore

\[
\rho_{j,k}^2=r_j^2K_k^2
\]

and the one-current-carrier residence fraction is

\[
\boxed{
\frac{\Delta t_{carrier}}{\rho_{j,k}^2}
\le
\frac{c_*}{K_k^2}.
}
\]

This exactly reproduces the M5 `K_k^{-2}` loss for information supplied only from the current first-hitting stage.

---

## 3. Why the old K^2 turnover inference is invalid

The previous draft asked a stage-`j` Eulerian structure to persist forward for a physical time comparable to

\[
\rho_{j,k}^2=r_j^2K_k^2.
\]

But the entire remaining physical time after `t_j` is only

\[
T-t_j=r_j^2.
\]

For `K_k>1`,

\[
\rho_{j,k}^2>T-t_j.
\]

Thus the hypothesized forward interval does not exist before the candidate singular time.

Consequently the implication

\[
\text{ancestor-scale dwell}
\Longrightarrow
N_{turn}\gtrsim K_k^2
\]

was not a valid historical genealogy statement and is retracted.

Likewise the associated formal throughput estimate

\[
N_{turn}\Phi_k\gtrsim K_k^2\Phi_k
\]

is retracted.

---

## 4. Correct historical interval

The actual ancestor interval is

\[
[\theta_{j-k},\theta_j]
\]

with

\[
\boxed{
\theta_j-\theta_{j-k}
=2\log K_k.
}
\]

Suppose, as an additional hypothesis, that an Eulerian compact-ribbon structure is present **gap-free throughout this entire similarity interval**, and that each individual material carrier can remain in the compact ribbon class for at most `tau_*` similarity time.

Then the number of sequential carriers must satisfy only

\[
N_{hist}(k)\tau_*
\ge
2\log K_k.
\]

Hence

\[
\boxed{
N_{hist}(k)
\ge
\frac{2\log K_k}{\tau_*}.
}
\]

This is logarithmic in `K_k`, not quadratic.

---

## 5. Relation to weighted return density

For a carrier entering at current stage `j`,

\[
\frac{\Delta t_{carrier}}{\rho_{j,k}}
\lesssim
\frac{r_j^2}{r_jK_k}
=
\frac{r_j}{K_k}
=
\frac{\rho_{j,k}}{K_k^2}.
\]

Thus the current-stage contribution alone still suffers the exact `K_k^{-2}` remote-age suppression.

But one may not multiply this current-stage contribution by a hypothetical `K_k^2` carrier count without a theorem producing that many carriers at comparable physical radius and with the required amplitude.

The historical return-density problem remains a time-distributed genealogy question.

---

## 6. Connection to prior M5 audit

This correction returns M17 to the earlier M5 conclusion:

- current remaining-time persistence is too short by `K_k^{-2}`;
- ancestor-radius matching alone does not produce ancestor-scale dwell;
- the missing information is historical material/amplitude persistence, repeated activity, or an independent rigidity theorem.

M17-126 subsequently improves the **spatial** genealogy under bounded similarity velocity, but it does not by itself provide the missing amplitude history.

---

## 7. DSD audit

### Audit A — exact algebraic K^-2 ratio

Retained.

### Audit B — K^2 carrier multiplicity

Retracted as a historical inference. It compared a current-stage carrier lifetime with a future interval longer than the entire remaining time to `T`.

### Audit C — logarithmic historical multiplicity

Conditional only on gap-free compact-ribbon coverage throughout `[theta_{j-k},theta_j]`.

### Audit D — throughput contradiction

Not derived. Neither `K_k^2 Phi_k` nor any finite total-variation director-flux budget follows from the corrected argument.

### Audit E — proof status

The correction narrows the valid statement but prevents a false turnover-cost route.

---

## 8. Correct frontier

The retained exact statement is

\[
\boxed{
\text{one current compact ribbon carrier}
\Longrightarrow
\text{remote-age dwell fraction }O(K_k^{-2}).
}
\]

The valid historical question is instead

\[
\boxed{
\text{remote shell at }\theta_j
\stackrel{?}{\Longrightarrow}
\text{sufficient same-scale amplitude/activity near }\theta_{j-k}.
}
\]

M17-126 resolves part of the location issue under bounded `U`; amplitude retention is the next unresolved gate.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
