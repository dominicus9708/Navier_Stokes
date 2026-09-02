# DSD M5-583 — Ergodic q-Averaged Wedge Energy ODE

Date: 2026-09-02

Status: **THE TERMINAL ENERGY PAYER IDENTITY IS THE z=0 BOUNDARY VALUE OF AN EXACT ONE-DIMENSIONAL ENERGY TRANSPORT LAW ACROSS THE FULL PARABOLIC WEDGE. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Exact wedge field

From M5-582,

\[
u=r^{-1}F(z,q,\omega),
\qquad
p=r^{-2}H(z,q,\omega),
\]

with

\[
z=(-s)/r^2,
\qquad
q=\log r,
\]

and

\[
\mathfrak D=\partial_q-2z\partial_z.
\]

Scaling/similarity recurrence is translation in \(q\) at fixed \(z\).

---

## 2. Wedge local energy variables

Define the scale-normalized energy density

\[
\boxed{
E(z,q,\omega)
:=\frac12|F(z,q,\omega)|^2.
}
\]

Since the physical energy density is

\[
e=\frac12|u|^2=r^{-2}E,
\]

its gradient is

\[
\nabla e
=r^{-3}\mathfrak G_2E,
\]

where

\[
\boxed{
\mathfrak G_2E
:=
e_r(\mathfrak D-2)E+\nabla_{S^2}E.
}
\]

Define the scale-normalized energy-flux vector

\[
\boxed{
\mathcal J
:=(E+H)F-\mathfrak G_2E.
}
\]

Then the physical local-energy flux is

\[
J=r^{-3}\mathcal J.
\]

---

## 3. Wedge dissipation density

For the vector field \(u=r^{-1}F\),

\[
|\nabla u|^2
=r^{-4}\mathcal D_F,
\]

with

\[
\boxed{
\mathcal D_F
:=
|(\mathfrak D-1)F|^2
+|\nabla_{S^2}F|^2
\ge0.
}
\]

Here the angular derivative is understood componentwise/ambiently on the sphere.

---

## 4. Exact wedge local-energy equality

For the smooth ancient solution,

\[
\partial_se+\nabla\cdot J=-|\nabla u|^2.
\]

Because

\[
\partial_se=-r^{-4}\partial_zE,
\]

and for a vector field \(r^{-3}\mathcal J\),

\[
\nabla\cdot(r^{-3}\mathcal J)
=r^{-4}
\left[
(\mathfrak D-1)\mathcal J_r
+\operatorname{div}_{S^2}\mathcal J_T
\right],
\]

we obtain

\[
-\partial_zE
+(\mathfrak D-1)\mathcal J_r
+\operatorname{div}_{S^2}\mathcal J_T
=-\mathcal D_F.
\]

Thus

\[
\boxed{
\partial_zE
=
(\mathfrak D-1)\mathcal J_r
+\operatorname{div}_{S^2}\mathcal J_T
+\mathcal D_F.
}
\]

This is an exact pointwise local-energy identity on the wedge.

---

## 5. Ergodic q-average

Let \(\langle\cdot\rangle_q\) denote the invariant/ergodic mean under \(q\)-translations and integrate over \(S^2\).

Define

\[
\boxed{
\mathscr E(z)
:=
\left\langle
\int_{S^2}E\,d\omega
\right\rangle_q,
}
\]

\[
\boxed{
\mathscr J(z)
:=
\left\langle
\int_{S^2}\mathcal J_r\,d\omega
\right\rangle_q,
}
\]

and

\[
\boxed{
\mathscr D(z)
:=
\left\langle
\int_{S^2}\mathcal D_F\,d\omega
\right\rangle_q
\ge0.
}
\]

Stationarity gives

\[
\langle\partial_q\mathcal J_r\rangle_q=0,
\]

while the sphere divergence integrates to zero.

Since

\[
\mathfrak D\mathcal J_r
=
\partial_q\mathcal J_r
-2z\partial_z\mathcal J_r,
\]

