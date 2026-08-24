# Amplitude-Sensitive Historical Genealogy Gate — 2026-08-24

Status: **ANTI-PROOF-CORRECTED TAIL REDUCTION / FIXED OCCUPANCY IS NO LONGER REQUIRED / GLOBAL REGULARITY NOT PROVED.**

This note replaces the fixed-positive-shell-occupancy selection used in the 2026-08-23 historical-shell closure by an amplitude-sensitive selection adapted to the corrected ancient tail frontier.

The corrected tail input is not a positive density of order-one `L^3` shells. It is the weaker and genuinely endpoint-compatible condition

\[
\sum_{k\ge 1} \mathfrak E_{1,k}^{3/2}=\infty,
\]

where

\[
\mathfrak E_{1,k}
:=R_k\int_{A_{R_k}}|\nabla V|^2,
\qquad
R_k\simeq q^{k/2}.
\]

The purpose of this note is to show that even if

\[
\mathfrak E_{1,k}^{1/2}\to0,
\]

there are necessarily arbitrarily old shells whose amplitude is still too large to be quietly forgotten in the `K^{-2}` fraction of natural time remaining near a hypothetical singular time.

---

## 1. Shell notation and critical amplitude

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
K_k:=q^{k/2}.
\]

In stage-`j` normalized variables its annular radius is `K_k`.

Define the scale-critical first-derivative shell quantity

\[
\boxed{
J_{j,k}
:=
K_k
\int_{A_{K_k}}
|\nabla U_j(y)|^2dy.
}
\]

Equivalently, in physical variables,

\[
J_{j,k}
=
R_{j,k}^{phys}
\int_{A_{R_{j,k}^{phys}}}
|\nabla u(x,t_j)|^2dx.
\]

Thus `J_{j,k}` is invariant under the Navier--Stokes first-hitting scaling.

Set

\[
\boxed{a_{j,k}:=J_{j,k}^{1/2}.}
\]

For an ideal critical shell `u\sim a/r`, this is exactly the amplitude parameter up to fixed annular constants.

---

## 2. Non-H gives a natural-band packet lower bound proportional to amplitude

Let `f_{j,k}` be the compact divergence-free shell packet obtained by radial cutoff plus Bogovskii correction at physical scale

\[
R:=R_{j,k}^{phys}.
\]

Define its normalized derivative ratio

\[
\Gamma_{j,k}
:=
\frac{R\|\nabla f_{j,k}\|_2}{\|f_{j,k}\|_2}.
\]

If

\[
\Gamma_{j,k}>\Gamma_*,
\]

then the shell is already in the derivative-frequency branch `H`.

Assume instead the non-H lane

\[
\Gamma_{j,k}\le\Gamma_*.
\]

Because `f_{j,k}=u` on the retained shell core,

\[
\|\nabla f_{j,k}\|_2^2
\ge
\int_{A_R}|\nabla u|^2dx
=
\frac{J_{j,k}}R.
\]

The derivative-ratio bound therefore gives

\[
\|f_{j,k}\|_2
\ge
\frac{R}{\Gamma_*}\|\nabla f_{j,k}\|_2
\ge
\frac1{\Gamma_*}\sqrt{J_{j,k}R}.
\]

The localized phase-space trichotomy supplies a fixed natural-band fraction `beta_*>0`, hence

\[
\boxed{
\|P_{j,k}f_{j,k}(t_j)\|_2
\ge
c_P a_{j,k}R^{1/2},
\qquad
c_P:=\beta_*/\Gamma_*.
}
\]

This is the amplitude-sensitive replacement for the old fixed lower bound `c_f R^{1/2}`.

---

## 3. Remaining-time compression for an old shell

The first-hitting stage corridor gives

\[
T^*-t_j\le C_Tr_j^2.
\]

Since

\[
R=K_kr_j,
\]

the fraction of one old-shell natural time left after `t_j` is

\[
\boxed{
\frac{T^*-t_j}{R^2}
\le
C_TK_k^{-2}.
}
\]

Thus an old shell at large `K_k` has only a vanishing fraction of its own natural parabolic time remaining.

---

## 4. Amplitude-sensitive forgetting inequality

Suppose the shell is strongly forgotten before `T^*`, meaning that for some later time `t_f<T^*`,

\[
\|P_{j,k}f_{j,k}(t_f)\|_2
\le
\varepsilon
\|P_{j,k}f_{j,k}(t_j)\|_2,
\qquad 0\le\varepsilon<1,
\]

with the same moving packet convention used in `LOCALIZED_PACKET_EXACT_EVOLUTION_AND_FORGETTING_GATE_2026-08-23.md`.

The exact localized Duhamel gate gives, for sufficiently large `K_k`,

\[
\int_{t_j}^{t_f}
\left(
\|P_{j,k}\mathcal N_{j,k}\|_2
+
\|P_{j,k}\mathcal R_{j,k}\|_2
\right)dt
\ge
c_\varepsilon
\|P_{j,k}f_{j,k}(t_j)\|_2,
\]

