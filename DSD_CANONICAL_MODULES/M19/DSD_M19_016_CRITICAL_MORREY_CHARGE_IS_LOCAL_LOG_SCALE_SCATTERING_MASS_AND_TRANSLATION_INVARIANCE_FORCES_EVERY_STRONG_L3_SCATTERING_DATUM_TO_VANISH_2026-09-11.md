# M19-016 — Critical Morrey charge is local log-scale scattering mass, and translation invariance forces every strong-L3 scattering datum to vanish

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL SCATTERING REDUCTION / MORREY-DATUM IDENTITY / INTERNAL STRONG-L3 RIGIDITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-013--015 rewrites the quiet critical tail as a scale-invariant kinetic Morrey tail with a low-frequency/relative-frequency split.

The repository already contains a more refined tail representation on the passive spectator branch.

M5-567 proves the log-scale scattering form

\[
\boxed{
U_Y(r\omega,\theta)
=
\frac1r
A_Y\left(\log r-\frac\theta2,\omega\right)
+O_X(r^{-3})
}
\]

and the exact covariance

\[
\boxed{
A_{\sigma_tY}(q,\omega)
=
A_Y\left(q-\frac t2,\omega\right).
}
\]

M18-052 repairs the measurable-factor step: invariant hull measures push forward to invariant log-radius scattering measures without requiring strong global scattering continuity.

The present module calculates two consequences.

First, the kinetic Morrey tail is exactly a fixed-window local \(L^2\) mass of \(A\) in the log-radius coordinate.

Second, no nonzero translation-invariant probability measure can be supported on globally strong-\(L^3\) scattering data. Thus the genuinely recurrent critical tail must be weak-critical/non-\(L^3\).

## 2. Annular Morrey charge in scattering coordinates

Let

\[
q_R
:=
\log R-\frac\theta2.
\]

On the annulus

\[
R<r<2R,
\]

M5-567 gives

\[
U(r\omega,\theta)
=r^{-1}A(q_R+\log(r/R),\omega)+O(r^{-3}).
\]

Therefore

\[
|U|^2r^2
=
|A|^2+O(r^{-2}|A|)+O(r^{-4}).
\]

On the bounded scattering branch, \(A\) is bounded in the retained angular norm, so after radial/angular integration

\[
\begin{aligned}
\frac1R
\int_{R<|y|<2R}|U(y,\theta)|^2dy
&=
\frac1R
\int_R^{2R}
\int_{S^2}
|A(\log r-\theta/2,\omega)|^2d\omega\,dr\\
&\qquad+O(R^{-2}).
\end{aligned}
\]

Set

\[
r=Re^\eta,
\qquad
0\le\eta\le\log2.
\]

Then

\[
dr=Re^\eta d\eta.
\]

Hence

\[
\boxed{
\mathcal A_U(R,\theta)
=
\int_0^{\log2}
e^\eta
\|A(q_R+\eta,\cdot)\|_{L^2(S^2)}^2d\eta
+O(R^{-2}).
}
\]

Since

\[
1\le e^\eta\le2,
\]

this is uniformly equivalent to

\[
\boxed{
\int_{q_R}^{q_R+\log2}
\|A(q,\cdot)\|_{L^2(S^2)}^2dq.
}
\]

Thus a nonvanishing critical Morrey tail is precisely a nonvanishing local log-radius scattering mass.

## 3. Strong L3 is unweighted q-integrability

For the leading tail,

\[
|U|^3r^2drd\omega
=
r^{-1}|A(q,\omega)|^3drd\omega.
\]

Because

\[
dq=\frac{dr}{r},
\]

we obtain

\[
\boxed{
\int_{r>R}|U|^3dy
\sim
\int_{q>q_R}
\int_{S^2}|A(q,\omega)|^3d\omega\,dq
}
\]

up to the integrable \(O(r^{-3})\) remainder and cross terms.

Therefore the strong-\(L^3\) tail condition is exactly the unweighted log-radius condition

\[
\boxed{
A\in L^3(\mathbb R_q\times S^2)
}
\]

when the complete scattering datum is considered.

This is the structural reason the bounded nonzero critical datum is weak-critical rather than strong-critical.

## 4. Translation-invariant probability measures on Lp have only the zero finite-mass state

We use a general lemma.

Let

\[
1\le p<\infty
\]

and let \(\mu\) be a probability measure on

\[
L^p(\mathbb R\times S^2)
\]

that is invariant under translations

\[
(T_aA)(q,\omega)=A(q-a,\omega).
\]

For integer \(n\), define the local mass

\[
\boxed{
m_n(A)
:=
\int_n^{n+1}\int_{S^2}|A(q,\omega)|^pd\omega\,dq.
}
\]

For every fixed \(A\in L^p\),

\[
\sum_{n\in\mathbb Z}m_n(A)<\infty.
\]

Hence

