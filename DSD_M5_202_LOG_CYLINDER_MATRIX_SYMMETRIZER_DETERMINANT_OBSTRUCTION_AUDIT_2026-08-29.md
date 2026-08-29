# DSD M5-202 — Log-Cylinder Matrix Symmetrizer and Determinant Obstruction

Date: 2026-08-29

Parent: `DSD_M5_201_FIXED_LAG_CONTACT_WEIGHTED_RETURN_SUMMABILITY_FIREWALL_2026-08-29.md`

Status: **NEW MATRIX-SYMMETRIZER FIREWALL / A POSITIVE-DEFINITE MATRIX WEIGHT CAN LOCALLY SYMMETRIZE THE GENERIC CRITICAL DRIFT+STRAIN SYSTEM ALONG CHARACTERISTICS, BUT GLOBAL UNIFORM ELLIPTICITY IS OBSTRUCTED BY AN EXACT DETERMINANT COHOMOLOGY EQUATION / INCOMPRESSIBILITY GIVES `div_cyl a=-Phi_r`, AND TRACE-FREE STRAIN THEN FORCES `a·grad log det H=3 Phi_r` FOR EXACT SKEW-SYMMETRIZATION / THUS THE MATRIX ANSATZ CANNOT BYPASS THE SCALAR RADIAL-COMPONENT OBSTRUCTION: NONZERO ORBITWISE MEAN `Phi_r` CAUSES EXPONENTIAL DETERMINANT DRIFT, WHILE MIXED-SIGN RADIAL ORBITS PREVENT A UNIVERSAL SIGNED COERCIVE SYMMETRIZER / THE M5-194A EXPLICIT ADMISSIBLE TAIL ALREADY FORCES EXPONENTIAL DET-H GROWTH/DECAY ON ITS POLAR CHARACTERISTICS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Critical cylinder transport

Use the log-radius variable

\[
y=-\log r.
\]

For a critical tail

\[
B_T
=
\frac1r
(\Phi_r e_r+\Phi_\tau),
\]

the scale-normalized first-order transport is

\[
\boxed{
T_\Phi
=
-\Phi_r\partial_y
+
\Phi_\tau\cdot\nabla_{S^2}.
}
\]

Define the cylinder vector field

\[
\boxed{
a
:=
(-\Phi_r,\Phi_\tau).
}
\]

Then

\[
T_\Phi=a\cdot D_{cyl}.
\]

---

## 2. Cylinder divergence from physical incompressibility

The physical divergence-free condition for the critical tail is

\[
\boxed{
\Phi_r
-
\partial_y\Phi_r
+
\operatorname{div}_{S^2}\Phi_\tau
=0.
}
\]

Hence

\[
\operatorname{div}_{S^2}\Phi_\tau
=
\partial_y\Phi_r-\Phi_r.
\]

Therefore the ordinary product-cylinder divergence of `a` is

\[
\begin{aligned}
\operatorname{div}_{cyl}a
&=
\partial_y(-\Phi_r)
+
\operatorname{div}_{S^2}\Phi_\tau\\
&=
-\partial_y\Phi_r
+
\partial_y\Phi_r-\Phi_r.
\end{aligned}
\]

Thus

\[
\boxed{
\operatorname{div}_{cyl}a=-\Phi_r.
}
\]

This identity is exact.

It explains why the critical drift is not skew on the flat cylinder even though the physical three-dimensional field is divergence free: the radial Jacobian has been removed by the critical normalization.

---

## 3. Scalar L2 adjoint

For scalar test functions on the product measure `dy dS`,

\[
T_\Phi^*
=
-T_\Phi
-
\operatorname{div}_{cyl}a.
\]

Hence

\[
\boxed{
T_\Phi^*
=
-T_\Phi+\Phi_r.
}
\]

The symmetric part is therefore

\[
\boxed{
\frac12(T_\Phi+T_\Phi^*)
=
\frac12\Phi_r.
}
\]

