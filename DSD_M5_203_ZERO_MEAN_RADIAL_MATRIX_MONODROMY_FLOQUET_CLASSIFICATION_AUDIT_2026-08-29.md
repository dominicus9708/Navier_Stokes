# DSD M5-203 — Zero-Mean Radial Matrix Monodromy / Floquet Classification

Date: 2026-08-29

Parent: `DSD_M5_202_LOG_CYLINDER_MATRIX_SYMMETRIZER_DETERMINANT_OBSTRUCTION_AUDIT_2026-08-29.md`

Status: **POSITIVE EXACT CLASSIFICATION / AFTER THE DETERMINANT COHOMOLOGY OBSTRUCTION IS REMOVED, THE DET-ONE MATRIX SYMMETRIZER IS GOVERNED BY THE TRACE-FREE STRAIN COCYCLE / ON A PERIODIC CHARACTERISTIC A POSITIVE PERIODIC METRIC EXISTS IFF THE MONODROMY PRESERVES SOME POSITIVE QUADRATIC FORM, EQUIVALENTLY IFF IT IS SIMILAR TO AN ORTHOGONAL MATRIX / HYPERBOLIC FLOQUET MULTIPLIERS AND NONSEMISIMPLE UNIT-MODULUS JORDAN BLOCKS ARE EXCLUDED / HOWEVER NONZERO TIME-DEPENDENT STRAIN CAN HAVE IDENTITY OR ELLIPTIC MONODROMY, SO NONZERO STRAIN ALONE IS NOT A NO-GO / THE MATRIX-SYMMETRIZABLE SURVIVOR IS REDUCED TO AN ELLIPTIC FLOQUET SUBCLASS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Remove the determinant scalar

On the exact skew-symmetrizer equation

\[
(a\cdot D)H
=
\Phi_rH-(H\Sigma+\Sigma H),
\]

write

\[
\boxed{H=e^hG}
\]

with

\[
\det G=1.
\]

The scalar factor satisfies

\[
\boxed{(a\cdot D)h=\Phi_r.}
\]

Assume the determinant cohomology condition is solvable with bounded `h`, for example on a periodic characteristic with

\[
\int_0^P\Phi_r\,ds=0.
\]

Then the determinant-one matrix obeys

\[
\boxed{
(a\cdot D)G
=-(G\Sigma+\Sigma G).
}
\]

Along one characteristic,

\[
\boxed{
G'=-G\Sigma-\Sigma G.
}
\]

Because `tr Sigma=0`, `det G` remains constant.

---

## 2. Fundamental strain cocycle

Let `U(s)` solve

\[
\boxed{
U'=\Sigma(s)U,
\qquad
U(0)=I.
}
\]

Since

\[
\operatorname{tr}\Sigma=0,
\]

Liouville's formula gives

\[
\boxed{\det U(s)=1.}
\]

Hence

\[
U(s)\in SL(3,\mathbb R).
\]

For any positive matrix `G_0`, define

\[
\boxed{
G(s)=U(s)^{-T}G_0U(s)^{-1}.
}
\]

Differentiating gives

\[
G'
=-\Sigma G-G\Sigma,
\]

because `Sigma=Sigma^T`.

Thus this is the general positive solution of the det-one metric transport equation.

---

## 3. Periodic characteristic and monodromy

Suppose the cylinder characteristic and coefficients are periodic with period `P`.

Define the monodromy matrix

\[
\boxed{M:=U(P)\in SL(3,\mathbb R).}
\]

A periodic metric requires

\[
G(P)=G(0)=G_0.
\]

Using the explicit solution,

\[
M^{-T}G_0M^{-1}=G_0.
\]

Equivalently,

\[
\boxed{M^TG_0M=G_0.}
\]

This is the exact matrix fixed-point equation.

---

## 4. Geometric meaning

The equation

\[
M^TG_0M=G_0,
\qquad
G_0>0,
\]

means that `M` is an isometry of the positive inner product

\[
\langle x,y\rangle_{G_0}=x^TG_0y.
\]

Let

\[
C=G_0^{1/2}MG_0^{-1/2}.
\]

Then

\[
C^TC=I.
\]

Therefore

\[
\boxed{
M
\text{ preserves a positive metric}
\iff
M\text{ is similar over }\mathbb R\text{ to an orthogonal matrix}.
}
\]

