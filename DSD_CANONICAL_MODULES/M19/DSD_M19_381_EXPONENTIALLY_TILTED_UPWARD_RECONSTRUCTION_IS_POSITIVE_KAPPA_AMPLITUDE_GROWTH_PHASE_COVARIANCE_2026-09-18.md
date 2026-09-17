# M19-381 — The exponentially tilted upward-reconstruction payer is a positive kappa–amplitude-growth phase covariance

**Date:** 2026-09-18  
**Status:** NEW CANONICAL RESOURCE COMPRESSION / COAREA + M5-668 + M5-688

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-380 compresses the M5-688 payer tree to

\[
\boxed{
P_{critical}
\lor
H_{\kappa\text{-}residence}
\lor
T_{amplitude}^{up}.
}
\]

The third currency arises from the exponentially tilted cutoff term.

The present module asks whether this is genuinely a third resource class or whether its positive sign already means a bounded-state phase correlation between `kappa` and local amplitude growth.

---

## 2. Ordinary and tilted cutoff currents

Write

\[
\gamma:=\sigma+\kappa-1
\]

so that

\[
D_B\log\rho=\gamma.
\]

For a regular threshold `a`, M5-668 defines

\[
\mathcal T(a)
=
 a\int_{\rho=a}
\frac{\gamma}{|\nabla\rho|}\,dS.
\]

M19-378 uses the tilted current

\[
\mathcal T_2(a)
=
 a\int_{\rho=a}
 e^{2\kappa}
\frac{\gamma}{|\nabla\rho|}\,dS.
\]

The M5-688 cutoff currency is

\[
\boxed{
\mathcal C
=
\int_0^\infty
\chi'(a)a^2\overline{\mathcal T_2}(a)\,da.
}
\]

Assume the cutoff is chosen monotonically so that `chi' >= 0`, as in the retained M5-688 construction.

---

## 3. Coarea converts the cutoff currency to a bulk phase average

Using the coarea formula,

\[
\int_0^\infty
\chi'(a)a^2
\mathcal T_2(a)\,da
=
\int_{\mathbb R^3}
\chi'(\rho)\rho^3e^{2\kappa}\gamma\,dy.
\]

Therefore

\[
\boxed{
\mathcal C
=
\left\langle
\int
w\,e^{2\kappa}\gamma\,dy
\right\rangle,
\qquad
w:=\chi'(\rho)\rho^3\ge0.
}
\]

Likewise define the un-tilted quantity

\[
\boxed{
\mathcal J
:=
\left\langle
\int w\,\gamma\,dy
\right\rangle.
}
\]

By M5-668,

\[
\overline{\mathcal T}(a)
=-\frac32\overline V_a.
\]

Hence

\[
\boxed{
\mathcal J
=-\frac32
\int_0^\infty
\chi'(a)a^2\overline V_a\,da
<0
}
\]

whenever the cutoff collar intersects a nontrivial recurrent amplitude population.

---

## 4. A finite invariant cutoff-collar probability measure

Let

\[
Z
:=
\left\langle
\int w\,dy
\right\rangle.
\]

On the fixed cutoff support,

\[
0<a_-\le\rho\le a_+<\infty
\]

and the enstrophy is uniformly bounded. Hence

\[
0<Z\le Z_*^{cut}<\infty
\]

on the nontrivial cutoff branch.

Define the invariant cutoff-collar probability expectation

\[
\boxed{
\mathbb E_\mu[f]
:=
\frac1Z
\left\langle
\int w f\,dy
\right\rangle.
}
\]

Then

\[
\mathbb E_\mu[\gamma]
=\frac{\mathcal J}{Z}<0,
\]

while

\[
\mathbb E_\mu[e^{2\kappa}\gamma]
=\frac{\mathcal C}{Z}.
\]

---

## 5. Positive tilted payment is exactly positive phase covariance

The covariance is

\[
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)
=
\mathbb E_\mu[e^{2\kappa}\gamma]
-
\mathbb E_\mu[e^{2\kappa}]\mathbb E_\mu[\gamma].
\]

Thus

\[
\boxed{
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)
=
\frac{\mathcal C}{Z}
-
\mathbb E_\mu[e^{2\kappa}]\frac{\mathcal J}{Z}.
}
\]

Since

\[
\mathcal J<0,
\]

we obtain the strict implication

\[
\boxed{
\mathcal C\ge0
\Longrightarrow
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)>0.
}
\]

If the M19-380 cutoff currency has a fixed floor

\[
\mathcal C\ge c_C>0,
\]

