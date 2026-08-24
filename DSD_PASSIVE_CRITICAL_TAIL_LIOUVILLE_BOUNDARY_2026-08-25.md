# DSD Passive Critical-Tail / Liouville Boundary

Date: 2026-08-25

Status: **KNOWN STATIONARY / STRONGLY INTEGRABLE / EXTREME-ROTATION SUBCLASSES REMOVED FROM THE PASSIVE-TAIL FRONTIER / GENUINELY NONSTATIONARY RECURRENT WEAK-L3 TYPE-I TAIL REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The internal genealogy audit has reduced the most persistent bounded-Z survivor to a borderline configuration of the form

\[
\boxed{
\text{passive critical }1/R\text{ velocity tail}
+
\text{nontrivial recurrent Leray core}.
}
\]

The quiet-ancestor scaling calculation explains why this branch is critical:

\[
|V(Y)|\sim |Y|^{-1},
\qquad
|W(Y)|\sim |Y|^{-2},
\]

so vorticity/strain Sobolev tails can remain tight while the velocity lies only at the weak-L3 threshold.

Before attempting a new rigidity theorem, this note separates the subclasses already excluded by the literature from the genuinely unresolved recurrent class.

---

## 2. Classical stationary backward self-similarity is already excluded

For a stationary backward-Leray profile

\[
V(Y,s)=U(Y),
\]

the physical solution is backward globally self-similar.

Classical results of Necas-Ruzicka-Sverak and Tsai exclude nontrivial stationary profiles under strong critical/supercritical integrability assumptions. Chae-Wolf later extended stationary self-similar Liouville theorems to Lorentz profiles

\[
U\in L^{p,\infty}(\mathbb R^3),
\qquad p>\frac32.
\]

A pointwise critical tail

\[
|U(Y)|\lesssim(1+|Y|)^{-1}
\]

belongs to

\[
L^{3,\infty}(\mathbb R^3).
\]

Therefore the exact stationary passive `1/R` branch is not an admissible nonzero singular profile:

\[
\boxed{
\partial_sV\equiv0
+
|V(Y)|\lesssim(1+|Y|)^{-1}
\Longrightarrow
V\equiv0.
}
\]

This is an external Liouville input, not an internally derived DSD theorem.

---

## 3. Strong-L3 recurrent/self-similar lane is also not the hard endpoint

The critical regularity theory and the classical self-similar Liouville results show that a profile/trajectory uniformly belonging to strong `L3` is substantially more rigid than the present tail.

The passive `1/R` model satisfies

\[
V\in L^p\quad(p>3),
\qquad
V\notin L^3,
\qquad
V\in L^{3,\infty}.
\]

Thus the surviving genealogy branch must genuinely use the distinction

\[
\boxed{
L^{3,\infty}\setminus L^3.
}
\]

Any later argument that silently upgrades the critical tail to strong `L3` would discard the actual endpoint and is not admissible.

---

## 4. 2026 rotated self-similar result

Ben Pineau and Vlad Vicol, `arXiv:2607.09619v2` (revised 2026-08-06), study backwards rotated self-similar (RSS) and rotated discretely self-similar (RDSS) solutions under the Type-I spatial bound

\[
|U(Y)|\le \frac{C}{1+|Y|}.
\]

For RSS, they prove triviality when the constant rotation rate `alpha` is sufficiently small or sufficiently large relative to the Type-I constant.

Thus

\[
\boxed{
\text{RSS}+1/R\text{ Type-I tail}
+\left(|\alpha|\ll1\ \text{or}\ |\alpha|\gg1\right)
\Longrightarrow0.
}
\]

Their theorem explicitly leaves an intermediate-rotation regime open.

For RDSS they obtain analogous exclusions for extreme rotation together with a discrete scaling factor sufficiently close to one.

Accordingly, exact rigid rotation cannot be used as an unrestricted surviving model. Only the intermediate/open parameter region can still serve as an analogy for the recurrent frontier.

---

## 5. Why the present survivor is not automatically RSS/RDSS

The first-hitting/Leray clock theorem gives

\[
s_j=j\log q+O(1)
\]

and bounded cumulative clock defect.

The compact EMGG theorem gives positive-measure bounded-gap material returns.

Neither statement yields

\[
V(s+T)=V(s)
\]

or

\[
V(s+T)=\mathcal R V(s)
\]

for one fixed rotation `R`, nor an RDSS group action.

A compact recurrent orbit may be periodic, quasi-periodic, rotating with variable angular speed, or genuinely nonperiodic.

