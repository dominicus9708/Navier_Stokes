# M18-050 — ROOT-CERT dependency certificate matrix isolates the W1–ratchet–hull bridge as the main uncertified middle arrow

**Date:** 2026-09-11  
**Status:** ROOT-CERT DEPENDENCY MATRIX / MIDDLE-BRIDGE FIREWALL / THEOREM-SCOPE CERTIFICATE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-049 found no fourth active upstream root beyond

\[
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC},
\]

but ROOT-CERT remains open because branch classification and theorem-ready dependency certification are different tasks.

This module replaces the broad R0--R5 labels of M18-041 by a more operational **dependency certificate matrix**.

For each major arrow, assign one of:

- `STD` — standard PDE/dynamical input;
- `INT` — internally proved in the repository under explicitly stated hypotheses;
- `EXT` — depends on an external theorem with scope firewall;
- `COND-R1/R2/R3` — valid on the complement of one of the three current root complexes;
- `MISS` — no explicit certified bridge presently identified.

## 2. Working proof-chain skeleton

The intended global chain may be written

\[
\boxed{
\begin{aligned}
\mathcal S_0 &: \text{hypothetical finite-time singularity},\\
\mathcal S_1 &: \text{first-hitting / blow-up tower},\\
\mathcal S_2 &: \text{bounded compact ancient ratchet element},\\
\mathcal S_3 &: \text{compact two-sided similarity/W1 hull with terminal trace},\\
\mathcal S_4 &: \text{hard ergodic terminal production system},\\
\mathcal S_5 &: \{CP-E,CP-S,CE-T,Migration,CE-H\},\\
\mathcal S_6 &: \text{parent contradiction / rigidity}.
\end{aligned}
}
\]

The key point is that \(\mathcal S_2\) and \(\mathcal S_3\) are **not the same object by definition**.

## 3. D0 — singularity implies unbounded first-hitting amplitude sequence

For a smooth solution approaching a first finite singular time, the first-hitting construction tracks increasing vorticity maxima

\[
W_j=q^jW_0,
\qquad q>1,
\]

with first times \(t_j\uparrow T_*\) whenever the vorticity supremum becomes unbounded.

The repository treats this as the standard starting normalization.

The standard Beale--Kato--Majda continuation criterion supports the necessity of vorticity control for smooth continuation, but the present module does not re-import its full statement as a new theorem.

Certificate:

\[
\boxed{D0:\ \mathcal S_0\to\mathcal S_1\quad\text{STD/FOUNDATIONAL}.}
\]

Caution: this certifies the first-hitting **sequence**, not yet a nontrivial compact blow-up limit.

## 4. D1 — first-hitting tower splits into strong exits or a bounded compact lane

The repository has explicit case splits for the main ways normalized compactness can fail:

- Type-II / amplitude escalation;
- normalized-enstrophy escalation;
- center turnover;
- weak-L3 / derivative-frequency escalation;
- Campanato/boundary turnover;
- reformation/replacement/export;
- remote active source formation.

M18-043--049 route these failures to

\[
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC}.
\]

On their complement, M5-474 proves local smooth compactness and extracts a nontrivial ancient element with

\[
\boxed{|\Omega_*(0,0)|=1}
\]

and

\[
\Omega_*\in L^\infty_{loc,t}(L^2\cap L^\infty).
\]

Certificate:

\[
\boxed{
D1:\ \mathcal S_1
\to
\mathcal R_{remote}\lor\mathcal R_{critical}\lor\mathcal R_{AC}\lor\mathcal S_2
\quad\text{INT + complement-classified}.
}
\]

This is substantially stronger than M18-041's original undifferentiated R0/R1 status.

## 5. D2 — internal structure of the bounded ancient ratchet lane

Inside \(\mathcal S_2\), the repository proves:

- exact first-hitting vorticity cap;
- bounded normalized enstrophy on compact backward intervals;
- Type-I backward decay;
- finite ancient palinstrophy;
- nontrivial backward record saturation;
- material ratchet/projective action marks;
- second-generation blow-down nontriviality;
- two-sided first-hitting/Leray clock comparability on the compact corridor.

Certificate:

\[
\boxed{D2:\ \mathcal S_2\to\text{marked bounded ancient ratchet package}\quad\text{INT}.}
\]

These are consequences **inside** the lane, not an identification with W1.

## 6. B-WR — the W1 / ratchet / two-sided-hull equivalence bridge

The August W1 line and the September first-hitting ratchet line use different state packages.

### W1 package

The active proof map describes a recurrent weak-critical similarity corridor with:

- compact/minimal recurrence;
- bounded weak-L3 on W1;
- global \(L^p\) precompactness for \(p>3\) under bounded frequency/Campanato;
- a critical terminal/boundary coordinate;
- terminal trace / global realization issues.

### Ratchet package

M5-474--478 gives:

- a physical first-hitting normalized ancient NS element;
- \(L^2\cap L^\infty\) vorticity control on compact backward intervals;
- geometric backward first-hitting records;
- material ratchet marks;
- Type-I backward decay.

