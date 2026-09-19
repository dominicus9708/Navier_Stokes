# M20-002 — Genuine terminal direction motion splits into Eulerian transport, transverse strain-eigenframe rotation, or viscous projective diffusion

Date: 2026-09-19  
Canonical ID: **M20-002**  
Status: **PROJECTIVE VORTICITY PDE DECOMPOSITION / THE ROBUST HIGH-VORTICITY DIRECTION BRANCH FROM M20-001 IS INSERTED INTO THE EXACT VORTICITY-DIRECTION EQUATION / WEDGE-DEPTH DIRECTION CHANGE IS NOT AUTOMATICALLY MATERIAL DIRECTION TURNOVER / IT SPLITS INTO ADVECTION OF EXISTING DIRECTION TEXTURE, TRANSVERSE STRAIN-EIGENFRAME ACTION, OR VISCOUS PROJECTIVE DIFFUSION / THE STRAIN CHANNEL HAS AN EXACT EIGENVALUE-VARIANCE FORM / NO CHANNEL YET GIVES NONCRITICAL CLOSURE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M20-001

On the genuine direction branch, there exists a fixed threshold

\[
\beta_*>0
\]

such that, with

\[
E_{\beta_*}:=\{|B|\ge\beta_*\},
\]

one has

\[
\boxed{
\left\langle
1_{E_{\beta_*}}
|\partial_z\xi_B|^2
\right\rangle
\ge
\eta_{\rm dir}>0.
}
\]

Here

\[
\xi_B:=\frac{B}{|B|}
\]

is well defined and smooth on \(E_{\beta_*}\).

The purpose of this module is to identify what can produce this direction motion.

## 2. Physical vorticity-direction equation

Write in physical variables

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|.
\]

The vorticity equation is

\[
(\partial_s+u\cdot\nabla)\omega
=
\Sigma_u\omega+\Delta\omega.
\]

Project perpendicular to \(\xi\). The scalar amplitude terms disappear and one obtains the exact direction equation

\[
\boxed{
(\partial_s+u\cdot\nabla)\xi
=
P_\xi^\perp\Sigma_u\xi
+
\frac1{\rho}
P_\xi^\perp\Delta\omega.
}
\]

Pressure does not appear.

## 3. Terminal wedge normalization

At the terminal boundary,

\[
u=r^{-1}A,
\qquad
\omega=r^{-2}B,
\qquad
\Sigma_u=r^{-2}\Sigma_A.
\]

Since

\[
z=\frac{-s}{r^2},
\]

at fixed physical point \(x\),

\[
r^2\partial_s\xi
=
-\partial_z\xi.
\]

For a direction field depending on \(q=\log r\) and \(\omega\),

\[
u\cdot\nabla\xi
=
r^{-2}\mathcal T_A\xi,
\]

where

\[
\boxed{
\mathcal T_A\xi
:=
A_r\partial_q\xi
+
A_T\cdot\nabla_{S^2}\xi.
}
\]

Also

\[
\Delta(r^{-2}B)
=
r^{-4}\mathcal L_2B,
\]

with

\[
\mathcal L_2
=
(\partial_q-2)(\partial_q-1)+\Delta_{S^2}.
\]

Therefore

\[
\boxed{
-\partial_z\xi_B
+
\mathcal T_A\xi_B
=
P_{\xi_B}^\perp\Sigma_A\xi_B
+
\mathcal V_\xi,
}
\]

where

\[
\boxed{
\mathcal V_\xi
:=
\frac1{|B|}
P_{\xi_B}^\perp\mathcal L_2B.
}
\]

Equivalently,

\[
\boxed{
\partial_z\xi_B
=
\mathcal T_A\xi_B
-
P_{\xi_B}^\perp\Sigma_A\xi_B
-
\mathcal V_\xi.
}
\]

## 4. Eulerian versus material projective motion

Define the normalized material direction derivative

\[
\boxed{
\mathcal M_\xi
:=
-\partial_z\xi_B+\mathcal T_A\xi_B.
}
\]

Then

\[
\boxed{
\mathcal M_\xi
=
P_{\xi_B}^\perp\Sigma_A\xi_B+\mathcal V_\xi.
}
\]

Thus a large fixed-coordinate wedge-depth derivative

