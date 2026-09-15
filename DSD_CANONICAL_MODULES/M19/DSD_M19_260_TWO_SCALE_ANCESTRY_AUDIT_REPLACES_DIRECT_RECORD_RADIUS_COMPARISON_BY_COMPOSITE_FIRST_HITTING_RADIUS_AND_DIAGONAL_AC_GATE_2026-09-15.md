# DSD M19-260 — Two-scale ancestry audit replaces direct record-radius comparison by the composite first-hitting radius and a diagonal ancestry-conversion gate

Date: 2026-09-15  
Canonical ID: **M19-260**  
Status: **ACTIVE CORRECTION / TWO-SCALE REPRESENTATION AUDIT / M19-256 SCALING IDENTITY RETAINED / M19-257--259 DIRECT RECORD-RADIUS COMPARISON SUPERSEDED / DIAGONAL ANCESTRY-CONVERSION + INCIDENCE GATE OPEN**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-256 correctly recomputed the physical parabolic derivative scaling

\[
\int_{Q_r}|D_x^k\omega|^2dxdt
=
r^{1-2k}
\int_{Q_1}|\nabla_y^k\omega^{(r)}|^2dyds.
\]

M19-257--259 then wrote the M17 record parameter `R_m` as though it were directly a small physical GMS shell radius.

The historical M17 definition is different. M5-478 and M17-307 define

\[
R_m^{bd}=\sqrt{T_m},
\qquad
T_m\asymp q^m,
\qquad
R_m^{bd}\asymp q^{m/2}\to\infty,
\]

where `R_m^{bd}` is a **backward record blow-down factor**, not a physical radius tending to zero.

Therefore the direct comparison

\[
R_m\asymp r_j
\]

used abstractly in M19-257--259 is not representation-safe for the actual historical M17 symbol.

The purpose of this module is to restore the exact two-scale composition.

---

## 2. First-hitting physical base scale

At first-hitting stage `j`, let the physical/natural scale be

\[
r_j=W_j^{-1/2},
\qquad
W_{j+1}=qW_j,
\]

so

\[
\boxed{
\frac{r_{j+1}}{r_j}=q^{-1/2}.
}
\]

A stage-normalized vorticity has the schematic exact scaling form

\[
\Omega_j(y,s)
=
r_j^2\,
\omega\!\left(X_j+r_jy,\ t_j+r_j^2s\right),
\]

up to the fixed viscosity/time normalization already used in the first-hitting modules.

Thus `r_j` is the small physical scale.

---

## 3. Backward record factor is a second scale

Inside a normalized first-generation ancient/stage field, a backward age-`k` record uses a large factor

\[
K_k\asymp q^{k/2}.
\]

M5-478/M17-307 denote the corresponding large record factor by `R_m`; here it is renamed

\[
R_m^{bd}
\]

to prevent collision with a physical radius.

The record blow-down has the schematic form

\[
\widetilde\Omega_{j,k}(z,\tau)
=
K_k^2
\Omega_j\!\left(a_{j,k}+K_k z,\ \sigma_{j,k}+K_k^2\tau\right).
\]

Composing the two scalings gives

\[
\widetilde\Omega_{j,k}
=
(r_jK_k)^2
\omega(\text{translated point}+r_jK_k z,\ \text{translated time}+(r_jK_k)^2\tau).
\]

Therefore the actual physical radius represented by the record is

\[
\boxed{
\rho_{j,k}:=r_jK_k.
}
\]

The existing ancestor-radius identity gives more sharply

\[
\boxed{
\rho_{j,k}=r_jK_k=r_{j-k}.
}
\]

Hence the historical large blow-down factor and the small physical radius must never be identified directly.

---

## 4. Exact derivative-weight composition

For raw vorticity `H2`, let

\[
H_{j,k}^{rec}
:=
\int_{Q_1}|D_z^2\widetilde\Omega_{j,k}|^2dzd\tau.
\]

The M17 backward-record pullback inside the stage-normalized parent is

\[
\boxed{
K_k^{-3}H_{j,k}^{rec}.
}
\]

Returning the stage-normalized parent to physical variables contributes the first-hitting base factor

\[
r_j^{-3}.
\]

