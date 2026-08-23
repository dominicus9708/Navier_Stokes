# Ancient Critical Tail: Leray Dilation Conveyor — 2026-08-24

Status: **EXACT LINEAR FAR-TAIL SCALING + HISTORICAL-REPLENISHMENT REDUCTION / GLOBAL REGULARITY NOT PROVED.**

The restricted ancient survivor can avoid the global `L^3` Liouville theorem only by carrying a backward-divergent critical velocity tail. The preceding shell analysis shows that such a tail is compatible with bounded global enstrophy and with dynamic passivity at the active core.

This note records the exact leading Leray transport of that tail and relates recurrent/DSS tail persistence to the already studied historical-recycling mechanism.

---

## 1. Leray equation and far blow-down

Let

\[
V_s+\frac12V+\frac12Y\cdot\nabla V+(V\cdot\nabla)V+\nabla\Pi=\nu\Delta V.
\]

At spatial scale `R`, define the blow-down

\[
V_R(z,s)=R V(Rz,s),
\qquad
\Pi_R(z,s)=R^2\Pi(Rz,s).
\]

Then

\[
\boxed{
\partial_sV_R
+\frac12V_R
+\frac12z\cdot\nabla V_R
+R^{-2}
\left[(V_R\cdot\nabla)V_R+\nabla\Pi_R-\nu\Delta V_R\right]
=0.
}
\]

Thus every bounded critical blow-down is asymptotically governed by

\[
\boxed{
V_s+\frac12V+\frac12Y\cdot\nabla V=0.
}
\]

This is the precise meaning of a dynamically passive far critical sector.

---

## 2. Exact dilation conveyor

The linear equation has the explicit solution operator

\[
\boxed{
V(Y,s+\Delta)
=e^{-\Delta/2}
V(e^{-\Delta/2}Y,s).
}
\]

Therefore a shell initially at radius `R` is transported to

\[
\boxed{R_+=e^{\Delta/2}R}
\]

while its velocity amplitude is multiplied by `e^{-Delta/2}`.

For an annulus `A_R={R<|Y|<2R}`, the shell `L^3` quantity is exactly invariant:

\[
\boxed{
\int_{A_{R_+}}|V(Y,s+\Delta)|^3dY
=
\int_{A_R}|V(Y,s)|^3dY.
}
\]

Hence the `1/R` critical tail is a conveyor: critical `L^3` occupancy is shifted outward rather than damped in the scale-invariant norm.

---

## 3. The annular Dirichlet critical quantity is also invariant

Let

\[
e_R(s)=\int_{A_R}|\nabla V(Y,s)|^2dY.
\]

Under the linear dilation,

\[
\nabla V(Y,s+\Delta)
=e^{-\Delta}\nabla V(e^{-\Delta/2}Y,s).
\]

Hence

\[
e_{R_+}(s+\Delta)
=e^{-\Delta/2}e_R(s).
\]

Since `R_+=e^(Delta/2)R`,

\[
\boxed{
R_+e_{R_+}(s+\Delta)
=Re_R(s).
}
\]

Thus

\[
\boxed{
J_R:=R\int_{A_R}|\nabla V|^2
}
\]

is exactly the annular critical invariant of the far linear conveyor.

This matches the previously derived necessity that a non-`L^3` ancient survivor must have a non-summable stack of critical annular derivative quantities.

---

## 4. Consequence for periodic/DSS recurrence

Suppose a Leray trajectory is exactly periodic with period `T_L`. The dilation conveyor shifts a passive shell by the factor

\[
\boxed{
\Lambda=e^{T_L/2}>1
}
\]

per period.

Therefore a periodic critical tail cannot consist of a finite set of old shells. To reproduce the same tail at the next period, the shell pattern at radius `R` must be supplied from radius `R/Lambda` one period earlier.

Equivalently, a periodic/DSS critical tail requires a logarithmic shell chain that is continually passed outward:

\[
\boxed{
\cdots\to R/\Lambda\to R\to\Lambda R\to\cdots.
}
\]

At the inner end of the passive tail this requires continual injection from the active/mesoscopic region, unless the critical stack already extends all the way into that region.

This is exactly the structural content of **historical recycling** in Leray coordinates.

---

## 5. Relation to the 2026-08-23 historical-shell reduction

The repository already obtained

\[
\boxed{
\text{historical weak-}L^3\text{ recycling}
\Longrightarrow
H_{remote}
\lor
T/\text{parent-energy turnover}.
}
\]

Therefore an exactly periodic/DSS recurrent survivor with a passive critical tail has only the following possibilities:

\[
\boxed{
\begin{aligned}
&\text{tail replenishment from smaller similarity radii}
\to H_{remote}\lor T,\\
&\text{or the tail is not dynamically passive at some scale}
\to\text{active remote-strain/pressure branch},\\
&\text{or the global periodic/DSS tail hypothesis fails}.
\end{aligned}
}
\]

This does **not** yet exclude every local recurrent core: a tail may drift to infinity and fail to recur globally while the active core is recurrent only in local topology.

---

## 6. Why the known DSS Liouville theorem does not finish the present branch

The standard locally asymptotically DSS nonexistence result for Navier--Stokes assumes a time-periodic blow-up profile in global `L^3`. The present restricted survivor is designed precisely to evade this condition by carrying a critical non-`L^3` tail.

Thus the new information here is not a direct application of the existing DSS theorem. It is the dynamical fact that the only tail capable of violating global `L^3` is transported outward by the Leray dilation and therefore requires a scale-by-scale replenishment mechanism if the **whole** state is to recur.

---

## 7. Remaining tail frontier

The final tail problem is now split into two genuinely different cases:

### A. Globally recurrent / DSS tail

The critical shell stack must replenish itself against the outward dilation conveyor. This is a historical-recycling problem and is routed to the existing `H_remote/T` machinery.

### B. Locally recurrent core + nonrecurrent escaping tail

The active Leray core may recur locally while old passive critical shells drift to infinity. A time-translation limit can then lose the tail at spatial infinity.

The remaining theorem-level target is to show that, on the no-replenishment branch, one can extract a **nontrivial core limit with bounded global `L^3`**, or another known Liouville-class bound. That requires a uniform tail-evacuation/tightness statement stronger than local compactness alone.

Status: **THE PASSIVE CRITICAL TAIL HAS AN EXACT OUTWARD LERAY DILATION CONVEYOR. SHELL `L^3` MASS AND `R TIMES ANNULAR DIRICHLET ENERGY` ARE THE CRITICAL INVARIANTS. GLOBAL PERIODIC/DSS RECURRENCE OF SUCH A TAIL REQUIRES HISTORICAL SCALE REPLENISHMENT AND THEREFORE RETURNS TO THE EXISTING `H_REMOTE/T` ROUTE. THE ONLY TAIL CASE NOT YET REDUCED IS A LOCALLY RECURRENT ACTIVE CORE WITH A NONRECURRENT PASSIVE TAIL ESCAPING TO INFINITY. GLOBAL REGULARITY REMAINS UNPROVED.**