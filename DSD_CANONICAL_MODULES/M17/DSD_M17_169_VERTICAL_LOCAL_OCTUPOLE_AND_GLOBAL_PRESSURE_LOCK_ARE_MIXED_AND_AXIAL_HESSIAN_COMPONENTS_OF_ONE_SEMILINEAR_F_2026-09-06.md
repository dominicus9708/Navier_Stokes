# DSD M17-169 — The vertical local octupole and global axial pressure lock are mixed and axial Hessian components of the same semilinear `F(q,x_3,theta)`

Date: 2026-09-06  
Canonical ID: **M17-169**

Status: **SEMILINEAR HESSIAN UNIFICATION / IN THE VERTICAL GREAT-CIRCLE BRANCH USE THE NODAL GAUGE `q(0,0,x_3,theta)=0`. THEN ALL PURE AXIAL DERIVATIVES OF `q` VANISH ON THE FILAMENT. THE KINEMATIC IDENTITIES `lambda_h=(1/2)Delta_h phi=-(1/2)partial_3 U_3`, `curl W=-Delta U`, AND `W_h=J grad_h q` GIVE `H_V=mathcal H_333=partial_33 Delta_h q`. WITH `Delta q=F(q,x_3,theta)` THIS REDUCES EXACTLY TO `H_V=F_33` ON THE FILAMENT. SIMULTANEOUSLY `kappa=F_q` GIVES AT A REGULAR CROSSING `kappa_3=F_q3`, SO `O_V=-(1/5)|Q|_F^2 F_q3`. HENCE THE OLD LOCAL/GLOBAL COVARIANCE IS THE RELATION BETWEEN THE MIXED AND AXIAL ENTRIES OF THE TWO-VARIABLE HESSIAN OF ONE SCALAR SEMILINEAR FUNCTION. IF `F_qq != 0` AND `q_*(x_3)` IS THE LOCAL ROOT OF `F_q=0`, THE CRITICAL-VALUE CURVATURE `C_*(x_3)=F(q_*(x_3),x_3)` SATISFIES `C_*''=F_33-F_q3^2/F_qq`. THEREFORE `H_V=C_*''+25 O_V^2/(|Q|_F^4 F_qq)`. THIS CREATES AN UNSIGNED SQUARE BRIDGE FROM THE M5-BIASED LOCAL OCTUPOLE TO THE GLOBAL PRESSURE STATE, AT THE PRICE OF A ROOT-CURVATURE SIGN/DEGENERACY BRANCH AND A CRITICAL-VALUE-CURVATURE COMPENSATOR. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vertical nodal gauge

Use the vertical great-circle representation

\[
W_h=J\nabla_hq,
\qquad
q=U_3-\partial_3\phi.
\]

The streamfunction has an `x_3,theta`-dependent gauge freedom.
Choose the nodal gauge

\[
\boxed{
q(0,0,x_3,\theta)=0
}
\]

along the entire regular vertical filament.

Consequently on the filament

\[
\boxed{
q_3=q_{33}=q_{333}=q_{3333}=\cdots=0.
}
\]

This is a gauge-fixed statement; physical quantities derived below are gauge invariant after the gauge is fixed consistently.

---

## 2. Horizontal strain trace and vertical velocity

Since

\[
U_h=\nabla_h\phi,
\]

incompressibility gives

\[
\Delta_h\phi+\partial_3U_3=0.
\]

Define

\[
\lambda_h:=\frac12(\Sigma_{11}+\Sigma_{22})
=\frac12\Delta_h\phi.
\]

Therefore

\[
\boxed{
\lambda_h=-\frac12\partial_3U_3.
}
\]

Hence

\[
\boxed{
\partial_3\lambda_h
=-\frac12\partial_{33}U_3.
}
\]

---

## 3. Rewrite the vertical viscous scalar by `q`

M17-082 defines

\[
V_V:=\Delta(\partial_3\lambda_h).
\]

Using Section 2,

\[
V_V
=-\frac12\partial_{33}\Delta U_3.
\]

For the present convention `q=U_3-phi_3`, direct curl computation gives

\[
W=(q_2,-q_1,0).
\]

Since

\[
\nabla\times W
=-\Delta U
\]

for incompressible `U`, the third component gives

\[
-\Delta_hq=-\Delta U_3.
\]

Thus

\[
\boxed{
\Delta U_3=\Delta_hq.
}
\]

Therefore

\[
\boxed{
V_V=-\frac12\partial_{33}\Delta_hq.
}
\]

M17-082 gives `H_V=-2V_V`, so

\[
\boxed{
H_V:=\mathcal H_{333}
=\partial_{33}\Delta_hq.
}
\]

---

## 4. Insert the semilinear equation

On the great-circle branch

\[
\boxed{
\Delta q=F(q,x_3,\theta).
}
\]

Thus

\[
\Delta_hq
=F(q,x_3,\theta)-q_{33}.
\]

Take two axial derivatives and restrict to the nodal filament.
The gauge gives

\[
q_3=q_{33}=q_{333}=q_{3333}=0.
\]

Therefore the total axial derivatives of `F` reduce to partial derivatives at fixed `q`:

\[
\partial_{33}F(q(x_3),x_3,\theta)
=F_{33}
\]

on the filament.
Hence

\[
\boxed{
H_V=F_{33}.
}
\]

This is an exact local representation of the global pressure coordinate forced by M17-082.

---

## 5. Local octupole is the mixed Hessian component

The multiplier is

\[
\boxed{\kappa=F_q.}
\]

Differentiate axially along the filament:

\[
\kappa_3
=F_{qq}q_3+F_{q3}.
\]

