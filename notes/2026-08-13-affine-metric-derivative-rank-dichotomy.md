# Affine metric / derivative covariance: exact coordinate identity, not a physical rank-reduction mechanism

Date: 2026-08-13

Status: **EXACT COVARIANCE IDENTITY / LOW-DIMENSIONAL PHYSICAL INTERPRETATION REJECTED BY COORDINATE-CANCELLATION AUDIT**.

This note records an exact affine-frame covariance identity but corrects an earlier overinterpretation.

The identity

\[
D_A=P\operatorname{tr}(AR)
\]

is valid.  However, a large eigenvalue of the coordinate diffusion metric `A` accompanied by a small derivative fraction in the same coordinate direction does **not** by itself mean that the physical flow becomes lower dimensional.  The coordinate deformation simultaneously rescales derivatives, and the metric/gradient changes compensate exactly at the physical dissipation level.

This is consistent with the earlier Lagrangian diffusion-metric audit.

---

## 1. Exact affine-frame identity

Let

\[
A=F^{-1}F^{-T}
\]

and for a transformed field `W` define

\[
P=\int|\nabla_zW|^2dz.
\]

When `P>0`, define

\[
\boxed{
R
=\frac1P
\left[
\int\partial_iW\cdot\partial_jW\,dz
\right]_{ij}.
}
\]

Then

\[
R\succeq0,
\qquad
\operatorname{tr}R=1.
\]

The affine-frame metric-weighted derivative quantity is exactly

\[
\boxed{
D_A
=\int\nabla W:A\nabla W\,dz
=P\operatorname{tr}(AR).
}
\]

If

\[
Ae_i=\lambda_i e_i,
\qquad
0<\lambda_1\le\lambda_2\le\lambda_3,
\]

and

\[
r_i=e_i^TRe_i,
\]

then

\[
\boxed{
\frac{D_A}{P}
=\sum_i\lambda_i r_i,
\qquad
r_i\ge0,
\qquad
\sum_i r_i=1.
}
\]

Consequently

\[
\boxed{
r_3\le\frac{D_A}{\lambda_3P}}
\]

and

\[
\boxed{
r_2+r_3\le\frac{D_A}{\lambda_2P}}.
\]

These are exact coordinate-covariance inequalities.

---

## 2. Why the apparent rank reduction can be a pure coordinate effect

Suppose, for example, that a scalar profile in physical coordinates depends on `y_3`,

\[
f(y)=g(y_3).
\]

Use an anisotropic coordinate map

\[
y=Fz
\]

whose third singular factor is `M^{-1}`.  Then

\[
f(Fz)=g(M^{-1}z_3)
\]

and

\[
\partial_{z_3}[f(Fz)]
=M^{-1}g'(M^{-1}z_3).
\]

Thus the transformed derivative in the strong metric direction becomes small automatically as the coordinate is stretched/compressed, even though the physical derivative `partial_{y_3} f` has not disappeared.

Therefore

\[
\boxed{
r_3\to0}
\]

in the transformed derivative covariance need not imply

\[
\boxed{\partial_{y_3}f\to0}
\]

in physical coordinates.

---

## 3. Exact physical dissipation cancellation

For the material-coordinate velocity transform the repository already derived

\[
\boxed{
(\nabla_aU)A(\nabla_aU)^T
=(\nabla_xu)(\nabla_xu)^T.
}
\]

Hence

\[
\boxed{
\sum_i(\nabla_aU_i)^TA(\nabla_aU_i)
=|\nabla_xu|^2.
}
\]

The same structural warning applies to affine-frame metric eigenvalues: a large coordinate diffusion coefficient is paired with a correspondingly rescaled coordinate derivative.

Therefore the route

\[
\text{large }\lambda_3
\Longrightarrow
\text{new physical viscous enhancement}
\]

is rejected.

Likewise the route

\[
\text{small }r_3
\Longrightarrow
\text{physical lower dimensionality}
\]

is rejected without an additional coordinate-invariant estimate.

---

## 4. What remains useful

The pairing

\[
\boxed{\operatorname{tr}(AR)}
\]

remains a useful **coordinate audit**:

- it checks that the anisotropic metric and transformed derivatives compensate consistently;
- it detects numerical/analytic mistakes in affine-frame implementations;
- it can be compared across coordinate descriptions as part of the DSD bookkeeping.

But it is not promoted to a new regularization or low-dimensionality theorem.

---

## 5. Preferred physical branch after this correction

The correct affine obstruction is instead measured before the coordinate transformation by the **optimal local affine representative** of the total physical/normalized gradient,

\[
L_\phi
=\frac{\int\phi\nabla U}{\int\phi}.
\]

Its coherent strain has the direct physical lower bound

\[
\boxed{
\int_I\int\phi|S_U|^2
\ge
\frac{\int\phi}{C_3^2|I|}
[\log\kappa(F_\phi)]^2.
}
\]

Thus an unbounded optimal affine condition number is charged to a genuine local normalized strain-energy concentration, not to a coordinate-metric eigenvalue.

---

## 6. Relation to the `H=FG` deformation ledger

The exact factorization

\[
H=FG
\]

remains valid for any affine/residual split and is useful for avoiding identification of a coarse affine map with the full material deformation.

However, once the **total** local affine representative is chosen optimally, a large affine factor is already a real coherent-strain concentration.  The transformed diffusion metric should then be treated as a coordinate consequence of that deformation, not as an additional independent physical sink.

---

## 7. Claim boundary

The algebraic gate `affine_metric_derivative_rank_gate.py` remains valid because it checks only

\[
D_A=P\operatorname{tr}(AR)
\]

and its spectral consequences.

Its output must be interpreted as **coordinate covariance**, not as evidence that the physical vorticity becomes one- or two-dimensional.

Status: **IDENTITY RETAINED / PHYSICAL RANK-REDUCTION ROUTE PRUNED**.