These packages overlap strongly but are not definitionally identical.

No module located in the current audit proves the theorem

\[
\boxed{
\mathcal S_2
\Longleftrightarrow
\mathcal S_3
}
\]

with all required global tail, terminal-trace, recurrence, pressure, and realization data preserved both ways.

Therefore define the explicit missing bridge

\[
\boxed{B_{WR}:=\text{W1--ratchet--two-sided-hull compatibility/equivalence}.}
\]

Certificate:

\[
\boxed{B_{WR}:\ \mathcal S_2\to\mathcal S_3\quad\text{MISS}.}
\]

This is the clearest currently identified **middle-chain ROOT-CERT gap**.

## 7. What B-WR must actually prove

A valid B-WR theorem must not merely compare notation.

It must certify at least:

1. common normalization or an exact conversion dictionary;
2. one common nonzero state/core mark;
3. two-sided time extension needed for the hull;
4. global tail topology sufficient for W1 state-space compactness;
5. terminal trace/scattering profile existence in the required class;
6. pressure/gauge compatibility;
7. preservation of the first-hitting/ratchet genealogy marks;
8. no loss of the critical boundary defect under the conversion;
9. explicit routing of every failure to R1--R3.

Without these items, the two analysis lines may study related survivors without forming one certified proof chain.

## 8. D3 — compact two-sided hull to ergodic terminal process

Once a compact two-sided similarity hull \((\mathfrak H,\sigma_t)\) and invariant probability measure are available, passing to an ergodic component is standard dynamical-systems machinery.

M5-571 then uses the equivariant terminal-trace factor map

\[
A_{\sigma_tY}(q,\omega)
=
A_Y(q-t/2,\omega)
\]

to push the ergodic measure to a stationary ergodic log-radius process.

Nontriviality gives positive mean cubic and terminal-vorticity observables.

Certificate:

\[
\boxed{
D3:\ \mathcal S_3\to\text{hard ergodic terminal process}\quad\text{STD+INT}.
}
\]

Scope firewall: this arrow presupposes the compact two-sided hull and the terminal-trace factor map. Those are part of B-WR/R2 rather than consequences of ergodicity itself.

## 9. D4 — terminal ergodic process to finite-depth production system

M5-587 derives a finite-depth production shell from the averaged wedge enstrophy identity.

M5-589 thickens it to a fixed positive-volume, positive-time, positive-density production event.

M5-590 links that event to a fixed persistent material-flux payer lineage after finite saturation.

Later modules extract the dual source/anchoring/projective alternatives.

Certificate:

\[
\boxed{
D4:\ \text{hard ergodic terminal process}\to\mathcal S_4\quad\text{INT}.}
\]

The remaining time-direction LOG-ALIGN issue concerns mapping selected late payer events into backward record ancestry and belongs to R3/ancestry conversion, not to existence of the terminal production event itself.

## 10. D5 — finite production system to the five-branch menu

M5-593--598 construct the finite production-linked menu

\[
\boxed{
CP-E\lor CP-S\lor CE-T\lor Migration\lor CE-H.
}
\]

M18-040 confirms the non-CE-H branches have standard-resource prices; the M12--M18 line develops CE-H.

Certificate:

\[
\boxed{D5:\ \mathcal S_4\to\mathcal S_5\quad\text{INT / subsystem-complete}.}
\]

This is the strongest branch-completeness arrow in the current repository.

## 11. D6 — branch selection to a local payer

M18-040 gives

\[
CP-E\to P/H,
\qquad
CP-S\to P\text{ or compactness loss},
\]

\[
CE-T\to H,
\qquad
Migration\to P.
\]

CE-H has a detailed payer/concentration tree including

- palinstrophy;
- raw-H2;
- D3/coefficient-gradient resources;
- zero-level/second-jet/critical-level endpoints;
- coefficient/amplitude decompactification;
- interface/domain/genealogy exits.

Certificate:

\[
\boxed{D6:\ \mathcal S_5\to\text{typed local payer/exit}\quad\text{INT}.}
\]

The difficulty is no longer absence of a local payer.

## 12. D7 — local payer to fixed-parent contradiction

This arrow is governed by M18-048's ancestry-conversion gate.

A fixed normalized event is not automatically a nonsummable parent charge.

One needs:

- common-parent record embedding;
- exact scale factor;
- nonreuse/bounded overlap;
- a resource with finite parent total;
- sufficient multiplicity/residence/growth against the ancestry weight.

The generic derivative weights are

\[
R^{-1},\quad R^{-3},\quad R^{-5},\dots
\]

while spacetime enstrophy has the stronger positive-\(R\) standard-energy ledger.

Certificate:

\[
\boxed{D7:\ \text{local payer}\to\mathcal S_6\quad\text{OPEN}=\mathcal R_{AC}\text{ plus downstream endpoint issues}.}
\]

## 13. External-theorem dependencies

