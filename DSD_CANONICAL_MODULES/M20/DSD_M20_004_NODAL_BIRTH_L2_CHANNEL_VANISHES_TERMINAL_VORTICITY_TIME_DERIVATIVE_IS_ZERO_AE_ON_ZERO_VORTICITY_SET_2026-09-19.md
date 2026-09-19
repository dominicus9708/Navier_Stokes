# M20-004 — The nodal-birth L2 channel vanishes: the terminal vorticity time derivative is zero almost everywhere on the zero-vorticity set

Date: 2026-09-19  
Canonical ID: **M20-004**  
Status: **NODAL-CHANNEL CLOSURE AT VOLUME-MEASURE LEVEL / SMOOTH TERMINAL VORTICITY HAS FIRST AND SECOND SPATIAL DERIVATIVES ZERO ALMOST EVERYWHERE ON ITS ZERO SET / THE TERMINAL VORTICITY PDE THEN FORCES D_OMEGA=G_z(0)=0 ALMOST EVERYWHERE ON THAT ZERO SET / THE M20-001 NODAL-BIRTH TERM HAS ZERO L2 INVARIANT MEASURE / CODIMENSIONAL NODAL INTERFACES MAY STILL MATTER GEOMETRICALLY BUT ARE NOT AN INDEPENDENT VOLUME PAYER / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. The M20-001 nodal term

M20-001 defines

\[
Z_0
:=
\left\langle
1_{\{B=0\}}
|D_\omega|^2
\right\rangle,
\]

where

\[
B=G(0),
\qquad
D_\omega=G_z(0).
\]

It was provisionally interpreted as vorticity birth/annihilation on the terminal zero-vorticity set.

The present module audits whether this can carry positive volume-measure L2 mass.

## 2. Regularity input

The retained terminal hard hull has smooth off-origin terminal coefficients with the local derivative regularity already used in the M19 terminal-jet construction.

In particular, on each fixed q-sphere chart we may use

\[
B\in C^2
\]

and hence locally

\[
B\in W^{2,p}_{loc}
\]

for every finite p.

This is more than sufficient for the standard level-set derivative property used below.

## 3. First derivatives vanish almost everywhere on the zero set

Let one scalar component of B be \(f\).

For a Sobolev \(W^{1,p}\) function,

\[
\nabla f=0
\quad\text{a.e. on a level set }\{f=c\}.
\]

Apply this with \(c=0\).

Since the vector zero set

\[
E:=\{B=0\}
\]

is contained in the zero set of every component, we obtain

\[
\boxed{
\nabla B=0
\quad\text{a.e. on }E.
}
\]

Here the derivatives include the q and spherical tangential derivatives in local charts.

## 4. Second derivatives also vanish almost everywhere

Each first derivative component

\[
g=\partial_j B_k
\]

belongs locally to \(W^{1,p}\).

From Section 3,

\[
g=0
\quad\text{a.e. on }E.
\]

Apply the same level-set derivative property to g.

Then

\[
\nabla g=0
\quad\text{a.e. on }E.
\]

Therefore

\[
\boxed{
\nabla^2 B=0
\quad\text{a.e. on }E.
}
\]

Equivalently, all first- and second-order q/angular derivatives entering the terminal vorticity operator vanish almost everywhere on the zero set.

## 5. Terminal vorticity equation

M5-585 gives the exact wedge vorticity equation

\[
-\partial_zG
+
\mathfrak A(F,G)
=
\mathfrak S(G,F)
+
\mathfrak L_2G.
\]

At z=0,

\[
F=A,
\qquad
G=B,
\qquad
\partial_zG=D_\omega.
\]

Hence

\[
\boxed{
-D_\omega
+
\mathfrak A(A,B)
=
\mathfrak S(B,A)
+
\mathcal L_2B.
}
\]

## 6. Every spatial term vanishes almost everywhere on E

On

\[
E=\{B=0\},
\]

we have almost everywhere:

\[
B=0,
\qquad
\nabla B=0,
\qquad
\nabla^2B=0.
\]

The stretching term is linear in B:

\[
\mathfrak S(B,A)=0.
\]

The advection term is first order in B:

\[
\mathfrak A(A,B)=0.
\]

The Laplacian/homogeneity operator uses only B and derivatives through second order:

\[
\mathcal L_2B=0.
\]

Therefore the terminal vorticity equation gives

