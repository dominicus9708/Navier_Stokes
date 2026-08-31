# DSD M5-413 — Master reconsolidation: critical scale-space throughput versus analytic realization defect

Date: 2026-08-31

Status: **POST-M5-408--412 MASTER UPDATE / ITERATED REMOTE SATELLITES, FINITE PHASE-MEMORY REUSE, GENERIC PROJECTIVE AXIS CHANGE, AND FORMED MATERIAL-FLUX EXPORT NO LONGER NEED TO BE CARRIED AS INDEPENDENT TERMINAL MECHANISMS / THEY ROUTE TO A COMMON SCALE-INVARIANT CRITICAL THROUGHPUT CONSISTING OF `dot H^{1/2}` PHASE-SPACE CARRIER NOVELTY, SHELL/FREQUENCY/CAPACITY/DIRECTION/FLUX ACTION, OR TO A NARROWER ANALYTIC REALIZATION/PRESSURE/LOCALIZATION DEFECT / THE CRITICAL THROUGHPUT CAN DIVERGE ON A HYPOTHETICAL SINGULARITY, SO THIS IS A STRUCTURAL REDUCTION RATHER THAN GLOBAL REGULARITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Starting frontier

M5-407 organized the late proof tree as

\[
H_{local}^{crit}
\lor
S_{remote}^{iterated}
\lor
T_{interface}^{projective/export/realization}.
\]

M5-408--412 have now supplied a common critical carrier unit and have propagated it through the remote, projective, and formed-export labels.

A new master frontier is therefore required.

---

## 2. Critical carrier atom

M5-408 proved that every coherent natural carrier with

\[
|\omega\cdot e|
\gtrsim
\frac\nu{r^2}
\]

on a fixed fraction of a natural ball has a scale-invariant coefficient

\[
\boxed{
|\langle\omega,\psi_{r,x,e}\rangle|
\gtrsim\nu
}
\]

for a normalized test atom

\[
\psi_{r,x,e}(y)
=r^{-1}\varphi((y-x)/r)e
\]

with fixed `dot H^{1/2}` norm.

For divergence-free velocity,

\[
\boxed{
\|\omega\|_{\dot H^{-1/2}}
=
\|u\|_{\dot H^{1/2}}.
}
\]

A phase-space separated family is Bessel, giving

\[
\boxed{
N_{crit}(t)\nu^2
\lesssim
\|u(t)\|_{\dot H^{1/2}}^2.
}
\]

This is the first common carrier counter with no shrinking physical `r` weight.

---

## 3. Define the critical phase-space novelty descriptor

At one smooth time `t`, let `F(t)` range over all retained families of formed coherent natural carriers whose M5-408 probes satisfy the fixed phase-space Bessel separation rule.

Define

\[
\boxed{
\mathfrak N_{crit}(t)
:=
\sup_{F(t)}
\sum_{i\in F(t)}
\frac{|\langle\omega(t),\psi_i\rangle|^2}{\nu^2}.
}
\]

Then

\[
\boxed{
\mathfrak N_{crit}(t)
\lesssim
\nu^{-2}
\|u(t)\|_{\dot H^{1/2}}^2.
}
\]

For a family in which every carrier coefficient has the fixed lower bound `c_* nu`, `mathfrak N_crit` is equivalent up to constants to the maximal number of genuinely distinct coherent critical carrier cells visible at that snapshot.

It does not count material labels twice inside one Eulerian phase-space cell.

---

## 4. Remote recursion is critical throughput

M5-409 showed that every finite depth of the M5-402 remote recursion can be pulled back to one physical prelimit snapshot.

Successive nodes are separated in position-scale phase space, although the physical natural scales need not be monotone.

Hence an arbitrarily long recursion satisfies the novelty/reuse fork:

\[
\boxed{
S_{remote}^{iterated}
\Longrightarrow
H_{\dot H^{1/2}\,novelty}
\lor
R_{remote}^{finite\ phase\ memory}
\lor
H_{local}^{crit}
\lor
T_{interface}.
}
\]

