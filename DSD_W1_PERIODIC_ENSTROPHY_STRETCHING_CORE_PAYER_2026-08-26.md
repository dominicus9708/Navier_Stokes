# DSD W1 Periodic Enstrophy / Stretching Core Payer

Date: 2026-08-26

Status: **GLOBAL PERIODIC ENSTROPHY IDENTITY DERIVED / CRITICAL 1-R TAIL SHOWN SUMMABLE FOR ENSTROPHY, PALINSTROPHY, AND STRETCHING / POSITIVE MEAN VORTEX-STRETCHING PAYER LOCALIZED TO A FINITE RECURRENT CORE / NO NONCIRCULAR STRETCHING-BUDGET CLOSURE DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

After the Barker--Prange audit correction, uniform weak-L3 is no longer a terminal contradiction.

The periodic W1 survivor must therefore be attacked through a genuinely dynamical quantity.

A useful distinction is that the canonical critical velocity tail

\[
U\sim r^{-1}
\]

is not globally L2, but its vorticity

\[
\Omega=\nabla\times U\sim r^{-2}
\]

is globally L2 at infinity.

Thus the periodic omega-limit admits a global enstrophy ledger even though it does not admit a global velocity-energy ledger.

## 2. Leray vorticity equation

For

\[
U_s+\frac12U+\frac12Y\cdot\nabla U
+(U\cdot\nabla)U+\nabla P
=\nu\Delta U,
\qquad
\nabla\cdot U=0,
\]

the vorticity satisfies

\[
\boxed{
\Omega_s
+\Omega
+\frac12Y\cdot\nabla\Omega
+(U\cdot\nabla)\Omega
=(\Omega\cdot\nabla)U
+\nu\Delta\Omega.
}
\]

Define

\[
Z(s):=\|\Omega(s)\|_2^2,
\qquad
P_\Omega(s):=\|\nabla\Omega(s)\|_2^2,
\]

and the signed vortex-stretching production

\[
\mathcal S(s)
:=
\int_{\mathbb R^3}
\Omega^T S\Omega\,dY,
\qquad
S:=\frac12(\nabla U+\nabla U^T).
\]

Since the antisymmetric part of grad U gives zero in the quadratic form,

\[
\int \Omega\cdot((\Omega\cdot\nabla)U)
=\mathcal S.
\]

## 3. Exact global enstrophy identity

Multiply the vorticity equation by Omega and integrate over R3.

The transport term vanishes:

\[
\int \Omega\cdot(U\cdot\nabla\Omega)=0.
\]

The similarity drift gives

\[
\frac12
\int \Omega\cdot(Y\cdot\nabla\Omega)
=
-\frac34Z.
\]

Combining with the explicit +Omega term gives the positive Leray enstrophy damping

\[
Z-\frac34Z=\frac14Z.
\]

Therefore

\[
\boxed{
\frac12 Z'(s)
+\frac14Z(s)
+\nu P_\Omega(s)
=\mathcal S(s).
}
\]

This is the exact normalized analogue of the physical whole-space enstrophy formation identity.

## 4. Legality on the periodic W1 omega-limit

The periodic W1 state need not be in velocity L2, because it is an Lp, p>3, omega-limit and may carry a nonzero 1/r critical tail.

However the W1 critical shell bounds give

\[
\int_{A_R}|\Omega|^2\lesssim R^{-1}.
\]

Summing dyadically,

\[
\sum_{k\ge0}(2^kR_0)^{-1}<\infty.
\]

The core is smooth. Hence

\[
\boxed{
\Omega(s)\in L^2(\mathbb R^3)
}
\]

for every periodic phase.

On the derivative-controlled W1 branch the old-shell derivative envelope likewise gives

\[
\int_{A_R}|\nabla\Omega|^2\lesssim R^{-3},
\]

so

\[
\boxed{
\nabla\Omega(s)\in L^2(\mathbb R^3).
}
\]

Thus the global enstrophy identity is legitimate on the periodic orbit.

## 5. Periodic averaging

Let the periodic orbit have least period S>0.

Then

\[
Z(s+S)=Z(s).
\]

Integrating one period,

\[
\int_0^S Z'(s)ds=0.
\]

Hence

\[
\boxed{
\left\langle\mathcal S\right\rangle_S
=
\frac14\left\langle Z\right\rangle_S
+\nu\left\langle P_\Omega\right\rangle_S.
}
\]

In particular, every nonzero periodic W1 vorticity orbit has

\[
\boxed{
\left\langle\mathcal S\right\rangle_S>0.
}
\]

If the inherited analytic occupied core gives a phase-uniform or period-averaged enstrophy floor

\[
\langle Z\rangle_S\ge z_*>0,
\]

then

\[
\boxed{
\langle\mathcal S\rangle_S
\ge z_*/4.
}
\]

## 6. The critical remote tail is summable in the enstrophy ledger

For the canonical periodic tail,

\[
T\sim r^{-1},
\qquad
\Omega_T\sim r^{-2},
\qquad
\nabla\Omega_T\sim r^{-3},
\qquad
S_T\sim r^{-2}.
\]

On a fixed-shape shell A_R of volume scale R3,

