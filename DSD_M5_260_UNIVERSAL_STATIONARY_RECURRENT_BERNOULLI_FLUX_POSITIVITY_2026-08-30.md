# DSD M5-260 — Universal Stationary-Recurrent Bernoulli-Flux Positivity

Date: 2026-08-30

Parent: `DSD_M5_259_LANDAU_HEAD_PRESSURE_SIGN_CHANGE_AND_POSITIVE_RADIAL_CORRELATION_2026-08-30.md`

Status: **STRONG POSITIVE STATIONARY IDENTITY / FOR ANY SMOOTH DIVERGENCE-FREE STATIONARY CRITICAL TAIL `T=r^-1 Phi(log r,theta)` WITH A BOUNDED RECURRENT LOG-TRANSLATION HULL, THE SCALE-NORMALIZED RADIAL BERNOULLI CORRELATION IS EXACTLY THE POSITIVE ANGULAR/LOG-PHASE DIRICHLET ENERGY `nu <|Phi_y|^2+|grad_S Phi|^2>` / HENCE EVERY NONZERO STATIONARY RECURRENT CRITICAL TAIL HAS STRICTLY POSITIVE OUTWARD BERNOULLI CORRELATION, NOT MERELY LANDAU OR SMALL PERTURBATIONS / COMBINED WITH M5-258 THIS ALSO FIXES THE MEAN HEAD PRESSURE BY `2 Hbar = Zbar-Gbar` / GLOBAL REGULARITY UNPROVED.**

---

## 1. Stationary energy current

Let

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=0,
\qquad
\nabla\cdot T=0
\]

on `R3\{0}`.

Set

\[
H:=P+\frac12|T|^2.
\]

Dotting the stationary equation with `T` gives

\[
-\nu\Delta\frac{|T|^2}{2}
+\nu|\nabla T|^2
+T\cdot\nabla H=0.
\]

Therefore the physical energy current

\[
\boxed{
J_E
:=
H T
-\nu\nabla\frac{|T|^2}{2}
}
\]

satisfies

\[
\boxed{
\nabla\cdot J_E
=-\nu|\nabla T|^2.
}
\]

---

## 2. Critical log representation

Write

\[
T(r,\theta)
=
\frac1r\Phi(y,\theta),
\qquad
H(r,\theta)
=
\frac1{r^2}h(y,\theta),
\qquad
y=\log r.
\]

Treat `Phi` as an `R3`-valued map on the sphere. Then

\[
\partial_rT
=
\frac1{r^2}(\Phi_y-\Phi),
\]

and the angular derivative contributes

\[
\frac1{r^2}\nabla_{S^2}\Phi.
\]

Hence

\[
\boxed{
|\nabla T|^2
=
\frac1{r^4}
\left(
|\Phi_y-\Phi|^2
+|\nabla_{S^2}\Phi|^2
\right).
}
\]

Define

\[
\boxed{
d(y)
:=
\int_{S^2}
\left(
|\Phi_y-\Phi|^2
+|\nabla_S\Phi|^2
\right)d\theta.
}
\]

---

## 3. Scale-normalized radial energy flux

Let

\[
F_E(r)
:=
\int_{|x|=r}J_E\cdot e_r\,dS.
\]

Because `J_E,r~r^-3`, write

\[
\boxed{
F_E(r)=r^{-1}j(y).
}
\]

The divergence theorem on an annulus gives

\[
\frac{d}{dr}F_E(r)
=-\nu\int_{|x|=r}|\nabla T|^2dS.
\]

Substitution of the critical scaling yields

\[
\boxed{
j_y-j=-\nu d(y).}
\]

---

## 4. Recurrent solution of the flux ODE

For a bounded recurrent `d(y)` and bounded recurrent `j(y)`, the unique bounded solution of

\[
j_y-j=-\nu d
\]

is

\[
\boxed{
 j(y)
=
\nu\int_0^\infty e^{-a}d(y+a)da.
}
\]

Indeed differentiating the right side gives `j_y=j-nu d`.

Therefore

\[
\boxed{j(y)\ge0}
\]

pointwise, and it is strictly positive whenever the future dissipation profile is nonzero.

For any invariant mean,

\[
\boxed{
\langle j\rangle
=\nu\langle d\rangle.
}
\]

---

## 5. Direct expansion of `j`

Let

\[
k:=\frac12|\Phi|^2.
\]

Since

\[
\partial_r\left(\frac{k}{r^2}\right)
=
\frac1{r^3}(k_y-2k),
\]

we get

\[
\boxed{
 j(y)
=
\int_{S^2}
\left[
 h\Phi_r
+\nu|\Phi|^2
-\nu\Phi\cdot\Phi_y
\right]d\theta.
}
\]

Under an invariant log mean,

\[
\left\langle\int\Phi\cdot\Phi_y\right\rangle
=
\frac12
\left\langle
\partial_y\int|\Phi|^2
\right\rangle
=0.
\]

Thus

\[
\boxed{
\langle j\rangle
=
\mathcal B_r
+\nu\mathcal E_\Phi,
}
\]

where

\[
\mathcal B_r
:=
\left\langle\int h\Phi_r\right\rangle,
\]

and

