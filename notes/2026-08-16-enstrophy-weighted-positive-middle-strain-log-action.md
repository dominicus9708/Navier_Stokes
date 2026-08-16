# Logarithmic enstrophy-weighted positive-middle-strain action per coherent episode

Date: 2026-08-16

Status: **EXACT GLOBAL ENSTROPHY/BETCHOV CONSEQUENCE. EVERY CLEAN-PRECURSOR TO COHERENT-CROSSING EPISODE PAYS A LOGARITHMIC PRODUCTIVE MIDDLE-STRAIN ACTION, INDEPENDENTLY OF WHETHER DERIVATIVE OR SPATIAL CONCENTRATION OCCURS. THIS IS A NECESSARY CRITICAL COST, NOT YET A NONREPEATABILITY CONTRADICTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Enstrophy logarithmic identity

Let

\[
E(s)=\|\Omega(s)\|_2^2,
\qquad
P(s)=\|\nabla\Omega(s)\|_2^2,
\]

and

\[
Q(s)=\int_{\mathbb R^3}\Omega\cdot S\Omega\,dx.
\]

The exact enstrophy identity is

\[
\frac12E'+\nu P=Q.
\]

On an interval with `E>0`, divide by `E`:

\[
\boxed{
\frac12\frac{d}{ds}\log E
+\nu\frac{P}{E}
=\frac{Q}{E}.
}
\]

Integrating from the clean minimum-enstrophy precursor `s_m` to the coherent crossing `s_c`,

\[
\boxed{
\int_{s_m}^{s_c}\frac{Q(s)}{E(s)}ds
=
\frac12\log\frac{E_c}{E_m}
+\nu\int_{s_m}^{s_c}\frac{P}{E}ds
\ge
\frac12\log\frac{E_c}{E_m}.
}
\]

Thus viscosity only increases the productive stretching action required for a prescribed enstrophy amplification.

## 2. Route Q to positive middle strain

For a smooth decaying incompressible whole-space velocity field, the global Betchov identity gives

\[
\boxed{
Q=-4\int\det S\,dx.
}
\]

Let

\[
\lambda_1\ge\lambda_2\ge\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0
\]

be the strain eigenvalues.

Where `lambda_2<=0`,

\[
\det S\ge0,
\]

so the contribution to `-4 det S` is nonpositive.

Where `lambda_2>0`,

\[
-4\det S
=4\lambda_1\lambda_2|\lambda_3|.
\]

Using

\[
\lambda_1|\lambda_3|
\le
\frac12(\lambda_1^2+\lambda_3^2)
\le
\frac12|S|^2,
\]

we obtain

\[
\boxed{
Q
\le
2\int\lambda_2^+|S|^2dx.
}
\]

Therefore

\[
\boxed{
\int_{s_m}^{s_c}
\frac{
\int\lambda_2^+|S|^2dx
}{E(s)}ds
\ge
\frac14\log\frac{E_c}{E_m}.
}
\]

This is a dimensionless productive-strain action.

## 3. Insert the clean precursor and coherent-core bounds

The clean deep checkpoint/minimum gives

\[
E_m
\lesssim
\frac{R^\beta}{\sqrt W},
\qquad
0<\beta<4.
\]

The coherent crossing core gives

\[
E_c\gtrsim R^3.
\]

Hence

\[
\frac{E_c}{E_m}
\gtrsim
\sqrt W\,R^{3-\beta}.
\]

The Gaussian-tail coherent-core kinetic-energy barrier gives

\[
\sqrt W
\gtrsim
R^5(\log R)^{5/2}.
\]

Consequently

\[
\boxed{
\frac{E_c}{E_m}
\gtrsim
R^{8-\beta}(\log R)^{5/2}.
}
\]

Therefore

\[
\boxed{
\int_{s_m}^{s_c}
\frac{
\int\lambda_2^+|S|^2dx
}{E(s)}ds
\ge
\frac{8-\beta}{4}\log R
+\frac58\log\log R
-O(1).
}
\]

For every fixed `beta<4`, the right-hand side diverges at least logarithmically.

## 4. Interpretation

This lower bound is independent of how the episode is decomposed into:

- residual seeding;
- fast-rotation resonance;
- spatial non-tightness;
- thin V2/palinstrophy pulses;
- material deformation;
- pressure-Hessian routing.

Those mechanisms can change **where** the required enstrophy production occurs, but cannot replace the positive-middle-strain production needed to raise global enstrophy from `E_m` to `E_c`.

Thus every coherent episode carries an unavoidable productive action

\[
\boxed{
\mathfrak A_{\lambda_2}
:=
\int
\frac{\int\lambda_2^+|S|^2}{E}ds
\gtrsim
c_\beta\log R.
}
\]

## 5. Relation to derivative concentration

A high-derivative pulse does not itself create enstrophy; diffusion enters the enstrophy identity with the opposite sign.

Therefore derivative concentration can only:

1. accompany the nonlinear productive strain;
2. localize it in space/time;
3. alter transport/projective geometry;
4. increase the viscous term and hence increase the stretching action required by the logarithmic identity.

This merges the conceptual roles of the final derivative and strain branches: derivative concentration is a localization/modulation mechanism around an unavoidable productive-strain budget.

## 6. Limitation

The action `A_lambda2` is scale critical and is not controlled by the finite kinetic-energy dissipation budget. A hypothetical singularity may have

\[
\mathfrak A_{\lambda_2}\to\infty.
\]

Hence the logarithmic lower bound is not yet a contradiction.

The missing theorem is a **cross-scale nonrepeatability/packing result** showing that the particular coherent, spatially organized positive-middle-strain action required at every renormalized crossing cannot be repeated indefinitely while all other established ledgers remain compatible.

Status: **EVERY CLEAN-TO-COHERENT EPISODE PAYS LOGARITHMIC ENSTROPHY-WEIGHTED POSITIVE-MIDDLE-STRAIN ACTION / DERIVATIVE PULSES CANNOT REPLACE THIS PRODUCTION / CRITICAL NONREPEATABILITY STILL OPEN / GLOBAL REGULARITY NOT PROVED.**