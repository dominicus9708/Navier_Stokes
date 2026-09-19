# M20 Current Frontier

**Date:** 2026-09-19  
**Active family:** M20  
**Current calculation tip:** M20-005  
**Next calculation ID:** M20-006  
**Previous frozen family:** M19 at M19-442  
**Status:** ACTIVE PROJECTIVE-VORTICITY PHASE / GLOBAL TANGENT RESIDUAL REFINED TO REWEIGHTING OR TRUE DIRECTION MOTION / POSITIVE-VOLUME NODAL ESCAPE CLOSED / TRUE DIRECTION MOTION SPLIT INTO TRANSPORT, STRAIN-EIGENFRAME ACTION, OR VISCOUS PROJECTIVE DIFFUSION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Canonical inherited input

From frozen M19,

\[
D_\omega=\mathcal K_3C=G_z(0),
\]

and

\[
\boxed{
C^\perp_{\rm mandatory}
\Longrightarrow
D_{\rm dip}^{\rm crit,cons}
\lor
V_{\rm norm}^{\rm curl}
\lor
V_{\rm tan}^{\rm curl}.
}
\]

The pressure-dipole branch remains a classified finite-dimensional critical conservative firewall.

## 2. M20-001 — global tangent is not pointwise direction tangent

Let

\[
\alpha
=
\frac{\langle B,D_\omega\rangle}{b_2},
\qquad
T_\omega=D_\omega-\alpha B.
\]

On \(\{B\neq0\}\), define

\[
\lambda=\frac{B\cdot D_\omega}{|B|^2},
\qquad
R_\omega=P_B^\perp D_\omega.
\]

Then

\[
T_\omega=(\lambda-\alpha)B+R_\omega.
\]

The exact invariant decomposition is

\[
\|T_\omega\|_H^2
=
b_2\operatorname{Var}_{\pi_B}(\lambda)
+
b_2\mathbb E_{\pi_B}|\partial_z\xi_B|^2
+
Z_0,
\]

where \(Z_0\) is the zero-vorticity-set contribution provisionally isolated in M20-001.

Thus global Hilbert tangency does not mean local vorticity-axis rotation.

## 3. M20-004 — nodal L2 channel is closed

Smooth terminal vorticity satisfies

\[
\nabla B=0,
\qquad
\nabla^2B=0
\]

almost everywhere on \(\{B=0\}\).

The terminal wedge vorticity PDE

\[
-D_\omega+\mathfrak A(A,B)
=
\mathfrak S(B,A)+\mathcal L_2B
\]

therefore gives

\[
\boxed{
D_\omega=0
\quad\text{a.e. on }\{B=0\}.
}
\]

Hence

\[
\boxed{Z_0=0.}
\]

The authoritative tangent identity is now

\[
\boxed{
\|T_\omega\|_H^2
=
b_2\operatorname{Var}_{\pi_B}(\lambda)
+
b_2\mathbb E_{\pi_B}|\partial_z\xi_B|^2.
}
\]

Therefore

\[
\boxed{
V_{\rm tan}^{curl}
\Longrightarrow
V_{\rm reweight}
\lor
V_{\rm dir}.
}
\]

Codimension-lower nodal interfaces remain possible geometric objects, but there is no independent positive-volume nodal L2 payer.

## 4. M20-001 robust high-vorticity placement

On a genuine direction branch, monotone convergence gives a fixed

\[
\beta_*>0
\]

such that a positive fraction of the direction residual lies on

\[
\{|B|\ge\beta_*\}.
\]

Using the compact amplitude ceiling \(|B|\le M_B\),

\[
\boxed{
\left\langle
1_{\{|B|\ge\beta_*\}}
|\partial_z\xi_B|^2
\right\rangle
\ge
\eta_{\rm dir}>0.
}
\]

Thus the true direction branch can be studied on a robust nonzero-vorticity set.

## 5. M20-002 — true direction motion has three PDE mechanisms

The exact terminal direction equation is

\[
-\partial_z\xi_B
+
\mathcal T_A\xi_B
=
P_{\xi_B}^\perp\Sigma_A\xi_B
+
\mathcal V_\xi,
\]

where

\[
\mathcal T_A\xi_B
=
A_r\partial_q\xi_B
+
A_T\cdot\nabla_S\xi_B,
\]

and

\[
\mathcal V_\xi
=
\frac1{|B|}
P_{\xi_B}^\perp\mathcal L_2B.
\]

Therefore

\[
\boxed{
V_{\rm dir}
\Longrightarrow
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj}.
}
\]

Interpretation:

