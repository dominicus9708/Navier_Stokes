# DSD M5-31 — Nonsmooth Threshold Surface Entropy

Date: 2026-08-27

Status: **DERIVED NONDEGENERATE ACTIVE-SET DISSIPATION / SMOOTH-COLLAR GAP REMOVED / REMAINING SOURCE COMPRESSES TO A CODIMENSION-ONE AMPLITUDE-BOUNDARY PRESSURE-HODGE FLUX / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation from M5-30

Every `C^1` hard-threshold radial entropy has

\[
\Phi'(1)=0,
\]

so its direction dissipation coefficient `a Phi'(a)` degenerates as `a downarrow 1`.

To remove that specific structural gap, allow a convex entropy with a jump in the first derivative at the threshold.

The canonical choice is

\[
\boxed{
\Phi_*(a)=\frac12(a^2-1)_+.
}
\]

For `a>1`, this is ordinary kinetic energy minus the threshold constant; for `a<1` it vanishes.

## 2. Exact entropy multiplier

The velocity-space gradient is

\[
\boxed{
W_*
=\nabla_V\Phi_*(V)
=V\,\mathbf 1_{\{a>1\}}.
}
\]

The multiplier is parallel to `V`, so the pointwise Lamb orthogonality is retained:

\[
(\Omega\times V)\cdot W_*=0.
\]

Thus any nonlinear work after Hodge projection is again a threshold-Hodge commutator effect.

## 3. Viscous Hessian and nondegenerate direction control

Approximate `Phi_*` by smooth convex functions and pass to the limit. In distributional radial-Hessian form,

\[
\Phi_*'(a)=a\,\mathbf1_{a>1},
\]

\[
\Phi_*''(a)=\mathbf1_{a>1}+\delta_{a=1}.
\]

Hence the viscous entropy production is

\[
\boxed{
\mathcal D_*
=
\int_{a>1}|\nabla V|^2\,dz
+
\mu_{\Sigma},
}
\]

where the nonnegative threshold measure is, for a regular level,

\[
\boxed{
\mu_{\Sigma}
=
\int_{\{a=1\}}|\nabla a|\,dS.
}
\]

Equivalently,

\[
\int_{a>1}|\nabla V|^2
=
\int_{a>1}
\left(
|\nabla a|^2+a^2|\nabla n|^2
\right)dz.
\]

Therefore the direction coefficient no longer vanishes at the threshold.

This removes the smooth-collar degeneracy of M5-30.

## 4. Divergence of the threshold multiplier

Since `div V=0`,

\[
\operatorname{div}
\left(V\mathbf1_{a>1}\right)
=
\delta(a-1)\,V\cdot\nabla a.
\]

For a regular level `Sigma={a=1}` with amplitude normal

\[
n_a=\frac{\nabla a}{|\nabla a|},
\]

coarea gives

\[
\boxed{
\langle \Pi,\operatorname{div}W_*\rangle
=
\int_{\Sigma}\Pi\,V\cdot n_a\,dS.
}
\]

Thus the bulk pressure source has collapsed to a codimension-one amplitude-state boundary flux.

## 5. Exact nonsmooth threshold ledger

For the normalized Navier--Stokes equation

\[
V_\sigma+(V\cdot\nabla)V+\nabla\Pi=\nu\Delta V,
\qquad \operatorname{div}V=0,
\]

testing by `W_*` through smooth convex approximation yields

\[
\boxed{
\frac{d}{d\sigma}
\int\frac12(a^2-1)_+\,dz
+
\nu\mathcal D_*
=
\int_{\Sigma}\Pi\,V\cdot n_a\,dS.
}
\]

The transport term cancels exactly by incompressibility.

## 6. Gauge independence and crossing balance

Because the superlevel set has divergence-free flux balance,

\[
\boxed{
\int_{\Sigma}V\cdot n_a\,dS=0.
}
\]

Hence the pressure boundary work is gauge independent.

Define

\[
Q_+
=
\int_{V\cdot n_a>0}V\cdot n_a\,dS,
\]

\[
Q_-
=
-\int_{V\cdot n_a<0}V\cdot n_a\,dS.
\]

Then

\[
Q_+=Q_-=:Q_\Sigma,
\]

and

\[
\boxed{
\int_{\Sigma}\Pi V\cdot n_a\,dS
=
Q_\Sigma
\left(
\overline\Pi_{out}-\overline\Pi_{in}
\right)
}
\]

up to the orientation convention for the amplitude normal.

Thus the only source is a pressure difference between the two crossing sectors of the amplitude boundary.

## 7. Hodge-commutator form

Let

\[
h(a)=\mathbf1_{a>1}.
\]

Since `W_*=hV` and `P V=V`,

\[
[\mathbb P,h]V
=\mathbb P W_*-W_*
=-\mathbb QW_*.
\]

Pointwise Lamb orthogonality gives

\[
\boxed{
T_*
:=-\langle\Omega\times V,[\mathbb P,h]V\rangle
=
\int_{\Sigma}\Pi V\cdot n_a\,dS.
}
\]

Therefore removal of the smooth collar does not remove the M5 source. It compresses it to a **singular threshold-Hodge commutator supported by the amplitude interface**.

## 8. What was gained and what remains

Gained:

1. full active-set gradient control
   \[
   \int_{a>1}|\nabla V|^2;
   \]
2. positive threshold measure
   \[
   \mu_\Sigma\ge0;
   \]
3. no bulk direction-coercivity degeneracy;
4. exact identification of the remaining source with a pressure difference across one amplitude state boundary.

Remaining:

\[
\boxed{
\text{Can the boundary pressure work}
\quad
\int_\Sigma \Pi V\cdot n_a
\quad
\text{be absorbed by}
\quad
\nu\mathcal D_*?
}
\]

A universal answer is not obtained here.

The next audit must analyze the threshold-surface flux itself rather than the already-removed smooth collar.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
