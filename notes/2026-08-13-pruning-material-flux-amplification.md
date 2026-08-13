# Pure material pruning forces flux amplification or large surface deformation

Date: 2026-08-13

Status: **DERIVED MATERIAL-SUBDISK FLUX AMPLIFICATION LEMMA / OPEN HIGH-OVERLAP PATCH EXTRACTION**.

The nested-pruning branch allows a later dangerous core to use only a smaller subset of earlier dangerous material.  For an oriented flux tube, however, a later natural cross-section cannot be obtained from a much lower-vorticity earlier material subdisk without either large geometric deformation or viscous creation of signed vorticity flux.

---

## 1. Two dangerous times

Let

\[
t_0<t_1
\]

and define

\[
W_0=\|\omega(t_0)\|_\infty,
\qquad
W_1=\|\omega(t_1)\|_\infty=qW_0,
\qquad q>1.
\]

At `t_1`, suppose an oriented dangerous cross-section `S_1` satisfies

\[
|S_1|
\le
\frac{C_A}{W_1}
\]

and carries signed vorticity flux

\[
\boxed{
\Phi_1
=\int_{S_1}\omega(t_1)\cdot n_1dA
\ge\Gamma_0>0.
}
\]

For a natural-radius one-polarity core, both `C_A` and `Gamma_0` are dimensionless order-one quantities.

---

## 2. Pure material-subdisk hypothesis

Assume `S_1` is the material image of one surface `S_0^*` at `t_0`:

\[
S_1=X(S_0^*,t_1;t_0).
\]

This is the clean pure-pruning model: the later smaller core section uses only old material.

Let

\[
K_A
\ge1
\]

bound backward area distortion:

\[
\boxed{
|S_0^*|
\le K_A|S_1|.
}
\]

For an incompressible flow map this area factor is controlled by the cofactor `F^{-T}` / inverse material metric and is therefore part of the existing Lagrangian deformation channel.

---

## 3. Earlier flux cannot already be as large

At `t_0`, by definition of `W_0`,

\[
|\omega(x,t_0)|\le W_0
\]

everywhere.

Hence the signed flux through the pulled-back material surface obeys

\[
|\Phi_0^*|
\le
W_0|S_0^*|
\le
K_AW_0|S_1|.
\]

Using the later natural-area bound,

\[
\boxed{
|\Phi_0^*|
\le
\frac{K_AC_A}{q}.
}
\]

Therefore if the vorticity amplification factor is chosen so that

\[
\boxed{
q
\ge
\frac{2K_AC_A}{\Gamma_0},
}
\]

then

\[
|\Phi_0^*|
\le
\frac{\Gamma_0}{2}.
\]

Since the later flux satisfies `Phi_1>=Gamma_0`, the same material surface must gain at least

\[
\boxed{
|\Phi_1-\Phi_0^*|
\ge
\frac{\Gamma_0}{2}.
}
\]

Thus sufficiently strong amplitude growth cannot be produced by pure geometric pruning with bounded area distortion while keeping material flux unchanged.

---

## 4. Material flux change is purely viscous

For the material surface

\[
S(t)=X(S_0^*,t;t_0),
\]

the exact identity is

\[
\frac{d\Phi}{dt}
=-\nu
\oint_{\partial S(t)}
(\nabla\times\omega)\cdot d\ell.
\]

Hence the order-one flux increase gives

\[
\boxed{
\nu
\left|
\int_{t_0}^{t_1}
\oint_{\partial S(t)}
(\nabla\times\omega)\cdot d\ell dt
\right|
\ge
\frac{\Gamma_0}{2}.
}
\]

By Cauchy--Schwarz,

\[
\boxed{
\int_{t_0}^{t_1}
\oint_{\partial S(t)}
|\nabla\times\omega|^2d\ell dt
\ge
\frac{\Gamma_0^2}
{4\nu^2
\int_{t_0}^{t_1}\ell_{\partial S}(t)dt
}.
}
\]

Thus pure pruning returns directly to the material-flux viscous-erosion/creation channel.

---

## 5. Large-deformation alternative

The only way to avoid the flux gap at fixed amplitude ratio `q` is for the earlier pullback area to be large enough that

\[
K_A
\gtrsim q.
\]

But material-surface area distortion is controlled by `F^{-T}` and therefore by accumulated strain.

Consequently the pure-pruning branch is reduced to

\[
\boxed{
\text{large material-surface deformation}
\quad\text{or}\quad
\text{order-one viscous material-flux creation}.
}
\]

Both are already active channels.

---

## 6. Natural nested family

If the later dangerous core contains a robust nested band of material subdisks

\[
r_1\le\rho\le2r_1
\]

all satisfying the same later flux lower bound and bounded backward area distortion, then the previous material-tube coarea lemma applies to the order-one flux creation on the whole family.

Under bounded Lagrangian distortion it yields a bulk second-derivative/palinstrophy cost rather than a codimension-two boundary cost.

If the distortion becomes large, the branch returns to strain/Lagrangian geometry.

---

## 7. Why this matters for pruning

The pruning note showed that later natural cores can have much smaller material volume than earlier cores.  The present lemma adds a flux constraint:

- **volume pruning alone is free at the scaling level**;
- **oriented flux amplification on the pruned material surface is not free**.

A later core with much higher `W` and the same natural signed flux cannot simply be an old small material disk unless viscosity has changed its material vorticity flux or the disk has undergone proportionally large area distortion.

---

## 8. Remaining geometry gap

High **three-dimensional volume overlap** between consecutive cores does not automatically give a full material subdisk with controlled boundary.

The old-material part of a later cross-section may be fragmented.

Therefore the next bridge is:

\[
\boxed{
\text{high material overlap}
\Rightarrow
\text{either a large coherent old-material surface patch}
\text{ or large old/new interface complexity}.
}
\]

The first branch feeds the present flux-amplification lemma.

The second branch should be charged to material-interface perimeter growth / strain deformation.

Status: **OPEN OVERLAP-TO-SURFACE-PATCH / INTERFACE-COMPLEXITY CLOSURE**.
