# DSD M5-439 — Galilean-invariant velocity-variance freezing on the remote old-shell corridor

Date: 2026-09-01

Status: **THE LOCALIZATION-ARTIFACT GAP LEFT BY M5-437 IS CLOSED AT THE QUIET OLD-SHELL LEVEL / TRACK A REMOTE SOURCE ANNULUS IN THE FRAME OF ITS WEIGHTED MEAN VELOCITY AND USE THE LOCAL ENERGY IDENTITY FOR THE VELOCITY VARIANCE MODULO CONSTANTS / OUTSIDE LARGE RELATIVE AMPLITUDE, DERIVATIVE, PRESSURE, OR FRAME-TRANSPORT ACTION, THE SQUARE ROOT OF THE LOCAL VARIANCE CHANGES AT NATURAL RATE `O(R^-2)` / ONLY `O(K^-2)` OF ONE SOURCE NATURAL TIME REMAINS, WHILE M5-437 GIVES INITIAL VARIANCE SIZE `>= c nu K^2 R^(1/2)` / HENCE THE TOTAL FUTURE RELATIVE VARIANCE CHANGE IS `O(K^-2)+O(K^-4)` AND A SUFFICIENTLY REMOTE QUIET SOURCE FREEZES IN A GALILEAN-INVARIANT PHYSICAL SENSE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Let a first-hitting target at time `t_j` have natural scale `r_j`, and let a fixed-fraction remote strain source occupy a fixed-shape annular domain of physical radius

\[
R\equiv R_j,
\qquad
K:=R/r_j\gg1.
\]

The first-hitting remaining-time estimate gives

\[
\boxed{
T_*-t_j
\le
C_T\frac{r_j^2}{\nu}
=
C_T\frac{R^2}{\nu K^2}.
}
\]

M5-437 gives the Galilean-invariant source oscillation lower bound

\[
\boxed{
E_{osc}(t_j)
:=
\inf_c\int_{D_R(t_j)}|u-c|^2dx
\ge
c_E\nu^2K^4R.
}
\]

Thus

\[
\boxed{
Q_j:=E_{osc}(t_j)^{1/2}
\ge
c_Q\nu K^2R^{1/2}.
}
\]

---

## 2. Mean-velocity moving frame

Choose a fixed smooth nonnegative cutoff `chi_R` adapted to the source annulus, with total mass

\[
M_\chi=\int\chi_Rdx\asymp R^3.
\]

Let the shell center `X(t)` solve

\[
\boxed{
\dot X(t)=c(t),
}
\]

where `c(t)` is the `chi_R`-weighted mean velocity in the moving annulus:

\[
\boxed{
c(t)
=
\frac1{M_\chi}
\int \chi_R(x-X(t))u(x,t)dx.
}
\]

Smoothness before `T_*` gives a local smooth solution of this center ODE.

In moving coordinates

\[
y=x-X(t)
\]

define

\[
w(y,t)=u(X(t)+y,t)-c(t).
\]

Then by construction

\[
\boxed{
\int\chi_R(y)w(y,t)dy=0.
}
\]

The time-dependent uniform acceleration `dot c(t)` is absorbed into the pressure exactly as in the translating/accelerating-frame gauge used in M5-406. Thus `w` satisfies Navier--Stokes in the moving frame with a modified pressure `pi`:

\[
\partial_tw+(w\cdot\nabla)w
=-\nabla\pi+\nu\Delta w,
\qquad
\nabla\cdot w=0.
\]

---

## 3. Weighted velocity variance

Define

\[
\boxed{
E(t)=\int\chi_R(y)|w(y,t)|^2dy.
}
\]

Because `c(t)` is the weighted mean, this is equivalent, up to fixed cutoff-domain constants, to

\[
\inf_c\int_{D_R(t)}|u-c|^2dx.
\]

The derivative of `c(t)` does not produce an energy term because

\[
\int\chi_Rw=0.
\]

Multiplying the moving-frame local energy equality by `chi_R` gives

\[
\frac12E'(t)
+
\nu\int\chi_R|\nabla w|^2
=
\int
\left(\frac{|w|^2}{2}+\pi\right)
w\cdot\nabla\chi_R
+
\frac\nu2\int(\Delta\chi_R)|w|^2.
\]

A constant may be subtracted from `pi` because

\[
\int c_p w\cdot\nabla\chi_R
=-c_p\int\chi_R\nabla\cdot w=0.
\]

---

## 4. Quiet scale-invariant shell bounds

Define the relative shell quantities

\[
A_*:=R\|w\|_{L^\infty(\operatorname{supp}\nabla\chi_R)},
\]

\[
\Gamma_*^2
:=
\frac{R^2\int\chi_R|\nabla w|^2}{E},
\]

and

\[
P_*:=R^{1/2}
\inf_{p_0}\|\pi-p_0\|_{L^2(\operatorname{supp}\nabla\chi_R)}.
\]

On the quiet old-shell corridor these remain bounded by fixed constants.

Failure of any bound is already a typed branch:

