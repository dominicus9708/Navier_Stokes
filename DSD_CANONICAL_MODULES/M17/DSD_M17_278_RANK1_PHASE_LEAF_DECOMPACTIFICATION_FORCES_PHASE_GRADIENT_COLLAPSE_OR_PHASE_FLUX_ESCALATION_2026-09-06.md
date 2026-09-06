# DSD M17-278 — Rank-1 phase-leaf decompactification forces phase-gradient collapse or phase-flux escalation

Date: 2026-09-06  
Canonical ID: **M17-278**

Status: **RANK-1 LEAF DECOMPACTIFICATION GATE / THE GREAT-CIRCLE PHASE SYSTEM OF M17-274 HAS AN EXACT DIVERGENCE-FREE PHASE CURRENT `J_phi=a^2 grad phi`. ITS FLUX THROUGH A REGULAR LEVEL LEAF `S_c={phi=c}` IS `Phi_phi(c)=int_{S_c} a^2 |grad phi| dA` AND IS CONSTANT ACROSS A REGULAR LEAF TUBE WITH NO SIDE-BOUNDARY LOSS. ON AN ACTIVE AMPLITUDE CORRIDOR `a>=a_*>0`, IF LEAF AREA `A_c` TENDS TO INFINITY WHILE THE PHASE FLUX REMAINS UNIFORMLY BOUNDED, THE LEAF-AVERAGE OF `|grad phi|` TENDS TO ZERO. MORE STRONGLY, FOR EVERY FIXED `delta>0`, THE AREA FRACTION ON WHICH `|grad phi|>=delta` TENDS TO ZERO. SINCE `|grad xi|=|grad phi|` IN RANK 1, A DECOMPACTIFYING BOUNDED-FLUX LEAF BECOMES RANK-0 ON ALMOST ALL OF ITS AREA. OTHERWISE THE PHASE FLUX ITSELF ESCALATES OR THE AMPLITUDE/INTERFACE CORRIDOR FAILS. THUS PURE LEAF-AREA DECOMPACTIFICATION IS NOT AN INDEPENDENT RANK-1 ENDPOINT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Weighted phase current

M17-274 gives

\[
\boxed{
\nabla\cdot(a^2\nabla\phi)=0.
}
\]

Define

\[
\boxed{J_\phi:=a^2\nabla\phi.}
\]

Then

\[
\boxed{\nabla\cdot J_\phi=0.}
\]

---

## 2. Flux through a regular phase leaf

On a regular level leaf

\[
S_c:=\{x:\phi(x)=c\}
\]

with unit normal

\[
n=\frac{\nabla\phi}{|\nabla\phi|},
\]

the directed phase flux is

\[
\boxed{
\Phi_\phi(c)
:=\int_{S_c}J_\phi\cdot n\,dA
=\int_{S_c}a^2|\nabla\phi|\,dA.
}
\]

Because `div J_phi=0`, the flux is constant across a regular tube of phase leaves as long as no side boundary, rank interface, or nodal leakage is crossed.

---

## 3. Decompactifying leaf area

Let

\[
A_c:=|S_c|.
\]

Consider a sequence of regular leaves with

\[
\boxed{A_{c_j}\to\infty.}
\]

Assume an active amplitude floor

\[
\boxed{a\ge a_*>0}
\]

on the retained leaf family and a bounded phase-flux corridor

\[
\boxed{\Phi_\phi(c_j)\le\Phi_*<\infty.}
\]

Then

\[
\Phi_\phi(c_j)
\ge a_*^2\int_{S_{c_j}}|\nabla\phi|\,dA.
\]

Hence

\[
\boxed{
\fint_{S_{c_j}}|\nabla\phi|\,dA
\le
\frac{\Phi_*}{a_*^2A_{c_j}}
\to0.
}
\]

---

## 4. Fixed-threshold collapse on most of the leaf

Fix any

\[
\delta>0.
\]

Let

\[
E_{j,\delta}
:=\{x\in S_{c_j}:|\nabla\phi|\ge\delta\}.
\]

Then

\[
\delta |E_{j,\delta}|
\le
\int_{S_{c_j}}|\nabla\phi|\,dA
\le
\frac{\Phi_*}{a_*^2}.
\]

Therefore

\[
\boxed{
\frac{|E_{j,\delta}|}{A_{c_j}}
\le
\frac{\Phi_*}{a_*^2\delta A_{c_j}}
\to0.
}
\]

Thus for every fixed positive director-gradient threshold, the fraction of the decompactifying leaf above that threshold vanishes.

---

## 5. Rank interpretation

For the Rank-1 great-circle phase,

\[
\boxed{|\nabla\xi|=|\nabla\phi|.}
\]

Hence the bounded-flux decompactifying leaf becomes Rank 0 on asymptotically full leaf area in the measure sense.

After local recentering at typical leaf points and using the C1-alpha compactness of M17-272, this returns to the Rank-0 tangent gate of M17-273/275, unless the degeneration is confined to a vanishing subcarrier or an interface is encountered.

---

## 6. Correct decompactification split

Therefore

\[
\boxed{
G_{Rank1\ phase\text{-}leaf\ area\ decompactification}
\Longrightarrow
G_{Rank0\ degeneration\ on\ dominant\ leaf\ area}
\lor
G_{phase\text{-}flux\ escalation}
\lor
G_{nodal/amplitude\ degeneration}
\lor
G_{leaf\ interface/side\ leakage}.
}
\]

Pure area growth with bounded phase flux and nondegenerate amplitude cannot remain a genuinely Rank-1 dominant carrier.

---

## 7. Relation to global Rank-0 closure

M17-275 closes a **global entire** nontrivial Rank-0 positive ancient heat tangent on the critical sign-balanced `K` branch.

M17-278 does not silently upgrade typical local leaf points to that global setting.
It only shows that bounded-flux Rank-1 decompactification geometrically returns toward Rank 0.

A further extension/interface argument is still required before importing the global Rank-0 contradiction.

---

## 8. DSD audit

- Phase flux conservation is used only on regular tubes without side leakage.
- Leaf-area decompactification and phase-flux escalation remain separate.
- Rank-0 degeneration is a measure statement unless C1 compactness is used after recentering.
- The global Rank-0 theorem is not applied to a merely local degeneration.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
