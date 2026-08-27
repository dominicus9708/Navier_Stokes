# DSD M5-168 — Exact Co-Moving Fuchsian Vorticity Fast–Slow System

Date: 2026-08-27

Status: **P1_B^S EXACT AXIS REFACTOR / THE FIXED-TIME INVERSE-RADIUS VORTICITY EQUATION IS REWRITTEN IN `z=e^-tau` AND PHYSICAL-GENEALOGICAL COORDINATE `q=s+log z` AS A COMPACT FUCHSIAN OPERATOR `4nu D^2+6nu D+partial_z+nu(2+Delta)` WITH `D=z partial_z+partial_q` / DEFINING THE FAST DEFECT `R=z F_z` PRODUCES AN EXACT FIRST-ORDER FAST EQUATION COUPLED TO THE SLOW RECONSTRUCTION `F_z=R/z` / THIS IS THE PREFERRED FORM FOR THE REMAINING DIRICHLET-QUOTIENT COMPATIBILITY AUDIT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Starting equation

M5-153 gives the exact fixed-Leray-time inverse-radius relative-vorticity equation

\[
0=
4\nu K_{\xi\xi}
-\left(1+\frac{2\nu}{\xi}\right)K_\xi
-\frac1\xi K_s
+\frac\nu{\xi^2}(2+\Delta_{S^2})K
-\frac1{\xi^2}\mathcal N_s[K].
\]

Set

\[
\boxed{z:=\xi^{-1}=e^{-\tau}}
\]

and introduce

\[
\boxed{q:=s+\log z=s-\tau.}
\]

Write

\[
F(z,q,\theta):=K(\xi,s,\theta).
\]

At fixed `s`,

\[
\partial_z|_s
=
\partial_z|_q
+\frac1z\partial_q.
\]

---

## 2. Exact transformed equation

A direct calculation gives

\[
\boxed{
\begin{aligned}
0={}&
4\nu z^2F_{zz}
+8\nu zF_{zq}
+(1+10\nu z)F_z\\
&+4\nu F_{qq}
+6\nu F_q
+\nu(2+\Delta_{S^2})F
-z\mathcal N[F].
\end{aligned}
}
\]

No asymptotic truncation is used.

---

## 3. Compact covariant-normal operator

Define

\[
\boxed{D:=z\partial_z+\partial_q.}
\]

Then

\[
D^2F
=
z^2F_{zz}
+zF_z
+2zF_{zq}
+F_{qq}.
\]

Therefore

\[
4\nu D^2F
+6\nu DF
+F_z
\]

has exactly the normal/genealogical derivative coefficients in Section 2.

Hence the full equation becomes

\[
\boxed{
4\nu D^2F
+6\nu DF
+F_z
+\nu(2+\Delta_{S^2})F
-z\mathcal N[F]
=0.
}
\]

This is the preferred exact co-moving Fuchsian vorticity equation.

---

## 4. Fast defect variable

Since

\[
DF=zF_z+F_q,
\]

define

\[
\boxed{R:=DF-F_q=zF_z.}
\]

Thus the slow field is reconstructed from

\[
\boxed{F_z=\frac Rz.}
\]

The flat boundary gives

\[
F=O(z^N),\qquad R=O(z^N)
\]

for every finite `N` in the audited same-tail Hilbert topology.

---

## 5. Exact fast equation

Let `G:=partial_q`, interpreted on the invariant pair Hilbert space as the skew-adjoint pair-flow generator.

Using

\[
DF=GF+R
\]

and

\[
D(GF+R)
=
G^2F+2GR+zR_z,
\]

the compact equation yields

\[
\boxed{
4\nu zR_z
+\left(\frac1z+6\nu+8\nu G\right)R
=
LF
+z\mathcal N[F],
}
\]

where

\[
\boxed{
L:=
-4\nu G^2
-6\nu G
-\nu(2+\Delta_{S^2}).
}
\]

Equivalently, defining the positive self-adjoint second-order cross operator

\[
A_0:=-4G^2-\Delta_{S^2}\ge0,
\]

we may write

\[
L
=
\nu A_0
-6\nu G
-2\nu I.
\]

Thus `L` has

- positive self-adjoint second-order part `nu A_0` in the backward-`z` orientation;
- skew first-order drift `-6nu G`;
- harmless zeroth-order shift.

---

## 6. Fast-normal structure

The leading fast equation is

\[
4\nu zR_z+\frac1zR\approx LF.
\]

The homogeneous branch satisfies

\[
R_z+\frac1{4\nu z^2}R=0,
\]

hence

\[
R_{hom}\sim e^{1/(4\nu z)}.
\]

This is exactly the explosive fast normal mode already excluded by M5-146/M5-160.

The flat-selected branch is therefore the stable particular branch with `R` slaved to the cross-section operator applied to `F`.

At formal leading order,

\[
R\sim zLF,
\qquad
F_z\sim LF,
\]

which is the backward-parabolic slow equation underlying M5-166.

---

## 7. Exact fast energy identity

Take the real `H` inner product of the fast equation with `R` and use skew-adjointness of `G`:

\[
\operatorname{Re}\langle GR,R\rangle=0.
\]

Then

\[
\boxed{
2\nu z\frac d{dz}\|R\|^2
+
\left(\frac1z+6\nu\right)\|R\|^2
=
\operatorname{Re}\langle LF,R\rangle
+z\operatorname{Re}\langle\mathcal N[F],R\rangle.
}
\]

The singular positive coefficient

\[
\boxed{z^{-1}\|R\|^2}
\]

is the exact fast-normal coercivity available for the compatibility audit.

---

## 8. Why this form is preferable to a frozen asymptotic expansion

M5-167 proves monotone damping of every frozen stable principal mode.

M5-168 provides the exact nonautonomous equation behind that result.  The change `a(τ)=e^-τ` is no longer an implicit adiabatic error; it is represented explicitly by the singular coefficient `1/z` and the small nonlinear factor `z`.

Thus the remaining task can be posed without freezing `a`:

\[
\boxed{
\text{combine the fast coercive identity with a Dirichlet quotient for }F
\text{ and prove that frequency cannot escape to infinity as }z\downarrow0.
}
\]

---

## 9. DSD four-chain audit

### Formation — GREEN

The equation is an exact reparameterization of M5-153.

### Axis — GREEN

`z` is normal terminal depth and `q` is the co-moving genealogical/physical-log-radius axis. Their derivative roles are explicit in `D`.

### Static aggregation — GREEN

The fast variable `R` is not a new independent field; it is exactly `z F_z`.

### Dynamics — GREEN

The explosive homogeneous fast branch is the already-audited rejected branch; the remaining flat solution lies on the stable particular branch.

### Cross-audit — GREEN

The compact equation reproduces both the M5-153 fixed-time identity and the M5-160/M5-167 fast-slow interpretation.

---

## 10. Next compatibility calculation

The remaining M5-166 YELLOW edge is now:

1. use the `z^-1 ||R||^2` fast coercivity to control deviation from `R=zLF`;
2. derive the Dirichlet-quotient/log-convexity inequality for the slow field `F` directly from the exact `(F,R)` system;
3. compare the resulting bounded-frequency conclusion with the M5-154 necessary parabolic frequency escape.

No Gaussian spectral assumption is required in this formulation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
