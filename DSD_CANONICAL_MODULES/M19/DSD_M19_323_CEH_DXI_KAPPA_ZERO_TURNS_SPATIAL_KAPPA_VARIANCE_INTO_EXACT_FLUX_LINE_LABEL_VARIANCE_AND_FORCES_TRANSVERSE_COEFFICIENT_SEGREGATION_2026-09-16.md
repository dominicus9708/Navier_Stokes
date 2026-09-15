# M19-323 — CE-H D_xi kappa = 0 turns spatial kappa variance into exact flux-line label variance and forces transverse coefficient segregation

**Date:** 2026-09-16  
**Status:** CONDITIONAL EXACT CE-H GEOMETRY / FLUX-LINE DISINTEGRATION / TRANSVERSE COEFFICIENT SEGREGATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-322

On the exact CE-H compact lane, M19-322 proves the spacetime enstrophy-weighted coefficient variance floor

\[
\operatorname{Var}_\Omega(\kappa)\ge c_\kappa>0.
\]

The law of total variance splits this into

\[
\mathbb E_\nu
\left[
\operatorname{Var}_{\pi_s}(\kappa)
\right]
+
\operatorname{Var}_\nu(\bar\kappa(s))
\ge c_\kappa.
\]

The present module identifies the geometry of the first term.

## 2. CE-H line constraint

Exact CE-H gives

\[
\Delta\Omega=\kappa\Omega,
\qquad
\nabla\cdot\Omega=0.
\]

Taking divergence yields

\[
\Omega\cdot\nabla\kappa=0.
\]

Writing

\[
\Omega=\rho\xi,
\]

we obtain on the active set

\[
\boxed{D_\xi\kappa=0.}
\]

Thus kappa is constant along every connected instantaneous vortex-line segment in the active region.

## 3. Flux-line coordinates

At a fixed retained time, disintegrate the active region into oriented vortex-line/tube labels `lambda`.

Let

\[
d\nu(\lambda)=|d\Phi_\lambda|
\]

be the positive absolute vorticity-flux measure and let `s_line` denote arclength along the line `Gamma_lambda`.

The standard tube-coordinate identity is

\[
\boxed{
 dV
 =
 \frac{d\nu(\lambda)\,ds_{line}}{\rho}.
}
\]

Define the first generalized residence factor

\[
\boxed{
L_1(\lambda)
:=
\int_{\Gamma_\lambda}\rho\,ds_{line}.
}
\]

Then the snapshot enstrophy is

\[
\boxed{
E
:=
\int\rho^2dV
=
\int_\Lambda L_1(\lambda)d\nu(\lambda).
}
\]

This is the `p=2` case of the M18-068 generalized residence hierarchy.

## 4. Coefficient moments disintegrate exactly by line label

Because kappa is constant along each instantaneous vortex line, write that value as

\[
\kappa_\lambda.
\]

Then

\[
\begin{aligned}
\int\kappa\rho^2dV
&=
\int_\Lambda
\int_{\Gamma_\lambda}
\kappa_\lambda\rho\,ds_{line}
\,d\nu(\lambda)\\
&=
\boxed{
\int_\Lambda
\kappa_\lambda L_1(\lambda)d\nu(\lambda).
}
\end{aligned}
\]

Likewise

\[
\boxed{
\int\kappa^2\rho^2dV
=
\int_\Lambda
\kappa_\lambda^2L_1(\lambda)d\nu(\lambda).
}
\]

## 5. Exact line-label probability

Define the enstrophy-residence weighted line probability

\[
\boxed{
 d\Pi(\lambda)
 :=
 \frac{L_1(\lambda)}{E}
 d\nu(\lambda).
}
\]

Then the spatial enstrophy-weighted coefficient moments are exactly

\[
\boxed{
\mathbb E_{\pi_s}[\kappa]
=
\mathbb E_\Pi[\kappa_\lambda],
}
\]

and

\[
\boxed{
\mathbb E_{\pi_s}[\kappa^2]
=
\mathbb E_\Pi[\kappa_\lambda^2].
}
\]

Therefore

\[
\boxed{
\operatorname{Var}_{\pi_s}(\kappa)
=
\operatorname{Var}_\Pi(\kappa_\lambda).
}
\]

This is an exact identity, not an estimate.

## 6. Meaning of the spatial variance branch

Suppose the M19-322 spatial branch carries a positive amount of the total variance:

\[
\mathbb E_\nu
\left[
\operatorname{Var}_{\pi_s}(\kappa)
\right]
\ge c_s>0.
\]

