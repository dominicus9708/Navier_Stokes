# DSD M5-265 — Convective Momentum-Force Mean Cancellation

Date: 2026-08-30

Parent: `DSD_M5_264_MOMENTUM_STRESS_ABSOLUTE_ACTION_GATE_2026-08-30.md`

Status: **EXACT CONVECTIVE REDUCTION / THE PURE LOCAL-MEAN COMPONENT CONTRIBUTES ZERO NET CONVECTIVE MOMENTUM FORCE THROUGH A SPHERE; AFTER `V=m+w`, ONLY THE MEAN--FLUCTUATION TERM `w(m·n)` AND THE RELATIVE QUADRATIC TERM `(w tensor w)n` REMAIN / BOTH ARE CONTROLLED BY THE MEAN-FREE BOUNDARY TRACE AND HENCE BY LOCAL GRADIENT/VARIANCE / THE CONVECTIVE FORCE IS NOT AN INDEPENDENT LARGE-MEAN ESCAPE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Convective momentum force

From M5-264,

\[
 b_{conv}
=-\frac1{M_R}
\int_{\partial B_R}(V\otimes V)n\,dS.
\]

Write

\[
V=m+w,
\qquad
m:=m_R,
\qquad
\int_{B_R}w\,dY=0.
\]

Since `m` is spatially constant and `div V=0`, also

\[
\nabla\cdot w=0.
\]

---

## 2. Expand the stress

We have

\[
V\otimes V
=m\otimes m
+m\otimes w
+w\otimes m
+w\otimes w.
\]

The sphere integral of the pure mean term is

\[
\int_{\partial B_R}(m\otimes m)n\,dS
=m(m\cdot\int_{\partial B_R}n\,dS)=0.
\]

The `m tensor w` term is

\[
\int_{\partial B_R}(m\otimes w)n\,dS
=m\int_{\partial B_R}w\cdot n\,dS.
\]

By divergence theorem and `div w=0`,

\[
\int_{\partial B_R}w\cdot n\,dS=0.
\]

Therefore

\[
\boxed{
\int_{\partial B_R}(m\otimes m)n=0,
\qquad
\int_{\partial B_R}(m\otimes w)n=0.
}
\]

---

## 3. Exact surviving convective force

Only two pieces remain:

\[
\boxed{
 b_{conv}
=-\frac1{M_R}
\int_{\partial B_R}
\left[
 w(m\cdot n)
+(w\otimes w)n
\right]dS.
}
\]

Thus pure mean drift cannot generate a net convective force through a centered sphere.

---

## 4. Trace bound

Let

\[
T_w:=\int_{\partial B_R}|w|^2dS.
\]

Then

\[
\left|
\int_{\partial B_R}w(m\cdot n)dS
\right|
\le
|m|\,|\partial B_R|^{1/2}T_w^{1/2},
\]

and

\[
\left|
\int_{\partial B_R}(w\otimes w)n\,dS
\right|
\le T_w.
\]

Hence

\[
\boxed{
|b_{conv}|
\le
\frac1{M_R}
\left[
|m|(4\pi R^2)^{1/2}T_w^{1/2}
+T_w
\right].
}
\]

---

## 5. Reduce the trace to local gradient

The ball trace inequality and mean-zero Poincare give

\[
T_w
\le
C_{tr}
\left[
R^{-1}\|w\|_{L^2(B_R)}^2
+R\|\nabla V\|_{L^2(B_R)}^2
\right]
\le
C_0R D_R,
\]

where

\[
D_R:=\int_{B_R}|\nabla V|^2.
\]

Therefore

\[
\boxed{
|b_{conv}|
\le
C_1|m|R^{-3/2}D_R^{1/2}
+C_2R^{-2}D_R.
}
\]

The constants depend only on the fixed ball trace convention.

---

## 6. Recurrent average

On the compact W1 fixed-ball hull,

\[
|m|\le m_+.
\]

Thus

\[
\boxed{
\langle|b_{conv}|\rangle
\le
C_1m_+R^{-3/2}
\langle D_R\rangle^{1/2}
+C_2R^{-2}\langle D_R\rangle.
}
\]

Consequently, if the convective component carries the M5-264 action floor

\[
\langle|b_{conv}|\rangle\ge b_*/3,
\]

then `D_R` must exceed the positive root of the corresponding quadratic inequality in `sqrt(<D_R>)`.

Thus

\[
\boxed{
T_{conv-force}
\Longrightarrow
\text{positive local gradient/relative-trace reservoir}.
}
\]

---

## 7. Relation to pure-corridor thresholds

A positive `D_R` floor is not automatically an H escape; order-one local gradient is allowed in the critical pure corridor.

The correct comparison is

\[
\boxed{
D_{R,forced}(b_*,m_+,R)
\stackrel{?}{>}
D_{R,pure,+}.
}
\]

If yes, the convective-force branch closes into H/T.

If no, it survives as a bounded but quantitatively constrained relative-gradient branch.

No threshold crossing is assumed here.

---

## 8. DSD verdict

### EXACT CANCELLATION

Pure mean drift contributes no net convective momentum force through a sphere.

### REDUCTION

\[
\boxed{
T_{conv-force}
\to
T_{rel-trace}/D_R.
}

Thus the truly independent momentum-force branches are reduced to

\[
\boxed{
T_{vis-force}
\lor
T_{pres-force}
\lor
\text{relative-gradient reservoir}.
}

### NEXT TARGET

Use volume representations

\[
\int_{\partial B_R}\partial_nV=\int_{B_R}\Delta V,
\qquad
\int_{\partial B_R}Pn=\int_{B_R}\nabla P
\]

to route viscous and pressure force directly to fixed-ball `H2` and nonlinear/pressure-gradient coefficients without boundary-trace losses.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
