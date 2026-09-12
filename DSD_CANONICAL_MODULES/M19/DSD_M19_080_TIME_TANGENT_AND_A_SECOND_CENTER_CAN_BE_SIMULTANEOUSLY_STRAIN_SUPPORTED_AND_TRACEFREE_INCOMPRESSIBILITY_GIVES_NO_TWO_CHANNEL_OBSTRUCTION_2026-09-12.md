# DSD M19-080 — Time tangent and a second center can be simultaneously strain-supported, and trace-free incompressibility gives no two-channel obstruction

Date: 2026-09-12

Status: **TWO-CENTER NEUTRALIZATION AUDIT / SPECIALIZING ONE CENTER DIRECTION TO THE EXACT TIME TANGENT DOES NOT REPAIR THE FAILED EXTERIOR-SQUARE TRACE ARGUMENT / A TRACE-FREE THREE-DIMENSIONAL STRAIN TENSOR MAY HAVE TWO COMPRESSIVE EIGENDIRECTIONS, SO TWO INDEPENDENT PERTURBATIONS CAN BOTH EXTRACT POSITIVE NEUTRALIZING WORK / GLOBAL WEIGHTED ORTHOGONALITY DOES NOT FORCE POINTWISE ORTHOGONALITY OR COLOCATION, AND MODES MAY LOCALIZE IN DIFFERENT STRAIN REGIONS / EXCLUDING A SECOND CENTER REQUIRES A DELOCALIZATION/OBSERVABILITY OR DYNAMICAL COHERENCE INPUT BEYOND INCOMPRESSIBILITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The proposed refinement

M19-079 showed that every nonzero bounded complete transverse center witness must neutralize the positive OU/viscous cost by persistent strain work.

One center direction is already known exactly:

\[
W_1:=\partial_\theta U.
\]

Suppose there is a second rotation-transverse center witness \(W_2\), linearly independent of \(W_1\).

A natural hope is that incompressibility,

\[
\operatorname{tr}S_U=0,
\]

prevents two independent zero-exponent directions from being simultaneously supported by the same strain field.

M19-080 tests this directly.

---

## 2. Polarized weighted energy identity

For two linearized solutions \(W_1,W_2\), define

\[
B_w(\theta):=\langle W_1,W_2\rangle_w.
\]

Polarizing the weighted energy identity gives schematically

\[
\frac{d}{d\theta}B_w
+2\mathcal C_{OU}[W_1,W_2]
+2\nu\mathcal G[W_1,W_2]
=
2\mathcal W_{tr}[W_1,W_2]
+2\mathcal W_{pr}[W_1,W_2]
+2\mathcal W_{str}[W_1,W_2],
\]

where the strain bilinear form is

\[
\boxed{
\mathcal W_{str}[W_1,W_2]
=-\int W_1^TS_UW_2\,w\,dy.
}
\]

Nothing in this identity vanishes merely because \(W_1=\partial_\theta U\).

The time tangent satisfies the same linearized equation but does not create an additional algebraic relation annihilating the mixed strain form.

---

## 3. Pointwise trace-free strain allows two compressive directions

At a fixed point, let the strain eigenvalues be

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Trace-free does not imply only one negative eigenvalue.

For example,

\[
\boxed{
S=\operatorname{diag}(-1,-1,2)
}
\]

is trace-free and has two independent compressive eigendirections.

Under the sign convention of M19-079,

\[
-W^TSW>0
\]

on either of the first two eigendirections.

Hence two linearly independent perturbations can simultaneously receive positive strain-supported neutralization at the same point.

Therefore

\[
\boxed{
\operatorname{tr}S=0
\not\Rightarrow
\text{at most one positive neutralization channel}.
}
\]

---

## 4. The time tangent is not forced into the unique compressive eigendirection

The exact identity

\[
W_1=\partial_\theta U
\]

does not imply pointwise alignment with one distinguished strain eigenvector.

