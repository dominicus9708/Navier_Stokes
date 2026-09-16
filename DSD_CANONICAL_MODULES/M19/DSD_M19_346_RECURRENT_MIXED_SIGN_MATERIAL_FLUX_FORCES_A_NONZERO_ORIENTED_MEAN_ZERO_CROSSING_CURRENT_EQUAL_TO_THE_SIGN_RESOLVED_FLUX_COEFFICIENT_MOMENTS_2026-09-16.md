# DSD M19-346 — Recurrent mixed-sign material flux forces a nonzero oriented mean zero-crossing current equal to the sign-resolved flux coefficient moments

Date: 2026-09-16  
Canonical ID: **M19-346**

Status: **ACTIVE ORIENTED SIGN CURRENT / INVARIANT-MEAN FLUX BALANCE / ZERO-CROSSING THROUGH-FLOW**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-339

M19-339 gives the exact sign-resolved material-flux equations

\[
\dot\Phi_+
=
\nu\int_{\{\kappa>0\}}\kappa\,d\Phi
+
C_0^\Phi,
\]

\[
\dot\Phi_-
=
\nu\int_{\{\kappa<0\}}\kappa\,d\Phi
-
C_0^\Phi,
\]

where

\[
\boxed{
C_0^\Phi
:=\int\delta(\kappa)D_t\kappa\,d\Phi.
}
\]

The sign convention is such that positive \(C_0^\Phi\) transfers positive material-flux weight from the negative sector into the positive sector.

## 2. Positive sign-resolved flux coefficient moments

Define

\[
\boxed{
A_+^\Phi
:=
\int_{\{\kappa>0\}}\kappa\,d\Phi
\ge0,
}
\]

and

\[
\boxed{
A_-^\Phi
:=
\int_{\{\kappa<0\}}(-\kappa)\,d\Phi
\ge0.
}
\]

Then the sign-flux equations become

\[
\boxed{
\dot\Phi_+
=
\nu A_+^\Phi+C_0^\Phi,
}
\]

\[
\boxed{
\dot\Phi_-
=
-
u A_-^\Phi-C_0^\Phi.
}
\]

## 3. Recurrent invariant mean

Assume the represented mixed-sign material-flux dynamics belongs to a compact recurrent / invariant-measure component on which \(\Phi_+\) and \(\Phi_-\) are bounded integrable state observables.

Then invariance gives

\[
\boxed{
\langle\dot\Phi_+\rangle=0,
\qquad
\langle\dot\Phi_-\rangle=0.
}
\]

Averaging the exact equations yields

\[
0
=
\nu\langle A_+^\Phi\rangle
+
\langle C_0^\Phi\rangle,
\]

and

\[
0
=
-
u\langle A_-^\Phi\rangle
-
\langle C_0^\Phi\rangle.
\]

Therefore

\[
\boxed{
\langle C_0^\Phi\rangle
=
-\nu\langle A_+^\Phi\rangle
=
-\nu\langle A_-^\Phi\rangle.
}
\]

In particular

\[
\boxed{
\langle A_+^\Phi\rangle
=
\langle A_-^\Phi\rangle.
}
\]

This is the flux-measure analogue of sign balance, but it is distinct from the enstrophy-weighted M17-458 balance.

## 4. Nontrivial mixed-sign recurrence forces oriented crossing

If both sign coefficient-flux moments are nontrivial in invariant mean,

\[
\langle A_+^\Phi\rangle
=
\langle A_-^\Phi\rangle
\ge a_*>0,
\]

then

\[
\boxed{
\langle C_0^\Phi\rangle
\le
-\nu a_*<0.
}
\]

Thus the recurrent mixed-sign state requires a **strictly oriented mean zero-crossing current from the positive coefficient sector into the negative coefficient sector** under the stated sign convention.

This is stronger than merely asserting nonzero total variation of sign exchange.

## 5. Why the oriented current is dynamically consistent