This recovers, in cylinder-energy language, the radial-component obstruction isolated in M5-194A/E.

---

## 4. Add the critical strain operator

Let the critical vector equation contain the trace-free symmetric strain matrix

\[
\Sigma(y,\theta,t),
\qquad
\operatorname{tr}\Sigma=0,
\]

schematically through

\[
\mathcal A W
:=
T_\Phi W-\Sigma W.
\]

The sign convention is chosen to match the usual vorticity-side lower-order operator. Reversing the convention only reverses the corresponding matrix signs; the determinant obstruction below is unchanged in substance.

---

## 5. Matrix-weighted energy

Let

\[
H(y,\theta,t)=H^T>0
\]

be a smooth positive-definite matrix field.

Use the weighted quadratic energy

\[
E_H[W]
:=
\frac12
\int
W^THW\,dy\,dS.
\]

For the transport term,

\[
\int W^TH(a\cdot D)W
=
-\frac12
\int
W^T
\left[
(a\cdot D)H
+
(\operatorname{div}a)H
\right]
W.
\]

Using

\[
\operatorname{div}a=-\Phi_r,
\]

and adding the strain term gives

\[
2\langle HW,\mathcal AW\rangle
=
\int W^T K_H W,
\]

where

\[
\boxed{
K_H
=
-(a\cdot D)H
+
\Phi_rH
-
(H\Sigma+\Sigma H).
}
\]

This is the exact symmetric matrix residual of the critical transport+strain operator in the `H` energy.

---

## 6. Exact skew-symmetrizer equation

To make the entire first-order critical operator skew in the weighted energy, one would require

\[
K_H=0.
\]

Equivalently,

\[
\boxed{
(a\cdot D)H
=
\Phi_rH
-
(H\Sigma+\Sigma H).
}
\]

Along a cylinder characteristic

\[
\frac{dX}{ds}=a(X(s)),
\]

this becomes the matrix Lyapunov ODE

\[
\boxed{
\frac{dH}{ds}
=
\Phi_rH
-
H\Sigma-\Sigma H.
}
\]

For any positive initial matrix `H(0)>0`, the ODE has a local positive-definite solution.

Therefore there is **no local algebraic obstruction** to a matrix symmetrizer.

The issue is global boundedness/uniform ellipticity along the full cylinder flow.

---

## 7. Determinant equation

Take the trace after multiplying by `H^{-1}`.

Since

