# DSD M5-572 — First Parabolic Terminal Jet and Stationary Residual

Date: 2026-09-02

Status: **THE LEADING 1/r TERMINAL PROFILE DOES NOT OBEY AN AUTONOMOUS STATIONARY NS EQUATION. ITS STATIONARY RESIDUAL IS EXACTLY ABSORBED BY THE FIRST (-s)/r^3 PARABOLIC CORRECTION. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Why this audit is needed

M5-571 upgrades the hard tail to a stationary ergodic log-radius process \(A(q,\omega)\) with positive mean cubic and vorticity densities.

It is tempting to insert

\[
u_0=r^{-1}A
\]

into a stationary Navier-Stokes balance and try to derive a contradiction on each log cell.

That inference is not valid for a time-dependent ancient solution. The first subcritical far-field coefficient contributes to the time derivative at exactly the same spatial order as viscosity, nonlinearity, and pressure acting on the leading \(1/r\) field.

This note computes that coefficient explicitly.

---

## 2. Two-term physical far-field expansion

Let

\[
a=-s>0,
\qquad
q=\log r.
\]

The similarity scattering expansion from M5-567/M5-568 has the physical form

\[
\boxed{
u(x,s)
=
 r^{-1}A(q,\omega)
+a r^{-3}C(q,\omega)
+O(a^2r^{-5})
}
\]

in the parabolic far-field regime

\[
r^2\gg a.
\]

Similarly write

\[
\boxed{
p(x,s)
=
 r^{-2}P(q,\omega)
+a r^{-4}Q(q,\omega)
+O(a^2r^{-6}).
}
\]

The leading coefficient \(A\) is independent of physical ancient time \(s\); time dependence begins in the coefficient multiplied by \(a=-s\).

---

## 3. Time derivative order

Since

\[
\partial_s a=-1,
\]

we obtain

\[
\boxed{
\partial_s u
=
-r^{-3}C
+O(ar^{-5}).
}
\]

Thus the first time derivative is already of order \(r^{-3}\).

But for \(u_0=r^{-1}A\),

\[
\Delta u_0=O(r^{-3}),
\qquad
(u_0\cdot\nabla)u_0=O(r^{-3}),
\qquad
\nabla p_0=O(r^{-3}).
\]

All four Navier-Stokes terms therefore enter at the **same** first nontrivial far-field order.

---

## 4. Log-spherical operators

For a scalar/cartesian component \(f(q,\omega)\),

\[
\Delta(r^{-1}f)
=
r^{-3}
\left[
\partial_q(\partial_q-1)+\Delta_{S^2}
\right]f.
\]

Define the componentwise operator

\[
\boxed{
\mathcal L_{-1}
:=
\partial_q(\partial_q-1)+\Delta_{S^2}.
}
\]

For the pressure,

\[
\nabla(r^{-2}P)
=
r^{-3}\mathcal G_{-2}P,
\]

where

\[
\boxed{
\mathcal G_{-2}P
:=
e_r(\partial_q-2)P+\nabla_{S^2}P.
}
\]

Let \(\mathcal N(A)\) denote the log-spherical coefficient of

\[
(r^{-1}A\cdot\nabla)(r^{-1}A)
=
r^{-3}\mathcal N(A).
\]

---

## 5. Exact first terminal-jet equation

At order \(r^{-3}\), the Navier-Stokes equation

\[
\partial_su+(u\cdot\nabla)u
=-\nabla p+\Delta u
\]

gives

\[
-C+\mathcal N(A)
=
-\mathcal G_{-2}P
+\mathcal L_{-1}A.
\]

Therefore

\[
\boxed{
C
=
-\mathcal L_{-1}A
+\mathcal N(A)
+\mathcal G_{-2}P.
}
\]

The right-hand side is exactly the stationary Navier-Stokes residual of the leading critical field \(r^{-1}A\).

Define

\[
\boxed{
\mathcal R_{stat}[A,P]
:=
-\mathcal L_{-1}A
+\mathcal N(A)
+\mathcal G_{-2}P.
}
\]

Then

\[
\boxed{C=\mathcal R_{stat}[A,P].}
\]

---

## 6. Divergence constraint for the correction

For a vector field \(r^{-3}C\), incompressibility gives

\[
\boxed{
(\partial_q-1)C_r
+\operatorname{div}_{S^2}C_T
=0.
}
\]

This is automatically required of the stationary residual after pressure is chosen consistently with incompressibility.

---

## 7. DSD anti-shortcut conclusion

The implication

\[
\text{time-independent leading coefficient }A
\Longrightarrow
\mathcal R_{stat}[A,P]=0
\]

is false.

The correct implication is

\[
\boxed{
\mathcal R_{stat}[A,P]
=
C,
}
\]

and the first parabolic correction supplies the exact time derivative needed to balance a nonzero stationary residual.

Thus a renormalized one-cell balance built from \(A\) alone cannot prove stationarity or contradiction.

---

## 8. Two genuine terminal-jet branches

The hard tail now splits into two mathematically distinct subbranches.

### Branch S — asymptotically stationary critical trace

\[
\boxed{C=0.}
\]

Then

\[
\mathcal R_{stat}[A,P]=0,
\]

so the leading \(1/r\) field solves the stationary NS equation on the log-cylinder/exterior asymptotic class.

This branch must be compared with known stationary critical profiles, including Landau-type exterior profiles, before any Liouville claim is made.

### Branch J — genuinely parabolic terminal jet

\[
\boxed{C\neq0.}
\]

Then the leading critical trace is not stationary; its residual is stored in the first \((-s)/r^3\) correction.

The correct recurrent object is therefore the joint log-radius process

\[
\boxed{(A,C),}
\]

not \(A\) alone.

---

## 9. Updated frontier

The tail reduction has advanced from

\[
\text{infinite critical shell stack}
\]

to

\[
\text{terminal profile }A
\]

and now to the first terminal jet

\[
\boxed{
(A,C),
\qquad
C=\mathcal R_{stat}[A,P].
}
\]

The next efficient calculation is:

1. classify the \(C=0\) stationary critical branch against known exterior stationary NS profiles and force/momentum-flux invariants;
2. for \(C\neq0\), push \(C\) through the invariant log-radius measure and derive whether positive mean residual density creates a controlled next-order budget or only another sign-indefinite recurrent channel.

Status: **THE LEADING TERMINAL TRACE IS NOT AUTONOMOUS. ANY PROOF THAT TREATS A AS A STATIONARY NS PROFILE WITHOUT FIRST SHOWING C=0 IS INVALID. GLOBAL REGULARITY REMAINS UNPROVED.**