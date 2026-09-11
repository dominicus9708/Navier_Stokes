# M19-065 — Time-averaged A2 contraction only needs a mean gap, but existing enstrophy/palinstrophy bounds give size control rather than automatic smallness

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / TIME-AVERAGED GAP FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-064 reduced strict contraction in a pressure-compatible \(A_2\) weight to a quantitative pointwise inequality

\[
\Lambda_{NL}(\theta)<c_{gap}.
\]

Pointwise strain smallness is stronger than one should expect on a recurrent nonlinear flow.  This module asks whether a positive **time-averaged** gap is enough, and whether the already certified enstrophy/palinstrophy bounds force such an average gap.

The first answer is yes: a uniform positive mean gap implies exponential contraction and collapses the recurrent hull.

The second answer is no with the current estimates: the similarity enstrophy identity gives a uniform long-time bound on mean palinstrophy and hence on mean \(L^3\) strain, but not the strict smallness needed to beat \(c_{gap}\).

## 2. Time-dependent nonlinear coefficient

From M19-064, after absorbing half of the weighted gradient term, one may write schematically

\[
\boxed{
\frac12E_w'
+\frac\nu2G_w
+
\left[c_{gap}-\Lambda_{NL}(\theta)\right]E_w
\le0,
}
\]

where one admissible coefficient is

\[
\boxed{
\begin{aligned}
\Lambda_{NL}(\theta)
:=
&\left(\frac12+2C_{CZ}(a)\right)L_wM_U(\theta)\\
&+C_1\nu^{-1}\|S_V(\theta)\|_3^2
+C_2L_w\|S_V(\theta)\|_3.
\end{aligned}
}
\]

The exact constants are not important for the structural argument; their signs and scaling are.

## 3. Mean-gap contraction theorem

Dropping the nonnegative \(G_w\) term,

\[
\frac{d}{d\theta}\log E_w
\le
-2c_{gap}+2\Lambda_{NL}(\theta)
\]

whenever \(E_w>0\).

Hence

\[
\boxed{
E_w(T)
\le
E_w(0)
\exp\left(
-2c_{gap}T
+2\int_0^T\Lambda_{NL}(\theta)d\theta
\right).
}
\]

Therefore if there exists \(\varepsilon>0\) such that uniformly over all trajectory pairs in the retained hull,

\[
\boxed{
\limsup_{T\to\infty}
\frac1T
\int_0^T\Lambda_{NL}(\theta)d\theta
\le
c_{gap}-\varepsilon,
}
\]

then

\[
\boxed{E_w(T)\lesssim e^{-2\varepsilon T}E_w(0).}
\]

Surjectivity of time translation on a compact complete invariant hull again forces zero diameter.  Thus a strict **mean** gap is enough; pointwise nonlinear smallness is unnecessary.

## 4. Similarity enstrophy identity

Let

\[
Z(\theta):=\|\Omega(\theta)\|_2^2,
\qquad
P(\theta):=\|\nabla\Omega(\theta)\|_2^2.
\]

The similarity vorticity equation gives

\[
\boxed{
\frac12Z'
+\frac14Z
+\nu P
=
\int\Omega\cdot S\Omega\,dy.
}
\]

The \(\frac14Z\) coefficient comes from

\[
\int\Omega\cdot
\left(
\Omega+\frac12y\cdot\nabla\Omega
\right)dy
=\frac14Z.
\]

## 5. Stretching is bounded by vorticity amplitude times enstrophy

Calderon--Zygmund and Holder give

\[
\left|
\int\Omega\cdot S\Omega
\right|
\le
\|S\|_3\|\Omega\|_3^2
\lesssim
\|\Omega\|_3^3.
\]

Since

\[
\|\Omega\|_3^3
\le
\|\Omega\|_\infty\|\Omega\|_2^2,
\]

if

\[
\|\Omega\|_\infty\le M_\Omega,
\qquad
Z\le Z_*,
\]

then

\[
\boxed{
\left|
\int\Omega\cdot S\Omega
\right|
\le
C M_\Omega Z.
}
\]

Consequently

\[
\nu P
\le
CM_\Omega Z
-\frac14Z
-\frac12Z'.
\]

## 6. Long-time mean palinstrophy is bounded, not forced small

Integrating from \(0\) to \(T\),

\[
\nu\int_0^TPd\theta
\le
CM_\Omega\int_0^TZd\theta
-\frac14\int_0^TZd\theta
+\frac12\bigl[Z(0)-Z(T)\bigr].
\]

Using \(0\le Z\le Z_*\),

\[
\boxed{
\limsup_{T\to\infty}
\frac1T\int_0^TPd\theta
\le
C\nu^{-1}M_\Omega Z_*.
}
\]

This is useful size control, but the right side is not forced to be small.

## 7. Mean L3 strain bound

Sobolev and interpolation give

