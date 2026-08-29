# DSD M5-194U — Finite-Descriptor Observability No-Go and PDE-Tangent Reduction Audit

Date: 2026-08-29

Parent: `DSD_M5_194T_CORE_SPEED_ROTATION_SHAPE_ORTHOGONAL_DECOMPOSITION_AUDIT_2026-08-29.md`

Status: **NEGATIVE FINITE-OBSERVABILITY FIREWALL / A FINITE FAMILY OF SCALAR DSD DESCRIPTORS CANNOT, BY ITSELF, COERCIVELY CONTROL THE FULL INFINITE-DIMENSIONAL ROTATION-ORTHOGONAL SHAPE TANGENT SPACE / THERE ARE NONZERO DIVERGENCE-FREE LOCAL SHAPE DIRECTIONS ANNIHILATED BY ALL FINITELY MANY DESCRIPTOR DIFFERENTIALS AND BY THE ROTATIONAL TANGENT FUNCTIONALS / THEREFORE POSITIVE SHAPE SPEED CANNOT BE ROUTED EXHAUSTIVELY TO EXISTING H/T CHANNELS BY ADDING FINITELY MANY OBSERVABLES UNLESS THE NAVIER--STOKES DYNAMICS FIRST RESTRICT THE ADMISSIBLE TANGENT SET / THE NEXT OBJECT MUST BE THE ACTUAL LERAY VECTOR FIELD, NOT AN ARBITRARY SHAPE PERTURBATION / GLOBAL REGULARITY UNPROVED.**

---

## 1. Proposed finite observability gate

M5-194T suggested testing whether a finite normalized observable family

\[
\mathcal O(V)
=(O_1(V),\dots,O_N(V))
\]

could satisfy a coercive estimate of the form

\[
\boxed{
\|h\|_{L^2(B_R)}
\le C
\left|D\mathcal O_V[h]\right|
}
\]

for every rotation-orthogonal shape tangent `h`.

If true, the positive shape-speed floor would force one of finitely many already costed descriptors to move.

The present audit shows that this cannot hold on the unrestricted local shape tangent space.

---

## 2. Infinite-dimensional divergence-free local tangent space

Fix a smaller ball

\[
B_r\Subset B_R.
\]

Consider

\[
\mathscr H
:=
\left\{
 h\in C_c^\infty(B_r;\mathbb R^3):
\nabla\cdot h=0
\right\}.
\]

This is infinite dimensional.

For example, if `psi` ranges over compactly supported smooth vector potentials,

\[
h=\nabla\times\psi
\]

belongs to `mathscr H`, and infinitely many linearly independent choices can be supported in pairwise disjoint tiny subballs.

Thus local divergence-free shape perturbations already contain infinitely many independent directions before any global tail is involved.

---

## 3. Impose rotation orthogonality

At a fixed profile `V`, the rotational tangent space has dimension at most three:

\[
\mathscr T_{rot}(V)
=
\operatorname{span}
\{\mathcal R_1V,\mathcal R_2V,\mathcal R_3V\}.
\]

Rotation orthogonality imposes at most three linear conditions:

\[
\boxed{
\langle h,\mathcal R_aV\rangle_{L^2(B_R)}=0,
\qquad a=1,2,3.
}
\]

The subspace

\[
\mathscr H_{shape}
:=
\mathscr H\cap\mathscr T_{rot}(V)^\perp
\]

therefore remains infinite dimensional.

---

## 4. Descriptor differentials are finitely many linear functionals

Assume each descriptor `O_k` is differentiable at `V` in the local function topology used by the compactness corridor.

Then

\[
\ell_k(h):=DO_k(V)[h]
\]

is a continuous linear functional on the admissible tangent space.

The condition of being invisible to all descriptors is

\[
\boxed{
\ell_k(h)=0,
\qquad k=1,\dots,N.
}
\]

These are only finitely many additional linear constraints.

Therefore

\[
\boxed{
\mathscr K_V
:=
\mathscr H_{shape}
\cap
\bigcap_{k=1}^N\ker\ell_k
}
\]

is still infinite dimensional, unless extra PDE restrictions have already collapsed the tangent space.

In particular, there exists

\[
\boxed{h\ne0}
\]

with

\[
h\perp\mathscr T_{rot}(V)
\]

and

\[
D\mathcal O_V[h]=0.
\]

---

## 5. Direct contradiction to finite coercivity

For such a nonzero `h`, a proposed estimate

\[
\|h\|_2
\le C|D\mathcal O_V[h]|
\]

would give

\[
\|h\|_2\le0,
\]

contradiction.

Therefore

