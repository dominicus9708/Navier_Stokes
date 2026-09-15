# DSD M19-277 — The CE-H source density is an exact spatial Laplacian and cannot by itself supply the positive-mean non-coboundary lag payer

Date: 2026-09-16  
Canonical ID: **M19-277**  
Status: **ACTIVE LAG-TO-SOURCE AUDIT / EXACT SPATIAL-DIVERGENCE FIREWALL / CLOSED-NETWORK NET SOURCE ZERO / WEIGHTED-SOURCE GATE ISOLATED / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-276 reduces every finite-population diffusion cycle to a continuum source response or external exchange. On CE-H the relevant scalar source is

\[
S_p
=
\rho^p\kappa
+
\rho^p|\nabla\xi|^2
+
(p-1)\rho^{p-2}|\nabla\rho|^2,
\qquad p\ge2.
\]

The immediate question is whether the positive finite-depth stretching/production subsystem of M5-587--590 can force a positive invariant mean of this source and thereby furnish the non-coboundary remainder required by M19-271.

The answer for the **raw unweighted source** is no.

The reason is exact rather than heuristic:

\[
\boxed{S_p=\frac1p\Delta(\rho^p).}
\]

Thus its whole-space integral is a boundary term, and on a closed finite material-population network its cell sources sum exactly to zero. The source can redistribute amplitude moment but cannot be a net recurrent positive source.

---

## 2. CE-H scalar amplitude equation

Write

\[
W=\rho\xi,
\qquad
|\xi|=1,
\qquad
\Delta W=\kappa W.
\]

Expanding,

\[
\Delta(\rho\xi)
=(\Delta\rho)\xi
+2\nabla\rho\cdot\nabla\xi
+\rho\Delta\xi.
\]

Take the scalar product with \(\xi\). Since

\[
\xi\cdot\partial_a\xi=0
\]

and

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

one obtains

\[
\kappa\rho
=
\Delta\rho-ho|\nabla\xi|^2.
\]

Hence

\[
\boxed{
\Delta\rho
=
\kappa\rho+ho|\nabla\xi|^2.
}
\]

---

## 3. Exact source identity for every p

For finite \(p\ge2\),

\[
\Delta(\rho^p)
=
p\rho^{p-1}\Delta\rho
+p(p-1)\rho^{p-2}|\nabla\rho|^2.
\]

Insert Section 2:

\[
\frac1p\Delta(\rho^p)
=
\rho^p\kappa
+ho^p|\nabla\xi|^2
+(p-1)\rho^{p-2}|\nabla\rho|^2.
\]

Therefore

\[
\boxed{
S_p
=
\frac1p\Delta(\rho^p).
}
\]

This identity is pointwise wherever the smooth CE-H representation is valid.

---

## 4. Relation to the M18 localized diffusion terms

The weighted bulk diffusion from M18-088 is

\[
D_p^P
=
\int_P
\left[
\rho^{p-2}|\nabla W|^2
+(p-2)\rho^{p-2}|\nabla\rho|^2
\right]dy.
\]

Because

\[
|\nabla W|^2
=|\nabla\rho|^2+ho^2|\nabla\xi|^2,
\]

this becomes

\[
\boxed{
D_p^P
=
\int_P
\left[
\rho^p|\nabla\xi|^2
+(p-1)\rho^{p-2}|\nabla\rho|^2
\right]dy.
}
\]

Thus

\[
S_p
=
\rho^p\kappa
+
\text{the pointwise density of }D_p.
\]

M18-088 gives

\[
\int_P\kappa\rho^pdy
=-D_p^P+B_p^P.
\]

Therefore

\[
\boxed{
\int_PS_pdy
=B_p^P.
}
\]

This is exactly the divergence theorem applied to \(\Delta(\rho^p)/p\).

---

## 5. Closed material-population network has zero net raw source

Let a compatible finite material partition cover \(\Omega_{loc}\):

\[
\Omega_{loc}=\bigcup_{i=1}^NP_i.
\]

M18-089 proves exact antisymmetry of internal boundary exchange. Hence

\[
\sum_iB_{p,i}=B_{p,ext}.
\]

Using Section 4,

\[
\boxed{
\sum_i\int_{P_i}S_pdy
=
B_{p,ext}.
}
\]

On the closed no-export/no-import branch,

\[
B_{p,ext}=0,
\]

so

\[
\boxed{
\int_{\Omega_{loc}}S_pdy=0.
}
\]

Thus no positive population source can be interpreted as a new net source; it must be compensated elsewhere in the same finite network.

---

## 6. Whole-space version

Whenever the whole-space CE-H field has sufficient decay for the boundary flux of \(\nabla(\rho^p)\) to vanish,

\[
\int_{\mathbb R^3}S_pdy
=
\frac1p
\lim_{R\to\infty}
\int_{S_R}\partial_n(\rho^p)dS
=0.
\]

Therefore

\[
\boxed{
\int_{\mathbb R^3}S_p=0
}
\]

under the stated decay/flux condition.

If the boundary flux does not vanish, that failure is an explicit outer-boundary/critical-tail exchange term and must be retained rather than called an interior source.

---

## 7. Positive stretching does not imply positive raw S_p

