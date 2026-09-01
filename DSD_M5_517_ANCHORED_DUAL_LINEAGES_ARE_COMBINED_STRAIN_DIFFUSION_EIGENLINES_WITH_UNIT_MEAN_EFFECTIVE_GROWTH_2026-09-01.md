# DSD M5-517 — Anchored dual lineages are combined strain-diffusion eigenlines with unit mean effective growth

Date: 2026-09-01

Status: **ANCHORED-AMPLITUDE LEDGER / ON THE M5-516 ANCHORED NONCOLLINEAR PAIR, EACH PERSISTENT LINEAGE HAS ZERO MATERIAL DIRECTION VELOCITY / THE SIMILARITY VORTICITY EQUATION THEN FORCES THE ORTHOGONAL PART OF `Sigma W + Delta W` TO VANISH EXACTLY, SO EACH ANCHORED VORTICITY VECTOR IS AN EIGENLINE OF THE COMBINED STRAIN-DIFFUSION ACTION, NOT OF STRAIN ALONE / THE PARALLEL PART GIVES THE EXACT MATERIAL AMPLITUDE LAW `D_B log rho = sigma - 1 + Delta rho/rho - |grad xi|^2` / IF THE COHERENT ANCHORED CARRIER REMAINS UNIFORMLY NONDEGENERATE, `log rho` IS A BOUNDED COBoundary AND THE INVARIANT MEAN EFFECTIVE GROWTH IS EXACTLY `1` / IF UNIFORM NONDEGENERACY FAILS, THE BRANCH IS A CARRIER-DEGENERATION/REFORMATION CHANNEL RATHER THAN A QUIET ANCHORED LINEAGE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-516

The narrow rigid-pair survivor has two persistent noncollinear material-flux lineages `a,b` with fixed similarity-frame directions

\[
\boxed{
\xi_a'\equiv0,
\qquad
\xi_b'\equiv0.
}
\]

For each lineage,

\[
W_i=\rho_i\xi_i,
\qquad
\rho_i>0
\]

on its coherent nonzero carrier corridor.

M5-516 already gives the orthogonal direction balance

\[
\boxed{
\tau_i=-\mathcal D_i,
}
\]

where

\[
\tau_i=(I-\xi_i\otimes\xi_i)\Sigma_i\xi_i
\]

and

\[
\mathcal D_i
=\rho_i^{-1}(I-\xi_i\otimes\xi_i)\Delta W_i.
\]

M5-517 derives the full vector and scalar consequences of this anchored condition.

---

## 2. Similarity material derivative

The similarity material velocity is

\[
\boxed{
B(y,\theta)
=U(y,\theta)+\frac12y.
}
\]

Write

\[
D_B
:=
\partial_\theta+B\cdot\nabla.
\]

The similarity vorticity equation from M5-486 is

\[
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
=(W\cdot\nabla)U+\Delta W.
\]

Because the antisymmetric part of `grad U` annihilates the vorticity vector itself,

\[
(W\cdot\nabla)U
=\Sigma W.
\]

Hence

\[
\boxed{
D_BW+W
=\Sigma W+\Delta W.
}
\]

This is the exact material similarity equation used below.

---

## 3. Split magnitude and direction

Let

\[
W=\rho\xi,
\qquad
|\xi|=1.
\]

Then

\[
D_BW
=(D_B\rho)\xi
+\rho D_B\xi.
\]

Thus

\[
(D_B\rho)\xi
+\rho D_B\xi
+\rho\xi
=
\rho\Sigma\xi+\Delta(\rho\xi).
\]

Project this equation parallel and perpendicular to `xi`.

---

## 4. Orthogonal projection: the combined eigenline relation

Apply

\[
P_\xi^\perp
:=
I-\xi\otimes\xi.
\]

The left side gives

\[
\rho D_B\xi.
\]

Therefore

\[
\boxed{
\rho D_B\xi
=P_\xi^\perp(\rho\Sigma\xi+\Delta W).
}
\]

Equivalently,

\[
D_B\xi
=\tau+\mathcal D_\xi,
\]

