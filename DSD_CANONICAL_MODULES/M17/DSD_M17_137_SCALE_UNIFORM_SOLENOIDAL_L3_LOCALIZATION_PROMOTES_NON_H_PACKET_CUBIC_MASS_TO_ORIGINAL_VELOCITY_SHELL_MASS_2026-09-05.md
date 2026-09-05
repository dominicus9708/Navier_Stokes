# DSD M17-137 — Scale-uniform solenoidal `L^3` localization promotes non-H packet cubic mass to original velocity shell mass

Date: 2026-09-05  
Canonical ID: **M17-137**

Status: **LOCALIZATION BRIDGE PROVED / THE M17-136 PACKET CUBIC LOWER BOUND CAN BE TRANSFERRED TO THE ORIGINAL VELOCITY ON A FIXED-SHAPE ENLARGED ANNULUS BY A TWO-COLLAR BOGOVSKII LOCALIZER WHOSE `L^3` CONSTANT IS SCALE INVARIANT. THIS CLOSES THE PACKET-VERSUS-ORIGINAL-VELOCITY MEASURE GAP ON THE NON-H LANE, PROVIDED THE SELECTED RIBBON FAMILY ITSELF CARRIES DIVERGENT `J^(3/2)` MASS. IT DOES NOT SHOW THAT EVERY NON-L3 TAIL IS RIBBON-CAPTURED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-shape shell geometry

Let

\[
A_R=\{a_1R<|y|<a_2R\}
\]

be the retained shell core and choose a fixed-shape enlarged annulus

\[
C_R=\{b_0R<|y|<b_3R\},
\qquad
0<b_0<a_1<a_2<b_3.
\]

Choose intermediate radii

\[
b_0<b_1<a_1<a_2<b_2<b_3
\]

and define two transition collars

\[
D_R^-:=\{b_0R<|y|<b_1R\},
\qquad
D_R^+:=\{b_2R<|y|<b_3R\}.
\]

Take a radial smooth cutoff `chi_R` such that

\[
\chi_R=1
\quad\text{on a neighborhood of }A_R,
\]

\[
\chi_R=0
\quad\text{near }\partial C_R,
\]

and

\[
\operatorname{supp}\nabla\chi_R
\subset D_R^-\cup D_R^+,
\qquad
|\nabla\chi_R|\le C_\chi R^{-1}.
\]

All domains are dilates of fixed reference domains.

---

## 2. Divergence defect lives only in the collars

Let the original velocity satisfy

\[
\nabla\cdot U=0.
\]

Then

\[
\nabla\cdot(\chi_RU)
=\nabla\chi_R\cdot U
=:g_R.
\]

Write

\[
g_R=g_R^-+g_R^+,
\qquad
\operatorname{supp}g_R^\pm\subset D_R^\pm.
\]

To correct each collar independently, one must verify

\[
\int_{D_R^\pm}g_R^\pm dy=0.
\]

This compatibility must not be assumed automatically.

---

## 3. Each collar defect has zero mean

Because `chi_R` is radial and constant on each boundary sphere of each transition collar,

\[
\int_{D_R^\pm}\nabla\chi_R\cdot U\,dy
=
\int_{\partial D_R^\pm}\chi_R U\cdot n\,dS.
\]

For every sphere centered at the shell center on which the smooth divergence-free field is defined through the enclosed ball,

\[
\int_{S_r}U\cdot n\,dS
=
\int_{B_r}\nabla\cdot U\,dy
=0.
\]

Hence each constant-`chi_R` boundary contribution vanishes separately and therefore

\[
\boxed{
\int_{D_R^-}g_R^-dy=0,
\qquad
\int_{D_R^+}g_R^+dy=0.
}
\]

Thus each collar admits an independent Bogovskii correction.

If a translated first-hitting center is used, the same argument applies to concentric spheres around that center because divergence is translation invariant.

---

## 4. Scale-invariant Bogovskii correction

Let

\[
v_R^\pm:=\mathcal B_R^\pm g_R^\pm,
\]

where `B_R^±` is a Bogovskii right inverse of divergence on `D_R^±`, with zero boundary trace:

\[
\nabla\cdot v_R^\pm=g_R^\pm,
\qquad
v_R^\pm\in W_0^{1,3}(D_R^\pm).
\]

Since

\[
D_R^\pm=R D_1^\pm
\]

are fixed-shape dilates, the scaled Bogovskii estimate is

\[
\boxed{
\|v_R^\pm\|_{L^3(D_R^\pm)}
\le
C_B R\|g_R^\pm\|_{L^3(D_R^\pm)},
}
\]

with `C_B` independent of `R`.

Using

\[
|g_R^\pm|
\le
C_\chi R^{-1}|U|,
\]

we obtain

\[
\boxed{
\|v_R^\pm\|_3
\le
C\|U\|_{L^3(D_R^\pm)}.
}
\]

This is the exact scale cancellation needed for the critical exponent `3`.

---

## 5. Solenoidal packet with exact retained-core equality

Extend `v_R^±` by zero outside their collars and define

\[
\boxed{
f_R:=\chi_RU-v_R^--v_R^+.}
\]

Then

\[
\nabla\cdot f_R=0,
\qquad
\operatorname{supp}f_R\subset C_R.
\]

Because the two corrections are supported only in the transition collars while `chi_R=1` on the retained core,

\[
\boxed{f_R=U\quad\text{on }A_R.}
\]

This is why a single Bogovskii correction on the whole enlarged annulus is insufficient for the present purpose: a global correction need not vanish on `A_R` and would contaminate the retained core.

The two-collar construction avoids that defect.

---

