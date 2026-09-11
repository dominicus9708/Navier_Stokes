# M18-062 — Multi-p recurrence forces exact positive amplitude covariance of sigma+kappa and a fixed growth-field oscillation

**Date:** 2026-09-11  
**Status:** EXACT MULTI-MOMENT SEGREGATION IDENTITY / AMPLITUDE-GROWTH COVARIANCE / COHERENT-BASELINE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-061 leaves a possible quiet recurrent picture in which aligned strain remains close to the appropriate amplitude-dependent similarity baseline and avoids large derivative payments.

The baseline, however, depends on \(p\):

\[
c_p=1-\frac{3}{2p}.
\]

One scalar field cannot independently equal all of these values on the same statistical population.

The present module compares two amplitude moments and derives an exact invariant covariance law. The conclusion is that a nontrivial recurrent CE-H state must segregate its net amplitude-growth field

\[
\boxed{h:=\sigma+\kappa}
\]

by vorticity amplitude: higher-amplitude populations have strictly larger mean \(h\).

## 2. Joint invariant amplitude-weighted measures

Let \(\mu\) be the invariant probability measure on the recurrent compact CE-H hull.

For each finite \(p\ge2\), define

\[
M_p(Y):=\int_{\mathbb R^3}\rho_Y(y)^pdy.
\]

On the nontrivial component,

\[
0<\langle M_p\rangle_\mu<\infty.
\]

Define a probability measure on hull-state/spatial-point pairs by

\[
\boxed{
d\mathbb P_p(Y,y)
:=
\frac{\rho_Y(y)^p}{\langle M_p\rangle_\mu}
\,dy\,d\mu(Y).
}
\]

For any integrable observable \(f(Y,y)\), write

\[
\mathbb E_p[f]
:=
\int f\,d\mathbb P_p.
\]

## 3. Exact p-weighted mean of sigma+kappa

M18-060 gives

\[
\frac1pM_p'
=
\int(\sigma+\kappa)\rho^pdy
-c_pM_p,
\]

where

\[
c_p=1-\frac{3}{2p}.
\]

Invariant averaging kills the bounded-state derivative:

\[
\langle M_p'\rangle=0.
\]

Therefore

\[
\boxed{
\mathbb E_p[\sigma+\kappa]
=c_p
=1-\frac{3}{2p}.
}
\]

Equivalently, for the actual logarithmic amplitude-growth rate

\[
g:=\sigma+\kappa-1,
\]

\[
\boxed{
\mathbb E_p[g]
=-\frac{3}{2p}.
}
\]

Thus all amplitude-weighted populations have negative mean material log-amplitude drift, but the mean drift approaches zero from below as the amplitude weight becomes more concentrated on the largest vorticity amplitudes.

## 4. Exact change of measure between p and q

Let

\[
q>p\ge2.
\]

Set

\[
w:=\rho^{q-p}.
\]

Then

\[
\boxed{
\mathbb E_q[f]
=
\frac{\mathbb E_p[fw]}{\mathbb E_p[w]}.
}
\]

Therefore

\[
\mathbb E_q[f]-\mathbb E_p[f]
=
\frac{\operatorname{Cov}_p(f,w)}{\mathbb E_p[w]}.
\]

Apply this to

\[
f=h=\sigma+\kappa.
\]

Using Section 3,

\[
\mathbb E_q[h]-\mathbb E_p[h]
=c_q-c_p.
\]

Hence the exact covariance identity is

\[
\boxed{
\operatorname{Cov}_p
\left(\sigma+\kappa,\rho^{q-p}\right)
=
\frac32
\left(\frac1p-\frac1q\right)
\mathbb E_p[\rho^{q-p}].
}
\]

The right-hand side is strictly positive.

## 5. Exact positive amplitude-growth covariance

Thus

\[
\boxed{
\operatorname{Cov}_p
\left(\sigma+\kappa,\rho^{q-p}\right)>0
\qquad(q>p\ge2).
}
\]

Equivalently,

\[
\boxed{
\operatorname{Cov}_p
\left(g,\rho^{q-p}\right)>0.
}
\]

This is not a heuristic statement that strong vorticity tends to experience stronger stretching.

It is an exact consequence of

- CE-H material amplitude evolution;
- similarity-volume divergence \(3/2\);
- compact invariant recurrence.

Higher-amplitude weighting necessarily shifts the mean net growth field upward.

## 6. Fixed oscillation floor

For any bounded random variable \(h\) and nonnegative nonzero tilt \(w\),

\[
\mathbb E_q[h]-\mathbb E_p[h]
\le
\operatorname*{ess\,sup}h
-
\operatorname*{ess\,inf}h.
\]

Therefore

\[
\boxed{
\operatorname*{ess\,osc}_{\mathbb P_p}(\sigma+\kappa)
\ge
c_q-c_p
=
\frac32\left(\frac1p-\frac1q\right).
}
\]

Taking \(p=2\),

\[
\boxed{
\operatorname*{ess\,osc}_{\mathbb P_2}(\sigma+\kappa)
\ge
\frac34-\frac{3}{2q}.
}
\]

Since this holds for every finite \(q>2\),

\[
\boxed{
\operatorname*{ess\,osc}_{\mathbb P_2}(\sigma+\kappa)
\ge
\frac34.
}
\]

Thus a recurrent nontrivial CE-H component cannot have a globally coherent net growth field \(\sigma+\kappa\) on its enstrophy-bearing population.

