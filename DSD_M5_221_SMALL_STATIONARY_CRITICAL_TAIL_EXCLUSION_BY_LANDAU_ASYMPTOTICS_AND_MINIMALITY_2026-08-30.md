# DSD M5-221 — Small Stationary Critical Tail Exclusion by Landau Asymptotics and Minimality

Date: 2026-08-30

Parent: `DSD_M5_220_TAIL_HOMOGENEITY_DEFECT_TO_RESIDUAL_OR_STATIONARY_CRITICAL_PROFILE_FORK_2026-08-30.md`

Status: **STATIONARY SUBBRANCH PARTIALLY CLOSED / ANY NONHOMOGENEOUS STATIONARY CRITICAL TAIL FORMED BY M5-220 CANNOT LIE IN THE SMALL SCALE-INVARIANT AMPLITUDE REGIME COVERED BY KOROLEV--SVERAK LARGE-DISTANCE LANDAU ASYMPTOTICS / COMPACT MINIMAL DILATION DYNAMICS TURNS LANDAU ASYMPTOTICS INTO EXACT HOMOGENEITY, CONTRADICTING THE M5-219 HOMOGENEITY-DEFECT FLOOR / ONLY LARGE-CRITICAL-AMPLITUDE STATIONARY TAILS REMAIN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Stationary branch from M5-220

Assume the residual-quiet branch of M5-220 forms

\[
T_*\in\mathcal T
\]

with

\[
\boxed{
-\nu\Delta T_*+(T_*\cdot\nabla)T_*+\nabla P_*=0,
\qquad
\nabla\cdot T_*=0
}
\]

on `R^3\{0}` and

\[
\boxed{
|T_*(x)|\le \frac{A_*}{|x|}.
}
\]

The M5-219 phase-action passage also preserves

\[
\boxed{
T_*+x\cdot\nabla T_*\ne0
}
\]

on at least one fixed annulus.

Thus `T_*` is a nonhomogeneous stationary critical tail candidate.

---

## 2. External large-distance theorem and exact scope

Korolev--Sverak, *On the large-distance asymptotics of steady state solutions of the Navier--Stokes equations in 3D exterior domains*, study stationary solutions on an exterior region with

\[
|u(x)|\le \frac{C_*}{R_0+|x|}.
\]

For each

\[
1<\alpha<2
\]

they prove that there exists a sufficiently small threshold

\[
\varepsilon_{KS}(\alpha)>0
\]

such that if

\[
C_*\le\varepsilon_{KS}(\alpha),
\]

then

\[
\boxed{
 u(x)=U^b(x)+O(|x|^{-\alpha})
}
\]

as `|x|->infinity`, where `U^b` is the Landau solution determined by the constant momentum-flux/stress-charge vector `b`.

The derivative asymptotics also hold:

\[
\nabla^k u
=
\nabla^kU^b
+O(|x|^{-k-\alpha}).
\]

The theorem is perturbative in the scale-invariant amplitude. It is **not** an arbitrary-large-data theorem.

---

## 3. Apply the theorem to the stationary W1 tail in the small-amplitude lane

Assume

\[
\boxed{
A_*\le\varepsilon_{KS}(\alpha)
}
\]

for one fixed `1<alpha<2` after viscosity normalization.

Then on the exterior of a fixed ball,

\[
\boxed{
T_*(x)=U^b(x)+R(x),
\qquad
|R(x)|\lesssim |x|^{-\alpha}.
}
\]

Since the Landau field is exactly degree `-1`,

\[
D_hU^b=U^b
\qquad(h\in\mathbb R).
\]

For the remainder,

\[
(D_hR)(Y)
=e^{-h/2}R(e^{-h/2}Y).
\]

To inspect large physical radius at one fixed normalized point, send

\[
h\to-\infty.
\]

Then `e^{-h/2}|Y| -> infinity`, and

\[
|D_hR(Y)|
\lesssim
 e^{-h/2}
(e^{-h/2}|Y|)^{-\alpha}
=
 e^{(\alpha-1)h/2}|Y|^{-\alpha}
\to0
\]

because `alpha>1` and `h->-infinity`.

Therefore on every fixed punctured compact set,

\[
\boxed{
D_hT_*
\longrightarrow
U^b
\qquad(h\to-\infty).
}
\]

---

## 4. Why the negative dilation times belong to the compact tail dynamics

The minimal W1 set has

