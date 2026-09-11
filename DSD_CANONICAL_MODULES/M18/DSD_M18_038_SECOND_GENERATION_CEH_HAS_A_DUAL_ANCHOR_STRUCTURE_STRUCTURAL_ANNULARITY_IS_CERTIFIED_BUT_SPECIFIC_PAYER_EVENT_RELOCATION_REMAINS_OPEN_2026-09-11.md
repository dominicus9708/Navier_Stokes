# M18-038 — Second-generation CE-H has a dual-anchor structure: structural annularity is certified, but specific payer-event relocation remains open

**Date:** 2026-09-11  
**Status:** AUTHORITATIVE DUAL-ANCHOR GENEALOGY AUDIT / STRUCTURAL-ANNULAR CERTIFICATE / EVENT-RELOCATION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-037 reduced the live genealogy issue to ANNULAR-LOC: a late-M18 payer must be placed inside a fixed normalized annular interval in order to use the already-certified bounded-overlap ancestry ledgers.

The upstream second-generation extraction M5-478 and the CE-H globalization step M5-599 show that two logically different anchors are present:

1. a nontrivial interior carrier at normalized time \(s=-1\);
2. a terminal boundary \(s=0\) probing a spatial critical tail.

This module separates those anchors and audits what CE-H analyticity actually transports between them.

## 2. Interior nontriviality anchor from M5-478

M5-478 selects backward first-hitting times

\[
\tau_m\to-\infty,
\qquad
T_m=-\tau_m,
\qquad
R_m=\sqrt{T_m},
\]

with geometric growth

\[
T_m\asymp q^m.
\]

The second-generation blow-down is

\[
V^{(m)}(y,s)=R_mV(R_my,T_ms),
\]

\[
\Omega^{(m)}(y,s)=R_m^2\Omega(R_my,T_ms).
\]

The old first-hitting carrier appears at

\[
\boxed{s=-1}
\]

with fixed nontrivial local enstrophy:

\[
\boxed{
\int_{B_{\rho_0}(y_*)}
|\Omega^{(m)}(y,-1)|^2dy
\ge c_0>0.
}
\]

After passage to the second-generation ancient limit,

\[
\boxed{
\int_{B_{\rho_0}(y_*)}
|\mathcal\Omega(y,-1)|^2dy
\ge c_0>0.
}
\]

Thus the extracted ancient cell has an intrinsic interior nontriviality witness at a time a fixed distance from the terminal boundary.

## 3. Terminal tail anchor from M5-478

At normalized terminal time \(s=0\), formally

\[
V^{(m)}(y,0)=R_mV(R_my,0),
\]

\[
\Omega^{(m)}(y,0)=R_m^2\Omega(R_my,0).
\]

This anchor has a different role: it probes the spatial critical tail of the first-generation marked ancient element at physical radius \(R_m\).

M5-478 explicitly does not infer a terminal trace from compactness on \(s<0\) alone.

Therefore

\[
\boxed{
\text{interior carrier at }s=-1
\neq
\text{terminal critical-tail probe at }s=0.
}
\]

The two anchors must not be used interchangeably in ancestry accounting.

## 4. CE-H structural globalization from M5-599

On the CE-H branch, M5-599 starts from production-linked open-ball equalities and, subject to its stated spatial/time analyticity theorems, obtains

\[
\boxed{
\omega\times S\omega\equiv0,
\qquad
\omega\times\Delta\omega\equiv0
}
\]

throughout the connected ancient spacetime interval.

Thus, on \(\{\omega\neq0\}\),

\[
\boxed{
S\omega=\sigma\omega,
\qquad
\Delta\omega=\kappa\omega
}
\]

for every negative time in the ancient interval.

Accordingly, once the CE-H branch is certified and the analyticity dependency is accepted, the **structural CE-H equations themselves are available at and around \(s=-1\)**.

## 5. STRUCT-ANNULAR certificate

Define

\[
\boxed{\text{STRUCT-ANNULAR}}
\]

to mean that there exists a fixed interval

\[
I_{str}=[-b,-a],
\qquad
0<a<1<b<\infty,
\]

containing \(s=-1\) in its interior such that:

1. the second-generation ancient solution is smooth on \(I_{str}\);
2. the global CE-H double-eigenline identities hold there;
3. the nontrivial carrier remains part of the same ancient element;
4. the domain is the same whole-space branch.

M5-478 plus M5-599 certify STRUCT-ANNULAR, subject to the explicit analyticity dependency of M5-599.

This is stronger than merely knowing that CE-H holds near a terminal event.

## 6. Structural annularity does not relocate a payer event

A late M18 payer may be defined by an additional condition such as:

\[
F(s_*,t)\le\theta J(t),
\]

\[
P(t)\ge p_*,
\]

\[
H(t)\ge h_*,
\]

\[
\mathfrak C_I\ge C_*,
\]

or another concentration threshold.

Time analyticity of the CE-H identities does **not** imply that any of these inequalities, maxima, threshold crossings, or concentration events occur at \(s=-1\) or on every annular interval.

Therefore

