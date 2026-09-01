# DSD M5-489 — Exact similarity material-flux law leaves a zero-mean recurrent diffusion obstruction

Date: 2026-09-01

Status: **P1 RESOLVED BUT NONCLOSING / MATERIAL VORTICITY FLUX IS EXACTLY SCALE INVARIANT UNDER THE BACKWARD NAVIER--STOKES SIMILARITY TRANSFORMATION / A PHYSICAL MATERIAL SURFACE BECOMES A SURFACE TRANSPORTED BY `B=U+y/2` IN SIMILARITY VARIABLES, AND ALL SIMILARITY DAMPING/AREA-DILATION TERMS CANCEL IN THE FLUX BALANCE / THE EXACT LAW IS `d Phi/d theta = int_{Sigma(theta)} Delta W · n dA` / THUS A PERSISTENT FLUX LINEAGE HAS ZERO CESARO MEAN SIGNED DIFFUSIVE INCREMENT ON A RECURRENT COMPACT HULL, BUT THE ABSOLUTE DIFFUSIVE VARIATION MAY REMAIN POSITIVE / FLUX ITSELF IS THEREFORE NOT THE MISSING STRICT LYAPUNOV COCYCLE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let `(mathcal U,mathcal Omega)` be one M5-483 ancient hull member on `s<0`, with viscosity normalized to one.

Set

\[
a=-s=e^{-\theta},
\qquad
y=\frac{x}{\sqrt a},
\]

and

\[
U(y,\theta)
=\sqrt a\,\mathcal U(\sqrt a y,-a),
\]

\[
W(y,\theta)
=a\,\mathcal\Omega(\sqrt a y,-a).
\]

M5-486 derived the corresponding similarity Navier--Stokes and vorticity equations.

The present calculation tracks a material vorticity-flux surface exactly through the same transformation.

---

## 2. Physical material surface

Let `S(s)` be an oriented surface transported by the ancient physical velocity:

\[
\frac{dX}{ds}
=\mathcal U(X,s).
\]

Its vorticity flux is

\[
\boxed{
\Phi(s)
:=
\int_{S(s)}
\mathcal\Omega(x,s)\cdot n_x\,dA_x.
}
\]

The exact material-surface identity used throughout M5-393--397 is

\[
\boxed{
\frac{d\Phi}{ds}
=
\int_{S(s)}
\Delta_x\mathcal\Omega\cdot n_x\,dA_x.
}
\]

The vortex-stretching term cancels exactly against the material area-vector evolution.

---

## 3. Similarity material trajectory

Write

\[
X(s)=\sqrt a\,Y(\theta).
\]

Since

\[
\frac{ds}{d\theta}=a,
\]

we have

\[
\frac{dX}{d\theta}
=a\mathcal U(X,s)
=\sqrt a\,U(Y,\theta).
\]

Differentiating `Y=X/sqrt(a)` gives

\[
\boxed{
\frac{dY}{d\theta}
=U(Y,\theta)+\frac12Y.
}
\]

Thus similarity material surfaces are transported by

\[
\boxed{
B(y,\theta)
:=U(y,\theta)+\frac12y.
}
\]

Note that

\[
\nabla\cdot B=\frac32.
\]

The similarity material flow is therefore not incompressible; its expansion exactly records the changing similarity length scale.

---

## 4. Flux itself is exactly scale invariant

Under

\[
x=\sqrt a\,y,
\]

a surface area transforms as

\[
dA_x=a\,dA_y.
\]

Also

\[
\mathcal\Omega(x,s)=a^{-1}W(y,\theta).
\]

Therefore

\[
\mathcal\Omega\cdot n_x\,dA_x
=
W\cdot n_y\,dA_y.
\]

Hence if `Sigma(theta)` is the similarity image of `S(s)`,

\[
\boxed{
\Phi(s)
=
\Phi_{sim}(\theta)
:=
\int_{\Sigma(\theta)}W\cdot n\,dA.
}
\]

There is no multiplicative renormalization factor.

This is the precise meaning of vorticity flux being Navier--Stokes scale critical.

---

## 5. Transform the diffusive flux

Since

\[
\mathcal\Omega=a^{-1}W,
\qquad
\nabla_x=a^{-1/2}\nabla_y,
\]

we have

\[
\boxed{
\Delta_x\mathcal\Omega
=a^{-2}\Delta_yW.
}
\]

Together with

\[
dA_x=a\,dA_y,
\]

this gives

\[
\int_{S(s)}
\Delta_x\mathcal\Omega\cdot n\,dA_x
=
a^{-1}
\int_{\Sigma(\theta)}
\Delta W\cdot n\,dA.
\]

Finally

\[
\frac{ds}{d\theta}=a.
\]

Therefore

\[
\begin{aligned}
\frac{d\Phi_{sim}}{d\theta}
&=
\frac{d\Phi}{ds}
\frac{ds}{d\theta}\\
&=
a\cdot a^{-1}
\int_{\Sigma(\theta)}
\Delta W\cdot n\,dA.
\end{aligned}
\]

Hence the exact similarity material-flux identity is

\[
\boxed{
\frac{d}{d\theta}
\int_{\Sigma(\theta)}W\cdot n\,dA
=
\int_{\Sigma(\theta)}
\Delta W\cdot n\,dA.
}
\]

---

