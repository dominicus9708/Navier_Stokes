# DSD M17-153 — The third log-amplitude jet splits into a CE-H-determined trace and a seven-component STF firewall directly seen by the generic fold

Date: 2026-09-05  
Canonical ID: **M17-153**

Status: **RANK-3 IRREDUCIBLE JET REDUCTION / M17-152 IDENTIFIES `2 nabla^3(log rho)[grad kappa]` AS THE NEW ADDITIVE RECHARGE OF `Hess kappa`. THE THIRD LOG-AMPLITUDE JET IS NOT FULLY FREE. DIFFERENTIATING `kappa=Delta psi+|grad psi|^2-|grad xi|^2`, `psi=log rho`, FIXES ITS TRACE VECTOR `t_j=T_iij` EXACTLY AS `t=grad kappa-2(Hess psi)grad psi+grad|grad xi|^2`. IN THREE DIMENSIONS EVERY SYMMETRIC RANK-3 TENSOR DECOMPOSES UNIQUELY AS `T=T_STF+(1/5)Sym(delta tensor t)`, LEAVING EXACTLY SEVEN STF COMPONENTS. THE M17-152 SOURCE THEN SPLITS INTO A COMPLETELY LOWER-JET-DETERMINED TRACE PART PLUS `2 T_STF[grad kappa]`. FOR NONZERO `grad kappa`, THIS STF CONTRACTION IS A TRACE-FREE SYMMETRIC RANK-2 SOURCE WITH FIVE ACCESSIBLE COMPONENTS; TWO STF-3 COMPONENTS LIE IN THE CONTRACTION KERNEL. AT A PEAK TANGENCY, GENERIC FOLD CURVATURE SATISFIES THE EXACT IDENTITY `C_k=D_k^2g=T_kkxi+qH_xin=T_STF_kkxi+(1/5)t_xi+qH_xin`. THUS THE FOLD ITSELF DIRECTLY PROBES THE RESIDUAL STF THIRD-JET FIREWALL. THE FINITE-JET ESCALATION HAS THEREFORE BEEN REDUCED TO A PRECISE SEVEN-COMPONENT NORMALIZED TENSOR, NOT AN UNSTRUCTURED THIRD-DERIVATIVE CLASS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Third log-amplitude tensor

Set

\[
\psi:=\log\rho.
\]

Define the fully symmetric Euclidean third derivative

\[
\boxed{
T:=\nabla^3\psi,
\qquad
T_{ijk}:=\partial_{ijk}\psi.
}
\]

In three dimensions a symmetric rank-3 tensor has

\[
\binom{3+3-1}{3}=10
\]

independent components.

Its trace vector is

\[
\boxed{
t_k:=T_{iik}=\partial_k\Delta\psi.
}
\]

This contains three components.

---

## 2. Differentiated scalar CE-H identity fixes the trace vector

M17-144 gives

\[
\boxed{
\kappa
=\Delta\psi+|\nabla\psi|^2-|\nabla\xi|^2.
}
\]

Differentiate spatially:

\[
\nabla\kappa
=
\nabla\Delta\psi
+2(\nabla^2\psi)\nabla\psi
-\nabla|\nabla\xi|^2.
\]

Let

\[
G:=\nabla\kappa,
\qquad
H:=\nabla^2\psi.
\]

Since

\[
\nabla\Delta\psi=t,
\]

we obtain the exact trace-vector law

\[
\boxed{
t
=G-2H\nabla\psi+\nabla|\nabla\xi|^2.
}
\]

Thus all three trace components of `T` are already determined by lower normalized jets.

---

## 3. Unique STF decomposition in three dimensions

Define

\[
\boxed{
T^0_{ijk}
:=
T_{ijk}
-\frac15
\left(
\delta_{ij}t_k
+\delta_{ik}t_j
+\delta_{jk}t_i
\right).
}
\]

Contract the first two indices:

\[
T^0_{iik}
=t_k-rac15(3t_k+t_k+t_k)=0.
\]