because the heat attenuation tends to one on the compressed interval.

Using the amplitude-sensitive packet lower bound,

\[
\boxed{
\int_{t_j}^{t_f}
(\cdots)dt
\ge
c_0a_{j,k}R^{1/2},
\qquad
c_0=c_\varepsilon c_P>0.
}
\]

Now assume the quiet non-H/non-T/non-pressure forcing ceiling at the old shell scale,

\[
\boxed{
\|P_{j,k}\mathcal N_{j,k}(t)\|_2
+
\|P_{j,k}\mathcal R_{j,k}(t)\|_2
\le
K_*R^{-3/2}.
}
\]

Then the total action available before `T^*` is at most

\[
K_*R^{-3/2}(T^*-t_j)
\le
K_*C_TK_k^{-2}R^{1/2}.
\]

Comparison gives the necessary quiet-forgetting condition

\[
\boxed{
 a_{j,k}K_k^2
\le
C_{quiet}
:=
\frac{K_*C_T}{c_0}.
}
\]

Equivalently,

\[
\boxed{
J_{j,k}
\le
C_{quiet}^2K_k^{-4}.
}
\]

This is the central amplitude-sensitive remaining-time gate.

A small shell may be quietly forgotten, but only if its critical derivative amplitude is exponentially smaller than its age.

---

## 5. Sequence lemma: a non-L3 critical stack necessarily violates the quiet-forgetting threshold

Let

\[
K_k=q^{k/2},
\qquad
 a_k\ge0.
\]

Assume

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

Proof: if `a_kK_k^2<=C` for all sufficiently large `k`, then

\[
a_k\le CK_k^{-2}=Cq^{-k},
\]

so

\[
\sum_ka_k^3
\le
C^3\sum_kq^{-3k}<\infty,
\]

a contradiction.

More strongly, for every fixed `C>0`, define

\[
S_C:=\{k:a_kK_k^2>C\}.
\]

On its complement,

\[
a_k^3\le C^3q^{-3k},
\]

so

\[
\sum_{k\notin S_C}a_k^3<\infty.
\]

Therefore

\[
\boxed{
\sum_{k\in S_C}a_k^3=\infty.
}
\]

Thus the high-ratio shells are not a negligible exceptional subsequence; they carry the entire divergent cubic tail up to a summable remainder.

---

## 6. Connection with the corrected ancient tail criterion

The anti-proof-corrected annular cubic estimate gives, on the corresponding no-local-energy-failure corridor,

\[
\|V\|_{L^3(|Y|>R_0)}^3
\lesssim
\sum_k
\mathfrak E_{1,k}^{3/2}.
\]

Hence a non-`L^3` ancient survivor requires

\[
\boxed{
\sum_kJ_k^{3/2}=\infty.
}
\]

With

\[
a_k=J_k^{1/2},
\]
this is exactly

\[
\sum_ka_k^3=\infty.
\]

The sequence lemma therefore supplies arbitrarily remote shells satisfying

\[
\boxed{
J_k^{1/2}K_k^2\gg1.
}
\]

Such shells cannot be quietly forgotten under the remaining-time ceiling.

---

## 7. Diagonal transfer back to smooth first-hitting stages

Local ancient convergence only gives direct control on each fixed normalized annulus. Therefore the remote-shell selection must be diagonalized rather than asserted uniformly.

Choose shell ages

\[
k_n\to\infty
\]

from the ancient high-ratio set so that

\[
J_{\infty,k_n}^{1/2}K_{k_n}^2\to\infty.
\]

Then choose first-hitting indices `j_n` sufficiently large that

1. the stage-`j_n` rescaling approximates the ancient field on the annulus of radius `K_{k_n}`;
2. the corresponding shell amplitude obeys
   \[
   J_{j_n,k_n}^{1/2}K_{k_n}^2\to\infty;
   \]
3. `j_n-k_n->infinity`.

The third condition makes the physical shell radius

\[
R_n^{phys}
=r_{j_n}q^{k_n/2}
=r_{j_n-k_n}
\to0,
\]

so the selected shells belong to the late sliding-history regime rather than to a fixed early outer scale.

This is the correct prelimit realization of an escaping ancient tail.

---

## 8. Genealogy dichotomy for the selected high-ratio shells

For a selected shell with

\[
a_{j,k}K_k^2>C_{quiet},
\]

there are only the following possibilities.

### A. Large derivative ratio

If

\[
\Gamma_{j,k}>\Gamma_*,
\]

then the shell is already in `H`.

### B. Strong forgetting

If the shell loses a fixed fraction of its natural-band packet before `T^*`, the amplitude-sensitive remaining-time gate contradicts the quiet forcing ceiling.

Hence at least one of

