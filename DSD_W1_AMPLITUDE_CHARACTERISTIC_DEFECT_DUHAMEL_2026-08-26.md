# DSD W1 Amplitude-Characteristic Defect Duhamel Formula

Date: 2026-08-26

Status: **EXACT TIME-AMPLITUDE DUHAMEL FORMULA / INVARIANT-MEASURE AVERAGING CONVERTS THE COUPLED CHARACTERISTIC GAIN INTO THE STATIC AMPLITUDE INTEGRAL THAT MATCHES `R3/3` / INDIVIDUAL NONSTATIONARY STATES MUST NOT DROP THE `s(lambda)` DEPENDENCE / GLOBAL REGULARITY UNPROVED.**

## 1. Threshold energy

Let

\[
a=|U|,
\qquad
\mathcal E_\lambda(s)
=
\frac12\int_{\mathbb R^3}(a^2-\lambda^2)_+\,dY.
\]

For almost every regular level `lambda>0`, the exact amplitude-threshold ledger is

\[
\boxed{
\partial_s\mathcal E_\lambda
-\frac12\partial_\lambda(\lambda\mathcal E_\lambda)
+\nu D_\lambda
=J_P(\lambda,s),
}
\]

where `D_lambda>=0` is the thresholded viscous term and `J_P(lambda,s)` is the gauge-independent pressure work through the velocity-amplitude level set.

## 2. Defect variable and characteristic

Define

\[
\boxed{K(s,\lambda):=\lambda\mathcal E_\lambda(s).}
\]

Multiplying the threshold equation by `lambda` gives

\[
\boxed{
\partial_sK
-\frac\lambda2\partial_\lambda K
+\nu\lambda D_\lambda
=\lambda J_P(\lambda,s).
}
\]

Thus the amplitude-state characteristic is

\[
\boxed{\lambda'(s)=-\lambda/2.}
\]

This is exactly the normalized representation of one fixed physical velocity level.

## 3. Exact Duhamel formula on one orbit

Along a characteristic `lambda=lambda(s)`, one has

\[
\boxed{
\frac{d}{ds}K(s,\lambda(s))
=
\lambda(s)\bigl[J_P(\lambda(s),s)-\nu D_{\lambda(s)}(s)\bigr].
}
\]

For `s0<s1`, write

\[
\lambda_1=\lambda(s_1),
\qquad
\lambda_0=\lambda(s_0)
=\lambda_1e^{(s_1-s_0)/2}.
\]

Since

\[
ds=-2\frac{d\lambda}{\lambda},
\]

the exact orbitwise formula is

\[
\boxed{
K(s_1,\lambda_1)-K(s_0,\lambda_0)
=
2\int_{\lambda_1}^{\lambda_0}
\Bigl[
J_P(\lambda,s(\lambda))
-\nu D_\lambda(s(\lambda))
\Bigr]d\lambda.
}
\]

The time argument `s(lambda)` is essential.

One must **not** replace this by a same-time amplitude integral on a generic nonstationary orbit.

## 4. Invariant-measure averaging removes the time-amplitude coupling

Let `mu` be an invariant probability measure on the compact minimal W1 set. Average the orbitwise characteristic identity over initial states distributed according to `mu`.

For each characteristic time shift, invariance gives

\[
(\Phi_h)_\#\mu=\mu.
\]

Therefore

\[
\left\langle
J_P(\lambda,s(\lambda))
-\nu D_\lambda(s(\lambda))
\right\rangle_\mu
=
\left\langle
J_P(\lambda)
-\nu D_\lambda
\right\rangle_\mu.
\]

Hence the invariant-averaged Duhamel formula is

\[
\boxed{
\langle K(\lambda_1)\rangle_\mu
-
\langle K(\lambda_0)\rangle_\mu
=
2\int_{\lambda_1}^{\lambda_0}
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu d\lambda.
}
\]

This is the correct static amplitude integral.

## 5. Endpoint limit

Take `lambda_0` above a common W1 amplitude ceiling so that `K(lambda_0)=0`, and then let `lambda_1 downarrow0`. The invariant weak-L3 defect gives

\[
\boxed{
\langle K(0+)\rangle_\mu
=
\frac{\mathscr R_3}{3}>0.
}
\]

Therefore

\[
\boxed{
2\int_0^{A_*}
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu d\lambda
=
\frac{\mathscr R_3}{3}.
}
\]

Equivalently,

\[
\boxed{
\int_0^{A_*}
\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu d\lambda
=
\frac{\mathscr R_3}{6}.
}
\]

This agrees with the invariant `p=3` endpoint balance.

## 6. Layer-cake match

For each state, the amplitude integration identities are

\[
\int_0^{A_*}J_P(\lambda,s)d\lambda=F_3(s),
\]

and

\[
\int_0^{A_*}D_\lambda(s)d\lambda=D_3(s),
\]

when interpreted by regular levels / smooth truncation.

Averaging gives

\[
\boxed{
\langle F_3\rangle_\mu
-\nu\langle D_3\rangle_\mu
=
\frac{\mathscr R_3}{6}.
}
\]

## 7. DSD interpretation

The low-amplitude boundary defect is the invariant-average output of amplitude characteristics passing through time-dependent finite-amplitude states.

The correct chain is

\[
\boxed{
\text{time-dependent finite-amplitude processing}
\xrightarrow{\lambda'=-\lambda/2}
\text{invariant low-amplitude boundary defect}.
}
\]

The characteristic formula and the invariant static amplitude formula are two levels of description and must not be conflated.

## 8. Consequence for the proof strategy

The former `uniform no-defect` route and the pressure-amplitude gain route are equivalent only after the correct invariant/characteristic bookkeeping.

A sufficient W1 closure theorem is

\[
\boxed{
\int_0^{A_*}
\left\langle J_P(\lambda)-\nu D_\lambda\right\rangle_\mu d\lambda
\le0,
}
\]

or equivalently

\[
\boxed{
\langle F_3\rangle_\mu
\le
\nu\langle D_3\rangle_\mu.
}
\]

No unconditional proof of this large weak-critical invariant gain inequality is available in the repository.

## 9. Energy-budget audit

Finite kinetic energy and finite total ordinary dissipation alone do not imply zero defect. A corridor `|u|~1/r` on `sqrt(T-t)<<r<<1` has finite `L2` energy and time-integrable ordinary dissipation while retaining order-one weak-L3 mass per logarithmic shell.

Thus the missing theorem must use genuinely critical pressure/amplitude/vorticity structure.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
