# Nested material pruning: the exceptional-label residual branch

Date: 2026-08-13

Status: **STRUCTURAL CORRECTION + DERIVED NATURAL-SCALE COST / OPEN INTER-WINDOW GEOMETRIC GAIN**.

The fixed-positive-volume material-core exclusion does **not** imply that every surviving singular scenario must recruit new material.  There is another escape: each later dangerous core can be a smaller material subset of the previous one.

This note types that branch separately as **material pruning**.

---

## 1. Natural core volume shrinks automatically

Let

\[
W_j=\|\omega(t_j)\|_\infty
\]

and use the natural vorticity radius

\[
r_j=aW_j^{-1/2}.
\]

A volumetrically thick natural core has volume

\[
V_j\asymp r_j^3
\asymp W_j^{-3/2}.
\]

Suppose the dangerous magnitude increases by a factor

\[
W_{j+1}=qW_j,
\qquad q>1.
\]

Then

\[
\boxed{
\frac{V_{j+1}}{V_j}
\asymp q^{-3/2}.
}
\]

For a doubling `q=2`,

\[
2^{-3/2}\approx0.353553.
\]

Thus a later natural core can consist entirely of old material while retaining only about 35 percent of the previous natural-core volume.

No new recruitment is logically required.

---

## 2. Nested material-core scenario

Let

\[
\widetilde C_j(t_{j+1})
=X(C_j(t_j),t_{j+1};t_j)
\]

be the material image of the previous core.

A pure-pruning branch has

\[
\boxed{
C_{j+1}\subset\widetilde C_j
}
\]

up to negligible errors, with

\[
|C_{j+1}|
\asymp q^{-3/2}|C_j|.
\]

The material-retention fraction relative to the previous core is therefore allowed to be

\[
\rho_j
\asymp q^{-3/2}<1.
\]

After `N` equal growth steps,

\[
\prod_{j=1}^{N}\rho_j
\asymp q^{-3N/2}
=
\left(\frac{W_N}{W_0}\right)^{-3/2}
\to0.
\]

Therefore even perfect **nested** retention of the later core does not leave a positive-volume material subset.

This corrects an over-strong reading of the turnover-summability idea: a positive infinite product is not expected when the target core volume itself tends to zero.

---

## 3. What survives in the limit

A nested sequence of material cores can converge to a zero-measure material-label set while remaining nonempty.

Hence the fixed-material-core exclusion only says

\[
\boxed{
\text{no fixed positive material volume can remain dangerous.}
}
\]

It does not exclude

\[
\boxed{
\text{a shrinking exceptional set of labels carrying the dangerous core.}
}
\]

This is consistent with the material-label deformation tail: arbitrarily strong deformation can occur on progressively smaller label sets without violating the finite global `L^2` strain budget.

---

## 4. Enstrophy floor of a thick natural core

Suppose on `C_j`

\[
|\omega|\ge bW_j
\]

and

\[
|C_j|\ge\theta r_j^3
\]

for fixed `b,theta>0`.

Then

\[
E_\omega(t_j)
\ge
\int_{C_j}|\omega|^2dx
\ge
b^2W_j^2\theta r_j^3.
\]

Therefore

\[
\boxed{
E_\omega(t_j)
\ge
c_{a,b,\theta}\sqrt{W_j}.
}
\]

Along `W_{j+1}=qW_j`, the instantaneous enstrophy floor grows by

\[
\sqrt q.
\]

Thus persistent thick natural cores force

\[
E_\omega(t_j)\to\infty.
\]

This is necessary but not contradictory.

---

## 5. Why the global energy budget still permits pruning

A natural time window has duration

\[
\tau_j\asymp W_j^{-1}.
\]

If the enstrophy is only at its natural-core floor, its contribution to the kinetic-energy dissipation budget over one window scales as

\[
E_\omega\tau_j
\gtrsim
\sqrt{W_j}\,W_j^{-1}
=
W_j^{-1/2}.
\]

For a dyadic sequence `W_j~2^j`,

\[
\boxed{
\sum_jW_j^{-1/2}<\infty.
}
\]

Thus the finite global energy budget can afford infinitely many increasingly intense but increasingly small natural cores at the level of scaling alone.

This is the same critical summability wall seen in the material-deformation tail.

---

## 6. Relation to oriented flux

In the projectively aligned one-polarity branch, a natural cross-section can carry order-one signed flux

\[
\Phi_j\sim W_jr_j^2\sim1.
\]

Shrinking the **intense** core does not require the total vorticity flux tube to terminate.  The same signed flux may continue through a broader/lower-intensity surrounding tube outside the threshold core.

Therefore the spatial flux trichotomy does not by itself forbid pruning of the high-intensity subset.

It forbids free termination of the signed flux, not free movement of the chosen intensity threshold along an existing flux tube.

This distinction must remain typed.

---

## 7. Two separate material mechanisms

The residual material branch is now

\[
\boxed{
\textbf{R-branch: material recruitment/turnover}
}
\]

versus

\[
\boxed{
\textbf{P-branch: nested material pruning/selection}.
}
\]

### R-branch

New labels cross from lower vorticity into the dangerous threshold.

Under bounded deformation, the Cauchy-vorticity lemma charges this to

\[
\int_I|\Delta\omega|^2
\gtrsim W^{3/2}.
\]

### P-branch

The later core uses only a smaller subset of the already-dangerous labels.

No recruitment cost is required.  The price is concentration of vorticity and deformation onto an increasingly exceptional label set.

---

## 8. What could close the pruning branch

Pure scaling cannot close it.  A strict gain must use one of the additional conditions that the residual core already has to satisfy:

1. **non-sparseness** at every natural scale;
2. **projective roughness** strong enough to evade the Campanato/coherence gate;
3. **one-polarity oriented flux** or its mixed-polarity alternative;
4. **large derivative-covariance mismatch** if viscosity regenerates geometry;
5. **inter-window overlap constraints** imposed by material transport and finite propagation of the dangerous geometry.

The most promising object is therefore not absolute retained material volume but a normalized overlap matrix between consecutive natural cores.

---

## 9. Normalized inter-window overlap

Define

\[
\boxed{
\mathcal O_{j\to j+1}
=
\frac{
|C_{j+1}\cap X(C_j,t_{j+1};t_j)|
}{|C_{j+1}|}.
}
\]

This measures what fraction of the **new smaller core** comes from old dangerous material.

Unlike retention normalized by `|C_j|`, this quantity can remain near one under pure pruning.

Hence the correct dichotomy is:

- `O_{j->j+1} near 1`: pruning/continuation of old dangerous labels;
- `O_{j->j+1} small`: true material recruitment/turnover.

The Cauchy-vorticity turnover lemma applies directly to the second case.

The first case requires a new estimate on how a nearly nested core can repeatedly shrink while remaining thick, projectively dangerous, and sign/flux compatible.

---

## 10. Principal next target

Construct a **normalized overlap cascade** on dyadic/natural vorticity levels and prove that one of two things happens:

\[
\boxed{
\text{low overlap infinitely often}
\Rightarrow
\text{repeated }k=2\text{ Cauchy-defect cost},
}
\]

or

\[
\boxed{
\text{high overlap eventually}
\Rightarrow
\text{one nested material-label chain must carry the full dangerous geometry}.
}
\]

The second implication must then be combined with projective/polarity/flux and deformation constraints to obtain a strict gain beyond the summable `W^{-1/2}` energy cost.

Status: **OPEN NORMALIZED-OVERLAP CASCADE / PRUNING CLOSURE**.