The nodal gauge gives `q_3=0`, so

\[
\boxed{
\kappa_3=F_{q3}.
}
\]

At a regular `kappa=0` crossing M17-090 gives

\[
O_V=-\frac15|Q|_F^2\kappa_3.
\]

Therefore

\[
\boxed{
O_V
=-\frac15|Q|_F^2F_{q3}.
}
\]

Thus the old local/global pair is

\[
\boxed{
O_V\ \leftrightarrow\ F_{q3},
\qquad
H_V\ \leftrightarrow\ F_{33}.
}
\]

They are entries of the same Hessian

\[
\nabla^2_{(q,x_3)}F
=\begin{pmatrix}
F_{qq}&F_{q3}\\
F_{q3}&F_{33}
\end{pmatrix}.
\]

---

## 6. The kappa-zero root and its slope

At the crossing,

\[
F_q=\kappa=0.
\]

Assume the root is nondegenerate in the `q` direction:

\[
\boxed{F_{qq}\neq0.}
\]

Then by the implicit function theorem there is a local root

\[
q=q_*(x_3,\theta)
\]

satisfying

\[
F_q(q_*(x_3),x_3,\theta)=0.
\]

Differentiate:

\[
F_{qq}q_{*,3}+F_{q3}=0.
\]

Hence

\[
\boxed{
q_{*,3}
=-\frac{F_{q3}}{F_{qq}}.
}
\]

This is the semilinear form of the root-slope relation already used in M17-091.

---

## 7. Critical-value curvature identity

Define the critical value of `F` along the kappa-zero root:

\[
\boxed{
\mathcal C_*(x_3,\theta)
:=F(q_*(x_3,\theta),x_3,\theta).
}
\]

Because `F_q=0` on the root,

\[
\mathcal C_{*,3}=F_3.
\]

Differentiate once more:

\[
\mathcal C_{*,33}
=F_{33}+F_{3q}q_{*,3}.
\]

Using symmetry `F_{3q}=F_{q3}` and Section 6,

\[
\boxed{
\mathcal C_{*,33}
=F_{33}-\frac{F_{q3}^2}{F_{qq}}.
}
\]

Therefore

\[
\boxed{
F_{33}
=\mathcal C_{*,33}
+\frac{F_{q3}^2}{F_{qq}}.
}
\]

---

## 8. Exact local/global square bridge

Substitute

\[
H_V=F_{33}
\]

and

\[
F_{q3}=-\frac{5O_V}{|Q|_F^2}.
\]

Then

\[
\boxed{
H_V
=\mathcal C_{*,33}
+\frac{25O_V^2}{|Q|_F^4F_{qq}}.
}
\]

Equivalently,

\[
\boxed{
H_V-\mathcal C_{*,33}
=\frac{25O_V^2}{|Q|_F^4F_{qq}}.
}
\]

This is an exact algebraic local/global pressure relation on the nondegenerate root branch.

---

## 9. New branch split

The square bridge produces the exact alternatives:

1. `F_qq -> 0` or changes sign — **root-curvature degeneration/turnover**;
2. `C_{*,33}` supplies the compensating axial curvature;
3. the global pressure coordinate `H_V` inherits a signed contribution with sign `sgn(F_qq)` and magnitude proportional to `O_V^2`.

Thus

\[
\boxed{
R_{1,V}^{cross}
\Longrightarrow
G_{F_{qq}\text{-deg/sign}}
\lor
G_{critical-value\ curvature}
\lor
G_{pressure\ square}.
}
\]

---

## 10. Compact nondegenerate consequence

If on a recurrent crossing subbranch

\[
0<c_F\le |F_{qq}|\le C_F,
\]

and `F_qq` has fixed sign, then

\[
\boxed{
|H_V-\mathcal C_{*,33}|
\ge
\frac{25}{C_F}
\frac{O_V^2}{|Q|_F^4}.
}
\]

Thus a nonzero local octupole forces a nonzero unsigned separation between the global pressure coordinate and the critical-value curvature.

This removes the relative-speed sign from this part of the bridge.

---

## 11. DSD audit

### Audit A — sign convention for `Delta U_3`
The derivation explicitly uses `q=U_3-phi_3`, giving `W=(q_2,-q_1,0)` and hence `Delta U_3=Delta_h q`.

### Audit B — using the nodal gauge without stating it
The identities `H_V=F_33` and `kappa_3=F_q3` are written in the gauge `q=0` along the filament. Physical `H_V`, `kappa_3`, and `O_V` remain gauge invariant.

### Audit C — using the root formula when `F_qq=0`
Rejected. `F_qq=0` is a separate root-degeneracy branch.

### Audit D — assigning a sign to the square term without fixing `F_qq`
Rejected. Its sign is `sgn(F_qq)`.

### Audit E — assuming the critical-value curvature vanishes
Rejected. `C_{*,33}` is a genuine compensator and must be separately controlled.

### Audit F — proof status
The local/global covariance is reduced to a single semilinear Hessian identity but is not closed.

---

## 12. Updated vertical Rank-1 gate

At a nondegenerate regular kappa-zero root,

\[
\boxed{
H_V
=\mathcal C_{*,33}
+\frac{25O_V^2}{|Q|_F^4F_{qq}}.
}
\]

The next target is to combine the strictly biased M5 crossing ensemble with this square relation. A quantitative M5 bias plus bounded `r_V`, `Q`, and `F_qq` forces a positive crossing-average of `O_V^2`; hence either root-curvature sign/degeneration or critical-value curvature must compensate a definite pressure-square contribution.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
