# M20-006 — Projective strain noncommutation obeys an exact signed transverse-pressure compensation law

Date: 2026-09-20  
Canonical ID: **M20-006**  
Status: **SIGNED PROJECTIVE-COMMUTATOR COMPENSATION / THE TRANSVERSE STRAIN VECTOR s_perp=P_xi^perp S xi HAS A CLOSED COVARIANT MATERIAL EVOLUTION IN WHICH THE S^2 TERMS CANCEL / THE PRESSURE HESSIAN ENTERS ONLY THROUGH ITS TRANSVERSE PROJECTIVE COMPONENT P_xi^perp (nabla^2 p) xi, EQUIVALENTLY THROUGH THE COMMUTATOR [nabla^2 p,Q] / POSITIVE AXIAL STRETCHING DAMPENS PROJECTIVE STRAIN NONCOMMUTATION UNLESS REPLENISHED BY TRANSVERSE PRESSURE, STRAIN DIFFUSION, VISCOUS PROJECTIVE COUPLING, OR COMPRESSIVE PHASES / THIS IS A SIGNED COMPENSATION LAW, NOT YET A GLOBAL CLOSURE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Projective strain variables

On the nonzero-vorticity set write

\[
\omega=\rho\xi,
\qquad
|\xi|=1.
\]

Let

\[
S=\frac12(\nabla u+\nabla u^T),
\qquad
H_p:=\nabla^2p,
\]

and define

\[
\gamma:=\xi^TS\xi,
\]

\[
\boxed{
s_\perp
:=
P_\xi^\perp S\xi
=
S\xi-\gamma\xi.
}
\]

M20-005 shows

\[
\|[S,Q]\|_F^2=2|s_\perp|^2,
\qquad
Q:=\xi\otimes\xi.
\]

Thus \(s_\perp\) and \([S,Q]\) are equivalent projective noncommutation variables.

## 2. Direction equation

The exact physical vorticity-direction equation is

\[
D_t\xi
=
s_\perp+v_\perp,
\]

where

\[
D_t:=\partial_t+u\cdot\nabla
\]

and

\[
\boxed{
v_\perp
:=
\frac{\nu}{\rho}
P_\xi^\perp\Delta\omega.
}
\]

Both

\[
s_\perp\cdot\xi=0,
\qquad
v_\perp\cdot\xi=0.
\]

## 3. Differentiate the transverse strain vector

Start from

\[
s_\perp=S\xi-\gamma\xi.
\]

Then

\[
D_ts_\perp
=
(D_tS)\xi
+
S D_t\xi
-
(D_t\gamma)\xi
-
\gamma D_t\xi.
\]

Project perpendicular to \(\xi\):

\[
P_\xi^\perp D_ts_\perp
=
P_\xi^\perp(D_tS)\xi
+
P_\xi^\perp S D_t\xi
-
\gamma D_t\xi.
\]

The longitudinal \(D_t\gamma\) term disappears under the projection.

## 4. Insert the exact strain equation

For incompressible Navier--Stokes,

\[
D_tS
=
-S^2-\Omega^2-H_p+\nu\Delta S.
\]

Because \(\xi\) is the vorticity axis,

\[
\Omega\xi=0,
\qquad
\Omega^2\xi=0.
\]

Also

\[
S\xi=\gamma\xi+s_\perp,
\]

so

\[
S^2\xi
=
\gamma S\xi+Ss_\perp.
\]

Hence

\[
P_\xi^\perp S^2\xi
=
\gamma s_\perp
+
P_\xi^\perp Ss_\perp.
\]

## 5. Exact cancellation of the internal S-squared terms

Using

\[
D_t\xi=s_\perp+v_\perp,
\]

we have

\[
P_\xi^\perp S D_t\xi
=
P_\xi^\perp Ss_\perp
+
P_\xi^\perp Sv_\perp.
\]

Therefore the terms

\[
-P_\xi^\perp Ss_\perp
\]

from \(-S^2\xi\) and

\[
+P_\xi^\perp Ss_\perp
\]

from \(S D_t\xi\) cancel exactly.

The remaining terms give

\[
\boxed{
\begin{aligned}
P_\xi^\perp D_ts_\perp
={}&
-2\gamma s_\perp
-
P_\xi^\perp H_p\xi
\\
&+
\nu P_\xi^\perp(\Delta S)\xi
+
P_\xi^\perp(S-\gamma I)v_\perp.
\end{aligned}
}
\]