Therefore

\[
\boxed{T^0=STF_3(T)}
\]

is symmetric and trace free.

Conversely,

\[
\boxed{
T_{ijk}
=
T^0_{ijk}
+\frac15
\left(
\delta_{ij}t_k
+\delta_{ik}t_j
+\delta_{jk}t_i
\right).
}
\]

A symmetric rank-3 STF tensor in three dimensions has

\[
10-3=7
\]

independent components.

Hence the scalar CE-H identity removes exactly the trace sector and leaves a seven-component irreducible rank-3 firewall.

---

## 4. Decompose the M17-152 source `T[G]`

M17-152 uses the symmetric rank-2 contraction

\[
[T[G]]_{ij}:=T_{ijm}G_m.
\]

Insert the STF decomposition:

\[
\boxed{
T[G]
=
T^0[G]
+\frac15
\left[
(t\cdot G)I
+t\otimes G
+G\otimes t
\right].
}
\]

The second term is fully determined by lower jets because `t` is fixed by Section 2.

The only genuinely residual third-jet source is

\[
\boxed{T^0[G].}
\]

Thus the leading M17-152 Hessian-`kappa` equation can be rewritten as

\[
\boxed{
\begin{aligned}
D_BK
={}&L_\rho K+2(HK+KH)-2K\\
&+2T^0[G]\\
&+\frac25\left[
(t\cdot G)I+t\otimes G+G\otimes t
\right]
+o(1),
\end{aligned}
}
\]

with `t` already lower-jet determined.

---

## 5. Dimension of the STF contraction channel

Fix a nonzero vector

\[
G\neq0.
\]

Choose an orthonormal frame with

\[
G=|G|e_3.
\]

Then

\[
[T^0[G]]_{ij}
=|G|T^0_{ij3}.
\]

Because `T^0` is trace free,

\[
\operatorname{tr}(T^0[G])
=|G|T^0_{ii3}=0.
\]

Thus `T^0[G]` lies in the five-dimensional space `STF_2` of symmetric trace-free rank-2 tensors.

The linear map

\[
STF_3\to STF_2,
\qquad
T^0\mapsto T^0[G]
\]

has a seven-dimensional domain and, for `G!=0`, can access the full five-dimensional STF-2 target.
Consequently its kernel has dimension two.

Hence, on the generic-fold branch where

\[
|G|\gtrsim1,
\]

the residual seven-component third jet can provide five independent trace-free recharge components to `Hess kappa`, while two components remain invisible to this particular contraction.

---

## 6. Generic fold curvature directly sees the third jet

At a peak,

\[
g=D_\xi\psi=0.
\]

At a director-area tangency,

\[
D_kg=0,
\qquad
D_k\xi=0.
\]

M17-099 gives

\[
D_kk=\gamma_k n,
\]

and tangency gives

\[
\gamma_k=q.
\]

M17-148 gives

\[
H_{\xi k}=0.
\]

Now

\[
D_kg=H(k,\xi).
\]

Differentiate once more along `k`:

\[
\begin{aligned}
D_k^2g
&=D_k[H(k,\xi)]\\
&=(\nabla_kH)(k,\xi)
+H(D_kk,\xi)
+H(k,D_k\xi).
\end{aligned}
\]

Because

\[
\nabla H=T,
\qquad
D_kk=qn,
\qquad
D_k\xi=0,
\]

we obtain the exact fold-curvature identity

\[
\boxed{
C_k:=D_k^2g
=T_{kk\xi}+qH_{\xi n}.
}
\]

A generic quadratic fold requires

\[
\boxed{C_k\neq0.}
\]

---

## 7. Fold curvature in STF variables

For the component `T_{kk xi}`, the STF decomposition gives

\[
T_{kk\xi}
=T^0_{kk\xi}+\frac15t_\xi
\]

because

\[
\delta_{kk}=1,
\qquad
\delta_{k\xi}=0.
\]

Therefore

