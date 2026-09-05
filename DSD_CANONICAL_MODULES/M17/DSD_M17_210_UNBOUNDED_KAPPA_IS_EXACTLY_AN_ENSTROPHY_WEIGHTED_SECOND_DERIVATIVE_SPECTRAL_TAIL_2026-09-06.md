# DSD M17-210 — Unbounded kappa is exactly an enstrophy-weighted second-derivative spectral tail

Date: 2026-09-06  
Canonical ID: **M17-210**

Status: **UNBOUNDED-KAPPA REPARAMETRIZATION / ON THE CE-H ACTIVE SET, `Delta W = kappa W` IMPLIES THE POINTWISE EXACT IDENTITY `kappa^2 rho^2 = |Delta W|^2`. THUS THE ENSTROPHY-WEIGHTED SECOND MOMENT OF KAPPA IS NOT A NEW QUOTIENT QUANTITY: IT IS EXACTLY THE `L2` SECOND-DERIVATIVE ENERGY OF VORTICITY. HIGH-`|kappa|` SETS HAVE A UNIFORM CHEBYSHEV ENSTROPHY TAIL `int_{|kappa|>K} rho^2 <= K^-2 ||Delta W||_2^2`. CONSEQUENTLY, FOR HIGH-`|kappa|` TO CARRY A FIXED FRACTION OF A REMOTE HARD SHELL, THE SHELL'S NORMALIZED `H2/L2` SPECTRAL RATIO MUST DIVERGE. THIS REPLACES THE UNTYPED `kappa,infinity` EXIT BY A PRECISE HIGH-FREQUENCY SPECTRAL-CONCENTRATION BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact CE-H multiplier identity

On the active set

\[
\rho=|W|>0,
\]

CE-H gives

\[
\boxed{\Delta W=\kappa W.}
\]

Taking norms,

\[
\boxed{|\Delta W|^2=\kappa^2|W|^2=\kappa^2\rho^2.}
\]

This is pointwise and requires no integration by parts.

---

## 2. Global weighted second moment

Integrating over the active set, with the nodal set contributing zero to both sides by continuity of `Delta W=kappa W` in its vector form,

\[
\boxed{
\int_{\mathbb R^3}\kappa^2\rho^2dy
=\int_{\mathbb R^3}|\Delta W|^2dy
=\|\Delta W\|_2^2.
}
\]

Thus the enstrophy-weighted kappa second moment is exactly the vorticity `H2` spectral energy.

---

## 3. Uniform tail estimate on a compact fixed-order hull

If the compact CE-H hull has

\[
\sup_\theta\|\Delta W(\theta)\|_2^2\le H_2^*<\infty,
\]

then for every `K>0`,

\[
K^2\int_{\{|\kappa|>K\}}\rho^2dy
\le
\int_{\{|\kappa|>K\}}\kappa^2\rho^2dy
\le H_2^*.
\]

Hence

\[
\boxed{
\int_{\{|\kappa|>K\}}\rho^2dy
\le\frac{H_2^*}{K^2}.
}
\]

Unbounded kappa may occur pointwise, especially near low amplitude, but it cannot carry arbitrary enstrophy mass at fixed large multiplier without paying second-derivative energy.

---

## 4. Shell spectral ratio

For a remote enlarged shell `C_R`, define

\[
E_R:=\int_{C_R}\rho^2dy,
\]

\[
H_R^{(2)}:=\int_{C_R}|\Delta W|^2dy
=\int_{C_R}\kappa^2\rho^2dy.
\]

When `E_R>0`, define the normalized second-derivative multiplier scale

\[
\boxed{
\Lambda_R^2
:=\frac{H_R^{(2)}}{E_R}
=\frac{\int_{C_R}\kappa^2\rho^2dy}
{\int_{C_R}\rho^2dy}.
}
\]

Thus `Lambda_R` is exactly the enstrophy-weighted RMS size of `|kappa|` on the shell.

---

## 5. Fixed-fraction high-kappa occupancy forces large spectral ratio

Suppose a set

\[
A_R\subset C_R\cap\{|\kappa|\ge K_R\}
\]

carries a fixed fraction `theta>0` of shell enstrophy:

\[
\int_{A_R}\rho^2dy\ge\theta E_R.
\]

Then

\[
H_R^{(2)}
\ge K_R^2\int_{A_R}\rho^2dy
\ge\theta K_R^2E_R.
\]

Therefore

\[
\boxed{
\Lambda_R^2\ge\theta K_R^2.
}
\]

Hence a high-kappa population can dominate a hard shell only if the shell's normalized `H2/L2` ratio grows on the same scale.

---

## 6. Critical-shell form

If

\[
E_R=\frac{b_R}{R}
\]

with bounded critical shell cost `b_R`, then fixed-fraction occupancy at level `K_R` gives

\[
\boxed{
K_R^2\frac{b_R}{R}
\le\theta^{-1}H_R^{(2)}.
}
\]

Using only the global hull ceiling `H_R^(2)<=H_2^*`,

\[
\boxed{
K_R
\le
C\sqrt{\frac{R}{b_R}}
}
\]

for a fixed-fraction high-kappa carrier.

This does not bound `K_R` uniformly as `R->infinity`; it identifies the maximal scale compatible with a fixed shell mass under the global `H2` ceiling.

---

## 7. Corrected unbounded-kappa frontier

The old branch

\[
G_{\kappa,\infty}
\]

should now be split into

\[
\boxed{
G_{\kappa,\infty}
\Longrightarrow
G_{high\text{-}frequency\ spectral\ ratio}
\lor
G_{enstrophy\text{-}negligible\ kappa\ spikes}.
}
\]

The second branch cannot carry a fixed fraction of the hard shell and must interact with another carrier population if the shell remains critical.

The first branch is quantified by

\[
\boxed{\Lambda_R\to\infty.}
\]

This is a standard spectral-concentration problem rather than an untyped quotient singularity.

---

## 8. DSD audit

- Pointwise `kappa` may diverge where `rho` is tiny; M17-210 does not deny this.
- The useful hard-shell statement is weighted by enstrophy.
- Uniform global `H2` boundedness does not imply uniform shell spectral ratio because `E_R` may decay.
- No contradiction is claimed from `Lambda_R -> infinity` alone.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
