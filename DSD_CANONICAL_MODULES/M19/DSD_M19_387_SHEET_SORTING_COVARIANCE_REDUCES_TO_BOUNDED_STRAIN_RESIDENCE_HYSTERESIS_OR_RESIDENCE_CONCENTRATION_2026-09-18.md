# M19-387 — Sheet-sorting covariance reduces to bounded strain-residence hysteresis or residence concentration

Date: 2026-09-18

Status: **NEW CANONICAL COMPRESSION / M19-386 + M5-684 + M19-349 + M19-380. THE POSITIVE SHEET-SORTING COVARIANCE NEEDED TO CANCEL THE NEGATIVE MATERIAL KAPPA-CURRENT IS NOT A FOURTH INDEPENDENT RESOURCE. ON A GENUINELY MATERIAL HIGH-AMPLITUDE VORTEX SEGMENT, THE RELATIVE LINE-RESIDENCE FACTOR `R=L_rho/Phi` OBEYS THE EXACT LAW `D log R = 2 sigma_bar_rho - 1/2`. HENCE LARGE INTER-SHEET DIFFERENCES IN RESIDENCE ARE ACCUMULATED STRAIN-RESIDENCE HISTORY. IF `R` REMAINS UNIFORMLY COMPARABLE, THE REQUIRED POSITIVE `Cov(L,h)` IS A BOUNDED-STATE PHASE/HYSTERESIS CIRCULATION ALREADY INSIDE THE M19-380 RESIDENCE CURRENCY. IF `R` LOSES UNIFORM COMPARABILITY OR UNIFORM INTEGRABILITY, THE BRANCH IS THE M19-349 LINE-RESIDENCE CONCENTRATION / SUPER-PARENT PARTICIPATION EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M19-386

At the zero coefficient level, the current-sign mismatch requires

\[
\operatorname{Cov}_0^\Phi(L_\chi,h)>0,
\qquad h=D_B\kappa,
\]

at the quantitative scale needed to offset

\[
\bar L_0G_\Phi(0)<0.
\]

M19-386 decomposes this into

\[
F_{cross-level}^{\mathfrak A\ne0}
\lor
H_{sheet}^{sort}
\lor
G_{critical/nodal}.
\]

The present note treats the noncritical sheet-sorting branch.

---

## 2. Exact material residence law

For a genuinely material vortex-line segment, M5-684 gives

\[
L_\rho
=
\int_{\Gamma_\lambda}\rho\,ds,
\]

and

\[
\frac d{d\theta}\log L_\rho
=
\kappa-\frac12+2\bar\sigma_\rho.
\]

The material vorticity flux satisfies

\[
\frac d{d\theta}\log\Phi=\kappa.
\]

Therefore the relative residence factor

\[
\boxed{
R_\lambda
:=
\frac{L_\rho}{\Phi}
}
\]

obeys the exact law

\[
\boxed{
\frac d{d\theta}\log R_\lambda
=
2\bar\sigma_{\rho,\lambda}-\frac12.
}
\]

Thus

\[
\boxed{
R_\lambda(\theta)
=R_\lambda(\theta_0)
\exp\left(
\int_{\theta_0}^{\theta}
\left[2\bar\sigma_{\rho,\lambda}(s)-\frac12\right]ds
\right).
}
\]

The multiplier \(\kappa\) cancels exactly from the relative residence law.

---

## 3. Meaning for sheet sorting

On sheet \(a\), write schematically

\[
\bar L_a
\sim
\bar\Phi_a\,\bar R_a
\]

for the current material-flux weighted population, with the usual caveat that averages of products are not products of averages unless the within-sheet covariance is controlled.

The key structural statement does not require that shortcut:

any persistent systematic excess in line residence between sheets must be produced by either

1. a persistent difference in current flux weight \(\Phi\), or
2. a persistent difference in the accumulated relative-residence factor \(R\).

But \(R\) is generated only by the integrated strain-residence phase

\[
2\bar\sigma_\rho-rac12.
\]

Hence the M19-386 sheet covariance is a history-dependent strain-residence sorting mechanism, not an independent measure artifact.

---

## 4. Bounded relative-residence branch

Assume there exist fixed constants

\[
0<R_-\le R_\lambda(\theta)\le R_+<\infty
\]

on the retained material population.

Then

\[
\log R_\lambda
\]

is a bounded state observable.

Its material drift

\[
2\bar\sigma_\rho-rac12
\]

has zero recurrent mean on a persistent recurrent label class.

Any positive correlation between the current residence weight and the coefficient velocity \(h\) is therefore a bounded phase relation between

\[
\boxed{
\text{coefficient crossing phase }h
\quad\text{and}\quad
\text{bounded accumulated strain-residence phase }\log R.
}
\]

This is precisely a recurrent hysteresis/circulation mechanism.

It does not provide monotone depletion.

Therefore

\[
\boxed{
H_{sheet}^{sort}
+\text{ bounded }R
\Longrightarrow
H_{\kappa\text{-}residence}^{+}
}
\]

in the resource classification of M19-380.

---

## 5. Unbounded/compressing relative-residence branch

If no uniform upper/lower comparability for \(R\) holds, then a subset of material labels acquires anomalously large or small line residence relative to its current flux.

Equivalently, the Radon--Nikodym bridge between flux-label and enstrophy-line measures becomes increasingly concentrated.

This is exactly the architecture already exposed in M19-337 and M19-349:

\[
\boxed{
\text{measure-transfer failure}
\Longrightarrow
\text{line-residence concentration / uniform-integrability failure}.
}
\]

Hence

\[
\boxed{
H_{sheet}^{sort}
+\text{ noncompact }R
\Longrightarrow
G_{residence}^{conc}
\lor
G_{super-parent}^{participation}
\lor
G_{threshold/genealogy}.
}
\]

The last terms record the known ways a material segment can cease to be represented by one persistent compact high-amplitude carrier.

---

## 6. Cutoff firewall

M19-385 uses a cutoff residence weight

\[
L_\chi
=
\int\chi(\rho)\rho\,ds.
\]

The exact law above is for a genuinely material segment without Eulerian threshold endpoints.

Therefore application to \(L_\chi\) is valid only on a time-thickened material subsegment that stays inside the region where \(\chi\equiv1\), or after adding the amplitude-threshold transfer term explicitly.

Failure of this condition is not a loophole to suppress; it is the already exposed

\[
T_{sheath}^{\rho=a_0}
\]

turnover branch of M19-374.

---

## 7. Canonical resource compression

Combining M19-386 with the residence law yields

\[
\boxed{
H_{Lh}^{0,+}
\Longrightarrow
F_{cross-level}^{\mathfrak A\ne0}
\lor
H_{\kappa\text{-}residence}^{+}
\lor
G_{residence}^{conc}
\lor
T_{sheath}^{\rho=a_0}
\lor
G_{critical/nodal}.
}
\]

Thus the M19-385 covariance gate does **not** add a fourth stationary currency beyond the M19-380 compression.

Its compact noncritical part is already the residence-hysteresis currency.

Its noncompact part is a residence/genealogy exit.

---

## 8. Consequence for the live frontier

The retained compact CE-H resource tree remains

\[
\boxed{
P_{critical}
\lor
H_{\kappa\text{-}residence}
\lor
T_{amplitude}^{up}
}
\]

plus explicit representation/decompactification exits.

The next genuinely new theorem must therefore break reuse in one of these three classes rather than invent another local payer.

In particular, the highest-value remaining compact target is to determine whether the same material genealogy can sustain an order-one residence-hysteresis loop across infinitely many retained scales without violating the finite base-transversal or record-cell incidence structure.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