\[
\boxed{
Z_T(A_R)
\sim R^{-4}R^3
\sim R^{-1}.
}
\]

Similarly,

\[
\boxed{
P_{\Omega,T}(A_R)
\sim R^{-6}R^3
\sim R^{-3}.
}
\]

and the absolute vortex-stretching contribution has critical scaling

\[
\boxed{
\int_{A_R}
|\Omega_T|^2|S_T|\,dY
\sim
R^{-4}R^{-2}R^3
\sim R^{-3}.
}
\]

Therefore

\[
\boxed{
\begin{aligned}
Z_T(|Y|>R)&=O(R^{-1}),\\
P_{\Omega,T}(|Y|>R)&=O(R^{-3}),\\
\int_{|Y|>R}|\Omega_T|^2|S_T|&=O(R^{-3}).
\end{aligned}
}
\]

The same powers hold for the periodic W1 tail under the already established old-shell derivative bounds and canonical-tail convergence, up to fixed constants.

This is an important contrast with cubic velocity occupancy:

\[
\int_{A_R}|U|^3\sim O(1),
\]

which is neutral in log radius.

Enstrophy and stretching do not count infinitely remote critical cells equally; they strongly discount them.

## 7. Finite-core stretching payer

Because

\[
\langle\mathcal S\rangle_S
\ge z_*/4>0
\]

and the absolute tail stretching outside R tends to zero like R^-3, choose one finite R_S large enough that

\[
\left\langle
\int_{|Y|>R_S}
|\Omega|^2|S|\,dY
\right\rangle_S
\le z_*/8.
\]

Then

\[
\begin{aligned}
\left\langle
\int_{|Y|<R_S}
\Omega^TS\Omega\,dY
\right\rangle_S
&=
\langle\mathcal S\rangle_S
-
\left\langle
\int_{|Y|>R_S}
\Omega^TS\Omega\,dY
\right\rangle_S\\
&\ge
z_*/4-z_*/8.
\end{aligned}
\]

Hence

\[
\boxed{
\left\langle
\int_{B_{R_S}}
\Omega^TS\Omega\,dY
\right\rangle_S
\ge
z_*/8>0.
}
\]

Thus the periodic survivor must pay a fixed positive signed vortex-stretching charge in one finite recurrent core.

The remote 1/r memory cannot itself pay the required mean stretching at infinity.

## 8. Relation to the earlier Stretching Budget-Closure Gate

The earlier first-hitting note

`DSD_GLOBAL_ENSTROPHY_FORMATION_STRETCHING_GATE_2026-08-25.md`

proved that the actual pre-singular bounded-Z trajectory must accumulate divergent total physical stretching over a sequence of shrinking first-hitting blocks.

The present periodic calculation is the omega-limit analogue:

\[
\boxed{
\text{periodic W1}
\Longrightarrow
\text{fixed positive stretching charge per Leray period in a finite core}.
}
\]

Under the inverse physical scaling, repeating this positive normalized period charge over infinitely many Leray periods reproduces the required singular stretching accumulation.

Thus the two ledgers are consistent rather than contradictory.

## 9. Why this still does not close the periodic branch

The kinetic-energy budget does not control

\[
\int\Omega^TS\Omega.
\]

The enstrophy identity itself permits stretching and palinstrophy to balance indefinitely:

\[
\mathcal S
=
\frac14Z+
u P_\Omega
\]

in period average.

Moreover positive stretching does not automatically imply projective rotation.

At a point where vorticity is aligned with a positive strain eigenvector,

\[
\Omega^TS\Omega
=
\lambda_+|\Omega|^2>0
\]

can persist while the direction of Omega is instantaneously fixed.

Therefore the implication

\[
\boxed{
\text{positive recurrent stretching}
\Longrightarrow
\text{positive projective action}
}
\]

is not available without a new theorem.

Likewise replacing stretching by a generic cubic derivative estimate only returns to the previously audited derivative ladder and is circular as a final closure.

## 10. Sharpened periodic SBCG

The periodic branch is now reduced to the following finite-core question.

Can a smooth compact recurrent Leray core sustain

\[
\boxed{
\left\langle
\int_{B_{R_S}}
\Omega^TS\Omega
\right\rangle_S
\ge c_S>0
}
\]

for every period while simultaneously preserving all W1 quietness, bounded-Z, derivative-frequency, projective, and turnover constraints?

A valid closure must prove a one-sided inequality of the form

\[
\boxed{
\text{positive recurrent finite-core stretching}
\Longrightarrow
H\lor T\lor\text{projective action}\lor\text{another finite budget loss},
}
\]

with a quantitatively nonzero threshold.

No such implication is established by the current repository.

## 11. Audit verdict

### PROVED

- periodic W1 vorticity and palinstrophy are globally integrable under the existing tail bounds;
- the exact Leray enstrophy identity has a positive +Z/4 damping term;
- period averaging forces strictly positive signed vortex-stretching production;
- the remote critical memory contributes only a summable O(R^-3) stretching tail;
- a fixed positive mean stretching payer is therefore localized to a finite recurrent core.

### NOT PROVED

- a finite a-priori budget for repeated vortex stretching;
- a coercive relation from positive stretching to projective/turnover action;
- exclusion of the periodic W1 orbit;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]