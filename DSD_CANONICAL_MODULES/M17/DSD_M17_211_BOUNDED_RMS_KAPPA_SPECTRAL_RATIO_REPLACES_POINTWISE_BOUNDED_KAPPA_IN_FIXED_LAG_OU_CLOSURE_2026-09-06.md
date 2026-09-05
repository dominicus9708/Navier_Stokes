# DSD M17-211 — Bounded RMS kappa spectral ratio replaces pointwise bounded kappa in the fixed-lag OU closure

Date: 2026-09-06  
Canonical ID: **M17-211**

Status: **SPECTRAL-RATIO STRENGTHENING / M17-205/208 USED POINTWISE `|kappa|<=K_*` TO OBTAIN FIXED-LAG MATERIAL ENSTROPHY COMPARABILITY, AND M17-158 USED THE SAME ASSUMPTION TO OBTAIN A UNIFORM FREQUENCY-SECOND-MOMENT RATIO FOR THE OU LIMIT. M17-210 SHOWS THAT THE NATURAL QUANTITY IS INSTEAD THE ENSTROPHY-WEIGHTED RMS MULTIPLIER `Lambda_A^2 = int_A kappa^2 rho^2 / int_A rho^2 = int_A |Delta W|^2 / int_A |W|^2`. IF `Lambda_A` IS UNIFORMLY BOUNDED ON THE FIXED-LAG MATERIAL CORRIDORS, THE MATERIAL ENSTROPHY OBEYS A GRONWALL COMPARABILITY LAW. AFTER NORMALIZATION, THE SAME BOUND GIVES `H2/L2` COMPACTNESS AND, BY INTERPOLATION, THE UNIFORM `H1/L2` SPECTRAL RATIO NEEDED IN THE M17-158 BACKWARD OU FOURIER CONTRADICTION. THUS POINTWISE KAPPA SPIKES OF ENSTROPHY-NEGLIGIBLE SIZE DO NOT FORM A NEW ESCAPE. THE TRUE HARD EXIT IS DIVERGENCE OF THE RMS SPECTRAL RATIO `Lambda`. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RMS multiplier on a material set

Let `A(theta)` be a material set transported by `B` and define

\[
E_A(\theta):=\int_{A(\theta)}\rho^2dy.
\]

When `E_A>0`, define

\[
\boxed{
\Lambda_A^2(\theta)
:=\frac{\int_{A(\theta)}\kappa^2\rho^2dy}{E_A(\theta)}
=\frac{\int_{A(\theta)}|\Delta W|^2dy}{E_A(\theta)}.
}
\]

Assume on a fixed lag interval

\[
\boxed{\Lambda_A(\theta)\le\Lambda_*<\infty.}
\]

No pointwise upper bound for `|kappa|` is assumed.

---

## 2. Exact material enstrophy derivative

Because

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\qquad
\nabla\cdot B=\frac32,
\]

Reynolds transport on a material set gives

\[
\boxed{
E_A'
=\int_A\left(2\sigma+2\kappa-\frac12\right)\rho^2dy.
}
\]

Let

\[
\|\sigma\|_{L^\infty}\le S_*
\]

on the compact smooth hull.

Cauchy--Schwarz gives

\[
\left|\int_A\kappa\rho^2dy\right|
\le
\left(\int_A\kappa^2\rho^2dy\right)^{1/2}
E_A^{1/2}
=\Lambda_AE_A.
\]

Therefore

\[
\boxed{
|E_A'|
\le
\left(2S_*+\frac12+2\Lambda_*\right)E_A.
}
\]

Gronwall yields for every fixed lag `T`

\[
\boxed{
e^{-C_*T}E_A(0)
\le E_A(T)\le e^{C_*T}E_A(0),}
\]

where

\[
C_*:=2S_*+\frac12+2\Lambda_*.
\]

Thus M17-205's material-mass comparability does not require pointwise bounded kappa.

---

## 3. Shell transfer remains finite-neighbor

The radial material-flow calculation of M17-205 uses only the remote Type-I velocity bound, not kappa.
Hence a fixed ancestor shell still maps into finitely many current dyadic neighbors.

