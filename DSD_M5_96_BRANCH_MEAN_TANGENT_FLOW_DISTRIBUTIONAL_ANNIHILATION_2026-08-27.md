# DSD M5-96 — Branch-Mean Tangent-Flow Distributional Annihilation

Date: 2026-08-27

Status: **TECHNICAL REPAIR OF M5-84/M5-85 / COMPONENTWISE PRESSURE MEANS ARE CONSTANT ALONG THE AMPLITUDE-TANGENT FLOWS IN THE DISTRIBUTIONAL SENSE / TOPOLOGY-CHANGING CRITICAL SETS PRODUCE NO HIDDEN TANGENTIAL JUMP TERM / WEIGHTED SKEW-ADJOINTNESS IS GLOBAL ON THE FIXED POSITIVE AMPLITUDE CELL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Problem left by M5-84

On each regular connected superlevel branch, M5-68 defines

\[
m_{P,k}(\lambda,t)
=
\frac{\displaystyle\int_{\Gamma_{\lambda,k}}
P|\nabla a|^{-1}dS}
{\displaystyle\int_{\Gamma_{\lambda,k}}|\nabla a|^{-1}dS},
\qquad a:=|U|.
\]

M5-84 used the amplitude-tangent vector fields

\[
\boxed{
L_{ij}
=(\partial_i a)\partial_j-(\partial_j a)\partial_i
}
\]

and the regular-branch identity

\[
L_{ij}m_{P,k}(a,t)=0.
\]

The remaining audit issue was whether branch birth/merger at critical amplitude sets could create an unrecorded distributional jump when the branchwise mean is viewed as one measurable field on the whole active band.

This memo closes that interface by using the flow of `L_ij` rather than differentiating branch labels.

---

# 2. Formation chain — define the branch-mean field only where it is formed

Fix one time in the smooth returned W1 pump cell and a positive amplitude band

\[
I=[\lambda_-,\lambda_+]\Subset(0,\infty)
\]

containing the support of the fixed mollifier `w`.

Because `a>=lambda_->0` on the active set, `a=|U|` is smooth there.

For every regular point `y` with

\[
a(y)=\lambda\in I,
\qquad \nabla a(y)\ne0,
\]

there is a unique connected superlevel volume component

\[
\Omega_{\lambda,k(y)}\subset\{a>\lambda\}
\]

whose full regular boundary contains `y`.

Define the measurable branch-mean field

\[
\boxed{
M(y):=m_{P,k(y)}(a(y),t)
}
\]

on the regular set.

On the critical set `grad a=0`, define `M` arbitrarily, for example by `M=0`. This choice will not affect the tangential derivative below because the tangent generators themselves vanish there.

On the fixed compact W1 pump cell, `P` is smooth modulo one irrelevant time gauge, so `M` is locally bounded on every compact sub-band where the defining regular means exist. For the distributional argument only local `L1` is needed.

---

# 3. Axial chain — the tangent vector field preserves amplitude exactly

Let

\[
V_{ij}
=(\partial_i a)e_j-(\partial_j a)e_i,
\qquad
L_{ij}=V_{ij}\cdot\nabla.
\]

Then

\[
\boxed{V_{ij}\cdot\nabla a=L_{ij}a=0.}
\]

Moreover

\[
\boxed{\nabla\cdot V_{ij}=0.}
\]

Let `Phi_tau` be the local flow of `V_ij`.

Along every flow curve,

\[
\frac d{d\tau}a(\Phi_\tau(y))
=V_{ij}\cdot\nabla a=0,
\]

hence

\[
\boxed{a(\Phi_\tau(y))=a(y)}
\]

for as long as the flow is defined.

Thus the flow never moves in the amplitude-normal direction.

---

# 4. Static aggregation chain — the superlevel component label is also preserved

Take a regular initial point `y` on the boundary of a connected superlevel component `Omega_{lambda,k}`.

The curve `tau -> Phi_tau(y)` remains continuously inside the same level set `{a=lambda}`.

Two distinct connected superlevel-volume boundaries at one regular value are disjoint regular hypersurfaces. A continuous curve lying in the regular level set cannot jump from the boundary of one superlevel component to another without meeting a topology-changing critical point.

At a critical point,

\[
\nabla a=0
\quad\Longrightarrow\quad
V_{ij}=0.
\]

Hence the tangent flow does not cross the critical point into another branch; that point is stationary for this flow.

