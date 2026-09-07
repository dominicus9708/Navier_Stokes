# DSD M17-374 — Uniform M17-134 resonant carriers cannot belong to the same positive-flux population that secularly evacuates

Date: 2026-09-08  
Canonical ID: **M17-374**

Status: **ACTIVE SAME-POPULATION RESONANCE/EVACUATION SEPARATION THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope firewall

M17-134 is a **single-material-carrier** theorem. It does not state that an arbitrary flux-family average satisfies

\[
\langle\kappa\rangle=\frac32.
\]

Accordingly the present module does not replace a labelwise material law by an ensemble average.

Instead, let `S` be a measurable positively oriented subfamily of material flux labels such that **every label in `S`** satisfies the M17-134 endpoint compactness hypotheses on one common long inter-stage block

\[
I=[\theta_-,\theta_+],
\qquad
L:=|I|=2\log K.
\]

The family identity is assumed to be preserved through `I`. Label loss through nodal/cutoff/interface/rank/domain changes is recorded as a separate exit.

## 2. Uniform labelwise M17-134 lower bound

M17-134 gives for one carrier

\[
\frac1L\int_I\kappa_\lambda(\theta)d\theta
=
\frac32+O(L^{-1}),
\]

provided the endpoint ratios of director area, the two pure-kernel director jets, and similarity vorticity amplitude are uniformly bounded above and below.

If those endpoint compactness constants are uniform over `S`, there is one constant `C_R<\infty` independent of the label and of the block age such that

\[
\boxed{
\int_I\kappa_\lambda d\theta
\ge
\frac32L-C_R
\qquad\text{for every }\lambda\in S.
}
\]

## 3. Exact flux amplification of the resonant subfamily

Each infinitesimal material flux weight satisfies

\[
\frac d{d\theta}d\Phi_\lambda
=
\kappa_\lambda d\Phi_\lambda.
\]

Therefore

\[
d\Phi_\lambda(\theta_+)
=
\exp\left(\int_I\kappa_\lambda d\theta\right)
 d\Phi_\lambda(\theta_-).
\]

Using Section 2,

\[
\boxed{
d\Phi_\lambda(\theta_+)
\ge
e^{-C_R}e^{3L/2}
 d\Phi_\lambda(\theta_-).
}
\]

Integrating over `S`,

\[
\boxed{
\Phi_S(\theta_+)
\ge
e^{-C_R}e^{3L/2}\Phi_S(\theta_-).
}
\]

Since `L=2 log K`, this is

\[
\boxed{
\Phi_S(\theta_+)
\ge c_RK^3\Phi_S(\theta_-).
}
\]

This is exactly the M17-328 `K^3` similarity-flux resonance, now written safely for a positive-flux subfamily with uniform labelwise hypotheses.

## 4. Compare with M17-371 secular evacuation

Suppose the whole same-genealogy nodal family `F` reaches a strict coefficient scale `r` on the compact coefficient-mass/local-H2 branch. M17-371 gives

\[
\boxed{
\Phi_F(\theta_+)\le C_*r^{5/2}.
}
\]

Because `S subset F` and all fluxes are positively oriented,

\[
\Phi_S(\theta_+)\le\Phi_F(\theta_+)\le C_*r^{5/2}.
\]

Combining with Section 3,

\[
c_RK^3\Phi_S(\theta_-)
\le
C_*r^{5/2}.
\]

Hence

\[
\boxed{
\Phi_S(\theta_-)
\le
C\,K^{-3}r^{5/2}.
}
\]

Therefore an old long-resonant M17-134 subfamily that later belongs to an `r^{5/2}`-evacuated population must already carry vanishingly small incoming flux unless one of the M17-134 or genealogy hypotheses fails.

## 5. Fixed positive incoming resonant flux is incompatible with evacuation

If instead

\[
\boxed{
\Phi_S(\theta_-)\ge\phi_*>0,
}
\]

then

\[
\Phi_F(\theta_+)
\ge
c_R\phi_*K^3.
\]

For `K -> infinity` this is incompatible not only with

\[
\Phi_F(\theta_+)=O(r^{5/2}),
\]

but with any uniformly bounded total positive flux on the same retained family.

Thus

\[
\boxed{
H_{uniform\ M17\text{-}134\ resonance}
+H_{fixed\ incoming\ positive\ flux}
\not\subset
H_{same\text{-}population\ secular\ evacuation}.
}
\]

## 6. Exact exits

A same-family secularly evacuating population can therefore avoid the preceding incompatibility only through at least one of

\[
\boxed{
\begin{aligned}
&G_{resonant\ subfamily\ incoming\ flux\ thinning},\\
&G_{J_\xi\ endpoint\ degeneration},\\
&G_{director\text{-}jet\ endpoint\ degeneration/unboundedness},\\
&G_{similarity\ amplitude\ endpoint\ exposure},\\
&G_{material\ family/interface/rank/domain\ change}.
\end{aligned}
}
\]

These are precisely the endpoint failures already listed by M17-134, now reinterpreted as **necessary** if the same population is to realize M17-371 flux evacuation.

## 7. Relation to M17-372

M17-372 proved that evacuation from fixed positive flux requires

\[
\int\overline{\kappa_-}_{\Phi,F}d\theta
\gtrsim\frac52\log\frac1r.
\]

The present result is stronger on a uniformly resonant positive-flux subfamily: its labelwise integrated `kappa` is strongly positive, so it cannot itself supply the required negative evacuation exposure.

Therefore the required negative exposure must be carried by

1. a different subpopulation;
2. intervals on which the M17-134 endpoint compactness fails;
3. or a genealogy/interface transition.

This prevents the same positive-flux carrier from being silently used simultaneously as the long-resonant skeleton and the flux-evacuating nodal bubble.

## 8. DSD-theory role

The useful DSD heuristic is population identity: two asymptotic statements may not be combined or cancelled unless they refer to the same structural carrier. The mathematics here is only the exact labelwise flux ODE plus the M17-134 endpoint estimate.

## 9. Audit verdict

**PASS.**

The new structural separation is

\[
\boxed{
\text{fixed-positive-flux long resonant carrier}
\neq
\text{same-population secularly evacuated nodal carrier}
}
\]

unless an explicit endpoint/genealogy degeneration occurs.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]