# DSD bounded-Z global recurrence defect gate

Date: 2026-08-25

Status: **EXACT GLOBAL RESCALING RECURRENCE EXCLUDED / APPROXIMATE GLOBAL L2 RECURRENCE DEFECT HAS A POSITIVE CESARO FLOOR / LOCAL-TO-GLOBAL RECURRENCE BRIDGE NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

This note continues the DSD-internal audit. It does not identify normalized descriptor reappearance (R1) with same-base or material recurrence. Instead it asks what bounded normalized enstrophy permits if a genuine global rescaling recurrence is independently formed.

## 1. Vorticity rescaling channel

For a fixed scale factor `lambda>1`, define

\[
\boxed{(S_\lambda f)(x):=\lambda^2f(\lambda x).}
\]

This is the natural vorticity scaling. In three dimensions,

\[
\begin{aligned}
\|S_\lambda f\|_2^2
&=\int_{\mathbb R^3}\lambda^4|f(\lambda x)|^2dx\\
&=\lambda\|f\|_2^2,
\end{aligned}
\]

hence

\[
\boxed{\|S_\lambda f\|_2=\lambda^{1/2}\|f\|_2.}
\]

This simple scaling mismatch is the gate used below.

## 2. Exact global recurrence is incompatible with bounded-Z and a nonzero core

Let a sequence of formed global vorticity states satisfy

\[
\boxed{\Omega_{n+1}=S_\lambda\Omega_n.}
\]

Then iterating gives

\[
\|\Omega_n\|_2=\lambda^{n/2}\|\Omega_0\|_2.
\]

Therefore, if

\[
\sup_n\|\Omega_n\|_2\le M<\infty,
\]

one must have

\[
\boxed{\Omega_0=0.}
\]

Consequently any nonzero globally formed state with uniform bounded-Z cannot possess an exact forward recurrence under a fixed nontrivial vorticity rescaling.

\[
\boxed{\text{bounded-Z}+\text{nonzero exact global DSS-type recurrence}\Rightarrow\text{contradiction}.}
\]

Status: **PROVED as an abstract global recurrence lemma.**

This is not yet a theorem about the actual first-hitting sequence, because the required same-base global recurrence has not been derived from first-hitting compactness.

## 3. Approximate recurrence defect

Define the finite global recurrence defect

\[
\boxed{E_n:=\Omega_{n+1}-S_\lambda\Omega_n,\qquad \delta_n:=\|E_n\|_2.}
\]

Let

\[
a_n:=\|\Omega_n\|_2.
\]

The reverse triangle inequality gives

\[
a_{n+1}
\ge
\lambda^{1/2}a_n-\delta_n,
\]

so

\[
\boxed{\delta_n\ge\lambda^{1/2}a_n-a_{n+1}.}
\]

Summing from `n=0` to `N-1`,

\[
\boxed{
\sum_{n=0}^{N-1}\delta_n
\ge
\lambda^{1/2}a_0-a_N
+(\lambda^{1/2}-1)\sum_{n=1}^{N-1}a_n.
}
\]

This identity is the finite-witness form required by the DSD formation discipline; no infinite recurrence object is needed.

## 4. First-hitting analytic occupancy supplies a global L2 floor

At normalized first-hitting snapshots the imported analytic corridor gives

\[
|\Omega_n(y_n)|=1
\]

and a fixed radius `r_a>0` such that

\[
|\Omega_n|\ge\frac12
\quad\text{on }B_{r_a}(y_n).
\]

Hence

\[
\boxed{a_n=\|\Omega_n\|_2\ge m_0:=\sqrt{\frac\pi3}\,r_a^{3/2}>0.}
\]

On the bounded-Z branch also suppose

\[
a_n\le M.
\]

Then the finite defect ledger becomes

\[
\sum_{n=0}^{N-1}\delta_n
\ge
(\lambda^{1/2}-1)m_0(N-1)-M+\lambda^{1/2}m_0.
\]

Therefore

\[
\boxed{
\liminf_{N\to\infty}\frac1N\sum_{n=0}^{N-1}\delta_n
\ge
(\lambda^{1/2}-1)m_0>0.
}
\]

In particular,

\[
\boxed{\delta_n\not\to0.}
\]

Thus a nonzero bounded-Z sequence cannot become globally L2-close to its fixed-factor rescaling at every late generation.

Status: **PROVED conditional only on the stated global approximate-recurrence comparison being the correct comparison map.**

## 5. Quantitative infinitely-many-defect generations

