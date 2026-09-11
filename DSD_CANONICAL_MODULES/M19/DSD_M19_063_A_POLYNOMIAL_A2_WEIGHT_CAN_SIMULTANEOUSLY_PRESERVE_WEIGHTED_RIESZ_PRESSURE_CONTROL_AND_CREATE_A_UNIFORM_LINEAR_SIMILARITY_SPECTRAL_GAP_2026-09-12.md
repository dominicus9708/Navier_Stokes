# M19-063 — A polynomial A2 weight can simultaneously preserve weighted Riesz pressure control and create a uniform linear similarity spectral gap

**Date:** 2026-09-12  
**Status:** CALCULATION / GLOBAL FACTOR RIGIDITY / POSITIVE PRESSURE-COMPATIBLE COERCIVITY RESULT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-062 found a genuine Ornstein--Uhlenbeck spectral gap in the Gaussian weighted norm, but the Gaussian weight is not Muckenhoupt \(A_2\), so standard weighted Calderon--Zygmund/Riesz pressure control is unavailable.

This module asks whether one can retain both properties:

1. coercivity of the linear similarity operator;
2. \(A_2\)-compatibility for the incompressible pressure.

The answer is yes.  A regularized polynomial weight

\[
\boxed{
w_{a,\kappa}(y):=(1+\kappa|y|^2)^{-a/2}
}
\]

has a nonempty parameter range in which it belongs to \(A_2(\mathbb R^3)\) and the weighted linear similarity energy coefficient is uniformly strictly negative.

This is a positive structural result.  It does not yet control the nonlinear transport, strain, and pressure defects.

## 2. Linear weighted difference calculation

For the velocity difference

\[
W:=U-V,
\]

the linear similarity part is

\[
\mathcal L_{lin}W
:=
\nu\Delta W
-\frac12W
-\frac12(y\cdot\nabla)W.
\]

Let \(w>0\) be a smooth scalar weight.  Componentwise integration by parts gives

\[
\int W\cdot\nu\Delta W\,w
=
-\nu\int|\nabla W|^2w
+\frac\nu2\int|W|^2\Delta w.
\]

Also

\[
-\frac12\int W\cdot(y\cdot\nabla W)w
=
\frac14\int|W|^2\nabla\cdot(yw)
=
\frac34\int|W|^2w
+\frac14\int|W|^2y\cdot\nabla w.
\]

Combining the explicit \(-\frac12W\) term,

\[
\boxed{
\int W\cdot\mathcal L_{lin}W\,w
=
-\nu\int|\nabla W|^2w
+
\int C_w(y)|W|^2w,
}
\]

where

\[
\boxed{
C_w(y)
=
\frac\nu2\frac{\Delta w}{w}
+
\frac14\left(
1+
\frac{y\cdot\nabla w}{w}
\right).
}
\]

Thus a uniform bound

\[
\sup_y C_w(y)<0
\]

is exactly a weighted linear spectral gap.

## 3. Polynomial A2 candidate

Set

\[
\boxed{
w(y)=(1+\kappa r^2)^{-a/2},
\qquad r=|y|,
\qquad s:=\kappa r^2.
}
\]

Then

\[
\boxed{
\frac{y\cdot\nabla w}{w}
=-\frac{as}{1+s}.
}
\]

A direct radial computation in dimension three gives

\[
\boxed{
\frac{\Delta w}{w}
=
a\kappa
\frac{(a-1)s-3}{(1+s)^2}.
}
\]

Introduce

\[
\boxed{\beta:=\nu\kappa.}
\]

Then

\[
4C_w(s)
=
\frac{N_{a,\beta}(s)}{(1+s)^2},
\]

with the exact quadratic numerator

\[
\boxed{
N_{a,\beta}(s)
=
(1-6a\beta)
+
\left[(2-a)+2a\beta(a-1)\right]s
+
(1-a)s^2.
}
\]

## 4. A nonempty uniformly coercive parameter window

Choose

\[
\boxed{\frac52<a<3.}
\]

Then choose \(\beta\) so that

\[
\boxed{
\frac1{6a}<\beta
\le
\frac{a-2}{2a(a-1)}.
}
\]

This interval is nonempty exactly because

\[
\frac1{6a}
<
\frac{a-2}{2a(a-1)}
\iff
3(a-2)>a-1
\iff
\boxed{a>\frac52.}
\]

Under these conditions,

\[
1-6a\beta<0,
\]

\[
(2-a)+2a\beta(a-1)\le0,
\]

and

\[
1-a<0.
\]

Therefore, for every \(s\ge0\),

\[
\boxed{N_{a,\beta}(s)<0.}
\]

Since \(C_w\) is continuous on \([0,\infty)\) and

\[
\lim_{s\to\infty}C_w(s)=\frac{1-a}{4}<0,
\]

there exists a parameter-dependent constant

\[
\boxed{c_{gap}(a,\beta)>0}
\]

such that

\[
\boxed{C_w(y)\le-c_{gap}<0\qquad\text{for all }y.}
\]

Hence

\[
\boxed{
\int W\cdot\mathcal L_{lin}W\,w
\le
-\nu\|\nabla W\|_{L^2(w)}^2
-c_{gap}\|W\|_{L^2(w)}^2.
}
\]

