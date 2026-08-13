# Multicore static aggregation: exact covariance and magnitude-variance rigidity

Date: 2026-08-13

Status: **EXACT DSD STATIC-AGGREGATION IDENTITIES / MULTICORE SATURATION RIGIDITY**.

A selected low-leakage parent buffer can contain more than one active vorticity core.  This does not create an untyped source term.  The DSD static-aggregation viewpoint gives exact decompositions of both projective direction dispersion and enstrophy-weighted magnitude heterogeneity into **within-core** and **between-core** contributions.

---

## 1. Disjoint active cores

Let

\[
C_1,\ldots,C_N
\]

be disjoint measurable active regions at one normalized time.

Define

\[
E_i=\int_{C_i}|\Omega|^2dy,
\qquad
E=\sum_iE_i,
\]

and assume `E_i>0` for retained components.

Use enstrophy weights

\[
\boxed{
w_i=E_i/E,
\qquad
\sum_iw_i=1.
}
\]

The component covariance matrices are

\[
\boxed{
C_i
=\frac1{E_i}
\int_{C_i}\Omega\otimes\Omega dy,
}
\]

and the aggregate covariance is

\[
\boxed{
C=\sum_iw_iC_i.
}
\]

All `C_i` and `C` are positive semidefinite with trace one.

---

## 2. Exact projective-dispersion decomposition

Define

\[
J(C)=1-\operatorname{tr}(C^2).
\]

Then

\[
\boxed{
J(C)
=
\sum_iw_iJ(C_i)
+
\frac12
\sum_{i,j}
w_iw_j
\|C_i-C_j\|_F^2.
}
\]

Proof: expand

\[
\frac12\sum_{i,j}w_iw_j\|C_i-C_j\|_F^2
=
\sum_iw_i\operatorname{tr}(C_i^2)
-
\operatorname{tr}(C^2),
\]

and add

\[
\sum_iw_iJ(C_i)
=1-\sum_iw_i\operatorname{tr}(C_i^2).
\]

Thus total projective roughness has two nonnegative sources:

1. **within-core projective dispersion**;
2. **between-core covariance/axis mismatch**.

---

## 3. Rank-one coherent-core specialization

If each core is exactly one-axis,

\[
C_i=n_i\otimes n_i,
\qquad |n_i|=1,
\]

then

\[
J(C_i)=0
\]

and

\[
\frac12
\|C_i-C_j\|_F^2
=1-(n_i\cdot n_j)^2.
\]

Therefore

\[
\boxed{
J(C)
=
\sum_{i,j}w_iw_j
\left[1-(n_i\cdot n_j)^2\right].
}
\]

The sign of the axis is irrelevant, as required by projective covariance.

Hence a collection of individually coherent cores is aggregate-coherent only if the significant cores share essentially the same **unoriented axis**.

---

## 4. Quantitative consequence of small aggregate `J`

Every term in the exact decomposition is nonnegative.  Therefore

\[
\boxed{
\sum_iw_iJ(C_i)\le J(C),
}
\]

and

\[
\boxed{
\frac12
\sum_{i,j}w_iw_j
\|C_i-C_j\|_F^2
\le J(C).
}
\]

Thus if

\[
J(C)\le\varepsilon,
\]

then both the average internal projective defect and the weighted pairwise axis mismatch are at most `epsilon`.

For any fixed weight threshold `w_i,w_j>=w0`,

\[
\boxed{
\|C_i-C_j\|_F^2
\le
\frac{2\varepsilon}{w_0^2}.
}
\]

So all macroscopically weighted cores must share nearly the same covariance axis whenever the parent cluster is nearly projectively coherent.

---

## 5. Enstrophy-weighted magnitude distribution

Let

\[
\rho=|\Omega|.
\]

On each component define the conditional enstrophy-weighted probability measure

\[
d\mu_i
=\frac{\rho^2}{E_i}\,1_{C_i}dy.
\]

Let

\[
m_i=\mathbb E_{\mu_i}[\rho],
\qquad
v_i=\operatorname{Var}_{\mu_i}(\rho).
\]

The aggregate enstrophy-weighted measure is

\[
\mu=\sum_iw_i\mu_i.
\]

Its mean is

\[
\boxed{
m=\sum_iw_im_i.}
\]

---

## 6. Exact law of total magnitude variance

The aggregate variance satisfies

\[
\boxed{
v_{\rm mag}
=
\sum_iw_iv_i
+
\sum_iw_i(m_i-m)^2.
}
\]

Thus magnitude heterogeneity also has two nonnegative sources:

1. **within-core magnitude variance**;
2. **between-core mean-level mismatch**.

Define

\[
\chi_{\rm mag}=v_{\rm mag}/m^2.
\]

If

\[
\chi_{\rm mag}\to0
\]

while the significant weights do not vanish, then necessarily

\[
v_i\to0
\]

for every significant core and

\[
m_i-m_j\to0
\]

for every pair of significant cores.

Hence source-interpolation saturation forces all significant cores toward the same enstrophy-weighted vorticity magnitude level.

---

## 7. Combined multicore saturation geometry

Suppose a parent buffer attempts to evade both direction and magnitude coefficient gaps:

\[
J(C)\to0,
\qquad
\chi_{\rm mag}\to0.
\]

Then every significant active component must satisfy simultaneously:

\[
\boxed{
C_i\approx n\otimes n
}
\]

for one common projective axis `[n]`, and

\[
\boxed{
\rho\approx m
}
\]

in enstrophy-weighted distribution with the same mean level across components.

Thus multiple disconnected active cores do not generate independent saturation degrees of freedom.  They collapse toward a **common-axis, common-magnitude cluster state**.

---

## 8. Return to polarity and flux

Projective covariance still does not distinguish `n` from `-n`.

Therefore the remaining multicore degree of freedom is polarity:

- mixed signs inside/between cores feed the polarity-variance/palinstrophy branch;
- one dominant sign across the cluster produces coherent signed axial vorticity flux components;
- such flux cannot terminate freely and returns to the side-leakage/material-flux geometry.

Hence the equality regime of the aggregate source estimate feeds back into the already-developed polarity/flux branch rather than opening a new multi-core escape.

---

## 9. Finite number of thick natural cores under bounded normalized enstrophy

At a fixed threshold `b>0`, let every retained thick component contain an intense subset of volume at least `theta>0` in normalized units and satisfy

\[
|\Omega|\ge b
\]

there.

Each such component contributes at least

\[
b^2\theta
\]

to normalized enstrophy.  If

\[
\|\Omega\|_2^2\le M_E,
\]

then the number of pairwise disjoint retained thick cores satisfies

\[
\boxed{
N_{\rm thick}
\le
\frac{M_E}{b^2\theta}.
}
\]

Thus the bounded normalized-enstrophy branch contains only finitely many macroscopically thick dangerous components at one checkpoint.

Small/thin residual components return to the occupancy/sparseness branch.

---

## 10. DSD interpretation

This is a literal static-aggregation law:

\[
\boxed{
\text{aggregate defect}
=
\text{within-channel defect}
+
\text{between-channel mismatch}.
}
\]

The same principle operates independently for

- projective axis covariance;
- vorticity magnitude distribution.

Therefore the parent-scale DSD descriptor should keep both diagonal component defects and off-diagonal inter-core mismatches instead of collapsing them into one scalar too early.

Status: **MULTICORE AGGREGATION EXACT / SOURCE-SATURATION GEOMETRY FURTHER RIGIDIFIED**.
