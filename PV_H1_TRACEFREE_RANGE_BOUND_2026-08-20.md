# Sharp Trace-Free Range Bound for P_V H1 Production — 2026-08-20

Overall status: **NEW UNIVERSAL ALGEBRAIC H1 PRODUCTION BOUND — GLOBAL REGULARITY NOT PROVED.**

This note improves the covariance-only `7/9` estimate by exploiting the exact algebra of squares of symmetric trace-free `3x3` matrices. The resulting H1 production bound is independent of any chosen covariance axis and gives a strict efficiency loss away from max-mid strain geometry.

---

## 1. A 3x3 trace-free square identity

Let `G` be a symmetric trace-free `3x3` matrix. Define

\[
(G^2)^\circ
=G^2-\frac13|G|_F^2I.
\]

For a trace-free `3x3` matrix, Newton's identities give

\[
\operatorname{tr}(G^4)
=\frac12\left(\operatorname{tr}(G^2)\right)^2
=\frac12|G|_F^4.
\]

Therefore

\[
\begin{aligned}
|(G^2)^\circ|_F^2
&=\operatorname{tr}(G^4)-\frac13|G|_F^4\\
&=\frac16|G|_F^4.
\end{aligned}
\]

Hence

\[
\boxed{
|(G^2)^\circ|_F
=\frac1{\sqrt6}|G|_F^2.
}
\]

---

## 2. Sharp bilinear inequality

Let `S` also be symmetric and trace free. Since `S:I=0`,

\[
\operatorname{tr}(SG^2)
=S:(G^2)^\circ.
\]

Cauchy--Schwarz gives the exact sharp bound

\[
\boxed{
|\operatorname{tr}(SG^2)|
\le
\frac1{\sqrt6}|S|_F|G|_F^2.
}
\]

Equality holds iff `S` is parallel or antiparallel to `(G^2)^circ`. For the most negative contraction,

\[
(G^2)^\circ
\parallel -S.
\]

This condition is stronger than the eigenvalue cap on the aggregate range covariance.

---

## 3. Application to the exact H1 residual

Recall

\[
G_k=\partial_kS,
\]

\[
M_{sp,ij}=\langle G_i,G_j\rangle_F,
\qquad
M_{rg}=\sum_kG_k^2,
\]

and

\[
\langle\mathcal R_{VI},-\Delta S\rangle
=\int S:M_{sp}+2\int S:M_{rg}.
\]

Let

\[
s_1\le s_2\le s_3
\]

be the strain eigenvalues. Since `M_sp` is positive semidefinite with trace `|grad S|^2`,

\[
S:M_{sp}
\ge
s_1|\nabla S|^2.
\]

For the range term, applying the sharp trace-free inequality to each `G_k` gives

\[
S:G_k^2
\ge
-\frac1{\sqrt6}|S||G_k|^2.
\]

Summing over `k`,

\[
S:M_{rg}
\ge
-\frac1{\sqrt6}|S||\nabla S|^2.
\]

Therefore

\[
\boxed{
\langle\mathcal R_{VI},-\Delta S\rangle
\ge
\int
\left(
s_1-\frac{2}{\sqrt6}|S|
\right)|\nabla S|^2dx.
}
\]

Equivalently, the nonlinear H1 production obeys

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
\int
\left(
-s_1+\frac{2}{\sqrt6}|S|
\right)|\nabla S|^2dx.
}
\]

---

## 4. Universal scalar cap

For a trace-free symmetric `3x3` strain,

\[
-s_1\le\sqrt{\frac23}|S|
=\frac{2}{\sqrt6}|S|.
\]

Hence

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
\frac4{\sqrt6}
\int|S||\nabla S|^2dx.
}
\]

The constant `4/sqrt(6)` is attained algebraically only in the max-mid eigenvalue geometry together with simultaneous saturation of the spatial and range contractions.

This improves the previous covariance-only scalar coefficient obtained from the `(5s_2+7s_3)/3` cap.