## 5. Explicit example

Take

\[
\boxed{a=\frac{11}{4},
\qquad
\beta=0.07.}
\]

Then

\[
1-6a\beta
=1-1.155
=-0.155,
\]

\[
(2-a)+2a\beta(a-1)
=-0.75+0.67375
=-0.07625,
\]

and

\[
1-a=-1.75.
\]

Thus every coefficient of \(N_{a,\beta}\) is nonpositive and the constant and quadratic coefficients are strictly negative.

The physical weight parameter is

\[
\boxed{\kappa=\beta/\nu.}
\]

So the spatial weighting scale adapts naturally to the viscosity.

## 6. A2 compatibility

At large radius,

\[
w(y)\sim C|y|^{-a}.
\]

In \(\mathbb R^3\), the power weight \(|y|^\alpha\) belongs to \(A_2\) iff

\[
-3<\alpha<3.
\]

For the present regularized weight, \(\alpha=-a\).  Therefore every

\[
\boxed{0<a<3}
\]

lies in the \(A_2\) range, and in particular the coercive window

\[
\boxed{\frac52<a<3}
\]

is pressure-compatible with standard weighted Calderon--Zygmund theory.

Thus the two requirements that failed to coexist in the Gaussian weight do coexist here:

\[
\boxed{
\text{uniform linear spectral gap}
+
\text{weighted Riesz-transform boundedness}.
}
\]

## 7. Exact full weighted difference identity

Return to the full difference equation

\[
\partial_\theta W
=\mathcal L_{lin}W
-(U\cdot\nabla)W
-(W\cdot\nabla)V
-\nabla Q.
\]

Then

\[
\boxed{
\begin{aligned}
\frac12\frac d{d\theta}\|W\|_{L^2(w)}^2
&+
\nu\|\nabla W\|_{L^2(w)}^2
+c_{gap}\|W\|_{L^2(w)}^2\\
&\le
I_{tr}+I_{str}+I_p,
\end{aligned}
}
\]

where

\[
I_{tr}
:=
-\int W\cdot(U\cdot\nabla W)w,
\]

\[
I_{str}
:=
-\int W_iW_j\partial_jV_i\,w,
\]

and

\[
I_p
:=
-\int W\cdot\nabla Q\,w.
\]

The remainder of the closure problem is therefore purely nonlinear/nonlocal; the linear weighted geometry is no longer an obstruction.

## 8. Useful derivative bound for the weight

For later estimates,

\[
|\nabla\log w|
=
\frac{a\kappa r}{1+\kappa r^2}.
\]

The elementary maximum

\[
\max_{r\ge0}\frac{\kappa r}{1+\kappa r^2}
=\frac{\sqrt\kappa}{2}
\]

gives

\[
\boxed{
\|\nabla\log w\|_{L^\infty}
\le
\frac{a\sqrt\kappa}{2}.
}
\]

This controls the weighted transport defect and the integration-by-parts form of the pressure defect, provided the velocity and pressure can be estimated in the same weighted class.

## 9. Significance

M19-063 changes the weighted-contraction picture from a pure firewall into a conditional positive route.

The previous Gaussian situation was

\[
\text{gap}
\quad\text{but no standard pressure control}.
\]

The polynomial weight gives

\[
\boxed{
\text{gap}
+
\text{A2 pressure compatibility}.
}
\]

Therefore a genuine contraction theorem is no longer blocked at the linear/pressure-weight design level.

The key unresolved issue is whether the nonlinear defects are smaller than \(c_{gap}\) on the retained recurrent corridor.

## 10. Certified / not certified

### Certified

1. Exact weighted linear coefficient \(C_w\).
2. Exact numerator \(N_{a,\beta}\) for the regularized polynomial weight.
3. Nonempty coercive window
   \[
   \frac52<a<3,
   \qquad
   \frac1{6a}<\beta\le\frac{a-2}{2a(a-1)}.
   \]
4. Uniform negative linear coefficient in that window.
5. The same weight belongs to \(A_2(\mathbb R^3)\).
6. Therefore pressure-compatible linear similarity coercivity exists.

### Not certified

1. Absorption of transport, strain, and pressure defects.
2. Smallness of the recurrent corridor in the weighted contraction norm.
3. Uniqueness/triviality of the recurrent hull.
4. Global 3D Navier--Stokes regularity.

## 11. Next calculation

M19-064 should estimate the three nonlinear defects under the strongest bounds already certified on the compact recurrent corridor.

In particular:

- weighted transport should be controlled by \(\|U\|_\infty\|\nabla\log w\|_\infty\);
- weighted pressure should use the \(A_2\) Riesz bound for
  \[
  -\Delta Q=\partial_i\partial_j(U_iW_j+W_iV_j);
  \]
- the strain term
  \[
  -\int W_iW_j\partial_jV_iw
  \]
  is expected to be the hardest part because bounded vorticity does not automatically imply bounded strain.

The exact outcome should determine whether the factor-rigidity theorem reduces to one quantitative strain-vs-gap condition.

---

\[
\boxed{\text{M19-063 COMPLETE; A PRESSURE-COMPATIBLE A2 WEIGHT WITH A TRUE LINEAR SIMILARITY GAP EXISTS.}}
\]