Therefore, along every nonstationary tangent-flow orbit issued from a regular point,

\[
\boxed{k(\Phi_\tau(y))=k(y).}
\]

Since the amplitude is also fixed,

\[
\boxed{M(\Phi_\tau(y))=M(y)}
\]

for almost every initial point in the active band.

This remains true if the full boundary of one superlevel volume has several connected surface pieces, because the same mean `m_{P,k}` is assigned to the entire boundary of that volume component.

---

# 5. Distributional annihilation

The flow-invariance statement gives the weak derivative directly.

Let `phi in C_c^infty` be supported inside the fixed positive-amplitude pump cell. Because `V_ij` is divergence free, its flow preserves Lebesgue measure.

Using `M o Phi_tau=M` almost everywhere,

\[
\int M(y)\phi(\Phi_{-\tau}(y))dy
=
\int M(y)\phi(y)dy.
\]

Differentiate at `tau=0` in the weak sense. Since `M` is locally integrable,

\[
\boxed{
\int M L_{ij}\phi\,dy=0.
}
\]

Equivalently,

\[
\boxed{L_{ij}M=0\quad\text{in }\mathcal D'.}
\]

Thus topology changes of the amplitude foliation create **no hidden distributional tangential jump term**.

The statement does not require differentiability of `lambda -> m_{P,k}` through critical values.

---

# 6. Weighted version

The M5 weight is

\[
\rho(a):=a w(a).
\]

Since

\[
L_{ij}a=0,
\]

we also have

\[
L_{ij}\rho(a)=0.
\]

Together with `div V_ij=0`,

\[
\boxed{
\nabla\cdot(\rho V_{ij})=0.
}
\]

Hence for compactly supported smooth test functions,

\[
\boxed{
\int f L_{ij}g\,\rho\,dy
=-\int g L_{ij}f\,\rho\,dy.
}
\]

The positive amplitude support is spatially contained in the fixed normalized W1 pump core, so there is no spatial-infinity boundary term. At the amplitude support boundary, the tangent field has zero amplitude-normal flux because `L_ij a=0`.

Therefore the weighted skew-adjointness used in M5-84 is legitimate globally on the active cell.

---

# 7. Apply to the M5-83 residual

Let

\[
q:=P-2\nu b,
\qquad
b:=U\cdot\nabla\log a,
\]

and

\[
r:=q-M.
\]

Since `L_ij M=0` distributionally,

\[
\boxed{L_{ij}r=L_{ij}q}
\]

in distributions.

Applying the same derivative once more gives

\[
\boxed{L_{ij}^2r=L_{ij}^2q}
\]

in distributions.

On the fixed smooth active cell the right-hand sides are ordinary smooth functions, while `r` belongs to the weighted `L2` space by the exact M5-83 residual identity.

Weighted integration by parts therefore yields

\[
\boxed{
\|L_{ij}q\|_{L^2(d\mu)}^2
=-\int r L_{ij}^2q\,d\mu
\le
\|r\|_{L^2(d\mu)}
\|L_{ij}^2q\|_{L^2(d\mu)}.
}
\]

Thus the M5-84 interpolation inequality survives critical topology changes without extra branch terms.

---

# 8. DSD four-chain audit

## Formation — GREEN

The branch mean is only assigned after a regular level/component is formed. Critical points are not forced to carry a fictitious branch label.

## Axial property — GREEN

`L_ij` is exactly tangent to amplitude and vanishes at critical points.

## Static aggregation — GREEN

A tangent orbit cannot jump between disconnected superlevel components at fixed regular amplitude. The full-boundary component mean is therefore invariant along the orbit.

## Dynamics — GREEN for this frozen-time interface

This lemma is statewise. It does not assume persistence of the topology under Leray-time evolution. At every smooth time the distributional statement is reconstructed from the current amplitude field.

## Cross-audit — GREEN

Formation changes at critical amplitudes do not create a tangential transport channel because the tangent generator itself degenerates there.

---

# 9. Repair verdict

The two YELLOW qualifications in M5-84 concerning hidden branch-gluing/critical-set tangential boundary terms are closed for the fixed positive-amplitude W1 cell.

M5-85's component-free tangential interpolation can therefore be used without assuming a uniform bound on component count or topology persistence.

This repair does **not** solve the separate problem of selecting a nontrivial bounded regular level component from the positive crossing integral. That is the next audit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
