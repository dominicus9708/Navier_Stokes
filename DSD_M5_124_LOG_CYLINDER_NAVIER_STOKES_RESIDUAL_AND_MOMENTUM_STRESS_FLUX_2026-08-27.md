# DSD M5-124 — Log-Cylinder Navier–Stokes Residual and Momentum-Stress Flux

Date: 2026-08-27

Status: **EXACT LOG-CYLINDER FORM OF THE CANONICAL-TAIL NAVIER--STOKES RESIDUAL / RESIDUAL SPLIT INTO LOG-DERIVATIVE, SPHERICAL-REDISTRIBUTION, AND SCALE-INVARIANT MOMENTUM-FLUX CHANNELS / INVARIANT MEAN NET MOMENTUM DEFECT VANISHES, SO THE POSITIVE CUBIC ANOMALY CANNOT BE IDENTIFIED WITH A NONZERO MEAN POINT-FORCE CHARGE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Let a canonical tail be written as

\[
\boxed{
T(Y)=r^{-1}\Phi(\rho,\theta),
\qquad
r=|Y|,
\quad
\rho=\log r,
\quad
\theta=Y/r.
}
\]

Choose the canonical/local pressure associated to the tail quadratic field, modulo the usual additive gauge, in the critical form

\[
\boxed{
P_T(Y)=r^{-2}\Psi(\rho,\theta).
}
\]

The additive pressure gauge does not affect any spherical momentum flux because

\[
\int_{S^2}\theta d\theta=0.
\]

Define the unprojected stationary residual

\[
\boxed{
F_T
:=
\nu\Delta T
-(T\cdot\nabla)T
-\nabla P_T.
}
\]

This is equivalent to the projected residual after the pressure is chosen consistently.

---

## 2. Differential operators in log-cylinder variables

For any Cartesian-component scalar of the form

\[
f=r^\alpha\psi(\rho,\theta),
\]

one has

\[
\Delta f
=r^{\alpha-2}
\left[
\partial_\rho^2
+(2\alpha+1)\partial_\rho
+\alpha(\alpha+1)
+\Delta_{S^2}
\right]\psi.
\]

For `alpha=-1`,

\[
\boxed{
\Delta T
=r^{-3}
(\Phi_{\rho\rho}-\Phi_\rho+\Delta_{S^2}\Phi).
}
\]

The full velocity gradient is

\[
\boxed{
\partial_jT_i
=r^{-2}\mathcal G_{ij}(\Phi),
}
\]

with

\[
\boxed{
\mathcal G_{ij}(\Phi)
:=
\theta_j(\partial_\rho\Phi_i-\Phi_i)
+(\nabla_{S^2})_j\Phi_i.
}
\]

The pressure gradient is

\[
\boxed{
\nabla P_T
=r^{-3}
\left[
\theta(\Psi_\rho-2\Psi)
+\nabla_{S^2}\Psi
\right].
}
\]

---

## 3. Convective term

Decompose

\[
\Phi=\Phi_r\theta+\Phi_\tau,
\qquad
\Phi_\tau\cdot\theta=0.
\]

Since the spherical gradient is tangential,

\[
\boxed{
(T\cdot\nabla)T
=r^{-3}
\left[
\Phi_r(\Phi_\rho-\Phi)
+(\Phi_\tau\cdot\nabla_{S^2})\Phi
\right].
}
\]

This formula uses Cartesian components for `Phi`; the spherical derivative therefore already contains the change of the geometric basis.

---

## 4. Exact log-cylinder residual

Combining the previous identities gives

\[
\boxed{
F_T(Y)
=r^{-3}\mathfrak F(\rho,\theta),
}
\]

where

\[
\boxed{
\begin{aligned}
\mathfrak F
={}&
\nu(\Phi_{\rho\rho}-\Phi_\rho+\Delta_{S^2}\Phi)\\
&-
\Phi_r(\Phi_\rho-\Phi)
-(\Phi_\tau\cdot\nabla_{S^2})\Phi\\
&-
\theta(\Psi_\rho-2\Psi)
-\nabla_{S^2}\Psi.
\end{aligned}
}
\]

Thus the `r^-3` scaling of the canonical-tail residual is exact, not merely schematic.

---

## 5. Pressure equation on the cylinder

For an incompressible velocity field,

\[
-\Delta P_T
=\partial_iT_j\,\partial_jT_i.
\]

Using the scaled gradient tensor `G`,

\[
\partial_iT_j\partial_jT_i
=r^{-4}\operatorname{tr}(\mathcal G^2).
\]

For `P_T=r^-2 Psi`, the scalar Laplacian formula gives

\[
\Delta P_T
=r^{-4}
(\Psi_{\rho\rho}-3\Psi_\rho+2\Psi+\Delta_{S^2}\Psi).
\]

Therefore

\[
\boxed{
-(\partial_\rho^2-3\partial_\rho+2+\Delta_{S^2})\Psi
=\operatorname{tr}(\mathcal G(\Phi)^2).
}
\]

