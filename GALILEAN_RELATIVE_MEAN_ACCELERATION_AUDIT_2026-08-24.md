# Galilean-Invariant Relative-Mean Acceleration Audit — 2026-08-24

Status: **DRIFT-GAUGE GAP SHARPENED / LARGE CONSTANT DRIFT REMOVED EXACTLY / TIME-DEPENDENT DRIFT REDUCED TO RELATIVE FLUX, PRESSURE, AND VISCOUS BOUNDARY ACTION / GLOBAL REGULARITY NOT PROVED.**

The anti-proof audit found that the absolute local kinetic-energy Morrey quantity

\[
\rho^{-1}\int_{B_\rho}|U|^2
\]

is not Galilean invariant. A very large almost-constant local drift can make it large without producing strain, vorticity, or a genuine turnover event.

Therefore absolute Morrey failure must not automatically be classified as `T`.

This note replaces that unsafe interpretation by an exact moving-relative-mean calculation.

---

## 1. Moving weighted mean

Let

\[
\phi_a(x,t)
=\Phi\!\left(\frac{x-a(t)}\ell\right)
\]

with fixed scale `ell` and fixed smooth compactly supported profile `Phi`.

Set

\[
M_\phi=\int\phi_a dx,
\]

\[
m(t)
=\frac1{M_\phi}\int\phi_a u\,dx,
\]

and choose the observation path self-consistently by

\[
\boxed{\dot a(t)=m(t).}
\]

Define the relative velocity

\[
\boxed{v=u-m.}
\]

Then

\[
\int\phi_a v\,dx=0.
\]

The frame follows the local weighted drift rather than declaring that drift to be turnover.

---

## 2. Exact acceleration identity

Because

\[
\phi_t=-m\cdot\nabla\phi,
\]

and

\[
u_t+(u\cdot\nabla)u+\nabla p=\nu\Delta u,
\]

differentiate the weighted mean:

\[
M_\phi\dot m
=\int \phi_tu+\int\phi u_t.
\]

The transport terms combine as

\[
\int[-m\cdot\nabla\phi]u
-\int\phi(u\cdot\nabla)u
=
\int u\,(u-m)\cdot\nabla\phi.
\]

Writing `u=m+v`, the part proportional to `m` vanishes because

\[
\int v\cdot\nabla\phi
=
\int u\cdot\nabla\phi
-m\cdot\int\nabla\phi
=0.
\]

Pressure and viscosity are integrated by parts. Therefore for any scalar gauge `c(t)`,

\[
\boxed{
M_\phi\dot m
=
\int (v\otimes v)\nabla\phi\,dx
+
\int (p-c)\nabla\phi\,dx
+
\nu\int v\,\Delta\phi\,dx.
}
\]

This identity is exact.

Most importantly, **no term proportional to `|m|` appears**.

A huge constant Galilean drift therefore has zero acceleration cost.

---

## 3. Scale-normalized acceleration bound

For a cutoff of radius `ell`,

\[
|\nabla\phi|\lesssim \ell^{-1},
\qquad
|\Delta\phi|\lesssim \ell^{-2},
\qquad
M_\phi\asymp \ell^3.
\]

Let

\[
V_\phi=\frac12\int\phi|v|^2,
\]

and let the shell pressure oscillation norm be

\[
P_\phi
:=
\|p-c\|_{L^2(\operatorname{supp}\nabla\phi)}.
\]

Then

\[
\boxed{
|\dot m|
\lesssim
\ell^{-4}V_{\phi,+}
+
\ell^{-5/2}P_\phi
+
\nu\ell^{-7/2}V_{\phi,+}^{1/2},
}
\]

where `V_{phi,+}` denotes a comparable relative-energy quantity on the cutoff support.

Equivalently, in a unit normalized first-hitting window,

\[
\boxed{
|m_s|
\lesssim
\mathcal C_{rel}
+
P_{osc}
+
\nu\mathcal C_{rel}^{1/2}
}
\]

up to fixed cutoff constants.

Thus time-dependent drift can become violent only if relative kinetic variance, pressure oscillation, or viscous boundary activity becomes large.

---

## 4. Exact accelerated-frame Navier--Stokes equation

Set

\[
z=x-a(t),
\]

and define

\[
\widetilde u(z,t)
=u(z+a(t),t)-m(t).
\]

Then

\[
\widetilde\omega(z,t)=\omega(z+a(t),t),
\]

so vorticity is unchanged by the frame.

A direct calculation gives

\[
\boxed{
\partial_t\widetilde u
+(\widetilde u\cdot\nabla)\widetilde u
+\nabla\widetilde p
=\nu\Delta\widetilde u,
}
\]

with

\[
\boxed{
\widetilde p(z,t)
=p(z+a(t),t)+\dot m(t)\cdot z.
}
\]

Thus the only price of using the self-consistent time-dependent drift frame is a spatially affine pressure term controlled by `dot m`.

The pressure Hessian is unaffected:

