# DSD M17-312 — High-amplitude negative-`kappa` phase converts to fixed flux-length occupancy on nondegenerate Rank-1 or Rank-2 geometry

Date: 2026-09-07  
Canonical ID: **M17-312**

Status: **SPATIAL-TO-FLUX INTERMEDIATE BRIDGE / M17-311 PRODUCES A FIXED SIGNED HIGH-AMPLITUDE SPATIAL CHARGE `int chi rho^2 kappa_- >= d_->0` UNLESS CRITICAL NEGATIVE COEFFICIENT MASS CONCENTRATES TOWARD THE NODAL SET. THIS CHARGE IS NOT YET THE MATERIAL FLUX-LABEL DISTRIBUTION OF M5-681. THE PRESENT MODULE INSERTS THE EXACT FLUX-COORDINATE JACOBIANS ALREADY DERIVED FOR THE REGULAR DIRECTOR BRANCHES. ON A NONDEGENERATE RANK-1 VORTEX-LINE FAMILY, `dy=dPhi ds/rho`, SO THE SPATIAL CHARGE GIVES A FIXED LOWER BOUND FOR `int kappa_- ds dPhi`. ON A NONDEGENERATE RANK-2 PURE-KERNEL RIBBON, M17-122 GIVES `dy=dPhi_J ds/|J_xi|`, AND A UNIFORM LOWER DIRECTOR-AREA DENSITY GIVES THE ANALOGOUS FIXED `dPhi_J ds` NEGATIVE-PHASE OCCUPANCY. WITH THE HIGH-AMPLITUDE COMPACT `|kappa|<=K_*` CEILING, BOTH BRANCHES ALSO FORCE A FIXED POSITIVE FLUX-LENGTH MEASURE OF THE SET `{kappa<0}`. THIS IS A REAL MEASURE-CONVERSION STEP, BUT IT IS NOT YET M5-681'S SAME-MATERIAL LABEL CURRENT: ARC-LENGTH OCCUPANCY AND CURRENT FLUX LABEL WEIGHTS STILL NEED A TRANSPORT/REUSE THEOREM. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-311

On the uniform high-amplitude-capture branch there exist fixed constants

\[
a_*>0,
\qquad
K_*<\infty,
\qquad
d_->0
\]

and a smooth cutoff `chi_*` supported away from the nodal set such that

\[
\boxed{
\int
\chi_*(\rho)\rho^2\kappa_-dy
\ge d_->0.
}
\]

On the support of the retained charge,

\[
\boxed{
a_*\lesssim\rho\le M_0<\infty}
\]

and

\[
\boxed{0\le\kappa_-\le K_*}
\]

for one compact-state upper amplitude bound `M_0`.

The purpose of this module is to convert the spatial charge to branch-appropriate flux-coordinate occupancy without yet claiming same-material label residence.

---

## 2. Rank-1 vortex-line flux coordinates

On a regular Rank-1 vortex-line family, the standard vorticity-flux coordinate Jacobian used in M17-190 is

\[
\boxed{
dy=\frac{d\Phi\,ds}{\rho},}
\]

where `dPhi` is the oriented vorticity flux measure and `ds` is arc length along the vortex line.

Therefore the M17-311 charge on the Rank-1 portion becomes

\[
\begin{aligned}
D_-^{(1)}
&:=
\int_{R_1}
\chi_*\rho^2\kappa_-dy\\
&=
\int
\int
\chi_*\rho\kappa_-\,ds\,d\Phi.
\end{aligned}
\]

Assume this branch carries a fixed fraction `eta_1>0` of the total high-amplitude negative charge:

\[
\boxed{D_-^{(1)}\ge\eta_1d_-.}
\]

If it does not, the charge is allocated to the other director branches/interfaces and no Rank-1 conclusion is asserted.

---

## 3. Rank-1 fixed negative phase flux-length moment

Because

\[
\rho\le M_0,
\]

we have

\[
D_-^{(1)}
\le
M_0
\int\int
\chi_*\kappa_-\,ds\,d\Phi.
\]

Hence

\[
\boxed{
\int\int
\chi_*\kappa_-\,ds\,d\Phi
\ge
\frac{\eta_1d_-}{M_0}
=:c_{\Phi,1}>0.
}
\]

Since

\[
\kappa_-\le K_*,
\]

this further implies a positive flux-length measure of the negative phase:

\[
\boxed{
\int\int
\chi_*\mathbf1_{\{\kappa<0\}}
\,ds\,d\Phi
\ge
\frac{c_{\Phi,1}}{K_*}
=:m_{\Phi,1}>0.
}
\]

Thus the high-amplitude Rank-1 branch cannot realize the M17-311 negative coefficient charge on a vanishing flux-length set.

---

## 4. Rank-2 pure-kernel ribbon coordinates

On the regular pure-transverse-kernel Rank-2 branch, M17-122 gives the exact volume element

\[
\boxed{
dy
=\frac{d\Phi_J\,ds}{|J_\xi|}.}
\]

Here `dPhi_J` is the frozen director-area flux and `ds` is arc length along the kernel fiber.

