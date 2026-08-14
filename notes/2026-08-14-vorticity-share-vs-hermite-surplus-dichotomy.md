# Vorticity share versus Hermite curvature-surplus dichotomy

Date: 2026-08-14

Status: **DERIVED STRUCTURAL DICHOTOMY; PRESSURE-FREE ON THE VORTICITY ROUTE / GLOBAL PACKING STILL OPEN**.

This note strengthens the local nonlinear-creation analysis by avoiding the pressure term and avoiding any blanket `L4` assumption on the full residual field.

The key comparison is between

\[
\Theta=\frac{V_\omega}{B}
\]

and the Hermite/Poincare curvature surplus

\[
\delta
:=
\frac{K-B}{B},
\qquad
K:=R^2D_g.
\]

Here `B` is the Gaussian residual-gradient variance and `K` is its whitened Hermite number energy.

## 1. Hermite meaning of delta

Let the mean-zero residual-gradient field have Hermite variance energies `e_n`, `n>=1`. Then

\[
B=\sum_{n\ge1}e_n,
\qquad
K=\sum_{n\ge1}n e_n.
\]

Therefore

\[
K-B
=
\sum_{n\ge2}(n-1)e_n.
\]

In particular,

\[
\sum_{n\ge2}e_n
\le K-B
=\delta B.
\]

Thus `delta` measures the total departure from first Hermite chaos, with additional weight on higher degrees.

## 2. Transfer to residual vorticity

Let

\[
\eta=\delta\Omega
\]

be the Gaussian mean-zero residual vorticity, with

\[
V_\omega
=\|\eta\|_{L^2(\gamma)}^2
=\Theta B.
\]

Because vorticity is a fixed linear projection of the residual gradient, its Hermite tail is bounded by the full-gradient tail. Hence

\[
V_{\omega,\ge2}
\lesssim
\delta B.
\]

Therefore, if

\[
\boxed{\delta\le c\Theta}
\]

with sufficiently small fixed `c`, then a fixed fraction of the vorticity variance lies in first chaos:

\[
\boxed{
V_{\omega,1}
\ge c_0\Theta B.
}
\]

Moreover its own Hermite number energy obeys

\[
K_\omega-V_\omega
\lesssim
\delta B,
\]

so under `delta <= c Theta`,

\[
\boxed{
K_\omega\lesssim V_\omega.
}
\]

Thus the residual vorticity is quantitatively near-Poincare relative to its own variance.

## 3. Previous-checkpoint vorticity inheritance is negligible

On the surviving branch

\[
m=W^{-1/3}\Lambda,
\qquad
H=\Lambda\Theta^{5/6}\to\infty.
\]

The previous total residual inheritance satisfies

\[
\frac{B_{\rm inh}}m
\lesssim
W^{-1/3-6\varepsilon}\Lambda^{-7/5}.
\]

Since

\[
\Theta
=H^{6/5}\Lambda^{-6/5},
\]

we get

\[
\frac{B_{\rm inh}}{\Theta m}
\lesssim
W^{-1/3-6\varepsilon}
\Lambda^{-1/5}
H^{-6/5}
\to0.
\]

Hence even when `Theta -> 0`, the inherited residual is negligible relative to the vorticity variance carried by a surviving source pulse.

Applying the matched heat-chain localization directly to vorticity therefore gives at least one parabolic block with

\[
\boxed{
V_{Q_\omega}\gtrsim \Theta m.
}
\]

## 4. Pressure-free residual-vorticity equation

In the co-affine frame, absorb all terms linear in the residual state into the homogeneous affine propagator.

The genuinely nonlinear residual-vorticity source is then schematically

\[
N_\omega
=
\nabla\times(r\times\eta),
\]

where

\[
r=R w(z),
\qquad
z=\frac{x-a}{R}.
\]

The Gaussian Poincare relation for the residual velocity gives

\[
\|w\|_2^2
\lesssim B,
\qquad
\|\nabla_z w\|_2^2
=B.
\]

For residual vorticity,

\[
\|\eta\|_2^2
=V_\omega,
\qquad
\|\nabla_z\eta\|_2^2
=K_\omega
\lesssim V_\omega
\]

