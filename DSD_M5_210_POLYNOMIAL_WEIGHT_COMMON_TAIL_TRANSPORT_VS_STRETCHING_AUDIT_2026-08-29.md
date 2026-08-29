# DSD M5-210 — Polynomial-Weight Common-Tail Transport vs Stretching Audit

Date: 2026-08-29

Parent: `DSD_M5_209_LEI_YANG_YUAN_POLYNOMIAL_WEIGHT_TYPE_I_HYPOTHESIS_AUDIT_2026-08-29.md`

Status: **MIXED RESULT / POLYNOMIAL SPATIAL WEIGHTS DO REMOVE THE SPECIFIC RADIAL-CARLEMAN `beta r^-2` TRANSPORT COMMUTATOR THAT BLOCKED M5-194, BUT THE COMMON-TAIL STRETCHING FORM REMAINS AN ARBITRARY-AMPLITUDE HARDY-CRITICAL QUADRATIC FORM / A DIRECT WEAK-`L^3` REPLACEMENT OF THE LEI–YANG–YUAN `L^∞` ABSORPTION THEREFORE FAILS WITHOUT A SMALLNESS OR PRINCIPAL-OPERATOR ARGUMENT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Polynomial weight

Let

\[
w_k(x):=(1+|x|^2)^{-k},
\qquad k>0.
\]

For a divergence-free relative field `W`, consider the common-tail transport

\[
(B_T\cdot\nabla)W,
\qquad
\nabla\cdot B_T=0.
\]

The weighted real form is

\[
\begin{aligned}
\int w_kW\cdot(B_T\cdot\nabla W)
&=\frac12\int w_k B_T\cdot\nabla|W|^2\\
&=-\frac12\int (B_T\cdot\nabla w_k)|W|^2.
\end{aligned}
\]

Hence

\[
\boxed{
\mathfrak T_k[W]
=-\frac12\int w_k
(B_T\cdot\nabla\log w_k)|W|^2.
}
\]

---

## 2. Polynomial weighting softens the critical transport commutator

We have

\[
\nabla\log w_k
=-\frac{2kx}{1+|x|^2}.
\]

For a canonical critical tail

\[
|B_T(x)|\lesssim \frac{C_T}{|x|},
\]

one gets

\[
|B_T\cdot\nabla\log w_k|
\lesssim
2kC_T\frac1{1+|x|^2}.
\]

Thus

\[
\boxed{
|\mathfrak T_k[W]|
\lesssim
kC_T
\int w_k\frac{|W|^2}{1+|x|^2}dx
\le
kC_T\int w_k|W|^2dx.
}
\]

This is a **zeroth-order bounded weighted potential**.

It is fundamentally better than the radial exponential-Carleman commutator in M5-194,

\[
\beta\frac{\Phi_r}{r^2}|W|^2,
\]

whose coefficient grows with the Carleman parameter.

Therefore

\[
\boxed{
\text{polynomial spatial weight genuinely fixes the transport-weight interaction.}
}
\]

This is a positive result.

---

## 3. Stretching does not receive the same improvement

The common-tail stretching term is

\[
\mathfrak S_k[W]
:=
\int w_k W^TS_{B_T}Wdx.
\]

At critical order,

\[
|S_{B_T}(x)|\lesssim \frac{C_T}{|x|^2}.
\]

Therefore

\[
|\mathfrak S_k[W]|
\lesssim
C_T
\int w_k\frac{|W|^2}{|x|^2}dx.
\]

A weighted Hardy estimate has the schematic form

\[
\int w_k\frac{|W|^2}{|x|^2}
\lesssim
\int w_k|\nabla W|^2
+C_k\int w_k|W|^2.
\]

Hence

\[
\boxed{
|\mathfrak S_k[W]|
\lesssim
C_TC_H
\int w_k|\nabla W|^2
+C_TC_k\int w_k|W|^2.
}
\]

The first coefficient is proportional to the full common-tail amplitude `C_T`.

There is no truncation parameter that makes it arbitrarily small while preserving the canonical weak-`L^3` tail.

---

## 4. Integration by parts does not remove the critical coefficient

