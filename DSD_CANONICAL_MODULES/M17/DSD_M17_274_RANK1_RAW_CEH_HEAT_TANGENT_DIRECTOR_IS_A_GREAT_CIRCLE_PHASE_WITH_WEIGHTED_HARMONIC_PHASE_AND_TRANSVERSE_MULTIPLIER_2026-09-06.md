# DSD M17-274 — Rank-1 raw CE-H heat-tangent director is a great-circle phase with weighted-harmonic phase and transverse multiplier

Date: 2026-09-06  
Canonical ID: **M17-274**

Status: **LOWER-RANK STRUCTURE THEOREM / M17-273 CONVERTS COMPACT `s2 -> 0` INTO AN ACTUAL RANK-1 OR RANK-0 DIRECTOR TANGENT. ON A CONNECTED CONSTANT-RANK-1 PATCH, THE CONSTANT-RANK THEOREM WRITES THE DIRECTOR LOCALLY AS `xi=gamma(phi)` FOR A CURVE `gamma` ON `S2`. REPARAMETRIZING `gamma` BY ARCLENGTH AND SUBSTITUTING INTO THE EXACT WEIGHTED HARMONIC-MAP EQUATION OF M17-269 SPLITS INTO TWO ORTHOGONAL TARGET DIRECTIONS: THE GEODESIC-CURVATURE COMPONENT AND THE PHASE-TANGENT COMPONENT. BECAUSE `|grad phi|>0` ON A RANK-1 PATCH, THE GEODESIC CURVATURE MUST VANISH, SO `gamma` IS A GREAT CIRCLE. AFTER A FIXED ROTATION, `xi=(cos phi,sin phi,0)`, AND THE PHASE SATISFIES `div(a^2 grad phi)=0`. M17-262 FURTHER GIVES `grad K · grad phi=0`, SO THE MULTIPLIER VARIES ONLY ALONG THE TWO-DIMENSIONAL PHASE-LEVEL LEAVES. THE FULL RANK-1 TANGENT IS THEREFORE A COUPLED SCALAR AMPLITUDE/PHASE/MULTIPLIER SYSTEM, NOT AN ARBITRARY 3D DIRECTOR FIELD. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rank-1 constant-rank coordinates

Let `U` be a connected active patch on which

\[
\boxed{\operatorname{rank}D\xi=1.}
\]

By the constant-rank theorem, after shrinking `U` if necessary there exists a scalar phase

\[
\phi:U\to I\subset\mathbb R
\]

and a regular curve

\[
\gamma:I\to S^2
\]

such that

\[
\boxed{\xi=\gamma(\phi).}
\]

Reparametrize the curve by arclength, so

