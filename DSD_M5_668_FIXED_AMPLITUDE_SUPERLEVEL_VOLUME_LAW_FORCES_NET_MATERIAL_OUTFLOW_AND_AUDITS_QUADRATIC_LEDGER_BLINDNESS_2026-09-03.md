# DSD M5-668 — Fixed-amplitude superlevel volume law forces net material outflow; the quadratic ledger is boundary-turnover blind

Date: 2026-09-03

Status: **INTERNAL MOVING-LEVEL-SET LEDGER / FOR `Omega_a={rho>a}`, THE RELATIVE NORMAL SPEED BETWEEN THE MATERIAL FLOW `B` AND THE AMPLITUDE LEVEL SURFACE IS DETERMINED BY `D_B rho=(sigma+kappa-1)rho`; THE EXACT VOLUME LAW IS `V_a'=(3/2)V_a + a int_{rho=a}(sigma+kappa-1)/|grad rho| dS` / ON A RECURRENT COMPONENT THE SIGNED MATERIAL CROSSING TERM HAS STRICTLY NEGATIVE MEAN `-(3/2)<V_a>` / HOWEVER THE M5-666 QUADRATIC TRUNCATION VANISHES TO SECOND ORDER ON `rho=a` AND THEREFORE DELIBERATELY DOES NOT SEE THIS CROSSING TERM / THE TWO LEDGERS CANNOT BE COUNTED AS INDEPENDENT DISSIPATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed amplitude superlevel

Fix a positive regular amplitude level `a>0` and define

\[
\Omega_a(\theta):=\{y:\rho(y,\theta)>a\},
\qquad
V_a(\theta):=|\Omega_a(\theta)|.
\]

The outward unit normal of the superlevel is

\[
\boxed{n_a=-\frac{\nabla\rho}{|\nabla\rho|}.}
\]

Let `V_{partial a}` denote the velocity of the moving level surface `rho=a`.

---

## 2. Relative normal velocity

The level-set kinematics gives

\[
\partial_\theta\rho+V_{\partial a}\cdot\nabla\rho=0
\qquad\text{on }\rho=a.
\]

On CE-H,

\[
D_B\rho
=\partial_\theta\rho+B\cdot\nabla\rho
=(\sigma+\kappa-1)\rho.
\]

Hence on `rho=a`,

\[
(B-V_{\partial a})\cdot\nabla\rho
=a(\sigma+\kappa-1).
\]

Since `n_a=-grad rho/|grad rho|`,

\[
\boxed{
(V_{\partial a}-B)\cdot n_a
=
\frac{a(\sigma+\kappa-1)}{|\nabla\rho|}.
}
\]

This is the signed material-crossing speed through the amplitude level.

---

## 3. Exact superlevel-volume law

By Reynolds transport,

\[
V_a'
=
\int_{\partial\Omega_a}V_{\partial a}\cdot n_a\,dS.
\]

Split the surface velocity into the material velocity plus relative motion:

\[
V_a'
=
\int_{\partial\Omega_a}B\cdot n_a\,dS
+
\int_{\partial\Omega_a}(V_{\partial a}-B)\cdot n_a\,dS.
\]

Because

\[
\nabla\cdot B=\frac32,
\]

the first term is

\[
\frac32V_a.
\]

Therefore

\[
\boxed{
V_a'
=
\frac32V_a
+
a\int_{\rho=a}
\frac{\sigma+\kappa-1}{|\nabla\rho|}\,dS.
}
\]

Define the signed threshold-crossing term

\[
\boxed{
\mathcal T_a
:=
a\int_{\rho=a}
\frac{\sigma+\kappa-1}{|\nabla\rho|}\,dS.
}
\]

Then

\[
\boxed{V_a'=\frac32V_a+\mathcal T_a.}
\]

---

## 4. Recurrent mean

On the compact recurrent hull `V_a` is bounded.

Hence its invariant mean derivative vanishes:

\[
\langle V_a'\rangle=0.
\]

Therefore

\[
\boxed{
\langle\mathcal T_a\rangle
=-\frac32\langle V_a\rangle.
}
\]

For every retained high-amplitude level with positive recurrent volume,

\[
\boxed{\langle\mathcal T_a\rangle<0.}
\]

Thus material labels have a strict **net outward/downward amplitude crossing** through every recurrent positive-volume high-amplitude layer.

---

## 5. Absolute turnover split

Write

\[
\gamma:=\sigma+\kappa-1.
\]

Define

\[
\mathcal T_a^+
:=
a\int_{\rho=a}\frac{\gamma_+}{|\nabla\rho|}\,dS,
\qquad
\mathcal T_a^-
:=
a\int_{\rho=a}\frac{(-\gamma)_+}{|\nabla\rho|}\,dS.
\]

Then

\[
\mathcal T_a=\mathcal T_a^+-\mathcal T_a^-.
\]

Hence

\[
\boxed{
\langle\mathcal T_a^-\rangle
-
\langle\mathcal T_a^+\rangle
=
\frac32\langle V_a\rangle>0.
}
\]

The average downward/shedding crossing strictly exceeds the upward/replenishing crossing.

This is a signed statement, but it does not by itself prevent repeated re-entry of material labels.

---

## 6. Relation to the M5-666 quadratic observable

M5-666 uses

\[
N_a=\frac12\int(\rho-a)_+^2dy.
\]

The density and its first derivative with respect to the level-set indicator vanish at `rho=a` strongly enough that no moving-level boundary term survives.

Its exact equation is

\[
N_a'
+
\frac12N_a
+
aM_a
+
D_a^{(2)}
=
Q_a^{(2)}.
\]

Thus the level-crossing term `T_a` is absent.

This is not an omission in the derivation; it is a structural consequence of the quadratic truncation.

---

## 7. DSD audit: no double counting

One must not claim that

\[
D_a^{(2)}
\]

and

\[
\mathcal T_a^-
\]

are two independent irreversible costs merely because both are positive quantities associated with the same amplitude threshold.

The quadratic ledger is deliberately insensitive to first-order motion of the level surface.

Conversely, the volume ledger contains no elliptic gradient deficit like `D_a^(2)`.

The two identities resolve different pieces of the same recurrent dynamics.

---

## 8. New dynamic frontier

At the fixed carrier threshold `a0`, the hard CE-H survivor must now satisfy simultaneously

\[
\boxed{
\langle Q_{a_0}^{(2)}\rangle>0,
}
\]

and

\[
\boxed{
\langle\mathcal T_{a_0}\rangle
=-\frac32\langle V_{a_0}\rangle<0.
}
\]

Thus there is strict weighted axial production inside the layer while the material population of that layer has strict net turnover.

The remaining problem is not to prove that turnover exists; it is to determine whether the upward replenishment part `T_a^+` can indefinitely reconstruct the persistent fixed-flux carrier without violating a scale-invariant flux or sheet-resource constraint.

---

## 9. Next target

The natural next observable is the vorticity-magnitude-weighted superlevel quantity

\[
S_a:=\int_{\rho>a}\rho\,dy,
\]

because its moving-boundary term equals `a` times the material-volume crossing and therefore measures threshold turnover in the same units as vortex-line flux-weighted arclength.

This will test whether the negative elliptic `kappa` balance of M5-651 gives a signed constraint on the replenishing part.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