\[
\boxed{m_n(A)\to0\quad(|n|\to\infty)}
\]

for every \(A\in L^p\).

But translation invariance of \(\mu\) implies that every \(m_n\) has the same probability law as \(m_0\).

Since

\[
m_n\to0
\]

pointwise \(\mu\)-almost surely, it also converges to zero in probability. A sequence with a fixed law that converges in probability to zero must have that law equal to \(\delta_0\).

Thus

\[
\boxed{
m_0=0\quad\mu\text{-a.s.}}
\]

and by translation,

\[
m_n=0
\]

for every integer \(n\), almost surely.

Therefore

\[
\boxed{A=0\quad\mu\text{-a.s.}}
\]

This proves:

\[
\boxed{
\text{the only translation-invariant probability measure supported on }L^p(\mathbb R\times S^2)
\text{ is concentrated at }0.
}
\]

## 5. Apply the lemma to the scattering factor

M18-052 gives an invariant probability measure \(\mu_A\) on the scattering data under the translation action

\[
A(q)\mapsto A(q-t/2).
\]

Suppose the critical-tail factor were supported on strong-\(L^3\) data:

\[
A\in L^3(\mathbb R\times S^2)
\qquad\mu_A\text{-a.s.}
\]

Then Section 4 with \(p=3\) gives

\[
\boxed{
A=0
\qquad\mu_A\text{-a.s.}
}
\]

Therefore a nontrivial invariant recurrent scattering factor cannot live in global strong \(L^3\).

## 6. Consequence for the critical Morrey tail

If

\[
A=0,
\]

then M5-567 reconstruction gives

\[
U(y,\theta)=O(|y|^{-3})
\]

in the retained scattering norm.

Consequently

\[
\mathcal A_U(R,\theta)\to0
\qquad(R\to\infty).
\]

Thus a nonzero recurrent critical Morrey tail requires

\[
\boxed{
A\notin L^3(\mathbb R_q\times S^2)
}
\]

on the nontrivial invariant scattering component.

The strong-\(L^3\) scattering branch is closed internally at the invariant-measure level.

## 7. Why this is stronger than periodic-only reasoning

Exact self-similarity gives constant \(A(q)\).

DSS gives periodic \(A(q)\).

Both nonzero cases are visibly non-\(L^3\) in \(q\).

Section 4 does not require periodicity. It applies equally to an aperiodic invariant recurrent scattering measure.

Thus the same conclusion holds for the full recurrent translation class:

\[
\boxed{
\text{nonzero recurrent scattering datum}
\Longrightarrow
\text{nonintegrable log-radius critical mass}.
}
\]

## 8. Relation to M19-015

M19-015 uses a global Fourier split and therefore requires a localization firewall before interpreting low-frequency mass as local ancestry.

The scattering representation bypasses part of that ambiguity on the passive spectator branch: the critical spatial tail is encoded directly by the local \(q\)-window mass of \(A\).

Thus on the spectator branch the better critical variable is

\[
\boxed{
q\mapsto A(q,\omega)
}
\]

rather than a global Fourier cutoff alone.

## 9. Remaining weak-critical branch

Translation-invariant nonzero bounded data such as periodic or stationary-random-like functions are perfectly compatible with

\[
A\notin L^3(\mathbb R_q\times S^2).
\]

Therefore the lemma does not close the genuine weak-critical tail.

The remaining root is now sharpened to

\[
\boxed{
G_{weak\ critical\ scattering}
:
\mu_A\text{ is translation invariant, nontrivial, and supported outside global }L^3_q.
}
\]

## 10. Conditional CE-H harmonic subbranch

On the additional coefficient-compact CE-H exterior-line hypotheses of M17-349, the exterior vorticity becomes harmonic or exits through bounded/winding tail topology.

M17-350 then reduces the harmonic weak-critical obstruction to the toroidal \(r^{-2}\) vorticity dipole coefficient

\[
\boxed{a\in\mathbb R^3.}
\]

This is a much smaller conditional subbranch, but those CE-H hypotheses are not imposed on the whole upstream R-critical root.

M19 must therefore keep the general scattering branch and the conditional CE-H dipole branch distinct.

## 11. Next calculation

The new general target is the nonintegrable recurrent scattering datum.

M19-017 should use the translation-invariant measure to quantify the density of log-radius windows on which

\[
\int_{q}^{q+\log2}\|A(s)\|_2^2ds
\]

has a fixed positive lower bound.

This will convert `nonzero recurrent weak-critical tail` into a positive-density stack of physical critical Morrey annuli.

The calculation must then check whether that positive log-density changes the summability conclusion of M19-014 or merely reproduces the same geometrically summable physical energy stack.

---

\[
\boxed{\text{M19-016 COMPLETE; STRONG-L3 RECURRENT SCATTERING IS CLOSED, WEAK-CRITICAL TRANSLATION DYNAMICS REMAINS.}}
\]
