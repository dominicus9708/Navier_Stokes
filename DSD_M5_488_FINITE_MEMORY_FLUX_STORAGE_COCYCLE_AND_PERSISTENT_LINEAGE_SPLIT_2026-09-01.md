# DSD M5-488 — Finite-memory flux storage yields a bounded cocycle with a persistent-lineage split

Date: 2026-09-01

Status: **R3 PARTIAL COCYCLE / THE M5-397 FINITE-MEMORY MULTIFLUX CAP CAN BE RECAST AS A BOUNDED INTEGER STORAGE POTENTIAL: EVERY FIXED-FLUX REPLACEMENT EITHER INCREASES THE NUMBER OF LOCALLY STORED COHERENT MATERIAL-FLUX LABELS OR PAYS A COMPENSATING VISCOUS-FLUX / PROJECTIVE-REORGANIZATION / EXPORT / NORMALIZED-ENSTROPHY EXIT / SUMMATION GIVES A CESARO COCYCLE INEQUALITY, SO POSITIVE-DENSITY REPLACEMENT FORCES POSITIVE-DENSITY COSTED EXITS / ON THE COMPACT NO-EXPORT NO-MASS-ESCAPE HULL, THE ONLY SURVIVORS ARE RECURRENT FLUX/PROJECTIVE COST OR ARBITRARILY LONG PERSISTENT FINITE-LINEAGE BLOCKS / THIS IS A GENUINE BOUNDED COCYCLE BUT NOT YET A CONTRADICTION BECAUSE THE COMPENSATING EXIT TERMS MAY THEMSELVES RECUR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs

M5-455 gives, on every quiet bounded-metric block, the dual-source alternative

\[
N_{metric}^{elliptic}
\Longrightarrow
G_{dual\ flux}^{metric}
\lor
H_{remote/derivative}^{strong}.
\]

M5-456 transports the material-flux genealogy through the bounded metric pullback:

\[
G_{dual\ flux}^{metric}
\Longrightarrow
R_{flux\ descendant}^{metric}
\lor
H_{metric\ diffusion/tilt}
\lor
T_{replacement/export}^{metric}.
\]

M5-397 proves a finite-memory theorem for repeated fixed-flux Taylor replacement on bounded normalized enstrophy.

M5-487 has now separated directional diffusion from direction Dirichlet energy and converted genuine directional-diffusion ratchet events into local weighted-tension spacetime charges.

The purpose here is to turn the finite-memory genealogy into an explicit bounded cocycle.

---

## 2. Local coherent flux-storage count

Work on a retained bounded normalized region and the bounded normalized-enstrophy branch

\[
Z_j\le Z_+.
\]

At generation/block `j`, let

\[
\boxed{
N_j
:=
\text{number of distinguishable coherent fixed-flux material populations stored locally}.
}
\]

The M5-397 multiflux packing theorem gives a uniform cap

\[
\boxed{
0\le N_j\le N_{max}<\infty.
}
\]

The count is only used after the fixed angular-sector partition and fixed flux threshold of the finite-memory theorem have been imposed.

Thus no claim is made that arbitrary infinitesimal material labels are countable in this manner.

---

## 3. Replacement and compensating-exit indicators

Let

\[
R_j\in\{0,1\}
\]

indicate a fixed-deficit replacement event that creates a new material flux population of size at least `c_rep nu`.

Let

\[
X_j\in\{0,1\}
\]

indicate that during the same step/block at least one finite-memory compensating exit occurs:

\[
\boxed{
X_j=1
\Longleftrightarrow
\begin{cases}
\text{fixed old-flux viscous change/loss},\\
\text{projective/noncoherent reorganization},\\
\text{export/remote loss},\\
\text{or }Z>Z_+.
\end{cases}
}
\]

If `R_j=1` and `X_j=0`, the new fixed-flux label is added while all previous stored populations survive coherently and locally.

Therefore

\[
\boxed{
R_j=1,\ X_j=0
\Longrightarrow
N_{j+1}\ge N_j+1.
}
\]

---

## 4. One-step bounded cocycle inequality

When `X_j=1`, the storage count may decrease, but because

\[
0\le N_j,N_{j+1}\le N_{max},
\]

its downward jump is at worst `N_max`.