The current chain imports several standard/external results at specific places.

Examples include:

- standard Navier--Stokes local energy / suitable-solution compactness facts where invoked;
- pointwise Type-I \(\Rightarrow\) scale-invariant local-energy estimates in the Campanato routing;
- analyticity results used to globalize CE-H identities in M5-599;
- stationary backward self-similar Liouville theorems where a stationary alpha-limit is considered.

These are **scope-local** dependencies.

No external theorem currently supplies B-WR or D7 in the general surviving class.

## 14. Certificate matrix

\[
\boxed{
\begin{array}{c|l|l}
\text{ID}&\text{arrow}&\text{certificate}\\
\hline
D0&\text{singularity}\to\text{first-hitting sequence}&STD/FOUNDATIONAL\\
D1&\text{first-hitting}\to\text{strong roots or bounded ancient lane}&INT+R1/R2/R3\text{ complements}\\
D2&\text{bounded ancient lane}\to\text{marked ratchet package}&INT\\
B_{WR}&\text{ratchet package}\to\text{W1/two-sided terminal hull}&\mathbf{MISS}\\
D3&\text{compact two-sided hull}\to\text{ergodic terminal process}&STD+INT\\
D4&\text{ergodic terminal process}\to\text{finite-depth production}&INT\\
D5&\text{production}\to\text{five-branch menu}&INT\\
D6&\text{branch}\to\text{typed local payer}&INT\\
D7&\text{payer}\to\text{parent contradiction/rigidity}&OPEN\ (R3/CE-H\ endpoints)
\end{array}
}
\]

Here `R1/R2/R3` in the D1 row refers to the three M18-049 root complexes, not M18-041's old gate numbering.

## 15. Main result of the dependency audit

The chain no longer has a vague statement that “everything upstream is open.”

The currently identified theorem-level gaps separate into two qualitatively different classes.

### Middle-chain compatibility gap

\[
\boxed{B_{WR}}
\]

This asks whether the bounded first-hitting ratchet ancient object and the compact W1/two-sided terminal-trace hull are one certified survivor package, with failures routed to the three roots.

### End-chain ancestry/rigidity gap

\[
\boxed{D7}
\]

This asks whether the typed local payments/critical structures produce a nonsummable fixed-parent charge or an independent rigidity contradiction.

The remote and critical root complexes also remain analytically open, but they are now explicit alternatives rather than hidden missing arrows.

## 16. Relation to ROOT-CERT

A theorem-ready ROOT-CERT would require a statement of the form

\[
\boxed{
\mathcal S_0
\Longrightarrow
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC}
\lor
\mathcal S_5,
}
\]

with every intermediate arrow certified.

The current audit gets close at the level of active branch classification, but B-WR prevents writing this as one verified theorem chain.

Therefore

\[
\boxed{ROOT\text{-}CERT\ remains\ open\ primarily\ at\ B_{WR},\text{ plus historical completeness}.}
\]

## 17. Immediate research priority

The next global calculation should target B-WR rather than another CE-H high-jet branch.

The most economical direction is one-way first:

\[
\boxed{
\mathcal S_2
\stackrel{?}{\Longrightarrow}
\mathcal S_3
\lor
\mathcal R_{remote}
\lor
\mathcal R_{critical}
\lor
\mathcal R_{AC}.
}
\]

One need not prove full equivalence if this one-way implication suffices for the proof tree.

Concretely, start from the M5-474 marked ancient element and audit whether its already proved Type-I decay, vorticity \(L^2\cap L^\infty\), first-hitting records, and ratchet marks imply the global \(L^p\) tightness / terminal trace / two-sided recurrence package used by M5-571.

Failure of each desired property must be routed explicitly to R1--R3.

## 18. Audit verdict

### Certified

1. The first-hitting compact lane yields a nontrivial marked ancient element unless one of the three root complexes occurs.
2. Once a compact two-sided terminal-trace hull exists, the hard ergodic terminal process is internally/standardly obtained.
3. The hard ergodic process produces the finite-depth production system and finite five-branch menu internally.
4. Every branch has a typed local payer/exit.
5. The active dependency chain has one newly isolated middle compatibility gap B-WR and one known end-chain ancestry/rigidity gap D7.

### Not certified

1. B-WR.
2. D7.
3. Closure of the remote root.
4. Closure of the critical root.
5. Historical branch-completeness outside active indexes.
6. Global 3D Navier--Stokes regularity.

## 19. Next target

M18-051 should attack the one-way B-WR bridge:

\[
\boxed{
\text{M5-474 marked ancient ratchet element}
\to
\text{compact two-sided similarity/terminal-trace hull}
\lor R1\lor R2\lor R3.
}
\]

Begin with the easiest pieces:

1. global \(L^p\), \(p>3\), control/tightness from \(\Omega\in L^2\cap L^\infty\) and Type-I decay;
2. similarity-time precompactness on fixed balls;
3. low-frequency/velocity-tail obstruction;
4. terminal trace/scattering profile existence.
