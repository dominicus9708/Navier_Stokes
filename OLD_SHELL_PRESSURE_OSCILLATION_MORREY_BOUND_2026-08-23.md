# Old-Shell Pressure Oscillation from the Parent Morrey Bound — 2026-08-23

Overall status: **ACTIVE PROOF ATTEMPT — PRESSURE OSCILLATION AND PRESSURE-GRADIENT CONSTANTS IN THE OLD-SHELL FORCING AUDIT ARE BOUNDED BY THE EXISTING MORREY/TYPE-I/DERIVATIVE CORRIDOR — GLOBAL REGULARITY NOT PROVED.**

This note sharpens `OLD_SHELL_QUIET_FORCING_CEILING_AUDIT_2026-08-23.md`.

The remaining-time closure allows pressure-buffer forcing as a possible escape only if the dimensionless old-shell pressure norms become large. Here we show that under the already used parent Morrey energy control and local Type-I shell amplitude/derivative control, those pressure norms are uniformly bounded.

Thus pressure is not an independent way for a quiet historical shell to defeat the `K^-2` time compression.

---

## 1. Geometry and assumptions

Fix center `X` and an old historical radius `R`.

Let the observation shell be

\[
A_R
=\{R/2<|x-X|<2R\},
\]

and let the local source shell be

\[
A_R^+
=\{R/4<|x-X|<4R\}.
\]

Assume the scale-invariant parent Morrey energy corridor

\[
\boxed{
\mathcal M_s(X,t)
:=s^{-1}\int_{B_s(X)}|u|^2dx
\le M_*
}
\]

for all parent radii needed in the dyadic pressure decomposition.

On `A_R^+`, assume the old-shell Type-I amplitude and derivative bounds

\[
\boxed{
\|u\|_{L^\infty(A_R^+)}
\le A_0R^{-1},
}
\]

\[
\boxed{
\|u\|_{L^2(A_R^+)}
\le E_0^{1/2}R^{1/2},
}
\]

\[
\boxed{
\|\nabla u\|_{L^2(A_R^+)}
\le G_0R^{-1/2}.
}
\]

These are exactly the old-shell corridor quantities already introduced in the forcing audit.

---

## 2. Pressure decomposition

The whole-space pressure satisfies

\[
p=\mathcal R_i\mathcal R_j(u_iu_j).
\]

Choose a smooth radial source cutoff `zeta_R` satisfying

\[
\zeta_R=1
\quad\text{on a neighborhood of }A_R,
\]

\[
\operatorname{supp}\zeta_R
\subset A_R^+,
\]

and

\[
|\nabla\zeta_R|\lesssim R^{-1}.
\]

Write

\[
\boxed{
p=p_{loc}+p_{far},
}
\]

where

\[
p_{loc}
:=
\mathcal R_i\mathcal R_j(\zeta_Ru_iu_j),
\]

and

\[
p_{far}
:=
\mathcal R_i\mathcal R_j((1-\zeta_R)u_iu_j).
\]

The far part is harmonic on the observation shell.

---

## 3. Local pressure oscillation

Calderon--Zygmund boundedness on `L2` gives

\[
\|p_{loc}\|_2
\le
C_{CZ}\|\zeta_Ru\otimes u\|_2.
\]

Using the shell amplitude and kinetic bounds,

\[
\|u\otimes u\|_{L^2(A_R^+)}
\le
\|u\|_{L^\infty(A_R^+)}
\|u\|_{L^2(A_R^+)},
\]

so

\[
\boxed{
\|p_{loc}\|_2
\le
C_{loc}A_0E_0^{1/2}R^{-1/2}.
}
\]

Therefore the dimensionless local pressure constant satisfies

\[
\boxed{
R^{1/2}\|p_{loc}\|_2
\le
C_{loc}A_0E_0^{1/2}.
}
\]

---

## 4. Far pressure gradient from the inner source

For `x in A_R`, sources with

\[
|y-X|\le R/4
\]

are at distance `gtrsim R`.

The gradient of the pressure kernel is homogeneous of degree `-4`, hence

\[
|\nabla p_{inner}(x)|
\lesssim
R^{-4}
\int_{B_{R/4}(X)}|u(y)|^2dy.
\]

Morrey control gives

\[
\int_{B_{R/4}}|u|^2
\le
M_*R/4.
\]

Thus

\[
\boxed{
|\nabla p_{inner}(x)|
\le
C M_*R^{-3}.
}
\]

The fact that the current singular core may have amplitude much larger than `R^-1` is harmless here: only its total Morrey energy enters the old-shell pressure field.

---

## 5. Far pressure gradient from outer sources

For the outer region, split into dyadic annuli

\[
A_k^{out}
=
\{2^kR<|y-X|<2^{k+1}R\},
\qquad k\ge2.
\]

For `x in A_R`, the distance to `A_k^{out}` is `gtrsim 2^kR`. Hence

\[
|\nabla p_k(x)|
\lesssim
(2^kR)^{-4}
\int_{A_k^{out}}|u|^2dy.
\]

The parent Morrey bound gives

\[
\int_{A_k^{out}}|u|^2
\le
M_*2^{k+1}R.
\]

Therefore

\[
|\nabla p_k(x)|
\lesssim
M_*2^{-3k}R^{-3}.
\]

Summing the geometric series,

\[
\boxed{
|\nabla p_{outer}(x)|
\le
C M_*R^{-3}.
}
\]

