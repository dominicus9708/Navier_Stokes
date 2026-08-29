# DSD M5-245 — Energy-Transverse Branch: Strict Outward Bernoulli-Flux Identity

Date: 2026-08-30

Parent: `DSD_M5_244_LOCAL_RG_ENERGY_DENSITY_EXACT_FLUX_IDENTITY_2026-08-30.md`

Status: **EXACT POSITIVE SIGN IDENTITY / ON THE LOCALLY ENERGY-TRANSVERSE RESIDUAL BRANCH, RECURRENT DEGREE `-1` GEOMETRY CONVERTS THE NEGATIVE CRITICAL ENERGY CURRENT INTO A STRICTLY POSITIVE OUTWARD BERNOULLI-RADIAL CORRELATION / THE POSITIVE AMOUNT IS EXACTLY VISCOSITY TIMES THE LOG-RADIAL PLUS ANGULAR SHAPE-DERIVATIVE ENERGY / THE BRANCH THEREFORE MERGES WITH A FINITE KINETIC-RADIAL OR PRESSURE-RADIAL PAYMENT FORK / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-244

On the strong local energy-transverse branch,

\[
a(y)=\int_{S^2}\Phi\cdot\mathcal R_T\,d\theta=0
\qquad\forall y.
\]

The exact current equation is

