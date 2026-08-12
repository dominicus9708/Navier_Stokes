# Axis alignment versus axial localization: a divergence-free uncertainty constraint

Date: 2026-08-13

Status: **DERIVED DIVERGENCE-FREE / UNCERTAINTY INEQUALITY / OPEN LOCAL-SPARSENESS TRANSFER**.

This note quantifies a basic geometric obstruction to a finite-energy vorticity field being both nearly one-axis and tightly localized along that same axis.

## 1. Constant-axis decomposition

Fix a unit vector `n` and decompose

\[
\boxed{
\omega=\alpha n+\beta,
\qquad
\alpha=n\cdot\omega,
\qquad
\beta=P_{n^\perp}\omega.
}
\]

Then

\[
\|\omega\|_2^2
=\|\alpha\|_2^2+\|\beta\|_2^2.
\]

Write

\[
E=\|\omega\|_2^2,
\qquad
O_n=\|\beta\|_2^2.
\]

Thus

\[
\|\alpha\|_2^2=E-O_n.
\]

## 2. Divergence-free coupling of axial and off-axis pieces

Because

\[
\nabla\cdot\omega=0,
\]

we have

\[
\boxed{
\partial_n\alpha
=-\nabla\cdot\beta.
}
\]

The Fourier form is

\[
(\xi\cdot n)\widehat\alpha
=-\xi\cdot\widehat\beta.
\]

Since `beta` is pointwise orthogonal to `n`, only the transverse part of `xi` contributes to the last scalar product. Therefore

\[
|(\xi\cdot n)\widehat\alpha|
\le|\xi|\,|\widehat\beta|.
\]

By Plancherel,

\[
\boxed{
\|\partial_n\alpha\|_2^2
\le
\|\nabla\beta\|_2^2.
}
\]

Thus axial variation of the dominant component cannot occur without gradient activity in the off-axis vorticity sector.

## 3. Axial uncertainty inequality

Let

\[
s=x\cdot n.
\]

For any real number `s_0`, integration by parts in the `n` direction gives

\[
\|\alpha\|_2^2
=-2\operatorname{Re}
\int(s-s_0)\overline\alpha\,\partial_n\alpha\,dx.
\]

Hence

\[
\boxed{
\|\alpha\|_2^2
\le
2\|(s-s_0)\alpha\|_2
\|\partial_n\alpha\|_2.
}
\]

Define the minimal axial `L^2` spread

\[
\boxed{
L_n^2
=
\inf_{s_0\in\mathbb R}
\frac{
\int|(x\cdot n)-s_0|^2|\alpha(x)|^2dx
}{
\|\alpha\|_2^2
}.
}
\]

Then

\[
\boxed{
\|\partial_n\alpha\|_2^2
\ge
\frac{\|\alpha\|_2^2}{4L_n^2}
=
\frac{E-O_n}{4L_n^2}.
}
\]

Combining with incompressibility,

\[
\boxed{
\|\nabla\beta\|_2^2
\ge
\frac{E-O_n}{4L_n^2}.
}
\]

## 4. Combine with off-axis `H^{-1}` coercivity

The optimal-off-axis Riccati note established

\[
\|\nabla\beta\|_2^2
\ge
\frac{O_n^2}{\|u\|_2^2}.
\]

Using the kinetic-energy bound

\[
\|u(t)\|_2^2\le U_0=\|u_0\|_2^2,
\]

we therefore have the dual coercivity

\[
\boxed{
\|\nabla\beta\|_2^2
\ge
\max\left\{
\frac{O_n^2}{U_0},
\frac{E-O_n}{4L_n^2}
\right\}.
}
\]

The two terms control opposite geometric regimes:

- large off-axis energy forces gradient cost through `H^{-1}` interpolation;
- very small off-axis energy still forces gradient cost if the aligned component is tightly localized along the axis.

## 5. Optimal covariance axis

At each time choose a principal covariance axis `n(t)`, so

\[
O=E\Pi
\]

is minimal among constant spatial axes.

Then

\[
E-O=E(1-\Pi)
\]

is the energy of the dominant axial vorticity component.

If

\[
\Pi\ll1
\]

and the axial spread `L_n` remains bounded on a small physical scale, the localization lower bound is approximately

\[
\boxed{
\|\nabla\beta\|_2^2
\gtrsim
\frac{E}{L_n^2}.
}
\]

Thus near-one-axis alignment cannot be used to eliminate projective/off-axis viscous cost while simultaneously keeping the dominant vorticity localized to a short axial region.

## 6. Exact one-axis finite-energy consequence

If

\[
O_n=0,
\]

then

\[
\omega=\alpha n.
\]

Divergence-free gives

\[
\partial_n\alpha=0.
\]

A nonzero function constant along an infinite spatial direction cannot belong to `L^2(R^3)`.

Therefore, in the finite-enstrophy whole-space class,

\[
\boxed{
O_n=0
\Longrightarrow
\omega=0.
}
\]

A nontrivial finite-energy whole-space vorticity can approach a one-axis covariance state only by becoming increasingly extended along that axis and/or by retaining a nonzero off-axis sector.

## 7. DSD / geometric interpretation

The covariance axis is an axis-property descriptor on the existing 3D field.

The inequality shows that two channels cannot be suppressed independently:

\[
\boxed{
\text{projective defect}
\quad\leftrightarrow\quad
\text{axial structural extent}.
}
\]

Near alignment lowers the directional defect but, unless the structure elongates, incompressibility transfers the cost into off-axis gradients.

This is consistent with the geometric picture of intense vorticity organizing into elongated vortex structures rather than terminating inside the fluid.

## 8. Remaining bridge

The global axial spread `L_n` can become large without contradiction. Therefore this inequality alone does not prove regularity.

The next target is local: combine

1. an adjoint observation window concentrated near a candidate singular core;
2. local covariance alignment;
3. divergence-free flux through short cylinders aligned with the local principal axis;
4. the existing volume-to-line-sparseness criterion.

The intended dichotomy is:

\[
\boxed{
\text{aligned core terminates/localizes}
\Rightarrow
\text{off-axis flux/gradient cost},
}
\]

or

\[
\boxed{
\text{aligned core persists axially}
\Rightarrow
\text{elongated tube geometry, to be tested against transverse sparseness}.
}
\]

Status: **OPEN LOCAL TUBE-FLUX / SPARSENESS CLOSURE**.
