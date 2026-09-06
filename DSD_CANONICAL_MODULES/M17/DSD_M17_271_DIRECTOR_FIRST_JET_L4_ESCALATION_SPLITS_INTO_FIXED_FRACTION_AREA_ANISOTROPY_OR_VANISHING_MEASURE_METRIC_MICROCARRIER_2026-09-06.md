# DSD M17-271 — Director first-jet L4 escalation splits into fixed-fraction area/anisotropy or a vanishing-measure metric microcarrier

Date: 2026-09-06  
Canonical ID: **M17-271**

Status: **FIRST-JET RECONNECTION / M17-269--270 RETURN BULK SECOND-JET GROWTH TO DIRECTOR FIRST-JET METRIC ESCALATION, NORMALIZED PALINSTROPHY, OR STRICT SUBSCALE. WRITE `g=|grad xi|^2`. DIVERGENCE OF `||grad xi||_4^4=int g^2` HAS THE SAME MEASURE-THEORETIC DICHOTOMY CORRECTED IN M17-219: EITHER A FIXED POSITIVE FRACTION OF THE ACTIVE PACKET LIES AT A THRESHOLD `g -> infinity`, OR THE SECOND MOMENT IS CARRIED BY SETS OF VANISHING PACKET MEASURE. ON THE FIXED-FRACTION BRANCH THE EXACT RANK-2 FACTORIZATION `g=2|J_xi| A_xi` FORCES A FIXED-FRACTION HIGH-DIRECTOR-AREA OR HIGH-ANISOTROPY SUBCARRIER. ON THE VANISHING-MEASURE BRANCH THE METRIC ESCALATION IS A TRUE MICROCARRIER AND RETURNS TO STRICT SUBSCALE/NODAL BOOKKEEPING. THUS FIRST-JET ESCALATION IS NOT A NEW UNTYPED ENDPOINT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Metric scalar

On a Rank-2 active tangent patch define

\[
\boxed{g:=|\nabla\xi|^2.}
\]

Then

\[
\boxed{
\|\nabla\xi\|_{L^4}^4
=\int g^2.
}
\]

On the active amplitude corridor of M17-270, packet-weighted and Lebesgue measures on a fixed rescaled ball are comparable because

\[
0<a_*\le a\le a^*<\infty.
\]

Thus the M17-219 concentration dichotomy may be used without changing which sets have vanishing or fixed positive packet fraction.

---

## 2. Measure-theoretic split

Suppose

\[
\int_B g_j^2\,dz\to\infty.
\]

Exactly one of the following mechanisms survives after subsequence extraction.

### Fixed-fraction high metric

There exist

\[
\vartheta>0,
\qquad
L_j\to\infty
\]

such that

\[
\boxed{
|\{g_j\ge L_j\}\cap B|
\ge\vartheta |B|.
}
\]

### Vanishing-measure metric microcarrier

Otherwise the high second moment can be captured on sets `S_j` satisfying

\[
\boxed{|S_j|/|B|\to0}
\]

while

\[
\boxed{
\int_{S_j}g_j^2\,dz
\not\to0
}
\]

and, along a suitable threshold sequence, carries the divergent tail.

This is the same uniform-integrability firewall used in M17-219.

---

## 3. Exact Rank-2 factorization

Let the nonzero singular values of `D xi` be

\[
s_1\ge s_2>0.
\]

Then

\[
\boxed{g=s_1^2+s_2^2}
\]

and

\[
\boxed{|J_\xi|=s_1s_2.}
\]

Define the anisotropy factor

\[
\boxed{
\mathcal A_\xi
:=\frac{s_1^2+s_2^2}{2s_1s_2}
\ge1.
}
\]

Therefore

\[
\boxed{
g=2|J_\xi|\mathcal A_\xi.}
\]

This is the M17-213 exact factorization.

---

## 4. Fixed-fraction high metric forces area or anisotropy

On

\[
g\ge L_j,
\]

at least one of

\[
|J_\xi|\ge L_j^{1/2}
\]

or

\[
\mathcal A_\xi\ge\frac12L_j^{1/2}
\]

must hold.

A finite pigeonhole split preserves at least half of the fixed packet fraction.
Hence

\[
\boxed{
G_{fixed\text{-}fraction\ high\ metric}
\Longrightarrow
G_{fixed\text{-}fraction\ high\ director\ area}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}.
}
\]

The first branch reconnects to the M17-214 director-area / flux-fiber compactness gate.
The second reconnects to M17-218/220 and the ancestry/strain/spectral audit.

No claim is made here that those older gates close every tangent geometry; their explicit thin, decompactified, rank, and interface exits remain in force.

---

## 5. Vanishing-measure high metric is a strict subscale event

On the microcarrier branch, choose a threshold `L_j -> infinity` and a carrier `S_j` with

\[
|S_j|\to0,
\qquad
|\nabla\xi_j|^2\gtrsim L_j
\]

on the retained high-metric portion.

Define an effective geometric length

\[
\boxed{
\varepsilon_j:=|S_j|^{1/3}\to0.
}
\]

Thus the first-jet escalation has concentrated below the current fixed tangent scale.

It is therefore recorded as

\[
\boxed{G_{director\text{-}metric\ microcarrier/strict\ subscale}.}
\]

If the carrier approaches the active-set boundary or the director ceases to be defined, use

\[
G_{nodal/rank/interface}
\]

instead.

---

## 6. Combined first-jet gate

Therefore

\[
\boxed{
G_{director\ first\text{-}jet\ L4\ escalation}
\Longrightarrow
G_{fixed\text{-}fraction\ high\ director\ area}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}
\lor
G_{director\text{-}metric\ microcarrier/strict\ subscale}
\lor
G_{nodal/rank/interface}.
}
\]

Combined with M17-269--270, the bulk second-jet lane now returns to already typed lower-order geometry or to a genuinely smaller derivative carrier.

---

## 7. DSD audit

- Divergence of a second moment is not silently upgraded to a fixed-fraction carrier.
- The vanishing-measure alternative is retained explicitly.
- Area and anisotropy are separated by the exact singular-value identity rather than heuristic geometry.
- Older M17 gates are imported only with their stated compactness/thickness/rank hypotheses.
- Strict subscale is not declared impossible merely because the original solution is smooth.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