M5-410 then proves that a finite reused set of natural-strength localized carriers cannot self-supply order-one target-natural remote strain. The residual source must recruit fresh shell/phase-space content or pay local/interface action.

Therefore

\[
\boxed{
S_{remote}^{iterated}
\Longrightarrow
H_{throughput}^{crit}
\lor
T_{realization/interface}.
}
\]

Remote recursion is no longer a conceptually independent final branch.

---

## 5. Projective action is critical throughput or replacement

M5-411 uses the exact direction equation on a retained active material carrier:

\[
D_t\xi
=
\tau
+
\frac\nu{|\omega|}
(I-\xi\otimes\xi)\Delta\omega.
\]

An order-one material-axis change therefore forces

\[
H_{\tau,act}^{crit}
\lor
H_{dir\,diff/freq/cap}^{crit}.
\]

If the active material carrier does not persist, the observational axis change is flux replacement/reformation, not a valid continuous projective path.

M5-395--410 route that branch to fresh carrier novelty, viscous-flux H, shell/direction H, or remote recruitment.

Thus

\[
\boxed{
T_{projective}^{generic}
\Longrightarrow
H_{throughput}^{crit}
\lor
T_{realization/interface}.
}

The projective label itself is removed as an independent terminal.

---

## 6. Formed flux export is critical throughput

M5-412 tracks a formed material cross-section with

\[
\Phi\asymp\nu.
\]

After it leaves a local natural window:

- fixed flux loss is viscous-flux H;
- coherent surviving flux elsewhere is another local/remote critical carrier;
- spread surviving flux becomes a distributed shell/occupancy reservoir;
- fragmentation enters the existing palinstrophy/capacity gate;
- direction change enters M5-411.

Therefore

\[
\boxed{
T_{export}^{formed\ flux}
\Longrightarrow
H_{throughput}^{crit}.
}

What remains under `interface` is not formed material-flux export but analytic realization/localization failure before a complete carrier description exists.

---

## 7. What is included in H_throughput^crit

Define schematically

\[
\boxed{
H_{throughput}^{crit}
:=
H_{\dot H^{1/2}\,novelty}
\lor
H_{shell/frequency/capacity}
\lor
H_{direction/tilt/diffusion}
\lor
H_{viscous\ flux}
\lor
H_{distributed\ source}.
}

These are not five unrelated mechanisms.

They are five descriptions of failure to keep the active source/carrier population inside a finite reusable compact scale-space structure.

Where a well-formed natural packet can be extracted, it enters `mathfrak N_crit`.

Where packet formation itself fails through diffuse shell spread or internal roughness, the event remains a critical shell/frequency/capacity action until it is point-picked or localized.

Thus the common object is **critical scale-space throughput**, not merely one specific norm.

---

## 8. Why H_throughput^crit is not yet a contradiction

The critical Sobolev norm

\[
\|u(t)\|_{\dot H^{1/2}}
\]

is not controlled by the Leray kinetic-energy inequality.

Likewise the critical shell/direction/flux actions are compatible with Navier--Stokes scaling.

A hypothetical singularity may therefore satisfy

\[
\mathfrak N_{crit}(t)	o\infty
\]

or

\[
\|u(t)\|_{\dot H^{1/2}}	o\infty.
\]

The new result is a **unification of mechanisms**, not a finite global budget.

The earlier L2 Bessel packing showed that physical action cannot be double-counted across scales but retained a summable `r` weight. The M5-408 critical atoms remove that weight, at the cost of moving to a norm that itself may blow up.

This is the correct current critical wall.

---

## 9. Remaining analytic realization defect

The only interface class not yet absorbed is

\[
\boxed{
T_{real}^{analytic}
:=
T_{pressure/localization/restart\ coherence}.
}

Examples include:

- a local solenoidal truncation whose global evolution does not approximate the actual satellite evolution on the inner cylinder;
- a nonvanishing far-field harmonic/pressure defect under expanding cutoffs;
- a large cutoff/Bogovskii correction before a formed carrier object can be assigned;
- failure of local/global compactness coherence in a velocity-pressure topology.

Existing repository results already narrow this class substantially.

---

## 10. What is already known about pressure/localization

The existing explicit cutoff gates prove that large localization leakage forces either annular vorticity mass or annular derivative content.

The old-shell pressure audit proves, under parent Morrey plus Type-I/derivative control, that pressure oscillation and pressure gradients remain at their natural scale and are not independent forcing amplifiers.

M5-266 similarly routes substantial pressure momentum force, under the W1 velocity cap, to a global H1/strain reservoir.

Thus a **large** pressure/localization defect generally returns to

\[
H_{throughput}^{crit}
\lor S_{remote}.
\]

The unresolved issue is subtler: a bounded but nonvanishing defect may still prevent an exact restart/coherence passage as the cutoff radius tends to infinity.

That is why `T_real^analytic` is retained.

---

## 11. Current master tree

The proof tree can now be written at its most compressed audited level as

\[
\boxed{
\text{hypothetical singular tower}
\Longrightarrow
H_{throughput}^{crit}
\lor
T_{real}^{analytic}.
}

Here

\[
\boxed{
H_{throughput}^{crit}
}

contains the local/remote/material/projective critical activity after all currently proved carrier/source routings.

And

\[
\boxed{
T_{real}^{analytic}
}

is no longer a physical turnover category. It is an analytic inheritance/coherence obstruction.

This distinction is important for the next phase.

---

## 12. Next target A — critical-throughput evolution

The first possible route is to find an evolution law for

\[
\mathfrak N_{crit}
\quad\text{or}\quad
\|u\|_{\dot H^{1/2}}^2
\]

that uses the extra first-hitting/source genealogy to impose more than the standard critical Sobolev blow-up alternative.

A useful theorem would need one of:

- a strict efficiency loss for creation of each genuinely new critical carrier atom;
- a bounded total variation/Carleson law for phase-space novelty;
- a non-reuse theorem converting critical throughput into a supercritical dissipative cost;
- a rigidity theorem for a critical element saturating the throughput indefinitely.

A bare statement that the critical norm diverges is not enough.

---

## 13. Next target B — eliminate bounded realization defects

The second route is to classify a nonvanishing restart/localization defect as the cutoff radius grows.

The desired fork is

\[
\boxed{
\text{realization defect}
\Longrightarrow
\text{critical weak-L3/Besov tail}
\lor
H_{throughput}^{crit}.
}

The first branch would return to the existing complete ancient Liouville theorem; the second would merge with the common throughput frontier.

This is now a narrower problem than the former generic `T_dynamic` category.

---

## 14. DSD interpretation

At the present resolution the physically meaningful descriptors are

\[
\boxed{
\text{formed critical carrier/source content}
}

and

\[
\boxed{
\text{failure to realize that content coherently under localization/limit passage}.
}

Many former words -- contact, replacement, remote, projective, export -- are no longer final categories once material identity, flux identity, axis identity, and phase-space identity are separated.

They are transitions between states of the same critical throughput system.

---

## 15. Audit verdict

### REMOVED AS INDEPENDENT TERMINALS AFTER M5-408--412

\[
\boxed{
S_{remote}^{iterated},
\quad
R_{remote}^{finite\ phase\ memory},
\quad
T_{projective}^{generic},
\quad
T_{export}^{formed\ flux}.
}

### CURRENT MASTER FRONTIER

\[
\boxed{
H_{throughput}^{crit}
\lor
T_{real}^{analytic}.
}

### STILL OPEN

- a coercive evolution/rigidity law excluding unbounded critical throughput;
- classification of bounded nonvanishing restart/pressure/localization defects;
- final closure of the hypothetical singular tower;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]