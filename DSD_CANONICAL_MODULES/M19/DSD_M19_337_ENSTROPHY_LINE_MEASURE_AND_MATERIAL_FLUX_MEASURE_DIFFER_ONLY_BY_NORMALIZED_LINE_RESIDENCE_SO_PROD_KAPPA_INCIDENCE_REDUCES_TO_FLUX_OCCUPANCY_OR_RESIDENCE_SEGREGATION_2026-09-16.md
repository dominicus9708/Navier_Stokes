# DSD M19-337 — Enstrophy line measure and material-flux measure differ only by normalized line residence, so productive-kappa incidence reduces to flux occupancy or residence segregation

Date: 2026-09-16  
Canonical ID: **M19-337**

Status: **ACTIVE MEASURE-TRANSFER REDUCTION / PROD-KAPPA INCIDENCE REFINEMENT / RESIDENCE-SEGREGATION FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-323--336

M19-323 writes the snapshot enstrophy-weighted coefficient law in flux-line coordinates. On a regular positive-orientation flux family let \(\lambda\) denote a vortex-line label, \(d\nu(\lambda)\) the corresponding positive vorticity-flux label measure, and

\[
L_1(\lambda):=\int_{\Gamma_\lambda}\rho\,ds.
\]

Then snapshot enstrophy is

\[
E=\int L_1\,d\nu,
\]

and M19-323 uses

\[
d\Pi(\lambda)=\frac{L_1(\lambda)}{E}\,d\nu(\lambda).
\]

Exact CE-H gives \(D_\xi\kappa=0\), so \(\kappa=\kappa_\lambda\) is a line label on every regular connected line.

M19-333--336 show that on the productive retained compact branch one must confront quantitative coefficient heterogeneity, and the sign-uniform recurrent alternative is driven into zero/sign transition or explicit compactness/genealogy loss. The remaining spatial branch is mixed-sign / coefficient-separated line structure.

M19-334 left an incidence firewall: a positive enstrophy-weighted coefficient population need not automatically be a positive material-flux population on a selected productive family.

The present module makes that firewall exact.

## 2. Material-flux probability on the same line family

Let the total positive flux of the represented family be

\[
\Phi:=\int d\nu>0.
\]

Define the flux-label probability

\[
\boxed{
dp_\Phi(\lambda):=\frac{d\nu(\lambda)}{\Phi}.
}
\]

Define the flux-weighted mean line residence

\[
\boxed{
\bar L_1:=\int L_1\,dp_\Phi=\frac{E}{\Phi}.
}
\]

Substituting \(d\nu=\Phi\,dp_\Phi\) into the definition of \(d\Pi\) gives the exact Radon--Nikodym identity

\[
\boxed{
 d\Pi
 =
 \frac{L_1}{\bar L_1}\,dp_\Phi.
}
\]

Hence enstrophy weighting differs from positive material-flux weighting only by the normalized line-residence density

\[
\boxed{
\ell(\lambda):=\frac{L_1(\lambda)}{\bar L_1},
\qquad
\int \ell\,dp_\Phi=1.
}
\]

No further geometric model is used in this identity.

## 3. Quantitative population transfer

Let \(S\) be any measurable coefficient-line population, for example

\[
S_+=\{\kappa_\lambda\ge \kappa_*\},
\qquad
S_- =\{\kappa_\lambda\le-\kappa_*\}.
\]

Then

\[
\boxed{
\Pi(S)=\int_S \ell\,dp_\Phi.
}
\]

Assume on \(S\) the residence density has a uniform upper bound

\[
\ell\le L_*<\infty.
\]

Then

\[
\Pi(S)\le L_*p_\Phi(S),
\]

so

\[
\boxed{
\Pi(S)\ge\theta_*>0
\Longrightarrow
p_\Phi(S)\ge \frac{\theta_*}{L_*}>0.
}
\]

Therefore a fixed enstrophy-weighted coefficient population transfers to a fixed material-flux population whenever line residence is not allowed to concentrate without bound.

## 4. Exact failure alternative

Conversely, suppose

\[
\Pi(S)\ge\theta_*>0
\]

but

\[
p_\Phi(S)=:\eta\to0.
\]

Since

\[
\theta_*\le\int_S\ell\,dp_\Phi,
\]

the average normalized residence over \(S\) obeys

\[
\boxed{
\frac1{\eta}\int_S\ell\,dp_\Phi
\ge
\frac{\theta_*}{\eta}
\to\infty.
}
\]

Thus the measure-transfer failure is not an untyped incidence defect. It is precisely

\[
\boxed{
G_{\rm line\text{-}residence\ segregation/concentration}.
}
\]

The coefficient population remains important to enstrophy only by occupying lines whose integrated amplitude residence \(L_1\) is anomalously large relative to the flux-family mean.

## 5. Two-sign version

Assume the quantitative spatial mixed-sign branch supplies

\[
\Pi(S_+)\ge\theta_+>0,
\qquad
\Pi(S_-)\ge\theta_->0.
\]

Then either

\[
\boxed{
 p_\Phi(S_+)\ge \eta_+>0,
 \qquad
 p_\Phi(S_-)\ge \eta_->0,
}
\]

or at least one sign population has unbounded normalized residence concentration.

Thus the old M19-334 gate refines to

\[
\boxed{
\mathcal T_{\rm inc}^{prod-\kappa}
\Longrightarrow
\mathcal T_{\rm flux}^{\pm\ occupancy}
\lor
G_{\rm residence\ segregation}
\lor
G_{\rm line/cross\text{-}section/genealogy\ loss}.
}
\]

## 6. Relation to M17-440--442

M17-440 uses a positive material-flux probability on a coherent transverse representation and defines the flux-weighted normalized amplitude. M19-337 identifies the exact additional line-residence density that must be controlled before the M19-323 enstrophy-line population can be read as a positive flux population.

This is compatible with M17-442's central warning: ensemble flux weighting can be redistributed among labels even when every individual material law is regular.

The present module therefore does not erase the amplitude/reweighting frontier. It isolates the missing density:

\[
\boxed{
\text{enstrophy-line heterogeneity}
\to
\text{flux-line heterogeneity}
\quad\text{iff normalized line residence does not concentrate.}
}
\]

## 7. Audit firewall

Do not identify a three-dimensional enstrophy-weighted coefficient fraction with a material-flux fraction without the common regular line-family representation.

Do not infer a uniform upper bound on \(L_1/\bar L_1\) from bounded total enstrophy or positive total flux alone.

Failure of such a bound is a real survivor, not a technical omission: it is line-residence segregation.

## 8. Consequence for the current spatial mixed-sign branch

The productive spatial branch is now narrower:

\[
\boxed{
\begin{aligned}
H_{\rm productive\ mixed\text{-}sign\ CEH}
\Longrightarrow{}&
H_{\rm two\ sign\ flux\ populations}\\
&\lor G_{\rm line\text{-}residence\ segregation}\\
&\lor G_{\rm remote/representation/interface/genealogy\ loss}.
\end{aligned}
}
\]

The first branch can now be combined with the M17-440--442 flux-weighted amplitude currency. The second is an explicit new concentration variable rather than a vague incidence failure.

## 9. Audit verdict

**PASS — M19-334's enstrophy-to-flux incidence gap is reduced to an exact Radon--Nikodym residence-weight problem.**

The next calculation is sign-resolved M17-440 factorization: determine what finite raw-H2 ancestry forces on the positive- and negative-kappa flux populations separately when both have nonvanishing flux fractions.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