## 7. Variance-versus-amplitude-spread inequality

Cauchy--Schwarz gives

\[
|\operatorname{Cov}_p(h,w)|
\le
\sqrt{\operatorname{Var}_p(h)}
\sqrt{\operatorname{Var}_p(w)}.
\]

Using the exact covariance identity,

\[
\boxed{
\sqrt{\operatorname{Var}_p(\sigma+\kappa)}
\cdot
\frac{\sqrt{\operatorname{Var}_p(\rho^{q-p})}}
{\mathbb E_p[\rho^{q-p}]}
\ge
\frac32\left(\frac1p-\frac1q\right).
}
\]

The second factor is the coefficient of variation of the amplitude tilt.

Hence recurrence requires at least one of:

1. substantial net-growth-field variance;
2. substantial amplitude-distribution spread.

A state that is simultaneously nearly monodisperse in amplitude and nearly coherent in \(\sigma+\kappa\) is impossible on the nontrivial recurrent component.

## 8. Split into strain and coefficient variation

Since

\[
h=\sigma+\kappa,
\]

an oscillation floor for \(h\) gives

\[
\operatorname{osc}h
\le
\operatorname{osc}\sigma+\operatorname{osc}\kappa.
\]

Therefore the \(p=2\) floor implies

\[
\boxed{
\operatorname{osc}\sigma
\ge\frac38
\quad\lor\quad
\operatorname{osc}\kappa
\ge\frac38
}
\]

on the joint enstrophy-bearing recurrent support, in the essential-support sense.

The constants are dimensionless in the viscosity-one similarity normalization.

This is a global support statement. It does not assert that the two extreme values occur on the same vortex tube or at the same time.

## 9. Relation to existing strain/coefficient branches

The two alternatives already have developed descendants.

### Strain variation

Same-tube persistent axial strain heterogeneity is reduced by M16-022--028 to

\[
\text{curvature/label turnover}
\lor
\text{rank-two director area}
\lor
\text{rank-one great-circle zero-set winding}.
\]

The present result is weaker geometrically because its oscillation may occur across different tubes/times, but stronger in universality: some nontrivial strain-or-kappa segregation is mandatory on every recurrent CE-H component.

### Kappa variation

Coefficient variation feeds the existing

- positive/negative \(\kappa\) compensation architecture;
- coefficient-phase/strain tilt;
- threshold-gradient and zero-corridor channels;
- coefficient-jet/decompactification branches.

Thus the quiet `uniform sigma + uniform kappa` recharge picture is removed.

## 10. Why this is not yet a contradiction

A compact recurrent state can support a stationary nontrivial covariance forever.

The identity

\[
\operatorname{Cov}_p(h,\rho^{q-p})>0
\]

is a state-ensemble relation, not a monotone time integral.

It does not consume a finite resource.

Likewise the oscillation floor does not by itself supply gradient energy: converting two separated values into a derivative payment requires spatial or material connectivity, thickness, or a transition theorem.

Therefore

\[
\boxed{
\text{mandatory segregation}
\neq
\text{ancestral contradiction}.
}
\]

## 11. Strongest immediate use

The new identity removes one possible loophole in M18-061.

A hypothetical survivor cannot avoid derivative/topological channels merely by choosing one common coherent aligned-strain baseline for all amplitude populations.

Instead it must maintain a persistent amplitude-growth segregation with an exact mean shift

\[
\boxed{
\mathbb E_q[\sigma+\kappa]
-
\mathbb E_p[\sigma+\kappa]
=
\frac32\left(\frac1p-\frac1q\right).
}
\]

This turns the next target into a **connectivity problem**:

> Does the mandatory high-amplitude / low-amplitude segregation occur inside connected coherent carriers, in which case gradient/director/coefficient-transition payments follow, or can it be maintained indefinitely by spatially/materially disconnected populations without paying a stronger genealogy/interface cost?

## 12. Audit verdict

### Certified

1. \(\mathbb E_p[\sigma+\kappa]=1-3/(2p)\) for every finite \(p\ge2\).
2. For \(q>p\),
   \[
   \operatorname{Cov}_p(\sigma+\kappa,\rho^{q-p})
   =(c_q-c_p)\mathbb E_p[\rho^{q-p}]>0.
   \]
3. The enstrophy-bearing recurrent support has
   \[
   \operatorname{ess\,osc}(\sigma+\kappa)\ge3/4.
   \]
4. Therefore either strain or coefficient phase has a fixed nontrivial recurrent oscillation.
5. Simultaneously amplitude-monodisperse and growth-coherent recurrence is impossible.

### Still open

- spatial/material connectivity of the two amplitude-growth populations;
- conversion of the oscillation floor into a gradient, interface, or genealogy payment;
- ancestry closure of any resulting derivative payment;
- rank-two director and zero-set-winding survivors;
- remote/critical roots;
- global regularity.

## 13. Next target

M18-063 should convert the mandatory covariance into a **two-population quantitative separation theorem**.

A natural approach is to use the tilt identity to choose amplitude quantiles and prove that positive recurrent measure must occur in both

\[
\{\rho\le a,\ h\le h_-\}
\]

and

\[
\{\rho\ge b,\ h\ge h_+\}
\]

with \(b>a\) and \(h_+-h_->0\), unless the amplitude distribution itself collapses into a thin exceptional layer.

That would make the current abstract covariance compatible with the existing packet/interface/genealogy machinery.