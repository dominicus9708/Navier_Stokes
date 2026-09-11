# M18-067 — Moment-space hysteresis does not force a new diffusion payment because the circulation is strain-driven and diffusion opposes it

**Date:** 2026-09-11  
**Status:** ANTI-SHORTCUT / HYSTERESIS-TO-DIFFUSION NO-GO / STRAIN-DRIVEN LOOP CLASSIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-066 shows that the recurrent-phase covariance is an oriented circulation in moment space:

\[
C_{phase}^{pq}
=
\frac1{p\langle M_p\rangle}
\left\langle
M_q(\log M_p)'
\right\rangle.
\]

A tempting next step is to argue that a nonzero hysteresis loop must dissipate a fixed amount of the weighted diffusion resource \(D_p\) each cycle.

The exact amplitude-moment equation shows that this inference is false in general.

The loop is actively driven by aligned strain; diffusion enters with the opposite sign. Therefore positive circulation does not itself provide a lower bound on diffusion beyond the already known source/sink identities.

## 2. Exact statewise decomposition

M18-060 gives

\[
\frac1pM_p'
=A_p-D_p-c_pM_p,
\]

where

\[
A_p=\int\sigma\rho^pdy,
\qquad
D_p\ge0,
\qquad
c_p=1-\frac{3}{2p}.
\]

Define

\[
\bar\sigma_p:=\frac{A_p}{M_p},
\qquad
 d_p:=\frac{D_p}{M_p}.
\]

Then

\[
\boxed{
\frac1p(\log M_p)'
=\bar\sigma_p-d_p-c_p.
}
\]

Insert this into the phase-circulation formula:

\[
\boxed{
C_{phase}^{pq}
=
\frac1{\langle M_p\rangle}
\left\langle
M_q(\bar\sigma_p-d_p-c_p)
\right\rangle.
}
\]

## 3. Strain source minus diffusion drag

Define

\[
\boxed{
S_{phase}^{pq}
:=
\frac1{\langle M_p\rangle}
\left\langle
M_q(\bar\sigma_p-c_p)
\right\rangle,
}
\]

and

\[
\boxed{
D_{phase}^{pq}
:=
\frac1{\langle M_p\rangle}
\left\langle
M_qd_p
\right\rangle
\ge0.
}
\]

Then exactly

\[
\boxed{
C_{phase}^{pq}
=
S_{phase}^{pq}
-D_{phase}^{pq}.
}
\]

Therefore a fixed positive circulation implies only

\[
\boxed{
S_{phase}^{pq}
\ge
C_{phase}^{pq}>0.
}
\]

It does **not** imply a positive lower bound on \(D_{phase}^{pq}\).

Indeed, larger diffusion suppresses the same oriented concentration-growth loop.

## 4. Why hysteresis area is not dissipative area

On a periodic orbit,

\[
C_{phase}^{pq}
\propto
\oint M_q\,d\log M_p.
\]

This line integral is an oriented geometric area/circulation in moment space.

A mechanical-looking hysteresis loop often suggests dissipation, but no such interpretation is automatic here. The generalized driving force contains the recurrent strain source, and there is no thermodynamic positivity theorem identifying the loop area with \(D_p\).

Thus

\[
\boxed{
\text{nonzero moment-loop area}
\not\Rightarrow
\int D_p\,d\theta>c_*\text{ per loop}.
}
\]

Any such theorem would require additional constitutive information beyond the present moment equations.

## 5. Abstract ledger countermodel

The anti-shortcut can be seen directly at the scalar ledger level.

Take any smooth positive periodic functions

\[
M_p(\theta),
\qquad
M_q(\theta)
\]

forming a nonzero oriented loop in moment space.

Choose any nonnegative periodic diffusion ratio

\[
d_p(\theta)\ge0,
\]

including one arbitrarily small at the ledger level.

Define

\[
\boxed{
\bar\sigma_p(\theta)
:=
c_p+d_p(\theta)
+rac1p(\log M_p)'(\theta).
}
\]