\[
\boxed{
C_k
=T^0_{kk\xi}
+\frac15t_\xi
+qH_{\xi n}.
}
\]

Thus the generic fold itself directly probes one component of the residual STF rank-3 log-amplitude jet.

If the lower-jet contribution

\[
\frac15t_\xi+qH_{\xi n}
\]

is small or cancels, fold nondegeneracy forces

\[
\boxed{|T^0_{kk\xi}|\gtrsim|C_k|.}
\]

No arbitrary third derivative has been invoked: this is one explicit STF component.

---

## 8. Lower-jet expression for `t_xi` at tangency

Section 2 gives

\[
t_\xi
=D_\xi\kappa
-2H(\xi,\nabla\psi)
+D_\xi|\nabla\xi|^2.
\]

At a peak tangency,

\[
\nabla\psi=u k+v n,
\]

and

\[
H_{\xi k}=0.
\]

Hence

\[
H(\xi,\nabla\psi)
=vH_{\xi n}.
\]

Therefore

\[
\boxed{
t_\xi
=D_\xi\kappa
-2vH_{\xi n}
+D_\xi|\nabla\xi|^2.
}
\]

The fold identity becomes

\[
\boxed{
C_k
=T^0_{kk\xi}
+\frac15D_\xi\kappa
+\left(q-\frac{2v}{5}\right)H_{\xi n}
+\frac15D_\xi|\nabla\xi|^2.
}
\]

Thus the fold curvature couples precisely four normalized ingredients:

1. one STF third log-amplitude component;
2. the fold-driver gradient `D_xi kappa`;
3. the mixed log-amplitude Hessian;
4. the vortex-direction derivative of the director metric.

---

## 9. Persistent-ribbon contrast

On a persistent critical ribbon,

\[
g\equiv0
\]

along the kernel fiber, so

\[
D_kg=0,
\qquad
D_k^2g=0.
\]

Therefore the same identity gives the exact ribbon constraint

\[
\boxed{
T^0_{kk\xi}
=-\frac15t_\xi-qH_{\xi n}.
}
\]

Hence the STF component that is free to make a generic fold nondegenerate is **not** free on a persistent ribbon; there it is slaved to lower jets.

This cleanly separates the generic-fold and persistent-ribbon rank-3 geometries.

---

## 10. DSD audit

### Audit A — `nabla^3 log rho` has ten unconstrained components

Rejected.
The differentiated scalar CE-H equation fixes its three trace components exactly.

### Audit B — the trace-free sector is scalar

Rejected.
It has seven independent components in three dimensions.

### Audit C — all seven STF components recharge `Hess kappa` independently for fixed `grad kappa`

Rejected.
The contraction `T^0[G]` has five-dimensional image and a two-dimensional kernel.

### Audit D — generic fold nondegeneracy is independent of the rank-3 jet

Rejected.
`C_k=T^0_kkxi+(1/5)t_xi+qH_xin` exactly.

### Audit E — nonzero `T^0_kkxi` is a contradiction

Rejected.
It is the current finite normalized STF firewall.

---

## 11. Updated frontier

The surviving quiet generic-fold mechanism has now been compressed to a precise irreducible normalized tensor:

\[
\boxed{
T^0
=STF_3(\nabla^3\log\rho),
\qquad
\dim T^0=7.
}
\]

Its contraction with the already-required order-one multiplier gradient gives the only genuinely new third-jet part of the M17-152 `Hess kappa` recharge:

\[
\boxed{T^0[\nabla\kappa].}
\]

And one component is directly measured by the quadratic fold curvature:

\[
\boxed{
D_k^2g
=T^0_{kk\xi}
+\frac15t_\xi
+qH_{\xi n}.
}
\]

The next efficient gate is to derive the material evolution of this STF rank-3 log-amplitude tensor, or at minimum of the fold-visible component `T^0_kkxi`, and test whether its recurrent maintenance again requires a higher irreducible jet or instead closes through existing `kappa`/director dynamics.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