The negative mean crossing current is not an immediate contradiction.

The recurrent balance is a through-flow:

\[
\boxed{
\begin{aligned}
&\kappa>0:\quad \text{coefficient diffusion increases material flux weight},\\
&\qquad\downarrow\ C_0^\Phi<0,\\
&\kappa<0:\quad \text{received flux weight is diffusively attenuated}.
\end{aligned}
}
\]

The positive-sector growth and negative-sector decay exactly compensate the oriented label transfer in invariant mean.

Hence the sign partition can be statistically stationary while carrying nonzero internal current.

## 6. Distinction from reversible graph exchange

M18-089 and M19-332 show that antisymmetric finite-population exchange may have zero mean or a cycle-space component invisible to total balance.

M19-346 is different. Once both sign coefficient-flux moments are nonzero, the mean current is fixed by the exact PDE balance:

\[
\boxed{
\langle C_0^\Phi\rangle
=-\nu\langle A_+^\Phi\rangle.
}
\]

It therefore cannot be set to zero by choosing a different finite-population representation while retaining the same mixed-sign flux moments.

The remaining issue is not existence or orientation of the current. It is its **cost**.

## 7. Relation to M19-335

Adding the two sign-flux equations gives

\[
\dot\Phi
=
\nu\int\kappa\,d\Phi.
\]

Invariant averaging yields M19-335's

\[
\langle\bar\kappa_{\Phi}\rangle=0.
\]

M19-346 is the sign-resolved refinement of that identity. The zero total coefficient exposure is realized by equal positive and negative flux-coefficient moments together with a nonzero oriented crossing current.

## 8. Relation to M19-340

M19-340 identifies

\[
C_{0,A}^\Phi
=-\int_{Z_A}\rho v_0d\ell.
\]

Therefore a nonzero negative invariant mean requires nontrivial time-averaged oriented zero-level sweep.

On a regular zero corridor with amplitude, gradient, and speed floors/ceilings, this can be compared to the positive zero-current \(J_0\). On the diffuse parent-length baseline, however, \(\rho\) may be of order \(R^{-1}\), so a fixed material-flux current can be maintained only by sufficient zero-interface extent, crossing speed, concentration, or failure of the regular compact geometry.

This is the next quantitative bridge.

## 9. Flux-thinning version

If one sign flux fraction thins, its flux coefficient moment may also thin. M19-345 shows that enstrophy-weighted sign cancellation can then survive only through sign-specific line-residence segregation on the compact coefficient branch.

Thus there are two main recurrent mixed-sign regimes:

1. **nontrivial sign flux moments:** fixed oriented mean crossing current;
2. **vanishing sign flux moment:** line-residence segregation / sparse-flux compensation must carry the enstrophy-weighted sign moment.

These regimes should not be conflated.

## 10. Updated spatial target

The spatial mixed-sign branch is now organized by a current-versus-residence dichotomy:

\[
\boxed{
\begin{aligned}
H_{\rm recurrent\ mixed\text{-}sign}
\Longrightarrow{}&
H_{\rm oriented\ zero\text{-}crossing\ current}^{\langle C_0^\Phi\rangle\ne0}\\
&\lor G_{\rm sign\ flux\text{-}moment\ thinning+residence\ segregation}\\
&\lor G_{\rm coefficient/representation/genealogy\ loss}.
\end{aligned}
}
\]

The first branch asks for a quantitative cost of persistent oriented low-amplitude zero-level sweep. The second asks whether sparse high-residence sign populations are compatible with the material genealogy and derivative ledgers.

## 11. Audit verdict

**PASS — recurrent mixed-sign material flux has a forced oriented mean zero-crossing current whenever both sign flux-coefficient moments remain nontrivial.**

This is a genuine signed invariant current, but not yet a contradiction because it participates in a consistent positive-growth / crossing / negative-decay through-flow. The next theorem must price that through-flow or force it into the sparse-residence branch.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
