# DSD M5-523 — Biot--Savart plus enstrophy tightness forces uniform velocity vanishing at spatial infinity

Date: 2026-09-01

Status: **DYNAMICAL SPATIAL-DECAY RECOVERY / M5-510 CORRECTLY SHOWED THAT ABSTRACT ALL-ORDER SOBOLEV COMPACTNESS DOES NOT FORCE THE SPATIAL TYPE-I RATE `|U(y)|<=C/|y|` / HOWEVER THE ACTUAL NAVIER--STOKES HULL ALSO HAS UNIFORM VORTICITY `L2` TIGHTNESS AND THE BIOT--SAVART RELATION / SPLITTING VORTICITY INTO AN INNER CORE AND AN OUTER TAIL GIVES A UNIFORM FAR-FIELD VELOCITY ESTIMATE `|U(y)| <= C Z_*^(1/2)|y|^(-1/2) + C M_*^(1/3) E_tail(|y|/2)^(1/3)` / HENCE `U(y,theta)->0` UNIFORMLY ON THE COMPACT HULL AS `|y|->infinity` / THE RATE IS STILL TOO WEAK TO SUPPLY `1/|y|` OR `L3`, SO GENERAL DSS/RECURRENT LIOUVILLE CLOSURE DOES NOT FOLLOW / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs

On the M5-508 globally smooth compact branch,

\[
\boxed{
\sup_\theta\|W(\theta)\|_2^2
\le Z_*<\infty,
}
\]

and

\[
\boxed{
\sup_\theta\|W(\theta)\|_\infty
\le M_*<\infty.
}
\]

Uniform enstrophy tightness gives the modulus

\[
\boxed{
\varepsilon_E(R)
:=
\sup_\theta
\int_{|z|>R}|W(z,\theta)|^2dz
\longrightarrow0
\quad(R\to\infty).
}
\]

The similarity velocity is reconstructed from vorticity by the whole-space Biot--Savart law after the Galilean mode is fixed:

\[
U(y)
=
C_{BS}
\int_{\mathbb R^3}
\frac{(y-z)\times W(z)}{|y-z|^3}\,dz.
\]

The kernel has magnitude `O(|y-z|^-2)`.

---

## 2. Split at half the observation radius

Fix `y` with

\[
r:=|y|\gg1
\]

and split

\[
W=W_{in}+W_{out}
\]

using a smooth radial cutoff at radius

\[
R:=r/2.
\]

The inner part is supported in `|z|<~R`, while the outer part is supported in the exterior of a comparable radius.

Write correspondingly

\[
U=U_{in}+U_{out}.
\]

---

## 3. Inner-core contribution

For `|z|<=r/2`,

\[
|y-z|\ge r/2.
\]

Therefore

\[
|U_{in}(y)|
\le
Cr^{-2}
\int_{|z|<r/2}|W(z)|dz.
\]

Cauchy--Schwarz gives

\[
\int_{|z|<r/2}|W|dz
\le
|B_{r/2}|^{1/2}\|W\|_2
\le
Cr^{3/2}Z_*^{1/2}.
\]

Hence

\[
\boxed{
|U_{in}(y)|
\le
C Z_*^{1/2}r^{-1/2}.
}
\]

This bound is uniform over the entire hull.

---

## 4. Biot--Savart `L2`--`Linfinity` estimate for the tail

Let `F` be a vorticity field in `L2 cap Linfinity` and let

\[
K*F
\]

be its Biot--Savart velocity.

Split the convolution around the evaluation point at a radius `rho>0`.

The near part satisfies

\[
\int_{|h|<\rho}|h|^{-2}|F(y-h)|dh
\le
C\rho\|F\|_\infty.
\]

The far part satisfies, by Cauchy--Schwarz,

\[
\begin{aligned}
\int_{|h|>\rho}|h|^{-2}|F(y-h)|dh
&\le
\|F\|_2
\left(\int_{|h|>\rho}|h|^{-4}dh\right)^{1/2}\\
&\le
C\rho^{-1/2}\|F\|_2.
\end{aligned}
\]

Optimizing

\[
\rho\|F\|_\infty
\sim
\rho^{-1/2}\|F\|_2
\]

gives

\[
\boxed{
\|K*F\|_\infty
\le
C
\|F\|_2^{2/3}
\|F\|_\infty^{1/3}.
}
\]

This is the same optimized splitting mechanism used earlier for the Type-I velocity bound.

---

## 5. Apply the tail estimate

For the exterior cutoff field `W_out`,

\[
\|W_{out}\|_2^2
\le
C\varepsilon_E(r/4)
\]

up to harmless cutoff-width changes, while

