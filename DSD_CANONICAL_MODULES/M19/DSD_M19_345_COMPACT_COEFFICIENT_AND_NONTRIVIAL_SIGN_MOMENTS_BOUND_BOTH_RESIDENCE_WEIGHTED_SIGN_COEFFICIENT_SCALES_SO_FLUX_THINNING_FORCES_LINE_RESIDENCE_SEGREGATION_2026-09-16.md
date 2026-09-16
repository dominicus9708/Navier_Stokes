# DSD M19-345 — Compact coefficient bounds and nontrivial sign moments bound both residence-weighted sign coefficient scales, so sign-flux thinning forces line-residence segregation

Date: 2026-09-16  
Canonical ID: **M19-345**

Status: **ACTIVE SIGN-SCALE COMPACTNESS / FLUX-THINNING REDUCTION / RESIDENCE-SEGREGATION ESCALATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-344

M19-344 factors the positive and negative weighted coefficient moments as

\[
K_+
=\Phi_+\bar L_+\bar\kappa_{+,L},
\]

\[
K_-
=\Phi_-\bar L_-\bar\kappa_{-,L},
\]

and hence

\[
\frac{K_+}{K_-}
=
\frac{\eta_+}{\eta_-}
\frac{\bar L_+}{\bar L_-}
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}.
\]

On the M17-458 good-time survivor,

\[
K_-/K_+\to1
\]

and the sign moments remain nontrivial.

M19-344 therefore left two possible compensators for sign-flux thinning: line-residence concentration or sign-dependent coefficient-scale escalation.

The present module removes the latter on the compact coefficient branch.

## 2. Sign enstrophy masses

Define the sign-resolved enstrophy masses in line coordinates

\[
\boxed{
E_+
:=\int_{S_+}L_1d\nu,
\qquad
E_-
:=\int_{S_-}L_1d\nu.
}
\]

Then exactly

\[
K_+=E_+\bar\kappa_{+,L},
\]

\[
K_-=E_-\bar\kappa_{-,L}.
\]

Assume the retained record has the uniform enstrophy ceiling

\[
\boxed{E_++E_-\le E_*<\infty.}
\]

This is part of the Type-I / compact record package on the late retained normalized windows.

## 3. Compact coefficient ceiling

On the compact exact CE-H coefficient branch assume

\[
\boxed{|\kappa|\le K_*<\infty.}
\]

Then by definition of the residence-weighted means,

\[
\boxed{
\bar\kappa_{+,L}\le K_*,
\qquad
\bar\kappa_{-,L}\le K_*.
}
\]

No sign population can compensate vanishing flux by sending its mean coefficient magnitude to infinity while this compactness survives.

## 4. Nontrivial sign moments give coefficient lower bounds

Assume on the M17-458 good-time branch

\[
\boxed{K_+\ge k_*>0.}
\]

Since

\[
K_-=K_++P\ge K_+,
\]

we also have

\[
K_-\ge k_*.
\]

Because

\[
E_\pm\le E_++E_-\le E_*,
\]

we obtain

\[
\boxed{
\bar\kappa_{+,L}
=\frac{K_+}{E_+}
\ge
\frac{k_*}{E_*},
}
\]

and

\[
\boxed{
\bar\kappa_{-,L}
=\frac{K_-}{E_-}
\ge
\frac{k_*}{E_*}.
}
\]

Thus

\[
\boxed{
\frac{k_*}{E_*}
\le
\bar\kappa_{\pm,L}
\le
K_*.
}
\]

## 5. Uniform comparability of the two sign coefficient scales

The previous bounds give

\[
\boxed{
\frac{k_*}{E_*K_*}
\le
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}
\le
\frac{E_*K_*}{k_*}.
}
\]

Hence the residence-weighted coefficient-scale ratio is uniformly compact.

The M19-344 coefficient-escalation escape is unavailable unless at least one of the retained coefficient/enstrophy/sign-moment hypotheses fails.

## 6. Near-perfect cancellation now ties flux fraction directly to residence

M19-344 gives

\[
\frac{\eta_+}{\eta_-}
\frac{\bar L_+}{\bar L_-}
\frac{\bar\kappa_{+,L}}{\bar\kappa_{-,L}}
\to1.
\]

Since the coefficient ratio is bounded above and below by fixed constants, there exist fixed \(c,C>0\) such that for sufficiently late good times

\[
\boxed{
c
\lesssim
\frac{\eta_+}{\eta_-}
\frac{\bar L_+}{\bar L_-}
\lesssim
C.
}
\]

Therefore

\[
\boxed{
\eta_+/\eta_-\to0
\Longrightarrow
\bar L_+/\bar L_-\to\infty
}
\]

up to fixed comparability constants.

Likewise

\[
\boxed{
\eta_-/\eta_+\to0
\Longrightarrow
\bar L_-/\bar L_+\to\infty.
}
\]

Thus sign-flux thinning is equivalent, on the compact cancellation branch, to sign-specific line-residence segregation.

## 7. If residence ratios are compact, both sign flux fractions survive

Assume additionally

\[
0<c_L
\le
\frac{\bar L_+}{\bar L_-}
\le
C_L<\infty.
\]

Then

\[
0<c_\eta
\le
\frac{\eta_+}{\eta_-}
\le
C_\eta<\infty.
\]

If the zero-level flux fraction is negligible or separately controlled, both \(\eta_+\) and \(\eta_-\) are bounded below.

M19-338 then forces simultaneous sign-resolved amplitude collapse,

\[
\sum_m\mathfrak a_{+,m}<\infty,
\qquad
\sum_m\mathfrak a_{-,m}<\infty.
\]

M19-343 corrects its natural scale to the parent-length baseline \(\mathfrak a_\pm\sim R^{-1}\).

## 8. Relation to M19-321--323

M19-321--323 give a fixed coefficient-variance gap and transverse line-label heterogeneity. M19-345 does not use that variance to obtain the coefficient upper/lower bounds; the latter already follow from compact \(|\kappa|\), nontrivial \(K_\pm\), and bounded total enstrophy.

The spectral/coefficient variance remains useful for preventing collapse to one coefficient value and for quantifying the coexistence of distinct line populations.

The present result is complementary: it says that **the two sign populations cannot trade arbitrarily in coefficient magnitude to preserve the M17-458 cancellation law.**

## 9. Updated spatial survivor

On the retained compact mixed-sign good-time branch,

\[
\boxed{
G_{\rm sign\ flux\ thinning}
\Longrightarrow
G_{\rm sign\text{-}specific\ line\text{-}residence\ segregation}
}
\]

unless one loses:

\[
G_{\rm coefficient\ compactness}
\lor
G_{\rm sign\text{-}moment\ floor}
\lor
G_{\rm enstrophy\ ceiling}
\lor
G_{\rm representation/genealogy}.
\]

Thus line residence is promoted from one possible incidence defect to the principal compensator for sign-flux imbalance.

## 10. Audit verdict

**PASS — coefficient-scale escalation is removed as a compensator for sign-flux thinning on the compact nontrivial sign-moment branch.**

The current preferred spatial target is now line-residence segregation itself: determine whether \(\bar L_+/\bar L_-\to\infty\) can coexist with parent-length diffuse geometry, fixed spectral width, positive-flux recurrence, and the finite palinstrophy/raw-H2 ancestry ledgers without forcing longitudinal amplitude gradients, extra length, or time/genealogy loss.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
