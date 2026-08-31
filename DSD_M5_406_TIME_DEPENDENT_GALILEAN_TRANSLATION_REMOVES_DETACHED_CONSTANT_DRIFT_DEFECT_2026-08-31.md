# DSD M5-406 — Time-dependent translating frame removes the detached constant-drift defect

Date: 2026-08-31

Status: **SCOPE CORRECTION TO M5-405 / THE SPATIAL CONSTANT `c(t)` ARISING FROM HOMOGENEOUS LORENTZ--SOBOLEV IS NOT A NEW DYNAMIC/REALIZATION T BRANCH / A TIME-DEPENDENT SPATIAL TRANSLATION WITH VELOCITY `a'(t)=c(t)` REMOVES THAT CONSTANT, AND THE RESULTING ACCELERATION IS A PURE GRADIENT THAT IS ABSORBED INTO THE PRESSURE / CRITICAL LORENTZ NORMS ARE TRANSLATION INVARIANT, SO THE BOUNDED-SHELL DETACHED CORRIDOR ENTERS THE ACTUAL WEAK-L3 ANCIENT CLASS AFTER THIS GAUGE FIX / THEREFORE THE M5-405 DICHOTOMY SHARPENS TO `DETACHED -> SHELL-H/REMOTE OR LIOUVILLE CONTRADICTION` WITHOUT AN INDEPENDENT CONSTANT-DRIFT EXIT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-405 proves from the detached shell bound

\[
\sup_{t<0,R}R\int_{A_R}|\nabla u|^2<\infty
\]

that, for every time,

\[
u(t)-c(t)\in L^{3,\infty}(\mathbb R^3)
\]

for a spatial constant vector `c(t)`.

It conservatively left open a possible `T_drift/realization` if those constants could not be put into one coherent ancient Navier--Stokes frame.

For a spatially uniform velocity drift this concern is unnecessary: Navier--Stokes is invariant under an arbitrary time-dependent translation once the corresponding uniform acceleration is absorbed into the pressure.

---

## 2. Time-dependent translating coordinates

Let

\[
a:(-\infty,0]\to\mathbb R^3
\]

be locally absolutely continuous and define

\[
y=x-a(t).
\]

For a sufficiently smooth `a`, set

\[
\boxed{
v(y,t)
:=
u(y+a(t),t)-\dot a(t).
}
\]

Then

\[
\nabla_yv=\nabla_xu,
\qquad
\Delta_yv=\Delta_xu,
\qquad
\nabla_y\cdot v=0.
\]

A direct calculation gives

\[
\partial_tv+(v\cdot\nabla)v
=
\partial_tu+(u\cdot\nabla)u-\ddot a(t).
\]

If

\[
\partial_tu+(u\cdot\nabla)u
=-\nabla p+\nu\Delta u,
\]

then

\[
\partial_tv+(v\cdot\nabla)v
=-\nabla_y\widetilde p+\nu\Delta v,
\]

where

\[
\boxed{
\widetilde p(y,t)
=
p(y+a(t),t)+\ddot a(t)\cdot y.
}
\]

Thus the uniform acceleration is exactly a pressure gradient.

The transformed velocity solves the standard unforced Navier--Stokes equation.

---

## 3. Apply the gauge to the Sobolev constant

On the M5-405 bounded-shell corridor, homogeneous Lorentz--Sobolev gives a unique spatial constant modulo the decaying class such that

\[
\boxed{
u(t)-c(t)\in L^{3,\infty}.}
\]

Choose `a(t)` with

\[
\dot a(t)=c(t)
\]

and normalize

\[
a(0)=0.
\]

Then the translated velocity is

\[
v(y,t)
=
u(y+a(t),t)-c(t).
\]

Spatial translation preserves Lorentz norms, hence

\[
\boxed{
\|v(t)\|_{L^{3,\infty}}
=
\|u(t)-c(t)\|_{L^{3,\infty}}
\le M_*.
}
\]

The bound is uniform on the complete ancient bounded-shell corridor.

---

## 4. Low regularity of `c(t)` is not a structural obstruction

The detached solution is smooth in space-time, while the Sobolev representative `c(t)` can be chosen canonically, for example through the unique constant for which the Lorentz representative belongs to `L^{3,infinity}`.

