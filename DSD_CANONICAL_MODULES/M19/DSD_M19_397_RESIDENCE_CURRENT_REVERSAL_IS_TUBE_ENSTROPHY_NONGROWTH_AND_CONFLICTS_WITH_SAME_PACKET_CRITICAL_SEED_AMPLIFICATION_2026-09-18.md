# M19-397 — Residence-current reversal is exactly non-growth of material tube enstrophy and conflicts with same-packet critical seed amplification

Date: 2026-09-18

Status: **NEW SAME-PACKET INCOMPATIBILITY / THE RESIDENCE-WEIGHTED ZERO-CROSSING WEIGHT `L_rho dPhi` IS EXACTLY THE ENSTROPHY CONTENT OF AN INFINITESIMAL MATERIAL VORTEX-TUBE SEGMENT. ITS LOGARITHMIC GROWTH RATE IS `2(kappa+sigma_bar_rho-1/4)`. THEREFORE THE M19-389 CONDITION FOR CANCELLING OR REVERSING THE NEGATIVE MATERIAL-FLUX CURRENT IS EXACTLY THE STATEMENT THAT THIS MATERIAL TUBE ENSTROPHY DOES NOT GROW ACROSS THE POSITIVE-KAPPA EXCURSION. BY CONTRAST, THE COHERENT COMPACT M19-365 CRITICAL SEED LOCK `(kappa,sigma)->(3/2,-1/2)` AMPLIFIES MATERIAL ENSTROPHY AT RATE `3/2`, THE PRECISE RATE NEEDED TO LIFT AN EXPONENTIALLY SMALL SEED TO ORDER ONE. HENCE THE SAME CERTIFIED MATERIAL PACKET/TUBE CANNOT BOTH REALIZE THE LONG CRITICAL SEED AMPLIFICATION AND PROVIDE RESIDENCE-CURRENT REVERSAL OVER THAT POSITIVE EXCURSION. SURVIVAL REQUIRES SPATIAL CURRENT SIGN TRANSFER, OR PACKET/LINE INCIDENCE SEGREGATION, OR GENEALOGY/REPRESENTATION LOSS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Material tube enstrophy in flux coordinates

For an infinitesimal oriented material vortex-tube label, the flow-box volume form is

\[
dV
=
\frac{d\Phi\,ds}{\rho}.
\]

Therefore its enstrophy content integrated along a represented material line segment \(\Gamma\) is

\[
\begin{aligned}
dE_{tube}
&=
\int_\Gamma \rho^2\,dV\\
&=
\int_\Gamma \rho^2
\frac{d\Phi\,ds}{\rho}\\
&=
\left(
\int_\Gamma\rho\,ds
\right)d\Phi.
\end{aligned}
\]

With

\[
L_\rho
:=
\int_\Gamma\rho\,ds,
\]

we have the exact identity

\[
\boxed{
dE_{tube}
=
L_\rho\,d\Phi.
}
\]

Thus the weight appearing in the M19-385 spatial-current bridge is an actual material enstrophy weight, not merely a Radon--Nikodym bookkeeping factor.

---

## 2. Exact material tube-enstrophy growth law

M5-684 gives

\[
\frac d{d\theta}\log L_\rho
=
\kappa
-
\frac12
+
2\bar\sigma_\rho,
\]

where

\[
\bar\sigma_\rho
=
\frac{\int_\Gamma\sigma\rho\,ds}
{\int_\Gamma\rho\,ds}.
\]

The material flux law is

\[
\frac d{d\theta}\log d\Phi
=
\kappa.
\]

Therefore

\[
\boxed{
\frac d{d\theta}
\log dE_{tube}
=
2\kappa
+
2\bar\sigma_\rho
-
\frac12.
}
\]

Equivalently,

\[
\boxed{
\frac d{d\theta}
\log dE_{tube}
=
2\left(
\kappa+\bar\sigma_\rho-\frac14
\right).
}
\]

---

## 3. Positive excursion identity

For a complete positive-kappa excursion

\[
\theta_u<\theta_d,
\qquad
\kappa>0
\quad
(\theta_u,\theta_d),
\]

M19-389 defines

\[
I_+
=
\int_{\theta_u}^{\theta_d}\kappa\,d\theta,
\]

and

\[
J_+
=
\int_{\theta_u}^{\theta_d}
\left(
2\bar\sigma_\rho-\frac12
\right)d\theta.
\]

Hence

\[
\boxed{
\log
\frac{
dE_{tube}(\theta_d)
}{
dE_{tube}(\theta_u)
}
=
2I_+
+
J_+.
}
\]

But M19-389--390 show that residence-current cancellation or reversal requires

\[
J_+\le-2I_+.
\]

Therefore

\[
\boxed{
dE_{tube}(\theta_d)
\le
dE_{tube}(\theta_u).
}
\]

