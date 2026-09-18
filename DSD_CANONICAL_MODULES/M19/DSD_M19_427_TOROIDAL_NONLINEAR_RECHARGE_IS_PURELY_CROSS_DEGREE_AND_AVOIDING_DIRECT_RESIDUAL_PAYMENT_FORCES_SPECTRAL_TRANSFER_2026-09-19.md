# M19-427 — Toroidal nonlinear recharge is purely cross-degree and avoiding direct residual payment forces quantitative spectral transfer

Date: 2026-09-19  
Canonical ID: **M19-427**  
Status: **TOROIDAL CROSS-DEGREE TRANSFER IDENTITY / SAME-DEGREE QUADRATIC RECHARGE CANCELS EXACTLY / A FIXED HIGHER-TOROIDAL MODE EITHER PAYS DIRECT SAME-DEGREE FIRST-RESIDUAL CORRELATION OR REQUIRES A QUANTITATIVE TOROIDAL NONLINEAR SOURCE GENERATED ONLY BY DIFFERENT SPHERICAL DEGREES / COMPACT SMOOTHNESS REDUCES THE COMPENSATING INTERACTION TO A FINITE LOW-DEGREE FAMILY / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Toroidal Hodge expansion

On the radial-free toroidal sector write

\[
A
=
\omega\times\nabla_{S^2}\psi,
\]

with spherical-harmonic decomposition

\[
\boxed{
\psi
=
\sum_{l\ge1}\psi_l,
\qquad
-\Delta_{S^2}\psi_l
=
\lambda_l\psi_l,
\qquad
\lambda_l=l(l+1).
}
\]

The surface vorticity is

\[
\boxed{
\zeta
=
-\Delta_{S^2}\psi
=
\sum_{l\ge1}\lambda_l\psi_l.
}
\]

## 2. Exact toroidal nonlinear source

For a tangential divergence-free surface flow, the toroidal projection of the convective acceleration is determined by the surface-vorticity transport

\[
J(\psi,\zeta),
\]

where \(J\) is the spherical Poisson bracket.

Expand:

\[
J(\psi,\zeta)
=
\sum_{l,k}
\lambda_kJ(\psi_l,\psi_k).
\]

The diagonal terms vanish:

\[
J(\psi_l,\psi_l)=0.
\]

Pair the ordered terms \((l,k)\) and \((k,l)\). Since

\[
J(\psi_k,\psi_l)
=
-J(\psi_l,\psi_k),
\]

we obtain the exact cross-degree identity

\[
\boxed{
J(\psi,\zeta)
=
\sum_{l<k}
(\lambda_k-\lambda_l)
J(\psi_l,\psi_k).
}
\]

Therefore

\[
\boxed{
\text{toroidal quadratic recharge is generated only by interactions between distinct spherical degrees.}
}
\]

No same-degree self-interaction can replenish a toroidal mode.

## 3. Degree-l projected first-residual equation

Let

\[
A_l
=
\omega\times\nabla_S\psi_l.
\]

Project the first terminal residual onto the toroidal degree-l sector:

\[
\boxed{
C_{tor,l}
=
L_lA_l
+
N_l,
}
\]

where

\[
\boxed{
L_l
:=
-\partial_q^2
+
\partial_q
+
\lambda_l
}
\]

is the coercive linear operator from M19-426, and \(N_l\) is the degree-l toroidal projection of the quadratic nonlinear source.

Pressure contributes no toroidal component.

By Section 2,

\[
\boxed{
N_l
\text{ is formed entirely from cross-degree interactions.}
}
\]

## 4. Invariant linear coercive energy

Define

\[
\boxed{
E_l
:=
\left\langle
\|\partial_qA_l\|_2^2
+
\lambda_l\|A_l\|_2^2
\right\rangle.
}
\]

Pair the residual equation with \(A_l\) and average in q.

As in M19-426,

\[
\left\langle
A_l\cdot L_lA_l
\right\rangle
=
E_l.
\]

Hence

\[
\boxed{
\left\langle
A_l\cdot C_{tor,l}
\right\rangle
=
E_l
+
\left\langle
A_l\cdot N_l
\right\rangle.
}
\]

For every nonzero recurrent degree-l component,

\[
E_l>0.
\]

## 5. Direct residual payment or cross-degree compensation

Fix one nonzero degree-l component.

Either

\[
\boxed{
\left\langle
A_l\cdot C_{tor,l}
\right\rangle
\ge
\frac{E_l}{2},
}
\]

or else

\[
\left\langle
A_l\cdot N_l
\right\rangle
\le
-rac{E_l}{2}.
\]

Thus

\[
\boxed{
T_l
\Longrightarrow
R_l^{direct}
\lor
X_l^{cross-degree}.
}
\]

The first branch is direct same-degree terminal-residual payment.

The second requires nonlinear cross-degree recharge of fixed size.

## 6. Quantitative nonlinear-source floor on the compensation branch

Suppose

\[
\left|
\left\langle
A_l\cdot N_l
\right\rangle
\right|
\ge
\frac{E_l}{2}.
\]

Cauchy-Schwarz gives

\[
\frac{E_l}{2}
\le
\left\langle\|A_l\|_2^2\right\rangle^{1/2}
\left\langle\|N_l\|_2^2\right\rangle^{1/2}.
\]

