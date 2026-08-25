# DSD W1 Periodic Tail: Energy-Flux Decomposition of the Second-Tail Charge

Date: 2026-08-26

Status: **SECOND-TAIL CHARGE DECOMPOSED INTO VISCOUS CELL DISSIPATION PLUS DISCRETELY SCALED EULERIAN ENERGY FLUX / ZERO CHARGE IDENTIFIED AS AN EXACT STATIONARY-TRACE SCALE-BALANCE CONDITION, NOT AS ZERO DYNAMICS / NO SIGN CLOSURE YET / GLOBAL REGULARITY UNPROVED.**

## 1. Canonical charge

On the H2-coherent periodic W1 branch the leading physical critical trace is

\[
T_*(x)
=
|x|^{-1}
\Phi(\widehat x,\log|x|)
\]

(after translating the singular point to the origin), with discrete homogeneity

\[
T_*(\lambda x)=\lambda^{-1}T_*(x),
\qquad
\lambda=e^{S/2}>1.
\]

Its projected stationary Navier--Stokes residual on the punctured space is

\[
\mathcal R(T_*)
:=
\nu\Delta T_*
-(T_*\cdot\nabla)T_*
-\nabla P_*.
\]

The canonical second-tail coefficient is the same residual in fixed-cell variables, and the preceding note defines

\[
\mathfrak A_F
=
\langle F_\infty,\mathcal N[F_\infty]\rangle.
\]

Equivalently, on a radius-R DSS cell,

\[
\int_{R<|x|<\lambda R}
T_*\cdot\mathcal R(T_*)dx
=
R^{-1}\mathfrak A_F.
\]

## 2. Define the physical Eulerian energy flux through a sphere

For the static trace define

\[
\boxed{
\mathcal J(r)
:=
\nu\int_{|x|=r}T_*\cdot\partial_rT_*\,dS
-
\frac12\int_{|x|=r}|T_*|^2T_*\cdot n\,dS
-
\int_{|x|=r}P_*T_*\cdot n\,dS.
}
\]

This is the boundary term obtained when the projected stationary residual is paired with `T_*` on a ball/shell.

It is an Eulerian scale-energy flux.  It is **not** automatically the moving-volume material-turnover functional used elsewhere in the DSD audit.

## 3. Exact shell energy identity

Let

\[
C_R:=\{R<|x|<\lambda R\}.
\]

Integration by parts gives

\[
\begin{aligned}
\int_{C_R}T_*\cdot\mathcal R(T_*)dx
={}&
-\nu\int_{C_R}|\nabla T_*|^2dx\\
&+\mathcal J(\lambda R)-\mathcal J(R).
\end{aligned}
\]

Thus

\[
\boxed{
R^{-1}\mathfrak A_F
=
-\nu\int_{C_R}|\nabla T_*|^2dx
+\mathcal J(\lambda R)-\mathcal J(R).
}
\]

No approximation is used in this shell identity on the punctured domain.

## 4. Discrete scaling of both terms

The degree-`-1` discrete homogeneity gives

\[
\nabla T_*(\lambda x)=\lambda^{-2}\nabla T_*(x).
\]

Therefore

\[
\int_{C_R}|\nabla T_*|^2dx
=R^{-1}\mathfrak D_F,
\]

where `D_F` is the positive fixed-cell gradient-energy coefficient.

The pressure has degree `-2` under the same discrete scaling, and each term in `J` scales like `r^-1`.  Hence

\[
\boxed{
\mathcal J(\lambda R)=\lambda^{-1}\mathcal J(R).
}
\]

Write

\[
\mathcal J(R)=R^{-1}\mathfrak J_F
\]

at a fixed log phase.  Then

\[
\boxed{
\mathfrak A_F
=
-\nu\mathfrak D_F
+(\lambda^{-1}-1)\mathfrak J_F
}
\]

or equivalently

\[
\boxed{
\mathfrak A_F
=
-\nu\mathfrak D_F
-(1-\lambda^{-1})\mathfrak J_F.
}
\]

This is the exact flux decomposition of the canonical second-tail charge.

## 5. Inward-flux convention

If one defines positive inward energy supply by

\[
\mathfrak I_F:=-\mathfrak J_F,
\]

then

\[
\boxed{
\mathfrak A_F
=
(1-\lambda^{-1})\mathfrak I_F
-\nu\mathfrak D_F.
}
\]

Thus the charge is simply

\[
\boxed{
\text{inward scale supply across one DSS cell}
-
\text{viscous dissipation in that cell}.
}
\]

The geometric factor `1-lambda^-1` is forced by discrete degree-`-1` scaling.

## 6. Meaning of zero charge

The condition

\[
\mathfrak A_F=0
\]

is equivalent to

\[
\boxed{
(1-\lambda^{-1})\mathfrak I_F
=
\nu\mathfrak D_F.
}
\]

Therefore zero second-tail energy charge does **not** mean that the leading trace is dynamically empty or that its gradient vanishes.

It means that its Eulerian inward scale flux pays its positive viscous cell dissipation exactly, so the leading static critical trace is energetically balanced at the log-cell level.

The full vector residual may still be nonzero even if its pairing with `T_*` vanishes.

## 7. Meaning of nonzero charge

If

\[
\mathfrak A_F\ne0,
\]

then the static critical trace has an energy imbalance on every corresponding DSS cell.  The canonical nonresonant correction

\[
T_{-3}
=-r^{-3}\mathcal N[F_\infty]
\]

is the first time-dependent response that carries this imbalance in the actual periodic Leray solution.

The renormalized shell-energy asymptotic is

\[
\int_{C_R}(|U|^2-|T|^2)
=
-2\mathfrak A_F R^{-1}+o(R^{-1}).
\]

Hence the sign of `A_F` determines from which side the actual orbit approaches the finite renormalized energy of its passive critical trace.

## 8. Why this still does not close the branch

Neither `J_F` nor `I_F` has a predetermined sign under the present hypotheses.  The pressure and nonlinear transport terms can transfer energy between logarithmic scales, while viscosity dissipates it.

Thus

\[
\mathfrak A_F
=
(1-\lambda^{-1})\mathfrak I_F-\nu\mathfrak D_F
\]

is a structural decomposition but not yet a sign-definite Lyapunov identity.

A closure would follow from an independent estimate forcing, for example,

\[
(1-\lambda^{-1})\mathfrak I_F
<\nu\mathfrak D_F
\]

or the opposite inequality together with a contradictory finite-core budget.  No such universal inequality has been proved here.

## 9. Updated periodic coherent target

The scalar tail question is now sharply stated:

\[
\boxed{
\text{Can a nonzero divergence-free log-periodic degree-1 critical trace sustain}
\quad
(1-\lambda^{-1})\mathfrak I_F
\text{ against }\nu\mathfrak D_F
\text{ while remaining compatible with the recurrent finite core?}
}
\]

This is narrower than the former unspecified core-tail interface problem.

## 10. DSD audit

The following are kept separate:

- Eulerian fixed-sphere energy flux;
- material/moving-volume turnover;
- similarity-coordinate radial dilation flux;
- viscous dissipation;
- full vector residual versus its scalar energy pairing.

No flux category is renamed into another without a bridge identity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