\[
\boxed{
\nabla_z^2\widetilde p
=\nabla_x^2p(z+a(t),t).
}
\]

Hence all strain, vorticity, pressure-Hessian, and projective calculations are invariant under this frame.

---

## 5. Relative Campanato becomes actual local energy in the drift frame

Let

\[
\mathcal C_\rho(a,t)
=
\rho^{-1}
\int_{B_\rho(a(t))}
|u-(u)_{B_\rho(a(t))}|^2dx.
\]

Because subtracting `m(t)` changes only the local constant velocity,

\[
\mathcal C_\rho(a,t)
\]

is identical in the accelerated frame.

Take the mean-defining scale `ell` as a fixed normalized core scale. If

\[
\sup_{\rho\in[\ell,R]}
\mathcal C_\rho(a,t)
\le C_*,
\]

then neighboring-ball mean estimates give

\[
|(u)_{B_\rho(a)}-m(t)|
\le
C C_*^{1/2}\ell^{-1}
\]

for every fixed `rho` in the range, after a finite/dyadic telescoping from the mean-defining scale.

Consequently

\[
\boxed{
\int_{B_\rho(0)}|\widetilde u(z,t)|^2dz
\le
C(\rho,\ell,C_*).
}
\]

Thus relative Campanato control supplies the local velocity-energy bound required for compactness **after the correct drift gauge is chosen**.

A large absolute local mean no longer creates a fake compactness failure.

---

## 6. Drift-coherence dichotomy

The exact acceleration identity yields the safe replacement for the old absolute-Morrey dichotomy.

### A. Drift-coherent corridor

If on every fixed compactness cylinder

\[
\mathcal C_{rel}\le C_*,
\qquad
P_{osc}\le P_*,
\]

and the viscous shell term is bounded, then

\[
\boxed{|\dot m|\le A_*<\infty.}
\]

The affine pressure in the moving frame is bounded on every fixed spatial ball by

\[
|\dot m\cdot z|\le A_*R.
\]

Therefore it does not destroy local suitable compactness.

### B. Drift-incoherent corridor

If `dot m` is not bounded, the exact identity forces at least one of

\[
\boxed{
\text{relative-energy escalation}
\lor
\text{pressure-work escalation}
\lor
\text{viscous boundary escalation}.
}
\]

These are precisely channels already present in the moving relative-variance turnover ledger.

Thus a large time-dependent drift is not silently relabeled as turnover; its **cause** is explicitly identified first.

---

## 7. Core-tracking issue remains separate

The self-consistent mean path `a(t)` need not coincide with the maximum-vorticity path.

This must not be hidden.

If the intense-vorticity core remains within a fixed normalized distance of `a(t)`, the moving frame preserves the nontrivial core in a fixed compact set and may be used for ancient extraction.

If instead the vorticity core repeatedly leaves every fixed neighborhood of the relative-mean path while the next first-hitting core remains nested around the singular point, then a fixed amount of core vorticity/material must cross the moving observation boundary or the active core must be replaced.

That is a genuine

\[
\boxed{T_{mat}/T_{core-replacement}}
\]

problem, not a Galilean-gauge problem.

A quantitative core-to-mean-path tracking lemma is still required before declaring the drift gauge completely closed.

---

## 8. Correct compactness frontier

The unsafe statement

\[
\text{absolute Morrey fails}\Rightarrow T
\]

should be replaced by

\[
\boxed{
\begin{aligned}
&\text{relative Campanato bounded}
+
\text{drift acceleration bounded}
+
\text{core tracks mean path}
\\
&\qquad\Longrightarrow
\text{Galilean/accelerated-frame local compactness},
\\[1mm]
&\text{otherwise}
\Longrightarrow
\text{relative-energy / pressure / viscous / material-core turnover frontier}.
\end{aligned}
}
\]

This formulation is Galilean invariant and does not delete a legitimate NSE branch merely because it carries a large coherent transport velocity.

---

## 9. Next theorem target

The remaining quantitative drift lemma is now sharply stated:

\[
\boxed{
\text{on a non-T first-hitting stage, the intense-vorticity core stays within }O(1)
\text{ normalized distance of the self-consistent relative-mean path.}
}
\]

If this fails, prove a fixed lower bound on the material crossing/core-replacement action in `MOVING_RELATIVE_VARIANCE_TURNOVER_LEDGER_2026-08-23.md`.

Once this is established, absolute Morrey can be removed from the compactness logic entirely and replaced by the Galilean-invariant relative Campanato corridor.

Status: **LARGE CONSTANT DRIFT IS NOW EXACTLY REMOVED RATHER THAN MISCLASSIFIED. THE TIME-DEPENDENT DRIFT ACCELERATION IS GENERATED ONLY BY RELATIVE QUADRATIC FLUX, PRESSURE OSCILLATION, AND VISCOUS BOUNDARY ACTION. THE TRUE REMAINING GAP IS CORE TRACKING RELATIVE TO THE SELF-CONSISTENT MEAN PATH. GLOBAL REGULARITY REMAINS UNPROVED.**