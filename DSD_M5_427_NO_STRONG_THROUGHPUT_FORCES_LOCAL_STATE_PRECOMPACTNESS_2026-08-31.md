# DSD M5-427 — No-strong-throughput corridor forces local Eulerian precompactness

Date: 2026-08-31

Status: **COMPACTNESS RECONSOLIDATION / STAGE-WIDE FIRST-HITTING ANALYTICITY ALREADY MAKES THE NORMALIZED VORTICITY FAMILY PRECOMPACT ON EVERY FIXED CYLINDER / AFTER REMOVING GALILEAN DRIFT, UNBOUNDED LOCAL VELOCITY-GRADIENT OR AFFINE/HARMONIC LOSS OF COMPACTNESS ROUTES BY M5-400--404 TO STRONG/DELOCALIZED CRITICAL THROUGHPUT / THEREFORE A LATE CORRIDOR WITH NO STRONG MASS/REMOTE/INTERFACE ESCAPE HAS NO INDEPENDENT BOUNDED-CLUSTER `STATE NOVELTY` MECHANISM / BOTH LABEL-FRESH AND CO-SHRINKING NEAR-BALANCED GEOMETRIES THEN ENTER THE EXISTING COMPLETE ANCIENT W1/W2 COMPACTNESS DICHOTOMY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-424 leaves two near-balanced geometries:

\[
C_{bal}^{co\text{-}shrink},
\qquad
C_{bal}^{fresh}.
\]

M5-426 corrects the second descriptor by showing that fresh material labels are not necessarily fresh Eulerian critical states.

The next question is whether a genuinely new normalized Eulerian state can keep appearing inside a bounded natural cluster while all strong mass/remote/interface exits remain absent.

The stage-wide analyticity already gives a strong answer.

---

## 2. Vorticity precompactness on every fixed normalized cylinder

At late first-hitting stage `j`, use parent variables

\[
y=\frac{x-X_j}{r_j},
\qquad
\tau=\frac{\nu(t-t_j)}{r_j^2},
\qquad
\Omega_j=\frac{\omega}{W_j}.
\]

M5-392 gives for every fixed integer `m>=0`

\[
\boxed{
\sup_j\sup_{\widehat I_j}
\|\nabla_y^m\Omega_j\|_{L^\infty(\mathbb R^3)}
\le C_m.
}
\]

Fix a compact parabolic cylinder

\[
K_{R,T}=B_R\times[-T,0]
\]

contained in the retained backward first-hitting tower.

The spatial derivative bounds give uniform equicontinuity in `y`.

The normalized vorticity equation is schematically

\[
D_\tau\Omega_j
=
\Sigma_j\Omega_j+\Delta\Omega_j.
\]

On the no-strong-interface corridor, the local strain/deformation action needed for M5-418 is uniformly bounded on each fixed cylinder; M5-392 controls `Delta Omega_j`.

Hence the time derivative is uniformly bounded after the local moving-frame/Galilean gauge is fixed.

Therefore Arzela--Ascoli/parabolic compactness gives