then compactness gives a fixed covariance floor as well. In particular, with `|kappa|<=K_*`,

\[
\boxed{
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)
\ge
\frac{c_C}{Z_*^{cut}}
>0.
}
\]

The additional contribution from `-J` only strengthens this estimate.

Thus the tilted sign reversal is not an independent mysterious source. It is a quantitative statement that **larger kappa is positively phase-sorted with upward/local amplitude growth** on the cutoff collar.

---

## 6. Split into kappa self-sorting and kappa–strain sorting

Because

\[
\gamma=\sigma+\kappa-1,
\]

we have

\[
\boxed{
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)
=
\operatorname{Cov}_\mu(e^{2\kappa},\kappa)
+
\operatorname{Cov}_\mu(e^{2\kappa},\sigma).
}
\]

The first term is nonnegative because `e^{2x}` is increasing.

More quantitatively, for `|kappa|<=K_*`,

\[
0
\le
\operatorname{Cov}_\mu(e^{2\kappa},\kappa)
\le
2e^{2K_*}\operatorname{Var}_\mu(\kappa).
\]

Therefore if

\[
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)
\ge c_{cov}>0,
\]

then, for example, choosing

\[
v_*:=\frac{c_{cov}}{4e^{2K_*}},
\]

forces the dichotomy

\[
\boxed{
\operatorname{Var}_\mu(\kappa)\ge v_*
\quad\lor\quad
\operatorname{Cov}_\mu(e^{2\kappa},\sigma)
\ge\frac12c_{cov}.
}
\]

Thus the upward-reconstruction currency reduces to either

1. fixed coefficient heterogeneity on the cutoff collar, or
2. fixed positive kappa–strain phase sorting.

---

## 7. Relation to the previous M19 branches

The first branch reconnects to the M19-321--329 coefficient-variance architecture.

The second is a bounded-state phase/covariance mechanism of the same general type as the M19-328--331 and M19-380 hysteresis currencies.

Therefore, at the resource-class level,

\[
\boxed{
T_{amplitude}^{up,+}
\Longrightarrow
H_{\kappa\text{-}phase}^{+}
}

where `H_{kappa-phase}` is understood broadly to include coefficient heterogeneity and kappa–strain/amplitude-growth sorting.

This does **not** say the actual material upward conveyor disappears. It says the positive M5-688 payment produced by that conveyor is possible only because of a fixed bounded-state phase bias.

---

## 8. Updated resource compression

M19-380 gave three classes:

\[
P_{critical}
\lor
H_{\kappa\text{-}residence}
\lor
T_{amplitude}^{up}.
\]

The present module shows that the third class is not independent at the stationary payer level:

\[
\boxed{
D_\kappa>0
\Longrightarrow
P_{critical}^{+}
\lor
H_{\kappa\text{-}phase}^{+}.
}
\]

Here the phase class includes

\[
\boxed{
\kappa\text{-residence hysteresis}
\lor
\kappa\text{-variance/heterogeneity}
\lor
\kappa\text{-strain/amplitude-growth covariance}.
}
\]

So the canonical CE-H stationary resource frontier compresses from three classes to **two broad classes**:

\[
\boxed{
\text{critical derivative occupancy}
\lor
\text{bounded recurrent phase segregation/hysteresis}.
}
\]

---

## 9. Firewall

This is a resource classification, not a contradiction.

- A positive covariance can recur forever on a compact dynamical system.
- Spatial kappa variance may be paid by the already present `D_kappa` diffusion and derivative currencies.
- Temporal/state phase sorting may form a recurrent loop.
- No monotone finite resource has yet been produced.

Therefore the missing theorem becomes sharper:

\[
\boxed{
\mathcal T_{recycle}^{break}:
\text{prevent simultaneous indefinite reuse of critical derivative occupancy and bounded kappa-phase segregation across the retained genealogy/scales.}
}
\]

---

## 10. Verdict

\[
\boxed{
\mathcal C_+>0
\Longrightarrow
\operatorname{Cov}_\mu(e^{2\kappa},\gamma)>0
\Longrightarrow
\operatorname{Var}_\mu(\kappa)>0
\lor
\operatorname{Cov}_\mu(e^{2\kappa},\sigma)>0.
}
\]

The exponential upward-reconstruction payer is therefore a phase-sorting mechanism rather than a third independent stationary resource class.

---

\[
\boxed{\text{M19-381 COMPLETE; THE CE-H STATIONARY RESOURCE FRONTIER IS NOW CRITICAL DERIVATIVE OCCUPANCY OR KAPPA-PHASE HYSTERESIS/SEGREGATION.}}
\]
