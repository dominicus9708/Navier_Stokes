# M20-010 — Axial stretching inserts an exact negative self-covariance into terminal enstrophy reweighting and upgrades the blind state from Q to the joint (Q,gamma) factor

Date: 2026-09-20  
Canonical ID: **M20-010**  
Status: **JOINT PROJECTIVE-STRETCHING COVARIANCE / USING THE M20-009 MAGNITUDE DECOMPOSITION lambda=Y-gamma, THE REWEIGHTING-SELECTION CURRENT OF THE AXIAL STRETCHING SCALAR CONTAINS AN EXACT -Var(gamma) TERM / ANY DIRECTION-FIBER-SILENT REWEIGHTING MUST MATCH DIRECTION-CONDITIONED STRETCHING HETEROGENEITY WITH TRANSPORT-DIFFUSION-DIRECTION-DAMPING HETEROGENEITY / THE NATURAL OBSERVABILITY STATE IS THEREFORE (Q,gamma), BUT A SMALLER JOINT-FIBER BLIND KERNEL STILL EXISTS / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M20-009

M20-009 gives

\[
\lambda
=
X_T+X_S+X_D+X_\xi,
\]

with

\[
X_S=-\gamma.
\]

Define the nonstretching combination

\[
\boxed{
Y:=X_T+X_D+X_\xi.
}
\]

Then

\[
\boxed{
\lambda=Y-\gamma.
}
\]

Let

\[
\alpha=\mathbb E_{\pi_B}\lambda,
\]

and

\[
\phi=\lambda-\alpha.
\]

## 2. Centered form

Write

\[
\bar Y:=\mathbb E_{\pi_B}Y,
\qquad
\bar\gamma:=\mathbb E_{\pi_B}\gamma.
\]

Since

\[
\alpha=\bar Y-\bar\gamma,
\]

we obtain

\[
\boxed{
\phi
=
(Y-\bar Y)
-
(\gamma-\bar\gamma).
}
\]

Thus the relative amplitude reweighting speed is exactly the mismatch between:

- nonstretching local growth heterogeneity;
- axial stretching heterogeneity.

## 3. Exact stretching-selection covariance

Take covariance with \(\gamma\):

\[
\begin{aligned}
\operatorname{Cov}(\lambda,\gamma)
&=
\operatorname{Cov}(Y-\gamma,\gamma)
\\
&=
\operatorname{Cov}(Y,\gamma)
-
\operatorname{Var}(\gamma).
\end{aligned}
\]

Hence

\[
\boxed{
\operatorname{Cov}_{\pi_B}(\lambda,\gamma)
=
-\operatorname{Var}_{\pi_B}(\gamma)
+
\operatorname{Cov}_{\pi_B}(Y,\gamma).
}
\]

This is the main M20-010 signed identity.

## 4. Meaning in the probability-reweighting law

M20-003 gives

\[
\partial_zd\pi_z|_0
=
2\phi\,d\pi_B.
\]

For any fixed terminal observable f, the pure selection contribution is

\[
\left.
\frac d{dz}
\mathbb E_{\pi_z}f
\right|_{\rm rw}
=
2\operatorname{Cov}(\lambda,f).
\]

Set

\[
f=\gamma.
\]

Then

\[
\boxed{
\left.
\frac d{dz}
\mathbb E_{\pi_z}\gamma
\right|_{\rm rw}
=
-2\operatorname{Var}(\gamma)
+
2\operatorname{Cov}(Y,\gamma).
}
\]

Therefore axial stretching heterogeneity creates an intrinsic negative self-selection term in backward wedge depth.

## 5. Time-orientation interpretation

Recall that increasing z moves backward in physical time.

Forward physical stretching

\[
\gamma>0
\]

amplifies vorticity toward the terminal time.

Therefore, when viewed backward in z, high-\(\gamma\) populations naturally lose relative enstrophy weight.

The term

