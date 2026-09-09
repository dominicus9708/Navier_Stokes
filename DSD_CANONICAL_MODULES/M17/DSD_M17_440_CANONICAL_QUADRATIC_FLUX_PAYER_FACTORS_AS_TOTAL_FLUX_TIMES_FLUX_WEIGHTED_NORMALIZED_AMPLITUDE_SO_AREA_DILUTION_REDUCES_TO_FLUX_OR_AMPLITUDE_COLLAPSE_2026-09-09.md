# DSD M17-440 — The canonical quadratic flux payer factors as total flux times flux-weighted normalized amplitude, so true area dilution reduces to flux thinning or flux-weighted amplitude collapse

Date: 2026-09-09  
Canonical ID: **M17-440**

Status: **ACTIVE QUADRATIC-FLUX FACTORIZATION / AREA-DILUTION REDUCTION / M17-439 REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Goal

M17-439 replaced the partition-dependent participation number `N_eff` by the partition-free cross-sectional currency

\[
\mathfrak Q_\Phi
:=
r^2\int_A\rho^2dA
\]

and geometric area participation

\[
\mathfrak A:=A_{tot}/r^2.
\]

The remaining question was whether growth of `mathfrak A` is an independent physical escape.

The present module shows that for the quadratic raw-`H2` payer it is more precise to factor `mathfrak Q_Phi` into total flux and a **flux-weighted normalized amplitude**. If total positive flux is retained, loss of the quadratic payer forces the vorticity flux measure itself to concentrate on vanishing normalized amplitude.

Thus physical area growth is a geometric consequence of amplitude dilution, not the primary invariant mechanism.

## 2. Own-scale normalized cross-section

Let `r` be the physical own scale and let `A` be a retained positive-orientation transverse cross-sectional region.

Define normalized transverse area and normalized vorticity amplitude by

\[
d\widetilde A:=r^{-2}dA,
\qquad
\widetilde\rho:=r^2\rho.
\]

The vorticity flux is scale invariant:

\[
\boxed{
\Phi
=
\int_A\rho\,dA
=
\int_{\widetilde A}\widetilde\rho\,d\widetilde A.
}
\]

The M17-439 quadratic currency becomes

\[
\boxed{
\mathfrak Q_\Phi
=
r^2\int_A\rho^2dA
=
\int_{\widetilde A}\widetilde\rho^2d\widetilde A.
}
\]

## 3. Flux probability measure

Assume

\[
\Phi>0.
\]

Define the normalized positive flux probability measure

\[
\boxed{
dp_\Phi
:=
\frac{\widetilde\rho\,d\widetilde A}{\Phi}.
}
\]

Then

\[
\int dp_\Phi=1.
\]

Define the flux-weighted normalized amplitude

\[
\boxed{
\mathfrak a_\Phi
:=
\int\widetilde\rho\,dp_\Phi.
}
\]

By construction,

\[
\begin{aligned}
\Phi\mathfrak a_\Phi
&=
\int\widetilde\rho^2d\widetilde A\\
&=\mathfrak Q_\Phi.
\end{aligned}
\]

Therefore the exact partition-free factorization is

\[
\boxed{
\mathfrak Q_\Phi
=
\Phi\,\mathfrak a_\Phi.
}
\]

This is the main identity of M17-440.

## 4. Meaning of the factorization

There are only two direct ways for `mathfrak Q_Phi` to vanish:

\[
\boxed{
\Phi\to0
\quad\text{or}\quad
\mathfrak a_\Phi\to0.
}
\]

The first is positive-flux thinning.

The second is **flux-weighted normalized amplitude collapse**.

It is not an arbitrary label-fragmentation effect.

## 5. Threshold formulation of amplitude collapse

For `a>0`, define the fraction of positive flux carried at normalized amplitude at least `a`:

\[
\boxed{
\eta_a
:=
p_\Phi\{\widetilde\rho\ge a\}.
}
\]

Because `widetilde rho` is nonnegative,

\[
\mathfrak a_\Phi
\ge
\int_{\{\widetilde\rho\ge a\}}
\widetilde\rho\,dp_\Phi
\ge
a\eta_a.
\]

Hence

\[
\boxed{
\eta_a\ge\eta_*>0
\Longrightarrow
\mathfrak Q_\Phi
\ge
a\eta_*\Phi.
}
\]

In particular, if

\[
\Phi\ge\Phi_*>0
\]

and a fixed positive fraction of the flux remains above a fixed normalized amplitude threshold, then

\[
\boxed{
\mathfrak Q_\Phi
\ge
a\eta_*\Phi_*>0.
}
\]

The quadratic payer is then uniformly nondegenerate independently of the total geometric area.

Conversely, Markov's inequality with respect to `p_Phi` gives

