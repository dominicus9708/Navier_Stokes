# DSD W1 Periodic Quotient: Dilation-Interface Audit

Date: 2026-08-26

Status: **LEADING CUTOFF FORCING CORRECTED FROM TAIL-RESIDUAL SCALE TO DILATION-INTERFACE SCALE / O(R) QUOTIENT ENERGY INJECTION IDENTIFIED / PURE PASSIVE TAIL MODEL SHOWS EXACT CANCELLATION OF L2 LERAY ANTI-DAMPING / NONLINEAR INFORMATION MOVED TO THE RENORMALIZED SUBLEADING INTERFACE DEFECT / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The periodic canonical-tail decomposition gives, for a fixed cutoff radius R,

\[
U=B_R+Q_R,
\]

where

\[
B_R=T
\qquad(|Y|>2R),
\]

`B_R` is a divergence-free cutoff extension of the critical tail, and

\[
Q_R\in L^2\cap L^3.
\]

The tail itself has nonlinear/viscous residual of order `r^-3`.

It is tempting to infer that the entire quotient forcing becomes small as `R -> infinity`.

That inference is false because the radial cutoff does not commute with the self-similar dilation operator.

## 2. Separate the linear dilation operator

Write

\[
\mathcal L_0
:=
\partial_s
+\frac12
+\frac12Y\cdot\nabla.
\]

The canonical leading tail satisfies exactly

\[
\boxed{
\mathcal L_0T=0.
}
\]

Let `chi_R(Y)=chi(Y/R)` be a time-independent radial cutoff with

\[
\chi_R=0\quad(r\le R),
\qquad
\chi_R=1\quad(r\ge2R).
\]

Then

\[
\mathcal L_0(\chi_RT)
=
\chi_R\mathcal L_0T
+\frac12(Y\cdot\nabla\chi_R)T.
\]

Therefore

\[
\boxed{
[\mathcal L_0,\chi_R]T
=
\frac12(Y\cdot\nabla\chi_R)T.
}
\]

## 3. The commutator is critical order R^-1, not R^-3

On the transition annulus

\[
A_R^*=\{R<r<2R\},
\]

one has

\[
Y\cdot\nabla\chi_R=O(1)
\]

and

\[
T=O(R^{-1}).
\]

Hence

\[
\boxed{
[\mathcal L_0,\chi_R]T
=O(R^{-1})
\quad\text{on }A_R^*.
}
\]

This is two powers larger than the genuine tail residual

\[
-\nu\Delta T
+\mathbb P\nabla\cdot(T\otimes T)
=O(R^{-3}).
\]

The distinction is structural:

- `R^-3`: dynamics of the critical tail itself;
- `R^-1`: artificial interface created by cutting a dilation-resonant `R^-1` field.

## 4. Scaling of the interface forcing

The transition annulus has volume scale `R^3`.

Thus an `R^-1` interface forcing has

\[
\|F_{int,R}\|_2
\sim R^{1/2}.
\]

The retained critical part of the quotient on the same transition region has

\[
\|Q_R\|_2
\sim R^{1/2}.
\]

Therefore its energy pairing has the natural size

\[
\boxed{
|\langle F_{int,R},Q_R\rangle|
\sim R.
}
\]

At the same time, because `Q_R=U` through the interior ball and the critical tail has `|U|~r^-1`,

\[
\boxed{
\|Q_R\|_2^2
\sim R
}
\]

at leading critical order as `R` grows.

Thus the interface pairing is exactly large enough to balance the Leray `L2` anti-damping term.

## 5. Exact pure-passive model

The leading mechanism can be checked without nonlinearity, viscosity, pressure, or Bogovskii correction.

Let `T` solve

\[
\mathcal L_0T=0
\]

and define

\[
Q_R^{lin}:=(1-\chi_R)T.
\]

Then `Q_R^{lin}` is compactly supported and

\[
\begin{aligned}
\mathcal L_0Q_R^{lin}
&=
-(\mathcal L_0\chi_R)T\\
&=
-\frac12(Y\cdot\nabla\chi_R)T.
\end{aligned}
\]

So

\[
\boxed{
\mathcal L_0Q_R^{lin}
=F_R^{lin},
\qquad
F_R^{lin}:=-\frac12(Y\cdot\nabla\chi_R)T.
}
\]

## 6. Global L2 ledger for the pure-passive cutoff

For any compactly supported field Q,

\[
\int Q\cdot
\left(
\frac12Q+\frac12Y\cdot\nabla Q
\right)dY
=-\frac14\|Q\|_2^2.
\]

Hence the linear quotient obeys

\[
\boxed{
\frac12\frac d{ds}\|Q_R^{lin}\|_2^2
-\frac14\|Q_R^{lin}\|_2^2
=
\langle F_R^{lin},Q_R^{lin}\rangle.
}
\]

For an S-periodic critical tail, period averaging gives

\[
\boxed{
-\frac14
\left\langle\|Q_R^{lin}\|_2^2\right\rangle_S
=
\left\langle
\langle F_R^{lin},Q_R^{lin}\rangle
\right\rangle_S.
}
\]

Substituting the forcing explicitly,

\[
\boxed{
\frac14
\left\langle\|Q_R^{lin}\|_2^2\right\rangle_S
=
\frac12
\left\langle
\int
(Y\cdot\nabla\chi_R)(1-\chi_R)|T|^2dY
\right\rangle_S.
}
\]

For a monotone radial cutoff the right side is nonnegative.