This is the main M20-006 vector law.

## 6. Interpretation of the four channels

The projective strain vector evolves through exactly four typed mechanisms:

### A. Axial stretching/compression

\[
\boxed{-2\gamma s_\perp.}
\]

If

\[
\gamma>0,
\]

positive axial stretching damps the transverse strain misalignment.

If

\[
\gamma<0,
\]

axial compression amplifies it.

Thus the same \(\gamma\) that controls vorticity magnitude also controls projective strain alignment with the opposite role for the transverse defect.

### B. Transverse pressure-Hessian forcing

\[
\boxed{
-h_\perp,
\qquad
h_\perp:=P_\xi^\perp H_p\xi.
}
\]

Only the pressure-Hessian component that rotates the vorticity axis relative to the strain eigenspaces enters.

The scalar directional pressure curvature

\[
\xi^TH_p\xi
\]

does not directly drive \(s_\perp\).

### C. Strain diffusion

\[
\boxed{
\nu P_\xi^\perp(\Delta S)\xi.
}
\]

This is a derivative channel and returns to the existing strain/raw-H2 derivative firewalls.

### D. Viscous projective coupling

\[
\boxed{
P_\xi^\perp(S-\gamma I)v_\perp.
}
\]

The viscous direction motion is filtered by the strain relative to the current Rayleigh quotient.

## 7. Exact signed magnitude ledger

Because

\[
s_\perp\cdot\xi=0,
\]

we have

\[
s_\perp\cdot D_ts_\perp
=
s_\perp\cdot P_\xi^\perp D_ts_\perp.
\]

Therefore

\[
\boxed{
\begin{aligned}
\frac12D_t|s_\perp|^2
={}&
-2\gamma|s_\perp|^2
-
s_\perp\cdot H_p\xi
\\
&+
\nu s_\perp\cdot(\Delta S)\xi
+
s_\perp\cdot(S-\gamma I)v_\perp.
\end{aligned}
}
\]

Equivalently,

\[
\boxed{
D_t|s_\perp|^2
+
4\gamma|s_\perp|^2
=
-2s_\perp\cdot H_p\xi
+
2\nu s_\perp\cdot(\Delta S)\xi
+
2s_\perp\cdot(S-\gamma I)v_\perp.
}
\]

This is a signed transport/forcing law rather than another unsigned norm identity.

## 8. Projective commutator form of the pressure coupling

For symmetric matrices \(S\) and \(H_p\),

\[
[S,Q]
=
s_\perp\otimes\xi
-
\xi\otimes s_\perp.
\]

Define

\[
h_\perp:=P_\xi^\perp H_p\xi.
\]

Then similarly,

\[
[H_p,Q]
=
h_\perp\otimes\xi
-
\xi\otimes h_\perp.
\]

Therefore

\[
\boxed{
\langle[S,Q],[H_p,Q]\rangle_F
=
2s_\perp\cdot h_\perp.
}
\]

Since the longitudinal part of \(H_p\xi\) is orthogonal to \(s_\perp\),

\[
s_\perp\cdot H_p\xi=s_\perp\cdot h_\perp.
\]

Thus the pressure contribution is exactly

\[
\boxed{
-s_\perp\cdot H_p\xi
=
-\frac12
\langle[S,Q],[H_p,Q]\rangle_F.
}
\]

The pressure compensation is therefore a **signed projective commutator correlation**.

## 9. Full commutator-energy law

Because

\[
\|[S,Q]\|_F^2=2|s_\perp|^2,
\]

Section 7 becomes

\[
\boxed{
\begin{aligned}
\frac14D_t\|[S,Q]\|_F^2
+
\gamma\|[S,Q]\|_F^2
={}&
-\frac12
\langle[S,Q],[H_p,Q]\rangle_F
\\
&+
\nu s_\perp\cdot(\Delta S)\xi
\\
&+
s_\perp\cdot(S-\gamma I)v_\perp.
\end{aligned}
}
\]

This is the desired M20 signed projective compensation law.

## 10. Positive-stretching consequence

Suppose along a material segment

\[
\gamma\ge\gamma_0>0
\]

and the three forcing/coupling terms on the right vanish.

Then

\[
D_t|s_\perp|^2
\le
-4\gamma_0|s_\perp|^2,
\]

so

