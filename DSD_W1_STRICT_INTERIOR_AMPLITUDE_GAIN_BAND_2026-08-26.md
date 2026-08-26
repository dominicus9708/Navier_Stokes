# DSD W1 Strict Interior-Amplitude Gain Band

Date: 2026-08-26

Status: **THE POSITIVE INVARIANT-AVERAGED RENORMALIZED CUBIC GAIN IS LOCALIZED TO AN AMPLITUDE BAND BOUNDED AWAY FROM BOTH ZERO AMPLITUDE AND A COMMON UPPER AMPLITUDE CEILING / THE RESULT IS STATISTICAL FIRST, WITH RECURRENT INSTANTANEOUS WITNESSES EXTRACTED BY MINIMALITY / GLOBAL REGULARITY UNPROVED.**

## 1. Invariant defect primitive

For one state define

\[
K_U(\lambda)=\lambda\mathcal E_{\lambda,U}.
\]

Let

\[
\bar K(\lambda)=\langle K_U(\lambda)\rangle_\mu.
\]

The invariant threshold ledger gives

\[
\boxed{
\bar G(\lambda)
:=
\left\langle J_P(\lambda)-\nu D_\lambda\right\rangle_\mu
=-\frac12\bar K'(\lambda).
}
\]

The total endpoint gain is

\[
\boxed{
\int_0^{A_*}\bar G(\lambda)d\lambda
=\frac12\bar K(0+)
=\frac{\mathscr R_3}{6}>0,
}
\]

where `A_*` is any common W1 amplitude ceiling above all statewise essential suprema.

## 2. Low-amplitude boundary contributes arbitrarily little

Since

\[
\bar K(\lambda)\to\bar K(0+)
\quad(\lambda\downarrow0),
\]

one has

\[
\boxed{
\int_0^{\lambda_-}\bar G(\lambda)d\lambda
=
\frac{\bar K(0+)-\bar K(\lambda_-)}2
\to0.
}
\]

Thus an arbitrarily thin low-amplitude boundary layer cannot carry a fixed fraction of the positive mean gain.

## 3. Upper-amplitude boundary also contributes arbitrarily little

Because `A_*` is a common upper ceiling,

\[
K_U(A_*)=0
\]

for every W1 state and hence

\[
\bar K(A_*)=0.
\]

By continuity from below,

\[
\bar K(\lambda)\to0
\quad(\lambda\uparrow A_*).
\]

Therefore

\[
\boxed{
\int_{\lambda_+}^{A_*}\bar G(\lambda)d\lambda
=
\frac{\bar K(\lambda_+)}2
\to0
}
\]

as `lambda_+ upward A_*`.

## 4. Strict interior invariant band

Choose

\[
0<\lambda_-<\lambda_+<A_*
\]

so that the two boundary contributions together are less than half the total gain. Then

\[
\boxed{
\int_{\lambda_-}^{\lambda_+}
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu d\lambda
\ge c_*>0.
}
\]

The strict band is fixed at the invariant-measure level.

## 5. Spatial localization

Since `lambda_->0` and the W1 tail obeys

\[
|U(Y)|\le A_0/|Y|
\]

for large `|Y|`, every statewise superlevel set `|U|>=lambda_-` lies in one fixed finite Leray parent ball.

Thus the invariant gain on the strict band is finite-parent.

## 6. Recurrent instantaneous witnesses

Define the state functional

\[
\mathcal G_I(U)
=
\int_{\lambda_-}^{\lambda_+}
[J_P(\lambda,U)-\nu D_\lambda(U)]d\lambda
\]

using smooth truncation at exceptional levels where needed.

Then

\[
\langle\mathcal G_I\rangle_\mu\ge c_*>0.
\]

On the compact finite-parent W1 class this functional is continuous after the standard regularization. Hence there exists a nonempty open event with

\[
\mathcal G_I(U)>c_*/2.
\]

Minimality makes this event recurrent with bounded gaps along every orbit.

Thus the correct logical order is

\[
\boxed{
\text{positive invariant interior-band gain}
\Longrightarrow
\text{recurrent instantaneous finite-core pump witnesses}.
}
\]

## 7. DSD chain

The state-space picture is

\[
\boxed{
\text{strict interior amplitude band}
\xrightarrow{\text{positive mean pressure-viscous gain}}
\text{time-amplitude characteristic transport}
\xrightarrow{}
\text{neutral slope-three low-amplitude boundary defect}.
}
\]

The lower and upper amplitude boundaries are output/termination layers, not the source of the fixed positive mean gain.

## 8. Remaining issue

A complete W1 closure can focus on this compact interior amplitude interval. The missing theorem is a genuinely large-critical statement forcing

\[
\int_{\lambda_-}^{\lambda_+}
\left\langle J_P-\nu D_\lambda\right\rangle_\mu d\lambda
\le0
\]

or otherwise ruling out the recurrent pump events extracted from it.

No such unconditional theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
