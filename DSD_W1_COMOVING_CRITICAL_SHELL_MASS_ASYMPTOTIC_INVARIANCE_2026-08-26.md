# DSD W1 Co-Moving Critical Shell Mass Asymptotic Invariance — 2026-08-26

Status: **ASYMPTOTIC CRITICAL-SHELL TRANSPORT LAW DERIVED / PERIODIC INVARIANT-FLUX CONSEQUENCE DERIVED / APERIODIC MEASURE EXTENSION PARTIAL / GLOBAL REGULARITY UNPROVED.**

## 1. Scope

Work on the W1 corridor, where dyadic annular Campanato and derivative-frequency bounds give a uniform H1 bound after scale-normalizing each remote shell to a fixed annulus.

Let

\[
\Phi_hU
\]

denote the Leray flow by self-similar time h.

The purpose is to quantify the statement that the critical L3 shell mass is transported outward by the linear dilation with only a vanishing nonlinear/viscous correction at large normalized radius.

## 2. Co-moving blow-down

Fix R>1 and define

\[
\lambda(s)=Re^{s/2},
\qquad
W_R(z,s)=\lambda(s)U(\lambda(s)z,s).
\]

A direct chain-rule calculation using the projected Leray equation gives

\[
\boxed{
\partial_sW_R
=
\lambda(s)^{-2}
\left[
\nu\Delta_zW_R
-\mathbb P\nabla_z\cdot(W_R\otimes W_R)
\right].
}
\]

Thus

\[
\boxed{
\partial_sW_R
=
R^{-2}e^{-s}\mathcal N(W_R).
}
\]

The entire linear dilation operator has disappeared.

## 3. Uniform H^{-1} time variation

On one fixed enlarged annulus A* the W1 shell bounds imply

\[
\|W_R(s)\|_{H^1(A^*)}\le C_*
\]

uniformly in large R and over each fixed finite time interval.

The viscous term satisfies

\[
\|\Delta W_R\|_{H^{-1}(A^*)}
\lesssim
\|\nabla W_R\|_2,
\]

and the quadratic term satisfies

\[
\|\mathbb P\nabla\cdot(W_R\otimes W_R)\|_{H^{-1}}
\lesssim
\|W_R\otimes W_R\|_2
\lesssim
\|W_R\|_4^2
\lesssim C_*^2.
\]

Hence for fixed h>0,

\[
\boxed{
\|W_R(h)-W_R(0)\|_{H^{-1}(A^*)}
\le C_hR^{-2}.
}
\]

## 4. Upgrade to L3

The H1 norm of the difference is bounded by 2C*. Interpolation between H^{-1} and H^1 gives

\[
\boxed{
\|W_R(h)-W_R(0)\|_2
\le C_hR^{-1}.
}
\]

Sobolev gives a uniform L6 bound, and L2--L6 interpolation yields

\[
\boxed{
\|W_R(h)-W_R(0)\|_3
\le C_hR^{-1/2}.
}
\]

## 5. Critical shell-mass transport law

Let

\[
A=\{1<|z|<2\}
\]

and define

\[
\Psi_R(U)
:=
\int_{R<|Y|<2R}|U(Y)|^3dY
=
\int_A|R U(Rz)|^3dz.
\]

At time h, the co-moving shell radius is e^{h/2}R. Therefore

\[
\Psi_{e^{h/2}R}(\Phi_hU)
=
\int_A|W_R(z,h)|^3dz.
\]

Using the uniform L3 ceiling and the preceding L3 difference estimate,

\[
\boxed{
\left|
\Psi_{e^{h/2}R}(\Phi_hU)-\Psi_R(U)
\right|
\le C_hR^{-1/2}.
}
\]

Thus critical shell mass is asymptotically conserved along the outward dilation characteristic.

## 6. Invariant-measure consequence

Let mu be an invariant probability measure supported on a compact recurrent W1 invariant set and define

\[
M_\mu(R)
:=
\int\Psi_R(U)d\mu(U).
\]

Invariance of mu and the shell transport law give

\[
\boxed{
|M_\mu(e^{h/2}R)-M_\mu(R)|
\le C_hR^{-1/2}.
}
\]

Taking h=2log2,

\[
|M_\mu(2R)-M_\mu(R)|
\le CR^{-1/2}.
\]

Along dyadic radii R_k=2^kR_0 the errors are summable. Therefore

\[
\boxed{
M_\mu(R_k)\to M_{\mu,\infty}
}
\]

for one finite asymptotic critical-shell density M_{mu,infinity}.

Moreover, for every fixed multiplicative factor a>0, the same argument implies

\[
M_\mu(aR)-M_\mu(R)\to0
\]

along the far-tail limit. Thus the invariant mean shell density is asymptotically scale-independent.

## 7. Periodic W1 branch

For an exact period-S W1 orbit, take mu to be normalized time measure over one period.

The Barker--Prange positive-density shell recovery gives, for large N,

\[
\frac1N\sum_{k=0}^{N-1}
\frac1S\int_0^S\Psi_{R_k}(U(s))ds
\ge a_*>0
\]

on the singular Type-I weak-L3 branch.

But the summands converge to M_{mu,infinity}. Their Cesaro average therefore has the same limit. Hence

\[
\boxed{
M_{\mu,\infty}\ge a_*>0.
}
\]

Thus any surviving long-period DSS orbit has a nonzero, scale-independent asymptotic mean cubic mass per logarithmic shell.

This is the rigorous invariant-flux form of the persistent critical-memory picture.

## 8. Aperiodic recurrent branch

For aperiodic minimal recurrence, empirical invariant measures exist by compactness. The asymptotic transport law and existence of M_{mu,infinity} hold for every such invariant measure.

To conclude M_{mu,infinity}>0 from Barker--Prange in complete generality, one still needs a uniform passage from the growing-radius pointwise-in-time lower bound to the chosen invariant empirical measure. This is expected from long-time averaging but is not written here as a completed theorem.

Therefore:

- asymptotic shell-mass invariance for invariant measures: PROVED;
- positivity for periodic W1: PROVED conditional on Barker--Prange input;
- positivity for arbitrary aperiodic invariant measures: OPEN/partial.

## 9. Interpretation

The W1 tail is not merely a collection of old shells. It carries an asymptotically conserved critical flux density in logarithmic radius.

This quantity is exactly invisible to p>3 norms and exactly critical at p=3.

The result does not provide a contradiction: a nonzero constant critical flux is compatible with finite enstrophy and the 1/r tail. It instead identifies the correct center-mode quantity that must be quotiented before any recurrent-core Lyapunov argument can work.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