- internal nonlinear turnover;
- material shell crossing;
- pressure-buffer transfer;
- viscous/Bogovskii boundary action;
- derivative leakage

must exceed the accepted quiet threshold.

This is an existing `T/H/pressure/residual` exit.

### C. Persistent natural-band memory

If neither A nor B occurs, the shell retains a fixed fraction of its natural-band packet through all sufficiently late checkpoint windows.

If infinitely many high-ratio shells remain in this persistent class, then they carry the divergent tail because the complement of every high-ratio set is cubically summable.

Moreover

\[
\sum_kJ_k^{3/2}=\infty
\quad\Longrightarrow\quad
\sum_kJ_k=\infty.
\]

Indeed, if infinitely many `J_k>=1` the latter sum is immediate; otherwise eventually `0<=J_k<1` and `J_k>=J_k^{3/2}`.

But

\[
\sum_kJ_k
\]

is precisely the dyadic form of the weighted derivative tower

\[
\boxed{
D_1
=
\int |x-X_*|\,|\nabla u|^2dx
}
\]

up to fixed annular overlap constants.

Thus the persistent high-ratio genealogy returns to the solenoidal Hardy--weighted-energy ledger.

After solenoidal localization and moving-center correction, the sharp Hardy--Leray gap forces the growing weighted derivative tower to appear as

\[
\boxed{
\text{weighted kinetic/pressure flux}
\quad\lor\quad
\text{rapid weighted-moment turnover}
\quad\lor\quad
\text{localization/center residual}.
}
\]

These are `T`/pressure/residual channels rather than a quiet persistent survivor.

---

## 9. Amplitude-sensitive historical genealogy reduction

Combining the three cases gives the conditional branch implication

\[
\boxed{
\begin{aligned}
\text{non-}L^3\text{ critical ancient tail}
\Longrightarrow\;&
H_{remote}
\\
&\lor T_{forget/rebuild}
\\
&\lor T_{Hardy\ flux/moment}
\\
&\lor\text{pressure/localization residual}.
\end{aligned}
}
\]

The fixed-positive-shell-occupancy hypothesis is no longer needed.

The crucial replacement is the arithmetic fact

\[
\boxed{
\sum a_k^3=\infty
\Longrightarrow
\text{the shells with }a_kK_k^2>C
\text{ still carry divergent cubic mass.}
}
\]

Remaining-time compression then kills forgetting on precisely those shells, while persistence returns them to the weighted Hardy ledger.

---

## 10. What is genuinely new versus the 2026-08-23 historical closure

The previous remaining-time closure selected an old shell using a positive-density fixed occupancy hypothesis

\[
m_{j,k}\ge\mu>0.
\]

That selection is invalid for a diffuse endpoint stack with amplitudes tending to zero.

The present note replaces it by

\[
\boxed{
J_{j,k}^{1/2}K_k^2\to\infty
}
\]

along an amplitude-selected subsequence.

The contradiction is correspondingly changed from

\[
1\lesssim K_k^{-2}
\]

to

\[
\boxed{
J_{j,k}^{1/2}
\lesssim K_k^{-2}.
}
\]

Divergent cubic tail mass is exactly strong enough to violate this exponential quiet-forgetting threshold.

---

## 11. Rigor status and remaining finite bridges

This is not yet a proof of global regularity. To make the branch implication theorem-level, three finite smooth bridges still need to be packaged with uniform constants:

1. **packet/annulus comparison:** the Bogovskii packet must transfer the annular `J_{j,k}` lower bound to the natural-band `L^2` lower bound with fixed constants on every selected shell;
2. **quiet forcing ceiling:** no-H/no-T/no-pressure hypotheses must imply
   \[
   \|P\mathcal N\|_2+\|P\mathcal R\|_2\le K_*R^{-3/2}
   \]
   uniformly even when the packet amplitude tends to zero;
3. **persistent Hardy localization:** the weighted Hardy--energy identity must be localized to the moving nested shell tower so that large flux, weighted-moment change, or correction terms are explicitly routed to the accepted `T/H/pressure` thresholds.

The diagonal transfer from the ancient tail to remote prelimit shells must also be written as a standard compactness diagonal argument, but it introduces no new mechanism.

Status: **THE DIFFUSE SMALL-AMPLITUDE ENDPOINT TAIL NO LONGER ESCAPES THE HISTORICAL-SHELL REDUCTION MERELY BECAUSE NO SHELL HAS FIXED POSITIVE OCCUPANCY. NON-L3 CUBIC DIVERGENCE FORCES ARBITRARILY OLD SHELLS ABOVE THE `K^{-2}` QUIET-FORGETTING AMPLITUDE THRESHOLD. SUCH SHELLS EITHER ACTIVATE H/T/PRESSURE DURING FORGETTING OR PERSIST INTO THE SOLENOIDAL HARDY FLUX/MOMENT LEDGER. GLOBAL REGULARITY REMAINS UNPROVED.**