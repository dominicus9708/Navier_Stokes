# M18-022 — Coefficient-level smoothing removes the pointwise D5 time barrier and yields an exact bulk rate-dissipation identity

**Date:** 2026-09-11  
**Status:** ACTIVE DSD ANALYSIS / BULK-SMOOTHING REDUCTION / TEMPORAL-JET DESCENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-021 derived the exact time derivative of the codimension-one level flux

\[
F(s,t)=\int_{\{\kappa=s\}}\rho^2|\nabla\kappa|\,dS
\]

and found a term

\[
\rho^2\partial_n h,
\qquad
h:=D_t\kappa.
\]

Since

\[
h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
\]

a direct pointwise level estimate of \(\partial_nh\) naturally reaches a third coefficient jet and therefore a D5-type vorticity derivative barrier.

The present audit asks whether that derivative escalation is intrinsic or whether it is caused by differentiating a codimension-one observable before using its coefficient-level neighborhood.

The answer is important:

\[
\boxed{
\text{after smoothing across coefficient levels, the }\nabla h\text{ term can be removed exactly by bulk integration by parts.}
}
\]

Thus the pointwise D5 barrier of M18-021 is **not universal**. It remains relevant for genuinely collapsing level-width events, but it is avoidable on a macroscopic coefficient-width branch.

## 2. Fixed record-scale coefficient cutoff

Fix one physical record and one reference coefficient width

\[
\delta_0>0.
\]

Let

\[
\psi\in C_c^1((-1,1)),
\qquad
\psi\ge0,
\]

and set

\[
\phi(s):=\psi\!\left(\frac{s}{\delta_0}\right).
\]

The reference width \(\delta_0\) is fixed in time on the local window. This avoids introducing a \(\dot\delta\) term. Across record scaling, \(\delta_0\) is scaled as a physical coefficient level.

Define the coefficient-level-smoothed first-jet charge

\[
\boxed{
B_\phi(t)
:=
\int_{\mathbb R^3}
\phi(\kappa)\rho^2|\nabla\kappa|^2dx.
}
\]

By coarea,

\[
\boxed{
B_\phi(t)
=
\int_{\mathbb R}
\phi(s)F(s,t)\,ds.
}
\]

Thus \(B_\phi\) is literally a smooth coefficient-level average of the level flux used in M18-016--021.

## 3. Scaling audit

Under physical Navier--Stokes scaling,

\[
\rho_R=R^2\rho,
\qquad
\kappa_R=R^2\kappa,
\qquad
\nabla\kappa_R=R^3\nabla\kappa,
\]

and

\[
dy=R^{-3}dx.
\]

With the scaled cutoff width

\[
\delta_{0,R}=R^2\delta_0,
\]

the cutoff is representation matched:

\[
\phi_R(\kappa_R)=\phi(\kappa).
\]

Therefore

\[
\boxed{
B_{\phi,R}=R^7B_\phi.
}
\]

Its time derivative scales as

\[
\boxed{
\partial_sB_{\phi,R}=R^9\partial_tB_\phi.
}
\]

After time integration, \(B_\phi\) belongs to the same \(R^{-5}\) ancestry class as the M17-445 first-coefficient-jet/D3 resource.

## 4. Material derivative before integration by parts

Write

\[
g:=|\nabla\kappa|,
\qquad
h:=D_t\kappa,
\qquad
a_n:=n\cdot(\nabla u)n,
\qquad
n:=\frac{\nabla\kappa}{g}.
\]

For incompressible flow, the whole-space material derivative has no volume-Jacobian contribution.

On exact CE-H,

\[
D_t\rho=(\sigma+\nu\kappa)\rho,
\]

and

\[
D_tg
=\partial_nh-ga_n.
\]

Also

\[
D_t\phi(\kappa)=\phi'(\kappa)h.
\]

Hence

\[
\begin{aligned}
\dot B_\phi
={}&
\int
\phi' h\rho^2g^2dx\\
&+2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx\\
&+2\int
\phi\rho^2\nabla\kappa\cdot\nabla h\,dx.
\end{aligned}
\]

At this stage the last term appears to contain the same high temporal coefficient derivative that produced the M18-021 pointwise barrier.

## 5. Bulk integration by parts removes \(\nabla h\)

Because \(\phi\) is compactly supported in coefficient space and the spatial fields are taken in the certified smooth whole-space class, integrate the last term by parts:

\[
2\int
\phi\rho^2\nabla\kappa\cdot\nabla h\,dx
=
-2\int
h\,\nabla\cdot(\phi\rho^2\nabla\kappa)\,dx.
\]

Expand