\[
\boxed{
|s_\perp(t)|^2
\le
e^{-4\gamma_0(t-t_0)}
|s_\perp(t_0)|^2.
}
\]

Thus persistent projective strain misalignment in a positively stretching material region cannot be self-sustained by strain algebra alone.

It requires at least one of:

- transverse pressure-Hessian replenishment;
- strain-diffusion replenishment;
- viscous projective coupling;
- or intervals with \(\gamma\le0\).

## 11. Compressional escape

If

\[
\gamma<0,
\]

then the homogeneous term

\[
-2\gamma s_\perp
\]

amplifies projective misalignment.

Therefore recurrent \([S,Q]\neq0\) can be maintained without pressure replenishment if the same material lineage repeatedly visits sufficiently compressive directional-strain phases.

This is a genuine signed escape.

Hence

\[
\boxed{
\text{persistent projective strain}
\not\Rightarrow
\text{persistent pressure-Hessian forcing}
}
\]

without a lower control on \(\gamma\).

## 12. Relation to M20-005

M20-005 derives

\[
D_t\gamma
=
-\gamma^2
+
|s_\perp|^2
-
\xi^TH_p\xi
+
\nu\xi^T\Delta S\,\xi
+
2v_\perp\cdot s_\perp.
\]

M20-006 supplies the complementary transverse law.

Together they separate the strain tensor relative to the vorticity axis into:

### longitudinal Rayleigh channel

\[
\gamma=\xi^TS\xi,
\]

### transverse projective channel

\[
s_\perp=P_\xi^\perp S\xi.
\]

Pressure also separates into:

\[
\xi^TH_p\xi
\]

and

\[
P_\xi^\perp H_p\xi.
\]

This is a complete longitudinal/transverse strain-pressure decomposition relative to the vorticity axis at first order.

## 13. Relation to earlier pressure-Hessian rotation audits

Earlier pressure-Hessian eigenaxis calculations already show that rapid strain-eigenaxis rotation must be paid by pressure-Hessian, vorticity leakage, or viscous derivative channels.

M20-006 is distinct in two ways:

1. no strain eigenvector is selected;
2. the observable is the coordinate-free vorticity-projector commutator \([S,Q]\).

Thus eigenvalue degeneracy does not create an artificial coordinate singularity.

## 14. Recurrence firewall

The M20 hard hull is recurrent in normalized/logarithmic variables.

M20-006 is a physical material-line identity.

A q-syndetic projective-strain event does **not** automatically imply that one material lineage returns syndetically to the same event.

Therefore one must not average

\[
D_t|s_\perp|^2
\]

to zero merely from q-recurrence.

This blocks a premature conclusion such as

\[
\langle\gamma|s_\perp|^2\rangle
=
-\frac12
\langle s_\perp\cdot H_p\xi\rangle+\cdots.
\]

A lineage/transport realization theorem would be needed first.

## 15. Updated strain branch

The M20 strain-eigenframe branch now refines to the signed alternatives

\[
\boxed{
S_{\rm eig}
\Longrightarrow
S_{\gamma^-}
\lor
P_{\rm off}
\lor
D_S
\lor
V_{S\xi}
\lor
R_{\rm material},
}
\]

where:

- \(S_{\gamma^-}\): compressive directional-strain phases replenish projective misalignment;
- \(P_{\rm off}\): transverse pressure-Hessian commutator correlation;
- \(D_S\): strain-diffusion derivative activity;
- \(V_{S\xi}\): viscous projective coupling;
- \(R_{\rm material}\): missing same-lineage realization needed to convert q-recurrence into material recurrence.

This is a structural split, not yet an exhaustive quantitative lower-bound theorem without additional localization.

## 16. Next target

The clean new quantity is

\[
\boxed{
\langle[S,Q],[H_p,Q]\rangle_F.
}
\]

M20-007 should test the pressure Poisson representation to determine whether this transverse projective pressure correlation is:

1. an independent nonlocal channel;
2. controlled by existing vorticity/strain projective covariance;
3. or another exactly critical Calderon--Zygmund firewall.

That calculation should avoid estimating the full pressure Hessian when only its off-axis commutator component is relevant.

\[
\boxed{\text{M20-006 COMPLETE; PROJECTIVE STRAIN NONCOMMUTATION HAS AN EXACT SIGNED TRANSVERSE-PRESSURE COMPENSATION LAW.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
