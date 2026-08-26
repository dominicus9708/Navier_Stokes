# DSD W1 Amplitude-Characteristic Defect Duhamel Formula

Date: 2026-08-26

Status: **THE LOW-AMPLITUDE WEAK-L3 DEFECT IS IDENTIFIED AS THE NET PRESSURE-MINUS-VISCOUS GAIN ACCUMULATED ALONG ONE AMPLITUDE-STATE CHARACTERISTIC / UNIFORM NO-DEFECT AND CORE PRESSURE-LOOP ROUTES ARE SHOWN TO BE THE SAME ENDPOINT PROBLEM / GLOBAL REGULARITY UNPROVED.**

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
=J_P(\lambda),
}
\]

where `D_lambda>=0` is the thresholded viscous term and `J_P(lambda)` is the gauge-independent pressure work through the velocity-amplitude level set.

## 2. Defect variable

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
=\lambda J_P(\lambda).
}
\]

Thus the amplitude-state transport velocity is

\[
\boxed{\lambda'(s)=-\lambda/2.}
\]

This is exactly the fixed-physical-amplitude characteristic.

## 3. Duhamel formula along the amplitude characteristic

Along a characteristic `lambda=lambda(s)`, one has

\[
\boxed{
\frac{d}{ds}K(s,\lambda(s))
=
\lambda(s)\bigl[J_P(\lambda(s))-
u D_{\lambda(s)}\bigr].
}
\]

Since

\[
\frac{d\lambda}{ds}=-\frac\lambda2,
\qquad
ds=-2\frac{d\lambda}{\lambda},
\]

integration through the amplitude range gives schematically

\[
\boxed{
K_{out}-K_{in}
=
2\int_{\lambda_{out}}^{\lambda_{in}}
\bigl[J_P(\lambda)-\nu D_\lambda\bigr]d\lambda.
}
\]

If the incoming level is above the normalized velocity ceiling, then `K_in=0`. Passing to the low-amplitude exit `lambda_out downarrow0` gives

\[
\boxed{
K(0+)
=
2\int_0^{A_{max}}
\bigl[J_P(\lambda)-\nu D_\lambda\bigr]d\lambda,
}
\]

with the usual interpretation through regular levels / smooth truncation.

## 4. Match with the p=3 endpoint

The layer-cake identities give

\[
\int_0^{A_{max}}J_P(\lambda)d\lambda=F_3,
\]

and

\[
\int_0^{A_{max}}D_\lambda d\lambda=D_3
\]

under the established threshold normalization.

The invariant endpoint balance is

\[
\boxed{
F_3-
u D_3
=\frac{\mathscr R_3}{6}.
}
\]

Therefore

\[
\boxed{
K(0+)=\frac{\mathscr R_3}{3}.
}
\]

This exactly matches the independently derived weak-L3 distribution defect coefficient.

## 5. DSD interpretation

The low-amplitude defect is not created ex nihilo at the state boundary. It is the output of one amplitude-state passage:

\[
\boxed{
\text{high normalized amplitude}
\to
\text{pressure/viscous processing across levels}
\to
\text{low-amplitude weak-L3 boundary defect}.
}
\]

The defect is therefore a **net-gain memory** of the amplitude-state dynamics.

## 6. Consequence for the proof strategy

The previously separated routes

\[
\text{uniform no-defect compactness}
\]

and

\[
\text{pressure-amplitude gain nonrepeatability}
\]

are not independent endpoint problems.

They are equivalent views of the same condition.

A sufficient closure theorem is

\[
\boxed{
\int_0^{A_{max}}J_P(\lambda)d\lambda
\le
\nu\int_0^{A_{max}}D_\lambda d\lambda.
}
\]

Equivalently,

\[
\boxed{F_3\le\nu D_3.}
\]

Such an inequality would force `K(0+)=0`, hence `mathscr R_3=0`, closing W1.

No unconditional proof of this large weak-critical gain inequality is currently available in the repository.

## 7. Audit of the former uniform-no-defect target

Finite kinetic energy and finite total physical energy dissipation alone do not imply uniform no-defect. A critical corridor `|u|~1/r` on `sqrt(T-t) << r << 1` has finite local `L2` energy and time-integrable ordinary dissipation while retaining order-one weak-L3 mass per log shell.

Thus the missing theorem must use genuinely critical pressure/amplitude/vorticity structure, not only the classical subcritical energy budget.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