Then the exact p-moment equation is satisfied identically, while the loop circulation is whatever was prescribed by \((M_p,M_q)\).

This is not a construction of a Navier--Stokes solution. It is a proof that the **moment balance alone** cannot force diffusion from loop area.

Additional PDE/geometric constraints are necessary.

## 6. Relation to M18-061

M18-061 already gives, after invariant averaging,

\[
\left\langle
\int(\sigma-c_p)\rho^pdy
\right\rangle
=
\langle D_p\rangle.
\]

This is an unweighted recurrent source-sink identity.

M18-067 concerns the different state weighting by \(M_q/M_p\) that defines the phase circulation.

The extra weighting can correlate strain source with concentration strongly enough to generate positive hysteresis even when no new diffusion floor follows.

Therefore M18-061 is not contradicted; the two identities use different state weights.

## 7. Spatial strain covariance versus phase strain covariance

The quantity

\[
M_q\bar\sigma_p
=
\frac{M_q}{M_p}A_p
\]

is not equal in general to

\[
A_q=\int\sigma\rho^qdy.
\]

Their difference is exactly a within-state amplitude/strain covariance term.

Hence the strain driving of the phase loop can itself split into

\[
\boxed{
\text{within-state strain/amplitude segregation}
\lor
\text{between-state strain/concentration phase locking}.
}
\]

The first returns to the M18-065 spatial transition machinery; the second remains a genuine recurrent phase-source mechanism.

## 8. What would be needed to force diffusion from a loop

A true loop-to-diffusion theorem would require at least one additional property such as

1. an upper bound on the strain work \(S_{phase}^{pq}\) strictly below the observed circulation unless \(D_p\) is positive;
2. an exact constitutive relation making the relevant moment-space 1-form a dissipative contact form;
3. a same-tube/material constraint tying concentration growth to transverse-area or flux loss;
4. a rigidity theorem excluding nonzero strain-driven periodic/recurrent moment loops.

None is presently certified at the required generality.

## 9. Consequence for the signed-route strategy

M18-059 eliminated naive unsigned accumulation.

M18-060--066 then found several exact signed/covariance structures.

M18-067 shows that the moment-space hysteresis branch also fails to become a consumptive resource by itself.

Thus the remaining useful signed routes are narrower:

\[
\boxed{
\text{material flux/label exit},
\quad
\text{director/zero-set topology},
\quad
\text{bounded-core spatial transition},
\quad
\text{critical-tail rigidity}.
}
\]

The general moment-loop area is not an additional closure currency.

## 10. Audit verdict

### Certified

1. The phase circulation decomposes exactly as
   \[
   C_{phase}^{pq}=S_{phase}^{pq}-D_{phase}^{pq}.
   \]
2. \(D_{phase}^{pq}\ge0\) enters with a negative sign.
3. Positive moment-space circulation forces positive strain driving but not positive diffusion cost.
4. Moment equations alone admit arbitrary smooth recurrent loops after suitable source choice, so loop-to-diffusion closure requires extra PDE structure.
5. The strain driving itself splits into spatial segregation or recurrent phase locking.

### Still open

- a constitutive constraint on recurrent strain driving strong enough to close the loop;
- material-flux cost of the phase loop;
- director/zero-set topology branches;
- component/thin-neck/interface degeneration;
- ancestry and remote/critical roots;
- global regularity.

## 11. Next target

The most concrete remaining signed object is the **material tube triad**

\[
D_B\log\rho=\sigma+\kappa-1,
\qquad
D_B\log A=1-\sigma,
\qquad
D_B\log\Phi=\kappa.
\]

M18-068 should revisit this triad using the new multi-p segregation results and ask whether the required high-amplitude/high-growth population can be supported by flux-neutral same-lineage loops, or whether the covariance necessarily forces a nonzero flux-residence correlation already identified by M16-020.

That target is more constrained than a generic moment-space hysteresis calculation.