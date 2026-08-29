# DSD M5-194N — Multi-Generation DSS Recurrence and Stage-Duration Cycle Audit

Date: 2026-08-29

Parent: `DSD_M5_194M_CHECKPOINT_PHASE_GAP_AND_DSS_LOCKING_FIREWALL_2026-08-29.md`

Status: **RECURRENCE-GATE CORRECTION / EXISTING STAGE LOWER AND UPPER BOUNDS CONTROL EACH DIMENSIONLESS DURATION BUT DO NOT FORCE ITS VARIATION TO VANISH / ONE-GENERATION PHASE LOCKING IS THEREFORE NOT DERIVED / PERIODIC OR RECURRENT STAGE-DURATION PATTERNS CAN FAIL ONE-STEP LOCKING WHILE PRODUCING `p`-GENERATION PHASE LOCKING / THE CORRECT DSS AUDIT MUST TEST EVERY FINITE GENERATION GAP `p`, NOT ONLY CONSECUTIVE CHECKPOINTS / GLOBAL REGULARITY UNPROVED.**

---

## 1. What the existing stage ledgers actually give

Let

\[
L_j=\int_{t_j}^{t_{j+1}}\overline W(t)\,dt
\]

be the dynamic stage clock and

\[
\theta_j:=W_j(t_{j+1}-t_j)
\]

the dimensionless physical stage duration.

During the first-hitting stage,

\[
W_j\le \overline W(t)\le qW_j.
\]

Therefore

\[
\boxed{
\theta_j\le L_j\le q\theta_j,
}
\]

or equivalently

\[
\boxed{
\frac{L_j}{q}\le\theta_j\le L_j.
}
\]

The repository has already derived, on the pure bounded-strain/low-turnover corridor,

\[
L_j\ge L_{-,0}>0
\]

and

\[
L_j\le L_{var,+}<\infty.
\]

Consequently

\[
\boxed{
0<\theta_-\le\theta_j\le\theta_+<\infty.
}
\]

This is sufficient for Type-I timing comparability.

But the reviewed ledgers do **not** supply any of

\[
\theta_{j+1}-\theta_j\to0,
\]

\[
\sum_j|\theta_{j+1}-\theta_j|<\infty,
\]

or

\[
\theta_j\to\theta_*.
\]

Thus one-generation phase locking cannot be inferred from the existing scalar stage bounds.

---

## 2. Bounded stage clocks do not imply a fixed one-step phase

M5-194M established

\[
a_{j,m}
=\sum_{\ell=1}^{m}q^\ell\theta_{j-\ell}
\]

and

\[
S_{j,m}^{(1)}
:=s_{j,m}-s_{j,m+1}
=\log\frac{a_{j,m+1}}{a_{j,m}}.
\]

If `theta_j` is merely bounded, the weighted sum remains `~q^m`, but its normalized coefficient can depend on the backward generation phase.

Hence

\[
\boxed{
\theta_-\le\theta_j\le\theta_+
\not\Rightarrow
S_{j,m}^{(1)}\to\log q.
}
\]

This is a strict logical firewall.

---

## 3. Explicit two-cycle timing test

Take an abstract admissible duration pattern

\[
\theta_{2k}=a,
\qquad
\theta_{2k+1}=b,
\qquad
0<a,b<\infty,
\qquad a\ne b.
\]

This satisfies the same positive lower and finite upper stage-duration bounds.

Because the checkpoint sum is geometrically weighted, for fixed parity of `m`

\[
q^{-m}a_{j,m}
\]

converges to a positive parity-dependent constant.

Write these limits as

\[
C_0>0,
\qquad
C_1>0.
\]

Then asymptotically

\[
a_{j,2n}\sim C_0q^{2n},
\]

\[
a_{j,2n+1}\sim C_1q^{2n+1}.
\]

Therefore the one-step ratios approach two generally different values:

\[
\frac{a_{j,2n+1}}{a_{j,2n}}
\to q\frac{C_1}{C_0},
\]

\[
\frac{a_{j,2n+2}}{a_{j,2n+1}}
\to q\frac{C_0}{C_1}.
\]

Thus the one-step phase gaps can alternate instead of converging.

But multiplying the two ratios gives

\[
\frac{a_{j,2n+2}}{a_{j,2n}}
\to q^2.
\]

Hence the two-generation similarity shift satisfies

\[
\boxed{
S_{j,2n}^{(2)}
:=
\log\frac{a_{j,2n+2}}{a_{j,2n}}
\to2\log q.
}
\]

So a failure of one-generation phase locking need not be genuinely aperiodic.

It may represent a two-generation cycle.

---

## 4. General `p`-periodic duration pattern

Suppose the backward stage-duration sequence is asymptotically `p`-periodic:

\[
\theta_{k+p}-\theta_k\to0
\]

along the relevant backward tail.

For each residue class `r mod p`, geometric summation yields a positive coefficient `C_r` such that

\[
a_{j,m}
\sim
C_r q^m
\qquad (m\equiv r\pmod p).
\]

After `p` generations the residue class is unchanged, so the coefficient cancels:

\[
\boxed{
\frac{a_{j,m+p}}{a_{j,m}}
\to q^p.
}
\]

Therefore