Together with the inner estimate,

\[
\boxed{
\|\nabla p_{far}\|_{L^\infty(A_R)}
\le
C_{far}M_*R^{-3}.
}
\]

---

## 6. Far pressure oscillation after subtracting a constant

Fix one point `x_R in A_R` and set

\[
c_R:=p_{far}(x_R).
\]

Since `A_R` has diameter `O(R)`, the gradient bound gives

\[
|p_{far}(x)-c_R|
\le
C R\|\nabla p_{far}\|_\infty
\le
C M_*R^{-2}.
\]

The shell volume is `O(R^3)`, hence

\[
\boxed{
\|p_{far}-c_R\|_{L^2(A_R)}
\le
C M_*R^{-1/2}.
}
\]

Thus

\[
\boxed{
R^{1/2}
\inf_c\|p_{far}-c\|_{L^2(A_R)}
\le
C M_*.
}
\]

---

## 7. Complete pressure-oscillation bound

Combining local and far parts gives

\[
\boxed{
P_0
:=
R^{1/2}
\inf_c\|p-c\|_{L^2(A_R)}
\le
C_P
\left(
A_0E_0^{1/2}+M_*
\right).
}
\]

This is the pressure norm needed for the buffer forcing estimate

\[
\|\mathbb P((p-c)\nabla\chi_R)\|_2
\lesssim
P_0R^{-3/2}.
\]

Therefore pressure-buffer forcing remains at the natural `R^-3/2` scale whenever the shell amplitude/energy and parent Morrey quantities remain bounded.

It cannot grow like the `K^2R^-3/2` amplification needed to erase an old shell in the compressed remaining time.

---

## 8. Pressure-gradient bound

The forcing audit also used

\[
P_1
:=
R^{3/2}\|\nabla p\|_{L^2(A_R)}.
\]

For the far part,

\[
\|\nabla p_{far}\|_{L^2(A_R)}
\le
C M_*R^{-3}R^{3/2}
=
C M_*R^{-3/2}.
\]

Hence

\[
R^{3/2}\|\nabla p_{far}\|_2
\le
C M_*.
\]

For the local part,

\[
\nabla p_{loc}
=\mathcal R_i\mathcal R_j
\nabla(\zeta_Ru_iu_j).
\]

Calderon--Zygmund gives

\[
\|\nabla p_{loc}\|_2
\lesssim
\|\nabla(\zeta_Ru\otimes u)\|_2.
\]

Using the shell amplitude/gradient bounds,

\[
\boxed{
\|\nabla p_{loc}\|_2
\le
C A_0(G_0+E_0^{1/2})R^{-3/2}.
}
\]

Thus

\[
\boxed{
P_1
\le
C_{P1}
\left[
A_0(G_0+E_0^{1/2})+M_*
\right].
}
\]

---

## 9. Consequence for the time-derivative norm

Navier--Stokes gives

\[
\partial_tu
=\nu\Delta u-(u\cdot\nabla)u-\nabla p.
\]

Therefore, with

\[
H_2=R^{3/2}\|\nabla^2u\|_2,
\]

we have

\[
\boxed{
T_0
:=R^{3/2}\|\partial_tu\|_2
\le
C
\left[
\nu H_2
+A_0G_0
+A_0E_0^{1/2}
+M_*
\right].
}
\]

Hence `T_0` is also bounded by the derivative-tight / Morrey / Type-I corridor. A blow-up of `T_0` requires a derivative or Morrey failure rather than a new temporal mechanism.

---

## 10. Updated forcing ceiling

Insert the pressure estimates into `OLD_SHELL_QUIET_FORCING_CEILING_AUDIT_2026-08-23.md`.

The scale-independent old-shell forcing constant can be taken schematically as

\[
\boxed{
K_*
\le
\mathcal K
(A_0,E_0,G_0,H_2,M_*,V_0,X_0,\nu),
}
\]

with no independent pressure parameter.

Thus, under bounded

- Type-I shell amplitude/energy;
- first and second derivative norms;
- parent Morrey energy;
- coherent relative velocity and center speed;

the entire localized forcing stays at natural size

\[
\boxed{
\|\mathcal N_R\|_2+\|\mathcal R_R\|_2
\le
K_*R^{-3/2}.
}
\]

The `K^-2` remaining-time contradiction then applies.

---

## 11. Branch reduction

For the old-shell historical recycling problem, pressure is now reduced as follows:

\[
\boxed{
\text{bounded Morrey + shell Type-I/derivative corridor}
\Longrightarrow
\text{bounded old-shell pressure oscillation/gradient}.
}
\]

Therefore a pressure explosion large enough to erase the shell in `O(K^-2)` of its natural time requires the failure of the parent Morrey or shell derivative corridor, which is already `T/H` typed.

This agrees with the earlier `PARENT_PRESSURE_ESCALATION_FINITE_GATE_2026-08-21.md`, where genuinely remote pressure action was shown unable to escalate indefinitely under the same Morrey control.

Status: **OLD-SHELL PRESSURE CANNOT PROVIDE AN INDEPENDENT `K^2` FORCING AMPLIFICATION UNDER THE EXISTING MORREY/TYPE-I CORRIDOR. THE HISTORICAL RECYCLING EXIT TREE IS FURTHER REDUCED TOWARD DERIVATIVE H OR MATERIAL/DRIFT T. GLOBAL REGULARITY REMAINS UNPROVED.**
