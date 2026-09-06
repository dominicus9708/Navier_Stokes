# DSD M17-219 — Divergent director-metric second moment splits into a fixed-fraction high-metric carrier or a vanishing-enstrophy microcarrier

Date: 2026-09-06  
Canonical ID: **M17-219**

Status: **MEASURE-BRIDGE CORRECTION / M17-212 GIVES DIVERGENCE OF THE ENSTROPHY-NORMALIZED SECOND MOMENT OF THE DIRECTOR METRIC, BUT THAT DOES NOT BY ITSELF GIVE A FIXED-ENSTROPHY-FRACTION HIGH-METRIC SET. WITH THE SHELL ENSTROPHY PROBABILITY MEASURE `dmu=rho^2/E_R dy`, THE DIVERGENT MOMENT `Q_R=int g^2 dmu`, `g=|grad xi|^2`, HAS AN EXACT CONCENTRATION-COMPACTNESS DICHOTOMY: EITHER SOME DIVERGING METRIC THRESHOLD IS CARRIED BY A FIXED POSITIVE `mu` FRACTION, OR THE FAMILY IS TIGHT IN `mu`-MEASURE WHILE ITS SECOND MOMENT IS NOT UNIFORMLY INTEGRABLE, SO VANISHING-`mu` SETS CARRY DIVERGENT METRIC-SQUARED COST. ONLY THE FIRST BRANCH MAY BE SENT DIRECTLY INTO M17-214/218. ON THAT BRANCH THE EXACT FACTORIZATION `g=2|J_xi| A_xi` FURTHER SPLITS THE FIXED-FRACTION CARRIER INTO LARGE DIRECTOR AREA OR LARGE CONDITION NUMBER. THE SECOND BRANCH IS A DISTINCT SPARSE SPECTRAL/DIRECTOR MICROCARRIER AND MUST NOT BE SILENTLY IDENTIFIED WITH FIXED-FRACTION ANISOTROPY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Shell probability measure

Let `C_R` be a remote shell with

\[
E_R:=\int_{C_R}\rho^2dy>0.
\]

Define the enstrophy probability measure

\[
\boxed{
d\mu_R:=\frac{\rho^2}{E_R}dy,
\qquad
\mu_R(C_R)=1.
}
\]

On the regular Rank-2 set put

\[
\boxed{g_R:=|\nabla\xi|^2.}
\]

The director-metric branch of M17-212 is precisely

\[
\boxed{
Q_R:=\int_{C_R}g_R^2\,d\mu_R
=\frac{\int_{C_R}\rho^2|\nabla\xi|^4dy}{E_R}
\to\infty.
}
\]

This is a second-moment statement. It is not yet a fixed-mass statement.

---

## 2. Fixed-fraction high-metric alternative

Call the sequence **fixed-fraction high metric** if there exist

\[
\vartheta>0,
\qquad
M_j\to\infty
\]

and a shell subsequence `R_j` such that

\[
\boxed{
\mu_{R_j}\{g_{R_j}\ge M_j\}\ge\vartheta.
}
\]

Equivalently,

\[
\boxed{
\int_{\{g_{R_j}\ge M_j\}}\rho^2dy
\ge\vartheta E_{R_j}.
}
\]

This is exactly the type of positive-enstrophy-fraction carrier required by the later material ancestry modules.

---

## 3. If the fixed-fraction alternative fails, the metric family is tight in enstrophy measure

Suppose no fixed `vartheta>0` admits diverging thresholds with the property in Section 2.

Then for every `epsilon>0` there is a finite `M_epsilon` such that, after passage to a tail of the sequence,

\[
\boxed{
\mu_R\{g_R>M_\epsilon\}<\epsilon.
}
\]

Indeed, if this failed for some `epsilon_0>0`, then for every integer `m` there would be infinitely many shells satisfying

\[
\mu_R\{g_R>m\}\ge\epsilon_0.
\]

A diagonal choice with `m->infinity` would produce the fixed-fraction alternative of Section 2.

Thus failure of fixed-fraction high metric is equivalent, after subsequence extraction, to tightness of `g_R` in `mu_R`-measure.

---

## 4. Divergent second moment plus measure tightness forces a sparse microcarrier

Assume the tight branch of Section 3 and still

\[
Q_R\to\infty.
\]

Choose `epsilon_j=1/j`.
For each `j`, tightness gives a finite threshold `M_j` and a tail on which

\[
\mu_R\{g_R>M_j\}\le\frac1j.
\]

Since `Q_R->infinity`, choose a further shell `R_j` in that tail such that

\[
Q_{R_j}\ge jM_j^2.
\]

Set

\[
\boxed{S_j:=\{g_{R_j}>M_j\}.}
\]

Then

\[
\boxed{
\mu_{R_j}(S_j)\le\frac1j\to0.
}
\]

But outside `S_j`,

\[
\int_{C_{R_j}\setminus S_j}g_{R_j}^2d\mu_{R_j}
\le M_j^2.
\]

Hence

\[
\begin{aligned}
\int_{S_j}g_{R_j}^2d\mu_{R_j}
&=Q_{R_j}-\int_{C_{R_j}\setminus S_j}g_{R_j}^2d\mu_{R_j}\\
&\ge (j-1)M_j^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\mu_{R_j}(S_j)\to0,
\qquad
\int_{S_j}g_{R_j}^2d\mu_{R_j}\to\infty.
}
\]