\[
\boxed{
S_m^{(p)}
:=s_m-s_{m+p}
=
\log\frac{a_{m+p}}{a_m}
\to p\log q.
}
\]

This is exactly the similarity-time period associated with the multi-generation scale factor

\[
\boxed{
\lambda_p=q^{p/2}.
}
\]

Indeed

\[
2\log\lambda_p=p\log q.
\]

---

## 5. Correct multi-generation recurrence defect

For every positive integer `p`, define

\[
\boxed{
S_m^{(p)}:=s_m-s_{m+p}>0
}
\]

and on a fixed compact cylinder

\[
\boxed{
\mathfrak R_m^{(p)}(R,T)
:=
\left\|
V(\cdot,s_m+\cdot)
-
V(\cdot,s_{m+p}+\cdot)
\right\|_{X(B_R\times[-T,T])}.
}
\]

A `p`-generation periodic checkpoint alpha-limit requires

\[
\boxed{
S_m^{(p)}\to S_p>0
}
\]

and

\[
\boxed{
\mathfrak R_m^{(p)}(R,T)\to0
}
\]

for every fixed `R,T` in the chosen local topology.

Then any common translated alpha-limit obeys

\[
\boxed{
V_*(\xi,\sigma+S_p)=V_*(\xi,\sigma).
}
\]

If the timing pattern is asymptotically `p`-periodic in generation number, the natural value is

\[
S_p=p\log q.
\]

---

## 6. DSS scale need not be one-generation scale

A periodic similarity profile with period `S_p` corresponds to a physical DSS factor

\[
\boxed{
\lambda_*=e^{S_p/2}.
}
\]

Therefore the proof tree must not require the minimal DSS factor to equal `sqrt(q)`.

The first-hitting discretization uses an arbitrary fixed amplification threshold `q>1`. The physical solution, if DSS, can recur only after several threshold crossings.

Thus

\[
\boxed{
\text{one-generation nonrecurrence}
\not\Rightarrow
\text{non-DSS}.
}
\]

A finite-generation cycle must also be excluded.

---

## 7. Correct dynamic trichotomy

The checkpoint dynamics should now be partitioned as follows.

### D — finite-generation periodic recurrence

There exists a finite `p>=1` such that

\[
S_m^{(p)}\to S_p
\]

and

\[
\mathfrak R_m^{(p)}\to0.
\]

This yields a nonzero periodic similarity alpha-limit and therefore a DSS candidate.

### A — compact but genuinely aperiodic alpha-dynamics

For every fixed finite `p`, either the `p`-step phase fails to lock or the `p`-step block recurrence defect stays positive, while translated blocks remain locally compact.

### E — compactness escape

The translated checkpoint blocks fail the local compactness or local-energy/pressure passage required to form an alpha-limit.

Thus

\[
\boxed{
\text{dynamic survivor}
=D\lor A\lor E.
}
\]

The stationary branch was already excluded in M5-194L.

---

## 8. Interaction with the existing variance ledger

The tightness-radius variance calculation gives an **upper bound on each stage length** and routes threshold failure to `T_var/bdry`.

The first-hitting strain-action calculation gives a **lower bound on each stage length**.

Neither result currently compares consecutive stage durations strongly enough to prove finite variation or asymptotic periodicity.

Therefore the correct audit verdict is:

\[
\boxed{
\text{stage compactness in a bounded interval}
\not\Rightarrow
\text{stage-time recurrence}.
}
\]

Any future claim of phase locking must use an additional dynamical relation, not the present scalar bounds alone.

---

## 9. External theorem boundary

A genuine periodic profile of the backward Leray similarity equation is equivalent to a backward DSS Navier--Stokes field, with period and scale related by

\[
S=2\log\lambda.
\]

Known DSS/nonexistence theorems generally require additional global integrability or decay assumptions. The current repository's nontrivial ancient survivor is already forced toward a critical global tail, so periodicity alone would not yet close the branch.

The present audit therefore prepares the correct object for the next Liouville comparison without overclaiming applicability.

---

## 10. DSD verdict

### CLOSED

- deriving stage-duration convergence from only the existing `L_- / L_+`-type bounds;
- identifying failure of one-step recurrence with genuine aperiodicity;
- restricting the DSS audit to the one-generation factor `sqrt(q)`.

### OPEN

- finite `p` recurrence for any `p>=1`;
- exclusion of all nonzero periodic similarity alpha-limits in the inherited Morrey/critical-tail class;
- compact genuinely aperiodic alpha-dynamics;
- routing persistent phase/block defects into the existing finite H/T ledgers;
- global regularity.

---

## 11. Next audit target

The next highest-value step is to study the **periodic alpha-limit branch without assuming global `L^3` tightness**.

For a periodic profile `V_*(xi,s)` with period `S`, retain the inherited bounds

\[
\sup_s\|\Omega_{V_*}(s)\|_\infty<\infty,
\]

and the centered critical Morrey energy control.

Then determine whether periodicity itself upgrades the critical tail enough to enter an existing DSS Liouville class, or whether a nonzero periodic survivor necessarily carries a quantitatively recurrent annular `L^3`/energy tail.

If the latter, that annular recurrent tail becomes a concrete turnover/export witness rather than an abstract failure of global `L^3` integrability.
