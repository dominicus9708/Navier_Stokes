# DSD M5-194M — Checkpoint Phase-Gap and DSS-Locking Firewall

Date: 2026-08-29

Parent: `DSD_M5_194L_CHECKPOINT_SIMILARITY_NONTRIVIALITY_AND_STATIONARY_ALPHA_EXCLUSION_2026-08-29.md`

Status: **CORRECTIVE DYNAMIC FIREWALL / THE FIRST-HITTING SPATIAL SCALE RATIO `q` FIXES THE NATURAL DSS SCALE FACTOR `lambda=sqrt(q)`, BUT IT DOES NOT BY ITSELF FIX THE ACTUAL CHECKPOINT SEPARATION IN SIMILARITY TIME / CHECKPOINT PHASE GAPS DEPEND ON THE DIMENSIONLESS STAGE DURATIONS `theta_k=W_k Delta t_k` / A DSS LIMIT REQUIRES BOTH PHASE LOCKING AND SPACETIME BLOCK RECURRENCE / FAILURE OF PHASE LOCKING IS ITSELF A FORMED APERIODIC DEFECT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why this audit is needed

M5-194L proposed comparing consecutive backward first-hitting checkpoints in similarity time.

The geometric first-hitting levels satisfy

\[
W_{j+1}=qW_j,
\qquad
r_{j+1}=q^{-1/2}r_j.
\]

Hence the natural discrete Navier--Stokes scale factor is

\[
\boxed{\lambda=\sqrt q.}
\]

A genuine `lambda`-DSS solution would have similarity-time period

\[
\boxed{S_{DSS}=2\log\lambda=\log q.}
\]

However, the actual first-hitting **time checkpoints** are not placed by the scale ratio alone. Their physical separation depends on the durations of all intervening stages.

Therefore

\[
\boxed{
\text{scale ratio }q
\not\Rightarrow
\text{checkpoint phase gap exactly }\log q.
}
\]

---

## 2. Dimensionless stage duration

Define

\[
\boxed{
\theta_k:=W_k\Delta t_k,
\qquad
\Delta t_k=t_{k+1}-t_k.
}
\]

The previously established stage-length bounds imply

\[
0<\theta_-\le\theta_k\le\theta_+<\infty
\]

for suitable constants depending on the existing `L_-,L_+,q` bounds.

Fix a terminal generation `j`. The earlier checkpoint `j-m` appears in stage-`j` time at

\[
\tau_{j,m}
=W_j(t_{j-m}-t_j)<0.
\]

Set

\[
a_{j,m}:=|\tau_{j,m}|.
\]

Then

\[
\begin{aligned}
a_{j,m}
&=W_j\sum_{k=j-m}^{j-1}\Delta t_k\\
&=\sum_{\ell=1}^{m}
\frac{W_j}{W_{j-\ell}}\,
W_{j-\ell}\Delta t_{j-\ell}\\
&=\boxed{
\sum_{\ell=1}^{m}q^\ell\theta_{j-\ell}.
}
\end{aligned}
\]

This is the exact finite-stage phase ledger.

---

## 3. Existing Type-I bounds recovered

Because

\[
\theta_-\le\theta_k\le\theta_+,
\]

we have

\[
\theta_-\sum_{\ell=1}^{m}q^\ell
\le
a_{j,m}
\le
\theta_+\sum_{\ell=1}^{m}q^\ell.
\]

Thus

\[
\boxed{
a_{j,m}\asymp q^m,}
\]

which recovers the previously used checkpoint estimate

\[
c_-q^m\le a_{j,m}\le c_+q^m.
\]

This estimate is enough for the bounded similarity-position and nonvanishing-vorticity conclusions of M5-194L.

But it is not enough for a fixed similarity-time period.

---

## 4. Exact similarity phase gap

Define the checkpoint similarity phase

\[
s_{j,m}:=-\log a_{j,m}.
\]

The gap from checkpoint `m` to `m+1` is

\[
\boxed{
S_{j,m}
:=s_{j,m}-s_{j,m+1}
=
\log\frac{a_{j,m+1}}{a_{j,m}}>0.
}
\]

Since

\[
a_{j,m+1}
=a_{j,m}+q^{m+1}\theta_{j-m-1},
\]

we obtain

\[
\boxed{
S_{j,m}
=
\log\left(
1+
\frac{q^{m+1}\theta_{j-m-1}}{a_{j,m}}
\right).
}
\]

Therefore the actual similarity phase gap depends on the recent backward stage-duration profile.

It is not determined by `q` alone.

---

## 5. Constant-duration cross-check

If, as a model case,

\[
\theta_k\equiv\theta,
\]

then

\[
a_{j,m}
=\theta\sum_{\ell=1}^{m}q^\ell
=\theta\frac{q(q^m-1)}{q-1}.
\]

Hence

\[
\frac{a_{j,m+1}}{a_{j,m}}
=
\frac{q^{m+1}-1}{q^m-1}
\longrightarrow q.
\]

Thus

\[
\boxed{S_{j,m}\to\log q}
\]

only asymptotically in this stationary-duration model.

Even here the finite-checkpoint gap is not exactly `log q`.

This cross-check shows why the distinction is not merely technical.

---

## 6. Bounded but nonconvergent durations

Suppose only

\[
\theta_-\le\theta_k\le\theta_+.
\]

Then `a_{j,m}` remains comparable to `q^m`, so `S_{j,m}` stays in a bounded positive range after excluding a finite initial segment.

