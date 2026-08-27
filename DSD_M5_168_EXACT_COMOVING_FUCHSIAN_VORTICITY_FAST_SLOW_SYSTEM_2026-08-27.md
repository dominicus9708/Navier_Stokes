# DSD M5-168 — Exact Co-Moving Fuchsian Vorticity Fast–Slow System

Date: 2026-08-27

Status: **CORRECTED EXACT AXIS REFACTOR / THE CO-MOVING FUCHSIAN VORTICITY EQUATION IS `4nu D^2 F + 6nu D F + F_z + nu(2+Delta)F - N[F]=0` WITH NO EXTRA `z` IN FRONT OF THE RELATIVE NONLINEAR OPERATOR / THE FAST DEFECT `R=zF_z` OBEYS AN EXACT FIRST-ORDER EQUATION WITH SOURCE `LF+N[F]` / THIS CORRECTION RESTORES EXACT AGREEMENT WITH M5-153/M5-154 / GLOBAL REGULARITY UNPROVED.**

---

## 1. Correction note

The first version of M5-168 incorrectly carried an extra factor `z` in front of the scaled relative transport/stretching term after the `(xi,s)->(z,q)` change of variables.

The mistake came from transforming the equation after division by `xi` and then losing one common factor `z` in the derivative terms.

Re-deriving from the original undivided M5-153 equation gives the corrected system below.

This correction also changes the source in M5-169 and the relative-coupling scale in M5-170.

---

## 2. Starting equation

M5-153 gives

\[
K_s+\xi K_\xi
-4\nu\xi K_{\xi\xi}
+2\nu K_\xi
-\frac\nu\xi(2+\Delta_{S^2})K
+\frac1\xi\mathcal N_s[K]=0.
\]

Set

\[
z:=\xi^{-1}=e^{-\tau},
\qquad
q:=s+\log z=s-\tau,
\]

and write

\[
F(z,q,\theta):=K(\xi,s,\theta).
\]

Define

\[
\boxed{D:=z\partial_z+\partial_q.}
\]

Since the fixed-`s` logarithmic radial derivative equals `-D`, direct substitution gives the exact corrected equation

\[
\boxed{
4\nu D^2F
+6\nu DF
+F_z
+\nu(2+\Delta_{S^2})F
-\mathcal N[F]
=0.
}
\]

There is **no factor `z` multiplying `N[F]`** in this `z`-equation.

Equivalently, returning to `tau=-log z`, the nonlinear term in the forward `tau` equation carries the expected factor `e^-tau=z`, in agreement with M5-154.

---

## 3. Expanded form

Using

\[
D^2F
=z^2F_{zz}+zF_z+2zF_{zq}+F_{qq},
\]

the corrected equation is

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
-\mathcal N[F].
\end{aligned}
}
\]

---

## 4. Fast defect

Set

\[
G:=\partial_q
\]

on the invariant pair Hilbert space and define

\[
\boxed{R:=DF-GF=zF_z.}
\]

Thus

\[
\boxed{F_z=R/z.}
\]

Also

\[
DF=GF+R,
\qquad
D(GF+R)=G^2F+2GR+zR_z.
\]

Insert these into the corrected compact equation.

---

## 5. Exact corrected fast equation

Define

\[
\boxed{
L:=-4\nu G^2-6\nu G-\nu(2+\Delta_{S^2}).
}
\]

Equivalently, with

\[
A_0:=-4G^2-\Delta_{S^2}\ge0,
\]

\[
L=\nu A_0-6\nu G-2\nu I.
\]

The fast equation is

\[
\boxed{
4\nu zR_z
+\left(\frac1z+6\nu+8\nu G\right)R
=
LF+\mathcal N[F].
}
\]

The source is `LF+N[F]`, not `LF+zN[F]`.

---

## 6. Fast-normal structure

The leading homogeneous equation remains

\[
4\nu zR_z+\frac1zR=0,
\]

so

\[
R_{hom}\sim e^{1/(4\nu z)}.
\]

The flat branch excludes this mode exactly as before.

On the stable particular branch, formally,

\[
R\sim z(LF+\mathcal N[F]),
\]

hence

\[
\boxed{
F_z\sim LF+\mathcal N[F].
}
\]

Consequently, in forward `tau=-log z`,

\[
F_\tau=-zF_z
\sim
-z(LF+\mathcal N[F]),
\]

which reproduces the M5-154 `e^-tau` scaling of both cross-section viscosity and relative transport/stretching.

---

## 7. Exact fast energy identity

Taking the real inner product with `R` and using skew-adjointness of `G` gives

\[
\boxed{
2\nu z\frac d{dz}\|R\|^2
+\left(\frac1z+6\nu\right)\|R\|^2
=
\operatorname{Re}\langle LF+\mathcal N[F],R\rangle.
}
\]

Thus the singular positive fast coercivity

\[
z^{-1}\|R\|^2
\]

is unchanged.

---

## 8. DSD cross-audit

### Formation — GREEN after correction

The corrected equation is obtained directly from the undivided M5-153 equation.

### Axis — GREEN

`z`, `q`, and the pair-flow generator remain separated.

### Static aggregation — GREEN

The scaling of `N[F]` is now consistent across M5-153, M5-154, and M5-168.

### Dynamics — GREEN

The forward `tau` coupling has the expected integrable factor `z=e^-tau`.

### Error status

The earlier extra-`z` version is **REJECTED** and must not be used downstream.

M5-169 and M5-170 are corrected accordingly.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
