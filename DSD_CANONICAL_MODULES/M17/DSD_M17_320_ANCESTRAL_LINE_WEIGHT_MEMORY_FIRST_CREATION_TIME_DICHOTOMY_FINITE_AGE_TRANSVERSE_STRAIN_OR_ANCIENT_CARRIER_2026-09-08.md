# M17-320 — Ancestral line-weight memory: finite-age transverse strain or ancient carrier

Date: 2026-09-08
Status: conditional reduction, ancient-memory branch remains open
Parent: M17-319

## 1. Purpose

M17-319 proves that persistent line-weight covariance cannot be charged directly to present strain if the line-weight contrast was already present at the beginning of the selected interval.

This note traces that inherited contrast backward.  The goal is to distinguish:

1. a finite ancestral time at which a fixed fraction of the terminal contrast is first created, in which case a quantitative transverse-strain payer is recovered; or
2. a contrast that persists on arbitrarily long backward intervals, in which case the energy lower bound degenerates like the reciprocal of the ancestral duration and no contradiction follows merely from age.

The second possibility is retained as an explicit ancient-carrier branch.

## 2. Terminal contrast and threshold

Let

\[
q(\theta):=\log\frac{L_{\rho,\lambda}(\theta)}{L_{\rho,\mu}(\theta)},
\]

with the M17-319 terminal bound

\[
|q(\Theta)|\ge c_L>0.
\]

Fix

\[
0<\eta<1.
\]

Assume the same pair of line labels is continuously trackable backward over the interval under consideration.

If the threshold `eta c_L` is crossed at a finite time, define the latest such time

\[
\tau_*:=\sup\{\tau<\Theta:\ |q(\tau)|=\eta c_L\}.
\]

By latest-crossing selection,

\[
|q(\theta)|>\eta c_L,
\qquad \tau_*<\theta\le\Theta.
\]

Therefore `q` has a fixed sign on `(tau_*,Theta]`.  Writing

\[
s:=\operatorname{sign}q(\Theta),
\]

we have

\[
\begin{aligned}
s\bigl(q(\Theta)-q(\tau_*)\bigr)
&=|q(\Theta)|-|q(\tau_*)|\\
&\ge (1-\eta)c_L.
\end{aligned}
\]

This signed formulation avoids differentiating `|q|` across a possible zero.

## 3. Exact creation identity

M17-319 gives

\[
q'
=(\kappa_\lambda-\kappa_\mu)
+2(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}).
\]

Set

\[
T_*:=\Theta-\tau_*,
\]

and define the integrated curvature exposure

\[
K_*:=
\int_{\tau_*}^{\Theta}
\max\{|\kappa_\lambda|,|\kappa_\mu|\}\,d\theta.
\]

Then

\[
\left|
\int_{\tau_*}^{\Theta}
(\kappa_\lambda-\kappa_\mu)d\theta
\right|
\le2K_*.
\]

Thus

\[
(1-\eta)c_L
\le
2K_*
+2\left|
\int_{\tau_*}^{\Theta}
(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu})d\theta
\right|.
\]

Define

\[
A_*:=\bigl((1-\eta)c_L-2K_*\bigr)_+.
\]

Whenever `A_*>0`,

\[
\boxed{
\left|
\int_{\tau_*}^{\Theta}
(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu})d\theta
\right|
\ge \frac{A_*}{2}.
}
\]

## 4. Finite-age normalized payer

Cauchy-Schwarz gives

\[
\int_{\tau_*}^{\Theta}
|\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}|^2d\theta
\ge
\frac{A_*^2}{4T_*}.
\]

Since

\[
|a-b|^2\le2(|a|^2+|b|^2),
\]

we obtain

\[
\boxed{
\int_{\tau_*}^{\Theta}
\left(
|\bar\sigma_{\rho,\lambda}|^2
+|\bar\sigma_{\rho,\mu}|^2
\right)d\theta
\ge
\frac{A_*^2}{8T_*}.
}
\]

Assume additionally that both tracked lines retain a positive weighted mass,

\[
L_{\rho,\alpha}(\theta)\ge L_*>0,
\qquad
\alpha\in\{\lambda,\mu\},
\quad
\theta\in[\tau_*,\Theta].
\]

