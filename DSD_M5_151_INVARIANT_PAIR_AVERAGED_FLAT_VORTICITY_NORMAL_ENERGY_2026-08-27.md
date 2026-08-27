# DSD M5-151 — Invariant-Pair Averaged Flat-Vorticity Normal Energy

Date: 2026-08-27

Status: **P1_B^S ENERGY IDENTITY / ON A NON-DIAGONAL INVARIANT SAME-TAIL PAIR MEASURE, THE INVERSE-FUCHSIAN VORTICITY DIFFERENCE ADMITS AN EXACT NORMAL ENERGY IDENTITY IN WHICH THE GENEALOGICAL MIXED DERIVATIVE CANCELS BY INVARIANCE AND THE LEADING NORMAL TERM HAS ONE-SIDED COERCIVE SIGN / CLOSURE NOW REQUIRES A TAME CROSS-SECTION DERIVATIVE/BIOT-SAVART ESTIMATE FOR THE `O(xi^-1)` REMAINDER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Statistical flat-fiber branch

Work on Branch `P1_B^S` from M5-150.

Thus there is an invariant probability measure `rho` on the same-tail relative product

\[
\mathcal R=M\times_{\mathcal T}M
\]

with positive off-diagonal mass.

For a pair `(V,W)`, let

\[
K:=\Xi
\]

be the scaled relative vorticity from M5-149 in inverse-Fuchsian coordinates

\[
\xi=r^2,\qquad\eta=\log r-\frac s2.
\]

All pair states are flat:

\[
K=O(\xi^{-N})\qquad\forall N.
\]

---

## 2. Exact inverse-Fuchsian vorticity operator

For vorticity scaling `Omega=r^-2 K`,

\[
\Delta\Omega
=r^{-4}
\left[
(D^2-3D+2+\Delta_{S^2})K
\right],
\]

with

\[
D=\partial_\eta+2\xi\partial_\xi.
\]

The relative vorticity equation can therefore be written exactly as

\[
\boxed{
\begin{aligned}
0={}&4\nu K_{\xi\xi}
-\left(1+\frac{2\nu}{\xi}\right)K_\xi
+\frac{4\nu}{\xi}K_{\eta\xi}\\
&+\frac{\nu}{\xi^2}
\left(
K_{\eta\eta}-3K_\eta+2K+\Delta_{S^2}K
\right)
-\frac1{\xi^2}\mathcal N_{rel},
\end{aligned}
}
\]

where `N_rel` is the exact local transport/stretching difference, with velocity difference recovered from `K` by the order-minus-one Biot--Savart map.

---

## 3. Pair invariant average

Let

\[
\langle F\rangle
:=
\int_{\mathcal R}
\int_{S^2}F\,d\theta\,d\rho.
\]

At fixed `xi`, translation in `eta` is the pair W1 flow up to the fixed factor of two from the M5-136 coordinate relation.

Pair-flow invariance therefore makes `partial_eta` skew under this average:

\[
\boxed{
\langle f\cdot f_\eta\rangle=0,
}
\]

and, in particular,

\[
\boxed{
\langle K_\xi\cdot K_{\eta\xi}\rangle=0.
}
\]

This cancellation is available only on Branch `P1_B^S`; it is not assumed on the proximal branch.

---

## 4. Multiply by the normal derivative

Define

\[
A:=\langle|K_\xi|^2\rangle,
\]

\[
B_\eta:=\langle|K_\eta|^2\rangle,
\qquad
B_\theta:=\langle|\nabla_{S^2}K|^2\rangle,
\qquad
E:=\langle|K|^2\rangle,
\]

and

\[
C:=\langle K_\eta\cdot K_\xi\rangle.
\]

Take the averaged inner product of the exact equation with `K_xi`.

The terms are

\[
4\nu\langle K_{\xi\xi}\cdot K_\xi\rangle
=2\nu A',
\]

\[
\frac{4\nu}{\xi}
\langle K_{\eta\xi}\cdot K_\xi\rangle
=0,
\]

\[
\langle K_{\eta\eta}\cdot K_\xi\rangle
=-\frac12B_\eta',
\]

\[
2\langle K\cdot K_\xi\rangle
=E',
\]

and

\[
\langle\Delta_{S^2}K\cdot K_\xi\rangle
=-\frac12B_\theta'.
\]

Thus

