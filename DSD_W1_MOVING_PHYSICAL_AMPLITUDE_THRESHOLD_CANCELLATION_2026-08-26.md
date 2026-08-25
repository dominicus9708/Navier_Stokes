# DSD W1 Moving Physical-Amplitude Threshold Cancellation

Date: 2026-08-26

Status: **THE ZERO-AMPLITUDE `R3/6` CHARGE IS SHOWN TO BE A FIXED-LERAY-THRESHOLD BOUNDARY TERM, NOT AN INDEPENDENT PHYSICAL POWER SOURCE / IT CANCELS EXACTLY WHEN THE AMPLITUDE THRESHOLD FOLLOWS A FIXED PHYSICAL VELOCITY LEVEL / GLOBAL REGULARITY UNPROVED.**

## 1. Input

The finite normalized-amplitude threshold identity is

\[
\boxed{
\partial_s\mathcal H_\epsilon
+\nu D_{3,\epsilon}
+\frac\epsilon2\mathcal E_\epsilon
=F_{3,\epsilon},
}
\]

where

\[
\mathcal E_\epsilon
=\frac12\int(|U|^2-\epsilon^2)_+dY,
\]

and

\[
\mathcal H_\epsilon
:=
\int_\epsilon^\infty\mathcal E_\lambda d\lambda.
\]

For fixed `epsilon`, invariant averaging and `epsilon downarrow 0` give

\[
\frac\epsilon2\langle\mathcal E_\epsilon\rangle
\to
\frac{\mathscr R_3}{6}.
\]

This note audits the physical meaning of that term.

---

## 2. Fixed physical velocity threshold

Let

\[
\tau=T_*-t=e^{-s}.
\]

Physical and Leray velocities satisfy

\[
u(x,t)=\tau^{-1/2}U(Y,s).
\]

Fix a physical velocity level

\[
L>0.
\]

The corresponding normalized amplitude threshold is

\[
\boxed{
\epsilon(s)
=L\sqrt\tau
=L e^{-s/2}.
}
\]

Hence

\[
\boxed{
\epsilon'(s)=-\frac12\epsilon(s).
}
\]

---

## 3. Moving-threshold derivative

Because

\[
\partial_\epsilon\mathcal H_\epsilon
=-\mathcal E_\epsilon,
\]

the total derivative along the moving threshold is

\[
\begin{aligned}
\frac d{ds}\mathcal H_{\epsilon(s)}
&=
\partial_s\mathcal H_\epsilon
+\epsilon'(s)\partial_\epsilon\mathcal H_\epsilon
\\
&=
\partial_s\mathcal H_\epsilon
+\frac\epsilon2\mathcal E_\epsilon.
\end{aligned}
\]

Substitute the fixed-threshold identity:

\[
\boxed{
\frac d{ds}\mathcal H_{\epsilon(s)}
+\nu D_{3,\epsilon(s)}
=
F_{3,\epsilon(s)}.
}
\]

The zero-amplitude boundary term cancels exactly.

---

## 4. Physical truncated cubic functional

For a scalar `z>=L`, define

\[
G_L(z)
:=
\frac{z^3}{3}
-\frac L2 z^2
+\frac{L^3}{6},
\]

and set `G_L(z)=0` for `z<=L`.

A direct scaling calculation gives

\[
\boxed{
\mathcal H_{\epsilon(s)}(U(s))
=
\int_{\mathbb R^3}G_L(|u(x,t)|)dx.
}
\]

Thus `H_{epsilon(s)}` is a genuine physical, scale-critical truncated cubic observable attached to the fixed physical amplitude level `L`.

The moving-threshold identity is simply its exact Navier--Stokes balance written in Leray time.

---

## 5. DSD audit consequence

The term

\[
\frac{\mathscr R_3}{6}
\]

must not be interpreted as an independent physical energy source injected by the far tail.

It arises because the fixed normalized boundary

\[
|U|=\epsilon
\]

moves relative to a fixed physical velocity state as the similarity normalization changes.

When the boundary is chosen to represent one fixed physical state `|u|=L`, its motion pays exactly the apparent endpoint charge.

Therefore

\[
\boxed{
\text{zero-amplitude boundary charge}
\neq
\text{new physical power source}.
}
\]

It remains an exact and useful critical boundary invariant of the recurrent Leray description.

---

## 6. Why this does not close W1

The physical truncated cubic observable

\[
\int G_L(|u|)dx
\]

is finite at every pre-blowup time, but the standard finite-energy inequality does not give a uniform-in-time bound strong enough to exclude logarithmic/weak-critical growth as `t upward T_*`.

Thus the moving-threshold cancellation prevents an invalid source interpretation but does not force `R3=0`.

The remaining difficulty is again a strong-critical versus weak-critical endpoint problem.

---

## 7. Updated DSD chain

The correct interpretation is

\[
\boxed{
\begin{array}{c}
\text{fixed normalized amplitude boundary}\
\Downarrow\\
\text{nonzero }R3/6\text{ boundary charge}\
\end{array}
}
\]

while

\[
\boxed{
\begin{array}{c}
\text{fixed physical amplitude boundary}\
\Downarrow\\
\text{boundary-motion cancellation}\
\end{array}
}
\]

The endpoint charge is therefore geometric/representational rather than an additional causal source.

This distinction should be retained in all subsequent proof routing.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
