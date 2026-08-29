# DSD M5-272 — Residual / Homogeneity-Tangent Pairing and Nonlinear-Pressure Firewall

Date: 2026-08-30

Parent: `DSD_M5_271_RESIDUAL_STRESS_FORCE_CHARGE_AND_ANGULAR_MEAN_SPLIT_2026-08-30.md`

Status: **SCALE-PHASE PAIRING AUDIT / PAIRING THE CRITICAL STATIONARY RESIDUAL WITH THE LOG-DILATION TANGENT PRODUCES A STRICTLY NEGATIVE VISCOUS LOG-AVERAGE `-nu ||Phi_y||_2^2` / HOWEVER THE CONVECTIVE TERM RETAINS AN EXPLICIT RADIAL/TANGENTIAL CUBIC CORRELATION AND THE PRESSURE TERM REDUCES TO THE NONVANISHING MEAN `⟨∫Pi Phi_(r,y)⟩` / THEREFORE THE RESIDUAL-HOMOGENEITY PAIRING IS NOT A SIGN-DEFINITE LYAPUNOV FUNCTIONAL AT ARBITRARY CRITICAL AMPLITUDE / IF THE FULL PAIRING IS SMALL OR ZERO, THE NONVISCOUS TERMS MUST PAY THE POSITIVE SCALE-PHASE VISCOSITY; IF IT IS LARGE, THAT IS A SEPARATE RESIDUAL-TANGENT WORK CHANNEL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Critical tail and homogeneity tangent

Write

\[
T(x)=r^{-1}\Phi(y,\theta),
\qquad
y=\log r,
\]

and

\[
P(x)=r^{-2}\Pi(y,\theta).
\]

The scale-homogeneity defect is

\[
\boxed{
\mathcal H_T
:=T+x\cdot\nabla T
=r^{-1}\Phi_y.
}
\]

M5-219/M5-224 give a positive critical scale-phase action on the surviving aperiodic/minimal corridor, so `Phi_y` is not identically zero there.

The residual is

\[
F_T
=\nu\Delta T-(T\cdot\nabla)T-\nabla P
=r^{-3}\mathcal R(y,\theta).
\]

---

## 2. Scale-invariant pairing

The Euclidean product `F_T . H_T` has degree `-4` and its shell integral has degree `-1`.

The natural log-scale-invariant pairing therefore inserts one factor of `r`:

\[
\int r F_T\cdot\mathcal H_T\,dx.
\]

Since

\[
dx=r^3dyd\theta,
\]

this becomes exactly

\[
\boxed{
\mathscr P_H
:=
\left\langle
\int_{S^2}
\mathcal R(y,\theta)\cdot\Phi_y(y,\theta)d\theta
\right\rangle_y.
}
\]

The brackets denote a recurrent/invariant log-radius mean.

---

## 3. Viscous coefficient in log coordinates

For each Cartesian component of `T`,

\[
\boxed{
\Delta T
=r^{-3}
\left(
\Phi_{yy}-\Phi_y+\Delta_{S^2}\Phi
\right).
}
\]

This is the same componentwise formula used in M5-220. The vector spherical connection is already encoded by treating the Cartesian components as scalar functions on `S2`.

Hence the viscous contribution to `P_H` is

\[
\nu\left\langle
\int
(\Phi_{yy}-\Phi_y+\Delta_S\Phi)\cdot\Phi_y
\right\rangle.
\]

Now

\[
\int\Phi_{yy}\cdot\Phi_y
=\frac12\frac d{dy}\int|\Phi_y|^2,
\]

and

\[
\int\Delta_S\Phi\cdot\Phi_y
=-\frac12\frac d{dy}\int|\nabla_S\Phi|^2.
\]

Both total `y` derivatives vanish in any bounded recurrent invariant mean.

Therefore

\[
\boxed{
\mathscr P_H^{vis}
=-\nu
\left\langle
\int_{S^2}|\Phi_y|^2d\theta
\right\rangle.
}
\]

This is an exact strict negative scale-phase viscosity whenever the tail is genuinely nonhomogeneous.

---

## 4. Spherical decomposition and incompressibility

Write

\[
\Phi=\phi\,\theta+v,
\]

where

\[
\phi=\Phi_r
\]

and `v` is tangent to `S2`.

For

\[
T=r^{-1}(\phi\theta+v),
\]

the divergence-free condition is

\[
\boxed{
\phi_y+\phi+\operatorname{div}_{S^2}v=0.
}
\]

Differentiating in `y`,

\[
\boxed{
\phi_{yy}+\phi_y+\operatorname{div}_{S^2}v_y=0.
}
\]

These identities will be used only for exact pressure simplification, not to impose a sign on the nonlinear term.

---

## 5. Exact pressure pairing

The pressure gradient is

\[
\nabla P
=r^{-3}
\left[
(\Pi_y-2\Pi)\theta
+\nabla_S\Pi
\right].
\]

Thus the pressure contribution is

\[
\mathscr P_H^p
=-\left\langle
\int
\left[
(\Pi_y-2\Pi)\phi_y
+\nabla_S\Pi\cdot v_y
\right]
\right\rangle.
\]

Integrate the angular-gradient term by parts:

\[
-\int\nabla_S\Pi\cdot v_y
=
\int\Pi\operatorname{div}_S v_y
=-\int\Pi(\phi_{yy}+\phi_y).
\]

Therefore, at each `y`,

\[
\begin{aligned}
\mathscr p(y)
&:=-\int
\left[
(\Pi_y-2\Pi)\phi_y
+\nabla_S\Pi\cdot v_y
\right]\\
&=
-\frac d{dy}
\int\Pi\phi_y
+
\int\Pi\phi_y.
\end{aligned}
\]

