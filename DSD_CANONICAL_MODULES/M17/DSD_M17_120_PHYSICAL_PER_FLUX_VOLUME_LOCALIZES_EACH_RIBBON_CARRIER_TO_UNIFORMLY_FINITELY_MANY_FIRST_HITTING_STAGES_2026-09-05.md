# DSD M17-120 — Physical per-flux volume localizes each ribbon carrier to uniformly finitely many first-hitting stages

Date: 2026-09-05
Canonical ID: **M17-120**

Status: **INTERNAL RIBBON MATERIAL-GENEALOGY LOCALIZATION / M17-118 SHOWS THAT THE PHYSICAL PER-DIRECTOR-AREA-FLUX VOLUME `V_phys` OF A MATERIAL KERNEL LOOP IS CONSTANT, WHILE ITS SIMILARITY VALUE IS `V_sim=r_j^-3 V_phys` AT FIRST-HITTING SCALE `r_j`. IF A COMPACT RIBBON CLASS REQUIRES `v_- <= V_sim <= v_+`, A FIXED MATERIAL LOOP CAN BELONG TO THAT CLASS ONLY WHILE `r_j^3` LIES IN THE FINITE MULTIPLICATIVE WINDOW `[V_phys/v_+, V_phys/v_-]`. SINCE SUCCESSIVE FIRST-HITTING SCALES SATISFY `r_{j+1}/r_j=q^-1/2`, `V_sim` CHANGES BY THE FIXED FACTOR `q^{3/2}` PER STAGE. CONSEQUENTLY EACH MATERIAL RIBBON LOOP CAN OCCUPY THE COMPACT CLASS FOR AT MOST `1 + (2/(3 log q)) log(v_+/v_-)` CONSECUTIVE STAGES, UP TO INTEGER ROUNDING. IN PARTICULAR, SUFFICIENTLY REMOTE AGE-k RIBBON STRUCTURES AT STAGES `j-k` AND `j` CANNOT BE THE SAME MATERIAL LOOP. THIS SHARPENS THE M5 ANCESTOR-RADIUS AUDIT: ON THE RIBBON SUBBRANCH, REMOTE SPATIAL SCALE CORRESPONDENCE DOES NOT REPRESENT LONG-LIVED SAME-PACKET GENEALOGY; IT NECESSARILY USES FRESH MATERIAL CARRIERS. THIS IS A STRONG GENEALOGY CLASSIFICATION BUT NOT AN ENERGY CONTRADICTION, BECAUSE THE FRESH-CARRIER RESERVOIR MAY BE GEOMETRICALLY SHRINKING. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Physical per-flux volume is a material invariant

M17-118 gives

\[
\boxed{
\mathscr V_{phys}
:=\oint\frac{ds_{phys}}{|J_{phys}|}
=\text{constant along a material closed kernel loop}.
}
\]

At first-hitting stage `j`, with physical scale `r_j`, the similarity per-flux volume is

\[
\boxed{
\mathscr V_{sim}(j)
=r_j^{-3}\mathscr V_{phys}.
}
\]

---

## 2. Compact ribbon-class window

Assume the retained compact nondegenerate ribbon class imposes

\[
\boxed{
0<v_-\le\mathscr V_{sim}\le v_+<\infty.
}
\]

For a fixed material loop with invariant `V_phys`, membership at stage `j` requires

\[
v_-
\le
r_j^{-3}\mathscr V_{phys}
\le
v_+.
\]

Equivalently,

\[
\boxed{
\frac{\mathscr V_{phys}}{v_+}
\le
r_j^3
\le
\frac{\mathscr V_{phys}}{v_-}.
}
\]

Thus the admissible physical scale for one material loop lies in a fixed multiplicative interval.

---

## 3. First-hitting scale ratio

The existing first-hitting construction uses

\[
W_j=q^jW_0,
\qquad
q>1,
\]

and

\[
r_j=W_j^{-1/2}.
\]

Therefore

\[
\boxed{
\frac{r_{j+1}}{r_j}
=q^{-1/2}.
}
\]

Hence

\[
\boxed{
\frac{r_{j+1}^3}{r_j^3}
=q^{-3/2}.
}
\]

Equivalently, for one fixed material loop,

\[
\boxed{
\frac{\mathscr V_{sim}(j+1)}
{\mathscr V_{sim}(j)}
=q^{3/2}.
}
\]

The similarity per-flux volume therefore moves monotonically through the compact-class window by a fixed geometric factor at each stage.

---