\[
\boxed{
\text{STRUCT-ANNULAR}
\not\Rightarrow
\text{EVENT-ANNULAR}.
}
\]

This is the central firewall of M18-038.

## 7. EVENT-ANNULAR certificate

Define

\[
\boxed{\text{EVENT-ANNULAR}}
\]

to mean that for the specific payer/concentration event being used, there is a fixed annular interval

\[
I=[-b,-a]\Subset(-\infty,0)
\]

independent of the record such that:

1. the event witness lies in an interior subinterval \(I_0\Subset I\);
2. every time-thickening/active-set payment remains inside \(I\);
3. the same CE-H/domain hypotheses remain valid there.

EVENT-ANNULAR is exactly the event-specific form of ANNULAR-LOC from M18-037.

## 8. Four-way placement classification

Every late CE-H payer should henceforth be classified as one of:

### A. Interior-carrier inherited

Its defining witness is attached to the M5-478 first-hitting carrier or another structure already known to occur near \(s=-1\).

Then EVENT-ANNULAR may be directly provable.

### B. Time-recurrent interior

A recurrence/density theorem produces the same quantitative event on a fixed compact subinterval of \(( -\infty,0)\).

Then EVENT-ANNULAR follows after a fixed time translation or subsequence selection.

### C. Terminal-only

The event is only known at or arbitrarily close to \(s=0\).

Then cross-record counting remains endpoint-nested unless an independent nonreuse certificate exists.

### D. Record-local but unplaced

The event is known somewhere in a record window but no uniform distance from \(s=0\) is certified.

Then the ancestry ledger cannot yet be invoked across records.

## 9. Why the M5-478 carrier matters

The presence of a nontrivial \(s=-1\) carrier means the second-generation genealogy does **not** intrinsically depend on terminal-time nontriviality.

Hence one should prefer local arguments that can be attached to the interior carrier or to a fixed compact neighborhood of it.

This has two advantages:

1. parent-time windows become annular and bounded-overlap automatically;
2. terminal-trace/backward-uniqueness hypotheses are avoided.

Thus a future local CE-H theorem that is valid wherever the ancient solution is nontrivial may be substantially more useful than one formulated only at the terminal tail.

## 10. What cannot be transported from s=0 to s=-1 automatically

The following do not propagate backward merely from smoothness or analyticity:

- a lower bound on a nonlinear norm at one time;
- a flux-loss ratio threshold;
- a local maximum or first-hitting property;
- a high-conductance collar;
- a spike height;
- a sign-separated coefficient distribution;
- a selected material interface label unless its transport is certified.

Analyticity propagates identities, not arbitrary inequalities or extremal events.

## 11. Relation to M5-598 same-event firewall

M5-598 showed that recurrence of the same unsigned similarity event is not automatically an additive physical cost.

M18-038 is consistent with that result:

- STRUCT-ANNULAR says the rigid CE-H equations are available on a fixed interior window;
- EVENT-ANNULAR requires a quantitative event to occur there;
- ancestry multiplicity still requires parent nonreuse/bounded overlap.

Thus no new charge is created merely by observing the same global CE-H structure at multiple normalized times.

## 12. Updated genealogy chain

The late CE-H ancestry chain is now

\[
\boxed{
\begin{aligned}
\text{second-generation record extraction}
&\Longrightarrow
\text{interior nontrivial carrier at }s=-1\\
&\Longrightarrow
\text{STRUCT-ANNULAR CE-H}\n\\
&\stackrel{?}{\Longrightarrow}
\text{EVENT-ANNULAR for selected payer}\\
&\Longrightarrow
\text{annular-safe }P/H/D3/\text{first-jet ledger}\\
&\Longrightarrow
\text{exact ancestry threshold test}.
\end{aligned}
}
\]

The question mark is now a very specific event-relocation/recurrence bridge.

## 13. Audit verdict

### Certified

1. M5-478 supplies an interior annular nontriviality anchor at \(s=-1\).
2. The terminal \(s=0\) anchor has a separate spatial-tail role and must not be conflated with the interior carrier.
3. Subject to M5-599's analyticity theorem, CE-H structural identities hold on a fixed annular interval around \(s=-1\).
4. Structural annularity does not imply a specific payer event is annularly located.
5. The genealogy gap is therefore event-specific, not a failure of the core derivative ledgers or CE-H structural availability.

### Not certified

1. EVENT-ANNULAR for every M18 payer/concentration endpoint.
2. Backward relocation of a terminal-only inequality event.
3. Recurrence of all quantitative late-M18 events near \(s=-1\).
4. ROOT-CERT/non-CE-H closure.
5. Global 3D Navier--Stokes regularity.

## 14. Next target

M18-039 should inspect the production-event architecture M5-589--M5-597.

The question is whether the positive-measure/recurrent production events that select CE-H already occur with a representation-safe density on fixed compact normalized time intervals, and whether any of the late M18 quantitative payers can be tied to those production events.

If yes, EVENT-ANNULAR may be obtained for a useful subclass. If not, terminal and interior event economies must remain separate.