\[
\boxed{j'(y)-j(y)=\nu d(y),}
\]

where

\[
d(y)=\int_{S^2}r^4|\nabla T|^2d\theta
\]

and

\[
\begin{aligned}
j(y)=\int_{S^2}\Bigg[
&\frac\nu2\partial_y|\Phi|^2
-\nu|\Phi|^2\\
&-\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\Bigg]d\theta.
\end{aligned}
\]

For an invariant mean on the compact log-translation hull,

\[
\boxed{\langle j\rangle=-\nu\langle d\rangle.}
\]

---

## 2. Exact gradient decomposition for a degree `-1` tail

For

\[
T(r\theta)=r^{-1}\Phi(y,\theta),
\]

the radial derivative is

\[
\partial_rT
=r^{-2}(\Phi_y-\Phi).
\]

The orthonormal tangential derivatives contribute

\[
r^{-2}\nabla_{S^2}\Phi.
\]

Therefore

\[
\boxed{
r^4|\nabla T|^2
=|\Phi_y-\Phi|^2
+|\nabla_{S^2}\Phi|^2.}
\]

After spherical and invariant-log averaging,

\[
\langle\Phi\cdot\Phi_y\rangle
=\frac12\langle\partial_y|\Phi|^2\rangle
=0.
\]

Hence

\[
\boxed{
\langle d\rangle
=\left\langle
\int_{S^2}
\left(
|\Phi_y|^2
+|\Phi|^2
+|\nabla_S\Phi|^2
\right)d\theta
\right\rangle.
}
\]

In particular,

\[
\boxed{
\langle d\rangle-
\left\langle\int|\Phi|^2\right\rangle
=
\left\langle\int
(|\Phi_y|^2+|\nabla_S\Phi|^2)
\right\rangle
\ge0.
}
\]

---

## 3. Average the explicit current

The total `y` derivative in `j` has zero invariant mean. Therefore

\[
\langle j\rangle
=
-\nu\left\langle\int|\Phi|^2\right\rangle
-
\left\langle
\int
\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\right\rangle.
\]

But M5-244 also gives

\[
\langle j\rangle=-\nu\langle d\rangle.
\]

Equating the two expressions yields

\[
\boxed{
\left\langle
\int_{S^2}
\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\,d\theta
\right\rangle
=
\nu
\left[
\langle d\rangle-
\left\langle\int|\Phi|^2\right\rangle
\right].
}
\]

Using Section 2:

\[
\boxed{
\left\langle
\int_{S^2}
\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\,d\theta
\right\rangle
=
\nu
\left\langle
\int_{S^2}
\left(
|\Phi_y|^2
+|\nabla_S\Phi|^2
\right)d\theta
\right\rangle.
}
\]

This is the central identity.

---

## 4. Strict positivity on the aperiodic branch

M5-219/224 gives a nonzero recurrent log-radial homogeneity action:

\[
\Phi_y\not\equiv0
\]

with positive invariant-mean derivative content.

Therefore

\[
\boxed{
\left\langle
\int
(|\Phi_y|^2+|\nabla_S\Phi|^2)
\right\rangle
>0.
}
\]

Consequently

\[
\boxed{
\left\langle
\int
\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\right\rangle
>0.
}
\]

Thus local RG energy transversality requires a strictly positive correlation between outward radial velocity and the Bernoulli scalar

\[
B:=\frac{|\Phi|^2}{2}+\Pi.
\]

---

## 5. Zero mass flux makes this a genuine correlation

For every `y`, incompressibility gives

\[
\boxed{\int_{S^2}\Phi_r\,d\theta=0.}
\]

Hence adding any spherical constant to `B` does not change the Bernoulli correlation.

The positivity cannot be explained by a nonzero mean radial mass flux.

It requires angular covariance:

\[
\boxed{
\operatorname{Cov}_{S^2}(B,\Phi_r)>0
\quad\text{on average in }y.
}
\]

Therefore outward sectors must preferentially coincide with above-mean Bernoulli values, or equivalently inward sectors with below-mean values.

---

## 6. Finite kinetic/pressure fork

Split the exact positive correlation as

\[
\mathcal C_B
=\mathcal C_K+\mathcal C_P,
\]

where

\[
\boxed{
\mathcal C_K
:=
\frac12
\left\langle
\int|\Phi|^2\Phi_r
\right\rangle,
}
\]

and

\[
\boxed{
\mathcal C_P
:=
\left\langle
\int\Pi\Phi_r
\right\rangle.
}
\]

Let

\[
\mathcal G
:=
\left\langle
\int
(|\Phi_y|^2+|\nabla_S\Phi|^2)
\right\rangle
>0.
\]

Then

\[
\boxed{
\mathcal C_K+\mathcal C_P
=\nu\mathcal G.
}
\]

Therefore at least one satisfies

\[
\boxed{
\mathcal C_K
\ge\frac{\nu\mathcal G}{2}
\quad\lor\quad
\mathcal C_P
\ge\frac{\nu\mathcal G}{2}.
}
\]

This is a formed two-channel payment fork.

---

## 7. Kinetic-radial payer

If

\[
\mathcal C_K
\ge\frac{\nu\mathcal G}{2},
\]

then

\[
\boxed{
\left\langle
\int|\Phi|^2\Phi_r
\right\rangle
\ge\nu\mathcal G.
}
\]

Since the negative radial sector only decreases the signed correlation,

\[
\left\langle
\int|\Phi|^2(\Phi_r)_+
\right\rangle
\ge\nu\mathcal G.
\]

This is a direct outward high-kinetic-energy sector locking condition, closely analogous to M5-233 but with the tail's own kinetic density as the weight rather than the finite-dilate difference.

---

## 8. Pressure-radial payer

If

\[
\mathcal C_P
\ge\frac{\nu\mathcal G}{2},
\]

then pressure must correlate positively with outward radial sectors:

\[
\boxed{
\left\langle
\int\Pi\Phi_r
\right\rangle
\ge\frac{\nu\mathcal G}{2}.
}
\]

Because `Phi_r` has zero spherical mean, one may again invert the spherical Laplacian and convert this into a tangential pressure-gradient correlation exactly as in M5-234.

Thus this branch routes to

\[
\boxed{
\text{large tangential pressure gradient}
\to
H2\text{-type derivative or large critical coefficient}.
}
\]

The precise constants depend on the corresponding tail, rather than relative-mode, spherical Poincare bounds.

---

## 9. Relation to the earlier stationary-current identity

For an actual stationary tail `F_T=0`, the same local energy identity has `a=0` automatically.

Therefore the Bernoulli-flux formula is not by itself a nonstationarity contradiction.

Its new value here is structural:

- in the residual-active `E_trans` branch, it is **forced by residual energy orthogonality**;
- its positive amount is exactly the nontrivial scale/angular shape derivative energy;
- it routes the supposedly invisible residual back into radial/pressure geometric channels.

---

## 10. DSD verdict

The strong first-order transverse branch satisfies

\[
\boxed{
E_{trans}
\Longrightarrow
K_{rad}^+
\lor
P_{rad}^+,
}
\]

where

\[
K_{rad}^+:
\text{outward radial sectors carry elevated kinetic energy},
\]

and

\[
P_{rad}^+:
\text{outward radial sectors carry elevated pressure / tangential pressure-gradient cost}.
\]

Thus first-order energy invisibility does **not** produce a free symmetry mode.  It forces a strict Bernoulli-flux payment.

### NEXT TARGET

Quantify the kinetic-radial branch using the compact Type-I amplitude ceiling and zero spherical flux.  Determine whether its required outward-sector locking forces a fixed radial-strain floor via M5-235, thereby merging `E_trans` entirely into the already identified large-strain/H2/large-coefficient stationary-style certificates.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]