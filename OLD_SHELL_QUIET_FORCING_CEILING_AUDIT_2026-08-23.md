# Old-Shell Quiet Forcing Ceiling Audit — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — THE `K_* R^{-3/2}` FORCING CEILING REQUIRED BY THE REMAINING-TIME CLOSURE IS REDUCED TO A FINITE LIST OF SCALE-INVARIANT LOCAL TYPE-I NORMS — GLOBAL REGULARITY NOT PROVED.**

This note audits the only quantitative hypothesis left in `SLIDING_HISTORY_REMAINING_TIME_CLOSURE_2026-08-23.md`:

\[
\|P_R\mathcal N_R\|_2
+
\|P_R\mathcal R_R\|_2
\le
K_*R^{-3/2}.
\]

The aim is to show that this is the natural consequence of bounded old-shell Type-I amplitude, derivative, pressure, time-derivative, and coherent-frame norms. If one of those quantities is not bounded, the shell has already exited into `H`, `T`, pressure/residual, or analyticity failure.

---

## 1. Dimensionless old-shell corridor constants

Fix a historical shell of physical radius `R` and a fixed-shape enlarged annulus `A_R^+`.

Define

\[
A_0
:=
R\|u\|_{L^\infty(A_R^+)},
\]

\[
E_0
:=
R^{-1}\|u\|_{L^2(A_R^+)}^2,
\]

\[
G_0
:=
R^{1/2}\|\nabla u\|_{L^2(A_R^+)},
\]

\[
T_0
:=
R^{3/2}\|\partial_tu\|_{L^2(A_R^+)},
\]

\[
P_0
:=
R^{1/2}
\inf_{c\in\mathbb R}
\|p-c\|_{L^2(A_R^+)},
\]

and for the coherent moving center

\[
V_0
:=
R\|u-\dot X\|_{L^\infty(\operatorname{trans})}.
\]

All are invariant under the Navier--Stokes first-hitting scaling.

For the Bogovskii `H^2` audit also define

\[
H_2
:=
R^{3/2}\|\nabla^2u\|_{L^2(A_R^+)},
\]

and, if time regularity is derived from the PDE rather than assumed directly,

\[
P_1
:=
R^{3/2}
\|\nabla p\|_{L^2(A_R^+)}.
\]

The quiet old-shell corridor means these constants stay below fixed scale-independent thresholds. Failure is already a typed derivative/pressure/drift exit.

---

## 2. Localized internal nonlinear term

Recall

\[
\mathcal N_R
=-\mathbb P\nabla\cdot(\chi_Ru\otimes u).
\]

The Leray projector is `L2` bounded, so

\[
\|\mathcal N_R\|_2
\le
\|\nabla(\chi_Ru\otimes u)\|_2.
\]

Using

\[
\|u\|_\infty\le A_0R^{-1},
\]

\[
\|u\|_2\le E_0^{1/2}R^{1/2},
\]

\[
\|\nabla u\|_2\le G_0R^{-1/2},
\]

and `|grad chi_R|<=C_chi/R`, we get

\[
\boxed{
\|\mathcal N_R\|_2
\le
C_NA_0
(G_0+E_0^{1/2})
R^{-3/2}.
}
\]

Thus the internal nonlinear forcing already has the required natural scale.

---

## 3. Material shell-crossing term

The moving-cutoff contribution is

\[
\mathcal R_{mat}
=
((u-\dot X)\cdot\nabla\chi_R)u.
\]

Therefore

\[
\begin{aligned}
\|\mathcal R_{mat}\|_2
&\le
\|u-\dot X\|_\infty
\|\nabla\chi_R\|_\infty
\|u\|_{L^2(\operatorname{trans})}\\
&\le
C_\chi
V_0E_0^{1/2}R^{-3/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\|\mathcal R_{mat}\|_2
\le
C_{mat}V_0E_0^{1/2}R^{-3/2}.
}
\]

If `V_0` is not uniformly bounded, this is precisely coherent-frame/material turnover rather than a quiet historical shell.

---

## 4. Pressure-buffer term

The pressure contribution after Leray projection is

\[
p\nabla\chi_R.
\]

A constant pressure may be subtracted freely because

\[
c\nabla\chi_R=\nabla(c\chi_R)
\]

and the Leray projector kills gradients.

