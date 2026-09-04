# DSD M17-119 — Director-area ribbon flux gives a quantitative annular dissipation lower bound and reduces M5 amplitude retention to flux capture

Date: 2026-09-05
Canonical ID: **M17-119**

Status: **INTERNAL M17-TO-M5 AMPLITUDE-RETENTION BRIDGE / FOR A COMPACT NONDEGENERATE RANK-TWO RIBBON BUNDLE AT FIRST-HITTING SCALE `r_j`, THE FROZEN DIRECTOR-AREA FLUX PROVIDES AN EXACT FLUX-COORDINATE DECOMPOSITION OF PHYSICAL VOLUME. USING `|grad u|^2>=|omega|^2/2`, THE PARABOLIC SCALING `rho_phys=r_j^-2 rho_sim`, `J_phys=r_j^-2 J_sim`, `ds_phys=r_j ds_sim`, AND COMPACT LOWER/UPPER BOUNDS ON `rho_sim`, `J_sim`, AND CIRCULAR-FIBER LENGTH, ONE OBTAINS `int_T |grad u|^2 dx >= c_* r_j^-1 Phi_J(T)`. FOR AN AGE-k ANNULUS AT PHYSICAL RADIUS `rho_k=r_j K_k=r_{j-k}`, THIS BECOMES `rho_k int_T |grad u|^2 dx >= c_* K_k Phi_k`. THEREFORE THE M5 SHELL AMPLITUDE/COMPARABILITY PREMISE `rho_k int_A |grad u|^2 >= c_0 J_k` WOULD FOLLOW IF THE RIBBON FLUX CAPTURES THE ANNULAR MASS IN THE QUANTITATIVE SENSE `J_k <= C K_k Phi_k`. THIS IS A REAL AMPLITUDE BRIDGE. IT DOES NOT SUPPLY THE MISSING PHYSICAL DWELL/RETURN-DENSITY LOWER BOUND, AND `Phi_k >= J_k/(C K_k)` MAY STILL BE SUMMABLE BECAUSE OF THE REMOTE-AGE `K_k` FACTOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Physical ribbon bundle and director-area flux

Consider a compact nondegenerate ribbon tube bundle `T_k` at first-hitting stage `j`.
Let

\[
\boxed{
\Phi_k
:=\int_{\Lambda_k}d\Phi_J
}
\]

be its director-area flux.

The flux is scale invariant because

\[
J_{phys}=r_j^{-2}J_{sim}
\]

and transverse area scales by `r_j^2`.

Use flux coordinates along the kernel fibers:

\[
\boxed{
dV_{phys}
=d\Phi_J\frac{ds_{phys}}{|J_{phys}|}.}
\]

---

## 2. Compact similarity bounds

Assume on the retained ribbon bundle

\[
\boxed{
\rho_{sim}\ge c_\rho>0,
}
\]

\[
\boxed{
|J_{sim}|\le C_J<\infty,
}
\]

and

\[
\boxed{
|q|\le C_q<\infty.
}
\]

A complete ribbon fiber is a circle with similarity length

\[
L_{sim}=\frac{2\pi}{|q|}.
\]

Therefore

\[
\boxed{
L_{sim}\ge L_0:=\frac{2\pi}{C_q}>0.
}
\]

These are standard compact nondegeneracy assumptions for the ribbon subbranch; no lower bound on physical size is imposed independently of scaling.

---

## 3. Velocity-gradient dissipation controls vorticity

For incompressible velocity,

\[
\nabla u=\Sigma+\Omega
\]

with symmetric and antisymmetric parts orthogonal in Frobenius norm.
The antisymmetric part satisfies

\[
|\Omega|^2=\frac12|\omega|^2.
\]

Hence pointwise

\[
\boxed{
|\nabla u|^2
=|\Sigma|^2+|\Omega|^2
\ge\frac12|\omega|^2.
}
\]

Write

\[
|\omega|=\rho_{phys}.
\]

---

## 4. Dissipation per unit director-area flux

Integrate over the ribbon bundle:

\[
\begin{aligned}
\int_{\mathcal T_k}|\nabla u|^2dx
&\ge
\frac12
\int_{\mathcal T_k}\rho_{phys}^2dx\\
&=\frac12
\int_{\Lambda_k}d\Phi_J
\oint
\frac{\rho_{phys}^2}{|J_{phys}|}
\,ds_{phys}.
\end{aligned}
\]

Use the parabolic scaling

\[
\rho_{phys}=r_j^{-2}\rho_{sim},
\]

\[
J_{phys}=r_j^{-2}J_{sim},
\]

\[
ds_{phys}=r_jds_{sim}.
\]

Therefore

\[
\frac{\rho_{phys}^2}{|J_{phys}|}ds_{phys}
=
 r_j^{-1}
\frac{\rho_{sim}^2}{|J_{sim}|}ds_{sim}.
\]

With the compact bounds,

\[
\oint
\frac{\rho_{sim}^2}{|J_{sim}|}ds_{sim}
\ge
\frac{c_\rho^2}{C_J}L_0.
\]

Hence

\[
\boxed{
\int_{\mathcal T_k}|\nabla u|^2dx
\ge
c_*\,r_j^{-1}\Phi_k,
}
\]

