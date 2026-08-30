# DSD M5-295 — Radial-Axis Alignment Dynamic Mismatch and Tangential-Stretching Cancellation Gate

Date: 2026-08-30

Parent: `DSD_M5_294_FORMATION_AXIS_CLOUD_BIOT_SAVART_LEADING_MULTIPOLE_AND_ANGULAR_STRAIN_ORDER_PARAMETER_2026-08-30.md`

Status: **AXIS-ATTRIBUTE DYNAMIC GATE / EXACT EVOLUTION OF THE LEADING-STRAIN-INVISIBILITY CONDITION `n × M = 0` / A REMOTE PACKET CAN REMAIN RADIAL-AXIS ALIGNED ONLY IF ITS TANGENTIAL VORTICITY-MOMENT EVOLUTION TRACKS THE MUCH SLOWER GEOMETRIC ROTATION OF THE RADIAL DIRECTION / ON A QUIET REMOTE NATURAL-TIME WINDOW THIS FORCES A TANGENTIAL STRETCHING-MOMENT CANCELLATION OR A BOUNDARY/DIFFUSIVE/RELATIVE-TRANSPORT EXIT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-294 showed that one localized satellite has zero leading `d^{-3}` far strain at the tracked core when

\[
M\parallel n,
\qquad
M=\int\chi\omega,
\qquad
n=\frac{y-X}{|y-X|}.
\]

The present note asks whether this leading-strain invisibility can remain dynamically stable.

The Formation/Axis language is used only to isolate the relevant variables.

The actual calculation is standard Navier–Stokes vorticity transport.

---

## 2. Relative radial geometry

Let `y(t)` be the satellite packet center and `X(t)` the tracked main-core center.

Define

\[
r=y-X,
\qquad
d=|r|,
\qquad
n=r/d.
\]

Let

\[
v_{rel}:=\dot y-\dot X.
\]

Then

\[
\boxed{
\dot d=n\cdot v_{rel},
}
\]

and

\[
\boxed{
\dot n
=\frac1dP_n v_{rel},
\qquad
P_n=I-n\otimes n.
}
\]

Thus only transverse relative motion rotates the radial direction.

---

## 3. Localized vorticity moment

Take a fixed-shape translating cutoff around the satellite center,

\[
\chi(x,t)=\chi_0\!\left(\frac{x-y(t)}\ell\right)
\]

on one short window where the packet scale `\ell` is treated as fixed.

Then

\[
\chi_t+\dot y\cdot\nabla\chi=0.
\]

Define

\[
\boxed{
M(t)=\int\chi\omega\,dx.
}
\]

The vorticity equation is

\[
\omega_t+u\cdot\nabla\omega
=S\omega+\nu\Delta\omega.
\]

Using `div u=0`, one obtains the exact localized moment equation

\[
\boxed{
\dot M
=
\int\chi S\omega\,dx
+
\int ((u-\dot y)\cdot\nabla\chi)\,\omega\,dx
+
\nu\int (\Delta\chi)\omega\,dx.
}
\]

Write

\[
\boxed{
\dot M=\mathcal S_M+\mathcal B_M,
}
\]

where

\[
\mathcal S_M:=\int\chi S\omega,
\]

and `B_M` contains material mismatch through the packet boundary plus viscous localization action.

No approximation has been made.

---

## 4. Alignment defect

Define the leading-strain alignment defect

\[
\boxed{
c:=n\times M.
}
\]

M5-294 gives

\[
c=0
\iff
M\parallel n
\]

for nonzero `M`, and the leading far-strain tensor is proportional to `sym(n⊗c)`.

Differentiate:

\[
\boxed{
\dot c
=\dot n\times M+n\times\dot M.
}
\]

At an exactly aligned instant,

\[
M=mn,
\qquad m=M\cdot n,
\]

so

\[
\boxed{
\dot c
=n\times\left(\dot M-m\dot n\right).
}
\]

Therefore exact alignment can persist only if

\[
\boxed{
P_n\dot M=m\dot n.
}
\]

Substituting the two exact evolution equations gives the two-component tangent-plane constraint

\[
\boxed{
P_n(\mathcal S_M+\mathcal B_M)
=
\frac{m}{d}P_n v_{rel}.
}
\]

This is the exact radial-axis maintenance equation.

---

## 5. Dynamic mismatch vector

Define

\[
\boxed{
\mathcal G_{align}
:=
P_n\mathcal S_M
+P_n\mathcal B_M
-\frac{m}{d}P_n v_{rel}.
}
\]

At exact alignment,

\[
\boxed{
\dot c=n\times\mathcal G_{align}.
}
\]

Thus any coherent nonzero alignment mismatch immediately creates the transverse moment `c` that was required to generate the leading `d^{-3}` far strain.

The quiet radial-alignment branch must therefore keep

\[
\boxed{
\mathcal G_{align}\approx0.
}
\]

in an integrated/directional sense.

---

## 6. Natural-scale comparison