Thus choose the minimizing shell pressure constant `c_R` and write

\[
\mathbb P(p\nabla\chi_R)
=
\mathbb P((p-c_R)\nabla\chi_R).
\]

Then

\[
\boxed{
\|\mathbb P(p\nabla\chi_R)\|_2
\le
C_pP_0R^{-3/2}.
}
\]

So the pressure part is controlled by a scale-invariant local pressure-oscillation norm; a failure is an explicit pressure branch, not a hidden localization error.

---

## 5. Direct viscous cutoff commutator

The explicit viscous boundary term is

\[
\mathcal R_{vis}
=-2\nu\nabla\chi_R\cdot\nabla u
-\nu(\Delta\chi_R)u.
\]

Using

\[
|\nabla\chi_R|\le C_\chi R^{-1},
\qquad
|\Delta\chi_R|\le C_\chi R^{-2},
\]

we obtain

\[
\boxed{
\|\mathcal R_{vis}\|_2
\le
C_{vis}\nu
(G_0+E_0^{1/2})R^{-3/2}.
}
\]

Again this is exactly the natural forcing scale.

---

## 6. Bogovskii correction: static estimates

Let

\[
g_R=\nabla\chi_R\cdot u.
\]

On each fixed-shape transition annulus, the mean of `g_R` is zero by the spherical flux cancellation.

The scaled Bogovskii operator gives

\[
\|\nabla b_R\|_2
\le
C_B\|g_R\|_2,
\]

and Poincare/scaling gives

\[
\|b_R\|_2
\le
C_BR\|g_R\|_2.
\]

Since

\[
\|g_R\|_2
\le
C_\chi R^{-1}\|u\|_2
\le
C_\chi E_0^{1/2}R^{-1/2},
\]

we have

\[
\boxed{
\|b_R\|_2
\le
C_BE_0^{1/2}R^{1/2},
}
\]

and

\[
\boxed{
\|\nabla b_R\|_2
\le
C_BE_0^{1/2}R^{-1/2}.
}
\]

Thus the solenoidal correction itself stays at the natural shell scale.

---

## 7. Time derivative of the Bogovskii correction

Work in coordinates translated with `X(t)` so that the reference annuli are fixed. Let

\[
D_X
:=
\partial_t+\dot X\cdot\nabla
\]

be the derivative in the moving frame.

Because the Bogovskii operator is fixed on the reference annulus and linear,

\[
D_Xb_R
=\mathcal B_R[D_Xg_R].
\]

Now

\[
g_R=\nabla\chi_R\cdot u.
\]

In the moving frame `D_X grad chi_R=0`, so

\[
D_Xg_R
=\nabla\chi_R\cdot D_Xu.
\]

Therefore

\[
\|D_Xg_R\|_2
\le
C_\chi R^{-1}
\left(
\|\partial_tu\|_2
+|\dot X|\|\nabla u\|_2
\right).
\]

Using

\[
\|\partial_tu\|_2
\le
T_0R^{-3/2},
\]

and a natural coherent-center speed bound

\[
R|\dot X|\le X_0
\]

with `X_0` scale independent, we get

\[
\|D_Xg_R\|_2
\le
C
(T_0+X_0G_0)R^{-5/2}.
\]

The Bogovskii operator gains one spatial scale in `L2`, hence

\[
\boxed{
\|D_Xb_R\|_2
\le
C_B
(T_0+X_0G_0)R^{-3/2}.
}
\]

Returning to fixed coordinates,

\[
\partial_tb_R
=D_Xb_R-\dot X\cdot\nabla b_R,
\]

and the second term also has size

\[
|\dot X|\|\nabla b_R\|_2
\le
C X_0E_0^{1/2}R^{-3/2}.
\]

Therefore

\[
\boxed{
\|\partial_tb_R\|_2
\le
C_{Bt}
(T_0+X_0G_0+X_0E_0^{1/2})R^{-3/2}.
}
\]

This confirms that the time-dependent divergence correction has the same natural forcing scale, provided the normalized time derivative and center speed remain bounded.

---

## 8. Laplacian of the Bogovskii correction

On a smooth fixed-shape annulus the Bogovskii operator has the standard one-derivative gain in Sobolev scales. At the `H^1 -> H^2` level,

\[
\|\nabla^2b_R\|_2
\le
C_B\|\nabla g_R\|_2.
\]

