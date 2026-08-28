# DSD M5-191 — Common-Tail Strain Sign Countermodel and Finite-Order Firewall

Date: 2026-08-28

Status: **P1_B COMMON-TAIL FORM AUDIT / A SMOOTH DIVERGENCE-FREE ZERO-FLUX 1/r ROTATIONAL TAIL HAS AN EXACT TRACE-FREE STRAIN WITH BOTH SIGNS AT THE CRITICAL r^-2 ORDER / THEREFORE NO GEOMETRY-ONLY OR HARDY-ONLY COERCIVE SIGN CAN CONTROL THE ARBITRARY-AMPLITUDE COMMON-TAIL OSEEN FORM / M5-135 ALSO SHOWS THAT A NONZERO LEADING TAIL RESIDUAL CAN BE ABSORBED BY NONRESONANT SUBLEADING CORRECTIONS TO EVERY FIXED FINITE ORDER, SO NO FINITE-ORDER ASYMPTOTIC NSE RECURSION AUTOMATICALLY RESTORES THE MISSING SIGN / ANY CLOSURE MUST USE A DYNAMIC/NONLOCAL BACKWARD-UNIQUENESS STRUCTURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Rotational critical tail

Fix a constant vector `a` and define

\[
\boxed{
B(x)
:=
c\,\frac{a\times x}{|x|^2}
=
\frac c{|x|}(a\times\theta),
\qquad \theta=\frac x{|x|}.
}
\]

This is the physical-space form of the constant-amplitude rotational log-cylinder field used in M5-123.

It is smooth on `R3\{0}` and satisfies

\[
\nabla\cdot B=0.
\]

It is purely tangential, hence its radial flux through every sphere is zero.

---

## 2. Exact gradient and strain

Set

\[
v:=a\times x.
\]

Then

\[
B=c\,r^{-2}v.
\]

Differentiation gives

\[
\partial_jB_i
=
c\,r^{-2}\varepsilon_{ikj}a_k
-2c\,r^{-4}v_i x_j.
\]

The first term is antisymmetric in `i,j`, so it disappears from the symmetric strain.

Thus

\[
\boxed{
S_B
:=
\frac12(\nabla B+\nabla B^T)
=
-c\,r^{-4}(v\otimes x+x\otimes v).
}
\]

Because

\[
v\cdot x=0,
\]

the matrix acts on the plane `span{x,v}` with eigenvalues

\[
\boxed{
\lambda_\pm
=
\pm\frac{|c|\,|v|}{r^3}
=
\pm\frac{|c|\,|a\times\theta|}{r^2},
}
\]

and has a third eigenvalue `0`.

Hence the critical strain is pointwise indefinite at every non-axis point.

---

## 3. Consequence for the relative energy form

The common-tail stretching form is

\[
\mathfrak q_B[W]
:=
\int W^TS_BW\,dx.
\]

Local divergence-free wave packets can be chosen with polarization arbitrarily close to either eigen-direction of `S_B` on a small ball away from the axis.

Therefore `q_B` admits both signs.

In particular there is no universal estimate of either form

\[
\mathfrak q_B[W]\ge0
\]

or

\[
\mathfrak q_B[W]\le0
\]

coming only from

- divergence freeness;
- zero radial flux;
- homogeneous `1/r` size;
- trace-free strain.

Thus

\[
\boxed{
\text{common-tail geometry}
\not\Rightarrow
\text{coercive strain sign}.
}
\]

---

## 4. Hardy boundedness remains unsigned

Hardy's inequality gives only

\[
|\mathfrak q_B[W]|
\le
C_B\int r^{-2}|W|^2dx
\le
4C_B\|\nabla W\|_2^2.
\]

This is a two-sided bound, not positivity.

If `4 C_B` is larger than viscosity, ordinary energy coercivity can fail.

Hence the following implication is RED:

\[
\boxed{
\text{Hardy-critical boundedness}
\Rightarrow
\text{large-amplitude backward injectivity}.
}
\]

---

## 5. Why this is not dismissed by finite-order NSE tail equations

The rotational field above is a geometry-level countermodel, not by itself asserted to be an actual W1 canonical descendant tail.

However M5-135 established that a leading `r^-1` tail residual at order `r^-3` is nonresonant in the subleading velocity sector and can be canceled by an `r^-3` correction.

The same mechanism iterates at every fixed finite asymptotic order.

Therefore a nonzero leading residual or the lack of a strain sign cannot be converted into an immediate finite-order contradiction.

This yields the firewall

\[
\boxed{
\text{finite-order asymptotic NSE recursion}
\not\Rightarrow
\text{positive common-tail strain form}.
}
\]

Any extra rigidity must be genuinely global in normal depth, dynamical in time, or nonlocal through the whole pressure/velocity system.

---

## 6. Effect on M5-190

M5-190 reduced the large backward-uniqueness gate to the common-tail operator

\[
\mathcal L_{B_T}
=
-\nu\Delta
+\mathbb P\nabla\cdot(B_T\otimes\cdot+\cdot\otimes B_T).
\]

M5-191 rules out the simplest proposed closure:

\[
\boxed{
\text{actual tail is divergence-free/zero-flux}
\Rightarrow
S_{B_T}\text{ has a favorable sign}.
}
\]

Status: RED at the geometry/finite-order level.

---

## 7. Legitimate next routes

Three noncircular routes remain:

1. **abstract parabolic backward uniqueness for the finite-energy nonautonomous form**, allowing a large critical skew+stretching principal operator;
2. **an adapted symmetrizer** derived from the full canonical-tail dynamics, not from pointwise strain geometry;
3. **a genuine critical Oseen--Stokes Carleman estimate** that absorbs the signed inverse-square form without smallness.

The first route is the least dependent on an unproved tail sign and should be audited next.

---

## 8. DSD audit

### Formation — GREEN

The countermodel is explicit and lies in the same geometric `1/r`, divergence-free, zero-flux class.

### Axis — GREEN

Pointwise strain sign and global W1 realizability are kept separate.

### Static aggregation — GREEN

Hardy boundedness is not confused with coercivity.

### Dynamics — GREEN FIREWALL / ACTUAL-TAIL SIGN STILL OPEN ONLY IF IT USES EXTRA GLOBAL DYNAMICS

The node does not claim that every canonical W1 tail equals the rotational model.

### Cross-audit — GREEN

M5-123 and M5-135 are used only to rule out geometry-only and finite-order-only sign arguments; no countermodel is promoted to an actual survivor.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