Using

\[
|\bar\sigma_{\rho,\alpha}|^2
\le
\frac{\int_{\gamma_\alpha}\rho\sigma_\alpha^2ds}
{L_{\rho,\alpha}},
\]

we obtain

\[
\int_{\tau_*}^{\Theta}
\sum_{\alpha\in\{\lambda,\mu\}}
\int_{\gamma_\alpha}
\rho\sigma_\alpha^2ds\,d\theta
\ge
\frac{L_*A_*^2}{8T_*}.
\]

For incompressible strain, M17-319 proved

\[
|P_\perp\Sigma P_\perp|_F^2\ge\frac12\sigma^2.
\]

Therefore

\[
\boxed{
\mathcal P_\perp([\tau_*,\Theta])
:=
\int_{\tau_*}^{\Theta}
\sum_\alpha
\int_{\gamma_\alpha}
\rho|P_{\perp,\alpha}\Sigma P_{\perp,\alpha}|_F^2
\,ds\,d\theta
\ge
\frac{L_*A_*^2}{16T_*}.
}
\]

This is the finite-age transverse-strain payer.

## 5. A fixed-threshold corollary

Take

\[
\eta=\frac12.
\]

If

\[
K_*\le\frac{c_L}{8},
\]

then

\[
A_*
\ge
\frac{c_L}{2}-\frac{c_L}{4}
=\frac{c_L}{4}.
\]

Hence

\[
\boxed{
\mathcal P_\perp([\tau_*,\Theta])
\ge
\frac{L_*c_L^2}{256T_*}.
}
\]

If the first-creation age is also uniformly bounded,

\[
T_*\le T_{\max}<\infty,
\]

then

\[
\boxed{
\mathcal P_\perp([\tau_*,\Theta])
\ge
\frac{L_*c_L^2}{256T_{\max}}.
}
\]

Thus a bounded-age creation event gives a genuinely fixed *normalized* payment.

It still does not by itself imply divergent physical dissipation across generations.

## 6. Arbitrarily ancient memory

Suppose instead that no finite latest threshold crossing can be found while the same genealogy remains trackable.  Then the contrast can persist above the threshold on arbitrarily long backward intervals:

\[
|q(\theta)|>\eta c_L
\]

for arbitrarily old `theta` within the available ancient history.

This persistence is not a contradiction by itself.  A bounded, nonzero line-weight ratio may simply be carried by an ancient recurrent structure.

To quantify why the previous coercivity degenerates, let `T>0`.  The exact telescope is

\[
q(\Theta)-q(\Theta-T)
=
\int_{\Theta-T}^{\Theta}
(\kappa_\lambda-\kappa_\mu)d\theta
+2\int_{\Theta-T}^{\Theta}
(\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu})d\theta.
\]

Define

\[
d_T:=|q(\Theta-T)|,
\]

and

\[
K_T:=
\int_{\Theta-T}^{\Theta}
\max\{|\kappa_\lambda|,|\kappa_\mu|\}d\theta.
\]

By the reverse triangle inequality,

\[
|q(\Theta)-q(\Theta-T)|
\ge (c_L-d_T)_+.
\]

Therefore

\[
2\int_{\Theta-T}^{\Theta}
|\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}|d\theta
\ge
(c_L-d_T-2K_T)_+.
\]

Cauchy-Schwarz yields

\[
\boxed{
\int_{\Theta-T}^{\Theta}
|\bar\sigma_{\rho,\lambda}-\bar\sigma_{\rho,\mu}|^2d\theta
\ge
\frac{(c_L-d_T-2K_T)_+^2}{4T}.
}
\]

The denominator is the key point:

\[
\text{coercive lower bound}\sim T^{-1}.
\]

Even if the numerator stays positive, the lower bound vanishes as `T -> infinity`.  Consequently, arbitrarily ancient memory cannot be ruled out by this finite-window Cauchy estimate.

## 7. Discrete genealogy version

The same obstruction survives if the ancestry consists of multiple tracked intervals `I_n`, possibly separated by canonical genealogy transitions that preserve the selected observable.

Writing

