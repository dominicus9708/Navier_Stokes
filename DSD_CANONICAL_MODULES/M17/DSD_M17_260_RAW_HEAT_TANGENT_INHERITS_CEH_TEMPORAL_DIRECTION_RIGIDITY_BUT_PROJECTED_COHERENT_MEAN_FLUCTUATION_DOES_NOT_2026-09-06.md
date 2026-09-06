# DSD M17-260 — Raw heat tangent inherits CE-H temporal-direction rigidity, but projected coherent-mean fluctuation does not

Date: 2026-09-06  
Canonical ID: **M17-260**

Status: **CE-H TANGENT-INHERITANCE AUDIT / THE ORIGINAL INTRINSICALLY RESCALED VORTICITY SATISFIES `Delta_z V_j = K_j V_j` WITH `K_j=r_j^2 kappa_j`. ON A RAW MASS-COMPACT NON-SPIKE BRANCH, STRONG LOCAL `L2` CONVERGENCE OF `V_j` AND WEAK-* COMPACTNESS OF BOUNDED `K_j` PASS THIS RELATION TO `Delta V=KV`. IF THE DYNAMIC LIMIT IS ALSO HEAT, THEN `partial_tau V=KV`, SO AT EVERY ACTIVE SPATIAL POINT THE VECTOR DIRECTION `V/|V|` IS EXACTLY TIME-INDEPENDENT. THIS IS GENUINE RIGIDITY ABSENT FROM THE GENERIC HEAT COUNTEREXAMPLE OF M17-259. HOWEVER, AFTER SUBTRACTING A LARGE COHERENT MEAN, `F_j=V_j-bar V_j` SATISFIES THE INHOMOGENEOUS RELATION `Delta F_j=K_j(F_j+bar V_j)`. HOMOGENEOUS CE-H THEREFORE DOES NOT PASS TO THE PROJECTED FLUCTUATION WITHOUT AN ADDITIONAL `K_j bar V_j` CONTROL. THE RAW AND PROJECTED CALORIC BRANCHES MUST REMAIN SEPARATE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact scaled CE-H relation

The original CE-H branch satisfies

\[
\Delta_yW=\kappa W.
\]

Under intrinsic scaling

\[
y=q_j+r_jz,
\qquad
V_j(z,\tau)
=\frac{1}{a_j}W(y,\theta_j+r_j^2\tau),
\]

we have exactly

\[
\boxed{
\Delta_zV_j=K_jV_j,
\qquad
K_j(z,\tau):=r_j^2\kappa(y,\theta_j+r_j^2\tau).
}
\]

No cutoff derivative appears in this identity when it is applied to the raw physical field on an interior region.

---

## 2. Non-spike coefficient compactness

Work on a fixed compact cylinder `Q=BK x [-T,0]` contained in the raw packet interior.

Assume the non-spike branch

\[
\boxed{
\|K_j\|_{L^\infty(Q)}\le K_*
}
\]

for one fixed `K_*`.

After a subsequence,

\[
K_j\rightharpoonup^* K
\quad\text{in }L^\infty(Q).
\]

Suppose M17-255 gives

\[
V_j\to V
\quad\text{strongly in }L^2(Q),
\]

and local elliptic/parabolic estimates give

\[
\Delta V_j\rightharpoonup\Delta V
\]

in distributions or weakly in the relevant local `L2` space.

Then for every compactly supported test field `phi`,

\[
\int K_jV_j\cdot\phi
\to
\int KV\cdot\phi.
\]

Indeed split

\[
K_jV_j-KV
=K_j(V_j-V)+(K_j-K)V,
\]

where the first term tends strongly to zero in `L2` and the second tends weakly to zero by weak-* convergence of `K_j` against the fixed `L1` coefficient `V phi`.

Therefore

\[
\boxed{\Delta V=KV.}
\]

---

## 3. Combine with the intrinsic heat tangent

On the dynamically quiet branch of M17-252/M17-255,

\[
\boxed{\partial_\tau V=\Delta V.}
\]

Combining with Section 2,

\[
\boxed{
\partial_\tau V=KV.
}
\]

Thus the time derivative is pointwise collinear with the field wherever the strong representative is nonzero.

---

## 4. Temporal direction rigidity

Define on the active set

