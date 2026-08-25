# DSD 2026 Liouville Endpoint Audit

Date: 2026-08-25

Status: **CURRENT SURVIVOR COMPARED AGAINST AVAILABLE TYPE-I/ANCIENT LIOUVILLE ROUTES / STRONG-L3 AND APPROXIMATE-SELF-SIMILARITY GAPS IDENTIFIED / NO EXISTING GENERAL THEOREM FOUND THAT CLOSES THE CURRENT CLASS / GLOBAL REGULARITY UNPROVED.**

## 1. Current exact target class

After the local compensated-turnover reductions, the unresolved branch has the schematic form

\[
\boxed{
\text{nonzero recurrent active core}
+
\text{permanently escaping passive critical tail}.
}
\]

The ancient/Leray survivor carries

\[
\sup_s\|\Omega(s)\|_2^2<\infty,
\]

local smoothness/analyticity on every fixed core cylinder, and a critical velocity tail compatible with

\[
U(Y,s)\sim |Y|^{-1},
\qquad
\Omega(Y,s)\sim |Y|^{-2}.
\]

The tail is compatible with finite enstrophy but prevents strong global `L3` control.

## 2. Albritton-Barker local Type-I/Liouville theorem

Albritton and Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems* (Journal of Mathematical Fluid Mechanics, 2019), prove a Liouville theorem for ancient solutions when the velocity is bounded in strong `L3` along a backward sequence of times. They also relate local Type-I singularities to nontrivial mild bounded ancient solutions satisfying the corresponding Type-I condition.

This does not close the present branch because a genuine critical tail

\[
|U|\sim R^{-1}
\]

has

\[
\int_R^\infty|U|^3R^2dR
\sim
\int_R^\infty\frac{dR}{R}
=\infty.
\]

Therefore the exact missing bridge to this theorem is

\[
\boxed{
\text{tail cancellation/extra decay}
\Longrightarrow
\text{strong }L^3\text{ on a backward sequence}.
}
\]

No such bridge is currently proved.

## 3. Weak-L3 is not the same endpoint

The critical `1/R` profile is naturally compatible with the Lorentz endpoint

\[
L^{3,\infty},
\]

but strong `L3` and weak `L3` are not interchangeable in the Albritton-Barker ancient Liouville hypothesis.

Existing large weak-`L3` theory supplies compactness/stability and restrictions on singular sets, but it does not give a general no-singularity theorem for arbitrary large weak-`L3` data that would solve the present ancient branch.

Thus proving only

\[
\sup_s\|U(s)\|_{L^{3,\infty}}<\infty
\]

would be useful but is not by itself the missing Liouville theorem.

## 4. Pineau-Vicol 2026 route

Pineau and Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations*, arXiv:2607.09619 (2026), prove Liouville-type results for rotated backwards self-similar and rotated discretely self-similar solutions under Type-I control in specified rotation/scaling regimes.

They also prove a local regularity criterion: under a Type-I upper bound, sufficiently close local approximate self-similarity at one time slice rules out a singular top-center.

The repository already used the contrapositive of this local criterion to obtain a persistent local self-similar-speed floor of the form

\[
\boxed{
\|U_s(\cdot,s)\|_{L^2(B_R)}
\ge\sigma_0>0
}
\]

for every sufficiently late singular recurrent time in a fixed core ball.

Thus a surviving singular core must remain quantitatively away from the small-self-similar-speed regime.

This theorem therefore narrows the survivor but does not itself force zero.

## 5. Stationary finite-Dirichlet Liouville results do not apply directly

There are strong stationary Liouville theorems for smooth whole-space stationary Navier-Stokes fields under finite Dirichlet integral and appropriate decay assumptions, including modern 2026 results.

The current exact core is an eternal/recurrent **time-dependent Leray trajectory**, not a stationary solution.

A frozen `1/R` tail under the dilation conveyor does not imply that the entire core-plus-tail solution is stationary.

Therefore stationary Liouville theorems cannot be applied without a new step proving

\[
U_s\equiv0
\]

or extracting a nonzero stationary blow-down/profile satisfying the theorem's hypotheses.

The Pineau-Vicol speed floor points in the opposite direction for the local core: a singular survivor must keep `U_s` nonzero.

## 6. Exact endpoint gap

The currently available rigidity doors are therefore:

### Strong-L3 door

\[
\text{strong }L^3\text{ along backward times}
\Longrightarrow
\text{ancient Liouville}.
\]

Blocked by the critical `1/R` tail.

### Approximate-self-similarity door

\[
\text{small local self-similar speed at one slice}
\Longrightarrow
\text{regularity}.
\]

Blocked by the derived positive local speed floor on a singular survivor.

### Stationary door

\[
U_s=0
+
\text{finite-Dirichlet/decay assumptions}
\Longrightarrow
U=0.
\]

Blocked because the recurrent core need not be stationary.

Hence the exact surviving wedge is

\[
\boxed{
\begin{gathered}
\text{nonstationary recurrent core},\\
\text{uniformly positive local Leray speed},\\
\text{finite global enstrophy},\\
\text{critical non-}L^3\text{ escaping tail}.
\end{gathered}
}
\]

## 7. Consequence for the proof strategy

The next calculation should not attempt to reapply a theorem whose endpoint hypothesis is known to fail.

A genuinely new bridge must establish at least one of:

1. **tail coefficient cancellation:** the leading `1/R` component is zero;
2. **supercritical export multiplicity:** repeated permanent export increases the tail coefficient and violates a finite budget;
3. **stationary/blow-down extraction:** a nonzero stationary or (R)DSS outer profile is forced, placing the survivor inside an available Liouville class;
4. **return theorem:** one-way frozen export is impossible, forcing historical recycling into the already typed H/T ledgers;
5. **new recurrent-core rigidity:** a nonzero eternal Leray trajectory with finite enstrophy, positive local speed, and the stated critical tail cannot exist.

## 8. Audit verdict

The literature audit does not close the branch.

It does confirm that the remaining obstruction is not a generic unknown ancient solution: it sits at a recognizable critical endpoint between strong `L3` Liouville theory and weak-`L3`/Type-I compactness.

No claim is made that the absence of a theorem in this audit proves that no such theorem exists; the conclusion is limited to the checked current routes and hypotheses.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]