For a natural packet,

\[
|\omega|\sim\ell^{-2},
\qquad
|S|\sim\ell^{-2},
\qquad
\operatorname{Vol}\sim\ell^3,
\qquad
|M|\sim\ell.
\]

Hence

\[
|\mathcal S_M|\sim\ell^{-1}.
\]

Use the natural packet time

\[
\tau=(t-t_0)/\ell^2.
\]

If the relative center velocity is no larger than natural size,

\[
|v_{rel}|\le C_v\ell^{-1},
\]

then with

\[
L=d/\ell\gg1
\]

one has

\[
\boxed{
\left|\frac{dn}{d\tau}\right|
\le\frac{C_v}{L}.
}
\]

Therefore the radial direction turns only `O(L^{-1})` per natural time.

By contrast the normalized stretching moment

\[
\ell\,P_n\mathcal S_M
\]

is naturally `O(1)`.

Thus persistent radial alignment requires the `O(1)` tangential stretching moment to be cancelled down to the much smaller geometric rate `O(L^{-1})`, unless an exit occurs.

---

## 7. Quiet-alignment consequence

Assume on a natural-time interval `I`:

1. `|m|\ge m_-\ell`;
2. `|v_rel|\le C_v/\ell`;
3. boundary/diffusive moment action is quiet,
   \[
   \int_I \ell\,|P_n\mathcal B_M|\,d\tau\le\varepsilon_B;
   \]
4. the leading far-strain alignment defect remains small,
   \[
   |c|\le\varepsilon_c\ell.
   \]

Then the maintenance equation implies schematically

\[
\boxed{
\int_I
\left|\ell P_n\mathcal S_M\right|\,d\tau
\lesssim
\varepsilon_B+arepsilon_c+rac{C_v|I|}{L}
+\mathcal A_{dir-cancel},
}
\]

where `A_dir-cancel` records cancellation due to rapid turning of the tangent-plane mismatch direction.

Hence an order-one tangential stretching-moment action forces at least one of

\[
\boxed{
T_{align-defect}
\lor
T_{align-dir}
\lor
T_{boundary/diff}
\lor
T_{fast-relative-motion}.
}
\]

The last branch corresponds to

\[
|v_{rel}|\gg\ell^{-1},
\]

which is itself a natural-scale material/center turnover event.

---

## 8. Important firewall: scalar cancellation is insufficient

The maintenance constraint lives in the two-dimensional tangent plane:

\[
P_n\mathcal S_M
+P_n\mathcal B_M
=\frac{m}{d}P_nv_{rel}.
\]

A scalar condition such as

\[
M\cdot n=\text{constant}
\]

or

\[
\xi^TS\xi=0
\]

does not enforce it.

Thus radial-axis invisibility is dynamically codimension two at the level of the localized vorticity moment.

However codimension alone is not a contradiction: an exact symmetric invariant subclass could preserve it.

A dynamic estimate, not genericity language, is still required.

---

## 9. Relation to the affine countermodel

The affine stationary examples from M5-291 show why this branch cannot be closed from local axis geometry alone.

An affine solution may maintain exact alignment/cancellation indefinitely because the whole spatial field supplies the required coherent strain and pressure structure.

Such examples are excluded from the original problem only by their non-finite-energy/global-growth behavior.

Therefore the remaining nonlocal ingredient is again **ancestry**:

\[
\boxed{
\text{can a finite-energy first-hitting sequence sustain the alignment-maintenance identity on expanding windows?}
}
\]

This unifies the radial-alignment cloud problem with the sparse/affine detached-satellite frontier.

---

## 10. Updated cloud split

Combining M5-294 and M5-295:

\[
\boxed{
\begin{aligned}
C_{cloud}
\Longrightarrow{}&H_{ambient}\\
&\lor T_{align/relative/boundary}\\
&\lor C_{tensor-cancel}\\
&\lor C_{M_0=0,next-multipole}\\
&\lor A_{ancestry-protected\ alignment}.
\end{aligned}
}
\]

The next high-value branch is collective tensor cancellation. It imposes five scalar trace-free tensor constraints instead of two per-packet alignment constraints. The efficient question is whether those five constraints can be propagated by the cloud dynamics without producing covariance/projective turnover.

---

## 11. Audit verdict

### PROVED / EXACT

- radial direction evolution `n_dot=d^{-1}P_n v_rel`;
- localized vorticity-moment equation;
- alignment defect equation;
- exact two-component maintenance condition;
- remote geometry rotates only `O(L^{-1})` per natural time under natural relative velocity.

### CONDITIONAL ROUTING

Under quiet boundary/diffusion and natural relative-speed ceilings, order-one tangential stretching-moment action cannot coexist with persistent small alignment defect without directional cancellation/turnover.

### NOT PROVED

- a universal lower bound on tangential stretching-moment action;
- exclusion of exact symmetric alignment subclasses;
- the ancestry bridge needed to remove affine-type maintenance;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]