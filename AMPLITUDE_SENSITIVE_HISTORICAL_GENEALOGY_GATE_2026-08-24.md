# Amplitude-Sensitive Historical Genealogy Gate — 2026-08-24

Status: **AMPLITUDE-SENSITIVE FORGETTING GATE VALID / PERSISTENT HARDY BRANCH REOPENED BY ANTI-PROOF AUDIT / GLOBAL REGULARITY NOT PROVED.**

This note replaces the fixed-positive-shell-occupancy selection used in the 2026-08-23 historical-shell closure by an amplitude-sensitive selection adapted to the corrected ancient tail frontier.

The robust result of this note is:

\[
\boxed{
\text{non-}L^3\text{ tail}
\Longrightarrow
\text{arbitrarily old shells above the }K^{-2}\text{ quiet-forgetting threshold}.
}
\]

What this note does **not** claim after the anti-proof correction is that a shell which remains persistent is automatically a `T` event. Pure viscous decay over the remaining `K^{-2}` fraction of natural time can pay the Hardy weighted-moment balance at exactly the correct size. The persistent passive tail therefore remains a genuine final survivor unless an additional rigidity argument is supplied.

---

## 1. Critical shell amplitude

At first-hitting stage `j`, let

\[
r_j=W_j^{-1/2},
\qquad
W_j=q^jW_0.
\]

A shell of age `k` has physical radius

\[
R_{j,k}^{phys}=r_jK_k,
\qquad
K_k=q^{k/2}.
\]

Define

\[
\boxed{
J_{j,k}
:=
K_k\int_{A_{K_k}}|\nabla U_j|^2dy
}
\]

or equivalently

\[
J_{j,k}
=
R_{j,k}^{phys}
\int_{A_{R_{j,k}^{phys}}}|\nabla u|^2dx.
\]

Set

\[
\boxed{a_{j,k}=J_{j,k}^{1/2}.}
\]

---

## 2. Non-H gives an amplitude-sensitive natural-band packet

Let `f_{j,k}` be the compact solenoidal shell packet at radius `R=R_{j,k}^{phys}` and define

\[
\Gamma_{j,k}
=
\frac{R\|\nabla f_{j,k}\|_2}{\|f_{j,k}\|_2}.
\]

If `Gamma_{j,k}>Gamma_*`, the shell is already a derivative-frequency event `H`.

On the non-H lane,

\[
\Gamma_{j,k}\le\Gamma_*.
\]

Because `f_{j,k}=u` on the retained shell core,

\[
\|\nabla f_{j,k}\|_2^2
\ge
\frac{J_{j,k}}R.
\]

Hence

\[
\|f_{j,k}\|_2
\ge
\Gamma_*^{-1}\sqrt{J_{j,k}R}.
\]

The localized phase-space trichotomy then supplies a fixed natural-band fraction `beta_*>0`, giving

\[
\boxed{
\|P_{j,k}f_{j,k}(t_j)\|_2
\ge
c_Pa_{j,k}R^{1/2},
\qquad
c_P=\beta_*/\Gamma_*.
}
\]

---

## 3. Remaining-time compression

The first-hitting stage corridor gives

\[
T^*-t_j\le C_Tr_j^2.
\]

Since `R=K_kr_j`,

\[
\boxed{
\frac{T^*-t_j}{R^2}
\le
C_TK_k^{-2}.
}
\]

Thus an old shell at large `K_k` has only a vanishing fraction of its own natural parabolic time remaining.

---

## 4. Amplitude-sensitive quiet-forgetting threshold

Suppose the shell loses a fixed fraction of its original natural-band packet before `T^*`.

The exact localized Duhamel gate gives

\[
\int_{t_j}^{t_f}
\left(
\|P_{j,k}\mathcal N_{j,k}\|_2
+
\|P_{j,k}\mathcal R_{j,k}\|_2
\right)dt
\ge
c_0a_{j,k}R^{1/2}
\]

for a fixed `c_0>0` once `K_k` is sufficiently large.

On the repaired relative quiet corridor,

\[
\|P_{j,k}\mathcal N_{j,k}\|_2
+
\|P_{j,k}\mathcal R_{j,k}\|_2
\le
K_*R^{-3/2}.
\]

The maximum action available before `T^*` is therefore

\[
\le
K_*C_TK_k^{-2}R^{1/2}.
\]

Hence quiet forgetting requires

\[
\boxed{
a_{j,k}K_k^2\le C_{quiet}}
\]

with

\[
C_{quiet}=K_*C_T/c_0.
\]

Equivalently,

\[
\boxed{
J_{j,k}\le C_{quiet}^2K_k^{-4}.
}
\]

This conclusion is unaffected by `a_{j,k}->0`.

---

## 5. Arithmetic selection lemma

Let

\[
K_k=q^{k/2},
\qquad a_k\ge0,
\]

and assume

\[
\boxed{
\sum_{k=1}^\infty a_k^3=\infty.
}
\]

Then

\[
\boxed{
\limsup_{k\to\infty}a_kK_k^2=\infty.
}
\]

Indeed, if `a_kK_k^2<=C` eventually, then

\[
a_k\le Cq^{-k}
\]

and therefore

\[
\sum a_k^3<\infty,
\]

a contradiction.

More strongly, for every finite `C`, the set

\[
S_C=\{k:a_kK_k^2>C\}
\]

still carries divergent cubic mass:

\[
\boxed{
\sum_{k\in S_C}a_k^3=\infty.
}
\]

The complement is cubically summable because there

\[
a_k^3\le C^3q^{-3k}.
\]

---

## 6. Connection with the corrected non-L3 tail criterion

The anti-proof-corrected annular cubic ledger gives the necessary condition

