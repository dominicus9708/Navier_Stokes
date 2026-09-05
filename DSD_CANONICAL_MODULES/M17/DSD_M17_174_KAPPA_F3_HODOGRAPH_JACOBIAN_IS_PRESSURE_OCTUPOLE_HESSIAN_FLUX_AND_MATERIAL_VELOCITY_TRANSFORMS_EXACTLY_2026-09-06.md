# DSD M17-174 — The `(kappa,F_3)` hodograph Jacobian is the pressure–octupole Hessian flux, and material label velocity transforms exactly through it

Date: 2026-09-06  
Canonical ID: **M17-174**

Status: **HODOGRAPH REDUCTION / THE MAP `Xi:(q,x_3)->(kappa,F_3)=(F_q,F_3)` HAS JACOBIAN MATRIX `D Xi = Hess_(q,3) F`. ITS DETERMINANT IS `F_qq F_33-F_q3^2=F_qq H_V-25O_V^2/|Q|^4`, EXACTLY THE NUMERATOR OF THE M17-170/173 PRESSURE-OCTUPOLE HESSIAN NORMAL FLUX. THE REDUCED MATERIAL VELOCITY `V_L=(H,K)` TRANSFORMS BY THE SAME HESSIAN: `(h-kappa_theta, D_L F_3-F_3theta)^T = Hess F (H,K)^T`. THUS, WHERE `det Hess F !=0`, `(kappa,F_3)` ARE LEGITIMATE LOCAL HODOGRAPH COORDINATES AND THE ZERO-WORLDSHEET BECOMES THE FLAT PLANE `kappa=0`; THE M5 NORMAL CROSSING SPEED IS THE FIRST HODOGRAPH VELOCITY COMPONENT WHILE THE SECOND COMPONENT IS MATERIAL TRANSPORT ALONG THE AXIAL-source coordinate. LOSS OF THIS COORDINATE SYSTEM IS EXACTLY THE ZERO OF THE PRESSURE-OCTUPOLE HESSIAN FLUX, NOT AN UNTYPED CHART FAILURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Define the hodograph map

At fixed `theta`, define

\[
\boxed{
\Xi_\theta(q,x_3)
:=(\kappa,F_3)
=(F_q,F_3).
}
\]

Its Jacobian matrix is

\[
D\Xi_\theta
=
\begin{pmatrix}
F_{qq}&F_{q3}\\
F_{q3}&F_{33}
\end{pmatrix}
=
\boxed{\nabla^2_{(q,3)}F.}
\]

Thus the semilinear Hessian is not merely an auxiliary matrix. It is the coordinate Jacobian from reduced labels to multiplier/source-slope variables.

---

## 2. Hodograph determinant

The Jacobian determinant is

\[
\boxed{
J_\Xi
:=\det D\Xi
=F_{qq}F_{33}-F_{q3}^2.
}
\]

At a vertical crossing, M17-169 gives

\[
F_{33}=H_V,
\qquad
F_{q3}=-\frac{5O_V}{|Q|_F^2}.
\]

Therefore

\[
\boxed{
J_\Xi
=F_{qq}H_V
-\frac{25O_V^2}{|Q|_F^4}.
}
\]

This is exactly the numerator of the M17-170/173 Hessian normal flux.

---

## 3. Relation to zero-curve tangential derivative

M17-171 gives

\[
\partial_sF_3
=\frac{J_\Xi}{|\nabla\kappa|}
\]

along an oriented regular `kappa=0` curve.
Hence

\[
\boxed{
J_\Xi
=|\nabla\kappa|\,\partial_sF_3.
}
\]

Thus hodograph degeneracy

\[
J_\Xi=0
\]

means precisely that `F_3` is stationary along the regular zero curve.

It does **not** require `grad kappa=0`.

---

## 4. Transform the material label velocity

The reduced material derivative is

\[
D_L
:=\partial_\theta
+\mathscr H\partial_q
+K\partial_3.
\]

For the multiplier,

\[
h=D_L\kappa.
\]

Therefore

\[
\boxed{
h-\kappa_\theta
=F_{qq}\mathscr H+F_{q3}K.}
\]

For `F_3`,

\[
D_LF_3-F_{3\theta}
=F_{q3}\mathscr H+F_{33}K.
\]

Hence

\[
\boxed{
\begin{pmatrix}
h-\kappa_\theta\\[1mm]
D_LF_3-F_{3\theta}
\end{pmatrix}
=
\begin{pmatrix}
F_{qq}&F_{q3}\\
F_{q3}&F_{33}
\end{pmatrix}
\begin{pmatrix}\mathscr H\\K\end{pmatrix}.
}
\]

Equivalently,

\[
\boxed{
\dot\Xi-\partial_\theta\Xi
=(D\Xi)V_L.
}
\]

This is the exact material hodograph law.

---

## 5. Nondegenerate hodograph branch