## 4. Uniform bound on stage multiplicity

Suppose one material loop belongs to the compact ribbon class at stages

\[
j_0,j_0+1,\ldots,j_0+m-1.
\]

Then

\[
q^{\frac32(m-1)}
\le
\frac{v_+}{v_-}.
\]

Thus

\[
\boxed{
m-1
\le
\frac{2}{3\log q}
\log\frac{v_+}{v_-}.
}
\]

Hence, with integer rounding,

\[
\boxed{
M_{stage}
\le
1+
\left\lfloor
\frac{2}{3\log q}
\log\frac{v_+}{v_-}
\right\rfloor
}
\]

is a uniform upper bound on the number of first-hitting stages at which one material loop can occupy the same compact ribbon class.

No dynamics of `sigma`, `kappa`, or pressure enters this bound.

---

## 5. Remote ages require different material loops

If

\[
k>M_{stage},
\]

then a ribbon carrier observed in the retained compact class at stage `j` cannot be the same material closed kernel loop that occupied the same class at stage `j-k`.

Therefore

\[
\boxed{
\text{remote-age recurrent ribbon geometry}
\Longrightarrow
\text{fresh material carrier labels}.
}
\]

This is stronger than merely failing to prove same-packet persistence.

---

## 6. Relation to the M5 ancestor-radius identity

M5 gives the exact spatial relation

\[
R_{j,k}^{phys}=r_{j-k}.
\]

That identity says an age-`k` annular structure at current stage `j` lies at the physical radius associated with the earlier distinguished scale.

The present module says that, on the compact ribbon subbranch and for sufficiently large `k`, this spatial ancestry **cannot** be represented by one material ribbon loop persisting from stage `j-k` to `j` inside the same compact class.

Thus

\[
\boxed{
\text{spatial ancestral scale}
\neq
\text{same ribbon material carrier}
}
\]

for remote age.

The carrier genealogy is necessarily replacement-based.

---

## 7. Bounded stage overlap per material label

For any family of material ribbon labels, each label contributes to the compact ribbon-class stage ledger at most `M_stage` times.

This gives a genuine bounded multiplicity in **stage index per carrier**.

It may be useful in future summations because repeated stage occupation cannot be concentrated on one exceptional material loop.

However it does not bound how many distinct labels may occur at one stage.

---

## 8. Why this still does not close the physical return ledger

The M5 weighted return density requires enough physical time spent by comparable shell activity:

\[
\mathfrak R_k
=\rho_k^{-1}
\sum_\ell\tau_{k,\ell}.
\]

The present theorem shows that remote stages use different ribbon labels.
It does not give a lower bound for the physical dwell time of each fresh label at the ancestral radius.

Indeed the fresh labels may be successively smaller in physical per-flux volume as shown by M17-118.

Therefore

\[
\boxed{
\text{bounded stage multiplicity}
\not\Rightarrow
\mathfrak R_k\gtrsim J_k^{1/2}.
}
\]

---

## 9. DSD analysis

The word "genealogy" now splits into

\[
\boxed{
\text{scale genealogy}
\quad\text{and}\quad
\text{material-carrier genealogy}.
}
\]

M5's ancestor-radius identity fixes the former.
M17's per-flux-volume invariant strongly restricts the latter.

For remote ribbon ages the two genealogies do not coincide.

---

## 10. DSD audit

### Audit A — inferring same material packet from the ancestor-radius identity
Rejected; on the remote ribbon branch it is explicitly impossible within the same compact class.

### Audit B — treating a finite stage window as finite physical return count for all labels
Rejected. Infinitely many different labels may enter.

### Audit C — claiming fresh labels destroy recurrence
Rejected. Eulerian recurrence can be replacement-based.

### Audit D — proof status
Material genealogy is sharply localized in stage index, but the physical weighted return-density lower bound remains open.

---

## 11. Updated genealogy frontier

For the compact circular-ribbon subbranch,

\[
\boxed{
\text{one material loop}
\to
\text{at most }M_{stage}\text{ first-hitting stages}.
}
\]

Hence any indefinitely recurrent Eulerian ribbon pattern requires an infinite fresh-carrier cascade.

The remaining closure question is no longer whether remote age can be a single persistent ribbon packet. It cannot.
The question is whether the **aggregate fresh-carrier cascade** has sufficient amplitude-weighted physical return density to violate the finite Leray ledger.

This returns the proof frontier to the M17-119 flux-capture condition plus the still-missing M5 temporal return lower bound.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