Hence all cases are covered by

\[
\boxed{
N_{j+1}-N_j
\ge
R_j-N_{max}X_j.
}
\]

This is the finite-memory storage cocycle.

It is not an ansatz: it is a compressed form of the M5-397 case split.

---

## 5. Cesaro balance

Sum from `j=0` to `M-1`:

\[
N_M-N_0
\ge
\sum_{j=0}^{M-1}R_j
-
N_{max}
\sum_{j=0}^{M-1}X_j.
\]

Therefore

\[
\frac1M\sum_{j=0}^{M-1}R_j
\le
N_{max}
\frac1M\sum_{j=0}^{M-1}X_j
+
\frac{N_M-N_0}{M}.
\]

Since `N_j` is uniformly bounded,

\[
\frac{N_M-N_0}{M}\to0.
\]

Thus

\[
\boxed{
\overline d(R)
\le
N_{max}\,\overline d(X)
}
\]

for every common limiting/Cesaro subsequence for which the densities exist; the analogous limsup inequality holds without assuming existence of the limits.

Consequently

\[
\boxed{
\text{positive-density replacement}
\Longrightarrow
\text{positive-density compensating exits}.
}
\]

This is the exact bounded-drift statement sought from the finite-memory mechanism.

---

## 6. Invariant-measure form

Include `N,R,X` in the M5-485 marked generation state.

For any invariant measure obtained from empirical averages of the original orbit, the telescoping storage term has zero mean. Therefore the cocycle inequality gives

\[
\boxed{
\langle R\rangle
\le
N_{max}\langle X\rangle.
}
\]

This is weaker than the ideal M5-485 contradiction

\[
\Phi\circ\sigma-\Phi\ge c a_{ratchet},
\]

because here there is a compensating nonnegative defect term.

But it identifies exactly what must pay for recurrent replacement.

---

## 7. Remove already-typed strong/noncompact exits

On the compact endpoint under audit, exclude

\[
H_Z,
\qquad
H_{remote/derivative}^{strong},
\qquad
T_{export/remote}
\]

as separate strong/noncompact branches.

Then the compensating-exit indicator reduces to

\[
\boxed{
X_j
\subset
X_{visc\ flux,j}
\lor
X_{proj,j}.
}
\]

Hence

\[
\boxed{
\langle R\rangle>0
\Longrightarrow
\langle X_{visc\ flux}\rangle
+
\langle X_{proj}\rangle
>0.
}
\]

Thus positive-density material replacement cannot be a quiet process on the compact bounded hull.

It must feed recurrent flux diffusion/loss or recurrent projective reorganization.

---

## 8. Relation to M5-487 charges

The projective exit branch has two submechanisms from the direction equation:

\[
\text{tilt}
\quad\text{or}\quad
\text{directional diffusion}.
\]

On the compact analytic carrier, M5-487 turns these into actual local spacetime charges:

\[
C_{tilt}
\sim
\int\rho^2|\tau|^2,
\]

or

\[
C_{tension}
\sim
\int\rho^2|\mathcal D_\xi|^2.
\]

Therefore a positive-density projective compensating exit produces a positive invariant mean of at least one of these thickened projective charges.

The viscous-flux branch is retained separately because scalar material-flux change is not identical to projected directional diffusion.

---

## 9. Zero/vanishing replacement density leads to persistent-lineage blocks

Suppose instead that replacement has zero asymptotic density along a selected invariant/ergodic component:

\[
\langle R\rangle=0.
\]

Then the generation sequence contains arbitrarily long intervals with no fixed-deficit replacement.

Otherwise a uniform upper bound `L` on replacement-free gaps would imply at least one replacement in every `L+1` generations and therefore positive lower density.

Thus there exist blocks

\[
[j_k,j_k+L_k],
\qquad
L_k\to\infty,
\]

on which no new fixed-flux material population is created by replacement.

Within each such block, any locally retained coherent dual-source population must be represented by descendants of a finite pre-existing label set, unless a flux/projective/export exit occurs.

After excluding export/strong branches, the remaining no-replacement compact lane is therefore a **persistent finite-lineage corridor** modulo recurrent flux/projective costs.

---

## 10. Persistent-lineage extraction

