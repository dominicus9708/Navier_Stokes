# M20-001 — The global enstrophy-tangent curl residual splits exactly into relative-amplitude reweighting, true vorticity-direction motion, or nodal birth

Date: 2026-09-19  
Canonical ID: **M20-001**  
Status: **FIRST M20 PROJECTIVE-VORTICITY MODULE / AUTHORITATIVE REFINEMENT OF THE M19-442 TANGENT BRANCH / GLOBAL HILBERT ORTHOGONALITY TO B DOES NOT MEAN POINTWISE ORTHOGONALITY / THE TANGENT CURL RESIDUAL HAS AN EXACT THREE-CHANNEL DECOMPOSITION INTO RELATIVE AMPLITUDE REWEIGHTING, POINTWISE DIRECTION TURNOVER, AND VORTICITY-NODAL BIRTH / A TRUE DIRECTION BRANCH ADMITS A FIXED POSITIVE HIGH-VORTICITY THRESHOLD AFTER INVARIANT AVERAGING / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from frozen M19

M19-442 defines

\[
D_\omega:=\mathcal K_3C=G_z(0)
\]

and, with

\[
b_2:=\langle\|B\|_2^2\rangle>0,
\qquad
\chi_\omega:=\langle B,D_\omega\rangle_H,
\]

sets

\[
\alpha:=\frac{\chi_\omega}{b_2}.
\]

The global Hilbert-tangent component is

\[
\boxed{
T_\omega:=D_\omega-\alpha B.
}
\]

M19-442's difficult branch is

\[
\boxed{
\|T_\omega\|_H^2>0.
}
\]

The first M20 audit asks what this actually means pointwise.

## 2. Global tangent does not mean local direction tangent

The relation

\[
\langle B,T_\omega\rangle_H=0
\]

is one global invariant-mean orthogonality condition.

It does **not** imply

\[
B(q,\omega)\cdot T_\omega(q,\omega)=0
\]

pointwise.

For example, a field of the form

\[
D_\omega=\lambda(q,\omega)B
\]

with nonconstant \(\lambda\) can satisfy

\[
D_\omega-\alpha B\neq0
\]

even though \(D_\omega\) is pointwise parallel to \(B\) everywhere.

Such a field changes local vorticity amplitudes at different relative rates but does not rotate the local vorticity direction.

Therefore the preliminary wording

\[
V_{\rm tan}^{curl}
\approx
\text{direction turnover}
\]

must be refined.

## 3. Pointwise amplitude-direction decomposition

On the set

\[
\mathcal N^c:=\{B\neq0\},
\]

define

\[
\boxed{
\lambda
:=
\frac{B\cdot D_\omega}{|B|^2}
}
\]

and

\[
\boxed{
R_\omega
:=
P_B^\perp D_\omega
=
D_\omega-\lambda B.
}
\]

Then

\[
B\cdot R_\omega=0
\]

pointwise.

On the nodal set

\[
\mathcal N:=\{B=0\},
\]

set

\[
\lambda:=0,
\qquad
R_\omega:=D_\omega.
\]

Thus everywhere,

\[
D_\omega=\lambda B+R_\omega.
\]

## 4. Exact decomposition of the global tangent residual

Subtract the global scalar part:

\[
T_\omega
=
(\lambda-\alpha)B+R_\omega.
\]

On \(\{B\neq0\}\), the two terms are pointwise orthogonal.

On \(\{B=0\}\), the first term vanishes.

Hence exactly

\[
\boxed{
\|T_\omega\|_H^2
=
\left\langle
(\lambda-\alpha)^2|B|^2
\right\rangle
+
\left\langle
1_{\{B\neq0\}}|R_\omega|^2
\right\rangle
+
\left\langle
1_{\{B=0\}}|D_\omega|^2
\right\rangle.
}
\]

This is the fundamental M20-001 identity.

## 5. Enstrophy-weighted probability measure

Define the invariant enstrophy probability

\[
\boxed{
d\pi_B
:=
\frac{|B|^2}{b_2}\,d\mu,
}
\]

where \(d\mu\) denotes invariant q-mean times sphere measure.

Because

\[
\langle B,D_\omega\rangle
=
\langle\lambda|B|^2\rangle,
\]

we have

