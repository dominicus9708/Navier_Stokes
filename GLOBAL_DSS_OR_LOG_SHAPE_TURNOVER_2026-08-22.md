# Global DSS-or-Log-Shape-Turnover Reduction — 2026-08-22

Status: **LITERATURE-ASSISTED CONDITIONAL REDUCTION. DSS-LIKE LIMIT BRANCH ONLY; NOT A DIRECT S-CLOSURE OF ALL SMOOTH STAGES. GLOBAL REGULARITY NOT PROVED.**

This note follows `GLOBAL_CRITICAL_HISTORICAL_SHELL_TOWER_2026-08-22.md`. The historical shell tower is compatible with all current energy/enstrophy packing estimates and has the borderline form `u~1/r`, i.e. bounded weak-L3 with logarithmically divergent strong L3.

The purpose here is to separate the tower into:

1. asymptotically recurrent/DSS-like shell recycling;
2. persistent log-scale shape turnover.

The first branch can be excluded under a standard Type-I/precompactness envelope by known backward-DSS results for scaling factor sufficiently close to one. The second branch remains the new active frontier.

## 1. Backward similarity variables

Assume hypothetically that the first singular point is `(X_*,T_*)`. Set

\[
\tau=T_*-t,
\qquad
s=-\log\tau,
\qquad
y=\frac{x-X_*}{\sqrt\tau},
\]

and define

\[
\boxed{
V(y,s)=\sqrt\tau\,u(X_*+\sqrt\tau\,y,T_*-\tau).
}
\]

A backward `lambda`-DSS solution obeys

\[
u(x,t)=\lambda u(X_*+\lambda(x-X_*),T_*+\lambda^2(t-T_*)).
\]

In similarity variables this becomes periodicity with period

\[
\boxed{
T_\lambda=2\log\lambda.
}
\]

Thus

\[
V(y,s+T_\lambda)=V(y,s)
\]

for an exact backward `lambda`-DSS orbit.

## 2. Recurrence defect

For `p>3` and fixed `R`, define

\[
\boxed{
\mathfrak D_{\lambda,p,R}(s)
=\|V(\cdot,s+T_\lambda)-V(\cdot,s)\|_{L^p(B_R)}.
}
\]

This is a finite-stage observable of the actual smooth solution in standard backward similarity coordinates.

A quiet shell-recycling lane would require, at least along late times,

\[
\mathfrak D_{\lambda,p,R}(s)\to0
\]

for every fixed `R` and suitable `p>3`, together with enough spatial tail control to identify one global limiting profile.

## 3. Conditional compactness package

The DSS-limit implication requires more than endpoint resemblance. Assume the shell-recycling branch supplies the following uniform package:

1. local parabolic precompactness of `V` on every bounded similarity cylinder;
2. a Type-I pointwise envelope
   \[
   |V(y,s)|\le \frac{C_*}{1+|y|};
   \]
3. nontrivial normalization inherited from the vorticity record core;
4. for one fixed `lambda>1`,
   \[
   \mathfrak D_{\lambda,p,R}(s)\to0
   \]
   for every fixed `R` and some `p>3`.

Then a diagonal subsequence yields a nontrivial limiting ancient similarity orbit `V_infty` satisfying

\[
V_\infty(s+T_\lambda)=V_\infty(s).
\]

Returning to physical variables, this is a backward `lambda`-DSS solution with the pointwise Type-I bound

\[
|u_\infty(x,t)|\le \frac{C_*}{\sqrt{-t}+|x|}.
\]

## 4. Near-one DSS exclusion

Chae and Wolf, *Removing discretely self-similar singularities for the 3D Navier-Stokes equations* (2016), prove that for every `C_*>0` there exists

\[
\lambda_*(C_*)>1
\]

such that every smooth backward `lambda`-DSS solution satisfying

\[
|u(x,t)|\le \frac{C_*}{\sqrt{-t}+|x|}
\]

is trivial whenever

\[
1<\lambda<\lambda_*(C_*).
\]

They also exclude an asymptotically DSS singularity under an explicit local-Lp convergence hypothesis.

Therefore, if we choose a geometric first-hitting ratio

\[
q=\lambda^2
\]

with

\[
1<\lambda<\lambda_*(C_*),
\]

the quiet asymptotically recurrent branch above is impossible because the limit is nontrivial by record normalization.

## 5. Finite-stage contrapositive

Under the compactness/envelope package, a surviving bounded weak-L3 Type-I shell tower must therefore violate asymptotic recurrence.

Hence for every admissible near-one `lambda`, there exist some bounded radius `R`, some `p>3`, a constant `delta_DSS>0`, and a sequence `s_n->infinity` such that

\[
\boxed{
\mathfrak D_{\lambda,p,R}(s_n)\ge\delta_{DSS}>0.
}
\]

This is a finite smooth statement on the original rescaled stages: the shell tower must keep paying an order-one log-scale profile-change event.

Call this complement

\[
\boxed{T_{log-shape}.}
\]

## 6. Why this does not yet prove global regularity

The argument above does **not** supply a globally finite positive budget controlling

\[
\sum_n\mathfrak D_{\lambda,p,R}(s_n).
\]

A fixed recurrence defect per logarithmic scale can in principle coexist with finite physical kinetic-energy dissipation, just as one natural T/H packet per scale can.

Thus the role of the DSS theorem is not to finish the proof, but to remove the most economical recurrent realization of the critical shell tower.

The surviving bounded weak-L3 Type-I branch must be genuinely nonstationary in logarithmic scale.

## 7. Updated critical frontier

The historical shell tower now splits as

\[
\boxed{
\begin{aligned}
&\text{asymptotically near-one DSS-like}
&&\to\text{excluded under the compactness/Type-I envelope package},\\
&\text{not asymptotically DSS-like}
&&\to T_{log-shape}\text{ infinitely often}.
\end{aligned}
}
\]

A separate branch remains if the weak-L3/Type-I envelope itself becomes unbounded; denote it by

\[
C_{weak-L3}.
\]

Thus the final global alternatives are sharpened to

\[
\boxed{
T_{log-shape}
\quad\lor\quad
C_{weak-L3}
\quad\lor\quad
\text{failure of the local compactness/envelope package}.
}
\]

The next direct task is to convert the order-one recurrence defect `T_log-shape` into one of the already quantified finite-stage mechanisms: boundary/material turnover, direction roughness, spectral-sign turnover, derivative packet, or active outer strain.

Status: **THE QUIET RECURRENT WEAK-L3 SHELL TOWER IS CONDITIONALLY REMOVED BY NEAR-ONE BACKWARD-DSS NONEXISTENCE. A SURVIVOR WITH BOUNDED TYPE-I ENVELOPE MUST KEEP GENERATING ORDER-ONE LOG-SCALE PROFILE DEFECTS. THE GLOBAL NONSUMMABILITY OF THOSE DEFECTS IS STILL OPEN.**