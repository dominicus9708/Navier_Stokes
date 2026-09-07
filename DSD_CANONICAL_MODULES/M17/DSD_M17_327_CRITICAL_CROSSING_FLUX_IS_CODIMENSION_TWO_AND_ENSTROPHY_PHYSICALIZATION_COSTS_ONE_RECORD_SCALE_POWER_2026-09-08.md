# DSD M17-327 — critical crossing flux is codimension-two and enstrophy physicalization costs one record-scale power

Date: 2026-09-08  
Status: **ACTIVE CANONICAL CALCULATION / MEASURE-PHYSICALIZATION AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-326

The directed material zero-\(\kappa\) crossing flux is

\[
\mathcal C_-(I)
=
\int_I\int
h_-\,\delta(\kappa)\,d\Phi\,ds,
\qquad
h=D_B\kappa.
\]

M17-326 proved exact parabolic scale invariance:

\[
\boxed{\mathcal C_{-,R}(I)=\mathcal C_-(R^2I).}
\]

The question is whether this critical measure is already a standard spatial PDE budget.

## 2. Flux measure versus volume measure

On a regular vortex tube,

\[
d\Phi=\rho\,dA,
\qquad
 dy=dA\,ds_{line}.
\]

For one retained material line/tube label define

\[
L_\rho
:=\int_\Gamma\rho\,ds_{line}.
\]

Then Fubini in flux coordinates gives

\[
\boxed{
\int L_\rho\,d\Phi
=
\int\rho^2dy.
}
\]

Thus pure flux measure \(d\Phi\) is not the same as a three-dimensional volume or enstrophy measure.  The natural passage to enstrophy volume inserts one line-weight factor \(L_\rho\).

## 3. Enstrophy-weighted directed crossing measure

Define

\[
\boxed{
\mathcal C_-^E(I)
:=
\int_I\int
L_\rho h_-\delta(\kappa)d\Phi\,ds.
}
\]

Because \(h\) and \(\kappa\) are constant along each connected regular CE-H vortex line, the flux-coordinate identity gives, on the retained material population,

\[
\boxed{
\mathcal C_-^E(I)
=
\int_I\int
h_-\delta(\kappa)\rho^2dy\,ds
}
\]

up to the already explicit amplitude-cutoff/end/replacement terms when the retained segment is not a complete material tube.

This is the one-sided version of the enstrophy-weighted zero-level current underlying M5-683/M5-688.

## 4. Scaling of the line weight

Under

\[
V_R(y,s)=R V(Ry,R^2s),
\]

we have

\[
\rho_R=R^2\rho,
\]

while line arclength transforms as

\[
ds_{line,R}=R^{-1}ds_{line}.
\]

Therefore

\[
\boxed{
L_{\rho,R}
=\int\rho_Rds_{line,R}
=R L_\rho.
}
\]

This is the exact missing scale factor between pure flux and enstrophy-weighted measures.

## 5. Scaling of the physicalized crossing measure

M17-326 gives

\[
h_R=R^4h,
\qquad
\delta(\kappa_R)=R^{-2}\delta(\kappa),
\qquad
 d\Phi_R=d\Phi,
\qquad
 ds_R=R^{-2}dt.
\]

Including the line weight,

\[
L_{\rho,R}h_{R,-}\delta(\kappa_R)d\Phi_Rds_R
=
R\,L_\rho h_-\delta(\kappa)d\Phi dt.
\]

Hence

\[
\boxed{
\mathcal C_{-,R}^E(I)
=R\mathcal C_-^E(R^2I).
}
\]

The natural three-dimensional enstrophy physicalization is therefore supercritical by exactly one record-scale power.

## 6. The criticality/physicalization tradeoff

We now have the exact pair

\[
\boxed{
\begin{array}{rcl}
\mathcal C_-&:&\text{scale critical, pure material-flux/genealogy measure},\\[2mm]
\mathcal C_-^E&:&\text{standard enstrophy-weighted spatial current, scale }R^{+1}.
\end{array}
}
\]

Thus the old pure-flux/enstrophy-current mismatch is not merely a technical covariance inconvenience.  It carries one full parabolic scaling power.

This explains why multiplying by the line weight makes the current spatially natural but loses the cross-generation criticality discovered in M17-326.

## 7. Relation to M17-307

M17-307 found that vorticity palinstrophy is also supercritical by one record-scale power and therefore enters the ancestral ledger with \(R^{-1}\).

The same exponent appears here:

\[
\boxed{
\mathcal C_-^E\sim R^{+1}.
}
\]

This is not yet an identity between the two quantities, but it shows that the one-power loss is structurally consistent across the natural enstrophy-weighted physicalizations.

Hence a proof strategy that first converts \(\mathcal C_-\) to \(\mathcal C_-^E\) and only then accumulates generations has reintroduced the M17-307 scale-loss problem.

## 8. Constitutive interpretation

At \(\kappa=0\), M5-682 gives

\[
h
=L_\rho^{op}\kappa
+L_\rho^{op}\sigma
+\mathcal R_{geom},
\]

where

\[
L_\rho^{op}f
:=\rho^{-2}\nabla\cdot(\rho^2\nabla f),
\]

and the linear term \(-\kappa\) vanishes at the zero level.

M5-683/M5-688 then push the **enstrophy-weighted** current to \(\kappa\)-space and decompose it into multiplier diffusion, strain-gradient work, threshold terms, and the explicit geometric remainder.  M17-196 further collapses the latter to palinstrophy-scale and threshold-gradient charges.

Therefore the standard PDE constitutive machinery is already attached to \(\mathcal C_-^E\), not directly to the critical pure-flux measure \(\mathcal C_-\).

## 9. Updated obstruction

The late branch now has a precise choice:

\[
\boxed{
H_{critical\ directed\ crossing}
\Longrightarrow
H_{codim2\ material\ genealogy\ rigidity}
\lor
H_{one\text{-}power\ enstrophy\ physicalization}
\lor
G_{line\text{-}weight/replacement}.
}
\]

To preserve criticality, the next theorem must work directly with material flux/genealogy or with a dimensionless normalization of \(L_\rho\).  Ordinary multiplication by \(L_\rho\) is mathematically legitimate but loses one scale power.

## 10. DSD-theory role and audit

The DSD heuristic was useful in distinguishing a transition channel from a state/volume channel.  The resulting one-power tradeoff is, however, an exact standard-math statement derived from vortex-tube coordinates and Navier--Stokes scaling.

No DSD theoretical axiom is used to assert conservation, compactness, or finiteness.

**Verdict:** PASS as a measure/scaling diagnosis; OPEN as a rigidity mechanism.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
