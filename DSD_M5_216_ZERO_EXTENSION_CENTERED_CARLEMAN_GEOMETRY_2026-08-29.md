# DSD M5-216 — Zero-Extension Centered Carleman Geometry

Date: 2026-08-29

Parent: `DSD_M5_215_ZERO_EXTENSION_AND_PARABOLIC_INFINITE_ORDER_REDUCTION_2026-08-29.md`

Status: **POSITIVE GEOMETRIC REDUCTION / ZERO EXTENSION PAST `T_*` REMOVES THE TERMINAL HYPERSURFACE AS A TIME BOUNDARY FOR A LOCAL CARLEMAN ARGUMENT / WITH A BOULAKIA-TYPE WEIGHT `psi=d(x)-beta(t-T_*)^2`, BOTH THE OLD-TIME CUTOFF COMMUTATOR AND THE INNER-SPATIAL LOCALIZATION COMMUTATOR CAN BE PLACED AT STRICTLY LOWER WEIGHT LEVELS THAN A FIXED EXTERIOR TARGET NEAR `T_*` / THE FUTURE-TIME CUTOFF COST IS EXACTLY ZERO BECAUSE THE EXTENDED FIELD IS ZERO THERE / NO TYPE-I CRITICAL COEFFICIENT APPEARS ON THE FIXED LOCAL DOMAIN / THE REMAINING ISSUE IS AN ACTUAL LOCAL NONSTATIONARY OSEEN-STOKES CARLEMAN ESTIMATE WITH PRESSURE USING THIS COMMON WEIGHT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Zero-extended local pair

Fix a point

\[
x_0\ne x_*
\]

and a bounded smooth spatial domain `D` satisfying

\[
\overline D\subset\mathbb R^3\setminus\{x_*\}.
\]

Let

\[
(Z,q)
\]

be the same-tail relative physical velocity-pressure pair on `D` for `t<T_*`.

By M5-145/M5-215, all terminal time jets of `Z` vanish on compact subsets of `D` and `Z(.,T_*)=0` exactly.

Extend

\[
\widetilde Z(t,x)
=
\begin{cases}
Z(t,x),&t<T_*,\\
0,&t\ge T_*,
\end{cases}
\]

and choose the relative pressure gauge so that

\[
\widetilde q(t,x)=0
\qquad(t\ge T_*).
\]

Extend the bounded Oseen coefficients smoothly past `T_*`.

Since the velocity jump at `T_*` is zero, there is no `delta_(t=T_*)` in `partial_t Z_tilde`.

The all-order terminal flatness makes the extension smooth to every finite order on compact subsets of `D`.

Thus the terminal hypersurface is now an **interior time slice** of a local smooth/weak linear system, not a terminal boundary.

---

## 2. Time cutoff without a future commutator cost

Choose

\[
0<\delta_1<\delta_2.
\]

Let `chi_t(t)` satisfy

\[
\chi_t=0
\quad(t\le T_*-\delta_2),
\]

\[
\chi_t=1
\quad(t\ge T_*-\delta_1),
\]

and be smoothly supported inside a symmetric interval

\[
(T_*-2\delta_2,T_*+2\delta_2).
\]

Because

\[
\widetilde Z=0
\quad(t\ge T_*),
\]

any additional cutoff placed on the future side produces no velocity commutator there.

The only nonzero time-cutoff commutator is supported in the older-time slab

\[
\boxed{
T_*-\delta_2<t<T_*-\delta_1.
}
\]

This is the first source region to be separated by the Carleman weight.

---

## 3. Spatial cutoff and target

Choose nested spatial sets

\[
D_{in}\Subset D_{tar}\Subset D_{out}\Subset D
\]

so that the desired exterior target lies in `D_tar`, while all spatial cutoff derivatives are supported in

\[
D_{out}\setminus D_{tar}
\]

or, in the fixed-exterior version, in an inner annular buffer separated from the target.

Choose a smooth function

\[
d\in C^2(\overline D)
\]

with the local Carleman geometry

\[
\boxed{
 d_{tar,-}
:=\inf_{D_{tar}}d
>
 d_{src,+}
:=\sup_{\operatorname{supp}\nabla\chi_x}d.
}
\]

Define the positive spatial gap

\[
\boxed{
\Delta_d:=d_{tar,-}-d_{src,+}>0.
}
\]

This is the Boulakia-style target/cutoff weight separation.

---

## 4. Center the time weight at T_*

Set

\[
\boxed{
\psi(t,x)
:=
d(x)-\beta(t-T_*)^2,
}
\]

with `beta>0`, and then

\[
\boxed{
\phi(t,x):=e^{\lambda\psi(t,x)}
}
\]

with `lambda` large enough for the spatial pseudoconvexity requirements of the chosen Stokes/elliptic Carleman architecture.