\[
\nabla\cdot(\phi\rho^2\nabla\kappa)
=
\phi'\rho^2g^2
+
\phi\left(
2\rho\nabla\rho\cdot\nabla\kappa
+ho^2\Delta\kappa
\right).
\]

Therefore

\[
\begin{aligned}
\dot B_\phi
={}&
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx\\
&-
\int
\phi' h\rho^2g^2dx\\
&-
4\int
\phi\rho h\nabla\rho\cdot\nabla\kappa\,dx\\
&-
2\int
\phi\rho^2h\Delta\kappa\,dx.
\end{aligned}
\]

No derivative of \(h\) remains.

This is the first key descent:

\[
\boxed{
\partial_nh\text{ / }\nabla h
\quad\longrightarrow\quad
h\text{ after coefficient-level bulk smoothing.}
}
\]

## 6. Weighted-operator compression

Recall

\[
L_\rho\kappa
=
\rho^{-2}\nabla\cdot(\rho^2\nabla\kappa)
=
\Delta\kappa
+2\nabla\log\rho\cdot\nabla\kappa.
\]

Hence

\[
2\rho\nabla\rho\cdot\nabla\kappa
+ho^2\Delta\kappa
=
\rho^2L_\rho\kappa.
\]

The last two terms in Section 5 combine exactly:

\[
-4\phi\rho h\nabla\rho\cdot\nabla\kappa
-2\phi\rho^2h\Delta\kappa
=
-2\phi\rho^2hL_\rho\kappa.
\]

Therefore

\[
\boxed{
\dot B_\phi
=
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx
-
\int
\phi'h\rho^2g^2dx
-
2\int
\phi\rho^2hL_\rho\kappa\,dx.
}
\]

This is already a lower-derivative exact identity than the pointwise level-flux time derivative.

## 7. Exact rate-dissipation identity

Use the physical coefficient law from M17-339:

\[
\boxed{
h=A+C,}
\]

where

\[
A:=L_\rho\kappa,
\qquad
C:=L_\rho\sigma+\mathcal R_{\rm geom}.
\]

The algebraic identity

\[
2hA=A^2+h^2-C^2
\]

is exact because \(h=A+C\).

Substituting into Section 6 gives

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+
\int\phi\rho^2
\left(
|L_\rho\kappa|^2+|h|^2
\right)dx\\
={}&
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx\\
&-
\int
\phi'h\rho^2g^2dx\\
&+
\int
\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
\end{aligned}
}
\]

This is the main M18-022 identity.

It reveals two nonnegative rate/diffusion channels on the left:

\[
\boxed{
\int\phi\rho^2|L_\rho\kappa|^2dx,
\qquad
\int\phi\rho^2|D_t\kappa|^2dx.
}
\]

The pointwise third coefficient jet has disappeared.

## 8. Interpretation of the three right-hand channels

The identity leaves three source/transport channels.

### A. Strain/normal-stretch channel

\[
\boxed{
\mathcal S_\phi
:=
2\int
\phi(\sigma+\nu\kappa-a_n)\rho^2g^2dx.
}
\]

If the normalized strain, normal strain, and coefficient remain uniformly bounded, this channel is controlled by \(B_\phi\), whose spacetime ancestry is already in the M17-445 \(R^{-5}\) class.

### B. Coefficient-cutoff current

\[
\boxed{
\mathcal C_\phi
:=-\int\phi'h\rho^2g^2dx.
}
\]

This term is supported only where the coefficient cutoff changes. It is not automatically absorbed by the existing first-jet ledger because it couples the coefficient rate \(h\) to \(g^2\).

It can be treated as a genuine coefficient-boundary/current channel or estimated conditionally at the price of a stronger weighted gradient moment.

### C. Strain/geometry source square

\[
\boxed{
\mathcal R_\phi
:=
\int\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
}
\]

No existing M17/M18 ledger has yet been certified for this full squared source combination.

It must remain explicit until a termwise estimate is proved.

## 9. Conditional compact-source consequence

Suppose on a retained macroscopic-width exact CE-H family:

1. \(|\sigma|+|a_n|+|\kappa|\le C_*\);
2. the cutoff-current term has an integrable record-uniform bound;
3. the source square \(\mathcal R_\phi\) has an integrable record-uniform bound;
4. \(B_\phi\) is controlled at the interval endpoints.

Then time integration of the exact identity gives finite control of

\[
\boxed{
\iint
\phi\rho^2|D_t\kappa|^2dxdt
}
\]

and

\[
\boxed{
\iint
\phi\rho^2|L_\rho\kappa|^2dxdt.
}
\]

This would supply a direct temporal coefficient-rate resource without introducing D5 derivatives.

The statement is conditional because items 2--3 are not yet certified from the existing ancestral ledgers.

## 10. Why level-width matters

