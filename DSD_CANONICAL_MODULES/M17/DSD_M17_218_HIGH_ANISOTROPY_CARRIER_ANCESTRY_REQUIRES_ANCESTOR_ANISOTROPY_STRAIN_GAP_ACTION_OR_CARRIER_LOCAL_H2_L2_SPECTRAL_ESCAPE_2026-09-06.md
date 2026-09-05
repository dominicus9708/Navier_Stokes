# DSD M17-218 — High-anisotropy carrier ancestry requires ancestor anisotropy, strain-gap action, or carrier-local H2/L2 spectral escape

Date: 2026-09-06  
Canonical ID: **M17-218**

Status: **RMS-SPECTRAL UPGRADE OF M17-217 / THE POINTWISE ANISOTROPY PULLBACK `K_+ <= K_- exp(I_T)` DOES NOT INVOLVE KAPPA. FOR A CURRENT HIGH-ANISOTROPY SET, USE THE EXACT M17-205 PUSHFORWARD MEASURE FIRST; ITS PULLBACK SPLITS INTO ANCESTOR ANISOTROPY OR LARGE STRAIN-GAP ACTION BEFORE ANY MASS-COMPARABILITY ASSUMPTION IS MADE. WHICHEVER MATERIAL SUBFAMILY CARRIES A FIXED CURRENT ENSTROPHY FRACTION THEN HAS ONLY TWO POSSIBILITIES: ITS OWN MATERIAL RMS MULTIPLIER `Lambda_S` STAYS BOUNDED, IN WHICH CASE M17-211 GIVES FIXED-LAG ENSTROPHY COMPARABILITY AND THE M17-217 ANCESTOR/ACTION LOWER BOUND; OR `Lambda_S` DIVERGES, WHICH IS EXACTLY A CARRIER-LOCAL H2/L2 SPECTRAL-CONCENTRATION EXIT. THUS POINTWISE BOUNDED KAPPA IS NOT REQUIRED. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Current high-anisotropy carrier

Fix a current remote shell `A_k^+`, lag `T>0`, threshold `K_0>1`, and retained regular Rank-2 set.

Define

\[
H^+
:=A_k^+\cap\{K_\xi^+\ge K_0\}\cap\mathcal R_{2,reg},
\]

where

\[
K_\xi:=\operatorname{cond}_+(\nabla\xi).
\]

Assume

\[
\boxed{
E_+(H^+)\ge\vartheta E_k^+,
\qquad\vartheta>0.
}
\]

Let

\[
H^-:=\Phi_T^{-1}(H^+).
\]

No pointwise bound on `kappa` is imposed.

---

## 2. Anisotropy ancestry split is independent of kappa

Define

\[
I_T(a)
:=\int_{\theta-T}^{\theta}\Gamma_\Sigma(\Phi(a,\tau),\tau)d\tau,
\]

with

\[
\Gamma_\Sigma
=\lambda_{max}(\Sigma)-\lambda_{min}(\Sigma).
\]

M17-216 gives

\[
\boxed{
K_\xi^+(\Phi_T(a))
\le K_\xi^-(a)e^{I_T(a)}.
}
\]

For every `L>0`, therefore,

\[
\boxed{
H^-
\subset
A^-_{anc}\cup A^-_{gap},
}
\]

where

\[
A^-_{anc}
:=H^-\cap\{K_\xi^-\ge K_0e^{-L}\},
\]

\[
A^-_{gap}
:=H^-\cap\{I_T\ge L\}.
\]

This split uses only material director frozenness and deformation geometry.

---

## 3. Use the exact transported enstrophy measure before comparability

For a measurable material subset `S^- subset H^-`, define its current transported enstrophy

\[
\boxed{
\mu_T(S^-)
:=E_+(\Phi_T(S^-)).
}
\]

M17-205 gives exactly

\[
\mu_T(S^-)
=
\int_{S^-}\rho_-^2
\exp\left[
\int_{\theta-T}^{\theta}
\left(2\sigma+2\kappa-\frac12\right)d\tau
\right]dy.
\]

Because