One may try to avoid `S_{B_T}` by integrating the derivative back onto `W`:

\[
\int w_k W_iW_j\partial_jB_{T,i}
=
-\int B_{T,i}\partial_j(w_kW_iW_j).
\]

Using `div W=0`, this becomes a sum of

\[
-\int w_k B_T\cdot(W\cdot\nabla W)
\]

and weight-derivative terms.

The latter are zeroth-order as in Section 2.

But the main term satisfies only the critical Lorentz estimate

\[
\left|
\int w_k B_T\cdot(W\cdot\nabla W)
\right|
\lesssim
\|B_T\|_{L^{3,\infty}}
\|w_k^{1/2}W\|_{L^{6,2}}
\|w_k^{1/2}\nabla W\|_2
+\text{weight terms}.
\]

Weighted Sobolev then again gives

\[
\boxed{
|\mathfrak S_k[W]|
\lesssim
C\|B_T\|_{L^{3,\infty}}
\int w_k|\nabla W|^2
+\text{lower order}.
}
\]

Thus the same non-small critical coefficient reappears.

---

## 5. Why a large temporal Carleman exponent does not automatically fix it

The Lei–Yang–Yuan weighted heat estimate supplies positive terms schematically of the form

\[
(a+1)\int w_k|W|^2
+
\int w_k|\nabla W|^2.
\]

Increasing `a` strengthens the `L^2` term.

It does **not** multiply the gradient coercivity by an arbitrarily large factor.

Therefore a term

\[
C_T\int w_k|\nabla W|^2
\]

cannot be absorbed for arbitrary `C_T` merely by choosing `a` large.

The critical derivative-scale obstruction remains.

---

## 6. Strong-`L^3` quotient remains harmless

For the strong quotient `Q_i`, the existing equiintegrability argument still gives, uniformly over the compact fiber,

\[
\boxed{
|\mathfrak q_{Q_i}[W]|
\le
\varepsilon
\int w_k|\nabla W|^2
+C_{\varepsilon,k}\int w_k|W|^2.
}
\]

Thus polynomial weighting does not revive a quotient obstruction.

The split remains

\[
\boxed{
\text{strong quotient = infinitesimal perturbation},
\qquad
\text{common weak-}L^3\text{ tail = non-small principal form}.
}
\]

---

## 7. Positive and negative conclusions

### Positive

Polynomial spatial decay solves two issues at once:

1. it is compatible with the Calderón–Zygmund pressure structure through the Lei–Yang–Yuan divergence estimate;
2. it turns the weighted critical transport commutator into a bounded zeroth-order term.

### Negative

It does not remove arbitrary-amplitude stretching:

\[
\boxed{
S_{B_T}\sim r^{-2}
\quad\Rightarrow\quad
\text{non-small Hardy-critical gradient form}.
}
\]

Thus the simple adaptation

\[
L^\infty\text{ background}
\rightsquigarrow
L^{3,\infty}\text{ background}
\]

in the published proof is not valid at arbitrary critical amplitude.

---

## 8. New exact frontier

The whole-space polynomial-weight route has now reduced to

\[
\boxed{
\text{derive a backward weighted estimate for the full common-tail Oseen operator}
}
\]

with the stretching term placed on the **principal side**, rather than treated perturbatively.

Equivalently, one needs a coercivity/log-convexity mechanism for

\[
-\nu\Delta
+(B_T\cdot\nabla)
+(\cdot\,\cdot\nabla)B_T
\]

at arbitrary weak-`L^3` / Hardy-critical amplitude.

This is more precise than the previous generic phrase `pressure-compatible BU`.

---

## 9. DSD audit

### Formation — GREEN

Transport and stretching are evaluated in the actual polynomial weighted quadratic form.

### Axis — GREEN

First-order transport and symmetric derivative stretching are kept separate.

### Static aggregation — GREEN

The improvement of one term is not promoted to the other.

### Dynamics — YELLOW

Principal-operator backward coercivity remains open.

### Cross-audit — GREEN

The result agrees simultaneously with M5-190 and M5-194: the pressure and radial-weight transport problems can be demoted, while arbitrary-amplitude critical stretching remains.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]