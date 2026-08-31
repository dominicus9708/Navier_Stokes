# DSD M5-425 — Co-shrinking lineage: zero-volume skeleton firewall

Date: 2026-08-31

Status: **ANTI-OVERCLAIM AUDIT / AN INDEFINITELY CO-SHRINKING MATERIAL-FLUX LINEAGE NEED NOT CARRY A FIXED POSITIVE 3D MATERIAL VOLUME / THE ACTIVE OLD-MATERIAL LABEL SET MAY SHRINK LIKE `q^{-3L/2}` AND HAVE ZERO 3D MEASURE IN THE INFINITE-GENERATION INTERSECTION / THEREFORE FIXED-VOLUME FILAMENT OR AFFINE CAPACITY THEOREMS SUCH AS M5-354 CANNOT BE APPLIED TO THE BARE CO-SHRINKING FLUX SKELETON WITHOUT AN ADDITIONAL THICKNESS/PERSISTENT-OCCUPANCY HYPOTHESIS / THE CORRECT TARGET IS A SURFACE/FILAMENT SKELETON RIGIDITY OR A PROOF THAT ANY THICKENING FORCES FRESH HANDOFF/INTERFACE ACTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let the geometric first-hitting levels satisfy

\[
W_{j+1}=qW_j,
\qquad
r_j=\sqrt{\nu/W_j},
\qquad q>1.
\]

Hence

\[
\boxed{r_{j+L}=q^{-L/2}r_j.}
\]

At stage `j`, let `C_j` be a formed natural Taylor/source carrier with

\[
|C_j|\asymp r_j^3.
\]

Let

\[
A_j(t)=\Phi_{t_j,t}(C_j)
\]

be its material image under the smooth incompressible flow map.

Incompressibility gives

\[
\boxed{|A_j(t)|=|C_j|\asymp r_j^3}
\]

for every pre-singular time.

---

## 2. Active old-material subset at a later generation

Suppose the stage-`j+L` natural carrier is supplied entirely or partly by material labels descending from `C_j`.

Define the old-material part of the later carrier

\[
E_{j,L}
:=
C_{j+L}\cap A_j(t_{j+L}).
\]

Regardless of whether the contact fraction is close to one,

\[
|E_{j,L}|
\le
|C_{j+L}|.
\]

Therefore

\[
\boxed{
|E_{j,L}|
\lesssim
r_{j+L}^3
=
q^{-3L/2}r_j^3.
}
\]

Pull this set back to the initial labels:

\[
\widetilde E_{j,L}
:=
\Phi_{t_j,t_{j+L}}^{-1}(E_{j,L})
\subset C_j.
\]

Since the flow is volume preserving,

\[
\boxed{
|\widetilde E_{j,L}|
=|E_{j,L}|
\lesssim q^{-3L/2}r_j^3.
}
\]

Thus the set of initial material labels that are still inside the later natural active carrier shrinks geometrically in 3D measure.

---

## 3. Infinite-generation intersection may have zero volume

Consider labels that remain active along every retained generation:

\[
E_{j,\infty}
:=
\bigcap_{L\ge1}
\widetilde E_{j,L}
\]

(or the corresponding limsup/selected descendant set when the active subsets are not literally nested).

For the nested case, continuity from above gives

\[
|E_{j,\infty}|
\le
\lim_{L\to\infty}
|\widetilde E_{j,L}|
=0.
\]

More generally, any indefinitely retained descendant family whose active volume is bounded by the current natural carrier has no reason to preserve a positive generation-independent 3D material measure.

Hence

\[
\boxed{
\text{indefinite co-shrinking activity}
\not\Longrightarrow
\text{fixed positive-volume material population}.
}
\]

The surviving material object may be a surface, filament, Cantor-like label skeleton, or another zero-volume descendant set.

---

## 4. Why persistent flux is compatible with zero volume

M5-393 deliberately tracks vorticity flux through a material surface rather than a material volume.

A material surface has zero 3D volume but can carry nonzero vorticity flux

\[
\Phi
=
\int_{S(t)}\omega\cdot n\,dA
\asymp\nu.
\]

Therefore the conclusions

\[
|E_{j,\infty}|=0
\]

and

\[
\Phi_{j\to\infty}\asymp\nu
\]

are not contradictory.

This is exactly why volume-contact and flux-ancestry were separated in M5-393.

---

## 5. M5-354 scope firewall

M5-354 derives a strong spatial/energy requirement for a **fixed coherent material population of volume**

\[
V_{mat}>0.
\]

Its rank-two affine estimate contains

\[
E_{aff}
\gtrsim
\frac{\sigma_1\sigma_2V_{mat}^2}{L}.
\]

The factor `V_mat^2` is essential.

If the active co-shrinking descendant volume itself tends to zero like

\[
q^{-3L/2},
\]

the fixed-volume hypothesis is absent.

Therefore the implication

\[
\text{co-shrinking flux lineage}
\Longrightarrow
\text{M5-354 fixed-volume filament escape}
\]

is not justified without an additional persistent-thickness or persistent-volume hypothesis.

---

## 6. What remains usable from M5-393

The material-surface area contraction remains valid for a genuine fixed-flux descendant:

\[
\boxed{
\frac{|S_j^L|}{|S_j^0|}
\lesssim q^{-L}.
}
\]

Hence complementary deformation still forces

\[
\boxed{
\sigma_1(D\Phi_{t_j,t_{j+L}})
\gtrsim q^L
}
\]

at at least one retained surface point, and

\[
\int_{t_j}^{t_{j+L}}
\|\nabla u\|_\infty dt
\ge
L\log q-O(1).
\]

But this is a **surface/deformation** statement, not a fixed-volume energy contradiction.

---

## 7. Correct co-shrinking target

The remaining `C_bal^{co-shrink}` branch must therefore be attacked at one of three genuinely compatible levels:

1. **surface skeleton rigidity** — show that an `O(nu)` material flux surface cannot contract at the first-hitting rate forever while remaining an efficient misaligned source;
2. **thickening/noncollapse theorem** — prove that analyticity/flux coherence forces a generation-independent material thickness around the surface, which would restore a fixed-volume argument;
3. **peeling/handoff theorem** — prove that every fixed-thickness material neighborhood is expelled/replaced at bounded generation age, forcing positive-frequency fresh source handoff or strong interface action.

The current repository has not yet proved any of these in full generality.

---

## 8. DSD interpretation

This is a useful example of the difference between descriptors:

- material identity can survive on a zero-volume set;
- flux identity can survive on a material surface;
- volume occupancy can vanish;
- geometric axis identity can still evolve separately.

Merging these descriptors would create a false fixed-volume contradiction.

---

## 9. Updated firewall

Do **not** use

\[
\text{same flux lineage}
\Rightarrow
\text{same positive-volume vortex tube forever}.
\]

Do **not** use M5-354 unless a fixed positive material volume or an equivalent thickness hypothesis has been independently proved.

The valid retained statement is

\[
\boxed{
C_{bal}^{co-shrink}
\text{ may survive only as a progressively thinner material skeleton unless it pays fresh occupancy/interface action.}
}
\]

---

## 10. Audit verdict

### PROVED

- later active old-material volume is at most `O(q^{-3L/2} r_j^3)`;
- an infinite co-shrinking descendant may have zero 3D material measure;
- persistent `O(nu)` flux is compatible with such a zero-volume material surface;
- fixed-volume M5-354 cannot be applied to the bare skeleton.

### NEXT TARGET

Quantify whether a shrinking flux skeleton can remain an efficient Biot--Savart source without generating persistent thickness, fresh handoff, or strong deformation-gradient action.

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