- \(T_{\rm texture}\): Eulerian advection of pre-existing direction texture;
- \(S_{\rm eig}\): transverse strain-eigenframe action;
- \(V_{\rm proj}\): viscous projective diffusion / amplitude-gradient coupling.

A fixed-coordinate wedge-depth direction change is not automatically a material direction turnover.

## 6. M20-003 — reweighting is an exact probability current

Define

\[
d\pi_z
=
\frac{|G(z)|^2}{b_2(z)}d\mu.
\]

Then

\[
\boxed{
\partial_zd\pi_z|_0
=
2(\lambda-\alpha)d\pi_B.
}
\]

Thus

\[
4\operatorname{Var}_{\pi_B}(\lambda)
\]

is the instantaneous Fisher-Rao speed squared of the normalized enstrophy distribution.

For the projective tensor

\[
Q_\xi=\xi_B\otimes\xi_B,
\qquad
\mathsf C_B=\mathbb E_{\pi_B}Q_\xi,
\]

one has

\[
\boxed{
\mathsf C_B'
=
2\operatorname{Cov}_{\pi_B}(\lambda,Q_\xi)
+
\mathbb E_{\pi_B}
[
\xi_z\otimes\xi+\xi\otimes\xi_z
].
}
\]

Hence global projective covariance can change either through local direction rotation or differential amplitude selection among directions already present.

Positive \(\operatorname{Var}(\lambda)\) does not force a nonzero projective covariance current.

Thus

\[
\boxed{
V_{\rm reweight}
\Longrightarrow
R_{\rm proj}
\lor
R_{\rm silent}.
}
\]

## 7. M20-005 — strain branch is a projective double commutator

Let

\[
Q=\xi\otimes\xi,
\qquad
\gamma=\xi^TS\xi,
\qquad
s_\perp=P_\xi^\perp S\xi.
\]

The strain-only projector motion is

\[
\boxed{
D_tQ|_S
=
[[S,Q],Q].
}
\]

Moreover

\[
\boxed{
\|[S,Q]\|_F^2
=
\|[[S,Q],Q]\|_F^2
=
2|s_\perp|^2.
}
\]

In a strain eigenframe,

\[
\boxed{
|s_\perp|^2
=
\sum_{i<j}
a_i a_j(\lambda_i-\lambda_j)^2.
}
\]

Thus \(S_{\rm eig}\) is a coordinate-free projective noncommutation detector.

## 8. Rayleigh compensation law

The physical material direction equation is

\[
D_t\xi=s_\perp+v_\perp,
\qquad
v_\perp=\frac{\nu}{|\omega|}P_\xi^\perp\Delta\omega.
\]

Using the exact strain equation gives

\[
\boxed{
D_t\gamma
=
-\gamma^2
+
|s_\perp|^2
-
\xi^T\nabla^2p\,\xi
+
\nu\xi^T\Delta S\,\xi
+
2v_\perp\cdot s_\perp.
}
\]

Therefore transverse strain produces a positive Rayleigh-ascent term, but pressure Hessian, evolving strain, and viscous projective coupling can compensate it.

No standalone Lyapunov sign follows.

## 9. Current authoritative M20 tangent architecture

Combining M20-001~005,

\[
\boxed{
V_{\rm tan}^{curl}
\Longrightarrow
R_{\rm proj}
\lor
R_{\rm silent}
\lor
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj}.
}
\]

These are typed mechanisms, not necessarily independent proof roots.

The strongest actual branch reduction so far is

\[
\boxed{
V_{\rm nodal}^{L^2}
\text{ removed}.
}
\]

## 10. Current highest-value target

The next target is the compensation structure of the strain/projective branch.

The useful exact observable is

\[
\boxed{
[S,Q]
}
\]

rather than a chosen strain eigenframe.

M20-006 should test whether recurrent positive projective noncommutation can be converted into a signed covariance/pressure-Hessian compensation law that is not merely another critical unsigned norm.

A secondary target is whether \(R_{\rm silent}\) is truly silent only at second moment or necessarily appears in a higher projective moment.

## 11. Persistent firewalls

Do not infer:

- global Hilbert tangent \(\Rightarrow\) pointwise direction tangent;
- wedge-depth direction change \(\Rightarrow\) material direction turnover;
- positive reweighting variance \(\Rightarrow\) projective covariance change;
- positive transverse strain commutator \(\Rightarrow\) monotone stretching growth;
- fixed normalized projective activity \(\Rightarrow\) original-variable contradiction.

M19-440 remains authoritative for terminal energy-payer bookkeeping.

\[
\boxed{\text{CURRENT TIP: M20-005 / NEXT: M20-006.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