Since `det M=1`, the orthogonal representative lies in `SO(3)`.

---

## 5. Spectral classification

For a real finite-dimensional matrix, similarity to an orthogonal matrix is equivalent to

1. all complex eigenvalues have modulus one;
2. the matrix is semisimple over `C` (no nontrivial Jordan blocks).

Thus periodic positive symmetrization requires

\[
\boxed{
|\lambda_j(M)|=1
\quad\text{for all }j,
}
\]

and

\[
\boxed{M\text{ diagonalizable over }\mathbb C.}
\]

Because `M` is real `3 x 3` with determinant one, its elliptic possibilities are, schematically,

\[
\{1,e^{i\vartheta},e^{-i\vartheta}\}
\]

including the identity and finite rotations.

---

## 6. Hyperbolic monodromy is impossible

If `M` has an eigenvalue

\[
|\lambda|>1,
\]

then `det M=1` forces another multiplier with modulus below one.

For an eigenvector `v`, repeated cycles give

\[
|M^nv|\sim|\lambda|^n.
\]

No positive metric satisfying

\[
M^TG_0M=G_0
\]

can preserve such exponential growth.

Therefore

\[
\boxed{
\text{hyperbolic Floquet multiplier}
\Longrightarrow
\text{no bounded periodic matrix symmetrizer}.
}
\]

This is a strict matrix no-go beyond the scalar determinant condition.

---

## 7. Unit-modulus Jordan shear is also impossible

Zero Lyapunov exponent alone is not sufficient.

For example, a unipotent monodromy

\[
M=
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix}
\]

has all eigenvalues on the unit circle, but

\[
M^n
=
\begin{pmatrix}
1&n&0\\
0&1&0\\
0&0&1
\end{pmatrix}
\]

has polynomial growth.

Such an `M` cannot be similar to an orthogonal matrix and cannot preserve a positive-definite quadratic form.

Thus

\[
\boxed{
\text{zero exponential Lyapunov exponents}
\not\Longrightarrow
\text{bounded symmetrizer}.
}
\]

Semisimplicity/no-shear is an independent requirement.

---

## 8. Condition-number interpretation

Let

\[
G(s)=U^{-T}G_0U^{-1}.
\]

If `U` has a singular value `sigma_max` growing while another shrinks, the eigenvalues of `G` acquire reciprocal squared growth.

Schematically,

\[
\kappa(G(s))
\gtrsim
\kappa(U(s))^2
\]

up to the fixed initial metric condition number.

Therefore a uniformly elliptic symmetrizer requires the strain cocycle to have uniformly bounded distortion in an equivalent norm.

The matrix method does not destroy hyperbolic deformation; it only changes the metric in which deformation is measured.

---

## 9. Important countermodel: nonzero strain can have identity monodromy

It would be incorrect to infer

\[
\Sigma\not\equiv0
\Longrightarrow
\text{hyperbolic monodromy}.
\]

Take a fixed nonzero symmetric trace-free matrix `S_0` and define a periodic piecewise-constant strain cycle

\[
\Sigma(s)=
\begin{cases}
S_0,&0<s<T,\\
-S_0,&T<s<2T.
\end{cases}
\]

The two halves commute, so the monodromy is

\[
M
=e^{-S_0T}e^{S_0T}
=I.
\]

Hence

\[
\boxed{M=I}
\]

despite nonzero strain throughout almost the whole cycle.

Smooth periodic approximations of this cycle retain monodromy arbitrarily close to identity, and exact smooth cancellation can be designed within the abstract cocycle class.

Therefore trace-free strain may stretch and later exactly undo that stretch.

This is a genuine structural countermodel to any attempted `nonzero strain => no matrix metric` shortcut.

It is not asserted that the piecewise cycle is itself generated by a Navier--Stokes critical tail; it proves only that the current generic structural hypotheses are insufficient.

---

## 10. Elliptic monodromy gives an explicit positive metric

Conversely, suppose `M` is similar to an orthogonal matrix:

\[
M=S^{-1}OS,
\qquad
O^TO=I.
\]

Then choose

\[
\boxed{G_0=S^TS>0.}
\]

Indeed,

\[
M^TG_0M
=S^TO^TO S
=S^TS
=G_0.
\]

