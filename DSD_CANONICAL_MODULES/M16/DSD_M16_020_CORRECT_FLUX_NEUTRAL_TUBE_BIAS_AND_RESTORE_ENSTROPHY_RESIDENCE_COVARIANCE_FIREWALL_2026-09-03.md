# DSD M16-020 — Correct the flux-neutral tube bias and restore the enstrophy/residence covariance firewall

Date: 2026-09-03
Canonical ID: **M16-020**

Status: **DSD AUDIT CORRECTION / THE LAST CONCLUSION OF M16-019 WAS TOO STRONG. A MATERIAL FLUX TUBE MAY HAVE ZERO TIME-MEAN `kappa` AND STILL PAY A STRICTLY NEGATIVE ENSTROPHY-WEIGHTED `kappa` BUDGET THROUGH PHASE COVARIANCE WITH ITS ENSTROPHY/LINE-RESIDENCE WEIGHT. THEREFORE A SEPARATE NEGATIVE-`kappa` COMPENSATOR POPULATION IS NOT YET FORCED. THIS RESTORES THE MEASURE-MISMATCH FIREWALL PREVIOUSLY IDENTIFIED IN THE LEGACY LINE AND REPLACES THE FALSE POPULATION SPLIT BY AN EXACT TUBE-RESIDENCE LEDGER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Point to be corrected

M16-019 correctly derived the CE-H material tube laws

\[
D_B\log\rho=\sigma+\kappa-1,
\qquad
D_B\log A=1-\sigma,
\qquad
D_B\log\Phi=\kappa,
\]

for vorticity amplitude `rho`, transverse material area `A`, and material vorticity flux `Phi`.

It then observed that a closed flux cycle satisfies

\[
\langle\kappa\rangle_{\rm time}=0.
\]

The over-strong step was to infer that such a neutral tube cannot itself contribute to the global negative Rayleigh budget

\[
\int\kappa\rho^2dy=-P<0.
\]

That inference is false because the two averages use different weights.

---

## 2. Exact tube-coordinate disintegration

Consider an oriented infinitesimal material vortex tube segment. Let `s` denote arclength along the vortex line and `dPhi` its transverse vorticity-flux measure. Since

\[
d\Phi=\rho\,dA,
\]

the volume element is

\[
dV=dA\,ds=\frac{d\Phi}{\rho}\,ds.
\]

Hence the tube-segment enstrophy is

\[
\boxed{
e_{\rm tube}
=\int \rho^2dV
=\Phi L_\rho,
}
\]

where

\[
\boxed{
L_\rho
:=\int_{\Gamma}\rho\,ds
}
\]

is the vorticity-weighted line-residence factor.

Because CE-H gives

\[
W\cdot\nabla\kappa=0,
\]

`kappa` is constant along each instantaneous vortex line. Therefore the tube contribution to the Rayleigh budget is

\[
\boxed{
\int_{\rm tube}\kappa\rho^2dV
=\kappa\Phi L_\rho
=\kappa e_{\rm tube}.
}
\]

Thus the enstrophy-weighted and flux-weighted `kappa` averages differ precisely by the residence factor `L_rho`.

---

## 3. Neutral flux does not imply neutral enstrophy-weighted kappa

For a recurrent material flux label with

\[
\langle\kappa\rangle_{\rm time}=0,
\]

one may still have

\[
\boxed{
\langle\kappa e_{\rm tube}\rangle<0.
}
\]

Indeed, since the unweighted mean is zero,

\[
\boxed{
\langle\kappa e_{\rm tube}\rangle
=\operatorname{Cov}_{\rm time}(\kappa,e_{\rm tube}).
}
\]

A completely legal cycle is one in which tube enstrophy is larger during the `kappa<0` phase and smaller during the `kappa>0` phase.

Therefore

\[
\boxed{
\langle\kappa\rangle=0
\not\Rightarrow
\langle\kappa e_{\rm tube}\rangle=0.
}
\]

This is the exact same measure-mismatch mechanism previously encountered in the legacy audit and must remain a firewall in the canonical line.

---

## 4. Exact evolution of the residence factor

Under CE-H,

\[
D_B ds=\left(\sigma+\frac12\right)ds,
\]

and

\[
D_B\rho=(\sigma+\kappa-1)\rho.
\]

Since `kappa` is constant along the vortex line, define

\[
S_\sigma
:=\int_\Gamma \sigma\rho\,ds,
\qquad
\bar\sigma_\rho
:=\frac{S_\sigma}{L_\rho}.
\]

Then

\[
\boxed{
L_\rho'
=\left(\kappa-\frac12\right)L_\rho
+2S_\sigma,
}
\]

or equivalently

\[
\boxed{
D_B\log L_\rho
=\kappa+2\bar\sigma_\rho-\frac12.
}
\]

Since

\[
e_{\rm tube}=\Phi L_\rho,
\qquad
\Phi'=\kappa\Phi,
\]

we obtain

\[
\boxed{
D_B e_{\rm tube}
=2\left(\kappa+\bar\sigma_\rho-\frac14\right)e_{\rm tube}.
}
\]

---

## 5. Recurrent tube identity

If the same material tube segment returns recurrently with bounded nonzero `Phi` and `e_tube`, then the mean logarithmic drifts vanish:

\[
\langle\kappa\rangle=0,
\]

and

\[
\left\langle
\kappa+\bar\sigma_\rho-\frac14
\right\rangle=0.
\]

Therefore

\[
\boxed{
\langle\bar\sigma_\rho\rangle=\frac14.
}
\]

For the ordinary (not logarithmic) enstrophy balance, recurrence gives

\[
0=\langle e_{\rm tube}'\rangle
=2\left\langle
\left(\kappa+\bar\sigma_\rho-\frac14\right)e_{\rm tube}
\right\rangle,
\]

so

\[
\boxed{
\langle\kappa e_{\rm tube}\rangle
=-\left\langle
\left(\bar\sigma_\rho-\frac14\right)e_{\rm tube}
\right\rangle.
}
\]

Hence a negative enstrophy-weighted `kappa` budget is exactly equivalent, on a recurrent neutral-flux tube, to a positive strain-residence surplus.

This is the tube-level version of the global similarity enstrophy ledger.

---

## 6. Corrected interpretation of M16-019

The correct statement is not

\[
\text{neutral source tubes}
\Rightarrow
\text{separate negative-`kappa` compensator population}.
\]

The correct dichotomy is

\[
\boxed{
\text{negative enstrophy-weighted `kappa` budget}
\Rightarrow
\text{negative flux bias}
\ \lor\ 
\text{negative `kappa`--residence/enstrophy covariance}.
}
\]

The second alternative allows the same recurrent tube population to carry both positive and negative `kappa` phases while remaining flux-neutral over a cycle.

---

## 7. DSD audit consequence

M16-019 remains valid through the exact three-way tube ledger

\[
D_B\log\rho=\sigma+\kappa-1,
\quad
D_B\log A=1-\sigma,
\quad
D_B\log\Phi=\kappa.
\]

Its final inference of a mandatory distinct compensator population is retracted.

The new canonical target is the residence/covariance mechanism itself:

1. can `L_rho` remain recurrent while paying a fixed negative covariance with `kappa`?;
2. if yes, what strain heterogeneity is required along the same vortex tube?;
3. if no, does line-residence drift force material replacement/exit?

These are addressed in M16-021+.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