It contains contributions from diffusion, pressure, transport and nonlinear evolution.

Thus even if one tried to reserve one compressive eigendirection for the time tangent, there is no certified pointwise theorem forcing it to occupy that direction everywhere or with full weight.

A second perturbation may exploit the remaining compressive direction or different spacetime regions.

---

## 5. Global Hilbert orthogonality is much weaker than pointwise orthogonality

After modulation, one can impose weighted orthogonality such as

\[
\langle W_1,W_2\rangle_w=0.
\]

But this only means

\[
\int W_1\cdot W_2\,w\,dy=0.
\]

It does not imply

\[
W_1(y)\cdot W_2(y)=0
\]

pointwise.

Nor does it imply that the two perturbations sample the same strain distribution.

In particular, two normalized modes can be essentially localized in disjoint regions,

\[
\operatorname{supp}_{eff}W_1
\cap
\operatorname{supp}_{eff}W_2
\approx\varnothing,
\]

and each can extract positive work from a different compressive region.

Therefore global orthogonality supplies no local trace cancellation.

---

## 6. Why the two-volume argument still fails

For a weighted orthonormal pair \(e_1,e_2\), the strain contribution to the logarithmic two-volume derivative is

\[
-\int
S_U:
\left(
 e_1\otimes e_1+e_2\otimes e_2
\right)
 w\,dy.
\]

Trace-free cancellation would require the tensor in parentheses to be proportional to the identity pointwise.

Weighted Hilbert orthonormality does not imply this.

Specializing \(e_1\) to the normalized time tangent does not alter the defect.

Thus M19-071 remains valid after the time-tangent refinement.

---

## 7. Even three or more global modes are not ruled out by pointwise eigenvalue count

At one point a three-dimensional trace-free strain cannot be compressive in all three independent directions simultaneously.

But global modes can localize in different regions or times.

Hence a family \(W_1,W_2,W_3,\ldots\) can in principle arrange its neutralizing work through distinct spacetime packets without forming a pointwise orthonormal frame.

Therefore the finite dimension of physical space does not by itself give a finite bound on the dimension of the global cocycle center.

A center-dimension theorem needs a mechanism preventing such localization freedom.

---

## 8. The missing ingredient is overlap/de-localization, not another trace identity

A useful theorem would need to show that every bounded complete center witness has a quantitatively nontrivial fraction of its weighted energy on a common recurrent core region where the strain quadratic form cannot support more than the symmetry directions.

Schematically, one would need an estimate such as

\[
\boxed{
\int_{K}|W|^2w\,dy
\ge c_K E_w
}
\]

for a common compact \(K\) and every normalized center witness, together with a finite-rank or sign property of the strain operator on that common region.

No such common-core observability estimate is presently certified.

---

## 9. Relation to scattering escape

The formal tail center from M19-068 is exactly a localization freedom in the log-radius/history variable.

M19-073 showed that moving farther along the history corresponds to smaller physical scales with geometrically summable cost.

Thus the failure of trace-based center counting is consistent with the weak-critical scattering picture: different center candidates can hide in different q/history sectors unless an interior observability theorem prevents it.

---

## 10. Certified conclusion

\[
\boxed{
\text{time tangent}
+\text{trace-free strain}
+\text{global orthogonality}
\not\Rightarrow
\text{one-dimensional transverse center}.
}
\]

The next useful target is therefore not another algebraic strain identity but a quantitative **common-core observability / no-escape estimate for complete center witnesses**.

---

## 11. Next calculation

M19-081 should ask whether the radial-A2 weighted norm itself supplies such a no-escape estimate.

Because the weight decays only polynomially and every center witness is assumed complete and normalized, one can test whether bounded diffusion plus zero exponent forces a fixed fraction of the mass to revisit a common compact ball, or whether a center witness may drift to larger similarity radii while remaining normalized.

The latter would reconnect directly to the q-translation scattering escape.
