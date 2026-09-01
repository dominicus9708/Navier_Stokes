# DSD M5-502 — Unbounded similarity palinstrophy is a remote derivative-mass escape, not a local pointwise derivative blowup

Date: 2026-09-01

Status: **DERIVATIVE CONCENTRATION-COMPACTNESS / THE M5-501 ALTERNATIVE `sup P = infinity` OCCURS INSIDE A HULL THAT IS SMOOTHLY PRECOMPACT ON EVERY FIXED SIMILARITY BALL / THEREFORE NO FIXED BALL CAN CARRY THE UNBOUNDED PART OF `P=||grad W||_2^2`; ALONG ANY PALINSTROPHY-DIVERGENT SEQUENCE, AN UNBOUNDED AMOUNT OF DERIVATIVE `L2` MASS MUST OCCUPY THE EXTERIOR OF EVERY FIXED BALL / THIS IS A REMOTE SHELL/OCCUPANCY ESCAPE `H_tail^(remote-P)`, CONSISTENT WITH THE M5-392 FIREWALL AGAINST PARENT-SCALE POINTWISE DERIVATIVE BLOWUP / THE REMOTE-P BRANCH IS NATURALLY ADJACENT TO THE TERMINAL DIRICHLET-TAIL/DILATION-GENEALOGY PROGRAM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-501

The projected-diffusion ratchet component satisfies either

\[
P(\theta)\le P_*<\infty
\]

with quantitative threshold conditions, or

\[
\boxed{
\sup_\theta P(\theta)=\infty,
}
\]

where

\[
P(\theta)
=
\int_{\mathbb R^3}|\nabla W(y,\theta)|^2dy.
\]

M5-502 audits the geometry of the second alternative.

---

## 2. Local smooth compactness of the similarity hull

The M5-478--485 compact branch is smoothly precompact on every fixed space-time compact set away from the terminal singular boundary.

After passing to the similarity suspension representation, for every fixed radius `R` there exists

\[
C_R<\infty
\]

such that

\[
\boxed{
\sup_{\mathbf Y\in\widehat{\mathfrak H}}
\int_{B_R}|\nabla W_{\mathbf Y}|^2dy
\le C_R.
}
\]

Indeed local smooth compactness gives stronger fixed-order derivative bounds on every fixed ball.

Thus local palinstrophy cannot diverge at one fixed normalized location.

---

## 3. Choose a palinstrophy-divergent sequence

Suppose

\[
\sup_\theta P(\theta)=\infty.
\]

Choose hull states/times `theta_n` such that

\[
P(\theta_n)\to\infty.
\]

For any fixed `R`, split

\[
P(\theta_n)
=
P_{loc}(R,\theta_n)
+
P_{ext}(R,\theta_n),
\]

where

\[
P_{loc}(R,\theta_n)
:=
\int_{|y|\le R}|\nabla W|^2dy
\]

and

\[
P_{ext}(R,\theta_n)
:=
\int_{|y|>R}|\nabla W|^2dy.
\]

The local compactness bound gives

\[
P_{loc}(R,\theta_n)
\le C_R.
\]

Therefore

\[
\boxed{
P_{ext}(R,\theta_n)
\ge
P(\theta_n)-C_R
\to\infty.
}
\]

for every fixed `R`.

---

## 4. Remote derivative-mass escape

Thus the unbounded palinstrophy necessarily escapes every fixed similarity ball.

Define

