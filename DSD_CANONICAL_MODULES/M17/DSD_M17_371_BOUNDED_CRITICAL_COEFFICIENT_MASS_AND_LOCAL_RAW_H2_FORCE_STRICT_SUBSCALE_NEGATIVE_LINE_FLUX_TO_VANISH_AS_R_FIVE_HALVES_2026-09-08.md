# DSD M17-371 — Bounded critical coefficient mass and local raw-`H2` force strict-subscale negative-line flux to vanish as `r^{5/2}`

Date: 2026-09-08  
Canonical ID: **M17-371**

Status: **ACTIVE STRICT-SUBSCALE FLUX-EVACUATION THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

Use the partition-free M17-370 inequality on a scale-`r` negative CE-H flux family:

\[
\boxed{
\Phi_r
\lesssim
r^{5/2}(M_rH_r)^{1/2},
}
\]

where

\[
M_r=\int_{F_r}\kappa_-^{3/2}dy
\]

and

\[
H_r=\int_{F_r}|\Delta W|^2dy.
\]

The retained line portion satisfies

\[
\kappa_-\gtrsim r^{-2},
\qquad
\ell_\lambda\gtrsim r.
\]

## 2. Compact coefficient-mass and local-H2 branch

Assume along a strict-subscale sequence

\[
r_j\to0
\]

that

\[
\boxed{
M_{r_j}\le M_*<\infty,
}
\]

and

\[
\boxed{
H_{r_j}\le H_*<\infty.
}
\]

Then immediately

\[
\boxed{
\Phi_{r_j}
\le C(M_*H_*)^{1/2}r_j^{5/2}
\to0.
}
\]

Thus strict coefficient descent cannot preserve a fixed positive amount of negative-line material flux on the compact `M_{3/2}` + local raw-`H2` branch.

## 3. Fixed-flux strict descent is closed under these bounds

If instead one assumes

\[
\Phi_{r_j}\ge\Phi_*>0,
\]

then M17-370 forces

\[
M_{r_j}H_{r_j}
\gtrsim
\Phi_*^2r_j^{-5}.
\]

Therefore

\[
\boxed{
\Phi_{r_j}\ge\Phi_*>0
\Longrightarrow
G_{M_{3/2}\ decompactification}
\lor
G_{raw\text{-}H2\ decompactification}
\lor
G_{retained\ geometry}.
}
\]

The fixed-flux strict-subscale branch is not available inside a compact coefficient/H2 state family.

## 4. Relation to M17-366--368

M17-366 allowed strict-subscale concentration of the critical measure

\[
d\mu_j=\kappa_{j,-}^{3/2}dy.
\]

M17-367 showed that coefficient mass alone cannot force raw `H2` because of amplitude homogeneity.

M17-368 showed that adding a fixed positive flux breaks that symmetry for an individual tube packet.

The present module removes the packet decomposition entirely and gives the sharper family-level conclusion:

\[
\boxed{
G_{strict\ subscale}
+H_{M_{3/2},H2\ compact}
\Longrightarrow
G_{material\ flux\ evacuation}.
}
\]

Thus the surviving compact nodal branch is genuinely **flux-poor**, not merely highly fragmented.

## 5. Companion weaker estimate from enstrophy

M17-370 also gives

\[
\Phi_r
\lesssim
r^{1/2}(M_rE_r)^{1/2}.
\]

Hence even without local `H2` compactness, bounded critical coefficient mass and enstrophy imply

\[
\Phi_r=O(r^{1/2}).
\]

The `H2` information strengthens the exponent from `1/2` to `5/2`.

This separation is useful when the branch itself is testing raw-`H2` decompactification.

## 6. Updated nodal split

The moving critical nodal branch now satisfies

\[
\boxed{
\begin{aligned}
G_{moving\ critical\ nodal}
\Longrightarrow{}&
G_{M_{3/2}\ decompactification}\\
&\lor G_{raw\text{-}H2\ decompactification}\\
&\lor G_{geometry/interface/domain}\\
&\lor H_{flux\text{-}evacuated\ coefficient\ bubble}.
\end{aligned}
}
\]

The last branch has

\[
\boxed{
\Phi_r=O(r^{5/2})
}
\]

under the compact `M_{3/2}` and local-H2 hypotheses.

## 7. Why flux evacuation is not itself a contradiction

Material flux is not a conserved scalar in the similarity coefficient conveyor used earlier. Along one retained material label,

\[
\frac d{d\theta}\log\Phi=\kappa.
\]

Therefore a large negative coefficient exposure can genuinely suppress the material flux of a lineage.

The next question is quantitative: reducing a previously order-one material flux to `O(r^{5/2})` requires a logarithmically large negative integrated `kappa` exposure. M17-372 records that exact cost.

## 8. Audit verdict

**PASS.**

The main conclusion is the fragmentation-independent evacuation law

\[
\boxed{
\Phi_r=O(r^{5/2})
}
\]

on the compact strict-subscale nodal branch.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]