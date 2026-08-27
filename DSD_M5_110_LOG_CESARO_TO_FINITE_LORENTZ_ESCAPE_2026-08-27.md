# DSD M5-110 — Log-Cesaro Defect to Finite-Lorentz Escape

Date: 2026-08-27

Status: **W1-CONDITIONAL CRITICAL-SPACE IDENTIFICATION / FAILURE OF UNIFORM LOG-CESARO TIGHTNESS FORCES ESCAPE OF EVERY FINITE-INDEX LORENTZ L^{3,q} NORM ALONG THE DEFECT SEQUENCE / WEAK-L3 q=infinity ALONE CAN KEEP A BOUNDED PLATEAU OF ARBITRARY LOG-DEPTH / THIS MATCHES THE CURRENT LITERATURE FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Distribution coordinate

For one W1 state `U`, let

\[
N_U(\lambda)
:=
|\{Y:|U(Y)|>\lambda\}|.
\]

Define the critical distribution coefficient

\[
\boxed{
Q_U(\lambda):=\lambda^3N_U(\lambda).
}
\]

For low amplitudes write

\[
\lambda=e^{-x},
\qquad x\ge0,
\]

and abbreviate

\[
\boxed{
Q_U(x):=e^{-3x}N_U(e^{-x}).
}
\]

The weak-L3 norm is equivalent to

\[
\boxed{
\|U\|_{L^{3,\infty}}^3
\asymp
\sup_x Q_U(x).
}
\]

Thus weak-L3 controls plateau height but not plateau length in `x`.

---

## 2. Finite-index Lorentz norms see log-length

For `1<=q<infinity`, the Lorentz distribution formula gives, up to fixed convention constants,

\[
\boxed{
\|U\|_{L^{3,q}}^q
\asymp
\int_0^\infty
\left[\lambda^3N_U(\lambda)\right]^{q/3}
\frac{d\lambda}{\lambda}.
}
\]

On the low-amplitude side this becomes

\[
\boxed{
\|U\|_{L^{3,q}}^q
\gtrsim
\int_0^\infty Q_U(x)^{q/3}dx.
}
\]

Therefore finite `q` integrates the critical distribution coefficient over log-amplitude depth.

By contrast `q=infinity` retains only `sup Q`.

---

## 3. Positive log-Cesaro blocks forced by the cubic residue

M5-104 showed that uniform critical-tail disappearance is equivalent, at the nonnegative distribution level, to uniform log-Cesaro tightness.

The surviving residue

\[
\mathscr R_3>0
\]

therefore implies failure of that tightness.

Hence there exist

\[
L_j\to\infty
\]

and states/approximants `U_j` in the retained defect sequence, together with one constant `c_0>0`, such that

\[
\boxed{
\frac1{L_j}
\int_0^{L_j}Q_{U_j}(x)dx
\ge c_0.
}
\]

The constant can be chosen strictly positive from the nonzero Abel/Mellin residue; no pointwise limit of `Q` is assumed.

---

## 4. Finite Lorentz index q>=3

Let

\[
r:=q/3\ge1.
\]

Jensen on `[0,L_j]` gives

\[
\frac1{L_j}
\int_0^{L_j}Q_{U_j}(x)^r dx
\ge
\left(
\frac1{L_j}
\int_0^{L_j}Q_{U_j}(x)dx
\right)^r.
\]

Therefore

\[
\int_0^{L_j}Q_{U_j}^{q/3}dx
\ge
L_j c_0^{q/3}.
\]

Thus

\[
\boxed{
\|U_j\|_{L^{3,q}}
\gtrsim
c_0^{1/3}L_j^{1/q},
\qquad 3\le q<\infty.
}
\]

Hence every finite-index critical Lorentz norm in this range escapes along the defect sequence.

---

## 5. Stronger finite Lorentz indices q<3

Suppose also the retained weak-L3 height bound is

\[
Q_{U_j}(x)\le M^3.
\]

For

\[
0<r=q/3<1,
\]

one has on `[0,M^3]`

\[
Q^r
\ge
M^{3(r-1)}Q.
\]

Hence

\[
\int_0^{L_j}Q_{U_j}^{q/3}dx
\ge
M^{q-3}c_0L_j.
\]

Therefore for every finite `q>=1`,

\[
\boxed{
\|U_j\|_{L^{3,q}}
\to\infty
}
\]

along the log-Cesaro defect sequence.

The exact constant depends on the Lorentz convention and on the weak-L3 height bound, but the divergence in `L_j` does not.

---

## 6. Why q=infinity is qualitatively different

For `q=infinity`,

\[
\|U_j\|_{L^{3,\infty}}^3
\asymp
\sup_xQ_{U_j}(x)
\le M^3.
\]

A plateau of height `O(1)` and length `L_j->infinity` therefore costs nothing additional in the weak-L3 norm.

This is the exact functional-analytic form of the W1 critical-tail obstruction:

\[
\boxed{
\text{finite q sees log-depth,}
\qquad
q=\infty\text{ sees only height}.
}
\]

---

## 7. Current literature boundary

The 2026 paper by Wen Feng, Jiao He, and Weinan Wang,

`Quantitative bounds for critically bounded solutions to the three-dimensional Navier-Stokes equations in Lorentz spaces`, DCDS-B 37 (2026), 175--205, DOI 10.3934/dcdsb.2026048,

proves quantitative regularity/blow-up results in

\[
L^{3,q_0},
\qquad 3\le q_0<\infty.
\]

This extends the finite-index critical Lorentz theory associated with Phuc's nonendpoint borderline result.

Luo--Tsai,

`Regularity criteria in weak L^3 for 3D incompressible Navier-Stokes equations`, Funkcialaj Ekvacioj 58 (2015), 387--404,

prove local regularity under **sufficient smallness** in

\[
L_t^\infty L_x^{3,\infty}
\]

plus pressure integrability.

The present W1 survivor is explicitly the large weak-L3 corridor, so these results do not automatically close it.

---

## 8. DSD four-chain audit

### Formation

The Lorentz norm is evaluated only after the log-Cesaro defect block has been formed.

### Axis

Amplitude depth `x=-log lambda` and Lorentz summability index `q` are separate coordinates.

### Static aggregation

Plateau height and plateau length are not conflated. `q=infinity` aggregates by supremum; finite `q` aggregates by log-depth integration.

### Dynamics

No finite-Lorentz regularity theorem is used to generate the W1 tail. It is only applied afterward as an exclusion boundary.

### Cross-audit

The argument is acyclic:

\[
\mathscr R_3>0
\to
\text{positive log-Cesaro blocks}
\to
L^{3,q}\text{ escape for every finite }q.
\]

---

## 9. Consequence

The current survivor is forced all the way to the true Lorentz endpoint:

\[
\boxed{
L^{3,\infty}
\text{ with large critical height and unbounded log-depth.}
}
\]

Thus searching for another finite-index Lorentz upgrade without additional dynamics would only rename the missing log-Cesaro tightness theorem.

The next useful target must exploit the **forced recurrent finite-core payer from M5-109** to break the large weak-L3 endpoint itself, rather than attempting another purely distributional critical-space upgrade.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