Now

\[
\nabla g_R
=\nabla^2\chi_R\,u
+\nabla\chi_R\,\nabla u,
\]

so

\[
\|\nabla g_R\|_2
\le
C
(E_0^{1/2}+G_0)R^{-3/2}.
\]

Hence

\[
\boxed{
\nu\|\Delta b_R\|_2
\le
C_{B2}\nu
(E_0^{1/2}+G_0)R^{-3/2}.
}
\]

Thus the complete Bogovskii term

\[
-\partial_tb_R+\nu\Delta b_R
\]

also satisfies the desired natural scale ceiling.

---

## 9. Time-derivative constant can be reduced to higher derivative/pressure constants

If `T_0` is not taken as an independent quiet-corridor parameter, use Navier--Stokes:

\[
\partial_tu
=\nu\Delta u-(u\cdot\nabla)u-\nabla p.
\]

Therefore

\[
T_0
\le
C
\left[
\nu H_2
+A_0G_0
+P_1
\right].
\]

Thus a failure of the time-derivative bound is itself a failure of

- second-derivative tightness;
- natural nonlinear amplitude/gradient control;
- or pressure-gradient control.

These are already derivative/pressure/residual exits from the quiet corridor.

---

## 10. Explicit schematic forcing constant

Collecting the previous estimates gives

\[
\boxed{
\|\mathcal N_R\|_2
+
\|\mathcal R_R\|_2
\le
K_*R^{-3/2},
}
\]

with

\[
\boxed{
\begin{aligned}
K_*
\le C_{loc}\big[&
A_0(G_0+E_0^{1/2})
+V_0E_0^{1/2}
+P_0\\
&+\nu(G_0+E_0^{1/2})
+T_0
+X_0G_0
+X_0E_0^{1/2}
\big].
\end{aligned}
}
\]

Here `C_loc` depends only on the fixed cutoff geometry and the fixed reference-annulus Bogovskii constants, not on `R` or the first-hitting stage index.

Replacing `T_0` by the PDE estimate makes `K_*` a function of the finite list

\[
A_0,
E_0,
G_0,
H_2,
P_0,
P_1,
V_0,
X_0,
\nu.
\]

---

## 11. Consequence for remaining-time compression

The remaining-time closure only needs `K_*` to be finite and scale independent. It does not need `K_*` to be small.

Indeed the contradiction was

\[
c_*
\le
K_*C_TK_j^{-2}.
\]

For every fixed finite `K_*`, the right-hand side tends to zero because

\[
K_j\to\infty.
\]

Therefore the quiet sliding-history branch is robust to large localization constants.

The only escape is for at least one normalized old-shell quantity entering `K_*` to become unbounded along the selected shells. But that is exactly a typed exit:

\[
\boxed{
\begin{aligned}
A_0,E_0,V_0 &\to \text{parent/material/turnover or Type-I envelope failure},\\
G_0,H_2 &\to H/derivative escape,\\
P_0,P_1 &\to pressure/residual branch,\\
X_0 &\to coherent-center/drift turnover.
\end{aligned}
}
\]

Thus `K_*` is not a new independent obstruction.

---

## 12. Current status

The key quantitative assumption required to close quiet sliding history has now been audited to natural local norms.

Subject to the standard smooth-annulus Bogovskii Sobolev mapping properties and an explicit identification of the quiet-corridor thresholds, the logic is now:

\[
\boxed{
\text{all normalized old-shell local quantities bounded}
\Longrightarrow
K_*<\infty
}
\]

and then

\[
\boxed{
K_j\to\infty
\Longrightarrow
\text{quiet forgetting impossible}.
}
\]

If the local quantities are not bounded, the shell has already exited into a named `H/T/pressure/drift` branch.

Status: **THE FORCING-CEILING CONSTANT NEEDED BY THE `K^{-2}` REMAINING-TIME CONTRADICTION IS REDUCED TO A FINITE SCALE-INVARIANT LOCAL NORM AUDIT. THE HISTORICAL-SHELL RECYCLING BRANCH IS VERY CLOSE TO BEING FULLY ROUTED INTO EXISTING H/T/PRESSURE/DRIFT EXITS, BUT THOSE EXIT BRANCHES ARE NOT YET ALL GLOBALLY CLOSED.**
