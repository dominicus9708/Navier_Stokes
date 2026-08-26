# DSD W1 Distribution-Slope Formation Band

Date: 2026-08-26

Status: **THE INVARIANT-AVERAGED PRESSURE-MINUS-VISCOUS AMPLITUDE GAIN IS REWRITTEN IN TERMS OF THE INVARIANT-AVERAGED VELOCITY DISTRIBUTION FUNCTION / POSITIVE GAIN REQUIRES A FINITE-AMPLITUDE DISTRIBUTION PROFILE STEEPER THAN THE WEAK-L3 EXPONENT THREE IN THE POWER-LAW MODEL / INDIVIDUAL NONSTATIONARY STATES MUST RETAIN TIME DEPENDENCE / GLOBAL REGULARITY UNPROVED.**

## 1. Statewise distribution variables

For one state `U`, let

\[
N_U(\lambda)=|\{|U|>\lambda\}|,
\qquad
C_U(\lambda)=\lambda^3N_U(\lambda),
\]

\[
\mathcal E_{\lambda,U}
=
\int_\lambda^\infty \mu N_U(\mu)d\mu,
\qquad
K_U(\lambda)=\lambda\mathcal E_{\lambda,U}.
\]

For every fixed state, purely algebraically,

\[
\boxed{
\lambda\partial_\lambda K_U
=K_U-C_U.
}
\]

## 2. Invariant averages

Let `mu` be an invariant probability measure on the compact minimal W1 set and define

\[
\bar N(\lambda)=\langle N_U(\lambda)\rangle_\mu,
\qquad
\bar C(\lambda)=\lambda^3\bar N(\lambda),
\]

\[
\bar K(\lambda)=\langle K_U(\lambda)\rangle_\mu.
\]

Linearity gives

\[
\boxed{
\lambda\bar K'(\lambda)
=\bar K(\lambda)-\bar C(\lambda).
}
\]

The invariant threshold balance gives

\[
\boxed{
\left\langle J_P(\lambda)-\nu D_\lambda\right\rangle_\mu
=-\frac12\bar K'(\lambda)
=
\frac{\bar C(\lambda)-\bar K(\lambda)}{2\lambda}.
}
\]

Thus positive **mean** gain occurs exactly when

\[
\boxed{\bar C(\lambda)>\bar K(\lambda).}
\]

This statement is invariant-average, not a same-time identity for an arbitrary nonstationary state.

## 3. Hardy-average representation

The averaged threshold energy satisfies

\[
\boxed{
\bar K(\lambda)
=
\lambda\int_\lambda^\infty
\frac{\bar C(\mu)}{\mu^2}d\mu.
}
\]

Hence `bar K` is the forward Hardy average of the invariant-averaged weak-L3 coefficient `bar C`.

## 4. Power-law model

Suppose on one amplitude band the **averaged** distribution is approximately

\[
\bar N(\lambda)\approx c\lambda^{-\alpha},
\qquad \alpha>2.
\]

Then

\[
\bar C(\lambda)=c\lambda^{3-\alpha},
\]

and away from the upper cutoff

\[
\bar K(\lambda)
\approx
\frac{1}{\alpha-2}\bar C(\lambda).
\]

Therefore

\[
\boxed{
\left\langle J_P-\nu D_\lambda\right\rangle_\mu>0
\iff
\alpha>3
}
\]

within this local power-law model.

At the weak-L3 slope `alpha=3`,

\[
\bar K\approx\bar C
\]

and the local mean gain is neutral to leading order.

## 5. DSD interpretation

The invariant endpoint requires a change of amplitude-distribution regime:

\[
\boxed{
\text{finite-amplitude averaged formation band}
\longrightarrow
\text{time-amplitude characteristic transport}
\longrightarrow
\text{neutral slope-three boundary defect}.
}
\]

The finite-core distribution statement is an invariant statistical description. Minimality and continuity are then used separately to extract recurrent instantaneous pump events.

## 6. Statewise geometric identity

For each regular level of each state,

\[
-N_U'(\lambda)
=
\int_{\{|U|=\lambda\}}
\frac{dS}{|\nabla|U||}.
\]

Thus statewise level-set geometry remains available for any instantaneous recurrent witness selected from the positive invariant band.

## 7. Closure target

A W1 closure would follow from a theorem forbidding the invariant-averaged finite-parent distribution/gain profile required above, or equivalently forcing

\[
\int
\left\langle J_P-\nu D_\lambda\right\rangle_\mu d\lambda\le0.
\]

No such unconditional large-data theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
