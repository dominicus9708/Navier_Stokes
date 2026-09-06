# DSD M17-255 — Finite-cylinder parabolic compactness follows from normalized local mass and scaled coefficient control

Date: 2026-09-06  
Canonical ID: **M17-255**

Status: **SPACETIME COMPACTNESS GATE / AFTER M17-251/254, THE PACKET HAS A NONZERO TIME-ZERO NORMALIZATION AND, ON THE NO-PAYMENT BRANCH, A TWO-SIDED LOCALIZED MASS CORRIDOR ON EVERY FIXED RESCALED BACKWARD TIME. WRITE THE OWN-SCALE EQUATION AS `partial_tau V_j-Delta V_j=-A_j·grad V_j+C_jV_j`. ON ANY FIXED PARABOLIC CYLINDER, IF THE NORMALIZED SURROUNDING `L2` MASS AND THE RESCALED LOWER-ORDER COEFFICIENTS ARE UNIFORMLY BOUNDED, A LOCAL CACCIoppoli ESTIMATE GIVES `L2_t H1_x` CONTROL AND THE EQUATION GIVES `partial_tau V_j` CONTROL IN `L2_t H^-1_x`. AUBIN--LIONS THEN YIELDS STRONG LOCAL SPACETIME `L2` COMPACTNESS. IF THE COEFFICIENTS TEND TO ZERO, THE LIMIT IS CALORIC. FAILURE IS THEREFORE TYPED AS SCALED AMBIENT/COEFFICIENT ACTION OR NORMALIZED SURROUNDING-MASS DECOMPACTIFICATION, NOT AN UNTYPED COMPACTNESS LOSS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rescaled packet equation

Use the M17-252 own-scale variables

\[
y=q_j(\theta)+r_jz,
\qquad
\theta=\theta_j+r_j^2\tau,
\]

and amplitude normalization

\[
W=a_jV_j.
\]

Then

\[
\boxed{
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j,
}
\]

where

\[
\boxed{
A_j(z,\tau)
:=r_j\left[B(q_j+r_jz,\theta)-B(q_j,\theta)\right]
}
\]

and

\[
\boxed{
C_j(z,\tau)
:=r_j^2\Sigma(q_j+r_jz,\theta)-r_j^2I.
}
\]

The moving center removes the zeroth-order translation velocity `B(q_j,theta)` exactly.

---

## 2. Normalized surrounding-mass profile

For fixed `K,T>0`, define

\[
\boxed{
\mathcal M_j(K,T)
:=
\sup_{-T\le\tau\le0}
\int_{B_K}|V_j(z,\tau)|^2dz.
}
\]

In original variables this is the packet-normalized surrounding enstrophy

\[
\mathcal M_j(K,T)
=
\sup_{-T\le\tau\le0}
\frac{
\int_{B_{Kr_j}(q_j(\theta))}|W(y,\theta)|^2dy
}{a_j^2r_j^3}.
\]

With the M17-251 normalization

\[
a_j^2r_j^3\asymp E_j,
\]

so

\[
\boxed{
\mathcal M_j(K,T)
\asymp
\sup_{-T\le\tau\le0}
\frac{
\int_{B_{Kr_j}(q_j(\theta))}|W|^2
}{E_j}.
}
\]

The packet core gives a positive lower normalization at fixed small `K`, but no theorem yet bounds this ratio for arbitrary larger `K`.

---

## 3. Scaled coefficient profile

Define

\[
\boxed{
\mathcal C_j(K,T)
:=
\|A_j\|_{L^\infty(B_K\times[-T,0])}
+
\|C_j\|_{L^\infty(B_K\times[-T,0])}.
}
\]

A bounded coefficient corridor means

\[
\boxed{
\sup_j\mathcal C_j(K,T)<\infty.
}
\]

The heat-tangent branch requires the stronger condition

\[
\boxed{
\mathcal C_j(K,T)\to0.
}
\]

Failure is an explicit scaled ambient/strain/drift branch.

---

## 4. Local Caccioppoli estimate

Fix nested cylinders

\[
Q'
:=B_{K'}\times[-T',0]
\Subset
Q
:=B_K\times[-T,0]
\]

with

\[
0<K'<K,
\qquad
0<T'<T.
\]

Choose a smooth cutoff `chi(z,tau)` equal to one on `Q'` and supported in `Q`.

Test the equation against

\[
\chi^2V_j.
\]

After the standard integration by parts, the diffusion term gives the positive quantity

\[
\int_Q\chi^2|\nabla V_j|^2.
\]

The cutoff, drift, and zero-order terms are estimated by Young's inequality using

\[
\|A_j\|_\infty+
\|C_j\|_\infty
\le C_{K,T}.
\]

One obtains

