# DSD M5-630 — Audit correction: zero-mean flux kappa does not remove the enstrophy-weighted negative budget

Date: 2026-09-03

Status: **DSD AUDIT CORRECTION / M5-628--629 CORRECTLY SHOW THAT DISTINCT ORDERED KAPPA LEVELS CANNOT EACH SUPPORT PERSISTENT BOUNDED NONDEGENERATE FIXED-FLUX LINEAGES UNDER ONE RELABELING ODE, BUT THEY OVERREACHED WHEN INFERRING THAT THE GLOBAL NEGATIVE ENSTROPHY-WEIGHTED KAPPA BUDGET MUST THEREFORE LIE OUTSIDE THE SYNCHRONIZED ZERO-MEAN ACTIVE LEVEL / `mean_time c_*=0` DOES NOT IMPLY `mean_time(c_* E_*)=0`; NEGATIVE COVARIANCE BETWEEN THE COMMON KAPPA HISTORY AND THE ACTIVE ENSTROPHY CAN PAY THE RAYLEIGH BUDGET / THE CORRECT SURVIVOR SPLIT IS EXTERNAL NEGATIVE-LEVEL TURNOVER OR SAME-LEVEL NEGATIVE KAPPA-ENSTROPHY COVARIANCE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. What remains valid from M5-628--629

On one connected `kappa` relabeling branch,

\[
D_B\kappa=f(\kappa,\theta),
\]

scalar ODE uniqueness preserves order of level values.

Every persistent bounded nondegenerate fixed-flux lineage satisfies

\[
\boxed{\langle\kappa\rangle_{flux\ time}=0.}
\]

Therefore two ordered persistent lineages governed by the same relabeling law must synchronize their level histories:

\[
\boxed{
\kappa_1=\cdots=\kappa_N=c_*(\theta)
}
\]

on the recurrent support.

Likewise, a genuinely distinct recurrent level lying strictly below or above `c_*` cannot itself carry another bounded persistent fixed-flux lineage, because its time-mean `kappa` has the corresponding strict sign.

These conclusions remain valid.

---

## 2. The invalid inference

M5-628--629 then suggested that because

\[
\langle c_*\rangle=0,
\]

the strict global identity

\[
\int\kappa|W|^2dy=-P<0
\]

must be paid outside the synchronized active level.

That implication is not valid.

The two averages use different measures.

The flux law samples `c_*` with material-time/flux-label weighting, while the Rayleigh law samples `kappa` with spatial enstrophy weight

\[
|W|^2dy.
\]

Zero mean in one measure does not imply zero mean in the other.

---

## 3. Same-level covariance mechanism

Let the synchronized persistent network occupy a retained active population with enstrophy

\[
E_*(\theta)>0.
\]

Since its common level value is `c_*(theta)`, its contribution to the Rayleigh integral is schematically

\[
\boxed{
R_*(\theta)=c_*(\theta)E_*(\theta).
}
\]

Even if

\[
\langle c_*\rangle=0,
\]

one can have

\[
\boxed{
\langle c_*E_*\rangle<0
}
\]

whenever negative `c_*` phases correlate with larger enstrophy.

Indeed

\[
\langle c_*E_*\rangle
=
\operatorname{Cov}(c_*,E_*)
+\langle c_*\rangle\langle E_*\rangle,
\]

so under `mean c_*=0`,

\[
\boxed{
\langle c_*E_*\rangle
=\operatorname{Cov}(c_*,E_*).
}
\]

A negative covariance can therefore pay a strictly negative enstrophy-weighted viscous budget while the same material flux has zero logarithmic drift.

---

## 4. Why fixed flux does not fix enstrophy weight

For a thin material vortex tube,

\[
\phi\sim\rho A_\perp,
\]

where `A_perp` is its cross-sectional area.

A fixed or recurrent scale-critical flux does not separately fix

\[
\rho,
\qquad
A_\perp,
\qquad
\text{or the tube enstrophy}.
\]

The CE-H laws are

\[
D_B\log\rho=\sigma+\kappa-1,
\]

\[
D_B\log A_\perp=1-\sigma,
\]

and therefore

\[
D_B\log\phi=\kappa.
\]

The cancellation in the flux observable precisely allows amplitude/area redistribution to correlate with `kappa` while the long-time flux drift remains zero.

Thus one may not replace flux weighting by enstrophy weighting.

---

## 5. Correct global budget split

Let `A` denote the synchronized persistent active level population and `R` the remainder.

Then

\[
\int\kappa|W|^2
=
\int_A c_*|W|^2
+
\int_R\kappa|W|^2
=-P.
\]

After invariant averaging, the strict negative budget can be paid through either or both of

\[
\boxed{
C_{same-level}
:=-\left\langle
c_*(\theta)E_A(\theta)
\right\rangle>0
}
\]

and

\[
\boxed{
C_{external-level}
:=-\left\langle
\int_R\kappa|W|^2dy
\right\rangle>0.
}
\]

Therefore the correct alternative is

\[
\boxed{
P_{mean}>0
\Longrightarrow
C_{same-level}>0
\lor
C_{external-level}>0
}
\]

up to quantitative splitting constants.

---

## 6. What M5-629 still proves about external levels

If the external-level term is positive and is carried by a genuinely distinct ordered relabeling level, M5-629 remains useful:

that level cannot itself become another persistent bounded fixed-flux population.

Hence

\[
\boxed{
C_{external-level}>0
\Longrightarrow
\text{nonpersistent/turnover negative-level population}
}
\]

on the relabeling branch.

Only the assertion that this is the **only** way to pay the Rayleigh budget is withdrawn.

---

## 7. Same-level covariance becomes a new hard branch

The new branch is

\[
\boxed{
C_{same-level}>0.
}
\]

Here the same synchronized fixed-flux level has

\[
\langle c_*\rangle=0
\]

but

\[
\langle c_*E_A\rangle<0.
\]

Thus its enstrophy must be systematically phase-shifted relative to the viscous multiplier.

The problem becomes a **phase-correlation problem**, not a measure-separation contradiction.

---

## 8. Natural next observable

For one coherent material tube element, let its amplitude be `rho` and cross-sectional area `A_perp`.

Since

\[
\phi=\rho A_\perp,
\]

fixed-flux recurrence allows the enstrophy density to vary through `rho` and geometry.

The exact amplitude equation gives

\[
D_B\log\rho=\sigma+c_*-1.
\]

Therefore the next quantity to audit is the correlation between

\[
c_*
\]

and

\[
\rho^2\quad\text{or localized tube enstrophy}.
\]

A useful candidate is a localized material-tube enstrophy-per-flux ratio, because dividing by the scale-invariant flux may remove one geometric degree of freedom while retaining the covariance information.

---

## 9. Corrected frontier

The relabeling branch must now be written as

\[
\boxed{
R_{relabel}
\Longrightarrow
C_{same-level}^{\kappa-E}
\lor
T_{external-level}^{viscous}
\lor
F_{\nabla D_B\kappa}.
}
\]

This replaces the stronger but invalid M5-629-only-turnover claim.

---

## 10. Audit classification

This document is a **correction note**.

For final proof reconstruction:

- retain the order-preservation and persistent-level uniqueness statements of M5-628--629;
- delete/override any inference that zero time-mean `kappa` forces zero enstrophy-weighted mean on the same active level;
- use the corrected covariance/turnover split above.

No earlier exact identities are affected.

---

## 11. Firewall

No sign is assigned to `Cov(c_*,E_A)` without proof.

The covariance branch is retained as a genuine survivor rather than assumed away.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
