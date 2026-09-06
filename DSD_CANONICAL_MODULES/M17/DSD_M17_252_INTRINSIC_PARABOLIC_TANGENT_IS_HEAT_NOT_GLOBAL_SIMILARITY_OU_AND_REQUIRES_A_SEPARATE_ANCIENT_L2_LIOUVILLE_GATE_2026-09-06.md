# DSD M17-252 — Intrinsic parabolic tangent is heat, not global similarity OU, and requires a separate ancient L2 Liouville gate

Date: 2026-09-06  
Canonical ID: **M17-252**

Status: **TIME-SCALE / LIMIT-EQUATION AUDIT. M17-249 CORRECTLY PROVES THAT A UNIFORMLY `L2`-BOUNDED ANCIENT SOLUTION OF THE GLOBAL LINEAR SIMILARITY VORTICITY EQUATION MUST VANISH. HOWEVER THE OWN-SCALE PACKET BLOW-UP USED AFTER M17-250/251 HAS TIME SCALE `r_j^2` AND A MOVING MATERIAL CENTER. ON THAT SCALE THE SIMILARITY DRIFT, LINEAR `-W` TERM, AND BOUNDED STRAIN ALL ACQUIRE `r_j^2` FACTORS; UNDER THE NO-PAYER COEFFICIENT BRANCH THE LOCAL LIMIT EQUATION IS THE HEAT EQUATION `partial_tau V=Delta V`, NOT THE GLOBAL SIMILARITY OU EQUATION. A SEPARATE FOURIER ARGUMENT SHOWS THAT A UNIFORMLY GLOBAL-`L2`-BOUNDED ANCIENT HEAT SOLUTION ON `R3` IS ZERO. THE NEW OBSTRUCTION IS THEREFORE NOT THE LIOUVILLE ENDPOINT ITSELF BUT THE EXTRACTION OF A NONZERO ANCIENT HEAT TANGENT WITH ENOUGH SPATIAL `L2` TIGHTNESS AND DERIVATIVE-CHARGE RETENTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Correction to the M17-251 time-zero compactness wording

M17-251 obtains, on the retained-inner-mass branch,

\[
\boxed{
\|V_j\|_{H^2(B^{in})}\le C,
\qquad
\|V_j\|_{L^2(B^{in})}^2\ge\eta>0.
}
\]

Here `B_in` is one fixed bounded smooth/Lipschitz rescaled domain.

Therefore the direct Rellich embedding

\[
\boxed{
H^2(B^{in})\Subset L^2(B^{in})
}
\]

already gives, after subsequence,

\[
V_j\to V_0
\quad\text{strongly in }L^2(B^{in}),
\]

and hence

\[
\boxed{
\|V_0\|_{L^2(B^{in})}^2
\ge\eta.
}
\]

Thus

\[
\boxed{V_0\not\equiv0.}
\]

No extra inner recentering is required for the time-zero nonzero limit.

This note is the canonical clarification of that point.

---

## 2. Similarity vorticity equation and moving center

The CE-H similarity vorticity dynamics used in M17-225 have the form

\[
\boxed{
\partial_\theta W+B\cdot\nabla W
=
\Delta W+\Sigma W-W,
}
\]

with

\[
B=U+\frac12y
\]

and the exact similarity divergence

\[
\nabla\cdot B=\frac32.
\]

Let `q_j(theta)` be the material center satisfying

\[
\boxed{
\dot q_j(\theta)=B(q_j(\theta),\theta).
}
\]

Let `r_j` be the scale-comparable packet radius from M17-250/251.

Use the own parabolic time

\[
\boxed{
\theta=\theta_j+r_j^2\tau
}
\]

and spatial scale

\[
\boxed{
y=q_j(\theta)+r_jz.}
\]

Normalize amplitude by a fixed packet amplitude `a_j>0` and write

\[
\boxed{
W(y,\theta)=a_jV_j(z,\tau).
}
\]

---

## 3. Exact own-scale rescaled equation

A direct chain-rule calculation gives

\[
\boxed{
\partial_\tau V_j
+r_j\bigl[B(q_j+r_jz,\theta)-B(q_j,\theta)\bigr]\cdot\nabla_zV_j
=
\Delta_zV_j
+r_j^2\Sigma_jV_j
-r_j^2V_j.
}
\]

Define the rescaled drift gradient size

\[
\mathfrak B_j(K,T)
:=
 r_j^2
 \sup_{|\tau|\le T}
 \sup_{|z|\le K}
 |\nabla B(q_j+r_jz,\theta_j+r_j^2\tau)|
\]

and the rescaled strain size

\[
\mathfrak S_j(K,T)
:=
 r_j^2
 \sup_{|\tau|\le T}
 \sup_{|z|\le K}
 |\Sigma(q_j+r_jz,\theta_j+r_j^2\tau)|.
\]

Then for fixed `K,T`,

\[
\left|
 r_j[B(q_j+r_jz)-B(q_j)]
\right|
\le
K\mathfrak B_j(K,T).
\]

Therefore, on a branch where

\[
\boxed{
\mathfrak B_j(K,T)+\mathfrak S_j(K,T)\to0
\qquad\text{for every fixed }K,T,
}
\]

the lower-order similarity coefficients disappear.

The term `-r_j^2V_j` also vanishes automatically.

---

## 4. Correct intrinsic limit equation

If the normalized fields have enough spacetime compactness to pass to a limit and the scaled coefficient condition in Section 3 holds, then the limit solves

\[
\boxed{
\partial_\tau V=\Delta V.
}
\]