\[
\boxed{
\mathbb E_{\pi_B}\lambda=\alpha.
}
\]

Therefore

\[
\boxed{
\left\langle
(\lambda-\alpha)^2|B|^2
\right\rangle
=
b_2\operatorname{Var}_{\pi_B}(\lambda).
}
\]

## 6. Exact meaning of lambda

Let

\[
\rho(z,q,\omega):=|G(z,q,\omega)|.
\]

At z=0,

\[
G(0)=B,
\qquad
G_z(0)=D_\omega.
\]

On \(\{B\neq0\}\),

\[
\rho_z(0)
=
\frac{B}{|B|}\cdot D_\omega
=
\lambda|B|.
\]

Thus

\[
\boxed{
\lambda
=
\partial_z\log\rho\big|_{z=0}.
}
\]

Also

\[
\frac12
\partial_z
\log
\langle|G(z)|^2\rangle
\Big|_{z=0}
=
\frac{\langle B,D_\omega\rangle}{b_2}
=
\alpha.
\]

Therefore

\[
\boxed{
\lambda-\alpha
=
\partial_z
\left[
\log|G|
-
\frac12\log\langle|G|^2\rangle
\right]_{z=0}.
}
\]

The first M20-001 channel is exactly **relative local vorticity-amplitude reweighting**.

This is the terminal-wedge analogue of the relative-amplitude reweighting mechanism previously isolated in M19-331.

## 7. Exact meaning of the pointwise perpendicular part

On \(\{B\neq0\}\), define

\[
\xi_B=\frac{B}{|B|}.
\]

The derivative of a normalized vector gives

\[
\boxed{
\partial_z\xi_B
=
\frac{P_B^\perp D_\omega}{|B|}
=
\frac{R_\omega}{|B|}.
}
\]

Therefore

\[
\boxed{
\left\langle
1_{\{B\neq0\}}|R_\omega|^2
\right\rangle
=
b_2
\mathbb E_{\pi_B}
\left[
|\partial_z\xi_B|^2
\right].
}
\]

This is the true local vorticity-direction turnover channel.

## 8. Nodal birth channel

On

\[
\{B=0\},
\]

the direction \(\xi_B\) is undefined.

If

\[
D_\omega\neq0
\]

there, then

\[
G(z)=zD_\omega+o(z)
\]

at first order.

Thus vorticity is being created from, or annihilated into, a terminal vorticity zero rather than rotating a pre-existing nonzero direction.

Define

\[
\boxed{
Z_0
:=
\left\langle
1_{\{B=0\}}|D_\omega|^2
\right\rangle.
}
\]

This is a separate nodal formation channel and must not be labeled direction turnover.

## 9. Exact three-channel normal form

Combining Sections 4--8,

\[
\boxed{
\|T_\omega\|_H^2
=
b_2\operatorname{Var}_{\pi_B}(\lambda)
+
b_2\mathbb E_{\pi_B}
|\partial_z\xi_B|^2
+
Z_0.
}
\]

Hence the M19-442 tangent branch refines to

\[
\boxed{
V_{\rm tan}^{curl}
\Longrightarrow
V_{\rm reweight}
\lor
V_{\rm dir}
\lor
V_{\rm nodal}.
}
\]

The three branches are:

\[
V_{\rm reweight}:
\operatorname{Var}_{\pi_B}(\lambda)>0,
\]

\[
V_{\rm dir}:
\mathbb E_{\pi_B}|\partial_z\xi_B|^2>0,
\]

\[
V_{\rm nodal}:
Z_0>0.
\]

## 10. Quantitative fork

Suppose the selected tangent branch has

\[
\|T_\omega\|_H^2\ge\tau_*>0.
\]

Then at least one of

\[
\boxed{
b_2\operatorname{Var}_{\pi_B}(\lambda)
\ge
\frac{\tau_*}{3},
}
\]

\[
\boxed{
b_2\mathbb E_{\pi_B}|\partial_z\xi_B|^2
\ge
\frac{\tau_*}{3},
}
\]

or

\[
\boxed{
Z_0\ge\frac{\tau_*}{3}
}
\]

holds.

This is the correct first M20 projective split.

## 11. Robust high-vorticity localization of a genuine direction branch

Assume the genuine direction term satisfies

