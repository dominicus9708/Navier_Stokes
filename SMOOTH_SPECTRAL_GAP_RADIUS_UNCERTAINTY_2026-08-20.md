# Smooth Spectral-Gap / Derivative-Radius Uncertainty — 2026-08-20

Status: **S-LEVEL WHOLE-SPACE IDENTITY AND UNCERTAINTY BOUND. GLOBAL REGULARITY NOT PROVED.**

This note quantifies the favorable viscous term in the finite-stage tightrope ledger:

\[
\mathcal G
=\frac HP-\frac PE\ge0.
\]

It shows that making this gap small requires spatial spreading of the derivative mass. Thus the plateau/hyperdissipation side of the smooth mainline is coupled directly to `H_remote`.

## 1. Spectral-variance identity

Let

\[
E=\|\Sigma\|_2^2,
\qquad
P=\|\nabla\Sigma\|_2^2,
\qquad
H=\|\Delta\Sigma\|_2^2,
\]

and define

\[
\boxed{
\lambda=\frac PE>0.
}
\]

Set

\[
L=-\Delta.
\]

Then

\[
\|(L-\lambda)\Sigma\|_2^2
=H-2\lambda P+\lambda^2E.
\]

Since `lambda=P/E`,

\[
\|(L-\lambda)\Sigma\|_2^2
=H-\frac{P^2}{E}.
\]

Therefore

\[
\boxed{
\mathcal G
:=
\frac HP-\frac PE
=
\frac{\|(L-\lambda)\Sigma\|_2^2}{P}.
}
\]

In Fourier language, if `mu` is the probability measure proportional to `|Sigma_hat(k)|^2 dk` and `X=|k|^2`, then

\[
\lambda=\mathbb E_\mu X
\]

and

\[
\boxed{
\mathcal G
=
\frac{\operatorname{Var}_\mu(X)}{\mathbb E_\mu X}.
}
\]

Thus the cross-order viscous term is exactly normalized radial-frequency variance.

## 2. Dilation commutator

Fix any spatial center `X0` and define the skew-adjoint dilation generator

\[
D_{X_0}
=(x-X_0)\cdot\nabla+\frac32.
\]

On smooth rapidly decaying tensor fields,

\[
\boxed{
[L,D_{X_0}]=2L.
}
\]

Taking the L2 pairing with `Sigma`,

\[
2P
=
\langle[L,D_{X_0}]\Sigma,\Sigma\rangle.
\]

Using self-adjointness of `L` and skew-adjointness of `D_X0`,

\[
P
=
\operatorname{Re}
\langle L\Sigma,D_{X_0}\Sigma\rangle.
\]

Because

\[
\operatorname{Re}
\langle\lambda\Sigma,D_{X_0}\Sigma\rangle=0,
\]

we obtain the exact identity

\[
\boxed{
P
=
\operatorname{Re}
\langle(L-\lambda)\Sigma,
D_{X_0}\Sigma\rangle.
}
\]

Hence

\[
P
\le
\|(L-\lambda)\Sigma\|_2
\|D_{X_0}\Sigma\|_2.
\]

## 3. Derivative rms radius

Define

\[
\boxed{
R_D^2(X_0)
=
\frac1P
\int_{\mathbb R^3}
|x-X_0|^2|\nabla\Sigma|^2dx.
}
\]

Then

\[
\|(x-X_0)\cdot\nabla\Sigma\|_2
\le
R_D\sqrt P.
\]

Also

\[
\|\Sigma\|_2
=\sqrt E
=\frac{\sqrt P}{\sqrt\lambda}.
\]

Therefore

\[
\|D_{X_0}\Sigma\|_2
\le
\sqrt P
\left(
R_D+
\frac{3}{2\sqrt\lambda}
\right).
\]

Combining with the commutator inequality and

\[
\|(L-\lambda)\Sigma\|_2
=\sqrt{P\mathcal G},
\]

gives

\[
\boxed{
\mathcal G
\ge
\left(
R_D+rac{3}{2\sqrt\lambda}
\right)^{-2}.
}
\]

This is a direct spatial-frequency uncertainty principle for the exact viscous gap appearing in the smooth tightrope ledger.

## 4. Optimized center

Define

\[
R_D^*
=
\inf_{X_0\in\mathbb R^3}R_D(X_0).
\]

Then

\[
\boxed{
\mathcal G
\ge
\left(
R_D^*+rac{3}{2\sqrt\lambda}
\right)^{-2}.
}
\]

Hence a derivative-tight state with

\[
R_D^*\le R_*,
\qquad
\lambda\ge\lambda_->0
\]

has the explicit positive hyperdissipative gap

\[
\boxed{
\mathcal G
\ge
G_*
:=
\left(
R_*+rac{3}{2\sqrt{\lambda_-}}
\right)^{-2}
>0.
}
\]

## 5. Converse: small viscous gap forces derivative spreading

If

\[
\mathcal G\le\varepsilon,
\]

then

\[
R_D^*
+\frac{3}{2\sqrt\lambda}
\ge
\varepsilon^{-1/2}.
\]

Thus

\[
\boxed{
R_D^*
\ge
\varepsilon^{-1/2}
-
\frac{3}{2\sqrt\lambda}.
}
\]

For fixed positive normalized frequency `lambda`, driving the viscous cross-order gap to zero forces the derivative rms radius to infinity.

This is exactly the `H_remote` geometry.

## 6. Insert into the smooth tightrope ledger

The exact finite-stage equation is

\[
\frac12(\log\chi)_s
+\frac12b
+\nu\mathcal G
=
\mathcal X,
\qquad
\chi=\frac PE=\lambda,
\]

where

\[
\mathcal X=\frac NP-\frac AE.
\]

On a derivative-tight lane,

\[
\mathcal G\ge G_*>0,
\]

so every unit of normalized time pays at least

\[
\nu G_*
\]

in additional cross-order production requirement.

Thus a long plateau/slow-growth interval is not free: either

- `mathcal X` continues to pay the positive gap;
- normalized frequency changes substantially;
- or derivative radius grows and the state enters `H_remote`.

## 7. Rigor scope

For smooth rapidly decaying initial data, all quantities above are finite on every finite smooth time slice. The uniform-in-stage use of the bound requires exactly the branch condition that `R_D^*` and `lambda` remain quantitatively controlled.

If the derivative rms radius is not uniformly controlled, that failure is not hidden inside a compact limit; it is explicitly the remote-derivative branch.

Status: **THE FAVORABLE VISCOUS CROSS-ORDER GAP IS EXACTLY RADIAL FREQUENCY VARIANCE AND HAS A LOWER BOUND IN TERMS OF THE DERIVATIVE RMS RADIUS. SMALL HYPERDISSIPATIVE GAP FORCES `H_remote`; DERIVATIVE TIGHTNESS FORCES A POSITIVE PER-TIME VISCOUS TAX.**