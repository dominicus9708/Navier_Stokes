# DSD M5-579 — Audit: Stationary Terminal Energy Defect vs Type-I Core

Date: 2026-09-02

Status: **THE STRICT POSITIVE TERMINAL ENERGY FLUX FROM M5-578 IS EXACTLY TYPE-I SCALE-COMPATIBLE WITH CORE ENERGY CHANGE, DISSIPATION, AND MOVING-BOUNDARY WORK. IT IS NOT BY ITSELF A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Purpose

M5-578 proved that every nontrivial recurrent stationary terminal profile obeys

\[
\Phi_E(q)>0
\]

and the physical stationary energy flux through a sphere is

\[
\int_{S_r}J_A\cdot n\,dS
=
\frac1r\Phi_E(\log r).
\]

Because this diverges like \(1/r\) toward the singular core, it is tempting to treat it as an impossible terminal source.

The correct audit must compare it with the natural shrinking Type-I core scale.

---

## 2. Type-I similarity variables

Let

\[
a=-s>0,
\qquad
\theta=-\log a,
\qquad
y=x/\sqrt a,
\]

and

\[
u(x,s)=a^{-1/2}U(y,\theta),
\qquad
p(x,s)=a^{-1}\Pi(y,\theta).
\]

Fix a large normalized radius \(L>1\) and consider the moving physical sphere

\[
\boxed{R(s)=L\sqrt a.}
\]

This is the natural Type-I parabolic boundary.

---

## 3. Core energy scaling

Define

\[
E_L(s)
:=
\frac12\int_{|x|<L\sqrt a}|u(x,s)|^2dx.
\]

Changing variables gives

\[
\boxed{
E_L(s)
=
\sqrt a\,\mathcal E_L(\theta),
}
\]

where

\[
\mathcal E_L(\theta)
:=
\frac12\int_{|y|<L}|U(y,\theta)|^2dy.
\]

Since

\[
\frac{d\theta}{ds}=a^{-1},
\qquad
\frac{d\sqrt a}{ds}=-\frac1{2\sqrt a},
\]

we obtain the exact scaling derivative

\[
\boxed{
\frac{dE_L}{ds}
=
a^{-1/2}
\left(
\mathcal E_L'(\theta)
-\frac12\mathcal E_L(\theta)
\right).
}
\]

Thus the natural Type-I core energy-change rate is \(O(a^{-1/2})\).

---

## 4. Exact moving-ball local-energy balance

For a smooth solution, with

\[
e=\frac12|u|^2,
\]

and

\[
J=(e+p)u-\nabla e,
\]

the local energy equality is

\[
\partial_se+\nabla\cdot J=-|\nabla u|^2.
\]

For the moving ball \(B_{R(s)}\), Reynolds transport gives

\[
\boxed{
\frac d{ds}\int_{B_{R(s)}}e\,dx
=
-\int_{S_{R(s)}}J\cdot n\,dS
-\int_{B_{R(s)}}|\nabla u|^2dx
+R'(s)\int_{S_{R(s)}}e\,dS.
}
\]

Since

\[
R'(s)=-\frac{L}{2\sqrt a},
\]

the boundary is shrinking toward the singular point.

---

## 5. Every term has the same Type-I order

Under the similarity scaling,

\[
e=a^{-1}e_U,
\qquad
J=a^{-3/2}J_U,
\qquad
|\nabla u|^2=a^{-2}|\nabla U|^2,
\]

and

\[
dx=a^{3/2}dy,
\qquad
dS_x=a\,dS_y.
\]

Therefore:

### Energy derivative

\[
\frac{dE_L}{ds}=O(a^{-1/2}).
\]

### Boundary energy flux

\[
\int_{S_{L\sqrt a}}J\cdot n\,dS
=
\boxed{a^{-1/2}\mathcal J_L(\theta)}.
\]

### Core dissipation

\[
\int_{B_{L\sqrt a}}|\nabla u|^2dx
=
\boxed{a^{-1/2}\mathcal D_L(\theta)}.
\]

### Moving-boundary term

\[
R'(s)\int_{S_{L\sqrt a}}e\,dS
=
\boxed{-a^{-1/2}\frac L2\mathcal B_L(\theta)}.
\]

Hence the moving-ball balance is exactly

\[
\boxed{
\mathcal E_L'-\frac12\mathcal E_L
=
-\mathcal J_L
-\mathcal D_L
-\frac L2\mathcal B_L.
}
\]

No term has a stronger singular scale than the others.

---

## 6. Match with the stationary terminal energy flux

On the stationary terminal branch, the far-field critical trace gives

\[
\int_{S_r}J_A\cdot n\,dS
=
\frac1r\Phi_E(\log r).
\]

At the Type-I boundary

\[
r=L\sqrt a,
\]

this becomes

\[
\boxed{
\int_{S_{L\sqrt a}}J_A\cdot n\,dS
=
\frac{a^{-1/2}}{L}
\Phi_E\!\left(\log L+\frac12\log a\right).
}
\]

Equivalently, since \(\theta=-\log a\),

\[
\boxed{
\frac{a^{-1/2}}{L}
\Phi_E\!\left(\log L-\frac\theta2\right).
}
\]

This is precisely the same \(a^{-1/2}\) scaling as the core-energy derivative and the viscous/moving-boundary terms.

Therefore

\[
\boxed{
\text{strict positive terminal energy flux}
\quad\text{is Type-I scale-compatible.}
}
\]

---

## 7. Why the large-L regime is legitimate

The terminal expansion is a parabolic far-field expansion requiring

\[
r^2\gg a.
\]

At

\[
r=L\sqrt a,
\]

this is simply

\[
L^2\gg1.
\]

Thus one may choose fixed sufficiently large \(L\) and compare the terminal critical flux with the outer part of the Type-I similarity core.

The conclusion is not based on extrapolating the far-field formula into \(L=O(1)\).

---

## 8. Anti-proof conclusion

M5-578's implication

\[
C=0,\ A\neq0
\Longrightarrow
\Phi_E(q)>0
\]

is correct.

But the further implication

\[
\Phi_E>0
\Longrightarrow
\text{impossible terminal source}
\]

is not justified.

At the shrinking Type-I radius, the required energy current scales exactly like the naturally available core energy-change rate:

\[
\boxed{
\frac{\Phi_E}{R(s)}
\sim
|s|^{-1/2},
\qquad
\frac d{ds}E_{core}(s)
\sim
|s|^{-1/2}.
}
\]

This is the energy analogue of M5-576's momentum audit, where a Landau stress defect was found compatible with linear Type-I relative-momentum drift.

---

## 9. Refined stationary closure target

The stationary branch cannot be eliminated by scaling alone.

A genuine closure must prove more than finiteness or growth-rate mismatch. It must control the **coefficient** or **sign structure** of the terminal defect in the shrinking parabolic local-energy balance.

Possible theorem-level targets are:

1. terminal local-energy defect compactness showing the point-supported defect coefficient vanishes;
2. a monotonicity or sign law inconsistent with the strictly outward \(\Phi_E\);
3. an inherited original-solution local-energy condition that survives the blow-up limit and forbids the defect coefficient.

No such theorem is currently present in the retained package.

Status: **THE STATIONARY ENERGY-DEFECT BRANCH SURVIVES THE TYPE-I SCALING AUDIT. POSITIVE TERMINAL ENERGY FLUX AND CORE ENERGY CHANGE HAVE EXACTLY MATCHING |s|^-1/2 SCALE. GLOBAL REGULARITY REMAINS UNPROVED.**