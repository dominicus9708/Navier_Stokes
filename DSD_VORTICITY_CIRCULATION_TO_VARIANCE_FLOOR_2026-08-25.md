# DSD Vorticity-Circulation -> Moving Variance Floor

Date: 2026-08-25

Status: **EXPLICIT POSITIVE LOCAL VELOCITY-VARIANCE FLOOR DERIVED FROM THE NORMALIZED VORTICITY CORE / COMPENSATED REFERENCE VARIANCE CANNOT DEGENERATE / ABSOLUTE-ACTION TURNOVER NOW HAS A UNIFORM FIXED COST / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The absolute-action compensated-variance gate left one quantitative issue: a turnover event pays a fixed fraction of the compensated reference variance

\[
\mathcal W_-.
\]

To sum or compare such event costs, one must know that `W_-` cannot collapse to zero along the coherent recurrent core.

A direct circulation argument provides this lower bound without any inverse Poincare inequality.

## 2. Directed vorticity floor near the normalized maximum

Work in the continuously dynamic first-hitting normalization, so along the coherent tracked maximum core

\[
\boxed{\|\Omega(s)\|_\infty=1.}
\]

Choose a maximum point `X(s)` and define

\[
e(s):=\Omega(X(s),s).
\]

Thus `|e|=1`.

The restart-analyticity Cauchy bound gives

\[
\|\nabla\Omega\|_\infty
\le
K_{1,+}
\le
\frac{M_0}{\rho_0}.
\]

Define

\[
\boxed{
\varrho_*
:=
\min\left\{
R_Z,
\frac{\rho_0}{2M_0}
\right\}.
}
\]

For every `|y-X(s)|<=varrho_*`,

\[
\begin{aligned}
e\cdot\Omega(y,s)
&\ge
1-|\Omega(y,s)-\Omega(X(s),s)|\\
&\ge
1-K_{1,+}|y-X(s)|\\
&\ge\frac12.
\end{aligned}
\]

Hence

\[
\boxed{
e\cdot\Omega\ge\frac12
\quad\text{on }B_{\varrho_*}(X(s)).}
\]

## 3. Stokes circulation on transverse disks

Inside this ball choose a cylinder with axis `e`, radial radius

\[
a:=\frac{\varrho_*}{2}
\]

and half-height

\[
h:=\frac{\varrho_*}{2}.
\]

It lies inside `B_varrho*` because

\[
\sqrt{a^2+h^2}=\frac{\varrho_*}{\sqrt2}<\varrho_*.
\]

For each axial coordinate `z in [-h,h]` and every transverse circle of radius `0<r<=a`, Stokes gives

\[
\oint_{C_r(z)}U\cdot\tau\,d\ell
=
\int_{D_r(z)}\Omega\cdot e\,dA
\ge
\frac12\pi r^2.
\]

For any constant vector `c`,

\[
\oint_{C_r(z)}c\cdot\tau\,d\ell=0,
\]

so the same circulation is obtained from `U-c`.

By Cauchy-Schwarz on the circle,

\[
\left(\frac12\pi r^2\right)^2
\le
(2\pi r)
\int_{C_r(z)}|U-c|^2d\ell.
\]

Therefore

\[
\boxed{
\int_{C_r(z)}|U-c|^2d\ell
\ge
\frac\pi8r^3.
}
\]

## 4. Integrate the circles to a cylinder variance floor

Integrate in `r`:

\[
\int_{D_a(z)}|U-c|^2dA
\ge
\int_0^a\frac\pi8r^3dr
=
\frac\pi{32}a^4.
\]

Then integrate in the axial direction over length `2h`:

\[
\int_{\mathcal C}|U-c|^2dy
\ge
\frac{\pi h}{16}a^4.
\]

With `a=h=varrho*/2`,

\[
\boxed{
\int_{\mathcal C}|U-c|^2dy
\ge
\frac\pi{512}\varrho_*^5.
}
\]

Choose

\[
c=(U)_{B_{R_Z}(X(s))}.
\]

Since the cylinder lies inside the moving tightness ball,

