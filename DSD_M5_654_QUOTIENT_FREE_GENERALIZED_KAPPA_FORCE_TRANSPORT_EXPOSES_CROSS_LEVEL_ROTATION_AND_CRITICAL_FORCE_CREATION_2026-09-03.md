# DSD M5-654 — Quotient-free generalized-kappa-force transport exposes cross-level rotation and critical force creation

Date: 2026-09-03

Status: **INTERNAL QUOTIENT-FREE FORCE DYNAMICS / ON CE-H, THE GENERALIZED KAPPA FORCE `F=rho^2 nabla kappa` OBEYS `D_B F=(2 gamma I-L^T)F+rho^2 nabla h`, WITH `h=D_B kappa`, `gamma=sigma+kappa-1`, `L=nabla B`; CROSSING WITH `F` REMOVES THE SCALAR AMPLITUDE TERM AND GIVES THE EXACT GLOBAL FORCE-ROTATION OBSERVABLE `F x (D_BF+L^TF)=rho^4 nabla kappa x nabla h` / AT ACTIVE CRITICAL POINTS `nabla kappa=0`, ONE HAS `D_BF=rho^2 nabla h`, SO MULTI-SHEET CRITICAL PATCHING REQUIRES MATERIAL CREATION OF GENERALIZED KAPPA FORCE FROM ZERO / THE LOCAL QUOTIENT BRANCH IS THEREFORE RECAST AS TWO PDE EVENTS: CROSS-LEVEL FORCE ROTATION OR CRITICAL FORCE CREATION / NEITHER IS YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Generalized kappa force

On the CE-H active set define

\[
\boxed{
F:=\rho^2\nabla\kappa.
}
\]

M5-615--617 give a quotient-free global extension through the nodal set using the eigenfield stress tensor, so `F` is treated as a globally smooth generalized force even where `kappa` itself is not a preferred quotient coordinate.

Let

\[
\boxed{
h:=D_B\kappa,}
\]

\[
\boxed{
\gamma:=\sigma+\kappa-1,
}
\]

and

\[
L:=\nabla B.
\]

---

## 2. Exact force transport

The CE-H amplitude equation gives

\[
D_B\rho=\gamma\rho,
\]

hence

\[
D_B(\rho^2)=2\gamma\rho^2.
\]

M5-627 gives

\[
D_B(\nabla\kappa)
=\nabla h-L^T\nabla\kappa.
\]

Therefore

\[
\begin{aligned}
D_BF
&=
D_B(\rho^2)\nabla\kappa
+
\rho^2D_B(\nabla\kappa)
\\
&=
2\gamma F
+
\rho^2\nabla h
-
L^TF.
\end{aligned}
\]

Thus

\[
\boxed{
D_BF
=
(2\gamma I-L^T)F
+
\rho^2\nabla h.
}
\]

Equivalently,

\[
\boxed{
D_BF+L^TF-2\gamma F
=\rho^2\nabla(D_B\kappa).
}
\]

---

## 3. Cross-level rotation observable

Take the cross product with `F`.

The scalar term disappears:

\[
F\times(2\gamma F)=0.
\]

Hence

\[
\boxed{
F\times(D_BF+L^TF)
=
\rho^2 F\times\nabla h.
}
\]

Since

\[
F=\rho^2\nabla\kappa,
\]

we obtain

\[
\boxed{
\mathcal C_\kappa
:=
F\times(D_BF+L^TF)
=
\rho^4
\nabla\kappa\times\nabla(D_B\kappa).
}
\]

Thus at regular active points

\[
\boxed{
\mathcal C_\kappa\ne0
\Longleftrightarrow
\text{genuine cross-level material acceleration.}
}
\]

This is the quotient-free version of the first branch of M5-627.

---

## 4. Critical-force creation

Suppose

\[
\rho>0,
\qquad
\nabla\kappa=0.
\]

Then

\[
F=0.
\]

The exact transport law reduces to

\[
\boxed{
D_BF
=
\rho^2\nabla h.
}
\]

Therefore if

\[
\nabla(D_B\kappa)\ne0
\]

at an active `kappa` critical point, the generalized force is instantaneously created from zero.

Define this as the critical-source event

\[
\boxed{
C_{crit}^{force}
:\quad
F=0,
\quad
D_BF\ne0.
}
\]

This is precisely the critical-point failure of a smooth scalar relabeling law that the ordinary cross product `nabla kappa x nabla h` cannot detect because that cross product vanishes automatically when `nabla kappa=0`.

---

## 5. Strong local relabeling condition

A genuinely smooth local relabeling patch through regular and critical points requires both:

1. on `F!=0`,

\[
\mathcal C_\kappa=0;
\]

2. on `F=0` with `rho>0`,

\[
D_BF=0.
\]

The second condition is equivalent there to

\[
\nabla h=0.
\]

Thus the patching defect has two complementary pieces:

\[
\boxed{
\text{patching defect}
=
\text{force rotation away from zero}
\lor
\text{force creation at zero}.
}
\]

---

## 6. Net-force mean constraint

M5-615 gives at every time

\[
\boxed{
\int_{\mathbb R^3}F\,dy=0.
}
\]

Differentiate this identity.

Since `div B=3/2`,

\[
\frac d{d\theta}\int Fdy
=
\int D_BFdy
+
\frac32\int Fdy
=
\int D_BFdy.
\]

Hence

\[
\boxed{
\int D_BFdy=0.
}
\]

Insert the transport equation:

\[
0
=
\int(2\gamma I-L^T)Fdy
+
\int\rho^2\nabla hdy.
\]

Therefore

\[
\boxed{
\int\rho^2\nabla hdy
=
\int(L^T-2\gamma I)Fdy.
}
\]

Equivalently, after integration by parts where justified,

\[
\boxed{
-\int h\nabla(\rho^2)dy
=
\int(L^T-2\gamma I)Fdy.
}
\]

Thus even the global mean cross-level source is not free: it is balanced by force deformation and amplitude growth.

No sign follows.

---

## 7. Relation to the tensor virial

M5-625--626 give

\[
\boxed{
\int y_kF_jdy
=
2\int\partial_jW\cdot\partial_kWdy.
}
\]

Hence the generalized force has a uniformly nondegenerate first-moment tensor on the marked compact CE-H hull.

M5-654 now shows that any surviving quotient dynamics must continually rotate/deform this force distribution or create force from critical zero-force locations.

Thus the forced quotient branch is no longer an abstract scalar-sheet phenomenon; it is a dynamical statement about the already nondegenerate three-dimensional `kappa`-force dipole.

---

## 8. Why this is not yet a strict cocycle

The quantity

\[
|\mathcal C_\kappa|^2
\]

is nonnegative, but positive recurrent force rotation can occur indefinitely on a compact state space.

Likewise, critical force creation can be followed by force destruction elsewhere while preserving zero net force.

No bounded scalar potential with one-sign drift has yet been derived from these events.

Therefore

\[
\boxed{
\text{positive force-rotation/creation activity}
\not\Rightarrow
\text{contradiction}
}

without an additional signed or finite-resource argument.

---

## 9. Updated quotient frontier

Combining M5-650 and the present force formulation, the unresolved CE-H quotient dynamics is

\[
\boxed{
E_{CEH}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{force}
\lor
R_{multi-sheet}^{globally\ disconnected}.
}
\]

Here `R_multi-sheet` denotes a genuinely global disconnected-sheet obstruction not resolved by local force rotation/critical creation alone.

The next calculation should test whether the tensor-virial positivity of `F` forces a minimum amount of force rotation/creation during every sheet-transfer cycle, and whether that cycle can be charged against one of the already bounded material/flux resources.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]