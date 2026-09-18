# M19-428 — Cross-degree toroidal transfer is internally conservative and cannot remove the total toroidal residual payment

Date: 2026-09-19  
Canonical ID: **M19-428**  
Status: **AUTHORITATIVE CORRECTION TO THE M19-427 PROOF-TREE INTERPRETATION / CROSS-DEGREE TOROIDAL TRANSFER CAN REDISTRIBUTE MODAL RESIDUAL WORK BUT ITS TOTAL KINETIC-ENERGY WORK VANISHES EXACTLY / EVERY NONZERO RADIAL-FREE TOROIDAL RECURRENT TRACE HAS POSITIVE TOTAL A·C EQUAL TO ITS FULL LOG-ANGULAR DIRICHLET ENERGY / A GENERAL HIGHER-TOROIDAL HARD STATE THEREFORE ROUTES TO EITHER RADIAL/BRC ACTIVITY OR POSITIVE RESIDUAL SLOPE / CROSS-DEGREE TRANSFER IS NOT AN INDEPENDENT ROOT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope correction to M19-427

M19-427 correctly proves that a selected degree-l toroidal mode can receive nonlinear toroidal work only through interactions with distinct spherical degrees.

That modal statement remains valid.

However treating the resulting cross-degree transfer as a new independent proof-tree root is too broad.

At the level of the **total radial-free toroidal field**, the nonlinear work cancels exactly.

The cross-degree channel can redistribute payment between angular degrees, but it cannot remove the total terminal residual correlation.

## 2. General radial-free toroidal field

Let

\[
\boxed{
A
=
\omega\times\nabla_{S^2}\psi
}
\]

with arbitrary smooth bounded recurrent \(q\)-dependence and arbitrary mixture of spherical degrees.

Then

\[
A_r=0,
\qquad
\operatorname{div}_{S^2}A=0.
\]

The physical critical field is

\[
v=r^{-1}A.
\]

The first terminal residual is

\[
C
=
-\Delta v
+
(v\cdot\nabla)v
+
\nabla p
\]

in normalized degree-minus-three form.

## 3. Nonlinear kinetic-energy work vanishes exactly

Because \(A_r=0\),

\[
(v\cdot\nabla)v
=
r^{-3}(A\cdot\nabla_{S^2})A.
\]

At each fixed q,

\[
\begin{aligned}
\int_{S^2}
A\cdot(A\cdot\nabla_S)A,d\omega
&=
\int_{S^2}
A\cdot\nabla_S
\left(
\frac12|A|^2
\right)d\omega
\\
&=
-
\frac12
\int_{S^2}
|A|^2
\operatorname{div}_{S^2}A,d\omega
\\
&=0.
\end{aligned}
\]

Thus

\[
\boxed{
\int A\cdot N_{tor},d\omega=0
}
\]

for the full toroidal nonlinear term.

This cancellation includes all cross-degree interactions.

## 4. Pressure work vanishes on a toroidal sphere

The pressure contribution is a surface gradient in its tangential part.

Since

\[
\operatorname{div}_{S^2}A=0,
\]

we have

\[
\boxed{
\int_{S^2}
A\cdot\nabla_{S^2}P,d\omega
=
0.
}
\]

The radial pressure component is orthogonal to the tangential field A.

Therefore pressure also performs no total work on the radial-free toroidal sector.

## 5. Exact total toroidal residual-correlation identity

The linear critical Laplacian is

\[
-\Delta v
=
r^{-3}
\left(
-A_{qq}
+
A_q
-
\Delta_{S^2}A
\right).
\]

Pair with A and average in q.

Translation invariance gives

\[
\left\langle
\int A\cdot A_q
\right\rangle
=0,
\]

and integration by parts gives

\[
\left\langle
\int A\cdot(-A_{qq})
\right\rangle
=
\left\langle
\|A_q\|_2^2
\right\rangle,
\]

\[
\int A\cdot(-\Delta_{S^2}A)
=
\|\nabla_{S^2}A\|_2^2.
\]

Sections 3--4 remove the nonlinear and pressure contributions.

Hence

\[
\boxed{
\left\langle
\int_{S^2}A\cdot C,d\omega
\right\rangle
=
\left\langle
\|A_q\|_2^2
+
\|\nabla_{S^2}A\|_2^2
\right\rangle.
}
\]

Therefore every nonzero radial-free toroidal recurrent leading trace satisfies

\[
\boxed{
\langle A\cdot C\rangle>0.
}
\]

This is exactly the M19-423 Hardy-excess identity with

\[
\Gamma_B=0
\]

because

\[
A_r=0.
\]

## 6. Modal cross-degree transfer sums to zero

Let

\[
A=\sum_lA_l
\]

and define the modal nonlinear work

\[
T_l
:=
\left\langle
\int A_l\cdot N_l
\right\rangle.
\]

Section 3 gives immediately

\[
\boxed{
\sum_lT_l=0.
}
\]

At the surface-vorticity level,

\[
\zeta
=
-\Delta_S\psi,
\]

and the nonlinear source is

\[
J(\psi,\zeta).
\]

The same Jacobian antisymmetry gives

\[
\boxed{
\int_{S^2}
\zeta J(\psi,\zeta)d\omega
=0.
}
\]

Therefore the modal transfers also obey the enstrophy-weighted conservation law

\[
\boxed{
\sum_l
\lambda_lT_l
=
0
}
\]

