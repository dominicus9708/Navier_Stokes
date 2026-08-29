# DSD M5-220 — Tail Homogeneity Defect to Residual or Stationary Critical Profile Fork

Date: 2026-08-30

Parent: `DSD_M5_219_TAIL_CONJUGACY_NO_SHORT_RETURN_TO_LOG_RADIAL_PHASE_ACTION_2026-08-30.md`

Status: **COMPACTNESS FORK / POSITIVE LOG-RADIAL HOMOGENEITY-DEFECT ACTION CANNOT BE DECLARED A NAVIER--STOKES RESIDUAL BY KINEMATICS ALONE / EITHER THE CANONICAL TAIL RESIDUAL IS QUANTITATIVELY ACTIVE ON A POSITIVE-DENSITY FAMILY OF LOG CELLS, OR A SUBSEQUENCE FORMS AN ACTUAL NONHOMOGENEOUS STATIONARY CRITICAL NAVIER--STOKES PROFILE ON THE PUNCTURED SPACE / SVERAK'S HOMOGENEOUS LANDAU CLASSIFICATION DOES NOT REMOVE THE LATTER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-219

For the surviving aperiodic/minimal W1 branch, M5-219 produces one fixed finite log-cylinder size and a positive-density family of translated cells on which

\[
\boxed{
\int_{C_*}
|\partial_y\Phi|^3
\,dy\,d\theta
\ge c_{ph}>0.
}
\]

Equivalently, for the canonical tail

\[
T(r\theta)=r^{-1}\Phi(\log r,\theta),
\]

the spatial homogeneity defect

\[
\boxed{
\mathcal H_T
:=T+(Y\cdot\nabla)T
}
\]

satisfies a fixed critical `L3` lower bound on the corresponding annulus:

\[
\boxed{
\|\mathcal H_T\|_{L^3(A_*)}
\ge h_*>0
}
\]

on a positive-density set in the tail translation hull.

---

## 2. Tail Navier--Stokes residual

The canonical tail satisfies only the passive dilation law

\[
T_s+\frac12T+\frac12Y\cdot\nabla T=0.
\]

It is not known a priori to solve the stationary Navier--Stokes equation.

Define its divergence-free stationary residual by

\[
\boxed{
F_T
:=
\nu\Delta T
-
\mathbb P\nabla\cdot(T\otimes T).
}
\]

Thus

\[
F_T=0
\]

is exactly the projected stationary Navier--Stokes equation on the punctured space.

On a scale-`R` annulus the residual has the critical scaling

\[
\boxed{
\|R^3F_T(R\cdot)\|_{H^{-1}(A)}\lesssim1,
}
\]

as already established in the canonical-tail construction.

---

## 3. Why homogeneity defect does not algebraically force residual

Write

\[
y=\log r,
\qquad
T=r^{-1}\Phi(y,\theta).
\]

For each scalar component,

\[
\boxed{
\Delta T
=
\frac1{r^3}
\left(
\partial_y^2\Phi
-
\partial_y\Phi
+
\Delta_{S^2}\Phi
\right),
}
\]

with the vector spherical-connection terms included in the full vector operator.

The nonlinear term also has exact degree `-3`:

\[
(T\cdot\nabla)T
=
\frac1{r^3}
\mathcal B(\Phi,\partial_y\Phi,\nabla_{S^2}\Phi).
\]

Hence

\[
F_T
=
\frac1{r^3}
\mathcal F_{cyl}
(\Phi,\partial_y\Phi,\partial_y^2\Phi,
\nabla_{S^2}\Phi,\nabla_{S^2}^2\Phi).
\]

A nonzero `partial_y Phi` may therefore be cancelled by viscosity, angular derivatives, nonlinear transport, and pressure.

Thus the implication

\[
\mathcal H_T\ne0
\Longrightarrow
F_T\ne0
\]

is **not** an algebraic identity and is forbidden without a coercivity theorem.

---

## 4. Local residual norm

Fix the same finite annular/log-cell geometry as M5-219 and define

\[
\boxed{
\mathfrak f(T)
:=
\|F_T\|_{H^{-1}(A_*^{+})},
}
\]

where `A_*^{+}` is a slightly enlarged annulus used to avoid cutoff-edge effects.

The tail compactness package gives local `L3` plus the derivative regularity needed for the residual to depend continuously on the tail in the local distributional/`H^-1` topology.

Thus on the compact tail hull `mathcal T`,

\[
\boxed{
T_n\to T
\Longrightarrow
F_{T_n}\to F_T
\quad\text{locally in }H^{-1}
}
\]

after using the already available local derivative compactness on the audited W1 corridor.

---

## 5. Residual-active versus residual-quiet fork

Let `E_ph` be the positive-density set on which

\[
\|\mathcal H_T\|_{L^3(A_*)}\ge h_*.
\]

Fix any threshold `epsilon_F>0`.

There are two possibilities.

### Branch R — residual active

On a positive-density subset,