\[
\boxed{
\text{finite scalar descriptor family}
\not\Rightarrow
\text{coercive control of all local shape directions}.
}
\]

This is independent of which particular finite collection is chosen.

Adding more but still finitely many scalar observables cannot repair the dimensional obstruction.

---

## 6. Examples of descriptor-invisible directions

The conclusion applies even if the descriptor list includes quantities such as

- total/local enstrophy;
- strain eigenvalues or finite projective coordinates;
- moving-ball variance;
- finitely many shell masses;
- finitely many moments;
- one or several derivative-frequency scalars;
- center and material-overlap coordinates.

At the differential level each contributes only finitely many linear functionals.

One can choose a compactly supported divergence-free perturbation satisfying all of them simultaneously while remaining nonzero.

The perturbation need not represent a true Navier--Stokes time derivative. That distinction is exactly the next gate.

---

## 7. Compactness of the state class does not remove the tangent obstruction automatically

A compact subset of an infinite-dimensional function space need not be a finite-dimensional manifold.

Even when the orbit closure

\[
\mathcal K
=
\overline{\{V(s):s\in\mathbb R\}}
\]

is compact in a strong local topology, this alone does not imply that its tangent cone is finite dimensional or finitely observable.

Thus

\[
\boxed{
\text{precompact orbit}
\not\Rightarrow
\text{finite-dimensional dynamics}.
}
\]

A genuine inertial-manifold, determining-modes, or finite-dimensional tangent theorem would be needed for that upgrade.

No such theorem has been established here for the critical 3D Leray flow.

---

## 8. The actual time derivative is highly constrained

The shape velocity arising in the proof is not an arbitrary `h`.

The complete Leray orbit satisfies

\[
\boxed{
V_s
=
\Delta V
-\frac12V
-\frac12(Y\cdot\nabla)V
-(V\cdot\nabla)V
-\nabla P.
}
\]

After Leray projection onto divergence-free fields, write

\[
\boxed{
V_s=\mathscr F(V).
}
\]

Therefore the only shape direction that matters at a given state is

\[
\boxed{
V_s^{shape}
=(I-P_{rot}(V))\mathscr F(V).
}
\]

This is one PDE-determined vector, not the whole abstract tangent space.

The finite-dimensional no-go therefore does **not** show that existing descriptors are useless. It shows that any successful observability statement must be proved **on the image of the Leray vector field or on the invariant orbit class**, not on arbitrary perturbations.

---

## 9. Correct PDE observability target

The potentially valid estimate has the form

\[
\boxed{
\|(I-P_{rot})\mathscr F(V)\|_{L^2(B_R)}
\le
C\,
\mathcal C_{HT}(V),
}
\]

where `C_HT(V)` is a genuinely PDE-generated cost functional involving, for example,

- derivative/palinstrophy production;
- projective strain deformation;
- material/boundary flux;
- variance production;
- pressure work;
- or another formed Navier--Stokes channel.

This is not a dimension-counting problem. It requires using the equation.

---

## 10. DSD verdict

### CLOSED

The strategy

\[
\boxed{
\text{add finitely many scalar descriptors until every shape direction is detected}
}
\]

is invalid on the unrestricted shape tangent space.

### PRECISE NEW KERNEL

For any finite descriptor family there is an infinite-dimensional descriptor-invisible local shape kernel before the PDE constraint is imposed.

This kernel must not be mislabeled as `H`, `T`, or harmless.

### SURVIVING ROUTE

Use the actual Leray vector field

\[
\mathscr F(V)
\]

and prove that a large rotation-orthogonal component of that **specific vector field** necessarily produces one of the existing cost channels.

---

## 11. Next audit target

The next calculation should derive a local norm ledger directly from the Leray equation.

Write

\[
V_s^{shape}
=(I-P_{rot})
\left[
\Delta V
-\frac12(V+Y\cdot\nabla V)
-\mathbb P(V\cdot\nabla V)
\right].
\]

Then test the exact alternative:

\[
\boxed{
\|V_s^{shape}\|_2\ge c_0
\Longrightarrow
\begin{cases}
\|\Delta V\|_2\text{ large},\\
\|V+Y\cdot\nabla V\|_2\text{ large},\\
\|\mathbb P(V\cdot\nabla V)\|_2\text{ large},
\end{cases}
}
\]

on the fixed core, after accounting for cutoff/pressure commutators.

The first branch is derivative/palinstrophy-like, the second is spatial homogeneity/scale-shape defect, and the third is nonlinear transport/turnover-like.

The key question is whether the latter two can be charged to existing DSD ledgers or whether one of them is the genuinely new final shape channel.
