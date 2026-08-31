# DSD M5-414 — Restart-coherence gap is bypassed by the intrinsic detached shell dichotomy

Date: 2026-08-31

Status: **THE M5-284 RESTART-COHERENCE FIREWALL REMAINS CORRECT AS A STATEMENT ABOUT LOCAL TRUNCATION, BUT IT IS NO LONGER A NECESSARY TERMINAL IN THE CURRENT MASTER ROUTE / M5-405--406 PROVIDE AN INTRINSIC DICHOTOMY FOR THE ACTUAL DETACHED ANCIENT SOLUTION: UNIFORM CRITICAL SHELL GRADIENT CONTROL DIRECTLY GIVES `u-c(t) in L^{3,infinity}` AND THE ALBRITTON--BARKER LIOUVILLE CONTRADICTION, WHILE FAILURE OF THAT SHELL CONTROL IS ALREADY CRITICAL THROUGHPUT H / IF LOCAL DETACHED COMPACTNESS ITSELF FAILS, M5-281, M5-400--410 AND THE PRESSURE/LOCALIZATION GATES ROUTE THE FAILURE TO AMBIENT/REMOTE/SHELL/DERIVATIVE THROUGHPUT / THEREFORE A SEPARATE BOUNDED RESTART-REALIZATION TERMINAL IS NOT REQUIRED TO CONTINUE THE MASTER PROOF TREE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-413 retained

\[
T_{real}^{analytic}
=
T_{pressure/localization/restart\ coherence}
\]

as the only non-throughput terminal.

This was deliberately conservative.

The main historical reason was M5-284, which correctly proved that a local solenoidal truncation of a detached satellite does **not** automatically evolve coherently with the actual satellite solution and that Barker--Seregin--Sverak stability requires a uniform global critical bound on the restart data.

Since M5-284, however, the repository has obtained M5-405--406.

Those later results change the logical necessity of the restart construction.

---

## 2. What M5-284 actually forbids

At a detached satellite time, choose a cutoff radius `R` and define a solenoidal compactly supported datum

\[
a_R=\chi_Ru-b_R.
\]

Let `v_R` be a global weak-`L^{3,infinity}` solution launched from `a_R`.

M5-284 correctly rejected the inference

\[
\boxed{
\text{local smoothness of }u
\Longrightarrow
v_R\to u\text{ coherently as }R\to\infty.
}
\]

The far pressure/harmonic field, material flux through the annulus, and localization correction can prevent such a conclusion.

This statement remains valid.

The present note does not claim that restart coherence has now been proved.

---

## 3. M5-405 gives an intrinsic alternative which does not use restart coherence

For the **actual detached ancient solution** `u`, M5-405 defines the critical shell derivative quantity

\[
E_1(R,t)
:=
R\int_{A_R}|\nabla u(x,t)|^2dx.
\]

If

\[
\boxed{
\sup_{t<0}\sup_{R>0}E_1(R,t)<\infty,
}
\]

then the dyadic distribution-function argument gives

\[
\boxed{
\nabla u(t)
\in L^{3/2,\infty}
}
\]

uniformly in `t`.

Lorentz--Sobolev then gives, for a spatial constant velocity `c(t)`,

\[
\boxed{
u-c(t)
\in L^{3,\infty}.
}
\]

M5-406 removes the time-dependent constant by an exact translating-frame transformation.

Thus the **actual satellite**, not a truncated comparison solution, belongs to the uniform weak-critical class.

No restart-coherence theorem is used.

---

## 4. The bounded-shell branch closes directly

On the M5-281 point-picked detached class, vorticity is bounded on every compact negative-time slab and standard local regularity gives the mild ancient class after the translating gauge is fixed.

The uniform `L^{3,infinity}` bound passes to the terminal trace, and

\[
L^{3,\infty}
\hookrightarrow
\dot B^{-1}_{\infty,\infty}
\]

with the distributional scaling property needed for the Albritton--Barker subspace `mathbb B`.

Therefore

\[
\boxed{
\sup_{t,R}E_1(R,t)<\infty
\Longrightarrow
u\equiv0,
}
\]

contradicting the detached nonzero vorticity mark.

Hence a nontrivial detached satellite cannot live on the uniformly bounded-shell corridor.

---

## 5. Failure of the shell bound is already throughput H

If the intrinsic detached shell condition fails, then

\[
\boxed{
\sup_{t,R}
R\int_{A_R}|\nabla u|^2
=\infty.
}
\]

This is exactly the shell-H side of M5-405.

M5-280 already routes large shell derivative/Campanato activity to the remote-satellite frontier unless a boundary/localization event is large.

M5-408--413 subsequently absorb the remote and formed-interface branches into critical throughput.

Therefore

