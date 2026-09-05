# DSD M17-217 — Eulerian high director-anisotropy mass pulls back to ancestor anisotropy or fixed-lag strain-gap action

Date: 2026-09-06  
Canonical ID: **M17-217**

Status: **EULERIAN/MATERIAL ANISOTROPY BRIDGE / ON A FIXED-LAG REGULAR RANK-2 MATERIAL CORRIDOR, M17-216 GIVES `K_+ <= K_- exp(I_T)`, WHERE `K=cond_+(grad xi)` AND `I_T=int Gamma_Sigma`. THEREFORE THE PULLBACK OF THE CURRENT HIGH-ANISOTROPY SET `{K_+>=K0}` IS CONTAINED IN `{K_->=K0 exp(-L)} UNION {I_T>=L}` FOR EVERY `L>0`. M17-205'S EXACT MATERIAL ENSTROPHY TRANSFER THEN CONVERTS THIS POINTWISE DICHOTOMY INTO AN ENSTROPHY-MASS DICHOTOMY. ON A GLOBALLY TEMPERED CURRENT SHELL, M17-207 CONTROLS THE FINITE ANCESTOR-SHELL NEIGHBORHOOD. HENCE A FIXED-FRACTION EULERIAN HIGH-ANISOTROPY PACKET MUST EITHER HAVE A FIXED-LAG HIGH-ANISOTROPY MATERIAL ANCESTOR AT THE LOWERED THRESHOLD OR PLACE A FIXED ENSTROPHY FRACTION ON TRAJECTORIES WITH NONTRIVIAL ACCUMULATED STRAIN SPECTRAL-GAP ACTION. THIS CLOSES `FRESH EULERIAN IMPORT` AS A FREE LABEL ON THE REGULAR TEMPERED LANE; IT DOES NOT BOUND THE STRAIN-GAP ACTION OR PROVE GLOBAL REGULARITY.**

---

## 1. Setting and notation

Fix a similarity time `theta` and a finite lag

\[
T>0.
\]

Let

\[
\Phi_T:a\mapsto y
\]

be the material flow of

\[
B=U+\frac12y
\]

from `theta-T` to `theta`.

Work on a retained material corridor on which:

\[
|\sigma|\le S_*,
\qquad
|\kappa|\le K_*,
\]

and the director differential remains regular Rank-2.

Define

\[
\boxed{
K_\xi(y,\tau)
:=\operatorname{cond}_+(\nabla\xi(y,\tau))
=\frac{s_1}{s_2}\ge1.
}
\]

Define the strain spectral gap

\[
\boxed{
\Gamma_\Sigma
:=\lambda_{max}(\Sigma)-\lambda_{min}(\Sigma)\ge0
}
\]

and its material fixed-lag action

\[
\boxed{
I_T(a)
:=\int_{\theta-T}^{\theta}
\Gamma_\Sigma(\Phi_{\tau-(\theta-T)}(a),\tau)\,d\tau.
}
\]

---

## 2. Pointwise ancestry dichotomy

M17-216 gives, along every retained Rank-2 material carrier,

\[
\boxed{
K_\xi^+(\Phi_T(a))
\le
K_\xi^-(a)e^{I_T(a)}.
}
\]

Fix a current anisotropy threshold

\[
K_0>1
\]

and an action threshold

\[
L>0.
\]

If

\[
K_\xi^+(\Phi_T(a))\ge K_0,
\]

then it is impossible to have simultaneously

\[
K_\xi^-(a)<K_0e^{-L}
\]

and

\[
I_T(a)<L.
\]

Hence

\[
\boxed{
\Phi_T^{-1}\{K_\xi^+\ge K_0\}
\subset
\{K_\xi^-\ge K_0e^{-L}\}
\cup
\{I_T\ge L\}.
}
\]

This is an exact logical split, not a probabilistic estimate.

---

## 3. Exact enstrophy push-forward

M17-205 gives for every material set `A_-`

\[
\int_{\Phi_T(A_-)}\rho_+^2dy
=
\int_{A_-}\rho_-^2w_T(a)da,
\]

where

