# DSD Recurrent Betchov Frequency Window

Date: 2026-08-25

Status: **YOUNG-FREE AVERAGED FREQUENCY WINDOW DERIVED / NEW SCALAR CLOSURE TEST DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

This note continues the bounded-`Z` recurrent ancient/Leray branch and combines two repository results without using Young absorption at the final step:

1. recurrent enstrophy balance plus the positive-middle/Betchov split;
2. the global Betchov residual interpolation bound.

The aim is to retain the full nonlinear dependence on the mean frequency ratio instead of replacing it by a free Young parameter.

---

## 2. Recurrent residual requirement

Let

\[
Z(s)=\|W(s)\|_2^2,
\qquad
Q(s)=\|\nabla W(s)\|_2^2,
\]

and let `R_B(s)` be the negative-middle Betchov residual.

The recurrent Leray balance and first-hitting Type-I amplitude ceiling give

\[
\langle \mathcal R_B\rangle
\ge
\left(\frac14-\frac{K_I}{2}\right)\langle Z\rangle
+\nu\langle Q\rangle.
\]

Define

\[
\boxed{
\bar\lambda
:=
\frac{\langle Q\rangle}{\langle Z\rangle}
}
\]

and

\[
\boxed{
a_I:=\frac14-\frac{K_I}{2}.}
\]

Then every nonzero recurrent survivor satisfies

\[
\boxed{
\frac{\langle\mathcal R_B\rangle}{\langle Z\rangle}
\ge
a_I+\nu\bar\lambda.
}
\]

The existing recurrent active-core argument also supplies

\[
\boxed{\bar\lambda\ge c_{\log}>0.}
\]

---

## 3. Global cubic residual upper bound

The exact determinant identity and Sobolev interpolation give pointwise in Leray time

\[
\mathcal R_B
\le
C_B Z^{3/4}Q^{3/4},
\]

where

\[
C_B=\frac4{3\sqrt3}C_S^{3/2}.
\]

Using the sharp homogeneous Sobolev constant already used in the repository,

\[
C_S
=
\frac1{\sqrt3}\left(\frac2\pi\right)^{2/3},
\]

one obtains

\[
\boxed{
C_B
=
\frac{8}{\pi\,3^{9/4}}
\approx0.21498952055.
}
\]

Assume the bounded-`Z` branch has

\[
0<Z(s)\le Z_+.
\]

Write

\[
\lambda(s):=\frac{Q(s)}{Z(s)}.
\]

Then

\[
Z^{3/4}Q^{3/4}
=Z^{3/2}\lambda^{3/4}
\le
Z_+^{1/2}Z\lambda^{3/4}.
\]

Hence

\[
\langle\mathcal R_B\rangle
\le
C_BZ_+^{1/2}
\langle Z\lambda^{3/4}\rangle.
\]

Introduce the probability weight

\[
d\mu_Z
:=
\frac{Z(s)\,ds}{\langle Z\rangle}.
\]

Because `x^(3/4)` is concave, Jensen gives

\[
\frac{\langle Z\lambda^{3/4}\rangle}{\langle Z\rangle}
\le
\left(
\frac{\langle Z\lambda\rangle}{\langle Z\rangle}
\right)^{3/4}.
\]

But

\[
Z\lambda=Q,
\]

so