\[
\boxed{
\sum_kJ_k^{3/2}=\infty
}
\]

for the surviving non-`L^3` ancient tail on the relative-energy corridor.

Since `a_k=J_k^{1/2}`, this becomes

\[
\sum a_k^3=\infty.
\]

Therefore the tail necessarily contains arbitrarily remote shells with

\[
\boxed{
J_k^{1/2}K_k^2\gg1.
}
\]

These shells cannot be strongly forgotten while all relative forcing channels remain quiet.

---

## 7. Finite-block diagonal transfer

The local ancient convergence may be diagonalized over arbitrarily large finite shell sets.

For every `n`, one can choose a finite remote set `F_n` such that

\[
\sum_{k\in F_n}J_{\infty,k}^{3/2}>n
\]

and

\[
J_{\infty,k}^{1/2}K_k^2>C_{quiet}+n
\qquad(k\in F_n).
\]

Then choose one sufficiently late smooth first-hitting stage `j_n` so that all shell quantities in `F_n` are simultaneously approximated and

\[
j_n-\max F_n\to\infty.
\]

Thus the same smooth snapshot contains a shrinking physical block of remote shells satisfying

\[
\sum_{k\in F_n}J_{j_n,k}^{3/2}\to\infty
\]

and every selected shell lies above the quiet-forgetting threshold.

This removes the concern that different remote ancient shells might require mutually incompatible prelimit subsequences.

---

## 8. Corrected genealogy dichotomy

For every selected high-ratio shell, one of three things occurs.

### A. Derivative-frequency failure

\[
\Gamma_{j,k}>\Gamma_*
\]

routes directly to `H`.

### B. Strong forgetting before `T^*`

The amplitude-sensitive remaining-time gate shows that quiet forgetting is impossible. Therefore at least one nonlinear/material/pressure/viscous/localization forcing channel exceeds its quiet threshold.

This is a typed `H/T/pressure/residual` exit.

### C. Persistent passive memory

The shell retains a fixed fraction of its natural-band packet through the later checkpoint windows.

This case **is not closed by the Hardy weighted-energy identity alone.**

The selected persistent shells satisfy

\[
\sum J_k^{3/2}=\infty
\Longrightarrow
\sum J_k=\infty,
\]

so they create a large weighted derivative tower

\[
D_1=\int |x-X_*||\nabla u|^2dx.
\]

However, over the short remaining interval

\[
T^*-t_j\sim r_j^2
=K_k^{-2}R^2,
\]

ordinary viscosity changes the shell weighted moment by the same natural order as

\[
\nu\int D_1dt.
\]

For an amplitude-`a` shell,

\[
D_{1,shell}\sim a^2,
\]

\[
M_{1,shell}\sim a^2R^2,
\]

and over the remaining time

\[
\Delta M_{1,shell}^{visc}
\sim
 a^2R^2K^{-2}
=
 a^2r_j^2,
\]

while

\[
\nu\int_{t_j}^{T^*}D_{1,shell}dt
\sim
 a^2r_j^2.
\]

Thus the Hardy balance can be paid by ordinary viscous weighted-moment decay without any order-one material turnover.

Therefore

\[
\boxed{
\text{persistent passive high-ratio tail}
}
\]

must remain as an honest survivor until a separate rigidity or tail-decoupling theorem removes it.

---

## 9. Corrected branch implication

The valid implication from this note is

\[
\boxed{
\begin{aligned}
\text{non-}L^3\text{ critical tail}
\Longrightarrow\;&
H
\\
&\lor T_{forget/rebuild}
\\
&\lor\text{pressure/localization residual}
\\
&\lor\text{persistent passive high-ratio tail}.
\end{aligned}
}
\]

The last branch must not be relabeled as `T` merely because its weighted derivative moment is large.

---

## 10. What remains genuinely useful

The fixed-positive-occupancy hypothesis has still been removed successfully.

The theorem-level gain is

\[
\boxed{
\sum a_k^3=\infty
\Longrightarrow
\text{divergent cubic mass lies on shells that cannot be quietly forgotten.}
}
\]

Therefore every surviving non-`L^3` tail is forced toward **persistence**, rather than being allowed to evade the old historical analysis through ever smaller amplitudes and continual silent forgetting.

This is a substantial structural reduction even though persistence itself remains open.

---

## 11. Current next target

The correct final tail question is now:

\[
\boxed{
\text{Can an active recurrent Leray core coexist with an infinite, dynamically passive, persistent high-ratio shell genealogy?}
}
\]

The next efficient approaches are:

1. prove that such a passive genealogy can be removed from the rigidity argument by a local/quotient Liouville theorem that does not require global `L^3`;
2. prove a tail-decoupling theorem strong enough that a recurrent time-translation limit retains the nonzero core but loses the persistent tail in a Liouville-compatible topology;
3. derive a new global constraint on the persistent genealogy stronger than the weighted Hardy identity, since the latter is exactly compatible with viscous decay at remaining-time scale.

Status: **THE AMPLITUDE-SENSITIVE REMAINING-TIME GATE IS VALID AND REMOVES SILENT FORGETTING OF THE DIFFUSE ENDPOINT TAIL. THE ANTI-PROOF AUDIT SHOWS THAT THE PERSISTENT PASSIVE TAIL CANNOT YET BE CALLED TURNOVER: VISCOSITY CAN PAY ITS HARDY WEIGHTED-MOMENT COST AT THE CORRECT `K^{-2}` SCALE. THE FINAL TAIL SURVIVOR IS THEREFORE A PERSISTENT PASSIVE HIGH-RATIO GENEALOGY COEXISTING WITH THE RECURRENT CORE. GLOBAL REGULARITY REMAINS UNPROVED.**