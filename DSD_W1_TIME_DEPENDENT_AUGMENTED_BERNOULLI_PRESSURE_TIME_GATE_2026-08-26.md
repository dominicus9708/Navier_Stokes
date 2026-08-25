# DSD W1 Time-Dependent Augmented Bernoulli and OU Correlation Gate

Date: 2026-08-26

Status: **EXACT TIME-DEPENDENT AUGMENTED-BERNOULLI PDE / STATIONARY MAXIMUM-PRINCIPLE STRUCTURE RECOVERED WITH ONE TEMPORAL PRESSURE TERM / INVARIANT OU-GAUSSIAN AVERAGING ELIMINATES THAT TERM AND FORCES A STRICT GAUGE-INVARIANT BERNOULLI--RADIAL-MOMENTUM CORRELATION / POSITIVE AUGMENTED-BERNOULLI GRADIENT FLOOR DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The final W1 endpoint is represented in the critical `p=3` ledger by Bernoulli-gradient work.  Classical stationary backward-self-similar Liouville arguments exploit a Bernoulli-like maximum principle, but the W1 minimal orbit is time dependent in general.

This note identifies exactly what changes in the time-dependent Leray equation and then shows that invariant averaging with the adjoint Ornstein--Uhlenbeck Gaussian removes the temporal-pressure obstruction in an integrated form.

The resulting identity is gauge invariant and supplies a new recurrent-core rigidity condition.

---

## 2. Notation

Use

\[
Q:=\frac12|U|^2,
\qquad
B:=P+Q,
\]

and define radial momentum

\[
H:=Y\cdot U.
\]

The augmented Bernoulli scalar is

\[
\boxed{
\Pi:=B+\frac12H
=P+\frac12|U|^2+\frac12Y\cdot U.
}
\]

Let

\[
\boxed{
\mathcal L
:=
\partial_s-\nu\Delta+(U+Y/2)\cdot\nabla.
}
\]

The Leray equation gives

\[
\mathcal L U=-\frac12U-\nabla P.
\]

---

## 3. Equation for kinetic energy `Q`

The product rule for the diffusion term gives

\[
\mathcal L Q
=U\cdot\mathcal L U-\nu|\nabla U|^2.
\]

Hence

\[
\boxed{
\mathcal L Q
=-Q-U\cdot\nabla P-\nu|\nabla U|^2.
}
\]

---

## 4. Pressure Poisson and Bernoulli Laplacian identity

Taking divergence of Leray gives the usual pressure Poisson equation

\[
\Delta P
=-\partial_iU_j\partial_jU_i.
\]

Also

\[
\Delta Q
=|\nabla U|^2+U\cdot\Delta U.
\]

Since

\[
|\nabla U|^2-\partial_iU_j\partial_jU_i
=|\Omega|^2,
\]

we obtain

\[
\boxed{
\Delta B
=|\Omega|^2+U\cdot\Delta U.
}
\]

Equivalently,

\[
\boxed{
\Delta P+|\nabla U|^2=|\Omega|^2.
}
\]

---

## 5. Equation for `B`

Directly,

\[
\mathcal LP
=P_s-\nu\Delta P+(U+Y/2)\cdot\nabla P.
\]

Add the equation for `Q`.  The `U·grad P` terms cancel and the pressure-Poisson identity gives

\[
\boxed{
\mathcal LB
=P_s
-Q
+\frac12Y\cdot\nabla P
-\nu|\Omega|^2.
}
\]

---

## 6. Equation for radial momentum `H`

Since

\[
H=Y\cdot U,
\]

a direct product calculation gives

\[
\boxed{
\mathcal LH
=2Q-Y\cdot\nabla P.
}
\]

Therefore adding one half of this identity to the equation for `B` cancels both `Q` and the radial pressure derivative.

Thus

\[
\boxed{
\mathcal L\Pi
=P_s-\nu|\Omega|^2.
}
\]

This is the exact time-dependent augmented-Bernoulli equation.

---

## 7. Stationary limit

For a stationary backward-self-similar profile,

\[
P_s=0.
\]

Then

\[
\boxed{
-\nu\Delta\Pi
+(U+Y/2)\cdot\nabla\Pi
=-\nu|\Omega|^2\le0.
}
\]

This is the sign-definite elliptic/drift structure underlying the classical stationary Bernoulli maximum-principle/Liouville route.