\[
H^-\subset A^-_{anc}\cup A^-_{gap},
\]

subadditivity gives

\[
E_+(H^+)
\le
\mu_T(A^-_{anc})+
\mu_T(A^-_{gap}).
\]

Hence

\[
\boxed{
\mu_T(A^-_{anc})
\ge\frac\vartheta2E_k^+
}
\]

or

\[
\boxed{
\mu_T(A^-_{gap})
\ge\frac\vartheta2E_k^+.
}
\]

This conclusion is exact and requires no pointwise bound on `kappa` and no pointwise bound on the transfer weight.

---

## 4. Material subfamily RMS multiplier

Let `S^-` denote whichever of `A^-_{anc}` or `A^-_{gap}` satisfies the corresponding lower bound.

Transport it through the interval:

\[
S(\tau):=\Phi_{\tau-(\theta-T)}(S^-).
\]

Define

\[
E_S(\tau)
:=\int_{S(\tau)}\rho^2dy
\]

and, whenever `E_S(τ)>0`,

\[
\boxed{
\Lambda_S^2(\tau)
:=
\frac{
\int_{S(\tau)}\kappa^2\rho^2dy
}{E_S(\tau)}
=
\frac{
\int_{S(\tau)}|\Delta W|^2dy
}{E_S(\tau)}.
}
\]

This is the M17-210/211 RMS spectral ratio applied to the actual material carrier selected by the anisotropy split.

---

## 5. Bounded-RMS branch

Assume along a sequence that for the selected carrier

\[
\boxed{
\sup_{\tau\in[\theta-T,\theta]}
\Lambda_S(\tau)
\le\Lambda_*<\infty.
}
\]

Assume also the compact smooth-hull strain bound used in M17-211,

\[
\|\sigma\|_{L^\infty}\le S_*.
\]

M17-211 then yields

\[
\boxed{
E_S(\theta-T)
\ge
e^{-C_*T}E_S(\theta),
}
\]

where

\[
C_*:=2S_*+\frac12+2\Lambda_*.
\]

Since

\[
E_S(\theta)=\mu_T(S^-)
\ge\frac\vartheta2E_k^+,
\]

we obtain

\[
\boxed{
E_-(S^-)
\ge
\frac\vartheta2e^{-C_*T}E_k^+.
}
\]

Thus bounded carrier-local RMS spectral ratio converts the exact transported-mass split into a genuine ancestor-enstrophy lower bound.

---

## 6. Ancestor-anisotropy branch

If

\[
S^-=A^-_{anc},
\]

then

\[
K_\xi^-
\ge K_0e^{-L}
\]

throughout `S^-`, and Section 5 gives

\[
\boxed{
E_-
\left(
H^-\cap\{K_\xi^-\ge K_0e^{-L}\}
\right)
\ge
\frac\vartheta2e^{-C_*T}E_k^+.
}
\]

Thus a fixed amount of current high-anisotropy carrier mass is inherited from a genuinely high-anisotropy material ancestor.

For a divergent threshold `K_n->infinity`, every fixed `L` preserves divergence because

\[
K_ne^{-L}\to\infty.
\]

---

## 7. Strain-gap action branch

If

\[
S^-=A^-_{gap},
\]

then

\[
I_T\ge L
\]

on `S^-`.

Section 5 gives

\[
E_-(S^-)
\ge
\frac\vartheta2e^{-C_*T}E_k^+.
\]

Therefore

\[
\boxed{
\int_{S^-}\rho_-^2I_Tdy
\ge
\frac{\vartheta L}{2}e^{-C_*T}E_k^+.
}
\]

This is a quantitative enstrophy-weighted fixed-lag strain-spectral-gap payment.

---

## 8. Unbounded-RMS branch

If no sequence-independent `Lambda_*` exists for the selected material carrier, then along a subsequence

\[
\boxed{
\sup_{\tau\in[\theta-T,\theta]}
\Lambda_S(\tau)
\to\infty.
}
\]

By definition,

\[
\Lambda_S^2
=
\frac{\int_{S(\tau)}|\Delta W|^2}
{\int_{S(\tau)}|W|^2}.
\]