For the projected Navier--Stokes equation, a spatially uniform time derivative is a pure gradient and is annihilated by the Leray projection.

Therefore only local integrability of `c(t)` is structurally needed to define the translating path

\[
a(t)=\int_0^t c(s)ds.
\]

Any additional regularization can be performed on finite time slabs and passed in the pressure distribution.

There is no physical flux, strain, or material turnover associated solely with this uniform drift gauge.

---

## 5. Vorticity and shell quantities are unchanged

The transformation preserves the velocity gradient and vorticity up to spatial translation:

\[
\boxed{
\nabla v(y,t)=\nabla u(y+a(t),t),
\qquad
\omega_v(y,t)=\omega_u(y+a(t),t).
}
\]

Therefore

- the nonzero detached vorticity witness is retained, after translating its spatial location;
- the shell-H1 versus bounded-shell dichotomy is unchanged modulo recentering;
- no derivative action is created or erased by the gauge.

The coordinate center may move, but this is a chosen reference-frame translation, not the first-hitting physical center-turnover event classified in M5-399.

---

## 6. Terminal condition is unchanged by choosing `a(0)=0`

Because

\[
a(0)=0,
\]

the terminal transformed field is

\[
v(y,0)=u(y,0)-c(0).
\]

By construction

\[
v(0)\in L^{3,\infty}.
\]

As in M5-276/405,

\[
L^{3,\infty}
\hookrightarrow
\dot B^{-1}_{\infty,\infty}
\]

and

\[
v(0)(\lambda\cdot)\to0
\quad\text{in }\mathcal D'
\]

as `lambda->infinity`.

Hence

\[
\boxed{v(0)\in\mathbb B.}
\]

Spatial translations at negative times do not change the uniform weak-critical norm used in the backward-sequence hypothesis.

---

## 7. Consequence for M5-405

The previous conservative split

\[
A_{detached}
\Longrightarrow
H_{shell/remote}
\lor
T_{drift/realization}
\lor
\bot
\]

sharpens to

\[
\boxed{
A_{detached}
\Longrightarrow
H_{shell/remote}
\lor
\bot.
}
\]

Here the contradiction is the Albritton--Barker weak-`L3` ancient Liouville endpoint on the uniformly bounded-shell branch.

There is no independent constant-velocity realization defect.

---

## 8. Firewall: this does not remove affine gradient

Only a spatially constant velocity is gauge.

A nonzero affine field

\[
Ax
\]

cannot be removed by a translating frame because

\[
\nabla(Ax)=A\ne0.
\]

Such a profile is already routed by M5-403--404 to palinstrophy/enstrophy/remote H.

Similarly, projective rotation of a material/vorticity axis is not a Galilean gauge.

Thus M5-406 removes only the harmless uniform-drift ambiguity.

---

## 9. DSD audit

### Standard symmetry

Time-dependent spatial translation changes the pressure by a linear potential representing the frame acceleration and leaves the unforced velocity equation invariant.

### Corrected

- `c(t)` from homogeneous Sobolev is a gauge quantity;
- time variation of that constant is not a material-turnover mechanism;
- the bounded-shell detached weak-`L3` conclusion can be stated in one actual translating Navier--Stokes frame.

### Firewall

- nonconstant/affine velocity gradients are not gauge;
- physical first-hitting center displacement remains governed by M5-399;
- shell-H1 escalation remains open and routes to remote activity.

---

## 10. Updated detached frontier

Combining M5-403--406,

\[
\boxed{
A_{detached}
\Longrightarrow
H_{shell/frequency/capacity}
\lor
S_{remote}^{next}
\lor
\bot.
}
\]

The exact affine/nondecaying anti-models route to H/remote through their finite-energy prelimit transition cost, while a genuinely bounded-shell critical detached profile enters the weak-`L3` Liouville corridor.

---

## 11. Audit verdict

### REMOVED AS INDEPENDENT T

\[
\boxed{T_{constant\ drift/realization}.}
\]

### SHARPENED DICHOTOMY

\[
\boxed{
A_{detached}
\Longrightarrow
H_{shell/remote}
\lor
\text{Liouville contradiction}.
}
\]

### STILL OPEN

- shell-H1/remote recursion;
- local critical frequency/direction action;
- projective/export exits;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