## 6. Scale-uniform `L^3` localization bound

By the triangle inequality and the preceding collar estimates,

\[
\begin{aligned}
\|f_R\|_{L^3(C_R)}
&\le
\|\chi_RU\|_3
+\|v_R^-\|_3
+\|v_R^+\|_3\\
&\le
C_{loc}\|U\|_{L^3(C_R)}.
\end{aligned}
\]

Thus

\[
\boxed{
\|f_R\|_3
\le
C_{loc}\|U\|_{L^3(C_R)},
}
\]

where `C_loc` depends only on the fixed annular geometry and cutoff profile, not on `R`.

Equivalently,

\[
\boxed{
\int_{C_R}|U|^3dy
\ge
C_{loc}^{-3}\|f_R\|_3^3.
}
\]

No localization residual is needed in this purely spatial `L^3` comparison.

---

## 7. Combine with the M17-136 non-H lower bound

M17-136 gives, on a selected non-H shell whose retained packet carries derivative cost `J_R`,

\[
\boxed{
\|f_R\|_3^3
\ge
c_*J_R^{3/2}.
}
\]

Therefore the original velocity satisfies

\[
\boxed{
\int_{C_R}|U|^3dy
\ge
c_{orig}J_R^{3/2},
\qquad
c_{orig}:=c_*C_{loc}^{-3}>0.
}
\]

Thus the packet cubic mass is not a localization artifact.

For the critical ribbon/bath scaling `J_R\asymp1`,

\[
\boxed{
\int_{C_R}|U|^3dy\gtrsim1.
}
\]

This rigorously identifies the shell-scale `1/R` velocity reservoir as genuine original-velocity cubic mass, not merely packet mass.

---

## 8. Bounded-overlap and residue-class extraction

The enlarged dyadic annuli `C_{R_k}` have uniformly bounded overlap.

If a selected family `S` satisfies

\[
\sum_{k\in S}J_k^{3/2}=\infty,
\]

partition `S` into finitely many residue classes so that, within each class, the corresponding enlarged annuli are pairwise disjoint or have a fixed bounded overlap constant.
At least one class `S_*` retains divergent mass:

\[
\boxed{
\sum_{k\in S_*}J_k^{3/2}=\infty.
}
\]

Then

\[
\sum_{k\in S_*}
\int_{C_{R_k}}|U|^3dy
\ge
c_{orig}
\sum_{k\in S_*}J_k^{3/2}
=\infty.
\]

With bounded overlap this implies

\[
\boxed{
U\notin L^3
}
\]

on that shell family.

Thus on a non-H ribbon-captured family carrying divergent critical mass, the M5 non-`L^3` obstruction is recovered directly in the original velocity measure.

---

## 9. What this does and does not close

This module closes the implication

\[
\boxed{
\begin{gathered}
\text{non-H selected shell family},\\
\text{ribbon/retained packet carries the relevant }J_k,\\
\sum J_k^{3/2}=\infty
\end{gathered}
\Longrightarrow
U\notin L^3\text{ on that family}.
}
\]

It does **not** prove the converse selection

\[
U\notin L^3
\Longrightarrow
\text{a fixed-fraction Rank-2 ribbon family carries divergent }J_k^{3/2}.
\]

The total tail may distribute its critical cost among Rank-1, Rank-2 finite-peak, ribbon, derivative-frequency, pressure/localization, or other already typed branches.

Therefore ribbon capture remains a branch hypothesis, not an exhaustive theorem.

---

## 10. DSD audit

### Audit A — one global Bogovskii correction preserves `f_R=U` on the retained core

Rejected in general.
A whole-annulus correction can penetrate the core.
The two-collar construction is required for exact core equality.

### Audit B — each collar divergence defect has zero mean automatically because the total defect does

Rejected as a logical shortcut.
The separate zero means were proved from the zero flux of a divergence-free field across each concentric sphere.

### Audit C — Bogovskii constants grow with shell radius and destroy the critical estimate

Rejected.
The factor `R` in the `L^3` Bogovskii estimate cancels the `R^{-1}` cutoff derivative, leaving a scale-uniform constant.

### Audit D — packet cubic mass and original cubic mass are interchangeable without construction

Rejected generally, but proved here for this explicit two-collar localizer.

### Audit E — divergent ribbon `J` is now proved for every non-`L^3` tail

Rejected.
Only the localization measure gap is closed; the ribbon-capture selection itself remains a separate branch question.

---

## 11. Updated Rank-2 ribbon frontier

On a fixed-fraction ribbon-captured non-H family,

\[
\boxed{
J_k\asymp1
\Longrightarrow
\begin{cases}
\Phi_k\gtrsim1,\\
\rho_k^2\sim K_k^{-1}\ \text{on the cheap critical scale},\\
\int_{C_k}|U|^3\gtrsim1,\\
\text{fresh material ribbon carriers across remote stages}.
\end{cases}
}
\]

Thus the hard survivor is now genuinely a coupled two-scale object:

\[
\boxed{
\text{low-amplitude, high-director-gradient ribbon skeleton}
+
\text{shell-scale critical }1/R\text{ velocity bath}.
}
\]

The next high-value gate is no longer localization.
It is the **full coupling/decoupling gate**:

\[
\boxed{
\text{Can the critical }1/R\text{ bath coexist with and repeatedly supply/import}
\text{ fresh order-one director-area ribbon geometry under CE-H/NS?}
}
\]

In particular, one must determine whether the incoming order-one director-area total variation has a non-summable physical cost, or whether the amplitude factor `rho_k^2\sim K_k^{-1}` makes every known positive energy/palinstrophy cost summable.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