Therefore the Rank-2 contribution is

\[
\begin{aligned}
D_-^{(2)}
&:=
\int_{R_2}
\chi_*\rho^2\kappa_-dy\\
&=
\int\int
\chi_*
\frac{\rho^2\kappa_-}{|J_\xi|}
\,ds\,d\Phi_J.
\end{aligned}
\]

Assume this branch carries a fixed fraction `eta_2>0`:

\[
\boxed{D_-^{(2)}\ge\eta_2d_-.}
\]

---

## 5. Nondegenerate Rank-2 conversion

On the nondegenerate ribbon branch retain

\[
\boxed{|J_\xi|\ge j_*>0.}
\]

The compact hull also gives

\[
\rho\le M_0.
\]

Hence

\[
\frac{\rho^2}{|J_\xi|}
\le
\frac{M_0^2}{j_*}.
\]

Therefore

\[
D_-^{(2)}
\le
\frac{M_0^2}{j_*}
\int\int
\chi_*\kappa_-\,ds\,d\Phi_J.
\]

Thus

\[
\boxed{
\int\int
\chi_*\kappa_-\,ds\,d\Phi_J
\ge
\frac{j_*\eta_2d_-}{M_0^2}
=:c_{\Phi,2}>0.
}
\]

Using again `kappa_-<=K_*`,

\[
\boxed{
\int\int
\chi_*\mathbf1_{\{\kappa<0\}}
\,ds\,d\Phi_J
\ge
\frac{c_{\Phi,2}}{K_*}
=:m_{\Phi,2}>0.
}
\]

Thus a nondegenerate Rank-2 ribbon family carrying a fixed fraction of the M17-311 charge has a fixed positive director-flux-length negative phase occupancy.

---

## 6. Exact Rank-2 failures

If the Rank-2 conversion cannot use a uniform

\[
|J_\xi|\ge j_*>0,
\]

then M17-122 already classifies the loss through

\[
\boxed{
G_{J\text{-}degeneration}
\lor
G_{q\text{-}flattening/decompactification}
\lor
G_{ribbon\ cover/interface}.
}
\]

Those branches remain explicit and are not absorbed into a generic failure of the present theorem.

Similarly, if the negative charge is not carried by either a uniformly nondegenerate Rank-1 or Rank-2 family, its allocation must lie in the complementary rank/interface classes.

---

## 7. Combined flux-length occupancy gate

On any regular nondegenerate director branch carrying a fixed fraction of the M17-311 high-amplitude negative charge,

\[
\boxed{
H_{high\text{-}amp\ negative\ spatial\ phase}
\Longrightarrow
H_{negative\ flux\text{-}length\ occupancy}
\lor
G_{rank/geometry/interface}.
}
\]

The surviving occupancy is quantitatively fixed:

\[
\boxed{
\int\kappa_-\,d\mathfrak m_{flux\times length}
\ge c_\Phi>0,
}
\]

and, under the compact coefficient ceiling,

\[
\boxed{
\mathfrak m_{flux\times length}(\kappa<0)
\ge m_\Phi>0.
}
\]

---

## 8. Why this is not yet the M5-681 material-flux distribution

M5-681 works on a **material label space** with current flux weight

\[
d\mu_\theta(\lambda)
\]

and one material multiplier trajectory

\[
\kappa_\lambda(\theta).
\]

The present measure contains an additional instantaneous arc-length coordinate `s`:

\[
d\Phi\,ds
\quad\text{or}\quad
d\Phi_J\,ds.
\]

A spatial line may contain both positive and negative `kappa` portions, and the active negative segment may move along the same material tube without changing its flux label.

Therefore

\[
\boxed{
\text{negative flux-length occupancy}
\not\Rightarrow
\text{fixed material label has negative }\kappa.
}
\]

This is the same type of identity firewall emphasized by M17-238 for marker versus packet genealogy.

---

## 9. The next missing transport theorem

To enter the exact M5-681 conveyor, one needs a theorem of the form

\[
\boxed{
\text{persistent negative flux-length occupancy}
\Longrightarrow
\text{same-material label residence}
\lor
\text{along-line phase migration/turnover}
\lor
\text{interface/rank replacement}.
}
\]

The second branch is itself useful: if the negative segment repeatedly migrates along a fixed tube, the migration speed and the coefficient material law

\[
h=D_B\kappa
\]

must support repeated zero-level crossings and can be compared with the M5-681 directed `kappa`-space current.

Thus the present result reduces the spatial/material gap to one concrete **arc-length-to-label transport problem**.

---

## 10. DSD audit

- M17-311's spatial measure is not identified with M5-681's material label measure.
- Exact branch-specific Jacobians are inserted before any flux statement.
- Fixed charge allocation to a director branch is explicit.
- Rank-2 director-area degeneration and ribbon decompactification remain named exits.
- The compact `kappa` ceiling is used only to convert a negative moment to negative-phase measure.
- No same-label time residence is claimed.
- No record-generation physical budget is inferred from the normalized flux-length occupancy.
- Global regularity remains unproved.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
