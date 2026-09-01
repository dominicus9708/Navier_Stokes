# DSD M5-520 — Exact material-surface vorticity-flux density continuity law

Date: 2026-09-01

Status: **EXACT SURFACE-CONTINUITY IDENTITY / ON THE GLOBALLY SMOOTH COMPACT SIMILARITY BRANCH, THE SIGNED VORTICITY-FLUX DENSITY `f=W·n` ON A MATERIAL SURFACE TRANSPORTED BY `B=U+y/2` SATISFIES AN EXACT LOCAL CONSERVATION LAW / THE SIMILARITY DAMPING, VORTEX STRETCHING, AND MATERIAL AREA-VECTOR DEFORMATION CANCEL AT THE ORIENTED-AREA LEVEL / THE ONLY SOURCE OF SIGNED FLUX REDISTRIBUTION IS THE VISCOUS SURFACE CURRENT `J_Sigma=(curl W)×n`, WITH `D_B f +(1-sigma_n)f + div_Sigma J_Sigma=0` / THUS MARKER MIGRATION CAN OCCUR WITHOUT LINEAGE REPLACEMENT, BUT IT MUST BE REALIZED BY TANGENTIAL SURFACE-CURRENT THROUGHPUT / THE CURRENT IS SIGN-INDEFINITE AND DOES NOT YET GIVE A STRICT COCYCLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity equations and material velocity

On the M5-508 globally smooth compact branch use the similarity vorticity equation

\[
\partial_\theta W
+W
+\frac12(y\cdot\nabla)W
+(U\cdot\nabla)W
=(W\cdot\nabla)U+\Delta W,
\]

with

\[
\nabla\cdot U=0,
\qquad
\nabla\cdot W=0.
\]

Define the similarity material velocity

\[
\boxed{B:=U+\frac12y.}
\]

Then

\[
\nabla\cdot B=\frac32
\]

and

\[
\boxed{
D_BW
:=(\partial_\theta+B\cdot\nabla)W
=(\nabla U)W-W+\Delta W.
}
\]

---

## 2. Oriented material area-vector evolution

Let `Sigma(theta)` be a smooth oriented material surface transported by `B`.

Write its oriented area vector as

\[
q:=n\,dA.
\]

For a material surface transported by a velocity field `B`, the oriented area vector obeys

\[
D_Bq
=\big[(\nabla\cdot B)I-(\nabla B)^T\big]q.
\]

Since

\[
\nabla B=\nabla U+\frac12I,
\qquad
\nabla\cdot B=\frac32,
\]

we obtain

\[
\boxed{
D_Bq
=\big[I-(\nabla U)^T\big]q.
}
\]

This form is the exact similarity counterpart of the physical material-area evolution.

---

## 3. Exact cancellation at the oriented-area level

The signed flux element is

\[
W\cdot q.
\]

Differentiate materially:

\[
D_B(W\cdot q)
=(D_BW)\cdot q+W\cdot D_Bq.
\]

Insert the equations from Sections 1--2:

\[
\begin{aligned}
D_B(W\cdot q)
&=
\big[(\nabla U)W-W+\Delta W\big]\cdot q\\
&\quad+
W\cdot\big[I-(\nabla U)^T\big]q.
\end{aligned}
\]

The strain/rotation terms cancel exactly because

\[
((\nabla U)W)\cdot q
=W\cdot(\nabla U)^Tq,
\]

and the explicit similarity `-W` cancels the `+I` area-vector term.

Therefore

\[
\boxed{
D_B(W\cdot q)=\Delta W\cdot q.
}
\]

Equivalently,

\[
\boxed{
D_B\big[(W\cdot n)dA\big]
=(\Delta W\cdot n)dA.
}
\]

This is the pointwise oriented-area version of the integrated M5-489 material-flux law.

---

## 4. Scalar flux-density equation

Define

\[
\boxed{f:=W\cdot n.}
\]

The material area element satisfies

\[
D_B(dA)
=\big(\nabla\cdot B-n\cdot(\nabla B)n\big)dA.
\]

Because the antisymmetric part of `grad U` drops out of the quadratic normal form, define

\[
\sigma_n:=n\cdot\Sigma n,
\qquad
\Sigma:=\frac12(\nabla U+\nabla U^T).
\]

Then

\[
\nabla\cdot B-n\cdot(\nabla B)n
=
\frac32-\left(\sigma_n+\frac12\right)
=1-\sigma_n.
\]

Hence

\[
\boxed{
D_B(dA)=(1-\sigma_n)dA.
}
\]

Combining with Section 3 gives

\[
\boxed{
D_Bf+(1-\sigma_n)f=\Delta W\cdot n.
}
\]

Where `f` does not vanish, this can also be written as

\[
\boxed{
D_B\log|f|
=
\frac{\Delta W\cdot n}{f}
-(1-\sigma_n).
}
\]

This logarithmic formula is only local to sign-nondegenerate flux-density markers and must not be used across `f=0`.

---

## 5. Viscous term is a surface divergence

Since

\[
\nabla\cdot W=0,
\]

we have the vector identity

\[
\Delta W
=-\nabla\times(\nabla\times W).
\]

Set

\[
A:=\nabla\times W.
\]

For any smooth oriented surface,

\[
n\cdot(\nabla\times A)
=
\operatorname{div}_{\Sigma}(A\times n).
\]

Therefore

\[
\boxed{
\Delta W\cdot n
=
-\operatorname{div}_{\Sigma}
\big[(\nabla\times W)\times n\big].
}
\]

Define the tangential surface current