Thus the order-R interface term is not an uncontrolled error: in the pure passive model it **exactly pays** the order-R Leray anti-damping of the truncated critical field.

## 7. Relation to the local-ball radial boundary flux

The same mechanism appears without any artificial cutoff in the exact local L2 energy identity on a ball.

For

\[
E_R(s):=\int_{B_R}|U|^2dY,
\]

the Leray equation gives

\[
\boxed{
\frac12E_R'
-\frac14E_R
+\nu\int_{B_R}|\nabla U|^2
=
\mathcal B_{2,R},
}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal B_{2,R}
={}&
\nu\int_{\partial B_R}\partial_nU\cdot U\,dS\\
&-\frac12\int_{\partial B_R}|U|^2U\cdot n\,dS\\
&-\frac R4\int_{\partial B_R}|U|^2dS\\
&-\int_{\partial B_R}P\,U\cdot n\,dS.
\end{aligned}
}
\]

For a critical tail `U~R^-1`, the similarity-radial term has size

\[
\boxed{
\frac R4\int_{\partial B_R}|U|^2dS
\sim R,
}
\]

whereas viscous, advective, and pressure boundary terms are lower order under the established W1 tail bounds.

Thus the large cutoff commutator is simply the quotient representation of the same similarity-radial L2 flux.

## 8. Exact period-average cancellation for the canonical tail

Write

\[
T(r\theta,s)
=r^{-1}\Phi(\theta,\log r-s/2),
\]

where `Phi` has log period `L=S/2`.

Define

\[
a_2(\eta)
:=
\int_{S^2}|\Phi(\theta,\eta)|^2d\theta.
\]

Averaging over one Leray period samples one full log period, so

\[
\overline a_2
:=
\frac1S\int_0^Sa_2(\rho-s/2)ds
\]

is independent of `rho`.

Therefore

\[
\boxed{
\left\langle
\int_{r_0<|Y|<R}|T|^2dY
\right\rangle_S
=
\overline a_2(R-r_0).
}
\]

Also

\[
\boxed{
\left\langle
\int_{\partial B_R}|T|^2dS
\right\rangle_S
=
overline a_2.
}
\]

Hence the leading terms satisfy

\[
\boxed{
\frac14\langle E_R^T\rangle_S
-
\frac R4
\left\langle
\int_{\partial B_R}|T|^2dS
\right\rangle_S
=O(1),
}
\]

with the `O(1)` coming only from the fixed inner cutoff.

The order-R Leray anti-damping and similarity-radial flux cancel exactly at leading order.

## 9. Bogovskii correction does not remove the leading interface scale

The divergence source of the raw cutoff satisfies

\[
g_R=\nabla\chi_R\cdot T=O(R^{-2}).
\]

On an annulus of diameter R, a scale-covariant Bogovskii correction has

\[
b_R=O(R^{-1}),
\qquad
\nabla b_R=O(R^{-2})
\]

in the corresponding Sobolev scaling.

Therefore

\[
\mathcal L_0b_R=O(R^{-1})
\]

at the interface as well.

The divergence-free repair changes the detailed coefficient and tensor structure of the leading interface forcing, but it cannot demote it from `R^-1` to `R^-3`.

Thus the order-R energy exchange persists in the true divergence-free quotient.

## 10. Correct interpretation of the quotient forcing

The true quotient forcing must be separated into

\[
\boxed{
\mathcal F_R
=
\mathcal F_R^{dil,int}
+
\mathcal F_R^{sub},
}
\]

where

\[
\mathcal F_R^{dil,int}
=O(R^{-1})
\]

on the cutoff annulus and represents the unavoidable linear dilation-interface exchange, while

\[
\mathcal F_R^{sub}
\]

contains:

- genuine tail Navier--Stokes residual `O(R^-3)`;
- viscosity cutoff commutators `O(R^-3)`;
- nonlinear cutoff/cross terms at critical lower order;
- canonical-tail correction terms;
- finite Bogovskii commutator defects after the leading dilation piece is separated.

The leading `F_R^{dil,int}` is not evidence of nonlinear replenishment by the core. It exists even for a purely passive linear critical tail.

## 11. Updated rigidity target

A successful quotient rigidity argument must first renormalize away the exact passive dilation-interface exchange.

It is invalid to argue

\[
\|Q_R\|_2^2\sim R
\quad\text{but forcing is }o(R)
\]

without removing `F_R^{dil,int}`; the forcing is actually order R in the energy pairing.

The genuine nonlinear/core-tail question is instead:

\[
\boxed{
\text{after subtracting the canonical passive dilation flux,}
\quad
\text{can the remaining interface defect sustain a nontrivial recurrent core?}
}
\]

This is a renormalized interface problem.

## 12. Audit verdict

### PROVED

- cutoff and Leray dilation fail to commute at critical order `R^-1`;
- the resulting quotient energy pairing is naturally order R;
- in the pure passive-tail model this interface pairing exactly balances the L2 Leray anti-damping;
- the same mechanism is the cutoff form of the similarity-radial local-energy boundary flux;
- period averaging of the canonical log-periodic tail shows exact leading order-R cancellation;
- Bogovskii divergence correction preserves the leading critical interface scale.

### NOT PROVED

- a coercive sign for the renormalized subleading interface defect;
- vanishing or finite total of that defect over recurrent cycles;
- exclusion of the periodic W1 quotient;
- extension of canonical-tail subtraction to the aperiodic branch at the same precision;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]