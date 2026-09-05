# DSD M17-152 — `kappa`-Hessian evolution reveals third-log-amplitude-jet recharge, so the finite-jet escalation does not close at second order

Date: 2026-09-05  
Canonical ID: **M17-152**

Status: **SECOND-MULTIPLIER-JET AUDIT / M17-151 ROUTES THE SURVIVING MIXED/TRANSVERSE GENERIC-FOLD PAYERS TO ORDER-ONE `Hess kappa`. DIFFERENTIATING THE M5-682 CONSTITUTIVE LAW TWICE GIVES AN EXACT PRINCIPAL STRUCTURE FOR `K:=Hess kappa`: `D_BK=L_rho K+2(Hess psi K+K Hess psi)-2K+2 nabla^3 psi[grad kappa]+F_K` IN THE QUIET LOW-AMPLITUDE LIMIT, `psi=log rho`, WHERE `F_K=o(1)` UNDER THE CORRESPONDING HIGH STRAIN/VELOCITY/NORMALIZED-JET HYPOTHESES. THE TERM `2 nabla^3 psi[grad kappa]` IS AN ADDITIVE NORMALIZED SOURCE FOR `K` WHEN `grad kappa` IS ALREADY ORDER ONE, AS REQUIRED BY THE GENERIC-FOLD DRIVER. THEREFORE `Hess kappa` DOES NOT OBEY A CLOSED HOMOGENEOUS DAMPED SYSTEM ANALOGOUS TO M17-150. THE SECOND-JET FOLD FIREWALL MOVES TO A FINITE THIRD LOG-AMPLITUDE JET, NOT TO AN UNCONTROLLED INFINITE DERIVATIVE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Starting constitutive law

Let

\[
\psi:=\log\rho,
\qquad
G:=\nabla\kappa,
\qquad
K:=\nabla^2\kappa.
\]

M5-682 gives

\[
\boxed{
D_B\kappa
=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom},
}
\]

where

\[
L_\rho
=\Delta+2\nabla\psi\cdot\nabla.
\]

M17-147 already differentiated this once and obtained the full-gradient law.
The present module differentiates once more.

---

## 2. Exact second-gradient material commutator

For every scalar `f`, M17-151 gives

\[
\boxed{
D_B(\nabla^2 f)
=
\nabla^2(D_Bf)
-(\nabla B)^T\nabla^2f
-(\nabla^2f)\nabla B
-\mathcal Q_B(\nabla f),
}
\]

with

\[
[\mathcal Q_B(\nabla f)]_{ij}
=(\partial_{ij}B_\ell)\partial_\ell f.
\]

Apply this to `f=kappa`:

\[
\boxed{
D_BK
=
\nabla^2h
-(\nabla B)^TK
-K\nabla B
-\mathcal Q_B(G),
}
\]

where

\[
h:=D_B\kappa.
\]

---

## 3. Exact Hessian of the weighted Laplacian

For a scalar `f`, first note

\[
\partial_i(L_\rho f)
=L_\rho(\partial_i f)
+2(\partial_{im}\psi)(\partial_mf).
\]

Differentiate once more:

\[
\boxed{
\begin{aligned}
\partial_{ij}(L_\rho f)
={}&
L_\rho(\partial_{ij}f)\\
&+2(\partial_{im}\psi)(\partial_{mj}f)
+2(\partial_{jm}\psi)(\partial_{mi}f)\\
&+2(\partial_{ijm}\psi)(\partial_mf).
\end{aligned}
}
\]

Let

\[
H:=\nabla^2\psi,
\qquad
T:=\nabla^3\psi.
\]

Define the symmetric contraction

\[
\boxed{
[T[G]]_{ij}:=T_{ijm}G_m.
}
\]

Then compactly

\[
\boxed{
\nabla^2(L_\rho f)
=
L_\rho(\nabla^2f)
+2\left(H\nabla^2f+(\nabla^2f)H\right)
+2T[\nabla f].
}
\]

This identity is exact.

---

## 4. Exact structural equation for `K=Hess kappa`

Insert

\[
h=L_\rho\kappa+L_\rho\sigma-\kappa+\mathcal R_{geom}
\]

into Section 2.
Using Section 3 for the `kappa` term,

\[
\begin{aligned}
D_BK
={}&
L_\rho K
+2(HK+KH)
+2T[G]
-K\\
&-(\nabla B)^TK-K\nabla B\\
&+\nabla^2(L_\rho\sigma)
+\nabla^2\mathcal R_{geom}
-\mathcal Q_B(G).
\end{aligned}
\]

Therefore the exact decomposition is

\[
\boxed{
D_BK
=
L_\rho K
+2(HK+KH)
-K
-(\nabla B)^TK-K\nabla B
+2T[G]
+\mathcal F_K,
}
\]

where

\[
\boxed{
\mathcal F_K
:=
\nabla^2(L_\rho\sigma)
+\nabla^2\mathcal R_{geom}
-\mathcal Q_B(G).
}
\]

---

## 5. Quiet low-amplitude high-jet reduction

On the retained M17-147--151 quiet hard hull,

\[
\nabla B
=\frac12I+o(1).
\]

Thus

\[
-(\nabla B)^TK-K\nabla B
=-K+o(1)
\]

for bounded normalized `K`.
Together with the explicit `-K` from the constitutive relaxation term, the total bare damping is

