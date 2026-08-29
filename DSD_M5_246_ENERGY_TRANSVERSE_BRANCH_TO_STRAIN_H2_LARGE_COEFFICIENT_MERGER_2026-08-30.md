# DSD M5-246 — Energy-Transverse Residual to Strain / H2 / Large-Coefficient Merger

Date: 2026-08-30

Parent: `DSD_M5_245_ENERGY_TRANSVERSE_BRANCH_STRICT_OUTWARD_BERNOULLI_FLUX_IDENTITY_2026-08-30.md`

Status: **BRANCH MERGER / THE KINETIC-RADIAL HALF OF THE STRICT BERNOULLI PAYMENT FORCES A FIXED RECURRENT RADIAL-VELOCITY L2 FLOOR UNDER THE COMPACT TYPE-I AMPLITUDE CEILING, AND THE M5-235 RECURRENT RADIAL-STRAIN IDENTITY CONVERTS THIS INTO A FIXED STRAIN-ENERGY FLOOR / THE PRESSURE-RADIAL HALF ROUTES BY SPHERICAL HODGE TO H2-TYPE DERIVATIVE OR LARGE CRITICAL COEFFICIENT / THEREFORE A LOCALLY FIRST-RG-ENERGY-TRANSVERSE RESIDUAL IS NOT AN INDEPENDENT ENDPOINT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Strict Bernoulli payment

M5-245 gives on the strong `E_trans` branch

\[
\mathcal C_K+\mathcal C_P
=\nu\mathcal G,
\]

where

\[
\mathcal G
:=
\left\langle
\int_{S^2}
\bigl(|\Phi_y|^2+|\nabla_S\Phi|^2\bigr)d\theta
\right\rangle
>0,
\]

\[
\mathcal C_K
=\frac12
\left\langle
\int|\Phi|^2\Phi_r
\right\rangle,
\]

and

\[
\mathcal C_P
=\left\langle
\int\Pi\Phi_r
\right\rangle.
\]

Hence

\[
\boxed{
\mathcal C_K\ge\frac{\nu\mathcal G}{2}
\quad\lor\quad
\mathcal C_P\ge\frac{\nu\mathcal G}{2}.
}
\]

---

## 2. Uniform tail amplitude ceiling

The compact Type-I tail hull has one finite bound

\[
\boxed{
M_\Phi
:=
\sup_{T\in\mathcal T}
\|\Phi_T\|_{L^\infty(cyl)}
<\infty.
}
\]

Consequently

\[
\int_{S^2}|\Phi|^2d\theta
\le
4\pi M_\Phi^2.
\]

The aperiodic phase-action residue from M5-219/224 also gives a fixed positive lower bound

\[
\boxed{
\mathcal G\ge g_*>0
}
\]

on the selected invariant component/measure after the usual compact positive-action extraction.

---

## 3. Kinetic-radial branch forces radial L2 mass

Assume

\[
\mathcal C_K
\ge\frac{\nu\mathcal G}{2}.
\]

Then

\[
\boxed{
\left\langle
\int|\Phi|^2\Phi_r
\right\rangle
\ge
\nu\mathcal G.
}
\]

Discard the negative radial sector:

\[
\left\langle
\int|\Phi|^2(\Phi_r)_+
\right\rangle
\ge
\nu\mathcal G.
\]

By Cauchy-Schwarz,

\[
\begin{aligned}
\left\langle
\int|\Phi|^2(\Phi_r)_+
\right\rangle
&\le
\left(
\left\langle
\int|\Phi|^4
\right\rangle
\right)^{1/2}
\left(
\left\langle
\int|(\Phi_r)_+|^2
\right\rangle
\right)^{1/2}.
\end{aligned}
\]

Use

\[
|\Phi|^4\le M_\Phi^2|\Phi|^2
\]

and the sphere-volume bound:

\[
\left\langle\int|\Phi|^4\right\rangle
\le
4\pi M_\Phi^4.
\]

Therefore

\[
\boxed{
\left\langle
\int|(\Phi_r)_+|^2
\right\rangle
\ge
\frac{\nu^2\mathcal G^2}
{4\pi M_\Phi^4}.
}
\]

Since `G>=g_*`,

\[
\boxed{
\left\langle
\int|\Phi_r|^2
\right\rangle
\ge
\frac{\nu^2g_*^2}
{4\pi M_\Phi^4}
>0.
}
\]

