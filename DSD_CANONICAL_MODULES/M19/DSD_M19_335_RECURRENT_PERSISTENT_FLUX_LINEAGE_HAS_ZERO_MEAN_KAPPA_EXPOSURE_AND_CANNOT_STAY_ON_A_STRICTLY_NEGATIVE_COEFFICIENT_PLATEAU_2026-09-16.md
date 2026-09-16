# M19-335 — A recurrent persistent fixed-flux lineage has zero mean kappa exposure and cannot stay on a strictly negative coefficient plateau

**Date:** 2026-09-16  
**Status:** ACTIVE CALCULATION / EXACT PERSISTENT-LINEAGE COEFFICIENT CONSTRAINT / PARTIAL INCIDENCE SHARPENING / NOT GLOBAL CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from the persistent-lineage branch

M5-488 reduces the quiet compact finite-memory branch to a persistent scale-critical material-flux lineage, modulo recurrent costed exits.

M5-590--591 later identify a fixed productive persistent lineage on positive-density annular production windows.

On the nondegenerate retained lineage assume the scale-critical material vorticity flux stays within fixed bounds

\[
\boxed{
0<\Phi_-\le \Phi_F(\theta)\le\Phi_+<\infty.
}
\]

This is the fixed-flux persistent-lineage branch. If the lower bound fails, the branch returns to flux evacuation/thinning/replacement/interface exits already typed in M5/M17.

## 2. Exact CE-H material-flux law

M17-389 gives on exact CE-H

\[
\boxed{
\frac d{d\theta}\log\Phi_F
=
\bar\kappa_{\Phi,F}^{sim}(\theta),
}
\]

where \(\bar\kappa_{\Phi,F}\) is the flux-weighted coefficient mean over the retained material family.

In physical variables the same law is representation-safe:

\[
\frac d{dt}\log\Phi_F
=
\nu\bar\kappa_{\Phi,F}^{ph}.
\]

The strain contribution cancels exactly against material cross-sectional deformation.

## 3. Invariant mean on the marked dilation hull

Lift the persistent lineage to the M5-485/M5-486 invariant suspension of the marked dilation hull.

Because

\[
\log\Phi_-\le\log\Phi_F\le\log\Phi_+,
\]

\(\log\Phi_F\) is a bounded state observable on this nondegenerate branch.

Invariance of the suspension measure gives

\[
\left\langle
\frac d{d\theta}\log\Phi_F
\right\rangle=0.
\]

Therefore

\[
\boxed{
\left\langle
\bar\kappa_{\Phi,F}
\right\rangle=0.
}
\]

This is an exact recurrent-lineage constraint.

## 4. Strictly negative coefficient plateau is impossible

Suppose there were \(\kappa_*>0\) such that along the persistent flux family

\[
\bar\kappa_{\Phi,F}(\theta)
\le -\kappa_*
\]

for all sufficiently late similarity times on the recurrent component.

Then

\[
\frac d{d\theta}\log\Phi_F
\le -\kappa_*.
\]

Integrating gives exponential decay

\[
\Phi_F(\theta)
\le C e^{-\kappa_*\theta},
\]

contradicting the fixed positive lower flux bound and recurrence.

Hence

\[
\boxed{
\text{persistent fixed-flux recurrence}
\Longrightarrow
\text{no uniformly strictly negative flux-weighted kappa plateau}.
}
\]

## 5. Quantitative zero/positive exposure alternative

Let the compact coefficient bound be

\[
|\bar\kappa_{\Phi,F}|\le M_\kappa.
\]

Fix any \(0<\varepsilon<M_\kappa\). If the set

\[
A_+:=\{\bar\kappa_{\Phi,F}\ge-\varepsilon\}
\]

had invariant measure \(m_+\) too small, then

\[
\langle\bar\kappa_{\Phi,F}\rangle
\le
-(1-m_+)\varepsilon+m_+M_\kappa.
\]

Since the mean is zero,

\[
0\le -\varepsilon+m_+(M_\kappa+\varepsilon),
\]

so

\[
\boxed{
\mu(A_+)
\ge
\frac{\varepsilon}{M_\kappa+\varepsilon}>0.
}
\]

