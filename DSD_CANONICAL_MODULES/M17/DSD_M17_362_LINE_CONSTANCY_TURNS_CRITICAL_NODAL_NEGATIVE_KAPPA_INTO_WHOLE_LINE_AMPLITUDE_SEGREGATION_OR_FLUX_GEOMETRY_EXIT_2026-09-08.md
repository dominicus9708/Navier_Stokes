# DSD M17-362 — Line constancy turns critical nodal negative-kappa into whole-line amplitude segregation or flux/geometry exit

Date: 2026-09-08  
Canonical ID: **M17-362**

Status: **ACTIVE CRITICAL-NODAL BRANCH REDUCTION / EXACT CE-H**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M17-310 gives the amplitude-independent critical lower bound

\[
\boxed{
\|\kappa_-\|_{L^{3/2}}\ge S_3>0.
}
\]

M17-311 splits the negative coefficient phase into a high-amplitude capture branch or a critical nodal/low-amplitude concentration branch.

The present module revisits the latter using the exact CE-H identity from M17-313:

\[
\boxed{D_\xi\kappa=0.}
\]

## 2. Negative coefficient is line-saturated

Let `Gamma_lambda` be one connected regular vortex line at a fixed time. Since

\[
D_\xi\kappa=0,
\]

there exists one scalar value

\[
\kappa_\lambda
\]

such that

\[
\boxed{
\kappa(x)=\kappa_\lambda
\quad\text{for every }x\in\Gamma_\lambda.
}
\]

Therefore the sign of `kappa` cannot occupy only one spatial subsegment of a connected regular vortex line.

In particular,

\[
\boxed{
\Gamma_\lambda\cap\{\kappa<0\}\ne\varnothing
\Longrightarrow
\Gamma_\lambda\subset\{\kappa<0\}.
}
\]

Thus a negative-`kappa` patch cannot migrate toward the nodal set along an otherwise positive-`kappa` connected vortex line.

## 3. Separate coefficient phase from amplitude phase

Fix a high-amplitude threshold

\[
a_*>0.
\]

For a negative coefficient line define its captured high-amplitude arclength

\[
\ell_{hi}(\lambda)
:=
\int_{\Gamma_\lambda}
\mathbf1_{\{\rho\ge a_*\}}ds.
\]

Because `kappa_lambda<0` is constant along the line, every high-amplitude segment on that line is automatically a high-amplitude negative-coefficient segment.

Thus the only way a negative line can contribute exclusively to the nodal/low-amplitude branch is for its high-amplitude captured arclength to vanish or degenerate.

## 4. Positive-flux family with nondegenerate high-amplitude capture returns to M17-312

Let `Lambda_-` be a material flux-label family of negative-`kappa` lines with

\[
\int_{\Lambda_-}d\Phi\ge\Phi_->0.
\]

Suppose on a subfamily of positive flux measure

\[
\ell_{hi}(\lambda)\ge\ell_*>0
\]

and the negative coefficient magnitude has a retained lower moment as supplied by the M17-311 allocation.

Then, because the sign and value are line-constant, the flux-length negative phase has a positive lower charge of the same type used in M17-312:

\[
\int_{\Lambda_-}
\int_{\Gamma_\lambda}
\mathbf1_{\{\rho\ge a_*\}}
\kappa_-\,ds\,d\Phi
>0.
\]

Hence this subbranch is not genuinely nodal; it routes back to

\[
\boxed{H_{high\text{-}amplitude\ negative\ flux\text{-}length\ occupancy}.}
\]

The exact quantitative constant depends on the M17-311 coefficient-moment allocation and is not invented here.

## 5. Correct nodal survivor

If the M17-311 high-amplitude branch is absent, the critical negative phase must therefore survive through at least one of the following:

\[
\boxed{G_{whole\text{-}line\ low\text{-}amplitude\ segregation},}
\]

meaning the negative coefficient is carried by vortex-line families whose captured high-amplitude arclength tends to zero;

\[
\boxed{G_{negative\text{-}line\ flux\ thinning},}
\]

meaning the negative lines that do reach high amplitude carry vanishing material-flux measure;

\[
\boxed{G_{capture\ length/segment\ collapse},}
\]

or

\[
\boxed{G_{nodal/interface/rank\ termination}.}
\]

Thus the critical nodal branch is no longer an unspecified local concentration near `rho=0`.

## 6. No along-line nodal migration escape

Before using `D_xi kappa=0`, one could imagine the negative coefficient charge occupying a moving low-amplitude portion of one line while the same line possessed an unrelated high-amplitude portion with another coefficient sign.

That mechanism is impossible on exact CE-H.

The remaining amplitude segregation is instead between **different material line families**, or between different retained/cutoff portions of a line whose common coefficient sign is already fixed.

This distinction is important for the next flux-area estimate.

## 7. Interaction with material genealogy

M17-359 proves that regular CE-H material flow preserves vortex-line identity. Therefore the whole-line low-amplitude segregation in Section 5 is itself materially meaningful: it cannot be erased by silently relabeling the same regular line as a different lineage.

If the negative-line population changes identity, the change must pass through the M17-359 nodal/cutoff/interface/rank/domain exits.

## 8. DSD-theory role

The heuristic is to distinguish a local amplitude phase from a line-saturated coefficient phase. The proof is the exact PDE consequence `D_xi kappa=0` plus flux-line bookkeeping.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated critical nodal branch

\[
\boxed{
\begin{aligned}
G_{critical\ nodal\ \kappa_-}
\Longrightarrow{}&
G_{whole\text{-}line\ low\text{-}amplitude\ segregation}\\
&\lor G_{negative\text{-}line\ flux\ thinning}\\
&\lor G_{capture\ segment\ collapse}\\
&\lor G_{nodal/interface/rank/domain\ exit}.
\end{aligned}
}
\]

The next target is to test whether a positive total material flux can remain entirely on whole-line low-amplitude families inside a bounded compact transversal geometry.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