This is the **heat equation**.

It is not

\[
\partial_\theta V+\frac12z\cdot\nabla V
=\Delta V-V.
\]

The latter is the global similarity-scale linear equation studied in M17-249.

The two equations arise from different limiting procedures:

- M17-249 keeps the global similarity spatial/time scale;
- M17-252 zooms to a packet of radius `r_j->0` and time `r_j^2` around a moving material center.

Thus

\[
\boxed{
\text{global similarity linear endpoint}
\neq
\text{intrinsic parabolic tangent endpoint}.
}
\]

---

## 5. Bounded ancient `L2` heat solutions vanish

Let

\[
V\in C(( -\infty,0];L^2(\mathbb R^3))
\]

solve

\[
\partial_\tau V=\Delta V
\]

and assume

\[
\boxed{
\sup_{\tau\le0}\|V(\tau)\|_2\le C_*<\infty.
}
\]

For every `T>0`, Fourier evolution gives

\[
\widehat V(\xi,0)
=e^{-T|\xi|^2}\widehat V(\xi,-T).
\]

Fix `delta>0`.

Then

\[
\begin{aligned}
\int_{|\xi|\ge\delta}|\widehat V(\xi,0)|^2d\xi
&\le
 e^{-2T\delta^2}
 \|V(-T)\|_2^2\\
&\le
 C_*^2e^{-2T\delta^2}.
\end{aligned}
\]

Letting `T->infinity`,

\[
\int_{|\xi|\ge\delta}|\widehat V(\xi,0)|^2d\xi=0.
\]

Since this holds for every `delta>0`, `widehat V(.,0)` is supported in the single point `xi=0`.

An `L2` function supported on a measure-zero set is zero.

Therefore

\[
V(0)=0.
\]

Forward uniqueness for the heat equation gives

\[
\boxed{V\equiv0.}
\]

Hence

\[
\boxed{
\text{uniformly global-}L^2\text{-bounded ancient heat solution}
\Longrightarrow0.
}
\]

---

## 6. Why the endpoint is not yet applicable

M17-251 only gives a nonzero **local time-zero** tangent.

It does not give the hypotheses of Section 5.

Three separate gaps remain.

### 6.1 Backward lifetime

To obtain an ancient limit, the normalized backward lifespan must satisfy

\[
\boxed{
\frac{T_j^{back}}{r_j^2}\to\infty.
}
\]

A fixed one-parabolic-lifetime corridor is not enough.

### 6.2 Spacetime compactness

For every fixed `K,T`, one needs sufficient uniform estimates on

\[
B_K\times[-T,0]
\]

to extract a diagonal ancient caloric limit.

Time-zero `H2` compactness alone does not imply this.

### 6.3 Global normalized `L2` tightness

The packet normalization uses

\[
a_j^2r_j^3=E_j.
\]

The full-space normalized mass is

\[
\frac{\|W_j\|_{L^2(\mathbb R^3)}^2}{E_j},
\]

which may diverge because `E_j->0`.

Therefore the global `L2` bound required by the heat Liouville theorem is **not inherited automatically**.

This is a new explicit concentration-compactness firewall.

---

## 7. Local heat limits are not enough

A nonzero heat solution on a bounded cylinder is not contradictory.

Even an ancient heat solution with no global `L2` control may be nonzero.

For example constants are ancient caloric functions, though not in `L2(R3)`.

Therefore the valid target is not merely

\[
V_j\to V\not\equiv0
\]

locally.

One needs an additional condition excluding loss of normalized mass to spatial infinity or convergence to an unbudgeted non-`L2` caloric profile.

The next useful gate is therefore a **normalized tangent tightness / growth gate**.

---

## 8. Derivative-charge retention is also separate

At time zero, scale comparability controls a raw second-derivative ratio.

However weak `H2` convergence does not preserve a positive `H2` norm lower bound.

Thus it is possible in principle for

\[
\|\Delta V_j\|_2\gtrsim1
\]

while

\[
\Delta V_j\rightharpoonup0.
\]

The nonzero `L2` limit from M17-251 could then be locally closer to a low-frequency or constant caloric profile.

Hence a second next-step target is a **derivative-charge no-defect gate** or an explicit identification of the defect as another strict subscale concentration.

---

## 9. Corrected frontier after M17-252

The intrinsic linear route should now be recorded as

\[
\boxed{
H_{scale\text{-}comparable\ nonzero\ time\text{-}zero\ tangent}
\Longrightarrow
H_{nonzero\ ancient\ heat\ tangent\ with\ global\ L2\ tightness}
\lor
G_{backward\ replenishment}
\lor
G_{spacetime\ compactness\ loss}
\lor
G_{normalized\ mass\ decompactification}
\lor
G_{derivative\ defect/subscale}
\lor
G_{ambient/interface\ forcing}.
}
\]

If the first branch is obtained, Section 5 closes it immediately:

\[
\boxed{
V\not\equiv0
\quad\text{and}\quad
V\text{ bounded ancient }L2\text{ heat}
\Longrightarrow\bot.
}
\]

---

## 10. DSD audit

- M17-249 remains valid on its global similarity-scale linear branch.
- M17-249 is not silently applied to an intrinsic `r_j^2` packet blow-up.
- The own-scale tangent equation is derived explicitly before taking a limit.
- Heat Liouville is proved separately by Fourier decay.
- Local nonzero convergence is not confused with global `L2` tightness.
- A positive prelimit `H2` lower bound is not assumed to survive weak convergence.
- Backward lifetime is retained as an independent obligation.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
