# DSD M5-42 — Static Far Field of the Pump-Anchored Ancient-to-Terminal Cell

Date: 2026-08-27

Status: **AUDITED AFTER M5-41 / EXACT CANCELLATION BETWEEN W1 LOG-RADIUS TRANSPORT AND PUMP-ANCHORED INVERSE-LERAY SCALING / LEADING `1/r` TAIL IS STATIC FOR PERIODIC OR APERIODIC HULLS / GLOBAL REGULARITY UNPROVED.**

## 1. W1 tail-hull transport

For the complete W1 trajectory `U^#`, define

\[
F_U(\theta,\rho,\eta)
:=e^\rho U^\#(e^\rho\theta,\eta).
\]

Every selected W1 far-tail hull satisfies

\[
\partial_\eta F_U+\frac12\partial_\rho F_U=0,
\]

hence

\[
\boxed{
F_U(\theta,\rho,\eta)
=\Phi(\theta,\rho-\eta/2).
}
\]

No periodicity is assumed.

---

## 2. Pump-anchored ancient-to-terminal representation

M5-41 now gives

\[
V_*(z,\sigma)
=
(\lambda_c^2-\sigma)^{-1/2}
U^\#\!\left(
\frac z{\sqrt{\lambda_c^2-\sigma}},
\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}
\right),
\qquad
\sigma<\lambda_c^2.
\]

Let

\[
r=|z|,
\qquad
\rho_Y=\log r-\frac12\log(\lambda_c^2-\sigma),
\]

and

\[
\eta
=\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}.
\]

Then

\[
rV_*(r\theta,\sigma)
=F_U(\theta,\rho_Y,\eta).
\]

---

## 3. Exact cancellation

Compute

\[
\begin{aligned}
\rho_Y-\eta/2
&=\log r
-\frac12\log(\lambda_c^2-\sigma)
-\frac12\log\frac{\lambda_c^2}{\lambda_c^2-\sigma}\\
&=\log r-\log\lambda_c\\
&=\log\frac r{\lambda_c}.
\end{aligned}
\]

Therefore every selected tail-hull profile of the cell satisfies

\[
\boxed{
rV_*(r\theta,\sigma)
=\Phi\!\left(\theta,\log\frac r{\lambda_c}\right)
}
\]

at leading `1/r` order, independently of `sigma`.

Equivalently,

\[
\boxed{
V_{tail}(z)
=
\frac1{|z|}
\Phi\!\left(
\frac z{|z|},
\log\frac{|z|}{\lambda_c}
\right).
}
\]

Thus changing the pump anchor only shifts the log-radius phase by `log lambda_c`; it does not reintroduce time dependence.

---

## 4. Periodic/aperiodic unification

If `Phi` is periodic, the static tail is log-periodic/DSS.

If `Phi` is aperiodic, the same static formula holds with an aperiodic log-radius pattern.

Hence

\[
\boxed{
\text{periodic}\lor\text{aperiodic W1 tail}
\Longrightarrow
\text{static leading far field of the pump-to-defect cell}.
}
\]

---

## 5. Divergence-free sphere constraint

Writing

\[
\Phi=\Phi_r\theta+\Phi_T,
\]

one has

\[
\boxed{
(\partial_\rho+1)\Phi_r
+\operatorname{div}_{S^2}\Phi_T=0.
}
\]

This is the same sphere Hodge constraint derived in M5-8.

---

## 6. Static tail is not a stationary NS solution

The static leading `1/r` trace need not satisfy stationary Navier--Stokes by itself.

Its stationary residual is order `r^{-3}`, and a subleading time-dependent correction can have a time derivative of the same order and cancel that residual.

Therefore no stationary-NS contradiction is claimed.

---

## 7. Correct DSD role

The pump-anchored cell now separates cleanly into

\[
\boxed{
\text{finite/intermediate scale: time-dependent pump and transport}
}
\]

and

\[
\boxed{
\text{far boundary: static critical `1/r` ancestry/reservoir}.
}
\]

The low-amplitude boundary defect reached as

\[
\sigma\uparrow\lambda_c^2
\]

is therefore not produced by a time-varying leading far-tail pattern. The actual source remains the finite-amplitude threshold-Hodge formation mechanism at the pump stage.

---

## 8. Liouville audit

The static `1/r` tail is compatible with weak `L^3` and may fail strong global `L^3` logarithmically. Hence strong-`L^3` ancient Liouville results are not automatically applicable.

A new bridge would still be needed: tail removal, a strong-`L^3` backward sequence, or a direct rigidity theorem for this pump-to-defect static-tail class.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