\[
\boxed{
\{\Omega_j\}
\text{ is precompact in }C^{m'}_{loc}
\text{ for every fixed }m'<m
}
\]

on fixed cylinders, after subsequence extraction.

---

## 3. Velocity gauge and local affine/harmonic part

Vorticity compactness alone does not determine velocity compactness because a curl-free/divergence-free harmonic or affine component can survive in a local frame.

This defect has already been audited.

- time-dependent constant velocity is an exact translating-frame gauge (M5-406);
- parent pointwise nonlocal strain escalation routes to normalized enstrophy mass and then to a remote active scale (M5-400--401);
- satellite ambient strain escalation routes to remote-of-remote activity (M5-402);
- nonzero affine detached limits force prelimit capacity/enstrophy escalation (M5-403--404).

Hence on a corridor which explicitly excludes

\[
C_{strong/deloc\,mass}
\lor H_{strong\,interface},
\]

the remaining local velocity-gradient/affine coefficients are bounded after the allowed gauge choice.

Standard local elliptic recovery from vorticity plus the bounded harmonic coefficients then makes

\[
\boxed{
\{U_j\}
\text{ locally precompact on every fixed normalized cylinder.}
}

---

## 4. Pressure is not an independent compactness defect on this corridor

The whole-space pressure satisfies

\[
p=\mathcal R_i\mathcal R_j(u_i u_j)
\]

up to the standard time-dependent scalar gauge.

The repository pressure audits show that under the retained Morrey/Type-I/derivative corridor, local pressure oscillation and pressure gradient are controlled by the same velocity/strain reservoirs; pressure escalation routes to derivative/remote throughput rather than a new compactness mechanism.

Therefore, once strong mass/remote/interface throughput is excluded, pressure does not produce an additional bounded-cluster state-novelty branch.

---

## 5. Consequence: bounded-cluster state novelty is not independent

Suppose there is a late sequence of source-bearing first-hitting states with

- bounded center displacement in natural units;
- no strong/delocalized critical mass escape;
- no strong interface/deformation exit;
- retained first-hitting analyticity.

Then the normalized Eulerian states are precompact on every fixed cylinder.

Thus

\[
\boxed{
C_{state\,novelty}^{bounded\ cluster}
\text{ cannot persist independently.}
}

Any genuine failure of state precompactness must be caused by one of the already typed noncompact directions:

\[
\boxed{
\text{growing spatial window}
\lor
\text{remote activity}
\lor
\text{relative-frequency escape}
\lor
\text{unbounded affine/strain/interface action}.
}
\]

These belong to `C_strong/deloc mass` or `H_strong interface`.

---

## 6. Apply to label-fresh recurrence

M5-426 splits a materially fresh source branch into Eulerian recurrence versus true state novelty.

The present result says that outside strong throughput, the state-novelty side is unavailable on bounded natural cylinders.

Therefore

\[
\boxed{
C_{bal}^{fresh}
\Longrightarrow
C_{Eulerian\,recurrent}
\lor
C_{strong/deloc\,mass}
\lor
H_{strong\,interface}.
}

The recurrent side enters the existing complete ancient orbit construction.

---

## 7. Apply to co-shrinking material skeletons

M5-425 shows that a persistent co-shrinking flux lineage may reduce to a zero-volume material skeleton, so fixed-volume material arguments cannot be used blindly.

But the Eulerian normalized source-bearing state around that skeleton is still subject to the same local analyticity/compactness mechanism.

Thus, if the co-shrinking main/source geometry remains in a bounded natural phase-space window and strong throughput is absent,

\[
\boxed{
C_{bal}^{co\text{-}shrink}
\Longrightarrow
C_{Eulerian\,recurrent}
\lor
C_{strong/deloc\,mass}
\lor
H_{strong\,interface}.
}

The zero-volume label skeleton does not create a new local Eulerian compactness class.

---

## 8. Recurrent branch enters the complete ancient W1/W2 dichotomy

The first-hitting center-nesting/time-scale construction gives expanding backward cylinders.

Local precompactness gives a nontrivial complete ancient limit carrying the first-hitting vorticity witness.

The existing master route is then

\[
\boxed{
C_{Eulerian\,recurrent}
\Longrightarrow
W_1\lor W_2.
}

For `W1`, the imported Albritton--Barker Liouville theorem yields the contradiction.

For `W2`, the failure of uniform weak-critical control routes to shell/frequency/Campanato/remote critical throughput, which after M5-399--424 belongs to

\[
C_{strong/deloc\,mass}
\lor H_{strong\,interface}.
\]

Hence

\[
\boxed{
C_{Eulerian\,recurrent}
\Longrightarrow
\bot
\lor
C_{strong/deloc\,mass}
\lor
H_{strong\,interface}.
}

---

## 9. What this does not prove

This note does not bound the global critical norm

\[
\|u(t)\|_{\dot H^{1/2}}.
\]

It does not exclude a sequence whose mass moves to expanding windows or increasingly remote/relative-frequency regions.

It does not prove that every strong-interface event creates a fixed amount of globally controlled Leray dissipation.

The gain is classification: there is no third mechanism in which a bounded natural cluster stays smooth, avoids strong throughput, but nevertheless keeps producing unrelated local normalized states forever.

---

## 10. Updated near-balanced reduction

Combining M5-425--427,

\[
\boxed{
C_{bal}^{co\text{-}shrink}
\lor
C_{bal}^{fresh}
}

reduces to

\[
\boxed{
C_{strong/deloc\,mass}
\lor
H_{strong\,interface}
\lor
C_{Eulerian\,recurrent}.
}

The recurrent branch returns to the ancient Liouville/W2 split.

Thus the truly surviving difficulty is increasingly concentrated in **critical noncompactness/strong throughput**, not in material-label genealogy by itself.

---

## 11. Audit verdict

### REMOVED AS INDEPENDENT QUIET MECHANISMS

- bounded-cluster critical-state novelty;
- label-fresh but Eulerian-compact recurrence as a separate final branch;
- co-shrinking label skeleton as a new local PDE class.

### SURVIVING

\[
\boxed{
C_{strong/deloc\,mass}
\lor
H_{strong\,interface}
}

plus the already known recurrent ancient route, which either contradicts or returns to those classes.

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
