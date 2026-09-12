# DSD M19-092 — One-dimensional center would reduce aperiodic recurrence to the still-open DSS log-periodic survivor, not close the critical branch

Date: 2026-09-12

Status: **M19 AUDIT-CORRECTION INSIDE THE ACTIVE CALCULATION PHASE / THE CENTER-RIGIDITY TARGET REMOVES APERIODIC RECURRENCE BUT DOES NOT BY ITSELF REMOVE EXACT DSS / M5-566 EXPLICITLY LEFT A NONZERO LOG-PERIODIC ONE-OVER-R DSS SURVIVOR / GENERAL BACKWARD DSS EXCLUSION IS NOT AVAILABLE FROM THE RETAINED EXTERNAL THEORY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Reason for this correction

M19-089 correctly observed that if, after rotational quotient,

\[
E_q^c=\operatorname{span}\{\partial_\theta U\},
\]

then a genuinely aperiodic recurrent factor cannot persist on a one-dimensional smooth center flow.

However this does **not** imply that the entire weak-critical branch is closed.

The remaining recurrent orbit may be exactly periodic in similarity time.

That is the backward discretely self-similar (DSS) branch.

---

## 2. Historical M5-566 status

M5-566 did not eliminate arbitrary DSS.

It proved that any unresolved exact DSS survivor on the passive spectator lane must carry a nonzero log-periodic critical tail

\[
\boxed{
U(y,\theta)
=\frac1{|y|}
 a\left(
\log|y|-\frac\theta2,
\frac y{|y|}
\right)
+O(|y|^{-3}),
}
\]

with

\[
\boxed{
a(s+\log\lambda,\omega)=a(s,\omega),}
\]

and

\[
\boxed{a\not\equiv0.}
\]

If `a=0`, the tail becomes subcritical and the old global-`L3` Liouville route applies. Therefore the unresolved DSS hard core is exactly the nonzero periodic critical tail.

---

## 3. Correct logical routing

The correct center/factor reduction is

\[
\boxed{
E^c_{extra}=0
\Longrightarrow
\text{stationary or exact periodic/DSS recurrent survivor}.
}
\]

The stationary backward self-similar branch has stronger Liouville theory available under the retained integrability hypotheses.

The exact DSS branch is different.

Therefore

\[
\boxed{
E^c_{extra}=0
\not\Longrightarrow
\text{critical branch closed}.
}
\]

Instead,

\[
\boxed{
E^c_{extra}=0
\Longrightarrow
\text{aperiodic branch removed, DSS branch remains}.
}
\]

---

## 4. External-theory boundary

Existing literature contains partial exclusion results for backward DSS singularities. In particular, Chae--Wolf (2017, DOI `10.1080/03605302.2017.1358275`) removes the singularity when the DSS scaling parameter `lambda` is sufficiently close to one, under the hypotheses of that theorem.

The same work does not claim removal for arbitrary `lambda`.

Accordingly M19 must not use

\[
\text{DSS}\Rightarrow0
\]

as a general theorem.

Applicability of the near-one result to any specific M19 subbranch must be checked hypothesis-by-hypothesis before use.

---

## 5. Revised analytic frontier

The current weak-critical analytic frontier therefore has two nested tasks.

### Task A — aperiodic center rigidity

Prove

\[
\boxed{
E^c_{extra}=0.
}
\]

M19-087--091 reduce this to the finite-dimensional interior quarter-gap compensation problem.

### Task B — exact DSS critical-tail rigidity

After Task A, exclude or otherwise close the remaining nonzero log-periodic amplitude

\[
\boxed{
a(s+\log\lambda)=a(s),\qquad a\neq0.}
\]

for arbitrary admissible `lambda`, or reduce it to a previously certified exit.

Thus the analytic closure has not yet become a single theorem.

---

## 6. Why invariant-mean generalization does not automatically solve DSS

One might try to replace exact period averaging by an invariant mean on the recurrent hull.

But M5-566 already shows that exact periodicity itself is compatible with a nonzero leading `1/r` amplitude at the current level of tail equations.

Therefore any invariant-mean extension of the same identities cannot by itself be expected to kill the aperiodic branch unless it uses additional interior information.

The obstacle is not merely the lack of a time average.

It is the existence of the critical log-periodic tail itself.

---

## 7. Updated proof-tree meaning

The correct picture is

\[
\boxed{
\text{weak-critical recurrent survivor}
\Longrightarrow
\begin{cases}
\text{aperiodic center/factor survivor},\\
\text{exact DSS log-periodic survivor},\\
\text{stationary branch}.
\end{cases}
}
\]

The stationary branch is the most rigid.

The two live difficult branches are presently

\[
\boxed{
\mathcal T_{extra-center}
}
\]

and

\[
\boxed{
\mathcal T_{DSS}^{critical}.
}
\]

---

## 8. Firewall

The following implication is prohibited:

\[
\boxed{
\text{one-dimensional quotient center}
\not\Rightarrow
\text{global regularity}.
}
\]

The valid implication is only

\[
\boxed{
\text{one-dimensional quotient center}
\Rightarrow
\text{no genuinely aperiodic recurrent factor}.
}
\]

Exact periodic/DSS recurrence must then be handled separately.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
