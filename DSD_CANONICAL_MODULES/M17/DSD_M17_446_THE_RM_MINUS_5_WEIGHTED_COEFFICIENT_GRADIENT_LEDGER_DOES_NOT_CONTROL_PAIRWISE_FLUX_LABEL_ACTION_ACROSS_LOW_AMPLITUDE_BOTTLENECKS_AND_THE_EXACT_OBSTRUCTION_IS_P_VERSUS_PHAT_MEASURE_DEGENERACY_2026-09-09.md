# DSD M17-446 — The `R_m^{-5}` weighted coefficient-gradient ledger does not control pairwise flux-label action across low-amplitude bottlenecks, and the exact obstruction is `p` versus `p-hat` measure degeneracy

Date: 2026-09-09  
Canonical ID: **M17-446**

Status: **ACTIVE MEASURE-MISMATCH NO-GO / LOW-AMPLITUDE BOTTLENECK FIREWALL / M17-443--445 COMPATIBILITY AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Problem

M17-443 reduces positive-flux label redistribution to pairwise cumulative coefficient-action contrast

\[
\nu\int(\kappa_\lambda-\kappa_\eta)dt.
\]

M17-445 supplies a genuine finite ancestral coefficient-gradient resource

\[
\sum_mR_m^{-5}
\iint\rho_m^2|\nabla\kappa_m|^2<\infty.
\]

It is tempting to use the new spatial gradient budget to control all pairwise coefficient contrasts.

That implication is false without an amplitude-connectivity or weighted-Poincare input.

The obstruction is exactly the low-amplitude survivor already identified by M17-440--441.

## 2. Two different probability measures

On one normalized transverse cross-section let

\[
q:=\widetilde\rho\ge0.
\]

The positive flux probability is

\[
\boxed{
dp=\frac{q\,dA}{\Phi},
\qquad
\Phi=\int q\,dA.
}
\]

The M17-440 quadratic-payer probability is

\[
\boxed{
d\widehat p
=\frac{q^2dA}{Q}
=\frac{q}{\mathfrak a_\Phi}dp,
}
\]

where

\[
Q=\int q^2dA,
\qquad
\mathfrak a_\Phi=Q/\Phi.
\]

Thus

\[
\boxed{
\frac{d\widehat p}{dp}
=\frac{q}{\mathfrak a_\Phi}.
}
\]

The coefficient-gradient currency is naturally concentrated according to `q^2 dA`, hence according to `p-hat`, while the replicator dynamics of M17-443 evolve the flux probability `p`.

## 3. Degeneracy in the amplitude-collapse survivor

M17-441 shows that on a retained positive-flux survivor,

\[
\mathfrak a_{\Phi,m}\to0
\]

and in fact

\[
\sum_m\mathfrak a_{\Phi,m}<\infty
\]

under uniform positive good-time density and flux.

M17-440 further shows that for every fixed `a>0`,

\[
p_m\{q\ge a\}\to0.
\]

Therefore the Radon--Nikodym density

\[
q/\mathfrak a_{\Phi,m}
\]

need not stay uniformly above or below positive constants on the flux-relevant set.

The two measures can become strongly singular relative to uniform comparison constants even though each is absolutely continuous with respect to the other at each strictly positive finite stage.

This is precisely where a `q^2`-weighted spatial energy can fail to control `p`-typical label contrasts.

## 4. Functional no-go model

The following model is only a functional counterexample to the desired inequality; it is **not** asserted to be a Navier--Stokes/CE-H solution.

Take a one-dimensional transverse path

\[
I=[-1,1].
\]

For `0<epsilon<<1`, choose smooth `q_epsilon` such that

\[
q_\varepsilon\equiv1
\]

near the endpoint regions

\[
[-1,-3/4]\cup[3/4,1],
\]

while

\[
q_\varepsilon\equiv\varepsilon
\]

on the central bridge

\[
[-1/2,1/2].
\]

Choose smooth `kappa_epsilon` with

\[
\kappa_\varepsilon=-1
\]

on the left endpoint region,

\[
\kappa_\varepsilon=+1
\]

on the right endpoint region, and all of its transition supported inside the low-amplitude central bridge, with

\[
|\kappa_\varepsilon'|\le C.
\]

Then the endpoint coefficient contrast is fixed:

\[
\boxed{
|\kappa_\varepsilon(1)-\kappa_\varepsilon(-1)|=2.
}
\]

But the weighted gradient charge satisfies

\[
\begin{aligned}
\int_Iq_\varepsilon^2
|\kappa_\varepsilon'|^2ds
&\le
C\varepsilon^2.
\end{aligned}
\]

Hence

\[
\boxed{
\int q_\varepsilon^2|\nabla\kappa_\varepsilon|^2
\to0
\quad\text{while pairwise coefficient contrast stays order one}.}
\]