\[
S(h)M=M
\qquad(h\ge0).
\]

Forward uniqueness makes the restricted flow injective, while the omega-limit construction gives surjectivity. Hence on the compact minimal class the restricted Leray evolution is a homeomorphic group after taking the unique complete orbit through each point.

M5-218 conjugates this complete restricted flow with the dilation action on `mathcal T`.

Thus

\[
D_hT_*\in\mathcal T
\qquad(h\in\mathbb R).
\]

Since `mathcal T` is compact and closed, the local limit above gives

\[
\boxed{U^b\in\mathcal T.}
\]

---

## 5. A homogeneous Landau point collapses the minimal hull

The Landau point is fixed by the entire dilation flow:

\[
D_hU^b=U^b.
\]

Hence the singleton

\[
\{U^b\}
\]

is a nonempty compact invariant subset of `mathcal T`.

But `mathcal T` is minimal because it is topologically conjugate to the minimal W1 set.

Therefore

\[
\boxed{
\mathcal T=\{U^b\}.
}
\]

By M5-218 conjugacy,

\[
\boxed{
M\text{ is also a singleton equilibrium.}
}
\]

This contradicts both

\[
\|V_s\|_{L^2(B_R)}\ge\sigma_0>0
\]

and the M5-219 tail phase-action floor

\[
\|T+x\cdot\nabla T\|_{L^3(A_*)}\ge h_*>0
\]

on the selected nonstationary survivor.

Thus the small stationary tail branch is impossible.

---

## 6. Zero stress charge is included automatically

If

\[
b=0,
\]

then

\[
U^b=0.
\]

The same argument gives

\[
D_hT_*\to0
\]

and hence

\[
0\in\mathcal T.
\]

Minimality would force

\[
\mathcal T=\{0\},
\]

which is again incompatible with the nontrivial first-hitting normalization.

Thus no separate zero-force subcase survives in the small-amplitude lane.

---

## 7. Exact remaining stationary amplitude gate

The stationary nonhomogeneous branch from M5-220 must therefore violate the Korolev--Sverak smallness hypothesis:

\[
\boxed{
A_*>arepsilon_{KS}(\alpha)
}
\]

for every `alpha in (1,2)` whose theorem threshold is invoked.

Equivalently, the only stationary critical survivor is a genuinely **large scale-invariant stationary tail**.

This is stronger than merely saying that the general stationary classification is open.

---

## 8. Why arbitrary D-solution asymptotics are not imported

The tail does satisfy exterior finite Dirichlet energy because

\[
|\nabla T_*|\lesssim |x|^{-2}
\]

on the smooth W1 tail corridor, so

\[
\int_{|x|>R}|\nabla T_*|^2dx<\infty.
\]

However the available 3D Landau leading-asymptotic theorem recovered above is perturbative in the scale-invariant `1/r` amplitude.

Korolev--Sverak explicitly note that the large-data extension would require ideas beyond their perturbation/standard energy argument.

Therefore

\[
\text{finite Dirichlet integral}
\not\Rightarrow
\text{Landau asymptotics}
\]

is retained as a firewall for the arbitrary-amplitude branch.

---

## 9. Updated stationary frontier

M5-220 gave

\[
A_{min}^{aper}
\Longrightarrow
R_{tail}
\lor
S_{crit}^{nonhom}.
\]

The present note sharpens the second branch to

\[
\boxed{
S_{crit}^{nonhom}
\Longrightarrow
S_{crit,large}^{nonhom},
}
\]

where

\[
S_{crit,large}^{nonhom}:
\begin{cases}
F_T=0,\\
|T(x)|\le A_*/|x|,\\
A_*>\varepsilon_{KS},\\
T+x\cdot\nabla T\ne0,\\
\text{compact minimal dilation hull.}
\end{cases}
\]

The small stationary critical tail is closed.

---

## 10. Next target

The remaining large stationary branch has extra structure not present in a generic exterior stationary problem:

- zero spherical mass flux;
- compact minimal dilation hull;
- all W1 local derivative bounds;
- canonical pressure/stress charge;
- nonzero recurrent homogeneity defect;
- origin and infinity are two directions of the same complete dilation orbit.

The next stationary audit should test whether these added recurrence/two-sided-scale conditions force an asymptotically homogeneous tangent without assuming small amplitude.

In parallel, the residual-active branch still requires a residual-work audit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]