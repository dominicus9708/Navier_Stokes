# DSD M17-397 — M5-688 contains the away-from-zero log-`kappa` diffusion channel but is a recurrence cycle-work balance, not a finite ancestral budget

Date: 2026-09-08  
Canonical ID: **M17-397**

Status: **ACTIVE ANCESTRAL-BUDGET NO-GO / M5-688 CROSS-AUDIT / LOG-DIFFUSION IDENTIFICATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Question

M17-396 reduces the positive-flux intrinsic coefficient-gradient branch to a fixed positive normalized log-coefficient diffusion charge.

The open question is whether the older M5-687/688 multiplier-diffusion machinery already supplies the finite ancestral budget needed to contradict infinitely many such normalized payments.

The answer is twofold:

1. **yes**, M5-688 contains the same coefficient-diffusion architecture away from `kappa=0`;
2. **no**, M5-688 is a recurrent cycle-work balance and does not provide a finite cross-generation total budget.

This distinction is the main result of M17-397.

## 2. M5-688 coefficient diffusion

On the recurrent high-amplitude similarity CE-H hull, M5-688 uses

\[
A_{\kappa\kappa}(k,\theta)
:=
\int
\delta(k-\kappa)
\chi(\rho)\rho^2|\nabla\kappa|^2dy
\ge0
\]

and the exponentially weighted recurrent mean

\[
\boxed{
D_\kappa
:=
\int e^{2k}\overline{A_{\kappa\kappa}}(k)dk.
}
\]

M5-687 gives the statewise/recurrent-hull gap

\[
\boxed{
D_\kappa\ge d_\kappa>0.
}
\]

The compact high-amplitude hull has

\[
|\kappa|\le K_*<\infty.
\]

## 3. Away-from-zero log-diffusion is quantitatively equivalent

Fix

\[
0<\delta<K_*.
\]

Define the away-from-zero part

\[
D_\kappa^{away}(\delta)
:=
\int_{|k|\ge\delta}
 e^{2k}\overline{A_{\kappa\kappa}}(k)dk.
\]

Define the corresponding recurrent log-coefficient diffusion

\[
\boxed{
D_{\log\kappa}^{away}(\delta)
:=
\int_{|k|\ge\delta}
 k^{-2}
\overline{A_{\kappa\kappa}}(k)dk.
}
\]

This is exactly

\[
\left\langle
\int_{|\kappa|\ge\delta}
\chi\rho^2
|\nabla\log|\kappa||^2dy
\right\rangle.
\]

Since

\[
\delta\le|k|\le K_*,
\]

and

\[
e^{-2K_*}\le e^{2k}\le e^{2K_*},
\]

we have the two-sided comparison

\[
\boxed{
K_*^{-2}e^{-2K_*}
D_\kappa^{away}(\delta)
\le
D_{\log\kappa}^{away}(\delta)
\le
\delta^{-2}e^{2K_*}
D_\kappa^{away}(\delta).
}
\]

Thus on every fixed normalized coefficient corridor separated from zero, M17-394/396 log-diffusion and the M5-688 multiplier diffusion are the same PDE channel up to fixed constants.

## 4. Away/near-zero dichotomy

Fix a fraction

\[
0<\eta<1.
\]

If

\[
D_\kappa^{away}(\delta)
\ge
\eta D_\kappa,
\]

then M5-687 and Section 3 give

\[
\boxed{
D_{\log\kappa}^{away}(\delta)
\ge
c(\delta,K_*,\eta)d_\kappa
>0.
}
\]

Hence the recurrent multiplier-diffusion gap directly supplies a fixed positive normalized log-diffusion gap.

Otherwise

\[
D_\kappa^{near}(\delta)
:=
\int_{|k|<\delta}
 e^{2k}\overline{A_{\kappa\kappa}}(k)dk
\ge
(1-\eta)D_\kappa
\ge
(1-\eta)d_\kappa.
\]

Then a fixed portion of the multiplier-diffusion charge is concentrated in a fixed coefficient corridor around zero.

This is a **near-zero coefficient-diffusion branch**, not an away-from-zero scale-migration branch.

If the zero level itself is regularly realized with the compact tube hypotheses, M17-343/346 supplies the corresponding zero-level thickening/spatial crossing machinery.

If the sign is preserved while the population approaches zero without a regular crossing, retain the explicit zero-approach/endpoint/derivative/interface branch instead of dividing by `kappa`.

Thus the logarithmic coordinate singularity is never used to manufacture an infinite physical payer at `kappa=0`.

## 5. Exact M5-688 cycle-work identity

M5-688 derives on the recurrent mean the identity

\[
\boxed{
D_\kappa+X_{\kappa\sigma}
=
\frac12\mathcal S
+\frac14\mathcal C
+\frac12\mathcal R
-\frac18\mathcal M,
}
\]

or equivalently

\[
\boxed{
D_\kappa+\frac18\mathcal M
=
-X_{\kappa\sigma}
+\frac12\mathcal S
+\frac14\mathcal C
+\frac12\mathcal R.
}
\]

Here

- `X_{kappa sigma}` is the mixed coefficient/strain-gradient work;
- `S` is the weighted strain-residence moment;
- `C` is the amplitude-cutoff transition source;
- `R` is the explicit CE-H/cutoff geometric remainder;
- `M>0` is the weighted mass.

