# Projective-axis polarity dichotomy: sign mixing versus oriented flux

Date: 2026-08-13

Status: **DERIVED LOCAL POLARITY/PALINSTROPHY LEMMA / OPEN ORIENTED-FLUX PERSISTENCE CLOSURE**.

The projective covariance intentionally identifies `xi` and `-xi`. Therefore a projectively one-axis intense core can still contain strong vorticity pointing in both orientations along that axis.

This note separates that residual degree of freedom into a polarity channel.

## 1. Axial scalar and polarity sets

Fix a unit axis `n` on a ball

\[
B=B_r(x_0).
\]

Define

\[
\boxed{\alpha=n\cdot\omega.}
\]

Let

\[
W=\|\omega\|_{L^\infty(B)}
\]

and fix `0<b<1`. Define the two oriented intense subsets

\[
A_+
=\{x\in B:\alpha(x)\ge bW\},
\]

\[
A_-
=\{x\in B:\alpha(x)\le-bW\}.
\]

Let

\[
\theta_+=|A_+|/|B|,
\qquad
\theta_-=|A_-|/|B|.
\]

## 2. Pair variance forces scalar variance when both polarities are present

The scalar pair-variance identity is

\[
\fint_B|\alpha-\bar\alpha_B|^2dx
=
\frac1{2|B|^2}
\iint_{B\times B}
|\alpha(x)-\alpha(y)|^2dxdy.
\]

For `(x,y) in A_+ x A_-`,

\[
|\alpha(x)-\alpha(y)|
\ge2bW.
\]

The reversed pair `A_- x A_+` gives the same contribution. Hence

\[
\boxed{
\fint_B|\alpha-\bar\alpha_B|^2dx
\ge
4b^2W^2\theta_+\theta_-.
}
\]

## 3. Poincare lower bound

The ball Poincare inequality gives

\[
\fint_B|\alpha-\bar\alpha_B|^2
\le
C_Pr^2\fint_B|\nabla\alpha|^2.
\]

Therefore

\[
\boxed{
\int_B|\nabla\alpha|^2dx
\ge
c
\frac{W^2|B|}{r^2}
\,b^2\theta_+\theta_-.
}
\]

Since

\[
|\nabla\alpha|
\le|\nabla\omega|
\]

for a constant axis `n`, this is a palinstrophy lower bound.

If `n=n_r(x)` varies spatially, then

\[
\nabla(n_r\cdot\omega)
=(\nabla n_r)^T\omega+(\nabla\omega)^Tn_r,
\]

so the same argument acquires the already typed axis-bending error `|grad n_r||omega|`. The constant-axis local lemma is therefore the clean baseline.

## 4. Natural-scale cost

At

\[
r\sim W^{-1/2},
\]

we have

\[
W^2|B|/r^2
\sim
W^2r
\sim
W^{3/2}.
\]

Thus if both orientations occupy fixed positive fractions,

\[
\boxed{
P_B
\gtrsim
b^2\theta_+\theta_-W^{3/2}.
}
\]

This is again the critical Navier--Stokes palinstrophy scaling.

## 5. Polarity dichotomy inside the projectively aligned branch

Suppose the covariance defect is small enough that most intense vorticity lies near the unoriented axis `[n]`.

Then two subbranches remain.

### A. Mixed polarity

Both

\[
\theta_+\gtrsim1,
\qquad
\theta_-\gtrsim1
\]

on the intense core.

Then the scalar axial component must transition between positive and negative values, producing the Poincare palinstrophy cost above.

### B. Oriented polarity

One orientation dominates, for example

\[
\theta_+\gg\theta_-.
\]

Then the core carries a substantial **signed axial vorticity flux** through cross-sections approximately normal to `n`.

Because

\[
\nabla\cdot\omega=0,
\]

such a flux cannot simply terminate inside the fluid. It must either

1. persist axially through neighboring regions; or
2. leak through transverse/off-axis vorticity.

This is the next geometric channel.

## 6. Why polarity must be typed separately from projective covariance

The matrices

\[
\xi\otimes\xi
\]

for `xi=n` and `xi=-n` are identical. Thus no projective covariance descriptor can distinguish the two orientation populations.

The polarity channel is therefore genuinely complementary rather than redundant:

- projective covariance records **axis participation**;
- polarity records **orientation along the selected axis**.

This fits the DSD axis-property discipline: an axis and its orientation/sign state are different typed properties.

## 7. Remaining oriented-flux target

The next target is a cylindrical divergence-free estimate.

For a cylinder aligned with the local covariance axis, define the signed axial flux

\[
\Phi(s)
=\int_{D_r}\omega\cdot n\,dA.
\]

Divergence-free gives

\[
\boxed{
\Phi(s_2)-\Phi(s_1)
=-\int_{s_1}^{s_2}
\int_{\partial D_r}
\omega_\perp\cdot\nu_\perp\,dS\,ds.
}
\]

Thus decay/termination of an oriented intense tube requires accumulated off-axis side flux.

The open problem is to convert that side-flux requirement into one of the already controlled volumetric channels:

- off-axis `L^2` projective defect;
- off-axis gradient/palinstrophy;
- transverse sparseness;
- or adjoint-window projective dissipation.

Status: **OPEN ORIENTED-FLUX / SIDE-LEAKAGE CLOSURE**.
