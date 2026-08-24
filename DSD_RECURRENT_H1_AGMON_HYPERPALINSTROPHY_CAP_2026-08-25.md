# DSD Recurrent H1 Agmon Hyperpalinstrophy Cap

Date: 2026-08-25

Status: **FINITE MEAN HYPERPALINSTROPHY CAP DERIVED ON BOUNDED-Z RECURRENT BRANCH / FREQUENCY UPPER BOUND DERIVED / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

Work on the bounded normalized-enstrophy recurrent Leray branch.

Let

\[
W=\nabla\times V,
\qquad
\Sigma=\frac12(\nabla V+\nabla V^T),
\]

and define

\[
E:=\|\Sigma\|_2^2,
\qquad
P:=\|\nabla\Sigma\|_2^2,
\qquad
H:=\|\Delta\Sigma\|_2^2.
\]

Whole-space incompressibility gives

\[
\boxed{
E=\frac12 Z,
\qquad
P=\frac12 Q,
\qquad
H=\frac12 R,
}
\]

where

\[
Z=\|W\|_2^2,
\qquad
Q=\|\nabla W\|_2^2,
\qquad
R=\|\Delta W\|_2^2.
\]

Assume

\[
0<Z(s)\le Z_+.
\]

---

## 2. Exact recurrent H1 balance

The Leray H1 strain identity is

\[
\boxed{
\frac12P_s
+\frac34P
+\nu H
=N_L.
}
\]

The previously established nonlinear H1 production ceiling is

\[
\boxed{
N_L
\le
C_N\int|\Sigma||\nabla\Sigma|^2dy,
\qquad
C_N:=\frac4{\sqrt6}.
}
\]

Only the positive-production direction matters for the upper estimate.

---

## 3. Agmon interpolation

Use the three-dimensional whole-space Agmon inequality

\[
\boxed{
\|F\|_\infty
\le
C_A
\|F\|_2^{1/4}
\|\Delta F\|_2^{3/4},
}
\]

for a universal finite constant `C_A`.

Applied to the tensor field `Sigma`,

\[
\|\Sigma\|_\infty
\le
C_A E^{1/8}H^{3/8}.
\]

Therefore

\[
N_L
\le
C_NC_A E^{1/8}H^{3/8}P.
\]

The Fourier interpolation identity gives

\[
\boxed{
P^2
\le
EH.
}
\]

Hence

\[
P\le E^{1/2}H^{1/2}
\]

and thus

\[
\boxed{
N_L
\le
C_*E^{5/8}H^{7/8},
\qquad
C_*:=C_NC_A.
}
\]

Since

\[
E\le E_+:=Z_+/2,
\]

we have

\[
\boxed{
N_L
\le
C_*E_+^{5/8}H^{7/8}.
}
\]

---

## 4. Recurrent averaging gives a finite H ceiling

Average the exact H1 balance over a recurrent invariant measure or over long Leray intervals along which the bounded endpoint term vanishes.

Then

\[
\frac34\overline P
+\nu\overline H
=
\overline{N_L}.
\]

Using the nonlinear upper bound and concavity of `x^(7/8)`,

\[
\begin{aligned}
\overline{N_L}
&\le
C_*E_+^{5/8}
\overline{H^{7/8}}\\
&\le
C_*E_+^{5/8}
\overline H^{7/8}.
\end{aligned}
\]

Discard the positive `3P/4` term. If `bar H>0`,

\[
\nu\overline H
\le
C_*E_+^{5/8}\overline H^{7/8}.
\]

Therefore

\[
\boxed{
\overline H
\le
C_*^8\frac{E_+^5}{\nu^8}.
}
\]

Equivalently,

\[
\boxed{
\overline R
\le
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
}
\]

Thus a bounded-`Z` recurrent survivor cannot support arbitrarily large mean second-vorticity-derivative energy.

---

## 5. Mean palinstrophy upper bound

Pointwise,

\[
P\le E_+^{1/2}H^{1/2}.
\]

