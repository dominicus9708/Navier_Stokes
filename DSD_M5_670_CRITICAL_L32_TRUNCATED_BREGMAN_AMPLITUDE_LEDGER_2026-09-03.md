# DSD M5-670 — Critical L^{3/2} truncated Bregman amplitude ledger

Date: 2026-09-03

Status: **INTERNAL SCALE-CRITICAL AMPLITUDE LEDGER / THE GENERAL CONVEX RENORMALIZED AMPLITUDE IDENTITY HAS A DISTINGUISHED HOMOGENEITY `p=3/2`, THE SCALE-CRITICAL VORTICITY EXPONENT / USING THE BREGMAN TRUNCATION `Psi_a(rho)=rho^(3/2)-a^(3/2)-(3/2)a^(1/2)(rho-a)` ABOVE `a`, WITH ZERO VALUE BELOW, REMOVES THE LEVEL-SURFACE DISTRIBUTION AND LEAVES AN EXACT LEDGER WITH A STRICT `a^(1/2) M_a` TERM PLUS MAGNITUDE/DIRECTION DIFFUSION / THE RIGHT SIDE REMAINS A WEIGHTED AXIAL-STRETCHING PRODUCTION TERM, SO THIS IS NOT YET A LYAPUNOV CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. General convex amplitude identity

Let `Phi:[0,infty)->R` be a sufficiently smooth convex function with enough truncation at small amplitude to make all integrals finite.

On CE-H,

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\qquad
\nabla\cdot B=\frac32.
\]

Hence

\[
\frac d{d\theta}\int\Phi(\rho)dy
=
\int\Phi'(\rho)(\sigma+\kappa-1)\rho\,dy
+
\frac32\int\Phi(\rho)dy.
\]

Use the parallel elliptic equation

\[
\kappa\rho
=\Delta\rho-\rho|\nabla\xi|^2.
\]

Integration by parts gives

