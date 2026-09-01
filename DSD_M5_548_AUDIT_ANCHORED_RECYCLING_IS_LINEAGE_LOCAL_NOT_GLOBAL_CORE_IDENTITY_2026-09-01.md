# DSD M5-548 — Audit correction: anchored transverse recycling is lineage-local, not a global core identity

Date: 2026-09-01

Status: **SCOPE CORRECTION OF M5-547 / THE EXACT ANCHORED IDENTITY `P_perp(Sigma W + Delta W)=0` IS PROVED ALONG THE PERSISTENT MATERIAL LINEAGE REPRESENTATIVE WHERE `D_B xi=0`; IT DOES NOT AUTOMATICALLY HOLD AT EVERY POINT OF THE FINITE ACTIVE CORE / CONSEQUENTLY M5-547'S POINTWISE CROSS-CHANNEL CANCELLATION IS EXACT ON THE MARKED TRAJECTORY AND CAN BE THICKENED TO AN APPROXIMATE CANCELLATION ON A SMALL ACTIVE TUBE BY UNIFORM SMOOTHNESS, BUT IT CANNOT BE INSERTED AS AN EXACT IDENTITY INTO THE ENTIRE CORE PALINSTROPHY INTEGRAL / THE CORRECT SURVIVOR IS A POSITIVE-MEASURE RECURRENT TUBE OF NEAR-RECYCLING, NOT GLOBAL TRANSVERSE CANCELLATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact statement inherited from M5-516

For an anchored persistent material lineage `Y_i(theta)`, let

\[
W(Y_i(\theta),\theta)=\rho_i(\theta)\xi_i,
\]

with fixed direction

\[
\xi_i'=0.
\]

The exact material direction equation gives **on that trajectory**

\[
\boxed{
(I-\xi_i\otimes\xi_i)
\left(
\Sigma W+\Delta W
\right)
(Y_i(\theta),\theta)
=0.
}
\]

Equivalently,

\[
\boxed{
A_i+B_i=0
}
\]

at the marked lineage point, where

\[
A_i=P_{\xi_i}^\perp\Sigma W,
\qquad
B_i=P_{\xi_i}^\perp\Delta W.
\]

This is exact.

---

## 2. What is not inherited

The anchored frame is a genealogy/material-lineage mark.

It does **not** imply that the full Eulerian direction field satisfies

\[
D_B\xi(y,\theta)=0
\]

for every

\[
y\in B_{R_{core}}.
\]

Nor does it imply

\[
P_\xi^\perp(\Sigma W+\Delta W)=0
\]

throughout the entire coherent carrier ball.

Nearby vorticity directions may have nonzero material directional velocity even when the representative lineage direction is anchored.

Therefore the exact cancellation

\[
P_\perp\Delta W=-P_\perp\Sigma W
\]

cannot be inserted globally into

\[
\int_{B_{R_{core}}}|\Delta W|^2dy
\]

without an additional rigidity theorem.

---

## 3. Correction to the M5-547 interpretation

M5-547 correctly derived the algebraic pointwise identity

\[
-\Sigma W\cdot\Delta W
=-ab+|A|^2
\]

whenever

\[
B=-A.
\]

It also correctly observed that at such a point

\[
|\Delta W|^2=b^2+|A|^2.
\]

The overreach is only the passage from this lineage-local equality to an exact cancellation of the **whole localized palinstrophy integral**.

The corrected statement is

\[
\boxed{
\text{exact projected recycling on the anchored lineage},
}
\]

not

\[
\text{exact projected recycling on the whole core}.
\]

---

## 4. Smooth thickening around an active anchored point

The correction does not reduce the result to a measure-zero curiosity.

On the M5-508 smooth compact core, all fixed derivatives of

\[
\Sigma W,
\qquad
\Delta W,
\qquad
D_B\xi
\]

are uniformly bounded on active regions where

\[
\rho\ge\rho_0>0.
\]

Suppose at the anchored marker

\[
|A_i(Y_i,\theta)|\ge a_0>0.
\]

Continuity gives a radius

\[
r_a=r_a(a_0,\rho_0,\text{smooth caps})>0
\]

such that on

\[
B_{r_a}(Y_i(\theta))
\]

we have

\[
|A(y)-A_i(Y_i)|\le a_0/10
\]

and

\[
|A(y)+B(y)|\le a_0/10
\]