\[
\boxed{
D_\omega=0
\quad\text{a.e. on }\{B=0\}.
}
\]

## 7. The M20-001 nodal L2 term vanishes

It follows immediately that

\[
\boxed{
Z_0
=
\left\langle
1_{\{B=0\}}
|D_\omega|^2
\right\rangle
=
0.
}
\]

Thus vorticity-nodal birth is not an independent invariant-volume L2 payer.

## 8. Important scope: interfaces are not removed

This result does **not** say that vorticity zeros are dynamically irrelevant.

A codimension-one or codimension-two nodal set can still carry:

- topology;
- crossing information;
- sign/orientation changes;
- interface flux;
- high derivative geometry;
- finite-order nodal jets.

Such sets normally have zero ambient volume measure.

M20-004 only removes the proposed positive-volume L2 channel

\[
1_{\{B=0\}}|D_\omega|^2.
\]

It does not remove lower-dimensional nodal/interface mechanisms already present in earlier M17 analyses.

## 9. Authoritative correction to M20-001

The exact M20-001 identity reduces from three terms to two:

\[
\boxed{
\|T_\omega\|_H^2
=
b_2\operatorname{Var}_{\pi_B}(\lambda)
+
b_2
\mathbb E_{\pi_B}
|\partial_z\xi_B|^2.
}
\]

There is no third positive-volume nodal term.

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

If

\[
\|T_\omega\|_H^2\ge\tau_*>0,
\]

then at least one of

\[
\boxed{
b_2\operatorname{Var}_{\pi_B}(\lambda)
\ge
\frac{\tau_*}{2}
}
\]

or

\[
\boxed{
b_2
\mathbb E_{\pi_B}
|\partial_z\xi_B|^2
\ge
\frac{\tau_*}{2}
}
\]

holds.

## 10. Robust high-vorticity threshold is now unconditional on the direction branch

If the second branch holds, then

\[
\left\langle
1_{\{B\neq0\}}
|R_\omega|^2
\right\rangle
\ge
\frac{\tau_*}{2}.
\]

Because the zero-set contribution vanishes and

\[
1_{\{|B|\ge\beta\}}
\uparrow
1_{\{B\neq0\}}
\qquad
(\beta\downarrow0),
\]

there exists a fixed

\[
\boxed{\beta_*>0}
\]

such that

\[
\boxed{
\left\langle
1_{\{|B|\ge\beta_*\}}
|R_\omega|^2
\right\rangle
\ge
\frac{\tau_*}{4}.
}
\]

Thus every genuine M20 direction branch can be placed on a robust positive-vorticity-amplitude subset.

## 11. Updated M20 tangent architecture

The former M19 tangent residual now has the sharper exact structure

\[
\boxed{
V_{\rm tan}^{curl}
\Longrightarrow
V_{\rm reweight}
\lor
V_{\rm dir}.
}
\]

Then M20-002 and M20-003 refine these as

\[
V_{\rm dir}
\Longrightarrow
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj},
\]

and

\[
V_{\rm reweight}
\Longrightarrow
R_{\rm proj}
\lor
R_{\rm silent}.
\]

Hence

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

No positive-volume nodal root remains.

## 12. Strategic consequence

This is a real branch reduction.

The difficult pressure-free tangent residual cannot hide its invariant L2 mass entirely at vorticity zeros.

It must act through one of two mechanisms on the nonzero-vorticity population:

1. differential amplitude reweighting;
2. actual direction motion.

The first is a probability-selection problem.

The second is a transport/strain/diffusion projective PDE problem.

## 13. Next target

The cleanest next step is to test the finite-dimensional strain channel

\[
S_{\rm eig}
\]

against the terminal/projective covariance dynamics.

The exact local density

\[
|P_\xi^\perp\Sigma_A\xi|^2
=
\sum_{i<j}
a_i a_j(\lambda_i-\lambda_j)^2
\]

should be compared with

\[
\gamma=\xi^T\Sigma_A\xi
\]

and the normalized direction projector

\[
Q_\xi=\xi\otimes\xi.
\]

The immediate question is whether transverse strain action produces an independent signed projective current or only a reversible eigenframe rotation.

\[
\boxed{\text{M20-004 COMPLETE; THE POSITIVE-VOLUME NODAL-BIRTH L2 CHANNEL IS CLOSED.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