Hence this is exactly a carrier-local normalized `H2/L2` spectral-concentration exit of the M17-210/211 type.

It is not relabeled as `kappa infinity`.

---

## 9. Strengthened three-way gate

Combining Sections 3--8 gives the corrected hard-shell implication

\[
\boxed{
G_{Eulerian\ high\ director\ anisotropy\ mass}
\Longrightarrow
G_{ancestor\ anisotropy}
\lor
H_{strain\ spectral\ gap\ action}
\lor
G_{carrier\text{-}local\ H2/L2\ spectral\ concentration}
}
\]

on every fixed-lag regular Rank-2 corridor, with rank/interface/domain failure retained outside the corridor.

Thus the pointwise bounded-`kappa` assumption of M17-217 is not needed for the corrected frontier.

---

## 10. Finite-shell localization and temperedness

Remote Type-I radial transport still implies

\[
\Phi_T^{-1}(A_k^+)
\subset
\mathcal N_{k,T}^-
\]

for a finite ancestor dyadic neighborhood.

If the relevant whole material neighborhood also has bounded RMS spectral ratio, M17-211 transfers its mass comparably to a finite current neighborhood.

On an M17-207 globally tempered current shell,

\[
\sum_{|m|\le M}E_{k+m}^+
\le C_{A,M}E_k^+.
\]

Hence

\[
E_-(\mathcal N_{k,T}^-)
\le C_{T,A,\Lambda_*}E_k^+.
\]

Together with the lower bounds in Sections 6 or 7, finite pigeonholing selects an ancestor shell on which the corresponding carrier occupies a fixed fraction of that ancestor shell mass.

If the whole-neighborhood RMS ratio is not bounded, that failure itself is the spectral-concentration branch.

---

## 11. Relation to M17-210 through M17-217

M17-210 identified weighted unbounded `kappa` with normalized `H2/L2` spectral concentration.

M17-211 showed bounded RMS `Lambda` is sufficient for fixed-lag material mass comparability and OU closure.

M17-212 split the spectral exit into amplitude curvature or director-metric concentration.

M17-213 split large Rank-2 director metric into director-area magnitude or anisotropy.

M17-214 closed enstrophy-dominant director-area concentration on the relative-thick compact-packet lane modulo explicit decompactification/thin exits.

M17-215/216 identified director anisotropy as inherited anisotropy or accumulated strain anisotropy.

M17-217 converted that pointwise law into an Eulerian/material mass statement under pointwise bounded `kappa`.

M17-218 removes that unnecessarily strong pointwise assumption and replaces its failure by the already-canonical RMS spectral exit.

---

## 12. DSD analysis

### 12.1 No subset-RMS inheritance assumption

A bounded RMS ratio on a parent shell does not automatically imply the same bound on every small selected subset.

M17-218 therefore computes `Lambda_S` on the selected material carrier itself.

If it is unbounded, that is retained as a spectral exit instead of being silently suppressed.

### 12.2 Exact measure before comparison

The logical order is:

\[
\text{current Eulerian mass}
\to
\text{material pullback}
\to
\text{pointwise ancestry split}
\to
\text{exact transported measure split}
\to
\text{RMS comparability or spectral exit}.
\]

This avoids using a mass-comparability theorem before verifying its hypotheses on the selected carrier.

### 12.3 No double counting

The carrier-local spectral branch is the same `H2/L2` mechanism already identified in M17-210/211, not a new independent payer.

---

## 13. DSD audit

- **M17-217 remains valid but specialized.** Its pointwise bounded-`kappa` corridor is a sufficient subcase of the new three-way gate.
- **No pointwise `kappa` ceiling is inferred from RMS control.**
- **No parent-to-subset RMS inheritance is assumed.** The selected carrier has its own `Lambda_S` test.
- **The spectral branch may recycle into the M17-212 director-metric branch.** This is an explicit possible cycle and is not claimed closed here.
- **The action branch is quantitative but not yet globally budgeted.**
- **Rank/interface/domain failure remains an external hard exit.**
- **Global regularity remains unproved.**

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
