# DSD M5-228 — Same-Point-Force Dilate Difference Relative Stationary Energy Gate

Date: 2026-08-30

Parent: `DSD_M5_227_STATIONARY_CRITICAL_TAIL_POINT_FORCE_EXTENSION_AND_ZERO_TORQUE_REDUCTION_2026-08-30.md`

Status: **EXACT RELATIVE EQUATION / TWO DILATES OF ONE STATIONARY CRITICAL TAIL SOLVE THE SAME `b delta_0` PROBLEM, SO THEIR DIFFERENCE SATISFIES AN UNFORCED STATIONARY OSEEN--NAVIER--STOKES RELATIVE EQUATION / THE EXTERIOR RELATIVE ENERGY IDENTITY HAS ONE ARBITRARY-AMPLITUDE HARDY-CRITICAL STRAIN FORM, EXACTLY THE SAME OBSTRUCTION SEEN IN THE DYNAMIC SAME-TAIL BACKWARD PROBLEM / SMALL WEAK-L3 BACKGROUND UNIQUENESS IS COMPATIBLE WITH THIS IDENTITY, BUT LARGE AMPLITUDE IS NOT COERCIVE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Two dilates solve the same point-force equation

Let

\[
T_0:=T
\]

be a stationary tail from M5-227 and for fixed `h` define

\[
\boxed{
T_h:=D_hT,
\qquad
T_h(x)=e^{-h/2}T(e^{-h/2}x).
}
\]

M5-227 proves

\[
-\nu\Delta T_0
+(T_0\cdot\nabla)T_0
+\nabla P_0
=b\delta_0,
\]

and

\[
-\nu\Delta T_h
+(T_h\cdot\nabla)T_h
+\nabla P_h
=b\delta_0.
\]

Thus the singular forcing cancels exactly after subtraction.

---

## 2. Relative field

Set

\[
\boxed{W_h:=T_h-T_0,}
\]

\[
q_h:=P_h-P_0.
\]

Then distributionally on all of `R3`,

\[
\boxed{
-\nu\Delta W_h
+(T_h\cdot\nabla)W_h
+(W_h\cdot\nabla)T_0
+\nabla q_h
=0,
}
\]

with

\[
\boxed{\nabla\cdot W_h=0.}
\]

The equivalent expansion

\[
(T_0\cdot\nabla)W_h
+(W_h\cdot\nabla)T_0
+(W_h\cdot\nabla)W_h
\]

is also exact.

The first form is preferable because the transport field `T_h` is divergence free and therefore energy-skew.

---

## 3. Log-radius form of the relative mode

Write

\[
T_0(r\theta)=r^{-1}\Phi(y,\theta),
\qquad y=\log r.
\]

Then

\[
T_h(r\theta)
=r^{-1}\Phi(y-h/2,\theta).
\]

Hence

\[
\boxed{
W_h(r\theta)
=
\frac1r
\left[
\Phi(y-h/2,\theta)-\Phi(y,\theta)
\right].
}
\]

For the fixed no-short-return shift `h=h_*` of M5-219, this difference has a positive critical cubic scale-phase density.

In particular it is not zero on the nontrivial minimal branch.

---

## 4. Exterior relative energy identity

Fix `R>0` and integrate on

\[
\Omega_R:=\{|x|>R\}.
\]

Pair the relative equation with `W_h`.

The diffusion term gives

\[
\nu\int_{\Omega_R}|\nabla W_h|^2dx
\]

plus the radial boundary contribution.

The transport term is a pure boundary flux:

\[
\int_{\Omega_R}
(T_h\cdot\nabla W_h)\cdot W_h
=
-\frac12
\int_{|x|=R}
|W_h|^2(T_h\cdot n)dS
\]

for the outward normal of the exterior region after the standard orientation convention.

The cross-gradient term is

\[
\int_{\Omega_R}
W_h^T(\nabla T_0)W_hdx
=
\int_{\Omega_R}
W_h^TS_{T_0}W_hdx
\]

because the antisymmetric part drops from the quadratic form.

The pressure term is also a boundary flux.

Thus

\[
\boxed{
\nu\int_{\Omega_R}|\nabla W_h|^2dx
+
\int_{\Omega_R}W_h^TS_{T_0}W_hdx
=
\mathcal B_h(R),
}
\]

where `mathcal B_h(R)` is the exact finite radial boundary work made of

- viscous normal derivative;
- transport kinetic flux;
- relative pressure flux.

The contribution at spatial infinity vanishes under the critical `1/r` / `1/r^2` bounds.

---

## 5. The relative field has finite exterior Dirichlet energy

Since

\[
|\nabla W_h(x)|\lesssim |x|^{-2},
\]

one has

\[
\boxed{
\int_{|x|>R}|\nabla W_h|^2dx<\infty.
}
\]

Indeed

\[
\int_R^\infty r^{-4}r^2dr
\sim R^{-1}.
\]

The velocity itself need not belong to exterior `L2`:

\[
|W_h|\sim r^{-1}
\]

may give linear `L2` divergence at infinity.

Thus the natural stationary relative topology is the exterior homogeneous `H1`/critical Lorentz topology, not global `L2`.

