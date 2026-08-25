# DSD Absolute-Action Compensated Variance Gate

Date: 2026-08-25

Status: **ABSOLUTE BOUNDARY ACTION + COMPENSATED-VARIANCE VARIATION GIVE A CLEAN PURE/PAID DICHOTOMY / eta AND NET-FLUX CANCELLATION REMOVED / PURE STAGE CEILING SHARPENED TO 6/pi^2 / GLOBAL REGULARITY UNPROVED.**

## 1. Exact compensated variance identity

Use the scale-compensated moving-ball variance from the preceding note:

\[
\mathcal W(s)=e^{-A(s)}V(s),
\qquad
A(s)=\int_{s_0}^sa(\sigma)d\sigma.
\]

The exact identity is

\[
\boxed{
\frac12\mathcal W'(s)+\nu E(s)=F_w(s),
}
\]

where

\[
E(s):=e^{-A(s)}D(s)\ge0,
\qquad
F_w(s):=e^{-A(s)}\mathcal F(s).
\]

Thus

\[
\boxed{
\mathcal W'(s)=2(F_w(s)-\nu E(s)).
}
\]

All normalization-growth effects have already been removed.

## 2. Total-variation action inequality

For any subinterval `J`,

\[
\operatorname{Var}_J(\mathcal W)
=
\int_J|\mathcal W'(s)|ds.
\]

Using the exact derivative formula,

\[
\boxed{
\operatorname{Var}_J(\mathcal W)
\le
2\left(
\int_J|F_w|ds
+
\nu\int_JEds
\right).
}
\]

Define the absolute weighted boundary work and viscous action

\[
\boxed{
\mathscr B_J:=\int_J|F_w|ds,
\qquad
\mathscr D_J:=\nu\int_JEds.
}
\]

Then

\[
\boxed{
\operatorname{Var}_J(\mathcal W)
\le2(\mathscr B_J+\mathscr D_J).
}
\]

Status: **EXACT/PROVED.**

## 3. Fixed cost of order-one compensated turnover

Let

\[
\mathcal W_*
:=
\inf_{s\in J}\mathcal W(s)>0.
\]

If

\[
\operatorname{Var}_J(\mathcal W)
>\delta\mathcal W_*
\]

for some fixed `delta>0`, then

\[
\boxed{
\mathscr B_J+\mathscr D_J
>
\frac\delta2\mathcal W_*.
}
\]

In particular, at least one of the two payers satisfies

\[
\boxed{
\mathscr B_J
>
\frac\delta4\mathcal W_*
\quad\lor\quad
\mathscr D_J
>
\frac\delta4\mathcal W_*.
}
\]

Thus compensated-variance turnover is not a merely geometric label: it has a fixed normalized local-energy action cost.

## 4. Absolute-action pure corridor

On one stage `I_j`, define

\[
\mathcal W_-
:=
\inf_{I_j}\mathcal W>0,
\]

and the dimensionless quantities

\[
\boxed{
b_c:=\frac{\mathscr B_{I_j}}{\mathcal W_-},
\qquad
v_c:=rac{\operatorname{Var}_{I_j}(\mathcal W)}{\mathcal W_-}.
}
\]

Define the absolute-action pure corridor by

\[
\boxed{
b_c\le1,
\qquad
v_c\le1.}
\]

Its complement is

\[
\boxed{
b_c>1
\quad\lor\quad
v_c>1.}
\]

If `b_c>1`, the stage directly carries order-one absolute boundary work.

If `v_c>1`, Section 3 gives order-one boundary work or viscous action.

Therefore every complement stage is genuinely paid.

## 5. Pure-stage dissipation bound without eta

Integrate the exact compensated identity:

\[
\mathscr D_{I_j}
=
\int_{I_j}F_wds
+
\frac12\left[
\mathcal W(s_0)-\mathcal W(s_1)
\right].
\]

Hence

\[
\mathscr D_{I_j}
\le
\mathscr B_{I_j}
+
\frac12
\operatorname{Var}_{I_j}(\mathcal W).
\]

On the pure corridor,

\[
\boxed{
\mathscr D_{I_j}
\le
\frac32\mathcal W_-.
}
\]

No boundary-absorption parameter `eta` and no cancellation-sensitive net-flux allowance appear.

## 6. Poincare gives the sharpened stage ceiling

On a Euclidean moving ball of radius `R`,

\[
V\le\frac{4R^2}{\pi^2}D.
\]

Therefore

\[
E=e^{-A}D
\ge
\frac{\pi^2}{4R^2}\mathcal W
\ge
\frac{\pi^2}{4R^2}\mathcal W_-.
\]