But boundedness of `theta_k` does **not** imply

\[
S_{j,m}\to\log q
\]

or even convergence of `S_{j,m}` to any single number.

For example, a persistent alternating or recurrent sequence of dimensionless durations can generate a persistent modulation of the weighted sums `a_{j,m}` and hence of the checkpoint phase gaps.

Therefore

\[
\boxed{
\text{Type-I timing bounds}
\not\Rightarrow
\text{phase locking}.
}
\]

---

## 7. Correct DSS criterion

A periodic similarity alpha-limit with period `S_*` requires two logically distinct ingredients.

### P1 — phase locking

Along the selected checkpoint subsequence,

\[
\boxed{
S_m:=s_m-s_{m+1}\to S_*>0.
}
\]

For the DSS factor to coincide with the geometric first-hitting scale factor `lambda=sqrt(q)`, one additionally needs

\[
\boxed{S_*=\log q.}
\]

That equality is an extra conclusion, not a consequence of the spatial scale ledger alone.

### P2 — spacetime block recurrence

For every fixed compact cylinder,

\[
\boxed{
V(\xi,s_m+\sigma)
-
V(\xi,s_{m+1}+\sigma)
\to0
}
\]

in a topology strong enough to pass the Navier--Stokes equation and vorticity witness.

Only P1 plus P2 allow a translated alpha-limit `V_*` to satisfy

\[
\boxed{
V_*(\xi,\sigma+S_*)=V_*(\xi,\sigma).
}
\]

Thus

\[
\boxed{
\text{DSS candidate}
=
\text{phase locking}
+
\text{block recurrence}.
}
\]

---

## 8. Recurrence defect must include a variable shift

The correct block defect is therefore not initially tied to `log q`.

Define, for a fixed compact spacetime norm `X(R,T)`,

\[
\boxed{
\mathfrak R_m(R,T)
:=
\left\|
V(\cdot,s_m+\cdot)
-
V(\cdot,s_{m+1}+\cdot)
\right\|_{X(B_R\times[-T,T])}.
}
\]

Equivalently, using `S_m=s_m-s_{m+1}`,

\[
\boxed{
\mathfrak R_m(R,T)
=
\left\|
V(\cdot,s_m+\cdot)
-
V(\cdot,s_m-S_m+\cdot)
\right\|_X.
}
\]

Then the dynamic fork is

\[
\boxed{
\begin{cases}
S_m\to S_*,\ \mathfrak R_m(R,T)\to0
&\Rightarrow \text{periodic alpha-limit candidate},\\
S_m\text{ does not lock}
&\Rightarrow \text{phase-wandering defect},\\
S_m\to S_*\text{ but }\limsup\mathfrak R_m>0
&\Rightarrow \text{block-recurrence defect}.
\end{cases}
}
\]

The last two branches are both genuinely aperiodic, but they are different formed witnesses.

---

## 9. DSD significance

DSD requires the following channels to remain separate:

- spatial generation scale;
- physical stage duration;
- similarity phase;
- normalized spacetime block;
- periodic identity.

The invalid shortcut would be

\[
\boxed{
W_{j+1}/W_j=q
\Longrightarrow
S_m=\log q
\Longrightarrow
\text{DSS}.
}
\]

The corrected chain is

\[
\boxed{
W_{j+1}/W_j=q
\Longrightarrow
\lambda=\sqrt q\text{ is the natural DSS scale factor},
}
\]

but actual DSS requires an independent timing-and-block locking result.

---

## 10. Relation to external DSS Liouville results

Known nonexistence results for backward discretely/asymptotically discretely self-similar Navier--Stokes scenarios are formulated in terms of an actual periodic similarity profile and additional global integrability/decay hypotheses, commonly including critical `L^3` control.

The present first-hitting branch has not yet supplied either of the two missing upgrades:

1. exact/limiting periodicity in similarity time;
2. the global critical tail control required by the classical DSS Liouville theorem.

Therefore those external theorems remain a conditional endpoint, not something that can be invoked from the scale ratio alone.

---

## 11. Audit verdict

### PROVED

- exact checkpoint-time ledger
  \[
  a_{j,m}=\sum_{\ell=1}^{m}q^\ell\theta_{j-\ell};
  \]
- exact phase-gap formula
  \[
  S_{j,m}=\log(a_{j,m+1}/a_{j,m});
  \]
- Type-I stage bounds imply bounded/comparable checkpoint phases but not phase locking;
- the geometric factor `q` fixes a natural DSS scale factor but not the actual checkpoint period;
- phase wandering and block nonrecurrence are distinct finite witnesses.

### NOT YET PROVED

- `S_m -> S_*`;
- `S_*=log q`;
- block recurrence `R_m -> 0`;
- existence of a periodic/DSS alpha-limit;
- exclusion of a periodic alpha-limit in the current Morrey/critical-tail class;
- global regularity.

---

## 12. Next audit target

The next calculation should quantify the relation between phase-gap variation and the dimensionless stage-duration sequence.

A useful formed timing defect is

\[
\boxed{
\mathfrak P_m
:=|S_{m+1}-S_m|.
}
\]

Then test whether

\[
\sum_m\mathfrak P_m<\infty
\]

or another finite-variation condition follows from the existing first-hitting variance/projective ledger.

If yes, phase locking follows and the proof moves to the DSS block-recurrence gate.

If no, persistent phase wandering itself becomes the explicit aperiodic scaling defect that must be routed back to the existing H/T/finite-cost branches.
