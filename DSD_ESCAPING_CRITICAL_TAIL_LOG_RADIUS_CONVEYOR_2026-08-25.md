# DSD Escaping Critical Tail: Log-Radius Conveyor and Endpoint Saturation

Date: 2026-08-25

Status: **PERMANENT-EXPORT SURVIVOR SHARPENED / STATIONARY NET-FORCE ROUTE REJECTED / LOG-RADIUS CONVEYOR IDENTIFIED / CRITICAL ENDPOINT REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The remaining global topology after the local D/R/T/H reductions is the permanent-export branch:

\[
\text{positive-frequency material export}
\to
\text{nonreturning critical tail at similarity infinity}.
\]

The aim here is to determine what the far-field Leray equation actually permits and why the existing finite-enstrophy ledgers do not automatically rule it out.

## 2. Leray equation and the critical dilation kernel

Use the autonomous Leray equation

\[
U_s+\frac12U+\frac12Y\cdot\nabla U
+U\cdot\nabla U+\nabla P
=\nu\Delta U,
\qquad \nabla\cdot U=0.
\]

Define the dilation operator

\[
\mathcal D U:=\frac12\left(U+Y\cdot\nabla U\right).
\]

For every vector field homogeneous of degree \(-1\),

\[
U(\lambda Y)=\lambda^{-1}U(Y),
\]

one has exactly

\[
\boxed{\mathcal D U=0.}
\]

Thus the entire degree-\(-1\) class is resonant with the Leray dilation.

This is the basic reason a \(1/R\) tail is critical.

## 3. Why the stationary Landau/net-force argument does not close this branch

For stationary Navier--Stokes in an exterior domain, a \(1/R\) leading term is tied to the Landau family and to nonzero net force under suitable hypotheses.

That fact cannot be imported directly into the present Leray tail.

The reason is structural: in the Leray equation the degree-\(-1\) leading term is annihilated by \(\mathcal D\). At large radius,

\[
U\sim R^{-1}
\]

gives

\[
U\cdot\nabla U,\ \nu\Delta U,\ \nabla P
\sim R^{-3},
\]

whereas the nominal order-\(R^{-1}\) dilation term cancels exactly.

Hence an unforced Leray far field may support a degree-\(-1\) leading tail without invoking the stationary net-force mechanism.

Status: **AUDIT CORRECTION.**

## 4. Exact passive critical transport

Drop the lower-order far-field terms temporarily and retain

\[
U_s+\frac12U+\frac12R\partial_RU=0.
\]

Let

\[
\rho=\log R.
\]

The characteristic equations are

\[
\frac{dR}{ds}=\frac12R,
\qquad
\frac{dU}{ds}=-\frac12U.
\]

Therefore

\[
RU=\text{constant along }\rho-\frac{s}{2}=\text{constant}.
\]

The general passive critical form is

\[
\boxed{
U(R,\theta,s)
=
R^{-1}F\!\left(\theta,\rho-\frac{s}{2}\right).
}
\]

Thus the permanent critical tail is naturally a traveling conveyor in logarithmic radius, moving with speed \(1/2\).

A strict \(R^{-1}A(\theta)\) tail is only the special case where \(F\) is independent of its log-radial argument.

## 5. Relation to positive-frequency export

Suppose uncompensated export events occur with positive Leray-time event frequency and the exported populations do not return.

Under the already derived dilation conveyor,

\[
R(s)\propto e^{(s-s_e)/2}
\]

for a population exported at time \(s_e\).

After thinning the event set by a fixed factor if necessary, one obtains geometrically separated historical shells at any sufficiently late observation time.

Equivalently, in \(\rho=\log R\), the exported populations form a positive-density pulse train in the traveling coordinate

\[
\eta=\rho-\frac{s}{2}.
\]

This is the precise form of the surviving permanent-export topology.

## 6. Why bounded enstrophy permits infinitely many geometric exports

A critical vorticity tail scales as

\[
|\Omega|\sim R^{-2}.
\]

On a dyadic/geometric shell of radius \(R\),

\[
\int_{A_R}|\Omega|^2dY
\sim
R^{-4}\,R^3
\sim
R^{-1}.
\]

For geometric radii

\[
R_k=R_0q^{k/2},
\]

one obtains

\[
\boxed{
\sum_{k\ge0}\int_{A_{R_k}}|\Omega|^2dY
\sim
\sum_{k\ge0}R_k^{-1}
<\infty.
}
\]