\[
\boxed{
\sup_{-T'\le\tau\le0}
\int_{B_{K'}}|V_j|^2dz
+
\int_{-T'}^0\int_{B_{K'}}|\nabla V_j|^2dzd\tau
\le
C_{K,T,K',T'}
\int_Q|V_j|^2dzd\tau.
}
\]

If

\[
\mathcal M_j(K,T)\le M_{K,T},
\]

then the right-hand side is uniformly bounded.

Thus

\[
\boxed{
V_j
\text{ is bounded in }
L^2([-T',0];H^1(B_{K'})).
}
\]

---

## 5. Time derivative bound in H^-1

From the rescaled equation,

\[
\partial_\tau V_j
=
\Delta V_j
-A_j\cdot\nabla V_j
+C_jV_j.
\]

On `B_K`, the Laplacian maps `H1` to `H^-1`, while bounded `A_j,C_j` make the other terms controlled by the `H1` and `L2` norms.

Therefore

\[
\boxed{
\partial_\tau V_j
\text{ is bounded in }
L^2([-T',0];H^{-1}(B_{K'})).
}
\]

with a constant depending only on the fixed cylinder and the mass/coefficient ceilings.

---

## 6. Aubin--Lions compactness

Use the compact-continuous chain

\[
H^1(B_{K'})
\Subset
L^2(B_{K'})
\hookrightarrow
H^{-1}(B_{K'}).
\]

Sections 4--5 and Aubin--Lions give a subsequence such that

\[
\boxed{
V_j\to V
\quad\text{strongly in }
L^2(B_{K'}\times[-T',0]).
}
\]

Also

\[
\nabla V_j\rightharpoonup\nabla V
\]

weakly in local spacetime `L2`.

Thus the finite-cylinder spacetime compactness problem is solved on the mass/coefficient-controlled branch.

---

## 7. Passing to the heat equation

Assume in addition

\[
\boxed{
\mathcal C_j(K,T)\to0.
}
\]

For every compactly supported smooth test function `phi` in `Q'`, the lower-order terms obey

\[
\int A_j\cdot\nabla V_j\,\phi\to0
\]

and

\[
\int C_jV_j\phi\to0,
\]

using the coefficient convergence and uniform local `H1/L2` bounds.

Passing to the weak formulation gives

\[
\boxed{
\partial_\tau V=\Delta V
\quad\text{on }Q'.
}
\]

Since `Q'` was arbitrary inside `Q`, the limit is caloric on the whole fixed controlled cylinder.

---

## 8. Compatibility with the nonzero time-zero tangent

M17-251 supplies a time-zero subsequence with

\[
V_j(\cdot,0)\to V_0
\quad\text{strongly in local }L^2
\]

and

\[
V_0\not\equiv0.
\]

The parabolic bounds above give weak time continuity in a negative Sobolev space, and the spacetime weak formulation identifies the terminal trace with the same `V_0` after passing to the common subsequence.

Hence on the no-payer controlled branch,

\[
\boxed{
V(\cdot,0)=V_0\not\equiv0.
}
\]

The caloric limit is genuinely nonzero.

---

## 9. Exhaustive finite-cylinder gate

For every fixed `K,T`,

\[
\boxed{
H_{normalized\ packet}
\Longrightarrow
H_{strong\ spacetime\ L2\ compactness}
\lor
G_{normalized\ surrounding\text{-}mass\ decompactification}
\lor
G_{scaled\ ambient/coefficient\ action}.
}
\]

On the first branch, if the scaled coefficients vanish, the limit is heat.

Define the two explicit failures as

\[
\boxed{
G_{mass\ decompactification}(K,T):
\quad
\mathcal M_j(K,T)\to\infty
}
\]

and

\[
\boxed{
G_{scaled\ coefficient}(K,T):
\quad
\mathcal C_j(K,T)\not\to0.
}
\]

No generic `compactness loss` label is needed.

---

## 10. Diagonal local ancient heat limit

Combine M17-254 with the present gate for integer

\[
K,T=1,2,3,\dots.
\]

If for every fixed pair `(K,T)` the normalized mass stays bounded and the scaled coefficients vanish, a diagonal subsequence yields

\[
\boxed{
V_j\to V
\quad\text{locally in spacetime},
}
\]

where

\[
\boxed{
\partial_\tau V=\Delta V
\quad\text{on }\mathbb R^3\times(-\infty,0],
}
\]

and

\[
\boxed{V(\cdot,0)\not\equiv0.}
\]

This produces a nonzero ancient **local-`L2`** heat tangent.

It does not yet give a uniform global `L2` bound.

---

## 11. New narrow frontier

After M17-255, the payer-free intrinsic line is reduced to

\[
\boxed{
H_{nonzero\ ancient\ local\text{-}L2\ heat\ tangent}
\lor
G_{normalized\ mass\ decompactification}
\lor
G_{scaled\ ambient/coefficient}
\lor
G_{subscale/nodal}.
}
\]

M17-252 closes the first branch only if a uniform global `L2` bound or another suitable heat-growth Liouville condition is added.

Thus the next genuinely new target is the **spatial growth/tightness profile of the normalized ancient heat tangent**.

---

## 12. DSD audit

- Full spacetime `H2` compactness is not assumed; `H1/H^-1` is sufficient for Aubin--Lions.
- The packet-normalized surrounding mass is made an explicit hypothesis/exit.
- Scaled lower-order coefficients are separated from mass decompactification.
- Strong local `L2` convergence is derived on strictly interior cylinders.
- The heat equation is obtained only when the scaled coefficients actually vanish.
- A local ancient heat tangent is not confused with a global `L2` ancient heat tangent.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