\[
\xi(z,\tau):=\frac{V(z,\tau)}{|V(z,\tau)|}.
\]

Since

\[
\partial_\tau V=KV,
\]

we have

\[
\partial_\tau|V|=K|V|
\]

and therefore

\[
\begin{aligned}
\partial_\tau\xi
&=\frac{\partial_\tau V}{|V|}
-\frac{V\,\partial_\tau|V|}{|V|^2}\\
&=K\xi-K\xi\\
&=0.
\end{aligned}
\]

Hence

\[
\boxed{
\partial_\tau\xi=0
\quad\text{where }V\ne0.
}
\]

Equivalently, for each fixed active spatial point, the heat evolution changes only the scalar amplitude and never the vector direction.

This property is absent from a generic divergence-free ancient heat solution such as the M17-259 Fourier example.

---

## 5. Spatial equation for a frozen director

Write locally

\[
V(z,\tau)=a(z,\tau)\xi(z)
\]

with `xi` independent of `tau`.

The heat equation gives

\[
\xi\,\partial_\tau a
=
\xi\,\Delta a
+2\sum_i(\partial_i a)(\partial_i\xi)
+a\Delta\xi.
\]

Project perpendicular to `xi`:

\[
\boxed{
2P_\xi^\perp
\left(
\sum_i(\partial_i a)(\partial_i\xi)
\right)
+aP_\xi^\perp\Delta\xi
=0.
}
\]

This must hold for every time in the ancient interval.

Thus a spatially varying frozen director cannot be arbitrary: its geometry must be compatible with the entire scalar heat orbit `a(z,tau)`.

No contradiction is claimed yet.

---

## 6. Why the projected coherent-mean branch is different

On M17-257 write

\[
F_j=V_j-\bar V_j.
\]

Because `bar V_j` is spatially constant,

\[
\Delta F_j=\Delta V_j.
\]

But CE-H gives

\[
\boxed{
\Delta F_j
=K_jV_j
=K_j(F_j+\bar V_j).
}
\]

Therefore

\[
\boxed{
\Delta F_j\ne K_jF_j
}
\]

unless the additional source

\[
K_j\bar V_j
\]

is controlled or vanishes.

This is exactly analogous to the mean-subtraction inheritance firewall of M17-232.

Consequently the projected caloric fluctuation of M17-257 does **not** automatically inherit temporal-direction rigidity.

---

## 7. New coefficient-mean coupling

The projected dynamic equation introduced the mean-shear coupling

\[
\Gamma_j
=|\bar V_j|\,\|C_j-\bar C_j\|_\infty.
\]

CE-H introduces a distinct elliptic mean coupling

\[
\boxed{
\Xi_j(K,T)
:=
|\bar V_j|\,
\|K_j\|_{L^2(Q_{K,T})}
}
\]

or a corresponding local `L^{3/2}`/distributional version depending on the available coefficient control.

If `Xi_j` does not vanish, the coherent mean is elliptically active and should be retained as a coefficient/mean payer.

If `Xi_j->0`, homogeneous CE-H can potentially pass to the projected fluctuation as well.

The relation between `Xi_j`, the M17-233 critical `K` occupancy, and normalized derivative charge is the next natural calculation.

---

## 8. Corrected branch split

The intrinsic heat line now separates into

\[
\boxed{
H_{raw\ mass\text{-}compact\ heat}
\Longrightarrow
H_{CEH\ temporal\text{-}direction\ rigid\ heat}
\lor
G_{K\text{-}spike/defect},
}
\]

while

\[
\boxed{
H_{projected\ coherent\text{-}mean\ heat}
\Longrightarrow
H_{generic\ projected\ caloric}
\lor
G_{elliptic\ mean\ coupling\ \Xi}.
}
\]

These branches must not be merged.

---

## 9. DSD audit

1. CE-H is passed only for the raw field, not silently for a mean-subtracted fluctuation.
2. Strong `L2` convergence of `V_j` and bounded `K_j` are used explicitly to pass the product.
3. Temporal direction rigidity holds only on the active set `V!=0`.
4. Nodal/interface points remain a separate branch.
5. The frozen-director spatial identity is a rigidity constraint, not yet a Liouville theorem.
6. M17-259 remains a valid firewall for the projected branch because its heat counterexample need not satisfy homogeneous CE-H.
7. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