\[
\boxed{
\mathfrak f(T(s))
\ge\varepsilon_F.
}
\]

Then the aperiodic tail carries a genuine repeated stationary-NS residual forcing.

This residual is not a descriptor artifact: it is exactly the forcing that appears in the finite-energy quotient equation after the divergence-free tail cutoff.

### Branch S — residual quiet along a homogeneity-active sequence

Otherwise, for arbitrarily small `epsilon_F` there exists a sequence

\[
s_n
\]

with

\[
\boxed{
\|\mathcal H_{T(s_n)}\|_{L^3(A_*)}
\ge h_*,
}
\]

and

\[
\boxed{
\|F_{T(s_n)}\|_{H^{-1}(A_*^+)}
\to0.
}
\]

Because the tail hull is compact, pass to a subsequence

\[
T(s_n)\to T_*
\]

locally on the punctured space.

Continuity of the residual gives

\[
\boxed{F_{T_*}=0}
\]

on the selected annulus, and covariance/minimal translation of the argument plus local equation continuation yields the stationary equation on every punctured compact set reached by the diagonal exhaustion.

At the same time strong local passage of the homogeneity defect gives

\[
\boxed{
\|T_*+Y\cdot\nabla T_*\|_{L^3(A_*)}
\ge h_*>0.
}
\]

Therefore

\[
\boxed{
T_*\text{ is a nonzero stationary critical punctured-space NS profile}
}
\]

which is **not** degree `-1` homogeneous.

---

## 6. The stationary branch is genuinely different from the Sverk/Landau branch

If

\[
T_*+Y\cdot\nabla T_*=0,
\]

then `T_*` is degree `-1` homogeneous and Sverk's classification applies: every nonzero smooth whole-sphere profile is Landau.

The present compactness branch satisfies the opposite inequality

\[
\boxed{
T_*+Y\cdot\nabla T_*\ne0.
}
\]

Therefore the homogeneous classification does not apply.

The stationary critical branch is instead

\[
\boxed{
\begin{cases}
-\nu\Delta T_*+(T_*\cdot\nabla)T_*+\nabla P_*=0,\\
\nabla\cdot T_*=0,\\
|T_*(Y)|\lesssim |Y|^{-1},\\
T_*+Y\cdot\nabla T_*\ne0.
\end{cases}}
\]

No general theorem excluding this arbitrary-amplitude, nonhomogeneous punctured-space class is imported here.

---

## 7. Literature scope audit

Sverk classifies smooth degree-`-1` stationary profiles on `R3\{0}` as Landau solutions.

Recent stationary-flow work continues to treat Landau solutions, small perturbations/asymptotics, or special symmetric/boundary configurations. These results do not supply a theorem saying

\[
|T(x)|\le C|x|^{-1}
\quad\Longrightarrow\quad
T\text{ is homogeneous/Landau}
\]

for arbitrary-amplitude smooth stationary solutions on the full punctured three-space.

Therefore the shortcut

\[
F_T=0
\Longrightarrow
\text{Landau}
\]

is RED unless exact homogeneity is separately proved.

---

## 8. Meaning of the residual-active branch

After choosing a large fixed divergence-free tail cutoff `B_T`, the finite-energy quotient

\[
Q=V-B_T
\in L^2\cap L^3
\]

satisfies

\[
\mathcal LQ
+
\mathbb P\nabla\cdot
(Q\otimes Q+Q\otimes B_T+B_T\otimes Q)
=
\mathcal F_{B_T}.
\]

Outside the transition annulus,

\[
\mathcal F_{B_T}=F_T.
\]

Hence Branch R gives a genuine recurrent forcing channel for the finite-energy quotient.

However critical shell scaling makes the physical cost of remote forcing potentially summable across generations. Therefore

\[
\text{positive residual density}
\not\Rightarrow
\text{finite-energy contradiction}
\]

without an additional noncritical gain.

---

## 9. DSD verdict

The aperiodic minimal branch is now reduced to the exact fork

\[
\boxed{
A_{min}^{aper}
\Longrightarrow
R_{tail}
\lor
S_{crit}^{nonhom},
}
\]

where

\[
R_{tail}:
\text{positive-density critical stationary-residual forcing},
\]

and

\[
S_{crit}^{nonhom}:
\text{an actual nonhomogeneous stationary punctured-space profile with }|T|\lesssim1/r.
\]

This is sharper than the previous generic `shape/nonlinear/pressure` language.

---

## 10. Next targets

Two separate attacks are now appropriate:

1. **Stationary rigidity audit** — determine what additional inherited W1 conditions (zero spherical flux, compact dilation hull, canonical Fuchsian regularity, stress charge, finite local enstrophy, recurrence in log radius) do to `S_crit^{nonhom}`.
2. **Residual-work audit** — pair `F_T` with the finite-energy quotient and test whether positive-density critical forcing necessarily creates a non-summable work/dissipation charge, or whether a critical anti-model survives.

The two branches must not be conflated.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]