\[
\left\langle
1_{\{B\neq0\}}|R_\omega|^2
\right\rangle
\ge r_*>0.
\]

For \(\beta>0\), define

\[
\mathcal R_{\ge\beta}
:=
\left\langle
1_{\{|B|\ge\beta\}}
|R_\omega|^2
\right\rangle.
\]

As \(\beta\downarrow0\),

\[
\mathcal R_{\ge\beta}
\uparrow
\left\langle
1_{\{B\neq0\}}|R_\omega|^2
\right\rangle.
\]

By monotone convergence, there exists a fixed

\[
\boxed{\beta_*>0}
\]

such that

\[
\boxed{
\mathcal R_{\ge\beta_*}
\ge
\frac{r_*}{2}.
}
\]

Thus a true direction branch always admits a positive fixed vorticity-amplitude threshold after invariant averaging.

If compactness gives

\[
|B|\le M_B,
\]

then on this subset

\[
|R_\omega|^2
=
|B|^2|\partial_z\xi_B|^2
\le
M_B^2|\partial_z\xi_B|^2.
\]

Therefore

\[
\boxed{
\left\langle
1_{\{|B|\ge\beta_*\}}
|\partial_z\xi_B|^2
\right\rangle
\ge
\frac{r_*}{2M_B^2}.
}
\]

This is the robust high-vorticity direction-turnover floor sought at the M20 boundary.

## 12. Covariance interpretation: direction can change without local rotation

Define the normalized terminal vorticity covariance

\[
\mathsf C_B
:=
\frac{\langle B\otimes B\rangle}{b_2}.
\]

Differentiating in z at the terminal boundary yields

\[
\boxed{
\mathsf C_B'
=
\frac{2}{b_2}
\left\langle
(\lambda-\alpha)B\otimes B
\right\rangle
+
\frac1{b_2}
\left\langle
R_\omega\otimes B
+
B\otimes R_\omega
\right\rangle.
}
\]

Therefore the global projective distribution can evolve through two distinct mechanisms:

1. **amplitude selection/reweighting** among already existing directions;
2. **actual local direction rotation**.

Even if

\[
R_\omega=0,
\]

the covariance may change if

\[
\lambda-\alpha
\]

is correlated with direction.

This matches the older projective-vorticity covariance framework and explains why a global tangent mode need not be a local turning mode.

## 13. Relation to earlier direction criteria

M5-360 and M5-667 concern spatial coherence/roughness of the vorticity direction in physical or normalized space.

M20-001 concerns a different derivative:

\[
\partial_z\xi_B
\]

at the terminal wedge boundary.

A positive depth-direction turnover floor does not by itself imply a Constantin--Fefferman/Giga--Miura spatial direction defect, nor vice versa.

A further PDE/transport coupling is required.

## 14. Updated M20 frontier

The authoritative M20 frontier is now

\[
\boxed{
C^\perp_{\rm mandatory}
\Longrightarrow
D_{\rm dip}^{crit,cons}
\lor
V_{\rm norm}^{curl}
\lor
V_{\rm reweight}^{curl}
\lor
V_{\rm dir}^{curl}
\lor
V_{\rm nodal}^{curl}.
}
\]

The pressure-dipole branch remains the classified critical conservative firewall.

The M19 tangent branch is no longer treated as synonymous with direction turnover.

## 15. Next targets

Two branches now deserve separate calculations.

### M20-002 — genuine direction branch

Use the fixed high-vorticity threshold \(\beta_*\) and the direction-turnover floor to project the vorticity equation onto the plane perpendicular to \(\xi_B\).

This should isolate the competition among:

- transverse strain/eigenframe rotation;
- transverse viscous diffusion;
- spatial transport of direction.

### M20-003 — reweighting branch

Use

\[
\lambda-\alpha
=
\partial_z
\left[
\log|G|
-
\frac12\log\langle|G|^2\rangle
\right]_{z=0}
\]

to derive the terminal relative-amplitude selection current and compare it with M19-331--332's recurrent reweighting firewall.

\[
\boxed{\text{M20-001 COMPLETE; GLOBAL HILBERT TANGENCY SPLITS INTO REWEIGHTING, TRUE DIRECTION TURNOVER, OR NODAL VORTICITY BIRTH.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