Thus every recurrent fixed-flux lineage spends a fixed positive fraction of similarity time in the coefficient collar

\[
\boxed{
\bar\kappa_{\Phi,F}\ge-\varepsilon.
}
\]

If the coefficient is known to stay away from zero in magnitude, this forces genuinely positive-coefficient episodes. Otherwise the lineage must visit the near-zero coefficient corridor with positive frequency.

## 6. Relation to the global enstrophy-weighted coefficient mean

For the whole CE-H state,

\[
\boxed{
\bar\kappa_E
:=
\frac{\int\kappa|\Omega|^2dx}{\int|\Omega|^2dx}
=-\frac{P}{E}<0
}
\]

for every nonzero state with positive palinstrophy.

The persistent productive lineage instead has recurrent flux-weighted mean coefficient zero:

\[
\langle\bar\kappa_{\Phi,F}\rangle=0.
\]

Therefore the productive lineage is coefficient-biased relative to the whole enstrophy population. Negative coefficient mass must be carried more strongly by complementary line populations.

Symbolically,

\[
\boxed{
\text{persistent productive flux family: mean kappa }0
\quad\text{vs}\quad
\text{whole packet: mean kappa }<0.
}
\]

This is a genuine coefficient-selection asymmetry.

## 7. Sharpening M19-334

M19-334 exhibited a compatible configuration in which the productive payer and companion remain on one constant \(\kappa_-\) plateau while a distinct transverse population carries \(\kappa_+\).

M19-335 rules out the simplest version with

\[
\kappa_-\le-\kappa_*<0
\]

persistently on the fixed-flux productive lineage.

The remaining possibilities are:

1. the productive lineage visits \(\kappa\approx0\) with positive frequency;
2. it experiences positive and negative coefficient phases whose flux-weighted mean cancels;
3. the fixed-flux lower bound fails, returning to flux-thinning/evacuation/replacement exits;
4. exact CE-H/lineage/representation coherence fails.

Thus the local incidence target is narrowed from arbitrary coefficient-label overlap to a **zero/sign-phase coupling problem on the productive lineage itself**.

## 8. Connection to M19-329 self-recycling

M19-329 shows negative-kappa coefficient variance creates intrinsic negative self-covariance capable of recycling log-kappa diffusion.

M19-335 adds that the productive recurrent fixed-flux lineage cannot remain uniformly in that negative-kappa regime. It must repeatedly approach zero or enter a positive coefficient phase.

Hence the productive lineage samples precisely the region where the sign-preserving log-kappa coordinate can lose uniform coercivity or switch sign.

This links the terminal marked-hull route back to the zero/interface architecture rather than to an everywhere-negative smooth self-recycling survivor.

## 9. Firewall

Zero **mean** coefficient exposure does not imply zero pointwise coefficient or zero total variation:

\[
\boxed{
\langle\bar\kappa_{\Phi,F}\rangle=0
\not\Rightarrow
\bar\kappa_{\Phi,F}\equiv0.
}
\]

The lineage may undergo recurrent sign-changing coefficient motion while its flux returns.

Therefore the flux observable itself is a bounded coboundary and not yet a strict Lyapunov function.

## 10. New immediate target

The persistent productive lineage now obeys simultaneously

\[
\boxed{
\langle\bar\kappa_{\Phi,F}\rangle=0,
}
\]

positive-density ratchet/production marks, and the whole-state spectral/coefficient variance of M19-333.

The next useful calculation is to ask whether recurrent approach to \(\kappa=0\) or sign switching on a fixed-flux productive lineage necessarily incurs one of the late-M17 zero-transition costs strongly enough to produce a non-coboundary/log-scale cost, or whether smooth sign-changing recurrence remains a viable compact survivor.

## 11. Conclusion

A recurrent scale-critical fixed-flux lineage cannot live forever on a strictly negative coefficient plateau. Its exact CE-H flux law forces zero invariant mean coefficient exposure and therefore positive-frequency near-zero/positive coefficient visits.

\[
\boxed{
\text{M19-335 COMPLETE; THE PRODUCTIVE-LINEAGE COEFFICIENT PROBLEM IS NOW A ZERO/SIGN-TRANSITION RECURRENCE PROBLEM.}
\]