\[
-\operatorname{Var}(\gamma)
\]

is exactly this selection bias.

Moving forward toward the terminal boundary reverses the interpretation: all else equal, higher stretching populations gain enstrophy weight.

## 6. Quantitative uncompensated-stretching gate

Suppose

\[
\operatorname{Cov}(Y,\gamma)
\le
(1-\delta)
\operatorname{Var}(\gamma)
\]

for some

\[
\delta>0.
\]

Then

\[
\boxed{
\operatorname{Cov}(\lambda,\gamma)
\le
-\delta
\operatorname{Var}(\gamma).
}
\]

Thus any quantitative stretching variance produces a quantitative signed selection current unless the nonstretching channels correlate with \(\gamma\) strongly enough to compensate it.

Conversely, if

\[
\operatorname{Cov}(\lambda,\gamma)\approx0
\]

while

\[
\operatorname{Var}(\gamma)>0,
\]

then necessarily

\[
\boxed{
\operatorname{Cov}(Y,\gamma)
\approx
\operatorname{Var}(\gamma).
}
\]

This is a precise compensation requirement.

## 7. Expand the compensating covariance

Since

\[
Y=X_T+X_D+X_\xi,
\]

we have

\[
\boxed{
\operatorname{Cov}(Y,\gamma)
=
\operatorname{Cov}(X_T,\gamma)
+
\operatorname{Cov}(X_D,\gamma)
+
\operatorname{Cov}(X_\xi,\gamma).
}
\]

Therefore suppressing the negative stretching self-covariance requires at least one of:

- transport/homogeneity correlated with stretching;
- scalar diffusion correlated with stretching;
- direction-gradient damping correlated with stretching.

This is a signed covariance fork, not an unsigned norm fork.

## 8. Quantitative covariance alternative

If

\[
\operatorname{Var}(\gamma)\ge g_*>0
\]

and

\[
|\operatorname{Cov}(\lambda,\gamma)|
\le
\varepsilon g_*
\]

with small \(\varepsilon\), then

\[
\operatorname{Cov}(Y,\gamma)
\ge
(1-\varepsilon)g_*.
\]

Hence at least one of the three covariances satisfies

\[
\boxed{
\operatorname{Cov}(X_j,\gamma)
\ge
\frac{1-\varepsilon}{3}g_*
}
\]

for

\[
j\in\{T,D,\xi\}.
\]

Thus a nearly selection-silent stretching variance cannot disappear; it is transferred into a positive correlation with another PDE mechanism.

## 9. Conditional direction-fiber balance

M20-008 defines the projective blind kernel by

\[
\mathbb E[\phi\mid Q]=0.
\]

Using

\[
\phi
=
(Y-\bar Y)-(\gamma-\bar\gamma),
\]

we obtain

\[
\boxed{
\mathbb E[Y\mid Q]-\bar Y
=
\mathbb E[\gamma\mid Q]-\bar\gamma.
}
\]

Thus on a Q-fiber-silent branch, every direction-conditioned stretching bias must be exactly mirrored by the direction-conditioned nonstretching growth bias.

This is a much stronger description than merely saying the direction marginal is stationary.

## 10. Joint (Q,gamma) observability

The natural enlarged state is

\[
\boxed{
Z_{Q\gamma}:=(Q,\gamma).
}
\]

For any bounded observable

\[
F(Q,\gamma),
\]

the reweighting-selection derivative is

\[
\boxed{
\left.
\frac d{dz}
\mathbb E_{\pi_z}F(Q,\gamma)
\right|_{\rm rw}
=
2\mathbb E[\phi F(Q,\gamma)].
}
\]

Hence the exact blind kernel for all joint \((Q,\gamma)\) observables is

\[
\boxed{
\mathbb E[\phi\mid Q,\gamma]=0.
}
\]

This strictly refines the pure-projective blind kernel

\[
\mathbb E[\phi\mid Q]=0.
\]

## 11. New reweighting split

