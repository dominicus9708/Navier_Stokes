# DSD W1 Strict Interior-Amplitude Gain Band

Date: 2026-08-26

Status: **THE POSITIVE RENORMALIZED CUBIC GAIN IS LOCALIZED TO AN AMPLITUDE BAND BOUNDED AWAY FROM BOTH ZERO AMPLITUDE AND THE MAXIMUM-AMPLITUDE CONTACT SET / FAR TAIL AND MAXIMUM DEGENERACY ARE DEMOTED FROM POSSIBLE GAIN SOURCES / GLOBAL REGULARITY UNPROVED.**

## 1. Net gain and defect primitive

For the invariant threshold ledger,

\[
G(\lambda):=J_P(\lambda)-\nu D_\lambda
=-\frac12K'(\lambda),
\]

where

\[
K(\lambda)=\lambda\mathcal E_\lambda.
\]

The total endpoint gain is

\[
\boxed{
\int_0^{A_{max}}G(\lambda)d\lambda
=\frac12K(0+)
=\frac{\mathscr R_3}{6}>0.
}
\]

## 2. Low-amplitude boundary contributes arbitrarily little

Since

\[
K(\lambda)\to K(0+)
\quad(\lambda\downarrow0),
\]

one has

\[
\boxed{
\int_0^{\lambda_-}G(\lambda)d\lambda
=
\frac{K(0+)-K(\lambda_-)}2
\to0
}
\]

as `lambda_- downarrow0`.

Thus the weak-L3 / far-tail boundary stores the defect but does not supply a fixed fraction of its net gain in an arbitrarily thin boundary layer.

## 3. Maximum-amplitude boundary also contributes arbitrarily little

Let

\[
A_{max}:=\|U\|_\infty
\]

on a fixed state, or use a common W1 ceiling and the actual essential supremum where needed. Since the superlevel set shrinks to zero and

\[
\mathcal E_\lambda\to0
\quad(\lambda\uparrow A_{max}),
\]

one has

\[
K(\lambda)\to0=K(A_{max}).
\]

Therefore

\[
\boxed{
\int_{\lambda_+}^{A_{max}}G(\lambda)d\lambda
=
\frac{K(\lambda_+)}2
\to0
}
\]

as `lambda_+ upward A_max`.

Hence neither a degenerate maximum-contact layer nor an arbitrarily thin top-amplitude layer can carry the full positive endpoint gain.

## 4. Strict interior band

Choose `lambda_->0` small and `lambda_+<A_max` close enough to `A_max` so that the two boundary contributions together are less than half of the total positive gain. Then

\[
\boxed{
0<\lambda_-<\lambda_+<A_{max}
}
\]

and

\[
\boxed{
\int_{\lambda_-}^{\lambda_+}
\bigl(J_P(\lambda)-\nu D_\lambda\bigr)d\lambda
\ge c_*>0.
}
\]

The constants may be chosen on the invariant-average level; compactness can then be used to extract recurrent finite-state witnesses.

## 5. Spatial localization

Because `lambda_->0` and the W1 tail obeys `|U(Y)|<=A_0/|Y|`, the whole superlevel region `|U|>=lambda_-` lies in one finite Leray parent ball. Because `lambda_+<A_max`, the band is also separated from the maximum-contact set.

Thus the net gain is a genuine finite-core **interior-state** phenomenon.

## 6. DSD chain

The corrected state-space picture is

\[
\boxed{
\text{strict interior amplitude band}
\xrightarrow{\text{positive pressure-viscous net gain}}
\text{amplitude characteristic}
\xrightarrow{}
\text{neutral slope-3 low-amplitude boundary defect}.
}
\]

The zero-amplitude tail is the output boundary. The maximum-amplitude contact set is an upper state boundary. The positive gain is generated between them.

## 7. Consequence

A complete W1 closure can focus on a compact amplitude interval separated from all state boundaries. This removes singular low-amplitude asymptotics and maximum-contact degeneracy from the local gain estimate itself.

The remaining challenge is to show that, on this strict interior band, pressure work cannot exceed critical viscous cost by the fixed positive amount required by the W1 defect.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