Cauchy--Schwarz gives

\[
|X_{\kappa\sigma}|
\le
\sqrt{D_\kappa D_\sigma}.
\]

Therefore the positive `D_kappa` gap forces at least one strain-gradient, strain-residence, cutoff, or geometric payer.

## 6. Why this is not a finite budget

The identity in Section 5 is a **stationary/recurrent mean balance**.

It does not have the form

\[
\frac d{d\theta}\mathcal F
+ D_\kappa
\le0
\]

with a bounded-below monotone functional `F` whose total drop controls

\[
\int_0^\infty D_\kappa d\theta.
\]

Instead, it has the form

\[
\boxed{
\text{positive recurrent diffusion}
=
\text{recurrent source/work payment}.
}
\]

Thus a compact recurrent state can in principle satisfy

\[
D_\kappa\sim1,
\qquad
D_\sigma+|\mathcal S|+|\mathcal C|+|\mathcal R|\sim1
\]

for arbitrarily long normalized time without violating M5-688 itself.

Consequently M5-688 does **not** imply

\[
\boxed{
\sum_jD_{\kappa,j}^{norm}<\infty
}
\]

across record generations or shrinking intrinsic cells.

Nor does it imply the corresponding finite total for

\[
\sum_jD_{\log\kappa,j}^{norm}.
\]

This is precisely the finite-ancestral-budget property required by M17-396 and it remains unproved.

## 7. M17-196 removes the catch-all geometric payer but not the budget firewall

M17-196 reduces the full M5-688 remainder to explicit fixed-order positive channels.

Its bulk geometric terms are controlled by weighted vorticity palinstrophy plus multiplier diffusion, and the remaining cutoff pieces are fixed-amplitude threshold-gradient charges.

Schematically,

\[
\boxed{
D_\kappa>0
\Longrightarrow
D_\sigma
\lor Q_\sigma
\lor P_W
\lor B_{threshold}
\lor\text{threshold replenishment/interface}.
}
\]

This is a strong payer classification.

But M17-196 itself explicitly treats the threshold quantities as positive occupancies, **not automatically finite cumulative costs**.

Hence removing the catch-all `R_geom` branch does not create the missing ancestral budget.

## 8. Relation to M17-396 positive-flux charge

On the M17-395/396 positive-flux intrinsic branch, one unit normalized episode satisfies

\[
\nu\mathscr D_{\log\kappa}^{norm}
\gtrsim
\Phi_*^2.
\]

If the episode lies in a fixed away-from-zero coefficient corridor, Sections 2--4 identify this charge with the M5-688 multiplier-diffusion architecture.

M5-688 then says that the order-one normalized log-diffusion must be balanced by an order-one normalized source/work architecture.

It does **not** say that the same source/work architecture cannot recur at the next record scale.

Therefore the M17-396 firewall becomes sharper:

\[
\boxed{
\text{fixed positive normalized log-diffusion}
\to
\text{fixed positive normalized M5-688 payer}
\not\to
\text{finite ancestral total}.
}
\]

## 9. Cross-generation obstruction

To turn M5-688 into the desired ancestral-budget theorem, at least one additional statement is required:

1. a bounded-below monotone functional whose generation-to-generation drop controls the normalized diffusion/work;
2. an exact physical pullback with a nonsummable record weight;
3. a rigidity theorem forbidding recurrent reuse of the source architecture;
4. a bounded multiplicity theorem in one common physical spacetime measure;
5. a forced escape to zero crossing, flux thinning, threshold/interface loss, or derivative decompactification.

No such statement follows from M5-687/688 alone.

## 10. Revised coefficient-diffusion frontier

The current coefficient-gradient branch is therefore

\[
\boxed{
\begin{aligned}
H_{positive\ normalized\ coefficient/log\text{-}diffusion}
\Longrightarrow{}&
H_{away\text{-}zero\ M5\text{-}688\ cycle\ work}\\
&\lor H_{near\text{-}zero\ coefficient\ diffusion}\\
&\lor H_{zero\text{-}level\ crossing/criticality}\\
&\lor G_{threshold/interface/derivative/genealogy}.
\end{aligned}
}
\]

On the first branch the missing theorem is no longer payer identification.

It is **ancestral summability or recurrence rigidity**.

## 11. DSD audit role

The DSD role is a budget-versus-balance audit.

A positive dissipation-like term inside an exact stationary identity is not automatically a finite dissipation budget.

The canonical proof must distinguish

\[
\text{who pays?}
\]

from

\[
\text{how many times can it be paid?}
\]

M5-688 answers the first question on the recurrent hull.

M17-397 records that it does not yet answer the second.

## 12. Audit verdict

**PASS — M5-688 is identified as the correct normalized payer balance but rejected as a finite ancestral budget.**

The strongest current statement is

\[
\boxed{
D_{\log\kappa}^{norm}>0
\Longrightarrow
\text{explicit normalized cycle-work payer}
}
\]

away from zero, with the zero corridor separately routed to the existing crossing/criticality machinery.

The next highest-value target is to inspect the explicit M5-688 payer branches and determine which ones return to already known cross-generation firewalls and which, if any, can support a genuinely finite ancestral total.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