The M20-008 fiber branch therefore refines to

\[
\boxed{
R_{\rm fiber}^{Q}
\Longrightarrow
R_{Q\gamma}
\lor
R_{\rm fiber}^{Q\gamma},
}
\]

where

\[
R_{Q\gamma}:
\mathbb E[\phi\mid Q,\gamma]\neq0,
\]

and

\[
R_{\rm fiber}^{Q\gamma}:
\mathbb E[\phi\mid Q,\gamma]=0
\quad\text{but}\quad
\mathbb E[\phi^2]>0.
\]

The latter remains hidden even after attaching axial stretching to projective direction.

## 12. Explicit joint-fiber anti-model

Let

\[
(Q,\gamma)
\]

be fixed on two or more spatial states, but let

\[
\phi
\]

take positive and negative values with zero conditional mean inside each identical \((Q,\gamma)\) fiber.

Then

\[
\operatorname{Var}(\lambda)>0,
\]

yet

\[
\mathbb E[\phi F(Q,\gamma)]=0
\]

for every joint observable \(F\).

Thus the \((Q,\gamma)\) enlargement improves observability but is still not complete in principle.

This is a kinematic state-space counterexample, not a Navier--Stokes solution.

## 13. Coupling to projective strain

M20-006 gives the material projective-strain law

\[
\frac12D_t|s_\perp|^2
=
-2\gamma|s_\perp|^2
+\text{pressure/diffusion/projective forcing}.
\]

Thus \(\gamma\) plays two roles simultaneously:

1. it contributes \(-\gamma\) to backward-depth vorticity-amplitude growth;
2. it damps or amplifies projective strain noncommutation through \(-2\gamma s_\perp\).

This is the first direct shared scalar between the reweighting and projective-strain branches.

Positive \(\gamma\) favors forward vorticity amplification while damping transverse strain misalignment.

Negative \(\gamma\) does the opposite.

## 14. Structural competition

The same axial stretching field therefore creates a built-in competition:

\[
\boxed{
\gamma>0:
\quad
\text{amplitude amplification}
+
\text{projective strain alignment},
}
\]

\[
\boxed{
\gamma<0:
\quad
\text{amplitude compression}
+
\text{projective strain misalignment amplification}.
}
\]

A recurrent hard survivor that needs both strong terminal amplitude selection and persistent projective noncommutation must organize compensating pressure/diffusion/transport phases around this competition.

This is structural information, not yet a contradiction.

## 15. Updated M20 joint target

The relevant joint state is now at least

\[
\boxed{
(Q,\gamma,[S,Q]).
}
\]

A promising signed observable is the enstrophy-weighted covariance between relative growth and axial stretching,

\[
\boxed{
C_{\lambda\gamma}
=
\operatorname{Cov}_{\pi_B}(\lambda,\gamma).
}
\]

A second is the projective-strain-weighted stretching moment

\[
\boxed{
\mathbb E_{\pi_B}
[
\gamma\|[S,Q]\|_F^2
].
}
\]

M20-006 shows the latter controls homogeneous damping/amplification of projective noncommutation along material trajectories.

## 16. Next target

M20-011 should determine whether the two signed quantities

\[
C_{\lambda\gamma}
\]

and

\[
\mathbb E[
\gamma\|[S,Q]\|_F^2
]
\]

can both remain asymptotically neutral on a recurrent hard component without forcing one of:

- transverse pressure-Hessian covariance;
- scalar diffusion/stretching covariance;
- direction-gradient/stretching covariance;
- or same-lineage material hysteresis.

The goal is a **joint signed compensation matrix**, not another scalar norm.

\[
\boxed{\text{M20-010 COMPLETE; AXIAL STRETCHING CONTRIBUTES AN EXACT NEGATIVE SELF-COVARIANCE TO TERMINAL REWEIGHTING AND DEFINES THE NATURAL JOINT (Q,gamma) FACTOR.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
