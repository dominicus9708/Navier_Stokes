# First-chaos vorticity parity obstruction

Date: 2026-08-14

Status: **EXACT HERMITE-SELECTION STATEMENT FOR THE GENUINE RESIDUAL-RESIDUAL VORTICITY NONLINEARITY / APPLICATION REQUIRES THE AFFINE-LINEAR PROPAGATOR SPLIT**.

This note records a stronger saturation obstruction on the near-Poincare branch.

Once affine/mean linear feedback is moved into the homogeneous propagator, the genuine residual-residual vorticity nonlinearity cannot regenerate a pure first-Hermite residual vorticity state from itself.

## 1. Pure first-chaos residual-gradient state

Work in whitened Gaussian coordinates `z`.

If the residual gradient is purely first Hermite chaos, then the residual velocity has only second Hermite chaos because differentiation lowers Hermite degree by one and the residual velocity has no degrees zero or one.

Thus write schematically

\[
w=w_2,
\qquad
\eta=\delta\Omega=\eta_1,
\]

where the subscripts denote Hermite degree.

The genuine residual-residual vorticity source is

\[
N_\omega
=
\nabla_z\times(w\times\eta).
\]

## 2. Hermite product parity

The product of second and first Hermite chaos contains only odd degrees:

\[
2\times1
\longrightarrow
1\oplus3.
\]

A spatial derivative lowers Hermite degree by one. Therefore

\[
\nabla_z\times(w_2\times\eta_1)
\subset
0\oplus2.
\]

Consequently

\[
\boxed{
\Pi_1 N_\omega[w_2,\eta_1]=0.
}
\]

This is an exact algebraic selection rule.

## 3. Dynamical meaning

A pure first-chaos residual vorticity state can feed

- the Gaussian mean vorticity, through degree-zero output;
- second-chaos residual vorticity, through degree-two output.

But it cannot produce first-chaos residual vorticity through the genuine residual-residual quadratic interaction.

Thus

\[
\boxed{
\text{first-chaos residual vorticity}
\not\to
\text{first-chaos residual vorticity}
}
\]

at quadratic residual-residual order.

In this sense the pure first-chaos state is a donor to the mean/higher-chaos channels rather than a self-reproducing nonlinear state.

## 4. Relation to the stretching mean source

The same parity structure is compatible with the exact mean-vorticity stretching source.

If both residual strain and residual vorticity are first chaos,

\[
\delta S=\delta S_1,
\qquad
\eta=\eta_1,
\]

then their Gaussian product contains a degree-zero component:

\[
1\times1
\longrightarrow
0\oplus2.
\]

Hence

\[
J_{\rm str}
=\int\gamma\,\delta S_1\eta_1
\]

can be nonzero even though first-chaos residual self-regeneration is forbidden.

So the leading near-Poincare mechanism is naturally

\[
\boxed{
\text{first-chaos residual}
\to
\text{mean-vorticity source}
\ \text{and/or}\
\text{second chaos},
}
\]

not first-chaos self-replication.

## 5. Near-saturation consequence

Let

\[
\delta=\frac{K-B}{B}.
\]

When `delta -> 0`, the residual gradient approaches first chaos in `L2`.

After the affine-linear contribution is placed in the homogeneous propagator, an order-`m` first-chaos residual pulse cannot then be supplied by the leading core-core quadratic interaction. Its regeneration must use at least one of:

1. a non-negligible higher-Hermite tail;
2. affine/mean linear feedback not yet absorbed into the homogeneous propagator;
3. a frame/covariance degeneration;
4. a separately routed nonlocal error.

Therefore exact Poincare saturation is incompatible with genuine residual-residual first-chaos self-generation.

## 6. Quantitative target

The next quantitative version is to prove a bound of the schematic form

\[
\boxed{
\|\Pi_1 N_\omega\|_2
\lesssim
B\sqrt\delta
}
\]

for the residual-residual source.

If this holds, a localized first-chaos creation block with

\[
V_{Q_\omega,1}\gtrsim\Theta m
\]

would force

\[
R^2m\sqrt\delta
\gtrsim
\sqrt{\Theta m},
\]

hence

\[
\boxed{
R^2\sqrt m
\gtrsim
\sqrt{\Theta/\delta}.
}
\]

This would turn the exact parity obstruction into a quantitative near-saturation incompatibility.

Status: **PURE FIRST-CHAOS SELF-REGENERATION FORBIDDEN / NEXT TARGET = PROVE THE `B sqrt(delta)` QUANTITATIVE LOW-MODE BOUND.**