Then, by Section 5,

\[
\boxed{
\mathbb E_\nu
\left[
\operatorname{Var}_{\Pi_s}(\kappa_\lambda)
\right]
\ge c_s>0.
}
\]

Thus the coefficient heterogeneity is necessarily a heterogeneity among different vortex-line labels.

It cannot be produced by longitudinal oscillation of kappa along one CE-H line.

## 7. Quantitative line-population separation

On a bounded-K compact branch assume

\[
|\kappa_\lambda|\le K_*.
\]

A positive variance lower bound implies a positive essential oscillation:

\[
\boxed{
\operatorname{ess\,osc}_\Pi\kappa_\lambda
\ge
2\sqrt{\operatorname{Var}_\Pi(\kappa_\lambda)}.
}
\]

Hence on a positive recurrent state subset there are two line-label populations carrying coefficient values separated by a fixed amount.

By a countable threshold extraction, one may choose component-dependent constants

\[
\kappa_-<\kappa_+,
\qquad
\delta_\kappa:=\kappa_+-\kappa_->0,
\]

such that both

\[
\Pi(\kappa_\lambda\le\kappa_-)>0
\]

and

\[
\Pi(\kappa_\lambda\ge\kappa_+)>0
\]

occur on a positive recurrent state set.

No universal probability fraction independent of the ergodic component is claimed without additional bounds.

## 8. Transverse nature of any connecting transition

Since kappa is constant along each line, a spatial path that remains on one line cannot connect the two coefficient populations.

Any controlled active-region transition must move transversely between line labels.

Therefore the spatial branch has the canonical routing

\[
\boxed{
\text{kappa line-label segregation}
\Longrightarrow
\text{transverse coefficient transition}
\lor
\text{line/component separation}
\lor
\text{zero/interface/domain loss}.
}
\]

On a bounded connected active component with controlled Poincare geometry and `rho >= a_0>0`, the first alternative yields a quantitative transverse-gradient payment

\[
\boxed{
\int |\nabla_\perp\kappa|^2
\ge c_{\perp\kappa}>0.
}
\]

The exact value depends on the extracted line-population masses, coefficient gap, and carrier geometry.

## 9. Relation to late M17 coefficient geometry

Late M17 already treats

- coefficient-gradient decompactification;
- sign-preserving coefficient residence;
- zero-corridor and rapid sign fragmentation;
- component/interface/genealogy loss;
- mesoscopic negative/positive kappa compensation.

M19-323 gives these branches an independent necessity source on the compact CE-H interior carrier: the coefficient cannot remain linewise and transversely uniform because spectral uncertainty forces a positive kappa variance.

Thus the compact CE-H branch necessarily activates coefficient geometry even before a sign-changing kappa argument is invoked.

## 10. Temporal branch remains separate

If the spatial line-label variance is small and M19-322 is instead paid by

\[
\operatorname{Var}_\nu(\bar\kappa(s))>0,
\]

then the coefficient changes primarily between recurrent phases.

This remains a temporal coefficient/frequency hysteresis route and is not converted into a transverse gradient by M19-323.

Do not mix the two branches.

## 11. Firewall

The line-label disintegration assumes the active CE-H foliation is valid on the charge-bearing region.

Nodal sets, topology changes, reconnection, or loss of a global tube labeling are not ignored; they are explicit exits.

Likewise a transverse coefficient-gradient payment remains an unsigned derivative-type event and is still subject to the M18-058--059 ancestry/budget firewall.

Therefore

\[
\boxed{
\text{transverse kappa segregation}
\not\Rightarrow
\text{global contradiction}.
}
\]

## 12. Next target

The compact spatial branch is now reduced to a transverse line-packing problem.

A high-value next calculation is to combine

\[
\operatorname{Var}_\Pi(\kappa_\lambda)>0
\]

with the positive-flux mesoscopic carrier geometry of late M17 and ask whether two coefficient-separated line populations can remain interleaved at own scale without forcing either

- order-one transverse coefficient gradient on a non-summable family;
- thin-neck / scale-free Poincare degeneration;
- sign-fragmentation or nodal/interface turnover;
- extra transverse size dilution.

This is more specific than the previous generic coefficient-gradient frontier.

---

\[
\boxed{\text{M19-323 COMPLETE; CE-H SPATIAL KAPPA VARIANCE IS EXACTLY TRANSVERSE VORTEX-LINE LABEL VARIANCE.}}
\]