Thus

\[
\mathscr D_{I_j}
=
\nu\int_{I_j}Eds
\ge
\nu\frac{\pi^2}{4R^2}
\mathcal W_-L_j.
\]

Combine with the pure upper bound:

\[
\nu\frac{\pi^2}{4R^2}
\mathcal W_-L_j
\le
\frac32\mathcal W_-.
\]

Cancel the positive floor:

\[
\boxed{
L_j
\le
\frac6{\pi^2}
\frac{R^2}{\nu}.
}
\]

Hence the absolute-action persistence coefficient is

\[
\boxed{
\Pi_{abs}:=\frac6{\pi^2}
\approx0.6079271019.
}
\]

This is half the previous `12/pi^2` compensated-net-flux ceiling and substantially below the older raw-variance `1.496776...` coefficient.

Status: **PROVED on the absolute-action pure corridor.**

## 7. Apply at the enstrophy-tightness radius

Choose

\[
R=R_Z
\]

on the coherent moving-core/tightness lane.

Then either

\[
\boxed{
T_{abs}(R_Z):
\quad
b_c>1
\lor
v_c>1,
}
\]

which carries a fixed boundary/dissipation action cost, or

\[
\boxed{
L_j
\le
L_{abs,+}
:=
\frac6{\pi^2}
\frac{R_Z^2}{\nu}.
}
\]

Thus the stage-time complement has become a quantitatively paid branch rather than merely a failure of a persistence assumption.

## 8. Combine with first-hitting strain action

A factor-`q` amplification requires

\[
\log q\le B_0L_j,
\]

where

\[
B_0
=
C_I
\left(\frac{M_0}{\rho_0}\right)^{3/5}
\left[
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
\right]^{1/5},
\]

\[
C_I
=
\frac{5\sqrt3}{3}6^{1/5}\pi^{-1/5}.
\]

On the absolute-action pure branch,

\[
\log q
\le
B_0
\frac6{\pi^2}
\frac{R_Z^2}{\nu}.
\]

Therefore every pure recurrent survivor requires

\[
\boxed{
R_Z
\ge
R_{Z,abs,-}
:=
\left[
\frac{\nu\log q}
{C_I(6/\pi^2)}
\left(\frac{\rho_0}{M_0}\right)^{3/5}
\left(
\frac{3(1-\varepsilon_Z)}{4\pi}
\right)^{1/5}
\right]^{5/13}.
}
\]

## 9. q=2 numerical benchmark

For `q=2`, `epsilon_Z=0`,

\[
\boxed{
R_Z
\gtrsim
0.5961616976
\nu^{5/13}
\left(\frac{\rho_0}{M_0}\right)^{3/13}.
}
\]

For `epsilon_Z=1/4`,

\[
\boxed{
R_Z
\gtrsim
0.5831139051
\nu^{5/13}
\left(\frac{\rho_0}{M_0}\right)^{3/13}.
}
\]

Thus replacing cancellation-sensitive net-flux bookkeeping by absolute action significantly enlarges the directly S-closed small-tightness region.

## 10. Long-time meaning of the complement

A stage in `T_abs(R_Z)` has one of two quantitative forms:

1. absolute boundary work
   \[
   \mathscr B_{I_j}>\mathcal W_-;
   \]
2. compensated variance turnover, which forces
   \[
   \mathscr B_{I_j}+\mathscr D_{I_j}>rac12\mathcal W_-.
   \]

Therefore repeated `T_abs` cannot be called a quiet turnover lane.

The unresolved issue is no longer whether a turnover event pays. It does.

The remaining issue is whether the normalized reference scale `W_-` can degenerate across the event sequence or whether recurrent active-core compactness supplies a uniform positive normalized floor. On a fixed compact recurrent active-core neighborhood this floor is expected to be positive; its exact inheritance should be stated before summing event costs globally.

## 11. Updated frontier

The local pure/turnover dichotomy is now

\[
\boxed{
\begin{aligned}
&\text{absolute-action pure at }R_Z
&&\Longrightarrow
L_j\le\frac6{\pi^2}\frac{R_Z^2}{\nu},\\
& T_{abs}(R_Z)
&&\Longrightarrow
\text{fixed normalized boundary/dissipation action cost}.
\end{aligned}
}
\]

The highest-leverage next calculation is to establish a uniform recurrent lower floor for the scale-compensated reference variance `W_-` on the active-core orbit. If that floor is obtained, positive-frequency `T_abs` produces a positive mean local-energy action floor and can be compared directly with the existing recurrent H1/energy/export budgets.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]