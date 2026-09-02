# DSD M5-599 — CE-H local equalities analytically globalize

Date: 2026-09-03

Status: **EXTERNAL-THEOREM-DEPENDENT RIGIDITY STEP. ON THE CE-H BRANCH, THE PRODUCTION-PAYING CARRIER CONTAINS A NONEMPTY OPEN BALL ON WHICH `W x Sigma W = 0` AND `W x Delta W = 0`. SPATIAL ANALYTICITY AT EACH SMOOTH ANCIENT TIME EXTENDS THESE IDENTITIES TO ALL SPACE AT THAT TIME. BECAUSE THE CE-H PRODUCTION TIMES HAVE POSITIVE MEASURE, TIME ANALYTICITY OF STRONG/BOUNDED-MILD NAVIER--STOKES SOLUTIONS EXTENDS THEM TO THE WHOLE CONNECTED ANCIENT TIME INTERVAL. THUS CE-H IS NOT MERELY A LOCAL CARRIER GEOMETRY: IT FORCES A GLOBAL SPACE-TIME DOUBLE-EIGENLINE CLASS. ALIGNMENT ITSELF IS NOT A CONTRADICTION; BURGERS-TYPE EXACT SOLUTIONS SHOW THAT SUCH LOCAL ALGEBRA CAN OCCUR, ALTHOUGH THEIR BACKGROUND STRAIN IS NOT IN THE PRESENT FINITE-ENERGY CLASS. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Input from M5-595/M5-597

On CE-H, during a positive-measure set of production-linked events, the coherent payer carrier contains an open ball on which

\[
\tau=0,
\qquad
\mathcal D_\xi=0.
\]

Equivalently, where

\[
W=\rho\xi,
\qquad \rho>0,
\]

we have

\[
\boxed{
(I-\xi\otimes\xi)\Sigma W=0,
}
\]

and

\[
\boxed{
(I-\xi\otimes\xi)\Delta W=0.
}
\]

These can be written without dividing by \(\rho\):

\[
\boxed{
W\times\Sigma W=0,
}
\]

and

\[
\boxed{
W\times\Delta W=0.
}
\]

The cross-product form is defined and smooth even at vorticity zeros.

## 2. Spatial analyticity removes the carrier localization

The inherited ancient solution is smooth for every physical time \(s<0\), and the existing analytic corridor supplies spatial real analyticity.

At any CE-H production time, each component of

\[
\mathcal X_1(x,s)
:=
\omega(x,s)\times S(x,s)\omega(x,s),
\]

and

\[
\mathcal X_2(x,s)
:=
\omega(x,s)\times\Delta\omega(x,s)
\]

is real analytic in \(x\).

The similarity and physical versions differ only by nonzero scale factors, so zero of the similarity cross products on the payer ball implies zero of \(\mathcal X_1,\mathcal X_2\) on a nonempty physical open ball.

The identity theorem for real-analytic functions on connected \(\mathbb R^3\) therefore gives

\[
\boxed{
\mathcal X_1(\cdot,s)=0,
\qquad
\mathcal X_2(\cdot,s)=0
\quad\text{on all }\mathbb R^3
}
\]

at every CE-H production time.

Thus one local open carrier event already globalizes spatially at that time.

## 3. Positive-measure CE-H times

M5-589--M5-593 construct the production-linked event set with positive invariant time measure.

On the CE-H subbranch, the relevant nonnegative carrier actions vanish on a positive-measure subset of those production times.

Hence the set

\[
\mathcal T_{CEH}
:=
\{s<0:\mathcal X_1(\cdot,s)=\mathcal X_2(\cdot,s)=0\}
\]

has positive measure after conversion between similarity time and physical time on any finite compact time window containing a density point.

## 4. External theorem: time analyticity

This step explicitly imports a standard external theorem.

Strong incompressible Navier--Stokes solutions are analytic in time in their interval of strong existence in standard functional settings. Pointwise time analyticity for bounded mild whole-space solutions and joint space-time analyticity results are also available in the literature.

