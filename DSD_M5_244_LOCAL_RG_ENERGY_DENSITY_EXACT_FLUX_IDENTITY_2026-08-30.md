# DSD M5-244 — Local RG Energy-Density Exact Flux Identity

Date: 2026-08-30

Parent: `DSD_M5_243_FIRST_RG_ENERGY_ORTHOGONALITY_FIREWALL_AND_LOCAL_DENSITY_REFINEMENT_2026-08-30.md`

Status: **EXACT LOCAL IDENTITY / THE LOG-RADIAL FIRST-RG ENERGY DENSITY IS THE DERIVATIVE-MINUS-SCALING OF A CRITICAL ENERGY CURRENT MINUS VISCOUS DISSIPATION / IF THE RESIDUAL IS LOCALLY ENERGY-TRANSVERSE AT EVERY LOG RADIUS, THE NORMALIZED ENERGY CURRENT IS NOT ZERO: IT IS THE UNIQUE BOUNDED RECURRENT CONVOLUTION THAT EXACTLY PAYS THE POSITIVE VISCOUS CELL DISSIPATION / THIS CREATES A STRICT FLUX CERTIFICATE BUT NOT YET A CONTRADICTION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Unprojected residual representation

The projected residual is

\[
F_T
=\nu\Delta T-\mathbb P\nabla\cdot(T\otimes T).
\]

Choose the canonical pressure gauge so that equivalently

\[
\boxed{
F_T
=\nu\Delta T-(T\cdot\nabla)T-\nabla P,
\qquad\nabla\cdot T=0.
}
\]

Pair with `T`.

---

## 2. Exact local energy identity

Use

\[
T\cdot\Delta T
=\Delta\frac{|T|^2}{2}-|\nabla T|^2,
\]

\[
T\cdot(T\cdot\nabla T)
=\nabla\cdot\left(\frac{|T|^2}{2}T\right),
\]

and

\[
T\cdot\nabla P
=\nabla\cdot(PT).
\]

Hence

\[
\boxed{
T\cdot F_T
=\nabla\cdot J_E
-\nu|\nabla T|^2,
}
\]

where

\[
\boxed{
J_E
:=
\frac\nu2\nabla|T|^2
-\left(\frac{|T|^2}{2}+P\right)T.
}
\]

This identity is pointwise on the punctured smooth region.

---

## 3. Critical log-cylinder scaling

Write

\[
T(r\theta)=r^{-1}\Phi(y,\theta),
\qquad
P(r\theta)=r^{-2}\Pi(y,\theta),
\qquad
y=\log r.
\]

The residual has degree `-3` form

\[
F_T(r\theta)=r^{-3}\mathcal R_T(y,\theta).
\]

Thus

\[
T\cdot F_T
=r^{-4}\Phi\cdot\mathcal R_T.
\]

The energy current has degree `-3`:

\[
J_E(r\theta)=r^{-3}\mathcal J_E(y,\theta).
\]

Define the spherical normalized quantities

\[
\boxed{
a(y)
:=
\int_{S^2}
\Phi\cdot\mathcal R_T\,d\theta,
}
\]

\[
\boxed{
j(y)
:=
\int_{S^2}
(\mathcal J_E)_r\,d\theta,
}
\]

and

\[
\boxed{
d(y)
:=
\int_{S^2}
r^4|\nabla T|^2\,d\theta.
}
\]

Here `d(y)>=0` is a scale-invariant dissipation density.

---

## 4. Divergence of a degree `-3` current

If

\[
J=r^{-3}(j_r e_r+j_\tau),
\]

then

\[
\nabla\cdot J
=r^{-4}
\left(
\partial_y j_r-j_r
+\operatorname{div}_{S^2}j_\tau
\right).
\]

Integrate over the sphere.  The angular divergence vanishes.

Therefore the local energy identity gives the exact scalar equation

\[
\boxed{
a(y)
=j'(y)-j(y)-\nu d(y).
}
\]

No periodicity or stationary-residual assumption is used.

---

## 5. Explicit current coefficient

Since

