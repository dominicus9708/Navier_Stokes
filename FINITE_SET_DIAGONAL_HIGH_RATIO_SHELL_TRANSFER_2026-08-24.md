# Finite-Set Diagonal High-Ratio Shell Transfer — 2026-08-24

Status: **COMPACTNESS-DIAGONAL GAP REDUCED / MANY ANCIENT TAIL SHELLS CAN BE REALIZED SIMULTANEOUSLY IN ONE SMOOTH FIRST-HITTING SNAPSHOT / GLOBAL REGULARITY NOT PROVED.**

The amplitude-sensitive genealogy gate selects remote annuli from the ancient limit. A possible logical gap is that local ancient convergence is only known on each fixed compact set, while the relevant shell radius tends to infinity.

This note closes that gap at the finite-block level: arbitrarily large finite collections of high-ratio ancient shells can be transferred simultaneously to a single sufficiently late smooth first-hitting rescaling.

---

## 1. Ancient high-ratio shell set

Let

\[
K_k=q^{k/2},
\]

and let

\[
J_{\infty,k}
:=
K_k
\int_{A_{K_k}}
|\nabla U_\infty|^2dy.
\]

Assume the non-`L^3` tail condition

\[
\boxed{
\sum_{k\ge1}J_{\infty,k}^{3/2}=\infty.
}
\]

For a threshold `C>0`, define

\[
S_C
:=
\{k:J_{\infty,k}^{1/2}K_k^2>C\}.
\]

The amplitude-sensitive sequence lemma gives

\[
\boxed{
\sum_{k\in S_C}J_{\infty,k}^{3/2}=\infty
}
\]

for every finite `C`.

---

## 2. Finite high-ratio blocks with arbitrarily large cubic mass

Fix an integer `n>=1` and choose the threshold

\[
C_n=C_{quiet}+n.
\]

Because the cubic sum over `S_{C_n}` diverges, there exists a finite set

\[
F_n\subset S_{C_n}
\]

such that

\[
\boxed{
\sum_{k\in F_n}J_{\infty,k}^{3/2}>n.
}
\]

Every shell in `F_n` also satisfies

\[
\boxed{
J_{\infty,k}^{1/2}K_k^2>C_{quiet}+n.
}
\]

We may additionally choose the sets so that

\[
\min F_n\to\infty.
\]

This is possible because deleting finitely many shell indices cannot turn a divergent positive series into a convergent one.

Hence the selected blocks are genuinely remote, not repeatedly using the same bounded collection of annuli.

---

## 3. Simultaneous local convergence on the largest selected ball

Let

\[
K_n^{max}:=\max_{k\in F_n}K_k.
\]

For each fixed `n`, this is finite. The no-H local derivative compactness in the first-hitting rescalings gives strong `H^1`/smooth convergence on every fixed compact set. Therefore, after taking the first-hitting index `j` sufficiently large,

\[
J_{j,k}
:=
K_k\int_{A_{K_k}}|\nabla U_j|^2dy
\]

approximates `J_{\infty,k}` simultaneously for every `k in F_n`.

Choose `j_n` so large that

\[
\boxed{
\sum_{k\in F_n}J_{j_n,k}^{3/2}>\frac n2
}
\]

and

\[
\boxed{
J_{j_n,k}^{1/2}K_k^2>C_{quiet}+\frac n2
\qquad(k\in F_n).
}
\]

Because `F_n` is finite, no uniform-in-`k` compactness theorem is needed for this step.

---

## 4. Force the selected physical shells into the late sliding regime

Increase `j_n` further, if necessary, so that

\[
\boxed{
j_n-\max F_n\to\infty.}
\]

For a selected shell `k in F_n`, its physical radius is

\[
R_{n,k}^{phys}
=r_{j_n}K_k
=r_{j_n-k}.
\]

Therefore

\[
\boxed{
\max_{k\in F_n}R_{n,k}^{phys}
=r_{j_n-\max F_n}
\to0.
}
\]

Thus every shell in the entire finite block belongs to the late shrinking physical tower. The construction does not smuggle in a fixed early outer scale.

---

## 5. Weighted derivative mass of the same smooth snapshot diverges

Let

\[
S_{1,n}:=
\sum_{k\in F_n}J_{j_n,k}.
\]

For any finite nonnegative sequence,

\[
\sum J_k^{3/2}
\le
\left(\max J_k\right)^{1/2}
\sum J_k
\le
\left(\sum J_k\right)^{3/2}.
\]

Hence

\[
\boxed{
S_{1,n}
\ge
\left(
\sum_{k\in F_n}J_{j_n,k}^{3/2}
\right)^{2/3}
>
\left(\frac n2\right)^{2/3}.
}
\]

Thus the selected finite block already carries weighted derivative mass tending to infinity in a **single smooth first-hitting snapshot**:

\[
\boxed{
\sum_{k\in F_n}
R_{n,k}^{phys}
\int_{A_{R_{n,k}^{phys}}}
|\nabla u(t_{j_n})|^2dx
\to\infty.
}
\]

This is exactly the finite prelimit form needed by the localized Hardy ledger.

---

## 6. Simultaneous remaining-time obstruction

Every shell in `F_n` satisfies

\[
J_{j_n,k}^{1/2}K_k^2>C_{quiet}+n/2.
\]

Therefore, on the repaired uniform relative old-shell forcing corridor, **none** of these shells can lose a fixed fraction of its natural-band packet before `T^*` without activating

\[
H/T/\text{pressure/localization residual}.
\]

Consequently, if the global proof branch remains quiet, the whole finite block must remain in the persistent-memory lane through the later checkpoint windows.

As `n->infinity`, these simultaneous persistent blocks carry unbounded weighted derivative mass.

This is stronger than selecting one old shell per subsequence and removes the objection that the divergent ancient tail might be assembled from mutually incompatible prelimit subsequences.

---

## 7. Exact role in the proof tree

The non-`L^3` ancient tail can now be transferred as

\[
\boxed{
\text{ancient divergent shell stack}
\Longrightarrow
\text{smooth finite high-ratio shell blocks of arbitrarily large total }D_1.
}
\]

For each block:

- any large normalized derivative ratio is `H`;
- any strong forgetting is `T/H/pressure` by remaining-time compression;
- otherwise the block persists and enters the localized solenoidal Hardy weighted-energy ledger.

Therefore the only remaining issue in this tail route is no longer compactness/diagonal selection. It is the theorem-level localization of the persistent Hardy flux/moment alternative into the accepted finite-stage turnover definitions.

Status: **LOCAL ANCIENT CONVERGENCE IS SUFFICIENT TO REALIZE ARBITRARILY LARGE FINITE COLLECTIONS OF HIGH-RATIO REMOTE TAIL SHELLS IN ONE SMOOTH FIRST-HITTING SNAPSHOT. THEIR TOTAL WEIGHTED DERIVATIVE MASS DIVERGES, AND NONE CAN BE QUIETLY FORGOTTEN UNDER THE AMPLITUDE-SENSITIVE REMAINING-TIME GATE. THE LAST TAIL BRIDGE IS THE PERSISTENT HARDY FLUX/MOMENT LOCALIZATION. GLOBAL REGULARITY REMAINS UNPROVED.**