# DSD M5-194 — Divergence-Free Drift Commutator Leaves a Critical Strain Barrier

Date: 2026-08-28

Status: **P1_B CRITICAL DRIFT AUDIT / PUTTING THE LARGE DIVERGENCE-FREE TYPE-I TRANSPORT INSIDE THE LEI–YANG–YUAN CONJUGATED OPERATOR REMOVES THE ARTIFICIAL `|b|^2|nabla Z|^2` FORCING COST, BUT THE SELF/SKEW COMMUTATOR LEAVES THE EXACT STRAIN FORM `-2 t^2 S_b : nabla v tensor nabla v`; TYPE-I SCALING MAKES THIS THE SAME `t|nabla v|^2` ORDER AS THE BASE HEAT GRADIENT COERCIVITY, WITH NO CARLEMAN-PARAMETER OR SHORT-TIME GAIN / ARBITRARILY LARGE CRITICAL STRAIN IS THEREFORE THE TRUE POLYNOMIAL-WEIGHT BARRIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Drift-inclusive conjugated operator

After reverse time, consider schematically

\[
L_b=\partial_t+\nu\Delta+b\cdot\nabla,
\qquad
\nabla\cdot b=0.
\]

In the Lei–Yang–Yuan scaling one multiplies the conjugated operator by `t`; hence the added drift piece is

\[
\boxed{B=t\,b\cdot\nabla}
\]

plus bounded zeroth-order commutators with the polynomial spatial weight.

Because `div b=0`, the principal differential part of `B` is skew-adjoint in unweighted conjugated `L2`.

---

## 2. Exact commutator with the Laplacian

Let `v` be compactly supported.  Since `Delta` is self-adjoint and `b·nabla` is skew,

\[
\langle[\Delta,b\cdot\nabla]v,v\rangle
=2\operatorname{Re}\langle b\cdot\nabla v,\Delta v\rangle.
\]

Integrating by parts,

\[
\begin{aligned}
2\int (b_j\partial_jv)\,\Delta v
&=-2\int \partial_i(b_j\partial_jv)\,\partial_i v\\
&=-2\int (\partial_i b_j)(\partial_jv)(\partial_iv)
-2\int b_j(\partial_{ij}v)(\partial_i v).
\end{aligned}
\]

The last term is

\[
-\int b\cdot\nabla |\nabla v|^2=0.
\]

Therefore

\[
\boxed{
\langle[\Delta,b\cdot\nabla]v,v\rangle
=-2\int (\partial_i b_j)(\partial_jv)(\partial_i v).
}
\]

Only the symmetric strain contributes to the real quadratic form:

\[
\boxed{
=-2\int S_b:\nabla v\otimes\nabla v.
}
\]

No second derivative of `v` remains.

---

## 3. Time-scaled commutator

The corresponding part of

\[
[t\nu\Delta,t b\cdot\nabla]
\]

is

\[
\boxed{
-2\nu t^2
\int S_b:\nabla v\otimes\nabla v.
}
\]

The additional commutators with `t partial_t` contain `t b` and `t^2 partial_t b`; these are lower differential order and can be paired with the zero-order Carleman term after Young splitting.  They are not the principal issue.

---

## 4. Type-I scaling of the strain term

The W1 physical coefficient satisfies

\[
|S_b(x,t)|\le\frac{C_S}{r^2+t}.
\]

Hence

\[
\boxed{
t^2|S_b|
\le
C_S\frac{t^2}{r^2+t}
\le C_S t.
}
\]

The base heat commutator in the same weighted identity produces a positive gradient term of the form

\[
\boxed{c_0\nu t\int|\nabla v|^2.}
\]

Thus the relative size is

\[
\frac{2\nu t^2|S_b|}{c_0\nu t}
\le C\,C_S,
\]

which does **not** tend to zero as `t->0`.

---

## 5. No help from the time Carleman parameter

In the Lei–Yang–Yuan weighted estimate, the large parameter `a` multiplies the zero-order term

\[
(a+1)|v|^2,
\]

but the positive gradient coercivity has no corresponding `a` factor.

Therefore increasing `a` cannot absorb

\[
C_S t|\nabla v|^2
\]

when `C_S` is arbitrary.

Likewise, shortening the time interval does not help because both the positive heat gradient term and the strain error carry the same factor `t`.

Hence

\[
\boxed{
\text{large Type-I strain is an exactly critical polynomial-weight obstruction.}
}
\]

---

## 6. Conditional small-strain subbranch

If one had the additional quantitative condition

\[
\boxed{C_S<c_*\nu}
\]

for a universal threshold determined by the weighted commutator, then the strain term would be absorbable and the remaining stretching/potential terms could be handled by the M5-193 form bound and large `a`.

No such smallness has been proved for the W1 compact minimal class.

Thus this is only a conditional closure branch, not a W1 theorem.

---

## 7. Consequence for the choice of weight

To handle arbitrary W1 Type-I strain, the backward estimate needs **large-parameter gradient coercivity**, schematically

\[
\boxed{
 a\,t^{-1}\,|\nabla Z|^2
}

or an equivalent positive term whose coefficient can dominate any fixed critical strain amplitude.

The polynomial-spatial Lei–Yang–Yuan estimate was designed for bounded coefficients and does not export this gain.

This points back to a genuinely spatially pseudoconvex/Carleman phase, but pressure must then be handled by a matched elliptic estimate rather than by the polynomial Calderon–Zygmund shortcut.

---

## 8. DSD audit

### Formation — GREEN

The strain form is obtained from an exact commutator identity.

### Axis — GREEN

Transport skewness and strain deformation are no longer conflated.

### Static aggregation — GREEN

The same critical `t` factor is not misread as a small-time gain.

### Dynamics — GREEN obstruction

Polynomial backward weight closes only a small-critical-strain subbranch; arbitrary W1 strain remains open.

### Cross-audit — GREEN

This refines M5-193 without reviving the invalid forcing-square treatment.

---

## 9. Next calculation

Test a terminal-singular **spatially pseudoconvex** phase whose gradient coercivity carries the large Carleman parameter, and pair it with an elliptic pressure estimate using the same spatial phase at each time.

The first target is a parabolically scaled quadratic phase, because its spatial Hessian has a fixed sign, unlike the rejected logarithmic phase M5-187.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