\[
\boxed{
w_T(a)
:=
\exp\left[
\int_{\theta-T}^{\theta}
\left(2\sigma+2\kappa-\frac12\right)d\tau
\right].
}
\]

On the retained bounded corridor,

\[
\boxed{
e^{-C_T}\le w_T\le e^{C_T},}
\]

with

\[
C_T=T(2S_*+2K_*+1/2).
\]

Thus the exact transported enstrophy measure is equivalent, with fixed-lag constants, to ancestor enstrophy measure.

---

## 4. Current high-anisotropy set

Let `A_k^+` be a remote current dyadic shell and define its retained high-anisotropy subset

\[
\boxed{
H_{k,K_0}^+
:=
A_k^+
\cap
\{K_\xi^+\ge K_0\}
\cap
\mathcal R_{2,reg},
}
\]

where `R_{2,reg}` denotes the retained regular Rank-2 corridor.

Let

\[
H^-:=\Phi_T^{-1}(H_{k,K_0}^+).
\]

By Section 2,

\[
H^-
\subset
H^-_{anc}(K_0e^{-L})
\cup
H^-_{gap}(L),
\]

where

\[
H^-_{anc}(K_0e^{-L})
:=H^-\cap\{K_\xi^-\ge K_0e^{-L}\},
\]

\[
H^-_{gap}(L)
:=H^-\cap\{I_T\ge L\}.
\]

Using the exact push-forward and `w_T<=e^{C_T}`,

\[
\boxed{
E_+(H_{k,K_0}^+)
\le
e^{C_T}
\left[
E_-(H^-_{anc})
+
E_-(H^-_{gap})
\right].
}
\]

Here

\[
E_\pm(S):=\int_S\rho_\pm^2dy.
\]

---

## 5. Finite ancestor-shell neighborhood

M17-205's remote radial transport law

\[
|y_+|^2=e^T|y_-|^2+O_T(1)
\]

has the inverse fixed-lag consequence that the pullback of one sufficiently remote current dyadic shell lies in finitely many ancestor dyadic neighbors.

Thus there are fixed integers `s_T^-` and `M_T^-` such that

\[
\boxed{
H^-
\subset
\bigcup_{|m|\le M_T^-}
A_{k+s_T^-+m}^-.
}
\]

Denote this finite union by

\[
\mathcal N_{k,T}^-.
\]

No Eulerian shell is being silently identified with a material set; the material pullback is taken first.

---

## 6. Tempered-shell normalization

Suppose the current shell index `k` lies in the globally tempered family of M17-207.

For every fixed finite current-neighbor width,

\[
\sum_{|m|\le M}E_{k+m}^+
\le C_{A,M}E_k^+.
\]

Apply the M17-205 fixed-lag shell transfer to each of the finitely many ancestor shells in `N_{k,T}^-` and use the tempered current-neighborhood bound.

Because the number and offsets of those shells depend only on fixed `T`, one obtains

\[
\boxed{
E_-(\mathcal N_{k,T}^-)
\le C_{T,A}E_k^+.
}
\]

Thus the entire relevant ancestor neighborhood has a uniform normalization by the current shell mass on the tempered family.

---

## 7. Fixed-fraction anisotropy dichotomy

Assume the current high-anisotropy set carries a fixed shell fraction:

\[
\boxed{
E_+(H_{k,K_0}^+)
\ge\vartheta E_k^+,
\qquad
\vartheta>0.
}
\]

Section 4 gives

\[
\vartheta E_k^+
\le
e^{C_T}
\left[
E_-(H^-_{anc})+E_-(H^-_{gap})
\right].
\]

Therefore at least one of the two terms satisfies

\[
\boxed{
E_-(H^-_{anc})
\ge\frac{\vartheta}{2}e^{-C_T}E_k^+
}
\]

or

\[
\boxed{
E_-(H^-_{gap})
\ge\frac{\vartheta}{2}e^{-C_T}E_k^+.
}
\]

Consequently

\[
\boxed{
G_{Eulerian\ high\ anisotropy\ mass}
\Longrightarrow
G_{fixed\!-\!lag\ ancestor\ anisotropy}
\lor
H_{fixed\!-\!lag\ strain\!-\!gap\ action}.
}
\]

The ancestor threshold is explicitly

