# DSD M19-121 — The top-m transverse Lyapunov sum is bounded by the compact-core Ky-Fan budget minus the m/4 vorticity gap

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-102 EXTENDED FROM ZERO CENTER TO THE FULL NONNEGATIVE TRANSVERSE SPECTRUM / HYPERBOLIC APERIODIC RECURRENCE REQUIRES ENOUGH POSITIVE COMPACT-CORE SPECTRAL WEIGHT TO OVERCOME ONE QUARTER PER TRANSVERSE DIMENSION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Corrected target after M19-120

After quotienting exact rotations and separating the flow tangent, let

\[
\lambda_1^\perp\ge\lambda_2^\perp\ge\cdots
\]

be the symmetry-transverse Lyapunov exponents of the finite-dimensional nonnegative cocycle supplied by M19-095.

M19-120 shows that the correct aperiodic-rigidity target is not merely absence of extra zero exponents but

\[
\boxed{
\lambda_1^\perp<0.
}
\]

Indeed any positive transverse exponent may support hyperbolic aperiodic recurrence even when the center itself is one-dimensional.

---

## 2. m-volume evolution

Let

\[
\eta_1(s),\ldots,\eta_m(s)
\]

be an orthonormal moving vorticity frame spanning the Oseledets m-plane associated with the top `m` transverse exponents.

The linearized vorticity equation has the form

\[
\partial_s\eta
=\mathcal L_0\eta+\mathcal K(s)\eta,
\]

with

\[
\langle\eta,\mathcal L_0\eta\rangle
=-\nu\|\nabla\eta\|_2^2-\frac14\|\eta\|_2^2.
\]

Let

\[
\mathcal K_s^{sym}
=\frac12(\mathcal K(s)+\mathcal K(s)^*).
\]

The logarithmic derivative of the induced m-volume is

\[
\frac d{ds}\log\operatorname{Vol}_m
=
-\frac m4
-\nu\sum_{j=1}^m\|\nabla\eta_j\|_2^2
+\sum_{j=1}^m
\langle\eta_j,\mathcal K_s^{sym}\eta_j\rangle.
\]

Taking long-time average gives

\[
\boxed{
\sum_{j=1}^m\lambda_j^\perp
=
-\frac m4
-\nu\left\langle\sum_{j=1}^m\|\nabla\eta_j\|_2^2\right\rangle
+\left\langle
\operatorname{Tr}(P_m\mathcal K_s^{sym}P_m)
\right\rangle.
}
\]

---

## 3. Ky-Fan upper bound

Let

\[
\lambda_1^+(s)\ge\lambda_2^+(s)\ge\cdots\ge0
\]

be the positive eigenvalues of the compact self-adjoint operator

\[
(\mathcal K_s^{sym})_+.
\]

The Ky-Fan principle gives

\[
\operatorname{Tr}(P_m\mathcal K_s^{sym}P_m)
\le
\sum_{j=1}^m\lambda_j^+(s).
\]

Hence

\[
\boxed{
\sum_{j=1}^m\lambda_j^\perp
\le
-\frac m4
-\nu\left\langle\sum_{j=1}^m\|\nabla\eta_j\|_2^2\right\rangle
+\left\langle\sum_{j=1}^m\lambda_j^+(s)\right\rangle.
}
\]

Dropping the favorable gradient term yields the simpler necessary estimate

\[
\boxed{
\sum_{j=1}^m\lambda_j^\perp
\le
-\frac m4
+\left\langle\sum_{j=1}^m\lambda_j^+(s)\right\rangle.
}
\]

---

## 4. Necessary condition for any nonnegative transverse exponent

If

\[
\lambda_1^\perp\ge0,
\]

then for some `m>=1` the partial sum of the leading nonnegative exponents is nonnegative. Therefore necessarily

\[
\boxed{
\left\langle\sum_{j=1}^m\lambda_j^+(s)\right\rangle
\ge
\frac m4.
}
\]

Thus the quarter-gap budget of M19-102 is not merely a zero-center condition. It is a necessary condition for **any** nonnegative transverse spectral block.

In particular, the sufficient condition

\[
\boxed{
\left\langle\lambda_1^+(s)\right\rangle<\frac14
}
\]

implies

\[
\boxed{
\lambda_1^\perp<0
}
\]

and therefore eliminates both extra center and unstable hyperbolic directions.

---

## 5. Uniform compact-tail consequence

By M19-102, the positive eigenvalue tails of the compact core coupling are uniformly small over the recurrent hull.

Hence only finitely many eigenchannels can participate in any nonnegative transverse block.

Therefore

\[
\boxed{
\dim E^{\ge0}_\perp<\infty
}

with an explicit finite-dimensional Ky-Fan budget.

This was already qualitatively implied by M19-095; the present module identifies the exact per-dimension spectral price:

\[
\boxed{
\text{one quarter of positive core spectral weight per nonnegative transverse dimension.}
}
\]

---

## 6. Hyperbolic recurrence interpretation

A hyperbolic aperiodic recurrent component with `u>=1` unstable dimensions must satisfy

\[
\lambda_1^\perp+\cdots+\lambda_u^\perp>0.
\]

Hence its compact-core symmetric coupling must obey

\[
\boxed{
\left\langle\sum_{j=1}^u\lambda_j^+(s)\right\rangle
>
\frac u4
}
\]

up to the additionally favorable viscous gradient payment.

Thus hyperbolic recurrence is not a free loophole: it requires persistent compact-core amplification strong enough to beat the quarter-gap in every unstable direction.

---

## 7. Revised live theorem

The corrected aperiodic theorem can be written purely as a Ky-Fan inequality:

\[
\boxed{
\mathcal T_{transverse}:
\forall m\ge1,
\quad
\left\langle\sum_{j=1}^m\lambda_j^+(s)\right\rangle
<
\frac m4
+
\nu\left\langle\sum_{j=1}^m\|\nabla\eta_j\|_2^2\right\rangle
}
\]

for every symmetry-transverse Oseledets m-plane.

A stronger but easier sufficient target is

\[
\boxed{
\left\langle\lambda_1^+(s)\right\rangle<\frac14.
}
\]

Neither inequality is currently proved.

---

## 8. Firewall

A finite number of positive compact-core eigenchannels may exist without violating any currently certified unsigned derivative budget.

Therefore

\[
\boxed{
\text{quasi-compactness + quarter-gap}
\neq
\text{transverse stability}.
}
\]

The remaining problem is finite-dimensional but genuine.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
