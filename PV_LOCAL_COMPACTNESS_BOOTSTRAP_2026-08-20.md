# Local Compactness Bootstrap for a Threshold P_V Cell — 2026-08-20

Overall status: **THE PRECOMPACT CORE CLASS IS REDUCED TO A SHELL-H2 DICHOTOMY — GLOBAL REGULARITY NOT PROVED.**

This note combines four ingredients:

1. exact spatial localization of the H1 threshold;
2. the sharp H1 curvature bootstrap;
3. the first-hitting/non-H palinstrophy bound;
4. a standard cutoff comparison.

The result is that a bounded-radius threshold cell automatically generates a uniformly bounded local `H2` profile unless higher-derivative mass accumulates in its surrounding shell. That shell failure is itself an `H/T` exit.

---

## 1. Local strain enstrophy from global palinstrophy

The strain is a zero-order Calderon--Zygmund transform of the vorticity. Therefore, for `1<p<infinity`,

\[
\|S\|_p\lesssim_p\|\Omega\|_p.
\]

Sobolev gives

\[
\|\Omega\|_6
\lesssim
\|\nabla\Omega\|_2.
\]

Hence

\[
\|S\|_6
\lesssim
\|\nabla\Omega\|_2.
\]

For any ball of normalized radius `R`,

\[
\begin{aligned}
\|S\|_{L^2(B_R)}
&\le |B_R|^{1/3}\|S\|_6\\
&\lesssim R\|\nabla\Omega\|_2.
\end{aligned}
\]

Thus

\[
\boxed{
\|S\|_{L^2(B_R)}^2
\lesssim
R^2P_\Omega,
}
\]

where

\[
P_\Omega=\|\nabla\Omega\|_2^2.
\]

Therefore on a non-`H` subsequence with

\[
P_\Omega\le P_*,
\]

every fixed normalized ball has a uniform local strain-enstrophy bound.

This estimate is compatible with a globally large passive velocity tail: it uses derivative/vorticity control rather than global kinetic energy.

---

## 2. A bounded threshold cell

By the threshold-localization lemma, if

\[
\eta_{VI}
=
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{\|\Delta S\|_2^2}
\ge\nu-o(1),
\]

then some spatial cell has local ratio at least the same threshold.

On the non-`T` branch, such threshold cells remain inside a fixed normalized parent radius `R_0` after recentering by the nested singular point.

Choose a smooth cutoff `chi` such that

\[
\chi=1\text{ on }B_{R_0},
\qquad
\operatorname{supp}\chi\subset B_{2R_0},
\]

and

\[
|\nabla\chi|\lesssim R_0^{-1},
\qquad
|\Delta\chi|\lesssim R_0^{-2}.
\]

Set

\[
F=\chi S.
\]

---

## 3. Cutoff derivative comparisons

The first derivative is

\[
\nabla F
=\chi\nabla S+S\otimes\nabla\chi.
\]

Hence

\[
\boxed{
\|\nabla F\|_2^2
\lesssim
\int_{B_{2R_0}}|\nabla S|^2
+
R_0^{-2}
\int_{A_{R_0,2R_0}}|S|^2.
}
\]

The second derivative is

\[
\Delta F
=\chi\Delta S
+2\nabla\chi\cdot\nabla S
+(\Delta\chi)S.
\]

Therefore

\[
\boxed{
\|\Delta F\|_2^2
\lesssim
\int_{B_{2R_0}}|\Delta S|^2
+
R_0^{-2}
\int_{A_{R_0,2R_0}}|\nabla S|^2
+
R_0^{-4}
\int_{A_{R_0,2R_0}}|S|^2.
}
\]

The final term is uniformly bounded by the local-enstrophy estimate from Section 1.

---

## 4. Threshold transfer or shell-H exit

Let the threshold cell be contained in the region where `chi=1`. The local sharp H1 estimate gives

\[
Q_{core}
\le
\frac4{\sqrt6}
N_{core},
\]

where

\[
N_{core}
=\int_{core}|S||\nabla S|^2.
\]

If

\[
Q_{core}\ge c_\nu H_{core}
\]

for some positive threshold `c_nu`, then