Therefore no inequality of the schematic form

\[
|\kappa(\lambda)-\kappa(\eta)|^2
\le C
\int q^2|\nabla\kappa|^2
\]

can hold uniformly without additional amplitude/connectivity hypotheses.

## 5. Why positive flux does not repair the model

The endpoint regions in Section 4 can retain order-one positive flux mass because `q_epsilon=1` there.

The coefficient transition is hidden in a low-amplitude bridge carrying negligible `q^2` gradient cost.

Thus even the coexistence of

\[
\Phi\ge\Phi_*>0
\]

and substantial flux on both coefficient populations does not force the connecting coefficient-gradient charge to be large.

One must control the amplitude of the **connecting path or separating interface**, not merely the amplitude at the labels being compared.

## 6. Conditional bridge under an amplitude-connected corridor

Suppose instead that two represented coefficient populations can be joined through a regular transverse corridor `C` satisfying

\[
\boxed{q\ge q_*>0}
\]

throughout the corridor.

Then

\[
\int_C|\nabla\kappa|^2
\le
q_*^{-2}
\int_Cq^2|\nabla\kappa|^2.
\]

If in addition the corridor geometry provides a genuine one-dimensional path-family or a uniform Poincare/Morrey-type control converting the spatial `L2` gradient into the relevant coefficient contrast, then a fixed pairwise contrast forces a fixed M17-445 payment.

However in a two-dimensional cross-section ordinary `W^{1,2}` alone does not uniformly control pointwise oscillation. Therefore an amplitude floor by itself is still not enough; one also needs one of:

1. a controlled path family of positive transverse thickness;
2. a weighted Poincare/spectral-gap inequality for the relevant measure;
3. stronger derivative control giving a Morrey estimate;
4. a regular separating level-set geometry to which coarea can be applied.

These conditions must be proved, not assumed silently.

## 7. Natural weighted Poincare formulation

A canonical conditional statement would be a spectral-gap inequality for the flux probability `p` or payer probability `p-hat`.

For example, if

\[
\boxed{
\operatorname{Var}_{\widehat p}(\kappa)
\le C_P
\int|\nabla\kappa|^2d\widehat p
}
\]

with a uniform `C_P`, then

\[
\operatorname{Var}_{\widehat p}(\kappa)
\lesssim
\frac{1}{Q}
\int q^2|\nabla\kappa|^2dA.
\]

This controls coefficient segregation under `p-hat`.

But M17-443 redistribution is governed by `p`, and passing from `p-hat` to `p` requires control of

\[
\frac{d\widehat p}{dp}
=\frac{q}{\mathfrak a_\Phi}.
\]

Exactly this density degenerates in the M17-441 amplitude-collapse survivor.

Thus a uniform weighted Poincare estimate on `p-hat` alone does not close the aggregate redistribution branch.

## 8. Cross-generation meaning

M17-445 gives a finite `R_m^{-5}` resource, but the no-go model shows that a descendant may realize large pairwise coefficient-action contrast while paying arbitrarily little of that resource if the transition is pushed through sufficiently low-amplitude regions.

Therefore the statement

\[
\boxed{
\text{large coefficient label reweighting}
\Rightarrow
\text{fixed order-one M17-445 packet}
}
\]

is false under the present hypotheses.

The quintic ledger remains genuine; the missing theorem is a **coercive amplitude-connected spatialization of coefficient action**.

## 9. Updated narrow split

The M17-443 cumulative coefficient-action branch now becomes

\[
\boxed{
\begin{aligned}
G_{cumulative\ coefficient\ action\ contrast}
\Longrightarrow{}&
G_{amplitude\text{-}connected\ coefficient\ transition}\\
&\lor G_{low\text{-}amplitude\ separating\ bottleneck}\\
&\lor G_{weighted\ Poincare/spectral\ gap\ loss}\\
&\lor G_{cross\text{-}sectional\ chart/topology\ loss}\\
&\lor G_{high\text{-}jet/scale/genealogy\ loss}.
\end{aligned}
}
\]

The second branch is naturally compatible with the M17-441 flux-weighted amplitude-collapse survivor and must be treated together with it.

## 10. DSD audit role

DSD is used only to identify the mismatch between the measure that evolves (`p`) and the measure that pays the gradient resource (`p-hat`). The no-go is elementary weighted Sobolev analysis.

## 11. Audit verdict

**PASS as a no-go and exact firewall.**

The new M17-445 coefficient-gradient ledger is real but cannot control M17-443 pairwise flux-label action across low-amplitude bottlenecks. A new amplitude-connected Poincare/coarea/level-set theorem, or stronger regularity/geometric rigidity, is required.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
