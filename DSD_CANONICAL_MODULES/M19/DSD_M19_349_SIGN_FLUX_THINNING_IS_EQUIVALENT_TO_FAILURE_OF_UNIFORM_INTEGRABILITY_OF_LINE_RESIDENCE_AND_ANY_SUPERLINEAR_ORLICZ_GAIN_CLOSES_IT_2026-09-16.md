# DSD M19-349 — Sign-flux thinning requires failure of uniform integrability of line residence; any superlinear Orlicz gain closes the sparse-residence branch

Date: 2026-09-16  
Canonical ID: **M19-349**

Status: **ACTIVE RESIDENCE-INTEGRABILITY THEOREM / SHARP L1 FIREWALL / ORLICZ CLOSURE CRITERION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setup

Let \(d\nu\) be the positive material-flux label measure on a regular represented flux family and

\[
\Phi:=\int d\nu.
\]

Define the flux probability

\[
\boxed{dp_\Phi:=\frac{d\nu}{\Phi}.}
\]

For each represented line label \(\lambda\), let

\[
\boxed{L_1(\lambda):=\int_{\Gamma_\lambda}\rho\,ds.}
\]

Then the total represented enstrophy is

\[
E=\int L_1d\nu
=\Phi\,\mathbb E_{p_\Phi}[L_1].
\]

Thus bounded enstrophy and retained total positive flux give only a finite first moment of \(L_1\).

## 2. A sign sector with nontrivial enstrophy

Let \(S\) be one coefficient-sign sector and define its flux fraction

\[
\eta:=p_\Phi(S)=\frac{\Phi_S}{\Phi}.
\]

Its sign enstrophy is

\[
E_S
:=\int_S L_1d\nu
=\Phi\eta\,\bar L_S,
\]

where

\[
\bar L_S
:=\frac1\eta\int_SL_1dp_\Phi.
\]

Assume the M19-345 nontrivial sign-moment/compact-coefficient branch, so

\[
\boxed{E_S\ge e_*>0.}
\]

Assume also recurrent total-flux bounds

\[
0<\Phi_-\le\Phi\le\Phi_+<\infty.
\]

Then

\[
\boxed{
\bar L_S
=\frac{E_S}{\Phi\eta}
\ge
\frac{e_*}{\Phi_+}\eta^{-1}.
}
\]

Therefore a thinning sign sector necessarily has diverging conditional mean line residence.

## 3. The first moment is exactly critical

The total first moment is

\[
\mathbb E_{p_\Phi}[L_1]
=E/\Phi.
\]

A sign sector with

\[
\eta\to0,
\qquad
\bar L_S\sim c\eta^{-1}
\]

contributes

\[
\eta\bar L_S\sim c
\]

to the first moment.

Thus finite \(L^1(p_\Phi)\) control permits the exact sparse-residence scaling found in M19-348.

Equivalently Markov gives only

\[
\boxed{
p_\Phi\{L_1\ge\Lambda\}
\le
\frac{E/\Phi}{\Lambda},
}
\]

and a population with probability \(\eta\sim\Lambda^{-1}\) at residence \(L_1\sim\Lambda\) saturates this estimate.

Hence no theorem using only the mean residence can exclude sign-flux thinning.

## 4. Superlinear Orlicz criterion

Let

\[
\Psi:[0,\infty)\to[0,\infty)
\]

be convex and superlinear:

\[
\boxed{
\frac{\Psi(x)}{x}\to\infty
\qquad(x\to\infty).
}
\]

By Jensen on the conditional probability \(p_\Phi(\cdot\mid S)\),

\[
\int_S\Psi(L_1)dp_\Phi
\ge
\eta\Psi(\bar L_S).
\]

Using Section 2,

\[
\boxed{
\int\Psi(L_1)dp_\Phi
\ge
\eta
\Psi\!\left(
\frac{e_*}{\Phi_+\eta}
\right).
}
\]

Let

\[
c_*:=e_*/\Phi_+.
\]

Then

\[
\eta\Psi(c_*/\eta)
=
c_*
\frac{\Psi(c_*/\eta)}{c_*/\eta}.
\]