\[
N_{core}\gtrsim_\nu H_{core}.
\]

Because `F=S` on the core,

\[
N_F
=\int|F||\nabla F|^2
\ge N_{core}.
\]

There are now two alternatives.

### Alternative A: controlled surrounding H2 mass

If

\[
\int_{B_{2R_0}}|\Delta S|^2
\le C_D H_{core}
\]

and the shell lower-order terms are controlled, then

\[
H_F\lesssim H_{core},
\]

so

\[
\boxed{
\frac{N_F}{H_F}
\ge c(\nu,C_D)>0.
}
\]

The curvature bootstrap then gives a uniform scale-invariant curvature cap for `F`.

### Alternative B: shell H2 domination

If no such `C_D` exists along a dangerous subsequence, then higher-derivative mass in the surrounding shell dominates the threshold core:

\[
\int_{A_{R_0,2R_0}}|\Delta S|^2
\gg H_{core}.
\]

This is a genuine higher-derivative secondary packet. Repeated occurrence is an `H` event, and if its spatial location escapes across expanding parent shells it is also derivative non-tightness `T`.

Thus the failure of threshold transfer is itself an already classified exit channel.

---

## 5. Automatic H1/H2 bounds in Alternative A

In Alternative A, the local strain-enstrophy estimate gives

\[
E_F=\|F\|_2^2
\le C(R_0,P_*).
\]

The lower bound

\[
N_F/H_F\ge c_0>0
\]

combined with

\[
N_F\lesssim P_F^{5/4}H_F^{1/4}
\]

yields the curvature cap

\[
H_F^{1/2}/P_F^{5/6}\le K(c_0).
\]

Together with

\[
P_F^2\le E_FH_F,
\]

this gives

\[
\boxed{
P_F\le C(R_0,P_*,\nu,C_D),
}
\]

and

\[
\boxed{
H_F\le C(R_0,P_*,\nu,C_D).
}
\]

Thus every transferred threshold core lies in a uniformly bounded local `H2` class.

---

## 6. Precompactness

With fixed center, fixed cutoff support, and uniform `H2` bounds, Rellich compactness gives

\[
F_j\to F_*
\]

strongly in `H^s` for every `s<2` along a subsequence. For `s>3/2`, this gives uniform/Hölder control, while for `s>1` it gives strong `H1` convergence.

The first-hitting nontriviality condition prevents the core limit from vanishing, provided the vorticity maximum remains in the interior cell.

Therefore

\[
\boxed{
\text{non-H/T transferred threshold cell}
\Longrightarrow
\text{precompact nontrivial local H2 class}.
}
\]

This is precisely the class needed for the strict H1 efficiency-gap argument.

---

## 7. Logical consequence

The previous conditional route

\[
\text{assume precompact class}
\Longrightarrow
\text{strict H1 efficiency gap}
\]

is now replaced, modulo the explicit shell-H alternative, by

\[
\boxed{
\text{dangerous threshold}
\Longrightarrow
\begin{cases}
H/T\text{ shell exit},\\
\text{precompact threshold core}.
\end{cases}
}
\]

Thus precompactness is no longer an independent endgame assumption.

---

## 8. Remaining local obstruction

On the precompact threshold-core class, exact maximal H1 production is impossible and a uniform efficiency gap exists. The remaining number is the attained variational ratio

\[
\Lambda_K
=
\sup_{S\in K}
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}
{\|\Delta S\|_2^2}.
\]

The decisive unresolved question remains

\[
\boxed{\Lambda_K<\nu\ ?}
\]

If `Lambda_K >= nu`, a maximizing compact core profile exists after subsequence extraction and becomes the next rigidity object.

Status: **A BOUNDED-RADIUS H1 THRESHOLD CELL EITHER GENERATES A SECONDARY H/T DERIVATIVE PACKET IN ITS SURROUNDING SHELL OR BOOTSTRAPS TO A UNIFORMLY BOUNDED PRECOMPACT LOCAL H2 CLASS. THE FINAL LOCAL OBSTRUCTION IS NOW AN ATTAINED VARIATIONAL THRESHOLD PROFILE. GLOBAL REGULARITY REMAINS UNPROVED.**