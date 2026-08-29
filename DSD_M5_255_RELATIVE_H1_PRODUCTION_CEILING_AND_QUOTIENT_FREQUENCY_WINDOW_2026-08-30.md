# DSD M5-255 — Relative H1 Production Ceiling and Quotient-Frequency Window

Date: 2026-08-30

Parent: `DSD_M5_254_RELATIVE_VORTICITY_RECURRENT_H1_TAX_AND_FREQUENCY_CHAIN_2026-08-30.md`

Status: **SHARPENED CROSS-TERM ROUTING / THE APPARENT `1/sqrt(lambda_0)` LOSS IN THE RELATIVE-VORTICITY CROSS COUPLING IS REMOVED BY THE GLOBAL `L6` SOBOLEV ESTIMATE FOR `Q` AND AN `L3` BOUND ON THE CANONICAL-TAIL VORTICITY GRADIENT / THE RELATIVE H1 RECURRENCE TAX THEREFORE ADMITS AN ORDER-ZERO PRODUCTION CEILING `C_rel`; IF `C_rel < 1/4` THE RELATIVE RECURRENT QUOTIENT IS IMPOSSIBLE, WHILE `C_rel > 1/4` GIVES AN EXPLICIT UPPER FREQUENCY WINDOW WHICH COMBINES WITH THE M5-251 TIGHTNESS LOWER BOUND / GLOBAL REGULARITY UNPROVED.**

---

## 1. Relative H1 balance

From M5-254,

\[
\boxed{
\nu\langle P_\eta\rangle
+\frac14\langle Z_\eta\rangle
=
\left\langle\int\eta^TS_V\eta\right\rangle
-\langle\mathcal C_{B,Q}\rangle
+\langle\mathcal R_\eta\rangle.
}
\]

Recall

\[
\mathcal C_{B,Q}
=
\int\eta\cdot
\bigl[(Q\cdot\nabla)\zeta-(\zeta\cdot\nabla)Q\bigr].
\]

---

## 2. Total-strain production coefficient

Define the positive stretching ceiling

\[
\boxed{
M_S
:=
\sup_{s,Y}
\lambda_{\max}^+(S_V(Y,s)).
}
\]

Then

\[
\boxed{
\int\eta^TS_V\eta
\le
M_SZ_\eta.
}
\]

No endpoint Riesz estimate relating `M_S` to total vorticity is assumed.

---

## 3. Tail-cross term without a low-frequency loss

The first cross term is

\[
I_1
:=
\int\eta\cdot(Q\cdot\nabla)\zeta.
\]

Use Holder with exponents `2,6,3`:

\[
|I_1|
\le
\|\eta\|_2\|Q\|_6\|\nabla\zeta\|_3.
\]

By homogeneous Sobolev,

\[
\|Q\|_6
\le C_S\|\nabla Q\|_2
=C_S\|\eta\|_2.
\]

Therefore

\[
\boxed{
|I_1|
\le
C_S\|\nabla\zeta\|_3Z_\eta.
}
\]

This removes the weaker estimate

\[
\|\nabla\zeta\|_\infty E_Q^{1/2}Z_\eta^{1/2},
\]

and with it the artificial `1/sqrt(lambda_0)` loss.

---

## 4. Second cross term

Let

\[
I_2
:=-\int\eta\cdot(\zeta\cdot\nabla)Q.
\]

Then

\[
|I_2|
\le
\|\zeta\|_\infty
\|\eta\|_2\|\nabla Q\|_2.
\]

Since

\[
\|\nabla Q\|_2=\|\eta\|_2,
\]

we get

\[
\boxed{
|I_2|
\le
\|\zeta\|_\infty Z_\eta.
}
\]

Thus

\[
\boxed{
|\mathcal C_{B,Q}|
\le
C_{cross}Z_\eta,
}
\]

where

\[
\boxed{
C_{cross}
:=
C_S\|\nabla\zeta\|_{L^\infty_sL^3_Y}
+\|\zeta\|_{L^\infty_{s,Y}}.
}
\]

For a smooth divergence-free extension of a `1/r` velocity tail, `zeta~r^-2` and `grad zeta~r^-3` at infinity, so the far-field parts of these norms are finite. Transition/core contributions are included explicitly in the coefficient.

---

## 5. Normalize curl-residual production

The curl-residual term is sign-indefinite. Define its positive recurrent production ratio by

\[
\boxed{
C_R^{(1)}
:=
\frac{\langle(\mathcal R_\eta)_+\rangle}
{\langle Z_\eta\rangle}
}
\]

for a nonzero recurrent relative state.

This is a formed signed-work observable, not merely a residual norm.

---

## 6. Relative production ceiling

Using the three estimates in the recurrent H1 balance,