\[
\boxed{|\gamma'(\phi)|=1.}
\]

Since the director rank is one,

\[
\boxed{|\nabla\phi|>0}
\]

on the retained patch.

---

## 2. Director derivatives

We have

\[
\partial_i\xi
=\gamma'(\phi)\partial_i\phi,
\]

so

\[
\boxed{|\nabla\xi|^2=|\nabla\phi|^2.}
\]

Also

\[
\Delta\xi
=\gamma''(\phi)|\nabla\phi|^2
+\gamma'(\phi)\Delta\phi.
\]

Let

\[
\psi:=\log a.
\]

Then

\[
2\nabla\psi\cdot\nabla\xi
=2\gamma'(\phi)\nabla\psi\cdot\nabla\phi.
\]

---

## 3. Insert into the weighted harmonic-map equation

M17-269 gives

\[
\Delta\xi
+2\nabla\psi\cdot\nabla\xi
+|\nabla\xi|^2\xi
=0.
\]

Substitution yields

\[
\boxed{
\left(\gamma''+\gamma\right)|\nabla\phi|^2
+\gamma'\left(\Delta\phi+2\nabla\psi\cdot\nabla\phi\right)
=0.
}
\]

For a unit-speed curve on `S2`,

\[
\gamma''+\gamma
\]

is the geodesic-curvature vector.
It is orthogonal to both

\[
\gamma
\quad\text{and}\quad
\gamma'.
\]

Therefore the two displayed vector terms are orthogonal.

---

## 4. Great-circle rigidity

Because

\[
|\nabla\phi|>0,
\]

the geodesic-curvature component must vanish:

\[
\boxed{\gamma''+\gamma=0.}
\]

Hence `gamma` is a great circle on the unit sphere.

After one fixed target-space rotation we may write

\[
\boxed{
\xi
=(\cos\phi,\sin\phi,0).
}
\]

This rotation is constant and does not change any spatial-rank or energy statement.

---

## 5. Weighted harmonic phase equation

The remaining `gamma'` component gives

\[
\boxed{
\Delta\phi
+2\nabla\log a\cdot\nabla\phi
=0.
}
\]

Equivalently,

\[
\boxed{
\nabla\cdot(a^2\nabla\phi)=0.
}
\]

Thus the Rank-1 director geometry is encoded by one scalar weighted-harmonic phase.

---

## 6. Multiplier is transverse to the phase gradient

M17-262 proves on every raw CE-H heat tangent

\[
D_{\nabla K}\xi=0.
\]

For the Rank-1 representation,

\[
D_{\nabla K}\xi
=\gamma'(\phi)(\nabla K\cdot\nabla\phi).
\]

Since `gamma'` is nonzero,

\[
\boxed{
\nabla K\cdot\nabla\phi=0.
}
\]

Therefore `K` is constant in the phase-gradient direction and can vary only tangentially to the two-dimensional level leaves of `phi`.

---

## 7. Amplitude equation

The parallel component of `Delta(a xi)=K a xi` from M17-269 is

\[
\frac{\Delta a}{a}
=K+|\nabla\xi|^2.
\]

Since

\[
|\nabla\xi|^2=|\nabla\phi|^2,
\]

we have

\[
\boxed{
\Delta a
=a\left(K+|\nabla\phi|^2\right).
}
\]

The heat-tangent time law is

\[
\boxed{
\partial_\tau a=Ka.
}
\]

Hence

\[
\boxed{
\partial_\tau a
=\Delta a-a|\nabla\phi|^2.
}
\]

The phase is time independent because `partial_tau xi=0`:

\[
\boxed{\partial_\tau\phi=0}
\]

modulo a fixed integer winding choice on each local chart.

---

## 8. Multiplier diffusion

M17-263 gives

\[
\boxed{
\partial_\tau K
=a^{-2}\nabla\cdot(a^2\nabla K).
}
\]

Together with

\[
\nabla K\cdot\nabla\phi=0,
\]

the diffusion of `K` takes place only inside the phase-level leaves.

Thus Rank 1 exchanges the Rank-2 one-dimensional director-fiber diffusion for a two-dimensional leafwise multiplier diffusion.

---

## 9. Divergence-free vorticity constraint

The tangent remains divergence free:

\[
\nabla\cdot V=0.
\]

Since

\[
V=a\xi,
\]

this gives the exact scalar constraint

\[
\boxed{
D_\xi\log a
=-\nabla\cdot\xi.
}
\]

For

\[
\xi=(\cos\phi,\sin\phi,0),
\]

this becomes

\[
\boxed{
\xi\cdot\nabla\log a
=-\gamma'(\phi)\cdot\nabla\phi.
}
\]

This condition must be retained in any Rank-1 construction; scalar amplitude/phase examples that violate it are not vorticity tangents.

---

## 10. Closed Rank-1 system

The local Rank-1 raw CE-H heat tangent therefore obeys

\[
\boxed{
\begin{cases}
\xi=(\cos\phi,\sin\phi,0),\\
\partial_\tau\phi=0,\\
\nabla\cdot(a^2\nabla\phi)=0,\\
\nabla K\cdot\nabla\phi=0,\\
\partial_\tau a=Ka,\\
\Delta a=a(K+|\nabla\phi|^2),\\
\partial_\tau K=a^{-2}\nabla\cdot(a^2\nabla K),\\
\nabla\cdot(a\xi)=0.
\end{cases}
}
\]

This is the correct starting point for the Rank-1 closure audit.

---

## 11. DSD audit

- Rank 1 is assumed on a connected constant-rank patch; the result is local across rank interfaces.
- The great-circle conclusion follows from orthogonal target components, not from a coordinate convention.
- The phase is scalar only after the constant-rank reduction.
- The divergence-free constraint is retained explicitly.
- No claim is yet made that the Rank-1 system has only trivial solutions.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
