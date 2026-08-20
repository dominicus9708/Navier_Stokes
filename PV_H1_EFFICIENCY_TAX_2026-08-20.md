# H1 Covariance Efficiency Tax — 2026-08-20

Overall status: **NEW SHARP NECESSARY CONDITION FOR THE REMAINING P_V BRANCH — GLOBAL REGULARITY NOT PROVED.**

This note inserts the previously derived `7/9` combined-gradient-covariance cap directly into the exact strain-palinstrophy ledger. The result is a positive, pointwise covariance-defect tax in the nonlinear H1 production.

---

## 1. Exact H1 ledger

Let

\[
P_S=\|\nabla S\|_2^2,
\qquad
H_S=\|\Delta S\|_2^2,
\]

and

\[
\mathcal R_{VI}
=P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right).
\]

Using

\[
\langle-\Delta S,\omega\otimes\omega\rangle=0,
\]

the exact physical H1 identity is

\[
\boxed{
\frac12P_S'+\nu H_S
=-\langle\mathcal R_{VI},-\Delta S\rangle.
}
\]

The previously derived covariance representation is

\[
\boxed{
\langle\mathcal R_{VI},-\Delta S\rangle
=3\int |\nabla S|^2 S:\overline C\,dx,
}
\]

where `Cbar` is positive semidefinite, trace one, and

\[
\lambda_{max}(\overline C)\le\frac79.
\]

---

## 2. Stronger contraction criterion for blowup

Define

\[
\eta_{VI}(t)
=
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{H_S}.
\]

If for some `delta>0`, eventually

\[
\eta_{VI}(t)\le \nu-\delta,
\]

then

\[
\frac12P_S'\le-\delta H_S\le0,
\]

so the H1 strain norm cannot blow up through this terminal interval. Therefore any finite-time singularity must satisfy the necessary condition

\[
\boxed{
\limsup_{t\uparrow T^*}
\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{\|\Delta S\|_2^2}
\ge\nu.
}
\]

For `nu=1`, this is stronger than the norm-only necessary condition

\[
\limsup
\frac{\|\mathcal R_{VI}\|_2}{\|\Delta S\|_2}
\ge1,
\]

because Cauchy--Schwarz gives

\[
-\langle\mathcal R_{VI},-\Delta S\rangle
\le\|\mathcal R_{VI}\|_2\|\Delta S\|_2.
\]

---

## 3. Pointwise covariance defect

Let

\[
s_1\le s_2\le s_3,
\qquad s_1+s_2+s_3=0
\]

be the strain eigenvalues. On the positive-middle-strain region, `s_1` is the unique compressive eigenvalue. Let `e_1` be its eigenvector and define

\[
c_-(x)=e_1^T\overline C e_1,
\]

\[
\boxed{
\varepsilon_C(x)=\frac79-c_-(x)\ge0.
}
\]

For fixed `c_-`, the minimum of `S:Cbar` is obtained by placing all remaining covariance mass on `s_2`. Hence

\[
S:\overline C
\ge
\left(\frac79-\varepsilon_C\right)s_1
+
\left(\frac29+\varepsilon_C\right)s_2.
\]

Therefore

\[
\boxed{
S:\overline C
\ge
\frac79s_1+rac29s_2
+arepsilon_C(s_2-s_1).
}
\]

The final term is a strictly positive loss away from optimal compressive covariance alignment.

---

## 4. Exact H1 efficiency tax

Using `-s_1=s_2+s_3`,

\[
-3S:\overline C
\le
\frac13(5s_2+7s_3)
-3\varepsilon_C(s_2-s_1).
\]

Consequently

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
\int
\left[
\frac13(5s_2+7s_3)
-3\varepsilon_C(s_2-s_1)
\right]
|\nabla S|^2dx.
}
\]

Define the covariance tax

\[
\boxed{
\mathcal D_C
=
3\int
\varepsilon_C(s_2-s_1)|\nabla S|^2dx
\ge0.
}
\]

Then

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
+\mathcal D_C
\le
\frac13\int(5s_2+7s_3)|\nabla S|^2dx.
}
\]

Thus non-saturation is not merely geometric: it removes a definite amount of the H1 production budget.

---

## 5. Max-mid specialization

For the exact max-mid strain state

\[
(s_1,s_2,s_3)=(-2m,m,m),
\qquad m>0,
\]

the bound becomes

\[
\boxed{
-3S:\overline C
\le
(4-9\varepsilon_C)m.
}
\]

Equivalently, since

\[
c_-=\frac79-\varepsilon_C,
\]

\[
\boxed{
-3S:\overline C
=3m(3c_--1)
}
\]

when the remaining covariance is placed in the degenerate positive eigenspace.

Hence max-mid H1 growth requires

\[
\boxed{c_->\frac13.}
\]

An isotropic covariance `Cbar=I/3` gives zero H1 production in the exact max-mid geometry. The maximal possible coefficient `4m` is attained only at the `7/9` cap.

---

## 6. New blowup necessary condition with the tax included

Combining the contraction criterion with the tax gives

\[
\boxed{
\limsup_{t\uparrow T^*}
\frac{
\displaystyle
\int
\left[
\frac13(5s_2+7s_3)
-3\varepsilon_C(s_2-s_1)
\right]
|\nabla S|^2dx
}{
\|\Delta S\|_2^2
}
\ge\nu.
}
\]

Thus a blowup candidate must not only create large compressive strain; it must place the gradient covariance sufficiently anisotropically into the compressive eigendirection to overcome a strictly positive defect tax.

---

## 7. Relation to the tight-core gap

The previous transverse-uncertainty result gives, for a coherent tight core,

\[
\overline\varepsilon_n
\ge
\frac{\|S\|_2^2}
{3R_{\perp,S}^2\|\nabla S\|_2^2}.
\]

Therefore on a transversely tight derivative-controlled coherent-axis branch, the covariance defect cannot tend to zero. The present note shows what that positive gap costs dynamically: it subtracts directly from the only H1 production term capable of balancing viscosity and first-hitting scale damping.

What is **not yet proved** is a universal inequality forcing the taxed production-to-hyperdissipation ratio below `nu`. The current result is therefore a sharp necessary-condition reduction, not a closure of the P_V branch.

---

## 8. Next target

The remaining quantitative problem is now explicit:

\[
\boxed{
\text{Can a tight Type-I core with }\varepsilon_C\ge\varepsilon_0>0
\text{ still satisfy }
\frac{\text{taxed H1 production}}{H_S}\ge\nu
\text{ infinitely often?}
}
\]

Any closure must either:

1. bound the taxed production strictly below `nu H_S` on the non-H/T compact class; or
2. show that maintaining the required compression amplitude forces a new derivative/transport/projective cost.

Status: **THE 7/9 GAP NOW ENTERS THE EXACT PALINSTROPHY BUDGET AS A POSITIVE TAX. FINITE-TIME BLOWUP REQUIRES THE TAXED CONTRACTION-TO-HYPERDISSIPATION RATIO TO REACH AT LEAST VISCOSITY. GLOBAL REGULARITY REMAINS UNPROVED.**