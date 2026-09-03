# DSD M17-014 — Normalized nodal-Jacobian shape is a material invariant and separates the axisymmetric core

Date: 2026-09-03
Canonical ID: **M17-014**

Status: **INTERNAL NON-AXISYMMETRIC GEOMETRY CLASSIFIER / M17-010 GIVES `D_B G_h=(kappa-3/2)G_h` ON A REGULAR WINDING NODAL FILAMENT. THEREFORE THE ENTIRE HORIZONTAL NODAL JACOBIAN CHANGES ONLY BY A SCALAR MULTIPLIER: ITS ORIENTATION CLASS, WINDING SIGN, SINGULAR-VALUE RATIO, AND NORMALIZED SHAPE TENSOR ARE MATERIAL INVARIANTS AS LONG AS THE FILAMENT REMAINS REGULAR. A SMOOTH AXISYMMETRIC NO-SWIRL CORE HAS `G_h=cJ`, SO ITS WINDING INDEX IS POSITIVE AND ITS TWO SINGULAR VALUES ARE EQUAL. CONSEQUENTLY ANY REGULAR FILAMENT WITH NEGATIVE INDEX OR UNEQUAL SINGULAR VALUES CANNOT CONTINUOUSLY ENTER THE AXISYMMETRIC FIREWALL WITHOUT RANK LOSS / NODAL DEGENERATION. THIS REMOVES AXISYMMETRIC REDUCTION AS AN ESCAPE FROM THE GENUINELY ANISOTROPIC REGULAR SUBBRANCH, BUT DOES NOT YET CONTRADICT A PERSISTENT NON-AXISYMMETRIC RECURRENT SURVIVOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-010

At a regular winding nodal filament, work in the fixed global great-circle frame

\[
W=(W_1,W_2,0).
\]

Let

\[
G_h
:=
\begin{pmatrix}
\partial_1W_1&\partial_2W_1\\
\partial_1W_2&\partial_2W_2
\end{pmatrix}
\]

be the horizontal-output / horizontal-input nodal Jacobian block.

M17-010 gives the exact material multiplier law

\[
\boxed{
D_BG_h
=
\left(\kappa-\frac32\right)G_h.
}
\]

Hence along the material filament

\[
\boxed{
G_h(\theta)
=
a_G(\theta)G_h(\theta_0),
}
\]

with

\[
a_G(\theta)
:=
\exp\left[
\int_{\theta_0}^{\theta}
\left(\kappa-\frac32\right)d\tau
\right]
>0.
\]

The multiplier is strictly positive.

---

## 2. Winding sign is invariant

Because

\[
\det G_h(\theta)
=
a_G(\theta)^2\det G_h(\theta_0),
\]

the determinant sign cannot change while the regular rank-two condition is maintained:

\[
\boxed{
\operatorname{sgn}\det G_h
=\text{constant along the material filament}.
}
\]

For a simple codimension-two zero, this sign is the local planar degree / winding index of the map

\[
(z_1,z_2)\mapsto(W_1,W_2)
\]

around the zero.

Thus the local winding orientation is materially frozen unless

\[
\det G_h=0,
\]

which is precisely a nodal-rank degeneration.

---

## 3. Singular-value ratio is invariant

Let the singular values of `G_h` be

\[
s_1\ge s_2>0.
\]

Scalar multiplication gives

\[
s_i(\theta)=a_G(\theta)s_i(\theta_0).
\]

Therefore

\[
\boxed{
\chi
:=
\frac{s_1}{s_2}
\ge1
}
\]

obeys

\[
\boxed{D_B\chi=0.}
\]

Thus the eccentricity of the first-order winding core is a material invariant.

---

## 4. Normalized shape tensor

Define

\[
C
:=
G_h^TG_h.
\]

Then

\[
D_BC
=2\left(\kappa-\frac32\right)C.
\]

Because

\[
\det C=(\det G_h)^2>0,
\]

define the determinant-normalized shape tensor

\[
\boxed{
\widehat C
:=
\frac{C}{\sqrt{\det C}}.
}
\]

It satisfies

\[
\det\widehat C=1.
\]

The common scalar multiplier cancels exactly, so

\[
\boxed{D_B\widehat C=0.}
\]

Equivalently, define the scalar anisotropy index

\[
\boxed{
\mathcal A
:=
\frac12\operatorname{tr}\widehat C
=
\frac12\left(\chi+\frac1\chi\right)
\ge1.
}
\]

Then

\[
\boxed{D_B\mathcal A=0.}
\]

Moreover,

\[
\boxed{
\mathcal A=1
\iff
s_1=s_2.
}
\]

Hence `A-1` is a clean local non-conformality descriptor of the regular nodal core.

---

## 5. Streamfunction interpretation

From M17-004,

\[
W_h=J\nabla_hq.
\]

At a nodal filament,

\[
\nabla_hq=0.
\]

Therefore

\[
G_h
=J\nabla_h^2q.
\]

Since `J` is orthogonal, `G_h` and the horizontal Hessian of `q` have the same singular values.
Thus

\[
\boxed{
\mathcal A
=\text{normalized anisotropy of the critical-point Hessian of }q.
}
\]

A regular winding filament is therefore a nondegenerate critical-point filament of the semilinear streamfunction, and its quadratic critical-point shape is materially frozen up to scale.

---

## 6. Axisymmetric no-swirl core

For a smooth axisymmetric no-swirl field near the symmetry axis,

\[
W=\omega_\theta(r,z)e_\theta.
\]

Smooth axis compatibility gives locally

\[
\omega_\theta(r,z)
=c(z)r+O(r^3).
\]

In Cartesian horizontal coordinates,

\[
e_\theta
=\frac1r(-y,x,0),
\]

so

\[
W_h
=c(z)(-y,x)+O(r^3).
\]

