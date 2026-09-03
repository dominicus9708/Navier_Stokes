# DSD M17-011 — Regular nodal skeleton is measure-thin but forces a third-jet curvature law

Date: 2026-09-03
Canonical ID: **M17-011**

Status: **INTERNAL NODAL-SKELETON / BULK-SHEATH AUDIT / THE SIGNED NODAL RECURRENCE LAW `⟨kappa⟩_nodal = 3/2` DOES NOT DIRECTLY CONFLICT WITH THE GLOBAL ENSTROPHY-WEIGHTED IDENTITY `∫ kappa |W|^2 = -P < 0`. AT A REGULAR CODIMENSION-TWO WINDING FILAMENT, `W` VANISHES LINEARLY IN THE TWO TRANSVERSE VARIABLES, SO THE LOCAL `kappa |W|^2` CONTENT OF A RADIUS-r TUBE IS ONLY `O(r^4)` PER UNIT FILAMENT LENGTH. THE TRANSVERSE GRADIENT ENERGY AND RADIAL BOUNDARY FLUX ARE BOTH `O(r^2)` WITH THE SAME LEADING COEFFICIENT, SO THEIR LEADING TERMS CANCEL IN THE LOCAL GREEN BALANCE. HOWEVER THE ZERO IS NOT STRUCTURALLY EMPTY: DIFFERENTIATING `Delta W = kappa W` AT THE FILAMENT GIVES THE EXACT THIRD-JET LAW `Delta G_j = kappa G_j`, AND HENCE A BOCHNER-TYPE CURVATURE IDENTITY FOR THE NODAL JACOBIAN. THE NEXT OBSTRUCTION MUST THEREFORE COME FROM FINITE-RADIUS JET-TO-SHEATH TRANSFER, NODAL DEGENERATION/TURNOVER, OR THE NON-AXISYMMETRIC CLASSIFICATION GAP; GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup: a regular material winding filament

Use the rank-one great-circle branch of M17-006--010.
Let `Gamma` be a regular material nodal filament and let `s` denote arclength along it.
Choose local transverse coordinates

\[
z=(z_1,z_2)\in N_s\Gamma.
\]

At a regular zero,

\[
W(s,0)=0,
\qquad
\operatorname{rank}\nabla W(s,0)=2.
\]

Because the tangent direction lies in the kernel of the Jacobian, the first nonzero transverse jet is a rank-two linear map

\[
A(s):N_s\Gamma\to n^\perp,
\]

and locally

\[
\boxed{
W(s,z)=A(s)z+O(|z|^2).
}
\]

Define

\[
Q(s):=A(s)^TA(s),
\qquad
q(s):=\operatorname{tr}Q(s)=|A(s)|_F^2>0.
\]

The strict positivity follows from regular rank two.

---

## 2. Enstrophy weight of the skeleton is quartically thin

Let `D_r` be a small transverse disk of radius `r` centered on the filament.
From

\[
|W|^2=z^TQz+O(|z|^3)
\]

and

\[
\int_{D_r}z_i z_j\,dz
=\delta_{ij}\frac{\pi r^4}{4},
\]

we obtain, per unit filament length,

\[
\boxed{
\int_{D_r}|W|^2\,dz
=
\frac{\pi r^4}{4}q(s)+O(r^5).
}
\]

Since `kappa` analytically extends through the regular filament by M17-007,

\[
\kappa(s,z)=\kappa_0(s)+O(r),
\qquad
\kappa_0(s):=\kappa(s,0),
\]

and therefore

\[
\boxed{
\int_{D_r}\kappa|W|^2\,dz
=
\frac{\pi r^4}{4}\kappa_0(s)q(s)+O(r^5).
}
\]

Thus the signed `kappa` content seen through the enstrophy measure is only quartic in the transverse radius.

This is the exact measure mismatch behind the apparent tension

\[
\langle\kappa\rangle_{nodal}=\frac32
\qquad\text{versus}\qquad
\int\kappa|W|^2=-P<0.
\]

The nodal mean is measured on the filament skeleton, while the global identity is weighted by `|W|^2`, which vanishes quadratically on that skeleton.

