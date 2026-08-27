# DSD M5-167 — Frozen Fast-Stable Principal Mode Monotone Damping

Date: 2026-08-27

Status: **P1_B^S FAST-NORMAL COMPATIBILITY / FOR EVERY FROZEN NORMAL DEPTH `a=e^-tau`, THE EXACT CONSTANT-COEFFICIENT CO-MOVING VORTICITY MODE EQUATION HAS A UNIQUE SLOW/STABLE ROOT WHOSE REAL PART IS MONOTONE NONINCREASING IN GENEALOGICAL FREQUENCY MAGNITUDE AND SPHERICAL DEGREE / THE FAST-NORMAL PRINCIPAL CHANNEL THEREFORE CANNOT PREFERENTIALLY AMPLIFY HIGH CROSS FREQUENCIES IN FORWARD EVOLUTION / ONLY NONAUTONOMOUS LAG AND VARIABLE FIRST-ORDER COUPLING REMAIN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Frozen principal equation

Ignore only the variable-coefficient relative transport/stretching term and freeze

\[
a=e^{-\tau}>0
\]

at one normal depth.

For a co-moving genealogical Fourier mode

\[
e^{i\omega q}
\]

and a spherical harmonic of degree `ell`, seek a local exponential normal mode

\[
F\sim e^{\lambda\tau}e^{i\omega q}Y_\ell.
\]

The exact frozen principal equation is

\[
\lambda
=
a\left[
4\nu(\lambda-i\omega)^2
-6\nu(\lambda-i\omega)
+\nu(2-\ell(\ell+1))
\right].
\]

Set

\[
y:=\lambda-i\omega,
\qquad
c_\ell:=2-\ell(\ell+1).
\]

Then

\[
4\nu a y^2
-(1+6\nu a)y
+\nu a c_\ell
-i\omega
=0.
\]

---

## 2. Slow and fast roots

Define

\[
A_a:=1+6\nu a
\]

and

\[
\boxed{
D_{\ell,\omega}(a)
:=
A_a^2
-16\nu^2a^2c_\ell
+16i\nu a\omega.
}
\]

The two roots are

\[
y_\pm
=
\frac{A_a\pm\sqrt{D_{\ell,\omega}}}{8\nu a}.
\]

As `a->0`, one root is of fast size `~(4 nu a)^-1`, while the minus root satisfies

\[
y_-\to-i\omega.
\]

Therefore the flat-selected stable/slow root is

\[
\boxed{
\lambda_s
=
i\omega
+
\frac{A_a-\sqrt{D_{\ell,\omega}}}{8\nu a}.
}
\]

The plus root is the fast growing normal mode excluded by the M5-146/M5-160 flat selection.

---

## 3. Real part of the slow root

Write

\[
D=d+iy,
\]

with

\[
d=A_a^2-16\nu^2a^2c_\ell>0,
\qquad
y=16\nu a\omega.
\]

For the principal square root,

\[
\boxed{
\operatorname{Re}\sqrt{d+iy}
=
\sqrt{
\frac{\sqrt{d^2+y^2}+d}{2}
}.
}
\]

Hence

\[
\boxed{
\operatorname{Re}\lambda_s
=
\frac{A_a-\operatorname{Re}\sqrt{D}}{8\nu a}.
}
\]

---

## 4. Monotonicity in genealogical frequency

For fixed `d>0`,

\[
\operatorname{Re}\sqrt{d+iy}
\]

is monotone increasing in `|y|`.

Since

\[
|y|=16\nu a|\omega|,
\]

we obtain

\[
\boxed{
|\omega_2|\ge|\omega_1|
\Rightarrow
\operatorname{Re}\lambda_s(\omega_2,\ell)
\le
\operatorname{Re}\lambda_s(\omega_1,\ell).
}
\]

Thus increasing genealogical frequency never increases the forward growth rate of the stable principal mode.

---

## 5. Monotonicity in spherical degree

Since

\[
c_\ell=2-\ell(\ell+1)
\]

decreases with `ell`, the real quantity

\[
d=A_a^2-16\nu^2a^2c_\ell
\]

increases with `ell`.

The real part of the square root increases with `d`, so

\[
\boxed{
\ell_2\ge\ell_1
\Rightarrow
\operatorname{Re}\lambda_s(\omega,\ell_2)
\le
\operatorname{Re}\lambda_s(\omega,\ell_1).
}
\]

Thus higher angular frequency is likewise no less damped.

---

## 6. Low-mode geometric growth does not affect the quotient mechanism

The lowest spherical modes can carry a bounded positive geometric growth contribution because of the vorticity similarity scaling.

This is a zeroth-order effect.  Subtracting the common lowest-mode growth rate from the generator leaves a nonnegative monotone damping symbol.

A common scalar growth/decay term cancels from the Dirichlet quotient

\[
\mathcal N=H/E.
\]

Therefore the result needed for M5-166 is the monotone *relative* damping with cross frequency, not absolute decay of every low mode.

---

## 7. Parabolic expansion

When

\[
a|\omega|\ll1
\]

and the angular degree is within the corresponding slow region, expansion of the slow root gives schematically

\[
\boxed{
\operatorname{Re}\lambda_s
=
O(a)
-c\nu a\bigl(4\omega^2+\ell(\ell+1)\bigr)
+
\text{higher slow terms}.
}
\]

In particular the parabolic scale required by M5-154,

\[
|\omega|,\ell\sim a^{-1/2},
\]

still satisfies

\[
a|\omega|\sim a^{1/2}\to0.
\]

Thus the required escape lies well inside the slow/fast separated regime, not near the fast spectral scale `a^-1`.

---

## 8. Consequence

For frozen `a`, the exact fast-stable principal dynamics is diagonal in the cross-section spectral representation and its stable growth rate is monotone decreasing with spectral frequency.

Therefore its contribution to a forward Dirichlet quotient is nonpositive after removal of harmless common zeroth-order growth.

This verifies the **principal frozen part** of the M5-166 compatibility edge.

---

## 9. Remaining compatibility pieces

Two effects are not yet included in this frozen calculation:

1. `a(\tau)=e^-tau` changes during the M5-160 future-kernel width;
2. variable-coefficient first-order transport/stretching couples different cross frequencies.

The second effect is already the M5-166 commutator term and has the desired first-order bound.

The remaining new task is therefore only to show that the nonautonomous stable-kernel lag does not create a positive frequency-production term larger than

\[
C e^{-\tau}(1+\mathcal N).
\]

---

## 10. DSD audit

### Formation — GREEN

The root is derived from the actual frozen co-moving vorticity principal equation.

### Axis — GREEN

Fast normal rate, genealogical frequency, and spherical degree are kept separate.

### Static aggregation — GREEN

Low-mode geometric growth is not confused with frequency transfer.

### Dynamics — GREEN / YELLOW

Frozen principal monotone damping is GREEN. Nonautonomous stable-kernel compatibility remains YELLOW.

### Cross-audit — GREEN

This result corrects the backward-amplification intuition without contradicting M5-164: backward reconstruction may amplify high modes, while actual forward stable evolution damps them more strongly.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