The present ancient element is smooth and Type-I bounded on every compact time interval strictly inside \(( -\infty,0)\), so it lies in the local strong/bounded-mild regime needed for this analyticity use.

Therefore, for every fixed spatial point \(x\),

\[
s\mapsto \mathcal X_1(x,s),
\qquad
s\mapsto \mathcal X_2(x,s)
\]

are real analytic on each compact subinterval of \(( -\infty,0)\).

## 5. Positive-measure zeros force time-global zeros

A nontrivial real-analytic scalar function cannot have a positive-measure zero set in an interval.

Since every component of \(\mathcal X_1(x,s)\) and \(\mathcal X_2(x,s)\) vanishes for every

\[
s\in\mathcal T_{CEH}
\]

and \(\mathcal T_{CEH}\) has an interior accumulation point in time, time analyticity implies

\[
\boxed{
\mathcal X_1(x,s)=0,
\qquad
\mathcal X_2(x,s)=0
}
\]

for all \(s\) in the connected ancient interval and every fixed \(x\).

Hence

\[
\boxed{
\omega\times S\omega\equiv0,
\qquad
\omega\times\Delta\omega\equiv0
\quad\text{on }\mathbb R^3\times(-\infty,0).
}
\]

Equivalently in similarity variables,

\[
\boxed{
W\times\Sigma W\equiv0,
\qquad
W\times\Delta W\equiv0
\quad\text{for all }(y,\theta).
}
\]

## 6. Global double-eigenline formulation

On the open set \(\{W\ne0\}\), there exist scalar fields \(\sigma\) and \(\kappa\) such that

\[
\boxed{
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W.
}
\]

Therefore the CE-H branch has been promoted from a local production-carrier condition to a global space-time overdetermined class.

The direction equation gives globally on \(\{W\ne0\}\)

\[
\boxed{D_B\xi=0.}
\]

Thus viscosity changes only the magnitude of vorticity, not its direction, throughout the solution.

## 7. External-theory firewall: alignment is not itself impossible

The conclusion

\[
S\omega\parallel\omega
\]

must **not** be called a contradiction.

Burgers vortices and related stretched-vortex exact solutions are well-known Navier--Stokes examples in which vorticity aligns with a strain eigenvector and viscous diffusion balances stretching.

The distinction is that the classical Burgers construction contains a nondecaying linear background strain and therefore does not belong to the present whole-space finite-enstrophy / \(U\in L^6\), \(\Sigma\in L^2\) ancient class.

Accordingly, the valid next question is not whether aligned vortices exist locally, but whether a nonzero **finite-enstrophy, decaying, recurrent ancient solution can satisfy the double-eigenline relations globally in space-time**.

## 8. Dependency status

This note should be classified as

- validity role: `EXTERNAL_THEOREM + INTERNAL_APPLICATION`;
- proof role: `OPEN-RIGIDITY REDUCTION`;
- external dependencies: spatial/time analyticity of smooth/strong or bounded-mild Navier--Stokes solutions.

If the precise functional setting of the imported time-analyticity theorem fails on the extracted ancient class, the global-in-time conclusion must be downgraded to the already valid global-in-space conclusion at positive-measure CE-H times.

## 9. Next target

Study the global double-eigenline system

\[
\boxed{
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W,
\qquad
\nabla\cdot W=0,
\qquad
W\in L^2\cap H^m\ \forall m,
}
\]

and exploit its exact divergence, transport, and commutator consequences.

Status: **CE-H HAS BEEN REDUCED, SUBJECT TO THE STATED ANALYTICITY THEOREM, TO A GLOBAL SPACE-TIME DOUBLE-EIGENLINE NAVIER--STOKES CLASS. THIS IS A GENUINE RIGIDITY REDUCTION, NOT YET A NONEXISTENCE THEOREM. GLOBAL REGULARITY REMAINS UNPROVED.**