This is the exact pressure-Poisson constraint on the log cylinder.

---

## 6. Momentum stress tensor

Define the stationary Navier--Stokes stress

\[
\boxed{
\mathbb S_T
:=
\nu(\nabla T+\nabla T^T)
-T\otimes T
-P_TI.
}
\]

Incompressibility gives

\[
\boxed{
\nabla\cdot\mathbb S_T=F_T.
}
\]

Since every term has degree `r^-2`, write

\[
\boxed{
\mathbb S_T(Y)
=r^{-2}\mathfrak S(\rho,\theta)
}
\]

with

\[
\boxed{
\mathfrak S
=
\nu(\mathcal G+\mathcal G^T)
-\Phi\otimes\Phi
-\Psi I.
}
\]

---

## 7. Scale-invariant momentum flux

Define the momentum flux across one sphere by

\[
\boxed{
\mathfrak M(\rho)
:=
\int_{S^2}
\mathfrak S(\rho,\theta)\theta\,d\theta.
}
\]

This is exactly the physical stress flux through the sphere `|Y|=e^rho`:

\[
\mathfrak M(\rho)
=
\int_{|Y|=e^\rho}
\mathbb S_Tn\,dS.
\]

Apply the divergence theorem to a logarithmic annulus `rho_1<log|Y|<rho_2`:

\[
\mathfrak M(\rho_2)-\mathfrak M(\rho_1)
=
\int_{\rho_1}^{\rho_2}
\int_{S^2}\mathfrak F(\rho,\theta)d\theta d\rho.
\]

Hence distributionally, and classically where smooth,

\[
\boxed{
\mathfrak M'(\rho)
=
\int_{S^2}\mathfrak F(\rho,\theta)d\theta.
}
\]

This is the exact log-radius momentum-defect ledger.

---

## 8. DSD channel split of the residual

The local formula and the stress ledger separate three structural channels.

### Log derivative

Terms containing `partial_rho` change the shell state along the genealogy axis and may contribute to bounded log-radius coboundaries.

### Spherical redistribution

Tangential derivatives and pressure gradients can redistribute momentum around one sphere without creating a net vector momentum defect after spherical integration.

### Net momentum defect

The only net vector defect across a log interval is

\[
\boxed{
\Delta\mathfrak M
=\int\int\mathfrak F.
}
\]

This is the candidate point-force/momentum-flux channel.

---

## 9. Invariant-factor mean of the net force channel

The canonical tail factor is translation invariant under the pushed invariant measure `nu`.

The stress-flux observable `mathfrak M` is bounded/integrable on the compact tail class under the established shell derivative and pressure bounds.

Therefore its translation derivative has zero invariant mean:

\[
\boxed{
\int_{\mathcal T}
\mathcal L_D\mathfrak M(T)d\nu(T)
=0.
}
\]

Equivalently,

\[
\boxed{
\left\langle
\int_{S^2}\mathfrak Fd\theta
\right\rangle_\nu
=0.
}
\]

Thus the positive scalar cubic anomaly

\[
\mathscr R_3
=\int\mathfrak c d\nu>0
\]

cannot be identified with a nonzero **mean vector point-force charge**.

A Landau-type net-force intuition, even when relevant to individual homogeneous snapshots, does not represent the invariant scalar anomaly by itself.

---

## 10. Countermodel audit

The M5-123 rotational family has

\[
\Phi=A(\rho)(a\times\theta).
\]

Its cubic density can have arbitrary positive recurrent mean while the spherical momentum-defect channel may have zero mean.

This explicitly demonstrates why the scalar anomaly and vector stress flux are different typed channels.

They must not be merged in static aggregation.

---

## 11. What this removes

The following shortcut is RED:

\[
\boxed{
\mathscr R_3>0
\Longrightarrow
\text{nonzero mean momentum point force at the singular center}.
}
\]

The log-cylinder stress ledger does not support that implication.

Any useful momentum-flux obstruction must therefore concern:

- fluctuations/cycles of `mathfrak M`, not its invariant mean;
- a scalar stress functional rather than net vector force;
- or coupling of `mathfrak F` to the strong-critical quotient/core.

---

## 12. New frontier

The next NSE-specific target is the quotient coupling.

The canonical tail residual `F_T` is exactly the exterior forcing appearing in the finite-energy quotient equation.  Since its net momentum mean vanishes, the question becomes:

\[
\boxed{
\text{Can a compact recurrent }Q\in L^2\cap L^3
\text{ absorb the nontrivial zero-mean log-cylinder residual }\mathfrak F
\text{ while the tail carries }\mathscr R_3>0?
}
\]

A viable next calculation is to pair the quotient equation with the tail residual/stress in a scale-critical duality, rather than with ordinary `L2` energy, whose subcritical recurrence shortcut was already closed in M5-117.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