\[
\frac{d}{ds}\log\det H
=
\operatorname{tr}(H^{-1}H'),
\]

we obtain

\[
\begin{aligned}
\frac{d}{ds}\log\det H
&=
3\Phi_r
-
\operatorname{tr}(H^{-1}H\Sigma)
-
\operatorname{tr}(H^{-1}\Sigma H)\\
&=
3\Phi_r
-2\operatorname{tr}\Sigma.
\end{aligned}
\]

Because incompressible strain is trace free,

\[
\boxed{
\frac{d}{ds}\log\det H
=3\Phi_r(X(s)).
}
\]

Equivalently in PDE form,

\[
\boxed{
(a\cdot D)\log\det H
=3\Phi_r.
}
\]

This is the determinant cohomology equation.

---

## 8. Orbitwise mean obstruction

Suppose a characteristic is periodic with period `P` and `H` is single-valued/periodic along it.

Then

\[
0
=
\log\det H(P)-\log\det H(0)
=
3\int_0^P\Phi_r(X(s))ds.
\]

Therefore a necessary condition is

\[
\boxed{
\frac1P
\int_0^P\Phi_r(X(s))ds=0.
}
\]

More generally, on a recurrent characteristic supporting an invariant time average, a bounded determinant requires zero mean radial component:

\[
\boxed{
\langle\Phi_r\rangle_{orbit}=0.
}
\]

If instead

\[
\langle\Phi_r\rangle_{orbit}=m_r\ne0,
\]

then

\[
\det H(s)
\sim
\exp(3m_rs)
\]

in the averaged sense, so a globally uniform ellipticity bound

\[
cI\le H\le CI
\]

is impossible.

---

## 9. Matrix freedom does not remove the scalar radial obstruction

Factor

\[
H=e^hG,
\qquad
\det G=1.
\]

Then

\[
\det H=e^{3h},
\]

so the determinant equation reduces to

\[
\boxed{
(a\cdot D)h=\Phi_r.
}
\]

Thus one scalar degree of the matrix symmetrizer must solve exactly a scalar transport/cohomology problem for `Phi_r`.

The remaining determinant-one matrix `G` may redistribute anisotropic strain, but it cannot change this scalar solvability condition.

Hence

\[
\boxed{
\text{matrix symmetrizer}
\not\supset
\text{a universal escape from the radial scalar obstruction}.
}
\]

This is the central firewall.

---

## 10. Explicit M5-194A admissible counterexample

Reuse the divergence-free critical tail

\[
\boxed{
\Phi_r=\cos\theta,
\qquad
\Phi_\tau
=-\frac12\sin\theta\,e_\theta.
}
\]

Then

\[
a
=
(-\cos\theta,
-\tfrac12\sin\theta\,e_\theta).
\]

At the north pole

\[
\theta=0,
\qquad
\Phi_r=1,
\qquad
\Phi_\tau=0.
\]

The characteristic is purely in the `y` direction and the determinant equation gives

\[
\frac{d}{ds}\log\det H=3.
\]

Therefore

\[
\boxed{
\det H(s)=\det H(0)e^{3s}.
}
\]

At the south pole,

\[
\theta=\pi,
\qquad
\Phi_r=-1,
\]

so

\[
\boxed{
\det H(s)=\det H(0)e^{-3s}.
}
\]

No single globally bounded uniformly elliptic matrix symmetrizer can accommodate both infinite polar characteristics.

This is an explicit admissible critical-drift counterexample, not merely a topological concern.

---

## 11. Approximate/dissipative symmetrizer trace identity

For a general `H`, the normalized trace of the symmetric residual is

\[
\begin{aligned}
\operatorname{tr}(H^{-1}K_H)
&=
-(a\cdot D)\log\det H
+3\Phi_r
-2\operatorname{tr}\Sigma\\
&=
\boxed{
-(a\cdot D)\log\det H+3\Phi_r.
}
\end{aligned}
\]

Therefore even an approximate matrix symmetrizer cannot make the normalized trace residual small on every recurrent orbit unless the determinant derivative compensates the orbitwise radial mean.

If `H` is uniformly bounded and recurrent/single-valued, the derivative term has zero orbit mean, so

\[
\boxed{
\left\langle
\operatorname{tr}(H^{-1}K_H)
\right\rangle_{orbit}
=
3\langle\Phi_r\rangle_{orbit}.
}
\]

Thus nonzero mean radial drift survives every bounded matrix change of metric at the trace level.

---

## 12. Uniform signed coercivity is also orbit-constrained

Suppose one seeks

\[
K_H\ge\kappa H
\]

for some fixed `kappa>0` along a recurrent orbit.

Taking normalized trace gives

\[
-(a\cdot D)\log\det H+3\Phi_r
\ge3\kappa.
\]

Averaging over a periodic/recurrent orbit with bounded `H`,

\[
\boxed{
\langle\Phi_r\rangle_{orbit}
\ge\kappa.
}
\]

Likewise the opposite coercive sign requires the opposite orbitwise radial sign.

Because divergence-free zero spherical flux does not force all characteristics to have one radial sign, no universal same-sign first-order coercive metric follows from the current structural hypotheses.

---

## 13. Pure tangential special case

If

\[
\Phi_r=0,
\]

then

\[
\operatorname{div}_{cyl}a=0
\]

and the determinant obstruction disappears:

\[
(a\cdot D)\log\det H=0.
\]

One may choose `det H` constant along characteristics.

However the determinant-one part must still solve

\[
(a\cdot D)G
=-(G\Sigma+\Sigma G)
\]

modulo the determinant constraint.

On closed angular orbits, a periodic uniformly elliptic `G` exists only if the strain monodromy preserves some positive quadratic form. Hyperbolic Floquet growth of the trace-free strain destroys such bounded periodicity.

Thus even the pure tangential branch is favorable but not universally symmetrizable.

The exact Killing/stationary subclass from M5-194G remains the natural special case.

---

## 14. Relation to scalar adapted weights

M5-194A proved that a scalar phase satisfying exact streamline adaptation and a uniform positive radial slope fails for the explicit critical tail because the poles force degeneration.

M5-202 shows the matrix analogue:

- local matrix adaptation is possible;
- the determinant must solve a scalar radial cohomology equation;
- the same polar radial drift causes exponential metric degeneration.

Therefore the scalar and matrix no-go results are consistent and nested rather than independent accidents.

---

## 15. What remains possible

This audit does **not** rule out all matrix methods.

Still open are:

1. matrix symmetrizers on special zero-orbit-mean radial subclasses;
2. finite-window symmetrizers whose ellipticity constants are allowed to depend on window length;
3. two-parameter Carleman limits where matrix growth is balanced against `beta` and support separation;
4. nonlocal/pseudodifferential symmetrizers rather than pointwise matrix metrics;
5. direct backward-uniqueness arguments that do not attempt to symmetrize the entire critical drift.

The only claim closed here is the universal globally bounded **local matrix-metric** shortcut under the current generic critical-tail hypotheses.

---

## 16. Updated critical-drift frontier

The main endpoint now has the sharper fork

\[
\boxed{
\begin{aligned}
\text{generic radial critical drift}
&\to
\text{determinant cohomology obstruction},\\
\text{zero-orbit-mean radial drift}
&\to
\text{anisotropic monodromy problem},\\
\text{pure tangential Killing drift}
&\to
\text{favorable skew/commuting subclass},\\
\text{failure of local metric symmetrization}
&\to
\text{nonlocal BU / finite-window Carleman frontier}.
\end{aligned}
}
\]

Thus the remaining generic proof route should not assume that a positive-definite pointwise matrix weight can absorb an arbitrary non-small critical `1/r` drift globally.

---

## 17. DSD verdict

### PROVED

- `div_cyl a=-Phi_r`;
- exact matrix-weighted symmetric residual `K_H`;
- exact local skew-symmetrizer Lyapunov equation;
- determinant equation `a·grad log det H=3 Phi_r` for trace-free strain;
- zero orbit-mean `Phi_r` is necessary for bounded periodic/recurrent exact symmetrization;
- nonzero orbit mean forces exponential determinant drift;
- explicit M5-194A tail rules out a global bounded matrix symmetrizer through its polar characteristics;
- approximate bounded symmetrizers retain the radial mean in the normalized trace residual;
- uniform signed coercivity requires corresponding orbitwise radial sign.

### OPEN

- finite-window matrix Carleman schemes;
- zero-mean radial subclasses;
- anisotropic Floquet/monodromy rigidity;
- nonlocal/pseudodifferential symmetrization;
- generic critical backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 18. Next target

The most informative surviving local-metric branch is the **zero-orbit-mean radial class**.

There the determinant obstruction vanishes, so the next question is whether the determinant-one symmetrizer can remain uniformly elliptic.

Along a characteristic, factor out the scalar determinant and write the trace-free strain cocycle. The next audit should compute its monodromy/Floquet exponents and show that a bounded positive metric exists iff the cocycle has zero hyperbolic Lyapunov exponent (equivalently, its monodromy is conjugate to an orthogonal action in the relevant metric).

That would separate the truly skew/elliptic critical drifts from the hyperbolic ones and determine whether any nontrivial matrix-symmetrizable survivor remains.