The smoothing argument requires a nontrivial physical coefficient band on which a fixed cutoff can be placed.

If the useful coefficient-level width collapses to zero from record to record, M18-019 already gives the representation-safe alternative

\[
P_\ell\gtrsim\frac{J}{\ell}
\qquad\text{or}\qquad
\Lambda_{\kappa,\delta}\gtrsim\frac{\delta}{\ell},
\]

up to the explicit compactness exits.

Therefore the current analysis naturally splits:

\[
\boxed{
\begin{aligned}
G_{\rm temporal\ flux\text{-}shape}
\Longrightarrow{}&
G_{\rm collapsing\ level\ width}\
&\lor G_{\rm bulk\ smoothed\ rate\ identity}.
\end{aligned}
}
\]

The first branch is already owned by M18-019. The second avoids the pointwise D5 escalation.

## 11. Representation and derivative-order audit

Every term in the main identity scales as \(R^9\) instantaneously.

Indeed:

\[
\dot B_{\phi,R}=R^9\dot B_\phi,
\]

\[
\rho_R^2|h_R|^2dy
\sim R^9,
\]

and

\[
\rho_R^2|L_{\rho_R}\kappa_R|^2dy
\sim R^9.
\]

The cutoff derivative scales as

\[
\phi_R'=R^{-2}\phi',
\]

so the cutoff current also scales as \(R^9\).

Thus no dimensional mismatch is hidden in the descent.

Most importantly, M18-022 does **not** assert a D4 or D5 ancestry ledger for \(h\). It identifies an exact energy-type identity in which the dangerous third coefficient jet is absent.

## 12. Relation to the M17-463 firewall

M17-339 now supplies the exact physical expression for \(\mathcal R_{\rm geom}\), correcting the historical premise in M17-463 that the formula had not yet been recovered during that audit pass.

However, the substantive M17-463 firewall remains valid:

\[
\boxed{
\text{exact source provenance}\neq\text{certified payer estimate}.
}
\]

Accordingly, the source square

\[
|L_\rho\sigma+\mathcal R_{\rm geom}|^2
\]

is not assigned to palinstrophy, raw-H2, or D3 by analogy.

## 13. Updated temporal branch

M18-021 gave

\[
G_{\rm active\text{-}time\ thinning}
\Longrightarrow
G_{\rm temporal\ flux\text{-}shape\ jet}
\lor\text{explicit compactness losses}.
\]

M18-022 refines the temporal jet branch to

\[
\boxed{
\begin{aligned}
G_{\rm temporal\ flux\text{-}shape\ jet}
\Longrightarrow{}&
G_{\rm level\text{-}width\ collapse}\
&\lor G_{\rm coefficient\ cutoff\ current}\
&\lor G_{\rm strain/geometry\ source\ square}\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\
&\lor G_{\rm controlled\ bulk\ coefficient\ rate}.
\end{aligned}
}
\]

The previous direct D5 branch is therefore demoted from a universal temporal obstruction to a **pointwise-level formulation hazard**. A genuine higher-jet branch may still reappear through the unresolved source/current terms, but it must be proved there rather than assumed.

## 14. DSD audit verdict

### Certified here

1. Coefficient-level smoothing converts the codimension-one flux family into the bulk charge \(B_\phi\).
2. The material derivative of \(B_\phi\) initially contains \(\nabla h\), but bulk integration by parts removes it exactly.
3. The remaining amplitude/coefficient terms combine into \(-2\rho^2hL_\rho\kappa\).
4. The constitutive law produces the exact positive pair
   \[
   \rho^2|D_t\kappa|^2+\rho^2|L_\rho\kappa|^2.
   \]
5. The pointwise D5 temporal barrier is not intrinsic on a macroscopic coefficient-width branch.
6. The remaining unresolved channels are explicitly typed rather than hidden in a generic high-jet exit.

### Not certified here

1. A finite ancestry ledger for \(D_t\kappa\).
2. Control of the coefficient-cutoff current by existing resources.
3. Control of the full squared strain/geometry source.
4. An ancestry contradiction.
5. Global 3D Navier--Stokes regularity.

## 15. Next analysis target

The best next target is the coefficient-cutoff current

\[
\mathcal C_\phi
=-\int\phi'h\rho^2g^2dx.
\]

It is localized to the two transition collars of the coefficient cutoff and is structurally simpler than the full geometry-source square.

The next audit should determine whether an adapted cutoff, a collar decomposition, or a weighted Cauchy estimate can send \(\mathcal C_\phi\) into

\[
\rho^2|h|^2,
\qquad
\rho^2|\nabla\kappa|^2,
\]

plus an explicit higher-gradient collar exit, without destroying the favorable \(R^{-5}\) ancestry class.

That is the appropriate M18-023 target.