Therefore on the axis

\[
\boxed{
G_h
=c(z)
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
=c(z)J_0.
}
\]

Hence

\[
G_h^TG_h=c(z)^2I_2,
\]

and consequently

\[
\boxed{
\mathcal A_{axis}=1.
}
\]

Also

\[
\det G_h=c(z)^2>0
\]

for a regular nonzero core coefficient.
Thus the local axisymmetric no-swirl firewall occupies the nodal-shape class

\[
\boxed{
\operatorname{sgn}\det G_h=+1,
\qquad
\mathcal A=1.
}
\]

---

## 7. Two genuinely non-axisymmetric regular core classes

A regular winding filament is locally incompatible with the axisymmetric firewall if either

### Class I — negative-index core

\[
\boxed{
\det G_h<0.
}
\]

This is a saddle-type simple zero of the horizontal streamfunction critical point.
The sign cannot become positive without

\[
\det G_h=0.
\]

### Class II — anisotropic positive-index core

\[
\boxed{
\det G_h>0,
\qquad
\mathcal A>1.
}
\]

This has the same positive winding orientation as the axisymmetric model but unequal singular values.
Because `A` is materially invariant, it cannot reach `A=1` while remaining regular.

Thus

\[
\boxed{
G_{nonaxis}^{core}
=
G_{index-}
\ \lor\ 
G_{aniso+}.
}
\]

Both are separated from the local axisymmetric core by nodal degeneration.

---

## 8. Axisymmetric-compatible class is only a local compatibility condition

The converse is not claimed.

A filament satisfying

\[
\det G_h>0,
\qquad
\mathcal A=1
\]

has a locally conformal first-order winding core, but that does **not** prove the entire surrounding field is axisymmetric.
Higher jets, the geometry of the nodal network, and `x_3` dependence may still be non-axisymmetric.

Therefore define

\[
G_{conf+}^{core}
\]

as merely the **axisymmetric-compatible local core class**.

Further classification is required before identifying it with the M17-008 firewall.

---

## 9. Relation to M17-013 hysteresis

M17-013 showed that

\[
\operatorname{div}_{(q,x_3)}V_L=\kappa
\]

and that the M5-685 amplification factor is the label-flow Jacobian.

But the scalar label dynamics contains no dependence on

\[
\mathcal A
\quad\text{or}\quad
\operatorname{sgn}\det G_h.
\]

Hence

\[
\boxed{
\text{kappa/flux hysteresis does not change nodal shape class.}
}
\]

A genuinely anisotropic or negative-index regular core may execute the same scalar expansion/contraction hysteresis while retaining its non-axisymmetric shape invariant.

This proves that the M17/M5 scalar bridge, although necessary, is not sufficient for rank-one closure.

---

## 10. DSD analysis

### 10.1 Separate amplitude from shape
The nodal Jacobian descriptor factorizes into

\[
G_h
=
\text{positive scalar amplitude}
\times
\text{fixed normalized shape}.
\]

M17-010 controls the amplitude through `kappa-3/2`; M17-014 isolates the orthogonal shape information that scalar averaging discards.

### 10.2 Describability difference
Two states can have identical

\[
\kappa(\theta),
\qquad
a(\theta),
\qquad h(\theta)
\]

along the reduced label orbit yet have different `widehat C`.
Thus the scalar hysteresis descriptor does not fully describe the nodal geometry.

### 10.3 Correct branch variable
The rank-one audit must carry

\[
(\kappa,h,a)
\]

and

\[
(\operatorname{sgn}\det G_h,\widehat C)
\]

as separate channels.
Dropping the second channel would merge the known regular firewall with genuinely non-axisymmetric survivors.

---

## 11. DSD audit

### Audit A — claiming every positive winding core is axisymmetric-like
Rejected.
Positive index does not imply equal singular values.

### Audit B — claiming `A=1` proves global axisymmetry
Rejected.
It is only a first-order local condition.

### Audit C — allowing continuous regular axisymmetric reduction from `A>1`
Rejected.
`A` is materially invariant under M17-010.

### Audit D — allowing winding-sign reversal without topology change
Rejected.
The determinant sign cannot change unless the regular Jacobian loses rank.

### Audit E — firewall preservation
Preserved.
The known axisymmetric no-swirl class lies inside the conformal positive-index class and is not declared contradictory.

### Audit F — proof status
The genuinely non-axisymmetric regular subbranch remains open.

---

## 12. Updated rank-one branch

The regular recurrent nodal branch now splits as

\[
\boxed{
R_{nodal}^{uniform}
\Longrightarrow
G_{conf+}^{core}
\ \lor\ 
G_{aniso+}^{core}
\ \lor\ 
G_{index-}^{core}.
}
\]

For the last two classes,

\[
\boxed{
\text{axisymmetric/no-swirl escape}
\Longrightarrow
\text{rank loss or finite-jet nodal degeneration first}.
}
\]

Thus the genuinely non-axisymmetric regular branch has been isolated without falsely excluding the regular firewall.

---

## 13. Next target — higher-jet / contour-geometry transport

The next calculation should use the semilinear equation

\[
\Delta q=F(q,x_3,\theta)
\]

on a filament whose normalized Hessian shape is fixed and non-axisymmetric.

The key question becomes:

\[
\boxed{
\text{Can a recurrent CE-H solution preserve }
\mathcal A>1
\text{ or negative index while also sustaining the M17-013/M5-685 hysteresis?}
}
\]

The natural descriptors are

1. third and fourth jets of `q` at the critical filament;
2. curvature and area of nearby q-level contours;
3. compatibility of those contour laws with the finite-radius positive/negative payer cycle of M17-012.

This is the new **Nodal Shape–Hysteresis Compatibility Gate (NSHCG)**.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