If

\[
\boxed{J_\Xi\neq0,}
\]

then the inverse function theorem makes `(kappa,F_3)` valid local coordinates.

The material label velocity can then be reconstructed:

\[
\boxed{
\begin{pmatrix}\mathscr H\\K\end{pmatrix}
=(\nabla^2F)^{-1}
\begin{pmatrix}
h-\kappa_\theta\\
D_LF_3-F_{3\theta}
\end{pmatrix}.
}
\]

Thus the two transformed velocity components are:

1. multiplier-level crossing velocity;
2. material transport of the axial source-slope coordinate.

The pressure/octet Hessian determinant controls whether these two coordinates resolve the original label velocity.

---

## 6. The zero set becomes a flat hodograph line

In `(kappa,F_3)` coordinates,

\[
\Gamma_0=\{\kappa=0\}
\]

is simply a coordinate line.

At fixed time the coordinate along that line is `F_3` whenever `J_Xi !=0`.

The M17-171 measure transformation follows directly:

\[
dF_3
=\partial_sF_3\,ds
=\frac{J_\Xi}{|\nabla\kappa|}ds.
\]

Thus on an orientation-preserving segment,

\[
\boxed{
\frac{ds}{|\nabla\kappa|}
=\frac{dF_3}{J_\Xi}.
}
\]

Absolute values may be used for unsigned coarea; signed formulas retain the orientation of `J_Xi`.

---

## 7. M5 crossing current in hodograph coordinates — conditional on M17-172

On the M17-172 pushforward branch,

\[
G_\Phi(0,\theta)
=\int_{\Gamma_0}
\frac{h w_\theta}{|\nabla\kappa|}ds.
\]

On a nondegenerate oriented hodograph segment,

\[
\boxed{
G_\Phi(0,\theta)
=\int
\frac{h\,w_\theta}{J_\Xi}\,dF_3
}
\]

with orientation understood.

Thus M5 hysteresis becomes a current in the source-slope coordinate `F_3`, weighted by the inverse pressure/octet hodograph Jacobian.

This is a direct same-coordinate coupling between the two previously separate ledgers.

---

## 8. Hodograph-degeneracy branch

If

\[
\boxed{J_\Xi=0}
\]

at a regular `kappa=0` point, then

\[
F_{qq}H_V
=\frac{25O_V^2}{|Q|_F^4}.
\]

This is a precise pressure/octet balance, not an unspecified chart failure.

Equivalently,

\[
\boxed{\partial_sF_3=0.}
\]

The zero curve remains regular if `grad kappa !=0`, but the second hodograph coordinate fails to distinguish neighboring points along it.

Hence the new branch split is

\[
\boxed{
\Gamma_0^{regular}
\Longrightarrow
G_{hod}^{nondegenerate}
\lor
G_{hod}^{J_\Xi=0}.
}
\]

---

## 9. Determinant form of the pressure-square relation

M17-169's graph formula

\[
H_V
=\mathcal C_{*,33}
+\frac{25O_V^2}{|Q|_F^4F_{qq}}
\]

is equivalent, when `F_qq !=0`, to

\[
\boxed{
J_\Xi=F_{qq}\mathcal C_{*,33}.
}
\]

Thus the critical-value curvature is the hodograph Jacobian normalized by root curvature.

M17-174 therefore unifies:

- Schur complement;
- zero-curve tangential derivative;
- Hessian current normal flux;
- local invertibility of `(kappa,F_3)` coordinates.

---

## 10. DSD audit

### Audit A — calling every `J_Xi=0` point a physical degeneration
Rejected. It is a hodograph-coordinate degeneration; the physical zero curve may remain regular.

### Audit B — dividing by `J_Xi` across a sign-changing segment
Rejected. Hodograph coordinates must be split into monotone nondegenerate charts.

### Audit C — dropping explicit time dependence
The transformed material velocity uses `h-kappa_theta` and `D_LF_3-F_3theta`; these are spatial-flow contributions. Full material derivatives retain explicit time terms.

### Audit D — using the M5 hodograph formula without M17-172
Rejected. The M5 measure pushforward remains conditional.

### Audit E — proof status
The flux covariance is geometrically unified, but no sign contradiction is obtained.

---

## 11. Updated next gate

On each nondegenerate hodograph chart,

\[
\boxed{
G_\Phi(0,\theta)
=\int\frac{h w_\theta}{J_\Xi}dF_3.
}
\]

The next question is whether recurrent negative M5 current can be maintained while `F_3` returns recurrently and `J_Xi` either stays uniformly away from zero or repeatedly crosses zero.

This creates two concrete subbranches:

1. **uniform hodograph branch** — control the signed inverse Jacobian current;
2. **hodograph-turnover branch** — quantify repeated `J_Xi=0` events, where the exact square balance `F_qqH_V=25O_V^2/|Q|^4` holds.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
