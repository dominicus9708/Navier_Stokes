# DSD Betchov High-Enstrophy / Remote-Mass Witness

Date: 2026-08-25

Status: **CANONICAL HIGH-ENSTROPHY WITNESS DERIVED / REMOTE MASS FRACTION DERIVED / NO IDENTIFICATION WITH TURNOVER MADE / GLOBAL REGULARITY NOT PROVED.**

## 1. Purpose

`DSD_RECURRENT_DIRECT_BETCHOV_FREQUENCY_BARRIER_2026-08-25.md` gives the standard backward-Leray necessary condition

\[
Z_{L,+}\ge54\pi^2\nu^{3/2}
\]

for every nonzero recurrent bounded-enstrophy survivor.

`DSD_FIRST_HITTING_TO_LERAY_ENSTROPHY_TRANSFER_2026-08-25.md` gives the exact conversion between standard Leray enstrophy and the parent first-hitting normalization.

The aim here is to turn the abstract large `Z_L` requirement into a finite, canonical spatial witness rather than an arbitrarily chosen tightness radius.

---

## 2. A near-maximal Leray-enstrophy time exists

Let

\[
Z_{L,+}:=\sup_{s\ge s_0}Z_L(s).
\]

Fix any finite fraction

\[
0<\eta_B<1.
\]

Since

\[
Z_{L,+}\ge54\pi^2\nu^{3/2},
\]

there exists a sufficiently late recurrent time `s=s_B` for which

\[
\boxed{
Z_L(s_B)
\ge
\eta_B\,54\pi^2\nu^{3/2}.
}
\]

No attainment of the supremum is assumed.

Let this physical time lie in first-hitting stage `j`.

---

## 3. Convert the witness to parent first-hitting variables

In the parent stage-`j` normalization define

\[
\widetilde Z_j(t)
=
\frac{r_j}{\nu^2}\|\omega(t)\|_2^2.
\]

The exact normalization relation is

\[
Z_L(s)
=
\nu^{3/2}\Theta_j(t)^{1/2}\widetilde Z_j(t),
\]

where

\[
\Theta_j(t)=W_j(T^*-t).
\]

On the recurrent stage corridor,

\[
\Theta_j(t)
\le
\Theta_+
=
\frac{q}{q-1}L_+.
\]

Therefore the Betchov witness time satisfies

\[
\boxed{
\widetilde Z_B
:=
\widetilde Z_j(t_B)
\ge
\eta_B\,54\pi^2
\Theta_+^{-1/2}.
}
\]

Equivalently,

\[
\boxed{
\widetilde Z_B
\ge
\eta_B\,54\pi^2
\sqrt{\frac{q-1}{qL_+}}.
}
\]

The viscosity cancels exactly.

Thus a recurrent survivor must contain actual late first-hitting stages with quantitatively large parent-normalized enstrophy.

---

## 4. Parent-stage pointwise amplitude cap

During stage `j`, the physical vorticity maximum is below the next first-hitting level:

\[
\|\omega(t)\|_\infty
\le
W_{j+1}=qW_j.
\]

Since

\[
\Omega_j=\omega/W_j,
\]

we have the global parent-normalized cap

\[
\boxed{
\|\Omega_j(t)\|_\infty\le q.
}
\]

In particular at the Betchov witness time,

\[
\boxed{
|\Omega_B(y)|^2\le q^2.
}
\]

---

## 5. Define the canonical enstrophy quantile radius

Fix

\[
0<\varepsilon<1.
\]

Around the tracked first-hitting center define

\[
\boxed{
R_\varepsilon[\Omega]
:=
\inf\left\{
R>0:
\int_{B_R}|\Omega|^2dy
\ge
(1-\varepsilon)\|\Omega\|_2^2
\right\}.
}
\]

This is a canonical finite witness attached to the actual vorticity distribution. It is not an arbitrarily enlarged tightness radius.

At the Betchov witness time write

\[
R_{\varepsilon,B}:=R_\varepsilon[\Omega_B].
\]

---

## 6. High enstrophy forces a finite radius floor

By the pointwise amplitude cap,

\[
\int_{B_R}|\Omega_B|^2dy
\le
q^2|B_R|
=
q^2\frac{4\pi}{3}R^3.
\]

At the quantile radius, approximating from above if the infimum is not attained,

\[
(1-\varepsilon)\widetilde Z_B
\le
q^2\frac{4\pi}{3}R_{\varepsilon,B}^3.
\]

Therefore