Therefore the Pineau-Vicol RSS/RDSS theorem removes genuine subbranches but does not eliminate the whole Leray Recurrent Motion Gate.

---

## 6. Local approximate-self-similarity regularity criterion

Pineau-Vicol also prove a local regularity criterion of a different type: under a local Type-I upper bound in a parabolic cylinder, one sufficiently good single time-slice of local approximate self-similarity regularizes the top-center point.

For the present proof tree this means:

\[
\boxed{
\text{on every subbranch where the required local Type-I / pressure hypotheses are verified,}
}
\]

any hypothetical singular survivor must avoid all sufficiently late slices satisfying the theorem's approximate-self-similarity smallness condition.

Equivalently, on that applicable subbranch there is a **one-slice motion floor**: the orbit may recur, but it cannot become too stationary/approximately self-similar at a late slice.

This is not a contradiction by itself. A nonstationary periodic or recurrent orbit can have a positive speed floor.

---

## 7. Exact external-boundary branch map

The passive critical-tail frontier may therefore be partitioned as follows.

### A. Stationary Leray profile

\[
\partial_sV=0.
\]

With the `1/R` critical tail, stationary Lorentz-space Liouville theory excludes the nonzero profile.

**Status: EXTERNALLY CLOSED.**

### B. Strong-L3 critical orbit/profile

This lies in a substantially stronger regularity class than the passive tail and is not the endpoint survivor.

**Status: ROUTED AWAY FROM THE TRUE ENDPOINT.**

### C. Exact RSS with extreme rotation

Pineau-Vicol excludes small and large rotation rates under Type-I.

**Status: EXTERNALLY CLOSED.**

### D. RDSS with extreme rotation and scaling factor sufficiently close to one

Pineau-Vicol excludes this class under Type-I.

**Status: EXTERNALLY CLOSED.**

### E. Intermediate rotated Type-I RSS/RDSS

The 2026 work itself leaves relevant intermediate rotation regimes open.

**Status: EXTERNAL OPEN BOUNDARY.**

### F. General compact nonstationary recurrent weak-L3 critical-tail orbit

No fixed period, rotation generator, or DSS group action has been derived in the repository.

**Status: MAIN INTERNAL FRONTIER.**

---

## 8. Correct rigidity target

The remaining target should not be stated as another generic shell or energy estimate.

The quiet-ancestor audit has already shown why those are critical and can remain summable.

The appropriate target is now a **phase-space rigidity statement**:

\[
\boxed{
\begin{gathered}
\text{compact nonzero recurrent Leray orbit}
+
\text{Type-I/weak-L3 passive critical tail}
+
\text{positive Betchov and H1 recurrence taxes}
\\
\stackrel{?}{\Longrightarrow}
\text{stationary / rigidly rotating / DSS-like suborbit}
\quad\text{or contradiction}.
\end{gathered}
}
\]

If the first alternative can be forced strongly enough, the known Liouville/RSS/RDSS theorems become usable.

If it cannot, the remaining object is genuinely more general than the currently classified self-similar families.

---

## 9. DSD audit

External theorem channels are kept distinct from internal derivations.

- `stationary` is a formed dynamic property, not inferred from recurrence;
- `RSS` requires one fixed rotation generator/rate;
- `RDSS` requires one fixed discrete spacetime symmetry;
- `recurrent` alone implies none of these;
- weak-L3 and strong-L3 are not merged;
- passive critical tail and local core recurrence remain separate channels until a rigidity theorem links them.

---

## 10. References

- Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619v2, revised 2026-08-06.
- Dongho Chae and Joerg Wolf, *On the Liouville type theorems for self-similar solutions to the Navier-Stokes equations*, Arch. Ration. Mech. Anal. 225 (2017), arXiv:1609.06962.
- Quansen Jiu, Yanqing Wang, Wei Wei, *Leray's backward self-similar solutions to the 3D Navier-Stokes equations in Morrey spaces*, arXiv:2006.15776.
- Classical stationary predecessors: Necas-Ruzicka-Sverak (1996); Tsai (1998).

---

## 11. Updated frontier

The remaining hard class can now be stated without already-solved baggage:

\[
\boxed{
\text{genuinely nonstationary compact recurrent Leray motion}
+
\text{passive }1/R\text{ weak-L3 critical tail}.
}
\]

It must avoid stationary Lorentz-space Liouville rigidity and, where the local Type-I theorem applies, avoid every sufficiently accurate one-slice approximate-self-similarity event.

This is the sharpened Leray Recurrent Motion Gate (LRMG).

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
