# DSD M19-160 — The compact-core compensation operator splits into local strain and gradient-vorticity Biot-Savart parts, but incompressibility does not force a one-channel rank bound

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / EXACT COMPENSATION DECOMPOSITION + RANK-SHORTCUT NO-GO / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-159 showed that one extra nonsymmetry `mu=1` kernel direction forces one additional generalized compensation eigenchannel above the enhanced threshold

\[
\Lambda_1
=
\frac14+\nu\lambda_{P,1}.
\]

A tempting route is to argue that incompressibility makes the compact-core compensation effectively rank one after the exact symmetry channel is removed.

The present module computes the compensation operator exactly enough to test that idea.

The simple rank-one shortcut fails.

## 2. Linearized similarity-vorticity equation

The similarity vorticity of the background satisfies

\[
\partial_s\Omega
+
\Omega
+
\frac12(y\cdot\nabla)\Omega
+
(U\cdot\nabla)\Omega
-
(\Omega\cdot\nabla)U
=
\nu\Delta\Omega.
\]

For a linearized velocity perturbation `W` with

\[
\eta=\nabla\times W,
\qquad
\nabla\cdot W=0,
\]

the exact linearized vorticity equation is

\[
\boxed{
\begin{aligned}
\partial_s\eta
={}&
\nu\Delta\eta
-
\eta
-
\frac12(y\cdot\nabla)\eta
-
(U\cdot\nabla)\eta\\
&+
(\eta\cdot\nabla)U
+
(\Omega\cdot\nabla)W
-
(W\cdot\nabla)\Omega.
\end{aligned}
}
\]

The divergence-free transport term contributes no `L2` energy.

## 3. Exact compensation form

Taking the `L2` pairing with `eta` gives

\[
\frac12\frac d{ds}\|\eta\|_2^2
+
\nu\|\nabla\eta\|_2^2
+
\frac14\|\eta\|_2^2
=
\mathcal C_U[W],
\]

where

\[
\boxed{
\begin{aligned}
\mathcal C_U[W]
={}&
\int_{\mathbb R^3}
\eta\cdot(\eta\cdot\nabla)U\,dy\\
&+
\int_{\mathbb R^3}
\eta\cdot(\Omega\cdot\nabla)W\,dy\\
&-
\int_{\mathbb R^3}
\eta\cdot(W\cdot\nabla)\Omega\,dy.
\end{aligned}
}
\]

Because `eta_i eta_j` is symmetric, the first term sees only the strain

\[
S_U
:=
\frac12(\nabla U+\nabla U^T).
\]

Hence

\[
\boxed{
\mathcal C_U[W]
=
\underbrace{\int\eta\cdot S_U\eta}_{\mathcal C_{strain}}
+
\underbrace{\mathcal C_{grad\Omega}[W]}_{\text{nonlocal vorticity-gradient part}}.
}
\]

## 4. Constant-vorticity cancellation in the nonlocal part

M19-091 sharpened one of the two nonlocal terms:

\[
\int
\eta\cdot(\Omega\cdot\nabla)W
=
-
\frac12
\int
(\partial_k\Omega_j)
(W\times\partial_jW)_k.
\]

Thus a spatially constant background vorticity does not contribute to this term.

The third term already contains `grad Omega` explicitly:

\[
-
\int
\eta_iW_j\partial_j\Omega_i.
\]

Therefore

\[
\boxed{
\mathcal C_{grad\Omega}
\text{ depends on }\nabla\Omega,
\text{ not on a constant part of }\Omega.
}
\]

After writing `W=BS eta` through the Biot--Savart operator, this is a compact/nonlocal quadratic form on the retained compact core.

## 5. Operator decomposition

Schematically, on vorticity variables,

\[
\boxed{
K_{comp}(s)
=
M_{S_U(s)}
+
K_{\nabla\Omega(s)},
}
\]

where

- `M_{S_U}` is the local multiplication/stretching form projected to divergence-free vorticity perturbations;
- `K_{grad Omega}` contains Biot--Savart and first derivatives of the background vorticity.

On the finite hard fiber, both become finite Hermitian matrices after period averaging.