\[
\mathcal E_\Phi
:=
\left\langle\int|\Phi|^2\right\rangle.
\]

---

## 6. Exact positive Bernoulli identity

Expand `d`:

\[
\begin{aligned}
\langle d\rangle
&=
\left\langle\int
\left(
|\Phi_y|^2+|\Phi|^2
-2\Phi\cdot\Phi_y
+|\nabla_S\Phi|^2
\right)
\right\rangle\\
&=
\mathcal E_\Phi
+
\left\langle\int
\left(
|\Phi_y|^2+|\nabla_S\Phi|^2
\right)
\right\rangle.
\end{aligned}
\]

Use

\[
\langle j\rangle=\nu\langle d\rangle
\]

and

\[
\langle j\rangle=\mathcal B_r+\nu\mathcal E_\Phi.
\]

Cancel the common amplitude term. The result is

\[
\boxed{
\mathcal B_r
=
\nu
\left\langle\int_{S^2}
\left(
|\Phi_y|^2
+|\nabla_{S^2}\Phi|^2
\right)d\theta
\right\rangle.
}
\]

This is the main identity.

---

## 7. Strict positivity for every nonzero divergence-free tail

The right side is nonnegative.

Equality would require

\[
\Phi_y=0,
\qquad
\nabla_{S^2}\Phi=0,
\]

so `Phi` is a constant Cartesian vector.

Then

\[
T(x)=\frac a{|x|}
\]

for a constant vector `a`.

But

\[
\nabla\cdot\left(\frac a{|x|}\right)
=-\frac{a\cdot x}{|x|^3},
\]

which vanishes identically only for `a=0`.

Therefore every nonzero divergence-free stationary recurrent critical tail satisfies

\[
\boxed{\mathcal B_r>0.}
\]

This includes homogeneous Landau tails and nonhomogeneous periodic/aperiodic tails.

---

## 8. Quantitative nonhomogeneous floor

On the aperiodic/minimal stationary branch, M5-219/224 supply a positive log-phase action for `Phi_y` on positive-density cells.

If the compact tail class has a uniform `L-infinity` bound on `Phi_y`, the existing critical `L3` phase residue converts to a positive `L2` phase floor on the selected cells:

\[
\int|\Phi_y|^2
\ge
\frac{\left(\int|\Phi_y|^3\right)}{\|\Phi_y\|_\infty}.
\]

Hence

\[
\boxed{
\mathcal B_r
\ge
\nu b_{ph}>0
}
\]

with a quantitative class-dependent constant on the nonhomogeneous minimal stationary branch.

Even without nonhomogeneity, angular variation yields strict positivity for every nonzero Landau-type state.

---

## 9. Combine with the head-pressure identity

M5-258 gives

\[
2\nu\overline H_0+\mathcal B_r
=\nu\mathcal Z_T.
\]

Insert the new formula:

\[
\boxed{
2\overline H_0
+
\left\langle\int
\left(
|\Phi_y|^2+|\nabla_S\Phi|^2
\right)
\right\rangle
=
\mathcal Z_T.
}
\]

Therefore the invariant mean head pressure is fixed exactly by

\[
\boxed{
\overline H_0
=
\frac12
\left[
\mathcal Z_T
-
\left\langle\int
(|\Phi_y|^2+|\nabla_S\Phi|^2)
\right\rangle
\right].
}
\]

Its sign remains indefinite, explaining the Landau sign behavior without weakening the positive Bernoulli flux result.

---

## 10. Relation to earlier radial/pressure channels

M5-231 and M5-245 kept radial transport and pressure-radial correlation separate because no cancellation was available for a general residual-active tail.

On the **stationary** branch the present energy identity recombines them into the single positive head-pressure/kinetic energy current.

Thus the stationary endpoint no longer has an arbitrary-sign radial Bernoulli channel:

\[
\boxed{
S_{crit}^{stationary}
\Longrightarrow
\mathcal B_r>0.
}
\]

---

## 11. What this still does not prove

A positive outward scale-normalized energy flux from the stationary point-force core is compatible with Landau solutions.

In the stationary punctured model, the point-force singularity can supply this flux.

For the actual W1 Navier--Stokes state there is no physical point force; the inner smooth core must replace the source. The next bridge is therefore:

\[
\boxed{
\text{stationary tail positive Bernoulli flux}
\to
\text{finite-depth smooth-core energy-export requirement}.
}
\]

M5-248 provides the fixed-depth inheritance mechanism needed to formulate this bridge without an expanding-window limit.

---

## 12. DSD verdict

### PROVED

For every nonzero stationary recurrent critical tail,

\[
\boxed{
\left\langle\int h\Phi_r\right\rangle
=
\nu
\left\langle\int
(|\Phi_y|^2+|\nabla_S\Phi|^2)
\right\rangle
>0.
}
\]

### STRENGTHENED

Landau positivity from M5-259 is a special case of a universal stationary recurrent identity.

### NEXT TARGET

Transfer this strict positive radial energy-current requirement through one fixed RG depth to the smooth W1 core, then compare it with the exact moving-ball/compensated-variance turnover ledger. This may finally connect the stationary tail endpoint to an already costed finite-stage export channel.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