Average and apply Cauchy/Jensen:

\[
\overline P
\le
E_+^{1/2}\overline H^{1/2}.
\]

Using the previous cap,

\[
\boxed{
\overline P
\le
C_*^4
\frac{E_+^3}{\nu^4}.
}
\]

Therefore

\[
\boxed{
\overline Q
\le
\frac{C_*^4}{4}
\frac{Z_+^3}{\nu^4}.
}
\]

This is a recurrent mean palinstrophy ceiling derived only from bounded `Z` and the H1 equation.

---

## 6. Convert to an upper mean-frequency bound

The recurrent active-core construction supplies a positive mean enstrophy floor.

If active windows have density at least `d_*` and carry local enstrophy at least `z_*`, then

\[
\boxed{
\overline Z
\ge
d_*z_*.
}
\]

Thus

\[
\bar\lambda
:=
\frac{\overline Q}{\overline Z}
\]

satisfies

\[
\boxed{
\bar\lambda
\le
\frac{C_*^4}{4}
\frac{Z_+^3}
{\nu^4d_*z_*}.
}
\]

The existing active-core lower bound is

\[
\boxed{
\bar\lambda
\ge
c_{\log}
=
\kappa_Q(R_*)
\frac{d_*z_*}{Z_+}.
}
\]

Therefore the recurrent branch is impossible whenever

\[
\boxed{
\kappa_Q(R_*)
\frac{d_*z_*}{Z_+}
>
\frac{C_*^4}{4}
\frac{Z_+^3}
{\nu^4d_*z_*}.
}
\]

Equivalently,

\[
\boxed{
Z_+^4
<
\frac{4\nu^4
\kappa_Q(R_*)
(d_*z_*)^2}
{C_*^4}.
}
\]

This is another explicit small-bounded-enstrophy closure certificate.

---

## 7. Density control of high second-derivative episodes

The mean hyperpalinstrophy cap also yields a quantitative density estimate.

For every `L>0`, Markov gives

\[
\boxed{
\operatorname{dens}\{s:H(s)\ge L\}
\le
\frac{C_*^8E_+^5}
{\nu^8L}.
}
\]

Thus very large normalized second-vorticity-derivative episodes cannot occupy a positive time density independent of their threshold.

This does not exclude sparse derivative needles.

It does show that an `N`/high-second-derivative rescue cannot be the persistent recurrent background on the bounded-`Z` branch.

---

## 8. Relation to the cubic-tail survivor

A critical `1/r` velocity tail has

\[
|W|\sim r^{-2},
\qquad
|\nabla W|\sim r^{-3},
\qquad
|\Delta W|\sim r^{-4},
\]

so its contributions to `Z`, `Q`, and `R` are all summable at spatial infinity.

Therefore the present cap does not exclude the passive critical tail itself.

Its role is different:

\[
\boxed{
\text{the recurrent active core cannot repeatedly compensate for the tail by an arbitrarily large mean derivative cascade.}
}
\]

Any derivative rescue beyond the cap must occur sparsely and must be routed through the finite `H_remote/N/T` event ledgers rather than treated as a stationary background.

---

## 9. DSD audit

This argument uses only the finite formed channels

\[
(E,P,H,Z,Q,R),
\]

plus recurrent time averages.

No infinite derivative hierarchy is used.

The highest derivative order in the formed object is second vorticity derivative / third velocity derivative through `R=||Delta W||_2^2`.

---

## 10. Updated frontier

On the bounded-`Z` recurrent critical-tail branch we now have simultaneous finite windows for

\[
\boxed{
\bar\lambda,
\qquad
\overline R,
\qquad
\text{Betchov residual production}.
}
\]

The remaining survivor must therefore be a genuinely scale-critical recurrent core whose mean derivative activity is bounded, accompanied by a passive/non-`L3` cubic tail, with only sparse `H_remote/N/T` excursions available.

This is substantially narrower than a generic bounded ancient solution but is not yet covered by a known Liouville theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
