# DSD M17-165 — M5 label hysteresis forces a positive relative-speed-weighted localized `-kappa rho^2` axial pressure-production bias

Date: 2026-09-06  
Canonical ID: **M17-165**

Status: **MEASURE-PRESERVING LOCAL/GLOBAL BRIDGE / M17-164 IDENTIFIES THE VERTICAL LOCAL OCTUPOLE `O_V` WITH THE SMALL-CORE COEFFICIENT OF THE ACTUAL GLOBAL KAPPA-PRODUCTION SOURCE `Pi_{V,kappa}^{prod}=-<kappa rho^2,K_333>`. INSERTING THIS LOCALIZED PRODUCTION COEFFICIENT INTO THE ORIGINAL M5 BASE-LABEL MEASURE OF M17-095 GIVES A NEW FAMILY `C_R`: `C_R=int a r_V |Q|^-2 [Pi_core(R)/R^2] delta(kappa)dmu_0`. ON A UNIFORMLY REGULAR COMPACT CROSSING HULL, `C_R -> (6/7)m_chi int a r_V O_V |Q|^-2 delta(kappa)dmu_0`, SO THE M5 HYSTERESIS CONDITION FORCES `lim_{R->0} mean C_R >0`. THIS IS THE FIRST EXACT STATEMENT IN WHICH M5'S TEMPORAL CROSSING BIAS AND A GENUINE PRESSURE-PRODUCTION SOURCE ARE PRESENT IN THE SAME LABEL LEDGER WITHOUT COAREA SUBSTITUTION. THE REMAINING OBSTRUCTION IS NO LONGER LOCAL SOURCE IDENTIFICATION; IT IS THE RELATIVE-SPEED WEIGHT AND THE SIGNED OUTER/MESOSCOPIC CONTRIBUTION NEEDED TO PASS FROM THE LOCALIZED PRODUCTION CORE TO THE FULL GLOBAL AXIAL STF RECURRENCE LAW. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. M5 crossing bias

M17-095 gives

\[
\boxed{
\overline{
\int
 a\,\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)\,d\mu_0
}>0.
}
\]

Here

\[
r_V=B_3-v_0
\]

is the material velocity relative to the local `kappa=0` surface and `dmu_0` is the original M5 base-label measure.

No spatial coarea substitution is made.

---

## 2. Localized pressure-production coefficient from M17-164

For each marked regular vertical crossing label `lambda`, center a radial cutoff at its marked spatial core and define

\[
\Pi_{\lambda,R}^{core}
:=-\int
\chi_R(Y_\lambda-y)
\,\kappa(y)\rho(y)^2
\,\mathcal K_{333}(Y_\lambda-y)dy.
\]

M17-164 gives, uniformly on a compact regular crossing hull,

\[
\boxed{
\Pi_{\lambda,R}^{core}
=c_\chi R^2O_{V,\lambda}
+\mathcal E_{\lambda,R},
}
\]

with

\[
\boxed{c_\chi:=\frac67m_\chi>0,}
\]

and

\[
|\mathcal E_{\lambda,R}|
\le C_*R^3.
\]

For a sharp ball, `c_chi=3/7`.

---

## 3. Define the localized production current in the same label measure

Define

\[
\boxed{
\mathcal C_R(\theta)
:=
\int
 a_\lambda
\frac{r_{V,\lambda}}{|Q_\lambda|_F^2}
\frac{\Pi_{\lambda,R}^{core}}{R^2}
\delta(\kappa_\lambda)
\,d\mu_0(\lambda).
}
\]

This is a pressure-production observable sampled on the same crossing labels and with exactly the same base-label measure as M5.

It is **not** a spatial volume integral over the present zero surface.

---

## 4. Small-core limit

Insert the M17-164 expansion:

\[
\begin{aligned}
\mathcal C_R
={}&c_\chi
\int
 a\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)d\mu_0\\
&+
\int
 a\frac{r_V}{|Q|_F^2}
\frac{\mathcal E_R}{R^2}
\delta(\kappa)d\mu_0.
\end{aligned}
\]

On a compact regular crossing hull assume the already retained bounds

\[
0<q_*\le |Q|_F,
\qquad
|a|+|r_V|\le C_*,
\]

and a finite crossing intensity under the M5 label current.
Then

\[
\left|
\int
 a\frac{r_V}{|Q|_F^2}
\frac{\mathcal E_R}{R^2}
\delta(\kappa)d\mu_0
\right|
\le C R.
\]

Therefore

\[
\boxed{
\mathcal C_R
\longrightarrow
c_\chi
\int
 a\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)d\mu_0
}
\]

as `R->0`.

---

