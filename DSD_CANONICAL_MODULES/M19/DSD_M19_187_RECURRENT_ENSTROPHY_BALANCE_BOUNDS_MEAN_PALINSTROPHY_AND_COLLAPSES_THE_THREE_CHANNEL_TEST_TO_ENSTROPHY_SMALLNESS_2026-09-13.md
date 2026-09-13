# M19-187 — Recurrent enstrophy balance bounds mean palinstrophy and collapses the three-channel test to enstrophy smallness

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / FURTHER PARAMETER REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Background recurrent enstrophy identity

For the background similarity vorticity,

\[
\frac12 Z_U'
+\frac14Z_U
+\nu P_U
=\int\Omega\cdot S_U\Omega.
\]

On a compact recurrent invariant component, long-time averaging gives

\[
\boxed{
\frac14\overline Z_U
+\nu\overline P_U
=
\left\langle\int\Omega\cdot S_U\Omega\right\rangle.
}
\]

Set

\[
\Pi:=\overline P_U.
\]

## 2. Stretching is sublinear in palinstrophy

Calderon--Zygmund gives

\[
\|S_U\|_3\lesssim\|\Omega\|_3.
\]

Hence

\[
\left|
\int\Omega\cdot S_U\Omega
\right|
\le
\|S_U\|_3\|\Omega\|_3^2
\lesssim
\|\Omega\|_3^3.
\]

Interpolate between `L2` and `L6`:

\[
\|\Omega\|_3
\le
\|\Omega\|_2^{1/2}\|\Omega\|_6^{1/2}
\lesssim
Z_U^{1/4}P_U^{1/4}.
\]

Therefore

\[
\boxed{
\left|
\int\Omega\cdot S_U\Omega
\right|
\le
C_E Z_U^{3/4}P_U^{3/4}.
}
\]

If

\[
Z_U(s)\le Z_+,
\]

then temporal concavity gives

\[
\frac14\overline Z_U+\nu\Pi
\le
C_E Z_+^{3/4}\Pi^{3/4}.
\]

Dropping the nonnegative enstrophy term,

\[
\nu\Pi
\le
C_E Z_+^{3/4}\Pi^{3/4}.
\]

For `Pi>0`,

\[
\boxed{
\Pi
\le
C_E^4\nu^{-4}Z_+^3.
}
\]

The `Pi=0` case is already contained in the low-activity branch.

## 3. Insert into the three-channel criterion

M19-186 gives the sufficient condition

\[
K_1\nu^{-3/2}Z_+^{7/8}\Pi^{3/8}
+
K_2\nu^{-1/3}\Pi^{2/3}
<\frac14.
\]

Using

\[
\Pi\le C_E^4\nu^{-4}Z_+^3,
\]

the first term satisfies

\[
K_1\nu^{-3/2}Z_+^{7/8}\Pi^{3/8}
\le
K_1C_E^{3/2}\nu^{-3}Z_+^2.
\]

The second satisfies

\[
K_2\nu^{-1/3}\Pi^{2/3}
\le
K_2C_E^{8/3}\nu^{-3}Z_+^2.
\]

Therefore define

\[
\boxed{
K_*:=K_1C_E^{3/2}+K_2C_E^{8/3}.
}
\]

Then

\[
\boxed{
K_*\frac{Z_+^2}{\nu^3}<\frac14
\Longrightarrow
N\le1.
}
\]

## 4. Consequence

Inside the certified recurrent hard corridor, sufficiently small dimensionless enstrophy ceiling

\[
\boxed{
\frac{Z_+^2}{\nu^3}
}
\]

forces quotient hard dimension at most one and hence, by M19-173,

\[
\boxed{
\text{relative-periodic dynamics after at most two quotient returns}.
}
\]

## 5. Complementary branch

A genuinely aperiodic hard survivor must therefore satisfy the explicit amplitude floor

\[
\boxed{
\frac{Z_+^2}{\nu^3}
\ge
\frac1{4K_*}.
}
\]

Thus the aperiodic branch is not merely high mean-palinstrophy; it is also a **large-enstrophy-amplitude recurrent branch** in the current normalized corridor.

## 6. Firewall

The retained W1/critical corridor provides finite `Z_+`, not universal smallness of `Z_+^2/nu^3`.

Therefore

\[
\boxed{
\text{finite enstrophy ceiling}
\neq
\text{small-enstrophy dimension-one closure}.
}
\]

M19-187 is a parameter reduction and conditional theorem, not unconditional closure.

---

\[
\boxed{\text{M19-187: THE APERIODIC DIMENSION TEST CAN BE STATED USING ONLY THE ENSTROPHY CEILING.}}
\]
