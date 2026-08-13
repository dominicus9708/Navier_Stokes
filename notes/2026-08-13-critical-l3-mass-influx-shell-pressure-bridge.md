# Critical local L3 mass influx: shell flux or pressure work

Date: 2026-08-13

Status: **EXACT LOCAL L3 BALANCE + CONDITIONAL TERMINAL-NONTRIVIALITY BRIDGE / GLOBAL REGULARITY NOT PROVED**.

The ancient-limit route now has an external Liouville gate: a mild ancient solution with uniformly bounded global `L3` norm along a backward sequence is trivial (Albritton--Barker, Theorem 1.2).  Avoiding that gate naturally leads to critical `L3` mass escaping to normalized spatial infinity.

This note shows how such an escape must return to the terminal dangerous core: if the terminal compact branch has nontrivial local critical velocity mass while a far physical past slice becomes locally invisible after blow-up scaling, then an order-one amount of critical mass must enter through shell flux and/or pressure work.

---

## 1. Terminal vorticity core gives local relative-velocity mass on the compact branch

At terminal first hitting,

\[
|\Omega(0,0)|=1.
\]

Assume the bounded compact branch supplies a uniform local Holder estimate

\[
[\Omega(\cdot,0)]_{C^\alpha(B_1)}\le C_*.
\]

Then for some `rho_*>0` depending only on the compactness constants, with

\[
e=\Omega(0,0)/|\Omega(0,0)|,
\]

we have

\[
\boxed{
\Omega(y,0)\cdot e\ge\frac12
\qquad(|y|\le\rho_*).
}
\]

Thus one curl component has fixed sign and fixed size on `B_{rho_*}`.

Let `V=U-b` for any spatially constant local reference velocity `b` (for example a weighted/local mean).  Since curl is unchanged by subtracting `b`, a standard local `H^{-1}` curl estimate gives

\[
\|\Omega\cdot e\|_{H^{-1}(B_{2\rho_*})}
\le C\|V\|_{L^2(B_{2\rho_*})}.
\]

The fixed positive curl component yields a uniform lower bound on the left side.  Hence

\[
\boxed{
\|V(\cdot,0)\|_{L^2(B_{2\rho_*})}
\ge c_*>0.
}
\]

Because the ball has finite volume,

\[
\boxed{
\|V(\cdot,0)\|_{L^3(B_{2\rho_*})}
\ge c_{**}>0.
}
\]

Therefore the compact terminal dangerous core carries nontrivial local critical velocity mass.

---

## 2. Fixed physical history becomes locally invisible

Fix `t0<T*` in the smooth physical past and terminal first-hitting scales

\[
r_j=W_j^{-1/2}.
\]

Because `u(t0) in L3(R3)`, for every fixed normalized radius `R`,

\[
\boxed{
\int_{B_R}|U_j(y,s_j)|^3dy
=
\int_{B_{Rr_j}(x_j)}|u(x,t_0)|^3dx
\to0,
}
\]

where

\[
s_j=W_j(t_0-t_j)\to-\infty.
\]

Thus along the prelimit ancient horizon the tracked local region starts with vanishing critical velocity mass but ends with a fixed positive amount on the compact terminal branch.

---

## 3. Exact local L3 identity

Use a generalized Galilean/moving frame so that `V` satisfies Navier--Stokes with a modified pressure `Pi` and no physically relevant uniform acceleration term.

For smooth divergence-free `V`, set

\[
\Phi(V)=\frac{|V|^3}{3}.
\]

Dotting the velocity equation with `|V|V` gives the exact identity

\[
\boxed{
\begin{aligned}
\partial_s\Phi
+\nabla\cdot\Big[
&\Phi V
+\Pi|V|V
-\nu\nabla\Phi
\Big]
={}&
\Pi V\cdot\nabla|V|\\
&-\nu|V|
\left(|\nabla V|^2+|\nabla|V||^2\right).
\end{aligned}
}
\]

The viscous interior term is nonpositive.

---

## 4. Moving-cutoff critical-mass budget

Let `chi` be a smooth cutoff supported in a parent ball and equal to one on the terminal core ball.  In the already chosen moving frame, define

\[
M_3(s)=\int\chi\,\Phi(V)dy.
\]

Then

\[
\boxed{
\frac{dM_3}{ds}
+\nu D_3
=\mathcal P_3+\mathcal F_3,
}
\]

where

\[
D_3
=\int\chi|V|
\left(|\nabla V|^2+|\nabla|V||^2\right)dy
\ge0,
\]

\[
\boxed{
\mathcal P_3
=\int\chi\,\Pi V\cdot\nabla|V|dy
}
\]

is the interior pressure-work channel, and

\[
\boxed{
\mathcal F_3
=\int
\left[
\Phi V+
\Pi|V|V-
\nu\nabla\Phi
\right]\cdot\nabla\chi\,dy
}
\]

is the shell channel containing advective, pressure, and viscous flux across the observation boundary.

All terms are scale critical under Navier--Stokes scaling when the cutoff radius is fixed in normalized coordinates.

---

## 5. Necessary order-one influx

Suppose an earlier normalized slice has

\[
M_3(s_-)=o(1)
\]

while the compact terminal core gives

\[
M_3(0)\ge m_*>0.
\]

Integrating the exact balance gives

\[
\boxed{
\int_{s_-}^{0}\mathcal P_3ds
+
\int_{s_-}^{0}\mathcal F_3ds
\ge
m_*-o(1),
}
\]

because the viscous interior contribution is dissipative.

Hence, after taking a sufficiently advanced subsequence,

\[
\boxed{
\left|\int\mathcal P_3ds\right|
\ge\frac{m_*}{4}
\quad\text{or}\quad
\left|\int\mathcal F_3ds\right|
\ge\frac{m_*}{4}
}
\]

up to harmless sign bookkeeping if the two channels partially cancel.

Thus critical mass escape cannot return to the terminal core for free.

---

## 6. Relation to the ancient Liouville gate

If the critical `L3` mass remains globally tight along a backward sequence, the Albritton--Barker Liouville theorem is the external rigidity gate.

If tightness fails, the present identity says that any nontrivial terminal core must be fed through

\[
\boxed{
\text{critical shell influx}
\quad\text{or}\quad
\text{interior pressure work}.
}
\]

Therefore the ancient route becomes

\[
\boxed{
\text{backward L3 tightness}
\Rightarrow\text{Liouville},
}

or

\[
\boxed{
\text{L3 escape}
\Rightarrow
\text{shell/pressure transport cost}.
}
\]

---

## 7. DSD interpretation

The critical mass that is outside every fixed backward observation window must cross a finite parent boundary before it can contribute to the terminal dangerous core.

The corresponding DSD state is

\[
\boxed{
(M_3,\mathcal F_3,\mathcal P_3,D_3).
}
\]

The terminal nontriviality is not inferred from a point value alone: on the bounded compact branch it is promoted to a fixed local critical mass by vorticity Holder thickness and the local curl-to-velocity bridge.

---

## 8. Active next target

The remaining task is to intersect the two order-one influx channels with existing gates:

1. control `P3` by the pressure-Hessian / pressure-difference / local-energy channels;
2. decompose `F3` by coarea across nested parent radii and show persistent inward critical flux forces either repeated shell occupancy, large pressure transport, or a finite-energy/strain budget cost.

Status: **ANCIENT L3 ESCAPE TYPED INTO CRITICAL SHELL OR PRESSURE INFLUX / INFLUX EXHAUSTION OPEN**.
