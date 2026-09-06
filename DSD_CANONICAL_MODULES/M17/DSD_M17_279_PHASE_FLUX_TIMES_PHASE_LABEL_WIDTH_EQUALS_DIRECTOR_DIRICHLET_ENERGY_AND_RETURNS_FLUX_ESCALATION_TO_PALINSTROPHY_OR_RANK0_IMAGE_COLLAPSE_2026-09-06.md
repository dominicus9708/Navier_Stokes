# DSD M17-279 — Phase flux times phase-label width equals director Dirichlet energy and returns flux escalation to palinstrophy or Rank-0 image collapse

Date: 2026-09-06  
Canonical ID: **M17-279**

Status: **PHASE-FLUX RETURN GATE / M17-278 REDUCES RANK-1 PHASE-LEAF DECOMPACTIFICATION TO RANK-0 DEGENERATION, PHASE-FLUX ESCALATION, OR INTERFACE/NODAL FAILURE. THE WEIGHTED-HARMONIC PHASE CURRENT HAS A STRONGER COAREA IDENTITY: ON A REGULAR PHASE TUBE `phi^-1(I)`, `int a^2|grad phi|^2 dx = int_I Phi_phi(c) dc`. WHEN THERE IS NO SIDE LEAKAGE, `Phi_phi(c)` IS CONSTANT, SO THE DIRECTOR PART OF NORMALIZED PALINSTROPHY IS EXACTLY `Phi_phi |I|`. HENCE PHASE-FLUX ESCALATION OVER A PHASE INTERVAL OF FIXED POSITIVE WIDTH FORCES NORMALIZED PALINSTROPHY. IF PALINSTROPHY REMAINS BOUNDED WHILE `Phi_phi -> infinity`, THE PHASE-LABEL WIDTH MUST COLLAPSE TO ZERO. SINCE THE RANK-1 DIRECTOR IMAGE IS A GREAT-CIRCLE ARC PARAMETRIZED BY `phi`, LABEL-WIDTH COLLAPSE IS DIRECTOR-IMAGE COLLAPSE AND RETURNS TO A RANK-0 TANGENT ON COMPACT RECENTERED PATCHES, OR TO A STRICT INTERFACE/SUBSCALE IF THE COLLAPSE OCCURS ONLY ON A VANISHING CARRIER. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular phase tube

Let

\[
I=(c_-,c_+)
\]

be an interval of regular phase values and define

\[
\Omega_I:=\phi^{-1}(I).
\]

Assume the tube has no side-boundary leakage and remains inside the active Rank-1 corridor.

The phase leaves are

\[
S_c:=\{\phi=c\}.
\]

---

## 2. Coarea identity for director Dirichlet energy

The Rank-1 director satisfies

\[
|\nabla\xi|=|\nabla\phi|.
\]

Hence its weighted Dirichlet contribution is

\[
E_{\phi}(I)
:=\int_{\Omega_I}a^2|\nabla\phi|^2dx.
\]

By the coarea formula,

\[
\begin{aligned}
E_{\phi}(I)
&=\int_I
\left(
\int_{S_c}
\frac{a^2|\nabla\phi|^2}{|\nabla\phi|}
\,dA
\right)dc\\
&=\int_I
\left(
\int_{S_c}a^2|\nabla\phi|\,dA
\right)dc.
\end{aligned}
\]

Therefore

\[
\boxed{
E_{\phi}(I)
=\int_I\Phi_\phi(c)\,dc.
}
\]

---

## 3. Flux conservation on the tube

M17-278 gives

\[
J_\phi=a^2\nabla\phi,
\qquad
\nabla\cdot J_\phi=0.
\]

With no side leakage,

\[
\boxed{\Phi_\phi(c)=\Phi_\phi}
\]

throughout the regular tube.

Thus

\[
\boxed{
E_{\phi}(I)
=\Phi_\phi |I|.
}
\]

This is an exact identity, not an inequality.

---

## 4. Fixed phase-label width

Suppose

\[
|I|\ge\delta_\phi>0.
\]

Then

\[
E_{\phi}(I)
\ge\delta_\phi\Phi_\phi.
\]

Therefore

\[
\boxed{
\Phi_\phi\to\infty
\Longrightarrow
E_{\phi}(I)\to\infty.
}
\]

But

\[
E_{\phi}(I)
\le\int_{\Omega_I}|\nabla V|^2dx
\]

by the exact polar identity of M17-270.

Hence fixed-width phase-flux escalation is a normalized-palinstrophy branch.

---

## 5. Palinstrophy-quiet flux escalation forces label collapse

Assume instead

\[
E_{\phi}(I)\le P_*<\infty
\]

while

\[
\Phi_\phi\to\infty.
\]

The exact identity gives

\[
\boxed{
|I|
=\frac{E_{\phi}(I)}{\Phi_\phi}
\le\frac{P_*}{\Phi_\phi}
\to0.
}
\]

Thus the phase-label interval collapses.

---

## 6. Director-image interpretation

The Rank-1 director is

\[
\xi=(\cos\phi,\sin\phi,0).
\]

Therefore the spherical image of the tube lies on a great-circle arc of length exactly comparable to

\[
|I|
\]

modulo the `2pi` chart convention.

Hence

\[
\boxed{|I|\to0}
\]

means that the director image itself collapses to a point.

On compact recentered patches with the `C1` compactness of M17-272, this yields a Rank-0 director tangent.

If the collapse occurs only on a vanishing spatial carrier or reaches a phase/rank boundary first, retain

\[
G_{strict\ subscale/interface}.
\]

---

## 7. Updated Rank-1 decompactification branch

Combining M17-278 and M17-279,

\[
\boxed{
G_{Rank1\ leaf\ decompactification}
\Longrightarrow
H_{normalized\ palinstrophy}
\lor
G_{Rank0\ degeneration/image\ collapse}
\lor
G_{nodal/interface/side\ leakage}.
}
\]

The former independent `phase-flux escalation` output has been absorbed.

---

## 8. Relation to M17-275

A compact recentered Rank-0 limit may enter M17-275 only if it extends to a global entire nontrivial positive ancient Rank-0 tangent.

Local image collapse alone is not enough to invoke the global positive-ancient representation theorem.

---

## 9. DSD audit

- Coarea is applied only to regular phase values.
- Flux constancy requires absence of side leakage.
- Phase-label collapse is distinguished from spatial-volume collapse.
- Palinstrophy is normalized tangent palinstrophy, not silently an amplitude-independent physical tail cost.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