we obtain

\[
\boxed{
\mathscr E'(z)
+2z\mathscr J'(z)
+\mathscr J(z)
=
\mathscr D(z).
}
\]

This is the exact q-averaged wedge energy ODE.

---

## 6. Equivalent total derivative form

Define

\[
\mathscr K(z)
:=
\mathscr E(z)+2z\mathscr J(z).
\]

Then

\[
\mathscr K'
=
\mathscr E'+2\mathscr J+2z\mathscr J'
=
\mathscr D+\mathscr J.
\]

Therefore

\[
\boxed{
\frac d{dz}
\left(
\mathscr E+2z\mathscr J
\right)
=
\mathscr D+\mathscr J.
}
\]

This form is potentially useful if the sign or endpoint behavior of \(\mathscr J\) can be controlled.

---

## 7. Recovery of the terminal payer identity

At \(z=0\),

\[
F(0,q,\omega)=A(q,\omega),
\]

and

\[
\partial_zF(0,q,\omega)=C(q,\omega).
\]

Hence

\[
\boxed{
\mathscr E'(0)
=
\left\langle
\int_{S^2}A\cdot C\,d\omega
\right\rangle.
}
\]

Also

\[
\boxed{
\mathscr J(0)=\langle\Phi_E\rangle,
}
\]

and

\[
\boxed{
\mathscr D(0)=\langle\mathcal D_A\rangle.
}
\]

The wedge ODE at \(z=0\) therefore gives

\[
\boxed{
\langle\mathcal D_A\rangle
=
\langle\Phi_E\rangle
+
\left\langle\int A\cdot C\right\rangle,
}
\]

exactly reproducing M5-575.

Thus M5-575 is not an isolated terminal-shell identity; it is the boundary trace of the full wedge energy transport.

---

## 8. Relation to similarity variables

Since

\[
z=|y|^{-2},
\]

fixing \(z\) fixes a similarity radius

\[
|y|=z^{-1/2}.
\]

At fixed \(z\), translation in \(q\) is equivalent to similarity-time translation because

\[
q=\log|y|-\theta/2.
\]

Therefore \(\mathscr E(z)\), \(\mathscr J(z)\), and \(\mathscr D(z)\) are time-averaged similarity-sphere quantities expressed as functions of scale-invariant depth.

The old separation between a recurrent core and a passive terminal tail is now replaced by one radial-depth transport ledger.

---

## 9. What the ODE does not yet prove

Although

\[
\mathscr D(z)\ge0,
\]

the ODE does not give monotonicity of \(\mathscr E\) because the radial energy-flux function \(\mathscr J\) has no known fixed sign on the dynamic branch.

Likewise,

\[
\mathscr K'=\mathscr D+\mathscr J
\]

is not one-sign unless \(\mathscr J\) can be controlled.

Therefore q-averaging removes the recurrence derivative but does not by itself create a Lyapunov function.

---

## 10. New reduced target

The dynamic terminal payer problem has been lifted from one boundary equation to

\[
\boxed{
\mathscr E'
+2z\mathscr J'
+\mathscr J
=
\mathscr D
\ge0
\qquad(z>0).
}
\]

The next high-value task is to combine this with:

1. the q-averaged wedge momentum equation;
2. the finite-enstrophy/similarity-vorticity bounds translated into endpoint conditions as \(z\to0\) and \(z\to\infty\);
3. the positive terminal densities \(c_3,c_\omega,c_C\).

A contradiction would require showing that the boundary data at \(z=0\) and the regular Type-I core behavior at \(z=\infty\) cannot be connected by this one-dimensional averaged transport system.

Status: **THE FULL ENERGY PART OF THE RECURRENT HARD CORE HAS BEEN REDUCED TO AN EXACT z-ODE AFTER ERGODIC q-AVERAGING. GLOBAL REGULARITY REMAINS UNPROVED.**