---

## 3. Transverse palinstrophy is only quadratically thin

Differentiate the local expansion:

\[
\nabla_zW=A+O(r).
\]

Hence

\[
\boxed{
\int_{D_r}|\nabla_zW|^2\,dz
=
\pi r^2 q(s)+O(r^3).
}
\]

The radial boundary flux has the same leading coefficient.
On `|z|=r`, write `z=rn`, `|n|=1`.
Then

\[
W=Ar n+O(r^2),
\qquad
\partial_nW=An+O(r),
\]

so

\[
\boxed{
\int_{\partial D_r}W\cdot\partial_nW\,d\ell
=
\pi r^2 q(s)+O(r^3).
}
\]

Therefore the local Green balance does **not** read as an uncancelled negative `O(r^2)` cost near the zero.
The transverse gradient energy and radial boundary flux have identical leading `O(r^2)` terms.
Their difference is controlled by higher jets and must match the much smaller `O(r^4)` `kappa|W|^2` content together with tangential/curvature corrections.

Consequently, a positive nodal value of `kappa` does not force an arbitrarily nearby negative-`kappa` sheath merely from integration by parts.

---

## 4. No infinitesimal sign contradiction

M17-010 gives, on every uniformly recurrent regular filament with bounded nonzero horizontal Jacobian,

\[
\boxed{
\langle\kappa_0\rangle_{nodal}=\frac32.
}
\]

The global CE-H identity remains

\[
\boxed{
\int\kappa|W|^2=-P<0.
}
\]

The tubular asymptotics show that these two statements can coexist at arbitrarily small tube radius because

\[
\int_{D_r}\kappa|W|^2=O(r^4).
\]

Thus the following shortcut is rejected:

\[
\boxed{
\text{positive nodal mean}
\not\Longrightarrow
\text{immediate local sign contradiction}.
}
\]

In particular, continuity alone does not force a `kappa=0` surface to approach the filament at vanishing radius.

Any useful contradiction must instead involve a **finite-radius transfer mechanism**, a degeneration/turnover event, or a global recurrence constraint.

---

## 5. The zero is not dynamically empty: differentiate the CE-H eigenvalue equation

The regular branch satisfies

\[
\Delta W=\kappa W.
\]

Let

\[
G_j:=\partial_jW.
\]

Differentiate the equation:

\[
\Delta G_j
=
(\partial_j\kappa)W+\kappa G_j.
\]

At the filament, `W=0`, hence

\[
\boxed{
\Delta G_j=\kappa_0 G_j
\qquad\text{on }\Gamma.
}
\]

Equivalently,

\[
\boxed{
\nabla\Delta W=\kappa_0\nabla W
\qquad\text{on }\Gamma.
}
\]

This is a third-order jet constraint on the vorticity field.
The nodal value of `kappa` is therefore encoded not in `W` itself, which vanishes, but in the Laplacian of its first spatial jet.

This is the correct descriptor switch at the nodal skeleton.

---

## 6. Exact nodal-Jacobian Bochner identity

Let

\[
G:=\nabla W.
\]

At a regular nodal point, `|G|_F>0`.
Using

\[
\frac12\Delta|G|_F^2
=
|\nabla G|_F^2+G:\Delta G,
\]

and

\[
\Delta G=\kappa_0G
\]

at the filament gives

\[
\boxed{
\frac12\Delta|G|_F^2
=
|\nabla G|_F^2
+
\kappa_0|G|_F^2.
}
\]

Hence

\[
\boxed{
\kappa_0
=
\frac{\frac12\Delta|G|_F^2-|\nabla G|_F^2}
{|G|_F^2}
\qquad\text{on }\Gamma.
}
\]

For a recurrent regular filament satisfying M17-010,

\[
\boxed{
\left\langle
\frac{\frac12\Delta|G|_F^2-|\nabla G|_F^2}
{|G|_F^2}
\right\rangle_{nodal}
=
\frac32.
}
\]

Thus the positive mean `kappa` law becomes a positive mean **normalized spatial curvature budget of the nodal Jacobian**.

