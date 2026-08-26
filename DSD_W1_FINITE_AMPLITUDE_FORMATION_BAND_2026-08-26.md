# DSD W1 Finite-Amplitude Formation Band

Date: 2026-08-26

Status: **THE POSITIVE WEAK-L3 DEFECT GAIN IS SHOWN NOT TO BE PRODUCED AT THE ZERO-AMPLITUDE BOUNDARY / A FIXED POSITIVE AMPLITUDE BAND IN A FINITE LERAY PARENT MUST CARRY A FIXED FRACTION OF THE NET PRESSURE-MINUS-VISCOUS GAIN / CORE AND BOUNDARY ROUTES REUNITED AS INPUT-OUTPUT OF ONE AMPLITUDE-STATE TRANSPORT / GLOBAL REGULARITY UNPROVED.**

## 1. Defect Duhamel identity

Let

\[
K(\lambda)=\lambda\mathcal E_\lambda
\]

on an invariant W1 state or invariant average. The amplitude-characteristic identity gives

\[
\boxed{
K(0+)
=2\int_0^{A_{max}}
\bigl(J_P(\lambda)-\nu D_\lambda\bigr)d\lambda
=\frac{\mathscr R_3}{3}>0.
}
\]

Hence

\[
\boxed{
\int_0^{A_{max}}
\bigl(J_P-\nu D_\lambda\bigr)d\lambda
=\frac{\mathscr R_3}{6}.
}
\]

## 2. The zero-amplitude boundary does not produce the gain

Because

\[
K(\lambda)\to K(0+)
\qquad(\lambda\downarrow0),
\]

one has

\[
\boxed{
\int_0^\eta
\bigl(J_P(\lambda)-\nu D_\lambda\bigr)d\lambda
=
\frac{K(0+)-K(\eta)}2
\to0
}
\]

as `eta downarrow0`.

Thus the positive endpoint defect is not generated in an arbitrarily thin low-amplitude layer.

## 3. Fixed positive amplitude band

Choose `eta_*>0` sufficiently small that

\[
\left|
\int_0^{\eta_*}
(J_P-\nu D_\lambda)d\lambda
\right|
\le
\frac{\mathscr R_3}{24}.
\]

Then

\[
\boxed{
\int_{\eta_*}^{A_{max}}
(J_P-\nu D_\lambda)d\lambda
\ge
\frac{\mathscr R_3}{8}>0,
}
\]

up to harmless constant choices; any fixed positive fraction below the full endpoint gain may be used.

Partition `[eta_*,A_max]` into finitely many amplitude bands. By pigeonhole, there exists one fixed band

\[
\boxed{
I_*=[\lambda_-,\lambda_+]
\subset(0,A_{max}]
}
\]

and `g_*>0` such that

\[
\boxed{
\int_{I_*}
(J_P-\nu D_\lambda)d\lambda
\ge g_*>0.
}
\]

This is the **finite-amplitude formation band**.

## 4. Finite-parent localization

The W1 Type-I tail has

\[
|U(Y)|\le A_0/|Y|
\]

for large `|Y|`. Therefore the superlevel region

\[
\{|U|\ge\lambda_-\}
\]

is contained in a fixed finite Leray ball

\[
\boxed{
B_{R_*},
\qquad
R_*\lesssim A_0/\lambda_-.
}
\]

Hence the entire formation band is finite-parent.

The low-amplitude / far-tail boundary stores the output defect, but it does not supply the positive net gain.

## 5. DSD input-output chain

The endpoint structure is therefore

\[
\boxed{
\text{finite-core amplitude band}
\xrightarrow{\ J_P-\nu D\ }
\text{positive net critical gain}
\xrightarrow{\lambda'=-\lambda/2}
\text{low-amplitude weak-L3 boundary defect}.
}
\]

Thus the previous `core-cycle` and `boundary-defect` proof routes are not competing explanations. They are the input and output sides of one amplitude-state transport system.

## 6. Consequence

A complete W1 closure may target the finite band directly:

\[
\boxed{
\int_{I_*}J_P(\lambda)d\lambda
\le
\nu\int_{I_*}D_\lambda d\lambda
}
\]

for every recurrent W1 state/average, or any estimate that makes the total band gain nonpositive.

No such unconditional large-data finite-band inequality is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