Combining this geometry with Section 2 gives the M17-205 shell transfer inequality under the weaker RMS assumption:

\[
\boxed{
E_j(-T)
\le C_{T,\Lambda_*}
\sum_{|m|\le M_T}E_{j+s_T+m}(0).
}
\]

The reverse fixed-lag estimate follows similarly.

---

## 4. Normalized H2 compactness

On a relative-thick packet shell, M17-155 supplies

\[
a_j^2\ge c_*E_j(0).
\]

If the shell RMS ratio is bounded,

\[
\int_{C_j}|\Delta W|^2dy
\le\Lambda_*^2E_j.
\]

For the normalized field

\[
V_j:=W/a_j,
\]

we therefore have

\[
\boxed{
\|\Delta V_j\|_2^2
\le\frac{\Lambda_*^2}{c_*}
}
\]

on the retained translated shell/packet region.

Together with the normalized `L2` ceiling this gives fixed-lag `H2` compactness on local translated regions.
In three dimensions, local `H2` compactness is strong enough to preserve a nonzero normalized packet after subsequence extraction without relying on pointwise bounded potential elliptic estimates.

---

## 5. H1/L2 spectral ratio

For an `L2` field with `Delta V in L2`, Fourier Cauchy--Schwarz gives

\[
\begin{aligned}
\|\nabla V\|_2^2
&=\int |\xi|^2|\widehat V|^2d\xi\\
&\le
\left(\int|\widehat V|^2\right)^{1/2}
\left(\int|\xi|^4|\widehat V|^2\right)^{1/2}\\
&=\|V\|_2\|\Delta V\|_2.
\end{aligned}
\]

Hence

\[
\boxed{
\frac{\|\nabla V\|_2^2}{\|V\|_2^2}
\le
\frac{\|\Delta V\|_2}{\|V\|_2}
\le\Lambda_*
}
\]

whenever the RMS ratio is bounded by `Lambda_*`.

This is precisely the spectral-ratio ceiling used in the M17-158 backward OU Fourier argument.

---

## 6. Tempered-shell OU closure under RMS boundedness

Combine:

1. M17-207 globally tempered finite-neighbor shell control;
2. Sections 2--3 fixed-lag mass comparability under `Lambda<=Lambda_*`;
3. M17-155 relative thickness and quiet translated dynamics;
4. Section 4 compactness;
5. Section 5 uniform spectral ratio.

Then for every fixed `T`, normalized packet mass remains finite on `[-T,T]` and the extracted OU limit satisfies

\[
\boxed{
\frac{\|\nabla V(\tau)\|_2^2}{\|V(\tau)\|_2^2}
\le\Lambda_*
\qquad\forall\tau\in\mathbb R.
}
\]

The M17-158 exponential backward Fourier tilting argument uses only this uniform ratio and the OU equation. It therefore again forces

\[
\boxed{V\equiv0,}
\]

contradicting the nonzero packet normalization.

Thus

\[
\boxed{
R_{2}^{relative\text{-}thick,\ quiet,\ tempered,\ bounded\ RMS\ kappa}
\Longrightarrow\bot.
}
\]

---

## 7. Correct hard exit

Pointwise kappa spikes may occur while carrying negligible enstrophy, but they do not defeat this argument if the RMS ratio remains bounded.

The genuine spectral escape is therefore

\[
\boxed{
\Lambda_R^2
=\frac{\int_{C_R}|\Delta W|^2}{\int_{C_R}|W|^2}
\to\infty.
}
\]

Hence the old branch label

\[
G_{\kappa,\infty}
\]

should be replaced, on the hard shell level, by

\[
\boxed{G_{H2/L2\ spectral\ concentration}.}
\]

---

## 8. DSD audit

- A local shell `H2/L2` bound is used where needed; a global `H2` ceiling alone is insufficient because shell `L2` mass decays.
- No pointwise bound on kappa is inferred from the RMS bound.
- The OU contradiction uses the uniform `H1/L2` spectral ratio, not the scalar potential equation itself.
- If the spectral ratio diverges, it remains an explicit hard branch.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