\[
\boxed{
A_{detached}^{nontrivial}
\Longrightarrow
H_{throughput}^{crit}.
}

The restart gap is bypassed by an intrinsic property of the detached solution.

---

## 6. What if detached local compactness itself fails?

M5-281 separates the point-picked remote branch according to local velocity-gradient/ambient-strain compactness.

If the local ambient strain remains bounded, a smooth detached ancient solution is extracted and Sections 3--5 apply.

If local ambient/full strain loses compactness, M5-402 routes it to another remote active scale.

M5-409--410 then show that indefinite remote recursion requires fresh critical phase-space throughput or local/interface H.

Thus

\[
\boxed{
\text{failure to extract a detached compact limit through ambient strain}
\Longrightarrow
H_{throughput}^{crit}.
}

A separate realization terminal is not needed for this failure mode.

---

## 7. Large localization defects are already critical throughput

The repository's explicit cutoff/Bogovskii audits give finite-radius alternatives of the form

\[
\boxed{
\text{large cutoff defect}
\Longrightarrow
\text{annular derivative fraction}
\lor
\text{annular vorticity-mass leakage}.
}
\]

The former is shell/frequency H.

The latter is formed spatial leakage and, after M5-395--412, routes to critical carrier/remote/shell throughput rather than an independent export terminal.

Hence a localization defect large enough to destroy the retained compactness estimates is already included in

\[
H_{throughput}^{crit}.
\]

---

## 8. Large pressure defects are also routed

Under parent Morrey plus Type-I/derivative control, the existing pressure audit bounds both pressure oscillation and pressure gradient at their natural critical size.

Under the W1 velocity cap, M5-266 further routes a substantial pressure-force payer to a global H1/strain reservoir.

Therefore a pressure defect that **escalates** enough to destroy local compactness requires failure of the shell/Morrey/derivative corridor, which is already critical throughput/remote activity.

The only historical concern left would be a bounded but nonvanishing far harmonic/pressure field.

But once a detached actual solution is extracted, such a field is part of that actual solution and is tested by the intrinsic shell dichotomy of M5-405.

- if it remains critical-shell bounded, weak-L3 Liouville applies;
- if it produces affine/noncritical growth, M5-403--405 give palinstrophy/enstrophy/shell H.

Thus it does not require a separate restart comparison solution.

---

## 9. Why the old restart issue is genuinely bypassed, not secretly assumed

The new logical route is

\[
\boxed{
\text{remote point-pick}
\to
\begin{cases}
\text{local compactness}
\to
\text{actual detached ancient solution}
\to
\text{intrinsic shell dichotomy},\\
\text{compactness failure}
\to
H_{throughput}^{crit}.
\end{cases}
}
\]

It is **not**

\[
\text{truncate}
\to
\text{assume comparison evolution matches}
\to
\text{weak-L3 stability}.
\]

Therefore M5-284's forbidden inference is never used.

The proof architecture has gone around the gap rather than filling it.

---

## 10. Remaining role of restart coherence

A genuine restart theorem would still be mathematically useful.

It could provide an alternative route to the same Liouville endpoint and may be valuable for independent publication or robustness.

But it is no longer necessary as a **terminal branch** in the present proof tree.

Thus the status of M5-284 changes from

\[
\text{master obstruction}
\]

to

\[
\boxed{
\text{valid firewall for one discarded proof route}.
}
\]

---

## 11. Updated realization verdict

Combining Sections 3--9,

\[
\boxed{
T_{real}^{analytic}
\Longrightarrow
H_{throughput}^{crit}
\lor
\bot,
}

where `bot` denotes the weak-L3 ancient Liouville contradiction on the bounded-shell detached branch.

Therefore `T_real^analytic` does not need to remain an independent unresolved terminal.

---

## 12. Audit firewall

- Restart coherence itself has **not** been proved.
- Barker--Seregin--Sverak stability is not applied to arbitrary local truncations.
- Pressure compactness is not assumed without a local boundedness route.
- The M5-405 shell condition is tested on the actual detached solution after extraction.
- If the shell condition fails, that failure is retained as H rather than silently discarded.
- If local extraction fails, the corresponding ambient/localization failure is retained as H throughput.

---

## 13. Consequence for the master frontier

M5-413 gave

\[
\text{singular tower}
\Longrightarrow
H_{throughput}^{crit}
\lor
T_{real}^{analytic}.
\]

The present bypass yields

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{throughput}^{crit}.
}

This is a major proof-tree consolidation.

It is **not** global regularity, because `H_throughput^crit` is a scale-critical blow-up mechanism and no finite global budget or rigidity theorem has yet excluded it.

---

## 14. Next target

The proof tree now has one surviving master class rather than several named geometric terminals.

The next task is therefore not more branch naming.

It is to study the evolution of the common critical throughput itself:

\[
\boxed{
H_{throughput}^{crit}.
}

The most concrete current scalar/functional representatives are

\[
\mathfrak N_{crit}(t)
\]

and

\[
\|u(t)\|_{\dot H^{1/2}}^2,
\]

supplemented by distributed shell/frequency actions when a coherent carrier atom is not yet extractable.

One must find either

- a strict efficiency gap for creation of new critical atoms;
- a critical-element rigidity theorem;
- a non-reuse/throughput Carleson law;
- or an evolution inequality strengthened by the first-hitting material/source genealogy.

---

## 15. Audit verdict

### BYPASSED, NOT PROVED

\[
\boxed{\text{restart coherence}.}
\]

The old gap remains a correct warning but is no longer required in the main route.

### REMOVED AS INDEPENDENT TERMINAL

\[
\boxed{T_{real}^{analytic}.}
\]

### SINGLE CURRENT MASTER FRONTIER

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{throughput}^{crit}.
}

### STILL OPEN

- exclusion/rigidity of the critical throughput class;
- a global or critical-element theorem using the extra genealogy/source structure;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]