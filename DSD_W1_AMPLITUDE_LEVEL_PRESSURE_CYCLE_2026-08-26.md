# DSD W1 Amplitude-Level Pressure Cycle

Date: 2026-08-26

Status: **GLOBAL `p=3` PRESSURE WORK DECOMPOSED INTO GAUGE-INVARIANT FLUXES ACROSS VELOCITY-AMPLITUDE LEVEL SETS / INCOMPRESSIBILITY FORCES EQUAL UP- AND DOWN-CROSSING VOLUME FLUX / ENDPOINT RESIDUE LOCALIZED TO A LEVEL-WISE PRESSURE-GAP CYCLE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current W1 endpoint satisfies

\[
\boxed{
\langle F_3\rangle_\mu
=
\nu\langle D_3\rangle_\mu
+\frac{\mathscr R_3}{6},
\qquad
\mathscr R_3>0.
}
\]

Here

\[
F_3
=
\int P\,U\cdot\nabla|U|\,dY.
\]

To express this in DSD state/boundary language, use the velocity amplitude itself as the state coordinate.

Set

\[
a(Y,s):=|U(Y,s)|.
\]

---

## 2. Incompressible crossing balance on an amplitude level

For almost every regular value `lambda>0`, define the level surface

\[
\Sigma_\lambda
:=
\{Y:a(Y)=\lambda\}
\]

and orient it by

\[
n_\lambda
:=
\frac{\nabla a}{|\nabla a|},
\]

which points toward increasing velocity amplitude.

Since `div U=0`, the divergence theorem applied to the superlevel set `{a>lambda}` gives

\[
\boxed{
\int_{\Sigma_\lambda}
U\cdot n_\lambda\,dS
=0.
}
\]

Thus the positive and negative crossing fluxes have equal magnitude.

Define

\[
Q_\lambda
:=
\int_{\Sigma_\lambda\cap\{U\cdot n_\lambda>0\}}
U\cdot n_\lambda\,dS.
\]

Then

\[
Q_\lambda
=
\int_{\Sigma_\lambda\cap\{U\cdot n_\lambda<0\}}
(-U\cdot n_\lambda)\,dS.
\]

This is a purely kinematic consequence of incompressibility.

---

## 3. Pressure-weighted crossing flux

Define

\[
\boxed{
J_P(\lambda)
:=
\int_{\Sigma_\lambda}
P\,U\cdot n_\lambda\,dS.
}
\]

Because the unweighted crossing flux is zero, `J_P(lambda)` is invariant under

\[
P\mapsto P+c(s).
\]

When `Q_lambda>0`, define the flux-weighted pressures

\[
P_+(\lambda)
:=
\frac1{Q_\lambda}
\int_{U\cdot n_\lambda>0}
P(U\cdot n_\lambda)dS,
\]

and

\[
P_-(\lambda)
:=
\frac1{Q_\lambda}
\int_{U\cdot n_\lambda<0}
P(-U\cdot n_\lambda)dS.
\]

Then exactly

\[
\boxed{
J_P(\lambda)
=
Q_\lambda
\bigl(P_+(\lambda)-P_-(\lambda)\bigr).
}
\]

Hence positive `J_P` means that the up-crossing flux toward larger velocity amplitude carries a larger flux-weighted pressure than the balancing down-crossing flux.

This pressure difference, not either absolute pressure value, is the gauge-invariant DSD quantity.

---

## 4. Coarea decomposition of the global `p=3` work

Since

\[
F_3
=
\int P\,U\cdot\nabla a\,dY,
\]

coarea gives

\[
\boxed{
F_3
=
\int_0^{A_{max}}
J_P(\lambda)\,d\lambda,
}
\]

where `A_max` is a uniform amplitude ceiling on the compact W1 class.

Thus the global endpoint pressure loop is an integral over amplitude-state boundary cycles.

---

## 5. Coarea decomposition of `D3`

From

\[
D_3
=
2\int a|\nabla a|^2dY
+\int a^3|\nabla n|^2dY,
\qquad
n=U/a,
\]