\[
\frac12|T|^2
=\frac1{2r^2}|\Phi|^2,
\]

we have

\[
\partial_r\frac{|T|^2}{2}
=r^{-3}
\left(
\frac12\partial_y|\Phi|^2-|\Phi|^2
\right).
\]

Thus

\[
\boxed{
\begin{aligned}
j(y)
=\int_{S^2}
\Bigg[
&\frac\nu2\partial_y|\Phi|^2
-\nu|\Phi|^2\\
&-\left(\frac{|\Phi|^2}{2}+\Pi\right)\Phi_r
\Bigg]d\theta.
\end{aligned}
}
\]

This displays the three mechanisms carried by the current:

1. viscous radial gradient of kinetic energy;
2. critical scaling kinetic term;
3. nonlinear kinetic/pressure radial transport.

---

## 6. Strong energy-transverse branch

The `E_trans` branch of M5-243 is

\[
\boxed{a(y)=0\quad\forall y.}
\]

Then

\[
\boxed{
j'(y)-j(y)=\nu d(y).}
\]

Because `Phi` belongs to a compact recurrent log-translation hull, `j` and `d` are bounded recurrent observables.

The bounded solution of this first-order equation is unique and equals

\[
\boxed{
j(y)
=-\nu\int_0^\infty e^{-s}d(y+s)\,ds.
}
\]

Indeed differentiation gives `j'-j=nu d`.

Therefore

\[
\boxed{j(y)\le0}
\]

for every `y`, and if the future translate of `d` is not identically zero then

\[
\boxed{j(y)<0.}
\]

---

## 7. Invariant-mean identity

For any invariant probability measure on the compact translation hull,

\[
\langle j'\rangle=0.
\]

Thus from `a=0`,

\[
\boxed{
\langle j\rangle
=-\nu\langle d\rangle.
}
\]

So local energy transversality does not eliminate energy transfer.

It forces a negative normalized current whose mean magnitude is exactly the viscous dissipation density.

With the present sign convention, negative `j` means the current in `J_E` points on average opposite to the outward radial direction.

---

## 8. Relation to the homogeneity-defect residue

M5-224 gives a positive mean log-scale action of

\[
\Phi_y.
\]

The full gradient density `d(y)` contains positive quadratic contributions from log-radial and angular derivatives of the degree `-1` field.

In particular, on the compact bounded tail class, the positive `L3` homogeneity-defect residue implies a positive invariant-mean `L2` derivative content on a fixed cell by Holder and bounded-volume interpolation.

Hence on the aperiodic survivor,

\[
\boxed{
\langle d\rangle>0.
}
\]

Consequently the `E_trans` branch has a strict mean current:

\[
\boxed{
\langle j\rangle<0.
}
\]

---

## 9. Why this is not yet a contradiction

A stationary critical `1/r` tail already obeys an analogous radial-current/dissipation balance.

A bounded recurrent positive dissipation density can be balanced by the exponentially weighted future convolution above.

Therefore

\[
\boxed{
\text{strict recurrent current}
\not\Rightarrow
\text{impossibility}.
}
\]

The current certificate is, however, much stronger than the scalar condition `A=0`: it identifies exactly what the residual must do to remain energy-transverse.

---

## 10. DSD verdict

The first-order locally transverse residual branch is now

\[
\boxed{
\begin{cases}
a(y)=0,\\
j'(y)-j(y)=\nu d(y),\\
j(y)=-\nu\displaystyle\int_0^\infty e^{-s}d(y+s)ds,\\
\langle j\rangle=-\nu\langle d\rangle<0.
\end{cases}}
\]

Thus the residual can hide from first RG energy only by maintaining an exact critical radial energy-current balance on every log scale.

### NEXT TARGET

Compare this forced current with the zero spherical mass flux and the M5-233 outward scale-phase locking.  In particular, decompose `j` into viscous, kinetic, and pressure radial pieces and test whether a strictly negative `j` on every phase forces a pressure/radial-sector certificate already covered by M5-233--235, or leaves a new pure viscous current branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]