\[
\partial_z\xi_B
\]

does not automatically mean a large material rotation of vorticity.

A direction pattern may move through the observation point by advection.

This is the first M20-002 firewall:

\[
\boxed{
\text{Eulerian depth direction motion}
\not\Rightarrow
\text{material direction turnover}.
}
\]

## 5. Quantitative three-way PDE fork

On \(E_{\beta_*}\),

\[
\partial_z\xi_B
=
\mathcal T_A\xi_B
-
\mathcal S_\xi
-
\mathcal V_\xi,
\]

where

\[
\boxed{
\mathcal S_\xi
:=
P_{\xi_B}^\perp\Sigma_A\xi_B.
}
\]

By

\[
|x+y+z|^2
\le
3(|x|^2+|y|^2+|z|^2),
\]

the direction floor implies

\[
\begin{aligned}
&\left\langle
1_{E_{\beta_*}}|\mathcal T_A\xi_B|^2
\right\rangle
+
\left\langle
1_{E_{\beta_*}}|\mathcal S_\xi|^2
\right\rangle
\\
&\qquad+
\left\langle
1_{E_{\beta_*}}|\mathcal V_\xi|^2
\right\rangle
\ge
\frac{\eta_{\rm dir}}3.
\end{aligned}
\]

Hence at least one of

\[
\boxed{
T_{\rm dir}:
\left\langle
1_{E_{\beta_*}}|\mathcal T_A\xi_B|^2
\right\rangle
\ge
\frac{\eta_{\rm dir}}9,
}
\]

\[
\boxed{
S_{\rm dir}:
\left\langle
1_{E_{\beta_*}}|\mathcal S_\xi|^2
\right\rangle
\ge
\frac{\eta_{\rm dir}}9,
}
\]

or

\[
\boxed{
V_{\rm dir}:
\left\langle
1_{E_{\beta_*}}|\mathcal V_\xi|^2
\right\rangle
\ge
\frac{\eta_{\rm dir}}9
}
\]

holds.

## 6. Transport branch forces spatial direction texture

Because

\[
\mathcal T_A\xi_B
=
A_r\partial_q\xi_B
+
A_T\cdot\nabla_S\xi_B,
\]

we have

\[
|\mathcal T_A\xi_B|^2
\le
|A|^2
\left(
|\partial_q\xi_B|^2
+
|\nabla_S\xi_B|^2
\right).
\]

Compact terminal regularity gives

\[
|A|\le M_A.
\]

Therefore \(T_{\rm dir}\) implies

\[
\boxed{
\left\langle
1_{E_{\beta_*}}
\left(
|\partial_q\xi_B|^2
+
|\nabla_S\xi_B|^2
\right)
\right\rangle
\ge
\frac{\eta_{\rm dir}}{9M_A^2}.
}
\]

Thus pure Eulerian direction motion is not structure-free.

It requires a fixed normalized spatial/log-radial direction texture.

This is consistent with the earlier M5-360 and M5-667 direction-coherence audits, but it remains a normalized critical quantity.

## 7. Exact strain-eigenframe formula

Let

\[
\Sigma_A e_i=\lambda_i e_i,
\qquad
i=1,2,3,
\]

with an orthonormal eigenframe.

Define

\[
a_i:=(\xi_B\cdot e_i)^2,
\qquad
\sum_i a_i=1.
\]

Then

\[
|\mathcal S_\xi|^2
=
|P_{\xi_B}^\perp\Sigma_A\xi_B|^2.
\]

Since

\[
|P_\xi^\perp S\xi|^2
=
\xi^TS^2\xi-(\xi^TS\xi)^2,
\]

we obtain

\[
\boxed{
|\mathcal S_\xi|^2
=
\sum_i a_i\lambda_i^2
-
\left(\sum_i a_i\lambda_i\right)^2.
}
\]

Equivalently,

\[
\boxed{
|\mathcal S_\xi|^2
=
\sum_{i<j}
a_i a_j(\lambda_i-\lambda_j)^2.
}
\]

Thus the strain channel is exactly an eigenframe-variance observable.

It vanishes precisely when the vorticity direction lies entirely inside one strain eigenspace, allowing for eigenvalue degeneracy.