\[
\boxed{
V_{R_Z}(s)
:=
\int_{B_{R_Z}(X(s))}
|U-(U)_{B_{R_Z}}|^2dy
\ge
\frac\pi{512}\varrho_*^5.
}
\]

Status: **PROVED.**

## 5. Pass to scale-compensated variance

Recall

\[
\mathcal W(s)=e^{-A(s)}V_{R_Z}(s),
\qquad
A(s)=\int_{s_0}^sa(\sigma)d\sigma.
\]

On a record first-hitting stage,

\[
a\ge0,
\qquad
0\le A(s)\le\log q.
\]

Therefore

\[
e^{-A(s)}\ge q^{-1}.
\]

Hence throughout every coherent tracked stage,

\[
\boxed{
\mathcal W(s)
\ge
\mathcal W_{core,-}
:=
\frac\pi{512q}\varrho_*^5.
}
\]

In particular,

\[
\boxed{
\mathcal W_-
\ge
\frac\pi{512q}
\min\left\{
R_Z,
\frac{\rho_0}{2M_0}
\right\}^5.
}
\]

Thus the reference variance cannot degenerate along the coherent normalized core.

## 6. Uniform fixed cost of absolute-action turnover

The preceding absolute-action gate showed:

- if `b_c>1`, then
  \[
  \mathscr B_{I_j}>\mathcal W_-;
  \]
- if `v_c>1`, then
  \[
  \mathscr B_{I_j}+\mathscr D_{I_j}>\frac12\mathcal W_-.
  \]

Consequently every `T_abs(R_Z)` event carries the uniform normalized cost

\[
\boxed{
\mathscr B_{I_j}+\mathscr D_{I_j}
>
\mathcal A_{turn,-}
:=
\frac\pi{1024q}
\varrho_*^5.
}
\]

Equivalently,

\[
\boxed{
\mathcal A_{turn,-}
=
\frac\pi{1024q}
\min\left\{
R_Z,
\frac{\rho_0}{2M_0}
\right\}^5
>0.
}
\]

Status: **PROVED on the coherent tracked-core branch.**

If the maximum/core center cannot be tracked so that the same moving ball carries this construction, that failure is center/material replacement turnover rather than a failure of the circulation estimate.

## 7. A persistent local viscous-action rate

Payne-Weinberger and the variance floor also give, at every coherent core time,

\[
E=e^{-A}D
\ge
\frac{\pi^2}{4R_Z^2}\mathcal W
\ge
\frac{\pi^3}{2048q}
\frac{\varrho_*^5}{R_Z^2}.
\]

Therefore the compensated local viscous action has the pointwise-in-dynamic-time floor

\[
\boxed{
\nu E
\ge
\frac{\nu\pi^3}{2048q}
\frac{\varrho_*^5}{R_Z^2}.
}
\]

This is a persistent core cost, not only an event cost.

It does not by itself contradict bounded global enstrophy, but it prevents arbitrarily cheap long coherent stages.

## 8. Turnover routing

The absolute boundary action `B` is the sum of the physical moving-boundary mechanisms already present in the exact relative-variance ledger:

\[
T_{mat},
\quad
T_{rad},
\quad
T_{vis},
\quad
T_{pres}.
\]

Thus an absolute-action turnover event must route by finite pigeonhole to at least one of

\[
\boxed{
\text{material/center crossing},
\quad
\text{radial export/contraction},
\quad
\text{viscous boundary leakage},
\quad
\text{pressure work},
\quad
\text{interior viscous action}.
}
\]

The local cost can no longer disappear through degeneration of the velocity-variance normalization.

## 9. Updated frontier

The previous unresolved sentence

\[
\text{“perhaps }\mathcal W_-\to0\text{ along turnover events”}
\]

is removed on the coherent active-core branch.

The remaining long-time question is now topological/dynamical rather than local-normalization based:

\[
\boxed{
\text{can the fixed positive turnover action recur indefinitely
without entering the existing viscous/H/projective ledgers
or permanent export to similarity infinity?}
}
\]

This matches the already isolated global export/escaping-tail frontier.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]