Thus the complete physical cost is

\[
\boxed{
r_j^{-3}K_k^{-3}H_{j,k}^{rec}
=
(r_jK_k)^{-3}H_{j,k}^{rec}
=
\rho_{j,k}^{-3}H_{j,k}^{rec}.
}
\]

This is the correct sense in which the M17 ancestry exponent matches the physical parabolic exponent.

Therefore:

\[
\boxed{
\text{M19-256 exponent calculation is valid},
}
\]

but only after the **two scaling stages are composed**.

The historical M17 statement

\[
\sum_kK_k^{-3}H_{j,k}^{rec}<\infty
\]

is a normalized-parent ancestry ledger. It is not, by itself, the physical statement

\[
\sum_n r_n^{-3}H_n^{phys}<\infty
\]

uniformly through the singular limit.

---

## 5. Correction to M19-257--259

M19-257's abstract algebraic theorem remains valid if its record radius `R_m` is **explicitly redefined as a composite physical radius**.

It is not valid to substitute the historical M17 blow-down factor `R_m^{bd}` directly into

\[
\Lambda^{-1}r_j\le R_m\le\Lambda r_j.
\]

Likewise, M19-259's generic cofinal-radius test

\[
R_m\to0
\]

does not describe the historical M17 record parameter, because

\[
R_m^{bd}\to\infty.
\]

Accordingly, the M19-259 `scale-density` question is superseded in its direct one-index form.

The correct radius variable is

\[
\rho_{j,k}=r_jR_k^{bd}.
\]

---

## 6. Spatial scale density is already built into the two-index identity

Because

\[
\rho_{j,k}=r_{j-k},
\]

the available composite radii lie on the same geometric first-hitting lattice

\[
r_n\asymp q^{-n/2}.
\]

Hence there is no independent arbitrary sparse-radius phenomenon **provided the required pairs `(j,k)` remain available**.

For the full first-hitting family,

\[
\boxed{
\sup_n\log\frac{r_n}{r_{n+1}}
=
\frac12\log q<\infty.
}
\]

Thus the abstract counterexample

\[
R_m=2^{-2^m}r_0
\]

from M19-259 is a valid warning for an arbitrary cofinal sequence, but it is not the intrinsic scale law of the canonical first-hitting family.

However an **arbitrarily sparse compactness subsequence** can still skip first-hitting generations. M5-478 passes to subsequences to obtain center convergence and an ancient limit. Such a subsequence does not automatically preserve bounded index gaps.

Therefore the possible gap is not a primitive physical scale gap; it is a **selection/ancestry gap**.

---

## 7. The actual new transfer gate is diagonal ancestry conversion

Let `n` denote the target physical GMS shell index.

Since

\[
\rho_{j,k}=r_{j-k},
\]

a record represents the physical shell `n` precisely when

\[
\boxed{
j-k=n.
}
\]

The correct bridge must therefore select a diagonal family

\[
(j_n,k_n),
\qquad
j_n-k_n=n,
\]

with the late-branch hypotheses retained.

Define

\[
\boxed{
\mathcal T_{GMS}^{diag-AC}
}
\]

to mean that, for all sufficiently small target shells, one can choose such a diagonal family satisfying:

1. **branch eligibility:** the selected record lies in the M17/CE-H branch actually carrying the certified derivative ledger;
2. **representation coherence:** the record is the same untruncated whole-space field, or all cutoff/interface terms are separately paid;
3. **center incidence:** after composition, the physical record lies within a fixed enlargement of one fixed Galilean cylinder family;
4. **time incidence:** the composed record window occupies the required parabolic-time shell rather than merely touching it at one instant;
5. **bounded ancestry reuse:** the same finite ancestral derivative charge is not counted through infinitely many different base stages;
6. **selection non-sparsity or substitute:** if a limit/subsequence is required, it either has controlled first-hitting gaps or another prelimit/uniform theorem supplies the skipped shells.

This is the corrected transfer problem.

---

## 8. Why fixing the record age does not automatically solve it

One could formally set `k_n=k_0` fixed and `j_n=n+k_0`, which preserves every physical first-hitting shell.

But the late CE-H structure may have been obtained only after a remote-age/ancient-limit extraction.