\[
\boxed{
\begin{aligned}
\frac d{d\theta}\int\Phi(\rho)dy
={}&
\int\sigma\rho\Phi'(\rho)dy
+
\int\left(\frac32\Phi(\rho)-\rho\Phi'(\rho)\right)dy\\
&-
\int\Phi''(\rho)|\nabla\rho|^2dy
-
\int\rho\Phi'(\rho)|\nabla\xi|^2dy.
\end{aligned}
}
\]

This is the master renormalized-amplitude identity.

---

## 2. Distinguished exponent

For a pure power

\[
\Phi(\rho)=\rho^p,
\]

the linear similarity coefficient is

\[
\frac32-p.
\]

Therefore the distinguished scale-critical exponent is

\[
\boxed{p=\frac32.}
\]

This is exactly the vorticity exponent invariant under the three-dimensional Navier--Stokes scaling.

The untruncated global quantity `int rho^(3/2)` need not be finite on the current critical tail, so a positive-threshold version is required.

---

## 3. Critical Bregman truncation

For fixed `a>0`, define

\[
\boxed{
\Psi_a(\rho)
:=
\begin{cases}
\rho^{3/2}-a^{3/2}-\frac32a^{1/2}(\rho-a),&\rho>a,\\
0,&0\le\rho\le a.
\end{cases}
}
\]

This is the Bregman remainder of the convex function `rho^(3/2)` at the tangent point `a`.

It satisfies

\[
\boxed{
\Psi_a(a)=0,
\qquad
\Psi_a'(a)=0.
}
\]

Thus both the density and its first derivative match continuously at the threshold, eliminating level-surface delta terms.

For `rho>a`,

\[
\Psi_a'(\rho)
=\frac32(\sqrt\rho-\sqrt a),
\]

and

\[
\Psi_a''(\rho)
=\frac34\rho^{-1/2}.
\]

---

## 4. Linear similarity remainder

For `rho>a`, compute

\[
\frac32\Psi_a(\rho)-\rho\Psi_a'(\rho).
\]

Using the explicit expression,

\[
\boxed{
\frac32\Psi_a(\rho)-\rho\Psi_a'(\rho)
=-\frac34a^{1/2}(\rho-a).
}
\]

Thus the exact critical homogeneity cancellation leaves a strictly negative threshold correction rather than a bulk similarity term.

---

## 5. Exact critical truncated ledger

Define

\[
\boxed{
\mathcal C_a(\theta)
:=
\int_{\mathbb R^3}\Psi_a(\rho(y,\theta))dy.
}
\]

Also recall

\[
M_a=\int(\rho-a)_+dy.
\]

Substituting `Psi_a` into the master identity gives

\[
\boxed{
\begin{aligned}
\mathcal C_a'
&+
\frac34a^{1/2}M_a
+
\frac34\int_{\rho>a}\rho^{-1/2}|\nabla\rho|^2dy\\
&+
\frac32\int_{\rho>a}
\rho(\sqrt\rho-\sqrt a)|\nabla\xi|^2dy\\
&=
\frac32\int_{\rho>a}
\sigma\rho(\sqrt\rho-\sqrt a)dy.
\end{aligned}
}
\]

Every term is finite for fixed `a>0` on the all-order compact hull.

---

## 6. Definitions

Set

\[
\boxed{
D_{a,mag}^{crit}
:=
\frac34\int_{\rho>a}\rho^{-1/2}|\nabla\rho|^2dy,
}
\]

\[
\boxed{
D_{a,dir}^{crit}
:=
\frac32\int_{\rho>a}
\rho(\sqrt\rho-\sqrt a)|\nabla\xi|^2dy,
}
\]

and

\[
\boxed{
Q_a^{crit}
:=
\frac32\int_{\rho>a}
\sigma\rho(\sqrt\rho-\sqrt a)dy.
}
\]

Then

\[
\boxed{
\mathcal C_a'
+
\frac34a^{1/2}M_a
+
D_{a,mag}^{crit}
+
D_{a,dir}^{crit}
=
Q_a^{crit}.
}
\]

---

## 7. Recurrent average

`C_a` is a bounded observable for every fixed positive threshold.

Hence on an invariant recurrent component,

\[
\boxed{
\langle Q_a^{crit}\rangle
=
\frac34a^{1/2}\langle M_a\rangle
+
\langle D_{a,mag}^{crit}\rangle
+
\langle D_{a,dir}^{crit}\rangle.
}
\]

For the retained carrier threshold `a0`, the right side has a uniform positive floor.

Thus the CE-H hard branch carries a strict **scale-critical high-amplitude stretching payer**.

---

## 8. Relation to physical critical regularity

The exponent `3/2` is distinguished because physical vorticity obeys the scale-invariant norm

\[
\|\omega\|_{L^{3/2}}.
\]

If the untruncated global quantity were finite and uniformly controlled on a suitable backward sequence, Biot--Savart/HLS would place velocity in the critical `L^3` class and reconnect to known critical regularity/Liouville theory.

The current hard survivor avoids that closure precisely through the low-amplitude critical tail identified in M5-527--540.

The present positive-threshold functional isolates the active core without assuming away that tail.

---

## 9. Firewall

The critical truncation does **not** create a strict Lyapunov function.

The weighted stretching term `Q_a^crit` can exactly pay the threshold, magnitude, and direction costs on a recurrent compact state space.

Thus one must not infer contradiction from positivity of the left-hand costs alone.

The new value is that the fixed-threshold active-core ledger is now written at the exact Navier--Stokes critical homogeneity.

---

## 10. Updated target

The active hard core simultaneously exhibits, at one fixed threshold `a0`,

\[
\boxed{
\langle Q_{a_0}^{crit}\rangle>0,
}
\]

strict net downward material amplitude current from M5-668--669, and positive-frequency dynamic sheet/force/sheath events from M5-665.

A genuine closure would require showing that upward carrier reconstruction cannot simultaneously satisfy the critical production ledger and bounded material-flux recurrence.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