provided the local direction projection is chosen continuously from the active marker.

Thus

\[
B=-A+\mathcal R,
\qquad
|\mathcal R|\le a_0/10
\]

on a fixed active tube.

---

## 5. Quantitative near-recycling on the active tube

On that tube,

\[
A\cdot B
=
-|A|^2+A\cdot\mathcal R.
\]

Hence

\[
-A\cdot B
\ge
|A|^2-|A||\mathcal R|.
\]

Since `|A|` remains comparable to `a_0`, one obtains

\[
\boxed{
-A\cdot B
\ge
c_a|A|^2
}
\]

for a fixed

\[
c_a>0.
\]

Likewise

\[
|B|^2
=|A-\mathcal R|^2
\]

is comparable to `|A|^2`.

Therefore the M5-547 recycling mechanism survives **quantitatively** on a positive-volume active tube, but only up to fixed comparability/error constants.

---

## 6. Positive spacetime tube measure

The anchored ratchet/dual events recur with positive log-scale frequency.

M5-493-style time thickening gives a fixed interval length

\[
\delta\theta_a>0
\]

around each active anchored event on which the smooth bounds and amplitude threshold persist.

Thus the near-recycling tube has positive spacetime measure per recurrent event:

\[
\boxed{
|B_{r_a}|\,\delta\theta_a>0.
}
\]

Hence the mechanism contributes a positive recurrent local integral, not merely a pointwise identity.

---

## 7. Corrected palinstrophy consequence

Decompose the localized core into

1. the active anchored tube `T_a`;
2. its complement.

On `T_a`, the transverse stretching-diffusion cross term recycles a fixed fraction of the projected-Laplacian cost.

Schematically,

\[
\boxed{
-\int_{T_a}
(P_\perp\Sigma W)\cdot(P_\perp\Delta W)
\ge
c_a
\int_{T_a}|P_\perp\Delta W|^2.
}
\]

However no equality is asserted for the complement.

Thus the global localized palinstrophy ledger retains

\[
H_R
\]

minus only a quantitatively recycled **tube fraction**, not the entire projected component.

---

## 8. Impact on the M5-546 excess strategy

The corrected conclusion cuts both ways.

It prevents the false claim that the anchored branch is completely cost-free at the projected derivative level.

But it also shows that a fixed portion of the marked projected cost can be paid automatically by the exact local cross-channel geometry.

Therefore an excess lemma must distinguish

\[
\boxed{
\text{recyclable anchored-tube cost}
}

from

\[
\boxed{
\text{unrecycled core cost outside that exact local cancellation}.
}
\]

The candidate contradiction cannot charge the same tube dissipation twice.

---

## 9. Revised branch-specific target

Let

\[
H_{tube}
:=
\int_{T_a}|P_\perp\Delta W|^2
\]

and let

\[
H_{rest}:=H_R-H_{tube}.
\]

The anchored branch can recycle a controlled fraction of `H_tube`.

A genuine excess theorem would need to prove one of the following:

1. a fixed positive part of `H_tube` remains unrecycled because the cancellation cannot be exact on the whole tube;
2. `H_rest` has a fixed positive mean forced by the dual/ratchet geometry;
3. maintaining the near-recycling tube forces a separate positive flux, amplitude-migration, or advection cost.

Any of these would restore a positive invariant excess.

---

## 10. DSD audit verdict

The valid inheritance chain is

\[
\boxed{
\text{anchored lineage}
\Rightarrow
\text{exact pointwise transverse recycling}
\Rightarrow
\text{positive-volume near-recycling tube}.
}
\]

The invalid shortcut is

\[
\boxed{
\text{anchored lineage}
\not\Rightarrow
\text{global core transverse cancellation}.
}
\]

M5-548 supersedes the global-integral interpretation of M5-547 while preserving its local algebraic mechanism.

---

## 11. Highest-value next target

Return to the exact scalar amplitude equation **along the representative anchored lineage**, where the identity is genuinely pointwise and no Eulerian-volume extension is required:

\[
D_B\rho+\rho=a+b.
\]

Because the marker itself can migrate within one material flux lineage (M5-518), the correct observable should use either

- the anchored material marker while it remains nondegenerate; or
- the material-surface flux-density transport law of M5-520--521 when the amplitude carrier migrates.

The next audit should split these two cases and determine whether the remaining parallel channel is an amplitude coboundary or a surface-current cost.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]