- large `A_*`: relative amplitude/frame crossing throughput;
- large `Gamma_*`: derivative/frequency throughput;
- large `P_*`: pressure/acceleration/remote forcing throughput.

Thus it is legitimate to derive freezing under fixed bounds and route their failure to strong throughput.

---

## 5. Differential inequality for the variance

Use

\[
|\nabla\chi_R|\lesssim R^{-1},
\qquad
|\Delta\chi_R|\lesssim R^{-2}.
\]

The advective flux obeys

\[
\left|
\int\frac{|w|^2}{2}w\cdot\nabla\chi_R
\right|
\le
C A_*R^{-2}E.
\]

The viscous dissipation term has magnitude bounded by

\[
\nu\int\chi_R|\nabla w|^2
\le
\nu\Gamma_*^2R^{-2}E.
\]

The cutoff viscous term obeys

\[
\left|
\frac\nu2\int\Delta\chi_R|w|^2
\right|
\le
C\nu R^{-2}E.
\]

For pressure,

\[
\left|
\int(\pi-p_0)w\cdot\nabla\chi_R
\right|
\le
C P_*R^{-3/2}E^{1/2}.
\]

Therefore

\[
\boxed{
|E'(t)|
\le
C_1R^{-2}E(t)
+
C_2P_*R^{-3/2}E(t)^{1/2},
}
\]

where `C1` includes the fixed quiet `A_*`, `nu`, and `Gamma_*` bounds.

For

\[
Q(t)=E(t)^{1/2},
\]

this yields

\[
\boxed{
|Q'(t)|
\le
C_3R^{-2}Q(t)
+
C_4P_*R^{-3/2}.
}
\]

The constants are independent of the late first-hitting stage.

---

## 6. Remaining-time compression freezes the variance

Integrate from `t_j` to any `t<T_*` while the quiet shell bounds remain active.

Using

\[
T_*-t_j
\le
C_T\frac{R^2}{\nu K^2},
\]

the homogeneous variation factor is

\[
\exp\left[
C_3R^{-2}(T_*-t_j)
\right]
=
1+O(K^{-2})
\]

up to fixed viscosity constants.

The pressure/source additive variation is at most

\[
C_4P_*R^{-3/2}(T_*-t_j)
\le
C\frac{P_*}{\nu}K^{-2}R^{1/2}.
\]

Relative to the formation lower bound

\[
Q_j\ge c_Q\nu K^2R^{1/2},
\]

this is

\[
O\left(\frac{P_*}{\nu^2}K^{-4}\right).
\]

Therefore

\[
\boxed{
\frac{|Q(t)-Q_j|}{Q_j}
\le
C K^{-2}
+
C'K^{-4}
}
\]

for every later time before `T_*` on the quiet corridor.

In particular, for sufficiently large `K`,

\[
\boxed{
Q(t)\ge\frac12Q_j
}
\]

throughout the remaining time.

Equivalently,

\[
\boxed{
E_{osc}(R,t)
\ge
c\nu^2K^4R
}
\]

for all later `t<T_*`, unless a strong relative amplitude/derivative/pressure/frame exit occurs.

---

## 7. Physical center drift and shell separation

The moving annulus is defined in its mean-velocity frame. A common Galilean translation is irrelevant.

For the common-time packing application, what matters is differential drift between different frozen shells. If the shell center moves by an order-one fraction of its radius relative to the nested physical source stack, then the coherent-frame/material-crossing quantity is already order one and belongs to the typed frame/transport throughput branch.

Thus on the retained quiet frozen lane, after choosing a sufficiently geometrically separated subsequence of radii, the enlarged moving annuli remain disjoint up to `T_*`.

This is the same geometric separation firewall used in M5-435, now applied to the Galilean-invariant variance rather than a raw cutoff packet.

---

## 8. Consequence

M5-434's qualitative remote freezing can now be stated without relying on a cutoff-generated natural-frequency packet:

\[
\boxed{
\text{fixed-fraction remote source at }K\gg1
\Longrightarrow
H_{strong\ relative/pressure/frame}
\lor
F_{osc}^{frozen},
}
\]

where the frozen object is the actual velocity oscillation modulo constants,

\[
\boxed{
E_{osc}(R,t)
\gtrsim
\nu^2K^4R.
}
\]

This is Galilean invariant and directly compatible with fractional Poincare.

---

## 9. Audit verdict

### Proved on the quiet old-shell corridor

- local velocity variance modulo constants obeys a natural-rate differential inequality;
- only `O(K^-2)` of one source natural time remains;
- the remote-source variance from M5-437 loses only `O(K^-2)+O(K^-4)` relatively;
- sufficiently remote quiet source oscillation freezes to the terminal time.

### Routed failures

Large relative amplitude, derivative ratio, pressure/acceleration oscillation, or coherent-frame drift are strong critical/interface throughput, not quiet frozen behavior.

### Still open

- common-time summation of the now-frozen local fractional seminorms;
- whether the resulting cumulative critical stack contradicts or merely refines the surviving critical-mass lane;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
