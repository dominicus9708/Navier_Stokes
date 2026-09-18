# M19-392 — Compact h bound turns deep kappa turnover into fixed positive action or genealogy replacement

Date: 2026-09-18

Status: **NEW CANONICAL DEEP-EXCURSION THICKENING / M19-391 GIVES FIXED DOWNWARD CURRENT THROUGH EVERY OCCUPIED AWAY-ZERO KAPPA LEVEL. ON THE COMPACT CE-H HULL, `h=D_B kappa` HAS A UNIFORM BOUND. THEREFORE ANY COMPLETE POSITIVE-KAPPA EXCURSION THAT REACHES A FIXED LEVEL `delta>0` HAS A UNIFORM POSITIVE MULTIPLIER ACTION `I_+ >= delta^2/H_*`. CONSEQUENTLY A FIXED DEEP CURRENT CANNOT BE REALIZED ONLY BY ARBITRARILY SHALLOW/INSTANTANEOUS COMPLETE EXCURSIONS: IT MUST PRODUCE POSITIVE-RATE FIXED-ACTION MATERIAL EXCURSIONS OR EXIT THROUGH REPLACEMENT/GENEALOGY/REPRESENTATION LOSS BEFORE COMPLETION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Uniform material kappa-velocity bound

On the retained compact all-order CE-H hull,

\[
h:=D_B\kappa
\]

is a continuous fixed-order observable.

Hence compactness gives

\[
\boxed{
|h|\le H_*<\infty.
}
\]

This is a similarity-variable bound on the retained high-amplitude compact branch.

---

## 2. One complete positive excursion

Let

\[
\theta_u<\theta_d
\]

be consecutive zero crossings of one material label with

\[
\kappa(\theta_u)=\kappa(\theta_d)=0,
\qquad
\kappa>0
\quad
(\theta_u,\theta_d).
\]

Assume this excursion reaches

\[
\max_{[\theta_u,\theta_d]}\kappa\ge\delta>0.
\]

Choose a time \(\theta_m\) with

\[
\kappa(\theta_m)\ge\delta.
\]

Because \(|\dot\kappa|=|h|\le H_*\),

\[
\kappa(\theta)
\ge
\delta-H_*|\theta-\theta_m|
\]

whenever the right-hand side is positive.

Since the trajectory must rise from zero to \(\delta\) and later return to zero, the two triangular subintervals of width \(\delta/H_*\) lie inside the excursion.

Therefore

\[
\begin{aligned}
I_+
&:=
\int_{\theta_u}^{\theta_d}\kappa(\theta)\,d\theta\\
&\ge
2\int_0^{\delta/H_*}(\delta-H_*s)\,ds\\
&=
\frac{\delta^2}{H_*}.
\end{aligned}
\]

Thus

\[
\boxed{
I_+\ge i_\delta
:=
\frac{\delta^2}{H_*}>0.
}
\]

---

## 3. Minimal excursion duration

The same Lipschitz argument gives

\[
\boxed{
\theta_d-\theta_u
\ge
\frac{2\delta}{H_*}.
}
\]

Hence a deep excursion also has a uniform positive similarity-time duration.

This prevents the away-zero current of M19-391 from being represented by complete excursions whose duration collapses to zero.

---

## 4. Combine with the all-level current

M19-391 gives, for a fixed away-zero threshold \(\delta\),

\[
-\overline G(\delta)
=
\int_\delta^{K_*}s\overline F(s)\,ds.
\]

If the recurrent current-flux mass above \(\delta\) has a fixed floor,

\[
\int_\delta^{K_*}\overline F(s)\,ds
\ge m_\delta>0,
\]

then

\[
\boxed{
-\overline G(\delta)
\ge
\delta m_\delta>0.
}
\]

Thus the retained branch has a nonvanishing net downward material-flux current through the deep coefficient level.

---

## 5. Complete-excursion / replacement dichotomy

A downward current-carrying material history through \(\kappa=\delta\) has only two canonical possibilities when traced backward and forward in the retained genealogy.

### A. Complete deep excursion

The material label has a preceding upward zero crossing and a following downward zero crossing inside the retained representation.

Then the excursion reaches \(\delta\), and Section 2 gives

\[
\boxed{I_+\ge i_\delta>0.}
\]

### B. Incomplete material history

The history cannot be paired to a complete retained zero-to-zero excursion because it

- enters the retained carrier after the relevant earlier crossing,
- leaves the carrier before the later crossing,
- undergoes packet/sheet replacement,
- loses genealogy/contact,
- crosses the amplitude/domain representation boundary,
- or otherwise ceases to be the same certified material object.

This must be recorded as

\[
\boxed{
G_{replacement/genealogy/representation},
}
\]

not treated as a free complete excursion.

Therefore the deep-current branch has the canonical split

\[
\boxed{
J_{\kappa\ge\delta}^{down,+}
\Longrightarrow
E_{deep}^{I_+\ge i_\delta}
\lor
G_{replacement/genealogy/representation}.
}
\]

---

## 6. Relation to M19-389--390

For a complete deep excursion, M19-389--390 say that if the residence-weighted zero-crossing current of that excursion cancels or reverses its negative material-flux current, then

\[
J_+\le-2I_+.
\]

Combining with the present action floor gives the conditional estimate

\[
\boxed{
J_+\le
-2i_\delta
=
-\frac{2\delta^2}{H_*}.
}
\]

Equivalently,

\[
\boxed{
\frac{R_d}{R_u}
\le
e^{-2\delta^2/H_*},
\qquad
R:=\frac{L_\rho}{\Phi}.
}
\]

Since

\[
\frac{\Phi_d}{\Phi_u}=e^{I_+},
\]

the enstrophy line-residence weight itself obeys

\[
\frac{L_d}{L_u}
=
e^{I_++J_+}
\le
e^{-I_+}
\le
e^{-\delta^2/H_*}.
\]

Hence

\[
\boxed{
\frac{L_d}{L_u}
\le
e^{-\delta^2/H_*}<1.
}
\]

So a deep complete excursion that reverses the spatial current must lose a fixed fraction of its enstrophy line residence during the positive-kappa phase.

---

## 7. What this does and does not close

The fixed multiplicative residence swing is real, but it is not yet nonrecyclable.

A later negative-kappa/extensional phase may restore the same line residence, as the M19-388 periodic witness demonstrates.

Thus the valid new information is

\[
\boxed{
\text{deep current}
\to
\text{fixed-action/fixed-residence-swing excursion}
\lor
\text{replacement/genealogy exit}.
}
\]

The next closure target is to determine whether repeated fixed residence reconstruction on the same certified genealogy can occur without either

1. positive amplitude-threshold turnover,
2. critical palinstrophy incidence,
3. projective/sheet replacement,
4. or loss of uniform line-residence integrability.

This is a nonreuse problem, not another local sign problem.

---

\[
\boxed{\text{M19-392 COMPLETE; DEEP KAPPA CURRENT HAS A FIXED-ACTION MATERIAL THICKNESS.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