\[
\boxed{
\begin{aligned}
0={}&2\nu A'
-\left(1+\frac{2\nu}{\xi}\right)A\\
&+\frac{\nu}{\xi^2}
\left(
-\frac12B_\eta'
-3C
+E'
-\frac12B_\theta'
\right)\\
&-\frac1{\xi^2}
\langle\mathcal N_{rel}\cdot K_\xi\rangle.
\end{aligned}
}
\]

This is the exact averaged normal energy identity.

---

## 5. Corrected normal energy

Set

\[
Q:=-\frac12B_\eta+E-\frac12B_\theta
\]

and

\[
\boxed{
\mathcal J(\xi)
:=2\nu A(\xi)
+\frac{\nu}{\xi^2}Q(\xi).
}
\]

Differentiating and using the preceding identity gives

\[
\boxed{
\begin{aligned}
\mathcal J'
={}&\left(1+\frac{2\nu}{\xi}\right)A
+\frac{3\nu}{\xi^2}C\\
&+\frac1{\xi^2}
\langle\mathcal N_{rel}\cdot K_\xi\rangle
-\frac{2\nu}{\xi^3}Q.
\end{aligned}
}
\]

The leading term is

\[
\boxed{+A=+\langle|K_\xi|^2\rangle.}
\]

All remaining terms carry at least one explicit inverse power of `xi` beyond the principal coefficient, except that `N_rel` can contain `xi K_xi`; after the displayed `xi^-2` prefactor this is still only `O(xi^-1)A`.

---

## 6. Flat boundary value at infinity

M5-145/M5-149 give superalgebraic decay of `K` and every fixed finite derivative.

Hence

\[
A,B_\eta,B_\theta,E,C,Q\to0
\qquad(\xi\to\infty),
\]

faster than every fixed inverse power, and

\[
\boxed{\mathcal J(\infty)=0.}
\]

If the remainder terms can be bounded by, for sufficiently large `xi`,

\[
\left|
\frac{3\nu}{\xi^2}C
+\frac1{\xi^2}\langle\mathcal N_{rel}\cdot K_\xi\rangle
-\frac{2\nu}{\xi^3}Q
\right|
\le
\frac12A
+\text{a derivative-hierarchy term absorbable into }\mathcal J,
\]

then

\[
\mathcal J'\ge\frac12A+\text{controlled terms}.
\]

Together with `J(infinity)=0` and positivity of the leading normal energy, this is the sign structure needed to rule out a nonzero statistical flat branch.

---

## 7. Structure of the nonlinear remainder

The relative nonlinear term is linear in `(K,Z)` once the pair backgrounds are fixed.

At large `xi`, the common W1 fields satisfy the critical tail bounds, while

\[
D K=K_\eta+2\xi K_\xi.
\]

Therefore the potentially largest normal piece of `N_rel` is schematic

\[
O(\xi K_\xi),
\]

so after multiplication by `xi^-2` and pairing with `K_xi` it contributes only

\[
O(\xi^{-1})A.
\]

Terms containing `Z` are one Biot--Savart order smoother than `K`, and the remaining tangential/genealogical pieces appear with `O(xi^-2)` coefficients.

Thus no nonlinear term changes the **principal sign** of the normal energy at sufficiently large `xi`.

What remains is a tame estimate that closes the cross-section derivative hierarchy without losing arbitrarily many `eta` or angular derivatives.

---

## 8. DSD four-chain audit

### Formation — GREEN

The invariant average is used only after M5-150 explicitly selects the statistical branch.

### Axis — GREEN

Normal derivative energy, genealogy, and angular derivatives are separately recorded.

### Static aggregation — GREEN

The `O(xi^-1)` nonlinear term is not promoted to principal order merely because the W1 background is critical in physical scaling.

### Dynamics — GREEN

Pair invariance is used solely for the skew cancellation of `eta` derivatives.

### Cross-audit — GREEN

The leading sign agrees with M5-146/M5-148 and no pressure variable has been reintroduced.

---

## 9. Current technical gate for Branch S

The statistical flat branch now reduces to proving a **finite/tame derivative hierarchy estimate** of the form

\[
\boxed{
\text{cross-section derivative energies}
\lesssim
\text{normal energy hierarchy}
}
\]

with constants uniform on the compact W1 pair class.

Because the W1 class already has local analytic/smooth compactness and Biot--Savart gains one derivative, this is a substantially more concrete task than the original generic backward-uniqueness problem.

It is not yet proved here.

---

## 10. Proximal branch untouched

Nothing in this note applies to `P1_B^P`, where no non-diagonal invariant pair measure exists.

That branch remains a separate mean-proximal/backward-uniqueness problem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]