\[
\|W_{out}\|_\infty
\le
CM_*.
\]

Therefore

\[
\boxed{
\|U_{out}\|_\infty
\le
C
M_*^{1/3}
\varepsilon_E(r/4)^{1/3}.
}
\]

The exact fraction `r/4` is immaterial; any fixed comparable exterior radius gives the same conclusion.

---

## 6. Uniform far-field velocity estimate

Combining Sections 3 and 5,

\[
\boxed{
\sup_\theta|U(y,\theta)|
\le
C Z_*^{1/2}|y|^{-1/2}
+
C M_*^{1/3}
\varepsilon_E(|y|/4)^{1/3}.
}
\]

Since

\[
\varepsilon_E(R)\to0,
\]

we obtain

\[
\boxed{
\lim_{R\to\infty}
\sup_\theta
\sup_{|y|>R}
|U(y,\theta)|
=0.
}
\]

Thus the actual Navier--Stokes compact hull has uniform velocity vanishing at infinity.

---

## 7. This improves M5-510 but does not contradict it

M5-510 gave an abstract function-space counterexample showing that

\[
\text{all-order smooth compactness}
\not\Rightarrow
|U(y)|\lesssim|y|^{-1}.
\]

M5-523 uses two additional pieces absent from that abstract counterexample:

1. `W=curl U` is uniformly enstrophy-tight;
2. `U` is the Biot--Savart reconstruction of `W`.

These imply

\[
U\to0
\]

uniformly, but the estimate only supplies a generic `r^-1/2` core bound plus the unspecified enstrophy-tail modulus.

Therefore M5-510's firewall against silently claiming `1/r` decay remains valid.

---

## 8. Why the core bound stops at `r^-1/2`

The loss comes from estimating the inner vorticity only in `L2`:

\[
\|W\|_{L^1(B_R)}
\le
C R^{3/2}\|W\|_2.
\]

Inserted into a `1/r^2` Biot--Savart kernel, this gives

\[
r^{-2}R^{3/2}
\sim
r^{-1/2}.
\]

To reach

\[
|U(y)|\lesssim r^{-1}
\]

by this route would require additional low-frequency/moment information, such as suitable `L1`-type vorticity control or cancellation of the leading multipole contribution.

Neither is presently available from finite enstrophy alone.

---

## 9. Uniform vanishing and external Liouville results

The recovered condition

\[
U(y,\theta)\to0
\quad\text{uniformly in }\theta
\]

is useful but does not by itself place a general recurrent similarity orbit in the known nonexistence classes.

For exact/local asymptotically DSS profiles, Chae's Navier--Stokes theorem uses a time-periodic profile in

\[
C^1_\theta\big(L^3_y\cap C^2_y\big).
\]

The present branch has

\[
U(\theta)\in L^6
\]

uniformly, but finite enstrophy does not imply

\[
U\in L^3.
\]

Likewise the 2026 Pineau--Vicol Type-I RSS/RDSS theorems impose stronger spatial Type-I structure and/or restrictions on the rotation/scaling parameters.

Thus no external Liouville theorem is imported here to close the general recurrent hull.

---

## 10. Low-frequency interpretation

The remaining gap between

\[
U\to0
\]

and

\[
U\in L^3
\quad\text{or}\quad
|U(y)|\lesssim|y|^{-1}
\]

is a low-frequency/far-field moment problem rather than a high-derivative problem.

M5-507 has already bounded every finite positive Sobolev order of `W`.

Therefore any obstruction to stronger velocity decay lives in quantities like

\[
\|W\|_{\dot H^{-1}},
\qquad
\|U\|_2,
\qquad
\text{or low spatial moments of }W,
\]

not in another positive-derivative escalation.

This identifies a new precise frontier:

\[
\boxed{
H_{low}^{velocity}
:
\text{insufficient low-frequency/moment control to upgrade uniform }U\to0
\text{ to a Liouville-class decay/integrability condition}.
}
\]

---

## 11. Highest-value next target

The next calculation should audit whether the first-hitting/dilation genealogy supplies extra **low-frequency cancellation** that a generic `L2` vorticity field does not have.

Useful candidates are

\[
\int W\,dy,
\qquad
\int y\times W\,dy,
\qquad
\|W\|_{\dot H^{-1}}^2=\|U\|_2^2,
\]

with cutoffs if the raw moments are not absolutely convergent.

The key question is whether persistent finite-flux lineages and global enstrophy tightness force one of these low-frequency quantities to be finite/tight.

If `U` could be upgraded to `L3` on a periodic component, existing asymptotically DSS nonexistence results would become directly applicable.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
