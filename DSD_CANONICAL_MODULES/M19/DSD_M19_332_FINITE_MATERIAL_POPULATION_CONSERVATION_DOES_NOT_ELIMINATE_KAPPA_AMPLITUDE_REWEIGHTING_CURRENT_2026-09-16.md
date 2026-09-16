# M19-332 — Finite material-population conservation does not eliminate the kappa-amplitude reweighting current

**Date:** 2026-09-16  
**Status:** ACTIVE NO-GO / POPULATION-CURRENT AUDIT / RECURRENT CYCLE SURVIVOR / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Question

M19-331 identifies

\[
\operatorname{Cov}_\pi(\sigma+\kappa,\log|\kappa|)
\]

as relative-amplitude reweighting among coefficient-labeled material populations.

A natural possible shortcut is to ask whether a finite persistent material-population architecture forbids such indefinite reweighting.

It does not.

## 2. Input from M18-089

For a compatible finite material partition

\[
\Omega_{loc}=\bigcup_{i=1}^NP_i,
\]

M18-089 realizes localized diffusive population defects as antisymmetric edge currents

\[
\boxed{
e_{ij}^{(p)}=-e_{ji}^{(p)}.
}
\]

Therefore internal exchange cancels globally:

\[
\boxed{
\sum_iB_{p,i}=0
}
\]

on a closed network.

But the mean graph current is determined only up to the cycle space

\[
\ker B_G,
\]

and instantaneous reversible sign-changing currents may persist even when their mean vanishes.

Thus finite-population conservation gives redistribution, not rigidity.

## 3. Kappa labels are not material labels

Exact CE-H gives spatial line constancy

\[
D_\xi\kappa=0,
\]

but it does **not** give material conservation

\[
D_t\kappa=0.
\]

Instead M17-394 gives

\[
D_t\log|\kappa|
=
L_\rho\log|\kappa|
+|\nabla\log|\kappa||^2
+\frac{L_\rho\sigma+\mathcal R_{geom}}{\kappa}.
\]

Therefore a partition by instantaneous coefficient bins

\[
\{\kappa\in I_1\},\dots,\{\kappa\in I_N\}
\]

is generally not a material partition. Material lines can move between coefficient bins through genuine coefficient evolution.

Thus one must not infer conservation of the mass of a fixed coefficient bin.

## 4. Fixed material labels still allow relative amplitude reweighting

Even if populations are defined by fixed material ancestry rather than instantaneous \(\kappa\), their enstrophy weights evolve as

\[
D_t\rho^2=2(\sigma+\kappa)\rho^2.
\]

Hence two fixed material populations can exchange **relative probability weight** without any material-label transfer at all:

\[
\boxed{
\frac d{dt}\log\frac{w_i}{w_j}
=2(g_i-g_j),
\qquad g=\sigma+\kappa.
}
\]

This is precisely the reweighting mechanism measured by M19-331.

Material population conservation therefore does not freeze enstrophy-weight probabilities.

## 5. Graph exchange does not remove the current

If spatial diffusion/interface exchange between material populations is included, M18-089 gives an additional conservative antisymmetric graph current.

This produces more, not less, room for recurrent redistribution:

\[
\boxed{
\text{relative amplitude growth}
+
\text{antisymmetric interface exchange}
+
\text{cycle-space circulation}.
}
\]

Internal graph exchange cannot create a global source, but neither can it eliminate a coefficient-biased recurrent current.

## 6. Closed-network mean balance

On a recurrent closed finite network,

\[
B_G\langle j_p\rangle=-s_p,
\]

where \(s_p\) is the vector of internal source/sink surpluses.

The homogeneous freedom

\[
\langle j_p\rangle
=j_{part}+j_C,
\qquad
j_C\in\ker B_G
\]

remains invisible to population moment balance.

Thus even exact finite-network bookkeeping does not force a one-way scalar potential.

## 7. Canonical NO-GO

The implication

\[
\boxed{
\text{finite persistent material populations}
\Longrightarrow
\text{no coefficient-amplitude reweighting current}
}
\]

is false.

The population framework only gives exact conservation/redistribution laws. It does not prohibit recurrent cycle currents or differential amplitude selection.

## 8. What would be stronger enough

To eliminate the M19-331 current one would need an additional theorem such as

1. one-dimensional slaving of relative growth \(g-\bar g\) to the coefficient coordinate with zero circulation;
2. a strict Lyapunov/entropy contraction for the coefficient-labeled probability distribution;
3. a finite signed action budget that recurrent reweighting would exhaust;
4. rigidity forcing all retained line populations to have the same relative growth;
5. or an explicit interface/geometry/export failure.

None is currently certified.

## 9. Conclusion

Finite material-population conservation is compatible with the joint coefficient-amplitude recurrent factor. M18-089 supplies exact internal cancellation but also explicitly retains cycle-space and reversible exchange freedom.

\[
\boxed{
\text{M19-332 COMPLETE; FINITE-POPULATION CONSERVATION IS NOT THE MISSING RIGIDITY THEOREM.}
}
\]
