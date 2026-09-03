# DSD M17-024 — A slanted regular nodal filament has frozen azimuth and an exact slope-strain law

Date: 2026-09-03
Canonical ID: **M17-024**

Status: **INTERNAL SLANTED-CORE KINEMATICS / AT A REGULAR GREAT-CIRCLE NODAL FILAMENT THE JACOBIAN `G=grad W` HAS RANK TWO AND ITS KERNEL IS THE FILAMENT TANGENT. WHEN THE HORIZONTAL BLOCK `G_h` IS INVERTIBLE, THE NONVERTICAL SLOPE VECTOR `p=tau_h/tau_3` IS EXACTLY `p=-G_h^{-1}G_3`. M17-010 GIVES `D_B G_h=(kappa-3/2)G_h` AND `D_B G_3=(3lambda+kappa-3/2)G_3`, SO `D_B p=3lambda p`. HENCE THE HORIZONTAL AZIMUTH `p/|p|` IS MATERIAL INVARIANT, WHILE THE INCLINATION MAGNITUDE OBEYS `D_B log|p|=3lambda`. A UNIFORMLY RECURRENT GENUINELY SLANTED FILAMENT THEREFORE REQUIRES ZERO MEAN LAMBDA, REPRODUCING M17-010 FROM PURE TANGENT KINEMATICS, AND ITS SLANT DIRECTION CANNOT ROTATE WITHOUT LEAVING THE REGULAR HORIZONTAL-JACOBIAN BRANCH. THE NORMALIZED NODAL SHAPE AND SLANT AZIMUTH FORM A RIGID MATERIAL CORE FRAME / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Kernel of the nodal Jacobian

At a regular codimension-two nodal filament,

\[
W=0,
\qquad
\operatorname{rank}\nabla W=2.
\]

Let

\[
\tau=(\tau_h,\tau_3)
\]

be a nonzero tangent vector to the filament.
Because `W` remains zero along the filament,

\[
\boxed{
G\tau=0,
\qquad
G:=\nabla W.
}
\]

In the great-circle frame `W=(W_1,W_2,0)`, write

\[
G=(G_h\mid G_3),
\]

where `G_h` is the `2x2` horizontal block and `G_3` is the vertical-derivative column.
Then

\[
\boxed{
G_h\tau_h+G_3\tau_3=0.
}
\]

---

## 2. Slanted slope vector

On the M17-010 uniformly regular branch assume

\[
\det G_h\ne0.
\]

For a nonhorizontal tangent with

\[
\tau_3\ne0,
\]

define the horizontal slope vector

\[
\boxed{
p:=\frac{\tau_h}{\tau_3}.}
\]

The kernel equation gives

\[
\boxed{
p=-G_h^{-1}G_3.}
\]

Thus the filament slope is encoded entirely by the nodal Jacobian columns.

In streamfunction variables,

\[
G_h=JQ,
\qquad
G_3=Jc,
\]

with

\[
Q=\nabla_h^2q,
\qquad
c=\nabla_hq_3.
\]

Hence equivalently

\[
\boxed{
p=-Q^{-1}c.}
\]

This is the critical-point continuation law for a slanted nodal filament.

---

## 3. Use the M17-010 column multiplier laws

M17-010 gives at the regular nodal core

\[
\boxed{
D_BG_h
=\left(\kappa-\frac32\right)G_h,
}
\]

and

\[
\boxed{
D_BG_3
=\left(3\lambda+\kappa-\frac32\right)G_3.
}
\]

Differentiate

\[
p=-G_h^{-1}G_3.
\]

Using

\[
D_B(G_h^{-1})
=-G_h^{-1}(D_BG_h)G_h^{-1},
\]

we obtain

\[
\begin{aligned}
D_Bp
&=
-G_h^{-1}(D_BG_3)
+G_h^{-1}(D_BG_h)G_h^{-1}G_3\\
&=
-\left(3\lambda+\kappa-\frac32\right)G_h^{-1}G_3
+\left(\kappa-\frac32\right)G_h^{-1}G_3.
\end{aligned}
\]

Since

\[
G_h^{-1}G_3=-p,
\]

we obtain the exact slope law

\[
\boxed{
D_Bp=3\lambda p.
}
\]

---

## 4. Frozen slant azimuth

Whenever `p != 0`, define its horizontal direction

\[
\widehat p:=\frac p{|p|}.
\]

Because the evolution of `p` is a scalar multiplier,

\[
\boxed{
D_B\widehat p=0.
}
\]

Thus a marked regular slanted filament cannot rotate its horizontal slant azimuth while remaining in the M17-010 branch.

Only its inclination magnitude changes.

---

## 5. Inclination amplitude

Taking the logarithmic norm,

\[
\boxed{
D_B\log|p|=3\lambda.
}
\]