## 5. Hysteresis now acts directly on localized pressure production

Time-average the preceding convergence. Under the same compact recurrence / dominated-crossing assumptions,

\[
\boxed{
\lim_{R\to0}
\overline{\mathcal C_R}
=
c_\chi
\overline{
\int
 a\frac{r_VO_V}{|Q|_F^2}
\delta(\kappa)d\mu_0
}.
}
\]

M17-095 makes the right-hand side strictly positive.
Hence

\[
\boxed{
\lim_{R\to0}
\overline{\mathcal C_R}>0.
}
\]

Equivalently, for all sufficiently small `R`,

\[
\boxed{
\overline{
\int
 a\frac{r_V}{|Q|_F^2}
\frac{\Pi_R^{core}}{R^2}
\delta(\kappa)d\mu_0
}>0.
}
\]

This is the first direct M5-to-pressure-production sign statement.

---

## 6. Relation to the original M5 current

At a regular crossing,

\[
h=-\frac{5r_V}{|Q|_F^2}O_V.
\]

Using the small-core coefficient,

\[
O_V
=\frac1{c_\chi R^2}\Pi_R^{core}+O(R).
\]

Thus the M5 current may be rewritten asymptotically as

\[
\boxed{
G_\Phi(0)
=-\frac{5}{c_\chi R^2}
\int a\frac{r_V}{|Q|_F^2}
\Pi_R^{core}
\delta(\kappa)d\mu_0
+O(R).
}
\]

The negative sign is exactly consistent with

\[
\overline{G_\Phi(0)}<0
\]

and

\[
\overline{\mathcal C_R}>0.
\]

---

## 7. What measure mismatch has now been removed

The old covariance firewall contained three logically different gaps:

1. local payer tensor versus global pressure source;
2. label measure versus present spatial measure;
3. local core versus global outer cancellation.

M17-164 removes Gap 1 for the `-kappa rho^2` production channel.
M17-165 avoids Gap 2 rather than removing it: the pressure-production core is sampled **inside the same label measure** as M5.

Thus the remaining gap is sharply reduced to:

\[
\boxed{
\text{relative-speed-weighted local production}
\quad\leftrightarrow?\quad
\text{unweighted full global axial STF production/transport}.
}
\]

---

## 8. The relative-speed factor remains essential

M5 controls

\[
r_V\Pi_R^{core},
\]

not `Pi_R^{core}` alone.
Therefore cancellation between crossings with opposite `r_V` remains possible.

Any theorem that drops `r_V` must control one of:

1. a fixed sign of `r_V` on the recurrent crossing population;
2. a lower bound on its conditional covariance with `Pi_R^{core}`;
3. a space-time crossing-flux identity that naturally includes `r_V` in the global production ledger.

No such theorem is assumed here.

---

## 9. Outer/global term remains signed

Write the full kappa-production channel at the marked core as

\[
\boxed{
\Pi_{V,\kappa}^{prod}
=
\Pi_{V,\kappa}^{core}(R)
+
\Pi_{V,\kappa}^{outer}(R).
}
\]

M17-165 controls only the first term in the relative-speed-weighted label average.
The outer term may have either sign because `K_333` changes sign.

Thus full global recurrence still requires either

\[
\boxed{
\text{core dominance / controlled outer covariance}
}
\]

or

\[
\boxed{
\text{an independent turnover cost for repeated outer cancellation}.
}
\]

---

## 10. DSD audit

### Audit A — converting `dmu_0` to spatial volume
Rejected. The new bridge deliberately stays in the label measure.

### Audit B — claiming the unweighted production sign
Rejected. The M5-controlled observable retains `r_V`.

### Audit C — dropping the `R^2` normalization
Rejected. A cubic source paired with the homogeneous degree `-4` kernel contributes at order `R^2`.

### Audit D — taking the time average before controlling the Taylor remainder
The compact crossing hull supplies uniform local fourth-jet bounds; dominated crossing intensity is required explicitly.

### Audit E — proof status
A genuine pressure-production sign bridge is obtained locally, but full global production/transport is not yet signed.

---

## 11. Updated vertical covariance gate

The local part of the old covariance firewall is now replaced by the exact statement

\[
\boxed{
\lim_{R\to0}
\overline{
\int
 a\frac{r_V}{|Q|_F^2}
\frac{\Pi_{V,\kappa}^{core}(R)}{R^2}
\delta(\kappa)d\mu_0
}>0.
}
\]

The next gate is to quantify the outer remainder

\[
\Pi_{V,\kappa}^{outer}(R)
\]

and determine whether repeated cancellation of this positive localized crossing-production bias can remain recurrent without paying an independent spatial/transport cost.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
