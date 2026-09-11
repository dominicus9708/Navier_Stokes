# M19-015 — Critical Morrey tail splits into infrared H^{-1} mass or large relative frequency

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL SPECTRAL SPLIT / LOW-FREQUENCY IDENTIFICATION / HIGH-FREQUENCY ROUTING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-013--014 reduces the critical-tail root to a physical/normalized kinetic Morrey charge and proves that standard energy summation does not exclude it.

The next question is spectral.

For a divergence-free normalized state,

\[
\|U\|_2^2
=
\|\Omega\|_{\dot H^{-1}}^2.
\]

A large-radius critical tail can therefore arise from genuinely low normalized frequencies or from oscillation at frequencies high relative to the radius.

The present module makes this dichotomy quantitative.

## 2. Critical annular energy assumption

Let

\[
A_R:=\{R<|y|<2R\}.
\]

Assume

\[
\boxed{
\int_{A_R}|U(y)|^2dy
\ge a_*R
}
\]

for some \(a_*>0\).

This is the annular form of the critical Morrey tail.

## 3. Frequency decomposition at the geometric scale

Fix a dimensionless frequency threshold

\[
A>1.
\]

Let

\[
\lambda_R:=\frac{A}{R}.
\]

Use a standard Littlewood--Paley split

\[
U=U_{lo}+U_{hi},
\]

with

\[
U_{lo}:=P_{\le\lambda_R}U,
\qquad
U_{hi}:=P_{>\lambda_R}U.
\]

Then on the annulus,

\[
|U|^2
\le
2|U_{lo}|^2+2|U_{hi}|^2.
\]

Therefore at least one of

\[
\boxed{
\int_{A_R}|U_{lo}|^2dy
\ge
\frac{a_*}{4}R
}
\]

or

\[
\boxed{
\int_{A_R}|U_{hi}|^2dy
\ge
\frac{a_*}{4}R
}
\]

must hold.

## 4. Low-frequency branch gives an H^{-1} floor

For divergence-free \(U\) with

\[
\Omega=\nabla\times U,
\]

the Fourier identity is

\[
\widehat U(\xi)
=
\frac{i\xi\times\widehat\Omega(\xi)}{|\xi|^2}.
\]

Since \(\xi\cdot\widehat\Omega=0\),

\[
|\widehat U(\xi)|^2
=
\frac{|\widehat\Omega(\xi)|^2}{|\xi|^2}.
\]

Hence

\[
\boxed{
\|P_{\le\lambda}U\|_2^2
=
\int_{|\xi|\lesssim\lambda}
\frac{|\widehat\Omega(\xi)|^2}{|\xi|^2}d\xi
}
\]

up to the harmless smooth cutoff constants.

If the low branch of Section 3 occurs, then its global norm is at least its annular norm, so

\[
\boxed{
\int_{|\xi|\lesssim A/R}
\frac{|\widehat\Omega(\xi)|^2}{|\xi|^2}d\xi
\ge
c a_*R.
}
\]

Thus the critical spatial tail forces a linearly growing amount of normalized infrared \(\dot H^{-1}\) mass unless the high-frequency branch carries a fixed fraction of the annular energy.

## 5. High-frequency branch gives a relative-frequency floor

If instead

\[
\int_{A_R}|U_{hi}|^2dy
\ge
\frac{a_*}{4}R,
\]

then globally

\[
\|U_{hi}\|_2^2
\ge
\frac{a_*}{4}R.
\]

By Fourier support,

\[
\|\nabla U_{hi}\|_2^2
\ge
\lambda_R^2\|U_{hi}\|_2^2.
\]

Therefore

\[
\|\nabla U_{hi}\|_2^2
\ge
\frac{A^2}{R^2}\frac{a_*}{4}R
=
\frac{a_*A^2}{4R}.
\]

Equivalently,

\[
\boxed{
R\|\nabla U_{hi}\|_2^2
\ge
c a_*A^2.
}
\]

Thus for arbitrarily large \(A\), failure of the infrared branch forces arbitrarily large derivative content relative to the geometric scale \(R\).

This is the spectral form of high relative frequency.

## 6. Localization firewall

The estimate above uses a global Littlewood--Paley projection and an annular observation.

Therefore one must not automatically identify

\[
R\|\nabla U_{hi}\|_2^2
\]

with a fully localized remote-shell frequency without checking commutators/cutoffs.

On the controlled localization branch used by the earlier high-shell-frequency audit, the two are comparable up to fixed cutoff errors.

If that localization comparability fails, record

\[
\boxed{G_{frequency/localization\ defect}.}
\]

rather than silently routing the term.

## 7. No-remote/high-frequency branch

M18 routes sufficiently high relative shell frequency to the remote/high-frequency complex or a localization/boundary exit.

Therefore on the retained **no-remote, controlled-localization** critical branch, choose \(A\) above the allowed relative-frequency ceiling.

Then the high-frequency alternative is excluded, and every sufficiently large critical annulus must satisfy

\[
\boxed{
\int_{|\xi|\lesssim A/R}
\frac{|\widehat\Omega(\xi)|^2}{|\xi|^2}d\xi
\gtrsim
R.
}
\]

Thus

\[
\boxed{
\text{controlled critical tail}
\Longrightarrow
\text{infrared }\dot H^{-1}\text{ accumulation}
}
\]

modulo the already separated remote/high-frequency and localization exits.

## 8. Relation to physical kinetic energy

The identity

\[
\|U\|_2^2
=
\|\Omega\|_{\dot H^{-1}}^2
\]

means that the infrared mass is not a new independent resource. It is precisely the low-frequency representation of kinetic energy.

Under blowup rescaling,

\[
\|U_j\|_2^2
=
r_j^{-1}\|u(t_j)\|_2^2,
\]

so the normalized global \(H^{-1}\) budget can grow like \(r_j^{-1}\) even while the physical kinetic energy stays finite.

Therefore the infrared lower bound itself is not a contradiction.

## 9. Critical-tail recompression

The R-critical tail now satisfies

\[
\boxed{
G_{critical\ Morrey\ tail}
\Longrightarrow
G_{infrared\ H^{-1}}
\lor
G_{high\ relative\ frequency}
\lor
G_{frequency/localization\ defect}.
}
\]

The second branch rejoins R-remote/high-frequency.

Hence the genuinely retained quiet critical branch is an infrared/low-frequency problem.

## 10. Next calculation

The next target is low-frequency inheritance across blowup rescalings.

M19-016 should compare the normalized infrared mass

\[
\int_{|\xi|\lesssim A/R}
\frac{|\widehat\Omega_j|^2}{|\xi|^2}d\xi
\]

with the physical parent energy at radii \(\ell=r_jR\).

The objective is to determine whether infrared accumulation can be converted into a nonzero terminal defect measure, a scale-critical Morrey trace, or merely another geometrically summable redistribution of the finite kinetic-energy budget.

---

\[
\boxed{\text{M19-015 COMPLETE; QUIET R-CRITICAL IS REDUCED TO INFRARED H^{-1} INHERITANCE.}}
\]