The production subsystem is controlled by the strain eigenvalue \(\sigma\). On CE-H the material amplitude law is

\[
D_B\rho
=(\sigma+\kappa-1)\rho.
\]

For a recurrent nondegenerate material population, M18-088 gives the exact baseline

\[
\boxed{
\mathbb E_p^P[\sigma+\kappa]
=
1-\frac{3}{2p}
=:c_p.
}
\]

Hence

\[
\boxed{
\mathbb E_p^P[\kappa]
=
c_p-\mathbb E_p^P[\sigma].
}
\]

A larger positive strain average can therefore be balanced by a more negative \(\kappa\) contribution. The CE-H equations do not require the raw spatial source \(S_p\) to become positive when stretching production is positive.

At population level the exact balance is

\[
\frac1p(M_p^P)'
=
A_p^P-D_p^P+B_p^P-c_pM_p^P.
\]

The boundary term \(B_p^P=\int_PS_p\) is a redistribution term, not a new production term.

Thus

\[
\boxed{
\text{positive finite-depth strain production}
\not\Rightarrow
\left\langle\int_PS_p\right\rangle>0
}
\]

without an additional localization/sign theorem.

---

## 8. Why this blocks the naive M19-271 bridge

M19-271 requires a positive-mean non-coboundary remainder capable of paying the signed energy event.

The unweighted source integral over a closed subsystem satisfies

\[
\boxed{
\sum_i\int_{P_i}S_p=0.
}
\]

Hence the proposed bridge

\[
\Gamma_E
\stackrel?\longrightarrow
\int S_p
\]

cannot yield a positive closed-network mean.

At most it can identify where positive and negative source-response sectors are located.

Therefore

\[
\boxed{
\mathcal T_{lag\to source}
\text{ cannot use the raw constant-weight source }S_p
\text{ as the terminal positive payer.}
}
\]

---

## 9. Weighted source pairings are the only remaining local source option

Let \(\psi\) be a smooth spatial test weight. Then, modulo the corresponding boundary term,

\[
\begin{aligned}
\int\psi S_pdy
&=
\frac1p\int\psi\Delta(\rho^p)dy\\
&=
\frac1p\int\rho^p\Delta\psi\,dy.
\end{aligned}
\]

Thus

\[
\boxed{
Q_{p,\psi}
:=
\int\psi S_p
=
\frac1p\int\rho^p\Delta\psi
}
\]

for whole-space/compact-support pairings with vanishing boundary terms.

Consequences:

- \(\psi\equiv1\) gives zero net source;
- harmonic \(\psi\) gives zero;
- any sign-definite weighted source theorem must come from the sign and geometry of \(\Delta\psi\), not from \(S_p\) alone.

Therefore the source route has been reduced to a weighted localization problem.

---

## 10. Spatial-divergence versus temporal coboundary

The identity

\[
S_p=\frac1p\Delta(\rho^p)
\]

is a **spatial** divergence, not the temporal finite-lag coboundary excluded by M19-271.

Nevertheless it has the same accounting consequence on a closed domain: its unweighted total vanishes exactly.

Thus a successful non-coboundary theorem must break both trivial cancellation mechanisms:

1. it cannot be merely a temporal state difference;
2. it cannot be merely the constant-weight integral of a spatial divergence.

This sharply narrows the admissible signed resource.

---

## 11. Refined dynamic target

Replace the broad source target of M19-276 by

\[
\boxed{
\mathcal T_{lag\to weighted\text{-}source}:
\text{derive at fixed lag a canonical nonconstant weight }\psi
\text{ for which }
\left\langle Q_{p,\psi}\right\rangle
\text{ has a strict signed lower bound.}
}
\]

The weight must be supplied by the PDE/geometry itself; choosing it retrospectively from the sign of \(S_p\) would be circular.

A candidate may come from

- the finite-depth wedge energy/enstrophy witnesses;
- a material population boundary geometry;
- a Green/adjoint solution tied to the signed energy observable;
- or a genuine nonlocal critical test function.

---

## 12. Permanent firewalls after M19-277

\[
\boxed{
S_p
=\frac1p\Delta(\rho^p).
}
\]

\[
\boxed{
\text{closed-network }
\int S_p=0.
}
\]

\[
\boxed{
\text{positive stretching}
\not\Rightarrow
\text{positive net }S_p.
}
\]

\[
\boxed{
\text{population boundary exchange}
=
\text{redistribution, not a net interior source}.
}
\]

\[
\boxed{
\text{raw }S_p
\text{ cannot by itself be the M19-271 positive-mean non-coboundary payer}.
}
\]

---

## 13. Immediate next target

Audit the weighted-source route before introducing a new observable family.

For compactly supported or bounded localization weights, determine whether one can have a nontrivial canonical \(\psi\) with sign-definite \(\Delta\psi\).

If no such weight exists, any positive weighted-source theorem must use a sign-changing weight plus an independent localization/correlation estimate. That would move the problem from source positivity to an adjoint-observability theorem.

In parallel, the stationary route remains

\[
\boxed{
\mathcal T_{stress}^{tight}
\lor
\mathcal T_{tail}^{zero\text{-}force\text{-}rigidity}.
}
\]

Global 3D Navier--Stokes regularity remains unproved.