The total derivative vanishes in recurrent average. Hence

\[
\boxed{
\mathscr P_H^p
=
\left\langle
\int_{S^2}\Pi\,\phi_y\,d\theta
\right\rangle.
}
\]

This term has no universal sign.

Zero spherical mass flux gives only an angular-mean constraint on `phi`; it does not cancel the correlation `Pi phi_y`.

---

## 6. Exact convective coefficient

Use the embedded-sphere derivative `D_v^E` along the tangential vector `v`.

Since

\[
\partial_r(r^{-1}\Phi)
=r^{-2}(\Phi_y-\Phi),
\]

one has the exact coefficient formula

\[
\boxed{
(T\cdot\nabla)T
=r^{-3}
\left[
\phi(\Phi_y-\Phi)
+D_v^E\Phi
\right].
}
\]

Therefore the convective contribution is

\[
\boxed{
\mathscr P_H^{nl}
=-\left\langle
\int_{S^2}
\left[
\phi(\Phi_y-\Phi)
+D_v^E\Phi
\right]\cdot\Phi_y
\,d\theta
\right\rangle.
}
\]

Equivalently,

\[
\mathscr P_H^{nl}
=
-\left\langle\int\phi|\Phi_y|^2\right\rangle
+\left\langle\int\phi\Phi\cdot\Phi_y\right\rangle
-\left\langle\int D_v^E\Phi\cdot\Phi_y\right\rangle.
\]

No term in this expression has a fixed sign at arbitrary critical amplitude.

Tangential integration by parts moves the final term between `v`, `Phi`, and `Phi_y`, but produces divergence/radial correlations through

\[
\operatorname{div}_S v=-\phi_y-\phi.
\]

It does **not** vanish generically.

---

## 7. Exact averaged pairing identity

Combining Sections 3, 5, and 6 gives

\[
\boxed{
\mathscr P_H
=
-\nu\mathscr D_{phase}
+\mathscr C_{nl}
+\mathscr C_p,
}
\]

where

\[
\boxed{
\mathscr D_{phase}
:=
\left\langle
\int_{S^2}|\Phi_y|^2d\theta
\right\rangle>0
}
\]

on a genuinely nonhomogeneous minimal tail,

\[
\boxed{
\mathscr C_{nl}
:=-\left\langle
\int
\left[
\phi(\Phi_y-\Phi)+D_v^E\Phi
\right]\cdot\Phi_y
\right\rangle,
}
\]

and

\[
\boxed{
\mathscr C_p
:=
\left\langle
\int\Pi\phi_y
\right\rangle.
}
\]

This is the correct arbitrary-amplitude residual/homogeneity identity.

---

## 8. Why it is not a Lyapunov sign

The viscous part alone gives

\[
-\nu\mathscr D_{phase}<0.
\]

But neither

\[
\mathscr C_{nl}=0
\]

nor

\[
\mathscr C_p=0
\]

follows from incompressibility, zero spherical flux, recurrence, or pressure determinacy.

Therefore

\[
\boxed{
\mathscr P_H
\le-\nu\mathscr D_{phase}
}
\]

is **not** established.

Likewise one cannot declare

\[
\mathscr P_H<0
\]

without an additional structural inequality controlling the nonlinear and pressure correlations.

This is the scale-phase analogue of the pressure/radial-transport firewall in M5-231.

---

## 9. A valid finite payment split

The exact identity does yield a useful trichotomy.

Fix a phase-action floor

\[
\mathscr D_{phase}\ge d_{ph}>0
\]

from the compact nonhomogeneous tail hull.

Then either the full residual/tangent work is visibly negative,

\[
\boxed{
\mathscr P_H
\le-\frac\nu3d_{ph},
}
\]

or the nonviscous correlations must compensate at least a fixed portion of the viscous scale-phase loss:

\[
\boxed{
\mathscr C_{nl}
\ge\frac\nu3d_{ph}
\quad\lor\quad
\mathscr C_p
\ge\frac\nu3d_{ph}.
}
\]

The numerical fraction `1/3` is only a convenient finite partition.

Thus a residual-active nonhomogeneous tail must carry at least one of:

1. **negative residual/dilation work**;
2. **positive critical nonlinear scale-phase transfer**;
3. **positive pressure/radial-phase correlation**.

---

## 10. Relation to the M5-271 moment split

M5-271 decomposes `R` into its spherical force/source mode and angular mean-free mode.

M5-272 decomposes the same residual by its pairing against the dilation tangent `Phi_y`.

These decompositions are complementary:

- M5-271 asks **where in spherical harmonic rank** the residual lives;
- M5-272 asks **whether it does signed work against scale-phase motion**.

A residual can be large in the M5-271 norm while almost orthogonal to `Phi_y`; therefore no lower bound for `|P_H|` follows from the residual gap alone.

Conversely a large signed `P_H` is stronger information than a generic residual norm.

---

## 11. Updated frontier

The residual-active realized tail is now constrained by both

\[
\boxed{
F_{charge}\lor A_{res}
}
\]

and

\[
\boxed{
W_{dil}^{-}
\lor
C_{nl}^{+}
\lor
C_p^{+}.
}
\]

The remaining useful target is not another scalar lower bound. It is an inequality that couples these two decompositions, for example:

- an angular-mean-free residual estimate that bounds `C_p` by the angular derivative payer;
- a force-charge identity that controls the radial part of `C_nl`;
- or a weighted energy identity that converts `W_dil^-` into a genuine state-function decrement.

Without such a coupling, the critical residual can rotate between norm, force, nonlinear, and pressure channels without violating a known finite budget.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
