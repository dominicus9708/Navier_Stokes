# DSD M19-343 — Parent-length positive-flux geometry already forces 1/R amplitude dilution, so the M19-342 line-length escape is baseline rather than a pathology

Date: 2026-09-16  
Canonical ID: **M19-343**

Status: **ACTIVE SCOPE CORRECTION / PARENT-LENGTH BASELINE / LONGITUDINAL COERCIVITY FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-342 proves a valid conditional statement: at fixed tube enstrophy and positive flux, cross-sectional flux-weighted amplitude collapse inside a uniformly bounded-length tube forces longitudinal palinstrophy unless amplitude/line geometry decompactifies.

The canonical late-M17 productive branch, however, is not uniformly bounded in normalized line length.

M17-450 already proves that the retained coherent positive-flux loop has parent-length geometry

\[
\boxed{
\ell_R\ge c_\ell R.
}
\]

Therefore the line-length exit in M19-342 must be audited against the actual canonical geometry before it is treated as a pathological survivor.

## 2. M17-450 baseline

On a fixed normalized record-time window, M17-450 has a uniform enstrophy upper bound

\[
\|\Omega_R\|_2^2\le E_I,
\]

a positive flux floor

\[
\Phi_R\ge\Phi_*>0,
\]

and a coherent parent-length loop

\[
\ell_R\ge c_\ell R.
\]

For the cross-sectional quadratic currency

\[
Q_R(z)=\int_{A_z}|\Omega_R|^2dA
\]

and flux-weighted normalized amplitude

\[
\mathfrak a_\Phi(z)=\frac{Q_R(z)}{\Phi_R},
\]

M17-450 gives

\[
\boxed{
\overline{\mathfrak a}_{\Phi,R}
:=
\frac1{\ell_R}
\int_{\Gamma_R}\mathfrak a_\Phi(z)dz
\lesssim
\frac{E_I}{\Phi_R\ell_R}
\lesssim
\frac{C}{R}.
}
\]

Thus record-linear longitudinal extent automatically produces record-inverse mean flux-weighted amplitude.

## 3. Transverse broadening is also baseline

M17-450 further proves the harmonic-mean area bound

\[
\boxed{
\mathfrak A_{H,R}\gtrsim R,
}
\]

and hence a transverse participation radius

\[
\boxed{
\Lambda_{\perp,H}(R)\gtrsim R^{1/2}.
}
\]

Therefore the diffuse mesoscopic carrier naturally combines

\[
\boxed{
\text{longitudinal length }\sim R
+
\text{transverse area }\gtrsim R
+
\text{mean flux-amplitude }\lesssim R^{-1}.
}
\]

This is not, by itself, a thin-neck or high-jet pathology.

## 4. Consequence for M19-342

M19-342 assumes a uniform line-length ceiling

\[
\ell_\lambda\le L_*.
\]

That hypothesis fails on the canonical parent-length branch when the represented line segments inherit the M17-450 geometry.

Therefore

\[
\boxed{
\text{M19-342 longitudinal coercivity}
\not\Rightarrow
\text{closure of the M17-450 parent-length survivor}.
}
\]

Instead M19-342 should be read as a localization theorem: if a substantial fixed-enstrophy productive subcarrier can be confined to uniformly bounded normalized line length, then cross-sectional amplitude collapse forces palinstrophy. The full parent-length carrier can avoid that conclusion through its certified longitudinal extent.

## 5. Compatibility with M17-441 summability

M17-441 requires, on retained positive-flux/good-time geometric records,

\[
\sum_m\mathfrak a_{\Phi,m}<\infty.
\]

For geometric records

\[
R_m\asymp q^m,
\qquad q>1,
\]

the M17-450 baseline

\[
\mathfrak a_{\Phi,m}\sim R_m^{-1}
\]

is already summable:

\[
\boxed{
\sum_mR_m^{-1}<\infty.
}
\]

Thus the raw-H2 ancestry requirement does **not** force amplitude decay faster than the natural parent-length diffuse baseline.