Hence a global normalized enstrophy ceiling is fully compatible with infinitely many exported critical shells.

This is not a defect in the earlier enstrophy ledger; it is the exact critical scaling.

## 7. Log-radius weights expose the endpoint

For the passive critical form

\[
U=R^{-1}F(\theta,\eta),
\]

one has schematically

\[
|\nabla U|\sim R^{-2}\mathcal G(F,\partial_\eta F,\nabla_\theta F).
\]

Since

\[
dY=R^2dR\,d\theta=R^3d\rho\,d\theta,
\]

the Dirichlet/enstrophy density satisfies

\[
\boxed{
|\nabla U|^2dY
\sim
e^{-\rho}\,\mathcal G^2\,d\rho\,d\theta.
}
\]

By contrast,

\[
\boxed{
|U|^3dY
\sim
|F|^3\,d\rho\,d\theta.
}
\]

Therefore:

- finite enstrophy sees the log-radius conveyor with the exponentially decaying weight \(e^{-\rho}\);
- the scale-critical \(L^3\) quantity sees the same conveyor with **no radial weight**.

Consequently a positive-density pulse train may have finite total enstrophy while forcing an unbounded strong \(L^3\) accumulation.

## 8. Critical first enstrophy moment

The same distinction is expressed by

\[
\mathcal M_1^\Omega
:=
\int_{\mathbb R^3}|Y|\,|\Omega|^2dY.
\]

For a critical shell,

\[
\int_{A_R}|Y||\Omega|^2dY
\sim 1.
\]

Thus positive-density geometric shells force

\[
\mathcal M_1^\Omega=\infty
\]

in the infinite conveyor limit.

Under first-hitting scaling centered at the tracked core,

\[
Y=\frac{x-X_j}{r_j},
\qquad
\Omega=\frac{\omega}{W_j},
\qquad
r_j^2=\frac\nu{W_j},
\]

one gets the exact scaling identity

\[
\boxed{
\int |Y||\Omega|^2dY
=
\frac1{\nu^2}
\int |x-X_j||\omega|^2dx.
}
\]

Thus a uniform physical first weighted-enstrophy bound would immediately kill the permanent critical conveyor.

However no such uniform bound has yet been derived from the standard Clay energy data; the weighted enstrophy evolution contains stretching and transport terms that are not controlled by the basic energy inequality.

Status: **SUFFICIENT NEW TARGET, NOT PROVED.**

## 9. Endpoint interpretation

The surviving tail therefore lies precisely at the scale-critical border:

\[
\boxed{
\dot H^1/L^6\text{ permits it},
\qquad
L^3\text{ counts every log shell equally}.
}
\]

This matches the known difficulty of replacing the strong \(L^3\) endpoint by the unrestricted weak-\(L^3\) endpoint in general Navier--Stokes regularity theory.

The present proof attempt has therefore not produced an independent contradiction at this step.

Instead it has reduced the final topology to the need for one additional scale-critical unweighted log-shell control.

## 10. Updated frontier

The permanent-export branch is now

\[
\boxed{
\text{positive-frequency export}
\to
\text{positive-density log-radius critical conveyor}.
}
\]

To close it, it is sufficient to prove at least one of:

1. a uniform strong \(L^3\) bound along a backward/recurrent sequence;
2. a uniform first weighted-enstrophy bound
   \(
   \int |Y||\Omega|^2<\infty
   \);
3. a logarithmically improved critical tail estimate that makes the per-shell \(L^3\) mass summable;
4. a return/recycling theorem contradicting permanent nonreturn;
5. a new rigidity theorem for nonstationary recurrent Leray trajectories with a positive-density log-radius conveyor.

## 11. Audit verdict

### PROVED / EXACT

- degree \(-1\) is the kernel of the Leray dilation operator;
- the passive critical tail is a log-radius traveling conveyor;
- geometric critical shells have summable enstrophy cost;
- \(L^3\) and the first weighted-enstrophy moment count critical log shells without the enstrophy decay weight;
- the physical/normalized first weighted-enstrophy scaling identity above.

### REJECTED ROUTE

- stationary Landau net-force cancellation cannot by itself eliminate the time-dependent Leray \(1/R\) tail.

### OPEN

- a scale-critical unweighted log-shell bound strong enough to eliminate the conveyor;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