Thus a fixed finite age cannot silently inherit every asymptotic CE-H property.

Conversely, choosing

\[
k_n\to\infty
\]

to access the late ancient structure requires

\[
j_n=n+k_n\to\infty
\]

and creates the genuine diagonal ancestry problem.

Therefore

\[
\boxed{
\text{late ancient rigidity}
+
\text{all physical shell coverage}
}
\]

must be proved simultaneously rather than by identifying one record index with one physical radius.

---

## 9. Relation to M18 center and genealogy audits

M18-043 already gives the center split

\[
G_{center\ turnover}
\Longrightarrow
G_{center\ nesting}
\lor
S_{remote}^{formed},
\]

and on the nested branch

\[
|X_*-X_j|\lesssim r_j.
\]

Thus the purely spatial center part of incidence is substantially controlled on the non-remote branch.

M18-045 gives the stronger warning that the remaining genealogy/contact problem is **temporal**:

\[
\text{instantaneous contact}
\not\Rightarrow
\text{sufficient ancestral physical return weight}.
\]

Its weighted return density remains

\[
\mathfrak R_k
=
\rho_k^{-1}\sum_\ell\tau_{k,\ell},
\]

and a current-epoch `O(1)` similarity dwell loses the remote-age factor `q^{-k}`.

Therefore the M19 `incidence` gate should be decomposed into

\[
\boxed{
\mathcal T_{GMS}^{incidence}
=
\mathcal T_{center}
+
\mathcal T_{time-return}
+
\mathcal T_{diag-AC}.
}
\]

The center component is routed by M18-043 versus the remote root. The temporal/diagonal components remain open.

---

## 10. Revised conditional GMS closure

The M19-254--255 analytic endpoint remains valid:

\[
D^3u\in L^2_{loc}
\Longrightarrow
u\in L^6_{x,t},
\qquad
p\in L^3_{x,t},
\qquad
\mathcal P_{GMS}^{log}(V)<\infty,
\]

contradicting the singular-point logarithmic payer.

But the input must now be written as a **physical composite transfer**, not as a direct M17-record-radius identification.

A corrected sufficient complex is

\[
\boxed{
\mathcal T_{GMS}^{diag-AC}
+
\mathcal T_{GMS}^{time-return}
+
\mathcal T_{GMS}^{repr}
+
\mathcal T_{GMS}^{root}.
}
\]

On the center-nested non-remote branch, no additional primitive spatial scale-density gate is required: the composite radius is already the first-hitting scale `r_{j-k}`.

---

## 11. Permanent firewalls after M19-260

\[
\boxed{
\text{M17 blow-down factor }R_m^{bd}
\neq
\text{small physical shell radius}.
}
\]

\[
\boxed{
\text{matching derivative exponent}
\neq
\text{uniform physical transfer without the base scale}.
}
\]

\[
\boxed{
\rho_{j,k}=r_jR_k^{bd}=r_{j-k}
\quad\text{must be used before any scale comparison}.
}
\]

\[
\boxed{
\text{full geometric first-hitting family}
\neq
\text{arbitrary compactness subsequence}.
}
\]

\[
\boxed{
\text{instantaneous material contact}
\neq
\text{parabolic spacetime incidence/return weight}.
}
\]

\[
\boxed{
\text{conditional CE-H/GMS closure}
\neq
\text{ROOT-CERT or global regularity}.
}
\]

---

## 12. Immediate next target

Audit exactly where the late CE-H hypotheses become valid relative to the M5-478 record sequence:

\[
\boxed{
\text{Are the CE-H/raw-H2 hypotheses uniform on the full geometric prelimit record family,}
}
\]

or do they hold only after an arbitrary subsequential ancient-limit extraction?

- If they are uniform before taking the limit, use the full geometric first-hitting family and construct the diagonal map `j-k=n` directly.
- If they are only subsequential, prove a bounded-gap/syndetic return theorem for the selected CE-H states, or retain an explicit **subsequence ancestry-gap** survivor.

After that, combine the result with M18-045's temporal return-weight frontier to test the actual GMS spacetime-incidence theorem.

Global 3D Navier--Stokes regularity remains unproved.