Therefore

\[
\boxed{
|p(\theta)|
=|p(\theta_0)|
\exp\left(
3\int_{\theta_0}^{\theta}\lambda(\tau)d\tau
\right).
}
\]

If `alpha` is the angle of the tangent away from the vertical, then

\[
|p|=\tan\alpha,
\]

so

\[
\boxed{
D_B\log\tan\alpha=3\lambda.
}
\]

---

## 6. Recurrent slanted filament forces mean lambda = 0

Suppose the marked filament is uniformly genuinely slanted:

\[
0<c_p\le|p(\theta)|\le C_p<\infty
\]

along the recurrent branch.
Then the long-time logarithmic drift of `|p|` vanishes, so

\[
\boxed{
\langle\lambda\rangle_{slanted}=0.
}
\]

This reproduces the M17-010 slanted-column conclusion by an independent geometric route.

The agreement is an internal audit of the nodal Jacobian dynamics.

---

## 7. Alignment exits

The exact solution shows the two possible asymptotic alignment limits if the integrated strain develops a one-sided drift:

### Positive mean lambda

\[
\int\lambda\to+\infty
\Longrightarrow
|p|\to\infty,
\]

so the tangent becomes increasingly horizontal.

### Negative mean lambda

\[
\int\lambda\to-\infty
\Longrightarrow
|p|\to0,
\]

so the tangent approaches the vertical class.

Thus a persistently slanted recurrent filament cannot carry a nonzero mean repeated-plane strain.

---

## 8. Rigid material core frame

M17-014 gives the material invariance of the normalized horizontal Jacobian shape

\[
\widehat C
=\frac{G_h^TG_h}{|\det G_h|}.
\]

M17-024 adds

\[
D_B\widehat p=0.
\]

Hence the pair

\[
\boxed{
(\widehat C,\widehat p)
}
\]

is a material invariant of a regular slanted filament.

In particular, the angle between the slant azimuth and the principal directions of the normalized nodal shape is frozen.

The core may change amplitude, but not its normalized horizontal shape-orientation data.

---

## 9. Streamfunction interpretation

Since

\[
p=-Q^{-1}c,
\]

we have

\[
\boxed{
c=-Qp.}
\]

Thus axial variation of the horizontal critical point is not independent.
It is determined by

1. the horizontal Hessian `Q`;
2. the frozen slant vector `p`.

Because normalized `Q` and the direction of `p` are frozen, the slanted critical-point geometry has fewer independent degrees of freedom than a generic moving critical curve.

---

## 10. DSD interpretation

### 10.1 Kernel descriptor
The filament tangent is not introduced as an external geometric variable; it is reconstructed from the nullspace of the vorticity Jacobian.

### 10.2 Amplitude vs orientation
The same scalar multiplier structure that froze the nodal shape now freezes the slant azimuth.
`lambda` controls only the relative horizontal/vertical amplitude.

### 10.3 Cross-audit
The independently obtained mean condition

\[
\langle\lambda\rangle=0
\]

matches M17-010 and strengthens confidence that the slanted recurrence constraint is not an artifact of one chosen descriptor.

---

## 11. DSD audit

### Audit A — horizontal tangent
The representation `p=tau_h/tau_3` excludes `tau_3=0`.
A purely horizontal filament is a separate chart/branch.

### Audit B — singular horizontal Jacobian
The formula `p=-G_h^{-1}G_3` uses `det G_h != 0`.
Loss of this condition is nodal rank/coordinate degeneration and remains a separate exit.

### Audit C — frozen azimuth means globally straight filament
Rejected.
The statement is along a marked material filament point in time; spatial variation of tangent along the filament is not excluded.

### Audit D — mean lambda zero means lambda pointwise zero
Rejected.
Only recurrent mean/logarithmic drift is constrained.

### Audit E — proof status
No contradiction is obtained.

---

## 12. Updated slanted branch

The genuinely slanted regular branch obeys

\[
\boxed{
\begin{aligned}
p&=-G_h^{-1}G_3,\\
D_Bp&=3\lambda p,\\
D_B\widehat p&=0,\\
\langle\lambda\rangle&=0
\quad\text{under uniform recurrent slant}.
\end{aligned}
}
\]

Together with M17-014,

\[
\boxed{
D_B(\widehat C,\widehat p)=0.
}
\]

---

## 13. Next target — tangent-covariant core compatibility

M17-015's vertical identity

\[
(G_q-1)Q=\lambda_3I
\]

cannot be copied unchanged to a slanted filament because differentiation along the filament contains horizontal motion.

The next calculation is to derive the tangent-covariant replacement and determine precisely what extra tensor channel allows a slanted non-axisymmetric core to evade the vertical conclusion `G_q=1`.

This is the **Slanted Core Compatibility Gate (SCCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