Therefore

\[
\boxed{
\eta\to0
\Longrightarrow
\int\Psi(L_1)dp_\Phi\to\infty.
}
\]

This is the central theorem.

## 5. Uniform integrability consequence

Suppose there exists one convex superlinear \(\Psi\) and one record-uniform constant \(C_\Psi\) such that

\[
\boxed{
\int\Psi(L_1)dp_\Phi
\le C_\Psi.
}
\]

Then Section 4 implies a fixed lower bound

\[
\boxed{\eta\ge\eta_*>0.}
\]

for every sign sector carrying the nontrivial enstrophy floor \(e_*\).

Thus the family \(\{L_1\}\) being uniformly integrable with respect to flux probability is enough to eliminate sign-flux thinning.

Conversely, a sequence of thinning sign sectors with fixed enstrophy mass forces failure of every such superlinear Orlicz bound.

This is the de la Vallee-Poussin form of the sparse-residence escape.

## 6. Power moments

Take

\[
\Psi(x)=x^{1+\varepsilon},
\qquad \varepsilon>0.
\]

Then

\[
\int L_1^{1+\varepsilon}dp_\Phi
\ge
\eta\bar L_S^{1+\varepsilon}
\gtrsim
\eta^{-\varepsilon}.
\]

Hence a uniform bound

\[
\sup_R
\int L_1^{1+\varepsilon}dp_\Phi
<\infty
\]

immediately gives

\[
\boxed{\eta\ge c_\varepsilon>0.}
\]

No large \(\varepsilon\) is required; any positive power improvement over \(L^1\) closes the thinning branch.

## 7. The near-endpoint L log L criterion

Take for large \(x\)

\[
\Psi(x)=x\log(1+x).
\]

Then

\[
\int L_1\log(1+L_1)dp_\Phi
\gtrsim
c_*\log(1+c_*/\eta).
\]

Thus even the weak superlinear gain

\[
\boxed{
\sup_R
\int L_1\log(1+L_1)dp_\Phi<\infty
}
\]

forbids \(\eta\to0\).

This shows that the required improvement over first-moment control can be arbitrarily mild in an Orlicz sense.

## 8. Relation to M19-348

M19-348 constructs the sharp scaling witness

\[
\eta\sim R^{-p},
\qquad
\bar L_S\sim R^p.
\]

For this witness,

\[
\eta\bar L_S\sim1,
\]

but

\[
\eta\bar L_S^{1+\varepsilon}
\sim R^{p\varepsilon}
\to\infty
\]

for every \(p>0\) and \(\varepsilon>0\).

Likewise

\[
\eta\bar L_S\log(1+\bar L_S)
\sim p\log R.
\]

Hence M19-348 is exactly critical at \(L^1\): it evades the first moment and violates every fixed superlinear uniform-integrability criterion.

## 9. Updated theorem gate

The principal sparse-residence gate is no longer vague line-length control. It is

\[
\boxed{
\mathcal T_{res}^{UI}:
\text{prove uniform integrability of }L_1
\text{ under flux probability on the retained productive CE-H family.}
}
\]

Any one of the following would suffice:

1. \(L^{1+\varepsilon}\) residence control for some \(\varepsilon>0\);
2. \(L\log L\) control;
3. any de la Vallee-Poussin superlinear Orlicz bound;
4. an equivalent geometric theorem preventing flux mass from escaping to arbitrarily high residence.

Failure of all such criteria is now an explicit concentration/decompactification branch.

## 10. Audit verdict

**PASS — finite mean line residence is exactly the critical endpoint, and sign-flux thinning is a uniform-integrability failure.**

A vanishing material-flux sign population carrying a fixed enstrophy/sign moment must move to arbitrarily large line residence. Any record-uniform superlinear moment, even \(L\log L\), rules this out.

The next task is to ask whether existing Navier--Stokes/CE-H resources can produce such a superlinear residence estimate. The most promising bridges are line-length/amplitude factorization, palinstrophy control of amplitude variation, and recurrent material-line deformation. None is asserted here.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