\[
\boxed{
J_{\Sigma}
:=(\nabla\times W)\times n.
}
\]

Then the exact local flux-density continuity equation is

\[
\boxed{
D_Bf
+(1-\sigma_n)f
+\operatorname{div}_{\Sigma}J_{\Sigma}
=0.
}
\]

Thus viscosity does not act as an untyped scalar source of signed vorticity flux on the material surface.

It redistributes signed flux density through a tangential surface current.

---

## 6. Recovery of the integrated M5-489 law

Let `Sigma(theta)` be a material surface patch with material boundary.

Integrating the local continuity law with the material surface transport theorem gives

\[
\frac d{d\theta}
\int_{\Sigma(\theta)}f\,dA
=
-\int_{\Sigma(\theta)}
\operatorname{div}_{\Sigma}J_{\Sigma}\,dA.
\]

By the surface divergence theorem,

\[
\boxed{
\frac d{d\theta}
\int_{\Sigma(\theta)}W\cdot n\,dA
=
-\oint_{\partial\Sigma(\theta)}
J_{\Sigma}\cdot\mu\,ds,
}
\]

where `mu` is the outward co-normal in the surface.

With the positively oriented boundary tangent

\[
t=n\times\mu,
\]

we have

\[
J_{\Sigma}\cdot\mu
=(\nabla\times W)\cdot t.
\]

Hence

\[
\boxed{
\frac d{d\theta}\Phi
=
-\oint_{\partial\Sigma}
(\nabla\times W)\cdot t\,ds
=
\int_{\Sigma}\Delta W\cdot n\,dA,
}
\]

which exactly recovers M5-489.

---

## 7. Closed surfaces and open lineage patches

For a closed smooth surface,

\[
\partial\Sigma=\varnothing,
\]

so the surface-current integral vanishes.

Also, because `div W=0`, the total vorticity flux through every closed surface is identically zero.

Therefore the useful lineage objects are necessarily open material patches/tubes or signed subregions, not closed surfaces carrying a net vorticity flux.

For an open material lineage patch, flux change is exactly a boundary-throughput statement.

---

## 8. Marker migration is now typed

M5-518 separated

\[
\text{marker degeneration}
\ne
\text{lineage replacement}.
\]

M5-520 sharpens the first side.

Suppose a persistent material surface continues to carry fixed nonzero total flux while one selected marker loses flux density and another region gains it.

The local continuity equation shows that this redistribution cannot occur invisibly.

It must be mediated by

\[
\boxed{J_{\Sigma}=(\nabla\times W)\times n.}
\]

Thus the marker-migration branch is more precisely

\[
\boxed{
H_{marker\ migration}
\Longrightarrow
H_{surface\ current}
}
\]

unless the apparent migration is only a relabeling with no actual material redistribution.

The latter must be audited in material coordinates.

---

## 9. Surface current is controlled by first derivatives

Pointwise,

\[
|J_{\Sigma}|
\le
|\nabla\times W|.
\]

Hence

\[
\|J_{\Sigma}\|_{L^2(\Sigma)}
\]

is a trace-level first-derivative observable.

On the M5-508 globally smooth compact branch, all fixed Sobolev orders are globally bounded, so such surface traces are well-defined on controlled material patches.

However an integrated lower bound on surface-current throughput is not automatically the same as a global palinstrophy lower bound without a uniform material-surface geometry/trace estimate.

That geometry must be retained explicitly.

---

## 10. No strict sign from the current law

The current `J_Sigma` is vector-valued and sign-indefinite.

A bounded recurrent lineage can exhibit

\[
\langle J_{\Sigma}\rangle_{signed}=0
\]

while

\[
\langle |J_{\Sigma}|\rangle>0.
\]

Similarly, a material patch can repeatedly export and re-import signed vorticity flux across its boundary.

Therefore the continuity law is exact but is not itself a strict Lyapunov/cocycle identity.

This is the same recurrence obstruction encountered for

1. scalar material flux in M5-489;
2. relative angle in M5-491;
3. phase-space arclength in M5-512.

---

## 11. Relation to anchored dual-pair branch

M5-516--518 reduced the most rigid pair branch to fixed noncollinear directions with exact transverse strain--diffusion cancellation,

\[
\tau_i+\mathcal D_i=0.
\]

M5-520 adds a different diffusion channel:

\[
J_{\Sigma,i}
=(\nabla\times W)\times n_i.
\]

The projected directional diffusion `mathcal D_i` and surface-current `J_Sigma,i` are not identical projections.

Thus exact cancellation of the direction equation does not freeze the flux-density distribution on the material surface.

An anchored direction can coexist with active viscous surface redistribution.

This channel distinction must be preserved.

---

## 12. Highest-value next target

The next calculation should place the local continuity law in **material-surface coordinates**.

Choose a reference material patch `Sigma_0` and pull the signed flux measure

\[
\mu_\theta:=f(\theta)\,dA_\theta
\]

back to `Sigma_0`.

For a bounded material-label test function `psi`, derive an exact weak moment identity of the form

\[
\frac d{d\theta}
\int_{\Sigma(\theta)}\psi\,f\,dA
=
\int_{\Sigma(\theta)}
\nabla_{\Sigma}\psi\cdot J_{\Sigma}\,dA
\]

when `psi` is transported materially and boundary terms are controlled.

Such an identity would quantify marker migration: moving a fixed signed flux amount across a fixed material-label distance would require a fixed amount of `L1` surface-current action.

The audit question is then whether recurrent marker migration becomes

\[
\text{positive surface-current action}
\]

only, or whether the finite lineage geometry forces a one-sided moment drift.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