\[
\nu\langle P_\eta\rangle
+\frac14\langle Z_\eta\rangle
\le
\left(M_S+C_{cross}+C_R^{(1)}\right)
\langle Z_\eta\rangle.
\]

Define

\[
\boxed{
C_{rel}
:=
M_S+C_{cross}+C_R^{(1)}.
}
\]

Then

\[
\boxed{
\nu\lambda_1+\frac14
\le
C_{rel},
}
\]

where

\[
\lambda_1
=
\frac{\langle P_\eta\rangle}
{\langle Z_\eta\rangle}.
\]

---

## 7. Immediate exclusion threshold

Because `lambda_1>=0`, every nonzero recurrent relative state must satisfy

\[
\boxed{C_{rel}\ge\frac14.}
\]

Therefore

\[
\boxed{
C_{rel}<\frac14
\quad\Longrightarrow\quad
\eta\equiv0
\quad\Longrightarrow\quad
Q\equiv0
}
\]

on the finite-energy relative class.

Subject to the canonical-extension nondegeneracy discussed in M5-250, this removes the nontrivial recurrent quotient.

---

## 8. Explicit upper frequency window

If

\[
C_{rel}>\frac14,
\]

then

\[
\boxed{
\lambda_1
\le
\frac{C_{rel}-1/4}{\nu}.
}
\]

M5-254 gives

\[
\lambda_0\le\lambda_1,
\]

where

\[
\lambda_0
=
\frac{\langle Z_\eta\rangle}
{\langle E_Q\rangle}.
\]

Hence

\[
\boxed{
\lambda_0
\le
\frac{C_{rel}-1/4}{\nu}.
}
\]

On the M5-250 anti-damping-dominant branch one also has

\[
\lambda_0\le\frac{3}{4\nu}.
\]

Thus

\[
\boxed{
\lambda_0
\le
\lambda_{0,+}
:=
\frac1\nu
\min\left\{
\frac34,
C_{rel}-\frac14
\right\}.
}
\]

---

## 9. Combine with the quotient tightness lower bound

M5-251 gives

\[
\lambda_0
\ge
\lambda_{Q,-}
=
\frac{1-\varepsilon}
{C_S^2(4\pi/3)^{2/3}R_Q^2}.
\]

Therefore every anti-damping recurrent quotient must satisfy

\[
\boxed{
\frac{1-\varepsilon}
{C_S^2(4\pi/3)^{2/3}R_Q^2}
\le
\frac1\nu
\min\left\{
\frac34,
C_{rel}-\frac14
\right\}.
}
\]

If the right-hand minimum is positive, this becomes the strengthened radius floor

\[
\boxed{
R_Q^2
\ge
\frac{\nu(1-\varepsilon)}
{C_S^2(4\pi/3)^{2/3}
\min\{3/4,C_{rel}-1/4\}}.
}
\]

When `C_rel` is only slightly above `1/4`, this floor becomes large.

---

## 10. Meaning of the coefficient `C_rel`

The new ceiling separates three physical mechanisms:

\[
\boxed{
C_{rel}
=
\underbrace{M_S}_{\text{total positive stretching}}
+
\underbrace{C_S\|\nabla\zeta\|_3+\|\zeta\|_\infty}_{\text{canonical-tail cross coupling}}
+
\underbrace{C_R^{(1)}}_{\text{positive curl-residual work}}.
}
\]

Thus a survivor needs at least one genuinely order-one recurrent production mechanism.

In particular, a weak low-frequency velocity tail cannot pay the H1 tax merely through its `L3` mass; it must carry derivative/vorticity coefficients or residual work of the correct size.

---

## 11. DSD verdict

### PROVED

The cross coupling has the order-zero bound

\[
\boxed{
|\mathcal C_{B,Q}|
\le
\left(
C_S\|\nabla\zeta\|_3+\|\zeta\|_\infty
\right)Z_\eta.
}
\]

Hence

\[
\boxed{
\nu\lambda_1+\frac14\le C_{rel}.
}
\]

### CLOSED SUBBRANCH

\[
\boxed{C_{rel}<1/4}
\]

cannot support a nonzero recurrent finite-energy quotient.

### SURVIVOR WINDOW

\[
\boxed{
\lambda_{Q,-}(R_Q)
\le
\lambda_0
\le
\frac1\nu\min\{3/4,C_{rel}-1/4\}.
}
\]

### NEXT TARGET

The only coefficient in `C_rel` not already a standard amplitude/derivative quantity is the signed curl-residual work `C_R^(1)`. The next audit should relate it to the velocity-level residual work from M5-250 and the RG residual structure from M5-237/238. If the two signed residual works cannot independently be large on a compact minimal hull, the residual payer may collapse to a finite coefficient threshold.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