which recovers the direction equation used in M5-491--516.

On an anchored lineage,

\[
D_B\xi=0.
\]

Hence

\[
\boxed{
P_\xi^\perp(\Sigma W+\Delta W)=0.
}
\]

Thus there exists a scalar `lambda_eff` such that

\[
\boxed{
\Sigma W+\Delta W
=\lambda_{eff}W
}
\]

along the anchored material lineage.

This is the **combined strain-diffusion eigenline** condition.

It must not be replaced by

\[
\Sigma W\parallel W,
\]

because transverse strain may be canceled by transverse diffusion.

---

## 5. Expand the projected diffusion exactly

Using

\[
\Delta(\rho\xi)
=(\Delta\rho)\xi
+2\nabla\rho\cdot\nabla\xi
+\rho\Delta\xi,
\]

and

\[
\xi\cdot\partial_j\xi=0,
\]

we obtain

\[
\boxed{
P_\xi^\perp\Delta W
=2\nabla\rho\cdot\nabla\xi
+\rho P_\xi^\perp\Delta\xi.
}
\]

Therefore the anchored balance is

\[
\boxed{
\rho\tau
+2\nabla\rho\cdot\nabla\xi
+\rho P_\xi^\perp\Delta\xi
=0.
}
\]

Equivalently,

\[
\boxed{
\tau
=-2\nabla(\log\rho)\cdot\nabla\xi
-P_\xi^\perp\Delta\xi.
}
\]

This makes explicit that the fixed direction can be maintained by a weighted harmonic-map-type diffusion tension opposing transverse strain.

---

## 6. Parallel projection: exact amplitude law

Dot the full material equation with `xi`.

Because

\[
\xi\cdot D_B\xi=0,
\]

we obtain

\[
D_B\rho+\rho
=\rho\sigma+\xi\cdot\Delta W,
\]

where

\[
\sigma
:=
\xi\cdot\Sigma\xi.
\]

Now

\[
\xi\cdot\Delta W
=\Delta\rho
+\rho\xi\cdot\Delta\xi.
\]

From differentiating `|xi|^2=1`,

\[
\xi\cdot\Delta\xi
=-|\nabla\xi|^2.
\]

Therefore

\[
\boxed{
D_B\rho
=(\sigma-1)\rho
+\Delta\rho
-\rho|\nabla\xi|^2.
}
\]

Dividing by positive `rho`,

\[
\boxed{
D_B\log\rho
=
\sigma-1
+\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2.
}
\]

This is the exact scalar amplitude ledger on an anchored coherent lineage.

---

## 7. Effective eigenvalue

The parallel part of the combined eigenline relation gives

\[
\lambda_{eff}
=
\sigma
+\frac{\xi\cdot\Delta W}{\rho}.
\]

Using the previous identity,

\[
\boxed{
\lambda_{eff}
=
\sigma
+\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2.
}
\]

The amplitude equation is therefore simply

\[
\boxed{
D_B\log\rho
=\lambda_{eff}-1.
}
\]

The similarity damping contributes the distinguished scalar `1`.

---

## 8. Carrier nondegeneracy split

To average `log rho`, one must not silently assume a positive amplitude floor.

There are two cases.

### A. Uniformly nondegenerate anchored carrier

There exist

\[
0<\rho_-
\le\rho_+<\infty
\]

such that along the coherent persistent material marker

\[
\boxed{
\rho_-
\le\rho(\theta)
\le\rho_+.
}
\]

The upper bound is inherited from the compact Type-I/smooth hull.

The lower bound is an additional property of the quiet nondegenerate lineage and must be checked or selected explicitly.

### B. Carrier degeneration

There is a sequence

\[
\theta_n
\]

with

\[
\boxed{
\rho(\theta_n)\to0.
}
\]

Then the normalized direction of that selected carrier loses uniform active meaning.  Recovering a fixed-flux coherent packet requires recentering, reselecting, or reforming the carrier.

This is a **carrier-degeneration/reformation channel**, not the quiet anchored subbranch.

M5-517 does not identify it with a contradiction.

---