But

\[
E_l
\ge
\lambda_l
\left\langle\|A_l\|_2^2\right\rangle.
\]

Therefore

\[
\boxed{
\left\langle
\|N_l\|_2^2
\right\rangle
\ge
\frac{\lambda_l}{4}
E_l.
}
\]

For \(l\ge2\),

\[
\lambda_l\ge6,
\]

so the cross-degree source carries a fixed quantitative floor relative to the selected toroidal-mode energy.

## 7. A selected higher-toroidal event contains a finite active degree

M19-421 supplies a syndetic fixed-window lower bound on

\[
A_{tor,\ge2}.
\]

The compact smooth terminal hull has uniform angular Sobolev bounds of arbitrarily fixed finite order.

Therefore its spherical-harmonic tail is uniformly small at sufficiently high l.

Choose \(L<\infty\) such that, uniformly on the finite detector family,

\[
\sum_{l>L}
\|A_l\|_2^2
\le
\frac14
\eta_T^2.
\]

If a selected event satisfies

\[
\|A_{tor,\ge2}\|_2
\ge
\eta_T,
\]

then

\[
\sum_{l=2}^{L}
\|A_l\|_2^2
\ge
\frac34\eta_T^2.
\]

Hence at least one fixed degree

\[
l_*
\in
\{2,\ldots,L\}
\]

carries a definite lower bound on a nonempty open subset.

After finite selection and minimality, one such degree can be chosen as a syndetic recurrent witness on every minimal-hull orbit.

Thus the T>=2 branch may be reduced to one finite selected \(l_*\).

## 8. Cross-degree compensation requires another active angular degree

On the \(X_{l_*}^{cross-degree}\) branch,

\[
N_{l_*}
\neq0.
\]

But Section 2 shows

\[
N_{l_*}
\]

is built solely from terms

\[
(\lambda_k-\lambda_j)
J(\psi_j,\psi_k),
\qquad
j\neq k.
\]

Therefore at least two distinct spherical degrees must be active.

In particular, a state supported only in the selected degree \(l_*\) cannot enter the compensation branch.

It must pay direct residual.

## 9. Finite low-degree reduction of the compensating partner

The same compact smoothness that controls the high-l tail of \(A\) controls the high-l contribution to the bilinear Jacobian in the fixed normalized windows.

Since the compensation branch has the fixed source floor

\[
\left\langle
\|N_{l_*}\|_2^2
\right\rangle
\ge
\frac{\lambda_{l_*}}4E_{l_*},
\]

the entire source cannot be carried by arbitrarily high angular degrees of vanishing norm.

After increasing \(L\) if necessary, a fixed positive fraction of the cross-degree source must come from a finite family

\[
j,k\le L',
\qquad
j\neq k.
\]

Thus the spectral compensation is not an uncontrolled ultraviolet escape on the compact hard hull.

It can be reduced to a finite low-degree interaction family.

## 10. Structural interpretation

The higher-toroidal branch therefore has only two mechanisms:

### Direct terminal-jet payment

\[
\boxed{
R_l^{direct}:
\left\langle
A_l\cdot C_{tor,l}
\right\rangle
\ge
E_l/2.
}
\]

This is an ordinary residual-correlation channel and remains critical under M19-414.

### Spectral-transfer payment

\[
\boxed{
X_l^{cross-degree}:
\text{a fixed nonlinear Jacobian interaction between distinct spherical degrees replenishes the selected mode.}
}
\]

This is a genuinely formed angular energy-transfer mechanism.

It is not another arbitrary unsigned derivative payer.

## 11. What is not yet proved

A finite collection of angular modes can exchange energy recurrently without contradiction.

The cross-degree Jacobian is antisymmetric at the level of total two-dimensional enstrophy/energy transfer, so a one-way cascade sign cannot be assumed.

Therefore

\[
\boxed{
X_l^{cross-degree}
\not\Rightarrow
\text{monotone spectral cascade}.
}
\]

A closure requires one more property:

- a signed mode-order drift;
- finite-dimensional cycle exclusion;
- coupling to radial/poloidal/pressure sectors;
- or an exact resonance incompatibility.

## 12. Updated frontier

The formerly broad

\[
T_{\ge2}^{syndetic}
\]

branch is now refined to

\[
\boxed{
R_{tor}^{direct,critical}
\lor
X_{tor}^{cross-degree,finite}.
}
\]

Together with M19-425, the current hard residual frontier is

\[
\boxed{
R3^{critical}
\lor
R_{tor}^{direct,critical}
\lor
S_{rr}^{critical}
\lor
P_{tan}^{critical}
\lor
\mathcal B_{res}^{finite-depth}
\lor
X_{tor}^{cross-degree,finite}.
}
\]

All branches except the last are already known critical/transport-compatible currencies.

Therefore the genuinely new unresolved structure is now the finite-dimensional cross-degree toroidal transfer graph.

The next calculation should derive its exact antisymmetry/conservation law and determine whether recurrent compensation cycles are free or must couple to a non-toroidal mode.

\[
\boxed{\text{M19-427 COMPLETE; HIGHER-TOROIDAL SURVIVAL WITHOUT DIRECT RESIDUAL PAYMENT REQUIRES QUANTITATIVE FINITE CROSS-DEGREE SPECTRAL TRANSFER.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