## 6. Why trace-free strain does not imply one positive channel

Incompressibility gives

\[
\operatorname{tr}S_U(y)=0
\]

pointwise.

But this does **not** imply that the compression/stretching operator restricted to a global finite-dimensional perturbation space has only one positive eigenvalue.

At a fixed point, a trace-free symmetric `3x3` matrix may already have two positive eigenvalues and one negative eigenvalue.

More importantly, global perturbations may localize in different spatial regions.

For example, suppose two disjoint compact regions `K_1,K_2` contain positive stretching directions `e_1(y),e_2(y)`. Choose divergence-free vorticity packets `eta_1,eta_2` essentially supported in the two regions and aligned with those local directions.

Then approximately

\[
\int\eta_1\cdot S_U\eta_1>0,
\qquad
\int\eta_2\cdot S_U\eta_2>0,
\]

while

\[
\langle\eta_1,\eta_2\rangle\approx0.
\]

Thus two independent positive restricted strain channels are compatible with

\[
\operatorname{tr}S_U=0.
\]

Consequently

\[
\boxed{
\operatorname{tr}S_U=0
\not\Rightarrow
\operatorname{rank}_+(K_{comp})\le1.
}
\]

## 7. The nonlocal term also has no automatic rank-one structure

`K_{grad Omega}` is compact on the hard fiber, but compactness controls eigenvalue accumulation, not finite-rank multiplicity.

A compact Hermitian operator may possess arbitrarily many nonzero positive eigenvalues.

Therefore

\[
\boxed{
\text{compact nonlocal coupling}
\not\Rightarrow
\text{one-channel compensation}.
}
\]

The finite-dimensionality obtained earlier is essential, but it is not itself a rank bound.

## 8. Consequence for the M19-159 target

M19-159 reduced nonsymmetry kernel exclusion to

\[
\kappa_{d_0+1}<\Lambda_1.
\]

The present module shows that this inequality cannot be proved merely from

\[
\operatorname{tr}S_U=0
\]

or from compactness of the nonlocal term.

A stronger statement is needed, for example:

1. a quantitative orientation theorem tying all high-compensation hard modes to the exact symmetry block;
2. a Schatten/trace bound too small to support `d_0+1` channels above `Lambda_1`;
3. a signed index theorem for the period-averaged compact-core operator;
4. a geometric alignment restriction on recurrent Type-I vorticity/strain that is stronger than incompressibility alone.

## 9. Useful norm bounds retained

The decomposition does retain the prior estimates

\[
|\mathcal C_{strain}|
\lesssim
\|S_U\|_3\,\|\eta\|_3^2,
\]

and, after the M19-091 cancellation,

\[
|\mathcal C_{grad\Omega}|
\lesssim
\|\nabla\Omega\|_3
\times
\text{Biot--Savart/Sobolev norms of }\eta.
\]

These can bound the operator norm or Schatten norms of the restricted compensation matrix, but current corridor estimates do not yet put those bounds below the M19-159 multiplicity threshold.

## 10. Audit verdict

### Proved

1. The compensation operator splits exactly into local strain stretching plus a nonlocal part controlled by `grad Omega` through Biot--Savart.
2. Constant background vorticity does not drive the nonlocal commutator term.
3. Pointwise trace-free strain does not imply a rank-one positive restricted operator.
4. Compactness of the nonlocal term does not imply a finite positive-rank bound small enough for kernel rigidity.

### Therefore

\[
\boxed{
\text{the one-channel rank shortcut is closed.}
}
\]

The kernel theorem remains a genuine compact-core spectral ordering problem.

## 11. Next target

M19-161 should replace the failed rank shortcut by a **Schatten/eigenvalue-count estimate**.

The natural target is an inequality of the form

\[
N_+(\Lambda_1)
:=
\#\{j:\kappa_j\ge\Lambda_1\}
\le
\frac{\|K_{comp}^+\|_{HS}^2}{\Lambda_1^2}
\]

and then derive the sharpest available bound on the Hilbert--Schmidt or positive-trace norm from the compact-core fields `S_U` and `grad Omega`.

If that upper bound is strictly below `d_0+1`, nonsymmetry kernel rigidity follows.