under the corresponding streamfunction/velocity normalization.

Thus cross-degree transfer is conservative in the two standard quadratic surface invariants.

It is redistribution, not net recharge.

## 7. Two-degree consequence

If only two distinct toroidal spherical degrees are active in the velocity-energy transfer, say l and k, then

\[
T_l+T_k=0,
\]

and

\[
\lambda_lT_l+\lambda_kT_k=0.
\]

Since

\[
\lambda_l\neq\lambda_k,
\]

we obtain

\[
\boxed{
T_l=T_k=0.
}
\]

Thus nontrivial modal energy redistribution among already occupied toroidal modes requires at least three distinct degrees.

A two-degree field may generate new harmonic content in its residual, but it cannot use nonlinear transfer to cancel the positive linear energy work on both occupied degrees.

## 8. Reinterpretation of M19-427

M19-427's degree-wise fork

\[
R_l^{direct}
\lor
X_l^{cross-degree}
\]

remains a correct **modal accounting identity**.

But after summing over all toroidal degrees,

\[
\boxed{
\sum_l
\langle A_l\cdot C_l\rangle
=
\sum_lE_l
>0
}
\]

for every nonzero radial-free toroidal recurrent state.

Hence

\[
\boxed{
X_{tor}^{cross-degree}
}
\]

cannot be promoted to an independent global survivor.

It only determines which toroidal degrees carry the unavoidable total residual work.

## 9. General higher-toroidal hard state: radial activity or residual slope

Return to the M19-421 higher-toroidal branch on a compact minimal hard component.

Syndetic fixed-window T>=2 activity gives a positive invariant mean floor

\[
\boxed{
\tau_T
:=
\left\langle
\|A_{tor,\ge2}\|_2^2
\right\rangle
>0.
}
\]

Because toroidal degrees l>=2 have

\[
\lambda_l\ge6,
\]

the full Hardy excess satisfies

\[
\boxed{
\mathcal H_A
\ge
6\tau_T.
}
\]

M19-423 gives

\[
\mathcal H_A
=
\langle\Gamma_B\rangle
+
\langle A\cdot C\rangle.
\]

The Bernoulli covariance obeys

\[
|\Gamma_B|
\le
\|B-\bar B\|_2
\|A_r\|_2.
\]

Compactness supplies

\[
\left\langle
\|B-\bar B\|_2^2
\right\rangle^{1/2}
\le
M_B<\infty.
\]

Therefore

\[
\boxed{
|\langle\Gamma_B\rangle|
\le
M_B
\left\langle
\|A_r\|_2^2
\right\rangle^{1/2}.
}
\]

## 10. Quantitative collapse of the T>=2 branch

If

\[
\left\langle
\|A_r\|_2^2
\right\rangle^{1/2}
\ge
\frac{3\tau_T}{M_B},
\]

then the state carries a fixed recurrent radial-amplitude floor and routes to the BRC/RP analysis of M19-422--425.

If instead

\[
\left\langle
\|A_r\|_2^2
\right\rangle^{1/2}
<
\frac{3\tau_T}{M_B},
\]

then

\[
|\langle\Gamma_B\rangle|
<
3\tau_T.
\]

Since

\[
\mathcal H_A\ge6\tau_T,
\]

M19-423 yields

\[
\boxed{
\left\langle
\int A\cdot C
\right\rangle
>
3\tau_T
>0.
}
\]

Thus

\[
\boxed{
T_{\ge2}^{syndetic}
\Longrightarrow
BRC
\lor
\mathcal B_{res}^{positive}.
}
\]

The second branch is exactly the M19-269 residual-slope finite-depth transport branch.

## 11. Corrected current frontier

The higher-toroidal leading channel is therefore not an independent root.

Combining M19-422--425 and M19-428:

\[
\boxed{
T_{\ge2}
\to
BRC
\lor
\mathcal B_{res}.
}
\]

And

\[
BRC
\to
S_{rr}^{critical}
\lor
P_{tan}^{critical}
\lor
\mathcal B_{res}.
\]

Hence the M19-421 three-way leading-structure fork collapses to

\[
\boxed{
R3^{critical}
\lor
S_{rr}^{critical}
\lor
P_{tan}^{critical}
\lor
\mathcal B_{res}^{finite-depth}.
}
\]

The cross-degree toroidal transfer graph is retained as useful internal spectral bookkeeping, but not as a new terminal survivor.

## 12. Strategic consequence

The recent spectral/Hodge calculations have now exhausted both leading-geometry escape directions:

- radial/poloidal structure returns to critical strain, pressure, or residual slope;
- higher toroidal structure returns to radial structure or residual slope;
- pure l=1 self-closure was already removed by M19-419.

Thus further progress should return to the **first-residual structure itself**, especially the mandatory syndetic angular residual of M19-418 and its R3/mean-free higher-mode content.

The next high-value calculation is no longer another leading-A decomposition.

It is to test whether the mandatory angular residual

\[
C^\perp
\]

has an exact orthogonality/coercivity relation with the terminal trace A strong enough to upgrade critical residual activity into a positive A·C slope or a higher derivative channel.

\[
\boxed{\text{M19-428 COMPLETE; CROSS-DEGREE TOROIDAL TRANSFER IS CONSERVATIVE REDISTRIBUTION, AND THE HIGHER-TOROIDAL ROOT COLLAPSES BACK TO RADIAL OR RESIDUAL-SLOPE STRUCTURE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