## 9. Invariant mean on the nondegenerate branch

Assume Case A.

Then

\[
\log\rho
\]

is bounded along the complete recurrent material lineage.

Integrating over a long interval,

\[
\frac1T
\int_0^T
D_B\log\rho\,d\theta
=
\frac{\log\rho(T)-\log\rho(0)}{T}
\to0.
\]

Hence the recurrent/Cesaro mean satisfies

\[
\boxed{
\langle\lambda_{eff}\rangle
=1.
}
\]

Equivalently,

\[
\boxed{
\langle\sigma\rangle
=
1
-\left\langle\frac{\Delta\rho}{\rho}\right\rangle
+\langle|\nabla\xi|^2\rangle.
}
\]

This is an exact scalar balance for each nondegenerate anchored lineage.

---

## 10. Sign audit

The last identity is not yet a one-sided lower bound for `sigma`.

The term

\[
\frac{\Delta\rho}{\rho}
\]

has no definite sign along a generic material marker.

Although at an instantaneous spatial maximum of `rho` one has

\[
\Delta\rho\le0,
\]

the persistent material marker need not remain an instantaneous spatial maximum at all times.

Therefore it would be invalid to conclude globally that

\[
\langle\sigma\rangle
\ge1+\langle|\nabla\xi|^2\rangle
\]

without an additional maximum-tracking theorem.

This firewall is essential.

---

## 11. Two anchored lineages

Apply the result separately to the fixed noncollinear pair `a,b`.

On the uniformly nondegenerate anchored subbranch,

\[
\boxed{
\Sigma_iW_i+\Delta W_i
=\lambda_iW_i,
\qquad
\langle\lambda_i\rangle=1,
\qquad i=a,b.
}
\]

Also

\[
\boxed{
\tau_i=-\mathcal D_i.
}
\]

Thus the narrow compact survivor must maintain two persistent nonparallel material vorticity axes, each satisfying simultaneously

1. exact orthogonal strain-diffusion cancellation;
2. a combined strain-diffusion eigenline equation;
3. unit mean effective growth against similarity damping.

The tensors/fields are evaluated at different lineage locations, so this still does not reduce to one common matrix eigenvector problem.

---

## 12. Relation to global production

The same ergodic component has

\[
\boxed{
\langle Q\rangle>0,
}

where

\[
Q
=\int\rho^2\sigma\,dy.
\]

The lineage mean condition

\[
\langle\lambda_i\rangle=1
\]

is a material/genealogical scalar balance, while `Q` is an Eulerian global `rho^2`-weighted production balance.

They must not be identified.

A future closure requires a quantitative bridge from persistent lineage sampling to the Eulerian production measure.

---

## 13. Updated anchored frontier

The M5-516 anchored branch becomes

\[
\boxed{
\mathcal B_{pair}^{anchor}
\Longrightarrow
H_{carrier}^{degenerate/reform}
\lor
\mathcal B_{eig}^{dual},
}
\]

where the nondegenerate eigenline branch satisfies

\[
\boxed{
\begin{aligned}
&\xi_a,\xi_b\text{ fixed and noncollinear},\\
&\Sigma_iW_i+\Delta W_i=\lambda_iW_i,\\
&\tau_i=-\mathcal D_i,\\
&\langle\lambda_i\rangle=1,
\qquad i=a,b.
\end{aligned}
}
\]

This is the sharpest current description of the quiet anchored escape.

---

## 14. Highest-value next target

The next audit should determine whether `H_carrier^(degenerate/reform)` is already absorbed by the finite-memory replacement ledger, and then study the nondegenerate eigenline branch through **lineage-to-Eulerian sampling**.

A useful target is to construct a fixed coherent packet weight `chi_i` around each anchored lineage and compare

\[
\int\chi_i\rho^2\sigma\,dy
\]

with the material scalar balance

\[
\lambda_i-1=D_B\log\rho_i.
\]

If repeated anchored-lineage maintenance forces a fixed positive local Eulerian production bill that cannot be supplied without nonzero scalar flux diffusion or packet replacement, the finite recurrent cycle may close.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
