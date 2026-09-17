# M19-375 — The M5-688 strain-gradient payer is controlled by palinstrophy and is not an independent finite resource

**Date:** 2026-09-18  
**Status:** NEW INTERNAL ESTIMATE / M5-688 + M17-190 PAYER AUDIT / PALINSTROPHY-ORDER NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M19-374 reduces the retained multi-sheet relabeling architecture to positive-rate dynamic activity.

M5-688 then shows that the positive \(\kappa\)-diffusion charge must be paid by strain-gradient, quarter-strain residence, cutoff transition, or explicit CE-H geometric sources.

M17-190 proves that one important compact high-amplitude recurrent-loop subbranch necessarily carries

\[
\boxed{D_\sigma\ge d_\sigma^{loop}>0}
\]

with

\[
D_\sigma
:=
\left\langle
\int
\chi(\rho)\rho^2e^{2\kappa}|\nabla\sigma|^2dy
\right\rangle.
\]

The question is whether this is a genuinely new derivative resource or simply another form of palinstrophy.

## 2. Differentiate the aligned strain

On the CE-H eigenline branch write

\[
W=\rho\xi,
\qquad |\xi|=1,
\]

and

\[
\sigma=\xi\cdot\Sigma\xi,
\]

where \(\Sigma\) is the symmetric velocity strain tensor.

For each spatial derivative \(\partial_j\),

\[
\boxed{
\partial_j\sigma
=
2(\partial_j\xi)\cdot\Sigma\xi
+
\xi\cdot(\partial_j\Sigma)\xi.
}
\]

Hence

\[
|\nabla\sigma|^2
\le
8|\Sigma|^2|\nabla\xi|^2
+2|\nabla\Sigma|^2.
\]

## 3. Insert the vorticity amplitude weight

Since

\[
W=\rho\xi,
\qquad
\xi\cdot\partial_j\xi=0,
\]

we have the exact decomposition

\[
\boxed{
|\nabla W|^2
=
|\nabla\rho|^2
+
\rho^2|\nabla\xi|^2.
}
\]

Therefore

\[
\rho^2|\nabla\xi|^2
\le
|\nabla W|^2.
\]

On the compact CE-H hull let

\[
\|\Sigma\|_\infty\le S_*,
\qquad
\rho\le \rho_*,
\qquad
|\kappa|\le K_*.
\]

Then

\[
\begin{aligned}
\chi\rho^2e^{2\kappa}|\nabla\sigma|^2
&\le
8e^{2K_*}S_*^2\rho^2|\nabla\xi|^2
+
2e^{2K_*}\rho_*^2|\nabla\Sigma|^2\\
&\le
8e^{2K_*}S_*^2|\nabla W|^2
+
2e^{2K_*}\rho_*^2|\nabla\Sigma|^2.
\end{aligned}
\]

No lower amplitude bound is needed for this estimate because the \(\rho^2\) weight already cancels the possible direction singularity.

## 4. Whole-space Biot--Savart/Riesz control

For divergence-free whole-space velocity,

\[
W=\nabla\times U
\]

and every component of \(\nabla U\), hence of \(\Sigma\), is a zero-order Calderon--Zygmund/Riesz transform of \(W\).

After one derivative,

\[
\boxed{
\|\nabla\Sigma\|_2
\le C_R\|\nabla W\|_2.
}
\]

Consequently, at every retained time,

\[
\boxed{
\int
\chi\rho^2e^{2\kappa}|\nabla\sigma|^2dy
\le
C_{\sigma,P}
\int|\nabla W|^2dy,
}
\]

where \(C_{\sigma,P}\) depends only on the retained compact-hull bounds and the whole-space Riesz constant.

Taking the recurrent mean gives

\[
\boxed{
D_\sigma
\le
C_{\sigma,P}\,\langle P\rangle,
\qquad
P:=\|\nabla W\|_2^2.
}
\]

## 5. Consequence for the M17-190 loop branch

M17-190 gives

\[
D_\sigma\ge d_\sigma^{loop}>0.
\]

Therefore

\[
\boxed{
\langle P\rangle
\ge
\frac{d_\sigma^{loop}}{C_{\sigma,P}}>0.
}
\]

This identifies a real palinstrophy occupancy, but does not create a derivative order beyond palinstrophy.

## 6. Scaling classification

The spacetime palinstrophy charge has critical physical weight

\[
\boxed{
r\int P(t)dt.}
\]

M17-307 and M19-314--315 already show that this currency is exactly critical under parent/physical restoration.

Hence the strain-gradient payer belongs to the same critical resource class:

\[
\boxed{
D_\sigma\text{ payer}
\subset
\text{palinstrophy-order currency}.
}
\]

It does not by itself provide the subcritical base gain required by the GMS route, nor a new finite cumulative resource for the M19-374 dynamic triad.

## 7. No-go conclusion

A proof strategy of the form

\[
\text{recurrent loop}
\Rightarrow
D_\sigma\ge d_*>0
\Rightarrow
\text{new dissipation contradiction}
\]

is invalid.

The correct implication is only

\[
\boxed{
\text{recurrent compact loop}
\Rightarrow
\text{fixed positive palinstrophy-order occupancy}.
}
\]

Such occupancy can recur on a critical compact state space unless one also proves a nonreuse/incidence theorem or a supercritical multiplicity statement.

## 8. Relation to M5-688 / M17-186

M17-186 rewrites the non-gradient M5-688 payer as an exponentially tilted quarter-strain line-residence excess.

The present result shows that the explicit strain-gradient branch is not an independent escape currency either: it is quantitatively dominated by palinstrophy.

Therefore a genuinely new closure must come from one of:

\[
\boxed{
\mathcal T_{dyn}^{nonreuse}
\lor
\mathcal T_{residence}^{irreversible}
\lor
\mathcal T_{cutoff/geom}^{finite\ resource}
\lor
\mathcal T_{scale}^{supercritical\ multiplicity}.
}
\]

## 9. Firewall

The estimate uses whole-space incompressible Biot--Savart/Riesz control and the retained compact-hull bounds. It does not assert local pointwise control of \(\nabla\Sigma\) by \(\nabla W\).

It is an \(L^2\)-level resource classification only.

## 10. Verdict

\[
\boxed{
D_\sigma\le C\,P,
}
\]

so M17-190 routes its subbranch to a certified payer but not to a new contradiction.

---

\[
\boxed{\text{M19-375 COMPLETE; THE STRAIN-GRADIENT PAYER IS PALINSTROPHY-CONTROLLED AND REMAINS CRITICAL.}}
\]
