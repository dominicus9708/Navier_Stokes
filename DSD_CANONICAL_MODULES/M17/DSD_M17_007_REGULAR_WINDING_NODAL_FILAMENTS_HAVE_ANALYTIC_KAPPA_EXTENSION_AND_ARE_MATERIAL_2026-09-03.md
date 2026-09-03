# DSD M17-007 — Regular winding nodal filaments have analytic kappa extension and are material

Date: 2026-09-03
Canonical ID: **M17-007**

Status: **INTERNAL ANALYTIC NODAL-RIGIDITY RESULT / IN THE GREAT-CIRCLE COMPLEX FORM `f=u+iv`, THE REAL-POTENTIAL CONDITION IS EQUIVALENT TO THE ANALYTIC CROSS IDENTITY `u Delta v - v Delta u = 0`. AT A REGULAR CODIMENSION-TWO ZERO WHERE `grad u` AND `grad v` ARE INDEPENDENT, ANALYTIC DIVISIBILITY FORCES A COMMON ANALYTIC SCALAR `kappa` THROUGH THE ZERO: `Delta u = kappa u`, `Delta v = kappa v`. THE SIMILARITY VORTICITY EQUATION IS THEN A HOMOGENEOUS LINEAR ODE FOR `W` ALONG MATERIAL TRAJECTORIES EVEN AT THE ZERO, SO THE REGULAR NODAL FILAMENT IS MATERIAL AND ITS WINDING INDEX IS TOPOLOGICALLY FROZEN. CREATION/ANNIHILATION OR RECONNECTION OF WINDING THEREFORE REQUIRES A SINGULAR/DEGENERATE NODAL EVENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Complex analytic nodal field

In M17-006,

\[
f=u+iv=W_1+iW_2
\]

satisfies on the active set

\[
\Delta f=\kappa f,
\qquad \kappa\in\mathbb R.
\]

Equivalently,

\[
\boxed{
u\,\Delta v-v\,\Delta u=0.
}
\]

Unlike the quotient definition of `kappa`, this cross identity is polynomial in the analytic fields `u,v` and therefore extends analytically through their common zero set.

---

## 2. Regular codimension-two zero

Let `p` satisfy

\[
u(p)=v(p)=0
\]

and suppose

\[
\boxed{
\nabla u(p),\nabla v(p)
\text{ are linearly independent}.
}
\]

Then the common zero set is locally a smooth analytic curve by the implicit-function theorem.

Moreover `(u,v,s)` may be used as local analytic coordinates after choosing one longitudinal coordinate `s` along the curve.

In the local analytic ring, `u` and `v` are therefore relatively prime coordinate functions.

---

## 3. Analytic divisibility of the Laplacians

Write

\[
A:=\Delta v,
\qquad
B:=\Delta u.
\]

The analytic identity is

\[
\boxed{uA=vB.}
\]

Since `u` and `v` are relatively prime in the regular local analytic ring,

\[
u\mid B
\]

and

\[
v\mid A.
\]

Hence there exist analytic functions `kappa_1,kappa_2` such that

\[
B=u\kappa_1,
\qquad
A=v\kappa_2.
\]

Substituting into `uA=vB`,

\[
uv\kappa_2=uv\kappa_1.
\]

By analyticity,

\[
\kappa_1=\kappa_2.
\]

Therefore there exists one real-analytic scalar `kappa_ext` such that

\[
\boxed{
\Delta u=\kappa_{ext}u,
\qquad
\Delta v=\kappa_{ext}v
}
\]

through the regular nodal filament.

It agrees with the original `kappa` on the punctured active neighborhood, so it is the analytic extension of the CE-H Laplacian multiplier.

---

## 4. Materiality of the regular zero set

The similarity vorticity equation is

\[
D_BW
=-W+(W\cdot\nabla)U+\Delta W.
\]

Since

\[
(W\cdot\nabla)U=(\nabla U)W,
\]

and the extended Laplacian eigenline is

\[
\Delta W=\kappa_{ext}W,
\]

we have locally

\[
\boxed{
D_BW
=
\left(\nabla U+(\kappa_{ext}-1)I\right)W.
}
\]

This is a homogeneous linear ODE for `W` along every material trajectory.

Therefore

\[
\boxed{
W(\theta_0)=0
\Longrightarrow
W(\theta)=0
}
\]

for as long as the trajectory remains in the regular neighborhood.

Hence the regular codimension-two nodal filament is transported by the material flow `B`.

---

## 5. Winding index is frozen on regular material filaments

Take a small material loop `gamma(theta)` linking the regular nodal filament and avoiding the zero set.

Because

\[
D_B\xi=0
\]

on the active complement, the director value attached to each material point of the loop is constant in time.

Therefore the degree

\[
\boxed{
N_\gamma
=\frac1{2\pi}\oint_{\gamma(\theta)}d\psi
}
\]

is invariant as long as the linked nodal filament remains regular and no zero crosses the loop.

Thus regular winding defects are true material topological defects of the CE-H rank-one branch.

---

## 6. Topology change requires nodal degeneracy

The regular-filament class cannot create, destroy, merge, or reconnect winding indices under a smooth material diffeomorphism.

Any such topology change therefore requires leaving the regular condition

\[
\operatorname{rank}(\nabla u,\nabla v)=2.
\]

Hence

\[
\boxed{
\text{winding topology change}
\Longrightarrow
\operatorname{rank}(\nabla u,\nabla v)<2
}
\]

at the event.

Call this the singular nodal branch

\[
\boxed{T_{nodal}^{deg}}.
\]

The retained rank-one winding problem is therefore split into

\[
\boxed{
R_{nodal}^{material}
\ \lor\ 
T_{nodal}^{deg}.
}
\]

---

## 7. DSD firewall

Materiality of a one-dimensional zero filament is **not** a contradiction with the similarity material-volume expansion law; the latter controls positive three-dimensional volume, not codimension-two sets.

Therefore the regular material-nodal branch remains a legitimate survivor.

The gain is that any dynamic winding replacement/reconnection is no longer free: it must pass through a quantitatively degenerate analytic nodal event. This creates a new bridge to the finite-order analytic critical-set machinery developed earlier for `kappa` sheets.

---

## 8. Next target

Two directions are now sharply separated:

1. **regular material nodal network** — classify whether such a persistent winding network under the full CE-H strain/eigenline equations is forced into an axisymmetric/no-swirl-like regular class;
2. **degenerate nodal events** — derive finite-order analytic jets and determine whether positive-rate nodal topology turnover forces a coherent cost/turnover event analogous to M14.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