\[
\boxed{
\eta_a
\le
\frac{\mathfrak a_\Phi}{a}.
}
\]

Therefore if

\[
\Phi\ge\Phi_*>0,
\qquad
\mathfrak Q_\Phi\to0,
\]

then

\[
\mathfrak a_\Phi\to0
\]

and for every fixed `a>0`,

\[
\boxed{
\eta_a\to0.
}
\]

Thus almost all retained positive flux, in the flux-probability sense, must move into arbitrarily small normalized amplitude.

## 6. Cross-sectional area growth is a consequence

M17-439 gives

\[
\mathfrak Q_\Phi
\ge
\frac{\Phi^2}{\mathfrak A}.
\]

Using

\[
\mathfrak Q_\Phi=\Phi\mathfrak a_\Phi,
\]

we obtain

\[
\boxed{
\mathfrak A
\ge
\frac{\Phi}{\mathfrak a_\Phi}.
}
\]

Hence under a retained positive flux floor,

\[
\mathfrak a_\Phi\to0
\Longrightarrow
\mathfrak A\to\infty.
\]

This identifies the direction of implication relevant to the proof architecture:

\[
\boxed{
\text{quadratic payer dilution at positive flux}
\Longrightarrow
\text{flux-weighted amplitude collapse}
\Longrightarrow
\text{area participation decompactification}.
}
\]

Large area alone does not force payer dilution, because the amplitude can remain concentrated on a smaller flux-carrying subset.

## 7. Raw-H2 record currency

M17-439 gives for the retained parent-length loop geometry

\[
R_m^{-3}H_m^{norm}
\gtrsim
c\alpha_m\mathfrak Q_{\Phi,m}.
\]

Using the exact factorization,

\[
\boxed{
R_m^{-3}H_m^{norm}
\gtrsim
c\alpha_m\Phi_m\mathfrak a_{\Phi,m}.
}
\]

Therefore the partition-free closure criterion becomes

\[
\boxed{
\sum_m
\alpha_m\Phi_m\mathfrak a_{\Phi,m}
=\infty.
}
\]

A sufficient retained branch is

\[
\alpha_m\ge\alpha_*>0,
\qquad
\Phi_m\ge\Phi_*>0,
\qquad
\mathfrak a_{\Phi,m}\ge a_*>0
\]

on infinitely many representation-safe records. Then every such record contributes a fixed positive amount to the ancestral raw-`H2` sum.

## 8. Relation to corrected M17-432

The new factorization also clarifies the scope of the M17-432 flux-weighted occupation theorem.

Since

\[
\mathfrak Q_\Phi
=
\int\widetilde\rho\,d\Phi,
\]

where

\[
d\Phi=\widetilde\rho\,d\widetilde A,
\]

the cross-sectional quadratic payer is a **flux-linear integral of the normalized amplitude observable**.

Therefore corrected M17-432 can be applied to robust compact amplitude classes of the form

\[
\{\widetilde\rho\ge a\}
\]

provided the label-state geometry and the common cross-sectional representation remain valid.

Pure material-label turnover cannot remove a positive flux-weighted amplitude class; the actual escape is the collapse of the normalized amplitude observable, flux loss, or failure of compact label-state/cross-section/genealogy hypotheses.

This does not reverse the correction to M17-432: raw-`H2` itself is not generally flux-linear. Rather, M17-440 identifies the correct flux-linear observable whose integral equals the cross-sectional quadratic currency.

## 9. Updated physical split

The M17-439 area-dispersion branch refines to

\[
\boxed{
\begin{aligned}
G_{quadratic\ payer\ dilution}
\Longrightarrow{}&
G_{positive\ flux\ thinning}\\
&\lor G_{flux\text{-}weighted\ normalized\ amplitude\ collapse}\\
&\lor G_{cross\text{-}section/coefficient\text{-}scale\ coherence\ loss}\\
&\lor G_{label/state\ noncompactness}\\
&\lor G_{genealogy/interface/domain\ loss}.
\end{aligned}
}
\]

Cross-sectional area growth remains a useful geometric symptom, but it is not the most primitive canonical escape for this payer.

## 10. DSD audit role

DSD is used only to separate a geometric denominator (`area`) from the invariant measure-theoretic mechanism (`flux-weighted amplitude`). The proof is ordinary scaling, normalization of a positive measure, Cauchy--Schwarz, and Markov's inequality.

## 11. Audit verdict

**PASS — M17-439 transverse-area dilution is refined to an exact flux × flux-weighted-amplitude factorization.**

At retained positive flux, quadratic payer collapse forces normalized amplitude collapse in flux measure; arbitrary label fragmentation and mere geometric area growth are not independent primary mechanisms.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