Because the local storage capacity is at most `N_max`, only finitely many coherent fixed-flux labels are present at the beginning of each long no-replacement block.

If every label disappeared within at most `L_*` generations through a costed local exit, then every sufficiently long block would contain a positive frequency of such exits.

Therefore the no-replacement branch has the split

\[
\boxed{
\text{long no-replacement block}
\Longrightarrow
\text{long-lived material-flux descendant lineage}
\lor
\text{positive-frequency flux/projective exits}.
}
\]

Diagonalizing blocks with length tending to infinity yields, on the quiet subbranch, a complete persistent material-flux lineage inside the limiting marked dilation hull.

This lineage is scale critical because vorticity flux is invariant under the Navier--Stokes parabolic scaling.

---

## 11. Signed flux evolution on a persistent lineage

For a selected material surface patch `S(t)` of one persistent lineage, M5-393/456 gives the exact identity

\[
\boxed{
\frac d{dt}
\Phi(t)
=
\int_{S(t)}
\Delta\omega\cdot n\,dA
}
\]

in ordinary isotropic variables, with the corresponding uniformly elliptic diffusion operator in the metric pullback.

The stretching term cancels exactly against material-area deformation.

Therefore longitudinal stretching cannot silently change the scalar material-vorticity flux.

Any scalar flux change on the persistent lineage is genuinely viscous/diffusive or accompanies loss of the retained material comparison.

---

## 12. Zero signed mean does not imply zero flux variation

Let `Phi_j` be the normalized scale-critical flux of a persistent descendant sampled once per generation.

On the compact corridor it is bounded:

\[
|\Phi_j|\le\Phi_*.
\]

Define the signed increment

\[
d_j:=\Phi_{j+1}-\Phi_j.
\]

Then

\[
\frac1M\sum_{j=0}^{M-1}d_j
=
\frac{\Phi_M-\Phi_0}{M}
\to0.
\]

Hence every recurrent persistent-lineage component has

\[
\boxed{
\langle d\rangle=0.
}
\]

However this does **not** imply

\[
\langle|d|\rangle=0.
\]

The scalar flux may undergo recurrent sign-cancelling diffusive variation.

Thus bounded flux itself is not a strict Lyapunov observable.

This is another anti-shortcut firewall.

---

## 13. DSD formation-level interpretation

The finite-memory storage descriptor is a bounded state variable.

Repeated formation of a genuinely new fixed-flux material population has positive drift in this descriptor.

Because the descriptor cannot grow indefinitely, the drift must be discharged through one of the explicitly typed structural exits.

Thus the correct general statement is

\[
\boxed{
\text{new-label formation}
=
\text{bounded storage drift}
+
\text{costed structural discharge}.
}
\]

This is precisely the kind of formation/descendant distinction that the DSD audit is intended to preserve.

---

## 14. Updated compact-hull split

Combining M5-486--488, the non-strong compact endpoint now satisfies

\[
\boxed{
E_{dual}^{marked}
\Longrightarrow
E_{persistent}^{lineage}
\lor
E_{cost}^{flux/projective},
}
\]

while every invariant component still has

\[
\langle Q\rangle>0
\]

from similarity enstrophy balance.

On `E_cost^{flux/projective}`, one additionally has positive mean viscous-flux change and/or M5-487 thickened tilt/tension charge.

On `E_persistent^{lineage}`, a finite set of scale-critical material-flux descendants survives through arbitrarily many generations and, after diagonal extraction, through the complete dilation hull.

---

## 15. Highest-value next target

The next calculation should attack the persistent-lineage branch because finite-memory has already converted repeated replacement into costed exits.

Two concrete questions remain.

### P1 — persistent-lineage similarity law

Write the material-surface flux identity directly in backward similarity coordinates and determine the exact damping/transport terms for a scale-critical persistent flux observable.

If the normalized flux becomes an exact bounded coboundary plus a nonnegative diffusion defect, this would supply the missing strict cocycle.

### P2 — recurrent cost balance

If the similarity flux law is sign-indefinite, combine it with the M5-486 positive axial-production identity and the M5-487 positive tilt/tension charge to determine the minimum forcing required to sustain zero-mean recurrent flux diffusion.

The key issue is now **persistent recurrent regeneration**, not creation of indefinitely many new flux labels.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