## 8. Meaning of the strain branch

A positive \(S_{\rm dir}\) floor forces recurrent quantitative coexistence of

- nontrivial strain eigengaps;
- and vorticity weight distributed across different eigendirections.

It is not merely positive scalar stretching

\[
\xi_B^T\Sigma_A\xi_B.
\]

The longitudinal stretching scalar and transverse direction-rotation amplitude are distinct.

This connects M20 to the earlier strain-eigenframe framework, including M5-608, without identifying their signed scalar ledgers.

## 9. Exact viscous projective term

Write

\[
B=\varrho\xi_B,
\qquad
\varrho=|B|.
\]

Since

\[
\mathcal L_2
=
\partial_q^2-3\partial_q+2+\Delta_S,
\]

the perpendicular projection eliminates the scalar zeroth-order \(2\varrho\xi_B\) term.

A direct product expansion gives

\[
\boxed{
\begin{aligned}
\mathcal V_\xi
&=
P_{\xi_B}^\perp
\left[
\partial_q^2\xi_B
-
3\partial_q\xi_B
+
\Delta_S\xi_B
\right]
\\
&\quad
+
2(\partial_q\log\varrho)\partial_q\xi_B
+
2\nabla_S\log\varrho\cdot\nabla_S\xi_B.
\end{aligned}
}
\]

Thus the viscous projective channel contains

- second direction derivatives;
- first direction derivatives;
- amplitude-gradient / direction-gradient coupling.

It is not a positive scalar dissipation by itself.

## 10. Material branch split

If the transport branch is small while \(\partial_z\xi_B\) is large, then the normalized material derivative

\[
\mathcal M_\xi
=
-\partial_z\xi_B+\mathcal T_A\xi_B
\]

must be large.

But

\[
\mathcal M_\xi
=
\mathcal S_\xi+\mathcal V_\xi.
\]

Hence material projective turnover itself splits into

\[
\boxed{
\text{transverse strain rotation}
\lor
\text{viscous projective diffusion}.
}
\]

No pressure or scalar amplitude term is available to pay this branch.

## 11. Criticality firewall

All three terms in the normalized direction equation are order one at the terminal critical scale.

Returning to physical variables adds the common \(r^{-2}\) material-time scale.

Therefore a fixed normalized floor in any of

\[
T_{\rm dir},
\qquad
S_{\rm dir},
\qquad
V_{\rm dir}
\]

is still Type-I critical.

No noncritical original-variable contradiction follows from the norm floor alone.

## 12. Updated direction frontier

The genuine M20 direction branch refines to

\[
\boxed{
V_{\rm dir}^{curl}
\Longrightarrow
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj}.
}
\]

Here:

- \(T_{\rm texture}\): advection of a nontrivial spatial/log-radial vorticity-direction texture;
- \(S_{\rm eig}\): transverse strain-eigenframe action;
- \(V_{\rm proj}\): viscous projective diffusion/amplitude-gradient coupling.

## 13. What is most promising

The strain branch has the cleanest finite-dimensional algebra:

\[
|\mathcal S_\xi|^2
=
\sum_{i<j}a_i a_j(\lambda_i-\lambda_j)^2.
\]

However existing recurrent CE-H/eigenframe firewalls show that an order-one strain misalignment floor alone need not be nonrecyclable.

The transport branch connects directly to spatial direction coherence/roughness criteria but is still critically scaled.

The viscous branch is the natural candidate for a derivative budget, but its projective form contains signed/cross terms and must not be counted as a fresh positive dissipation without further identity.

## 14. Next target

The next highest-value calculation is to derive the **relative-amplitude reweighting branch** from M20-001 in the same exact probability-current language.

That branch can change global projective covariance even with

\[
\partial_z\xi_B=0.
\]

A correct projective theory must therefore track both:

\[
\boxed{
\text{local direction rotation}
\quad\text{and}\quad
\text{amplitude reweighting among pre-existing directions}.
}
\]

This is the natural M20-003 target.

\[
\boxed{\text{M20-002 COMPLETE; TRUE TERMINAL DIRECTION MOTION SPLITS INTO TRANSPORT, STRAIN-EIGENFRAME ACTION, OR VISCOUS PROJECTIVE DIFFUSION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