For a time-dependent W1 orbit the only additional term is

\[
P_s.
\]

At the pointwise PDE level, therefore, temporal pressure variation is the exact obstruction to importing the stationary maximum principle verbatim.

---

## 8. Gauge-safe reformulation

A time-dependent scalar pressure gauge

\[
P\mapsto P+c(s)
\]

changes both `P_s` and `Pi`.

Rather than interpret `P_s` by itself, subtract it algebraically.

Since

\[
\Pi-P=Q+\frac12H,
\]

the exact equation is equivalently

\[
\boxed{
\partial_s\left(Q+\frac12H\right)
-\nu\Delta\Pi
+(U+Y/2)\cdot\nabla\Pi
=-\nu|\Omega|^2.
}
\]

This form is gauge invariant: the time derivative contains no pressure and only spatial derivatives of `Pi` occur.

This is the form used below.

---

## 9. Adjoint Ornstein--Uhlenbeck Gaussian

Choose

\[
\boxed{
\phi_0(Y)
:=
\exp\left(-\frac{|Y|^2}{4\nu}\right).
}
\]

It satisfies the adjoint Ornstein--Uhlenbeck identity

\[
\boxed{
\nu\Delta\phi_0
+\frac12Y\cdot\nabla\phi_0
+\frac32\phi_0
=0.
}
\]

Also

\[
\boxed{
\nabla\phi_0
=-\frac{Y}{2\nu}\phi_0.
}
\]

---

## 10. A useful radial cancellation

For every divergence-free decaying `U`,

\[
\int\phi_0H\,dY
=
\int\phi_0Y\cdot U\,dY
=0.
\]

Indeed `phi_0(Y)Y` is the gradient of a radial scalar, so its pairing with a divergence-free whole-space field vanishes.

Consequently

\[
\boxed{
\int\phi_0\left(Q+\frac12H\right)dY
=
\int\phi_0Q\,dY.
}
\]

The same cancellation also means that adding any spatially constant pressure gauge to `Pi` does not alter the correlation `int phi_0 Pi H` below.

---

## 11. Exact statewise OU-weighted identity

Multiply the gauge-safe augmented-Bernoulli equation by `phi_0` and integrate over space.

Use integration by parts.  The linear diffusion plus `Y/2` drift terms cancel exactly because `phi_0` solves the adjoint OU equation.

The only drift term left is the nonlinear velocity `U`.

The result is

\[
\boxed{
\frac d{ds}
\int\phi_0Q\,dY
-
\int\Pi\,U\cdot\nabla\phi_0\,dY
=
-\nu\int\phi_0|\Omega|^2dY.
}
\]

Using `grad phi_0=-(Y/(2nu))phi_0`, this becomes

\[
\boxed{
\frac d{ds}
\int\phi_0Q\,dY
=
-\nu\int\phi_0|\Omega|^2dY
-
\frac1{2\nu}
\int\phi_0\Pi H\,dY.
}
\]

Thus Gaussian kinetic energy can recur only if augmented Bernoulli/radial-momentum sorting pays the weighted vorticity loss.

---

## 12. Invariant measure eliminates the time derivative

Let `mu` be any invariant probability measure on the nontrivial compact minimal W1 set.

Average the exact statewise identity.  The derivative of the bounded continuous Gaussian kinetic-energy observable has zero invariant mean.

Therefore

\[
\boxed{
\left\langle
\int\phi_0\Pi H\,dY
\right\rangle_\mu
=
-2\nu^2
\left\langle
\int\phi_0|\Omega|^2dY
\right\rangle_\mu.
}
\]

This is the central correlation identity.

For a nontrivial decaying divergence-free state, `Omega` cannot vanish identically.  On a compact minimal set the Gaussian enstrophy observable is continuous and strictly positive, so

\[
\boxed{
Z_{0,*}
:=
\min_{U\in M}
\int\phi_0|\Omega|^2dY
>0.
}
\]

Hence

\[
\boxed{
\left\langle
\int\phi_0\Pi H\,dY
\right\rangle_\mu
<0.
}
\]

A recurrent W1 survivor therefore requires a strict negative correlation between augmented Bernoulli and radial momentum.

This statement is gauge invariant because `int phi_0 H=0` statewise.

---

## 13. Bernoulli oscillation cannot collapse to a spatial constant

Let