\[
-2K.
\]

With the corresponding higher strain/velocity jet bounds,

\[
\nabla^2(L_\rho\sigma)=o(1),
\]

\[
\nabla^2\mathcal R_{geom}=o(1),
\]

and

\[
\mathcal Q_B(G)=o(1)
\]

for bounded normalized `G`.

Hence

\[
\boxed{
D_BK
=
L_\rho K
+2(HK+KH)
-2K
+2T[G]
+o(1).
}
\]

This is the leading quiet normalized second-multiplier-jet equation.

---

## 6. Why `T[G]` is a genuine additive second-jet recharge

The term

\[
2T[G]
\]

is independent of `K` itself.
If

\[
G=\nabla\kappa
\]

is order one, then a bounded order-one third log-amplitude jet `T` can continuously create/replenish an order-one `K` even when `K` would otherwise damp.

But M17-144/M17-147 show that a uniformly nondegenerate quiet generic fold already requires

\[
|D_\xi\kappa|\gtrsim1,
\]

hence

\[
|G|\gtrsim1.
\]

Therefore the additive source is naturally active on exactly the branch where M17-151 needs `Hess kappa` recharge.

This prevents a direct M17-150-style homogeneous-damping closure at second multiplier order.

---

## 7. The source remains amplitude-scale-free

Under constant fixed-time amplitude rescaling

\[
\rho\mapsto\varepsilon\rho,
\]

all derivatives of

\[
\psi=\log\rho
\]

are unchanged.
Also `kappa` and its normalized derivatives are unchanged within the fixed-time CE-H/director subsystem.

Thus

\[
T[G]
\]

is scale-free.

No quadratic physical-amplitude shell ledger can force it to vanish merely because

\[
\rho\to0.
\]

As always, this homogeneity is not asserted to be a symmetry of the full nonlinear Navier--Stokes system.

---

## 8. Spectral form of the homogeneous part

Ignoring diffusion and `T[G]` momentarily, the homogeneous algebraic action on `K` is

\[
2(HK+KH)-2K.
\]

If `H` is diagonalized with eigenvalues

\[
\lambda_1,\lambda_2,\lambda_3,
\]

then the component `K_ab` has algebraic rate

\[
\boxed{
2(\lambda_a+\lambda_b-1)K_{ab}.
}
\]

Thus the same positive log-amplitude convexity identified in M17-147 can reduce or reverse damping of selected `kappa`-Hessian components.

This reinforces, rather than removes, the normalized-convexity firewall.

---

## 9. Relation to M17-151

M17-151 shows that recurrent mixed/transverse log-amplitude Hessian payers require order-one `K=Hess kappa` recharge.

M17-152 gives the exact leading source for that `K`:

\[
\boxed{2\nabla^3\log\rho[\nabla\kappa].}
\]

Therefore the chain becomes

\[
\boxed{
G_{mix/trans}
\Rightarrow
|\nabla^2\kappa|\gtrsim1
\Rightarrow
\left(
|\nabla^3\log\rho[\nabla\kappa]|\gtrsim1
\ \lor\
\text{convective/diffusive import}
\right)
}
\]

unless a hard exit occurs.

The branch has moved one finite normalized derivative upward.

---

## 10. Why this is not yet an infinite-jet cascade claim

It would be premature to state that each differentiation necessarily introduces an unconstrained new derivative forever.

The third log-amplitude jet `T` is not arbitrary: differentiating the scalar CE-H identity

\[
\kappa
=\Delta\psi+|\nabla\psi|^2-|\nabla\xi|^2
\]

constrains the trace vector of `T`.

Therefore the next audit must split

\[
T=\nabla^3\psi
\]

into

1. its trace part, already determined by `G`, `H`, `grad psi`, and director jets;
2. its symmetric trace-free rank-3 part, not fixed by the scalar CE-H equation.

Only after that decomposition can the true remaining freedom be counted correctly.

---

## 11. DSD audit

### Audit A — `Hess kappa` inherits only homogeneous damping from `kappa`

Rejected.
Differentiating the variable-coefficient weighted diffusion produces the additive `2 T[G]` source.

### Audit B — `T[G]` vanishes on the low-amplitude branch

Rejected.
It is built from derivatives of `log rho` and normalized `kappa` geometry and is amplitude-scale-free.

### Audit C — the new source proves the branch realizable

Rejected.
It only prevents a false second-order damping closure.

### Audit D — the third log-amplitude jet is completely free

Not established. Its trace is constrained by differentiated CE-H and must be removed before counting the true residual degrees of freedom.

### Audit E — this already implies an infinite high-jet escape

Rejected.
The next step is a finite rank-3 trace/STF decomposition.

---

## 12. Updated frontier

The quiet recurrent generic-fold branch now reaches the concrete second-jet equation

\[
\boxed{
D_B\nabla^2\kappa
=
L_\rho\nabla^2\kappa
+2\left(
H_\psi\nabla^2\kappa+
\nabla^2\kappa H_\psi
\right)
-2\nabla^2\kappa
+2\nabla^3\psi[\nabla\kappa]
+o(1).
}
\]

The next highest-value calculation is the exact irreducible decomposition of

\[
\nabla^3\psi
\]

under the scalar CE-H trace constraint and the generic-fold conditions.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