Thus the kinetic-radial payer carries a fixed recurrent radial-velocity energy.

---

## 4. Convert radial energy to strain energy

M5-235 proves the exact recurrent identity

\[
\left\langle
\int|\Sigma_{rr}|^2
\right\rangle
=
\left\langle
\int
\left(
|\partial_y\Phi_r|^2+|\Phi_r|^2
\right)
\right\rangle.
\]

Hence

\[
\left\langle
\int|\Sigma_{rr}|^2
\right\rangle
\ge
\left\langle
\int|\Phi_r|^2
\right\rangle.
\]

Combining with Section 3:

\[
\boxed{
\left\langle
\int|\mathcal S_\Phi|^2
\right\rangle
\ge
\frac{\nu^2g_*^2}
{4\pi M_\Phi^4}
>0.
}
\]

Therefore

\[
\boxed{
K_{rad}^+
\Longrightarrow
S_{amp},
}
\]

a fixed recurrent critical-strain amplitude certificate.

---

## 5. Pressure-radial branch

Assume instead

\[
\mathcal C_P
\ge\frac{\nu\mathcal G}{2}.
\]

Thus

\[
\boxed{
\left\langle
\int\Pi\Phi_r
\right\rangle
\ge
\frac{\nu\mathcal G}{2}.
}
\]

For each `y`, zero spherical mass flux gives

\[
\int_{S^2}\Phi_r=0.
\]

Solve

\[
-\Delta_{S^2}\chi=\Phi_r,
\qquad\int_{S^2}\chi=0.
\]

Then

\[
\int\Pi\Phi_r
=
\int\nabla_S\Pi\cdot\nabla_S\chi.
\]

The first spherical eigenvalue yields

\[
\|\nabla_S\chi\|_2
\le\frac1{\sqrt2}\|\Phi_r\|_2.
\]

Hence a fixed positive pressure-radial payment forces a corresponding tangential pressure-gradient floor unless the radial velocity amplitude is itself already large.

The latter case returns to Section 4.

In the former case, the autonomous cylinder momentum equation expresses

\[
\nabla_S\Pi
\]

as viscosity times second derivatives of `Phi` plus first-order/quadratic critical coefficient terms.

Thus exactly as in M5-234:

\[
\boxed{
P_{rad}^+
\Longrightarrow
H2_{tail}
\lor
L_{tail,1},
}
\]

where `H2_tail` denotes a fixed second-derivative tail mode and `L_tail,1` a sufficiently large critical coefficient regime.

---

## 6. Unified transverse endpoint

The strong first-order energy-transverse branch therefore satisfies

\[
\boxed{
E_{trans}
\Longrightarrow
S_{amp}
\lor
H2_{tail}
\lor
L_{tail,1}.
}
\]

It does not survive as an abstract energy-orthogonal or symmetry-like mode.

---

## 7. Relation to prior stationary certificates

The same three structural types already arose in M5-232--236 while auditing the stationary large-amplitude branch:

- large recurrent strain;
- higher derivative mode;
- large remaining critical coefficient.

M5-246 shows that the supposedly nonstationary, locally energy-transverse residual branch is forced back into the same structural frontier.

This is a genuine branch merger:

\[
\boxed{
\text{stationary large branch}
\quad\text{and}\quad
\text{residual energy-transverse branch}
}
\]

share the same final large-structure certificates.

---

## 8. Scope firewall

A fixed recurrent strain-energy floor is not itself a contradiction.  Critical scale invariance permits `O(1)` normalized strain on all generations.

Likewise a tail H2 mode is not yet automatically the finite-prelimit `H` budget; an inheritance bridge is still required.

Therefore M5-246 is a **structural merger**, not closure of the large branch.

---

## 9. Updated residual-active split

After M5-243--246:

\[
\boxed{
R_{gap}
\Longrightarrow
E_{local}
\lor
S_{amp}
\lor
H2_{tail}
\lor
L_{tail,1}.
}
\]

Only `E_local`, the genuinely first-order energy-visible residual branch, remains outside the common large-structure frontier.

### NEXT TARGET

Audit `E_local`.  Since its `R^{-1}` shell-energy charge is geometrically summable, ordinary energy cannot close it.  The next useful question is whether the **sign-changing recurrent charge** necessarily has nonzero total variation per log scale, and whether that variation can be related to `Phi_y`, pressure, or strain so that `E_local` also merges into the same large-structure frontier.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]