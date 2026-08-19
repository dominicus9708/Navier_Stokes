# Local constant middle-axis replacement — 2026-08-20

Status: **CONDITIONAL LOCAL LEMMA ON THE NON-H SUBBRANCH; GLOBAL PACKING NOT YET PROVED.**

This note continues `M_NONSAT_MIDDLE_AXIS_LOCK_2026-08-20.md` and closes the spatial replacement gap under the local derivative control that defines the non-`H` branch.

---

## 1. Dangerous point

Let `y_*` be a normalized first-hitting core point on the fixed-gap `M` branch. Use increasing eigenvalue order

\[
s_1\le s_2\le s_3,
\]

and set

\[
s:=s_2(y_*)>0.
\]

Write at the center

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\]

with

\[
\frac d m\ge\frac13.
\]

Then the middle eigenvalue has the spectral gap

\[
\boxed{
\operatorname{gap}_2(y_*)
\ge\frac23m.
}
\]

Let

\[
n=e_2(y_*)
\]

be the middle eigenvector at the center, interpreted projectively.

---

## 2. Non-H local derivative control

Assume on a normalized ball `B_R(y_*)` that

\[
\boxed{
\|\nabla S\|_{L^\infty(B_R)}\le L_S
}
\]

and, for the normalized vorticity magnitude `rho=|Omega|` with `rho(y_*)=1`,

\[
\boxed{
\|\nabla\rho\|_{L^\infty(B_R)}\le L_\rho.
}
\]

Failure of such local control along the dangerous sequence is assigned to the higher-derivative/interface channel `H`.

Choose

\[
\boxed{
r
=c_0\min\left\{\frac{s}{L_S},\frac1{L_\rho},R\right\}
}
\]

with a sufficiently small universal `c_0>0`.

---

## 3. Positive middle strain persists on B_r

Eigenvalues of a symmetric matrix are Lipschitz with respect to the operator norm. Therefore for `y in B_r(y_*)`,

\[
|s_2(y)-s|
\le L_Sr
\le c_0s.
\]

Hence

\[
\boxed{
s_2(y)\ge(1-c_0)s.}
\]

Similarly the spectral gaps change by at most `O(L_S r)=O(c_0 s)`. Since `m >= s` and the center gap is at least `2m/3`, choosing `c_0` small gives

\[
\boxed{
\operatorname{gap}_2(y)\ge c_gm
}
\]

throughout the smaller ball, for a universal `c_g>0`.

---

## 4. Middle eigenvector variation is smaller than the occupancy scale

For a smooth symmetric matrix field with a simple middle eigenvalue, differentiating

\[
Se_2=s_2e_2
\]

and projecting onto the other eigenspaces gives

\[
\partial_k e_2
=
\sum_{j\ne2}
\frac{e_j^T(\partial_kS)e_2}{s_2-s_j}e_j.
\]

Hence

\[
|\nabla e_2|
\lesssim
\frac{|\nabla S|}{\operatorname{gap}_2}
\lesssim
\frac{L_S}{m}.
\]

Across the chosen ball,

\[
\operatorname{dist}_{proj}(e_2(y),n)
\lesssim
r\frac{L_S}{m}
\lesssim
c_0\frac{s}{m}.
\]

Therefore the squared angular defect satisfies

\[
\boxed{
1-(n\cdot e_2(y))^2
\lesssim
c_0^2\left(\frac{s}{m}\right)^2.
}
\]

The key point is that this becomes **stronger**, not weaker, when `s/m` is small.

---

## 5. Constant-axis strain remains positive

At each point,

\[
n^TSn-s_2
=
\sum_{j\ne2}(s_j-s_2)(n\cdot e_j)^2.
\]

Hence

\[
|n^TSn-s_2|
\le
(s_3-s_1)
\left[1-(n\cdot e_2)^2\right].
\]

Since on the positive-middle parameterization

\[
s_3-s_1=3m+d<4m,
\]

we obtain