---

## 6. The only bulk indefinite term is Hardy-critical strain

The background satisfies

\[
|S_{T_0}(x)|\le \frac{A_S}{|x|^2}.
\]

Therefore

\[
\left|
\int_{\Omega_R}
W_h^TS_{T_0}W_hdx
\right|
\le
A_S
\int_{\Omega_R}
\frac{|W_h|^2}{|x|^2}dx.
\]

After the appropriate exterior Hardy inequality/cutoff form,

\[
\int
\frac{|\chi_R W_h|^2}{|x|^2}
\le
4\int|\nabla(\chi_RW_h)|^2,
\]

so the bulk strain has exactly the critical form bound

\[
\boxed{
|\mathfrak q_{T_0}[W_h]|
\lesssim
4A_S
\|\nabla W_h\|_2^2
+
\text{boundary-shell terms}.
}
\]

The coefficient cannot be made small by moving `R` outward because both the strain and Hardy weight scale as `r^-2`.

This is an **arbitrary-amplitude Hardy-critical obstruction**.

---

## 7. Small amplitude recovers perturbative uniqueness

If the scale-invariant background amplitude is sufficiently small so that the strain form can be absorbed into viscosity,

\[
4A_S<\nu
\]

schematically, and the radial boundary contribution is sent through the standard exterior cutoff limit, then the relative identity forces

\[
\nabla W_h=0.
\]

Decay at infinity then gives

\[
W_h=0.
\]

Thus every dilation equals the original field and the tail is homogeneous.

This is consistent with the perturbative stationary uniqueness/Landau asymptotic literature and with M5-221.

The exact numerical threshold from external theorems is not identified with the crude Hardy constant above.

---

## 8. Large amplitude loses coercivity

On the surviving branch

\[
A_* > \varepsilon_{KS},
\]

no smallness of the critical strain form is available.

The quadratic form

\[
\nu\|\nabla W_h\|_2^2
+
\int W_h^TS_{T_0}W_h
\]

may therefore have either sign or a nontrivial kernel.

Hence

\[
\boxed{
\text{same point force}
+
\text{finite exterior Dirichlet difference}
\not\Rightarrow
T_h=T_0
}
\]

by the current energy argument.

This is the precise large-data stationary uniqueness gap.

---

## 9. Relation to existing stationary uniqueness criteria

Known 3D exterior uniqueness criteria in critical Lorentz classes impose smallness on at least one stationary solution/background.

That is exactly what the relative energy/form structure predicts: the only noncompact bulk obstruction is the scale-critical background strain.

The current branch is specifically the complement where this perturbative absorption is unavailable.

Thus no literature theorem is silently promoted to arbitrary amplitude.

---

## 10. Infinitesimal dilation mode

For small `h`,

\[
\frac{W_h}{h}
\to
-\frac12
\left(T_0+x\cdot\nabla T_0\right)
=-\frac12\mathcal H_T
\]

locally.

Therefore the homogeneity-defect field is the infinitesimal same-point-force relative mode.

Differentiating the stationary point-force equation along dilation gives the homogeneous linearized stationary system

\[
\boxed{
-\nu\Delta\mathcal H_T
+(T\cdot\nabla)\mathcal H_T
+(\mathcal H_T\cdot\nabla)T
+\nabla\pi_H
=0
}
\]

on all of `R3` in the distributional sense, with no derivative of `delta_0` because the point-force coefficient `b` is dilation invariant.

This is an important structural reformulation.

---

## 11. Positive critical residue becomes a linearized zero mode

M5-224 gives

\[
\underline{\mathscr R}_H(T)>0.
\]

Thus the large stationary endpoint supports a nontrivial solution

\[
\boxed{
\mathcal H_T
=T+x\cdot\nabla T
}
\]

of the **homogeneous linearized stationary operator around `T`**, with critical `1/r` size and positive logarithmic cubic density.

Therefore the endpoint can be stated spectrally as:

> an arbitrary-large point-force stationary solution whose linearized operator has a nontrivial critical dilation zero-mode.

For a homogeneous Landau solution this mode is identically zero.

---

## 12. Updated stationary frontier

The stationary endpoint is sharpened to

\[
\boxed{
S_{point,large}^{nonhom}
\Longrightarrow
\begin{cases}
\mathcal L_T^{stat}\mathcal H_T+\nabla\pi_H=0,\\
\mathcal H_T\not\equiv0,\\
\underline{\mathscr R}_H(T)>0,\\
\text{Hardy-critical quadratic form not perturbatively coercive}.
\end{cases}}
\]

This connects the stationary large-data problem to the spectral/nondegeneracy theory of Landau-type point-force solutions.

---

## 13. Next target

A useful next literature/internal audit is now precise:

1. determine known **nondegeneracy/kernel results for the stationary linearization around Landau solutions** beyond the small regime;
2. test whether a nonzero dilation kernel can occur for a fixed point-force solution without generating a bifurcation branch;
3. compare with Kwon--Tsai's stationary DSS/self-similar bifurcation analysis, carefully respecting its symmetry and perturbative scope.

No spectral nondegeneracy theorem is assumed here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]