---

## 5. Fixed positive-eigengap loss

Write the positive-middle-strain eigenvalues as

\[
s_1=-2m,
\qquad
s_2=m-d,
\qquad
s_3=m+d,
\qquad 0\le d<m.
\]

Then

\[
|S|^2=6m^2+2d^2,
\]

so

\[
\frac{|S|}{\sqrt6}
=\sqrt{m^2+\frac{d^2}{3}}.
\]

The sharp pointwise H1 production coefficient becomes

\[
\boxed{
2m+2\sqrt{m^2+\frac{d^2}{3}}.
}
\]

At fixed `|S|`, the maximum possible coefficient is

\[
\frac4{\sqrt6}|S|,
\]

and is attained only when `d=0`.

The efficiency fraction is

\[
\boxed{
\Theta_{gap}(d/m)
=
\frac12
+
\frac{1}{2\sqrt{1+\frac13(d/m)^2}}
<1
\qquad(d>0).
}
\]

Thus if

\[
\frac dm\ge\eta>0,
\]

then

\[
\boxed{
\Theta_{gap}
\le
\frac12+
\frac1{2\sqrt{1+\eta^2/3}}
=:\theta_\eta<1.
}
\]

This is a universal fixed-gap H1 efficiency loss requiring no spatial tightness or covariance-axis assumption.

---

## 6. Explicit quadratic loss near max-mid

The difference between the max-mid scalar cap and the actual fixed-`d` coefficient is

\[
\begin{aligned}
\mathcal G_{mm}
&=
\frac4{\sqrt6}|S|
-
\left(-s_1+\frac2{\sqrt6}|S|\right)\\
&=
2\sqrt{m^2+\frac{d^2}{3}}-2m\\
&=
\frac{2d^2/3}{\sqrt{m^2+d^2/3}+m}.
\end{aligned}
\]

Since `d<m`,

\[
\sqrt{m^2+d^2/3}+m
<\frac73m,
\]

and therefore

\[
\boxed{
\mathcal G_{mm}
\ge
\frac{2}{7}\frac{d^2}{m}.
}
\]

Thus the H1 efficiency defect is quadratic in the positive-eigenvalue splitting near max-mid.

---

## 7. Equality geometry

To attain the full scalar cap simultaneously, one needs:

1. spatial covariance saturation:
\[
S:M_{sp}=s_1|\nabla S|^2,
\]
so the spatial derivative covariance lies entirely in the compressive direction;

2. range saturation for every active derivative:
\[
(G_k^2)^\circ
\parallel -S.
\]

3. max-mid strain eigenvalues:
\[
s_2=s_3.
\]

These are far stronger than merely requiring a large positive middle eigenvalue.

The earlier exact/near max-mid rigidity calculations and transverse-tightness arguments can therefore be attached directly to the equality/near-equality regime of this new bound.

---

## 8. Consequence for the remaining P_V branch

The non-H/T recurrent P_V branch must now either:

- remain quantitatively near max-mid in the derivative-active region; or
- accept a universal fixed fractional loss `1-theta_eta` in its maximum possible H1 replenishment efficiency.

This removes the need to use the `7/9` cap alone to establish a fixed-gap loss. The `7/9` covariance analysis remains valuable for the near-max-mid equality regime, where it provides spatial/range rigidity and transverse uncertainty.

What remains unproved is the final comparison of the reduced production coefficient against viscous hyperdissipation and first-hitting scale damping on the entire non-H/T compact class.

Status: **A SHARP TRACE-FREE MATRIX IDENTITY GIVES A UNIVERSAL P_V H1 PRODUCTION CAP. ANY FIXED POSITIVE EIGENGAP PRODUCES A STRICT FRACTIONAL EFFICIENCY LOSS; FULL EFFICIENCY REQUIRES MAX-MID PLUS SIMULTANEOUS SPATIAL/RANGE SATURATION. GLOBAL REGULARITY REMAINS UNPROVED.**