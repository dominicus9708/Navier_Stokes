# Cauchy two-lane amplification: inviscid directional stretch versus viscous material rewrite

Date: 2026-08-13

Status: **EXACT CAUCHY CONTRIBUTION DECOMPOSITION + DERIVED FINAL-CORE TWO-LANE DICHOTOMY / OPEN STRICT-GAIN CLOSURE**.

The amplification-step deformation/viscous dichotomy can be refined.  The full operator norm of the deformation gradient is too coarse: only deformation acting on the material's earlier vorticity can directly create the inviscid part of the later vorticity.

The exact viscous Cauchy formula separates these mechanisms.

---

## 1. Exact two-contribution formula

Restart at `t0` and let

\[
F(a,t)=D_aX(a,t),
\qquad
\zeta=F^{-1}\omega(X,t).
\]

Since

\[
\partial_t\zeta=\nu F^{-1}\Delta\omega(X,t),
\]

we have

\[
\zeta(a,t_1)
=\omega(a,t_0)
+\nu\int_{t_0}^{t_1}
F(a,s)^{-1}\Delta\omega(X(a,s),s)ds.
\]

Multiplying by `F(a,t1)`,

\[
\boxed{
\omega(X(a,t_1),t_1)
=I(a)+V(a),
}
\]

where

\[
\boxed{
I(a)=F(a,t_1)\omega(a,t_0),
}
\]

and

\[
\boxed{
V(a)=
\nu F(a,t_1)
\int_{t_0}^{t_1}
F(a,s)^{-1}\Delta\omega(X(a,s),s)ds.
}
\]

Interpretation:

- `I`: the inviscid Cauchy transport of the earlier material vorticity;
- `V`: the physical contribution created by viscous alteration of the Cauchy invariant.

This is an exact identity on the smooth lifespan.

---

## 2. Final dangerous-core partition

Let

\[
W_1=qW_0,
\qquad
W_0=\|\omega(t_0)\|_\infty,
\]

and let

\[
C_1\subset\{|\omega(t_1)|\ge bW_1\}.
\]

Pull `C1` back to labels `A0`.

For every `a in A0`, triangle inequality gives

\[
|I(a)|+|V(a)|
\ge
bqW_0.
\]

Hence define

\[
A_I
=\{a\in A_0:|I(a)|\ge bqW_0/2\},
\]

\[
A_V=A_0\setminus A_I.
\]

On `A_V`, necessarily

\[
|V(a)|\ge bqW_0/2.
\]

Since

\[
A_0=A_I\cup A_V,
\]

at least one lane occupies half the final-core volume:

\[
\boxed{
|A_I|\ge|C_1|/2
\quad\text{or}\quad
|A_V|\ge|C_1|/2.
}
\]

No earlier-core overlap assumption is used.

---

## 3. I-lane gives directional strain exposure

For `a in A_I`, if `omega(a,t0) != 0`, define the inviscidly transported vector

\[
z(a,t)=F(a,t)\omega(a,t_0).
\]

It satisfies

\[
\partial_tz=(\nabla u)(X,t)z.
\]

Let

\[
e_z=z/|z|.
\]

Because the antisymmetric part of `grad u` does not change vector magnitude,

\[
\boxed{
\frac d{dt}\log|z|
=e_z^TS(X,t)e_z.
}
\]

At `t0`,

\[
|z(a,t_0)|=|\omega(a,t_0)|\le W_0.
\]

At `t1`, the I-lane definition gives

\[
|z(a,t_1)|\ge bqW_0/2.
\]

Therefore

\[
\boxed{
\int_{t_0}^{t_1}
e_z(a,t)^TS(X(a,t),t)e_z(a,t)dt
\ge
\log\frac{bq}{2}.
}
\]

whenever `bq>2`.

Thus the deformation lane is not merely `large ||F||`: a positive-volume part of the final core must carry **large positive directional strain exposure along the transported earlier-vorticity vector**.

By Cauchy--Schwarz in time and volume preservation, if `|A_I|>=|C1|/2`,

\[
\boxed{
\int_{t_0}^{t_1}\int_{X(A_I,t)}|S|^2dxdt
\ge
\frac{|C_1|}{2\tau}
\left(\log\frac{bq}{2}\right)^2.
}
\]

This lower bound is exact up to using `|S|` to dominate the directional quadratic form.

---

## 4. V-lane gives a viscous second-derivative cost

Let

\[
K_+=\sup_{A_0\times I}\|F\|_{op},
\qquad
K_-=\sup_{A_0\times I}\|F^{-1}\|_{op}.
\]

Then

\[
\|V\|_{L^2(A_V)}
\le
\nu K_+K_-\sqrt\tau
\left(
\int_I\int_{X(A_V,t)}|\Delta\omega|^2dxdt
\right)^{1/2}.
\]

If `|A_V|>=|C1|/2`, the pointwise V-lane lower bound yields

\[
\frac{b^2q^2W_0^2}{4}|A_V|
\le
\|V\|_{L^2(A_V)}^2.
\]

Hence

\[
\boxed{
\int_I\int_{X(A_V,t)}|\Delta\omega|^2dxdt
\ge
\frac{b^2q^2W_0^2|C_1|}
{8\nu^2K_+^2K_-^2\tau}.
}
\]

For a thick natural final core

\[
|C_1|\gtrsim(qW_0)^{-3/2},
\]

this becomes

\[
\boxed{
\int_I|\Delta\omega|^2
\gtrsim
\frac{q^{1/2}}
{\nu^2K_+^2K_-^2\sigma}
W_0^{3/2},
\qquad
\sigma=W_0\tau.
}
\]

up to fixed core-thickness/threshold constants.

---

## 5. DSD channel interpretation

The final dangerous core does not need to be typed first by its material genealogy.

At an amplification checkpoint it is enough to resolve two causally distinct channels:

\[
\boxed{
q_I(a)
=\log\frac{|F(a,t_1)\omega(a,t_0)|}
{|\omega(a,t_0)|},
}
\]

when the denominator is nonzero, and

\[
\boxed{
q_V(a)
=|V(a)|.
}
\]

The first is an **axis/deformation history channel**; the second is a **viscous material-rewrite channel**.

Formation discipline also requires that `omega(t0)=0` be treated correctly: the logarithmic I-channel is inapplicable there, and such a label can enter the final intense core only through the V contribution.

---

## 6. Relation to existing strain/projective gates

The I-lane exposure

\[
e_z^TSe_z
\]

can now be compared with the already typed channels:

- positive middle strain eigenvalue;
- strongest extensional eigenvalue and alignment;
- local/projective vorticity-axis coherence;
- strain-gap weighted axis conversion.

The V-lane cost enters directly at derivative order `k=2` and can be compared with

\[
D_2=E_2J_2
\]

and the derivative covariance hierarchy.

This is more precise than treating arbitrary deformation and arbitrary high derivatives as independent escape routes.

---

## 7. Remaining critical wall

The two lanes remain scale-critical at natural core size and natural time.

- I-lane strain-square cost on a shrinking natural volume is summable by scaling alone.
- V-lane `k=2` cost has the same natural exponent already identified by Sobolev interpolation.

Therefore the useful next step is **not** another power-counting bound.  It is to prove a strict gain from the fact that the same final dangerous core must simultaneously evade the projective/coherence/sparseness gates.

A proof-producing closure should show that a thick projectively dangerous core cannot repeatedly obtain its amplification through I and V lanes at their generic critical costs.

Status: **OPEN I/V STRICT-GAIN CLOSURE AT THE CRITICAL WALL**.
