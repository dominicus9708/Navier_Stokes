# DSD M19-364 — A near-critical three-halves seed pipeline has finite stationary dormant resource and finite instantaneous amplification rate

Date: 2026-09-17  
Canonical ID: **M19-364**

Status: **ACTIVE AGE-STRUCTURED SCALING WITNESS / STATIONARY SEED-CONVEYOR FIREWALL / NOT AN EXACT PDE SOLUTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-362 shows that one fixed base slice can contain infinitely many future curvature seeds with geometrically summable volume, flux and enstrophy.

A stronger possible objection is that a positive renewal rate might nevertheless force an infinite **instantaneous** amount of dormant seed resource when the conveyor is viewed in a statistically stationary regime.

The present module audits that objection.

The answer is negative at the scaling level: the critical \(3/2\) pipeline admits a finite stationary dormant reservoir.

This is a scaling/transport witness, not the construction of an exact Navier--Stokes solution.

## 2. Remaining-time coordinate

Fix a similarity time \(\theta\). For a dormant material seed that will enter the fixed-flux curvature carrier class after remaining time

\[
s\ge0,
\]

write its present flux as \(q(s)\).

M19-360 gives the critical upper scale

\[
q(s)\lesssim C e^{-3s/2}.
\]

At the borderline M19-361/M19-362 regime take the model law

\[
\boxed{
q(s)=\phi_*e^{-3s/2},
}
\]

so that the seed reaches

\[
q(0)=\phi_*
\]

at activation.

As time increases along one scheduled seed,

\[
\dot s=-1.
\]

Hence

\[
\frac{dq}{d\theta}
=-q'(s)
=\frac32q,
\]

which is exactly the material-flux law at the critical coefficient

\[
\boxed{\kappa=\frac32.}
\]

## 3. Constant activation-rate model

Let \(\lambda>0\) denote a schematic activation/renewal rate per unit similarity time.

The stationary remaining-time population then has density

\[
\lambda\,ds.
\]

Thus the instantaneous total dormant flux represented by all future cohorts is

\[
\mathcal F_{dorm}
:=
\lambda\int_0^\infty q(s)ds.
\]

Substituting the critical profile,

\[
\boxed{
\mathcal F_{dorm}
=
\lambda\phi_*
\int_0^\infty e^{-3s/2}ds
=
\frac23\lambda\phi_*<\infty.
}
\]

Therefore positive renewal rate does not force infinite instantaneous dormant absolute flux.

## 4. Instantaneous positive amplification rate is also finite

The critical positive flux-growth rate of one seed is

\[
\kappa q
=
\frac32q.
\]

Integrating over the stationary dormant population gives

\[
\mathcal G_{amp}
:=
\lambda\int_0^\infty\frac32q(s)ds.
\]

Hence

\[
\boxed{
\mathcal G_{amp}
=
\lambda\phi_*.
}
\]

This has a useful exact interpretation: per unit similarity time, the dormant reservoir supplies order \(\lambda\) newly activated packets, each arriving with flux \(\phi_*\), while the total instantaneous positive amplification action stays finite.

The conveyor is therefore compatible with a finite nonzero recurrent flux-growth rate.

## 5. Stationary transport balance

The remaining-time profile satisfies

\[
q'(s)=-\frac32q(s).
\]

Thus

\[
-\partial_s q
=
\frac32q.
\]

Integrating over \(s>0\),

\[
\int_0^\infty\frac32q(s)ds
=
q(0)-\lim_{s\to\infty}q(s)
=
\phi_*.
\]

After multiplying by \(\lambda\),

\[
\boxed{
\mathcal G_{amp}
=
\lambda q(0).
}
\]

Hence the positive amplification action is exactly the boundary outflow of the dormant seed reservoir in this age/remaining-time coordinate.

This is the stationary continuum analogue of the fixed per-reset action in M19-363.

## 6. Material volume has the same stationary profile

The similarity material-volume law is

\[
D_B\log dV=\frac32.
\]

A seed that reaches a fixed activation volume \(V_*\) after remaining time \(s\) has present volume

\[
\boxed{
v(s)=V_*e^{-3s/2}.
}
\]

Therefore the total instantaneous dormant material volume is

\[
\boxed{
\mathcal V_{dorm}
=
\lambda\int_0^\infty v(s)ds
=
\frac23\lambda V_*<\infty.
}
\]

The same critical exponent makes both flux and material-volume reservoirs finite.

## 7. Enstrophy consistency at the scaling level

If dormant seed amplitudes remain uniformly bounded by an order-one scale in the witness, their enstrophy is at most proportional to their volume.

Thus an age profile

\[
E(s)\lesssim C_E e^{-3s/2}
\]

gives

\[
\boxed{
\lambda\int_0^\infty E(s)ds<\infty.
}
\]

This is only a consistency scaling statement. It does not assert that a true CE-H solution realizes independent disjoint seeds with this exact profile.

## 8. Discrete generation version

The retained first-hitting generations have stage durations bounded below and above,

\[
0<\ell_-\le\Delta\theta_j\le\ell_+<\infty.
\]

Hence a selected representative renewal sequence has uniformly bounded event count per unit similarity-time interval.

For any observation time \(\theta\), M19-360 gives for future events

\[
|\phi_j(\theta)|
\lesssim
 e^{-3(\theta_j-\theta)/2}.
\]

Uniform local event-count bounds therefore imply

\[
\boxed{
\sum_{\theta_j>\theta}|\phi_j(\theta)|
\le C_{dorm}<\infty
}
\]

uniformly at the scaling level, by comparison with a geometric series.

Thus the continuous stationary model is consistent with the actual bounded-stage-duration generation architecture.

## 9. Coupling to the mixed-sign conveyor

M19-363 shows that every activation requires fixed positive flux-amplification action.

M19-346/356 show that recurrent positive flux-growth currency can be balanced by

\[
\langle C_0^\Phi\rangle
=-\nu\langle A_+^\Phi\rangle
=-\nu\langle A_-^\Phi\rangle
\]

through an extensive diffuse zero-interface conveyor.

M19-364 now shows that the **dormant positive side of the conveyor itself need not accumulate an infinite instantaneous reservoir**.

Therefore neither static occupancy nor instantaneous positive-action finiteness is enough to exclude the critical pipeline.

## 10. What would actually break the stationary witness

A successful closure must prohibit at least one ingredient of the stationary profile:

\[
\boxed{
\begin{aligned}
&\text{(i) the critical amplification rate }\bar\kappa\approx3/2,\\
&\text{(ii) exponentially small dormant seed flux/volume,}\\
&\text{(iii) bounded event-rate material genealogy,}\\
&\text{(iv) recyclable negative-sector/zero-interface discharge.}
\end{aligned}
}
\]

This points again to a strict amplification gap, a minimum seed-size theorem, an irreversible genealogy/topology budget, or a nonrecyclable coupling between positive amplification and negative discharge.

## 11. Audit verdict

**PASS-NO-GO / SCALING WITNESS.**

The near-critical \(3/2\) reset mechanism can be organized as an age-structured stationary seed pipeline with finite instantaneous dormant flux, finite dormant material volume, finite scaling-level enstrophy, and finite positive amplification rate. Therefore a contradiction based only on finite instantaneous resource occupancy is unavailable at the current level of information.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