on the `delta <= c Theta` branch.

Gaussian creation/annihilation estimates imply

\[
\|z w\|_2\lesssim \sqrt B,
\qquad
\|z\eta\|_2\lesssim \sqrt{V_\omega}.
\]

## 5. First-chaos source bound by Gaussian duality

Let `Pi_1` denote projection to first Hermite chaos.

Pair the curl source with a first-chaos Gaussian test function. Weighted integration by parts differentiates `h_1 gamma`; its derivative is a fixed polynomial of degree at most two times `gamma`.

Splitting the polynomial factors between `w` and `eta` and using Cauchy--Schwarz gives

\[
\boxed{
\|\Pi_1N_\omega\|_2
\lesssim
\sqrt B\sqrt{V_\omega}
=
B\sqrt\Theta.
}
\]

No pressure term occurs, and no global `L4` bound is needed.

Over one matched parabolic block of duration comparable to `R^2`, the first-chaos nonlinear Duhamel output therefore satisfies

\[
\boxed{
\|\Pi_1Q_\omega\|_2
\lesssim
R^2m\sqrt\Theta.
}
\]

## 6. Criticality on the near-Poincare vorticity branch

At the child pulse, first-chaos vorticity carries a fixed fraction of

\[
V_\omega=\Theta m.
\]

The inherited contribution is `o(Theta m)`, so the localized nonlinear block must create first-chaos amplitude

\[
\|\Pi_1Q_\omega\|_2
\gtrsim
\sqrt{\Theta m}.
\]

Combining with the pressure-free upper bound,

\[
\sqrt{\Theta m}
\lesssim
R^2m\sqrt\Theta.
\]

The vorticity share cancels:

\[
\boxed{
R^2\sqrt m\gtrsim1
}
\]

or

\[
\boxed{
mR^4\gtrsim1.}
\]

Thus even a very small but surviving vorticity share cannot evade the same critical local-velocity threshold, provided the full Hermite curvature surplus is smaller than that share.

## 7. The complementary branch

If the near-Poincare condition fails, then

\[
\boxed{
\delta\gtrsim\Theta.
}
\]

Using

\[
H=\Lambda\Theta^{5/6}\to\infty,
\]

we have

\[
\Theta
=H^{6/5}\Lambda^{-6/5}.
\]

Hence the curvature-surplus branch satisfies

\[
\boxed{
\delta\Lambda^{6/5}
\gtrsim
H^{6/5}
\to\infty.
}
\]

So the complementary escape is not merely `delta>0`: its curvature surplus is large relative to the minimum vorticity share compatible with survival.

This is precisely the branch in which the earlier Hermite gap-two drift estimate can remain efficient:

\[
|J_{\rm drift}|
\lesssim
B\sqrt\delta.
\]

When `delta << Theta`, drift is smaller than the natural typed source scale `B sqrt(Theta)` and stretching must dominate. When `delta >= c Theta`, drift/high-Hermite transfer remains a legitimate route and must be priced separately.

## 8. Revised local dichotomy

A surviving nonlinear creation block now falls into one of two sharply typed cases:

### A. Near-Poincare relative to vorticity share

\[
\delta\ll\Theta.
\]

Then

- residual vorticity is mostly first Hermite chaos;
- inherited vorticity is negligible;
- pressure-free nonlinear creation localizes to one block;
- drift is suppressed relative to the typed source scale;
- stretching/projective/Cauchy channels dominate;
- and

\[
\boxed{mR^4\gtrsim1.}
\]

### B. Hermite curvature-surplus branch

\[
\delta\gtrsim\Theta.
\]

Then

\[
\boxed{
\delta\Lambda^{6/5}\to\infty
}
\]

along the surviving sequence, and high-Hermite/gap-two/viscous structure must carry the escape.

Status: **PRESSURE-FREE NEAR-POINCARE VORTICITY CREATION REDUCED TO THE CRITICAL LOCAL-VELOCITY SCALE / REMAINING ESCAPE = QUANTITATIVELY RESCALED HERMITe CURVATURE SURPLUS.**