coarea yields

\[
\boxed{
D_3
=
\int_0^{A_{max}}
\mathcal D_3(\lambda)d\lambda,
}
\]

with

\[
\boxed{
\mathcal D_3(\lambda)
:=
2\lambda
\int_{\Sigma_\lambda}|\nabla a|dS
+
\lambda^3
\int_{\Sigma_\lambda}
\frac{|\nabla n|^2}{|\nabla a|}dS.
}
\]

The formula is understood for regular levels, with the standard coarea interpretation across the negligible critical-value set.

---

## 6. Endpoint residue becomes a level-wise surplus

Average the global endpoint identity over the invariant measure:

\[
\int_0^{A_{max}}
\left[
\langle J_P(\lambda)\rangle_\mu
-
\nu\langle\mathcal D_3(\lambda)\rangle_\mu
\right]d\lambda
=
\frac{\mathscr R_3}{6}.
\]

Therefore there exists at least one regular amplitude level `lambda_*` for which

\[
\boxed{
\langle J_P(\lambda_*)\rangle_\mu
-
\nu\langle\mathcal D_3(\lambda_*)\rangle_\mu
\ge
\frac{\mathscr R_3}{6A_{max}}
}
\]

in the essential-supremum/pigeonhole sense; equivalently, a positive-measure set of levels carries positive surplus.

Thus one may choose a level with

\[
\boxed{
\left\langle
Q_{\lambda_*}
\Delta P_{\lambda_*}
\right\rangle_\mu
>
\nu\left\langle\mathcal D_3(\lambda_*)\right\rangle_\mu,
}
\]

where

\[
\Delta P_{\lambda_*}
:=P_+(\lambda_*)-P_-(\lambda_*).
\]

The strict excess contains the endpoint residue.

---

## 7. DSD interpretation: a closed amplitude-state cycle

At the selected amplitude level:

1. incompressibility requires equal volume flux toward higher and lower amplitude;
2. pressure is systematically larger on the up-crossing flux;
3. the resulting pressure-gap work exceeds the level-wise viscous `D3` cost by a fixed critical surplus.

Hence the W1 survivor must recurrently realize a **closed amplitude-state cycle**:

\[
\boxed{
\text{down-crossing at }a=\lambda_*
\to
\text{pressure-gap conversion}
\to
\text{up-crossing at }a=\lambda_*
\to
\text{critical viscous loss}
}
\]

with net `p=3` scale surplus.

This is not net mass transport across the amplitude boundary: the mass/volume crossing is exactly balanced. The nonzero quantity is the pressure-weighted work around that balanced crossing cycle.

---

## 8. Why pressure cannot be only a function of amplitude

For every sufficiently regular scalar function `G(a)`,

\[
\int G(a)\,U\cdot\nabla a\,dY
=
\int U\cdot\nabla H(a)dY
=0,
\]

where `H'=G`.

Therefore if

\[
P=G(a)+c(s)
\]

were a single-valued function of velocity amplitude alone, then

\[
F_3=0.
\]

Thus the W1 endpoint necessarily requires **pressure-amplitude hysteresis/non-single-valuedness**: equal-amplitude crossings must see different pressures depending on the crossing branch.

The level-set formula `J_P=Q_lambda Delta P_lambda` is the exact quantitative expression of this fact.

---

## 9. Updated frontier

The large weak-critical pressure loop is no longer merely an abstract integral correlation. It contains a fixed amplitude-state boundary on which a gauge-invariant pressure gap drives a balanced up/down crossing cycle with positive critical surplus.

A final closure theorem could therefore target the level-wise statement directly:

\[
\boxed{
Q_\lambda\Delta P_\lambda
\le
\nu\mathcal D_3(\lambda)
}
\]

for almost every amplitude level, or any averaged variant strong enough to force the integrated surplus to be nonpositive.

No such universal inequality is proved here; ordinary Navier--Stokes pressure redistribution may violate it at individual levels.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
