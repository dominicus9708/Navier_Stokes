# M_nonsat determinant deficit — 2026-08-20

Status: **ACTIVE CALCULATION NOTE — NOT A GLOBAL REGULARITY PROOF.**

This note continues `RIGIDITY_KERNEL_INVARIANT_2026-08-20.md` and attacks the remaining non-max-mid positive-middle-strain branch.

---

## 1. Eigenvalue parameterization

On the positive-middle-strain sector, order the strain eigenvalues by

\[
s_1\le s_2\le s_3,
\qquad s_1+s_2+s_3=0,
\qquad s_2>0.
\]

Write

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\]

with

\[
m>0,
\qquad
0\le d<m.
\]

The exact max-mid state is `d=0`.

The basic invariants are

\[
|S|^2=6m^2+2d^2=2(3m^2+d^2),
\]

and

\[
\det S=-2m(m^2-d^2).
\]

---

## 2. Exact determinant saturation defect

For every trace-free symmetric `3 x 3` matrix,

\[
-\det S\le \frac{|S|^3}{3\sqrt6},
\]

with equality at the max-mid spectrum `(-2m,m,m)` up to overall sign/order conventions.

Define the pointwise saturation defect

\[
\boxed{
\mathfrak D_{det}(S)
:=
\frac{|S|^3}{3\sqrt6}+\det S
\ge0.
}
\]

With `x=d/m`, one obtains exactly

\[
\frac{\mathfrak D_{det}}{m^3}
=
\frac{2\sqrt3}{9}(3+x^2)^{3/2}-2(1-x^2).
\]

Let

\[
f(x)
=
\frac{2\sqrt3}{9}(3+x^2)^{3/2}-2(1-x^2).
\]

Then

\[
f(0)=0,
\]

and for `y=x^2`,

\[
\frac{d}{dy}
\left[f(\sqrt y)-3y\right]
=
\frac{\sqrt3}{3}\sqrt{3+y}-1
\ge0.
\]

Therefore

\[
\boxed{
\mathfrak D_{det}(S)
\ge
3md^2.
}
\]

Equivalently,

\[
\boxed{
\mathfrak D_{det}(S)
\ge
\frac38(-s_1)(s_3-s_2)^2.
}
\]

This is an exact quantitative loss from max-mid determinant saturation.

---

## 3. Fixed nonsaturation gives a cubic middle-strain penalty

If

\[
\frac d m\ge\eta>0,
\]

then

\[
\mathfrak D_{det}
\ge
3\eta^2m^3.
\]

Since

\[
s_2=m-d\le m,
\]

one also has

\[
\boxed{
\mathfrak D_{det}
\ge
3\eta^2(s_2^+)^3
}
\]

on the positive-middle nonsaturated sector.

Hence

\[
\boxed{
\int\mathfrak D_{det}
\ge
3\eta^2
\int_{\{s_2>0,\ d/m\ge\eta\}}
(s_2^+)^3.
}
\]

---

## 4. Exact enstrophy-growth decomposition

For Navier--Stokes strain,

\[
\frac d{dt}\|S\|_2^2
=
-2\nu\|\nabla S\|_2^2
-4\int\det S.
\]

Using

\[
-\det S
=
\frac{|S|^3}{3\sqrt6}-\mathfrak D_{det},
\]

this becomes

\[
\boxed{
\frac d{dt}\|S\|_2^2
+2\nu\|\nabla S\|_2^2
=
\frac{4}{3\sqrt6}\|S\|_3^3
-4\int\mathfrak D_{det}.
}
\]

Thus determinant nonsaturation appears as an **exact negative cubic correction** to the maximally self-amplifying cubic strain term.

On the fixed nonsaturation sector,

\[
\boxed{
\frac d{dt}\|S\|_2^2
+2\nu\|\nabla S\|_2^2
\le
\frac{4}{3\sqrt6}\|S\|_3^3
-12\eta^2
\int_{\{s_2>0,\ d/m\ge\eta\}}
(s_2^+)^3.
}
\]

---

## 5. Dynamic first-hitting form

Let

\[
W=\|\omega\|_\infty,
\qquad
\lambda=W^{1/2},
\qquad
\frac{ds}{dt}=W,
\]

and let

\[
\Sigma=S_U
\]

be the normalized strain, so physical strain is

\[
S=W\Sigma.
\]

Define

\[
E_\Sigma=\|\Sigma\|_2^2,
\qquad
P_\Sigma=\|\nabla\Sigma\|_2^2.
\]

Because

\[
\|S\|_2^2=W^{1/2}E_\Sigma,
\qquad
\|\nabla S\|_2^2=W^{3/2}P_\Sigma,
\]

and the cubic determinant terms also scale like `W^(3/2)`, division by `W^(3/2)` gives

\[
\boxed{
E_\Sigma'
+aE_\Sigma
+2\nu P_\Sigma
=
\frac{4}{3\sqrt6}\|\Sigma\|_3^3
-4\int\mathfrak D_{det}(\Sigma).
}
\]

Therefore on the normalized nonsaturated sector

\[
\boxed{
E_\Sigma'
+aE_\Sigma
+2\nu P_\Sigma
\le
\frac{4}{3\sqrt6}\|\Sigma\|_3^3
-12\eta^2
\int_{\{\sigma_2>0,\ d/m\ge\eta\}}
(\sigma_2^+)^3.
}
\]

This places the determinant saturation loss directly in the same first-hitting ledger as the scale-damping term `a E_Sigma`.

---

## 6. Interpretation

The branch `M_nonsat*` cannot be treated as a merely weaker version of max-mid amplification. It pays an explicit cubic loss

\[
\mathfrak D_{det}
\gtrsim
m d^2.
\]

For a fixed relative gap `d/m >= eta`, the loss is a fixed fraction of the local cubic strain scale.

However this identity alone does **not** yet yield a contradiction, because the positive cubic production elsewhere can in principle compensate the defect. A local occupancy/packing statement is still required.

---

## 7. Next target

Combine the fixed-gap sector with the A/C/M trichotomy. The non-extensional, low-axis-conversion `M` branch should force the vorticity direction toward the **middle strain eigenvector** when `d/m` is bounded below. If that locking is quantitative, the aligned-tube incompressibility identity can route the fixed-gap branch to `H/T`, leaving only the near-max-mid defect-reorganization branch already isolated in `RIGIDITY_KERNEL_INVARIANT_2026-08-20.md`.

Status: **DETERMINANT SATURATION LOSS QUANTIFIED; M_NONSAT NOW CARRIES AN EXACT CUBIC PENALTY; NEXT = MIDDLE-EIGENVECTOR LOCKING.**