\[
(\Pi)_{\phi_0}
:=
\frac{\int\phi_0\Pi}{\int\phi_0}.
\]

Since constants are orthogonal to `H` under `phi_0`,

\[
\int\phi_0\Pi H
=
\int\phi_0
[\Pi-(\Pi)_{\phi_0}]H.
\]

Cauchy--Schwarz on the product probability space `mu times phi_0 dY` gives

\[
2\nu^2\bar Z_0
\le
\left\langle
\int\phi_0|\Pi-(\Pi)_{\phi_0}|^2
\right\rangle^{1/2}
\left\langle
\int\phi_0H^2
\right\rangle^{1/2},
\]

where

\[
\bar Z_0
:=
\left\langle\int\phi_0|\Omega|^2\right\rangle.
\]

Thus

\[
\boxed{
\left\langle
\int\phi_0|\Pi-(\Pi)_{\phi_0}|^2
\right\rangle
\ge
\frac{4\nu^4\bar Z_0^2}
{\left\langle\int\phi_0H^2\right\rangle}.
}
\]

The denominator is finite on the compact W1 class.

Therefore the augmented Bernoulli field has a nonzero recurrent spatial oscillation floor.

---

## 14. Convert oscillation to a gradient floor

The normalized Gaussian with density proportional to

\[
e^{-|Y|^2/(4\nu)}
\]

has covariance `2nu I`, so the Gaussian Poincare inequality gives

\[
\int\phi_0
|f-(f)_{\phi_0}|^2
\le
2\nu
\int\phi_0|\nabla f|^2.
\]

Apply this to `Pi`. Then

\[
\boxed{
\left\langle
\int\phi_0|\nabla\Pi|^2
\right\rangle_\mu
\ge
\frac{2\nu^3\bar Z_0^2}
{\left\langle\int\phi_0H^2\right\rangle_\mu}
>0.
}
\]

Using compactness more coarsely,

\[
\bar Z_0\ge Z_{0,*}>0
\]

and

\[
H_{0,+}
:=
\max_{U\in M}\int\phi_0H^2<\infty,
\]

so

\[
\boxed{
\left\langle
\int\phi_0|\nabla\Pi|^2
\right\rangle_\mu
\ge
\frac{2\nu^3Z_{0,*}^2}{H_{0,+}}
>0.
}
\]

Thus recurrent W1 cannot become Bernoulli-flat in its formed finite core.

---

## 15. DSD interpretation

The pointwise time-dependent Bernoulli equation first appears to leave the branch

\[
P_s
\]

as an independent obstruction.

The gauge-safe reformulation and invariant OU averaging show that this is not the correct terminal classification.

The temporal pressure derivative disappears from the invariant integrated ledger and leaves instead the exact recurrent condition

\[
\boxed{
\text{weighted vorticity loss}
\Longleftrightarrow
\text{negative augmented-Bernoulli/radial-momentum correlation}.
}
\]

Therefore `P_s` should not be promoted to a new final branch.

The actual invariant requirement is a persistent spatial Bernoulli sorting/gradient structure.

This is consistent with the previous critical Bernoulli surplus, but it is a distinct finite-core identity rather than a relabeling of the endpoint shell flux.

---

## 16. What this does not prove

The negative correlation and gradient floor are necessary conditions, not contradictions.

A recurrent solution may in principle sustain a nonzero `grad Pi` indefinitely.

No available energy inequality directly controls

\[
\int\phi_0|\nabla\Pi|^2
\]

strongly enough to make the positive invariant floor impossible.

Likewise the classical stationary maximum principle cannot be invoked merely from the invariant correlation identity.

What has been removed is a bookkeeping ambiguity: **time-dependent pressure itself is not a new terminal escape.**

---

## 17. Updated narrow target

A new possible endpoint closure theorem is now:

\[
\boxed{
\text{a finite-energy blow-up prelimit cannot generate a compact recurrent limit with}
\quad
\left\langle\int\phi_0|\nabla\Pi|^2\right\rangle>0
}
\]

while simultaneously carrying the positive critical shell current.

More realistically, one should seek a bridge between the finite-core Bernoulli gradient floor and the already proved large-scale Bernoulli surplus `S_B(infinity)>0`.

If one can show that the same Bernoulli sorting cannot persist at both the OU core scale and every critical log scale without a summable gain or a derivative escalation, the single W1 endpoint would close.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