## 6. Why no similarity damping remains

The similarity vorticity equation contains explicit linear/dilation terms

\[
W+rac12(y\cdot\nabla)W.
\]

One might therefore expect a term proportional to `Phi` in the flux law.

That expectation is false because the similarity material surface itself expands under

\[
B=U+\frac12y.
\]

The area-vector expansion contributes exactly the compensating factor.

Equivalently, the direct physical-to-similarity transformation in Sections 4--5 already proves the cancellation without any formal transport calculation.

Thus:

\[
\boxed{
\text{similarity damping affects enstrophy, but not scale-critical material vorticity flux.}
}
\]

---

## 7. Persistent-lineage flux increment

For a persistent M5-488 material-flux descendant, sample one full generation/suspension return interval

\[
[\theta_j,\theta_{j+1}].
\]

Define

\[
\Phi_j:=\Phi(\theta_j)
\]

and

\[
\boxed{
D_j
:=
\int_{\theta_j}^{\theta_{j+1}}
\int_{\Sigma(\theta)}
\Delta W\cdot n\,dA\,d\theta.
}
\]

Then the exact flux law gives

\[
\boxed{
\Phi_{j+1}-\Phi_j=D_j.
}
\]

Thus the signed diffusive flux is an exact coboundary on a persistent lineage.

---

## 8. Recurrent compact hull forces zero signed mean

On the retained compact fixed-flux lineage,

\[
|\Phi_j|\le\Phi_*.
\]

Summing,

\[
\sum_{j=0}^{N-1}D_j
=
\Phi_N-\Phi_0.
\]

Therefore

\[
\boxed{
\frac1N
\sum_{j=0}^{N-1}D_j
\to0.
}
\]

In invariant-measure notation,

\[
\boxed{
\langle D\rangle=0.
}
\]

Thus any persistent recurrent material-flux lineage must have zero mean **signed** diffusive flux change.

---

## 9. Absolute diffusive variation can remain positive

The previous result does not imply

\[
\langle|D|\rangle=0.
\]

For example, a bounded scalar observable may undergo indefinitely many alternating increments while remaining recurrent.

Hence the compact survivor may satisfy simultaneously

\[
\boxed{
\langle D\rangle=0,
\qquad
\langle|D|\rangle>0.
}
\]

This represents recurrent viscous exchange with exact long-run signed cancellation.

It is compatible with bounded flux and is not ruled out by the finite-memory theorem.

---

## 10. Flux diffusion and directional diffusion remain distinct

M5-487 defined

\[
\mathcal D_\xi
=
\rho^{-1}(I-\xi\otimes\xi)\Delta W.
\]

The scalar surface-flux derivative instead involves

\[
\Delta W\cdot n.
\]

These are different projections of the same vector Laplacian.

A large tangential/projective diffusion event can occur with small scalar flux change through one selected material surface, and scalar flux can change through components that do not produce large projective direction motion.

Therefore

\[
\boxed{
D_j
\not\equiv
\text{M5-487 weighted-tension charge}.
}
\]

They must remain separate audit channels.

---

## 11. P1 verdict

M5-488 asked whether the persistent flux could become a strict similarity cocycle.

The answer is:

\[
\boxed{
\text{No, not from flux alone.}
}
\]

The exact equation is a coboundary with a sign-indefinite diffusive source:

\[
\Phi\circ\sigma-\Phi=D.
\]

Invariant averaging yields

\[
\langle D\rangle=0
\]

rather than a contradiction.

Thus P1 is resolved as a **nonclosing exact identity**.

---

## 12. What the survivor must now do

A persistent compact lineage carrying nonzero fixed flux has only two quiet possibilities.

### A. Asymptotically quiet scalar flux

\[
\langle|D|\rangle=0.
\]

Then scalar material flux is effectively frozen on the recurrent component, and all recurrent ratchet action must be paid predominantly through tilt/projected directional tension rather than net flux exchange.

### B. Oscillatory viscous flux exchange

\[
\langle|D|\rangle>0,
\qquad
\langle D\rangle=0.
\]

Then viscosity repeatedly changes the selected material flux but must regenerate the lost/gained signed amount with exact zero mean over recurrence.

Both cases still coexist with the M5-486 requirement

\[
\langle Q\rangle>0.
\]

---

## 13. Updated persistent endpoint

The persistent-lineage endpoint is now split as

\[
\boxed{
E_{persistent}^{lineage}
\Longrightarrow
E_{flux\ frozen}^{ratchet}
\lor
E_{flux\ osc}^{ratchet}.
}
\]

Both are finite-lineage recurrent similarity states.

The oscillatory branch has

\[
\langle D\rangle=0,
\qquad
\langle|D|\rangle>0,
\]

while the frozen branch must carry the recurrent projective action with negligible scalar flux exchange.

---

## 14. Highest-value next target

Because flux itself is not monotone, the next step should exploit the **finite number of persistent lineages**.

M5-455 reforms a dual-source/companion geometry in every quiet bounded block. On a finite-lineage persistent hull, repeated dual-source formation cannot use infinitely many new labels.

Therefore a finite set of persistent flux descendants must be reused recurrently.

The next calculation should extract a recurrent **persistent dual-pair subsystem** and determine whether its relative orientation/flux matrix has a bounded invariant capable of detecting projective cycling or oscillatory diffusive exchange.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