The normalized director-metric cost is thus carried by a vanishing-enstrophy set.

Call this branch

\[
\boxed{G_{director\text{-}metric\ microcarrier}.}
\]

---

## 5. Exact concentration-compactness dichotomy

Sections 2--4 give

\[
\boxed{
Q_R\to\infty
\Longrightarrow
G_{fixed\text{-}fraction\ high\ metric}
\lor
G_{director\text{-}metric\ microcarrier}.
}
\]

The alternatives refer to the enstrophy measure, not Euclidean volume.

The microcarrier may have small volume, moderate volume with very small amplitude weight, or a mixture; only its enstrophy fraction is forced to vanish.

---

## 6. Fixed-fraction metric carrier splits into area or anisotropy with fixed fraction

On Rank-2 points let

\[
s_1\ge s_2>0,
\qquad
K_\xi:=\frac{s_1}{s_2}\ge1,
\]

and

\[
\mathcal A_\xi
:=\frac{s_1^2+s_2^2}{2s_1s_2}
=\frac12\left(K_\xi+K_\xi^{-1}\right).
\]

M17-213 gives

\[
\boxed{
g_R=|\nabla\xi|^2
=2|J_\xi|\mathcal A_\xi.
}
\]

Suppose

\[
\mu_R\{g_R\ge M\}\ge\vartheta.
\]

On the set `g_R>=M`, at least one of

\[
|J_\xi|\ge M^{1/2}
\]

or

\[
\mathcal A_\xi\ge\frac12M^{1/2}
\]

must hold; otherwise `2|J_xi| A_xi<M`.

Hence by subadditivity one of the two sets carries at least half the enstrophy fraction:

\[
\boxed{
\mu_R\{|J_\xi|\ge M^{1/2}\}
\ge\frac\vartheta2
}
\]

or

\[
\boxed{
\mu_R\{\mathcal A_\xi\ge\tfrac12M^{1/2}\}
\ge\frac\vartheta2.
}
\]

For large `M`, the second inequality forces

\[
\boxed{K_\xi\ge cM^{1/2}}
\]

on a fixed-fraction subcarrier, with a universal positive `c`.

Thus

\[
\boxed{
G_{fixed\text{-}fraction\ high\ metric}
\Longrightarrow
G_{fixed\text{-}fraction\ high\ area}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}.
}
\]

---

## 7. Consequence on the relative-thick compact packet lane

M17-214 rules out an enstrophy-dominant `|J_xi|->infinity` sequence when total director flux, fiber length, packet volume, and amplitude comparability remain compact.

Therefore, on that lane,

\[
\boxed{
G_{fixed\text{-}fraction\ high\ metric}
\Longrightarrow
G_{fixed\text{-}fraction\ high\ anisotropy}
}
\]

modulo the already explicit exits

\[
G_{relative\text{-}thin/amplitude\ concentration},
\quad
G_{director\ flux\ decompactification},
\quad
G_{fiber\ length\ decompactification},
\quad
G_{rank/interface/domain}.
\]

Only now is the hypothesis of M17-218 justified measure-theoretically.

---

## 8. Corrected spectral-to-anisotropy chain

The valid chain from M17-212 is not simply

\[
G_{director\ metric^2}\to G_{anisotropy}.
\]

It is

\[
\boxed{
G_{director\ metric^2}
\Longrightarrow
G_{director\text{-}metric\ microcarrier}
\lor
G_{fixed\text{-}fraction\ high\ area}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}.
}
\]

On the relative-thick compact packet lane the high-area branch is closed by M17-214, leaving

\[
\boxed{
G_{director\ metric^2}^{compact}
\Longrightarrow
G_{director\text{-}metric\ microcarrier}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}.
}
\]

The second branch may enter M17-218.
The first may not.

---

## 9. Relation to spectral concentration

M17-212 starts from

\[
\Lambda_R^2
\le
2\frac{\int|\Delta\rho|^2}{E_R}
+2Q_R.
\]

Therefore the full spectral exit has the refined split

\[
\boxed{
G_{H2/L2\ spectral}
\Longrightarrow
G_{amplitude\ curvature}
\lor
G_{fixed\text{-}fraction\ high\ anisotropy}
\lor
G_{director\text{-}metric\ microcarrier}
\lor
G_{thin/decompactification/interface}.
}
\]

The microcarrier is the measure-theoretic residual that was not represented in the previous compressed frontier.

---

## 10. DSD analysis

### 10.1 Quantity type

`Q_R` is a second moment under the enstrophy probability measure.
A divergent second moment can be caused by either a macroscopic carrier or non-uniform integrability on microscopic mass.

### 10.2 Scope correction

M17-214 and M17-218 are fixed-fraction statements.
M17-219 does not weaken them; it supplies the missing gate deciding when their hypotheses are actually available.

### 10.3 No volume substitution

`mu_R(S)->0` does not imply `|S|->0` without amplitude information.
The residual is therefore called an enstrophy microcarrier rather than a small-volume set.

---

## 11. DSD audit

- A divergent `L2(mu_R)` norm is not converted into fixed positive `mu_R` mass at a divergent threshold without the explicit dichotomy above.
- The sparse branch is retained rather than hidden inside `anisotropy`.
- The high-area/high-anisotropy split preserves a fixed mass fraction by a two-set pigeonhole argument.
- M17-218 remains valid exactly on the fixed-fraction anisotropy branch.
- No contradiction is claimed for the microcarrier branch.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
