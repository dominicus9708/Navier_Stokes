# DSD W1 Distribution-Slope Formation Band

Date: 2026-08-26

Status: **THE PRESSURE-MINUS-VISCOUS AMPLITUDE GAIN IS REWRITTEN PURELY IN TERMS OF THE VELOCITY DISTRIBUTION FUNCTION / POSITIVE GAIN REQUIRES A FINITE-AMPLITUDE DISTRIBUTION SLOPE STEEPER THAN THE WEAK-L3 EXPONENT THREE / THE FAR DEFECT TAIL IS THE NEUTRAL SLOPE-THREE OUTPUT / GLOBAL REGULARITY UNPROVED.**

## 1. Distribution variables

Let

\[
N(\lambda)=|\{|U|>\lambda\}|,
\qquad
C(\lambda)=\lambda^3N(\lambda).
\]

The threshold energy is

\[
\mathcal E_\lambda
=
\int_\lambda^\infty \mu N(\mu)d\mu,
\]

and define

\[
K(\lambda)=\lambda\mathcal E_\lambda.
\]

Equivalently,

\[
\boxed{
K(\lambda)
=
\lambda\int_\lambda^\infty
\frac{C(\mu)}{\mu^2}d\mu.
}
\]

Thus `K` is a forward Hardy average of the instantaneous weak-L3 coefficient `C`.

## 2. Exact derivative identity

Since

\[
\partial_\lambda\mathcal E_\lambda
=-\lambda N(\lambda),
\]

one gets

\[
\boxed{
\lambda K'(\lambda)
=K(\lambda)-C(\lambda).
}
\]

The invariant threshold balance gives

\[
J_P(\lambda)-\nu D_\lambda
=-\frac12K'(\lambda).
\]

Therefore

\[
\boxed{
J_P(\lambda)-\nu D_\lambda
=
\frac{C(\lambda)-K(\lambda)}{2\lambda}.
}
\]

Positive net gain occurs exactly when the instantaneous coefficient exceeds its Hardy average:

\[
\boxed{C(\lambda)>K(\lambda).}
\]

## 3. Local power-law interpretation

Suppose on one amplitude band

\[
N(\lambda)\approx c\lambda^{-\alpha},
\qquad \alpha>2.
\]

Then

\[
C(\lambda)=c\lambda^{3-\alpha},
\]

and

\[
K(\lambda)
\approx
\frac{1}{\alpha-2}C(\lambda)
\]

away from the upper cutoff.

Hence

\[
\boxed{
J_P-\nu D_\lambda>0
\iff
\alpha>3.
}
\]

At the critical weak-L3 slope

\[
\alpha=3,
\]

one has

\[
K=C
\]

to leading order and the local amplitude gain is neutral.

## 4. DSD formation interpretation

The positive W1 defect therefore requires a change of distribution regime:

\[
\boxed{
\text{finite-amplitude band with effective slope }\alpha>3
\longrightarrow
\text{amplitude-state transport}
\longrightarrow
\text{low-amplitude boundary with slope }\alpha=3.
}
\]

The finite core is a **formation band** where supercritical distribution steepness supplies positive net gain. The far weak-L3 tail is the neutral storage/output state.

## 5. Geometric level-set form

For regular levels,

\[
-N'(\lambda)
=
\int_{\{|U|=\lambda\}}
\frac{dS}{|\nabla|U||}.
\]

The effective logarithmic distribution slope is

\[
\boxed{
\alpha_{eff}(\lambda)
:=-\frac{\lambda N'(\lambda)}{N(\lambda)}.
}
\]

Thus a positive-gain power-law-like band requires

\[
\boxed{
\lambda
\int_{\{|U|=\lambda\}}
\frac{dS}{|\nabla|U||}
>3N(\lambda)
}
\]

in the corresponding differential sense.

This connects the amplitude-state gain to the geometry of velocity-magnitude level sets.

## 6. Closure target

A new route to W1 closure would be any theorem forbidding a recurrent finite-parent band with the required supercritical distribution slope and positive pressure-minus-viscous gain while maintaining the W1 critical boundary output.

No such large-data level-set theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