\[
\boxed{
H_{tail}^{remote-P}
:
\quad
\exists\theta_n
\text{ with }
P(\theta_n)\to\infty
\]

and, equivalently, for every fixed `R`,

\[
\boxed{
\int_{|y|>R}|\nabla W(y,\theta_n)|^2dy
\to\infty.
}
\]

Hence

\[
\boxed{
\sup P=\infty
\Longrightarrow
H_{tail}^{remote-P}.
}
\]

This is stronger than mere failure of palinstrophy tightness: the exterior derivative mass itself diverges along the selected sequence.

---

## 5. Compatibility with M5-392

M5-392 proved that on the original first-hitting parent normalization, every fixed-order **pointwise** normalized vorticity derivative remains uniformly bounded during a smooth stage.

M5-502 does not contradict that result.

The new branch is an integral occupancy phenomenon:

\[
\boxed{
\text{bounded local derivative amplitude}
+
\text{increasing remote spatial occupancy}
\Longrightarrow
\text{unbounded global derivative }L^2\text{ mass}.
}
\]

Thus the label `H_P^global` should be interpreted as remote mass/frequency occupancy, not a reappearance of the eliminated thin-center pointwise derivative singularity.

---

## 6. Dyadic-shell representation

Write the exterior as dyadic shells

\[
A_k(R)
:=
\{2^kR<|y|<2^{k+1}R\}.
\]

Then

\[
P_{ext}(R,\theta_n)
=
\sum_{k\ge0}
\int_{A_k(R)}|\nabla W|^2dy.
\]

Since the sum diverges along the selected states for each fixed `R`, the remote-P branch must realize at least one of the following along suitable subsequences:

1. increasingly many shells carry nonnegligible derivative energy;
2. some remote shells carry increasingly large derivative energy;
3. derivative energy shifts to larger and larger shell indices while maintaining an unbounded total exterior mass.

All are spatial occupancy/frequency-tail mechanisms.

---

## 7. Relation to M5-496 remote enstrophy tail

M5-496 defined

\[
H_{tail}^{remote-E}
\]

through non-tight vorticity `L2` mass.

M5-502 defines the stronger derivative-tail quantity

\[
H_{tail}^{remote-P}.
\]

Neither implication

\[
H_{tail}^{remote-P}
\Rightarrow
H_{tail}^{remote-E}
\]

nor its converse is automatic.

High-frequency remote packets can carry large derivative mass with small enstrophy, while broad remote packets can carry enstrophy with modest derivative mass.

The two tails therefore form distinct concentration-compactness channels.

---

## 8. Relation to the terminal Dirichlet tail

M5-481--483 force a critical terminal Dirichlet tail and a complete dilation genealogy on the compact bounded route.

The quantity

\[
\int_{A}|\nabla U|^2
\]

on terminal blow-down annuli is the same derivative order as the remote-P observable.

Therefore `H_tail^(remote-P)` is structurally adjacent to the terminal H1/Dirichlet-tail hard core.

However M5-502 does not yet prove that recurrent interior remote-P mass converges to or generates the terminal tail state.

That requires a space-time transport/compactness argument across similarity time.

---

## 9. Updated projected-diffusion branch

M5-501--502 give

\[
\boxed{
\mathcal C_{ax+projdiff}
\Longrightarrow
H_{tail}^{remote-P}
\lor
\mathcal C_{bounded-P}^{proj},
}
\]

where the bounded-P survivor obeys quantitative thresholds

\[
Z_*P_*
\ge K_{EP}
\]

and

\[
P_*
\ge P_{min}^{proj}(Z_*,h_{proj}).
\]

Thus the projected-diffusion hard core is now either an explicit remote derivative-tail escape or a quantitatively large bounded derivative component.

---

## 10. Highest-value next target

The next tail audit should compare the two remote channels

\[
H_{tail}^{remote-E}
\quad\text{and}\quad
H_{tail}^{remote-P}
\]

with the M5-479--483 terminal dilation genealogy.

A useful target is a shell compactness dichotomy:

\[
\boxed{
\text{recurrent remote }E/P\text{ tail}
\Longrightarrow
\text{terminal critical tail strengthening}
\lor
\text{scale-frequency defect}.
}
\]

If this can be established, both the local-payer and projected-diffusion escape routes reconnect to the same terminal dilation hard core rather than remaining separate untyped branches.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
