# DSD M5-596 — Finite-depth payer return: radial balance and marker-migration fork

Date: 2026-09-03

Status: **A PERSISTENT PRODUCTION-PAYING LINEAGE THAT RETURNS TO THE FIXED FINITE-DEPTH ANNULUS OBEYS AN EXACT SIMILARITY-RADIAL COBoundary. IF ONE MATERIAL MARKER REMAINS ACTIVE ACROSS RETURNS, ITS RETURN-CYCLE AVERAGE SATISFIES `<U_r/r>=-1/2`, AND ITS NONDEGENERATE AMPLITUDE OBEYS THE EXISTING PARALLEL BALANCE `<sigma + Delta rho/rho - |grad xi|^2>=1`. IF THE ACTIVE MARKER MIGRATES, THE AMPLITUDE COBoundary CANNOT BE USED; THE BRANCH RETURNS TO THE M5-520--522 SURFACE-CURRENT MIGRATION COST. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Similarity material trajectory

Let a material representative of the persistent payer lineage satisfy

\[
Y'(\theta)=B(Y,\theta),
\qquad
B=U+\frac12Y.
\]

Write

\[
r(\theta)=|Y(\theta)|,
\qquad
n(\theta)=Y/r,
\qquad
U_r=U(Y,\theta)\cdot n.
\]

Then exactly

\[
\boxed{
r'=U_r+\frac12r.
}
\]

Hence

\[
\boxed{
\frac{d}{d\theta}\log r
=
\frac12+rac{U_r}{r}.
}
\]

## 2. Wedge-depth form

Set

\[
z=r^{-2}.
\]

Then

\[
\boxed{
\frac{z'}{z}
=-1-2\frac{U_r}{r}.
}
\]

Using the wedge profile \(U=r^{-1}F\),

\[
\frac{U_r}{r}=zF_r,
\]

so

\[
\boxed{
z'=-z(1+2zF_r).}
\]

For the scale-translation coordinate

\[
q=\log r-\frac\theta2,
\]

one obtains

\[
\boxed{q'=\frac{U_r}{r}=zF_r.}
\]

Thus the material radial motion has an exact wedge representation.

## 3. Return-cycle radial identity

Let

\[
\theta_1<\theta_2<\cdots
\]

be production-linked return times at which the same material representative lies in the fixed annulus

\[
r_-\le r(\theta_j)\le r_+,
\]

with

\[
0<r_-<r_+<\infty.
\]

Integrating the radial equation from \(\theta_1\) to \(\theta_N\),

\[
\int_{\theta_1}^{\theta_N}
\frac{U_r}{r}d\theta
=
-\frac12(\theta_N-\theta_1)
+
\log\frac{r(\theta_N)}{r(\theta_1)}.
\]

The endpoint logarithm is uniformly bounded.

Therefore

\[
\boxed{
\lim_{N\to\infty}
\frac1{\theta_N-\theta_1}
\int_{\theta_1}^{\theta_N}
\frac{U_r}{r}d\theta
=-\frac12.
}
\]

This is an exact return-cycle balance; no ergodic approximation is required beyond the existence of infinitely many returns with unbounded total elapsed time.

## 4. Consequence: similarity outward drift must be canceled

The explicit similarity drift contributes \(+r/2\) to \(r'\).

A recurrent finite-depth material trajectory must therefore pay, on average,

\[
\boxed{\left\langle\frac{U_r}{r}\right\rangle_{return}=-\frac12.}
\]

Thus the physical velocity supplies exactly enough inward radial transport, in return-cycle average, to cancel the similarity dilation.

This is independent of the vorticity-direction equations.

## 5. Nondegenerate same-marker amplitude balance

Assume now that the **same material marker** remains an active representative at the selected return times and has fixed amplitude bounds

\[
0<\rho_-\le\rho(Y(\theta_j),\theta_j)\le\rho_+<\infty.
\]

The exact material amplitude equation is

\[
\boxed{
D_B\log\rho
=
\sigma-1
+
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2.
}
\]

Integrating between return times gives

\[
\begin{aligned}
\int_{\theta_1}^{\theta_N}
\left(
\sigma
+
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2
\right)d\theta
={}&
(\theta_N-\theta_1)
\\
&+
\log\frac{\rho(\theta_N)}{\rho(\theta_1)}.
\end{aligned}
\]

The endpoint amplitude logarithm is bounded, so

\[
\boxed{
\left\langle
\sigma
+
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2
\right\rangle_{return}
=1.
}
\]

On CE this is equivalently

\[
\boxed{\langle\lambda_{eff}\rangle_{return}=1.}
\]

## 6. Two independent scalar recurrence balances

On the nondegenerate same-marker branch, a persistent finite-depth payer must satisfy simultaneously

\[
\boxed{
\left\langle\frac{U_r}{r}\right\rangle=-\frac12,
}
\]

and

\[
\boxed{
\left\langle
\sigma
+
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2
\right\rangle=1.
}
\]

Subtracting the first from the second gives the derived identity

\[
\boxed{
\left\langle
\sigma-rac{U_r}{r}
+
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2
\right\rangle
=\frac32.
}
\]

This is a genuine additional scalar constraint, although it has no sign by itself because of the parallel diffusion term.

## 7. Marker-migration firewall

M5-518 showed that a persistent material-flux lineage need not preserve one active point marker.

The active maximum/coherent representative may migrate across the material surface while the lineage survives.

Therefore if the marker used at one annular production return is not the same material point used at later returns, the amplitude endpoint telescoping in Section 5 is invalid.

One must not write

\[
\langle\lambda_{eff}\rangle=1
\]

for a sequence of different markers.

## 8. Migration branch returns to the surface-current ledger

M5-520/M5-521 give the exact material-surface flux-density continuity law

\[
D_B f+(1-\sigma_n)f
=
-\operatorname{div}_\Sigma J_\Sigma,
\]

with

\[
J_\Sigma=(\nabla\times W)\times n.
\]

Hence migration of a fixed amount of active flux across a fixed material-label distance requires a fixed surface-current action.

M5-522 then thickens that action into a three-dimensional palinstrophy spacetime charge.

Thus

\[
\boxed{
\text{persistent annular payer}
\Longrightarrow
\text{same-marker scalar return balances}
\lor
\text{surface-current migration/palinstrophy charge}.
}
\]

## 9. DSD audit

The radial return identity is robust because it follows from the same material trajectory geometry and only uses bounded annular endpoint radii.

The amplitude identity is conditional on a nondegenerate common marker and must remain separated from the migration branch.

This preserves the M5-518 correction.

## 10. Next target

On CE-H the same-marker branch is especially narrow:

\[
\tau=0,
\qquad
\mathcal D_\xi=0,
\qquad
\Sigma\xi=\sigma\xi,
\]

plus the two scalar return constraints above.

The remaining sign-indefinite term is the **parallel diffusion** \(\Delta\rho/\rho\).

A natural next audit is whether that term can sustain the required mean value without producing a magnitude-gradient/surface-migration charge already counted in M5-588/M5-522.

Status: **FINITE-DEPTH RECURRENCE NOW SUPPLIES AN EXACT RADIAL COBoundary AND, WHEN A COMMON ACTIVE MARKER SURVIVES, AN EXACT AMPLITUDE COBoundary. FAILURE OF THE LATTER IS NOT FREE: IT IS THE PREVIOUSLY AUDITED SURFACE-CURRENT MIGRATION BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**