where

\[
\boxed{
c_*:=\frac{c_\rho^2L_0}{2C_J}
=\frac{\pi c_\rho^2}{C_JC_q}.}
\]

---

## 5. Insert the ancestor physical radius

The existing M5 ancestor-radius identity gives for age `k`

\[
\boxed{
\rho_k
=r_jK_k
=r_{j-k}.
}
\]

Multiply Section 4 by `rho_k`:

\[
\boxed{
\rho_k
\int_{\mathcal T_k}|\nabla u|^2dx
\ge
c_*K_k\Phi_k.
}
\]

This is the quantitative annular critical-dissipation content forced by a ribbon bundle of director-area flux `Phi_k`.

---

## 6. Bridge to the M5 shell-amplitude premise

The M5 weighted return-density ledger assumes on a tracked shell that

\[
\rho_k
\int_{A_{k,\ell}(t)}
|\nabla u|^2dx
\ge
c_0J_k.
\]

Section 5 shows that the ribbon geometry supplies this premise whenever

\[
\boxed{
J_k
\le
C_{cap}K_k\Phi_k
}
\]

for a uniform capture constant `C_cap` and the ribbon bundle stays inside the tracked comparable shell.

Indeed then

\[
\rho_k\int|\nabla u|^2
\ge
\frac{c_*}{C_{cap}}J_k.
\]

Thus the unresolved **amplitude retention** question is reduced to a flux-capture statement:

\[
\boxed{
\text{does the relevant Rank-2 ribbon flux satisfy }
K_k\Phi_k\gtrsim J_k
\text{ on a cubic-divergent subset?}
}
\]

---

## 7. Why this does not yet imply a flux contradiction

The capture condition gives only

\[
\Phi_k
\gtrsim
\frac{J_k}{K_k}.
\]

Even if

\[
\sum J_k^{3/2}=\infty,
\]

the factor

\[
K_k^{-1}=q^{-k/2}
\]

may make

\[
\sum\frac{J_k}{K_k}
\]

finite.

Thus the total amount of fresh director-area flux needed across ages need not diverge merely from the cubic annular ledger.

No global director-area reservoir contradiction follows at this stage.

---

## 8. Dwell remains the independent missing ingredient

Even when Section 6 supplies the instantaneous shell lower bound, the M5 weighted return argument also needs enough physical return duration:

\[
\mathfrak R_k
=\frac1{\rho_k}
\sum_\ell\tau_{k,\ell}.
\]

M17-117--118 show that an `O(1)` current similarity dwell gives only the remote-age-suppressed contribution

\[
\frac{\tau}{\rho_k}
\asymp
\frac{\rho_k}{K_k^2}.
\]

Therefore amplitude capture and temporal return density are distinct obligations.

---

## 9. New precise M17-to-M5 bridge

The remaining ribbon-to-energy closure is now split into two explicit statements:

### Flux capture

\[
\boxed{
K_k\Phi_k\gtrsim J_k.
}
\]

### Physical return density

\[
\boxed{
\mathfrak R_k\gtrsim J_k^{1/2}
}
\]

on a subset still satisfying

\[
\sum J_k^{3/2}=\infty.
\]

If both are obtained under bounded overlap, the existing M5 Leray ledger gives the contradiction.

---

## 10. DSD analysis

Director-area flux and annular dissipation are different descriptors, but the flux-coordinate volume formula gives a legitimate bridge because both are evaluated on the same physical ribbon bundle.

The bridge is quantitative rather than identificatory:

\[
\boxed{
\Phi_k
\to
\text{minimum shell dissipation content}
}
\]

under compact amplitude and geometry bounds.

This is stronger and safer than declaring `Phi_k` itself to be the M5 annular mass.

---

## 11. DSD audit

### Audit A — identifying director-area flux with J_k
Rejected. Only an inequality through physical dissipation is derived.

### Audit B — forgetting the age factor K_k
Rejected; it appears explicitly in `rho_k=r_jK_k`.

### Audit C — claiming cubic divergence forces infinite total ribbon flux
Rejected because `K_k^-1` can make the required flux summable.

### Audit D — treating amplitude capture as dwell
Rejected. The temporal return-density theorem remains independent.

### Audit E — proof status
A quantitative instantaneous amplitude bridge is proved conditionally on compact ribbon bounds and shell containment, but the decisive temporal genealogy remains open.

---

## 12. Updated ribbon energy frontier

The Eulerian ribbon-turnover branch now reduces to

\[
\boxed{
\begin{aligned}
&K_k\Phi_k\gtrsim J_k,\\
&\mathfrak R_k\gtrsim J_k^{1/2},\\
&\sum J_k^{3/2}=\infty
\end{aligned}
\quad\Longrightarrow\quad
\text{M5 Leray contradiction},
}
\]

with the first line now tied directly to director-area geometry and the second still missing.

The next highest-value question is whether the exact one-way material aging of `mathscr V_J` forces enough repeated occupation of the ancestral physical scale `r_{j-k}` to improve the `K_k^-2` dwell loss. If not, the ribbon turnover survivor remains a sparse nested cascade.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