This is an important correction to any reading that treats sign-wide amplitude collapse itself as exceptional.

## 6. Fixed tube-enstrophy lower bound gives the matching scale under length comparability

Suppose in addition a represented tube has

\[
E_{\mathcal T,R}\ge e_*>0,
\]

\[
\Phi_R\le\Phi^*<\infty,
\]

and its length is also bounded above by

\[
\ell_R\le C_\ell R.
\]

Then the loop-average identity

\[
E_{\mathcal T,R}
=\Phi_R
\int_{\Gamma_R}\mathfrak a_\Phi(z)dz
\]

up to the retained chart-comparability constants gives

\[
\boxed{
\overline{\mathfrak a}_{\Phi,R}
\gtrsim
\frac{c}{R}.
}
\]

Combined with M17-450,

\[
\boxed{
\overline{\mathfrak a}_{\Phi,R}
\asymp
R^{-1}
}
\]

on a fixed-enstrophy, positive-flux, length-comparable diffuse tube.

Hence \(R^{-1}\) is the natural baseline amplitude scale for this geometry.

## 7. New quantity: excess dilution relative to the diffuse baseline

Define the baseline-renormalized amplitude

\[
\boxed{
\mathfrak b_{\Phi,R}
:=
R\,\overline{\mathfrak a}_{\Phi,R}.
}
\]

On the M17-450 minimal diffuse geometry, \(\mathfrak b_{\Phi,R}=O(1)\).

If the represented tube also retains an order-one enstrophy fraction and length \(\asymp R\), then \(\mathfrak b_{\Phi,R}\) is bounded below as well.

Therefore the genuinely new dilution branch is not

\[
\mathfrak a_\Phi\to0,
\]

which is baseline, but rather

\[
\boxed{
\mathfrak b_{\Phi,R}=R\overline{\mathfrak a}_{\Phi,R}\to0,
}
\]

or failure of the fixed-enstrophy/length-comparability incidence needed to prevent it.

## 8. Sign-resolved consequence

M19-338 showed that if both coefficient signs retain positive flux fractions, both sign-resolved amplitudes must collapse.

M19-343 now corrects the interpretation: a collapse of order \(R^{-1}\) is already compatible with the canonical diffuse geometry.

The next useful question is whether the positive and negative sign populations can both realize the same baseline scale

\[
\mathfrak a_{\pm,R}\asymp R^{-1}
\]

while preserving:

1. the M17-458 near-perfect first-moment sign cancellation;
2. M19-321--323 coefficient variance / line-label heterogeneity;
3. productive persistent material-flux recurrence.

Any additional sign-dependent collapse beyond \(R^{-1}\) should be recorded through

\[
R\mathfrak a_{\pm,R}.
\]

## 9. Updated survivor

The canonical mixed-sign diffuse branch is therefore

\[
\boxed{
\begin{aligned}
H_{\rm parent\text{-}length\ mixed\text{-}sign\ diffuse}
\Longrightarrow{}&
H_{\mathfrak a_\pm\sim R^{-1}\ baseline}\\
&\lor G_{\rm excess\ sign\text{-}dependent\ amplitude\ dilution}\\
&\lor G_{\rm tube\ enstrophy\ incidence\ loss}\\
&\lor G_{\rm super\text{-}parent\ line\ residence/length}\\
&\lor G_{\rm transverse\ shape/Poincare\ degeneration}\\
&\lor G_{\rm time/chart/genealogy/interface\ loss}.
\end{aligned}
}
\]

## 10. Audit verdict

**PASS AS A SCOPE CORRECTION — the parent-length line-residence escape of M19-342 is already the certified M17-450 baseline.**

Record-inverse flux-weighted amplitude dilution is natural and ancestry-summable. The new quantitative target is the baseline-renormalized sign-resolved amplitude \(R\mathfrak a_\pm\), together with carrier-to-productive-tube enstrophy incidence and any excess longitudinal/transverse dilution beyond the M17-450 geometry.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