Thus **current reversal is exactly a non-growth condition for the material tube enstrophy across the positive-kappa excursion.**

For strict reversal,

\[
J_+<-2I_+,
\]

the material tube enstrophy strictly decreases despite positive material-flux amplification.

---

## 4. Critical seed enstrophy amplification

M19-365 gives on the fully compact critical seed lock

\[
\bar\kappa\to\frac32,
\qquad
\bar\sigma_{seed}\to-\frac12.
\]

For a coherent material packet whose constituent strain follows the same critical lock, one material enstrophy element obeys

\[
D_B\log(\rho^2dV)
=
2\sigma+2\kappa-\frac12.
\]

At the lock,

\[
2\left(-\frac12\right)
+
2\left(\frac32\right)
-
\frac12
=
\frac32.
\]

Hence

\[
\boxed{
D_B\log(\rho^2dV)
\to
\frac32.
}
\]

Over a long critical activation interval of duration \(T\),

\[
\boxed{
E_{seed}(T)
\sim
E_{seed}(0)e^{3T/2+o(T)}.
}
\]

This is precisely the amplification used by the M19-362--365 critical seed conveyor to raise exponentially small dormant material enstrophy to order-one retained enstrophy.

---

## 5. Same-packet incompatibility

Assume now that

1. the critical seed amplification interval is contained in a complete positive-kappa excursion up to \(o(T)\) endpoint transitions;
2. the represented material vortex-tube segment in M19-389 is the same certified material packet/tube whose enstrophy is being amplified in M19-365;
3. amplitude/line representation remains regular so that no material mass is silently exchanged with a different packet.

Then the critical seed law requires

\[
\log
\frac{E_{tube,d}}{E_{tube,u}}
=
\frac32T+o(T)
>0.
\]

Residence-current reversal requires

\[
\log
\frac{E_{tube,d}}{E_{tube,u}}
\le0.
\]

These are incompatible for sufficiently large \(T\).

Therefore

\[
\boxed{
\text{same coherent critical seed packet}
+
\text{residence-current reversal}
\Longrightarrow
\bot.
}
\]

This is a conditional branch closure, not a proof of global regularity.

---

## 6. Relation to the 3/4 strain gap

M19-396 found that current reversal on a critical excursion requires

\[
\overline{\bar\sigma_\rho}
\le
-\frac54,
\]

whereas the coherent seed lock has

\[
\overline{\sigma_{seed}}
\to
-\frac12.
\]

The present module explains the exact physical meaning of that \(3/4\) discrepancy.

Changing the line-weighted strain from \(-1/2\) to at most \(-5/4\) changes the material tube-enstrophy growth rate from

\[
\frac32
\]

to

\[
\le0.
\]

Thus the \(3/4\) line-strain segregation is exactly the amount needed to cancel the critical enstrophy amplification.

---

## 7. Updated survivor split

The critical seed/current branch now has the sharper form

\[
\boxed{
G_{seed}^{3/2}
\Longrightarrow
G_{spatial\ current}^{negative}
\lor
G_{packet/line\ incidence\ segregation}
\lor
G_{genealogy/representation/amplitude\ exchange}.
}
\]

The previous generic longitudinal strain-segregation branch is now interpreted more concretely:

if the spatial current reverses, the residence-weighted line population cannot be the same coherent material packet that is undergoing critical enstrophy amplification.

It must be carried by a different line portion/population or by material exchange across the represented packet boundary.

---

## 8. Why this is stronger than a payer lower bound

Earlier modules often produced a positive local cost that remained recurrently recyclable.

M19-397 instead compares two required signs for the **same material enstrophy observable** over the same long interval:

\[
\boxed{
\text{critical seed activation: }
\Delta\log E_{tube}\sim+\frac32T,
}
\]

versus

\[
\boxed{
\text{current reversal: }
\Delta\log E_{tube}\le0.
}
\]

No summation or finite-budget argument is needed on the same-packet branch.

The remaining issue is therefore incidence/identity:

\[
\boxed{
\mathcal T_{inc}^{seed\leftrightarrow current}:
\text{prove that the critical seed packet and the residence-weighted current carrier must coincide on a positive-rate family of events.}
}
\]

If that incidence theorem is obtained, the critical current-reversal escape closes directly.

---

## 9. Firewall

Do not claim the incidence theorem for free.

M19-365 concerns a coherent material seed packet; M19-389 concerns a residence-weighted vortex-line current carrier.

Without certified packet/line identity, the system may try to place

- critical enstrophy amplification on one material subpopulation, and
- current-reversal residence weight on another.

That is now the explicit survivor, not an untracked loophole.

---

\[
\boxed{\text{M19-397 COMPLETE; SAME-PACKET CRITICAL SEED AMPLIFICATION AND RESIDENCE-CURRENT REVERSAL ARE INCOMPATIBLE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