\[
q_N-q_0
=
\sum_{n=0}^{N-1}
\int_{I_n}
(\Delta\kappa_n+2\Delta\bar\sigma_n)d\theta,
\]

and

\[
T_{\rm anc}:=\sum_n|I_n|,
\qquad
K_{\rm anc}:=
\sum_n\int_{I_n}
\max(|\kappa_{\lambda,n}|,|\kappa_{\mu,n}|)d\theta,
\]

Cauchy-Schwarz across the full ancestral duration gives the schematic bound

\[
\boxed{
\sum_n\int_{I_n}|\Delta\bar\sigma_n|^2d\theta
\ge
\frac{(c_L-|q_0|-2K_{\rm anc})_+^2}
{4T_{\rm anc}}.
}
\]

Thus merely splitting the genealogy into generations does not remove the `1/T_anc` degeneration.  A bounded-overlap/finite-resource or nonnegative-production theorem would be needed to obtain a true cumulative obstruction.

## 8. Corrected M17-320 branch

The inherited-memory branch from M17-319 is therefore reduced to

\[
\boxed{
\begin{aligned}
H_{\rm ancestral\ line\text{-}weight\ memory}
\Longrightarrow{}&
H_{\rm finite\text{-}age\ transverse\text{-}strain\ payer}\\
&\lor H_{\rm ancient\ line\text{-}weight\ carrier}\\
&\lor G_{\rm curvature\ budget}\\
&\lor G_{\rm genealogy/replacement}\\
&\lor G_{\rm amplitude/line\text{-}weight}.
\end{aligned}
}
\]

Combining M17-319 and M17-320 gives

\[
\boxed{
\begin{aligned}
H_{\rm persistent\ covariance}
\Longrightarrow{}&
H_{\rm finite\text{-}age\ transverse\text{-}strain\ payer}\\
&\lor H_{\rm ancient\ line\text{-}weight\ carrier}\\
&\lor G_{\rm curvature}\\
&\lor G_{\rm genealogy/replacement}\\
&\lor G_{\rm amplitude/line\text{-}weight}\\
&\lor G_{\kappa\text{-}corridor/nodal}\\
&\lor G_{h\text{-}coefficient}.
\end{aligned}
}
\]

## 9. DSD audit

### 9.1 Signed threshold crossing

The proof uses the signed variable `q`, not a derivative of `|q|` through zero.  The latest threshold crossing guarantees a fixed sign on the creation interval.

### 9.2 Genealogy coverage

The same pair of line labels must be trackable.  If a replacement event occurs, it is an explicit branch and requires a separate coverage theorem.  This is required by the R27/R38 leakage audit.

### 9.3 Curvature accounting

Curvature is integrated as `K_*` or `K_T`; it is not silently assumed negligible.  Large curvature is an explicit payer/exit.

### 9.4 Amplitude/weight bridge

The conversion from averaged strain to raw weighted strain requires `L_rho >= L_* > 0`.  This is not supplied by director geometry alone; absence of the bound remains the amplitude/line-weight exit required by R34.

### 9.5 Normalized versus physical budget

Even the fixed finite-age bound is normalized/local.  R21 and R33 prohibit summing it as physical dissipation without a physicalization and bounded-multiplicity theorem.

### 9.6 Ancient-age degeneration

The `1/T` factor is structural.  Infinite ancestral age cannot be declared contradictory from the present estimate.  Doing so would be an invalid coercivity extrapolation.

## 10. Result and next target

M17-320 closes the naive idea that inherited line-weight memory can always be pushed backward until it pays a fixed amount.  That is true only when a fixed fraction of the contrast is created within a uniformly bounded ancestral age and the curvature/genealogy/amplitude hypotheses survive.

The genuinely surviving branch is

\[
\boxed{H_{\rm ancient\ line\text{-}weight\ carrier}.}
\]

The next natural target, M17-321, is to place this branch inside the recurrent-hull/cocycle framework of the earlier modules.  Recurrence can at most force cancellation of the signed cocycle unless an additional nonnegative production, variance, entropy, or finite-resource mechanism is found; therefore recurrence itself must not be mistaken for a positive cost theorem.