\[
\boxed{
\frac{\langle\mathcal R_B\rangle}{\langle Z\rangle}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

This step contains no Young parameter.

---

## 4. Exact scalar frequency-window inequality

Combining the lower and upper residual bounds gives the necessary condition

\[
\boxed{
\nu\bar\lambda+a_I
\le
C_BZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

Equivalently, with

\[
\boxed{x:=\bar\lambda^{1/4}\ge0,}
\]

and

\[
\boxed{b:=C_BZ_+^{1/2},}
\]

every recurrent survivor must satisfy

\[
\boxed{
F(x):=\nu x^4-bx^3+a_I\le0.
}
\]

Together with the active-core frequency floor,

\[
\boxed{x\ge c_{\log}^{1/4}.}
\]

Thus recurrence is confined to a finite algebraic frequency window rather than merely being required to have positive frequency.

---

## 5. No-frequency-window closure criterion

For `x>0`,

\[
F'(x)=x^2(4\nu x-3b).
\]

The unique positive critical point is

\[
\boxed{x_*:=\frac{3b}{4\nu}.}
\]

It is the global positive minimum, and

\[
F(x_*)
=
a_I-
\frac{27}{256}\frac{b^4}{\nu^3}.
\]

Since

\[
b^4=C_B^4Z_+^2,
\]

and

\[
\frac{27}{256}C_B^4
=
\boxed{\frac{16}{729\pi^4}},
\]

we obtain

\[
\boxed{
F(x_*)
=
\frac14-\frac{K_I}{2}
-
\frac{16}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
}
\]

Therefore the recurrent bounded-`Z` branch is impossible whenever

\[
\boxed{
\frac14-\frac{K_I}{2}
>
\frac{16}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
}
\]

Equivalently,

\[
\boxed{
K_I
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<
\frac12.
}
\]

This is exactly the zero-frequency-tax endpoint of the previous global Betchov absorption certificate, now recovered as the statement that the algebraic frequency window is empty.

---

## 6. Frequency-floor closure beyond the empty-window test

Even when the polynomial has an allowed interval, the active-core lower bound may lie above it.

Define

\[
\mathcal A
:=
\{x\ge0:F(x)\le0\}.
\]

Every recurrent survivor must satisfy

\[
\boxed{
\mathcal A\cap[c_{\log}^{1/4},\infty)\ne\varnothing.
}
\]

Therefore a second exact closure certificate is

\[
\boxed{
F(x)>0
\quad\text{for every }x\ge c_{\log}^{1/4}
\quad\Longrightarrow\quad
\text{no recurrent survivor}.
}
\]

When `a_I>=0`, the necessary inequality immediately implies

\[
\nu\bar\lambda
\le
b\bar\lambda^{3/4},
\]

so

\[
\boxed{
\bar\lambda
\le
\left(\frac b\nu\right)^4
=
C_B^4\frac{Z_+^2}{\nu^4}.
}
\]

Hence for `K_I<=1/2`, a convenient sufficient contradiction is

\[
\boxed{
c_{\log}
>
C_B^4\frac{Z_+^2}{\nu^4}.
}
\]

This criterion is not claimed optimal; the quartic test above is the exact one.

---

## 7. Interpretation

The recurrent bounded-`Z` branch cannot arbitrarily increase its mean palinstrophy frequency to pay the recurrent enstrophy tax.

The reason is that the same frequency that strengthens viscous payment enters the Betchov mismatch only sublinearly:

\[
\text{required residual}
\sim \nu\bar\lambda,
\]

while

\[
\text{available cubic residual}
\lesssim
Z_+^{1/2}\bar\lambda^{3/4}.
\]

Therefore

\[
\boxed{
\text{very high mean frequency is self-defeating.}
}
\]

This supplies an upper as well as lower frequency restriction.

---

## 8. DSD audit

The formed finite channels are:

- mean normalized enstrophy `⟨Z⟩`;
- mean palinstrophy `⟨Q⟩`;
- mean frequency ratio `bar lambda`;
- mean Betchov residual `⟨R_B⟩`;
- finite constants `K_I`, `Z_+`, `nu`.

No infinite derivative hierarchy or global velocity `L3` tail is promoted into the finite-stage object.

The critical tail is absent from the final inequality.

---

## 9. Updated frontier

The previous proposed comparison

\[
G_{rec}\stackrel? >G_{analytic,+}
\]

is not a generic closure mechanism: analyticity gives a finite upper derivative bound, while recurrence gives only a finite positive lower derivative requirement, and their constants need not conflict.

The higher-leverage scalar gate is instead

\[
\boxed{
\nu\bar\lambda
+\frac14-\frac{K_I}{2}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4},
\qquad
\bar\lambda\ge c_{\log}.
}
\]

The next calculation should substitute the best repository bounds for `K_I`, `Z_+`, and `c_log` into this exact algebraic window and determine which parameter is quantitatively responsible for survival.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