The time factor has its maximum exactly at

\[
t=T_*.
\]

Because the field is zero for `t>T_*`, this symmetric maximum creates no future-side unknown to control.

---

## 5. Old-time source receives a strict weight loss

On the target time slab

\[
|t-T_*|\le\frac{\delta_1}{2},
\]

one has

\[
\psi(t,x)
\ge
 d_{tar,-}
-\frac14\beta\delta_1^2
\qquad(x\in D_{tar}).
\]

On the time-commutator slab

\[
\delta_1\le T_*-t\le\delta_2,
\]

one has

\[
\psi(t,x)
\le
 d_{max}
-\beta\delta_1^2.
\]

By shrinking the spatial local domain or choosing `beta` large relative to the finite oscillation of `d`, one can ensure

\[
\boxed{
\sup_{time-src}\psi
<
\inf_{target}\psi.
}
\]

Define the resulting positive temporal-source gap

\[
\boxed{
\Delta_t>0.
}
\]

Thus the older-time commutator is exponentially lower in the large Carleman parameter.

---

## 6. Spatial source receives a strict weight loss

At times near `T_*`, the common time penalty is almost the same for target and spatial-source regions.

Therefore the spatial gap `Delta_d` yields

\[
\boxed{
\sup_{space-src}\psi
<
\inf_{target}\psi
}
\]

provided the near-terminal time slab is chosen sufficiently thin.

Let

\[
\boxed{
\Delta_x>0
}
\]

be this spatial level gap.

---

## 7. One unified source gap

Set

\[
\boxed{
\Delta_*
:=
\min\{\Delta_t,\Delta_x\}>0.
}
\]

If a compatible local Carleman estimate gives a weighted target coercivity with factor

\[
e^{2s\phi_{tar}}
\]

while all cutoff/commutator terms are supported where

\[
\phi\le\phi_{tar}-c\Delta_*,
\]

then after division by the target weight they are suppressed by

\[
\boxed{
 e^{-c s\Delta_*}.
}
\]

Hence

\[
\boxed{
\text{old-time source}
+
\text{inner spatial source}
\longrightarrow0
\quad(s\to\infty)
}
\]

at the level of Carleman geometry.

This mechanism does **not** use the smallness of the commutator fields or their terminal-flat amplitude.

---

## 8. Why zero extension is essential

Without zero extension, a Carleman window centered at `T_*` would terminate at the time where the weight is maximal.

One would then have to justify terminal boundary terms directly.

After zero extension:

1. `T_*` is an interior time;
2. the field is identically zero on one full side of that time slice;
3. temporal cutoff derivatives can be placed strictly in the past;
4. the symmetric Boulakia-type time geometry is available without a terminal boundary term.

Thus

\[
\boxed{
\text{terminal backward problem}
\rightsquigarrow
\text{interior spacetime unique-continuation geometry}.
}
\]

This is stronger than the M5-213 formulation.

---

## 9. Coefficient audit

On `D`, which is separated from `x_*`,

\[
\|u^{V,W}\|_\infty
+
\|\nabla u^{V,W}\|_\infty
+
\|\omega^{V,W}\|_\infty
<\infty
\]

uniformly near `T_*`.

Therefore all Oseen lower-order terms are ordinary bounded perturbations of the local nonstationary Stokes operator.

No weak-`L^3` / Hardy-critical amplitude enters this local problem.

The whole-space M5-210 critical stretching obstruction has been bypassed rather than solved.

---

## 10. Remaining estimate target

The geometry above closes every support/weight-placement issue **conditional on** a local estimate of the following structural type for the zero-extended pair:

\[
\boxed{
I_Z(s)+I_q(s)
\le
C
\bigl(
I_{lower-order}(s)
+E_{cutoff}(s)
\bigr),
}
\]

where

- `I_Z` contains positive `s|grad Z|^2+s^3|Z|^2` terms;
- `I_q` contains compatible weighted pressure control;
- bounded Oseen terms can be absorbed for large `s`;
- cutoff terms are exactly on the lower levels constructed above.

M5-214 shows algebraically that the pressure source contains only `grad Z`, so there is no derivative-count obstruction to such a pair.

The estimate itself is not re-proved here.

---

## 11. DSD verdict

### Formation — GREEN

Every cutoff and extended field is an ordinary finite local PDE object.

### Axis — GREEN

Past-time, future-time, and spatial-cutoff supports are explicitly separated.

### Static aggregation — GREEN

The existence of a favorable weight geometry is not counted as the Carleman inequality itself.

### Dynamics — YELLOW, one local estimate

The only remaining gate in this line is the compatible local Oseen–Stokes parabolic/elliptic Carleman estimate.

### Cross-audit — GREEN

The construction uses M5-145 flatness only to justify smooth zero extension; it does not invoke forbidden terminal analyticity.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]