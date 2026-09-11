# M18-053 — Root leverage audit prioritizes ancestry conversion but blocks the false forward-stage-to-positive-R-record shortcut

**Date:** 2026-09-11  
**Status:** ROOT-PRIORITY AUDIT / ANCESTRY-DIRECTION FIREWALL / NEXT-LINE SELECTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

After M18-052 the active upstream classification has three principal root complexes:

\[
\boxed{
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC}.
}
\]

The next calculation should be chosen by leverage, not by how deep one branch already is.

This module compares the three roots using:

1. existing finite parent budget;
2. guaranteed normalized witness;
3. scaling favorability;
4. external rigidity input;
5. reduction to a precise missing inequality or map.

It also corrects a tempting ancestry shortcut before selecting \(\mathcal R_{AC}\) as the next primary line.

## 2. Root R-remote

\[
\boxed{\mathcal R_{remote}:=\mathcal R_{remote/II/historical}.}
\]

### Available structure

A strong remote source at distance

\[
R_j=K_jr_j,
\qquad K_j\to\infty,
\]

has the canonical Euler scale

\[
U_j^E=\frac{\nu K_j^2}{R_j},
\qquad
T_j^E=\frac{R_j}{U_j^E}=\frac{r_j^2}{\nu},
\]

and vanishing normalized viscosity

\[
\boxed{\varepsilon_j=K_j^{-2}\to0.}
\]

The Euler-scaled vorticity remains order one and a nonzero local oscillation witness survives.

Thus the root splits into

\[
\boxed{
E_{ancient}^{Euler,compact}
\lor
H_{Euler\text{-}scale\ noncompact}^{strong}.
}
\]

### Main weakness

No general finite global budget excludes the compact ancient Euler profile, and no general Liouville theorem applies to the inherited class.

If Euler-scale compactness fails, the failure itself still requires a new source-scale pricing theorem.

### Leverage verdict

\[
\boxed{\mathcal R_{remote}:\text{ highest analytic difficulty}.}
\]

It is the least attractive next target unless another root routes into it with extra structure.

## 3. Root R-critical

\[
\boxed{
\mathcal R_{critical}
:=
G_{escaping\ critical\ tail/W1\ boundary/realization}.
}
\]

### Available structure

On the passive critical branch the far field has

\[
U\sim R^{-1}A(\log R-\theta/2,\omega),
\]

with a measurable equivariant scattering factor and positive ergodic cubic/vorticity densities on the hard component.

The exact self-similar stationary subbranch is eliminated by classical backward self-similar Liouville theory using the inherited global \(L^6\) class.

The near-one DSS subbranch is partly removed by known DSS rigidity results.

A surviving exact DSS state must carry a nonzero log-periodic critical amplitude.

### Anti-shortcut from M5-564

M5-563 shows fixed remote-shell recurrence requires historical replenishment from smaller similarity radii.

However the fixed-shell Dirichlet balance is

\[
\boxed{
\frac12J_{R,\chi}'
+\frac14J_{R,\chi}
=
\mathcal F_{dil}(R)
+R^{-2}\mathcal S_{PDE}(R).
}
\]

At critical scale the order-one balance can be paid by the similarity-dilation flux \(\mathcal F_{dil}\) while the genuine PDE source is only \(O(R^{-2})\).

Therefore

\[
\boxed{
\text{historical critical replenishment}
\not\Rightarrow
\text{physical turnover/ancestry payment}.
}
\]

In particular,

\[
\boxed{\mathcal R_{critical}\not\subset\mathcal R_{AC}}
\]

by this argument alone.

### Remaining hard core

After stationary pruning, the critical root contains at least