\[
|n^TSn-s_2|
\lesssim
4m\,c_0^2\frac{s^2}{m^2}
\lesssim
C c_0^2s.
\]

Combining with `s_2(y) >= (1-c_0)s`, and choosing `c_0` sufficiently small,

\[
\boxed{
n^TS(y)n\ge c_s s>0
\qquad
\text{for all }y\in B_r(y_*),
}
\]

with a universal `c_s>0`.

Thus the varying robust-gap middle axis can be replaced by **one constant axis** on the natural positive-middle occupancy ball.

---

## 6. Vorticity magnitude also remains occupied

Because `rho(y_*)=1`, the choice

\[
r\le c_0/L_\rho
\]

implies

\[
\boxed{
\rho(y)\ge1-c_0
}
\]

on `B_r(y_*)`.

Consequently for a nonnegative cutoff `phi` supported in `B_r` and equal to one on a fixed inner fraction,

\[
\boxed{
\int\phi\rho^2n^TSn
\gtrsim
s r^3.
}
\]

This is a strictly positive local axial-strain budget.

---

## 7. Exact incompressibility identity forces transverse action

For the constant axis `n`, decompose

\[
U=U_nn+U_\perp.
\]

Incompressibility gives

\[
n^TSn=\partial_nU_n=-\nabla_\perp\cdot U_\perp.
\]

Therefore exactly

\[
\boxed{
\int\phi\rho^2n^TSn
=
\int\rho^2U_\perp\cdot\nabla_\perp\phi
+2\int\phi\rho U_\perp\cdot\nabla_\perp\rho.
}
\]

Since the left-hand side is bounded below by `c s r^3`, at least one of the two transverse terms must carry a comparable absolute action:

\[
\boxed{
\left|\int\rho^2U_\perp\cdot\nabla_\perp\phi\right|
+
2\left|\int\phi\rho U_\perp\cdot\nabla_\perp\rho\right|
\gtrsim
s r^3.
}
\]

The first term is bounded-radius side-shell/material turnover `T`. The second is transverse magnitude-interface action, assigned to `H_rho` unless it is realized by material turnover.

Thus, under the stated non-H local derivative control,

\[
\boxed{
M_{nonsat}(d/m\ge1/3)
\Longrightarrow
T_{bounded}\ \text{or}\ H_\rho.
}
\]

---

## 8. Role of the pointwise middle-axis locking lemma

The previous note also proved, directly on this branch,

\[
|\xi\cdot e_2|^2>43/48
\]

and

\[
|s_2-\Gamma|<0.153\,\Gamma.
\]

These facts identify the constant-axis positive budget above with the same middle-axis mechanism supplying the first-hitting vorticity stretching. Thus the route is not an unrelated positive-strain region: it is the spatial continuation of the dangerous `M` point.

---

## 9. Current consequence

Modulo the explicit interpretation that failure of the local Lipschitz/eigenframe control is an `H` escape, the fixed-gap nonsaturated branch is no longer an independent survivor:

\[
\boxed{
M_{nonsat}^*
\Longrightarrow
H\lor T_{bounded}.
}
\]

The remaining positive-middle branch is therefore concentrated near max-mid,

\[
\boxed{
0\le d/m<1/3,
}
\]

where `RIGIDITY_KERNEL_INVARIANT_2026-08-20.md` already forces max-mid defect reorganization or projection visibility/derivative action.

---

## 10. Updated local survivor tree

The local production tree is now reduced to

\[
\boxed{
H
\lor
T_{bounded}
\lor
P_V^*
\lor
P_{defect}^*.
}
\]

The broad `M_nonsat*` branch has been absorbed into `H/T` under the non-H compact local-control hypothesis.

The remaining unresolved non-H/non-T mechanism is therefore **projective reorganization**: vorticity--strain projective turnover `P_V*` and near-max-mid defect reorganization `P_defect*`.

Status: **FIXED-GAP M BRANCH ROUTED TO H/T UNDER LOCAL DERIVATIVE CONTROL; ACTIVE LOCAL ENDGAME = PROJECTIVE REORGANIZATION.**