Thus the spectral criterion is not merely necessary; it is sufficient.

The resulting

\[
G(s)=U^{-T}G_0U^{-1}
\]

is periodic and uniformly elliptic on the finite period.

---

## 11. Relation to pure tangential/Killing drift

In the favorable M5-194G tangential Killing subclass,

\[
\Phi_r=0
\]

and the angular transport is skew/commuting at the scalar level.

M5-203 shows that the remaining strain issue is exactly whether its cocycle monodromy is elliptic in the above sense.

Thus the hierarchy is

\[
\boxed{
\text{Killing transport}
+
\text{elliptic strain monodromy}
\Longrightarrow
\text{bounded local matrix metric candidate}.
}
\]

Hyperbolic or Jordan strain monodromy destroys that candidate even when the transport itself is perfectly tangential.

---

## 12. Recurrent nonperiodic characteristics

For a nonperiodic recurrent orbit, define the cocycle `U(s2,s1)`.

A globally bounded positive metric solution requires, in an equivalent norm,

\[
\sup_{s_2,s_1}
\|U(s_2,s_1)\|
+
\|U(s_2,s_1)^{-1}\|
<\infty
\]

along the relevant orbit if the metric itself is uniformly bounded above and below.

Vanishing Lyapunov exponents are necessary but not sufficient, because polynomial/unipotent growth can remain.

Thus the correct recurrent analogue is **uniform boundedness of the cocycle up to a bounded change of metric**, not merely zero average strain or zero maximal Lyapunov exponent.

---

## 13. DSD classification

The zero-radial-mean matrix branch splits into finite mathematical types:

\[
\boxed{
\begin{aligned}
\text{hyperbolic monodromy}
&\to\text{matrix symmetrizer impossible},\\
\text{Jordan/parabolic monodromy}
&\to\text{matrix symmetrizer impossible},\\
\text{elliptic semisimple monodromy}
&\to\text{positive periodic metric exists},\\
\text{nonperiodic recurrent cocycle}
&\to\text{uniform-cocycle boundedness problem}.
\end{aligned}
}
\]

This is sharper than a binary `symmetrizer exists/does not exist` statement.

---

## 14. What remains Navier--Stokes-specific

The abstract matrix classification is now complete at the pointwise-cocycle level.

The unresolved PDE question is whether a **nontrivial critical Navier--Stokes tail** can actually realize the elliptic/metric-preserving cocycle while also satisfying

- incompressibility;
- the log-cylinder pressure constraint;
- the critical tail residual equation;
- recurrent core coupling;
- the positive speed/stretching payers already derived;
- and the first-hitting/canonical-tail inheritance conditions.

The abstract cancellation countermodel does not answer this.

Therefore the next useful calculation must insert the NSE residual rather than continue pure matrix algebra.

---

## 15. DSD verdict

### PROVED

- exact fundamental-matrix representation of the det-one symmetrizer;
- periodic metric iff `M^T G M=G` for some `G>0`;
- equivalence with similarity of `M` to an orthogonal matrix;
- unit-modulus + semisimple spectral criterion;
- hyperbolic and Jordan/parabolic Floquet types excluded;
- zero Lyapunov exponent alone insufficient;
- nonzero symmetric trace-free strain can have identity monodromy, so nonzero strain is not by itself a no-go;
- elliptic monodromy is genuinely sufficient for a bounded periodic metric.

### OPEN

- whether NSE-compatible critical tails can realize elliptic monodromy nontrivially;
- recurrent nonperiodic uniformly bounded cocycles;
- nonlocal/pseudodifferential symmetrizers;
- generic backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 16. Next target

The next nonredundant step is to insert the **NSE log-cylinder residual** into the elliptic monodromy branch.

A natural test is to pair the stationary/recurrent tail equation with the symmetrizer metric and derive the period-averaged identity for

\[
\int W^TG W.
\]

If the first-order drift+strain is exactly skew in `G`, only viscous cylinder diffusion, weight curvature, pressure-compatible constraints, and core/tail forcing remain in the symmetric energy balance.

The question becomes whether a nonzero periodic/recurrent critical tail can have zero net diffusion payment while maintaining the elliptic monodromy. This is the first place where the matrix classification may combine with NSE dissipation rather than abstract cocycle geometry.