\[
\boxed{
E_{DSS}^{general\ finite\ period}
\lor
E_{recurrent}^{aperiodic},
}

plus uncontrolled terminal-trace/low-frequency realization failures.

### Leverage verdict

\[
\boxed{\mathcal R_{critical}:\text{ intermediate difficulty}.}
\]

It has strong exact asymptotics and partial external rigidity, but the exact critical dilation conveyor is a real noncoercive mechanism.

## 4. Root R-AC

\[
\boxed{
\mathcal R_{AC}:=\mathcal R_{ancestry\ conversion}.
}
\]

### Available structure

Several local events already have fixed normalized costs:

- dissipation-paid compensated-variance turnover;
- palinstrophy/raw-H2 branch payers;
- contact/exposure/replacement events;
- fresh-carrier return events.

There are also exact finite parent budgets, most importantly standard kinetic-energy dissipation.

For a certified large record family,

\[
\boxed{
\sum_mR_m\int E_m(s)ds<\infty.
}
\]

A fixed positive normalized enstrophy-dissipation payment would therefore be impossible if it appears as a nonreused bounded-overlap family with \(R_m\to\infty\).

The return-density subproblem is also reduced to an explicit target such as

\[
\boxed{
\mathfrak R_k\gtrsim J_k^{1/2}
}
\]

on a cubic-divergent subset.

### Leverage verdict

\[
\boxed{\mathcal R_{AC}:\text{ strongest existing coercive structure}.}
\]

The root is difficult, but its missing objects are representation, nonreuse, and physical-time weights rather than a new unknown PDE dynamics class.

## 5. Important ancestry-direction firewall

The preceding positive-\(R\) standard-energy ledger can easily be misused.

Let stage \(n\) be earlier/coarser and stage \(j>n\) later/finer, with

\[
r_j=r_nq^{-(j-n)/2}.
\]

Define

\[
R_{j/n}:=\frac{r_n}{r_j}=q^{(j-n)/2}>1.
\]

The later event has **smaller physical scale** than the earlier parent.

If one simply expresses the later stage inside the earlier stage's coordinates, its natural spatial size is

\[
R_{j/n}^{-1},
\]

not \(R_{j/n}\).

Therefore a forward chronological first-hitting sequence does **not** automatically become a large-\(R\) blow-down record family in one earlier-stage parent.

Symbolically,

\[
\boxed{
\text{later finer first-hitting stage}
\not\equiv
\text{large-}R\text{ ancestry record of an earlier parent}.
}
\]

The positive-\(R\) ledger applies to the correctly oriented blow-down/ancestor representation, not to an arbitrary forward nesting of shrinking stages.

## 6. Why the direction matters numerically

A fixed normalized spacetime enstrophy charge at own physical scale \(r_j\) has physical cost

\[
q_{E,j}^{phys}\asymp r_jq_{E,j}.
\]

With geometric first-hitting scales,

\[
\sum_jr_j<\infty.
\]

Thus the chronological forward stage sequence is naturally summable.

By contrast, if a **single fixed physical parent event** is represented by older/larger blow-down records of ratio \(R_m\to\infty\), the normalized-to-parent conversion is

\[
q_E^{parent}=R_mq_E^{(R_m)},
\]

which is the positive-\(R\) ledger.

These are different constructions.

Therefore R-AC cannot be closed by merely relabeling the first-hitting generation index as the record index.

## 7. Correct AC target A — backward record embedding

The first viable ancestry target is:

\[
\boxed{
\text{selected local payer event}
\to
\text{one backward/ancestor blow-down family}
}
\]

such that:

1. the same parent physical history is used;
2. record ratios satisfy \(R_m\to\infty\);
3. event windows map into annular-safe bounded-overlap parent windows;
4. the events are not one-to-one rerecordings of the same physical occurrence;
5. the payer is retained after the blow-down.

Only then may positive-\(R\), \(R^{-1}\), \(R^{-3}\), etc. ancestry economics be applied.

## 8. Correct AC target B — physical dwell amplification

For fresh/contact carrier recurrence, one instead needs enough physical dwell at the ancestral scale.

If

\[
\rho_k=r_jK_k,
\qquad K_k=q^{k/2},
\]

then an \(O(1)\) current-epoch similarity dwell gives only

\[
\frac{\tau_{phys}}{\rho_k}
\asymp
\frac{\rho_k}{K_k^2}.
\]

Thus the missing theorem must produce either

- dwell of ancestral order \(\rho_k^2\), or
- sufficiently many independent fresh carriers/events, or
- a lower-order resource with a stronger ancestry weight.

Merely knowing recurrent contact is insufficient.

## 9. Correct AC target C — boundary-only turnover

M18-044 gives

\[
\mathscr B_j+\mathscr D_j\ge c_{turn}.
\]

If \(\mathscr D_j\) owns a fixed fraction, standard-energy dissipation is available once ancestry conversion is solved.

If instead the payment is almost entirely

\[
\mathscr B_j=\int|F_w|ds,
\]

there is no currently certified finite global parent budget for absolute moving-boundary work.

Therefore R-AC itself has a sharp internal split:

\[
\boxed{
\mathcal R_{AC}
=
\mathcal R_{embed/dwell}
\lor
\mathcal R_{boundary\text{-}only}.
}
\]

The first is a genealogy/representation problem; the second may require a new coercive boundary-to-bulk conversion.

## 10. Root leverage table

\[
\boxed{
\begin{array}{l|c|c|c|c|c}
\text{root}&\text{fixed witness}&\text{finite budget}&\text{favorable scaling}&\text{external rigidity}&\text{missing object}\\
\hline
R\text{-remote}&\checkmark&\text{weak}&\text{mixed}&\text{scenario-only}&\text{Euler compactness/rigidity}\\
R\text{-critical}&\checkmark&\text{critical only}&\text{neutral}&\text{partial}&\text{DSS/aperiodic conveyor rigidity}\\
R\text{-AC}&\checkmark&\checkmark\text{ on bulk subbranches}&\checkmark\text{ if correctly oriented}&\text{not needed}&\text{embedding/dwell/coercivity}
\end{array}
}
\]

## 11. Priority decision

The next primary root should be

\[
\boxed{\mathcal R_{AC}.}
\]

Reason:

- it already has exact finite budgets on significant subbranches;
- it does not require solving a new Euler Liouville problem;
- its major gaps are concrete and auditable;
- success can simultaneously strengthen every downstream canonical branch because all of them eventually need ancestry placement/nonreuse.

The second priority is R-critical.

R-remote should remain third unless a new external or internal compactness theorem becomes available.

## 12. What should not be attempted next

Low-value next moves include:

1. another CE-H derivative escalation to D4/D5 without lower-order descent;
2. treating historical critical replenishment as material turnover despite M5-564;
3. summing own-scale first-hitting payments as though they were positive-\(R\) parent records;
4. attacking general ancient Euler nonexistence without extra structure.

## 13. Immediate AC program

Proceed in the following order.

### AC-1 — event-orientation dictionary

Build the exact map among:

- chronological first-hitting stages;
- first-generation ancient history;
- second-generation blow-down records;
- terminal similarity events;
- fixed-parent physical windows.

This should state which direction produces \(R\), \(R^{-1}\), or no independent record at all.

### AC-2 — nonreuse certificate

For each event family, mark whether independence comes from:

- disjoint physical time;
- bounded overlap;
- distinct material labels with finite-memory control;
- or no valid multiplicity.

### AC-3 — payer inheritance

Determine which local payers survive the correct backward record map and with what exact homogeneous exponent.

### AC-4 — boundary-only conversion

Attempt to bound absolute moving-boundary work by bulk enstrophy/palinstrophy/pressure resources or route its persistent failure to R-remote/R-critical.

## 14. Audit verdict

### Certified

1. R-remote is presently the least coercive root.
2. R-critical has exact asymptotics and partial Liouville pruning but admits a genuine kinematic critical conveyor.
3. R-critical cannot simply be absorbed into R-AC via historical replenishment.
4. R-AC has the strongest current finite-budget structure.
5. Forward shrinking first-hitting stages are not automatically large-\(R\) fixed-parent records.
6. Correct ancestry orientation is a prerequisite for using the positive-\(R\) standard-energy ledger.
7. R-AC should be the next primary line.

### Still open

1. AC event-orientation dictionary across all representations.
2. AC nonreuse and dwell theorems.
3. Absolute boundary-work coercivity.
4. R-critical DSS/aperiodic rigidity.
5. R-remote Euler-scale closure.
6. Global 3D Navier--Stokes regularity.

## 15. Next target

M18-054 should construct the **AC event-orientation dictionary**.

For each of the main event sources

\[
\text{first-hitting stage},
\quad
\text{backward ancestor},
\quad
\text{second-generation record},
\quad
\text{terminal similarity production},
\]

write the exact spatial/time scaling into one chosen fixed parent and identify:

- large versus small record ratio;
- parent-time window location;
- whether bounded overlap is automatic;
- whether one event is being rerecorded or a genuinely distinct physical event is present.