\[
\boxed{
R_{\varepsilon,B}^3
\ge
\frac{3(1-\varepsilon)}{4\pi q^2}
\widetilde Z_B.
}
\]

Insert the Betchov lower bound:

\[
\boxed{
R_{\varepsilon,B}^3
\ge
\eta_B
\frac{81\pi}{2q^2}
(1-\varepsilon)
\Theta_+^{-1/2}.
}
\]

Using the stage ceiling,

\[
\boxed{
R_{\varepsilon,B}^3
\ge
\eta_B
\frac{81\pi}{2q^2}
(1-\varepsilon)
\sqrt{\frac{q-1}{qL_+}}.
}
\]

This is a canonical radius lower bound at a real late recurrent time.

---

## 7. Remote-mass witness

By definition of the quantile radius, for every

\[
0<R<R_{\varepsilon,B}
\]

one has

\[
\int_{B_R}|\Omega_B|^2dy
<
(1-\varepsilon)\widetilde Z_B.
\]

Hence

\[
\boxed{
\int_{|y|>R}|\Omega_B|^2dy
>
\varepsilon\widetilde Z_B.
}
\]

Choose, for example,

\[
R=\alpha R_{\varepsilon,B},
\qquad
0<\alpha<1.
\]

Then the finite remote witness obeys

\[
\boxed{
\int_{|y|>\alpha R_{\varepsilon,B}}
|\Omega_B|^2dy
>
\varepsilon\widetilde Z_B
\ge
\varepsilon\eta_B\,54\pi^2
\sqrt{\frac{q-1}{qL_+}}.
}
\]

Thus the direct Betchov barrier forces not merely large total normalized enstrophy, but a definite remote enstrophy fraction beyond a definite canonical radius unless the tracked center ball itself has the required large volume.

---

## 8. q=2 representative values

For `q=2`, the radius floor becomes

\[
\boxed{
R_{\varepsilon,B}^3
\ge
\eta_B
\frac{81\pi}{8}
(1-\varepsilon)
(2L_+)^{-1/2}.
}
\]

Taking the limiting display value `eta_B -> 1` and, only for scale illustration,

\[
\varepsilon=\frac14,
\]

gives approximately

\[
\begin{array}{c|c}
L_+ & R_{1/4,B}\text{ floor}\\
\hline
0.10 & 3.7644\\
0.20 & 3.3537\\
0.30 & 3.1346\\
0.50 & 2.8787\\
0.75 & 2.6906\\
1.00 & 2.5647\\
1.50 & 2.3971\\
2.00 & 2.2849
\end{array}
\]

These are not imported proof constants; they show the scale of the forced finite witness.

---

## 9. Relation to the existing remote branch

The repository already distinguishes

\[
V_{remote}
=
\text{loss of scale-uniform vorticity/enstrophy tightness around the tracked core}
\]

from material turnover `T`.

The present result does not identify

\[
V_{remote}=T.
\]

Instead it provides a new finite source for that branch:

\[
\boxed{
\text{bounded-Z recurrent survivor}
\Longrightarrow
\text{late high-enstrophy quantile-radius witness}.
}
\]

At that witness time, either

- the remote vorticity mass is derivative-active and routes to `H_remote`; or
- the amplitude-sensitive localized-solenoidal estimates convert it into a kinetic / critical-cubic velocity reservoir.

Thus DBRFB connects directly to the already derived common frontier

\[
\boxed{
\text{critical cubic tail}
\lor H_{remote}
\lor T/V_{remote}.
}
\]

---

## 10. DSD audit

The formed finite witness consists of

- one late recurrent time `t_B`;
- parent normalized enstrophy `Ztilde_B`;
- pointwise amplitude cap `q`;
- canonical quantile radius `R_epsilon,B`;
- finite exterior enstrophy fraction `epsilon Ztilde_B`.

No infinite tail is treated as a primitive formed object.

---

## 11. Updated frontier

The direct Betchov barrier now has a spatially explicit consequence:

\[
\boxed{
\text{recurrent bounded-Z}
\Longrightarrow
\text{large finite vorticity reservoir at a late time},
}
\]

and that reservoir cannot fit inside an arbitrarily small normalized region because the first-hitting amplitude is capped.

The next dynamic question is therefore no longer whether remote mass exists. It does.

The remaining gate is:

\[
\boxed{
\text{Can these repeatedly forced finite remote-vorticity witnesses be reconfigured from stage to stage}
\text{ without accumulating }H_{remote}\text{ or }T\text{ cost?}
}
\]

This is the precise bridge to the genealogy/return-density ledger.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
