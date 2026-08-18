# Tight-core obstruction for near-saturated middle-strain production

Date: 2026-08-19

Status: **DERIVED CONDITIONAL TIGHTNESS LEMMA / M-TO-H/T REDUCTION / GLOBAL REGULARITY NOT PROVED**.

This note continues `notes/2026-08-19-middle-strain-saturation-defect.md`.

---

## 1. Critical local middle-strain mass

Write

\[
f=\lambda_2^+.
\]

The refined enstrophy ledger is

\[
\boxed{
\frac12E_\omega'
+4\|f\|_3^3
\le
\mathfrak E_M P_\omega,
\qquad
\mathfrak E_M=C_S\|f\|_{3/2}-\nu.
}
\]

Suppose a measurable set `G` of finite volume carries local critical middle-strain mass

\[
L_G=\|f\|_{L^{3/2}(G)}.
\]

By finite-measure norm comparison,

\[
\|f\|_{L^2(G)}^2
\ge
|G|^{-1/3}L_G^2.
\]

Also, by Cauchy applied to `f^(3/2)`,

\[
\boxed{
\int_G f^3
\ge
|G|^{-1}L_G^3.
}
\]

Thus a fixed amount of scale-critical `L^(3/2)` mass cannot be packed into a fixed volume without paying a fixed cubic-defect density.

---

## 2. Tight critical mass forces cubic defect

If `G subset B_R` and

\[
L_G\ge \theta\frac{\nu}{C_S}
\]

for fixed `theta>0`, then

\[
\boxed{
\|f\|_3^3
\ge
\frac{\theta^3\nu^3}{C_S^3|B_R|}
=
\frac{\theta^3\nu^3}{C_S^3(4\pi/3)R^3}.
}
\]

At a time of nondecreasing enstrophy,

\[
E_\omega'\ge0,
\]

the refined ledger therefore implies

\[
\boxed{
\mathfrak E_M P_\omega
\ge
\frac{4\theta^3\nu^3}{C_S^3(4\pi/3)R^3}.
}
\]

Hence a spatially tight `M` episode close to the critical threshold `mathfrak E_M -> 0^+` forces

\[
\boxed{
P_\omega\to\infty.
}
\]

This gives a direct `M -> H` reduction for tight near-threshold episodes.

---

## 3. Near determinant saturation forces enstrophy or non-tightness

Now suppose additionally that on `G`

\[
\frac{f}{|S|}\le\kappa.
\]

Then

\[
|S|\ge f/\kappa,
\]

and therefore

\[
\|S\|_2^2
\ge
\kappa^{-2}\|f\|_{L^2(G)}^2
\ge
\kappa^{-2}|G|^{-1/3}L_G^2.
\]

Since

\[
E_\omega=2\|S\|_2^2,
\]

we obtain

\[
\boxed{
E_\omega
\ge
2\kappa^{-2}|G|^{-1/3}L_G^2.
}
\]

For `G subset B_R` and `L_G >= theta nu/C_S`,

\[
\boxed{
E_\omega
\ge
2\left(\frac{3}{4\pi}\right)^{1/3}
\frac{\theta^2\nu^2}{C_S^2}
\frac{1}{\kappa^2R}.
}
\]

Thus if determinant-production saturation drives

\[
\kappa=\lambda_2^+/|S|\to0
\]

while the critical `L^(3/2)` mass remains in a fixed-radius core, normalized enstrophy must diverge at least like `kappa^(-2)`.

---

## 4. First-hitting consequence

At terminal first-hitting normalization,

\[
\|\Omega\|_\infty\le1.
\]

Therefore if

\[
E_\Omega=\int|\Omega|^2dy\to\infty,
\]

no fixed bounded spatial region can contain a fixed positive fraction of total enstrophy: for every fixed measurable region `K` of finite volume,

\[
\int_K|\Omega|^2dy\le|K|,
\]

so

\[
\frac{\int_K|\Omega|^2dy}{E_\Omega}
\le
\frac{|K|}{E_\Omega}
\to0.
\]

Hence normalized enstrophy divergence under the first-hitting cap is an explicit spatial non-tightness certificate.

Combining with the previous section gives the conditional implication

\[
\boxed{
\begin{gathered}
\text{fixed-radius critical }L^{3/2}\text{ middle-strain mass}
\\
+\ \lambda_2^+/|S|\to0
\\
\Longrightarrow
\text{normalized enstrophy divergence}
\Longrightarrow
\text{spatial non-tightness }(T).
\end{gathered}
}
\]

Thus a spatially tight determinant-saturated `M` branch cannot persist under the first-hitting cap.

---

## 5. Remaining segregation loophole

The argument requires the critical `L^(3/2)` mass and the near-saturated strain geometry to overlap in a fixed-radius region.

If they fail to overlap, the remaining possibility is a typed **mass/production segregation** scenario:

1. the critical `L^(3/2)` middle-strain mass lives far from the determinant-productive core; or
2. the critical mass spreads over growing spatial volume at low amplitude; or
3. the productive set and the critical-norm set separate across scales.

All three are naturally routed to the existing spatial non-tightness / multicore / shell-transport `T` branch unless a new local overlap theorem recovers them.

Therefore the principal next local theorem target is an overlap statement of the schematic form

\[
\boxed{
\text{fresh local enstrophy production}
\Longrightarrow
\text{a fixed fraction of critical }L^{3/2}\text{ mass overlaps the tracked productive core}.
}
\]

If such an overlap theorem is proved, then the near-saturated `M` branch is reduced to `H` or `T` by the inequalities above.

Status: **TIGHT NEAR-THRESHOLD M -> H; TIGHT DETERMINANT-SATURATED M -> T; MASS/PRODUCTION OVERLAP REMAINS OPEN**.