The bounded-Z ceiling also gives

\[
\delta_n\le a_{n+1}+\lambda^{1/2}a_n
\le(1+\lambda^{1/2})M=:D_{\max}.
\]

Let

\[
d_0:=(\lambda^{1/2}-1)m_0.
\]

Since the Cesaro lower bound is at least `d_0`, there is a fixed positive threshold, for example `d_0/2`, attained on infinitely many generations:

\[
\boxed{\delta_n\ge d_0/2\quad\text{for infinitely many }n.}
\]

Otherwise all sufficiently late defects would be below `d_0/2`, forcing the Cesaro limsup below `d_0/2`, contradicting the preceding lower bound.

This produces arbitrarily late **finite global describability-difference witnesses**.

## 6. Local recurrence plus global defect forces spatial escape of the defect

Now impose a strictly stronger, separately typed condition: for every fixed finite radius `R`, suppose the same recurrence defect satisfies

\[
\boxed{\|E_n\|_{L^2(B_R)}\to0.}
\]

This is a local same-comparison recurrence statement, stronger than mere R1 convergence unless the comparison maps have been explicitly aligned.

Choose one of the infinitely many generations with

\[
\|E_n\|_2\ge d_0/2.
\]

For any fixed `R`, once

\[
\|E_n\|_{L^2(B_R)}\le d_0/4,
\]

orthogonality of the inside/outside decomposition gives

\[
\begin{aligned}
\|E_n\|_{L^2(|x|>R)}^2
&=\|E_n\|_2^2-\|E_n\|_{L^2(B_R)}^2\\
&\ge\frac{d_0^2}{4}-\frac{d_0^2}{16}
=\frac{3d_0^2}{16}.
\end{aligned}
\]

Hence along infinitely many late generations,

\[
\boxed{
\|E_n\|_{L^2(|x|>R)}
\ge\frac{\sqrt3}{4}d_0
}
\]

for every fixed finite `R` after passing sufficiently far along that subsequence.

Thus

\[
\boxed{
\text{local recurrence}
+\text{bounded-Z nonzero core}
\Rightarrow
\text{persistent global recurrence defect escaping every fixed base}.
}
\]

Status: **PROVED CONDITIONAL on local L2 convergence of the correctly aligned recurrence defect.**

## 7. DSD interpretation

This separates three descriptions that must not be collapsed:

1. `R1 descriptor reappearance`: stage-dependent normalized compact descriptions become close;
2. `global rescaling recurrence`: the whole formed state is close to `S_lambda` of the previous state in global L2;
3. `remote recurrence defect`: the local difference tends to zero while a fixed amount of global L2 difference survives outside every finite base.

The previous DSD audit already showed

\[
R1\not\Rightarrow R2/R3.
\]

The present note adds:

\[
\boxed{
\text{if a global rescaling recurrence were formed, bounded-Z itself forbids exact recurrence.}
}
\]

And if local recurrence survives while the global L2 comparison is made, then the only possible defect is spatially non-tight.

This is a new sharply typed survivor:

\[
\boxed{\text{remote global-L2 recurrence-defect migration}.}
\]

It is not the previously pruned passive cubic tail: the defect is defined by a **difference between successive rescaled states**, not by one state's static remote shell mass.

## 8. What remains open

The following bridges are not derived here:

1. first-hitting descriptor reappearance R1 implies a global comparison
   \[
   \Omega_{n+1}\approx S_\lambda\Omega_n;
   \]
2. the physical first-hitting time/center maps furnish the exact fixed `lambda` recurrence comparison used above;
3. the remote defect at different generations consists of the same material packet;
4. remote-defect migration forces a nonsummable energy/enstrophy cost;
5. global regularity.

In particular, no first-hitting timing symbol is identified with a DSS step without a separate derivation.

## 9. Audit verdict

### PROVED

- `||S_lambda f||_2=lambda^{1/2}||f||_2`;
- nonzero exact fixed-factor global recurrence is incompatible with a uniform global L2 vorticity ceiling;
- approximate global recurrence defects have a positive Cesaro lower bound when the normalized states have a uniform nonzero L2 floor;
- therefore global recurrence defect cannot vanish generation by generation;
- if that defect vanishes on every fixed local base, fixed L2 mass must escape outside every fixed radius.

### NOT DERIVED

- promotion of R1 first-hitting descriptor reappearance to the global recurrence comparison;
- dynamic/material genealogy of the escaped defect;
- a nonsummable budget charge from defect migration;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