\[
K_0e^{-L},
\]

not `K_0`; the loss in threshold is the exact price allowed by an action budget below `L`.

---

## 8. Quantitative action payment

On the second branch,

\[
I_T\ge L
\]

on a set carrying at least

\[
\frac{\vartheta}{2}e^{-C_T}E_k^+
\]

of ancestor enstrophy.

Therefore

\[
\boxed{
\int_{\mathcal N_{k,T}^-}
\rho_-^2 I_T\,dy
\ge
\frac{\vartheta L}{2}e^{-C_T}E_k^+.
}
\]

So the strain-gap branch is not merely a label: it carries a quantitative enstrophy-weighted action charge.

Since

\[
I_T
=\int_{\theta-T}^{\theta}\Gamma_\Sigma\,d\tau,
\]

this charge is a fixed-lag spacetime strain-anisotropy payer.

It is not yet shown to be globally summable or incompatible with Navier--Stokes regularity assumptions.

---

## 9. Divergent-threshold consequence

Let a tempered shell sequence satisfy

\[
K_n\to\infty
\]

and

\[
E_+(H_{k_n,K_n}^+)\ge\vartheta E_{k_n}^+.
\]

For every fixed `T>0` and `L>0`, M17-217 yields along a subsequence at least one of:

\[
\boxed{
E_-
\left(
\mathcal N_{k_n,T}^-
\cap
\{K_\xi^-\ge K_ne^{-L}\}
\right)
\gtrsim_{T,\vartheta}E_{k_n}^+
}
\]

or

\[
\boxed{
\int_{\mathcal N_{k_n,T}^-}
\rho_-^2 I_T\,dy
\gtrsim_{T,\vartheta,L}E_{k_n}^+.
}
\]

Because `K_ne^{-L}->infinity` for fixed `L`, the first alternative preserves divergent anisotropy backward by one fixed material lag.

Thus fresh current Eulerian anisotropy cannot repeatedly appear from uniformly bounded-anisotropy ancestors without paying the second branch.

---

## 10. DSD analysis

### 10.1 Eulerian/material separation

The current shell subset is Eulerian.
It is first pulled back by `Phi_T^{-1}` before any material identity is applied.
This prevents the support error corrected earlier in M17-178--183 from being repeated in a different form.

### 10.2 State-versus-history split

Current large anisotropy is a state variable.
Ancestor large anisotropy is inherited state.
`I_T` is a historical path functional.

The theorem keeps them distinct:

\[
\text{current state}
\Longrightarrow
\text{ancestor state}
\lor
\text{path action}.
\]

### 10.3 Threshold bookkeeping

Backward inheritance lowers the anisotropy threshold by exactly `e^{-L}`.
No claim is made that the same numerical threshold survives backward transport.

### 10.4 Resolution boundary

The argument applies only while the material carrier stays inside the retained regular Rank-2 corridor.
Rank loss, director-domain loss, unbounded `kappa`, or failure of the compact strain hull is exported as an explicit branch rather than absorbed into the estimate.

---

## 11. DSD audit

- **Fixed lag only.** Iteration to arbitrarily long backward time requires a separate ancestry-chain extraction.
- **No action-budget closure.** A positive lower bound on enstrophy-weighted `I_T` is a payer identification, not a contradiction.
- **No hidden shell/material identification.** `H^-=Phi_T^{-1}(H^+)` is materialized before applying M17-205.
- **Temperedness is used only for normalization.** The pointwise ancestry dichotomy and exact material-set transfer hold without M17-207; temperedness controls the finite shell neighborhood relative to `E_k^+`.
- **Threshold degradation is explicit.** `K_0` becomes `K_0 e^{-L}` on the ancestor branch.
- **Failure of bounded `kappa` or compact strain is not ignored.** Such failure leaves the retained lane and is already an explicit hard exit.
- **Carrier-fraction loss is visible.** If the high-anisotropy set ceases to carry a fixed enstrophy fraction, it cannot by itself carry the hard shell stack.
- **No global regularity claim.** The result removes `fresh Eulerian import` as a free terminal explanation on this lane but does not yet rule out an infinite backward anisotropy ancestry chain or repeated strain-gap payment.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