This is stronger than the measure-zero observation: the skeleton is invisible to the `|W|^2` measure but remains visible to the first-jet descriptor `G`.

---

## 7. DSD analysis

### 7.1 Descriptor dependence
The same geometric set has two very different descriptions:

1. **field descriptor `W`** — vanishes on the filament;
2. **first-jet descriptor `G=∇W`** — nonzero and rank two on a regular filament.

Therefore information that is absent at the `W` level reappears at the `G` level.
This is a direct DSD-style describability difference rather than a contradiction.

### 7.2 Measure dependence
The global identity uses the weighted measure

\[
|W|^2dx,
\]

which suppresses the regular filament quadratically.
The nodal recurrence law uses the material filament trajectory and the nondegenerate Jacobian.
These are not interchangeable measures.

### 7.3 Structural transfer question
The relevant question is no longer whether the skeleton and bulk have opposite signs.
It is whether the nonzero first-jet curvature budget at the skeleton must transfer, within a controlled finite radius, into one of:

- a negative-`kappa` bulk payer;
- a `kappa=0` transition sheet;
- loss of regular rank two;
- finite-jet topology turnover;
- axisymmetric/no-swirl-type regularization;
- genuinely non-axisymmetric recurrent great-circle geometry.

---

## 8. DSD audit

### Audit A — hidden measure substitution
Rejected.
The nodal average and the global enstrophy-weighted average are kept distinct.

### Audit B — false local integration-by-parts contradiction
Rejected.
The `O(r^2)` transverse gradient cost is accompanied by an `O(r^2)` radial boundary flux with the same leading coefficient.

### Audit C — treating the zero set as information-free
Rejected.
Although `W=0`, the regular Jacobian is nonzero and obeys the exact third-jet law

\[
\Delta G=\kappa_0G.
\]

### Audit D — accidental exclusion of known regular geometry
Avoided.
M17-008 already shows that axisymmetric Navier--Stokes without swirl is a regular model carrying this type of winding/nodal geometry.
Therefore M17-011 does not claim winding or positive nodal `kappa` is itself singular.

### Audit E — recurrence scope
The mean identity

\[
\langle\kappa_0\rangle=\frac32
\]

is used only under the bounded, uniformly regular recurrent-Jacobian assumptions of M17-010.

### Audit F — proof status
No global contradiction has been derived.
No global regularity theorem is claimed.

---

## 9. Updated rank-one frontier

The regular nodal branch is refined to

\[
\boxed{
R_{nodal}^{material}
\Longrightarrow
J_{core}^{3rd\text{-}jet}
\ \lor\ 
S_{finite\text{-}radius}
\ \lor\ 
T_{nodal}^{finite\text{-}jet}
\ \lor\ 
G_{axis/no\text{-}swirl}
\ \lor\ 
G_{nonaxis}^{rank1}.
}
\]

Here

- `J_core^{3rd-jet}` is the exact nodal constraint `Delta G = kappa_0 G` together with the recurrent normalized curvature mean `3/2`;
- `S_finite-radius` is the unresolved transfer from the first-jet skeleton to the enstrophy-weighted sheath;
- `T_nodal^{finite-jet}` is the already isolated topology-turnover branch;
- `G_axis/no-swirl` is a known regular firewall model;
- `G_nonaxis^{rank1}` remains the genuine classification gap.

---

## 10. Next target — jet-to-sheath transfer gate

The highest-value next calculation is now a **finite-radius jet-to-sheath transfer estimate**.

A successful estimate would need to connect

\[
\boxed{
\Delta G=\kappa_0G,
\qquad
\langle\kappa_0\rangle=\frac32
}
\]

on the material skeleton to a quantitative statement at some nonzero radius where `|W|^2` no longer suppresses the structure.

The target alternatives are:

\[
\boxed{
\text{finite-radius negative payer}
\ \lor\ 
\kappa=0\text{ sheet}
\ \lor\ 
\text{rank loss / turnover}
\ \lor\ 
\text{regular axisymmetric-type escape}
\ \lor\ 
\text{non-axisymmetric recurrent survivor}.
}
\]

This is the new **Jet-to-Sheath Transfer Gate (JSTG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