\[
\|S\|_3
\lesssim
\|\Omega\|_3,
\]

and

\[
\|\Omega\|_3^2
\le
\|\Omega\|_2\|\Omega\|_6
\lesssim
Z^{1/2}P^{1/2}.
\]

Therefore

\[
\boxed{
\|S\|_3^2
\lesssim
Z_*^{1/2}P^{1/2}.
}
\]

Averaging and using Cauchy--Schwarz,

\[
\frac1T\int_0^T\|S\|_3^2d\theta
\lesssim
Z_*^{1/2}
\left(
\frac1T\int_0^TPd\theta
\right)^{1/2}.
\]

Hence

\[
\boxed{
\limsup_{T\to\infty}
\frac1T\int_0^T\|S\|_3^2d\theta
\le
C M_\Omega^{1/2}Z_*\nu^{-1/2}.
}
\]

Similarly,

\[
\boxed{
\limsup_{T\to\infty}
\frac1T\int_0^T\|S\|_3d\theta
\le
C M_\Omega^{1/4}Z_*^{1/2}\nu^{-1/4}.
}
\]

Again these are boundedness estimates, not vanishing estimates.

## 8. Resulting average nonlinear bound

The velocity bound from M19-064 is

\[
M_U\lesssim M_\Omega^{1/3}Z_*^{1/3}.
\]

Thus the current estimates yield a finite explicit upper bound of the schematic form

\[
\boxed{
\begin{aligned}
\overline\Lambda_{NL}
\lesssim{}&
L_w M_\Omega^{1/3}Z_*^{1/3}\\
&+
M_\Omega^{1/2}Z_*\nu^{-3/2}\\
&+
L_wM_\Omega^{1/4}Z_*^{1/2}\nu^{-1/4}.
\end{aligned}
}
\]

The exact universal constants depend on the Sobolev/CZ estimates and on \(a\).

Nothing in the current bounded corridor forces this quantity below \(c_{gap}\).

## 9. Why the old physical-time ledgers cannot be silently substituted

Several earlier ancestry modules contain finite physical-time or annular palinstrophy/H2/D3 ledgers.  Those statements have specific scaling weights and nonreuse hypotheses.

The present requirement is instead a forward similarity-time Cesaro average along one complete recurrent hull trajectory:

\[
\frac1T\int_0^T\|S(\theta)\|_3^2d\theta.
\]

These are not the same object.

Therefore one must not infer the needed mean smallness from ancestry summability merely because both involve derivative resources.

This preserves the established ancestry/provenance firewall.

## 10. Updated factor-rigidity frontier

M19-065 narrows the gap as follows.

### Sufficient closure theorem

\[
\boxed{
\overline\Lambda_{NL}<c_{gap}
\Longrightarrow
\text{strict mean contraction}
\Longrightarrow
\mathcal H\text{ is a singleton}
\Longrightarrow
\text{no aperiodic scattering factor}.}
\]

### What current budgets provide

\[
\boxed{
\overline\Lambda_{NL}<\infty
}
\]

with an explicit bound, but not the strict inequality needed for closure.

Thus the obstruction is no longer lack of a contraction framework.  It is the absence of a mechanism forcing **sub-gap average strain/transport size** on the retained recurrent branch.

## 11. Certified / not certified

### Certified

1. A strict positive long-time mean gap suffices for global factor rigidity.
2. Similarity enstrophy obeys the displayed exact balance.
3. Bounded normalized vorticity amplitude/enstrophy give a finite mean palinstrophy bound.
4. They give finite mean \(L^3\)-strain and squared-strain bounds.
5. Existing estimates do not force those means below the \(A_2\) spectral gap.

### Not certified

1. Mean-gap smallness on the retained recurrent hull.
2. Conversion of ancestry ledgers into the required Cesaro average.
3. Global factor rigidity in the large recurrent corridor.
4. Global 3D Navier--Stokes regularity.

## 12. Next calculation

The next question is whether the similarity enstrophy identity has enough **signed recurrence information** to improve boundedness into smallness.

On a recurrent invariant measure, the average of \(Z'\) vanishes, so formally

\[
\nu\langle P\rangle
+\frac14\langle Z\rangle
=
\left\langle\int\Omega\cdot S\Omega\right\rangle.
\]

M19-066 should combine this with the already developed CE-H / strain-segregation structure and ask whether a nontrivial recurrent state necessarily pays a positive excess that is incompatible with the contraction threshold, or conversely whether an explicit balanced recurrent scaling model shows that the average identity can saturate without smallness.

The latter would close the average-contraction shortcut as another conditional route and return the frontier to a genuinely nonlinear recurrent-hull rigidity theorem.

---

\[
\boxed{\text{M19-065 COMPLETE; TIME AVERAGING RELAXES POINTWISE SMALLNESS BUT CURRENT LEDGERS DO NOT FORCE A SUB-GAP MEAN.}}
\]
